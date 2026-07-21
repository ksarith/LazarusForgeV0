"""
Lazarus Forge - Metadata Parser v0.2
Evidence-first, provenance-rich, conflict-aware parser.

Design philosophy (per Automation subsystem doctrine):
    Parser observes.  It does not decide.
    Every conclusion is explainable; every conflict is preserved;
    every automated choice is traceable.

This module has two responsibilities, kept deliberately separate:

    1. MetadataParser   — extracts document metadata as an evidence
                           ledger (never "first wins", never silently
                           discards a conflicting reading).

    2. SectionExtractor — pulls an isolated slice of a document's body
                           for scrutiny, stripped of the surrounding
                           context (title, status, version, other
                           sections) that could anchor or bias a
                           reviewer's judgment before they've looked
                           at the material itself. This exists for
                           AP-017-style blind review: an auditor
                           should be able to evaluate a claim without
                           first being told what grade/status the
                           document already carries.

Zero external dependencies (stdlib only). YAML support is a
deliberately restricted subset — flat key: value pairs and simple
one-level "- item" lists — documented as such rather than silently
failing on nested/complex YAML.
"""

import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Evidence primitives
# ---------------------------------------------------------------------------

@dataclass
class FieldValue:
    """A single observed reading of a field, with full provenance."""
    value: Any
    source: str      # 'yaml', 'markdown_table', 'legacy_inline'
    line: int
    raw: str

    def __repr__(self) -> str:
        return f"FieldValue({self.value!r} @ {self.source}:{self.line})"


@dataclass
class NormalizedField:
    """
    A parser-proposed value derived from the evidence ledger for one
    canonical field, WITHOUT silently hiding disagreement.

    preferred_value / preferred_source: the parser's best guess,
        chosen by documented precedence (yaml > markdown_table >
        legacy_inline), never invented.
    conflict: True if two or more sources disagree on this field.
    all_readings: every FieldValue observed for this field, in
        discovery order. Nothing is thrown away.
    """
    preferred_value: Optional[Any] = None
    preferred_source: Optional[str] = None
    conflict: bool = False
    all_readings: List[FieldValue] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "preferred_value": self.preferred_value,
            "preferred_source": self.preferred_source,
            "conflict": self.conflict,
            "all_readings": [r.__dict__ for r in self.all_readings],
        }


@dataclass
class MetadataResult:
    """Normalized evidence container for one document's metadata."""

    file_path: str
    detected_schemas: List[str] = field(default_factory=list)
    metadata_blocks: int = 0

    # Full evidence ledger: canonical_field -> every reading found
    evidence: Dict[str, List[FieldValue]] = field(default_factory=dict)

    # Parser-proposed (but explainable, never silently forced) values
    document_id: NormalizedField = field(default_factory=NormalizedField)
    title: NormalizedField = field(default_factory=NormalizedField)
    repo_version: NormalizedField = field(default_factory=NormalizedField)
    document_version: NormalizedField = field(default_factory=NormalizedField)
    status: NormalizedField = field(default_factory=NormalizedField)
    last_updated: NormalizedField = field(default_factory=NormalizedField)
    dependencies: NormalizedField = field(default_factory=NormalizedField)

    # Fields the schema wasn't expecting — preserved, not discarded
    extra_fields: Dict[str, List[FieldValue]] = field(default_factory=dict)

    # Two independent axes — deliberately not collapsed into one score
    parse_confidence: float = 0.0        # "could I read this document?"
    metadata_completeness: float = 0.0   # "does it have what's expected?"

    # Diagnostics
    fields_found: int = 0
    fields_missing: List[str] = field(default_factory=list)
    conflicting_fields: List[str] = field(default_factory=list)

    # Human-readable, attachable-to-audit-report trace
    trace: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        canonical = ["document_id", "title", "repo_version", "document_version",
                     "status", "last_updated", "dependencies"]
        return {
            "file_path": self.file_path,
            "detected_schemas": self.detected_schemas,
            "metadata_blocks": self.metadata_blocks,
            "parse_confidence": round(self.parse_confidence, 2),
            "metadata_completeness": round(self.metadata_completeness, 2),
            "fields_found": self.fields_found,
            "fields_missing": self.fields_missing,
            "conflicting_fields": self.conflicting_fields,
            "warnings": self.warnings,
            "errors": self.errors,
            "trace": self.trace,
            "normalized": {k: getattr(self, k).to_dict() for k in canonical},
            "evidence": {k: [v.__dict__ for v in vs] for k, vs in self.evidence.items()},
            "extra_fields": {k: [v.__dict__ for v in vs] for k, vs in self.extra_fields.items()},
        }


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

class MetadataParser:
    """Multi-schema evidence collector for Lazarus Forge markdown documents."""

    LEGACY_PATTERNS = {
        "repo_version": [r"Repo(?:sitory)?\s*Version:\s*(v?[\d\.]+)"],
        "document_version": [r"(?:Doc(?:ument)?\s*Version|Version):\s*(v?[\d\.]+)"],
        "document_id": [r"Document\s*ID:\s*([\w\-]+)", r"ID:\s*([\w\-]+)"],
        "status": [r"Status:\s*(\w+)"],
        "last_updated": [r"(?:Last\s*Updated|Date):\s*([\d\-\/]+)"],
    }

    # Fields expected on a fully-described canonical document.
    # Drives metadata_completeness independently of parse_confidence.
    EXPECTED_FIELDS = [
        "document_id", "title", "repo_version", "document_version",
        "status", "last_updated", "dependencies",
    ]

    # Precedence used only to propose a preferred_value when sources
    # disagree — the disagreement itself is always preserved regardless.
    SOURCE_PRECEDENCE = {"yaml": 3, "markdown_table": 2, "legacy_inline": 1}

    KEY_MAPPINGS = {
        "document_id": ["document_id", "doc_id", "id"],
        "title": ["title", "document_title", "name"],
        "repo_version": ["repo_version", "repository_version"],
        "document_version": ["document_version", "doc_version", "version"],
        "status": ["status", "doc_status"],
        "last_updated": ["last_updated", "date", "updated"],
        "dependencies": ["dependencies", "deps", "requires"],
    }

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.result = MetadataResult(file_path=file_path)

    # -- orchestration -------------------------------------------------

    def parse(self) -> MetadataResult:
        r = self.result

        if not os.path.exists(self.file_path):
            r.errors.append(f"File not found: {self.file_path}")
            r.trace.append(f"ABORT: file not found ({self.file_path})")
            return r

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            r.errors.append(f"Read error: {str(e)}")
            r.trace.append(f"ABORT: read error ({e})")
            return r

        if not lines:
            r.warnings.append("File is empty.")
            r.trace.append("File is empty; nothing to parse.")
            return r

        # raw_evidence: canonical-ish key -> list of FieldValue (all kept)
        raw_evidence: Dict[str, List[FieldValue]] = {}

        yaml_found, yaml_fields, yaml_span = self._parse_yaml_frontmatter(lines)
        if yaml_found:
            r.detected_schemas.append("yaml")
            r.metadata_blocks += 1
            r.trace.append(
                f"Detected YAML frontmatter (lines {yaml_span[0]}-{yaml_span[1]}); "
                f"recovered {len(yaml_fields)} keys."
            )
            for k, v in yaml_fields.items():
                raw_evidence.setdefault(k, []).append(v)

        table_found, table_fields = self._parse_markdown_tables(lines)
        if table_found:
            r.detected_schemas.append("markdown_table")
            r.metadata_blocks += 1
            r.trace.append(f"Detected markdown metadata table; recovered {len(table_fields)} keys.")
            for k, v in table_fields.items():
                raw_evidence.setdefault(k, []).append(v)

        legacy_found, legacy_fields = self._parse_legacy_inline(lines)
        if legacy_found:
            r.detected_schemas.append("legacy_inline")
            r.metadata_blocks += 1
            r.trace.append(f"Detected legacy inline headers; recovered {len(legacy_fields)} keys.")
            for k, v in legacy_fields.items():
                raw_evidence.setdefault(k, []).append(v)

        if not r.detected_schemas:
            r.trace.append("No recognized metadata schema found.")

        self._normalize(raw_evidence)
        self._compute_confidence_and_diagnostics()
        r.trace.append("Parse complete.")

        return r

    # -- YAML (restricted subset: flat keys + simple one-level lists) --

    def _parse_yaml_frontmatter(
        self, lines: List[str]
    ) -> Tuple[bool, Dict[str, FieldValue], Tuple[int, int]]:
        fields: Dict[str, FieldValue] = {}
        if not lines or lines[0].strip() != "---":
            return False, fields, (0, 0)

        end_idx = -1
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                end_idx = idx
                break

        if end_idx == -1:
            self.result.warnings.append(
                "Malformed YAML frontmatter: opening '---' without closing '---'."
            )
            self.result.trace.append("YAML frontmatter opened but never closed — skipped.")
            return False, fields, (0, 0)

        idx = 1
        while idx < end_idx:
            line_str = lines[idx].strip()
            if not line_str or line_str.startswith("#"):
                idx += 1
                continue

            if ":" in line_str:
                key, val = line_str.split(":", 1)
                clean_key = key.strip().lower().replace(" ", "_")
                clean_val = val.strip()

                if clean_val == "":
                    # Possible start of a one-level YAML list:
                    #   dependencies:
                    #     - Admin/A.md
                    #     - Admin/B.md
                    list_items = []
                    j = idx + 1
                    while j < end_idx:
                        item_line = lines[j].strip()
                        if item_line.startswith("- "):
                            list_items.append(item_line[2:].strip().strip("\"'"))
                            j += 1
                        elif item_line == "":
                            j += 1
                        else:
                            break
                    if list_items:
                        fields[clean_key] = FieldValue(
                            value=list_items,
                            source="yaml",
                            line=idx + 1,
                            raw=lines[idx].strip(),
                        )
                        idx = j
                        continue
                    else:
                        # empty scalar
                        fields[clean_key] = FieldValue(
                            value="", source="yaml", line=idx + 1, raw=lines[idx].strip()
                        )
                else:
                    fields[clean_key] = FieldValue(
                        value=clean_val.strip("\"'"),
                        source="yaml",
                        line=idx + 1,
                        raw=lines[idx].strip(),
                    )
            idx += 1

        return True, fields, (1, end_idx + 1)

    # -- Markdown tables -------------------------------------------------

    def _parse_markdown_tables(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        fields: Dict[str, FieldValue] = {}
        for idx, line in enumerate(lines[:30]):
            line_str = line.strip()
            if line_str.startswith("|") and line_str.endswith("|"):
                parts = [p.strip() for p in line_str.split("|")[1:-1]]
                if len(parts) >= 2:
                    k, v = parts[0].strip(), parts[1].strip()
                    if set(k).issubset({"-"}) or set(v).issubset({"-"}):
                        continue
                    clean_key = k.lower().replace(" ", "_")
                    clean_val = v.strip("\"'")
                    fields[clean_key] = FieldValue(
                        value=clean_val, source="markdown_table", line=idx + 1, raw=line_str
                    )
        return len(fields) > 0, fields

    # -- Legacy inline -----------------------------------------------------

    def _parse_legacy_inline(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        fields: Dict[str, FieldValue] = {}
        for idx, line in enumerate(lines[:30]):
            line_str = line.strip()
            for key, patterns in self.LEGACY_PATTERNS.items():
                if key in fields:
                    continue
                for pat in patterns:
                    match = re.search(pat, line_str, re.IGNORECASE)
                    if match:
                        fields[key] = FieldValue(
                            value=match.group(1), source="legacy_inline", line=idx + 1, raw=line_str
                        )
        return len(fields) > 0, fields

    # -- Normalization: evidence ledger -> explainable proposals ----------

    def _normalize(self, raw_evidence: Dict[str, List[FieldValue]]) -> None:
        r = self.result

        for canonical_field, target_keys in self.KEY_MAPPINGS.items():
            readings: List[FieldValue] = []
            for tk in target_keys:
                if tk in raw_evidence:
                    readings.extend(raw_evidence[tk])

            if not readings:
                continue

            # last_updated: try to normalize each reading's date string,
            # but keep the raw reading regardless of parse success.
            if canonical_field == "last_updated":
                for fv in readings:
                    parsed = self._try_parse_date(str(fv.value))
                    if parsed:
                        fv.value = parsed
                    else:
                        r.warnings.append(
                            f"Line {fv.line}: could not parse ISO date from '{fv.value}'"
                        )

            r.evidence[canonical_field] = readings

            distinct_values = {str(fv.value) for fv in readings}
            nf = NormalizedField(all_readings=readings)
            if len(distinct_values) > 1:
                nf.conflict = True
                r.conflicting_fields.append(canonical_field)
                sources_seen = ", ".join(f"{fv.source}='{fv.value}' (line {fv.line})" for fv in readings)
                r.trace.append(f"CONFLICT on '{canonical_field}': {sources_seen}")

            # propose (not force) a preferred reading by source precedence
            best = max(readings, key=lambda fv: self.SOURCE_PRECEDENCE.get(fv.source, 0))
            nf.preferred_value = best.value
            nf.preferred_source = best.source

            setattr(r, canonical_field, nf)

        # anything harvested but not part of the canonical schema
        mapped_keys = {k for keys in self.KEY_MAPPINGS.values() for k in keys}
        for raw_key, readings in raw_evidence.items():
            if raw_key not in mapped_keys:
                r.extra_fields[raw_key] = readings
                r.trace.append(f"Preserved unrecognized field '{raw_key}' ({len(readings)} reading(s)).")

    # -- Confidence: two independent axes ----------------------------------

    def _compute_confidence_and_diagnostics(self) -> None:
        r = self.result

        # Parse confidence: did we recognize a schema at all, and cleanly?
        if not r.detected_schemas:
            r.parse_confidence = 0.0
        else:
            base = {"yaml": 1.0, "markdown_table": 0.85, "legacy_inline": 0.6}
            score = max(base.get(s, 0.3) for s in r.detected_schemas)
            # malformed frontmatter / unparseable dates dock parse confidence
            penalty = 0.1 * len(r.warnings) + 0.25 * len(r.errors)
            r.parse_confidence = max(0.0, min(1.0, score - penalty))

        # Metadata completeness: independent of *how* it was read
        present = []
        missing = []
        for field_name in self.EXPECTED_FIELDS:
            nf: NormalizedField = getattr(r, field_name)
            if nf.preferred_value not in (None, "", []):
                present.append(field_name)
            else:
                missing.append(field_name)

        r.fields_found = len(present)
        r.fields_missing = missing
        r.metadata_completeness = len(present) / len(self.EXPECTED_FIELDS)

        if r.conflicting_fields:
            r.warnings.append(
                f"{len(r.conflicting_fields)} field(s) had disagreeing readings across schemas: "
                f"{', '.join(r.conflicting_fields)}"
            )

    @staticmethod
    def _try_parse_date(date_str: str) -> Optional[str]:
        formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%B %d, %Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        return None


# ---------------------------------------------------------------------------
# Section extraction for blind / scrutiny review (AP-017)
# ---------------------------------------------------------------------------

@dataclass
class SectionExtract:
    """
    An isolated slice of a document's body, deliberately stripped of
    surrounding context (title, status, version, sibling sections)
    that could anchor a reviewer before they've evaluated the
    material on its own terms.
    """
    file_path: str
    heading: Optional[str]
    start_line: int
    end_line: int
    content: str
    stripped_context: List[str] = field(default_factory=list)  # what was deliberately withheld

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_path": self.file_path,
            "heading": self.heading,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "content": self.content,
            "stripped_context": self.stripped_context,
        }


class SectionExtractor:
    """
    Pulls one section of a markdown document for isolated scrutiny.

    Use case: an auditor (human or agent) should be able to evaluate
    a specific claim, procedure, or clause without first seeing the
    document's declared status (e.g. "Canonical", "RATIFIED"),
    version history, or neighboring sections that could bias the
    read. This is a read-only, non-mutating operation — it never
    rewrites the source file.

    Headings are matched against markdown ATX headers (#, ##, ###...).
    A section runs from its heading to the next heading of the same
    or shallower depth, or end of file.
    """

    HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")

    def __init__(self, file_path: str):
        self.file_path = file_path

    def list_headings(self) -> List[Tuple[int, int, str]]:
        """Returns (line_number, depth, heading_text) for every heading."""
        out = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            for idx, line in enumerate(f.readlines()):
                m = self.HEADING_RE.match(line)
                if m:
                    out.append((idx + 1, len(m.group(1)), m.group(2)))
        return out

    def extract(self, heading_text: str, include_heading: bool = False,
                blind: bool = True) -> Optional[SectionExtract]:
        """
        Extract the section whose heading contains heading_text
        (case-insensitive substring match).

        blind=True (default): the returned content contains ONLY that
        section's body — no YAML frontmatter, no document title, no
        status/version fields, no other sections. This is the mode
        intended for handing a slice to an auditor for unbiased review.

        blind=False: same section, but notes in stripped_context what
        would normally be withheld, without withholding it — useful
        for a human operator sanity-checking the extraction itself.
        """
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        headings = self.list_headings()
        target_idx = None
        for i, (line_no, depth, text) in enumerate(headings):
            if heading_text.lower() in text.lower():
                target_idx = i
                break

        if target_idx is None:
            return None

        start_line, depth, matched_heading = headings[target_idx]

        end_line = len(lines)
        for line_no, d, _ in headings[target_idx + 1:]:
            if d <= depth:
                end_line = line_no - 1
                break

        body_start = start_line if include_heading else start_line + 1
        section_lines = lines[body_start - 1:end_line]
        content = "".join(section_lines).strip("\n")

        stripped = []
        if lines and lines[0].strip() == "---":
            stripped.append("YAML frontmatter (title/status/version/dependencies)")
        if not include_heading:
            stripped.append(f"Section heading text: '{matched_heading}'")
        other_headings = [h for i, h in enumerate(headings) if i != target_idx]
        if other_headings:
            stripped.append(f"{len(other_headings)} sibling/other section(s) in the same file")

        extract = SectionExtract(
            file_path=self.file_path,
            heading=matched_heading,
            start_line=body_start,
            end_line=end_line,
            content=content,
            stripped_context=stripped if blind else [],
        )
        return extract


# ---------------------------------------------------------------------------
# CLI smoke test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import sys
    import json

    if len(sys.argv) < 2:
        print("Usage: python parser.py <file.md> [--section 'Heading text']")
        sys.exit(1)

    target = sys.argv[1]

    if "--section" in sys.argv:
        idx = sys.argv.index("--section")
        heading = sys.argv[idx + 1]
        extractor = SectionExtractor(target)
        result = extractor.extract(heading, blind=True)
        if result is None:
            print(f"No heading matching '{heading}' found.")
        else:
            print(json.dumps(result.to_dict(), indent=2))
    else:
        parser = MetadataParser(target)
        result = parser.parse()
        print(json.dumps(result.to_dict(), indent=2))

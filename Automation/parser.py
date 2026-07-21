"""
Lazarus Forge - Metadata Parser (parser.py)
Layer 1: Schema Detection
Layer 2: Schema-Specific Extraction (YAML, Markdown Tables, Legacy Inline)
Layer 3: Normalization & Provenance Capture
Layer 4: Evidence Container Assembly
"""

import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class FieldValue:
    """Encapsulates a parsed metadata value along with its line-level evidence."""
    value: Any
    source: str  # 'yaml', 'markdown_table', 'legacy'
    line: int
    raw: str


@dataclass
class MetadataResult:
    """Normalised evidence container for document metadata."""
    file_path: str
    detected_schemas: List[str] = field(default_factory=list)
    confidence: float = 0.0

    # Normalized fields with provenance
    document_id: Optional[FieldValue] = None
    title: Optional[FieldValue] = None
    repo_version: Optional[FieldValue] = None
    document_version: Optional[FieldValue] = None
    status: Optional[FieldValue] = None
    last_updated: Optional[FieldValue] = None
    dependencies: Optional[FieldValue] = None

    # Diagnostic logs (No execution decisions made here)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the evidence container for json output / logging."""
        out = {
            "file_path": self.file_path,
            "detected_schemas": self.detected_schemas,
            "confidence": self.confidence,
            "warnings": self.warnings,
            "errors": self.errors,
            "fields": {}
        }
        for key in ["document_id", "title", "repo_version", "document_version", "status", "last_updated", "dependencies"]:
            attr = getattr(self, key)
            if attr:
                out["fields"][key] = {
                    "value": attr.value,
                    "source": attr.source,
                    "line": attr.line,
                    "raw": attr.raw
                }
        return out


class MetadataParser:
    """Multi-schema evidence collector for Lazarus Forge markdown documents."""

    # Standard field mapping regexes
    LEGACY_PATTERNS = {
        "repo_version": [r"Repo(?:sitory)?\s*Version:\s*(v?[\d\.]+)"],
        "document_version": [r"(?:Doc(?:ument)?\s*Version|Version):\s*(v?[\d\.]+)"],
        "document_id": [r"Document\s*ID:\s*([\w\-]+)", r"ID:\s*([\w\-]+)"],
        "status": [r"Status:\s*(\w+)"],
        "last_updated": [r"(?:Last\s*Updated|Date):\s*([\d\-\/]+)"]
    }

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.result = MetadataResult(file_path=file_path)

    def parse(self) -> MetadataResult:
        """Executes evidence collection across all 4 layers."""
        if not os.path.exists(self.file_path):
            self.result.errors.append(f"File not found: {self.file_path}")
            return self.result

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            self.result.errors.append(f"Read error: {str(e)}")
            return self.result

        if not lines:
            self.result.warnings.append("File is empty.")
            return self.result

        # Layer 1 & 2: Detect schemas and harvest raw field evidence
        raw_evidence: Dict[str, FieldValue] = {}

        # 1. Check YAML Frontmatter
        yaml_found, yaml_fields = self._parse_yaml_frontmatter(lines)
        if yaml_found:
            self.result.detected_schemas.append("yaml")
            raw_evidence.update(yaml_fields)

        # 2. Check Markdown Tables
        table_found, table_fields = self._parse_markdown_tables(lines)
        if table_found:
            self.result.detected_schemas.append("markdown_table")
            # Fill missing or log duplicate findings
            for k, v in table_fields.items():
                if k not in raw_evidence:
                    raw_evidence[k] = v

        # 3. Check Legacy Inline Headers
        legacy_found, legacy_fields = self._parse_legacy_inline(lines)
        if legacy_found:
            self.result.detected_schemas.append("legacy_inline")
            for k, v in legacy_fields.items():
                if k not in raw_evidence:
                    raw_evidence[k] = v

        # Layer 3: Normalize fields & compute confidence
        self._normalize_and_populate(raw_evidence)

        return self.result

    def _parse_yaml_frontmatter(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        """Extracts key-value pairs from YAML frontmatter between triple dashes."""
        fields = {}
        if not lines[0].strip() == "---":
            return False, fields

        end_idx = -1
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                end_idx = idx
                break

        if end_idx == -1:
            self.result.warnings.append("Malformed YAML frontmatter: opening '---' without closing '---'.")
            return False, fields

        for idx in range(1, end_idx):
            line_str = lines[idx].strip()
            if not line_str or line_str.startswith("#"):
                continue
            if ":" in line_str:
                key, val = line_str.split(":", 1)
                clean_key = key.strip().lower().replace(" ", "_")
                clean_val = val.strip().strip("\"'")
                fields[clean_key] = FieldValue(
                    value=clean_val,
                    source="yaml",
                    line=idx + 1,
                    raw=lines[idx].strip()
                )

        return True, fields

    def _parse_markdown_tables(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        """Extracts metadata from key-value Markdown tables (| Field | Value |)."""
        fields = {}
        in_table = False
        
        for idx, line in enumerate(lines[:30]):  # Restrict search to top header region
            line_str = line.strip()
            if line_str.startswith("|") and line_str.endswith("|"):
                in_table = True
                parts = [p.strip() for p in line_str.split("|")[1:-1]]
                if len(parts) >= 2:
                    k, v = parts[0].strip(), parts[1].strip()
                    # Ignore header separators (|---|---|)
                    if set(k).issubset({"-"}) or set(v).issubset({"-"}):
                        continue
                    clean_key = k.lower().replace(" ", "_")
                    clean_val = v.strip("\"'")
                    fields[clean_key] = FieldValue(
                        value=clean_val,
                        source="markdown_table",
                        line=idx + 1,
                        raw=line_str
                    )

        return len(fields) > 0, fields

    def _parse_legacy_inline(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        """Extracts isolated key-value lines matching legacy formats."""
        fields = {}
        for idx, line in enumerate(lines[:30]):
            line_str = line.strip()
            for key, patterns in self.LEGACY_PATTERNS.items():
                if key in fields:
                    continue
                for pat in patterns:
                    match = re.search(pat, line_str, re.IGNORECASE)
                    if match:
                        fields[key] = FieldValue(
                            value=match.group(1),
                            source="legacy_inline",
                            line=idx + 1,
                            raw=line_str
                        )
        return len(fields) > 0, fields

    def _normalize_and_populate(self, raw_evidence: Dict[str, FieldValue]) -> None:
        """Assigns harvested raw evidence to canonical fields with date parsing."""
        key_mappings = {
            "document_id": ["document_id", "doc_id", "id"],
            "title": ["title", "document_title", "name"],
            "repo_version": ["repo_version", "repository_version"],
            "document_version": ["document_version", "doc_version", "version"],
            "status": ["status", "doc_status"],
            "last_updated": ["last_updated", "date", "updated"],
            "dependencies": ["dependencies", "deps", "requires"]
        }

        for canonical_field, target_keys in key_mappings.items():
            for tk in target_keys:
                if tk in raw_evidence:
                    fv = raw_evidence[tk]
                    
                    # Special handling for date formatting
                    if canonical_field == "last_updated":
                        parsed_date = self._try_parse_date(str(fv.value))
                        if parsed_date:
                            fv.value = parsed_date
                        else:
                            self.result.warnings.append(
                                f"Line {fv.line}: Could not parse ISO date from '{fv.value}'"
                            )

                    setattr(self.result, canonical_field, fv)
                    break

        # Calculate preliminary parser confidence score
        schema_weights = {"yaml": 1.0, "markdown_table": 0.8, "legacy_inline": 0.5}
        if self.result.detected_schemas:
            highest_weight = max(schema_weights.get(s, 0.3) for s in self.result.detected_schemas)
            self.result.confidence = highest_weight
        else:
            self.result.confidence = 0.0

    @staticmethod
    def _try_parse_date(date_str: str) -> Optional[str]:
        """Tries common date formats and returns ISO 8601 (YYYY-MM-DD)."""
        formats = ["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y", "%B %d, %Y"]
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt).strftime("%Y-%m-%d")
            except ValueError:
                continue
        return None

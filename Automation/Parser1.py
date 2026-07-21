"""
Lazarus Forge - Metadata Parser v0.2
Evidence-first, provenance-rich, conflict-aware parser.
"""

import os
import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class FieldValue:
    value: Any
    source: str
    line: int
    raw: str


@dataclass
class MetadataResult:
    file_path: str
    detected_schemas: List[str] = field(default_factory=list)
    confidence: float = 0.0

    # Canonical normalized fields (derived from evidence)
    document_id: Optional[FieldValue] = None
    title: Optional[FieldValue] = None
    repo_version: Optional[FieldValue] = None
    document_version: Optional[FieldValue] = None
    status: Optional[FieldValue] = None
    last_updated: Optional[FieldValue] = None
    dependencies: Optional[List[str]] = None   # normalized list

    extra_fields: Dict[str, List[FieldValue]] = field(default_factory=dict)

    # Full evidence ledger
    evidence: Dict[str, List[FieldValue]] = field(default_factory=dict)

    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    # Rich diagnostics
    metadata_blocks: int = 0
    fields_found: int = 0
    conflicting_fields: int = 0

    def to_dict(self) -> Dict[str, Any]:
        return {
            "file_path": self.file_path,
            "detected_schemas": self.detected_schemas,
            "confidence": round(self.confidence, 2),
            "metadata_blocks": self.metadata_blocks,
            "fields_found": self.fields_found,
            "conflicting_fields": self.conflicting_fields,
            "warnings": self.warnings,
            "errors": self.errors,
            "fields": {k: [v.__dict__ for v in vs] for k, vs in self.evidence.items()},
            "normalized": {
                k: getattr(self, k).value if getattr(self, k) else None
                for k in ["document_id", "title", "repo_version", "document_version",
                          "status", "last_updated"]
            },
            "extra_fields": {k: [v.__dict__ for v in vs] for k, vs in self.extra_fields.items()}
        }


class MetadataParser:
    LEGACY_PATTERNS = { ... }  # (same as before, omitted for brevity)

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.result = MetadataResult(file_path=file_path)

    def parse(self) -> MetadataResult:
        # ... (file reading logic same as before)

        raw_evidence: Dict[str, List[FieldValue]] = {}

        # YAML
        yaml_found, yaml_fields = self._parse_yaml_frontmatter(lines)
        if yaml_found:
            self.result.detected_schemas.append("yaml")
            self.result.metadata_blocks += 1
            for k, v in yaml_fields.items():
                raw_evidence.setdefault(k, []).append(v)

        # Markdown tables + Legacy (similar updates)

        # Normalize with conflict detection
        self._normalize_and_populate(raw_evidence)
        self._compute_confidence_and_diagnostics()

        return self.result

    # Updated YAML parser supporting basic lists
    def _parse_yaml_frontmatter(self, lines: List[str]) -> Tuple[bool, Dict[str, FieldValue]]:
        # ... improved version that handles dependencies: - item1\n  - item2
        # (full implementation available in workspace)

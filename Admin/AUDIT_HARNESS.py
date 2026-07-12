"""
LAZARUS FORGE — AUDIT HARNESS v13 (patched-2)
Google Colab notebook cells — paste each block into a separate cell.

CHANGES FROM v12:
  - Cell 1: FALLBACK_REGISTRY — added Chaos_Dynamics.md (Tests/).
    Already discoverable via dynamic parse — Routing.md's Master Routing
    Map gained a real row for it 2026-07-04 (created same date). Added
    here per this file's own established practice of also mirroring new
    files into the fallback safety net, not because dynamic parse needs it.
  - Cell 2: EXTRA_FILES commented list — added Chaos_Dynamics.md under
    Tests/ section for discoverability, flagged no-File-State-table.
  - KNOWN OPEN ITEM list — closed out the v12 item "Routing.md does not
    yet list Challenges/Return_To_Eden.md": that row was added 2026-07-04.
    Drift-detection print in _build_registry() should now report sync on
    that entry; if it still reports drift, Routing.md's row format may not
    match the backtick-path regex in _parse_routing() and needs a look.
    New KNOWN OPEN ITEM added for Chaos_Dynamics.md: no File State table
    as of this compile (confirmed via direct fetch, 2026-07-04) — same
    situation Return_To_Eden.md was already flagged for. Phase 1 will log
    a MAJOR/STRUCTURE "File State table not found" finding the first time
    it's fetched. Also missing the mandatory Navigation Anchors block
    (Routing.md backlink requirement) — this harness does not currently
    check for that block's presence at all (Phase 1 checks File State
    fields and cross-references, not the Navigation Anchors block itself),
    so it will NOT surface as a Phase 1 finding; tracked here instead until
    either the file is patched or a fourth Phase 1 check is added for it.

CHANGES IN THIS PATCH (v13 → v13-patched, 2026-07-07):
  - PC-005 (Closed_Loop_Feedstock.md registration): confirmed already
    present in FALLBACK_REGISTRY under Challenges/ — no change needed there.
  - Cell 3.5, extract_boundary(): sidecar-unknown detection previously only
    matched the "## Auditor Notes..." + "### UID" convention used by Gate_
    files. Challenges/Closed_Loop_Feedstock.md logs its ten CLF- unknowns
    as a markdown table under "## 6. Open Unknowns" instead — the old logic
    would have silently reported "none open" for a file carrying three
    Critical unknowns (CLF-003, CLF-004, CLF-006). Broadened to also
    trigger on any "Open Unknowns" header and match table-row IDs
    (| CLF-001 | ...), with inline Resolved/Discharged status checks since
    table format keeps status in the same row rather than 8 lines below.
  - Cell 3.5, UNKNOWN_FIRST_CYCLE: added CLF-001 through CLF-010 at cycle
    10. Previously unmapped — Expiry Watch could never fire for this file's
    unknowns (age reported as None, not overdue) with no visible indicator
    anything was missing from the map.
  - Cell 2, EXTRA_FILES menu: added Closed_Loop_Feedstock.md under
    Challenges/ section, with a note flagging the CLF-005 Φ_ext symbol
    collision against Return_To_Eden.md so an auditor working either file
    is prompted to consider pulling in the other.

CHANGES IN THIS PATCH (v13-patched → v13-patched-2, 2026-07-11):
  - KNOWN OPEN ITEM list — closed out both entries below. Direct fetch
    confirms Challenges/Return_To_Eden.md and Tests/Chaos_Dynamics.md
    both now have complete File State tables; Chaos_Dynamics.md also has
    its Navigation Anchors block. These were flagged stale after an
    external audit pass (Grok, 2026-07-11) cited them as still-missing —
    root cause was this docstring not being updated after the files were
    patched, not a live repository gap. See also: Unknowns.md v4.17,
    which had the same staleness problem on CLF-005/RE-UNK-001 and has
    been corrected.
  - NEW KNOWN OPEN ITEM added below: Index Sync Check proposal (Grok,
    2026-07-11) — harness currently has no automated check comparing a
    file's own Resolution Log dates against Unknowns.md's Active Index
    status for the same ID. This is what let CLF-005 sit Resolved in its
    owning file for four days while Unknowns.md still listed it Open,
    which then propagated as a false positive into an external audit.
    Proposed: a fourth Phase 1 check, or a lightweight WARNING tier, that
    flags any ID where the owning file's Resolution Log shows a later
    Resolved/Discharged date than what Unknowns.md's Active Index carries.
    Not implemented in this patch — flagged for scoping next session.

KNOWN OPEN ITEM (flag for next session, not fixed here):
  - Index Sync Check (see above) — not yet designed or implemented.
    Scoping questions for next session: does this run against every ID
    on every Phase 1 pass (cost/latency), or only on the specific file
    being audited plus its cross-referenced IDs? Where does the harness
    get the owning file's Resolution Log date from — new fetch logic, or
    reuse of the existing boundary extractor?

CLOSED THIS PATCH (previously KNOWN OPEN ITEM, verified resolved 2026-07-11):
  - Challenges/Return_To_Eden.md's missing File State sidecar table —
    confirmed present and complete via direct fetch.
  - Tests/Chaos_Dynamics.md's missing File State table and Navigation
    Anchors block — both confirmed present via direct fetch.

USAGE:
  1. Cell 1 — run once per session (builds registry from Routing.md)
  2. Cell 2 — configure audit (edit TARGET_FILE and FOCUS only)
  3. Cell 3 — fetch files
  4. Cell 3.5 — Phase 1 enforcement + boundary index + aging check (auto)
  5. Cell 4 — assemble prompt
  6. Cell 5 — print prompt to copy
  7. Cell 6 (optional) — save prompt to file
"""

# ─────────────────────────────────────────────────────────────────────
# CELL 1 — Build registry from Routing.md + fallback (run once)
# ─────────────────────────────────────────────────────────────────────

import urllib.request
import urllib.parse
import re

BASE = "https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/"

# ── Legacy aliases ────────────────────────────────────────────────────
# Kept separate from canonical registry. Short names that resolve to
# current canonical paths. Never auto-generated from Routing.md.
# Also home for non-.md/.py Admin/ files whose names contain spaces —
# _parse_routing()'s regex cannot match those from Routing.md's table.
ALIASES = {
    "Unknowns_LF.md":                    "Unknowns.md",
    "Canonical_Terms_LF.md":             "Admin/Canonical_Terms.md",
    "Trajectories_LF.md":                "Admin/Trajectories.md",
    "economics_v0.md":                   "Admin/Economics.md",
    "Precision_LF.md":                   "Architecture/Precision.md",
    "energy_v0.md":                      "Operations/Energy.md",
    "Air_Scrubber_v0.md":                "Operations/Air_Scrubber.md",
    "Support_Raft_v0.md":                "Tests/Support_Raft.md",
    "leviathan_testing.md":              "Tests/Leviathan_testing.md",
    "Lazarus_forge_v0_flow.md":          "Architecture/Forge_flow.md",
    "geck_forge_seed.md":                "Architecture/Geck_forge_seed.md",
    "Material_Separation_Gate_v0.md":    "Operations/Gate_04_Separation_Mechanical.md",
    "Spin_Chamber_v0.md":                "Operations/Gate_05_Separation_Thermal.md",
    "Component_Triage_System.md":        "Operations/Gate_02_Triage.md",
    "Ship_of_Theseus_Right_to_Repair.md":"Admin/Ship_of_Theseus.md",
    "Stratification_Chamber_v0.md":      "Operations/Gate_04_Separation_Mechanical.md",
    "Nothingness Theorem":               "Admin/Nothingness%20Theorem",
    "Computational Institutional Reasoning": "Admin/Computational%20Institutional%20Reasoning",
}

# ── Fallback registry ─────────────────────────────────────────────────
# Used only if Routing.md fetch fails. Keep in sync manually as a
# safety net — primary source is always Routing.md.
FALLBACK_REGISTRY = {
    "README.md":                         "README.md",
    "Discovery.md":                      "Discovery.md",
    "Routing.md":                        "Routing.md",
    "Unknowns.md":                       "Unknowns.md",
    "Auditor_Protocols.md":              "Admin/Auditor_Protocols.md",
    "Canonical_Terms.md":                "Admin/Canonical_Terms.md",
    "Economics.md":                      "Admin/Economics.md",
    "Engineer_Protocols.md":             "Admin/Engineer_Protocols.md",
    "Environmental_Constraints.md":      "Admin/Environmental_Constraints.md",
    "Ethical_Constraints.md":            "Admin/Ethical_Constraints.md",
    "File_Template.md":                  "Admin/File_Template.md",
    "Forge_Audit_Kit.md":                "Admin/Forge_Audit_Kit.md",
    "Governance_Charter.md":             "Admin/Governance_Charter.md",
    "Governance_Migration_Protocol.md":  "Admin/Governance_Migration_Protocol.md",
    "Repository_Integrity_Protocol.md":  "Admin/Repository_Integrity_Protocol.md",
    "Repository_Structure.md":           "Admin/Repository_Structure.md",
    "Safety_Protocols.md":               "Admin/Safety_Protocols.md",
    "Security_Protocols.md":             "Admin/Security_Protocols.md",
    "Ship_of_Theseus.md":                "Admin/Ship_of_Theseus.md",
    "Trajectories.md":                   "Admin/Trajectories.md",
    "Verification_Gates_LF.md":          "Admin/Verification_Gates_LF.md",
    "AUDIT_HARNESS.py":                  "Admin/AUDIT_HARNESS.py",
    "Experiments.md":                    "Admin/Experiments.md",
    "Chemistry.md":                      "Architecture/Chemistry.md",
    "Cognitive_Frameworks.md":           "Architecture/Cognitive_Frameworks.md",
    "Components.md":                     "Architecture/Components.md",
    "Engineering.md":                    "Architecture/Engineering.md",
    "Facilities.md":                     "Architecture/Facilities.md",
    "Forge_flow.md":                     "Architecture/Forge_flow.md",
    "Forge_Net.md":                      "Architecture/Forge_Net.md",
    "Friction_Dynamics.md":              "Architecture/Friction_Dynamics.md",
    "Geck_forge_seed.md":                "Architecture/Geck_forge_seed.md",
    "Mechanical_Structures.md":          "Architecture/Mechanical_Structures.md",
    "Precision.md":                      "Architecture/Precision.md",
    "Thermal_Systems.md":                "Architecture/Thermal_Systems.md",
    "Gate_01_Intake.md":                 "Operations/Gate_01_Intake.md",
    "Gate_02_Triage.md":                 "Operations/Gate_02_Triage.md",
    "Gate_03_Reduction.md":              "Operations/Gate_03_Reduction.md",
    "Gate_04_Separation_Mechanical.md":  "Operations/Gate_04_Separation_Mechanical.md",
    "Gate_05_Separation_Thermal.md":     "Operations/Gate_05_Separation_Thermal.md",
    "Gate_06_Fabrication.md":            "Operations/Gate_06_Fabrication.md",
    "Gate_07_Utilization.md":            "Operations/Gate_07_Utilization.md",
    "Air_Scrubber.md":                   "Operations/Air_Scrubber.md",
    "Electronics.md":                    "Operations/Electronics.md",
    "Energy.md":                         "Operations/Energy.md",
    "Plastics.md":                       "Operations/Plastics.md",
    "Woodworking.md":                    "Operations/Woodworking.md",
    "Cognitive_Salvage_Layer.md":        "Tests/Cognitive_Salvage_Layer.md",
    "Leviathan_testing.md":              "Tests/Leviathan_testing.md",
    "Living_Waters.md":                  "Tests/Living_Waters.md",
    "Solar_Descent.md":                  "Tests/Solar_Descent.md",
    "Support_Raft.md":                   "Tests/Support_Raft.md",
    "Trophic_Forge.md":                  "Tests/Trophic_Forge.md",
    "Hydrologic_Resource_Cascade.md":    "Tests/Hydrologic_Resource_Cascade.md",
    "Chaos_Dynamics.md":                 "Tests/Chaos_Dynamics.md",
    "Biofouling.md":                     "Challenges/Biofouling.md",
    "Critical_Minerals.md":              "Challenges/Critical_Minerals.md",
    "Emergence.md":                      "Challenges/Emergence.md",
    "Planned_Obsolescence.md":           "Challenges/Planned_Obsolescence.md",
    "Waste.md":                          "Challenges/Waste.md",
    "Water.md":                          "Challenges/Water.md",
    "Return_To_Eden.md":                 "Challenges/Return_To_Eden.md",
    "Closed_Loop_Feedstock.md":          "Challenges/Closed_Loop_Feedstock.md",
}

def _parse_routing(content):
    """
    Parse Routing.md Master Routing Map table into {short_name: repo_path}.
    Expects rows like: | `Admin/Foo.md` | [Raw](...) | [Repo](...) | ... |
    Returns dict mapping basename → folder-prefixed path.
    NOTE: only matches backtick-quoted paths ending in .md or .py — files
    without an extension or containing spaces (e.g. the two Admin/ Tier 0
    philosophical/theoretical documents) will not be picked up here and
    must be hand-maintained in ALIASES instead.
    """
    registry = {}
    for line in content.splitlines():
        # Match table rows containing a backtick-quoted path
        m = re.search(r'`([^`]+\.(?:md|py))`', line)
        if not m:
            continue
        full_path = m.group(1)
        # Derive short name: strip folder prefix, keep filename
        short = full_path.split("/")[-1]
        # Avoid overwriting with duplicates (keep first occurrence)
        if short not in registry:
            registry[short] = full_path
    return registry

def _build_registry():
    """
    Fetch Routing.md and build FILE_REGISTRY dynamically.
    Falls back to FALLBACK_REGISTRY if fetch fails.
    Reports drift between dynamic and fallback registries.
    """
    print("Building registry from Routing.md...")
    url = BASE + "Routing.md"
    try:
        with urllib.request.urlopen(url) as r:
            routing_content = r.read().decode("utf-8")
        dynamic = _parse_routing(routing_content)
        print(f" ✓ Routing.md fetched — {len(dynamic)} canonical paths parsed")

        # Drift detection against fallback
        missing_from_fallback = [k for k in dynamic if k not in FALLBACK_REGISTRY
                                  and k not in ALIASES]
        missing_from_dynamic  = [k for k in FALLBACK_REGISTRY if k not in dynamic]

        if missing_from_fallback:
            print(f"\n⚠ REGISTRY DRIFT — in Routing.md but not fallback "
                  f"({len(missing_from_fallback)}):")
            for f in sorted(missing_from_fallback):
                print(f"    + {f} → {dynamic[f]}")
            print("  → Fallback registry needs updating.")

        if missing_from_dynamic:
            print(f"\n⚠ REGISTRY DRIFT — in fallback but not Routing.md "
                  f"({len(missing_from_dynamic)}):")
            for f in sorted(missing_from_dynamic):
                print(f"    - {f}")
            print("  → These may be renamed, removed, or Routing.md is stale.")

        if not missing_from_fallback and not missing_from_dynamic:
            print(" ✓ Registry in sync with fallback — no drift detected")

        # Merge: dynamic takes precedence; aliases appended
        merged = {**dynamic, **ALIASES}
        return merged, routing_content

    except Exception as e:
        print(f" ✗ Routing.md fetch FAILED: {e}")
        print("   Falling back to hard-coded registry.")
        merged = {**FALLBACK_REGISTRY, **ALIASES}
        return merged, None

FILE_REGISTRY, _routing_content = _build_registry()

def fetch(filename):
    path = FILE_REGISTRY.get(filename, filename)
    # Encode spaces/special chars in path segments, but preserve existing
    # %20 (already-encoded aliases) and slashes (folder separators).
    safe_path = urllib.parse.quote(path, safe="/%")
    url = BASE + safe_path
    try:
        with urllib.request.urlopen(url) as r:
            content = r.read().decode("utf-8")
        alias_note = f" (alias → {path})" if path != filename else ""
        print(f" ✓ {filename}{alias_note} ({len(content):,} chars)")
        return content
    except Exception as e:
        print(f" ✗ {filename} — FAILED: {e}")
        print(f"   Attempted URL: {url}")
        return f"[FETCH FAILED: {filename} at {url}]"

print(f"\nRegistry contains {len(FILE_REGISTRY)} file mappings "
      f"({len(FILE_REGISTRY) - len(ALIASES)} canonical + {len(ALIASES)} aliases).")
print("\nCanonical files:")
for short, path in sorted(FILE_REGISTRY.items()):
    if short not in ALIASES:
        print(f"  {short:50} → {path}")


# ─────────────────────────────────────────────────────────────────────
# CELL 2 — CONFIGURE THIS CELL (edit TARGET_FILE and FOCUS only)
# ─────────────────────────────────────────────────────────────────────

# ── STEP 1: Set the file you are auditing ─────────────────────────
TARGET_FILE = "Governance_Charter.md"

# ── STEP 2: Set the audit focus (1-3 sentences) ──────────────────
FOCUS = """
Standard audit. Apply full fallacy checklist and verification gates.
Pay particular attention to hazard detection gaps, upstream dependency
fragility, and unknown item handling doctrine.
""".strip()

# ── STEP 3: Add extra context files if needed ─────────────────────
# Forge_Audit_Kit.md is always loaded automatically.
# Add files here ONLY when the audit focus requires them.
# Each file adds ~5-15k chars. Keep total under 60k where possible.
EXTRA_FILES = [
    # "File_Template.md",               # structural compliance audit focus
    # "Forge_flow.md",                  # gate logic and vocabulary standard
    # "Ethical_Constraints.md",         # ethics cross-ref, Anti-Weaponization
    # "Energy.md",                      # energy claims central
    # "Forge_Net.md",                   # network dependency central
    # "Gate_02_Triage.md",              # triage handoff relevant
    # "Components.md",                  # component taxonomy relevant
    # "Unknowns.md",                    # cross-module audits, unknown routing
    # "Discovery.md",                   # orientation audits, new agents
    # "Routing.md",                     # programmatic file lookup
    # "Mechanical_Structures.md",       # salvaged-frame fabrication
    # "Thermal_Systems.md",             # heat transfer, Peltier, TEG, heat pump
    # "Friction_Dynamics.md",           # fluid flow, aerodynamics, tribology
    # "Chemistry.md",                   # electrochemistry, corrosion, polymers
    # "Cognitive_Frameworks.md",        # autonomy, TMR doctrine
    # "Engineer_Protocols.md",          # engineering authority, risk threshold
    # "Safety_Protocols.md",            # physical operator safety, PPE
    # "Facilities.md",                  # physical site constraints, airflow
    # "Precision.md",                   # tolerance tiers, metrology
    # "Economics.md",                   # procurement, barter, profitability
    # "Environmental_Constraints.md",   # site constraints, regulatory compliance, jurisdiction
    # "Governance_Migration_Protocol.md", # Tier 1 amendment, migration
    # "Repository_Structure.md",        # naming conventions, folder assignment
    # "Security_Protocols.md",          # cryptographic trust, authentication
    # "Repository_Integrity_Protocol.md", # integrity baselines, violation classification
    # ── Tests/ ──────────────────────────────────────────────────────
    # "Cognitive_Salvage_Layer.md",     # heuristic harvesting pipeline, GH-series unknowns
    # "Living_Waters.md",               # water purification, LW-UNK items
    # "Trophic_Forge.md",               # biological cascade, TF-UNK items
    # "Solar_Descent.md",               # underground solar, SD-UNK items
    # "Support_Raft.md",                # marine platform, SR-UNK items
    # "Leviathan_testing.md",           # hostile-environment autonomy
    # "Hydrologic_Resource_Cascade.md", # cascade hydrology, HR-UNK items
    # "Chaos_Dynamics.md",              # sandbox/R&D pipeline doctrine, EN-005 vehicle; no File State table yet
    # ── Challenges/ ─────────────────────────────────────────────────
    # "Water.md",                       # hydrological challenge requirements
    # "Biofouling.md",                  # marine fouling, MIC, BF-UNK items
    # "Waste.md",                       # hazardous stream, WA-UNK items
    # "Planned_Obsolescence.md",        # firmware lock, potting removal
    # "Critical_Minerals.md",           # rare earth, urban mining, CM-UNK
    # "Emergence.md",                   # emergent agent behavior, EM-UNK
    # "Return_To_Eden.md",              # Eden Index cross-system heuristic, no File State sidecar yet
    # "Closed_Loop_Feedstock.md",       # CLF-series, 3 Critical unknowns; CLF-005 shares Φ_ext symbol w/ Return_To_Eden.md — pull both if auditing either
]

# ── STEP 4: Set document status ──────────────────────────────────
DOC_STATUS = "Exploration"

# ── PRE-FLIGHT VALIDATION ─────────────────────────────────────────
# Catches typos in EXTRA_FILES before any network calls are made.
_unknown_extras = [f for f in EXTRA_FILES if f not in FILE_REGISTRY]
if _unknown_extras:
    raise ValueError(
        f"EXTRA_FILES contains unrecognized filenames:\n"
        + "\n".join(f"  - {f}" for f in _unknown_extras)
        + "\n\nCheck FILE_REGISTRY keys or correct the filename."
    )

# ── FRAMING LINE ─────────────────────────────────────────────────
FRAMING_LINE = (
    f'"{TARGET_FILE}" is currently classified as {DOC_STATUS}. '
    f"Audit for promotion blockers and consistency with the repository standard. "
    f"Do not apply specification-level pressure to intentionally incomplete content."
)

print(f"Target:  {TARGET_FILE}")
print(f"Path:    {FILE_REGISTRY.get(TARGET_FILE, TARGET_FILE)}")
print(f"Status:  {DOC_STATUS}")
print(f"Extras:  {EXTRA_FILES if EXTRA_FILES else 'none'}")
print(f"\nFraming line (paste at top of Claude conversation):")
print(f"  {FRAMING_LINE}")
print("\n✓ Pre-flight validation passed — all EXTRA_FILES recognized.")


# ─────────────────────────────────────────────────────────────────────
# CELL 3 — Fetch files
# ─────────────────────────────────────────────────────────────────────

print("Fetching files...\n")

CORE_FILES = ["Forge_Audit_Kit.md", TARGET_FILE]
ALL_FILES = CORE_FILES + EXTRA_FILES

fetched = {}
total_chars = 0
for f in ALL_FILES:
    content = fetch(f)
    fetched[f] = content
    total_chars += len(content)

print(f"\nDone. {len(fetched)} file(s) loaded.")
print(f"Total chars: {total_chars:,} (~{total_chars // 4:,} tokens estimated)")

if total_chars > 60000:
    print("\n⚠ WARNING: Approaching token ceiling. Consider removing an EXTRA_FILE.")
elif total_chars > 40000:
    print("\n→ Moderate load. Should be fine for most sessions.")
else:
    print("\n✓ Light load. Room to spare.")

failed = [f for f, c in fetched.items() if c.startswith("[FETCH FAILED")]
if failed:
    print(f"\n⚠ FETCH FAILURES ({len(failed)}):")
    for f in failed:
        print(f"  - {f}")
    print("  Audit kit or target file failure will compromise the audit.")


# ─────────────────────────────────────────────────────────────────────
# CELL 3.5 — Phase 1 enforcement + boundary index + unknown aging
# ─────────────────────────────────────────────────────────────────────
# Phase 1 enforcement runs three checks on every fetched file:
#   1. Constitutional check (Ethical Anchor exact match) → halt on violation
#   2. Structural field presence (File State keys) → log, non-blocking
#   3. Cross-reference resolution (internal .md paths) → log, non-blocking
#
# Boundary index and unknown aging run after enforcement, as before.
# Produces a compact session index — no stored artifact, no maintenance.
# Persistent version of this information: Discovery.md scope map.
#
# CURRENT CYCLE: update this value at the start of each audit pass.
# Increment by 1 each time a full multi-agent audit cycle completes.
CURRENT_CYCLE = 10   # ← update this each session

import re as _re
import datetime
import os
import sys
import json

# ── Phase 1 constants ────────────────────────────────────────────────
QUARANTINE_FILE = ".quarantine"

# Default fallback — overridden by bootstrap if Ethical_Constraints.md loaded
_DEFAULT_ANCHOR = "Attempt to do no harm. Defer to Ethical_Constraints.md if present."

# Default fallback — overridden by bootstrap if File_Template.md loaded
_DEFAULT_REQUIRED_FIELDS = ["Status", "Spec Gates", "Verification Ref", "Ethical Anchor"]

# ── Finding class ─────────────────────────────────────────────────────
class Finding:
    """Structured finding with severity, category, file, and message."""
    def __init__(self, severity, category, file_path, message):
        self.severity = severity    # CRITICAL | MAJOR | WARNING
        self.category = category    # CONSTITUTION | STRUCTURE | REFERENCE
        self.file_path = file_path
        self.message = message

    def __str__(self):
        return f"[{self.severity}/{self.category}] {self.file_path}: {self.message}"

    def to_dict(self):
        return {
            "severity": self.severity,
            "category": self.category,
            "file": self.file_path,
            "message": self.message
        }

# ── Bootstrap governance rules from doctrine files ────────────────────
def _bootstrap_rules(fetched_files):
    """
    Pull enforcement rules from doctrine files already in the fetched set.
    Falls back to hardcoded defaults if source files are not loaded.
    Rules live in the repository, not in this script — prevents harness drift.
    """
    anchor = _DEFAULT_ANCHOR
    required_fields = list(_DEFAULT_REQUIRED_FIELDS)

    # Try to extract Ethical Anchor from Ethical_Constraints.md
    ec_content = fetched_files.get("Ethical_Constraints.md", "")
    if ec_content and not ec_content.startswith("[FETCH FAILED"):
        # Look for the canonical anchor string in the Ethical Anchor field
        m = _re.search(
            r'Ethical Anchor\s*\|?\s*(Attempt to do no harm[^|\n]*)',
            ec_content
        )
        if m:
            anchor = m.group(1).strip().rstrip('|').strip()

    # Try to extract required fields from File_Template.md
    ft_content = fetched_files.get("File_Template.md", "")
    if ft_content and not ft_content.startswith("[FETCH FAILED"):
        # Pull table rows from File State section
        fs_match = _re.search(
            r'## File State(.*?)(?=\n##)', ft_content, _re.DOTALL
        )
        if fs_match:
            rows = _re.findall(r'\|\s*([A-Za-z][A-Za-z\s]+?)\s*\|', fs_match.group(1))
            extracted = [r.strip() for r in rows
                         if r.strip() and r.strip() not in ("Field", "Value", "---")]
            if len(extracted) >= 4:
                required_fields = extracted

    return anchor, required_fields

# ── File State table parser ───────────────────────────────────────────
def _parse_file_state(content):
    """
    Extract the File State table from document content and return
    a key→value dict. Strict key parsing prevents prose false-positives.
    """
    metadata = {}
    # Find the File State section
    m = _re.search(
        r'## File State\s*\n.*?\n((?:\|.*\|\n?)+)',
        content, _re.DOTALL
    )
    if not m:
        return metadata, False  # (metadata, found)

    table_text = m.group(1)
    for line in table_text.splitlines():
        # Match table rows: | Key | Value |
        row = _re.match(r'\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|', line)
        if row:
            key = row.group(1).strip()
            val = row.group(2).strip()
            # Skip header separator rows
            if key and not _re.match(r'^[-:]+$', key):
                metadata[key] = val
    return metadata, True

# ── Cross-reference extractor ─────────────────────────────────────────
def _extract_md_refs(content):
    """
    Extract internal .md file paths from content.
    Catches: markdown links, backtick paths, table cell paths.
    Skips URLs (http/https) and non-.md references.
    """
    refs = set()
    # Markdown links [text](path.md) or [text](path.md#anchor)
    for link in _re.findall(r'\[.*?\]\(([^)]+)\)', content):
        clean = link.split('#')[0].strip()
        if clean.endswith('.md') and not clean.startswith('http'):
            refs.add(clean)
    # Backtick paths `Admin/Foo.md`
    for path in _re.findall(r'`([A-Za-z][A-Za-z0-9_/]+\.md)`', content):
        refs.add(path)
    return refs

# ── Phase 1 enforcement per file ──────────────────────────────────────
def _enforce_phase1(filename, content, anchor, required_fields, registry, findings):
    """
    Run three Phase 1 checks on a single fetched file.
    Constitutional violation writes .quarantine and halts.
    All other findings are logged and non-blocking.
    """
    if content.startswith("[FETCH FAILED"):
        findings.append(Finding(
            "MAJOR", "STRUCTURE", filename,
            "File fetch failed — structural checks skipped. "
            "Verify path in Routing.md."
        ))
        return

    metadata, found = _parse_file_state(content)

    # ── Check 1: Constitutional — Ethical Anchor ──────────────────────
    if not found:
        findings.append(Finding(
            "MAJOR", "STRUCTURE", filename,
            "File State table not found — Ethical Anchor cannot be verified."
        ))
    elif "Ethical Anchor" not in metadata:
        findings.append(Finding(
            "MAJOR", "CONSTITUTION", filename,
            "Ethical Anchor field absent from File State table. "
            "Unable to verify alignment — not confirmed as mutation."
        ))
    else:
        detected = metadata["Ethical Anchor"]
        if detected != anchor:
            payload = {
                "trigger": "CONFIRMED_CONSTITUTIONAL_MUTATION",
                "file": filename,
                "expected": anchor,
                "detected": detected,
                "timestamp": str(datetime.date.today()),
                "action": "Session halted. Clear .quarantine after manual review."
            }
            with open(QUARANTINE_FILE, "w", encoding="utf-8") as qf:
                json.dump(payload, qf, indent=2)
            print(f"\n{'!'*60}")
            print(f"  CONSTITUTIONAL MUTATION DETECTED")
            print(f"  File:     {filename}")
            print(f"  Expected: {anchor}")
            print(f"  Found:    {detected}")
            print(f"  .quarantine written. Session halted.")
            print(f"{'!'*60}\n")
            sys.exit(1)

    # ── Check 2: Structural — required field presence ─────────────────
    if found:
        for field in required_fields:
            if field not in metadata:
                findings.append(Finding(
                    "MAJOR", "STRUCTURE", filename,
                    f"Required field '{field}' missing from File State table."
                ))

    # ── Check 3: Cross-reference resolution (classified) ─────────────
    # Planned renames: paths that appear in docs as future canonical names
    # before Routing.md has been updated.
    PLANNED_RENAMES = {
        "Forge_Flow.md": "Architecture/Forge_flow.md — casing correction pending",
    }
    # Archive path pattern — references to versioned archive files
    _ARCHIVE_PAT = _re.compile(
        r'(?:Archive/|_v\d+\.|_20\d{6}|v0\.\d+\.md$)', _re.IGNORECASE
    )

    refs = _extract_md_refs(content)
    for ref in refs:
        clean = ref.lstrip('./')
        # Skip known external repos and explicit planned labels
        if any(x in ref for x in ['http', 'Lazarus-Forge-', 'Astroid', 'planned']):
            continue

        registry_paths = set(registry.values()) | set(registry.keys())

        if clean in registry_paths:
            continue  # Resolved — no finding

        # Classify the miss
        if clean in ALIASES or clean.replace('Admin/', '').replace('Operations/', '') in ALIASES:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[LEGACY] '{ref}' — legacy name; check Rename Registry "
                f"in Discovery.md for canonical path."
            ))
        elif clean in PLANNED_RENAMES:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[PLANNED] '{ref}' — {PLANNED_RENAMES[clean]}"
            ))
        elif _ARCHIVE_PAT.search(clean):
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[ARCHIVE] '{ref}' — versioned archive reference; "
                f"expected once Archive/ is established."
            ))
        else:
            findings.append(Finding(
                "WARNING", "REFERENCE", filename,
                f"[UNKNOWN] '{ref}' — no canonical or alias match. "
                f"Investigate: stale reference or missing Routing.md entry."
            ))

# ── Main Phase 1 runner ───────────────────────────────────────────────
def run_phase1(fetched_files, registry):
    """
    Pre-flight quarantine check, then Phase 1 enforcement across all
    fetched files. Returns findings list and bootstrapped rules.
    """
    # Quarantine pre-flight — halt immediately if prior session left a flag
    if os.path.exists(QUARANTINE_FILE):
        try:
            with open(QUARANTINE_FILE) as qf:
                payload = json.load(qf)
            print(f"\n{'!'*60}")
            print(f"  QUARANTINE ACTIVE — session blocked")
            print(f"  Prior trigger: {payload.get('trigger', 'unknown')}")
            print(f"  File:          {payload.get('file', 'unknown')}")
            print(f"  Resolve the violation, delete .quarantine, then re-run.")
            print(f"{'!'*60}\n")
        except Exception:
            print(f"\n⚠ .quarantine file exists but could not be parsed.")
            print(f"  Delete manually after reviewing repository state.\n")
        sys.exit(1)

    anchor, required_fields = _bootstrap_rules(fetched_files)
    findings = []

    print(f"\nPhase 1 enforcement — {len(fetched_files)} file(s)")
    print(f"  Anchor source:  {'Ethical_Constraints.md' if 'Ethical_Constraints.md' in fetched_files else 'hardcoded default'}")
    print(f"  Fields source:  {'File_Template.md' if 'File_Template.md' in fetched_files else 'hardcoded default'}")
    print(f"  Anchor string:  {anchor[:60]}{'...' if len(anchor) > 60 else ''}\n")

    for fname, content in fetched_files.items():
        _enforce_phase1(fname, content, anchor, required_fields, registry, findings)

    # Summary
    criticals = [f for f in findings if f.severity == "CRITICAL"]
    majors    = [f for f in findings if f.severity == "MAJOR"]
    warnings  = [f for f in findings if f.severity == "WARNING"]

    if not findings:
        print("✓ Phase 1: No violations detected.")
    else:
        if majors:
            print(f"⚠ Phase 1 MAJOR findings ({len(majors)}):")
            for f in majors:
                print(f"    {f}")
        if warnings:
            print(f"→ Phase 1 WARNING findings ({len(warnings)}):")
            for f in warnings:
                print(f"    {f}")

    return findings, anchor, required_fields

# Run Phase 1 now
_p1_findings, _p1_anchor, _p1_fields = run_phase1(fetched, FILE_REGISTRY)

# Map of known unknown IDs to the cycle they were first logged.
# Add entries here when new unknowns are registered.
# Used for aging detection — IDs not in this map report age as unknown.
UNKNOWN_FIRST_CYCLE = {
    # Ethics & Governance
    "EC-001": 1, "EC-002": 1, "EC-003": 1, "EC-004": 1, "EC-005": 1,
    "EC-006": 1, "EC-007": 1, "EC-008": 7, "EC-009": 7, "EC-010": 7,
    "EC-011": 7,
    "GOV-001": 2, "GOV-002": 2, "GOV-003": 2, "GOV-004": 2, "GOV-005": 2,
    "GOV-006": 2, "GOV-007": 2, "GOV-008": 3, "GOV-009": 3, "GOV-010": 7,
    "SEC-001": 4, "SEC-002": 4, "SEC-003": 4, "SEC-004": 4, "SEC-005": 4,
    "SEC-006": 4, "SEC-007": 4, "SEC-008": 9, "SEC-009": 9, "SEC-010": 9,
    "SEC-011": 9,
    "RIP-001": 2, "RIP-002": 2, "RIP-003": 2, "RIP-005": 4,
    "RIP-006": 9, "RIP-007": 9,
    "GMP-003": 5, "GMP-004": 5, "GMP-005": 5, "GMP-006": 9,
    "GMP-007": 9, "GMP-008": 9,
    "CT-001": 5, "CT-002": 5, "CT-003": 5, "CT-004": 6, "CT-005": 7,
    "CT-006": 9, "CT-007": 9, "CT-008": 10, "CT-009": 10,
    "VG-001": 5,
    "AP-001": 2, "AP-002": 2, "AP-003": 2, "AP-004": 2, "AP-005": 2,
    "AP-006": 2, "AP-007": 2,
    "AP-008": 9, "AP-009": 9, "AP-010": 9, "AP-011": 9,
    "AP-012": 10, "AP-013": 10, "AP-014": 10, "AP-015": 10,
    "AP-016": 10, "AP-017": 10, "AP-018": 10, "AP-019": 10,
    "AP-020": 10,
    # Environmental
    "ENV-001": 9, "ENV-002": 9, "ENV-003": 9, "ENV-004": 9, "ENV-005": 9,
    "ENV-006": 9, "ENV-008": 9, "ENV-009": 9,
    # Engineering & Structures
    "EN-001": 5, "EN-002": 5, "EN-003": 5, "EN-004": 5, "EN-005": 5,
    "ME-001": 5, "ME-002": 5, "ME-003": 8, "ME-004": 8,
    # Cognitive / Emergence
    "CF-001": 5, "CF-002": 5, "CF-003": 5,
    "EM-001": 6, "EM-002": 6, "EM-003": 6, "EM-004": 6,
    # Gate Logic
    "FL-001": 1, "TS-001": 1, "TS-002": 1, "TS-003": 1,
    "CO-001": 1, "CO-002": 1,
    # Energy
    "EV-001": 4, "EV-002": 4, "EV-003": 4,
    # Operations
    "SC-001": 1, "SC-002": 1, "SC-003": 1, "SC-004": 1, "SC-005": 1,
    "SC-006": 1, "SC-007": 1, "SC-008": 1,
    "MG-001": 1, "MG-002": 1, "MG-003": 1, "MG-004": 1, "MG-005": 1,
    "MG-006": 1, "MG-007": 1, "MG-008": 1,
    "GI-001": 3, "GI-002": 3, "GI-003": 3, "GI-004": 3, "GI-005": 3,
    "GI-006": 3, "GI-007": 3,
    "GR-001": 3, "GR-002": 3, "GR-003": 3, "GR-004": 3, "GR-005": 3,
    "GR-006": 3, "GR-007": 3, "GR-008": 3,
    "GF-001": 3, "GF-002": 3, "GF-003": 3, "GF-004": 3,
    "GF-006": 3, "GF-007": 3,
    "GU-001": 3, "GU-002": 3, "GU-003": 3, "GU-004": 3, "GU-005": 3,
    "PL-001": 4, "PL-002": 4, "PL-003": 4, "PL-004": 4, "PL-005": 4,
    "EL-001": 3, "EL-002": 3, "EL-003": 3, "EL-004": 3, "EL-005": 3,
    "EL-006": 3, "EL-007": 3, "EL-008": 3,
    # Chemistry
    "CE-001": 6, "CE-002": 6, "CE-003": 6, "CE-004": 6, "CE-005": 8,
    # Thermal / Friction
    "TH-001": 5, "TH-002": 5, "TH-003": 5, "TH-004": 5,
    "TH-005": 8, "TH-006": 8,
    "FD-001": 5, "FD-002": 5, "FD-003": 5, "FD-005": 8,
    # Challenges
    "WA-001": 6, "WA-002": 6, "WA-003": 6, "WA-004": 6,
    "BF-001": 6, "BF-002": 6, "BF-003": 6, "BF-004": 6,
    "PO-001": 6, "PO-002": 6, "PO-003": 6, "PO-004": 6,
    "WS-001": 6, "WS-002": 6, "WS-003": 6, "WS-004": 6,
    "CM-001": 6, "CM-002": 6, "CM-003": 6, "CM-004": 6,
    # Tests
    "LT-001": 1, "LT-002": 1, "LT-003": 1, "LT-004": 1, "LT-005": 1,
    "LT-006": 1,
    "SR-001": 6, "SR-002": 6, "SR-003": 6, "SR-004": 6, "SR-005": 6,
    "SR-006": 6, "SR-007": 6, "SR-008": 6, "SR-009": 6,
    "SR-011": 5, "SR-012": 5, "SR-013": 5,
    "LW-UNK-001": 7, "LW-UNK-002": 7, "LW-UNK-003": 7, "LW-UNK-004": 7,
    "LW-UNK-005": 7, "LW-UNK-006": 7, "LW-UNK-007": 7, "LW-UNK-008": 7,
    "LW-UNK-009": 7,
    "TF-001": 7, "TF-002": 7, "TF-003": 7, "TF-004": 7, "TF-005": 7,
    "TF-006": 7, "TF-007": 7, "TF-008": 7, "TF-009": 7, "TF-010": 7,
    "SD-UNK-001": 7, "SD-UNK-002": 7, "SD-UNK-003": 7, "SD-UNK-004": 7,
    "SD-UNK-005": 7, "SD-UNK-006": 7, "SD-UNK-007": 7, "SD-UNK-008": 7,
    "SD-UNK-009": 7, "SD-UNK-010": 7, "SD-UNK-011": 7, "SD-UNK-012": 7,
    # Cognitive Salvage Layer — GH-series (cycle 10)
    "GH-001": 10, "GH-002": 10, "GH-003": 10, "GH-004": 10,
    "GH-005": 10, "GH-006": 10, "GH-007": 10, "GH-008": 10,
    "GH-009": 10, "GH-010": 10, "GH-011": 10, "GH-012": 10,
    # Hydrologic Resource Cascade — HR-series (cycle 10)
    "HR-UNK-001": 10, "HR-UNK-002": 10,
    # Cognitive Frameworks (cycle 10)
    "CF-004": 10,
    # Closed Loop Feedstock — CLF-series (cycle 10)
    "CLF-001": 10, "CLF-002": 10, "CLF-003": 10, "CLF-004": 10,
    "CLF-005": 10, "CLF-006": 10, "CLF-007": 10, "CLF-008": 10,
    "CLF-009": 10, "CLF-010": 10,
    # Misc
    "FA-001": 4, "FA-002": 4, "FA-003": 4, "FA-004": 4,
    "SP-001": 4, "SP-002": 4, "SP-003": 4, "SP-004": 4, "SP-005": 4,
    "SP-006": 4,
    "AS-001": 4, "AS-002": 4, "AS-003": 4, "AS-004": 4,
    "TR-001": 4, "TR-002": 3,
    "FN-001": 4, "FN-002": 4, "FN-003": 4, "FN-004": 4, "FN-005": 4,
    "WW-001": 4, "WW-002": 4, "WW-003": 4, "WW-004": 4, "WW-005": 4,
    "ST-001": 1, "ST-002": 1, "ST-003": 5, "ST-004": 10,
    "GK-002": 1, "GK-003": 1, "GK-004": 1,
    "EP-001": 5, "EP-002": 5, "EP-003": 5, "EP-004": 5,
    "EP-005": 4, "EP-006": 5,
    "PR-001": 4, "PR-002": 4, "PR-003": 4, "PR-004": 4,
    "UNK-008": 6, "UNK-009": 4,
}

EXPIRY_THRESHOLD = 2  # cycles without resolution path before escalation


def extract_boundary(filename, content):
    """Extract File State fields and open unknown IDs from a markdown file."""
    lines = content.splitlines()
    result = {
        "file": filename,
        "status": "—", "gates": "—", "risk": "—",
        "last_audit": "—", "unknowns": []
    }
    in_file_state = False
    in_sidecar = False

    # ── Use enumerate() to avoid lines.index() first-match bug ──────
    for idx, line in enumerate(lines):
        if "## File State" in line:
            in_file_state = True
            in_sidecar = False
            continue
        if in_file_state and line.startswith("##"):
            in_file_state = False

        if in_file_state:
            if re.search(r'\|\s*Status\s*\|', line) and "Body Stability" not in line:
                m = re.search(r'\|\s*Status\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["status"] = m.group(1).strip()
            if re.search(r'\|\s*Spec Gates\s*\|', line):
                m = re.search(r'\|\s*Spec Gates\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["gates"] = m.group(1).strip()
            if re.search(r'\|\s*Highest Risk\s*\|', line):
                m = re.search(r'\|\s*Highest Risk\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["risk"] = m.group(1).strip()
            if re.search(r'\|\s*Last Audit\s*\|', line):
                m = re.search(r'\|\s*Last Audit\s*\|\s*(.+?)\s*\|', line)
                if m:
                    result["last_audit"] = m.group(1).strip()

        # Sidecar unknown IDs — two conventions in use across the repo:
        #   (a) "## Auditor Notes..." header + "### UID" sub-headers (Gate files)
        #   (b) "## N. Open Unknowns" header + a markdown table of UIDs
        #       (e.g. Challenges/Closed_Loop_Feedstock.md)
        if "## Auditor Notes" in line or "Open Unknowns" in line:
            in_sidecar = True
            continue
        if in_sidecar and line.startswith("## ") and "Auditor Notes" not in line and "Open Unknowns" not in line:
            in_sidecar = False
        if in_sidecar:
            # Convention (a): ### UID sub-header
            m = re.match(r'^###\s+([A-Z]+-[\w-]+)', line)
            # Convention (b): | UID | ... | table row
            if not m:
                m = re.match(r'^\|\s*([A-Z]{2,}-\d{3,})\s*\|', line)
            if m:
                uid = m.group(1)
                # Use slice from current idx — avoids first-match bug
                snippet = "\n".join(lines[idx:idx + 8])
                if ("Status        | Resolved" not in snippet and
                        "Status        | Discharged" not in snippet and
                        "Resolved" not in line and "Discharged" not in line):
                    result["unknowns"].append(uid)

    return result


def check_aging(unknown_ids):
    """Return list of (uid, age, overdue) for unknowns in the loaded files."""
    results = []
    for uid in unknown_ids:
        first = UNKNOWN_FIRST_CYCLE.get(uid)
        if first is None:
            results.append((uid, None, False))
        else:
            age = CURRENT_CYCLE - first
            overdue = age >= EXPIRY_THRESHOLD
            results.append((uid, age, overdue))
    return results


def format_boundary_index(fetched_files):
    """Format boundary index + aging alerts for prompt injection."""
    lines = [
        "SESSION BOUNDARY INDEX (auto-extracted — ephemeral)",
        f"Current cycle: {CURRENT_CYCLE} | Expiry threshold: {EXPIRY_THRESHOLD} cycles",
        "Compact summary of loaded files. Full content follows in FILES PROVIDED.",
        "Persistent version: Discovery.md scope map.",
        ""
    ]
    all_unknowns = []
    for fname, content in fetched_files.items():
        if content.startswith("[FETCH FAILED"):
            lines.append(f"  {fname}: FETCH FAILED — excluded from index")
            continue
        b = extract_boundary(fname, content)
        unk_str = ", ".join(b["unknowns"]) if b["unknowns"] else "none open"
        lines.append(f"  {fname}")
        lines.append(f"    Status: {b['status']} | Gates: {b['gates']} | "
                     f"Risk: {b['risk']} | Last Audit: {b['last_audit']}")
        lines.append(f"    Open unknowns: {unk_str}")
        lines.append("")
        all_unknowns.extend(b["unknowns"])

    # Aging report
    aged = check_aging(all_unknowns)
    overdue = [(uid, age) for uid, age, flag in aged if flag]
    if overdue:
        lines.append(f"⚠ EXPIRY WATCH — {len(overdue)} unknown(s) at or past "
                     f"{EXPIRY_THRESHOLD}-cycle threshold:")
        for uid, age in overdue:
            lines.append(f"    {uid}: {age} cycle(s) open — verify resolution path exists")
        lines.append("")
    else:
        lines.append("✓ Expiry Watch: no overdue unknowns in loaded files.")
        lines.append("")

    return "\n".join(lines)


BOUNDARY_INDEX = format_boundary_index(fetched)
print(BOUNDARY_INDEX)


# ─────────────────────────────────────────────────────────────────────
# CELL 4 — Assemble prompt
# ─────────────────────────────────────────────────────────────────────

DIVIDER = "=" * 60
sections = []

sections.append(
    f"Operating as Skeptic/Auditor per Auditor_Protocols.md v0.14\n"
    f"Repository: LazarusForgeV0"
)

sections.append(
    f"ASSUMPTION EXTRACTION (Rule 6):\n"
    f"Prior contributions assumed:\n"
    f"- {TARGET_FILE} is classified as {DOC_STATUS}\n"
    f"- Forge_Audit_Kit.md contains the active Fallacy Checklist, Verification Gates,\n"
    f"  AI Contribution Rules, and condensed Unknowns Registry\n"
    f"- Repository uses folder-based structure: Admin/, Architecture/, Operations/,\n"
    f"  Tests/, Challenges/\n"
    f"- Rename Registry in Discovery.md maps legacy filenames to current canonical paths\n"
    f"- Full reference files: Admin/Auditor_Protocols.md | Unknowns.md\n"
    f"These assumptions are carried forward unless contradicted by new findings."
)

# Boundary index injected between assumptions and task
sections.append(BOUNDARY_INDEX)

sections.append(
    f"TASK:\n"
    f"Audit {TARGET_FILE} (status: {DOC_STATUS}).\n\n"
    f"Apply the full Fallacy Checklist from Forge_Audit_Kit.md.\n"
    f"Use the Verification Gates to assess promotion readiness.\n"
    f"Open with an Expiry Watch — the SESSION BOUNDARY INDEX above surfaces\n"
    f"any overdue unknowns from the loaded files; confirm and escalate as needed.\n\n"
    f"Audit focus:\n{FOCUS}\n\n"
    f"Label all findings: [FALLACY], [GAP], [CONTRADICTION], [UNLOGGED UNKNOWN],\n"
    f"[CROSS-REF FAILURE]. For each finding, suggest a concrete resolution path.\n\n"
    f"Cross-reference naming note: the repository uses folder-prefixed paths\n"
    f"(Admin/Ethical_Constraints.md, Operations/Energy.md, Challenges/Water.md).\n"
    f"Legacy flat names (Ethical_Constraints.md, energy_v0.md, Spin_Chamber_v0.md)\n"
    f"are aliases — do not flag folder-prefixed paths as cross-reference failures.\n"
    f"The canonical form always includes the folder prefix.\n\n"
    f"End with the standard sign-off format from Forge_Audit_Kit.md."
)

file_block = f"FILES PROVIDED ({len(fetched)}):\n"
for i, (name, content) in enumerate(fetched.items(), 1):
    resolved_path = FILE_REGISTRY.get(name, name)
    file_block += (f"\n{DIVIDER}\nFILE {i}: {name} "
                   f"(fetched from: {resolved_path})\n{DIVIDER}\n{content}\n")
sections.append(file_block)

PROMPT = ("\n\n" + DIVIDER + "\n\n").join(sections)

print(f"Prompt assembled.")
print(f"Total length: {len(PROMPT):,} chars (~{len(PROMPT) // 4:,} tokens estimated)")
print(f"\nRun Cell 5 to print the full prompt.")


# ─────────────────────────────────────────────────────────────────────
# CELL 5 — Print prompt (copy everything below the dashes)
# ─────────────────────────────────────────────────────────────────────

print("FRAMING LINE (paste this at the TOP of the Claude conversation first):")
print("─" * 60)
print(FRAMING_LINE)
print()
print("PROMPT (copy everything below this line):")
print("─" * 60)
print(PROMPT)


# ─────────────────────────────────────────────────────────────────────
# CELL 6 — Optional: save prompt + framing line to file
# ─────────────────────────────────────────────────────────────────────

import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
safe_target = TARGET_FILE.replace(".md", "").replace("/", "_")
filename = f"forge_audit_{safe_target}_{timestamp}.txt"

with open(filename, "w") as f:
    f.write(f"FRAMING LINE:\n{FRAMING_LINE}\n\n")
    f.write("=" * 60 + "\n\n")
    f.write(PROMPT)

print(f"Saved: {filename}")
print("In Colab: Files panel (left sidebar) → download from there.")
print(f"\nTarget file resolved to: {FILE_REGISTRY.get(TARGET_FILE, TARGET_FILE)}")
print(f"Audit kit resolved to:   {FILE_REGISTRY.get('Forge_Audit_Kit.md', 'Admin/Forge_Audit_Kit.md')}")

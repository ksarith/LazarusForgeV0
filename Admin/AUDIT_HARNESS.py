"""
LAZARUS FORGE — AUDIT HARNESS v3
Google Colab notebook cells — paste each block into a separate cell.

CHANGES FROM v2:
  - File registry added — maps short filenames to full repo paths.
    The repository moved from flat to folder-based structure.
    All paths now resolve correctly regardless of folder location.
  - Forge_Audit_Kit.md now correctly fetched from Admin/ folder.
  - Protocol version updated to v0.5.
  - Discovery.md fetch added to EXTRA_FILES options for orientation audits.

USAGE:
  1. Cell 1 — run once per session (fetch helper + registry)
  2. Cell 2 — configure your audit (edit TARGET and FOCUS only)
  3. Cell 3 — fetch files
  4. Cell 4 — assemble prompt
  5. Cell 5 — print prompt to copy
  6. Cell 6 (optional) — save prompt to file

When you hit the token limit, wait for reset, start a new Claude conversation,
paste the output from Cell 5, and add the framing line shown in Cell 2.
"""

# ─────────────────────────────────────────────────────────────────────
# CELL 1 — Fetch helper + file registry (run once per session)
# ─────────────────────────────────────────────────────────────────────

import urllib.request

BASE = "https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/"

# File registry — maps short filenames to full repo paths.
# Update this when files are added, renamed, or moved.
# Short name is what you type in Cell 2. Path is what gets fetched.
FILE_REGISTRY = {
    # Root
    "README.md":                        "README.md",
    "Discovery.md":                     "Discovery.md",
    "Unknowns.md":                      "Unknowns.md",

    # Admin
    "Auditor_Protocols.md":             "Admin/Auditor_Protocols.md",
    "Ethical_Constraints.md":           "Admin/Ethical_Constraints.md",
    "File_Template.md":                 "Admin/File_Template.md",
    "Forge_Audit_Kit.md":               "Admin/Forge_Audit_Kit.md",
    "Ship_of_Theseus.md":               "Admin/Ship_of_Theseus.md",
    "Trajectories.md":                  "Admin/Trajectories.md",
    "AUDIT_HARNESS.py":                 "Admin/AUDIT_HARNESS.py",
    "Governance_Charter.md":            "Admin/Governance_Charter.md",

    # Architecture
    "Cognitive_Frameworks.md":          "Architecture/Cognitive_Frameworks.md",
    "Components.md":                    "Architecture/Components.md",
    "Forge_flow.md":                    "Architecture/Forge_flow.md",
    "Forge_Net.md":                     "Architecture/Forge_Net.md",
    "Geck_forge_seed.md":               "Architecture/Geck_forge_seed.md",

    # Operations
    "Air_Scrubber.md":                  "Operations/Air_Scrubber.md",
    "Electronics.md":                   "Operations/Electronics.md",
    "Energy.md":                        "Operations/Energy.md",
    "Gate_01_Intake.md":                "Operations/Gate_01_Intake.md",
    "Gate_02_Triage.md":                "Operations/Gate_02_Triage.md",
    "Gate_03_Reduction.md":             "Operations/Gate_03_Reduction.md",
    "Gate_04_Separation_Mechanical.md": "Operations/Gate_04_Separation_Mechanical.md",
    "Gate_05_Separation_Thermal.md":    "Operations/Gate_05_Separation_Thermal.md",
    "Gate_06_Fabrication.md":           "Operations/Gate_06_Fabrication.md",
    "Gate_07_Utilization.md":           "Operations/Gate_07_Utilization.md",

    # Tests
    "Leviathan_testing.md":             "Tests/Leviathan_testing.md",
    "Support_Raft.md":                  "Tests/Support_Raft.md",

    # Legacy aliases — resolve to current canonical names.
    # These exist so stale references in cached context still work.
    "Unknowns_LF.md":                   "Unknowns.md",
    "Trajectories_LF.md":               "Admin/Trajectories.md",
    "energy_v0.md":                     "Operations/Energy.md",
    "Air_Scrubber_v0.md":               "Operations/Air_Scrubber.md",
    "Support_Raft_v0.md":               "Tests/Support_Raft.md",
    "leviathan_testing.md":             "Tests/Leviathan_testing.md",
    "Lazarus_forge_v0_flow.md":         "Architecture/Forge_flow.md",
    "geck_forge_seed.md":               "Architecture/Geck_forge_seed.md",
    "Material_Separation_Gate_v0.md":   "Operations/Gate_04_Separation_Mechanical.md",
    "Spin_Chamber_v0.md":               "Operations/Gate_05_Separation_Thermal.md",
    "Component_Triage_System.md":       "Operations/Gate_02_Triage.md",
    "Ship_of_Theseus_Right_to_Repair.md": "Admin/Ship_of_Theseus.md",
}

def fetch(filename):
    path = FILE_REGISTRY.get(filename, filename)
    url = BASE + path
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

print("Fetch helper ready.")
print(f"Registry contains {len(FILE_REGISTRY)} file mappings.")
print("\nKnown files:")
for short, path in sorted(FILE_REGISTRY.items()):
    if not short.endswith("_v0.md") and "LF.md" not in short:  # skip aliases in display
        print(f"  {short:45} → {path}")


# ─────────────────────────────────────────────────────────────────────
# CELL 2 — CONFIGURE THIS CELL (edit TARGET_FILE and FOCUS only)
# ─────────────────────────────────────────────────────────────────────

# ── STEP 1: Set the file you are auditing ──────────────────────────
TARGET_FILE = "Governance_Charter.md"

# ── STEP 2: Set the audit focus (1-3 sentences) ───────────────────
FOCUS = """
Standard audit. Apply full fallacy checklist and verification gates.
Pay particular attention to hazard detection gaps, upstream dependency
fragility, and unknown item handling doctrine.
""".strip()

# ── STEP 3: Add extra context files if needed ─────────────────────
# Forge_Audit_Kit.md is always loaded automatically.
# Add files here ONLY when the audit needs extra context.
# Each file adds ~5-15k chars. Keep total under 60k where possible.
EXTRA_FILES = [
    # "Forge_flow.md",          # if gate logic is central
    # "Ethical_Constraints.md", # if ethics cross-ref needed
    # "Energy.md",              # if energy claims are central
    # "Forge_Net.md",           # if network dependency is central
    # "Gate_02_Triage.md",      # if handoff to triage is relevant
    # "Components.md",          # if component taxonomy is relevant
    # "Discovery.md",           # for orientation audits / new agents
]

# ── STEP 4: Set document status ───────────────────────────────────
DOC_STATUS = "Exploration"

# ── FRAMING LINE ──────────────────────────────────────────────────
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


# ─────────────────────────────────────────────────────────────────────
# CELL 3 — Fetch files
# ─────────────────────────────────────────────────────────────────────

print("Fetching files...\n")

# Always load: audit kit + target document
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

# Warn if any fetch failed
failed = [f for f, c in fetched.items() if c.startswith("[FETCH FAILED")]
if failed:
    print(f"\n⚠ FETCH FAILURES ({len(failed)}):")
    for f in failed:
        print(f"  - {f}")
    print("  Audit kit or target file failure will compromise the audit.")
    print("  Verify file exists in repository before proceeding.")


# ─────────────────────────────────────────────────────────────────────
# CELL 4 — Assemble prompt
# ─────────────────────────────────────────────────────────────────────

DIVIDER = "=" * 60

sections = []

# Role declaration
sections.append(
    f"Operating as Skeptic/Auditor per Auditor_Protocols.md v0.5\n"
    f"Repository: LazarusForgeV0"
)

# Assumption extraction (Rule 6 compliance)
sections.append(
    f"ASSUMPTION EXTRACTION (Rule 6):\n"
    f"Prior contributions assumed:\n"
    f"- {TARGET_FILE} is classified as {DOC_STATUS}\n"
    f"- Forge_Audit_Kit.md contains the active Fallacy Checklist, Verification Gates,\n"
    f"  AI Contribution Rules, and condensed Unknowns Registry\n"
    f"- Repository uses folder-based structure: Admin/, Architecture/, Operations/, Tests/\n"
    f"- Rename Registry in Discovery.md maps legacy filenames to current canonical paths\n"
    f"- Full reference files: Admin/Auditor_Protocols.md | Unknowns.md\n"
    f"These assumptions are carried forward unless contradicted by new findings."
)

# Task
sections.append(
    f"TASK:\n"
    f"Audit {TARGET_FILE} (status: {DOC_STATUS}).\n\n"
    f"Apply the full Fallacy Checklist from Forge_Audit_Kit.md.\n"
    f"Use the Verification Gates to assess promotion readiness.\n"
    f"Open with an Expiry Watch — check the Active Unknowns table for any entries\n"
    f"past two cycles before proceeding.\n\n"
    f"Audit focus:\n{FOCUS}\n\n"
    f"Label all findings: [FALLACY], [GAP], [CONTRADICTION], [UNLOGGED UNKNOWN],\n"
    f"[CROSS-REF FAILURE]. For each finding, suggest a concrete resolution path.\n\n"
    f"Cross-reference naming note: the repository uses folder-prefixed paths\n"
    f"(Admin/Ethical_Constraints.md, Operations/Energy.md). Legacy flat names\n"
    f"(Ethical_Constraints.md, energy_v0.md) are aliases. Do not flag folder-prefixed\n"
    f"paths as cross-reference failures — they are the canonical form.\n\n"
    f"End with the standard sign-off format from Forge_Audit_Kit.md."
)

# Files
file_block = f"FILES PROVIDED ({len(fetched)}):\n"
for i, (name, content) in enumerate(fetched.items(), 1):
    resolved_path = FILE_REGISTRY.get(name, name)
    file_block += f"\n{DIVIDER}\nFILE {i}: {name} (fetched from: {resolved_path})\n{DIVIDER}\n{content}\n"
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
print("In Colab: Files panel (left sidebar) -> download from there.")
print(f"\nTarget file resolved to: {FILE_REGISTRY.get(TARGET_FILE, TARGET_FILE)}")
print(f"Audit kit resolved to:   {FILE_REGISTRY.get('Forge_Audit_Kit.md', 'Admin/Forge_Audit_Kit.md')}")

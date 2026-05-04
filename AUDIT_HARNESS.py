"""
LAZARUS FORGE — AUDIT HARNESS v2
Google Colab notebook cells — paste each block into a separate cell.

USAGE:
  1. Cell 1 — run once per session (fetch helper)
  2. Cell 2 — configure your audit (edit TARGET and FOCUS only)
  3. Cell 3 — fetch files
  4. Cell 4 — assemble prompt
  5. Cell 5 — print prompt to copy
  6. Cell 6 (optional) — save prompt to file

When you hit the token limit, wait for reset, start a new Claude conversation,
paste the output from Cell 5, and add the framing line shown in Cell 2.
"""

# ─────────────────────────────────────────────────────────────────────
# CELL 1 — Fetch helper (run once per session)
# ─────────────────────────────────────────────────────────────────────

import urllib.request

BASE = "https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/"

def fetch(filename):
    url = BASE + filename
    try:
        with urllib.request.urlopen(url) as r:
            content = r.read().decode("utf-8")
        print(f"  ✓ {filename} ({len(content):,} chars)")
        return content
    except Exception as e:
        print(f"  ✗ {filename} — FAILED: {e}")
        return f"[FETCH FAILED: {filename}]"

print("Fetch helper ready.")


# ─────────────────────────────────────────────────────────────────────
# CELL 2 — CONFIGURE THIS CELL (edit TARGET_FILE and FOCUS only)
# ─────────────────────────────────────────────────────────────────────

# ── STEP 1: Set the file you are auditing ──────────────────────────
TARGET_FILE = "Components.md"

# ── STEP 2: Set the audit focus (1-3 sentences) ───────────────────
# What should the auditor pay particular attention to?
FOCUS = """
Audit for consistency with Component_Triage_System.md taxonomy and gate logic.
Check for Lifecycle Truncation (Fallacy #8) — does the taxonomy describe only
working-state components, or does it account for degraded, failed, and end-of-life paths?
Note any findings relevant to UNK-012 (gate logic determinism) or UNK-024 (forge duty threshold).
""".strip()

# ── STEP 3: Add extra context files if needed ─────────────────────
# Forge_Audit_Kit.md is always loaded automatically.
# Add files here ONLY when the audit needs extra context beyond the kit.
# Each file adds ~5-10k chars. Keep total under 50k where possible.
EXTRA_FILES = [
    # "Component_Triage_System.md",   # uncomment if auditing taxonomy consistency
    # "Lazarus_forge_v0_flow.md",     # uncomment if gate logic is central
    # "Ethical_Constraints.md",       # uncomment if ethics cross-ref needed
    # "energy_v0.md",                 # uncomment if energy claims are central
    # "Trajectories_LF.md",           # uncomment if scope questions arise
    # "leviathan_testing.md",         # uncomment if Leviathan relevance flagged
]

# ── STEP 4: Set document status ───────────────────────────────────
# Options: "Exploration" | "Draft" | "Specification"
DOC_STATUS = "Exploration"

# ── FRAMING LINE ──────────────────────────────────────────────────
# Copy this line and paste it at the TOP of the Claude conversation
# before pasting the prompt from Cell 5.
FRAMING_LINE = (
    f'"{TARGET_FILE}" is currently classified as {DOC_STATUS}. '
    f"Audit for promotion blockers and consistency with the repository standard. "
    f"Do not apply specification-level pressure to intentionally incomplete content."
)

print(f"Target:  {TARGET_FILE}")
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
    fetched[f] = fetch(f)
    total_chars += len(fetched[f])

print(f"\nDone. {len(fetched)} file(s) loaded.")
print(f"Total chars: {total_chars:,} (~{total_chars // 4:,} tokens estimated)")

if total_chars > 60000:
    print("\n⚠  WARNING: Approaching token ceiling. Consider removing an EXTRA_FILE.")
elif total_chars > 40000:
    print("\n→  Moderate load. Should be fine for most free-tier sessions.")
else:
    print("\n✓  Light load. Room to spare.")


# ─────────────────────────────────────────────────────────────────────
# CELL 4 — Assemble prompt
# ─────────────────────────────────────────────────────────────────────

DIVIDER = "=" * 60

sections = []

# Role declaration
sections.append(
    f"Operating as Skeptic/Auditor per Auditor_Protocols.md v0.4\n"
    f"Repository: LazarusForgeV0"
)

# Assumption extraction (Rule 6 compliance)
sections.append(
    f"ASSUMPTION EXTRACTION (Rule 6):\n"
    f"Prior contributions assumed:\n"
    f"- {TARGET_FILE} is classified as {DOC_STATUS}\n"
    f"- Forge_Audit_Kit.md contains the active Fallacy Checklist, Verification Gates,\n"
    f"  AI Contribution Rules, and condensed Unknowns Registry (v0.8)\n"
    f"- Full reference files: Auditor_Protocols.md | Unknowns_LF.md\n"
    f"These assumptions are carried forward unless contradicted by new findings."
)

# Task
sections.append(
    f"TASK:\n"
    f"Audit {TARGET_FILE} (status: {DOC_STATUS}).\n\n"
    f"Apply the full Fallacy Checklist from Forge_Audit_Kit.md.\n"
    f"Use the Verification Gates to assess promotion readiness.\n"
    f"Open with an Expiry Watch — check the Active Unknowns table for any entries\n"
    f"  past two cycles before proceeding.\n\n"
    f"Audit focus:\n{FOCUS}\n\n"
    f"Label all findings: [FALLACY], [GAP], [CONTRADICTION], [UNLOGGED UNKNOWN],\n"
    f"[CROSS-REF FAILURE]. For each finding, suggest a concrete resolution path.\n"
    f"End with the standard sign-off format from Forge_Audit_Kit.md."
)

# Files
file_block = f"FILES PROVIDED ({len(fetched)}):\n"
for i, (name, content) in enumerate(fetched.items(), 1):
    file_block += f"\n{DIVIDER}\nFILE {i}: {name}\n{DIVIDER}\n{content}\n"
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

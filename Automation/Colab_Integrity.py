import sys, subprocess, os

# --- Colab_Launcher_IntegrityCheck.py ---
# Rename Automation/Integrity_Check.py -> Automation/integrity_check.py
# on GitHub FIRST — same case-sensitivity issue AUDIT_HARNESS.PY had.
# This launcher will fail with ModuleNotFoundError until that's done.

result = subprocess.run(
    ["git", "clone", "-q", "https://github.com/ksarith/LazarusForgeV0.git", "/content/LazarusForgeV0"],
    capture_output=True, text=True
)
if result.returncode != 0 and "already exists" not in result.stderr:
    print("CLONE FAILED:", result.stderr)
    raise SystemExit(1)

sys.path.append('/content/LazarusForgeV0/Automation')
from integrity_check import run, print_summary

report = run("/content/LazarusForgeV0")
print_summary(report)

# Optional: write full structured JSON alongside the summary
with open("/content/integrity_report.json", "w") as f:
    import json
    json.dump(report, f, indent=2)
print("\nFull report: /content/integrity_report.json — Files panel (left sidebar) to download.")

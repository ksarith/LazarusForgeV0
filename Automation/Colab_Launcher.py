import sys, subprocess

result = subprocess.run(
    ["git", "clone", "-q", "https://github.com/ksarith/LazarusForgeV0.git", "/content/LazarusForgeV0"],
    capture_output=True, text=True
)
if result.returncode != 0 and "already exists" not in result.stderr:
    print("CLONE FAILED:", result.stderr)
    raise SystemExit(1)

sys.path.append('/content/LazarusForgeV0/Automation')
from AUDIT_HARNESS import run_audit

result = run_audit(
    target_file="Governance_Charter.md",
    focus="Standard audit. Apply full fallacy checklist and verification gates.",
    extra_files=[],
    doc_status="Exploration",
)

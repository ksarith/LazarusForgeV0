import sys, subprocess, json

result = subprocess.run(
    ["git", "clone", "-q", "https://github.com/ksarith/LazarusForgeV0.git", "/content/LazarusForgeV0"],
    capture_output=True, text=True
)
if result.returncode != 0 and "already exists" not in result.stderr:
    print("CLONE FAILED:", result.stderr)
    raise SystemExit(1)

sys.path.append('/content/LazarusForgeV0/Automation')
from cold_session_bundler import ColdSessionBundler

bundler = ColdSessionBundler("/content/LazarusForgeV0")
bundle = bundler.bundle(["Admin/Auditor_Protocols.md"])  # target file(s), explicit

print("=== MANIFEST (keep for your own records — never paste this to the auditor) ===")
print(json.dumps(bundle.manifest(), indent=2))

payload = bundle.render()
with open("/content/cold_session_payload.txt", "w") as f:
    f.write(payload)
print(f"\nPayload: {len(payload):,} chars — written to /content/cold_session_payload.txt")
print("Download via Files panel. Paste the ENTIRE file as the very first message")
print("to a brand-new chat session — nothing else before or after it, no framing of your own.")



=== MANIFEST (keep for your own records — never paste this to the auditor) ===
{
  "tool": "cold_session_bundler",
  "tool_version": "0.1",
  "created_at": "2026-07-23T10:47:53.094946Z",
  "target_files": [
    "Admin/Auditor_Protocols.md"
  ],
  "included": [
    {
      "file_path": "Admin/Auditor_Protocols.md",
      "raw_sha256": "eabbb7993240e848dbac2b112b6521523e67520d3cd2d8ad7e3b75eca025e413",
      "raw_char_count": 90285,
      "included_char_count": 88837,
      "stripped_block_count": 1,
      "stripped": [
        {
          "reason": "tracker metadata table (Status/Risk/Priority/history) \u2014 pre-judged framing, not doctrine",
          "line": 6,
          "char_count": 1435
        }
      ]
    }
  ],
  "excluded": [],
  "guarantees_true_independence": false
}

Payload: 89,340 chars — written to /content/cold_session_payload.txt
Download via Files panel. Paste the ENTIRE file as the very first message
to a brand-new chat session — nothing else before or after it, no framing of your own.

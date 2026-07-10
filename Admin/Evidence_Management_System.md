# Evidence_Management_System.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field              | Value |
|--------------------|-------|
| Status             | Resolved — Discharge via Merge into `Admin/Verification_Gates_LF.md` |
| Version            | v0.3 (final) |
| Body Stability     | Transitional |
| Spec Gates         | 0/6 |
| Verification Ref   | `Admin/Verification_Gates_LF.md` |
| Ethical Anchor     | Attempt to do no harm. Defer to `Admin/Ethical_Constraints.md` if present. |
| Highest Risk       | This file's proposed architecture is mistaken for adopted doctrine and referenced by `Admin/AUDIT_HARNESS.py` or any live promotion logic before EMS-001/EMS-002 are resolved. |
| Last Audit         | 2026-07-09 (creation); revised 2026-07-10 (multi-agent review round integrated) |
| Auditor            | Gemini, ChatGPT, Grok — original proposal, iterative refinement, and 2026-07-10 review pass (external contributions, human-relayed); Claude — Skeptic/Auditor, vulnerability hardening, structural correction, and revision integration, 2026-07-09/10 |
| Open Unknowns      | 2 (EMS-001, EMS-002) |
| Active Disputes    | 0 |
| Pending Ratification | 1 (this entire file — see Status) |
| Sidecar Link       | #auditor-notes--unknowns |

---

## Scope Boundary

**This file DOES define:**
- A proposed 7-dimensional maturity vector model as an alternative or complement to the existing Spec Gates system — **not yet adopted**.
- Proposed schemas for a decoupled Claims / Evidence / Computed-Maturity architecture.
- A hardened reference implementation correcting three identified scoring vulnerabilities.
- The open structural questions that must be resolved before any of this becomes operative.

**This file DOES NOT define (and must not be treated as defining until ratified):**
- Any change to `Admin/Verification_Gates_LF.md`'s six-gate Spec Gates system, which remains the sole live promotion mechanism.
- Any change to `Admin/AUDIT_HARNESS.py`'s actual behavior — nothing in this file is wired into the harness.
- A resolution to GOV-008 (`Admin/Governance_Charter.md`) — GOV-008 is Minimum hardware and agent quorum for bootstrap compliance, an unrelated question. See EMS-002; this file's telemetry-binding concept was misattributed to GOV-008 across all three originating agent drafts and has been corrected here.
- Constitutional or Tier 1 doctrine of any kind.

---

## File Purpose

Three external agents (Gemini, ChatGPT, Grok), working with the human governing authority across a single extended exchange, independently converged on and iteratively refined a proposal for grounding this repository's maturity/promotion claims in structured, evidence-backed, computationally-derived scores rather than self-reported or directly-edited values. The core insight — that claims and evidence should be decoupled so that no agent can inflate its own maturity score by editing a field — is genuinely good and consistent with this repository's existing doctrine (`Challenges/Return_To_Eden.md`'s Eden Index, the weakest-link logic already implicit in Dependency Clusters throughout `Unknowns.md`).

However, the proposal as developed also: (a) misattributed its core physical-grounding problem to an existing unknown ID (GOV-008) that means something else entirely, (b) never resolved its relationship to the repository's actual live promotion mechanism (Spec Gates), and (c) was gaining implementation momentum — "let's just build the harness" — inside the same thread that produced it, without a ratification checkpoint.

This file exists to preserve the genuine architectural work — including the three real scoring vulnerabilities identified and hardened during the exchange — in a proper, addressable location, at Exploration status, explicitly not wired into anything live, pending human governing authority ratification of its two open structural questions.

**Honest v0 acknowledgment:** Nothing in this file has been implemented. `Admin/AUDIT_HARNESS.py` does not read, execute, or reference any schema or function below. Treat all code in this file as a preserved proposal, not a running system.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|----|------------|-------|------------|-----------------|
| ASM-EMS-001 | The Claims/Evidence/Computed-Maturity decoupling pattern is architecturally sound and worth preserving regardless of implementation timeline | Consistent with Eden Index and existing weakest-link promotion logic already present elsewhere in the repository | High | A structural flaw in the decoupling pattern itself is identified |
| ASM-EMS-002 | A vector representation (7 independent dimensions) is preferable to a tensor representation for this repository's current maturity, per Claude's cross-review of Gemini's NT-009 observation | Tensor math would substantially complicate `AUDIT_HARNESS.py` relative to the repository's v0 scale and single-contributor bandwidth | Medium | Repository scale or contributor bandwidth changes materially |
| ASM-EMS-003 | Human governing authority ratification is required before any part of this file becomes operative, following the same pattern as ENV-DS-001 and the Embedded Value Preservation principle | Established repository pattern for drafted-but-unratified doctrine | High | Explicit ratification decision recorded in Resolution Log |

---

## Body

### 1. The Core Problem This Addresses

Prior to this proposal, nothing in the repository's architecture prevented a maturity or confidence score from being a directly-editable field — a claim asserting its own truth. The proposal's central move is to make maturity a **computed, read-only property**, derived by `AUDIT_HARNESS.py` from an append-only evidence ledger, rather than a value any agent or human can simply set. This is the same self-authorization concern `Admin/Repository_Integrity_Protocol.md` names for Resolution Logs and Tier 1 Axiom text, applied to a new surface: numeric maturity claims.

---

### 2. The Proposed 7-Dimensional Maturity Vector

Rather than a single scalar maturity value, each claim ("Concept Node") would carry seven independently-scored dimensions:

| Dimension | Meaning |
|-----------|---------|
| `m_phys` | Direct physical sensor telemetry / hardware testing evidence |
| `m_exp` | Empirical replication across independent test cycles |
| `m_math` | Theoretical, bounding-equation, and analytical verification |
| `m_eng` | CAD/BOM/fabrication-tolerance completeness |
| `m_gov` | Integrity, compliance, and signature validity |
| `m_ops` | Field deployment durability — **time-decaying**, not permanent |
| `m_rep` | Reproducibility — distinguishes "worked once" from "works reliably" |

**Aggregation is conservative minimum, not average:**

```
m_effective = min(m_phys, m_exp, m_math, m_eng, m_gov, m_ops, m_rep)
```

This is the single most important design choice in the proposal, and it fits existing repository philosophy precisely: a perfectly-modeled reactor that has never been built should not receive a high maturity score because its mathematics are elegant. This mirrors the "weakest verified dependency governs promotion" pattern already implicit throughout `Unknowns.md`'s Dependency Clusters (e.g., CE-003 gating all hot pyrolysis regardless of how mature any other prerequisite is).

`m_rep` (reproducibility) was Gemini's addition in the second iteration and is a genuine improvement over the first draft — it separately penalizes an isolated success (`m_phys` high, `m_rep` low) from a demonstrated stable process (both high), which a single scalar or even a 6-dimension vector without it would conflate.

---

### 3. Architecture: Claims, Evidence, and Computed Maturity as Distinct Objects

The proposal's second core move, refined by ChatGPT: strict separation into three layers, with information flowing one direction only.

```
Concept Node (claims — human/agent-authored)
        │
        │  points to, never sets
        ▼
Evidence Ledger (pointers to evidence records)
        │
        │  parsed by
        ▼
AUDIT_HARNESS.py (the only writer of computed_state)
        │
        │  injects, read-only from the node's perspective
        ▼
Computed Maturity Vector
```

A Concept Node may only ever *submit evidence*. It cannot write `m_phys = 0.85` directly — no manifest, telemetry binding, or node edit is permitted to set a vector dimension by assignment. The harness alone computes and injects `compiled_state`. This is the fix for the exact failure mode Repository_Integrity_Protocol.md's Constitutional-violation ladder exists to prevent, applied here to a lower-stakes but still real self-authorization surface.

### 3a. Evidence, Trust, and Integrity Are Distinct Properties

Added 2026-07-10, per Gemini's review of v0.1. The original draft treated cryptographic signatures largely as a single "governance" bucket. Three separable questions were being conflated:

| Property | Question It Answers | Where It Lives |
|----------|----------------------|-----------------|
| **Evidence** | Did the experiment produce this result? | `empirical_data`, `validation_criteria` |
| **Trust** | Who produced this record, and are they authorized to? | `provenance.operator_or_agent`, `provenance.hardware_signature` |
| **Integrity** | Has this record changed since it was recorded? | Would require append-only enforcement / hash comparison — not yet specified; see `Admin/Repository_Integrity_Protocol.md`'s own Phase 2/3 dependency for the pattern this would follow |

`m_gov`'s deduction checklist (§5c, §6) currently scores Trust and a partial proxy for Integrity (signature presence) but has no mechanism for true Integrity verification (detecting a record was altered post-hoc) at this file's current maturity. That gap is inherited from Repository_Integrity_Protocol.md's own honest v0 acknowledgment — full Integrity verification depends on the same Phase 3 cryptographic tooling RIP.md is itself waiting on.

---

### 4. Proposed Schemas (unadopted — preserved for reference)

#### 4a. Concept Node Schema (preferred draft — evidence-ledger form, v1.1)

This is the corrected, adopted-if-ratified draft. An earlier draft (§4c, below) allowed direct `maturity_vector` field edits and is preserved only for historical contrast — it reintroduces the self-authorization problem this whole proposal exists to close, and should not be used.

```yaml
---
id: "node_fa_001_fluid_stratification"
type: "Concept"
version: "0.1.3"
title: "Thermal Fluid Stratification Bounds"

# Claims require backing evidence objects. The engine parses these to compute the vector.
evidence_ledger:
  mathematical:
    - "proof_fa001_navier_stratification_v1.json"
  engineering:
    - "cad_fa001_manifold_rev3.json"
  physical:
    - "run_log_leviathan_2026_07_09_14.json"
    - "run_log_leviathan_2026_07_09_15.json"
  operational:
    - "field_report_node_fa001_alpha_run.json"

# Read-only block calculated and injected strictly by AUDIT_HARNESS.py
compiled_state:
  last_audit_timestamp: "2026-07-09T16:45:00Z"
  scoring_algorithm:
    id: "EMS-Score-v2"    # Added 2026-07-10 per Gemini review — ties every
                          # computed score to the algorithm version that
                          # produced it, so a future scoring revision doesn't
                          # silently reinterpret historical maturity values
  calculated_vector:
    m_phys: 0.85
    m_exp: 0.70
    m_math: 0.95
    m_eng: 0.90
    m_gov: 1.00
    m_ops: 0.45  # Subject to active temporal decay
    m_rep: 0.66  # Based on 2/3 successful consecutive trials
  m_effective: 0.45
---
```

#### 4b. Evidence Record Schema (Physical)

Every piece of physical or experimental evidence carries its own error margins, calibration state, and provenance. No evidence record may express uncertainty as free text — see §5a for why.

```json
{
  "$schema": "https://raw.githubusercontent.com/ksarith/LazarusForgeV0/main/Admin/Schemas/evidence_record.json",
  "evidence_id": "run_log_leviathan_2026_07_09_14",
  "target_node_id": "node_fa_001_fluid_stratification",
  "timestamp": "2026-07-09T14:22:18Z",
  "provenance": {
    "environment": "RIG-LEVIATHAN-01",
    "operator_or_agent": "agent_gemini_auditor_v1",
    "hardware_signature": "0x3c9a...88ff"
  },
  "instrumentation_metadata": {
    "sensor_id": "THERMOCOUPLE-K-042",
    "last_calibration_date": "2026-05-12",
    "estimated_sensor_drift_per_annum_pct": 0.4,
    "systemic_confidence_interval_pct": 95.0
  },
  "empirical_data": {
    "target_metric": "thermal_equilibrium_temperature",
    "observed_value": 417.0,
    "absolute_uncertainty": 2.0,
    "unit": "C",
    "duration_held_seconds": 3600
  },
  "validation_criteria": {
    "expected_range": "410C to 425C",
    "outcome": "PASS"
  },
  "reproducibility_context": {
    "trial_series_id": "SERIES-PYRO-04",
    "sequence_number": 1,
    "total_consecutive_passes_in_series": 1
  }
}
```

Note: `observed_value`, `absolute_uncertainty`, and `estimated_sensor_drift_per_annum_pct` are all numeric fields, not embedded in free-text strings — this correction is required throughout; see §5a. (The drift field was still string-typed as of v0.1 — an inconsistency with §5a's own rule, caught in the 2026-07-10 review round and corrected here.)

#### 4c. Rejected precursor — Concept Node with directly-editable `maturity_vector` (Grok, first draft)

Preserved only to document why it was superseded. **Do not implement.** This schema lets any editor set `m_phys: 0.85` etc. directly in front-matter, which is the exact self-authorization vulnerability the evidence-ledger form in §4a exists to close.

```yaml
---
id: "node_fa_001_fluid_stratification"
type: "Concept"
maturity_vector:
  m_phys: 0.00
  m_exp: 0.40
  m_math: 0.90
  m_eng: 0.75
  m_gov: 1.00
  m_ops: 0.00
aggregation:
  method: "MINIMUM"
  calculated_m_effective: 0.00
signature: "0x8f2c...9be3"
---
```

---

### 5. Three Scoring Vulnerabilities Identified and Hardened

During review, three specific exploitable weaknesses were found in earlier drafts of the scoring logic (documented here because the *pattern* of each vulnerability is instructive beyond this specific proposal — they are variants of exploits this repository should watch for anywhere a score is computed from text).

#### 5a. The String-Matching Telemetry Exploit

**Vulnerable code:** `score = 0.85 if "±2" in unc or "95%" in conf else 0.65`

**The flaw:** Brittle substring matching. An uncertainty string like `"±200°C (Not ±2°C)"` or a confidence value like `"0.95% Confident"` would accidentally trigger the highest score tier via naive substring containment.

**The fix:** Ban free-text numeric limits entirely. Evidence records must separate the scalar value from an explicit numeric `absolute_uncertainty` field (§4b). Scoring compares floats, never scans strings for patterns.

#### 5b. The Survivorship-Bias Reproducibility Flaw

**Vulnerable code:** `m_rep = min(1.0, 0.4 * math.log2(passed_runs + 1))`

**The flaw:** Counts only successes. A rig that runs 50 times, fails 45, and passes 5 would score `m_rep` at its cap of 1.0 — a 90% failure rate produces a perfect reproducibility score, because the formula never sees the 45 failures.

**The fix:** `m_rep` must be a **stability ratio** (`passed_runs / total_runs_attempted`) multiplied against the logarithmic volume scale, not the volume scale alone. See §6 for the corrected function.

#### 5c. The Hollow-Governance Auto-Pass

**Vulnerable code:** `if node_metadata.get("signature") and ledger: m_gov = 1.0`

**The flaw:** Grants a perfect governance score merely because a signature *string exists* — no verification that the signature matches the payload, no check that evidence records themselves passed schema validation.

**The fix:** `m_gov` starts at 1.0 and is strictly *degraded* by an explicit deduction checklist (unsigned node, unverified evidence signatures, etc.) — never auto-granted by presence alone.

#### 5d. Negative Evidence Is Not the Same as No Evidence (added 2026-07-10, per Gemini review)

The v0.1 draft did not distinguish two states that currently collapse to similar low scores but mean very different things:

- **No evidence** — no experiment has been run. The claim is simply untested.
- **Negative evidence** — an experiment was run and it failed, or produced a result outside `validation_criteria.expected_range`.

Both currently drag `m_phys`/`m_exp` toward zero in §6's implementation, which is directionally correct for aggregation purposes but loses information a human reviewer would want: "nobody has checked this yet" and "we checked and it doesn't hold" warrant different next actions. A failed run should remain a first-class, retained evidence record (not discarded or treated as a null result) — the reference implementation already does this correctly by requiring every attempted run to appear in `physical_refs` regardless of outcome (§5b's stability-ratio fix depends on failed runs being counted, not dropped). What's still missing is a way to *surface* that distinction to a reader of `compiled_state`, rather than only to the scoring math. Left as an open refinement for whichever revision resolves EMS-001, rather than resolved here — this is a display/reporting question, not a scoring-correctness one, so it doesn't block ratification the way EMS-001/002 do.

Related, deferred further: contradictory evidence (Run A passes, Run B fails, Run C passes on the same claim) is handled correctly by the stability-ratio math but the document doesn't yet discuss what that pattern means for repository knowledge beyond the score itself. Noted for a future revision, not v0.2.

---

### 6. Hardened Reference Implementation (preserved, unexecuted)

This is the corrected function incorporating all three fixes from §5. It is preserved here as a reference for any future ratified implementation — **it is not called anywhere in `Admin/AUDIT_HARNESS.py` and has no live effect.**

```python
import math
import datetime
from typing import Dict, Any, Tuple

def calculate_maturity_from_evidence_v2(
    node_metadata: Dict[str, Any],
    evidence_vault: Dict[str, Any],
    lambda_decay: float = 0.05,
    current_time: datetime.datetime = None
) -> Tuple[Dict[str, float], float]:

    if current_time is None:
        current_time = datetime.datetime.utcnow()

    # Base state before verification processing
    computed = {
        "m_phys": 0.0, "m_exp": 0.0, "m_math": 0.0,
        "m_eng": 0.0, "m_gov": 1.0, "m_ops": 0.0, "m_rep": 0.0
    }

    ledger = node_metadata.get("evidence_ledger", {})

    # 1. MATHEMATICAL & ENGINEERING
    if ledger.get("mathematical"):
        computed["m_math"] = 0.95  # Standard proof schema ceiling
    if ledger.get("engineering"):
        computed["m_eng"] = 0.90   # Standard complete CAD/BOM ceiling

    # 2. PHYSICAL & EXPERIMENTAL
    physical_refs = ledger.get("physical", [])
    total_runs_attempted = len(physical_refs)
    passed_runs = 0
    max_phys_score = 0.0

    for ref in physical_refs:
        run = evidence_vault.get(ref)
        if not run:
            continue

        # Every attempted run must be recorded; count passes strictly
        if run.get("validation_criteria", {}).get("outcome") == "PASS":
            passed_runs += 1

            # Robust Uncertainty Evaluation (No string matching — fixes 5a)
            empirical = run.get("empirical_data", {})
            val = float(empirical.get("observed_value", 0.0))
            abs_unc = float(empirical.get("absolute_uncertainty", float('inf')))

            relative_precision = abs_unc / val if val != 0 else float('inf')

            if relative_precision <= 0.005:    # Highly precise (<= 0.5% error)
                run_score = 0.90
            elif relative_precision <= 0.02:   # Standard precision (<= 2% error)
                run_score = 0.75
            else:                              # Loose tolerances
                run_score = 0.50

            # Degrade score further if instrumentation drift is high
            # (numeric field per §5a fix — no string parsing)
            drift_val = float(run.get("instrumentation_metadata", {}).get(
                "estimated_sensor_drift_per_annum_pct", 0.0))
            if drift_val > 1.0:
                run_score *= 0.8

            max_phys_score = max(max_phys_score, run_score)

    computed["m_phys"] = max_phys_score

    if total_runs_attempted > 0:
        computed["m_exp"] = 0.90 * (passed_runs / total_runs_attempted)

    # 3. REPRODUCIBILITY (stability-ratio-aware — fixes 5b)
    if passed_runs > 0 and total_runs_attempted > 0:
        stability_ratio = passed_runs / total_runs_attempted
        volume_scale = min(1.0, 0.4 * math.log2(passed_runs + 1))
        computed["m_rep"] = round(stability_ratio * volume_scale, 2)

    # 4. OPERATIONAL DECAY
    ops_reports = ledger.get("operational", [])
    if ops_reports:
        latest = evidence_vault.get(ops_reports[-1])
        if latest:
            ts_str = latest.get("timestamp", "").replace("Z", "+00:00")
            evidence_time = datetime.datetime.fromisoformat(ts_str)
            delta_days = (current_time - evidence_time).days

            base_ops = 0.90
            computed["m_ops"] = round(base_ops * math.exp(-lambda_decay * delta_days), 2)

    # 5. GOVERNANCE INTEGRITY (deduction-based — fixes 5c)
    if not node_metadata.get("signature"):
        computed["m_gov"] -= 0.50  # Node is unsigned

    for ref in physical_refs + ops_reports:
        run = evidence_vault.get(ref)
        if run and not run.get("provenance", {}).get("hardware_signature"):
            computed["m_gov"] -= 0.10  # Evidence trace lacks cryptographic proof

    computed["m_gov"] = max(0.0, computed["m_gov"])

    # 6. CONSERVATIVE AGGREGATION GATE
    m_effective = min(computed.values())

    return computed, m_effective


def load_evidence_vault(vault_dir: str) -> Dict[str, Dict]:
    """Simple filesystem vault loader — the repo's own Git history is the
    distributed store; no external database required at v0 scale."""
    import json
    from pathlib import Path
    vault = {}
    for p in Path(vault_dir).glob("**/*.json"):
        try:
            with open(p) as f:
                data = json.load(f)
                vault[data.get("evidence_id") or p.stem] = data
        except Exception:
            continue  # TODO if ratified: log warning rather than silently skip
    return vault
```

---

### 7. The Three-Tier Framing (narrative context, not adopted mechanism)

One contributing agent (Grok) framed `Admin/Repository_Integrity_Protocol.md`'s Phase 0 / Phase 1 / Phase 2+ structure as a "three-tier defense-in-depth" model — Phase 0 as a cognitive anchor against silent forgetting between disconnected agent sessions, Phase 1 as a structural validator against informational drift, Phase 2+ as a cryptographic substrate firewall against tampering.

This is useful *descriptive* language for explaining RIP.md's existing structure to a new thread or contributor, and is preserved here for that purpose. It is not a new mechanism, does not modify RIP.md itself, and should not be read as implying RIP.md's Phase 0 constitutes more automation or enforcement strength than RIP.md's own v0.7 text already claims — see RIP.md's Drift Indicator explicitly guarding against Phase 0 being described as "automation."

**A related claim from the same exchange — that the repository has "crossed its own Systemic Autonomy Threshold (R > 1)" — is not adopted and is assessed as unsupported.** What has been demonstrated is multi-agent semantic persistence and cross-session continuity via an external ledger (Reddit). What has not been demonstrated is autonomous self-governance: humans are still selecting revisions, resolving disputes, and approving ratifications throughout this repository's actual history. The more accurate framing, per this session's own review: *"The repository demonstrates cross-agent semantic persistence; autonomous governance remains a future objective."*

---

## Upstream/Downstream

**Upstream (would constrain this file, if ratified):**
- `Admin/Verification_Gates_LF.md` — relationship undefined; see EMS-001
- `Admin/Governance_Charter.md` — Tier 1 Axioms would remain the ethical floor for any computed score
- `Admin/Repository_Integrity_Protocol.md` — self-authorization prevention doctrine this proposal extends into a new surface

**Downstream (would depend on this file, if ratified):**
- `Admin/AUDIT_HARNESS.py` — would be the sole execution and injection point; currently has zero references to anything in this file
- Any future physical test rigs (`Tests/Leviathan_testing.md`, `Tests/Support_Raft.md`) — would be evidence *sources*, never direct maturity writers

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|-----------------|--------------|--------------------|------------|----------------------|
| 2026-07-09 | Audit Review | Three independent agent drafts all cited GOV-008 for the physical-telemetry-binding problem | GOV-008 is actually about bootstrap quorum, an unrelated question — none of the three agents checked the ID against source before building on it | Convergence across multiple agents is not confirmation of correctness — it can mean one agent's error propagated into the others' context rather than three independent verifications agreeing. Always check a cited ID against source text directly, regardless of how many agents agree on it. | Internally Derived | No |
| 2026-07-09 | Audit Review | Building implementation momentum ("let's draft the production-ready harness") within the same thread that produced an unratified architectural proposal | No ratification checkpoint existed between "this is a good idea" and "let's start building it" | Genuinely good architecture still needs the same drafted-then-held pattern as any other major doctrine change, especially when the proposing agents have momentum — the risk isn't the idea's quality, it's skipping the checkpoint | Internally Derived | No |
| 2026-07-10 | Audit Review | Three agents reviewing v0.1 independently converged quickly on "feed vector into Spec Gates, don't replace" as the safer EMS-001 path | Not itself a failure — Grok's independent Path 2/3 alternatives showed real divergent thinking, unlike the earlier GOV-008 echo — but fast multi-agent agreement is exactly the pattern that produced GOV-008's error, so it still warranted a deliberate check rather than being taken as confirmation by volume | The same scrutiny this file applies to its own subject matter (convergence ≠ correctness) needs to be applied to reviews *of* this file too, not just to the proposal's original content | Internally Derived | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|------------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|-----------------|---------------|
| 2026-07-09 | Tensor-based multi-dimensional maturity representation | A vector of 7 independent scalar dimensions captures the same "maturity isn't one number" insight (originally surfaced via Nothingness Theorem's NT-009) without the implementation complexity tensor math would add relative to this repository's v0 scale and single-contributor bandwidth | Yes — if repository scale or contributor bandwidth changes materially |
| 2026-07-09 | Directly-editable `maturity_vector` node schema (§4c) | Reintroduces the exact self-authorization vulnerability the evidence-ledger architecture exists to close | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Any function or schema in this file referenced by `Admin/AUDIT_HARNESS.py` before EMS-001 and EMS-002 are resolved and this file is ratified
- GOV-008 cited anywhere in this repository as the source of the telemetry-binding problem described here, rather than its actual definition (bootstrap quorum)
- The rejected §4c schema (directly-editable `maturity_vector`) implemented anywhere, reintroducing the self-authorization vulnerability
- This file's Status advanced beyond Exploration without an explicit human governing authority ratification entry in the Resolution Log
- The §7 "Systemic Autonomy Threshold" framing adopted as a repository claim rather than treated as an assessed-and-rejected characterization

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### EMS-001 — Relationship to Verification_Gates_LF.md's Spec Gates system undefined

| Field | Value |
|-------|-------|
| Status | Resolved — Discharge via Merge |
| Risk | High |
| Priority | Critical |
| Type | Governance / Architectural |
| Blocking | Yes (for any implementation work on this proposal) |
| Owner | `Admin/Evidence_Management_System.md` |
| First Logged | 2026-07-09 |
| Last Reviewed | 2026-07-10 |

**Description:** This proposal's 7-dimensional maturity vector and MIN aggregation is a parallel structure to `Admin/Verification_Gates_LF.md`'s six-gate Spec Gates system, which is the repository's actual live promotion mechanism. Whether the vector should replace Spec Gates, feed into them as an input, or run entirely alongside them for physical-evidence tracking specifically has not been decided.

**Candidate paths, per 2026-07-10 review round (Grok):**
1. **Input Pipeline** — the vector feeds specific Spec Gates as quantitative backing (e.g., a gate requiring empirical grounding could require `m_phys ≥ 0.75` and `m_rep ≥ 0.50`). Spec Gates remain the sole live promotion mechanism; the vector becomes a structured input to some of them. Lowest structural risk, fully reversible.
2. **Structural Replacement** — the vector replaces the 0/6 Spec Gates system entirely across every governed file's File State table. Highest structural risk: every file in the repository currently references `Admin/Verification_Gates_LF.md` by name in its Verification Ref field, so this path's propagation scope is comparable to or larger than CT-010's rename sweep.
3. **Physical-Domain Sandbox** — the vector applies only to Architecture/ and Operations/ files; Admin/ and governance-tier files continue using Spec Gates unmodified. Splits the repository into two promotion regimes by file domain.

**2026-07-10 update:** Human governing authority has indicated an initial leaning toward integration/replacement (Path 2 direction) rather than Path 1's narrower feed-in model, and intends to review `Admin/Verification_Gates_LF.md` directly in an upcoming session. **This unknown cannot close, and no path should be finalized, until that review happens** — this file's own drafting has proceeded entirely from *references to* Verification_Gates_LF.md in other files, never from its actual Scope Boundary, gate definitions, or body text. Status moved from Open to In Progress to reflect that a decision process has begun, without treating any path as selected yet.

**Why It Matters:** Building this out before deciding risks the repository ending up with two maturity systems that can disagree with each other about the same file's promotion readiness — worse than the current single, imperfect system. Given the leaning toward Path 2, the risk sharpens further: a full structural replacement decided without reading the file being replaced risks losing gate logic or Verification_Gates_LF.md-specific doctrine (e.g., any existing violation classes, promotion exceptions, or cross-references from `Admin/Repository_Integrity_Protocol.md`'s Audit Lineage checks) that isn't visible from other files' references to it alone.

**Resolution Path:** Upload/review `Admin/Verification_Gates_LF.md` directly. Map its actual gate definitions against the 7-dimensional vector concretely before ruling on which of the three paths (or a fourth, informed by what the file actually contains) is correct.

**Resolved 2026-07-10:** Reviewed against all six gate definitions directly. Overlap found with Gate 2 only — Gates 1, 3–6 have no evidence-vector overlap (fallacy checking, hazard battery, scope alignment, cross-reference resolution, textual conflict). Full structural replacement (Path 2) ruled out on this basis; a narrow Input Pipeline (Path 1), scoped to Gate 2 specifically, merged in as backing material. See `Admin/Verification_Gates_LF.md` VG-002 for the live tracking of this integration, which remains held pending `Admin/Auditor_Protocols.md` AP-021.

---

### EMS-002 — No correct ID exists for the physical-telemetry-binding problem this proposal addresses

| Field | Value |
|-------|-------|
| Status | Resolved — Discharge via Merge (moot) |
| Risk | Medium |
| Priority | Critical |
| Type | Governance / Technical |
| Blocking | Yes (for registration of any future work in this area) |
| Owner | `Admin/Evidence_Management_System.md` |
| First Logged | 2026-07-09 |
| Last Reviewed | 2026-07-09 |

**Description:** All three originating agent drafts cited GOV-008 for "the interface linking physical telemetry to maturity scores." GOV-008 is actually registered in `Unknowns.md` as "Minimum hardware and agent quorum for bootstrap compliance" — an unrelated question about bootstrap governance authority. No ID currently exists for the actual problem this file addresses.

**Why It Matters:** Continuing to informally call this "GOV-008" anywhere in future discussion would propagate a real ID collision into the repository, the same class of error CT-007 and the early CF-/CLF- collision both represent.

**Resolution Path:** If this file is ratified past Exploration, register a new ID at that time — candidate prefix `EMS-` (matching this file) or folding into `Admin/Security_Protocols.md`'s SEC- series, since the underlying question is fundamentally about hardware/telemetry trust binding. Human governing authority's call.

**Resolved 2026-07-10 (moot):** This file's content merged into `Admin/Verification_Gates_LF.md` as Gate 2 backing material rather than being ratified as an independent file. The telemetry-binding tracking now lives under that file's own VG- prefix (see VG-002) rather than needing a new EMS- or SEC- namespace, since it's tracked as backing material for an existing gate rather than a standalone system requiring its own registration.

---

### Resolution Log

- 2026-07-10: **v0.3 (final) — Discharged via Merge into `Admin/Verification_Gates_LF.md`.** Direct review of that file's six actual gate definitions found overlap with Gate 2 only (physical plausibility / confidence labeling) — Gates 1, 3–6 test fallacious reasoning, hazard battery application, scope alignment, cross-reference resolution, and textual conflict, none of which this file's evidence vector has any mechanism to evaluate. Full structural replacement (EMS-001 Path 2) ruled out on that basis. Schemas, hardened reference implementation, and a confidence-label mapping merged into Verification_Gates_LF.md as a new "Gate 2 Evidentiary Backing" subsection, explicitly held inactive. EMS-001 and EMS-002 both resolved/mooted, superseded by that file's VG-002. This file is retained per repository convention (resolved unknowns and superseded files are not deleted) as the historical record of the original multi-agent proposal, its hardening pass, and its 2026-07-10 review round — but is no longer the live location for this work. Live tracking is now `Admin/Verification_Gates_LF.md` VG-002.

- 2026-07-10: **v0.2 — Multi-agent review round integrated.** (1) §4b/§6: `estimated_sensor_drift_per_annum` converted from string to numeric field (`estimated_sensor_drift_per_annum_pct`), fixing an inconsistency with §5a's own anti-string-matching rule that survived into v0.1's reference implementation — caught by ChatGPT's review. (2) §3a added: Evidence, Trust, and Integrity formally distinguished as separate properties, per Gemini's review — `m_gov` currently scores Evidence and Trust proxies but has no true Integrity (tamper-detection) mechanism, a gap inherited honestly from Repository_Integrity_Protocol.md's own Phase 3 dependency. (3) §4a compiled_state schema gained `scoring_algorithm.id`, per Gemini's review — ties every computed score to the algorithm version that produced it. (4) §5d added: negative evidence (a failed run) distinguished from no evidence (untested), per Gemini's review — noted as a display/reporting gap, not a scoring-correctness one, and left open rather than fully resolved in this pass. (5) EMS-001 updated to In Progress: human governing authority has indicated an initial leaning toward integration/replacement (Path 2) and intends to review `Admin/Verification_Gates_LF.md` directly; the unknown explicitly cannot close until that review happens, since this file's understanding of Spec Gates has so far come only from other files' references to it. (6) New Lessons Learned entry: applying this file's own "convergence ≠ correctness" lesson to the review round that produced this revision, not only to the original proposal.
- 2026-07-09: File created (v0.1). Synthesized and preserved from an extended multi-agent exchange (Gemini, ChatGPT, Grok) proposing a 7-dimensional evidence-backed maturity vector system, hardened against three identified scoring vulnerabilities (string-matching exploit, survivorship-bias reproducibility flaw, hollow-governance auto-pass) during Claude's Skeptic/Auditor review of the exchange. Created at Exploration status, explicitly not wired into `Admin/AUDIT_HARNESS.py` or any live promotion logic. Two Critical unknowns logged (EMS-001: relationship to Spec Gates undefined; EMS-002: GOV-008 misattribution — no correct ID exists yet for the telemetry-binding problem, found independently repeated across all three originating agent drafts). The "Systemic Autonomy Threshold (R > 1)" claim from the same exchange was reviewed and not adopted — assessed as overstating what cross-agent semantic persistence actually demonstrates. Filed per the same drafted-then-held pattern as ENV-DS-001 and the Embedded Value Preservation principle (`Challenges/Closed_Loop_Feedstock.md` §2a).

---

## Relationship to Existing Documents

- `Admin/Verification_Gates_LF.md` — the existing live promotion mechanism this proposal would need to reconcile with or replace; see EMS-001
- `Admin/Governance_Charter.md` — GOV-008 is registered here as bootstrap quorum, not telemetry binding; see EMS-002
- `Admin/Repository_Integrity_Protocol.md` — the self-authorization-prevention doctrine (Resolution Logs, Tier 1 Axiom text) this proposal extends into numeric maturity claims; also the source of the Phase 0/1/2+ framing referenced descriptively in §7
- `Admin/AUDIT_HARNESS.py` — the proposed sole execution/injection point if ratified; currently has zero references to this file
- `Admin/Nothingness Theorem` — NT-009's observation (maturity/verification/epistemic-debt may be multi-dimensional rather than scalar) is the philosophical origin of §2's vector approach; this file's content has not been independently verified against Nothingness Theorem's own source text, only against the multi-agent discussion that referenced it
- `Challenges/Return_To_Eden.md` — existing precedent for a normalized multi-variable index in this repository, informing the aggregation approach here
- `Challenges/Closed_Loop_Feedstock.md` — §2a (Embedded Value Preservation) is the structural precedent this file's drafted-then-held pattern follows

---

## Status

Version 0.3 (final) — **Resolved — Discharge via Merge into `Admin/Verification_Gates_LF.md`.** Content is now live there as Gate 2 Evidentiary Backing (inactive, held pending AP-021), tracked under that file's VG-002. This file is retained as the historical record only.

**First priority action (now owned by `Admin/Verification_Gates_LF.md` VG-002):** Resolve `Admin/Auditor_Protocols.md` AP-021 (confidence-label system inconsistency), then update Gate 2's live pass criteria to require the evidentiary mapping.

**What must remain constant:**

**A good idea preserved and held is not lost. A good idea implemented before its open questions are resolved becomes a liability wearing the shape of progress.**

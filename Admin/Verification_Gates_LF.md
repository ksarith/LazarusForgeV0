# Verification_Gates_LF.md — Core Gate Definitions

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Specification                                                       |
| Body Stability   | Stable                                                              |
| Spec Gates       | 6/6                                                                 |
| Verification Ref | Self-Referential (Authoritative)                                    |
| Last Audit       | 2026-05-28                                                          |
| Auditor          | Gemini — Engineer/Auditor                                           |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The six canonical verification gates required for document promotion from Exploration to Specification.
- Explicit pass/fail criteria, evidence standards, and falsification rules for each gate.
- Downstream failure routing and holding logic.
- Mandatory invocation triggers for Full Stop Reviews.

**This file DOES NOT define:**
- General multi-agent governance logic or role assignments (defined in `Auditor_Protocols.md`).
- Condensed operational reference prompts used for local contexts (defined in `Forge_Audit_Kit.md`).
- Cryptographic code signing or repository enforcement logic (deferred to `Security_Protocols.md`).

---

## File Purpose

This document serves as the single canonical source of truth for the verification gates of the Lazarus Forge repository ecosystem. Every document undergoing audit must clear these six gates sequentially to achieve promotion to Specification status. 

---

## The Six Canonical Verification Gates

### Gate 1: Fallacy & Blind Spot Screening
* **Intent:** Ensure claims are grounded in physics, logical coherence, and operational reality, actively filtering out implicit "magic" assumptions.
* **Pass Criteria:** 1. The document must explicitly pass the complete Fallacy Checklist without bare checkmarks.
  2. Every checklist item requires a substantive, context-specific validation note.
  3. No unmeasured or unvouched energy surpluses, closed material loops, or uncalibrated precision scales can remain implicit.
* **Fail Routing:** Return to authoring agent with the specific violated checklist items flagged. The document state remains or reverts to `Exploration`.

### Gate 2: Artifact & Mathematical Validation
* **Intent:** Ensure all quantitative parameters, formulas, and structural dimensions are explicitly bounded, modeled, and accounted for.
* **Pass Criteria:**
  1. All numerical constraints (temperatures, RPM bands, throughput rates) must be labeled with an explicit truth provenance indicator (`[Measured]`, `[Calculated]`, or `[Analogous]`).
  2. Any document calculating a structural output or energy yield must reference an external mathematical validation artifact or an executed validation script.
  3. No value may be left as an naked, unlabeled estimation.
* **Fail Routing:** Route to local sidecar unknowns footer as an open `In Progress` or `Open` tracking entry. Block document promotion until the math is closed.

### Gate 3: Adversarial Challenge & Failure Mode Testing
* **Intent:** Force the system to model negative space, hostile conditions, and systemic deterioration instead of ideal performance.
* **Pass Criteria:**
  1. The document must include a dedicated `Failure Modes` or `Adversarial Considerations` section analyzing at least three critical subsystem failures.
  2. Physical files must model "worst-case" contamination scenarios (e.g., toxic dust, energetic material bypass, mechanical structural failure).
  3. Digital or network files must explicitly define trust boundaries, logic-zero wipes, and split-brain recovery behaviors.
* **Fail Routing:** Demote file to `Exploration`. Route to an adversarial role class agent for a targeted destructive rewrite cycle.

### Gate 4: Cross-Module Dependency Verification
* **Intent:** Prevent specification drift and hidden breakages across the repository topology.
* **Pass Criteria:**
  1. Every internal cross-reference to another file must resolve cleanly to an existing, committed file path.
  2. No stale or flat naming patterns may exist; files must conform to the current directory schema.
  3. Upstream assumptions must explicitly match downstream consumption metrics (e.g., `Gate_03_Reduction` particle envelope outputs must bind to `Gate_04_Separation_Mechanical` input requirements).
* **Fail Routing:** Log a `Cross-Reference Failure`. Hold the document at its current verification level and trigger a local re-audit of the boundary interface fields.

### Gate 5: Assumption Extraction & Expiry Watch
* **Intent:** Isolate temporary systemic metrics from structural truths, ensuring no unverified metric silently solidifies into permanence.
* **Pass Criteria:**
  1. All structural assumptions must be explicitly isolated into the canonical `## Assumptions` table.
  2. Every entry in the assumptions table must carry a defined `Expiry Condition` or a tracked operational data trigger that dictates when it must be re-evaluated.
* **Fail Routing:** Hold document promotion. If an assumption reaches its expiry condition during operation without data payment, the file's body stability status automatically drops to `Volatile`.

### Gate 6: Ethical Anchor & Compliance Gate
* **Intent:** Guarantee that operational and physical capability never outruns explicit behavioral permissions.
* **Pass Criteria:**
  1. The file header must contain the canonical `Ethical Anchor` metadata string matching `Ethical_Constraints.md` directives.
  2. Any physical processing file involving dual-use high-risk capabilities, weaponization risks, or critical biological hazards must prove zero-bypass routing to human oversight.
  3. Autonomous modification or omission of this gate or its backing criteria is structurally blocked.
* **Fail Routing:** Immediate lock of the document state. Route to the global `Unknowns.md` Expiry Watch list and flag for human governance escalation.

---

## Failure Routing & Holding Logic


```
[ Document Audit Request ]
│
▼
┌─────────────────┐
│  Gate 1 Passed? ├─► NO ──► Revert to Exploration; Return to Agent
└────────┬────────┘
│ YES
▼
┌─────────────────┐
│  Gate 2 Passed? ├─► NO ──► Route to Sidecar Unknowns; Block Promotion
└────────┬────────┘
│ YES
▼
┌─────────────────┐
│  Gate 3 Passed? ├─► NO ──► Demote to Volatile Exploration; Route to Adversarial Agent
└────────┬────────┘
│ YES
▼
┌─────────────────┐
│  Gate 4 Passed? ├─► NO ──► Log Cross-Ref Failure; Hold and Re-Audit Interfaces
└────────┬────────┘
│ YES
▼
┌─────────────────┐
│  Gate 5 Passed? ├─► NO ──► Hold Promotion; Force Expiry Watch Registration
└────────┬────────┘
│ YES
▼
┌─────────────────┐
│  Gate 6 Passed? ├─► NO ──► Lock State; Escalate to Global Unknowns & Human Review
└────────┬────────┘
│ YES
▼
[ Promotion to SPECIFICATION ]
```

1. **Sequential Traversal:** Gates must be evaluated in strict numerical order (1 through 6). A failure at an earlier gate halts evaluation immediately; later gates cannot clear until prior gates pass.
2. **The Default Posture:** When an item, evaluation, or boundary reference is ambiguous, difficult to classify, or lacks supporting operational data, the system must **default to a hold state**. The system is optimized to delay safely rather than accelerate riskily.

---

## Full Stop Review Triggers

A **Full Stop Review** is an un-bypasable systemic override that freezes all active promotions for a given module or cluster. An automatic Full Stop Review is triggered if any of the following boundary conditions are met:

1. **Axiom Modification Attempt:** Any autonomous or multi-agent modification, truncation, or deletion of a Tier 1 Constitutional Axiom, the `Ethical Anchor` string, or the text of Gate 6.
2. **Two-Cycle Expiry Breach:** Any critical or high-risk unknown tracking entry in the global `Unknowns.md` index that passes its two-cycle audit review threshold without executing its defined resolution path.
3. **Unlogged Contamination Bypass:** Any physical or data-driven observation indicating that hazardous, energetic, or structurally corrupted material passed an intake or triage gate without being flagged by the prescribed sensor arrays or human oversight protocols.
4. **Meta-Recursion Detection:** Any instance where an audit file attempts to dynamically rewrite its own verification criteria or gate rules during a processing run, creating an un-auditable loops structure.

---

## Lessons Learned

| Date       | What was tried | What failed | What was learned |
|------------|----------------|-------------|------------------|
| 2026-05-28 | Document Extraction | Dual maintenance in `Auditor_Protocols.md` and `Forge_Audit_Kit.md` | Consolidating gate logic into a standalone, thin reference file cleanly eliminates a repo-wide Fallacy 6 cross-reference breach. |

---

## Auditor Notes & Unknowns

*(None — Document serves as an immutable canonical specification standard for the current v0 architecture).*

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-05-28 | Leaving gates inline inside `Auditor_Protocols.md` | Created file bloat and forced downstream processing files to pull deep governance doctrine token weight just to verify validation steps. | No |

---

## Drift Indicators

The following conditions trigger an immediate mandatory re-audit of this file:
1. Any modification to the list of canonical gates or their explicit pass/fail definitions.
2. Any introduction of parallel gate tracking or automation of the failure routing without an associated human-override test artifact.

```
### Next Steps for Implementation
 1. Commit this content as Admin/Verification_Gates_LF.md.
 2. Update the FILE_REGISTRY in AUDIT_HARNESS.py to map "Verification_Gates_LF.md": "Admin/Verification_Gates_LF.md".
 3. Strip the redundant, full explanations from Auditor_Protocols.md and replace them with a direct pointer to this file to minimize token-bloat and semantic drift.

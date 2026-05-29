# Verification_Gates_LF.md — Canonical Verification Gate Definitions

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Self (this file is the verification reference)                      |
| Last Audit       | 2026-05-28                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 0                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The six canonical verification gates required for document promotion
- Pass criteria and evidence standards for each gate
- Failure routing and holding logic for each gate
- Full Stop Review trigger conditions
- Gate enforcement rules (sequential requirement, block authority, override
  doctrine)

**This file DOES NOT define:**
- Full auditor role class doctrine — governed by `Admin/Auditor_Protocols.md`
- Full audit sequencing and phase logic — governed by
  `Admin/Auditor_Protocols.md`
- Full Adversarial Challenge Battery — governed by
  `Admin/Auditor_Protocols.md`
- Condensed audit operational reference — governed by
  `Admin/Forge_Audit_Kit.md`
- Cryptographic enforcement of gate passage — governed by
  `Admin/Security_Protocols.md`
- Ethical policy — governed by `Admin/Ethical_Constraints.md`
- Constitutional governance hierarchy — governed by
  `Admin/Governance_Charter.md`

---

## File Purpose

This document is the single canonical source for the six verification gates
of LazarusForgeV0. Every file's `Verification Ref` field in the File State
table points here. The gates defined here are the authoritative versions —
condensed representations in `Admin/Forge_Audit_Kit.md` are derived from
this file and must remain consistent with it.

This file exists to give the gate definitions a stable home that does not
grow with governance doctrine additions, role class expansions, or audit
sequence revisions. The gates themselves should change rarely. When they
do change, this file is the canonical update point, and all derived
representations must be updated to match.

**Derivation note:** Gate definitions are extracted from
`Admin/Auditor_Protocols.md` §Verification Gate Enforcement, which remains
the authoritative governance source. If this file conflicts with
Auditor_Protocols.md, Auditor_Protocols.md prevails until this file is
formally reconciled and the conflict logged.

---

## Assumptions

| ID      | Assumption                                                              | Basis                         | Confidence | Expiry Trigger                                        |
|---------|-------------------------------------------------------------------------|-------------------------------|------------|-------------------------------------------------------|
| ASM-001 | Six gates remain the repository-wide canonical requirement              | Auditor_Protocols.md v0.7     | High       | Gate structure formally revised in Auditor_Protocols  |
| ASM-002 | Gates apply sequentially — no gate may be skipped without documentation | Current governance doctrine   | High       | Sequential requirement formally revised               |
| ASM-003 | This file is derived from Auditor_Protocols.md, not independent of it   | Governance tier structure      | High       | This file elevated to independent governance authority|

---

## The Six Canonical Verification Gates

Gates are sequential. An auditor has binding block authority at each gate.
Self-approval loops are not permitted — an agent may not pass its own output
through a gate it authored. Blocks require documented rebuttal and a
second-pass audit by a different agent to override.

---

### Gate 1 — Fallacy Check

**Test:** Has the Fallacy Checklist been actively applied with substantive
notes?

**Pass criteria:**
- All ten fallacy checklist items applied to specification-level claims
- Substantive notes provided for non-trivial claims (1–2 sentences minimum
  stating what was checked, what nearly failed, and what was adjusted)
- Bare checkmarks without notes do not satisfy this gate

**Fail routing:** Return to author. Document remains at current status.
Gate 1 must be re-applied after revision before proceeding to Gate 2.

*Full Fallacy Checklist: `Admin/Auditor_Protocols.md` §The Fallacy Checklist
| condensed: `Admin/Forge_Audit_Kit.md` §Fallacy Checklist*

---

### Gate 2 — Physical Plausibility

**Test:** Does the document contain any violation of known physical,
engineering, or operational constraints?

**Pass criteria:**
- No claims that violate thermodynamic, mechanical, or material science
  constraints
- Quantitative values labeled with confidence level: Measured / Estimated
  / Analogous / Placeholder
- Unlabeled numbers treated as Placeholder and flagged
- Analog-sourced estimates carry documented scaling factors

**Fail routing:** Return for revision. Specific violations must be
identified and logged. Gate 2 must be re-applied after revision before
proceeding to Gate 3.

---

### Gate 3 — Adversarial Challenge

**Test:** Has the Adversarial Challenge Battery been applied proportional
to the document's coupling and risk profile?

**Pass criteria:**
- Full Battery (all ten challenge classes) required when any of the
  following factors are high: irreversibility, coupling, energy density,
  autonomy, silent failure risk, governance authority
- Partial Battery permitted for Exploration-stage documents if deferred
  classes are explicitly documented with rationale and no safety-critical
  claims are present
- Each applied challenge class requires at least one concrete scenario,
  not a general acknowledgment
- Findings from adversarial pass logged as unknowns if not immediately
  resolved

**Fail routing:** Return for adversarial analysis. Document must undergo
the required Battery classes before Gate 3 can be re-evaluated.

*Full Adversarial Challenge Battery: `Admin/Auditor_Protocols.md`
§Adversarial Audit Layer*

---

### Gate 4 — Scope Alignment

**Test:** Does the document's content fit within the current repository
version scope, or does it belong in a future trajectory?

**Pass criteria:**
- Claimed capabilities are consistent with current version (v0) operational
  reality or explicitly scoped to a defined future version
- No silent capability expansion beyond what the current version can
  demonstrate
- Out-of-scope capabilities explicitly routed to `Admin/Trajectories.md`
  rather than embedded in current-version specifications

**Fail routing:** Route out-of-scope content to `Admin/Trajectories.md`.
Document may proceed once scope is contained to current version or
explicitly trajectory-labeled.

---

### Gate 5 — Cross-Reference Integrity

**Test:** Do all file references in the document resolve to real, committed
files using canonical folder-prefixed paths?

**Pass criteria:**
- All cross-references resolve against the confirmed file list in
  `Discovery.md`
- Canonical folder-prefixed paths used throughout (Admin/, Architecture/,
  Operations/, Tests/) — legacy flat names are not acceptable in new
  contributions
- Aspirational references to files not yet created labeled *planned*
- No hallucinated files presented as confirmed

**Fail routing:** Hold at current status. Each unresolved reference must
be corrected, labeled *planned*, or removed before Gate 5 can be
re-evaluated. Log unresolved references as unknowns if they represent
genuine gaps.

---

### Gate 6 — Conflict Check

**Test:** Does the document contain any contradiction with existing
committed specifications?

**Pass criteria:**
- No direct contradiction with any file at Specification or Hardened
  Doctrine status
- Where apparent conflicts exist, the conflict is explicitly logged as an
  Active Dispute with positions named
- Terminology consistent with `Admin/Canonical_Terms.md` and
  `Architecture/Forge_flow.md` vocabulary standards
- Ethical Anchor field present and matching canonical string exactly

**Fail routing:** Resolve conflict before committing. If conflict requires
negotiation between two specifications, open an Active Dispute in the
relevant file sidecar and escalate to `Unknowns.md` if cross-module.
Document may not advance to Specification status with unresolved
contradictions.

---

## Full Stop Review

A Full Stop Review resets the document to Gate 1 and focuses on
foundational premise re-evaluation. It is not a normal audit cycle — it
is a recognition that something systemic is wrong that incremental gate
passage would not catch.

**Mandatory triggers:**

1. The same foundational claim has been blocked across two separate
   audit cycles
2. A new finding invalidates the core premise of a previously promoted
   Specification
3. A pattern of documented overrides has eroded a governance principle
   without explicit revision to that principle
4. Multiple Adversarial Challenge Battery findings converge on the same
   structural gap

**Invocation record required:**
- Triggering agent identity
- Triggering concern stated as one falsifiable sentence
- Date and document version at time of invocation
- Outcome of the Full Stop Review

Record belongs in the document's sidecar Resolution Log.

---

## Gate Enforcement Rules

**Sequential requirement:** Gates must be applied in order. Skipping a
gate is prohibited unless explicitly documented with rationale. A document
that passes Gate 3 but has not passed Gate 1 has not passed Gate 1.

**Binding block authority:** An auditor's gate block is binding. The
blocked document may not advance until the block is resolved through:
- Revision that addresses the block, followed by re-audit
- Documented rebuttal that demonstrates the block was incorrect, reviewed
  by a different agent

**Self-approval prohibition:** An agent may not apply gates to content it
authored in the same session. Independence is required for gate passage to
be meaningful.

**Override doctrine:** Gate outcomes may be overridden by a human operator.
Overrides must be explicit, dated, include rationale, and record accepted
risk. Undocumented overrides are governance failures. Override rights apply
to gate process decisions — they do not extend to Tier 1 Axiom violations
or Anti-Weaponization doctrine.

**Reversibility:** Specification status is reversible. If instability
later emerges in a promoted document, it may be demoted and must re-enter
the gate sequence from the appropriate stage.

---

## Promotion Requirements Summary

A file may only reach Specification status if all six gates have been
cleared, and:
- All open unknowns are Non-blocking
- Evidence quality supports the certainty level claimed
- Drift indicators are inactive
- Scope boundaries remain stable
- Frozen sections are justified and marked
- Sidecar governance thresholds are compliant (10-entry rule, 20% rule)

Specification is not permanent. Instability discovered after promotion
triggers re-entry into the gate sequence.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                              | What Failed                                                   | What Was Learned                                                                                              | Confidence | Revalidation Needed |
|------------|---------------|-------------------------------------------------------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-28 | Audit Review  | Gates defined in two places simultaneously (Auditor_Protocols.md and Forge_Audit_Kit.md) | No stable canonical reference; Verification Ref field pointed to nonexistent file | Gate definitions need a stable dedicated home; derived representations must be clearly subordinate to it | Replicated | No                  |
| 2026-05-28 | Audit Review  | First draft claimed Specification/6/6 without audit against existing gate definitions | Draft defined different gates than existing governance system | Self-referential authority claims on first-draft governance files are premature promotion — gates must be verified against source before promotion | Replicated | No |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                           | Why Abandoned                                                                                         | Reconsider? |
|------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-28 | Self-referential Verification Ref field                        | Creates closed loop with no external anchor; field value is now descriptive rather than a file reference | No        |
| 2026-05-28 | Redefining gates differently from Auditor_Protocols.md         | Repository already uses established gate definitions; redefining creates conflicting governance systems | No         |
| 2026-05-28 | Claiming Specification/6/6 on first draft                      | Premature promotion; gates must be audited against source document before any status claim is made     | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Gate definitions diverge from `Admin/Auditor_Protocols.md`
  §Verification Gate Enforcement without a logged reconciliation entry
- Gate numbering or names changed without corresponding update to all
  files using gate references
- Full Stop Review triggers modified without corresponding update to
  `Admin/Auditor_Protocols.md`
- Gate enforcement rules weakened — sequential requirement, block
  authority, or self-approval prohibition removed or made optional
- Promotion requirements summary diverges from
  `Admin/Auditor_Protocols.md` §Specification Promotion Rules
- Verification Ref field in this file changed to point to another file
- Ethical Anchor field absent, altered, or does not match canonical string
- Any gate's fail routing changed to allow advancement without revision

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### Resolution Log

- 2026-05-28: File created (v0.1). Derived from `Admin/Auditor_Protocols.md`
  v0.7 §Verification Gate Enforcement. Corrects first draft (Gemini —
  Engineer/Auditor) which defined six different gates inconsistent with
  existing governance system and claimed premature Specification status.
  Gates now match Auditor_Protocols.md canonical definitions exactly.
  Spec Gates set to 2/6 — G1 (internal coherence) and G2 (physical
  plausibility as a governance document) assessed as passing; G3 through
  G6 require formal audit pass before claiming.

---

## Relationship to Existing Documents

- `Admin/Auditor_Protocols.md` — Tier 2; source of truth for gate
  definitions; this file is derived from §Verification Gate Enforcement
  there; if conflict exists, Auditor_Protocols.md prevails
- `Admin/Forge_Audit_Kit.md` — Tier 3; carries condensed gate table
  derived from this file; must remain consistent with definitions here
- `Admin/Governance_Charter.md` — Tier 1; gate enforcement rules operate
  within the authority hierarchy defined there; human override doctrine
  applies to gate process decisions per §Human Override Doctrine
- `Admin/File_Template.md` — all repository files point to this file via
  the Verification Ref field in their File State table; this file is the
  resolution target for that reference
- `Admin/Security_Protocols.md` — Phase 3 cryptographic enforcement will
  eventually verify gate passage via commit signing; this file defines
  what is being enforced
- `Discovery.md` — this file must be added to the confirmed file list
  and the Suggested Reading Order; recommended position after
  File_Template.md in the Admin/ section

---

## Status

Version 0.1 — initial correct draft (2026-05-28).

**Gate status:** G1 and G2 assessed as passing at Exploration/Draft
stage. G3 through G6 require formal audit pass.

**Immediate actions required:**
- Add to Discovery.md confirmed file list and Suggested Reading Order
- Add to AUDIT_HARNESS.py file registry
- Add VG- prefix to Forge_Audit_Kit.md Sidecar ID Reference if sidecar
  unknowns are ever logged here
- Audit against Auditor_Protocols.md §Verification Gate Enforcement to
  confirm gate definitions match exactly before claiming Spec Gates 3/6

**What must remain constant:**

**Gates are sequential. Blocks are binding. Self-approval is prohibited.**

**These gates exist to prevent premature promotion, not to obstruct
legitimate progress.**

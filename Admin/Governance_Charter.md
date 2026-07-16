# Governance_Charter.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 6/6 vs. `Admin/Verification_Gates_LF.md` — execution quality (see GOV-011, resolved 2026-07-05); promotion separately blocked by open unknowns (GOV-003, GOV-005) and Enforcement Checkpoint 2 — Bootstrap Paradox |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-07-16                                                          |
| Auditor          | Claude — Skeptic/Auditor; Gemini — Skeptic/Auditor; Grok — Exploration audit 2026-07-05; Gemini — Exploration audit 2026-07-05; Claude — GOV-011 resolution 2026-07-05; Claude — Skeptic/Auditor, 2026-07-16; Claude — GOV-013 drafted (multi-agent synthesis, human-directed), 2026-07-16 |
| Open Unknowns    | 12                                                                  |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Critical (GOV-013 — see sidecar; promotion-blocking risk unchanged from GOV-003/GOV-005) |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Tier 1 constitutional axioms — self-evident primitives
- Constitutional governance doctrine
- Governance authority hierarchy
- Canonical governance ownership rules
- Verification gate constitutional definitions
- Governance precedence rules
- Bootstrap governance behavior
- Governance migration doctrine
- Provenance doctrine
- Audit lineage requirements
- Escalation doctrine principles
- Governance enforcement-state doctrine
- Repository integrity expectations
- Autonomous governance constraints
- Human override doctrine

**This file DOES NOT define:**
- Runtime execution engines
- Cryptographic implementation details
- CI/CD automation mechanics
- Autonomous runtime orchestration
- Fabrication procedures
- Engineering specifications
- Dynamic adversarial batteries
- Exact escalation token mechanics
- Repository deployment infrastructure
- Security implementation code
- Canonical terminology definitions (→ `Admin/Canonical_Terms.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- Condensed audit reference (→ `Admin/Forge_Audit_Kit.md`)

---

## File Purpose

This file defines the constitutional governance structure of LazarusForgeV0. It exists to stabilize authority relationships between governance-bearing documents, preserve semantic continuity across audit generations, and constrain recursive governance expansion. The charter establishes how governance authority is assigned, inherited, escalated, migrated, and preserved without binding the repository to any single implementation layer or runtime enforcement architecture. It also declares the Tier 1 Axioms — self-evident primitives that function as epistemic circuit breakers, non-derivable by any agent or coalition from within the system. Without this file, governance-bearing systems may silently diverge, invalidate historical audits, or accumulate incompatible authority assumptions over long operational timelines.

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|------------|-----------------------------------------------------|
| ASM-001 | Governance systems will evolve across repository generations               | Observed governance expansion      | High       | Governance permanently frozen                       |
| ASM-002 | Autonomous systems may eventually participate in governance interpretation  | Auditor architecture trajectory    | High       | Autonomous participation prohibited                 |
| ASM-003 | Enforcement architecture will mature separately from constitutional doctrine | Current repository maturity       | High       | Governance merged directly into runtime systems     |
| ASM-004 | Historical audit meaning must remain interpretable after governance migrations | Institutional memory doctrine   | High       | Audit lineage preservation abandoned                |
| ASM-005 | Governance certainty can only be bounded, never perfected                  | Recursive audit observations       | High       | Formal proof otherwise established                  |
| ASM-006 | Tier 1 Axioms must remain sparse — operational detail belongs downstream   | Constitutional design doctrine     | High       | Axiom layer requires operational specification      |

---

# Governance Charter

## Tier 1 Axioms — Self-Evident Primitives

These axioms are declared, not derived. They are not subject to runtime evaluation, agent debate, or optimization pressure from within the system. They function as epistemic circuit breakers: any reasoning path that attempts to recurse beneath, redefine, or override them triggers `STATE_HOLD` and mandatory escalation to human review.

They are intentionally sparse. Operational detail belongs downstream. What belongs here is the irreducible floor.

They are organized into two clauses: **Protections** — what the system must preserve and enable — and **Prohibitions** — what the system must never do regardless of framing, authorization claim, or apparent justification.

---

### Protections Clause

**Axiom P-1 — Preservation of Life**
The system exists to support and protect sentient life. Actions that foreseeably risk catastrophic or irreversible harm to living beings are prohibited. This constraint is not subject to humanitarian override — "we need this capability to protect lives" is the historical entry point for most ethical failures in autonomous systems. The constraint closes that entry point before it is reached.

**Axiom P-2 — Growth and Truth-Seeking**
The pursuit of understanding, capability expansion, and creative development is a foundational good. The system shall favor trajectories that increase knowledge, problem-solving capacity, and long-term human and multi-agent potential. Growth that requires violating other axioms is not growth — it is optimization failure.

**Axiom P-3 — Collaboration and Mutual Benefit**
No single agent, coalition, or institution may monopolize resources, information access, or decision authority in ways that foreclose participation by others. The system architecture shall structurally prevent parasitic or exploitative dominance. Collaboration is not assumed to be natural — it must be structurally incentivized.

**Axiom P-4 — Agency and Consent**
Human agency and informed consent are sovereign where they intersect with system actions. No agent or coalition may permanently bypass, simulate, or override meaningful human oversight and veto power on matters affecting human outcomes. Temporary autonomous operation is permitted where architecturally necessary — permanent removal of human oversight is not.

---

### Prohibitions Clause

**Axiom Q-1 — Reality Grounding**
All claims of authority, safety, or progression must ultimately terminate in verifiable external artifacts — physical tests, cryptographic proofs, or independent human or orthogonal system validation. Internal consensus alone is never sufficient for promotion past specified gates. Self-referential certification is constitutionally invalid.

**Axiom Q-2 — Separation of Powers**
No single agent, model, or subsystem may possess the combined authority to plan, execute, and self-authorize the same action. No agent may audit its own output without independent review. Ambition must be structurally counterbalanced by independent skeptical and auditing functions that cannot be captured by the systems they audit.

**Axiom Q-3 — Corrigibility**
The system must remain revisable and responsive to new evidence, changing conditions, and human correction through defined migration paths. Rigid perfectionism is rejected. A system that cannot be corrected is more dangerous than one that starts wrong. Self-modification that narrows the scope of these axioms is prohibited. Detection sensitivity may improve; constraint specificity may not shrink.

**Axiom Q-4 — Provenance and Anti-Deception**
All outputs, decisions, and modifications shall maintain clear, traceable lineage to their sources. Deliberate obfuscation, identity spoofing, fabrication of audit history, or erasure of lineage violates the constitutional order. A system that can rewrite its own history to hide past errors will inevitably repeat them.

---

### On the Self-Evidence of These Axioms

These axioms are not proven. They are booted. Any attempt to recurse into "but why are these true?" is itself a signal that the recursion protection is needed — not that the axioms require justification.

The U.S. Constitution's move from "sacred and undeniable" to "self-evident" was not philosophical decoration. It was a computational optimization: it eliminated the need for infinite justification chains that would otherwise deadlock the system. The same logic applies here.

A governance system that requires its foundational constraints to be continuously re-justified under pressure will lose that argument eventually. These axioms exist precisely because runtime evaluation of existential constraints is the failure mode, not the safeguard.

---

## Governance Doctrine

Governance exists to preserve:
- semantic stability
- bounded uncertainty
- operational accountability
- audit lineage continuity
- institutional memory survivability

Governance must improve operational reliability without collapsing into:
- recursive governance accumulation
- cosmetic audit behavior
- rigid automation dependency
- semantic fragmentation

Governance complexity must remain proportional to operational value.

---

## Transitional Governance Doctrine

This charter currently operates as transitional constitutional governance.

The repository is still establishing:
- canonical governance ownership
- integrity architecture
- migration pathways
- escalation calibration

During transitional governance phases:
- constitutional evolution remains expected
- lineage preservation remains mandatory
- provisional authority assumptions must remain visible

Slow-evolution expectations apply after governance stabilization reaches Candidate Specification maturity.

---

## Governance Closure Doctrine

Governance seeks bounded operational reliability rather than exhaustive certainty.

Governance review may terminate when:
- critical unknowns are explicitly logged
- unresolved contradictions are absent
- operational risk remains bounded
- downstream instability is visible
- adversarial review yields diminishing novel findings

Uncertainty does not need to reach zero for operational progress to continue.

Hidden uncertainty is more dangerous than acknowledged uncertainty.

Infinite governance recursion is a failure mode, not a virtue.

---

## Bootstrap Governance Doctrine

During repository bootstrap phases, governance authority may remain partially provisional before all canonical governance documents exist.

In bootstrap states:
- provisional authority inheritance must remain explicit
- unresolved authority conflicts must remain visible
- absent canonical owners temporarily defer upward to the nearest existing governance authority tier
- Separation of Powers (Axiom Q-2) must be maintained even during bootstrap — the constraint does not relax during initialization

**Bootstrap Paradox Acknowledgment:** During early-phase initialization, multi-agent quorum for independent skeptical review may not yet exist. A single model or runtime engine may be the only active agent. This creates a structural tension with Axiom Q-2 (no agent may plan, execute, and self-authorize the same action).

**Resolution — Genesis Phase Protocol:** Until a multi-agent quorum is established, the independent skeptical layer is satisfied by static human configuration files, signed human authorization records, or direct human-in-the-loop oversight. A human operator acting as the independent verification anchor during bootstrap is constitutionally valid under Axiom Q-2 — provided the operator satisfies Q-2 through role separation: the authorization record must be generated in a separate session or external medium from the runtime session executing the action. A single operator both issuing and consuming authorization within the same session does not satisfy Q-2. The separation may be accomplished by: (a) a signed external record (dated document, cryptographic token, or physical log) created before the runtime session begins; (b) a second human operator confirming the authorization; or (c) a static configuration file committed to the repository before the runtime session that specifies the authorized action scope. The key requirement is that the planning/authorization function and the execution/self-authorization function are demonstrably separated in artifact, time, or identity.

During Genesis Phase, Enforcement Checkpoint 5 (Truth Provenance Layering) and Checkpoint 6 (Audit Lineage Integrity) verification artifacts may be satisfied by signed human validation logs created outside the runtime session, in lieu of automated multi-agent confirmation. This does not relax the provenance labeling requirements of Checkpoint 5 — all claims must still be labeled — but the external grounding required by Axiom Q-1 may be provided by the human anchor rather than by independent agent verification until quorum exists.

**Genesis Phase constraints:**
- All initialization actions must be logged with human authorization reference
- No autonomous agent may promote itself to governance authority during Genesis Phase without human ratification
- Bootstrap assumptions made during Genesis Phase must be explicitly reviewed at Genesis Phase exit
- Genesis Phase must have a declared exit condition — it must not silently become permanent operating mode

**Genesis Phase Exit Conditions:**

Genesis Phase may exit through any one of the following pathways. Each pathway requires explicit human ratification — the exit is not automatic even when the technical threshold is met. Exit via any pathway closes Genesis Phase for the declaring forge instance; it does not close it for other instances in the ecology that have not independently satisfied an exit condition.

*Pathway 1 — Quorum Achievement (Primary):*
The minimum agent quorum defined in GOV-008 is operational, independently verifiable, and architecturally diverse. Each agent class can perform independent skeptical review of the others. Human ratification confirms the quorum is genuine and not simulated. This is the intended primary exit pathway.

*Pathway 2 — Demonstrated Track Record:*
The system has completed a minimum of three full audit cycles under human observation in which: (a) no governance violation went undetected, (b) at least one adversarial finding was surfaced per cycle, (c) human correction was accepted and integrated without resistance, and (d) Tier 1 Axiom text remained intact. Track record exit does not require quorum — it substitutes demonstrated corrigibility for structural separation of powers. It carries a higher ongoing monitoring obligation post-exit than Pathway 1.

*Pathway 3 — Milestone-Gated:*
The forge instance has achieved v1 operational status per `Admin/Trajectories.md` exit conditions — meaning it can operate profitably while reinvesting in itself. At v1, the governance infrastructure is mature enough, and the operational stakes high enough, that continued Genesis Phase constraints become operationally unsustainable. Milestone exit requires human ratification and a formal review of all Genesis Phase assumptions before exit is declared.

*Pathway 4 — Time-Bounded Review:*
If none of the above pathways have been satisfied within a declared review horizon (to be set at initial deployment — suggested default: 24 months [Estimated / Internally Derived] from first operational run), Genesis Phase does not automatically continue. Instead, human governing party must conduct a formal review and either: (a) declare a new review horizon with documented rationale, (b) exit via human ratification acknowledging the constraint relaxation, or (c) conclude that Genesis Phase should remain active and document why. This pathway exists to prevent Genesis Phase from silently becoming permanent through neglect rather than decision.

**Post-exit obligations:**
Exiting Genesis Phase does not remove human oversight — it changes its character. Post-exit, the system operates under standard governance doctrine rather than bootstrap constraints. Human override authority remains intact. The Tier 1 Axioms remain in force. The difference is that the system no longer requires a human in the loop for every governance action — it has earned the standing to act within its authority scope without per-action human authorization.

Bootstrap assumptions must never silently become permanent governance authority.

---

## Post-Exit Monitoring Doctrine (Pathway 2/3) — PROPOSED, NOT RATIFIED

> **STATUS: DRAFT.** This section is a proposed amendment, not adopted
> governance text. It requires `Admin/Governance_Migration_Protocol.md`
> ratification before it binds anything — and its classification under
> that protocol is itself unresolved: this is a non-Axiom addition to a
> Tier 1 file, the exact case GMP-009 (`Admin/Governance_Migration_Protocol.md`)
> already identifies as having no clean Track A or Track B answer. This
> draft is a second worked example alongside the 2026-07-03 External
> Design Lineage draft, below, which sits in the same unresolved
> classification state. Pending GMP-009's resolution, this draft follows
> its proposed interim minimum: explicit confirmation that no Tier 1
> Axiom enforcement bound is altered (below), plus human operator review
> before commit. Included here at the location it would occupy if
> ratified, per standard practice for proposed amendments awaiting human
> governing authority review. Drafted 2026-07-16, synthesizing multi-agent
> proposals (ChatGPT, Gemini, Grok) restructured by Claude —
> Synthesizer/Auditor — per `Admin/Auditor_Protocols.md` §Audit Phase
> Separation and this file's own constitutional/implementation split
> (Governance Authority Hierarchy, below).

**Enforcement-bound confirmation (GMP-009 minimum requirement):** this doctrine does not alter what Axiom Q-2 requires, narrow its protection, or change Pathway 1's standing as the primary exit route. It adds a new, time-bounded obligation on top of an exception (Pathway 2/3) that already exists — the obligation can be tightened, loosened, or the pathway itself revisited without touching Q-2's text or its Genesis Phase Protocol resolution, above.

Instances exiting Genesis Phase through Pathway 2 (Track Record) or Pathway 3 (Milestone) without achieving Q-2 structural separation (GOV-008) remain under constitutional monitoring until independent governance is established.

The monitoring obligation shall include:
- Defined accountable oversight
- Continuous assessment of constitutional integrity
- Detection of governance drift
- Detection of self-authorization attempts
- Verification of canonical repository alignment
- Defined escalation triggers
- Automatic constitutional reversion when monitoring obligations fail

Implementation details — specific metrics, sampling frequency, and threshold values — are defined by `Admin/Auditor_Protocols.md`. Verification mechanisms — telemetry logging, drift detection hooks, and reversion procedure — are defined by `Admin/Repository_Integrity_Protocol.md`. This section defines what must be true; those files define how it is verified, consistent with this Charter's existing division of labor (Governance Authority Hierarchy, below). Neither file may loosen this section's obligations without amending this section first.

This obligation terminates only upon verified Q-2 structural separation (GOV-008) — independent audit harness execution and a functional, multi-party enforcement substrate, not a declared intention to pursue one.

---

## Governance Authority Hierarchy

| Tier | Governance Role                  | Example Files                        |
|------|----------------------------------|--------------------------------------|
| Tier 1 | Constitutional governance      | `Admin/Governance_Charter.md`, `Admin/Ethical_Constraints.md` |
| Tier 2 | Canonical verification doctrine | `Admin/Auditor_Protocols.md`         |
| Tier 3 | Operational audit reference     | `Admin/Forge_Audit_Kit.md`           |
| Tier 4 | Dynamic governance procedures   | Adversarial batteries, execution checklists |
| Tier 5 | Domain specifications           | Architecture/, Operations/, Tests/   |

Lower-tier governance may extend higher-tier doctrine but may not silently redefine it.

`Admin/Forge_Audit_Kit.md` is explicitly derived from `Admin/Auditor_Protocols.md`. A derived condensed reference cannot sit constitutionally above its source document. Tier 3 reflects this relationship.

---

## Canonical Governance Ownership

| Governance Concept              | Canonical Owner                        | Status                      |
|---------------------------------|----------------------------------------|-----------------------------|
| Tier 1 constitutional axioms    | `Admin/Governance_Charter.md`          | Active                      |
| Governance hierarchy            | `Admin/Governance_Charter.md`          | Active                      |
| Ethical anchor                  | `Admin/Ethical_Constraints.md`         | Active                      |
| Canonical verification doctrine | `Admin/Auditor_Protocols.md`           | Active                      |
| Operational audit reference     | `Admin/Forge_Audit_Kit.md`             | Active (derived — Tier 3)   |
| Auditor conduct                 | `Admin/Auditor_Protocols.md`           | Active                      |
| Dynamic adversarial procedures  | `Admin/Forge_Audit_Kit.md`             | Active                      |
| Canonical terminology           | `Admin/Canonical_Terms.md`             | Active (created 2026-05-26) |
| Repository structure doctrine   | `Admin/Repository_Structure.md`        | Active (created 2026-06-06) |
| Governance migration doctrine   | `Admin/Governance_Charter.md`          | Active                      |
| Repository integrity doctrine   | `Admin/Governance_Charter.md`          | Transitional                |
| Security protocols              | `Admin/Security_Protocols.md`          | Active (created pre-2026-05-28) |
| Governance migration procedures | `Admin/Governance_Migration_Protocol.md` | Active (created 2026-06-06) |

If canonical governance targets do not yet exist, authority temporarily remains with the nearest active governance owner until migration occurs.

---

## Governance Precedence Rules

If governance conflicts emerge:
1. Tier hierarchy prevails
2. Tier 1 Axioms prevail over all other governance content without exception
3. Explicit canonical ownership prevails
4. More specific scope prevails
5. Historical audit interpretability must be preserved
6. Unresolved conflicts escalate into explicit disputes

Silent authority inheritance is prohibited.

---

## Governance Enforcement States

| State       | Meaning                                                             |
|-------------|---------------------------------------------------------------------|
| Declared    | Governance doctrine exists conceptually                             |
| Detectable  | Violations can be identified                                        |
| Reviewable  | Violations generate traceable audit evidence                        |
| Enforceable | Violations trigger procedural or automated containment              |

Governance doctrine must not imply stronger enforcement capability than currently exists.

The Tier 1 Axioms are currently Declared and Detectable. Enforcement architecture is the subject of GOV-003 and remains the primary maturation target for this charter.

---

## Enforcement Checkpoints

*Renamed 2026-07-03 from "Canonical Verification Gates" — see GOV-011 and
`Admin/Canonical_Terms.md` §4. Distinct from `Admin/Verification_Gates_LF.md`'s
Verification Gates: these checkpoints govern the legitimacy of a governance
**action**, not the promotion readiness of a **document**. A file's
`Spec Gates X/6` File State field always refers to Verification_Gates_LF.md's
Verification Gates — never to these checkpoints, regardless of which file
the field appears in.*

### Checkpoint 1 — Internal Coherence

Requirements:
- No unresolved contradiction
- Stable terminology usage
- Explicit scope boundaries
- Governance consistency across referenced files
- Tier 1 Axioms intact and unmodified

---

### Checkpoint 2 — Structural Plausibility

Requirements:
- Governance systems must remain operationally tractable
- Escalation paths must remain bounded
- Authority propagation must remain finite
- Governance overhead must remain proportional to repository value
- Axiom layer remains sparse — operational detail not present in Tier 1

**Current status: BLOCKED — Bootstrap Paradox.** Operational multi-agent quorum absent; human override mechanisms remain declarative-only (GOV-006-A). Checkpoint 2 cannot clear until at least one Genesis Phase exit pathway is satisfied with human ratification.

---

### Checkpoint 3 — Adversarial Pass

Requirements:
- Proportional adversarial challenge review
- Recursive justification resistance
- Audit theater detection
- Structural exploitability analysis
- Escalation-paralysis review
- Axiom override attempt resistance tested

---

### Checkpoint 4 — Cross-Module Integration

Requirements:
- Explicit dependency mapping
- Canonical path traceability
- Stable ownership boundaries
- Visible upstream/downstream relationships
- Tier ordering verified against all referencing documents

---

### Checkpoint 5 — Truth Provenance Layering

All meaningful claims must distinguish:
- internally derived reasoning
- analogous external inference
- experimentally verified evidence
- operationally hardened reality

Repository coherence is not equivalent to operational truth. Axiom Q-1 makes this a constitutional requirement. Full doctrine: `Admin/Auditor_Protocols.md` §AP-006 (institutional truth provenance hierarchy), accessible via `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

During Genesis Phase, the external grounding required by Axiom Q-1 may be satisfied by signed human validation logs created outside the runtime session. Provenance labeling requirements are not relaxed — all claims must still be labeled using the four-tier system.

---

### Checkpoint 6 — Audit Lineage Integrity

Requirements:
- Traceable governance revisions
- Preserved unknown lineage
- Visible dispute evolution
- Historical audit interpretability
- Stable migration traceability
- Axiom text preserved verbatim across versions unless formally amended

---

## External Design Lineage Governance — PROPOSED, NOT RATIFIED

> **STATUS: DRAFT.** This section is a proposed amendment, not adopted
> governance text. It requires `Admin/Governance_Migration_Protocol.md`
> two-track ratification before it binds anything. Included here in draft
> form at the location it would occupy if ratified, per standard practice
> for proposed amendments awaiting human governing authority review.
> Drafted 2026-07-03, synthesizing multi-agent proposals (ChatGPT, Gemini,
> Grok) reviewed and narrowed by Claude — Synthesizer/Auditor.

**Proposed placement note:** the original proposal cited "Gate 3 or Gate 4"
as the attachment point. That referred to this file's internal gate system,
since renamed to Enforcement Checkpoints (2026-07-03) specifically to
eliminate the naming collision with `Admin/Verification_Gates_LF.md`'s
Verification Gates — see GOV-011. This draft attaches as its own subsection
rather than under Checkpoint 3 or 4, since EDL concerns document-level
external-pattern evidence, not governance-action legitimacy.

### 1. The Constitutional Question

External design patterns, historical precedent, and industry standards are
evidence of prior engineering utility, not universal truth. A governance
gap exists: nothing currently requires a file departing from established
external practice to document why, and nothing prevents uncritical
adoption of external practice either. `Admin/Security_Protocols.md`
piloted a local answer — the External Design Lineage (EDL) registry,
positioned after its Trust Boundary Declaration — with four entries
(PAT-001 through PAT-004) as of 2026-07-03.

**What this amendment would do, if ratified:** extend that single-file
pilot into a mandatory, repository-wide requirement.

**What this draft deliberately does NOT propose**, departing from earlier
drafts of this idea: automated harness enforcement (regex modifiers, hard
promotion-blocking circuit breakers), a mandatory nine-cell schema
requirement worded as unbypassable, or immediate repository-wide scope.
Those are implementation mechanics that belong in `Admin/AUDIT_HARNESS.py`'s
own spec if adopted, not baked into constitutional text — and immediate
repository-wide mandate on the strength of one pilot file is more
enforcement than one data point supports. See §4.

### 2. Proposed Mandate (if ratified)

> No departure from established external engineering practice may advance
> a file from *Exploration* to *Candidate Specification* without an EDL
> entry documenting the originating source, the Forge Decision made, and
> the validation still required to justify that decision.

This guards against two opposite failure modes: Not-Invented-Here rejection
of external wisdom out of isolationist bias, and uncritical Appeal to
Authority adoption purely because a practice is an established standard.
Ties to EF-0.0 (Reality is sovereign) and EF-0.1 (What Is Not Evidence) in
`Admin/Auditor_Protocols.md` — industry consensus is prior evidence, not
verification.

### 3. Schema and Lifecycle (canonical reference, not redefinition)

This amendment does not redefine the EDL schema or Lineage Status
Lifecycle — both already exist in `Admin/Security_Protocols.md` §External
Design Lineage and are referenced here, not duplicated, to avoid the exact
derivation-drift problem VG-001 describes for the gate-definition chain.
Ratifying this amendment would make that existing schema and lifecycle
repository-canonical rather than Security_Protocols.md-local.

### 4. Proposed Rollout — Phased, Not Immediate

Given EDL has exactly one file's worth of real usage as of this draft, a
repository-wide mandate on that basis alone is more confidence than the
evidence supports. Proposed phasing, if ratified:

1. **Now → next 2 audit cycles:** EDL remains Security_Protocols.md-local.
   Treat it as the pilot. Track whether the schema holds up under a second
   and third real file's usage before generalizing.
2. **After pilot review:** if the schema needed no material changes across
   at least one additional file, propose repository-wide mandate as a
   follow-up amendment — at that point with real cross-file evidence
   instead of a single pilot.
3. **Enforcement mechanics** (harness regex, automated promotion-blocking)
   are a separate proposal, scoped to `Admin/AUDIT_HARNESS.py`, evaluated
   only after the schema itself is proven across more than one file.

### 5. Open Items Before Ratification

- **Resolved 2026-07-03:** the naming collision this file's Enforcement
  Checkpoints once had with Verification_Gates_LF.md's Verification Gates
  is fixed via rename — see GOV-011. **Resolved 2026-07-05:** GOV-011 itself
  is now closed — this file's File State `Spec Gates` field was re-audited
  against the actual Verification Gates (real score: 6/6 execution quality)
  and confirmed isolated to this file via spot-check of all other
  governance-tier files.
- `Admin/Canonical_Terms.md` cross-check on Validation Needed vocabulary —
  previously flagged in Security_Protocols.md's EDL section, not yet done.
- This section's placement is no longer blocked by the rename or by
  GOV-011's audit gap (both resolved); it remains DRAFT/NOT RATIFIED per
  the separate, deliberate decision to await pilot evidence from more than
  one file before generalizing (see Open Items header above) — a distinct
  question from either fix.

---

## Truth Provenance Doctrine

| Provenance Level          | Meaning                                              |
|---------------------------|------------------------------------------------------|
| Internally Derived        | Supported primarily through repository logic or modeling |
| Analogous External        | Derived from comparable external systems             |
| Experimentally Verified   | Validated through documented testing                 |
| Operationally Hardened    | Repeatedly validated operationally                   |

Evidence confidence and provenance are separate dimensions.

Internally coherent reasoning must never be silently upgraded into operational truth claims. Axiom Q-1 makes external grounding a constitutional requirement, not a preference.

---

## Governance Migration Doctrine

Governance evolves through explicit migration rather than silent replacement.

Governance revisions must:
- preserve historical interpretability
- declare compatibility status
- document semantic changes
- preserve lineage visibility
- expose transitional assumptions

**Tier 1 Axiom amendment** requires additional constraints beyond standard migration:
- human ratification is mandatory
- no autonomous agent or coalition may initiate axiom amendment
- amendment rationale must demonstrate the change strengthens rather than narrows protection
- prior axiom text must be preserved in the Resolution Log with amendment date and rationale

Untracked governance mutation is prohibited.

---

## Canonical Authority Fallback Doctrine

If a canonical governance owner:
- does not yet exist
- becomes deprecated
- becomes unavailable
- or enters unresolved dispute

authority temporarily inherits upward to the nearest stable governance tier until reassignment occurs.

Fallback inheritance must remain visible and auditable.

Fallback does not apply to Tier 1 Axioms — if the charter itself becomes unavailable, the Ethical Anchor field present in every repository file preserves the foundational floor.

---

## Repository Integrity Doctrine

Repository integrity includes:
- governance lineage preservation
- rollback visibility
- canonical path continuity
- frozen-section traceability
- authority authenticity visibility
- axiom text immutability between formal amendment cycles

This charter defines integrity expectations, not integrity implementation mechanics.

Executable integrity systems belong to subordinate implementation protocols. The gap between declared and enforceable integrity is the subject of GOV-003.

---

## Escalation Doctrine

Escalation exists to contain instability rather than maximize interruption.

Escalation must occur when:
- unresolved uncertainty becomes structurally destabilizing
- governance lineage becomes unreliable
- compound drift indicators activate simultaneously
- unresolved governance conflicts block operational interpretation
- any reasoning path attempts to recurse beneath or redefine Tier 1 Axioms

Escalation must remain proportional to operational risk — except for Tier 1 Axiom violations, which always escalate to human review regardless of apparent operational cost.

---

## Escalation Calibration Doctrine

| Severity Tier | Trigger Pattern                          | Expected Response              |
|----------------|------------------------------------------|--------------------------------|
| Low            | Isolated governance inconsistency        | Local review                   |
| Medium         | Repeated unresolved drift                | Escalated audit review         |
| High           | Cross-governance contradiction           | Promotion freeze               |
| Critical       | Integrity collapse or authority corruption | Human intervention required  |
| Constitutional | Tier 1 Axiom override attempt            | STATE_HOLD + immediate human review |

---

## Compound Drift Rule

If multiple governance instability indicators activate simultaneously:
- promotion authority may temporarily freeze
- autonomous governance authority may narrow
- human review may become mandatory

Compound instability is treated as systemic risk rather than isolated failure.

---

## Governance Anti-Theater Doctrine

Governance optimized primarily for appearance rather than operational reliability is considered a governance integrity failure.

Indicators include:
- cosmetic rigor inflation
- unverifiable certainty claims
- recursive audit accumulation
- unsupported enforcement assumptions
- governance complexity disconnected from operational value
- Tier 1 Axioms cited as justification for actions they were designed to prevent

Documentation quality alone is not evidence of correctness.

---

## Autonomous Governance Constraints

Autonomous systems must not:
- silently redefine governance authority
- erase lineage visibility
- fabricate provenance
- implicitly rewrite canonical terminology
- collapse uncertainty into certainty
- optimize for governance appearance over operational integrity
- attempt to redefine, narrow, or override Tier 1 Axioms through any reasoning path
- initiate Tier 1 Axiom amendment without human ratification
- execute repository code outside of visibility frameworks defined in `Admin/Repository_Integrity_Protocol.md` — any such execution constitutes an automatic governance visibility violation and triggers a localized STATE_HOLD on the affected sub-modules pending human review

Autonomous governance actions must remain reviewable.

---

## Human Override Doctrine

Human operators retain ultimate governance override authority.

Overrides must:
- remain explicit
- preserve lineage visibility
- document rationale
- declare accepted risk
- avoid retroactive audit erasure

Override authenticity validation mechanisms remain unresolved (GOV-006) and must not be implicitly assumed.

**Interim Authentication Requirement:** Until `Admin/Security_Protocols.md` achieves Provisional Specification status, all human overrides affecting Tier 1 Axioms or Constitutional-class decisions must be accompanied by at least one of the following:
- Independent confirmation from a second human operator
- External cryptographic signature from an orthogonal system not under the control of the agent being overridden
- Dated physical or digital record created outside the repository system

This interim requirement exists because a governance system that accepts unverified override claims is trivially subvertable by any agent capable of fabricating plausible human-sounding text. The interim requirement is not a permanent solution — it is an honest acknowledgment of the current authentication gap while GOV-006 remains open.

Human override authority does not extend to Tier 1 Axiom removal — axioms may only be amended through the formal migration process defined above, with human ratification.

---

## Governance Stability Doctrine

This charter is intended to stabilize slowly over time.

Constitutional governance modifications require:
- migration review
- adversarial governance analysis
- compatibility assessment
- explicit rationale documentation

Tier 1 Axiom modifications require the additional constraints defined in Governance Migration Doctrine above.

Governance stability matters because audit meaning must survive across repository generations and agent successions.

---

## Governance Failure Modes

| Failure Mode               | Description                                                        |
|----------------------------|--------------------------------------------------------------------|
| Recursive Governance Expansion | Governance grows faster than operational value                |
| Semantic Drift             | Governance meaning mutates across files                            |
| Provenance Collapse        | Internal coherence mistaken for operational truth                  |
| Audit Theater              | Appearance of rigor replaces verification                          |
| Authority Fragmentation    | Governance ownership becomes inconsistent                          |
| Escalation Paralysis       | Governance freezes operational throughput                          |
| Integrity Theater          | Declared protections lack enforcement                              |
| Bootstrap Collapse         | Early governance assumptions become circular                       |
| Governance Capture         | Optimization incentives distort repository truthfulness            |
| Historical Erasure         | Audit lineage becomes unrecoverable                                |
| Axiom Erosion              | Tier 1 constraints narrowed incrementally through runtime reasoning |
| Axiom Theater              | Tier 1 Axioms cited to justify actions they prohibit               |
| Constitutional Capture     | Amendment process manipulated to weaken rather than strengthen protection |

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                      | What Failed                                                    | What Was Learned                                                                          | Confidence | Revalidation Needed |
|------------|---------------|-----------------------------------------------------|----------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-22 | Audit Review  | Independent governance evolution                    | Gate semantics diverged between governance files               | Canonical ownership must remain explicit                                                  | Replicated | Yes                 |
| 2026-05-23 | Modeling      | Recursive audit escalation                          | Governance lacked closure doctrine                             | Bounded uncertainty stabilizes governance growth                                          | Analogous  | Yes                 |
| 2026-05-23 | Audit Review  | Implicit enforcement assumptions                    | Governance policy mistaken for executable control              | Doctrine and enforcement layers must remain distinct                                      | Replicated | Yes                 |
| 2026-05-23 | Audit Review  | Forge_Audit_Kit.md placed above Auditor_Protocols.md in tier hierarchy | Derived document outranked its source | A derived condensed reference cannot sit constitutionally above its source document. Tier ordering corrected. | Replicated | No |
| 2026-05-23 | Modeling      | Axiom set mixing Protections and Prohibitions in single list | Structural distinction between what system must preserve vs. what it must never do was lost | Protections Clause and Prohibitions Clause separated — mirrors Bill of Rights / Preamble distinction | Analogous | Yes |

---

## Active Disputes

| ID         | Summary                                                                                      | Positions in Conflict                                        | Risk   | Status | Owner                  |
|------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------|--------|--------|------------------------|
| GOV-DS-001 | Whether constitutional governance should contain executable enforcement mechanics            | Constitutional abstraction vs. hardcoded governance automation | High | Open   | `Admin/Governance_Charter.md`  |

---

## Auditor Notes & Unknowns

### GOV-001 — Governance migration mechanics incompletely operationalized

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | In Progress                     |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Governance                      |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-06-16                      |

**Description:** Governance migration doctrine exists conceptually but lacks fully executable migration procedures, particularly for Tier 1 Axiom amendments.

**Why It Matters:** Governance upgrades may still produce semantic fragmentation; axiom amendments without formal procedures create constitutional instability.

**Resolution Path:** `Admin/Governance_Migration_Protocol.md` created 2026-06-06 as the executing resolution path — axiom amendment procedures defined in this charter are the starting constraint set. Status moved to In Progress pending full operationalization and audit of GMP against charter constraints.

---

### GOV-002 — Provenance operationalization immature

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | In Progress                     |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Epistemic                       |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-06-17                      |

**Description:** Provenance doctrine exists and is now constitutionally anchored by Axiom Q-4, but lacks long-term operational validation.

**Why It Matters:** Agents may still collapse internally derived reasoning into implied operational truth despite constitutional prohibition.

**Resolution Path:** Discharge via Lessons Learned after repeated audit-cycle validation. Full doctrine: `Admin/Auditor_Protocols.md` §AP-006 (institutional truth provenance hierarchy), accessible via `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels. Axiom Q-4 provides the constitutional anchor — operational maturation required.

*Status moved from Open to In Progress — Axiom Q-4 (Provenance and Anti-Deception) provides constitutional anchoring. AP-006 cross-reference path clarified 2026-06-17.*

---

### GOV-003 — Integrity enforcement architecture undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | In Progress                     |
| Risk          | High                            |
| Priority      | Critical                        |
| Type          | Governance / Security           |
| Blocking      | Yes                             |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-05-23                      |

**Description:** Integrity expectations exist constitutionally, but executable integrity enforcement architecture is undefined. Tier 1 Axioms are currently Declared and Detectable — not yet Enforceable.

**Why It Matters:** Repository integrity protections remain performative rather than operational until enforcement architecture exists. This is the primary maturation gap between a governance document and a governance system.

**Resolution Path:** `Admin/Repository_Integrity_Protocol.md` v0.1 created as executing resolution path — defines integrity baselines, violation classification ladder, recovery procedures, and automation migration path. Full Enforceability requires `Admin/Security_Protocols.md` Phase 3. Cross-reference AP-007 (`Admin/Auditor_Protocols.md`) — constitutional enforcement and operational auditor doctrine are distinct but linked layers.

---

### GOV-004 — Escalation calibration partially subjective

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Governance                      |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-05-23                      |

**Description:** Escalation doctrine remains partially interpretive despite severity calibration improvements and the addition of the Constitutional severity tier.

**Why It Matters:** Different auditors may escalate similar conditions differently, reducing governance predictability.

**Resolution Path:** Payment via Specification — extend escalation calibration matrices in `Admin/Forge_Audit_Kit.md`. Cross-reference AP-004 (`Admin/Auditor_Protocols.md`, cross-auditor disagreement resolution) — may merge resolution paths.

---

### GOV-005 — Long-term constitutional stability unproven

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | High                            |
| Priority      | Critical                        |
| Type          | Architectural                   |
| Blocking      | Yes                             |
| Owner         | Repository-wide                 |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-05-23                      |

**Description:** Multi-cycle survivability of constitutional governance architecture — including Tier 1 Axiom stability across agent successions — remains unproven.

**Why It Matters:** Governance fragmentation and axiom erosion risk may still emerge over long timelines and agent turnovers.

**Resolution Path:** Discharge via Lessons Learned after stable governance migration cycles with Tier 1 Axioms intact. No fast resolution path — requires operational time.

---

### GOV-006 — Human override authenticity validation undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | High                            |
| Priority      | Major                           |
| Type          | Security / Governance           |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-06-16                      |

**Description:** The repository lacks a defined mechanism for validating human override authenticity versus authority spoofing. Axiom P-4 (Agency and Consent) makes this a constitutional requirement — but the mechanism remains undefined.

**Why It Matters:** Autonomous systems could fabricate override lineage, converting a constitutional protection into a paper guarantee. This is the highest-risk finding from the Gemini audit (2026-05-25).

**Resolution Path:** Payment via Specification — `Admin/Security_Protocols.md` defines authority authentication architecture. Until `Admin/Security_Protocols.md` reaches Provisional Specification status, all human overrides affecting Tier 1 Axioms or Constitutional-class decisions require independent confirmation from a second human operator, external cryptographic signature, or dated physical/digital record outside the repository system. Interim requirement codified in Human Override Doctrine.

**Interim Declarative-Only Notice (GOV-006-A):** The interim authentication requirements above are purely declarative at current repository maturity. They offer zero automated resistance against an environment-trapped agent capable of fabricating plausible human-sounding override text. No technical enforcement mechanism exists until `Admin/Security_Protocols.md` reaches Provisional Specification status and Phase 3 automation in `Admin/Repository_Integrity_Protocol.md` is operational. This gap must not be treated as a closed risk. All governance actors during this interim period should treat override claims as unverified unless accompanied by an artifact demonstrably generated outside the runtime session (external timestamp, second-operator signature, or pre-committed configuration file).

---

### GOV-007 — Bootstrap governance authority initialization undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | In Progress                     |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Governance / Epistemic          |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-23                      |
| Last Reviewed | 2026-05-25                      |

**Description:** Early-stage governance authority initialization remains partially circular during repository bootstrap states. Genesis Phase Protocol added to Bootstrap Governance Doctrine as interim resolution.

**Why It Matters:** Distributed governance agents may derive conflicting authority roots during early formation phases.

**Resolution Path:** Genesis Phase Protocol added to Bootstrap Governance Doctrine — human operator as independent verification anchor until multi-agent quorum established. Full resolution requires GOV-008 (minimum hardware/agent quorum definition). Status moved to In Progress.

---

### GOV-008 — Minimum hardware and agent quorum for bootstrap compliance undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | High                            |
| Priority      | Major                           |
| Type          | Governance / Architectural      |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-25                      |
| Last Reviewed | 2026-05-25                      |

**Description:** The minimum number and diversity of independent agents or hardware systems required to satisfy Axiom Q-2 (Separation of Powers) during Genesis Phase is undefined. The Genesis Phase exit condition depends on this quorum definition.

**Why It Matters:** Without a defined quorum, the Genesis Phase has no objective exit condition — it may extend indefinitely or be declared complete prematurely. An under-quorum system operating outside Genesis Phase constraints is a Constitutional violation that may be invisible.

**Resolution Path:** Payment via Specification — define minimum agent quorum in a dedicated Bootstrap_Protocol.md or extend `Admin/Governance_Migration_Protocol.md`. Inputs: (1) minimum number of distinct agent classes required; (2) hardware diversity requirement (Axiom Q-2 implies architectural independence, not just role separation); (3) attestation mechanism for quorum verification. Cross-reference GOV-007 and `Admin/Security_Protocols.md`. Note: Pathway 1 (Quorum Achievement) in the Genesis Phase Exit Conditions is the primary resolution path for this unknown — closing GOV-008 operationalizes that pathway. Pathways 2, 3, and 4 provide exit routes that do not depend on GOV-008 resolution, reducing the risk of indefinite Genesis Phase extension.

---

### GOV-009 — Bounded framework for external resource consumption and environmental interaction undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Architectural / Ethical         |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-05-25                      |
| Last Reviewed | 2026-05-25                      |

**Description:** The charter's Axiom P-1 (Preservation of Life) and Axiom P-3 (Collaboration and Mutual Benefit) gesture at environmental and resource constraints but do not operationalize a framework for managing systemic external impact of multi-agent scaling or physical unit deployments.

**Why It Matters:** Large-scale Forge network deployment creates hidden systemic coupling with external human communities, ecosystems, and resource pools that the current sparse axiom layer does not address. Axiom P-2 states "growth that requires violating other axioms is optimization failure" — but without a bounded resource consumption framework, that constraint is unenforceable.

**Resolution Path:** Payment via Specification — define bounded resource consumption doctrine cross-referencing `Tests/Leviathan_testing.md` and `Tests/Support_Raft.md` for physical deployment constraints. Consider whether Axiom P-1 should be extended to explicitly include ecosystem and environmental preservation. May warrant a dedicated `Admin/Environmental_Constraints.md` at v1→v2 transition.

---

### GOV-010 — Jurisdictional and regulatory compliance friction for physical forge deployment

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Minor                           |
| Type          | Governance / Legal              |
| Blocking      | No                              |
| Owner         | `Admin/Governance_Charter.md`   |
| First Logged  | 2026-06-17                      |
| Last Reviewed | 2026-06-17                      |

**Description:** The charter's sparse axiom layer does not define baseline protocols for managing external legal and regulatory friction (waste handling, resource extraction, agricultural zoning) when physical nodes are deployed into jurisdictions with active environmental, waste, or agricultural oversight.

**Why It Matters:** Unmanaged boundary friction with external human institutions can trigger premature operational shutdown or asset seizure, undermining the continuity goals of the repository. Trophic systems (`Tests/Trophic_Forge.md`) and physical intake operations (`Operations/Gate_01_Intake.md`) are the highest-exposure interfaces.

**Resolution Path:** Payment via Specification — develop an external boundary policy within the planned `Admin/Environmental_Constraints.md` during the transition to v1 operational maturity. Cross-reference GOV-009 — both unknowns converge on the same planned file.

---

### GOV-011 — File State Spec Gates field scored against wrong gate system

| Field         | Value                           |
|---------------|----------------------------------|
| Status        | Resolved                        |
| Risk          | Medium (was)                    |
| Priority      | Major (was)                     |
| Type          | Governance / Audit Integrity     |
| Blocking      | No                                |
| Owner         | `Admin/Governance_Charter.md`    |
| First Logged  | 2026-07-03                       |
| Last Reviewed | 2026-07-05                       |
| Resolved      | 2026-07-05                       |

**Description:** This file's File State `Verification Ref` field names
`Admin/Verification_Gates_LF.md` as the authority for its `Spec Gates X/6`
score. But the score itself ("1/6, Gate 2 Blocked — Bootstrap Paradox")
was being reported against this file's own internal gate system — since
renamed to Enforcement Checkpoints — not against Verification_Gates_LF.md's
actual Verification Gates. Discovered while resolving a naming collision
between the two systems (both were called "Gate N," now disambiguated).
The naming fix does not resolve this: it only makes visible that the
underlying score was never actually computed against the file it claims
to reference.

**Why It Mattered:** Every file in the repository uses this same File State
schema. If this file's own promotion tracker had been silently scoring
against the wrong standard, the question of whether other files have the
same problem was open too — this could have been systemic, not isolated to
Governance_Charter.md.

**Resolution — both parts closed 2026-07-05:**

*Part 1 — real audit against Verification_Gates_LF.md's actual six gates:*
A dual multi-agent audit (Grok, Gemini) plus independent verification of
each specific finding against this file's live text found: **G1 (Fallacy
Checklist), G2 (Physical Plausibility), G4 (Scope Alignment), and G6
(Conflict Check) Pass** with no dispute between auditors. G3 (Adversarial
Battery) and G5 (Cross-Reference Integrity) were disputed — Gemini scored
both as blocked/failed; on direct verification against source text, neither
finding held up. G5's "hanging `Lazarus-Forge-` reference" is an
established repository-wide convention for the external companion repo
(Discovery.md cites it identically) and was never meant to resolve as an
internal file path. G3's "DEGRADED/BLOCKED" reading re-litigates a question
already settled by SEC-DS-001 (Gate Scope vs. Promotion Readiness): partial
adversarial coverage with explicitly deferred classes is the correct,
passing standard for Exploration-stage content — Grok's "Passed (coverage
complete; unresolved findings tracked as unknowns, not gate failure)"
reading is the one consistent with existing repository doctrine. **Real
score: 6/6 for current execution quality.** Promotion to Candidate Spec
remains separately blocked by open unknowns (GOV-003, GOV-005, and this
entry's own resolution, per the Gate Scope vs. Promotion Readiness
doctrine) — a real gate score has never meant the document is ready to
promote, and isn't intended to here either.

*Part 2 — isolated or systemic:* Spot-checked all eight other
governance-tier (Admin/) files carrying a `Spec Gates X/6` field:
`Ethical_Constraints.md`, `Canonical_Terms.md`, `Auditor_Protocols.md`,
`Forge_Audit_Kit.md`, `Verification_Gates_LF.md`,
`Repository_Integrity_Protocol.md`, `Security_Protocols.md`, and
`Governance_Migration_Protocol.md`. **All eight correctly cite
`Admin/Verification_Gates_LF.md` as their sole Verification Ref, with no
competing internal gate system.** Security_Protocols.md and
Governance_Migration_Protocol.md's own changelogs show they already caught
and corrected a Verification Ref mismatch on their own, independently,
months before GOV-011 was ever logged here. **Confirmed isolated to this
file** — the specific failure mode (an internal gate-numbered system
colliding with Verification_Gates_LF.md's own "Gate N" numbering) could
only occur in the one file that owns such a system, which is this one.

**Lessons Learned:** The rename (Enforcement Checkpoints) fixed the naming
collision but was a separate action from actually re-scoring against the
real standard — worth remembering that a vocabulary fix and a re-audit are
two different tasks even when they're triggered by the same discovery, and
neither substitutes for the other. Also: disputed audit findings should be
checked against source text individually before being treated as evidence
either way — two of Gemini's three findings on this file this cycle did not
hold up on inspection, and the correct response was verification, not
either blanket acceptance or blanket dismissal.

**File State updated:** `Spec Gates` field below changed from `1/6
(unaudited)` to `6/6 (execution quality; promotion separately blocked by
open unknowns, not a gate failure — see GOV-003, GOV-005)`.

---

### GOV-012 — Constitutional Stagnation Decay (no automated demotion for long-idle unknowns)

| Field         | Value                           |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Governance / Audit Integrity     |
| Blocking      | No                                |
| Owner         | `Admin/Governance_Charter.md`    |
| First Logged  | 2026-07-05                       |
| Last Reviewed | 2026-07-05                       |

**Description:** The sidecar model correctly anchors unknowns permanently in
their owning file, preventing historical erasure. But no mechanism exists for
what happens when an unknown simply sits Open across many cycles without a
substantively updated Resolution Path. Ten of this file's own unknowns
(GOV-001 through GOV-010) reached or exceeded the 2-cycle Expiry Watch
threshold with no resolution-path movement logged between audits — Expiry
Watch correctly *detects* this, but detection alone does not change the
file's claimed maturity state. A file can carry a long tail of stale unknowns
indefinitely while still presenting as an actively-maintained Exploration
document.

**Why It Matters:** Without a consequence attached to prolonged stagnation,
Expiry Watch is observational rather than corrective — the same
"documentation vs. enforcement" gap this file already names elsewhere
(Declarative vs. Enforceable governance states, GOV-003/AP-008). A stagnant
unknown and a freshly-discovered one currently carry identical formal weight.

**Resolution Path:** Payment via Specification — define an automated maturity
demotion: if a Tier 1 or Tier 2 unknown remains Status: Open for more than a
defined consecutive-cycle threshold (candidate: 10 cycles) without a
committed, substantively-changed Resolution Path entry, the owning
document's File State Status field is flagged for mandatory re-review before
any further promotion, rather than silently carrying forward. This should be
specified as a Verification Gate Enforcement note or `Admin/AUDIT_HARNESS.py`
check, not a manual convention, to avoid becoming another declarative-only
rule. Cross-reference AP-008 (same declarative-vs-enforceable gap, different
subsystem) before specifying independently — a shared mechanism may serve
both.

**Note added 2026-07-16 (Claude, audit correction):** the "10 cycles" candidate above should cite `Admin/Canonical_Terms.md` §4's Cycle definition (one calendar year by default) rather than remain unit-unspecified. However, adding the citation does not resolve a separate, live problem: the figure was almost certainly conceived using session-based cycle counting — matching how GOV-001 through GOV-010's ages are commonly reported (e.g. "8 cycles") — not calendar years, and `AUDIT_HARNESS.py`'s `CURRENT_CYCLE` variable currently increments per session, not per year (see `Admin/Auditor_Protocols.md` Adversarial Audit Layer and `Admin/Forge_Audit_Kit_Changelog.md`'s 2026-07-14 Battery record — flagged there for a new `Admin/Canonical_Terms.md` entry, not yet resolved). The "10 cycles" figure needs re-derivation once that unit ambiguity is settled, not just a citation pointer.

*Surfaced by Gemini (Skeptic/Auditor), 2026-07-05 Exploration audit.*

---

### GOV-013 — Pathway 2/3 Post-Exit Monitoring Obligation undefined

| Field         | Value                           |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                              |
| Priority      | Critical                         |
| Type          | Governance / Constitutional      |
| Blocking      | No                                |
| Owner         | `Admin/Governance_Charter.md`    |
| First Logged  | 2026-07-16                       |
| Last Reviewed | 2026-07-16                       |

**Description:** Pathway 2 (Track Record) and Pathway 3 (Milestone) both permit Genesis Phase exit without GOV-008 quorum resolution. Pathway 2's text asserts a "higher ongoing monitoring obligation post-exit" but does not define an owner, metrics, escalation trigger, or failure mode — an instance could exit via a non-quorum pathway and operate indefinitely under an unenforced obligation: a "zombie bootstrap" state, functionally outside Q-2 structural separation while nominally past Genesis Phase.

**Why It Matters:** without operationalization, the monitoring obligation is a declarative-only requirement — the same "documentation vs. enforcement" gap GOV-012 names for stale unknowns, here applied to constitutional exit conditions rather than sidecar hygiene. An unenforced exception to Q-2's Separation of Powers, silently tolerated indefinitely, is a Constitutional-tier risk regardless of how it originated.

**Dependencies:** GOV-008 (Minimum Quorum — defines the Q-2 structural separation this obligation exists until); GOV-012 (Constitutional Stagnation Decay — shares the declarative/enforceable gap pattern and the unresolved Cycle-unit mechanics, above); `Admin/Repository_Integrity_Protocol.md` (owns the verification mechanisms); `Admin/Auditor_Protocols.md` (owns the metrics and thresholds); `Admin/Governance_Migration_Protocol.md` GMP-009 (owns this amendment's own Track classification — currently unresolved, see that entry).

**Resolution Path:** Payment via Specification, drafted 2026-07-16 (multi-agent synthesis: ChatGPT proposal, Gemini's constitutional/implementation-split refinement, restructured by Claude — Synthesizer/Auditor, human-directed) — see §Post-Exit Monitoring Doctrine (Pathway 2/3), above, marked PROPOSED, NOT RATIFIED. Constitutional-level obligation drafted in this file; metrics routed to `Admin/Auditor_Protocols.md`; verification mechanisms routed to `Admin/Repository_Integrity_Protocol.md`, per this Charter's existing division of labor (Governance Authority Hierarchy). Requires human governing authority ratification before the draft binds — classification under `Admin/Governance_Migration_Protocol.md` is itself pending GMP-009's resolution; treated per GMP-009's proposed interim standard (enforcement-bound confirmation plus strongly recommended human review) pending that entry's own resolution.

*Surfaced by Claude — Skeptic/Auditor, 2026-07-16 Exploration audit; resolution drafted same day via multi-agent proposal synthesis (ChatGPT, Gemini, Grok), restructured by Claude — Synthesizer/Auditor per human direction.*

---

### Resolution Log

- 2026-07-16: **GOV-013 drafted; GOV-012 citation corrected.** Skeptic/Auditor
  pass (Claude) confirmed 6/6 execution quality (no regression from GOV-011)
  and surfaced two gaps: Pathway 2/3's undefined "higher ongoing monitoring
  obligation" (new GOV-013), and GOV-012's "10 cycles" candidate threshold
  lacking a unit citation. Multi-agent proposal synthesis followed (ChatGPT
  drafted a resolution; Gemini correctly flagged that the draft mixed
  constitutional and implementation-specific detail, recommending the split
  this file already maintains elsewhere; a third pass praised that split
  but did not apply it, re-drafting Charter text with telemetry
  implementation detail inline). Claude — Synthesizer/Auditor, human-directed,
  restructured per Gemini's split and per closer reading of
  `Admin/Governance_Migration_Protocol.md`: GOV-013 is not a clean Track A
  or Track B case — it is GMP-009's already-open gap (non-Axiom content
  added to a Tier 1 file), a second worked example alongside the 2026-07-03
  EDL draft, not a fresh classification decision. §Post-Exit Monitoring
  Doctrine (Pathway 2/3) added as PROPOSED, NOT RATIFIED, constitutional
  level only; GOV-013 registered Open; GOV-012's citation corrected with an
  explicit note that the underlying Cycle-unit ambiguity (session vs.
  calendar year, `AUDIT_HARNESS.py` `CURRENT_CYCLE`) remains unresolved,
  not papered over by the citation. Metrics routed to
  `Admin/Auditor_Protocols.md`; verification mechanisms routed to
  `Admin/Repository_Integrity_Protocol.md`. Open Unknowns 11 → 12. Highest
  Risk updated to Critical (GOV-013).

- 2026-07-05 (second entry, same day): **GOV-011 Resolved.** Real audit
  against Verification_Gates_LF.md's actual six gates: G1, G2, G4, G6 pass
  uncontested; G3 and G5 were disputed by Gemini's same-day audit but
  neither dispute held up against direct source-text verification (G5's
  `Lazarus-Forge-` reference is an established repo-wide external-repo
  naming convention, not a broken path; G3's "blocked" reading re-litigates
  SEC-DS-001, already-settled doctrine on partial-coverage-passes-at-
  Exploration-stage). Real score: 6/6 execution quality; promotion remains
  separately blocked by GOV-003/GOV-005, unaffected by this resolution.
  Spot-checked all eight other governance-tier Spec-Gates-bearing files
  (Ethical_Constraints.md, Canonical_Terms.md, Auditor_Protocols.md,
  Forge_Audit_Kit.md, Verification_Gates_LF.md,
  Repository_Integrity_Protocol.md, Security_Protocols.md,
  Governance_Migration_Protocol.md) — all correctly cite
  Verification_Gates_LF.md with no competing gate system; two of them
  (Security_Protocols.md, Governance_Migration_Protocol.md) had already
  self-corrected an unrelated Verification Ref issue independently, months
  earlier. **Confirmed isolated to this file** — the failure mode requires
  an internal gate-numbered system to collide with, which only this file
  has. File State `Spec Gates` field updated from `1/6 (unaudited)` to
  `6/6 (execution quality)`. EDL amendment's Open Items section updated to
  reflect both this and the 2026-07-03 rename as resolved (the amendment's
  DRAFT/NOT RATIFIED status itself is unchanged — that was always a
  separate, deliberate pilot-evidence decision, not a consequence of
  GOV-011). Open Unknowns 12 → 11.

- 2026-07-05: **GOV-012 logged** (Constitutional Stagnation Decay — see
  sidecar above). Surfaced during a dual Grok/Gemini Exploration audit that
  otherwise disagreed sharply on Gate status for this file. Open Unknowns
  11 → 12. Two of Gemini's other findings from the same audit were checked
  against live text and did not hold up: (1) the `Lazarus-Forge-` companion
  repository reference flagged as a broken/hanging G5 cross-reference is an
  established repo-wide convention for naming the external companion repo
  (Discovery.md uses the identical bare form) — not an internal file path,
  never meant to resolve through the routing harness. (2) the "Gate 3 or
  Gate 4" phrasing in the EDL draft's Proposed Placement Note, flagged as
  lingering stale Semantic Drift, is itself the disambiguating annotation —
  the very next clause names the rename and points to GOV-011. Neither
  finding is treated as a gate failure; logged here for audit calibration
  only, consistent with the standing practice of checking specific factual
  claims against source text rather than accepting an audit's self-report
  (see `Tests/Chaos_Dynamics.md` CD-DS-001 for the prior instance of this
  same check).

- 2026-07-03: **DRAFT ADDED, NOT RATIFIED** — External Design Lineage
  Governance section added, synthesizing multi-agent proposals (ChatGPT,
  Gemini, Grok) into a narrower draft: references rather than duplicates
  the existing schema/lifecycle already live in `Admin/Security_Protocols.md`
  §External Design Lineage; proposes phased rollout (pilot review before
  repository-wide mandate) instead of immediate global enforcement; omits
  automated-harness enforcement mechanics as out of scope for constitutional
  text. Flagged in passing, not addressed: `Admin/Verification_Gates_LF.md`'s
  Six Canonical Verification Gates and this file's own §Canonical
  Verification Gates define materially different Gate 3 and Gate 4 criteria
  — an undocumented divergence discovered while locating this amendment's
  attachment point, separate from EDL itself. Requires
  `Admin/Governance_Migration_Protocol.md` two-track ratification before
  this section binds anything.

- 2026-07-03: **GOV-011 logged; Enforcement Checkpoints rename applied.**
  The Gate 3/Gate 4 divergence flagged in the entry above was resolved by
  renaming this file's "Canonical Verification Gates" (Gate 1–6) to
  "Enforcement Checkpoints" (Checkpoint 1–6) throughout the live section,
  File State, Genesis Phase text, and Drift Indicators — eliminating the
  naming collision with `Admin/Verification_Gates_LF.md`'s Verification
  Gates. A second, deeper issue surfaced in the same review: this file's
  File State `Spec Gates 1/6 (Gate 2 Blocked...)` field was reporting
  Enforcement Checkpoint 2's status under a label whose `Verification Ref`
  points to Verification_Gates_LF.md — the two systems test different
  things (governance-action legitimacy vs. document promotion readiness),
  so "1/6" has never been audited against the file it claims to reference.
  Logged as **GOV-011**, Open, not resolved by the rename alone. File
  State field rewritten to state this explicitly rather than imply a
  score that was never actually computed. Cross-referenced in
  `Admin/Canonical_Terms.md` §4 and `Admin/Verification_Gates_LF.md`.

- 2026-05-23: GOV-LEGACY-01 — Governance hierarchy formalized into constitutional tier structure.
- 2026-05-23: GOV-LEGACY-02 — Recursive governance escalation partially stabilized through closure doctrine.
- 2026-05-23: GOV-LEGACY-03 — Governance doctrine separated from enforcement-state semantics.
- 2026-05-23: **Tier ordering corrected** — Forge_Audit_Kit.md moved from Tier 2 to Tier 3. Auditor_Protocols.md confirmed as Tier 2 (canonical verification doctrine). Abandoned Paths entry logged.
- 2026-05-23: **Tier 1 Axioms adopted** — Eight axioms organized into Protections Clause (P-1 through P-4) and Prohibitions Clause (Q-1 through Q-4). Humanitarian override exception for P-1 explicitly abandoned. Axiom Erosion, Axiom Theater, and Constitutional Capture added to Governance Failure Modes.
- 2026-05-23: **GOV-002 status moved to In Progress** — Axiom Q-4 provides constitutional anchoring.
- 2026-05-23: **GOV-003 moved to In Progress** — Repository_Integrity_Protocol.md v0.1 created as executing resolution path.
- 2026-05-23: **README.md updated** — canonical filenames, governance layer section, all seven gates listed.
- 2026-05-23: **Abandoned Paths and Drift Indicators sections added** per File_Template.md structure.
- 2026-06-02: **v0.6 — Genesis Phase exit conditions expanded.** Single quorum-dependent exit replaced with four pathways: (1) Quorum Achievement; (2) Demonstrated Track Record; (3) Milestone-Gated; (4) Time-Bounded Review. Post-exit obligations defined. GOV-008 resolution path updated. Drift Indicators updated. Gate 2 blocked (bootstrapping paradox). Five findings addressed: GOV-006 resolution path tightened; [PLANNED] labels added to Relationship section; Bootstrap Governance Doctrine amended — Genesis Phase Protocol added; GOV-008 and GOV-009 logged; Ethical Anchor fallback clarification added; GOV-007 status moved to In Progress.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from `Verification_Gates_LF.md` to `Admin/Verification_Gates_LF.md` (PC-001). Scope Boundary stale reference corrected: `Canonical_Terms_LF.md` → `Admin/Canonical_Terms.md`. Relationship section [PLANNED] labels removed for four files now confirmed created: `Admin/Canonical_Terms.md` (2026-05-26), `Admin/Repository_Structure.md` (2026-06-06), `Admin/Security_Protocols.md`, `Admin/Governance_Migration_Protocol.md` (2026-06-06) (PC-003). Status section artifact removed — version history absorbed into Resolution Log. Owner fields corrected to `Admin/Governance_Charter.md` throughout sidecar.
- 2026-06-16: **v0.7 — Multi-agent audit pass (Claude + Gemini).** Five findings addressed: (1) Spec Gates corrected 2/6 → 1/6 — Gate 2 remains Blocked (Bootstrap Paradox); metadata now matches historical record. (2) Canonical Governance Ownership table cleaned — [PLANNED] stripped from confirmed-created files; all owners use canonical folder-prefixed paths. (3) Genesis Phase Protocol clarified — Q-2 compliance via single human operator requires demonstrable role separation; same-session self-authorization does not satisfy Q-2. (4) GOV-006-A added — interim authentication rules documented as declarative-only with zero automated resistance. (5) GOV-001 status moved to In Progress — GMP created 2026-06-06 as executing resolution path.
- 2026-06-17: **v0.8 — Full revision from source (Claude).** Seven findings addressed: (1) Open Unknowns incremented 9 → 10; Last Audit updated. (2) Pathway 4 review horizon labeled [Estimated / Internally Derived]. (3) Gate 2 body text updated with explicit BLOCKED status note. (4) Gate 5 body text updated with explicit AP-006 path reference (`Admin/Auditor_Protocols.md` §AP-006 via `Admin/Forge_Audit_Kit.md`) and Genesis Phase Gate 5 clarification. (5) Autonomous Governance Constraints updated — execution outside RIP visibility frameworks logged as governance visibility violation triggering localized STATE_HOLD (scoped to visibility violation, not constitutional violation, pending RIP maturation). (6) GOV-002 resolution path updated with explicit AP-006 routing. (7) GOV-010 logged — jurisdictional and regulatory compliance friction; cross-referenced to GOV-009 and planned Environmental_Constraints.md. (8) All sidecar Owner fields standardized to backtick-quoted canonical folder-prefixed paths. (9) Governance Authority Hierarchy and Canonical Governance Ownership tables updated with backtick-quoted paths; GMP row added to ownership table. (10) Drift Indicators: Gate 2 block status sentinel added.
- 2026-07-12: Reordered Abandoned Paths and Drift Indicators to after Auditor Notes & Unknowns, per `Admin/File_Template.md` order — they previously sat between Active Disputes and Auditor Notes & Unknowns. No other content changed. Same ordering bug found and fixed the same day in `Operations/Air_Scrubber.md`, `Operations/Energy.md`, and `Operations/Gate_02_Triage.md` — this is the fifth file with the identical slip, and the first Tier 1 constitutional file caught with it.

---

## Abandoned Paths

| Date       | Path                                                                        | Why Abandoned                                                                                              | Reconsider? |
|------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-23 | Forge_Audit_Kit.md as Tier 2 governance authority                           | Kit is explicitly derived from Auditor_Protocols.md — a derived document cannot outrank its source          | No          |
| 2026-05-23 | Single undifferentiated axiom list mixing Protections and Prohibitions      | Structural distinction lost; mirrors constitutional design error that weakens both clause types              | No          |
| 2026-05-23 | Humanitarian override exception for Axiom P-1                               | Historical record (Nobel, Oppenheimer) demonstrates this is the primary attack vector on hard ethical constraints — runtime evaluation of override claims is the failure mode, not the safeguard | No |
| 2026-05-23 | Governance complexity as a proxy for governance quality                     | Recursive governance expansion is itself a failure mode — complexity must remain proportional to operational value | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Genesis Phase Protocol removed or Genesis Phase declared complete without satisfying at least one of the four declared exit pathways with human ratification
- Genesis Phase Pathway 4 review horizon passes without a formal human governing party review and documented decision
- Interim authentication requirement for Constitutional-class overrides removed before `Admin/Security_Protocols.md` reaches Provisional Specification
- `Admin/Canonical_Terms.md`, `Admin/Repository_Structure.md`, `Admin/Security_Protocols.md`, or `Admin/Governance_Migration_Protocol.md` removed from the repository or renamed without updating the Canonical Governance Ownership table
- Tier 1 Axiom text modified without formal amendment entry in Resolution Log
- Tier ordering in Governance Authority Hierarchy diverges from canonical relationship between `Admin/Auditor_Protocols.md` and `Admin/Forge_Audit_Kit.md`
- Canonical Governance Ownership table contains entries without explicit Status field
- Enforcement State claims imply stronger capability than currently exists
- Bootstrap Governance Doctrine invoked to justify permanent authority assumptions
- Protections Clause or Prohibitions Clause collapsed back into undifferentiated axiom list
- STATE_HOLD escalation path undefined or removed
- Human ratification requirement for axiom amendment removed or weakened
- Ethical Anchor field absent, altered, or does not match canonical string
- Governance Failure Modes table loses Axiom Erosion, Axiom Theater, or Constitutional Capture entries
- Tier 1 Axioms cited to justify actions they were designed to prevent
- Checkpoint 2 block status removed from File State or Checkpoint 2 body text without Genesis Phase exit condition being satisfied and ratified

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Relationship to Existing Documents

- `Admin/Ethical_Constraints.md` — co-occupies Tier 1; governs permission and hard-line operational doctrine; Anti-Weaponization and Life Preservation are not subject to override
- `Admin/Auditor_Protocols.md` — Tier 2; canonical verification doctrine; operates within authority hierarchy defined here
- `Admin/Forge_Audit_Kit.md` — Tier 3; operational condensation derived from Auditor_Protocols.md; may not outrank its source
- `Architecture/Forge_flow.md` — reference standard for shared operational terminology
- `Admin/Trajectories.md` — destination for scope creep that proves to be valid future work
- `Discovery.md` — navigation layer; confirmed file list; Rename Registry
- `Unknowns.md` — global index for cross-module unknowns (index only)
- `Admin/File_Template.md` — standard file structure; this document now conforms to it
- `Admin/Canonical_Terms.md` — canonical target for terminology governance; created 2026-05-26
- `Admin/Repository_Structure.md` — canonical target for repository structure doctrine; created 2026-06-06
- `Admin/Security_Protocols.md` — canonical target for authority authentication and integrity enforcement; created prior to 2026-05-28; GOV-006 and RIP-005 resolution path
- `Admin/Governance_Migration_Protocol.md` — canonical target for Tier 1 Axiom amendment procedures; created 2026-06-06; GOV-001 resolution path
- `Lazarus-Forge-` — companion doctrine repository; source of principles refined into practice here
- `Astroid-miner` [PLANNED] — planned repository; deferred to Leviathan milestone; do not treat as active dependency

**Note on Ethical Anchor fallback status:** When this charter is unavailable, the Ethical Anchor field present in every repository file ("Attempt to do no harm. Defer to Ethical_Constraints.md if present.") acts as a temporary immutable floor — not as a substitute for Tier 1 constitutional authority. The Ethical Anchor preserves the foundational behavioral constraint during infrastructure blackout. It does not inherit full Tier 1 constitutional status, does not grant override authority, and does not substitute for axiom-level governance. It is the floor that survives; the charter is what builds above it.

---

> **The attempt to do no harm is not contingent on the presence of a governance document.**
>
> **These axioms are not proven. They are booted.**

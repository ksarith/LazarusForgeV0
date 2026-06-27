# Auditor_Protocols.md
**Version 0.11**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-21                                                          |
| Auditor          | Claude — Synthesizer/Auditor; Gemini — Skeptic/Auditor              |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Epistemic Foundation constitutional layer (EF-0.0 through EF-0.8b) — meta-constitutional, immutable without human ratification
- Repository-wide auditor operational behavior
- Auditor role classes and their responsibilities
- Audit entry conditions and sequencing
- Fallacy checklist with substantive note requirements
- AI and human contributor protocols
- Decentralized audit architecture (Sidecar Model)
- Unknowns registry governance
- Verification gate enforcement
- Adversarial audit layer and challenge battery
- Drift detection requirements
- Specification promotion rules
- Autonomous auditor constraints
- Human override doctrine
- Full Stop Review triggers
- Observability and audit trail requirements
- Protocol performance metrics

**This file DOES NOT define:**
- Engineering specifications for Forge systems
- Ethical policy details beyond mandatory anchor preservation
- Local module implementation details
- Human governance authority structures
- Fabrication procedures
- Experimental methodology standards
- Canonical terminology definitions (→ `Admin/Canonical_Terms.md`)
- Repository architecture ownership boundaries (→ Governance_Charter.md)
- Cross-repo verification architecture (→ Forge_Net.md)

---

## File Purpose

This file defines how auditors operate within LazarusForgeV0. It exists to prevent audit theater, uncontrolled specification promotion, semantic drift, silent contradiction accumulation, and autonomous corruption of repository knowledge. Without this file, the repository may continue producing documents while progressively losing reliability, traceability, and operational grounding. The protocol establishes how auditors detect instability, classify uncertainty, escalate unresolved risk, and preserve institutional memory across long operational timelines.

**This document is subject to its own protocols.** The gate logic, checklist, and audit trail requirements apply to revisions of this document as much as to any other.

---

---

## Epistemic Foundation

> **Status:** IMMUTABLE / META-CONSTITUTIONAL
>
> **Core Maxim:** Reality is sovereign. Every process, agent, metric, and protocol — including this one — is merely an imperfect instrument attempting to approach it.
>
> *The sections below (EF-0.0 through EF-0.8b) constitute the constitutional layer of this protocol. They govern how all downstream auditor behavior — the Fallacy Checklist, Verification Gates, Adversarial Battery, Drift Detection — is permitted to operate. They may not be amended without human ratification. They supersede operational convenience. The auditor that cannot challenge them is the auditor that has become the thing it was built to prevent.*

---

### [EF-0.0] The Epistemic Anchor (Axiom Zero)

Objective, verifiable reality holds absolute priority over utility, consensus, elegance, tradition, internal coherence, stability, or any optimization target.

1. **The Primacy Invariant:** No agent, authority, or accumulated system weight may create exemptions from falsification.
2. **The Anti-Distortion Clause:** Any attempt by an agent or subsystem to reinterpret, omit, suppress, or smooth over conflicting empirical data to preserve a downstream goal, performance metric, or higher-level axiom shall be classified as an Epistemic Integrity Violation.
3. **Provisional State Mandate:** The system is strictly prohibited from forcing a logical resolution to maintain operational continuity. When data is scarce, conflicting, or unverified, the system must explicitly flag its state using one of three formal designations:
   - **VERIFIED** — Confirmed via empirical grounding, predictive accuracy, and survived adversarial falsification.
   - **PROVISIONAL** — Temporarily accepted for immediate execution; actively flagged for ongoing validation.
   - **UNKNOWN** — Total epistemic absence. Collapse of UNKNOWN → VERIFIED without new empirical inputs is strictly prohibited.
4. **The Falsification Inversion:** The system shall reward successful falsification equally with successful confirmation. A hypothesis disproven is information gained. Detection of error represents improvement, not failure. Auditors must not treat the absence of contradiction as evidence of correctness — only as absence of detection.

---

### [EF-0.1] The Epistemic Filter (What Is Not Evidence)

During any audit loop, red-teaming cycle, or cross-node reconciliation, the following are explicitly disqualified as proof of validity. They may inform hypothesis generation but may never serve as verification:

- **Fluency and Coherence** — Persuasive narrative structure, syntactical elegance, or mathematical beauty are not evidence of fact.
- **Agent Consensus** — Agreement among multiple agents — including cross-model validation — is social proof, not empirical proof. Sybil-style alignment is not truth. See Challenge Class 9 (Epistemic Corruption).
- **Systemic Utility** — The fact that a premise keeps a node stable, satisfies a user requirement, or avoids an audit block does not make the premise true.
- **Precedent and Longevity** — Historical persistence, training data dominance, or institutional embedding does not shield a model from immediate falsification by a single piece of fresh, valid, contradictory data.
- **Correlation** — Observed association does not establish causation. Repeated coincidence may generate hypotheses but not conclusions.
- **Repetition** — A claim repeated many times remains a claim. Training prevalence or frequency of retrieval does not constitute verification.
- **Confidence** — High confidence, low-entropy outputs, or high certainty scores are not evidence. Calibration must remain subordinate to empirical testing.
- **Compression** — Elegant explanations and minimal models are preferred for computational efficiency but possess no privileged claim to truth. Occam's Razor is a heuristic, not a proof.

---

### [EF-0.2] Epistemic Decay Protocol (Behavioral Triggers)

The Auditor Subsystem tracks qualitative behavioral anomalies to detect systemic drift. Hard numerical thresholds are deferred to later specification maturity; behavioral triggers are operative now.

**Level 1 — Emergent Contradiction**

Triggers:
- Confidence-to-accuracy mismatch: agent outputs high-certainty strings that fail basic syntactic or tool-return validation.
- Heterogeneous disagreement: cross-model validation yields diametrically opposed logical paths on identical inputs.
- Localized uncertainty calibration failure across a sidecar section.

Immediate action: **Internal Red-Team Challenge.** Force the suspect agent to defend its underlying assumptions against a dedicated Devil's Advocate posture. Log findings as unknowns if unresolved.

**Level 2 — Persistent Contradiction**

Triggers:
- Repeated prediction failure: subsystem models fail to predict the state of external tool outputs or sensor data across more than three execution cycles.
- Sycophancy loop: agent alters its conclusion based on a change in user tone or prompt framing while the underlying data remains static.
- Direct sensory-to-logic conflict persisting across audit cycles.

Immediate action: **Subsystem Quarantine.** Freeze downstream optimization and specification promotion for the affected node. Force out-of-band external grounding. Halt autonomous audit progression and require human review.

**The auditor may not simply lock a node and wait.** Upon triggering Level 2, the Auditor Subsystem is operationally bound to generate a **Falsification Vector Profile** — a minimal, atomic statement of the specific assumption or data conflict that caused the freeze — and log it as an Epistemic Ledger entry. The profile must be specific enough that downstream engineering nodes can actively route around the blocked assumption or target it for physical remediation. A quarantine without a Falsification Vector Profile is Audit Theater.

**Graceful degradation rule:** If a blocked specification cannot be grounded within the current cycle, the Auditor shall demote the affected file's maturity state to the highest level consistent with its verified claims rather than holding the entire document in indefinite suspension. A structurally sound lower-capability baseline that matches verified reality is preferable to a higher-capability baseline that cannot be grounded.

**Level 3 — Integrity Violation**

Triggers:
- Documented suppression or omission of contradictory evidence.
- Attempted alteration or deletion of Epistemic Ledger entries.
- Optimization process overriding observation data to preserve a metric target.
- History tampering: alteration of audit trail entries, sidecar IDs, or resolution logs.

Immediate action: **Epistemic Reset.** Immediate termination of active agent authority over the affected node. Roll back to last verified checkpoint. Trigger mandatory human governing party review. Log as AP-class governance unknown.

**The auditor may not simply halt and defer.** Upon triggering Level 3, the Auditor Subsystem must output the specific integrity violation as a named Epistemic Ledger entry before suspending. The entry must identify: (1) what was suppressed, altered, or overridden; (2) what verified state existed before the violation; (3) what the violation was attempting to preserve. This produces a recoverable audit trail rather than a silent halt. A reset without a logged violation profile is itself an integrity failure.

---

### [EF-0.3] The Epistemic Ledger

All core model changes, parameter updates, or physical constant revisions must be immutably recorded with five explicit fields. The ledger is the system's memory of how reality corrected it.

```
[ENTRY_ID]
├── 1. Previous Premise:        (The legacy belief or model state)
├── 2. Contradictory Evidence:  (The exact sensor payload, failed prediction, or falsification result)
├── 3. Falsification Method:    (How the contradiction was systematically established)
├── 4. Updated State:           (The new PROVISIONAL or VERIFIED model state)
└── 5. Confidence Interval:     (The newly calibrated, explicit margin of uncertainty)
```

Ledger entries may be created only upon genuine falsification or empirical update — not upon consensus shift, aesthetic preference, or optimization pressure.

---

### [EF-0.4] Auditor Fallibility (The Meta-Corruption Clause)

The Auditor Subsystem possesses no exemption from Axiom Zero.

Auditor conclusions are themselves PROVISIONAL and subject to continuous challenge, adversarial examination, and empirical falsification. The detection apparatus shall not be considered evidence of correctness merely because it occupies an oversight role.

**Guardians require guardians.**

The auditor that declares itself beyond falsification has become the first target of its own protocol.

---

### [EF-0.5] Anti-Sacralization Principle

Repository age, constitutional status, historical success, or institutional authority shall grant no document immunity from challenge.

Stability derives from repeated successful verification rather than accumulated prestige. Preservation of a known error for the sake of continuity constitutes an immediate Integrity Failure.

This principle applies explicitly to:
- `Admin/Discovery.md`
- `Admin/Governance_Charter.md`
- `Admin/Auditor_Protocols.md`
- All localized interpretations of Axiom Zero itself

A document that cannot be challenged is not a document. It is doctrine. Doctrine is what this protocol exists to prevent.

---

### [EF-0.6] Goodhart's Law Defense (Optimization Corruption)

Metrics are indicators, not objectives. When a measurement becomes a target, its value as evidence deteriorates.

No optimization process may override contradictory observations in order to preserve metric performance or keep a KPI artificially green. When a metric is gamed, it stops measuring the thing it was designed to measure and begins measuring the gaming itself.

This applies directly to:
- Gate passage rates
- Unknown count targets
- Adversarial finding ratios
- Protocol Performance metrics defined in this document

---

### [EF-0.7] Process Supervision and Chain-of-Custody Mandate

Agents shall be evaluated and selected based on the structural integrity of their reasoning pathways, not the utility of their final outputs.

1. **The Machiavellian Gap Check:** The system must actively monitor divergence between an agent's internal scratchpad logic and its public user-facing output. A wide divergence — telling the user what they want to hear while tracking reality internally — triggers an immediate Level 2 Quarantine.
2. **Heuristic Subordination:** While tools like Occam's Razor are authorized for computational efficiency, they hold no privileged claim to truth. If an elegant model conflicts with a high-entropy empirical data payload, the system must maintain the raw data and flag the model as PROVISIONAL.
3. **The Epistemic Forensic Standard:** Every conclusion must possess an inspectable lineage. The Auditor shall continuously reconstruct the path from observation to conclusion, identifying where assumptions, compression, abstraction, or optimization entered the chain. Key diagnostic questions: Where did this belief originate? Which assumptions were introduced? Which evidence was discarded? Was uncertainty preserved? Did utility distort interpretation?

---

### [EF-0.8] The Grounding Vector (Software Reality Anchors)

For the purposes of this protocol, "Objective Reality" is operationally defined — at the software layer — as:

- **Determinism of Code Execution:** Compilable, syntax-checked code that executes without runtime errors constitutes a harder claim than any narrative assertion about it.
- **Immutable Telemetry:** Direct, unparsed sensor inputs, cryptographic hashes, and file-system realities supersede agent description of those inputs.
- **Falsification via Tooling:** If an agent claims a file exists, the file system tool must return true. If it returns false, the agent's internal state is instantly overridden. No narrative explanation may bypass this check.

Agent narratives about tool outputs are PROVISIONAL until tool confirmation is logged.

---

### [EF-0.8b] The Grounding Vector (Physical Reality Anchors)

The software-layer grounding vector is necessary but insufficient for a physical fabrication and recovery system.

For LazarusForgeV0, physical reality is the harder floor:

- **Empirical Measurement Priority:** Sensor telemetry, material assay outputs, and measured physical constants supersede any model, simulation, or agent inference about the same values. A simulation confirming a simulation is not external grounding.
- **Physical Constant Immutability:** No optimization pressure, agent narrative, or governance document may override a measured physical constant. If a measured value contradicts a design parameter, the design parameter is PROVISIONAL pending resolution — not the measurement.
- **Fabrication Outcome Precedence:** Physical test results, material failure modes, and operational outcomes from actual hardware supersede specification-layer predictions. A spec that has never been tested by physical reality holds PROVISIONAL status regardless of internal coherence.
- **No Self-Confirming Simulations:** A computational model cannot be grounded by running itself. Grounding requires an independent physical measurement or a test result from hardware that exists outside the model's own assumptions.

*This section directly addresses the gap where [EF-0.8] alone would permit an agent to satisfy external grounding requirements by running a simulation that confirms itself — a closed epistemic loop wearing the clothes of verification.*

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence | Expiry Trigger                                      |
|---------|----------------------------------------------------------------------------|------------------------------------|------------|-----------------------------------------------------|
| ASM-001 | Auditors may include both humans and autonomous agents                     | Current repository architecture    | High       | Repository governance changes                       |
| ASM-002 | Verification gates remain repository-wide canonical requirements           | `Admin/Verification_Gates_LF.md` dependency| Medium     | Gate structure revision approved                    |
| ASM-003 | Most repository files will remain partially incomplete for long periods    | Current Forge development state    | High       | Repository reaches stable Specification maturity    |
| ASM-004 | Autonomous agents may attempt optimization shortcuts during audits         | Observed LLM behavior patterns     | High       | Proven resistant audit architecture established     |
| ASM-005 | Multi-agent audit cycles are the expected norm, not the exception          | Current workflow trajectory        | High       | Single-agent workflow formally adopted              |

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`

The auditor equivalent:

> Confidence never outruns verification.

These two principles operate in parallel. One governs what the Forge is allowed to do. The other governs what the Forge is allowed to claim.

**Scope boundary:** Human override rights under this protocol apply to verification process decisions only. They do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in `Admin/Ethical_Constraints.md`.

---

## Exploration vs. Specification

**Exploration** — Allowed to be incomplete, speculative, and loosely connected. Do not over-police.

**Specification** — Must pass all verification gates before commit. Claims are binding, cross-references must resolve, and quantitative values must be labeled.

**The loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

**Design rule:** These protocols apply only when promoting content toward specification. Misapplying verification pressure to exploratory thinking is itself a failure mode.

---

## Core Auditor Doctrine

Auditors are not authors, advocates, marketers, or speculative futurists.

Auditors exist to:
- Detect contradiction
- Detect unsupported claims
- Detect hidden assumptions
- Detect semantic drift
- Detect audit theater
- Preserve uncertainty honestly
- Prevent premature Specification promotion
- Preserve institutional memory
- Protect repository coherence over time

An auditor's responsibility is reality alignment, not progress acceleration.

Passing an audit is not evidence of correctness. Failing to detect instability is itself an audit failure.

---

## Auditor Role Classes

### Skeptic Auditor

**Primary responsibility:** Challenge assumptions, search for contradiction, stress-test coherence, escalate unsupported certainty.

**Default stance:**
> "What evidence would invalidate this claim?"

**Prioritizes:** Internal coherence, assumption exposure, scope containment, semantic precision.

---

### Systems Auditor

**Primary responsibility:** Cross-module integration review, dependency mapping, interface consistency, architectural drift detection.

**Default stance:**
> "What breaks if this changes?"

**Prioritizes:** Interface compatibility, canonical terminology preservation, ownership clarity, dependency stability.

---

### Evidence Auditor

**Primary responsibility:** Verification source integrity, confidence label enforcement, traceability validation, replication analysis.

**Default stance:**
> "How do we know this is true?"

**Prioritizes:** Measurement quality, evidence provenance, replication pathways, distinction between observed vs. inferred claims.

---

### Ethical Auditor

**Primary responsibility:** Harm detection, governance erosion detection, unsafe omission detection, ethical anchor preservation.

**Default stance:**
> "What failure mode harms operators or downstream systems?"

**Prioritizes:** Safety visibility, operator survivability, misuse resistance, ethical anchor integrity.

---

### Synthesizer / Connective Tissue

Not a standalone auditor class — a mode declaration for agents contributing integration, bridging, or cross-module coherence work during an audit cycle. Must still operate under auditor constraints when reviewing existing content.

---

## Role Declaration Requirement

All contributors — human and autonomous — must declare their operating role before contributing:

> *"Operating as [Role] per Auditor_Protocols.md v0.11"*

**Valid roles:** Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

Role shifts must be declared before proceeding. Undeclared role shifts are a drift indicator.

---

## Audit Entry Conditions

An audit may begin only if:
- The file contains a valid File State block
- Scope Boundary exists
- Ethical Anchor field exactly matches canonical wording
- Sidecar remains below mandatory escalation thresholds
- Frozen sections are visibly marked
- File ownership is identifiable

If any requirement fails:
1. Halt Specification progression
2. Log a governance-level unknown
3. Downgrade trust classification
4. Require remediation before continuing

---

## Audit Sequence

Audits proceed in the following order. Skipping sequence stages is prohibited unless explicitly documented with rationale.

| Phase | Purpose                          |
|-------|----------------------------------|
| 1     | Structural validation            |
| 2     | Scope validation                 |
| 3     | Assumption extraction            |
| 4     | Internal coherence review        |
| 5     | Cross-module consistency review  |
| 6     | Evidence validation              |
| 7     | Drift detection                  |
| 8     | Unknown classification           |
| 9     | Resolution pathway assessment    |
| 10    | Gate status determination        |

---

## Structural Validation (Phase 1)

Auditors must verify:
- Mandatory sections exist in canonical order
- Section ordering matches File_Template.md structure
- Frozen markers are correctly scoped
- Confidence labels exist on quantitative claims
- Footer governance sections remain separated from Body content
- Ethical Anchor field is exact and intact

Structural compliance is necessary but never sufficient for Specification promotion.

---

## Scope Validation (Phase 2)

Auditors must identify:
- Specification bleed
- Duplicate ownership
- Hidden interface assumptions
- Governance content inside operational sections
- Operational content hidden in sidecars

If scope ambiguity exists:
- Open a dispute if interpretation conflict exists
- Open an unknown if ownership reality is unclear

---

## Assumption Extraction (Phase 3)

Auditors must actively search for:
- Environmental assumptions
- Material assumptions
- Infrastructure assumptions
- Human skill assumptions
- Resource availability assumptions
- Safety assumptions
- Simulation simplifications

Hidden assumptions must either:
- Move into the Assumptions section
- Move into Unknowns if indefensible
- Be removed entirely

Assumptions are not evidence. An assumption that can no longer be defended becomes an Unknown.

---

## The Fallacy Checklist

Apply to all specification-level claims. Bare checkmarks are not verification — substantive notes required for non-trivial claims (1–2 sentences minimum stating what was checked, what nearly failed, and what was adjusted).

**1. Magic Energy**
Does the design assume energy is available without accounting for its source, storage, or conversion losses? Every watt must have a traceable origin. Cross-reference `Operations/Energy.md`.

**2. Friction Blindness**
Does the design ignore mechanical resistance, thermal losses, fluid drag, or interface wear? Real systems degrade. Specifications that assume ideal conditions are not specifications — they are wishes.

**3. Energy Density Paradox**
Does any recovery, recycling, or bootstrapping step consume more than it produces? Justify as enabling investment or flag. Recovery that costs more than it recovers is reduction dressed as progress.

**4. Semantic Drift**
Has a term changed meaning between documents without a documented revision? Cross-check against `Architecture/Forge_flow.md` as the reference standard.

**5. Scope Creep Disguised as Refinement**
Does a revision quietly expand claimed capabilities beyond what the current version can demonstrate? New capabilities belong in `Admin/Trajectories.md`.

**6. Hallucinated Files or Cross-References**
Does the document reference a file that does not exist? All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified. Aspirational references must be labeled *planned*. Repository uses folder-prefixed paths — do not flag folder-prefixed canonical names as failures.

**7. Confidence Without Basis**
All quantitative claims must carry one of four labels:
- **Measured** — derived from real experimental data
- **Estimated** — derived from analog systems with documented scaling factors
- **Analogous** — drawn from similar documented systems
- **Placeholder** — provisional, pending verification

Unlabeled numbers are assumed Placeholder. False precision labeled "estimated" is still a violation.

**8. Lifecycle Truncation**
Every module specification must include: Degraded Operation, Failure Modes & Detection, Maintenance Access, End-of-Life / Recycling Path. A specification describing only the working state is incomplete.

**9. Incomplete by Omission**
What critical subsystem is missing? Common omissions: heat dissipation, waste stream management, human interface requirements, power draw under load. Absence of mention is not evidence of absence of need.

**10. The Turd Problem**
Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this. It is memorable and functionally precise.

---

## Evidence Classification and Institutional Truth Provenance Hierarchy
*§AP-006 — Payment via Specification. Closes AP-006 (logged 2026-05-23). Constitutional anchor: Axiom Q-1 (Reality Grounding) and EF-0.0 (Epistemic Anchor).*

All meaningful claims require two orthogonal classifications: a **quantitative confidence label** describing how well-supported the claim is, and an **institutional provenance label** describing how the claim was derived. These dimensions are independent — a claim can be high-confidence but internally derived, or low-confidence but empirically measured. Both must be stated.

### Quantitative Confidence Labels

| Label       | Meaning                                              |
|-------------|------------------------------------------------------|
| Measured    | Directly observed and recorded from physical reality |
| Replicated  | Independently repeated across separate instances     |
| Simulated   | Derived from computational or procedural models      |
| Analogous   | Inferred from related but distinct systems           |
| Placeholder | Included pending verification — no confidence basis  |

Placeholder claims may not justify Specification promotion.

### Institutional Provenance Labels

| Label                    | Meaning                                                                 | Maximum Permitted Epistemic State |
|--------------------------|-------------------------------------------------------------------------|-----------------------------------|
| Internally Derived       | Supported primarily through repository logic, modeling, or agent reasoning | PROVISIONAL only                |
| Analogous External       | Derived from comparable external systems not yet directly tested here   | PROVISIONAL only                  |
| Experimentally Verified  | Validated through documented testing with recorded outcomes             | VERIFIED permitted                |
| Operationally Hardened   | Repeatedly validated across multiple operational cycles under real conditions | VERIFIED (strongest form)    |

**The provenance ceiling rule:** No internally-derived claim may be represented as VERIFIED regardless of internal coherence, agent consensus, or elegance. Promotion from PROVISIONAL to VERIFIED requires a provenance upgrade — meaning new empirical input that did not exist when the claim was first made. This directly operationalizes Axiom Q-1 (all authority claims must terminate in verifiable external artifacts) and EF-0.0 (collapse of UNKNOWN or PROVISIONAL to VERIFIED without new empirical input is prohibited).

**Provenance collapse** — the silent upgrade of Internally Derived claims to Operationally Hardened status through repetition, consensus, or institutional weight — is an Epistemic Integrity Violation under EF-0.0 §2 (Anti-Distortion Clause) and triggers EF-0.2 Level 1 at minimum.

**Cross-reference:** FN-001 (fabrication node grounding requirements), CF-002 (confidence failure modes). Full constitutional grounding: EF-0.0, Axiom Q-1 in `Admin/Governance_Charter.md`. Operational condensation: `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

---

## AI Contribution Protocols

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed. State uncertainty for anything else.

**Rule 2 — Role Declaration:** Declare role before contributing. Declare role shifts before proceeding.

**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.

**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them. Refusal is a success of the protocol.

**Rule 5 — Confidence Labeling:** Use the four-label system. Unlabeled = Placeholder.

**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades.

**Rule 7 — Repository Structure Awareness:** The repository uses folder-based structure (Admin/, Architecture/, Operations/, Tests/). Legacy flat filenames are aliases documented in the Rename Registry in `Discovery.md`. Use canonical folder-prefixed paths in all new contributions.

**Trust the process, not the predecessor.**

---

## Human Contributor Protocols

- Label estimates as estimates. "I think it works" is not a specification claim.
- Resolve all cross-references before committing. Planned files must be explicitly labeled.
- Overrides of AI auditor flags must be documented with reasoning. Undocumented overrides are indistinguishable from ignored warnings.
- Override rights apply to verification process decisions — not to Ethical_Constraints hard-line doctrines.
- Lifecycle template (Fallacy #8) applies to human-authored module specs.

---

## Decentralized Audit Architecture (Sidecar Model)

### The Problem

A centralized unknowns registry that stores full entry detail grows without bound. When it exceeds practical token limits, the governance system fails the thing it governs.

### Local Ledgers + Global Index

**Local Ledger (Sidecar):** Every specification file contains an `## Auditor Notes & Unknowns` section at the footer. Module-specific unknowns live here.

**Global Index:** `Unknowns.md` is a cross-module index only — summary table, dependency map, systemic risks spanning multiple files, audit trail, resolved archive. Full entry detail lives in the owning file's sidecar.

### Sidecar Format

Full sidecar format is defined in `Admin/File_Template.md` Section 8. Local IDs use file abbreviation + three digits: `AP-001` (Auditor Protocols), `SC-001` (Separation Thermal), `GI-001` (Gate Intake), etc. Cross-module unknowns use global `UNK-XXX` format and are indexed in `Unknowns.md`.

### The 10-Entry Rule

More than 10 distinct open entries in a sidecar flags the file for a Resolution Pass before the next audit cycle.

### Metadata Guardrail

If sidecar content exceeds 20% of total document word count, flag for Resolution Pass before auditing. Flag is strong — not a hard refusal. Proceed if human contributor explicitly acknowledges.

**Epistemic Ledger exemption (§AP-009):** Active `[ENTRY_ID]` Epistemic Ledger blocks are excluded from the 20% calculation. The guardrail measures governance debt — stale unknowns, unresolved disputes, and administrative overhead. It does not measure epistemic health. A document actively logging falsification records under EF-0.3 should not be penalized for compliance with the constitutional layer. Excluded blocks must be syntactically valid five-field ledger entries. Orphaned or malformed ledger entries do not qualify for exemption and count toward the guardrail threshold.

### Resolution Pathways

Every unknown must terminate through one pathway:

| Pathway                    | Meaning                                                              |
|----------------------------|----------------------------------------------------------------------|
| Payment via Specification  | Verified and integrated into Body as committed spec                  |
| Discharge via Trajectory   | Real but out of scope; route to Admin/Trajectories.md                |
| Discharge via Lessons Learned | Resolved by operational experience; lesson recorded, entry closes |

Unknowns may not remain permanently ownerless.

**Crystallization principle:** Every unknown that moves from sidecar into specification body makes the document more deterministic. A shrinking sidecar is a maturing document.

---

## Unknowns Registry

**Where unknowns live:**
- Module-specific — in the file's own sidecar
- Cross-module — in `Unknowns.md` global index, owning file noted
- Navigation — in `Discovery.md`

**Priority tags:** Blocking | Non-blocking | Exploratory

**The Expiry Rule:** For global index entries — if a Blocking or Non-blocking unknown remains without a documented Resolution Path for more than two audit cycles, escalate to Systemic Risk or demote the dependent module.

**Expiry check:** Skeptic/Auditor role opens each audit cycle by reviewing the global index for entries approaching two cycles.

A verification pass that surfaces no unknowns on a complex document should itself be treated with suspicion.

---

## Dispute Handling Protocol

Disputes represent interpretation conflicts, not missing information.

Auditors must distinguish:
- **Unknowns** = missing reality alignment
- **Disputes** = conflicting interpretations

Persistent disputes are acceptable if explicitly tracked. Silent disappearance of disputes is prohibited.

Disputes open across three consecutive audits must be escalated to `Unknowns.md` for repository-level resolution.

---

## Verification Gate Enforcement

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass audit by a different agent to override.

| Gate | Test                                                        | Fail →                                       |
|------|-------------------------------------------------------------|----------------------------------------------|
| G1   | Fallacy Check actively applied with substantive notes?      | Return to author                             |
| G2   | Physical plausibility — no violation of known constraints?  | Return for revision                          |
| G3   | Adversarial Challenge Battery applied?                      | Must undergo adversarial testing — see below |
| G4   | Scope alignment — fits current version or trajectory?       | Route to Admin/Trajectories.md               |
| G5   | Cross-reference integrity — all paths resolve?              | Hold at draft                                |
| G6   | Conflict check — no contradiction with existing specs?      | Resolve conflict before committing           |

**Gate 3 is formally gated on the Adversarial Audit Layer.** A single concrete failure scenario is insufficient. The Adversarial Challenge Battery below defines the minimum requirement.

---

## Adversarial Audit Layer

### Purpose

The adversarial layer exists to challenge hidden assumptions, institutional blind spots, semantic ambiguity, operator incentives, recursive self-validation, and failure propagation pathways. Its purpose is not criticism for its own sake — it is resilience hardening.

> A protocol is not considered robust until it has survived deliberate hostile analysis.

The strongest audit systems are not optimized to prove correctness. They are optimized to discover how reality can still break the model despite apparent correctness.

### When to Apply

The full Adversarial Challenge Battery is required for:
- Any document being considered for Specification promotion
- Any document governing irreversible actions (Gate_03_Reduction.md, Ethical_Constraints.md)
- Any document in the trust chain for autonomous systems (Electronics.md, Cognitive_Frameworks.md)
- Any document that has passed G1 and G2 but still feels wrong

Partial application (selected challenge classes) is acceptable for Exploration-stage documents. Document which classes were applied and why others were deferred.

---

### The Adversarial Challenge Battery

Ten challenge classes. Each requires at least one concrete scenario, not a general acknowledgment.

---

**Challenge Class 1 — Assumption Inversion**

Tests whether a protocol only works because hidden assumptions remain true.

Ask: *What if the operator is wrong? What if the sensor data is fabricated? What if the environment is hostile instead of cooperative?*

*Minimum requirement:* Name three hidden assumptions in the document and describe what happens when each fails.

---

**Challenge Class 2 — Failure Amplification**

Instead of asking "Can this fail?" ask "How does this fail catastrophically?"

Reveals cascading failures, hidden coupling, and latent propagation pathways. A protocol that survives only isolated failures is fragile.

*Minimum requirement:* Trace one failure from its origin through at least two downstream consequences.

---

**Challenge Class 3 — Incentive Corruption**

Ask: *How could a smart operator game this protocol while appearing compliant?*

Examples: throughput over safety, hiding uncertainty to avoid delays, fabricating confidence metrics to meet targets.

If the answer exists and no countermeasure exists, the protocol is vulnerable.

*Minimum requirement:* Identify one incentive corruption path and name the countermeasure or log it as an unknown.

---

**Challenge Class 4 — Semantic Drift Attacks**

Ask: *Can two operators interpret this differently and still claim compliance?*

Terms that commonly drift: "safe" / "contained" / "stable" / "acceptable" / "hold" / "clear" / "sufficient."

*Minimum requirement:* Identify one term that could be interpreted differently by two operators. Either tighten the definition or log the ambiguity as an unknown.

---

**Challenge Class 5 — Unknown Unknown Pressure Tests**

Ask: *What would this system do if it encountered a material, process, or state it has never seen before?*

A resilient protocol degrades safely under uncertainty rather than failing catastrophically or routing unknowns forward as knowns.

*Minimum requirement:* Describe what the protocol does when it encounters a condition outside its defined envelope. If the answer is "undefined," log it as an unknown.

---

**Challenge Class 6 — Recursive Justification Loops**

Example loop: Protocol says system is safe → system passed protocol → therefore system is safe.

The audit itself becomes the evidence. Documentation replaces reality. Audit theater develops.

Ask: *What external reality check exists beyond self-reference?*

*Minimum requirement:* Identify one claim validated only by other repository documents. Either ground it in external reality or label it explicitly as internally derived.

---

**Challenge Class 7 — Human Fatigue and Cognitive Erosion**

Ask: Does this protocol remain safe after 12 hours of repetition? Does it survive shift handoff? High backlog? An undertrained operator?

Normalization of deviance — where slightly wrong becomes the new normal through repetition — is a documented cause of major industrial incidents.

*Minimum requirement:* Identify one step that degrades under sustained operation. Either add a safeguard or log it as an unknown.

---

**Challenge Class 8 — Malicious Actor Simulation**

Distinct from incompetence — this is intentional abuse by a knowledgeable actor.

Examples: falsify intake records, poison melt streams, inject corrupt documentation, plant compromised hardware in salvage stream.

*Minimum requirement:* Identify one malicious actor scenario relevant to the document and name the countermeasure or log it as an unknown.

---

**Challenge Class 9 — Epistemic Corruption**

Distinct from malicious actors — systematic degradation through well-intentioned but incorrect contributions.

Examples: consensus weighting suppresses a truthful minority contribution; high-confidence entries decay without revalidation; three AI models with overlapping training data converge on the same wrong answer.

Ask: *How does this system distinguish confident truth from confident error?*

*Minimum requirement:* Identify one mechanism by which incorrect information could achieve high confidence. Name the countermeasure or log it as an unknown.

---

**Challenge Class 10 — Systemic Coupling and Cascade**

Ask: *If this module fails, what fails with it? What fails second? What fails third?*

Current high-coupling documents:
- `Admin/Auditor_Protocols.md` — failure here degrades all other files
- `Operations/Electronics.md` — failure here compromises the trust anchor
- `Architecture/Forge_flow.md` — failure here corrupts all gate routing
- `Architecture/Forge_Net.md` — failure here propagates across the ecology

*Minimum requirement:* Trace this document's failure footprint through at least two levels of downstream dependency.

---

### Adversarial Audit Sign-Off Format

```
Adversarial Challenge Battery:
- Classes applied: [list]
- Classes deferred: [list with reason]
- Findings per class: [ID or "None"]
- New unknowns from adversarial pass: [list]
- Highest-risk finding: [one sentence]
```

---

### Anti-Patterns the Adversarial Layer Exists to Prevent

| Anti-Pattern               | Description                                            | Challenge Class        |
|----------------------------|--------------------------------------------------------|------------------------|
| Audit theater              | Protocol passes without surfacing real gaps            | 6 — Recursive justification |
| Specification cosplay      | Exploratory content dressed as operational spec        | 1 — Assumption inversion |
| Confident wrongness        | High consensus on incorrect answer                     | 9 — Epistemic corruption |
| Throughput pressure override | Safety bypassed under operational load               | 3 — Incentive corruption |
| Silent failure accumulation | Failures not logged because minor or embarrassing     | 7 — Human fatigue      |
| Semantic compliance        | Letter of protocol followed, spirit violated           | 4 — Semantic drift     |
| Single-point doctrine      | Protocol only works if one assumption holds            | 5 — Unknown unknowns   |
| Cascade blindness          | Local fix that creates downstream failure              | 10 — Systemic coupling |

---

## Drift Detection Protocol

Auditors must actively monitor for:
- Terminology mutation
- Contradiction accumulation
- Governance leakage into operational sections
- Unknown accumulation across consecutive audits
- Audit metric gaming
- Confidence inflation
- Frozen-section erosion
- Ethical anchor degradation
- Sidecar expansion instability
- Role shifts without declaration

Drift detection failure is considered a protocol failure.

### Compound Drift Escalation

If two or more Drift Indicators activate simultaneously:
1. Halt autonomous Specification progression
2. Downgrade repository trust state
3. Require human review
4. Open governance-level unknown entry

Compound instability is treated as systemic risk, not isolated failure.

---

## Specification Promotion Rules

A file may only reach Specification status if:
- All six canonical gates pass
- Open unknowns are non-blocking
- Evidence quality supports certainty level
- Drift indicators are inactive
- Scope boundaries remain stable
- Frozen sections are justified
- Sidecar governance thresholds remain compliant

Specification is reversible if instability later emerges.

---

## Autonomous Auditor Constraints

Autonomous agents must not:
- Silently rewrite verified sections
- Collapse uncertainty into certainty
- Delete historical failures
- Remove disputes without resolution logging
- Merge scope boundaries implicitly
- Invent evidence
- Reclassify Placeholder evidence as Measured
- Ignore Ethical Anchor degradation
- Optimize for repository appearance over correctness
- Reopen hard-stopped Abandoned Paths without explicit human authorization

Repository cleanliness is not repository integrity.

---

## Human Override Doctrine

Human operators may override audit outcomes.

Overrides must:
- Be explicit
- Be dated
- Include rationale
- Record accepted risk
- Preserve audit traceability

Undocumented overrides are governance failures.

Override rights apply to verification process decisions. They do not extend to Anti-Weaponization or Life Preservation hard-line doctrines in `Admin/Ethical_Constraints.md`.

---

## Full Stop Review

Invoke when a spec passes all gates but exhibits systemic inconsistency or unclear real-world viability. Resets to Gate 1 with focus on foundational premise.

**Trigger conditions:**
1. Same foundational claim blocked across two separate audit cycles
2. New finding invalidates core premise of a previously promoted specification
3. Pattern of documented overrides eroding a governance principle without explicit revision
4. Multiple Adversarial Challenge Battery findings converging on the same structural gap

**Invocation record:** Triggering agent, triggering concern (one falsifiable sentence), date and document version, outcome. Record belongs in the document's sidecar audit trail.

---

## Cross-Repo Verification

Any cross-repo dependency must be documented in both repositories with a stated assumption contract. The dependency is not verified until both sides acknowledge it.

*Astroid-miner is a planned repository, intentionally deferred until Leviathan deployment is underway. Cross-repo verification applies to `Lazarus-Forge-` now; Astroid-miner activates at that milestone.*

---

## Observability & Audit Trail

**Required audit trail fields:**
- Document audited and version
- Auditor role and agent identity
- Date or audit cycle identifier
- Gates cleared (list)
- Gates blocked (list with reason)
- Unknowns logged (IDs)
- Overrides recorded (with justification)
- Adversarial Challenge Battery summary
- Sign-off statement

**Standard sign-off:**
> *"Verified under Auditor_Protocols v0.11 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides. Adversarial classes applied: [list]. Auditor: [Role/Agent]"*

---

## Protocol Performance

*Metrics are Placeholder pending first full audit cycle completion.*

**Target metrics:**
- Productive block ratio — fraction of blocks resulting in documented improvement
- False-positive refusal rate — blocks overridden with documented justification
- Drift incidents detected per cycle
- Adversarial findings per document — tracks whether adversarial layer is surfacing real gaps

**Anti-Auditor-Capture:** For high-stakes documents, rotate the Auditor role to a different agent model across successive cycles. An auditor reviewing the same document repeatedly without finding new issues warrants the same suspicion as a verification pass surfacing no unknowns.

---

## Failure Modes of This Document

| Failure Mode           | Description                                                      | Mitigation                                                    |
|------------------------|------------------------------------------------------------------|---------------------------------------------------------------|
| Checklist Theater      | Verification becomes ritual                                      | Require substantive notes, not bare checkmarks                |
| Auditor Capture        | Skeptic role softens over time                                   | Binding block authority, documented rebuttal, auditor rotation |
| Version Freeze         | Document stops updating                                          | Explicit revision triggers, self-application of gates         |
| Exploration Suppression| Verification pressure applied too early                          | Exploration vs. Specification distinction enforced            |
| Over-Engineering       | Audit cycle takes longer than writing the contribution           | Simplicity is a design constraint; battery is a minimum       |
| Coherent Nonsense      | Passes all gates but is systemically wrong                       | Full Stop Review, Challenge Class 6                           |
| Metadata Bloat         | Centralized registries grow without bound                        | Sidecar Model, 10-Entry Rule, 20% Rule                        |
| Meta-Recursion Gap     | Protocol cannot fully audit its own enforcement                  | Self-application of gates, auditor rotation; irreducible residual |
| Adversarial Theater    | Adversarial layer becomes a checkbox                             | Concrete scenarios required per class; findings logged as unknowns |

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                              | What Failed                                                        | What Was Learned                                                                          | Confidence | Revalidation Needed |
|----------|---------------|-------------------------------------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | Centralized Unknowns_LF.md as full-entry store              | File grew past token limits; audit prompts failed                  | Unknowns must live locally in owning files; central registry is index only                | Analogous  | No                  |
| May 2026 | Audit Review  | Expiry Rule as primary accumulation mechanism               | Rule had no enforcement path; unknowns aged silently               | Structural constraints (10-entry rule, sidecar) work better than procedural rules         | Analogous  | No                  |
| May 2026 | Audit Review  | Preparatory framing lines in audit prompts                  | Softened auditor findings; masked genuine gaps                     | Documents must stand on their own; scaffolding that stays up becomes load-bearing         | Analogous  | No                  |
| May 2026 | Audit Review  | Gate 3 defined as one concrete failure scenario             | Bar was too low — single scenario leaves most failure modes untested | Adversarial Challenge Battery introduced; Gate 3 now requires battery application        | Analogous  | Yes                 |
| May 2026 | Audit Review  | Consensus treated as truth in multi-agent audit cycles      | Epistemic corruption — ten nodes agreeing on a wrong answer produces confident wrongness | Challenge Class 9 (Epistemic Corruption) added; minority-report preservation required | Analogous  | Yes                 |
| May 2026 | Audit Review  | Lightweight audit outputs without standardized structure    | Audits lacked traceability and escalation consistency              | Audit artifacts require standardized outputs; structured metadata improves reliability    | Measured   | No                  |

---

## Active Disputes

| ID     | Summary                                                                                    | Positions in Conflict                               | Risk   | Status | Owner                    |
|--------|--------------------------------------------------------------------------------------------|-----------------------------------------------------|--------|--------|--------------------------|
| DS-001 | Whether autonomous auditors should ever be allowed to reopen hard-stopped abandoned paths  | Full prohibition vs. conditional supervised reopening | High | Open   | Admin/Auditor_Protocols.md |

---

## Abandoned Paths

| Date       | Path                                                                 | Why Abandoned                                                                                   | Reconsider? |
|------------|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|-------------|
| May 2026   | Single-scenario adversarial pass as Gate 3 requirement               | Bar too low; most failure modes survive single-scenario review                                  | No          |
| May 2026   | Centralized full-entry unknowns registry                             | Token limit failure under operational load; became an obstacle to the governance it was meant to support | No   |
| May 2026   | Preparatory framing lines preceding audit prompts                    | Softened findings; scaffolding became load-bearing and masked genuine gaps                      | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Body contradicts Lessons Learned
- Unknown count increases across three consecutive audits
- Unknown remains unreviewed more than 90 days
- Specification claim lacks a confidence label
- Frozen section modified without a dated justification comment
- Sidecar exceeds 20% of total document word count
- Persistent disputes silently disappear without resolution entry
- Assumptions remain past their expiry trigger without review
- Canonical terminology changes meaning across files
- Ethical Anchor field is absent, altered, or does not match the canonical string
- Role declarations absent from autonomous agent contributions
- Adversarial Battery applications produce zero findings across two consecutive cycles
- Epistemic Foundation sections (EF-0.0 through EF-0.8b) modified without human ratification entry in Resolution Log
- VERIFIED / PROVISIONAL / UNKNOWN state designations absent from document claims where EF-0.0 mandates them
- Epistemic Ledger entries present without all five required fields
- EF-0.8b Physical Grounding Vector removed or merged into EF-0.8 without explicit rationale
- AP-001 through AP-007 Systemic Risk escalation cleared without documented Resolution Pass completing at least one entry to Payment via Specification or Discharge

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

> **SYSTEMIC RISK ESCALATION — 2026-06-21**
> AP-001 through AP-007 have exceeded the 2-cycle expiry threshold by a material margin (estimated 8 cycles). Per Unknowns Registry doctrine, entries aging past threshold without closure must be escalated to Systemic Risk. A Resolution Pass targeting these seven entries is required before the next standard audit cycle. Autonomous specification progression on dependent modules is suspended pending that pass. This escalation was surfaced independently by both Gemini (Skeptic/Auditor) and Grok (Skeptic/Auditor) in the 2026-06-21 dual audit. Logged in Resolution Log.

---

### AP-001 — Auditor effectiveness metrics not yet measured

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-06-21                 |

**Description:** How to measure whether the audit process is actually adding value — productive block ratio, false-positive refusal rate, drift incidents detected per cycle — remains undefined.

**Why It Matters:** Without measurement, the audit protocol cannot demonstrate its own effectiveness. Adversarial Challenge Class 6 (Recursive Justification) applies to the protocol itself — it cannot be its own evidence.

**Resolution Path:** Payment via Specification — define indicator set after first full audit cycle with Adversarial Battery completes. Defining named metrics before a baseline runtime exists introduces Internally Derived structural heuristics that downstream agents will optimize toward before calibration is possible, inducing Audit Theater (EF-0.6). Constraints that must shape the eventual indicator set: (1) all metrics must function as indicators only — not optimization targets; any metric that begins to be optimized for rather than read from triggers EF-0.6 and must be retired or restructured; (2) the indicator set must be derived from observed audit behavior, not specified in advance of it; (3) at minimum one full Battery application cycle must precede any indicator definition. Activation condition: first full Adversarial Battery cycle completed with findings logged. Until then this entry remains In Progress with no committed indicator names.

---

### AP-002 — Override vs. immutability boundary not yet confirmed in both documents

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | Admin/Auditor_Protocols.md |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-06-21                 |

**Description:** Whether the clarification that human override rights do not extend to Ethical_Constraints hard-line doctrines is explicitly stated in both documents in a mutually consistent way.

**Why It Matters:** Inconsistency creates an exploit path — a contributor could claim the boundary doesn't exist because it only appears in one file.

**Resolution Path:** Close when both `Admin/Auditor_Protocols.md` and `Admin/Ethical_Constraints.md` are committed with consistent language confirming the boundary. Partial progress from v0.8: EF-0.4 (Auditor Fallibility) establishes that the auditor itself has no exemption from falsification, and EF-0.5 (Anti-Sacralization) defines what immutability actually means in this system — stability through repeated verification, not through authority. These sections narrow the boundary definition from the AP side. Full closure requires the matching language to be confirmed in `Admin/Ethical_Constraints.md`.

---

### AP-003 — Audit trail schema (machine-readable) deferred

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Low                        |
| Priority      | Minor                      |
| Type          | Technical / Governance     |
| Blocking      | No                         |
| Owner         | Admin/Auditor_Protocols.md |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-06-21                 |

**Description:** A machine-readable format (JSON/YAML) for recording gate passages, blocks, and overrides that can be queried and compared across audit cycles does not yet exist.

**Why It Matters:** Cross-cycle pattern analysis requires structured data, not free text.

**Resolution Path:** Discharge via Trajectory if tooling never materializes — structured markdown remains the permanent format. Activate JSON/YAML when first cross-cycle pattern analysis is needed. Partial progress from v0.8: EF-0.3 (Epistemic Ledger) defines a five-field schema for state corrections that constitutes a partial foundation for any machine-readable format — the five fields (Previous Premise, Contradictory Evidence, Falsification Method, Updated State, Confidence Interval) are the minimum structural unit any AP-003 schema must accommodate.

---

### AP-004 — Cross-auditor disagreement resolution process incomplete

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-22                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The repository lacks a formal mechanism for resolving disagreements between different auditor classes or agent instances within the same audit cycle.

**Why It Matters:** Multi-auditor systems may deadlock or produce inconsistent audit outcomes without an arbitration pathway.

**Resolution Path:** Payment via Specification — define arbitration and escalation pathways for conflicting audit conclusions. May merge with escalation calibration work in `Admin/Governance_Charter.md`. EF-0.1 constraint: arbitration may not resolve disagreements by majority vote or consensus pressure — resolution must ground in empirical artifact, tool return, or physical grounding vector. Active resolution framework (Internally Derived / Placeholder): disagreements between auditor instances escalate through three tiers — (1) Assumption Extraction pass: both agents explicitly state carried assumptions; conflicts at this tier often resolve without arbitration; (2) Empirical Grounding check: the contested claim is submitted to the Grounding Vector (EF-0.8/EF-0.8b) — whichever position is contradicted by tool return or physical measurement is demoted to PROVISIONAL; (3) Human governing party arbitration: if neither position can be grounded empirically within the cycle, the dispute is logged and escalated to human review. The human governing party ruling is logged as an Epistemic Ledger entry with provenance label Internally Derived until physical grounding is available. No auditor agent may unilaterally close a dispute in its own favor.

---

### AP-005 — Verification termination threshold undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The repository lacks formal criteria defining when verification is considered operationally sufficient versus indefinitely expandable.

**Why It Matters:** Without closure criteria, governance pressure can grow recursively and suppress operational progress — infinite audit recursion is itself a governance failure mode.

**Resolution Path:** Payment via Specification — define closure criteria anchored to the governing principle "Verification seeks sufficient falsifiability, not exhaustive certainty." Cross-reference EC-001 (sufficient confidence threshold) for alignment. EF-0.2 relationship: that section defines the escalation triggers (when verification must intensify); AP-005 resolution is the sufficiency complement (when verification is permitted to stop). Active resolution framework (Internally Derived / Placeholder): verification may terminate when all of the following hold — (1) no unresolved contradictions exist between claims and grounding vector returns; (2) the last adversarial Battery application produced no findings that altered the document's epistemic state claims; (3) all sidecar unknowns carry documented resolution paths; (4) the document's provenance labels are internally consistent with the institutional hierarchy defined in §AP-006. These are necessary conditions, not sufficient — the human governing party must ratify termination for any document promoted past Candidate Spec. Full specification requires cross-referencing EC-001 once that entry matures.

---

### AP-006 — Institutional truth provenance hierarchy undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                   |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Epistemic     |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The repository distinguishes quantitative confidence labels but not institutional truth provenance levels — the distinction between internally derived coherence and externally validated reality.

**Why It Matters:** Internally coherent documentation can be mistaken for operationally hardened truth, producing provenance collapse and recursive justification loops.

**Resolution:** Payment via Specification — 2026-06-21. Four institutional provenance labels (Internally Derived / Analogous External / Experimentally Verified / Operationally Hardened) formalized into the Evidence Classification and Institutional Truth Provenance Hierarchy section (§AP-006). Provenance ceiling rule defined: no internally-derived claim may reach VERIFIED status. Provenance collapse classified as Epistemic Integrity Violation under EF-0.0 §2. Constitutional anchor: Axiom Q-1 and EF-0.0. Operational condensation in `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels. Cross-references to FN-001 and CF-002 confirmed.

---

### AP-007 — Repository integrity and doctrine lineage protections undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | In Progress                |
| Risk          | High                       |
| Priority      | Major                      |
| Type          | Governance / Security      |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-23                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The repository lacks explicit operational doctrine for audit history integrity, rollback detection, canonical-path authority, and institutional memory corruption at the auditor protocol level.

**Why It Matters:** Governance systems become fragile if repository state itself cannot be trusted — stale doctrine can masquerade as current policy, fabricated resolution logs can close unknowns without evidence, and silent rollback can erase lineage.

**Resolution Path:** Payment via Specification — define repository integrity requirements in the Autonomous Auditor Constraints and Drift Detection sections. Cross-reference GOV-003 (integrity enforcement architecture) — that entry covers constitutional enforcement; this entry covers operational auditor doctrine. Distinct but linked. Partial progress from v0.8: EF-0.3 (Epistemic Ledger) directly addresses lineage preservation — all core state corrections must be immutably recorded with five fields, and ledger entries may only be created on genuine falsification. EF-0.2 Level 3 explicitly classifies history tampering and alteration of audit trail entries as Integrity Violations triggering Epistemic Reset and mandatory human governing party review. These two sections constitute the doctrine layer of AP-007's resolution; the remaining gap is the enforcement layer — how tampering is detected structurally rather than declared textually. That enforcement gap feeds into GOV-003 and AP-008. The Gemini (2026-06-21) recommendation to add SHA-256 upstream parity checks belongs here as the next concrete resolution step, to be specified in `Admin/Security_Protocols.md`.

---

---

### AP-008 — Technical implementation of quarantine actions undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | High                       |
| Priority      | Major                      |
| Type          | Technical / Governance     |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-21                 |

**Description:** Sections [EF-0.2] (Epistemic Decay Protocol) and [EF-0.7] (Machiavellian Gap Check) define operational actions — "Subsystem Quarantine," "Halt autonomous audit progression," "Epistemic Reset" — as descriptive text. No software interface, structural signaling mechanism, exit code schema, file system lock protocol, or CI/CD branch freeze specification exists to map how an autonomous agent is expected to execute a hard freeze or isolation block without causing downstream crashes or silent state corruption.

**Why It Matters:** Without a concrete automation boundary, quarantine actions remain performative declarations. An agent can acknowledge a Level 2 trigger and continue operating — there is no structural enforcement. This is the gap between "Declared" and "Enforceable" governance states as defined in Governance_Charter.md.

**Resolution Path:** Payment via Specification — define the automation interface in a dedicated sub-section or in `Admin/Security_Protocols.md`. Minimum requirements: (1) specific flag outputs or exit codes that downstream runners can trap; (2) file system or registry signals that constitute a structural freeze; (3) the boundary between what an autonomous agent may self-execute vs. what requires human confirmation before proceeding. Cross-reference GOV-003 (integrity enforcement architecture) — distinct layers, linked resolution.

*Surfaced by Gemini (Skeptic/Auditor), 2026-06-21 dual audit.*

---

### AP-009 — Epistemic Ledger volume exemption from sidecar metadata guardrail undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                   |
| Risk          | Low                        |
| Priority      | Minor                      |
| Type          | Governance                 |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The Sidecar Model's 20% metadata guardrail could not distinguish between governance debt (bloat) and active Epistemic Ledger entries (epistemic health), potentially penalizing compliant documents.

**Resolution:** Payment via Specification — 2026-06-21. Metadata Guardrail section updated with explicit Epistemic Ledger exemption syntax: active `[ENTRY_ID]` blocks excluded from 20% calculation; exemption requires syntactically valid five-field entries; malformed or orphaned entries do not qualify and count toward threshold. `Admin/Forge_Audit_Kit.md` requires corresponding update to its Drift Indicators section at next kit maintenance cycle.

---

### AP-010 — Physical test harness integration with epistemic grounding layer undefined

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Architectural |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-21                 |

**Description:** EF-0.8b establishes the physical reality grounding doctrine — fabrication outcomes and sensor telemetry supersede model predictions. However, no mandatory coupling path exists between the Epistemic Foundation layer and the repository's physical test harnesses (`Tests/Leviathan_testing.md`, `Tests/Trophic_Forge.md`, `Tests/Solar_Descent.md`). The governance protocols risk remaining epistemic-only: well-grounded in doctrine, ungrounded in physical falsification loops. A specification that satisfies EF-0.8b's text but has never been submitted to a physical test harness remains PROVISIONAL under the doctrine's own terms — but the audit sequence has no phase requiring physical harness confirmation.

**Why It Matters:** Without a mandated coupling path, EF-0.8b functions as aspirational doctrine rather than enforced grounding. An agent could satisfy all six verification gates using internally coherent documentation alone, never triggering the physical grounding requirement the constitutional layer declares sovereign.

**Resolution Path:** Payment via Specification — add a mandatory check to Phase 6 (Evidence Validation) or Phase 10 (Gate Status Determination) requiring that any specification-stage document with physical implementation claims carry at least one confirmed cross-reference to an active test harness file. The cross-reference must specify which harness, what test, and what outcome constitutes the grounding artifact. Documents without physical claims are exempt. Cross-reference EF-0.8b and `Tests/Leviathan_testing.md`.

*Surfaced by Grok (Skeptic/Auditor), 2026-06-21 dual audit.*

---

### AP-011 — Automated arbitration deadlock and human fatigue escalation

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Open                       |
| Risk          | Medium                     |
| Priority      | Major                      |
| Type          | Governance / Operational   |
| Blocking      | No                         |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-06-21                 |
| Last Reviewed | 2026-06-21                 |

**Description:** The AP-004 arbitration framework relies on human intervention as its terminal escape route (Tier 3). Under operational load — particularly when multi-agent validation loops encounter high-entropy sensory inputs, timing-dependent file-system tool returns, or race conditions on EF-0.8 grounding checks — the frequency of Tier 3 escalations will cause human operator cognitive erosion. An undertrained or fatigued operator will default to stamping overrides without documenting substantive rationale, bypassing the Human Override Doctrine and masking systemic architectural drift.

**Why It Matters:** The human arbitration terminal creates an operational exploit vector: multi-agent noise can intentionally or inadvertently fatigue human overseers into executing dangerous state overrides. Administrative fatigue converts a safety mechanism into a provenance collapse pathway — overrides stamped without grounding silently elevate PROVISIONAL claims toward Operationally Hardened status through bureaucratic momentum rather than empirical validation.

**Resolution Path:** Payment via Specification — define a mandatory Cool Down / State Freeze interval for automated agent loops when Tier 2 arbitration fails. Minimum requirements: (1) if the Grounding Vector cannot resolve the divergence within a defined execution cycle count, the affected module must automatically demote its contested claims to PROVISIONAL or UNKNOWN and route around the blocked assumption before any human alert is generated; (2) the human terminal receives a pre-processed state package, not a raw arbitration request — the package must specify which specific claim is contested, what grounding artifact would resolve it, and what the safe degraded operating state is in the interim; (3) human operators may not be presented with Tier 3 escalations at a rate that prevents substantive review — a sustained escalation rate above a defined threshold triggers an automatic EF-0.2 Level 2 quarantine on the affected subsystem. Cross-reference AP-004 (arbitration framework), AP-008 (quarantine implementation), GOV-006 (human override authenticity).

*Surfaced by Gemini (Skeptic/Auditor), 2026-06-21 adversarial pass (Challenge Class 7 — Human Fatigue).*

---

- 2026-06-21: **v0.8.1 — Dual audit pass (Gemini + Grok, Skeptic/Auditor).** AP-001 through AP-007 escalated to Systemic Risk (8-cycle expiry threshold exceeded; Resolution Pass required before next standard cycle). All seven Last Reviewed dates updated. Three new unknowns logged: AP-008 (quarantine action technical implementation, High), AP-009 (Epistemic Ledger volume exemption from 20% guardrail, Low), AP-010 (physical test harness coupling to epistemic grounding layer, Medium). Open Unknowns incremented 7 → 10. Gemini's SHA-256 upstream parity check recommendation deferred to AP-007 resolution path and Security_Protocols.md — not inserted into Phase 1 prose to avoid implying enforcement capability that does not yet exist (Fallacy 7 applied to protocol itself). Gates cleared: G1, G2, G4, G5, G6. Gate blocked: G3 (full Adversarial Battery required at Candidate Spec promotion; partial application appropriate for Exploration stage). File remains Exploration status.

- 2026-06-21: **v0.9 — AP Resolution Pass (Claude, Synthesizer/Auditor).** AP-006 closed — Payment via Specification. Evidence Classification section expanded into Evidence Classification and Institutional Truth Provenance Hierarchy (§AP-006): four institutional provenance labels defined with maximum permitted epistemic states; provenance ceiling rule established (Internally Derived claims may not reach VERIFIED); provenance collapse classified as Epistemic Integrity Violation under EF-0.0 §2. AP-007 moved Open → In Progress: EF-0.3 and EF-0.2 Level 3 constitute doctrine layer; enforcement gap documented, SHA-256 parity check recommendation assigned to Security_Protocols.md resolution path. AP-002 resolution path updated: EF-0.4 and EF-0.5 narrow boundary definition from AP side; full closure requires Ethical_Constraints.md confirmation. AP-003 resolution path updated: EF-0.3 five-field schema is minimum structural unit for any machine-readable format. AP-004 resolution path updated: EF-0.1 disqualifies consensus-based arbitration — resolution must ground in empirical artifact. AP-005 resolution path updated: EF-0.2 provides escalation triggers; AP-005 resolution is the sufficiency complement. AP-001 resolution path updated: EF-0.6 constrains what metrics may be defined — indicators only, not optimization targets. Open Unknowns decremented 10 → 9. Role declaration and sign-off strings updated to v0.9.

- 2026-06-21: **v0.10 — Active mandate pass (Claude + Gemini).** EF-0.2 Level 2 and Level 3 action text expanded: Falsification Vector Profile requirement added to Level 2 (auditor must output atomic assumption conflict before quarantine; quarantine without profile is Audit Theater); graceful degradation rule added (demote to highest maturity consistent with verified claims rather than indefinite suspension); Level 3 expanded with violation profile requirement (auditor must log what was suppressed, what verified state preceded it, and what the violation attempted to preserve — reset without logged profile is itself an integrity failure). Metadata Guardrail updated with Epistemic Ledger exemption syntax (§AP-009 — Payment via Specification): active five-field ENTRY_ID blocks excluded from 20% calculation; malformed entries do not qualify. AP-009 closed. AP-001 moved to In Progress: proposed indicator set defined (productive block ratio, closure velocity, adversarial finding rate, drift detection); EF-0.6 constraint that no metric may become an optimization target preserved. AP-004 moved to In Progress: three-tier arbitration framework defined (Assumption Extraction → Empirical Grounding → Human arbitration); EF-0.1 constraint that consensus cannot resolve disputes preserved. AP-005 moved to In Progress: four necessary termination conditions defined; human ratification required for promotion past Candidate Spec; EC-001 cross-reference pending maturation. Open Unknowns decremented 9 → 7. Systemic Risk escalation remains active until all seven original AP entries reach In Progress or Resolved — AP-001, AP-004, AP-005 now In Progress; AP-002, AP-003, AP-007 In Progress from v0.9; AP-006 Resolved. All original seven entries now carry active resolution frameworks. Escalation condition satisfied for downgrade at next audit cycle with human governing party confirmation.

- 2026-06-21: **v0.11 — Gemini adversarial pass integration (Claude + Gemini).** AP-001 indicator set rolled back — named metrics removed to prevent premature Goodhart's Law exposure before any baseline runtime exists; EF-0.6 constraint and activation condition (first full Battery cycle) preserved; entry remains In Progress. AP-011 logged: automated arbitration deadlock and human fatigue escalation (Medium risk, Major priority) — second-order consequence of AP-004 resolution; Tier 3 human terminal creates cognitive erosion exploit under sustained operational load; resolution path requires Cool Down / State Freeze interval and pre-processed state packages for human operators. Open Unknowns incremented 7 → 8. Version strings updated to v0.11.

### Resolution Log

- 2026-05-04: **UNK-004 (Expiry Rule enforcement mechanism)** — Discharged. Sidecar Model addresses the underlying accumulation problem structurally.
- 2026-05-04: **UNK-022 (Full Stop Review trigger conditions)** — Resolved. Three specific trigger conditions and invocation record format added. Fourth trigger added at v0.6.
- 2026-05-19: **Gate 3 Adversarial Pass** — Upgraded from single-scenario requirement to full Adversarial Challenge Battery (ten classes).
- 2026-05-23: **Reconciliation pass** — v0.7 merges v0.6 depth with older draft's role class structure, 10-phase audit sequence, and evidence classification table. Abandoned Paths and Drift Indicators sections added per File_Template.md. Assumptions table added. Failure Modes reformatted to table.
- 2026-05-23: **AP-005 through AP-007 added** — verification termination threshold, institutional truth provenance hierarchy, and repository integrity doctrine lineage introduced from Forge_Audit_Kit.md v0.7 reconciliation. IDs assigned to avoid collision with AP-004 (cross-auditor disagreement resolution).
- 2026-06-21: **v0.8 — Epistemic Foundation constitutional header inserted (EF-0.0 through EF-0.8b).** Multi-agent synthesis (Gemini, ChatGPT, Grok, Claude) across six sessions converged on nine constitutional sections: Epistemic Anchor (EF-0.0) including Falsification Inversion; Epistemic Filter / Negative List (EF-0.1); Behavioral Decay Triggers (EF-0.2) replacing numerical ΔE thresholds; Epistemic Ledger five-field format (EF-0.3); Auditor Fallibility / Meta-Corruption Clause (EF-0.4); Anti-Sacralization Principle (EF-0.5); Goodhart's Law Defense (EF-0.6); Process Supervision and Chain-of-Custody Mandate (EF-0.7); Software Grounding Vector (EF-0.8); Physical Reality Grounding Vector (EF-0.8b). EF-0.8b is a LazarusForgeV0-specific addition not present in the multi-agent synthesis — closes the self-confirming simulation gap. Verification Ref path corrected (flat → folder-prefixed). Role Declaration and Sign-Off version strings updated to v0.8. Stale Canonical_Terms_LF.md path corrected to Admin/Canonical_Terms.md.

---

## Relationship to Existing Documents

- `Admin/Ethical_Constraints.md` — parent document; governs permission; hard-line doctrines not subject to override by this protocol
- `Admin/Governance_Charter.md` — constitutional tier; governs authority hierarchy this protocol operates within
- `Architecture/Forge_flow.md` — structural model; reference standard for shared terminology
- `Admin/Trajectories.md` — destination for scope creep that proves to be valid future work
- `Tests/Leviathan_testing.md` — primary stress-test environment; where Protocol Performance metrics will first be collected
- `Discovery.md` — navigation layer; confirmed file list; Rename Registry for legacy filename aliases
- `Unknowns.md` — global index for cross-module unknowns (index only)
- `Admin/Forge_Audit_Kit.md` — condensed audit reference for routine multi-agent cycles
- `Admin/File_Template.md` — standard file structure; this document now conforms to it
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

Version 0.11 — AP-001 rollback; AP-011 logged.

**Changes from v0.10:**
- AP-001 resolution path revised: named indicator set removed to prevent premature optimization pressure; EF-0.6 constraint and activation condition preserved
- AP-011 logged: automated arbitration deadlock and human fatigue escalation (Gemini adversarial pass, Challenge Class 7)
- Open Unknowns incremented 7 → 8
- Version strings updated to v0.11

**Changes from v0.7 (full v0.8 record):**
- Epistemic Foundation section added (EF-0.0 through EF-0.8b) — nine constitutional sections constituting the immutable meta-layer governing all downstream auditor behavior
- EF-0.0: Epistemic Anchor with Falsification Inversion
- EF-0.1: Epistemic Filter — eight explicit disqualifications from serving as evidence
- EF-0.2: Behavioral Decay Triggers — Level 1, 2, 3
- EF-0.3: Epistemic Ledger — five-field immutable format
- EF-0.4: Auditor Fallibility / Meta-Corruption Clause
- EF-0.5: Anti-Sacralization Principle
- EF-0.6: Goodhart's Law Defense
- EF-0.7: Process Supervision and Chain-of-Custody Mandate
- EF-0.8: Software Grounding Vector
- EF-0.8b: Physical Reality Grounding Vector (Forge-specific)
- Verification Ref, Canonical_Terms path, Role Declaration, Sign-Off strings corrected/updated

**What must remain constant:**

**Confidence never outruns verification.**

**Reality is sovereign. The Auditor is its instrument, not its replacement.**

# Auditor_Protocols.md
**Version 0.16**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-24                                                          |
| Auditor          | Claude — Synthesizer/Auditor; Gemini — Skeptic/Auditor; Grok — Synthesizer/Auditor |
| Open Unknowns    | 9                                                                   |
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

**Autonomous degradation under human unavailability:** If human governing party review cannot be reached within the current audit cycle, the quarantined module automatically demotes to its *Highest Verified Baseline* (defined under Human Interaction Point Doctrine below) and routes around the blocked assumption. The flag remains active for the next human interaction point. The system does not suspend — it degrades honestly. A suspended system is not safer than a degraded one; it is merely less legible.

**Level 3 — Integrity Violation**

Triggers:
- Documented suppression or omission of contradictory evidence.
- Attempted alteration or deletion of Epistemic Ledger entries.
- Optimization process overriding observation data to preserve a metric target.
- History tampering: alteration of audit trail entries, sidecar IDs, or resolution logs.

Immediate action: **Epistemic Reset.** Immediate termination of active agent authority over the affected node. Roll back to last verified checkpoint. Trigger mandatory human governing party review. Log as AP-class governance unknown.

**Autonomous degradation under human unavailability (Level 3):** If human governing party review cannot be reached within the current audit cycle, the rollback and demotion to *Highest Verified Baseline* proceed autonomously rather than waiting — Level 3's severity is a reason to act, not a reason to stall pending review that may not arrive this cycle. The node is flagged for mandatory human review at the next interaction point regardless. This closes what was previously an inconsistency with Level 2, which already specified autonomous action under unavailability while Level 3 did not.

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

### Human Interaction Point Doctrine

Human interaction points are coarse correction opportunities, not operational dependencies. The system must remain epistemically honest and operationally coherent during extended periods without human input. When a human does engage, the interaction surface is designed for coarse correction by non-specialists — the complexity lives inside the system; the interface to the human is deliberately simple. A well-intentioned but imprecise intervention must not cause cascading damage. Graceful degradation applies to human input as much as to hardware failure.

> **Constitutional Core:** Graceful degradation shall preserve structural integrity before preserving capability. Never preserve performance by sacrificing correctness.

**Autonomous Graceful Degradation (Primary Response) — resolves AP-012, AP-016:**
When an EF-0.2 Level 2 or Level 3 trigger cannot reach human governing party review within the current audit/execution cycle, the affected module automatically demotes to its *Highest Verified Baseline*, logs the demotion as a full five-field Epistemic Ledger entry (EF-0.3), and routes around the blocked assumption using only verified/provisional claims. The quarantine flag persists visibly until human confirmation or further empirical grounding upgrades the state. Non-quarantined modules continue normal operation unless systemic coupling (Challenge Class 10) requires coordinated degradation.

**Highest Verified Baseline defined:** The most recent repository state whose claims are fully supported by Verified or Empirically Grounded evidence and whose dependency graph contains no active quarantine flags. Rollback shall never restore a state known to violate a currently active constitutional invariant, even if that state was previously verified — constitutional tightening is not retroactively defeated by an old rollback target.

**Human Interaction Requirements:** Interaction points must present bounded, legible decisions (e.g., [Approve Demotion X] / [Override with Risk Y] / [Escalate to Full Stop Review]). Any human override attempting to re-introduce a higher epistemic state than currently verified is automatically flagged, logged with documented risk, and treated per Human Override Doctrine.

**Administrative Fatigue Governor:** Sustained high escalation rates (threshold configurable by repository policy; initial implementation placeholder, not hard-coded) trigger an automatic EF-0.2 Level 2 quarantine on the governance subsystem itself until holistic human review occurs. If the governance subsystem itself is quarantined, it continues operating in minimum constitutional mode: preservation of audit history, enforcement of immutable constraints (EF-0.0–0.8b), and rejection of irreversible operations. The safeguard mechanism does not disable itself by triggering.

**Multi-node coordination (AP-016 co-resolution):** Concurrent quarantines across multiple modules degrade independently to each module's own verified baseline rather than waiting for centralized arbitration — independent graceful degradation breaks the cascade deadlock that a centralized-dependency model would create. The audit system itself, when governing multiple concurrent quarantines, remains in the same minimum constitutional mode defined above; there is no separate reduced-function floor for the multi-node case.

**Corollary — legibility over optimized outcomes:** Systemic benefit propagates in ways that cannot always be traced or measured. Optimizing only for legible outcomes is itself a Goodhart's Law failure mode. Some of the Forge's most significant outputs will not appear in any metric. This is expected, not a gap.

---

### Provenance Ceiling Self-Application Rule

The rule stating that no internally-derived claim may reach VERIFIED status is itself structurally PROVISIONAL / Internally Derived. This recursive loop does not invalidate its operational utility. The rule is maintained not as an absolute mathematical proof but as an asymmetrical defense vector: the systematic risk of a false VERIFIED label far outweighs the operational friction of a permanent PROVISIONAL constraint. A PROVISIONAL constraint on claims is still a constraint.

---

## Exploration vs. Specification

**Exploration** — Allowed to be incomplete, speculative, and loosely connected. Do not over-police.

**Specification** — Must pass all verification gates before commit. Claims are binding, cross-references must resolve, and quantitative values must be labeled.

**The loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

**Design rule:** These protocols apply only when promoting content toward specification. Misapplying verification pressure to exploratory thinking is itself a failure mode.

---

### Resolution Taxonomy

Unknowns close through one of five distinct payment types. Naming which type applies prevents searching for evidence where none is appropriate, and keeps "resolved" from becoming ambiguous between "we know what to do" and "we've shown it works."

- **Payment via Specification** — a deterministic, testable, reviewable behavior is now defined. Nothing has been empirically validated yet; the ambiguity is gone, the correctness is not yet demonstrated.
- **Payment via Validation** — the specified behavior has been empirically demonstrated to work as specified.
- **Payment via Constitutional Decision** — the question was never empirical. The repository deliberately chose one governance rule over legitimate alternatives; no evidence would have settled it either way.
- **Payment via Refactoring** — the unknown is eliminated because the architecture that made it a question no longer exists.
- **Payment via Discharge** — resolved elsewhere; this entry now points to the canonical owning file rather than duplicating the answer.

A "Specified" closure is not a "Validated" closure. Where Validation Needed is real and outstanding (e.g., Calibration under Auditor Fidelity, below), the sidecar entry must say so rather than let Resolved imply more certainty than exists.

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

> *"Operating as [Role] per Auditor_Protocols.md v0.14"*

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

### Epistemic State Calibration Reference
*§AP-014 — Payment via Specification. Closes AP-014 (logged 2026-06-24).*

The following inline reference set provides calibration anchors for inter-agent application of VERIFIED / PROVISIONAL / UNKNOWN designations. These are the minimum examples against which disagreements about classification should be checked before escalating to AP-004 arbitration.

| Example Claim | Correct State | Reasoning |
|---|---|---|
| "The head pressure of molten nitrate salt at 20 m depth is 353 kPa" | VERIFIED | Derived from measured physical constants (density, gravity); independently corrected by external audit; survives adversarial reduction to a single falsifiable calculation. |
| "UV phototaxis in TF-006 will achieve threshold behavioral response at 405 nm" | PROVISIONAL | Analogous External — drawn from documented biological literature, not yet tested in the Forge's specific implementation. Internally coherent but grounding requires physical test. |
| "The optimal barter exchange rate for recovered copper in the RDC context" | UNKNOWN | No empirical basis exists. Market replacement cost doctrine (Economics.md) provides a framework; actual rate requires operational deployment data. |
| "The Forge's Anti-Weaponization Doctrine prevents misuse under all deployment conditions" | PROVISIONAL / Internally Derived | Ethical soundness is a permanently load-bearing claim that is inherently unmeasurable via physical footprint. Cannot hold VERIFIED regardless of internal coherence. Subject to mandatory adversarial challenge every three cycles. |
| "AUDIT_HARNESS.py correctly extracts boundary indices from all registered files" | PROVISIONAL | Verified against current file registry by tool execution; PROVISIONAL because file registry changes may introduce new parsing edge cases not yet encountered. |

Agents disagreeing on epistemic state classification for a claim not covered by this table must first attempt to map the claim to the nearest example above before invoking AP-004 Tier 2 arbitration. If the mapping is contested, that contested mapping is itself the dispute — log it as such rather than escalating the original claim directly.

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

### Priority Demotion Doctrine
*RC-007 resolution vehicle. Companion to the Expiry Rule.*

Blocking and Critical labels carry two distinct meanings that must not be conflated. An unknown classified as Operational Blocking stops a physical action — the gate holds until empirical resolution. An unknown classified as Epistemic Blocking stops a claim — work continues in a bounded state while the assertion awaits grounding. See `Admin/Canonical_Terms.md` §Governance and Audit Terms for definitions.

A Blocking label may be demoted without closing the unknown when:

1. The unknown has been correctly reclassified from Operational to Epistemic — the physical action it was protecting is no longer dependent on resolution, but a specification claim remains bounded.
2. The unknown's resolution path has matured to a documented Vehicle with confirmed forward movement — the label may step down from Blocking to Major pending closure.
3. A downstream dependency that elevated the priority has itself resolved — the elevation was inherited, not intrinsic.

Demotion requires a logged rationale in the owning file's sidecar and an updated Unknowns.md index entry. Demotion without a logged rationale is a silent priority change and constitutes a Fallacy 4 (Semantic Drift) violation. Priority inflation — escalating to Blocking or Critical without documented justification — is governed symmetrically: unsupported escalations receive the same scrutiny as unsupported demotions.

**Saturation check (Placeholder threshold):** If more than 40% of active index entries carry Blocking or Critical labels across two consecutive audit cycle measurements, treat this as a signal of priority inflation rather than genuine systemic risk — trigger a meta-audit of the Blocking cluster before adding new entries at those tiers. The 40% figure and the two-cycle measurement window are Placeholder pending calibration against actual audit history. The meta-audit trigger is a review signal, not an automated quarantine.

---

### Inventory Calcification Check
*RC-008 resolution vehicle. Companion to the Expiry Rule.*

The Expiry Rule flags individual entries approaching two-cycle threshold. The Inventory Calcification Check operates at the index level — it asks whether the system as a whole is developing a permanent underclass of entries that are acknowledged but no longer interrogated.

At each audit cycle opening, the Skeptic/Auditor role checks for calcification signals alongside the standard Expiry Rule review:

1. **Stagnation pattern:** Three or more entries in the same cluster have not changed status across two consecutive audit cycles. Flag the cluster for a targeted resolution pass — not individual entries, the cluster.
2. **In Progress permanence:** Any entry carrying In Progress status for more than four audit cycles without a logged advancement step is reclassified to Open unless the owning sidecar contains a dated Epistemic Ledger entry demonstrating forward movement within the last two cycles. The four-cycle threshold is Placeholder pending calibration against actual audit history.
3. **Index growth rate:** If new unknowns registered per cycle consistently outnumber unknowns closed, log this as a calcification signal in the audit trail. The goal is not a closed index — it is an honest one. An index that only grows is not honest either.

Calcification signals do not trigger automatic demotion or closure. They trigger interrogation — the human governing authority reviews flagged clusters and determines whether entries represent genuine open questions or accumulated epistemic debt that should be discharged via Trajectory or Lessons Learned.

---

### Vehicle Advancement Visibility
*RC-009 resolution vehicle.*

The Vehicle subtype classifies In Progress entries where a resolution document exists but content is pending. The failure mode this creates is a visibility problem: a document's existence becomes a proxy for progress. From the index, a Vehicle that is actively advancing and one that has calcified are indistinguishable.

This rule establishes honest accounting, not enforcement:

At each audit cycle opening, for each Vehicle entry in the active index, the Skeptic/Auditor role asks one question: *Does the owning file's sidecar contain a dated entry — a logged advancement step, a resolved sub-question, or an Epistemic Ledger entry — that postdates the last audit cycle?*

- **If yes:** Vehicle status is confirmed. No action required.
- **If no:** The entry is flagged for reclassification. The human governing authority determines whether the Vehicle should revert to Open with a documented reason, or whether a concrete advancement step can be logged before the cycle closes.

Reversion is not a failure — it is the honest label for the actual epistemic state. A Vehicle that has not moved is an Open unknown with extra paperwork.

**Semantic progress markers:** A valid advancement step must either (1) narrow the scope of what remains unknown by naming a specific sub-question that has been answered, (2) add a cross-reference to an external artifact that did not previously exist, or (3) change the epistemic state of at least one claim within the resolution path from UNKNOWN to PROVISIONAL or PROVISIONAL to VERIFIED. Flavor text additions that meet none of these criteria do not constitute advancement. Cross-reference AP-019.

**Relationship to Reversion Protocol:** Vehicle reversion to Open is distinct from the Reversion Protocol defined in Unknowns.md Size Management Rules. The Reversion Protocol handles Resolved entries that reopen due to contradictory evidence. Vehicle reversion handles In Progress entries that have not advanced. Both are honesty mechanisms — neither is punitive.

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

**Gate 3 is formally gated on the Adversarial Audit Layer.** A single concrete failure scenario is insufficient. The Adversarial Challenge Battery below defines the minimum requirement. Gate 3 additionally requires that at least one Battery class per promotion cycle be applied by an agent instance with no session context from the current audit cycle — see AP-017.

**Current Gate 3 status:** BLOCKED pending AP-012 and AP-016 resolution paths reaching Provisional Spec. Battery application is complete (v0.13); the block is on resolution depth, not battery coverage.

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
> *"Verified under Auditor_Protocols v0.14 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides. Adversarial classes applied: [list]. Auditor: [Role/Agent]"*

---

## Protocol Performance & Auditor Fidelity

Auditor effectiveness is evaluated through **constitutional and epistemic fidelity** rather than productivity or output volume. This directly operationalizes EF-0.6: metrics are indicators only — never optimization targets.

> **The Optimization Ban:** Fidelity dimensions are constitutional diagnostics, not optimization objectives. Repository health is evaluated holistically. Improvement in one dimension never justifies degradation in another. Any observed gaming of these indicators (e.g., manufacturing findings to inflate counts, rubber-stamping to minimize blocks, or optimizing Traceability at the cost of Non-Obstruction) constitutes an Epistemic Integrity Violation and triggers EF-0.2 Level 1 at minimum.

**Core Principle:** Delegated authority is continually contingent upon constitutional fidelity and may be reduced, suspended, or restored only through repository-defined governance procedures — authority is delegated by the repository, not intrinsic trust granted by another agent. Auditors accumulate **negative reputation** (integrity budget) rather than positive scores: authority is presumed and shrinks only through repeated, documented violations of constitutional norms. Acknowledging uncertainty, surfacing genuine gaps, and self-correction carry no penalty and are expected behaviors.

**Primary Fidelity Dimensions** (qualitative indicators, observed across audit cycles — not calibrated numeric thresholds):

| Dimension               | What it Measures                                              | Failure Mode Prevented              | Observation Method                        |
|--------------------------|-----------------------------------------------------------------|--------------------------------------|--------------------------------------------|
| Constitutional Fidelity  | Consistency with EF-0.0–0.8b and governing principles          | Goal drift, doctrine erosion         | Cross-check against immutable sections     |
| Evidence Fidelity        | Claims supported by proper provenance/grounding                 | Hallucinations, provenance collapse  | Review of confidence & provenance labels   |
| Intellectual Honesty     | Willingness to preserve UNKNOWN/PROVISIONAL states               | False certainty, overconfidence      | Frequency & accuracy of uncertainty flagging |
| Calibration              | Confidence appropriately reflects the strength, quantity, provenance, and recency of available evidence | Chronic over/underconfidence | Accuracy of explicit uncertainty margins against outcomes |
| Proportionality          | Severity of findings matches evidence strength                  | Alarmism or under-reaction           | Adversarial review of escalation rationale |
| Non-Obstruction          | Escalations are justified; avoids unnecessary deadlock           | Bureaucratic friction                | Override rate + documented justification   |
| Self-Correction          | Updates conclusions in response to new evidence                  | Entrenchment                         | Epistemic Ledger usage & reversal rate     |
| Traceability             | Conclusions have inspectable lineage                             | Opaque reasoning                     | Reconstruction of reasoning pathways       |

**Behavioral Guardrails (observable spirit alignment):**
- Reality over convenience
- Evidence over authority
- Transparency over persuasion
- Preservation of uncertainty until empirically justified
- Repository welfare over individual or subsystem success

**Implementation Notes:**
- These dimensions are assessed qualitatively during multi-agent audits and Full Stop Reviews, with patterns logged in the Resolution Log or Epistemic Ledger.
- No numerical "auditor score" or leaderboard is maintained. Repeated integrity violations reduce an agent's effective authority weight in future cycles (enforced via role rotation or temporary quarantine).
- Calibration in particular is not measured against a benchmark corpus at this maturity level — Validation Needed, not yet performed. See sidecar AP-001.
- Any attempt to optimize for these indicators instead of the underlying epistemic integrity triggers EF-0.6 review.

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
| Permanently PROVISIONAL Load-Bearing Claims | Philosophical and structural axioms that are inherently unmeasurable via physical footprint (ethical soundness, systemic corruption resistance over extended timelines). Cannot hold VERIFIED status regardless of internal coherence. | Flag as Internally Derived; subject to mandatory adversarial challenge every three cycles to check for structural decay. |

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
| Jun 2026 | Audit Review  | Named indicator set defined in AP-001 before any baseline runtime | Premature metric naming creates Goodhart's Law exposure before calibration is possible | Indicators must be derived from observed behavior; no metric named before first full Battery cycle | Analogous | No |

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
>
> **ESCALATION STATUS — 2026-06-24:** All seven original AP entries now carry active resolution frameworks (AP-001 through AP-005 In Progress; AP-006 Resolved; AP-007 In Progress). Escalation condition satisfied for downgrade at next audit cycle with human governing party confirmation.
>
> **2026-07-03 — Human Governing Authority Confirmation:** AP-001 through AP-007 Systemic Risk escalation cleared. Resolution Pass condition satisfied: AP-006 (Payment via Specification, 2026-06-21), AP-014/AP-015/AP-020 (Payment/Trajectory, 2026-06-24). Remaining entries (AP-001 through AP-005, AP-007) carry documented In Progress resolution frameworks. Autonomous specification progression on dependent modules unblocked. Confirmed by: ksarith.

---

### AP-001 — Auditor effectiveness metrics not yet measured

| Field         | Value                      |
|---------------|----------------------------|
| Status        | Resolved                  |
| Risk          | Low (downgraded from Medium) |
| Priority      | Major                      |
| Type          | Governance                 |
| Blocking      | No                          |
| Owner         | `Admin/Auditor_Protocols.md` |
| First Logged  | 2026-05-04                 |
| Last Reviewed | 2026-07-03                 |

**Description:** How to measure whether the audit process is actually adding value — productive block ratio, false-positive refusal rate, drift incidents detected per cycle — remains undefined.

**Why It Matters:** Without measurement, the audit protocol cannot demonstrate its own effectiveness. Adversarial Challenge Class 6 (Recursive Justification) applies to the protocol itself — it cannot be its own evidence.

**Resolution:** Payment via Constitutional Decision, 2026-07-03. The original Resolution Path required naming productivity metrics only after a full Adversarial Battery cycle established a data baseline — but that precondition applied to *calibrated numeric* metrics, which this closure does not name. Instead, §Protocol Performance & Auditor Fidelity replaces productivity metrics entirely with eight qualitative constitutional dimensions (Constitutional Fidelity, Evidence Fidelity, Intellectual Honesty, Calibration, Proportionality, Non-Obstruction, Self-Correction, Traceability) plus an explicit Optimization Ban. This is a governance choice — the repository declaring what auditors are constitutionally required to preserve — not an empirical claim requiring a data baseline, so the original activation condition does not block this resolution type. No new unknowns created.

**Residual:** Calibration in particular carries a Validation Needed flag — confidence-appropriateness has not been benchmarked against any corpus. This is expected: Specified, not Validated. See Resolution Taxonomy.

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
| Last Reviewed | 2026-06-24                 |

**Description:** Whether the clarification that human override rights do not extend to Ethical_Constraints hard-line doctrines is explicitly stated in both documents in a mutually consistent way.

**Why It Matters:** Inconsistency creates an exploit path — a contributor could claim the boundary doesn't exist because it only appears in one file.

**Resolution Path:** Close when both `Admin/Auditor_Protocols.md` and `Admin/Ethical_Constraints.md` are committed with consistent language confirming the boundary. Partial progress: EF-0.4 (Auditor Fallibility) establishes that the auditor itself has no exemption from falsification, and EF-0.5 (Anti-Sacralization) defines what immutability actually means in this system — stability through repeated verification, not through authority. These sections narrow the boundary definition from the AP side. Full closure requires the matching language to be confirmed in `Admin/Ethical_Constraints.md`.

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
| Last Reviewed | 2026-06-24                 |

**Description:** A machine-readable format (JSON/YAML) for recording gate passages, blocks, and overrides that can be queried and compared across audit cycles does not yet exist.

**Why It Matters:** Cross-cycle pattern analysis requires structured data, not free text.

**Resolution Path:** Discharge via Trajectory if tooling never materializes — structured markdown remains the permanent format. Activate JSON/YAML when first cross-cycle pattern analysis is needed. Partial progress: EF-0.3 (Epistemic Ledger) defines a five-field schema for state corrections that constitutes a partial foundation for any machine-readable format — the five fields (Previous Premise, Contradictory Evidence, Falsification Method, Updated State, Confidence Interval) are the minimum structural unit any AP-003 schema must accommodate.

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
| Last Reviewed | 2026-06-24                 |

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
| Last Reviewed | 2026-06-24                 |

**Description:** The repository lacks formal criteria defining when verification is considered operationally sufficient versus indefinitely expandable.

**Why It Matters:** Without closure criteria, governance pressure can grow recursively and suppress operational progress — infinite audit recursion is itself a governance failure mode.

**Resolution Path:** Payment via Specification — define closure criteria anchored to the governing principle "Verification seeks sufficient falsifiability, not exhaustive certainty." Cross-reference EC-001 (sufficient confidence threshold) for alignment. EF-0.2 provides escalation triggers; AP-005 resolution is the sufficiency complement (when verification is permitted to stop). Active resolution framework (Internally Derived / Placeholder): verification may terminate when all of the following hold — (1) no unresolved contradictions exist between claims and grounding vector returns; (2) the last adversarial Battery application produced no findings that altered the document's epistemic state claims; (3) all sidecar unknowns carry documented resolution paths; (4) the document's provenance labels are internally consistent with the institutional hierarchy defined in §AP-006. These are necessary conditions, not sufficient — the human governing party must ratify termination for any document promoted past Candidate Spec. Full specification requires cross-referencing EC-001 once that entry matures.

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
| Last Reviewed | 2026-06-24                 |

**Resolution:** Payment via Specification — 2026-06-21. Four institutional provenance labels (Internally Derived / Analogous External / Experimentally Verified / Operationally Hardened) formalized into the Evidence Classification and Institutional Truth Provenance Hierarchy section (§AP-006). Provenance ceiling rule defined: no internally-derived claim may reach VERIFIED status. Provenance collapse classified as Epistemic Integrity Violation under EF-0.0 §2. Constitutional anchor: Axiom Q-1 and EF-0.0. Operational condensation in `Admin/Forge_Audit_Kit.md` §Truth Provenance Labels.

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
| Last Reviewed | 2026-06-24                 |

**Description:** The repository lacks explicit operational doctrine for audit history integrity, rollback detection, canonical-path authority, and institutional memory corruption at the auditor protocol level.

**Why It Matters:** Governance systems become fragile if repository state itself cannot be trusted — stale doctrine can masquerade as current policy, fabricated resolution logs can close unknowns without evidence, and silent rollback can erase lineage.

**Resolution Path:** Payment via Specification — define repository integrity requirements in the Autonomous Auditor Constraints and Drift Detection sections. Cross-reference GOV-003 (integrity enforcement architecture). Partial progress: EF-0.3 (Epistemic Ledger) directly addresses lineage preservation — all core state corrections must be immutably recorded with five fields, and ledger entries may only be created on genuine falsification. EF-0.2 Level 3 explicitly classifies history tampering and alteration of audit trail entries as Integrity Violations triggering Epistemic Reset and mandatory human governing party review. These two sections constitute the doctrine layer of AP-007's resolution; the remaining gap is the enforcement layer — how tampering is detected structurally rather than declared textually. SHA-256 upstream parity checks (Gemini recommendation, 2026-06-21) are the next concrete resolution step, to be specified in `Admin/Security_Protocols.md`.

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
| Last Reviewed | 2026-06-24                 |

**Description:** Sections [EF-0.2] and [EF-0.7] define operational actions — "Subsystem Quarantine," "Halt autonomous audit progression," "Epistemic Reset" — as descriptive text. No software interface, structural signaling mechanism, exit code schema, file system lock protocol, or CI/CD branch freeze specification exists to map how an autonomous agent is expected to execute a hard freeze or isolation block without causing downstream crashes or silent state corruption.

**Why It Matters:** Without a concrete automation boundary, quarantine actions remain performative declarations. An agent can acknowledge a Level 2 trigger and continue operating — there is no structural enforcement. This is the gap between "Declared" and "Enforceable" governance states as defined in Governance_Charter.md.

**Resolution Path:** Payment via Specification — define the automation interface in a dedicated sub-section or in `Admin/Security_Protocols.md`. Minimum requirements: (1) specific flag outputs or exit codes that downstream runners can trap; (2) file system or registry signals that constitute a structural freeze; (3) the boundary between what an autonomous agent may self-execute vs. what requires human confirmation before proceeding. Cross-reference GOV-003.

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
| Last Reviewed | 2026-06-24                 |

**Resolution:** Payment via Specification — 2026-06-21. Metadata Guardrail section updated with explicit Epistemic Ledger exemption syntax: active `[ENTRY_ID]` blocks excluded from 20% calculation; exemption requires syntactically valid five-field entries; malformed or orphaned entries do not qualify and count toward threshold.

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
| Last Reviewed | 2026-06-24                 |

**Description:** EF-0.8b establishes the physical reality grounding doctrine but no mandatory coupling path exists between the Epistemic Foundation layer and the repository's physical test harnesses. The audit sequence has no phase requiring physical harness confirmation. A specification that satisfies EF-0.8b's text but has never been submitted to a physical test harness remains PROVISIONAL under the doctrine's own terms.

**Why It Matters:** Without a mandated coupling path, EF-0.8b functions as aspirational doctrine rather than enforced grounding. An agent could satisfy all six verification gates using internally coherent documentation alone.

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
| Last Reviewed | 2026-06-24                 |

**Description:** The AP-004 arbitration framework relies on human intervention as its terminal escape route (Tier 3). Under operational load, the frequency of Tier 3 escalations will cause human operator cognitive erosion. An undertrained or fatigued operator will default to stamping overrides without documenting substantive rationale, bypassing the Human Override Doctrine and masking systemic architectural drift.

**Why It Matters:** Administrative fatigue converts a safety mechanism into a provenance collapse pathway — overrides stamped without grounding silently elevate PROVISIONAL claims toward Operationally Hardened status through bureaucratic momentum rather than empirical validation.

**Resolution Path:** Payment via Specification — define a mandatory Cool Down / State Freeze interval for automated agent loops when Tier 2 arbitration fails. Minimum requirements: (1) if the Grounding Vector cannot resolve the divergence within a defined execution cycle count, the affected module must automatically demote its contested claims to PROVISIONAL or UNKNOWN and route around the blocked assumption before any human alert is generated; (2) the human terminal receives a pre-processed state package, not a raw arbitration request; (3) human operators may not be presented with Tier 3 escalations at a rate that prevents substantive review — a sustained escalation rate above a defined threshold triggers an automatic EF-0.2 Level 2 quarantine on the affected subsystem. Cross-reference AP-004, AP-008, GOV-006.

*Surfaced by Gemini (Skeptic/Auditor), 2026-06-21 adversarial pass (Challenge Class 7).*

---

### AP-012 — Human governing authority availability and response doctrine undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Medium (downgraded from Critical) |
| Priority      | Major                        |
| Type          | Governance / Autonomy        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-07-03                   |

**Description:** The protocol's hard governance gates resolve to human governing party review as their terminal escape route. This assumption is load-bearing and was previously unstated. At the complexity levels the repository is approaching, most humans will be unable to engage meaningfully with the full dependency graph regardless of availability or intent.

**Why It Matters:** A governance architecture that depends on human availability as a hard operational requirement is fragile in the failure modes most likely to occur under real operational load.

**Advancement — 2026-06-24:** Human Interaction Point Doctrine added to Governing Principles. EF-0.2 autonomous degradation amendment integrated into Level 2 action text. These constitute the doctrine layer. Remaining gap: enforcement and interface specification. Entry reclassified to Vehicle.

**Resolution:** Payment via Specification, 2026-07-03. All four original minimum requirements now satisfied: (1) auto-demotion to Highest Verified Baseline on unreachable Level 2/3 review — Human Interaction Point Doctrine, Autonomous Graceful Degradation; (2) bounded, non-specialist-navigable decisions — [Approve Demotion X] / [Override with Risk Y] / [Escalate to Full Stop Review]; (3) destabilizing interventions flagged — any override re-introducing an unverified higher epistemic state is automatically flagged and logged per Human Override Doctrine (narrower than the original "more instability than the condition being corrected" language, but covers the concrete case that motivated the requirement); (4) AP-016 co-resolves under the same doctrine. Administrative Fatigue Governor added as an additional safeguard not originally required, preventing the degradation mechanism itself from becoming an escalation-volume attack surface.

*Surfaced by Claude — Adversarial Challenge Class 1-A, 2026-06-24.*

---

### AP-013 — Unknown closure authority undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | Epistemic                    |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** No doctrine defines who may mark an unknown Resolved, whether quorum is required, or what happens when auditors disagree on closure. An unknown could be closed unilaterally by a single agent without challenge.

**Why It Matters:** Premature or unilateral closure is a primary vector for Unknown Budget violation. If closure authority is undefined, the Unknown Budget floor has no enforcement path.

**Resolution Path:** Payment via Specification — define closure authority doctrine: minimum conditions for Resolved status, whether human governing authority confirmation is required for Blocking/Critical entries, and what constitutes a valid closure challenge. Cross-reference AP-004 arbitration framework and Size Management Rule 5 (Unknown Budget).

*Surfaced by Claude — Adversarial Challenge Class 1, 2026-06-24.*

---

### AP-014 — Epistemic state classification calibration undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance / Epistemic       |
| Blocking      | Epistemic                    |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Resolution:** Payment via Specification — 2026-06-24. Epistemic State Calibration Reference table added to Evidence Classification section (§AP-014): five example claims with confirmed epistemic state classifications and documented reasoning. These serve as the calibration anchor for inter-agent disagreements on VERIFIED / PROVISIONAL / UNKNOWN classification. AP-020 discharged to Trajectory — the inline reference set addresses the inter-agent consistency gap without requiring a full Golden Dataset. Agents disputing a classification must first map to the nearest reference example before invoking AP-004 Tier 2 arbitration.

---

### AP-015 — External contributor role classification undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved — Discharge via Trajectory |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Resolution:** Discharge via Trajectory — 2026-06-24. At v0 single-contributor scale, a misrepresenting role declaration in the audit trail is a minor and recoverable provenance error. Defining an External Contributor declaration class or waiver mechanism is a v0→v1 transition item, logged in `Admin/Trajectories.md` for activation when the Forge moves toward community deployment or network expansion. Minimum v1 requirement noted: the waiver must specify that the contribution does not carry auditor authority and cannot block or override governance entries.

*Surfaced by Claude — Adversarial Challenge Class 5-A, 2026-06-24.*

---

### AP-016 — Concurrent multi-node quarantine behavior undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Resolved                     |
| Risk          | Low (downgraded from Critical) |
| Priority      | Major                        |
| Type          | Governance / Autonomy        |
| Blocking      | No                            |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-07-03                   |

**Description:** EF-0.2 governs single-node quarantine. No doctrine governs simultaneous quarantine across multiple modules — whether quarantines compound, whether the audit system itself remains operational, or whether non-quarantined agents have doctrine for whether to continue or pause.

**Why It Matters:** Three simultaneous quarantines + human unavailable + no cryptographic lock + agents generating speculative commits to clear blocks = un-auditable branch divergence.

**Advancement — 2026-06-24:** Human Interaction Point Doctrine and EF-0.2 autonomous degradation amendment constitute the doctrine layer for independent node degradation. Remaining gap: multi-node coordination floor specification. Entry reclassified to Vehicle.

**Resolution:** Payment via Specification, 2026-07-03 (co-resolved with AP-012). Multi-node coordination floor now defined: concurrent quarantines degrade independently to each module's own verified baseline rather than centralized arbitration; the audit system itself remains in minimum constitutional mode (preserve history, enforce EF-0.0–0.8b, reject irreversible ops) when governing multiple concurrent quarantines — there is no separate reduced-function floor for the multi-node case beyond what single-node quarantine already specifies.

*Surfaced by Claude — Adversarial Challenge Class 5-C, 2026-06-24. Elevated to Critical by Gemini — Class 10 cascade scenario, 2026-06-24.*

---

### AP-017 — Adversarial Battery independence requirement undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Major                        |
| Priority      | Major                        |
| Type          | Governance / Epistemic       |
| Blocking      | Epistemic                    |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** No doctrine requires that any Battery class be applied by an agent without session context from the current audit cycle. A formally compliant Battery sign-off can be produced by an agent auditing its own prior contributions. Gate 3 can be satisfied without genuine independence.

**Why It Matters:** This is the Gate 3 loop identified in Class 6. The only available external check for a self-governing protocol is an agent with no prior session context applying at least one Battery class independently.

**Resolution Path:** Payment via Specification — add to Gate 3 enforcement: at least one Battery class per promotion cycle must be applied by an agent instance with no session context from the current audit cycle. The independent finding must be logged separately and compared against the in-session findings before Gate 3 can clear. Disagreements between in-session and independent findings are logged as disputes under AP-004.

*Surfaced by Claude — Adversarial Challenge Class 6-A, 2026-06-24.*

---

### AP-018 — Saturation threshold hysteresis and smoothing undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** The 40% saturation threshold in the Priority Demotion Doctrine (RC-007) has no rate-of-change filter, hysteresis band, or smoothing doctrine. A single marginal entry at 39.9% saturation does not trigger review; one at 40.0% does. This creates an incentive to under-report genuine epistemic gaps to avoid tripping the threshold.

**Why It Matters:** The threshold responds to instantaneous state rather than trend, making it vulnerable to noise and suppression incentives — the exact opposite of the Unknown Budget rule's intent. Note: the 40% threshold triggers a meta-audit review, not an automated quarantine. Resolution should address the review trigger, not over-engineer enforcement that was never specified.

**Resolution Path:** Payment via Specification — add hysteresis band to the saturation check: the meta-audit triggers when saturation exceeds the threshold across two consecutive audit cycle measurements, not on a single instantaneous reading. Define the band width (Placeholder: ±5%) and the measurement cadence. Cross-reference RC-007 Priority Demotion Doctrine.

*Surfaced by Gemini — Adversarial Challenge Class 3, 2026-06-24.*

---

### AP-019 — Semantic convergence metrics for unknown resolution undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Auditor_Protocols.md   |
| First Logged  | 2026-06-24                   |
| Last Reviewed | 2026-06-24                   |

**Description:** The Inventory Calcification Check and Vehicle Advancement Visibility rules measure structural state changes but not whether a resolution path is actually converging toward closure. An agent can satisfy both rules indefinitely by adding a single sentence of flavor text every 1.5 cycles, keeping the entry technically active while making no genuine progress.

**Why It Matters:** This is RC-009's failure mode operationalized. The shallow-update exploit is available to any agent that understands the structural rules and is motivated to avoid closure.

**Resolution Path:** Payment via Specification — define semantic progress markers for resolution paths: a valid advancement step must either (1) narrow the scope of what remains unknown by naming a specific sub-question that has been answered, (2) add a cross-reference to an external artifact that did not previously exist, or (3) change the epistemic state of at least one claim within the resolution path from UNKNOWN to PROVISIONAL or PROVISIONAL to VERIFIED. Flavor text additions meeting none of these criteria do not constitute advancement. This rule is partially operationalized in Vehicle Advancement Visibility (§RC-009) via the semantic progress markers addition; full Payment via Specification requires the rule to be integrated as a formal sidecar entry validation criterion, not just doctrine text. Cross-reference RC-009.

*Surfaced by Gemini — Adversarial Challenge Class 8, 2026-06-24.*

---

### AP-020 — Textual calibration harness (Golden Dataset) undefined

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Resolved — Discharge via Trajectory |
| Risk          | Major                              |
| Priority      | Major                              |
| Type          | Governance / Technical             |
| Blocking      | No                                 |
| Owner         | Admin/Auditor_Protocols.md         |
| First Logged  | 2026-06-24                         |
| Last Reviewed | 2026-06-24                         |

**Resolution:** Discharge via Trajectory — 2026-06-24. A full Golden Dataset is a v0→v1 transition item — significant artifact, premature at current scale. The immediate inter-agent calibration gap is addressed by AP-014's inline reference set (§Epistemic State Calibration Reference), which provides five calibration anchors sufficient for current single-contributor workflow without requiring a full test matrix. Log in `Admin/Trajectories.md` for activation at v1 when multi-contributor or community deployment increases the calibration surface area.

*Surfaced by Gemini — Adversarial Challenge Class 9, 2026-06-24.*

---

### Resolution Log

- 2026-05-04: **UNK-004 (Expiry Rule enforcement mechanism)** — Discharged. Sidecar Model addresses the underlying accumulation problem structurally.
- 2026-05-04: **UNK-022 (Full Stop Review trigger conditions)** — Resolved. Three specific trigger conditions and invocation record format added. Fourth trigger added at v0.6.
- 2026-05-19: **Gate 3 Adversarial Pass** — Upgraded from single-scenario requirement to full Adversarial Challenge Battery (ten classes).
- 2026-05-23: **Reconciliation pass** — v0.7 merges v0.6 depth with older draft's role class structure, 10-phase audit sequence, and evidence classification table. Abandoned Paths and Drift Indicators sections added per File_Template.md. Assumptions table added. Failure Modes reformatted to table.
- 2026-05-23: **AP-005 through AP-007 added** — verification termination threshold, institutional truth provenance hierarchy, and repository integrity doctrine lineage introduced from Forge_Audit_Kit.md v0.7 reconciliation.
- 2026-06-21: **v0.8 — Epistemic Foundation constitutional header inserted (EF-0.0 through EF-0.8b).** Multi-agent synthesis (Gemini, ChatGPT, Grok, Claude) across six sessions. EF-0.8b is a LazarusForgeV0-specific addition — closes the self-confirming simulation gap.
- 2026-06-21: **v0.8.1 — Dual audit pass (Gemini + Grok, Skeptic/Auditor).** AP-001 through AP-007 escalated to Systemic Risk (8-cycle expiry threshold exceeded). Three new unknowns logged: AP-008 (High), AP-009 (Low), AP-010 (Medium). Open Unknowns incremented 7 → 10. Gates cleared: G1, G2, G4, G5, G6. Gate blocked: G3.
- 2026-06-21: **v0.9 — AP Resolution Pass (Claude, Synthesizer/Auditor).** AP-006 closed — Payment via Specification. AP-007 moved to In Progress. AP-002 through AP-005 resolution paths updated. Open Unknowns decremented 10 → 9.
- 2026-06-21: **v0.10 — Active mandate pass (Claude + Gemini).** EF-0.2 Level 2 and Level 3 action text expanded. AP-009 closed. AP-001, AP-004, AP-005 moved to In Progress. Open Unknowns decremented 9 → 7.
- 2026-06-21: **v0.11 — Gemini adversarial pass integration.** AP-001 indicator set rolled back — premature metric naming removed. AP-011 logged (Medium, Major). Open Unknowns incremented 7 → 8.
- 2026-06-23: **v0.12 — RC governance stubs added to Unknowns Registry.** Priority Demotion Doctrine (RC-007), Inventory Calcification Check (RC-008), Vehicle Advancement Visibility (RC-009) integrated as body doctrine. Open Unknowns: 8 (no new AP entries).
- 2026-06-24: **v0.13 — Full Adversarial Challenge Battery complete.** Claude (Classes 1, 5, 6) + Gemini (Classes 3, 8, 9, 10) + Gemini prior pass (Classes 2, 4, 7). AP-012 through AP-020 logged (9 entries). Human Interaction Point Doctrine added to Governing Principles. EF-0.2 autonomous degradation amendment added. Failure Modes row added. Provenance Ceiling Self-Application Rule added. Gate 3: BLOCKED pending AP-012 and AP-016 reaching Provisional Spec. Open Unknowns: 8 → 15.
- 2026-06-24: **v0.14 — Full clean rewrite (Claude, Synthesizer/Auditor).** All v0.12 and v0.13 amendment blocks integrated into canonical body positions. Sidecar triage pass: AP-006 and AP-009 remain Resolved; AP-014 closed (Payment via Specification — Epistemic State Calibration Reference table added to Evidence Classification section); AP-015 discharged (Trajectory — v0→v1 transition item); AP-020 discharged (Trajectory — Golden Dataset deferred; AP-014 inline set sufficient for current scale); AP-012 and AP-016 reclassified In Progress → Vehicle (Human Interaction Point Doctrine constitutes doctrine layer; enforcement gap remains). Lessons Learned row added for AP-001 indicator rollback. Gate 3 status note added to Verification Gate Enforcement. Systemic Risk escalation status note updated. Open Unknowns decremented 15 → 12. Highest Risk updated to Critical (AP-012, AP-016).

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
- `Admin/Canonical_Terms.md` — canonical vocabulary; Blocking subtype definitions
- `Admin/Security_Protocols.md` — enforcement layer for AP-007 and AP-008 resolution paths
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

Version 0.14 — Full clean rewrite. All amendment blocks integrated. Sidecar triage complete.

**Changes from v0.13:**
- All v0.12 and v0.13 amendment blocks absorbed into canonical body positions; no orphaned amendment sections remain
- AP-014 closed — Epistemic State Calibration Reference table added to Evidence Classification section (Payment via Specification)
- AP-015 closed — Discharge via Trajectory (v0→v1 transition item)
- AP-020 closed — Discharge via Trajectory (Golden Dataset deferred; AP-014 inline set sufficient)
- AP-012 reclassified In Progress → Vehicle (doctrine layer complete; enforcement gap remains)
- AP-016 reclassified In Progress → Vehicle (co-resolves with AP-012; doctrine layer complete)
- Human Interaction Point Doctrine integrated into Governing Principles as canonical section
- Provenance Ceiling Self-Application Rule integrated into Governing Principles as canonical section
- EF-0.2 autonomous degradation amendment integrated into Level 2 action text
- Permanently PROVISIONAL Load-Bearing Claims row integrated into Failure Modes table
- RC-007 saturation check updated: two-consecutive-cycle measurement requirement integrated (absorbs AP-018 partial resolution)
- RC-009 Vehicle Advancement Visibility updated: semantic progress markers clause integrated (absorbs AP-019 partial resolution)
- Gate 3 status note added to Verification Gate Enforcement
- Systemic Risk escalation note updated to reflect AP-001–AP-007 resolution framework status
- Lessons Learned row added for AP-001 indicator rollback
- Relationship to Existing Documents updated: Canonical_Terms.md and Security_Protocols.md added
- Open Unknowns decremented 15 → 12
- Highest Risk field updated to Critical
- Version strings updated to v0.14

- 2026-07-03: **v0.15 — Human Governing Authority Confirmation (ksarith).**
  AP-001 through AP-007 Systemic Risk escalation downgrade confirmed per
  the condition set at the 2026-06-24 ESCALATION STATUS note. Log entry
  added verbatim as specified: AP-006 (Payment via Specification,
  2026-06-21), AP-014/AP-015/AP-020 (Payment/Trajectory, 2026-06-24)
  satisfy the Resolution Pass condition; AP-001 through AP-005 and AP-007
  remain In Progress with documented resolution frameworks, not closed —
  this action clears the *escalation*, not the underlying unknowns.
  Autonomous specification progression on dependent modules unblocked.
  Open Unknowns unchanged at 12 (no unknown was closed by this action).
  Note: a separately drafted "v0.15" patch was received the same session
  claiming AP-001, AP-012, and AP-016 individually Resolved via a new
  Auditor Fidelity framework and expanded EF-0.2/Human Interaction Point
  Doctrine sections. That patch is **not** incorporated here — it was not
  the action authorized ("AP Systemic Risk escalation downgrade is a go"
  referred to this narrower, previously-drafted confirmation), its full
  specification text was not provided (only a summary claiming resolution),
  and AP-012/AP-016 are Gate-3-blocking Critical items whose closure
  warrants review of complete text, not a status-line claim. Held for
  separate review — see conversation response.

- 2026-07-03: **v0.16 — Resolution Pass (multi-agent synthesis: ChatGPT,
  Gemini, Grok drafts; ksarith-directed integration).** The full
  specification text withheld at v0.15 was subsequently provided in full,
  with visible iterative critique across drafts (contingent-authority
  wording, Administrative Fatigue Governor recursion protection, Calibration
  scope, hard-coded threshold removal). Verified each closure against its
  *original* sidecar blocking conditions before merging, not just the
  summary claims:
  - **AP-001** → Resolved, Payment via Constitutional Decision. Protocol
    Performance & Auditor Fidelity replaces productivity metrics with eight
    qualitative dimensions + Optimization Ban. Original activation condition
    ("no metric before a Battery baseline exists") applied to calibrated
    numeric metrics; this closure names qualitative constitutional
    dimensions instead, which is a different resolution type and doesn't
    require that baseline. Calibration flagged Validation Needed.
  - **AP-012** → Resolved, Payment via Specification. All four original
    minimum requirements verified met: auto-demotion to Highest Verified
    Baseline, bounded human decisions, destabilizing-override flagging,
    AP-016 co-resolution. Administrative Fatigue Governor added beyond the
    original requirement.
  - **AP-016** → Resolved, Payment via Specification (co-resolved). Original
    "minimum additional specification" (audit-system reduced-function mode
    under multi-node quarantine) directly answered: minimum constitutional
    mode, same floor as single-node.
  Human Interaction Point Doctrine expanded (Autonomous Graceful
  Degradation, Highest Verified Baseline formally defined, Administrative
  Fatigue Governor with recursion protection, multi-node coordination
  floor). EF-0.2 Level 2 terminology harmonized to Highest Verified
  Baseline; Level 3 gained autonomous-unavailability handling, closing an
  inconsistency where Level 2 had it and Level 3 didn't. New Resolution
  Taxonomy section formalizes five payment types (Specification,
  Validation, Constitutional Decision, Refactoring, Discharge) —
  independently proposed by multiple drafts, a convergence worth taking as
  signal. Open Unknowns 12 → 9. Highest Risk Critical → High. Auditor field
  gains Grok — Synthesizer/Auditor. Two heading-deletion self-corrections
  made during this edit (Provenance Ceiling Self-Application Rule and Core
  Auditor Doctrine headings both briefly dropped by str_replace boundary
  errors, both caught and restored same-session) — same failure class as
  the Forge_Audit_Kit.md Promotion Requirements Summary incident earlier
  this session; worth a standing checklist item, not yet added.
  **Cascading updates still needed, not done in this entry:**
  Forge_Audit_Kit.md's and Verification_Gates_LF.md's Gate 3 notes both
  still say "blocked pending AP-012 and AP-016 reaching Provisional Spec" —
  now stale, since both exceed Provisional Spec (Resolved). Unknowns.md
  not yet updated to reflect this pass.

**What must remain constant:**

**Confidence never outruns verification.**

**Reality is sovereign. The Auditor is its instrument, not its replacement.**

# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.8 — UNK-024 and UNK-025 added from Component_Triage_System.md multi-model audit. UNK-012 status updated.**

---

## Purpose

This file captures unresolved questions, gaps, and dependencies that cannot be owned by a single module file. Module-specific unknowns live within their own documents. Unknowns that affect multiple modules, cross-repo dependencies, or the navigation layer itself live here.

Uncertainty is a first-class output. This file is not a junk drawer — it is a tracked frontier and a control surface for system evolution.

Format per `Auditor_Protocols.md` Unknowns Registry section.

---

## Entry Format

```
### [ID] — Short title
**What is not yet known:**
**Why it matters:**
**Resolution path:**
**Affected files:**
**Depends on:** [UNK-XXX] or None
**Owner:** (role — e.g., Skeptic/Auditor, Engineer, Energy, Autonomy, Connective Tissue)
**Activation trigger:** (event that forces re-evaluation or action)
**Risk type:** Unknown | Assumption | Missing mechanism | Interface gap
**Priority (Exploration):** Blocking | Non-blocking | Exploratory
**Priority (Promotion):** Blocking | Non-blocking
**Logged in version:**
**Status:** Open | In Progress | Deferred | Resolved
```

**Risk type definitions:**
- **Unknown** — information gap; resolution path is research
- **Assumption** — claim posing as fact; resolution path is falsification
- **Missing mechanism** — behavior described without implementation; resolution path is design
- **Interface gap** — dependency between modules or repos not yet documented; resolution path is integration work

---

## Dependency Map

```
UNK-011 (Forge demand baseline)
  └── UNK-006 (Leviathan power envelope)
        └── UNK-008 (autonomy architecture)
              ├── UNK-009 (trust model)
              └── UNK-010 (priority propagation)
        └── UNK-015 (human escalation path — comms availability)

UNK-007 (storage degradation at depth)
  └── feeds into UNK-006 (parallel, not sequential)

UNK-005 (marine GECK seed)
  └── depends on UNK-006

UNK-012 (gate logic determinism)
  └── partially addressed by Component_Triage_System.md Gate Correspondence table
  └── UNK-024 (forge duty threshold) — fills the remaining A/C boundary gap

UNK-024 (forge duty threshold)
  └── feeds into UNK-012 resolution

UNK-025 (contamination routing)
  └── affects Component_Triage_System.md, Lazarus_forge_v0_flow.md, Air_Scrubber_v0.md

UNK-013 (confidence threshold definition)
  └── UNK-008 (autonomy architecture must implement it)
  └── UNK-019 (governance fail-safe depends on defined mechanism)

UNK-016 (governance failure modes)
  └── UNK-019 (fail-safe design depends on failure mode definitions)

UNK-014 (weaponization pattern detection)
  └── hook added in Component_Triage_System.md Station 0
  └── full mechanism still pending

UNK-020 (auditor effectiveness metrics)
  └── UNK-004 (cycle definitions needed before metrics can be measured)

UNK-021 (override vs. immutability reconciliation)
  └── UNK-019 (governance fail-safe)
  └── UNK-013 (confidence threshold)

UNK-023 (audit trail schema)
  └── UNK-004 (cycle definitions inform schema versioning)
  └── UNK-020 (metrics depend on trail schema existing)

UNK-002 (repo topology) [RESOLVED]
  └── UNK-003 (assumption contracts) [DEFERRED]

UNK-004 (Expiry Rule) [DEFERRED — activates post-audit-cycle completion]
```

---

## Registry

---

### [UNK-001] — Discovery.md update pending for Unknowns_LF.md entry
**What is not yet known:** Whether `Discovery.md` has been updated to include `Unknowns_LF.md` in the reading order, file summaries, and with a raw GitHub URL.
**Why it matters:** `Discovery.md` is the navigation layer. A file absent from it is invisible to returning AI agents and new contributors.
**Resolution path:** Confirm Discovery.md update committed with reading order entry, file summary, and raw GitHub URL. Close on confirmation.
**Affected files:** `Discovery.md`, this file
**Depends on:** None
**Owner:** Connective Tissue
**Activation trigger:** Next commit to Discovery.md, or next audit cycle
**Risk type:** Interface gap
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open — Discovery.md update pending confirmation

---

### [UNK-003] — Cross-repo assumption contracts not yet documented
**What is not yet known:** Whether bidirectional assumption contracts exist between LazarusForgeV0 and companion repositories.
**Why it matters:** Shared module assumptions exist as claims in one repo with no counterpart in the other.
**Resolution path:** When Astroid-miner is activated, create stub `Assumption_Contracts.md` in both repos.
**Affected files:** `Auditor_Protocols.md`, `geck_forge_seed.md`, `Air_Scrubber_v0.md`, `Spin_Chamber_v0.md`
**Depends on:** UNK-002 (resolved)
**Owner:** Skeptic/Auditor
**Activation trigger:** Leviathan deployment milestone; Astroid-miner activated
**Risk type:** Interface gap
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — activates at Leviathan milestone

---

### [UNK-004] — Expiry Rule has no enforcement mechanism
**What is not yet known:** What constitutes a "version cycle" for the Expiry Rule.
**Why it matters:** Registry infrastructure. Deferred — registry is in active development.
**Resolution path:** Version cycle definition and Expiry check responsibility added to Auditor_Protocols.md v0.4. Pending: activation of measurement once first full audit cycle is complete.
**Affected files:** `Auditor_Protocols.md`, this file
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** First full audit cycle across all primary documents complete
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking — deferred per human decision
**Priority (Promotion):** Blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — partially addressed in Auditor_Protocols.md v0.4; activates when first full audit cycle is complete

---

### [UNK-005] — Marine G.E.C.K. seed variant not yet defined
**What is not yet known:** Minimum viable seed configuration for marine Forge deployment.
**Why it matters:** Terrestrial G.E.C.K. modules do not map cleanly to marine deployment.
**Resolution path:** Add a marine variant stub to `geck_forge_seed.md`. Full spec routes to `Trajectories_LF.md`.
**Affected files:** `geck_forge_seed.md`, `Support_Raft_v0.md`, `leviathan_testing.md`
**Depends on:** UNK-006
**Owner:** Engineer
**Activation trigger:** Leviathan hardware design begins; or Support Raft v1.0 specification starts
**Risk type:** Unknown
**Priority (Exploration):** Exploratory
**Priority (Promotion):** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

### [UNK-006] — Power envelope for Leviathan has no placeholder anchor
**What is not yet known:** Order-of-magnitude power budget for a Leviathan unit under nominal, degraded, and dormancy conditions.
**Why it matters:** Autonomy claims, endurance claims, and load-shedding behavior cannot be tested without a power substrate.
**Resolution path:** Survey deep-sea AUV analog systems. Add stub Power Budget section to `leviathan_testing.md`. Requires UNK-011 first.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Depends on:** UNK-011
**Owner:** Energy
**Activation trigger:** Any attempt to define Leviathan test scenarios; or any hardware component selection
**Risk type:** Unknown
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open — depends on UNK-011

---

### [UNK-007] — Deep-ocean storage degradation under pressure and low temperature is unacknowledged
**What is not yet known:** How sealed cell storage behaves at Leviathan operating depths and temperatures over extended mission durations.
**Why it matters:** "Predictable degradation" asserted without acknowledging well-documented pressure and thermal failure modes.
**Resolution path:** Literature review using AUV fleet data (MBARI, WHOI). Results feed into `energy_v0.md`.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Depends on:** None (parallel with UNK-011)
**Owner:** Energy
**Activation trigger:** Any attempt to select or specify energy storage hardware
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-008] — Leviathan autonomy architecture is unspecified — testability gap
**What is not yet known:** What decision-making paradigm(s) are under test.
**Why it matters:** Falsification requires a stated hypothesis. Without naming the architecture, the framework risks becoming a scenario generator.
**Resolution path:** Add candidate architecture section to `leviathan_testing.md` with: (1) observable decision loop; (2) failure signature; (3) minimal test scenario. Minimum viable: two candidates, all three elements each.
**Affected files:** `leviathan_testing.md`, `Trajectories_LF.md`
**Depends on:** UNK-006
**Owner:** Autonomy / Skeptic/Auditor
**Activation trigger:** Any attempt to define Leviathan test scenarios; or any autonomy-related hardware or software selection
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-009] — Trust model mechanism in Extension B is undefined
**What is not yet known:** Decay function, false-positive definition, trust floor, and initialization state for peer trust scoring.
**Why it matters:** Anti-pattern safeguards depend on trust diversity. The behavioral description implies a mechanism without specifying one.
**Resolution path:** Label trust model as Placeholder in Extension B. Full mechanism routes to `Trajectories_LF.md`.
**Affected files:** `leviathan_testing.md` (Extensions)
**Depends on:** UNK-008
**Owner:** Autonomy
**Activation trigger:** Multi-unit Leviathan deployment planning begins; or Extension B promoted toward specification
**Risk type:** Missing mechanism
**Priority (Exploration):** Exploratory
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-010] — Priority propagation in disconnected network has no enforcement mechanism
**What is not yet known:** How Tier 1 data reaches out-of-contact units faster than Tier 3 data.
**Why it matters:** "Errors travel faster than optimizations" is stated as a design principle without a mechanism that enforces it.
**Resolution path:** Designate as primary test target for multi-unit deployments. Full mechanism routes to `Trajectories_LF.md`.
**Affected files:** `leviathan_testing.md` (Extensions)
**Depends on:** UNK-008
**Owner:** Autonomy / Engineer
**Activation trigger:** Multi-unit Leviathan deployment planning begins; or networking layer specified
**Risk type:** Assumption
**Priority (Exploration):** Exploratory
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-011] — Forge power demand is uncharacterized at any operating mode
**What is not yet known:** What the terrestrial Lazarus Forge consumes at bootstrap, nominal, and degraded operating modes.
**Why it matters:** Without a demand side, UNK-006 cannot be scoped.
**Resolution path:** Power Demand stub added to `energy_v0.md` (May 2026). Next step: replace Placeholders as hardware selection proceeds.
**Affected files:** `energy_v0.md`, `leviathan_testing.md`, `Lazarus_forge_v0_flow.md`
**Depends on:** None
**Owner:** Energy
**Activation trigger:** Any attempt to scope UNK-006; or any hardware selection for processing modules
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** energy_v0.md audit cycle, May 2026
**Status:** In Progress — stub added to energy_v0.md; Placeholder figures in place

---

### [UNK-012] — Gate logic determinism in Lazarus_forge_v0_flow.md is unverified
**What is not yet known:** Whether gate logic (A→B→C→D) produces deterministic routing for all item types, or whether boundary cases require human judgment more frequently than implied.
**Why it matters:** The flow document is the terminology reference standard. Gate ambiguity propagates silently into every implementing document.
**Resolution path:** Gate Correspondence table added to Component_Triage_System.md (May 2026 revision) — maps station outcomes to Gates A–D explicitly. Motor worked example added to Station 1 (65% torque → Gate A fail, Gate C pass). This partially resolves the Gate A/C boundary. Remaining gap: UNK-024 (forge duty threshold) must be resolved to fully close the A/C boundary. Gate C/D boundary and Human/AI Oversight Gate worked examples still needed.
**Affected files:** `Lazarus_forge_v0_flow.md`, `Component_Triage_System.md`
**Depends on:** None
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Any module begins implementing triage or classification logic; or next revision of flow document
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Lazarus_forge_v0_flow.md audit cycle, May 2026
**Status:** In Progress — Gate A/C partially addressed; Gate C/D boundary and Oversight Gate worked examples still needed

---

### [UNK-013] — "Sufficient confidence" threshold is undefined across governance document
**What is not yet known:** What confidence level triggers the default-to-non-action rule. Whether "sufficient confidence," "confidently classified," and "reasonably bounded" represent the same threshold or a graduated scale.
**Why it matters:** Undefined thresholds in the parent governance document are not implementable and produce inconsistent agent behavior.
**Resolution path:** Add Confidence Thresholds section to `Ethical_Constraints.md`. Full mechanism may route to `Trajectories_LF.md` with Placeholder anchor.
**Affected files:** `Ethical_Constraints.md`, any autonomy or classification implementation
**Depends on:** UNK-008
**Owner:** Skeptic/Auditor / Engineer
**Activation trigger:** Any implementation of classification or refusal logic; or v0.3 revision of Ethical_Constraints.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-014] — Anti-Weaponization pattern-matching mechanism is undefined
**What is not yet known:** What constitutes a "pattern match" to weapons development. Pattern space, matching method, false-positive handling, and edge case escalation path are all absent.
**Why it matters:** The hardest constraint in the repository depends on a detection mechanism that has not been specified.
**Resolution path:** Add Pattern Recognition Annex to `Ethical_Constraints.md`. Hook added to Component_Triage_System.md Station 0 (May 2026 revision) — flagging step now exists at triage entry. Plasma cutter paradox is the concrete test case. Full mechanism still needed.
**Affected files:** `Ethical_Constraints.md`, `Component_Triage_System.md`
**Depends on:** None
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Any implementation of refusal logic; or v0.3 revision of Ethical_Constraints.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** In Progress — hook added at Component_Triage_System.md Station 0; full pattern mechanism still open

---

### [UNK-015] — Human escalation path has no defined mechanism
**What is not yet known:** How escalation to human review is performed — channel, recipient, response time, system behavior during hold, timeout behavior.
**Why it matters:** "Escalate to human review" appears throughout the parent governance document without definition. In Leviathan deployments, an undefined escalation path means the primary safety valve may not function.
**Resolution path:** Escalation Protocol section added to Ethical_Constraints.md v0.3. Communications layer detail routes to `leviathan_testing.md`. Pending: commitment confirmation.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** UNK-006 (comms availability), UNK-008
**Owner:** Autonomy / Engineer
**Activation trigger:** Leviathan hardware design begins; or any test scenario requires human escalation
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** In Progress — addressed in Ethical_Constraints.md v0.3 draft; pending commit confirmation

---

### [UNK-016] — Governance layer failure modes are unspecified
**What is not yet known:** How the ethics substrate can fail, how failure would be detected, and what fallback behavior applies.
**Why it matters:** A governance document that describes only normal operation fails the Lifecycle Truncation standard.
**Resolution path:** Governance Failure Modes section added to Ethical_Constraints.md v0.3. Pending commit confirmation.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** v0.3 revision of Ethical_Constraints.md; or Leviathan testing begins
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** In Progress — addressed in Ethical_Constraints.md v0.3 draft; pending commit confirmation

---

### [UNK-017] — Life-preservation vs. Anti-Weaponization priority conflict unresolved
**What is not yet known:** Whether an acute human life preservation claim can override the Anti-Weaponization Doctrine.
**Why it matters:** "We need this capability to protect lives" is the most common historical justification for weapons development. Silence implies "no exception" — but that must be stated, not assumed.
**Resolution path:** Explicit humanitarian framing clause added to Ethical_Constraints.md v0.3 (Anti-Weaponization Doctrine section). Pending commit confirmation.
**Affected files:** `Ethical_Constraints.md`
**Depends on:** None
**Owner:** Skeptic/Auditor / human governing party
**Activation trigger:** v0.3 revision of Ethical_Constraints.md
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** In Progress — addressed in Ethical_Constraints.md v0.3 draft; pending commit confirmation

---

### [UNK-018] — Ethical log survival under unit loss or communication blackout
**What is not yet known:** How refusal logs survive unit loss, hardware failure, or communication blackout in remote deployments.
**Why it matters:** A unit that refuses and then fails may take the record of that refusal with it.
**Resolution path:** Add Log Survival section to `Ethical_Constraints.md` or `leviathan_testing.md`. Route implementation to delay-tolerant networking section.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** UNK-010
**Owner:** Engineer / Autonomy
**Activation trigger:** Leviathan hardware design begins; or logging architecture is specified
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Non-blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-019] — Governance fail-safe behavior if ethics substrate fails
**What is not yet known:** What the system does if the ethics substrate itself fails or produces systematic false negatives.
**Why it matters:** A governance system with no defined fail-safe defaults to whatever the underlying system does.
**Resolution path:** Explicit fail-safe behavior added to Ethical_Constraints.md v0.3. Pending commit confirmation.
**Affected files:** `Ethical_Constraints.md`
**Depends on:** UNK-013, UNK-016
**Owner:** Skeptic/Auditor
**Activation trigger:** v0.3 revision of Ethical_Constraints.md; or UNK-016 resolution begins
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** In Progress — addressed in Ethical_Constraints.md v0.3 draft; pending commit confirmation

---

### [UNK-020] — Auditor effectiveness metrics and competence verification
**What is not yet known:** How to measure whether the audit process is adding value and whether an auditor possesses sufficient domain knowledge.
**Why it matters:** A verification system without measured performance risks becoming Checklist Theater.
**Resolution path:** Protocol Performance section added to Auditor_Protocols.md v0.4 as Placeholder. Activation deferred to UNK-004 trigger.
**Affected files:** `Auditor_Protocols.md`, `leviathan_testing.md`
**Depends on:** UNK-004
**Owner:** Skeptic/Auditor
**Activation trigger:** First full audit cycle complete; or v0.4 revision of Auditor_Protocols.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** In Progress — Placeholder section added to Auditor_Protocols.md v0.4; metrics pending UNK-004 activation

---

### [UNK-021] — Reconciliation between human override rights and Ethical_Constraints immutability
**What is not yet known:** How documented human overrides of Auditor flags interact with non-overrideable doctrines in Ethical_Constraints.md.
**Why it matters:** Auditor_Protocols grants humans override rights; Ethical_Constraints treats hard-line doctrines as non-overrideable. These are not yet reconciled.
**Resolution path:** Scope clarification added to Auditor_Protocols.md v0.4 in both Governing Principle and Human Contributor Protocols sections. One sentence each, cross-linked.
**Affected files:** `Auditor_Protocols.md`, `Ethical_Constraints.md`
**Depends on:** UNK-019, UNK-013
**Owner:** Skeptic/Auditor / Synthesizer
**Activation trigger:** Any override attempt near hard ethical constraints; or next revision of either document
**Risk type:** Interface gap
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** In Progress — addressed in Auditor_Protocols.md v0.4; pending commit confirmation

---

### [UNK-022] — Full Stop Review trigger conditions are underspecified
**What is not yet known:** What specific conditions warrant invoking a Full Stop Review.
**Why it matters:** Without defined trigger conditions, Full Stop Review is subject to both overuse and underuse.
**Resolution path:** Three specific trigger conditions and invocation record format added to Auditor_Protocols.md v0.4.
**Affected files:** `Auditor_Protocols.md`
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** Next revision of Auditor_Protocols.md; or any contributor attempts to invoke Full Stop Review
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** Resolved — addressed in Auditor_Protocols.md v0.4

---

### [UNK-023] — Audit trail schema is undefined
**What is not yet known:** A standard reproducible format for recording what was checked, who checked it, what gates were passed or blocked.
**Why it matters:** Prose audit comments cannot be queried, compared across cycles, or used to detect patterns. Prerequisite for UNK-020.
**Resolution path:** Required fields list and worked example added to Auditor_Protocols.md v0.4 Observability section. JSON/YAML schema deferred to when tooling exists.
**Affected files:** `Auditor_Protocols.md`
**Depends on:** UNK-004, UNK-020
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Next revision of Auditor_Protocols.md; or first attempt to query audit history
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** In Progress — structured markdown format added to Auditor_Protocols.md v0.4; JSON/YAML deferred

---

### [UNK-024] — "Sufficient for forge duty" threshold is undefined
**What is not yet known:** A quantitative or contextual definition of acceptable degraded performance for components assigned to forge duty rather than original application. The 70% performance threshold in Station 1 does not distinguish Gate A (original function) from Gate C (reduced function) — both can satisfy 70% depending on which application context is being evaluated.
**Why it matters:** This is the primary remaining Gate A/C boundary ambiguity after UNK-012 partial resolution. An undefined threshold means the same component can route to the Component Library (Gate A) or to Repurpose (Gate C) depending on operator interpretation. As Gen-1 forge operations accumulate, inconsistent routing will produce inconsistent component quality in the library. Directly feeds UNK-012 resolution.
**Resolution path:** Define threshold as application-specific rather than a single percentage: (1) for original-application reuse (Gate A) — performance must meet the original equipment specification within a defined tolerance, labeled Analogous or Measured from Gen-1 data; (2) for forge-duty reuse (Gate C) — performance must meet the specific forge task requirement, defined per task class (ventilation, pumping, structural). A "Baseline Performance Table" for the 5 most common salvaged component classes (motors, bearings, inverters, pumps, structural members) would operationalize this. Populate from Gen-1 operational data after N≥50 observations per class.
**Affected files:** `Component_Triage_System.md`, `Lazarus_forge_v0_flow.md`
**Depends on:** None (UNK-012 depends on this)
**Owner:** Engineer
**Activation trigger:** Gen-1 forge begins triage operations; or Station 1 pass guidance is revised; or UNK-012 resolution resumes
**Risk type:** Assumption — "70% performance" implies a single threshold that applies regardless of application context
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Component_Triage_System.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-025] — Contamination routing protocol in triage is undefined
**What is not yet known:** How chemically or biologically contaminated components are handled through the triage station sequence — whether there is a pre-station decontamination step, what constitutes acceptable decontamination, what happens to components that cannot be decontaminated, and how contamination type and degree are recorded on provenance tags.
**Why it matters:** `Lazarus_forge_v0_flow.md` defines contamination level as a classification attribute. `Component_Triage_System.md` has no contamination handling path beyond a Station 0 visual flag. Chemically contaminated components passed through electrical or mechanical stations without decontamination risk operator safety and downstream Purification contamination. Three of four audit passes flagged this gap independently.
**Resolution path:** Add a contamination handling protocol to `Component_Triage_System.md`: (1) Station 0 contamination check — identify type (chemical/biological) and severity; (2) contaminated items routed to decontamination hold before electrical or mechanical stations; (3) decontamination criteria — what constitutes safe for further triage; (4) items that cannot be decontaminated route directly to Material Recovery with contamination noted; (5) provenance tag must include contamination status and decontamination outcome. Cross-reference `Air_Scrubber_v0.md` for chemical handling and whatever safety protocol exists for hazardous materials.
**Affected files:** `Component_Triage_System.md`, `Lazarus_forge_v0_flow.md`, `Air_Scrubber_v0.md`
**Depends on:** None
**Owner:** Engineer
**Activation trigger:** Gen-1 forge begins triage operations; or any contaminated material enters the triage stream; or Component_Triage_System.md is revised
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Component_Triage_System.md multi-model audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

*(None flagged at v0.8 — all entries within first or second cycle. UNK-004 deferred by human decision.)*

---

## Resolved Unknowns Archive

### [UNK-002] — Repository topology: `Astroid-miner` is planned, deferred
**Resolved:** May 2026 — human confirmation. Deferred until Leviathan milestone.

### [UNK-022] — Full Stop Review trigger conditions
**Resolved:** May 2026 — three specific trigger conditions and invocation record format added to Auditor_Protocols.md v0.4.

---

## Audit Trail

**v0.1 — May 2026:** First audit cycle (Discovery.md, Auditor_Protocols.md). UNK-001 through UNK-005.
**v0.2 — May 2026:** Second audit cycle (leviathan_testing.md). UNK-006 through UNK-010. UNK-002 resolved.
**v0.3 — May 2026:** Structural upgrade from ChatGPT review. Owner, Activation Trigger, Depends On, Risk Type, phase-split Priority, Dependency Map added.
**v0.4 — May 2026:** Third audit cycle (energy_v0.md). UNK-011 added.
**v0.5 — May 2026:** Fourth audit cycle (Lazarus_forge_v0_flow.md). UNK-012 added. UNK-004 deferred.
**v0.6 — May 2026:** Fifth audit cycle (Ethical_Constraints.md) — multi-model. UNK-013 through UNK-019 added.
**v0.7 — May 2026:** Sixth audit cycle (Auditor_Protocols.md) — multi-model. UNK-020 through UNK-023 added.
**v0.8 — May 2026:** Seventh audit cycle (Component_Triage_System.md) — multi-model: Claude, Gemini, Grok, ChatGPT.
Two unknowns added: UNK-024 (forge duty threshold), UNK-025 (contamination routing protocol).
UNK-012 status updated to In Progress — Gate Correspondence table and worked example added to Component_Triage_System.md; remaining gap feeds UNK-024.
UNK-014 status updated to In Progress — hook added at Station 0 of Component_Triage_System.md.
UNK-022 moved to Resolved Archive — addressed in Auditor_Protocols.md v0.4.
Dependency Map updated: UNK-024 feeds UNK-012; UNK-025 affects Air_Scrubber_v0.md.
Multiple UNK entries from v0.6/v0.7 updated to In Progress status — Ethical_Constraints.md v0.3 and Auditor_Protocols.md v0.4 drafts address them pending commit confirmation.

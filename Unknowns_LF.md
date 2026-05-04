# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.9 — UNK-026 added from Components.md audit. UNK-012 and UNK-024 updated with new inputs.**
**v1.0 trigger: first full audit cycle across all primary documents complete. Expiry Rule activates.**

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

UNK-026 (Graduation Rule detection circularity)
  └── feeds UNK-012 (gate logic determinism — concrete input)

UNK-024 (forge duty threshold)
  └── feeds UNK-012 resolution
  └── requires Forge loop definition (Bootstrap Doctrine)

UNK-012 (gate logic determinism)
  └── partially addressed: Gate Correspondence table in Component_Triage_System.md
  └── remaining: detection circularity (UNK-026), forge duty threshold (UNK-024),
      Gate C/D boundary worked example

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

UNK-004 (Expiry Rule) [DEFERRED — activates at v1.0 / first full audit cycle complete]
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
**Resolution path:** Version cycle definition and Expiry check responsibility added to Auditor_Protocols.md v0.4. Activation deferred to v1.0 — first full audit cycle complete.
**Affected files:** `Auditor_Protocols.md`, this file
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** v1.0 of this registry — first full audit cycle across all primary documents complete
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking — deferred per human decision
**Priority (Promotion):** Blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — activates at registry v1.0

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
**Resolution path:** Gate Correspondence table added to Component_Triage_System.md — maps station outcomes to Gates A–D. Motor worked example added (65% torque → Gate A fail, Gate C pass). Remaining gaps: (1) UNK-026 detection circularity in Graduation Rule requires human-in-the-loop proxy at v0; (2) UNK-024 forge duty threshold must be explicitly defined; (3) Gate C/D boundary and Human/AI Oversight Gate worked examples still needed in Lazarus_forge_v0_flow.md.
**Affected files:** `Lazarus_forge_v0_flow.md`, `Component_Triage_System.md`, `Components.md`
**Depends on:** None
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Any module begins implementing triage or classification logic; or next revision of flow document
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Lazarus_forge_v0_flow.md audit cycle, May 2026
**Status:** In Progress — Gate A/C partially addressed; three remaining gaps identified

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
**Resolution path:** Add Pattern Recognition Annex to `Ethical_Constraints.md`. Hook added to Component_Triage_System.md Station 0. Plasma cutter paradox is the concrete test case. Full mechanism still needed.
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
**Why it matters:** "Escalate to human review" appears throughout the parent governance document without definition.
**Resolution path:** Escalation Protocol section added to Ethical_Constraints.md v0.3 draft. Pending commit confirmation.
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
**Resolution path:** Governance Failure Modes section added to Ethical_Constraints.md v0.3 draft. Pending commit confirmation.
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
**Why it matters:** Silence implies "no exception" — but that must be stated, not assumed, because the assumption will be tested.
**Resolution path:** Explicit humanitarian framing clause added to Ethical_Constraints.md v0.3 draft. Pending commit confirmation.
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
**Resolution path:** Add Log Survival section to `Ethical_Constraints.md` or `leviathan_testing.md`.
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
**Resolution path:** Explicit fail-safe behavior added to Ethical_Constraints.md v0.3 draft. Pending commit confirmation.
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
**What is not yet known:** How to measure whether the audit process is adding value.
**Why it matters:** A verification system without measured performance risks becoming Checklist Theater.
**Resolution path:** Protocol Performance section added to Auditor_Protocols.md v0.4 as Placeholder. Activation deferred to UNK-004 trigger (registry v1.0).
**Affected files:** `Auditor_Protocols.md`, `leviathan_testing.md`
**Depends on:** UNK-004
**Owner:** Skeptic/Auditor
**Activation trigger:** Registry v1.0 / first full audit cycle complete
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** In Progress — Placeholder section added to Auditor_Protocols.md v0.4; metrics pending v1.0

---

### [UNK-021] — Reconciliation between human override rights and Ethical_Constraints immutability
**What is not yet known:** How documented human overrides of Auditor flags interact with non-overrideable doctrines in Ethical_Constraints.md.
**Why it matters:** Auditor_Protocols grants humans override rights; Ethical_Constraints treats hard-line doctrines as non-overrideable. Not yet reconciled.
**Resolution path:** Scope clarification added to Auditor_Protocols.md v0.4 in both Governing Principle and Human Contributor Protocols sections.
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

### [UNK-023] — Audit trail schema is undefined
**What is not yet known:** A standard reproducible format for recording what was checked, who checked it, what gates were passed or blocked.
**Why it matters:** Prose audit comments cannot be queried, compared across cycles, or used to detect patterns. Prerequisite for UNK-020.
**Resolution path:** Required fields list and worked example added to Auditor_Protocols.md v0.4. JSON/YAML schema deferred.
**Affected files:** `Auditor_Protocols.md`
**Depends on:** UNK-004, UNK-020
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** First attempt to query audit history across multiple cycles
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** In Progress — structured markdown format added to Auditor_Protocols.md v0.4; JSON/YAML deferred

---

### [UNK-024] — "Sufficient for forge duty" threshold is undefined
**What is not yet known:** A quantitative or contextual definition of acceptable degraded performance for components assigned to forge duty. The 70% threshold in Station 1 does not distinguish Gate A (original function) from Gate C (reduced function).
**Why it matters:** Primary remaining Gate A/C boundary ambiguity after UNK-012 partial resolution. Inconsistent routing produces inconsistent component quality in the library.
**Resolution path:** Bootstrap Doctrine in Components.md offers the best current candidate: "A component is sufficient if it allows the Forge loop to close." However, "the Forge loop" is not yet explicitly defined — adding one sentence defining the loop to the Bootstrap Doctrine section would make the sufficiency criterion falsifiable and directly resolve this unknown. Define as application-specific thresholds once Gen-1 operational data is available. Populate Baseline Performance Table after N≥50 observations per component class.
**Affected files:** `Component_Triage_System.md`, `Lazarus_forge_v0_flow.md`, `Components.md`
**Depends on:** None (UNK-012 depends on this)
**Owner:** Engineer
**Activation trigger:** Gen-1 forge begins triage operations; or Station 1 pass guidance is revised; or UNK-012 resolution resumes
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Component_Triage_System.md multi-model audit cycle, May 2026
**Status:** In Progress — Bootstrap Doctrine candidate identified in Components.md; Forge loop definition needed to make it falsifiable

---

### [UNK-025] — Contamination routing protocol in triage is undefined
**What is not yet known:** How chemically or biologically contaminated components are handled through the triage station sequence — decontamination steps, acceptability criteria, routing for components that cannot be decontaminated, and provenance tag requirements.
**Why it matters:** Contaminated components passed through electrical or mechanical stations without decontamination risk operator safety and downstream Purification contamination.
**Resolution path:** Station 0 contamination check and Contaminated bin added to Component_Triage_System.md (May 2026 revision). Full decontamination protocol still needed. Cross-reference `Air_Scrubber_v0.md` for chemical handling.
**Affected files:** `Component_Triage_System.md`, `Lazarus_forge_v0_flow.md`, `Air_Scrubber_v0.md`
**Depends on:** None
**Owner:** Engineer
**Activation trigger:** Gen-1 forge begins triage operations; or any contaminated material enters the triage stream
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Component_Triage_System.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-026] — Graduation Rule detection circularity at v0
**What is not yet known:** How the Graduation Rule's detection requirement is satisfied at v0, when the Advanced Sensing capability needed to detect component degradation is classified as Useful (non-critical) rather than Critical. A component cannot graduate until the Forge can detect its degradation — but detection capability may not yet exist when graduation decisions need to be made.
**Why it matters:** This is a concrete architectural circularity in `Components.md` that feeds directly into UNK-012 (gate logic determinism). The Graduation Rule implies automation of a decision that requires sensing capability the forge doesn't yet have. At Gen-1 scale with a skilled human operator this gap is filled informally — but as automation increases, the absence of an explicit proxy mechanism becomes a real failure mode. Four audit passes on the component stack converged on this pattern.
**Resolution path:** Two options: (1) elevate basic degradation detection (not Advanced Sensing — just threshold monitoring of critical components) to Critical status at v0, explicitly acknowledging it as a bootstrap requirement; or (2) explicitly state in the Bootstrap Doctrine that graduation decisions at v0 require human-in-the-loop verification as a proxy for automated detection, and that this proxy is a defined v0 operating condition, not a gap. Either answer closes the circularity. The second option is lower effort and more honest about v0 reality. Add one sentence to the Graduation Rule: *"At v0, graduation assessment requires human operator verification as a proxy for automated degradation detection."*
**Affected files:** `Components.md`, `Lazarus_forge_v0_flow.md`, `Component_Triage_System.md`
**Depends on:** None (feeds UNK-012)
**Owner:** Engineer
**Activation trigger:** Components.md next revision; or any automation of graduation decisions begins
**Risk type:** Assumption — Graduation Rule implies detection capability exists when it may not
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Components.md audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

*(None flagged at v0.9 — all entries within first or second cycle. UNK-004 deferred; activates at registry v1.0.)*

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
**v0.7 — May 2026:** Sixth audit cycle (Auditor_Protocols.md) — multi-model. UNK-020 through UNK-023 added. UNK-022 resolved.
**v0.8 — May 2026:** Seventh audit cycle (Component_Triage_System.md) — multi-model. UNK-024, UNK-025 added. UNK-012 and UNK-014 updated to In Progress.
**v0.9 — May 2026:** Eighth audit cycle (Components.md). UNK-026 added (Graduation Rule detection circularity). UNK-012 updated with three remaining gaps. UNK-024 updated with Bootstrap Doctrine candidate resolution path. UNK-004 activation trigger updated to registry v1.0.

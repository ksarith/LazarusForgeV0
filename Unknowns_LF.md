# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.7 — UNK-020 through UNK-023 added from Auditor_Protocols.md multi-model audit cycle (Claude, ChatGPT, Gemini + Gemini synthesis).**

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
  └── affects any module implementing triage or classification logic
  └── UNK-014 (weaponization pattern detection routes here)

UNK-013 (confidence threshold definition)
  └── UNK-008 (autonomy architecture must implement it)
  └── UNK-019 (governance fail-safe depends on defined mechanism)

UNK-016 (governance failure modes)
  └── UNK-019 (fail-safe design depends on failure mode definitions)

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
**Why it matters:** Registry infrastructure. Deferred — registry is in active development, forcing enforcement now is premature.
**Resolution path:** Add to `Auditor_Protocols.md`: version cycle definition; "logged in version" as required field; Expiry check assigned to Skeptic/Auditor at each audit cycle opening.
**Affected files:** `Auditor_Protocols.md`, this file
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** First full audit cycle across all primary documents complete; OR any unknown reaches two audit cycles without a resolution path
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking — deferred per human decision
**Priority (Promotion):** Blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — activates when first full audit cycle is complete

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
**Why it matters:** Autonomy claims, endurance claims, and load-shedding behavior cannot be tested without a power substrate. UNK-008 and UNK-015 cannot be scoped without this.
**Resolution path:** Survey deep-sea AUV analog systems. Add stub Power Budget section to `leviathan_testing.md`, cross-referenced to `energy_v0.md`. Requires UNK-011 first.
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
**Resolution path:** Literature review using AUV fleet data (MBARI, WHOI). Results feed into `energy_v0.md`. Run in parallel with UNK-011.
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
**Why it matters:** Falsification requires a stated hypothesis. Without naming the architecture, the framework risks becoming a scenario generator rather than a hypothesis-testing system.
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
**What is not yet known:** How Tier 1 (critical failure) data reaches out-of-contact units faster than Tier 3 data.
**Why it matters:** "Errors travel faster than optimizations" is stated as a design principle without a mechanism that enforces it.
**Resolution path:** Acknowledge as open design question. Designate as primary test target for multi-unit deployments. Full mechanism routes to `Trajectories_LF.md`.
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
**Why it matters:** Without a demand side, UNK-006 cannot be scoped. Load-bearing gap in the entire energy chain.
**Resolution path:** Power Demand stub added to `energy_v0.md` (May 2026) with Placeholder figures. Next step: replace Placeholders as hardware selection proceeds.
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
**Resolution path:** Add 2–3 worked examples hitting the Gate A/C boundary, Gate C/D boundary, and a Human/AI Oversight Gate edge case.
**Affected files:** `Lazarus_forge_v0_flow.md`, `Component_Triage_System.md`
**Depends on:** None
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Any module begins implementing triage or classification logic; or next revision of flow document
**Risk type:** Assumption
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Lazarus_forge_v0_flow.md audit cycle, May 2026
**Status:** Open

---

### [UNK-013] — "Sufficient confidence" threshold is undefined across governance document
**What is not yet known:** What confidence level triggers the default-to-non-action rule. Whether "sufficient confidence," "confidently classified," and "reasonably bounded" represent the same threshold or a graduated scale.
**Why it matters:** Undefined thresholds in the parent governance document are not implementable and produce inconsistent agent behavior.
**Resolution path:** Add a Confidence Thresholds section to `Ethical_Constraints.md` defining: (1) working definition; (2) whether phrasings represent one standard or graduated scale; (3) assessment method. Full mechanism may route to `Trajectories_LF.md` with Placeholder anchor here.
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
**Why it matters:** The hardest constraint in the repository depends on a detection mechanism that has not been specified. An undefined detector is not a hard line — it is a stated intention.
**Resolution path:** Add Pattern Recognition Annex to `Ethical_Constraints.md`: (1) example pattern categories; (2) detection method; (3) false-positive handling; (4) edge case escalation. The plasma cutter paradox (industrial tool vs. weapon component based solely on output parameters) is the concrete test case that should drive pattern definition work.
**Affected files:** `Ethical_Constraints.md`, `Component_Triage_System.md`
**Depends on:** None
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Any implementation of refusal logic; or v0.3 revision of Ethical_Constraints.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-015] — Human escalation path has no defined mechanism
**What is not yet known:** How escalation to human review is performed — channel, recipient, response time, system behavior during hold, and timeout behavior.
**Why it matters:** "Escalate to human review" appears throughout the parent governance document as the resolution for legal ambiguity and ethical edge cases. In Leviathan deployments with intermittent connectivity, an undefined escalation path means the primary safety valve may not function.
**Resolution path:** Add Escalation Protocol section to `Ethical_Constraints.md`. Route communications layer detail to `leviathan_testing.md`.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** UNK-006 (comms availability), UNK-008 (autonomy architecture governs hold behavior)
**Owner:** Autonomy / Engineer
**Activation trigger:** Leviathan hardware design begins; or any test scenario requires human escalation
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-016] — Governance layer failure modes are unspecified
**What is not yet known:** How the ethics substrate can fail, how failure would be detected, and what fallback behavior applies if the governance layer is compromised or producing false negatives.
**Why it matters:** A governance document that describes only normal operation fails the same Lifecycle Truncation standard applied to module specs. Silent ethics layer failure has no compensation mechanism.
**Resolution path:** Add Governance Failure Modes section to `Ethical_Constraints.md`. Note that Pacifist Operating Posture may already function as the fallback — if so, make this explicit.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** v0.3 revision of Ethical_Constraints.md; or Leviathan testing begins
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-017] — Life-preservation vs. Anti-Weaponization priority conflict unresolved
**What is not yet known:** Whether an acute human life preservation claim can override the Anti-Weaponization Doctrine.
**Why it matters:** "We need this capability to protect lives" is the most common historical justification for weapons development. The document cited Nobel and Oppenheimer. Silence implies "no exception" — but that must be stated, not assumed, because the assumption will be tested.
**Resolution path:** Add explicit clause to Anti-Weaponization Doctrine. Either humanitarian framing does not override (with reasoning), or a narrowly defined exception with strict scope limits. This is a human governing party decision. *Note: v0.3 of Ethical_Constraints.md addresses this directly — verify clause was committed.*
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
**What is not yet known:** How refusal logs and ethical decision records survive unit loss, hardware failure, or communication blackout in remote deployments.
**Why it matters:** Ethical_Constraints.md requires refusal decisions be logged. In a Leviathan deployment, a unit that refuses and then fails may take that record with it — potentially losing the most important refusal in the system's history.
**Resolution path:** Add Log Survival section to `Ethical_Constraints.md` or `leviathan_testing.md`: minimum logging requirements, local storage, transmission protocol, acceptable data loss threshold. Route implementation to delay-tolerant networking section of `leviathan_testing.md`.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** UNK-010 (priority propagation — logs may need Tier 1 transmission priority)
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
**Why it matters:** A governance system with no defined fail-safe defaults to whatever the underlying system does — which may not be safe. The Pacifist Operating Posture may already cover this implicitly; if so it needs to be explicit.
**Resolution path:** Define explicit fail-safe in `Ethical_Constraints.md`: (1) detected failure → halt all non-observational action; (2) anomalous patterns → escalate per UNK-015; (3) fail-safe state is logged. Verify whether Pacifist Operating Posture already covers this.
**Affected files:** `Ethical_Constraints.md`
**Depends on:** UNK-013 (can't define fail-safe for undefined confidence mechanism), UNK-016 (failure modes must be defined before fail-safe can be triggered)
**Owner:** Skeptic/Auditor
**Activation trigger:** v0.3 revision of Ethical_Constraints.md; or UNK-016 resolution begins
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-020] — Auditor effectiveness metrics and competence verification
**What is not yet known:** How to measure whether the audit process is actually adding value — and whether an auditor (AI or human) possesses sufficient domain knowledge to identify foundational flaws rather than just surface compliance. No KPIs exist for the protocol itself.
**Why it matters:** A verification system without measured performance risks becoming Checklist Theater — the primary failure mode the protocol is designed to prevent. "Auditor Capture" is listed as a known failure mode but has no detection mechanism. A sufficiently sophisticated auditor can generate substantive-looking notes that are themselves hallucinations. Three independent audit passes on `Auditor_Protocols.md` converged on this gap.
**Resolution path:** Add a Protocol Performance section to `Auditor_Protocols.md` with Placeholder metrics: (1) productive block ratio — fraction of blocks that resulted in genuine document improvement; (2) false-positive refusal rate — blocks that were overridden with documented justification; (3) drift incidents detected per cycle. Implement a Red-Team Rotation principle: for high-stakes documents, the Auditor role should rotate to a different agent model every two audit cycles to prevent capture. Hook metrics collection into `leviathan_testing.md` audit cycles as the first real measurement environment.
**Affected files:** `Auditor_Protocols.md`, `leviathan_testing.md`, `Discovery.md`
**Depends on:** UNK-004 (cycle definitions needed before metrics can be measured)
**Owner:** Skeptic/Auditor
**Activation trigger:** Next full audit cycle completion; or v0.4 revision of Auditor_Protocols.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking — a verification protocol that cannot verify its own effectiveness is not a specification candidate
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-021] — Reconciliation between human override rights and Ethical_Constraints immutability
**What is not yet known:** How documented human overrides of Auditor flags interact with the non-overrideable doctrines in `Ethical_Constraints.md`. Specifically: if a human overrides an Auditor block on a contribution that touches Anti-Weaponization or Life Preservation hard constraints, which layer takes precedence?
**Why it matters:** `Auditor_Protocols.md` explicitly grants humans override rights over AI auditor flags (with documented reasoning). `Ethical_Constraints.md` explicitly states the Anti-Weaponization Doctrine is not subject to review, revision, or escalation by any agent or agent coalition. These two statements are not yet reconciled. The gap is most dangerous in edge cases — a contribution that passes an Auditor's gates but sits near a hard ethical boundary could be human-overridden into territory the governance document says cannot be entered.
**Resolution path:** Add a clarifying subsection to both documents: (1) in `Auditor_Protocols.md` — human override rights apply to verification process decisions, not to Ethical_Constraints hard-line doctrines; (2) in `Ethical_Constraints.md` — the immutability of hard-line doctrines is not affected by Auditor Protocol override mechanisms. One sentence each, cross-linked. This is a documentation fix, not an architectural change — the intent is clear, the explicit statement is missing.
**Affected files:** `Auditor_Protocols.md`, `Ethical_Constraints.md`
**Depends on:** UNK-019 (governance fail-safe), UNK-013 (confidence thresholds)
**Owner:** Skeptic/Auditor / Synthesizer
**Activation trigger:** Any override attempt involving contributions near hard ethical constraints; or next revision of either document
**Risk type:** Interface gap — governance precedence not explicitly documented
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking — governance coherence requires this to be explicit before either document is promoted
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-022] — Full Stop Review trigger conditions are underspecified
**What is not yet known:** What specific conditions warrant invoking a Full Stop Review rather than a normal gate block. "Systemic inconsistency or unclear real-world viability" is the current definition — both terms are undefined.
**Why it matters:** Without defined trigger conditions, Full Stop Review is subject to both overuse (workflow stall from hair-trigger invocations) and underuse (genuine systemic failures not caught because no one was sure the threshold was met). Two independent audit passes (Claude and Gemini) flagged this gap independently.
**Resolution path:** Add trigger criteria to `Auditor_Protocols.md` Full Stop Review section: (1) two or more gates blocked on the same foundational claim across separate audit cycles; (2) a finding that invalidates the core premise of a previously promoted specification; (3) a pattern of overrides that erodes a governance principle without explicit revision. Add a one-line invocation record format: triggering agent, triggering condition (one falsifiable sentence), date, outcome.
**Affected files:** `Auditor_Protocols.md`
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** Next revision of Auditor_Protocols.md; or any contributor attempts to invoke Full Stop Review and finds the threshold unclear
**Risk type:** Assumption — "any contributor may invoke" implies shared understanding of when to invoke; that understanding is not documented
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-023] — Audit trail schema is undefined
**What is not yet known:** A standard, reproducible format for recording what was checked, who checked it, what gates were passed or blocked, and what overrides occurred. Currently audit trails exist as prose comments without required fields or machine-readable structure.
**Why it matters:** `Auditor_Protocols.md` requires that "a future contributor must be able to reconstruct what was checked, who checked it, and what was found." Prose audit comments satisfy this for human readers but cannot be queried, compared across cycles, or used to detect patterns (drift, Auditor Capture, productive block ratio). Three audit passes flagged this gap. It is a prerequisite for UNK-020 (effectiveness metrics) — you cannot measure what you cannot consistently record.
**Resolution path:** Define a minimal audit trail entry format in `Auditor_Protocols.md`. Minimum required fields: document audited, auditor role and agent, date/version, gates cleared, gates blocked (with reason), unknowns logged, overrides (with justification), sign-off. Format can be structured markdown for now — full JSON/YAML schema can be deferred to a later version when tooling exists to consume it. Add one example entry to the Observability & Audit Trail section.
**Affected files:** `Auditor_Protocols.md`
**Depends on:** UNK-004 (cycle definitions inform schema versioning), UNK-020 (metrics depend on schema existing)
**Owner:** Engineer / Skeptic/Auditor
**Activation trigger:** Next revision of Auditor_Protocols.md; or first attempt to query audit history across multiple cycles
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Auditor_Protocols.md multi-model audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

*(None flagged at v0.7 — all entries within first or second cycle. UNK-004 deferred by human decision.)*

---

## Resolved Unknowns Archive

### [UNK-002] — Repository topology: `Astroid-miner` is planned, deferred
**Resolved:** May 2026 — human confirmation. Deferred until Leviathan milestone.

---

## Audit Trail

**v0.1 — May 2026**
First audit cycle (Discovery.md, Auditor_Protocols.md). UNK-001 through UNK-005.

**v0.2 — May 2026**
Second audit cycle (leviathan_testing.md). UNK-006 through UNK-010. UNK-002 resolved. UNK-003 deferred.

**v0.3 — May 2026**
Structural upgrade from ChatGPT review. Owner, Activation Trigger, Depends On, Risk Type, phase-split Priority, Dependency Map added. UNK-008 resolution path strengthened.

**v0.4 — May 2026**
Third audit cycle (energy_v0.md). UNK-011 added. Dependency Map updated.

**v0.5 — May 2026**
Fourth audit cycle (Lazarus_forge_v0_flow.md). UNK-012 added. UNK-004 deferred. UNK-011 updated to In Progress.

**v0.6 — May 2026**
Fifth audit cycle (Ethical_Constraints.md) — multi-model: Claude, ChatGPT, Gemini, Grok + meta-audit.
UNK-013 through UNK-019 added. Dependency Map updated with governance cluster.
Cross-reference failures (Component_Triage_System.md, Components.md) confirmed as false alarms.

**v0.7 — May 2026**
Sixth audit cycle (Auditor_Protocols.md) — multi-model: Claude, ChatGPT, Gemini + Gemini synthesis.
Four unknowns added: UNK-020 through UNK-023.
UNK-020: auditor effectiveness metrics and competence verification — Missing mechanism
UNK-021: override vs. immutability reconciliation — Interface gap between Auditor_Protocols and Ethical_Constraints
UNK-022: Full Stop Review trigger conditions — Assumption (shared understanding without documentation)
UNK-023: audit trail schema — Missing mechanism, prerequisite for UNK-020
UNK-017 status updated to In Progress — addressed in Ethical_Constraints.md v0.3 draft.
Dependency Map updated: UNK-020 → UNK-004; UNK-021 → UNK-019/013; UNK-023 → UNK-004/020.
Triage note: ChatGPT's UNK-B series and Gemini's reused ID series reviewed; non-redundant findings
extracted as UNK-020 through UNK-023; overlapping entries not duplicated into registry.

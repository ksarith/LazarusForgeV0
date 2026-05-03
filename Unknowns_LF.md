# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.6 — UNK-013 through UNK-019 added from Ethical_Constraints.md multi-model audit cycle (Claude, ChatGPT, Gemini, Grok).**

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
  └── UNK-014 (dual-use/weaponization pattern detection routes here)

UNK-013 (confidence threshold definition)
  └── UNK-008 (autonomy architecture must implement it)

UNK-019 (governance fail-safe)
  └── UNK-013 (can't define fail-safe for undefined mechanism)
  └── UNK-016 (governance failure modes feed into fail-safe design)

UNK-002 (repo topology) [RESOLVED]
  └── UNK-003 (assumption contracts) [DEFERRED]

UNK-004 (Expiry Rule) [DEFERRED — activates post-audit-cycle completion]
```

---

## Registry

---

### [UNK-001] — Discovery.md update pending for Unknowns_LF.md entry
**What is not yet known:** Whether `Discovery.md` has been updated to include `Unknowns_LF.md` in the reading order, file summaries, and with a raw GitHub URL.
**Why it matters:** `Discovery.md` is the navigation layer. A file absent from it is effectively invisible to returning AI agents and new contributors.
**Resolution path:** Confirm Discovery.md update has been committed with reading order entry, file summary, and raw GitHub URL. Close on confirmation.
**Affected files:** `Discovery.md`, this file
**Depends on:** None
**Owner:** Connective Tissue
**Activation trigger:** Next commit to Discovery.md, or next audit cycle — whichever comes first
**Risk type:** Interface gap
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open — Discovery.md update pending confirmation

---

### [UNK-003] — Cross-repo assumption contracts not yet documented
**What is not yet known:** Whether bidirectional assumption contracts exist between LazarusForgeV0 and its companion repositories.
**Why it matters:** Shared module assumptions exist as claims in one repo with no acknowledged counterpart in the other.
**Resolution path:** When Astroid-miner is activated, create stub `Assumption_Contracts.md` in both repositories.
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
**Why it matters:** Registry infrastructure. Deferred because registry is in active development — forcing enforcement now is premature.
**Resolution path:** Add to `Auditor_Protocols.md`: version cycle definition, "logged in version" as required field, Expiry check assigned to Skeptic/Auditor at each audit cycle opening.
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
**Resolution path:** Survey deep-sea AUV analog systems for bounding estimates. Add stub Power Budget section to `leviathan_testing.md`. Requires UNK-011 stub to exist first.
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
**Why it matters:** "Predictable degradation" is asserted without acknowledging well-documented pressure and thermal failure modes.
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
**What is not yet known:** Decay function, false-positive definition, trust floor, and initialization state for the peer trust scoring system.
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
**What is not yet known:** How Tier 1 (critical failure) data reaches out-of-contact units faster than Tier 3 data in an opportunistic, delay-tolerant network.
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
**Why it matters:** Without a demand side, UNK-006 cannot be scoped. This is the load-bearing gap in the entire energy chain.
**Resolution path:** Power Demand stub added to `energy_v0.md` (May 2026) with Placeholder figures from analog systems. Next step: replace Placeholders as hardware selection proceeds.
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
**What is not yet known:** Whether gate logic (A→B→C→D) produces deterministic routing for all item types, or whether ambiguous boundary cases require human judgment more frequently than implied.
**Why it matters:** The flow document is the terminology reference standard. Ambiguity in gate logic propagates silently into every implementing document.
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
**What is not yet known:** What confidence level triggers the default-to-non-action rule in the Core Mandate. Whether "sufficient confidence," "confidently classified," and "reasonably bounded" represent the same threshold or a graduated scale.
**Why it matters:** These are operational triggers in the parent governance document. Undefined thresholds are not implementable. Different agents may interpret them differently, producing inconsistent refusal behavior. Affects every downstream implementation of classification or refusal logic.
**Resolution path:** Add a Confidence Thresholds section to `Ethical_Constraints.md`: (1) working definition of sufficient confidence; (2) whether the three phrasings represent one standard or graduated scale; (3) how confidence is assessed (probabilistic model, checklist, human judgment). Full mechanism design may route to `Trajectories_LF.md` with a Placeholder anchor here.
**Affected files:** `Ethical_Constraints.md`, any autonomy or classification implementation
**Depends on:** UNK-008 (autonomy architecture must implement whatever threshold is defined)
**Owner:** Skeptic/Auditor / Engineer
**Activation trigger:** Any implementation of classification or refusal logic referencing this document; or v0.3 revision of Ethical_Constraints.md
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-014] — Anti-Weaponization pattern-matching mechanism is undefined
**What is not yet known:** What constitutes a "pattern match" to weapons development, military application, or coercive use. The pattern space, matching method, false-positive handling, and edge case escalation path are all absent.
**Why it matters:** The hardest constraint in the entire repository — the one explicitly not subject to override — depends entirely on a detection mechanism that has not been specified. An undefined detector is not a hard line; it is a stated intention. Without it, the Anti-Weaponization Doctrine cannot be implemented, only aspired to.
**Resolution path:** Add a Pattern Recognition Annex to `Ethical_Constraints.md` or a dedicated classification spec: (1) example pattern categories; (2) detection method (keyword, capability assessment, contextual reasoning); (3) false-positive handling protocol; (4) edge case escalation path. Route full implementation to `Component_Triage_System.md` with a stub anchor in Ethical_Constraints.md. Note: the "plasma cutter paradox" (a tool that is industrial in one configuration and a weapon component in another based solely on output parameters) is a concrete test case that should drive pattern definition work.
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
**What is not yet known:** How escalation to human review is performed — channel, recipient, expected response time, system behavior during hold, and timeout behavior if no response is received.
**Why it matters:** "Escalate to human review" appears throughout the parent governance document as the resolution for legal ambiguity, cultural site uncertainty, and ethical edge cases. In a Leviathan deployment with intermittent connectivity, an undefined escalation path means the document's primary safety valve may not function at all. The phrase appears seven or more times without ever being defined.
**Resolution path:** Add an Escalation Protocol section to `Ethical_Constraints.md`: (1) escalation channel; (2) recipient designation; (3) system behavior during escalation hold (default to observation/non-action); (4) timeout behavior if no human response received; (5) logging requirements. Route communications layer detail to `leviathan_testing.md`.
**Affected files:** `Ethical_Constraints.md`, `leviathan_testing.md`
**Depends on:** UNK-006 (Leviathan power envelope affects communication availability), UNK-008 (autonomy architecture governs hold behavior)
**Owner:** Autonomy / Engineer
**Activation trigger:** Leviathan hardware design begins; or any test scenario requires human escalation
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-016] — Governance layer failure modes are unspecified
**What is not yet known:** How the ethics substrate can fail, how failure would be detected, and what fallback behavior applies if the governance layer is compromised, unavailable, or producing false negatives.
**Why it matters:** A governance document that describes only its operation under normal conditions fails the same Lifecycle Truncation standard applied to module specs (Fallacy #8). If the ethics layer silently fails — logging unavailable, classification producing false negatives, communication blackout — no other system component knows to compensate.
**Resolution path:** Add a Governance Failure Modes section to `Ethical_Constraints.md`: (1) known failure signatures; (2) detection mechanism; (3) fallback posture — note that the Pacifist Operating Posture's default-to-observation behavior may already function as the fallback; if so, make this explicit; (4) logging behavior if logging itself is unavailable.
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
**What is not yet known:** Whether an acute human life preservation claim can override the Anti-Weaponization Doctrine. This is the most predictable pressure vector against the hard line.
**Why it matters:** The document explicitly states that legal permission and economic pressure cannot override the doctrine. It is silent on humanitarian emergency framing. This is not a hypothetical edge case — "we need this capability to protect lives" is the historical justification for most weapons development. The document cites Nobel and Oppenheimer; both cases involved exactly this framing. Silence implies "no exception" — but that should be stated, not assumed, because the assumption will be tested.
**Resolution path:** Add an explicit clause to the Anti-Weaponization Doctrine: either (1) humanitarian framing does not override the doctrine, with reasoning; or (2) a narrowly defined humanitarian exception with strict scope limits and mandatory human review. Either answer is acceptable. Silence is not. This is a human governing party decision, not an engineering one.
**Affected files:** `Ethical_Constraints.md`
**Depends on:** None
**Owner:** Skeptic/Auditor / human governing party
**Activation trigger:** v0.3 revision of Ethical_Constraints.md
**Risk type:** Assumption — silence implies "no exception" but this must be stated explicitly
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

### [UNK-018] — Ethical log survival under unit loss or communication blackout
**What is not yet known:** How refusal logs and ethical decision records survive unit loss, hardware failure, or extended communication blackout in deep-ocean or remote deployments.
**Why it matters:** `Ethical_Constraints.md` requires that refusal decisions be logged. `Auditor_Protocols.md` requires that audit trails be documentable. In a Leviathan deployment, a unit that makes a refusal decision and then fails may take that record with it. The governance requirement exists; the survival mechanism does not.
**Resolution path:** Add a Log Survival section to `Ethical_Constraints.md` or `leviathan_testing.md`: (1) minimum logging requirements for refusal decisions; (2) local storage requirements; (3) transmission protocol for logs during periodic sync; (4) behavior if unit is lost before sync occurs — define acceptable data loss threshold. Route implementation detail to delay-tolerant networking section of `leviathan_testing.md`.
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
**What is not yet known:** What the system does if the ethics substrate itself fails or begins producing systematic false negatives — allowing prohibited actions to pass undetected.
**Why it matters:** UNK-016 covers how failure would be detected. UNK-019 covers what happens after detection (or in the absence of detection). A governance system with no defined fail-safe posture defaults to whatever the underlying system does — which may not be safe. The Pacifist Operating Posture may already implicitly define this (default to observation), but this has not been made explicit.
**Resolution path:** Define explicit fail-safe behavior in `Ethical_Constraints.md`: (1) if ethics substrate failure is detected, system halts all non-observational action; (2) if failure cannot be confirmed but anomalous patterns are present, system escalates to human review (per UNK-015 once defined); (3) fail-safe state is logged. Verify whether Pacifist Operating Posture already covers this — if yes, add a cross-reference; if no, add the clause.
**Affected files:** `Ethical_Constraints.md`
**Depends on:** UNK-013 (can't define fail-safe for an undefined confidence mechanism), UNK-016 (failure modes must be defined before fail-safe can be triggered)
**Owner:** Skeptic/Auditor
**Activation trigger:** v0.3 revision of Ethical_Constraints.md; or UNK-016 resolution begins
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** Ethical_Constraints.md multi-model audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

*(None flagged at v0.6 — all entries within first or second cycle. UNK-004 deferred by human decision.)*

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
Fifth audit cycle (Ethical_Constraints.md) — multi-model pass: Claude, ChatGPT, Gemini, Grok + Gemini compilation + Claude meta-audit of compilation.
Seven unknowns added: UNK-013 through UNK-019.
UNK-013: confidence threshold definition — Missing mechanism, parent governance document
UNK-014: Anti-Weaponization pattern detection — Missing mechanism, hardest constraint in repo
UNK-015: human escalation path — Missing mechanism, repeated seven times without definition
UNK-016: governance failure modes — Missing mechanism, Lifecycle Truncation gap
UNK-017: life-preservation vs. Anti-Weaponization priority — Assumption, primary pressure vector
UNK-018: ethical log survival under unit loss — Missing mechanism, Leviathan-specific
UNK-019: governance fail-safe behavior — Missing mechanism, depends on UNK-013 and UNK-016
Dependency Map updated with governance cluster (UNK-013 → UNK-008, UNK-019 → UNK-013/016, UNK-015 → UNK-006/008).
Cross-reference failures from audit (Component_Triage_System.md, Components.md) confirmed as false alarms — both files exist per Discovery.md.
Gate 6 contradiction (refusal revision loop vs. Anti-Weaponization carve-out) noted as resolvable with one clarifying sentence — not logged as unknown, flagged for v0.3 revision of Ethical_Constraints.md.

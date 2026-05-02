# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.4 — UNK-011 added from energy_v0.md audit cycle.**

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

UNK-007 (storage degradation at depth)
  └── feeds into UNK-006 (parallel, not sequential)

UNK-005 (marine GECK seed)
  └── depends on UNK-006

UNK-002 (repo topology) [RESOLVED]
  └── UNK-003 (assumption contracts) [DEFERRED]

UNK-004 (Expiry Rule) — infrastructure; no dependencies, everything depends on it
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
**Why it matters:** Shared module assumptions (Air Scrubber marine variant, Spin Chamber zero-G, GECK bootstrap logic) exist as claims in one repo with no acknowledged counterpart in the other.
**Resolution path:** When Leviathan milestone is reached and Astroid-miner is activated, create stub `Assumption_Contracts.md` in both repositories using format from `Auditor_Protocols.md` §Cross-Repo Verification.
**Affected files:** `Auditor_Protocols.md`, `geck_forge_seed.md`, `Air_Scrubber_v0.md`, `Spin_Chamber_v0.md`
**Depends on:** UNK-002 (resolved)
**Owner:** Skeptic/Auditor
**Activation trigger:** Leviathan deployment milestone reached; Astroid-miner repository activated
**Risk type:** Interface gap
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — activates at Leviathan milestone

---

### [UNK-004] — Expiry Rule has no enforcement mechanism
**What is not yet known:** What constitutes a "version cycle" for the Expiry Rule. `Auditor_Protocols.md` defines the rule but does not define version cycle, does not require timestamps on entries, and does not assign responsibility for triggering escalation checks.
**Why it matters:** Registry infrastructure. Without enforcement, unknowns accumulate without conversion into action. Silent failure degrades entire system rigor.
**Resolution path:** Add to `Auditor_Protocols.md`: (1) version cycle definition; (2) "logged in version" as required entry field; (3) Expiry check assigned to Skeptic/Auditor at opening of each audit cycle.
**Affected files:** `Auditor_Protocols.md`, this file
**Depends on:** None
**Owner:** Skeptic/Auditor
**Activation trigger:** Next revision of `Auditor_Protocols.md` — must be included
**Risk type:** Missing mechanism
**Priority (Exploration):** Blocking — registry infrastructure
**Priority (Promotion):** Blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

### [UNK-005] — Marine G.E.C.K. seed variant not yet defined
**What is not yet known:** Minimum viable seed configuration for instantiating a Support Raft or marine Forge deployment from minimal resources.
**Why it matters:** Terrestrial G.E.C.K. modules do not map cleanly to marine deployment. Without a marine variant, Leviathan and Support Raft deployments have no defined seed.
**Resolution path:** Add a marine variant stub to `geck_forge_seed.md`. Full spec routes to `Trajectories_LF.md` as a v1/v2 milestone.
**Affected files:** `geck_forge_seed.md`, `Support_Raft_v0.md`, `leviathan_testing.md`
**Depends on:** UNK-006 (power envelope informs minimum seed power requirements)
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
**Why it matters:** Autonomy claims, endurance claims, and load-shedding behavior cannot be tested without a power substrate. UNK-008 cannot be scoped without this. Note: UNK-011 (terrestrial Forge demand baseline) is a prerequisite — Leviathan envelope cannot be scoped until the terrestrial demand side exists as a reference point.
**Resolution path:** Survey deep-sea AUV analog systems (Remus, Seaglider, Nereid Under-Ice) for bounding estimates. Label as Analogous or Placeholder. Add stub Power Budget section to `leviathan_testing.md`, cross-referenced to `energy_v0.md`. Requires UNK-011 stub to exist first.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Depends on:** UNK-011 (Forge demand baseline must exist before Leviathan envelope can be scoped)
**Owner:** Energy
**Activation trigger:** Any attempt to define Leviathan test scenarios; or any hardware component selection
**Risk type:** Unknown
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open — depends on UNK-011

---

### [UNK-007] — Deep-ocean storage degradation under pressure and low temperature is unacknowledged
**What is not yet known:** How sealed cell storage behaves at Leviathan operating depths and temperatures (2–4°C) over extended mission durations.
**Why it matters:** `leviathan_testing.md` asserts "predictable degradation" as a power system requirement. `energy_v0.md` notes salvaged batteries as preferred storage without acknowledging state-of-health uncertainty. Pressure and thermal effects are well-documented failure modes not yet engaged by either document.
**Resolution path:** Literature review of battery performance at depth and temperature (MBARI, WHOI data). Results feed into `energy_v0.md` storage section. Run in parallel with UNK-011, not sequentially after.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Depends on:** None (parallel with UNK-011)
**Owner:** Energy
**Activation trigger:** Any attempt to select or specify energy storage hardware; or UNK-011 power demand work begins
**Risk type:** Assumption — "predictable degradation" stated as requirement, not verified as achievable
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-008] — Leviathan autonomy architecture is unspecified — testability gap
**What is not yet known:** What decision-making paradigm(s) are under test. None are named in `leviathan_testing.md`.
**Why it matters:** Falsification requires a stated hypothesis. Without naming what architecture is under test, the framework risks becoming a scenario generator rather than a hypothesis-testing system.
**Resolution path:** Add a candidate architecture section to `leviathan_testing.md` with three required elements per candidate: (1) observable decision loop; (2) failure signature; (3) minimal test scenario. Minimum viable: two candidates, all three elements each.
**Affected files:** `leviathan_testing.md`, `Trajectories_LF.md`
**Depends on:** UNK-006 (power envelope constrains which architectures are feasible)
**Owner:** Autonomy / Skeptic/Auditor
**Activation trigger:** Any attempt to define Leviathan test scenarios; or any autonomy-related hardware or software selection
**Risk type:** Missing mechanism
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-009] — Trust model mechanism in Extension B is undefined
**What is not yet known:** Decay function, false-positive definition, trust floor, and initialization state for the peer trust scoring system in Extension B.
**Why it matters:** Anti-pattern safeguards depend on trust diversity. The behavioral description implies a mechanism without specifying one.
**Resolution path:** Label trust model as Placeholder in `leviathan_testing.md` Extension B. Full mechanism design routes to `Trajectories_LF.md`.
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
**What is not yet known:** How Tier 1 (critical failure) data reaches out-of-contact units faster than Tier 3 (optimization) data in an opportunistic, delay-tolerant network.
**Why it matters:** "Errors travel faster than optimizations" is stated as a design principle without a mechanism that enforces it in a disconnected network.
**Resolution path:** Acknowledge as open design question in Extensions. Designate as primary test target for multi-unit deployments. Full mechanism routes to `Trajectories_LF.md`.
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
**What is not yet known:** What the terrestrial Lazarus Forge actually consumes at bootstrap, nominal, and degraded operating modes — even at order-of-magnitude resolution.
**Why it matters:** `energy_v0.md` describes five supply sources without any demand side to calibrate against. The primary metric (kWh per kg of recovered usable output) cannot be calculated or falsified without a demand anchor. More critically, UNK-006 (Leviathan power envelope) cannot be scoped until a terrestrial demand baseline exists as a reference point. This is the load-bearing gap in the entire energy chain.
**Resolution path:** Add a stub Power Demand section to `energy_v0.md` with three operating modes: bootstrap (minimum to sustain triage and control), nominal (full triage + partial processing), and degraded (triage only, processing suspended). Source placeholder values from terrestrial analog systems — industrial shredder and sorting line data is publicly available and appropriate for order-of-magnitude anchoring. Label all figures as Placeholder or Analogous. Accuracy is not required at v0 — the integration point must exist.
**Affected files:** `energy_v0.md`, `leviathan_testing.md`, `Lazarus_forge_v0_flow.md`
**Depends on:** None
**Owner:** Energy
**Activation trigger:** Any attempt to scope UNK-006; or any hardware selection for processing modules; or energy_v0.md promotion begins
**Risk type:** Missing mechanism — supply side exists without a demand side to anchor against
**Priority (Exploration):** Non-blocking
**Priority (Promotion):** Blocking
**Logged in version:** energy_v0.md audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

The following unknowns are approaching or past two version cycles without a documented resolution path. Review at next audit cycle.

*(None flagged at v0.4 — all entries are within their first or second cycle.)*

---

## Resolved Unknowns Archive

### [UNK-002] — Repository topology: `Astroid-miner` is planned, deferred
**Resolved:** May 2026 — human confirmation. `Astroid-miner` is a separate planned repository, deferred until Leviathan milestone. Cross-repo verification scoped to `Lazarus-Forge-` only until activation.

---

## Audit Trail

**v0.1 — May 2026**
Created from findings of first formal Skeptic/Auditor cycle over `Discovery.md` and `Auditor_Protocols.md`.
Auditor: Claude (Sonnet 4.6). Five unknowns logged: UNK-001 through UNK-005.

**v0.2 — May 2026**
Updated from second formal Skeptic/Auditor cycle over `leviathan_testing.md`.
Auditor: Claude (Sonnet 4.6). Five unknowns added: UNK-006 through UNK-010.
UNK-002 resolved. UNK-003 deferred.

**v0.3 — May 2026**
Structural upgrade from ChatGPT review, triaged and applied by Claude (Sonnet 4.6).
Added Owner, Activation Trigger, Depends On, Risk Type, phase-split Priority, Dependency Map.
UNK-004 reclassified Blocking (Exploration). UNK-008 resolution path strengthened.

**v0.4 — May 2026**
Updated from third formal Skeptic/Auditor cycle over `energy_v0.md`.
Auditor: Claude (Sonnet 4.6). One unknown added: UNK-011 (Forge power demand baseline).
Dependency Map updated: UNK-011 now sits upstream of UNK-006, making it the earliest
load-bearing gap in the Leviathan power chain. UNK-006 dependency updated accordingly.

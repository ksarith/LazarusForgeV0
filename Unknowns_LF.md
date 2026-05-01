# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.2 — updated from second formal audit cycle (leviathan_testing.md).**

---

## Purpose

This file captures unresolved questions, gaps, and dependencies that cannot be owned by a single module file. Module-specific unknowns live within their own documents. Unknowns that affect multiple modules, cross-repo dependencies, or the navigation layer itself live here.

Uncertainty is a first-class output. This file is not a junk drawer — it is a tracked frontier.

Format per `Auditor_Protocols.md` Unknowns Registry section.

---

## Entry Format

```
### [ID] — Short title
**What is not yet known:**
**Why it matters:**
**Resolution path:**
**Affected files:**
**Priority:** Blocking | Non-blocking | Exploratory
**Logged in version:** (document version or audit cycle identifier)
**Status:** Open | In Progress | Resolved
```

---

## Registry

---

### [UNK-001] — `Unknowns_LF.md` absence created governance gap
**What is not yet known:** N/A — this file now exists. Logging for audit trail completeness.
**Why it matters:** `Auditor_Protocols.md` references this file as the canonical location for cross-module unknowns. `Discovery.md` also routes cross-file unknowns here. While the file was absent, there was no functioning central registry and no location for unknowns surfaced during multi-agent audit cycles.
**Resolution path:** File created (this document). Add to Discovery.md reading order and file summaries. Add raw GitHub URL to Discovery.md entry.
**Affected files:** `Auditor_Protocols.md`, `Discovery.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** In Progress — file created, Discovery.md update pending

---

### [UNK-002] — Repository topology clarified: `Astroid-miner` is a planned, deferred repo
**What is not yet known:** N/A — resolved by human clarification.
**Why it matters:** `Auditor_Protocols.md` referenced `Astroid-miner` as a cross-repo dependency. `Discovery.md` named `Lazarus-Forge-` as the companion repo. These appeared to conflict.
**Resolution path:** Confirmed: `Astroid-miner` is a separate planned repository, intentionally deferred until Leviathan deployment is underway. Merge/migration trigger defined: Leviathan in focus or active. All `Astroid-miner` references in `Auditor_Protocols.md` should be labeled `(planned — activates at Leviathan milestone)`. Cross-repo verification requirements currently scoped to `Lazarus-Forge-` only.
**Affected files:** `Discovery.md`, `Auditor_Protocols.md`, `geck_forge_seed.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Resolved — awaiting label updates in Auditor_Protocols.md

---

### [UNK-003] — Cross-repo assumption contracts not yet documented
**What is not yet known:** Whether bidirectional assumption contracts exist in any form between LazarusForgeV0 and its companion repositories.
**Why it matters:** Shared module assumptions (Air Scrubber marine variant, Spin Chamber zero-G, GECK bootstrap logic) currently exist as claims in one repo with no acknowledged counterpart in the other. Changes to shared modules cannot be safely verified without bidirectional documentation.
**Resolution path:** Deferred — blocked on Astroid-miner activation (see UNK-002). When Leviathan milestone is reached and Astroid-miner is activated, create stub `Assumption_Contracts.md` in both repositories using format defined in `Auditor_Protocols.md` §Cross-Repo Verification.
**Affected files:** `Auditor_Protocols.md`, `geck_forge_seed.md`, `Air_Scrubber_v0.md`, `Spin_Chamber_v0.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Deferred — activates at Leviathan milestone per UNK-002 resolution

---

### [UNK-004] — Expiry Rule has no enforcement mechanism
**What is not yet known:** What constitutes a "version cycle" for purposes of the Expiry Rule. `Auditor_Protocols.md` defines the rule but does not define what a version cycle is, does not require a timestamp on unknown entries, and does not assign responsibility for triggering the escalation check.
**Why it matters:** Without a definition and an assigned enforcer, the Expiry Rule is aspirational. Unknowns can age indefinitely without triggering escalation.
**Resolution path:** Add to `Auditor_Protocols.md`: (1) definition of version cycle — recommended: any commit that increments a module version number, or any completed multi-agent audit cycle; (2) "logged in version" as a required field; (3) assignment of Expiry check to the Skeptic/Auditor role at the opening of each audit cycle.
**Affected files:** `Auditor_Protocols.md`, this file
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

### [UNK-005] — Marine G.E.C.K. seed variant not yet defined
**What is not yet known:** The minimum viable seed configuration for instantiating a Support Raft or marine Forge deployment from minimal resources. `Support_Raft_v0.md` routes this to `geck_forge_seed.md`, which does not yet acknowledge it.
**Why it matters:** The terrestrial G.E.C.K. modules do not map cleanly to a marine deployment context. Without a marine variant, Leviathan and Support Raft deployments have no defined seed — they can grow but cannot be instantiated from scratch.
**Resolution path:** Add a marine variant stub to `geck_forge_seed.md` drawing from `Support_Raft_v0.md` Unknowns Registry. Full spec routes to `Trajectories_LF.md` as a v1/v2 milestone.
**Affected files:** `geck_forge_seed.md`, `Support_Raft_v0.md`, `leviathan_testing.md`
**Priority:** Exploratory
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

### [UNK-006] — Power envelope for Leviathan has no placeholder anchor
**What is not yet known:** Order-of-magnitude power budget for a Leviathan unit under nominal, degraded, and dormancy conditions.
**Why it matters:** Autonomy claims, endurance claims, and load-shedding behavior cannot be tested without a power substrate. "Limited, finite, and degradable" is a design stance, not a testable parameter. Blocks promotion to specification.
**Resolution path:** Survey deep-sea AUV analog systems (Remus, Seaglider, Nereid Under-Ice) for bounding estimates. Label resulting figures as Analogous or Placeholder. Add as a stub section to `leviathan_testing.md` Power and Endurance, cross-referenced to `energy_v0.md`.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Priority:** Non-blocking (exploration); Blocking at promotion to specification
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-007] — Deep-ocean storage degradation under pressure and low temperature is unacknowledged
**What is not yet known:** How sealed cell storage behaves at Leviathan operating depths (nominally 200–6000m, unspecified) and temperatures (2–4°C) over extended mission durations.
**Why it matters:** `leviathan_testing.md` asserts "predictable degradation" as a power system requirement while omitting well-documented pressure and thermal failure modes for lithium-based storage. This is a Friction Blindness flag.
**Resolution path:** Literature review of battery performance at depth and temperature using existing AUV fleet data (publicly available from MBARI, WHOI). Results feed into `energy_v0.md` and inform the power budget stub in UNK-006.
**Affected files:** `leviathan_testing.md`, `energy_v0.md`
**Priority:** Non-blocking (exploration); Blocking at promotion to specification
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-008] — Leviathan autonomy architecture is unspecified — testability gap
**What is not yet known:** What decision-making paradigm(s) are under test. Candidate classes include reactive, deliberative, hybrid, and learned policy approaches. None are named in `leviathan_testing.md`.
**Why it matters:** The core purpose of Leviathan is to falsify autonomy assumptions. Falsification requires a stated hypothesis. Without naming what architecture is under test, the framework can confirm that autonomous behavior is hard — but cannot falsify specific assumptions about which approaches fail and why. This is the most significant promotion blocker identified in this audit cycle.
**Resolution path:** Add a candidate architecture list to `leviathan_testing.md` framed explicitly as hypotheses under evaluation, not commitments. Minimum viable: name 2–3 approaches being considered and what failure condition would eliminate each.
**Affected files:** `leviathan_testing.md`, `Trajectories_LF.md`
**Priority:** Non-blocking (exploration); Blocking at promotion to specification
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-009] — Trust model mechanism in Extension B is undefined
**What is not yet known:** Decay function, false-positive definition, trust floor, and initialization state for the peer trust scoring system described in Extension B.
**Why it matters:** Anti-pattern safeguards (echo chamber prevention, runaway convergence resistance) depend on trust diversity being maintained. The behavioral description implies a mechanism without specifying one — safeguards are hypothesized, not demonstrated.
**Resolution path:** Label trust model as Placeholder in `leviathan_testing.md`. Full trust model design is trajectory-scope — route to `Trajectories_LF.md`.
**Affected files:** `leviathan_testing.md` (Extensions)
**Priority:** Exploratory
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

### [UNK-010] — Priority propagation in disconnected network has no enforcement mechanism
**What is not yet known:** How Tier 1 (critical failure) data reaches out-of-contact units faster than Tier 3 (optimization) data in an opportunistic, delay-tolerant network with no guaranteed connectivity.
**Why it matters:** "Errors travel faster than optimizations" is stated as a Core Networking Principle. In a disconnected opportunistic-sync network, this priority ordering is not guaranteed by the architecture as described — it is an intention without a mechanism.
**Resolution path:** Acknowledge as open design question in `leviathan_testing.md` Extensions. Designate priority propagation as a primary test target for multi-unit deployments.
**Affected files:** `leviathan_testing.md` (Extensions)
**Priority:** Exploratory
**Logged in version:** leviathan_testing.md audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

The following unknowns are approaching or past two version cycles without a documented resolution path. Review at next audit cycle.

*(None flagged at v0.2 — all entries are within their first cycle.)*

---

## Resolved Unknowns Archive

### [UNK-002] — Repository topology: `Astroid-miner` is planned, deferred
**Resolved:** May 2026 — human confirmation. `Astroid-miner` is a separate planned repository, deferred until Leviathan milestone. Cross-repo verification scoped to `Lazarus-Forge-` until activation. Label updates to `Auditor_Protocols.md` pending.

---

## Audit Trail

**v0.1 — May 2026**
Created from findings of first formal Skeptic/Auditor cycle over `Discovery.md` and `Auditor_Protocols.md`.
Auditor: Claude (Sonnet 4.6), Skeptic/Auditor role per `Auditor_Protocols.md` v0.3.
Five unknowns logged: UNK-001 through UNK-005.
UNK-001 partially resolved by creation of this file.
UNK-003 blocked on UNK-002 resolution.

**v0.2 — May 2026**
Updated from second formal Skeptic/Auditor cycle over `leviathan_testing.md`.
Auditor: Claude (Sonnet 4.6), Skeptic/Auditor role per `Auditor_Protocols.md` v0.3.
Five unknowns added: UNK-006 through UNK-010.
UNK-002 resolved by human clarification — moved to Resolved Archive.
UNK-003 status updated to Deferred pending Leviathan milestone.
UNK-008 flagged as highest-priority open unknown: autonomy architecture testability gap is the primary design work required before Leviathan can promote from Exploration.
Verified under Auditor_Protocols v0.3 — exploration-stage audit, promotion gates not yet applied.

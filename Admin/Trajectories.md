# Lazarus Forge — Trajectory (v0 → Interstellar)

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-23                                                          |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 2                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Version trajectory from v0 through v5
- Survival threshold and exit condition per version
- Forge Regeneration Threshold (FRT) doctrine and floor value
- Revenue allocation framework (operator-defined layer)
- Scope routing destination for out-of-version capabilities
- Design doctrine notes governing version advancement
- Economic model placeholder for v1 profitability baseline

**This file DOES NOT define:**
- Component taxonomy or implementation specs for future versions
  (defined in module documents when versions become active)
- Detailed economic model (→ planned economics_v0.md at v0→v1 transition)
- FRT measurement and logging procedures
  (→ Operations/Gate_07_Utilization.md)
- Component procurement doctrine
  (→ Architecture/Geck_forge_seed.md)
- Formal quality certification standards (→ future v2+ assignment)

---

## File Purpose

This document outlines the evolutionary trajectory of the Lazarus Forge as a
system. Each version represents a capability threshold, not a finished product.
The Forge is treated as a living industrial organism: it begins fragile, gains
resilience, and eventually becomes location-independent.

This is the scope routing destination for the repository. When a capability or
feature is identified as beyond the current version's scope, it routes here.
Version milestones are survival thresholds — not specifications. Component
taxonomy and implementation specs for future versions do not exist in this
document; they are defined in module documents when those versions become active.

Without this file, out-of-scope capabilities accumulate in operational documents,
blurring the boundary between what the Forge can do now and what it is designed
to eventually become.

*Exit conditions are labeled **[Placeholder]** unless operational data or analog
systems provide a basis for a higher confidence label. All exit conditions require
external or proxy validation — see individual notes.*

---

---

## v0 — Proof of Persistence (Terrestrial Seed)

**Question answered:** Can a Forge exist at all?

**Core Characteristics**
- Single-location, Earth-bound
- Human-supervised operation
- Narrow material scope (1–2 metals)
- Energy externally supplied

**Required Capabilities**
- Melt, refine, and form basic metal stock
- Recycle scrap into usable feedstock
- Maintain thermal control without catastrophic failure
- Document processes and outcomes

**Exit Condition** [Placeholder]
> The Forge can repair itself faster than it degrades.

*Verification note: This exit condition cannot be self-reported by the Forge — the detector and the thing being detected are the same system at v0. Verification requires an external observer or proxy metric (e.g., mean time between failures trending downward over N cycles, tracked by human operator). See UNK-026 / CO-001 in Components.md.*

---

## v1 — Self-Sustaining Industrial Node

**Question answered:** Can a Forge stay alive?

**Core Characteristics**
- Modular subsystems
- Semi-autonomous operation
- Expanded alloy handling
- On-site power generation (partial) — see `Operations/Energy.md`; UNK-011 / EV-001 tracks demand baseline

**Required Capabilities**
- Closed-loop material recycling
- Powderization and feedstock standardization
- Component fabrication for adjacent systems
- Environmental control (air, slag, heat)

**Exit Condition** [Placeholder]
> The Forge can operate profitably while reinvesting in itself.

*"Profitably" definition [Placeholder — see TR-001]:* Revenue or barter value generated from external outputs exceeds operating costs while maintaining a reinvestment rate sufficient to sustain v1 capability. Economic model and baseline not yet defined.

---

## v2 — Replicable Forge Network

**Question answered:** Can a Forge reproduce?

**Core Characteristics**
- G.E.C.K.-based seeding — see `Architecture/Geck_forge_seed.md` for G.E.C.K. definition and minimum viable seed. Marine and environmental variants tracked in UNK-005 / GK-003.
- Standardized interfaces
- Distributed documentation and learning
- Minimal expert intervention

**Exit Condition** [Placeholder]
> A Forge can be built without the original builders present.

*G.E.C.K. variant note: Applies to terrestrial deployments. Marine and off-world variants require additional seeding specifications — see UNK-005.*

---

## v3 — Off-World Industrialization

**Question answered:** Can a Forge leave Earth?

**Core Characteristics**
- Reduced gravity tolerance
- Vacuum-compatible processes
- Radiation-hardened control systems
- Extreme material reuse

**Required Capabilities**
- Regolith and asteroid material processing
- Autonomous maintenance cycles — *contingent on UNK-008 / LT-003 resolution in `Tests/Leviathan_testing.md`*
- Energy scavenging (solar, nuclear, thermal)
- Zero-waste material flows

**Exit Condition** [Placeholder]
> The Forge can survive without Earth resupply.

---

## v4 — Autonomous Stellar Industry

**Question answered:** Can industry scale without humans nearby?

**Core Characteristics**
- Fully autonomous operation — *contingent on UNK-008 / LT-003 (autonomy architecture) resolution*
- Adaptive process optimization
- Long-duration reliability

**Exit Condition** [Placeholder]
> The Forge can expand faster than it fails.

---

## v5 — Interstellar Propagation (Conceptual Horizon)

**Question answered:** Can civilization carry itself forward?

*Note: v5 is a conceptual horizon, not a testable milestone. No exit condition is defined — this is intentional. If a falsifiable exit condition ever becomes articulable, add it at that time.*

**Core Characteristics**
- Self-contained industrial ecosystems
- Multi-generational operation
- Minimal external instruction

---

## Design Doctrine Notes

- Version numbers reflect survival thresholds, not feature lists
- Each version must be stable before advancement
- Skipping versions leads to systemic fragility
- Capabilities listed under future versions are trajectory markers — component taxonomy and implementation specs for those versions do not exist until those versions become active

> A Forge that cannot begin humbly will never reach the stars.

---

## Forge Regeneration Threshold (FRT)

### Doctrine

A system that consumes more than it regenerates is in decline regardless of
how productive it appears in the short term. The birthrate analogy applies
directly: a country that falls below its population replacement threshold is
shrinking even while its current population remains active and productive.
A Forge that processes material indefinitely without reinvesting in its own
capability is extractive, not regenerative — and that contradicts the core
mission.

The Forge Regeneration Threshold is the minimum fraction of material
throughput value that must be reinvested in Forge capability development
to keep the system alive and growing.

This is not an efficiency metric. It is a survival metric.

### Definition

> **Forge Regeneration Threshold (FRT):** The minimum fraction of material
> throughput value reinvested in Forge capability development per operating
> cycle. A Forge operating below its declared FRT for more than [N]
> consecutive cycles is considered to be in systemic decline.

**FRT floor:** [2–5%] *(Placeholder — not yet validated against first
operational cycle. Apply conservative end of range until calibrated.
See TR-002.)*

**FRT cycle definition:** [Placeholder — one operating month, one audit
cycle, or one defined throughput batch. To be declared by operator at v0
commissioning.]*

### What Counts as Reinvestment

Reinvestment in Forge capability development includes:

- Purchase of precision components or tooling the Forge cannot yet
  self-fabricate (bootstrap procurement doctrine — correct at v0)
- Repair or replacement of degraded Forge subsystems
- Tooling upgrades that expand the precision ceiling
- Calibration equipment and measurement capability
- Documentation and institutional memory infrastructure
- Energy system improvements that reduce per-cycle draw

Reinvestment does not include:

- General operating costs (utilities, consumables, labor)
- Materials purchased for external fabrication jobs
- Revenue distributed to operator or community

### Revenue Allocation Framework

Beyond the FRT floor, remaining throughput value allocation is
operator-defined. The repository does not prescribe how the remainder
is distributed. Common paths include:

| Allocation Path | Notes |
|----------------|-------|
| Utilities and operating costs | Non-negotiable operational floor |
| Community contribution | Consistent with Axiom P-3 (Collaboration and Mutual Benefit) |
| Materials sale → component purchase | Trading recovered material value for purchased precision capability is not a failure of salvage-first doctrine — it is the bootstrap path applied to the regeneration cycle |
| Operator/owner return | Legitimate at any allocation above FRT floor |
| Additional capability reinvestment above FRT | Accelerates version advancement |

The only constraint the repository places on this allocation is the FRT
floor. Everything above that floor is the operator's domain.

### Relationship to Existing KPIs

The FRT is a companion metric to the primary KPI:

| Metric | Measures |
|--------|---------|
| Value recovered per kWh consumed | Operational efficiency per cycle |
| Forge Regeneration Threshold | System health across cycles |

A Forge can be highly efficient per cycle while still declining if it
never reinvests. Both metrics are needed to characterize a healthy system.

### FRT and Version Advancement

FRT doctrine applies differently across versions:

| Version | FRT Relevance |
|---------|--------------|
| v0 | FRT floor declared; measurement begins; Placeholder value applies |
| v1 | FRT calibrated against first operational data; incorporated into profitability baseline (TR-001) |
| v2 | FRT must be positive across the forge network — not just per instance |
| v3+ | FRT applied to off-world resource loops; definition extends beyond monetary value |

### Logging

FRT measurement and per-cycle logging lives in
`Operations/Gate_07_Utilization.md`. This document owns the doctrine and
floor value. Gate_07 owns the measurement record.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                            | What Failed                                                           | What Was Learned                                                                                                   | Confidence | Revalidation Needed |
|----------|---------------|-----------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | Exit conditions written without confidence labels         | Implied false precision — conditions read as verified targets         | All exit conditions labeled [Placeholder]; verification notes added                                               | Replicated | No                  |
| May 2026 | Audit Review  | v5 written with same structural pattern as v0–v4          | Implied testable milestone status                                     | v5 explicitly designated as conceptual horizon with rationale for absent exit condition                           | Replicated | No                  |
| 2026-05-23 | Modeling    | No system health metric existed alongside efficiency KPI  | A Forge could be efficient per cycle while declining across cycles — the gap was invisible | FRT doctrine added. Efficiency and regeneration are distinct dimensions; both required to characterize a healthy system | Analogous | Yes |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                                      | Reconsider? |
|------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------|
| May 2026   | Exit conditions as verified targets without confidence labels     | False precision — implies operational validation that does not exist at v0                                         | No          |
| May 2026   | v5 as testable milestone with defined exit condition              | No falsifiable exit condition is currently articulable — forcing one produces theater                              | Yes — if falsifiable condition becomes articulable |
| 2026-05-23 | Fixed FRT percentage as mandatory doctrine                        | False precision at v0 — denominator unknown, operational cycles not yet run. Floating value with declared floor is more honest | No — floor remains floating until calibrated |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- FRT floor value claimed as validated without operational cycle data
- FRT floor removed or set to zero without explicit human rationale
- Revenue allocation framework prescribes operator allocation above FRT floor
- Exit conditions upgraded from Placeholder without external validation evidence
- Version capabilities listed as implementation specs rather than trajectory markers
- Stale flat filenames present in cross-references
- TR-001 or TR-002 unknown entries closed without resolution evidence
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### TR-001 — v1 profitability baseline undefined

| Field         | Value                  |
|---------------|------------------------|
| Status        | Open                   |
| Risk          | Medium                 |
| Priority      | Major                  |
| Type          | Architectural          |
| Blocking      | Yes                    |
| Owner         | Admin/Trajectories.md  |
| First Logged  | May 2026               |
| Last Reviewed | 2026-05-23             |

**Description:** What "profitably" means in the v1 exit condition remains
undefined — economic model, profit baseline, reinvestment definition, and
required rate are all absent.

**Why It Matters:** Without a defined profitability baseline, the v1 exit
condition cannot be verified — advancement from v0 to v1 is blocked.

**Resolution Path:** Full economic model is a v0→v1 transition task. Inputs
needed: (1) operating cost model from `Operations/Energy.md` — feeds from
EV-001; (2) revenue model for external outputs; (3) FRT-calibrated reinvestment
rate definition. Route to a dedicated `economics_v0.md` document when
v0→v1 transition planning begins. FRT doctrine (TR-002) is a prerequisite input.

---

### TR-002 — Forge Regeneration Threshold floor value not yet calibrated

| Field         | Value                  |
|---------------|------------------------|
| Status        | Open                   |
| Risk          | Medium                 |
| Priority      | Major                  |
| Type          | Architectural          |
| Blocking      | No                     |
| Owner         | Admin/Trajectories.md  |
| First Logged  | 2026-05-23             |
| Last Reviewed | 2026-05-23             |

**Description:** The FRT floor is declared at [2–5%] Placeholder. The actual
minimum viable reinvestment rate has not been validated against operational
data. The cycle definition has not been declared by an operator.

**Why It Matters:** A floor that is too low allows systemic decline while
appearing compliant. A floor that is too high creates unsustainable obligation
at bootstrap scale.

**Resolution Path:** Discharge via Lessons Learned — calibrate FRT floor
against first operational cycle data. Operator declares cycle definition at
v0 commissioning. Update floor from Placeholder to Analogous once first cycle
data exists. Cross-reference TR-001 — FRT is a required input to the v1
economic model.

---

### Resolution Log

- May 2026: All exit conditions labeled [Placeholder]. Verification notes added per condition.
- May 2026: v5 designated as conceptual horizon — explicit rationale for absent exit condition.
- May 2026: G.E.C.K. cross-references added at v2. UNK-008 / LT-003 autonomy dependency noted at v3 and v4.
- May 2026: v0 exit condition verification note added — self-reporting circularity acknowledged, human proxy defined.
- 2026-05-23: Retrofitted to File_Template.md structure. File State, Scope Boundary, File Purpose, Abandoned Paths, Drift Indicators added. Stale flat filenames corrected. Lessons Learned reformatted to full table. TR-002 added. FRT doctrine section added with definition, reinvestment taxonomy, revenue allocation framework, KPI companion table, version advancement table, and logging cross-reference to Gate_07_Utilization.md.

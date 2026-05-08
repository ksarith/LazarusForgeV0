# Lazarus Forge — Trajectory (v0 → Interstellar)

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 1 (Blocking at promotion)
- Sidecar: [#auditor-notes--unknowns]

This document outlines the evolutionary trajectory of the Lazarus Forge as a system. Each version represents a capability threshold, not a finished product.

The Forge is treated as a living industrial organism: it begins fragile, gains resilience, and eventually becomes location-independent.

**Role of this document:** This is the scope routing destination for the repository. When a capability or feature is identified as beyond the current version's scope, it routes here. Version milestones are survival thresholds — not specifications. Component taxonomy and implementation specs for future versions do not exist in this document; they are defined in module documents when those versions become active.

*Exit conditions are labeled **[Placeholder]** unless operational data or analog systems provide a basis for a higher confidence label. All exit conditions require external or proxy validation — see individual notes.*

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
- On-site power generation (partial) — see `energy_v0.md`; UNK-011 / EV-001 tracks demand baseline

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
- G.E.C.K.-based seeding — see `geck_forge_seed.md` for G.E.C.K. definition and minimum viable seed. Marine and environmental variants tracked in UNK-005 / GK-003.
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
- Autonomous maintenance cycles — *contingent on UNK-008 / LT-003 resolution in leviathan_testing.md*
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

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Exit conditions written without confidence labels | Implied false precision — conditions read as verified targets | All exit conditions labeled [Placeholder]; verification notes added |
| May 2026 | v5 written with same structural pattern as v0–v4 | Implied testable milestone status | v5 explicitly designated as conceptual horizon with rationale for absent exit condition |

---

## Auditor Notes & Unknowns

### TR-001 — v1 profitability baseline undefined
**Status:** Open
**Risk:** Medium
**What is not yet known:** What "profitably" means in the v1 exit condition. Specifically: what economic model applies, what the profit baseline is measured against, what counts as reinvestment, and at what rate reinvestment must occur to satisfy the condition.
**Resolution path:** "Profitably" Placeholder added to v1 exit condition (this revision). Full economic model is a v0→v1 transition task. Inputs needed: (1) operating cost model from `energy_v0.md` — feeds from EV-001; (2) revenue model for external outputs; (3) reinvestment rate definition. Route economic model development to a dedicated `economics_v0.md` document when v0→v1 transition planning begins.
**Logged:** Trajectories_LF.md audit cycle, May 2026
*Cross-module reference: UNK-027 in Unknowns_LF.md*

### Resolution Log
- May 2026: All exit conditions labeled [Placeholder]. Verification notes added per condition.
- May 2026: v5 designated as conceptual horizon — explicit rationale for absent exit condition.
- May 2026: G.E.C.K. cross-references added at v2. UNK-008 / LT-003 autonomy dependency noted at v3 and v4.
- May 2026: v0 exit condition verification note added — self-reporting circularity acknowledged, human proxy defined.

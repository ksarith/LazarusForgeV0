# Lazarus Forge — Trajectory (v0 → Interstellar)

This document outlines the evolutionary trajectory of the Lazarus Forge as a system, with clear versioning compatible with Git-based development. Each version represents a capability threshold, not a finished product.

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

**Outputs**
- Rods, plates, wire, powder
- Replacement parts for the Forge itself

**Exit Condition** [Placeholder]
> The Forge can repair itself faster than it degrades.

*Verification note: This exit condition cannot be self-reported by the Forge — the detector and the thing being detected are the same system at v0. Verification requires an external observer or proxy metric (e.g., mean time between failures trending downward over N cycles, tracked by human operator). See UNK-026 in `Unknowns_LF.md`. At v0, human-in-the-loop verification is the defined proxy, not a gap.*

---

## v1 — Self-Sustaining Industrial Node

**Question answered:** Can a Forge stay alive?

**Core Characteristics**
- Modular subsystems
- Semi-autonomous operation
- Expanded alloy handling
- On-site power generation (partial) — see `energy_v0.md` for power trajectory; UNK-011 tracks demand baseline

**Required Capabilities**
- Closed-loop material recycling
- Powderization and feedstock standardization
- Component fabrication for adjacent systems
- Environmental control (air, slag, heat)

**Outputs**
- Marketable industrial components
- Standardized feedstock formats
- Replacement modules

**Exit Condition** [Placeholder]
> The Forge can operate profitably while reinvesting in itself.

*"Profitably" definition [Placeholder]: Revenue or barter value generated from external outputs exceeds operating costs (energy, consumables, maintenance labor) while maintaining a reinvestment rate sufficient to sustain v1 capability. Economic model and baseline are not yet defined — see UNK-027 in `Unknowns_LF.md`.*

---

## v2 — Replicable Forge Network

**Question answered:** Can a Forge reproduce?

**Core Characteristics**
- G.E.C.K.-based seeding — see `geck_forge_seed.md` for G.E.C.K. definition and minimum viable seed configuration. Marine and environmental variants tracked in UNK-005.
- Standardized interfaces
- Distributed documentation and learning
- Minimal expert intervention

**Required Capabilities**
- Manufacture of Forge submodules
- Deployment kits for new sites
- Remote diagnostics and updates
- Logistics-aware production planning

**Outputs**
- New Forge seeds
- Infrastructure components
- Network-level redundancy

**Exit Condition** [Placeholder]
> A Forge can be built without the original builders present.

*G.E.C.K. variant note: This exit condition applies to terrestrial deployments. Marine and off-world variants require additional seeding specifications not yet defined — see UNK-005.*

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
- Autonomous maintenance cycles — *autonomy architecture dependency: see UNK-008 in `Unknowns_LF.md`. Autonomous maintenance at v3 requires UNK-008 resolution. v3 exit condition is contingent on UNK-008.*
- Energy scavenging (solar, nuclear, thermal)
- Zero-waste material flows

**Outputs**
- Structural elements for space construction
- Refined metals from celestial bodies
- Replacement parts for space assets

**Exit Condition** [Placeholder]
> The Forge can survive without Earth resupply.

---

## v4 — Autonomous Stellar Industry

**Question answered:** Can industry scale without humans nearby?

**Core Characteristics**
- Fully autonomous operation — *contingent on UNK-008 (autonomy architecture) resolution. v4 exit condition cannot be satisfied without a defined and tested autonomy architecture.*
- Adaptive process optimization
- Long-duration reliability

**Required Capabilities**
- Self-upgrading hardware and software
- Material discovery and adaptation
- Failure isolation and recovery
- Long-term mission planning

**Outputs**
- Space habitats
- Propulsion structures
- New Forge seeds

**Exit Condition** [Placeholder]
> The Forge can expand faster than it fails.

---

## v5 — Interstellar Propagation (Conceptual Horizon)

**Question answered:** Can civilization carry itself forward?

*Note: v5 is a conceptual horizon, not a testable milestone. No exit condition is defined — this is intentional. v5 represents the outer boundary of the trajectory, not a promotable version threshold. If a falsifiable exit condition for v5 ever becomes articulable, it should be added at that time.*

**Core Characteristics**
- Self-contained industrial ecosystems
- Multi-generational operation
- Minimal external instruction

**Required Capabilities**
- Interstellar transport compatibility
- Total resource independence
- Knowledge preservation across centuries

**Outputs**
- New industrial footholds
- Long-term survivability of human capability

---

## Design Doctrine Notes

- Version numbers reflect survival thresholds, not feature lists
- Each version must be stable before advancement
- Skipping versions leads to systemic fragility
- Git commits should map to version criteria, not ambition
- Capabilities listed under future versions are trajectory markers — component taxonomy and implementation specs for those versions do not exist until those versions become active

> A Forge that cannot begin humbly will never reach the stars.

---

## Audit Status

Reviewed under Auditor_Protocols.md v0.4, Trajectories_LF.md first audit cycle, May 2026.
Status: Exploration. Single-model audit pass: Claude (Sonnet 4.6).
Key changes from prior version: Added role statement and exit condition labeling note to header; added v0 exit condition verification note (UNK-026 cross-ref); added v1 "profitably" definition placeholder (UNK-027 cross-ref); added G.E.C.K. cross-ref and UNK-005 note at v2; added UNK-008 autonomy dependency notes at v3 and v4; added v5 conceptual horizon label with explicit rationale for absent exit condition; added doctrine note clarifying version markers vs. specifications.
Open unknowns: UNK-005 (marine G.E.C.K.), UNK-008 (autonomy architecture), UNK-026 (Graduation Rule detection circularity), UNK-027 (v1 profitability baseline). See `Unknowns_LF.md`.

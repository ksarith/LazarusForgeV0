# Unknowns_LF.md — Cross-Module Unknowns Global Index
**Version 1.0 — First full audit cycle complete. All unknowns migrated to owning file sidecars.**
**Expiry Rule now active. Protocol Performance metrics begin collecting.**

---

## Purpose

Cross-module unknowns index. Full entry detail lives in each owning file's sidecar. This file is the navigation layer only.

Module-specific unknowns → owning file sidecar
Cross-module unknowns → listed here, full entry in owning file
Navigation unknowns → Discovery.md

---

## What v1.0 Means

- First full audit cycle across all primary documents is complete
- UNK-004 (Expiry Rule) activates — check this index at the opening of each audit cycle for entries approaching two cycles
- Protocol Performance metrics begin collecting (see Auditor_Protocols.md Protocol Performance section)
- Preparatory framing lines drop from audit prompts — documents stand on their own
- The Sidecar Model is fully operational — new unknowns go into owning file sidecars first, cross-module entries are indexed here

---

## Dependency Map

```
EV-001 (energy_v0.md) -> LT-001 (leviathan_testing.md)
  -> LT-003 (autonomy architecture)
     -> LT-004 (trust model)
     -> LT-005 (priority propagation)
     -> SR-003 (battery buffer sizing)

LT-002 (storage degradation) -> feeds LT-001 (parallel)

GK-003 (induction pad) -> depends on LT-001

CO-001 (graduation rule circularity) -> feeds FL-001
TS-001 (forge duty threshold) -> feeds FL-001
FL-001 (gate logic determinism) — In Progress

TS-002 (contamination routing) -> affects AS-003 (air scrubber waste)

EC-001 (confidence threshold) -> LT-003 / EC-007
EC-004 (governance failure modes) -> EC-007
EC-007 (governance fail-safe) — In Progress

TR-001 (v1 profitability) -> depends on EV-001

EL-001 (forge standard interface) -> depends on LT-001

AP-001 (auditor metrics) -> depends on UNK-004 (now active)
AP-003 (audit trail schema) -> AP-001
```

---

## Active Unknowns Index

### Energy & Power

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| EV-001 | Forge power demand uncharacterized | `energy_v0.md` | In Progress | Blocking |

### Leviathan / Autonomy

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| LT-001 | Power envelope — no placeholder anchor | `leviathan_testing.md` | Open | Blocking |
| LT-002 | Deep-ocean storage degradation | `leviathan_testing.md` | Open | Blocking |
| LT-003 | Autonomy architecture unspecified | `leviathan_testing.md` | Open | Blocking |
| LT-004 | Trust model mechanism undefined | `leviathan_testing.md` | Open | Blocking |
| LT-005 | Priority propagation — no mechanism | `leviathan_testing.md` | Open | Blocking |
| LT-006 | Ethical log survival at depth | `leviathan_testing.md` | Open | Non-blocking |

### Gate Logic & Triage

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| FL-001 | Gate logic determinism | `Lazarus_forge_v0_flow.md` | In Progress | Blocking |
| TS-001 | "Sufficient for forge duty" threshold | `Component_Triage_System.md` | In Progress | Blocking |
| TS-002 | Contamination routing protocol | `Component_Triage_System.md` | Open | Blocking |
| TS-003 | Gate determinism (downstream) | `Component_Triage_System.md` | In Progress | Blocking |
| CO-001 | Graduation Rule detection circularity | `Components.md` | In Progress | Blocking |

### Ethics & Governance

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| EC-001 | "Sufficient confidence" threshold | `Ethical_Constraints.md` | Open | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Ethical_Constraints.md` | Open | Blocking |
| EC-003 | Human escalation path | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-004 | Governance failure modes lifecycle | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-006 | Ethical log survival under unit loss | `Ethical_Constraints.md` | Open | Non-blocking |
| EC-007 | Governance fail-safe | `Ethical_Constraints.md` | In Progress | Blocking |

### Governance & Verification

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| AP-001 | Auditor effectiveness metrics | `Auditor_Protocols.md` | Open | Blocking |
| AP-002 | Override vs. immutability boundary | `Auditor_Protocols.md` | In Progress | Blocking |
| AP-003 | Audit trail schema | `Auditor_Protocols.md` | Open | Blocking |

### Hardware Modules

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| SC-001 | RPM envelope not validated | `Spin_Chamber_v0.md` | Open | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Spin_Chamber_v0.md` | Open | Blocking |
| SC-003 | MHD damping effectiveness | `Spin_Chamber_v0.md` | Open | Exploratory |
| SC-004 | Wire extrusion nozzle design | `Spin_Chamber_v0.md` | Open | Exploratory |
| AS-001 | 500W power budget not validated | `Air_Scrubber_v0.md` | Open | Medium |
| AS-002 | Marine bubble-column depth scope | `Air_Scrubber_v0.md` | In Progress | Low |
| AS-003 | Scrubber waste stream and saturation | `Air_Scrubber_v0.md` | In Progress | Medium |
| SR-001 | Galvanic corrosion mitigation | `Support_Raft_v0.md` | Open | High |
| SR-002 | Sacrificial shell material selection | `Support_Raft_v0.md` | Open | Medium |
| SR-003 | Battery buffer sizing | `Support_Raft_v0.md` | Open | Medium |
| SR-004 | Induction charging pad design | `Support_Raft_v0.md` | Open | Medium |
| SR-005 | Chicken-and-egg end-of-region | `Support_Raft_v0.md` | Open | Medium |
| SR-006 | Cold storage rack design | `Support_Raft_v0.md` | Open | Low |
| SR-007 | Cache sanitization on hull compromise | `Support_Raft_v0.md` | Open | Medium |
| SR-008 | Dynamic positioning vs. mooring | `Support_Raft_v0.md` | Open | Low |
| SR-009 | Ballast pump energy draw | `Support_Raft_v0.md` | Open | Medium |
| SR-010 | Thermal management modularity | `Support_Raft_v0.md` | Open | Low |

### Salvage & Fabrication

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| GK-001 | Forge loop definition | `geck_forge_seed.md` | Resolved | — |
| GK-002 | Sacrificial anode material | `geck_forge_seed.md` | Open | Medium |
| GK-003 | Induction charging pad design | `geck_forge_seed.md` | Open | Low |
| GK-004 | Marine AM material durability | `geck_forge_seed.md` | Open | Low |
| ST-001 | Grain storage and tracking protocol | `Ship_of_Theseus_Right_to_Repair.md` | Open | Low |
| ST-002 | QR documentation standard | `Ship_of_Theseus_Right_to_Repair.md` | Open | Low |
| ST-003 | Legal applicability by jurisdiction | `Ship_of_Theseus_Right_to_Repair.md` | Open | Medium |
| EL-001 | Forge-Standard interface spec | `Electronics.md` | Open | Medium |
| EL-002 | PCB trace width for v0 tooling | `Electronics.md` | Open | Low |
| EL-003 | TMR voter implementation | `Electronics.md` | Open | Medium |
| EL-004 | Chemical etch waste stream | `Electronics.md` | Open | Medium |

### Trajectory

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| TR-001 | v1 profitability baseline | `Trajectories_LF.md` | Open | Blocking |

### Future / Deferred

| ID | Title | Owning file | Status |
|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Auditor_Protocols.md` | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | `geck_forge_seed.md` | In Progress (stub added) |
| UNK-001 | Discovery.md Unknowns_LF.md entry | `Discovery.md` | In Progress |

---

## Expiry Watch

*Expiry Rule is now active at v1.0. Check this table at the opening of each audit cycle.*

No entries past two cycles at v1.0 — all entries are new this cycle.

---

## Resolved & Discharged Archive

| ID | Title | Resolution | Date |
|---|---|---|---|
| UNK-002 | Repo topology — Astroid-miner | Resolved — human confirmation; deferred to Leviathan milestone | May 2026 |
| UNK-004 | Expiry Rule enforcement | Discharged — Sidecar Model addresses structurally | May 2026 |
| UNK-022 | Full Stop Review trigger conditions | Resolved — added to Auditor_Protocols.md v0.5 | May 2026 |
| GK-001 | Forge loop definition | Resolved — defined in geck_forge_seed.md Section III | May 2026 |

---

## Audit Trail

**v0.1–v0.91:** See prior version history. Full entry detail for all unknowns now migrated to owning file sidecars per Auditor_Protocols.md v0.5 Sidecar Model.

**v1.0 — May 2026:**
First full audit cycle across all primary documents complete.
All unknowns migrated to owning file sidecars.
Global index restructured — summary tables only, full detail in owning files.
UNK-004 (Expiry Rule) activates — Expiry Watch section now live.
Electronics.md added — EL-001 through EL-004 logged.
Expiry Rule now active. Protocol Performance metrics begin collecting.
Preparatory framing lines drop from audit prompts from this version forward.

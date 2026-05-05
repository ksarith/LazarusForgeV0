# Unknowns_LF.md — Cross-Module Unknowns Global Index
**Version 0.91 — Restructured as global index only per Auditor_Protocols.md v0.5 Sidecar Model.**
**Full entry detail lives in each owning file's sidecar. This file is the navigation layer.**
**v1.0 trigger: first full audit cycle across all primary documents complete.**

---

## Purpose

Cross-module unknowns index. Entries here span multiple files or affect system-wide navigation. Module-specific unknowns live in each file's own `## Auditor Notes & Unknowns` sidecar.

---

## Dependency Map

```
UNK-011 (energy_v0.md) -> UNK-006 (leviathan_testing.md)
  -> UNK-008 (leviathan_testing.md)
     -> UNK-009, UNK-010, UNK-015

UNK-027 (Trajectories_LF.md) -> feeds UNK-011

UNK-007 (leviathan_testing.md) -> feeds UNK-006 (parallel)

UNK-026 (Components.md) -> feeds UNK-012
UNK-024 (Component_Triage_System.md) -> feeds UNK-012
UNK-012 (Lazarus_forge_v0_flow.md) — In Progress

UNK-005 (geck_forge_seed.md) -> depends on UNK-006

UNK-013 (Ethical_Constraints.md) -> UNK-008 / UNK-019
UNK-016 (Ethical_Constraints.md) -> UNK-019
UNK-014 (Ethical_Constraints.md) — In Progress (hook added)

UNK-002 [RESOLVED] -> UNK-003 [DEFERRED]
```

---

## Active Unknowns Index

### Governance & Verification

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-001 | Discovery.md update pending for Unknowns_LF.md | `Discovery.md` | Open | Non-blocking |
| AP-001 | Auditor effectiveness metrics | `Auditor_Protocols.md` | Open | Blocking |
| AP-002 | Override vs. immutability boundary | `Auditor_Protocols.md` | In Progress | Blocking |
| AP-003 | Audit trail schema deferred | `Auditor_Protocols.md` | Open | Blocking |

### Ethics & Governance

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-013 | "Sufficient confidence" threshold undefined | `Ethical_Constraints.md` | Open | Blocking |
| UNK-014 | Anti-Weaponization pattern-matching undefined | `Ethical_Constraints.md` | In Progress | Blocking |
| UNK-015 | Human escalation path undefined | `Ethical_Constraints.md` | In Progress | Blocking |
| UNK-016 | Governance failure modes unspecified | `Ethical_Constraints.md` | In Progress | Blocking |
| UNK-017 | Life-preservation vs. Anti-Weaponization | `Ethical_Constraints.md` | In Progress | Blocking |
| UNK-018 | Ethical log survival at depth | `Ethical_Constraints.md` | Open | Non-blocking |
| UNK-019 | Governance fail-safe behavior | `Ethical_Constraints.md` | In Progress | Blocking |

### Gate Logic & Triage

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-012 | Gate logic determinism | `Lazarus_forge_v0_flow.md` | In Progress | Blocking |
| UNK-024 | "Sufficient for forge duty" threshold | `Component_Triage_System.md` | In Progress | Blocking |
| UNK-025 | Contamination routing protocol | `Component_Triage_System.md` | Open | Blocking |
| UNK-026 | Graduation Rule detection circularity | `Components.md` | In Progress | Blocking |

### Energy & Power

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-011 | Forge power demand uncharacterized | `energy_v0.md` | In Progress | Blocking |
| UNK-007 | Deep-ocean storage degradation | `leviathan_testing.md` | Open | Blocking |

### Leviathan / Autonomy

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-006 | Leviathan power envelope | `leviathan_testing.md` | Open | Blocking |
| UNK-008 | Leviathan autonomy architecture | `leviathan_testing.md` | Open | Blocking |
| UNK-009 | Trust model mechanism | `leviathan_testing.md` | Open | Blocking |
| UNK-010 | Priority propagation mechanism | `leviathan_testing.md` | Open | Blocking |

### Future / Deferred

| ID | Title | Owning file | Status | Priority (Promo) |
|---|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Auditor_Protocols.md` | Deferred (Leviathan milestone) | Non-blocking |
| UNK-005 | Marine G.E.C.K. seed variant | `geck_forge_seed.md` | Open (Exploratory) | Non-blocking |
| UNK-027 | v1 profitability baseline | `Trajectories_LF.md` | Open | Blocking |

---

## Expiry Watch

*(No entries past two cycles at v0.91. UNK-004 discharged — see Resolved Archive.)*

---

## Resolved & Discharged Archive

| ID | Title | Resolution | Date |
|---|---|---|---|
| UNK-002 | Repo topology — Astroid-miner | Resolved — human confirmation; deferred to Leviathan milestone | May 2026 |
| UNK-004 | Expiry Rule enforcement | Discharged — Sidecar Model addresses structurally; Expiry Rule retained as backstop only | May 2026 |
| UNK-022 | Full Stop Review trigger conditions | Resolved — three trigger conditions added to Auditor_Protocols.md v0.5 | May 2026 |

---

## Audit Trail

**v0.1–v0.9:** See prior versions for full entry history. All full entries now migrated to owning file sidecars.

**v0.91 — May 2026:**
Restructured as global index per Auditor_Protocols.md v0.5 Sidecar Model.
Full entry detail for AP-001, AP-002, AP-003 migrated to `Auditor_Protocols.md` sidecar.
UNK-004 discharged — Sidecar Model supersedes it structurally.
UNK-020, UNK-021, UNK-023 renumbered as AP-001, AP-002, AP-003 in owning file.
All other entries retained as index rows pointing to owning files.
Full entry detail for UNK-006 through UNK-027 to be migrated to owning file sidecars during remaining audit cycles.

# Unknowns_LF.md — Cross-Module Unknowns Global Index
**Version 1.4 — Gate_03_Reduction and Gate_06_Fabrication added. GR and GF entries logged.**
**Expiry Rule active. Protocol Performance metrics collecting.**

---

## Purpose

Cross-module unknowns index. Full entry detail lives in each owning file's sidecar. This file is the navigation layer only.

Module-specific unknowns → owning file sidecar
Cross-module unknowns → listed here, full entry in owning file
Navigation unknowns → Discovery.md

---

## What v1.4 Means

- Operations/Gate_03_Reduction.md created — only irreversible
  step, doctrine before specification, three hard prerequisites
- Operations/Gate_06_Fabrication.md created — arc welding
  gatekeeper, add-to-excess and mill-to-spec, precision ceiling
- GR-001 through GR-005 added to Reduction section
- GF-001 through GF-005 added to Fabrication section
- GR-003 (waste disposal) flagged Critical — no owner in repository
- FL-002 and UNK-007 effectively resolved by Gate_03_Reduction.md
  creation — file now exists and owns the doctrine
- Gate_07_Utilization.md identified as next pending file via GF-005
- Dependency map updated with GR and GF entries
- Discovery.md updated

---

## What v1.3 Means

- Operations/Gate_01_Intake.md created — system entry
  point, safety screening, identification, provenance
- GI-001 through GI-005 added to Intake section
- GI-002 (energetic discharge) and GI-003 (augmented
  detection) are hard prerequisites for first operational
  Intake run — highest safety priority in Operations cluster
- Dependency map updated with GI entries
- Discovery.md updated to reflect Gate_01_Intake.md addition

---

## What v1.2 Means

- Architecture/Forge_Net.md created — decentralized network
  and logistics prerequisite
- FN-001 through FN-005 added to Network section
- FN-001 and FN-005 are Hard prerequisites for first
  forge-to-forge connection — highest priority in network cluster
- Dependency map updated with FN entries
- Discovery.md updated to reflect Forge_Net.md addition

---

## What v1.1 Means

- Spin_Chamber_v0.md and Material_Separation_Gate_v0.md retrofitted
  to File_Template.md structure and audited this cycle
- SC-001 through SC-008 and MG-001 through MG-008 added to Hardware
  Modules table
- SC-001 status updated from Open to In Progress following RPM
  safety calculation (2026-05-15)
- Material Separation Gate prefix corrected from GK to MG to avoid
  collision with geck_forge_seed.md GK prefix
- UNK-006 through UNK-008 added as new cross-module unknowns
- DS-001 logged in Material_Separation_Gate_v0.md — Purification
  stage terminology dispute; owner is Lazarus_forge_v0_flow.md

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

SC-001 (RPM envelope) -> SC-005 (drive system geometry)
SC-002 (segregation effectiveness) — primary Gen-0 validation target
SC-006 (siting) -> UNK-006 (master safety registry)
MG-006 (siting) -> UNK-006 (master safety registry)
SC-006 (siting) -> UNK-006 (master safety registry)
MG-006 (siting) -> UNK-006 (master safety registry)
UNK-007 (reduction module) -> MG-001, MG-002, MG-007
UNK-008 (welding wire) -> SC-004
FN-001 (validation criteria) -> blocks first network connection
FN-005 (privacy doctrine) -> blocks first network connection
FN-002 (replication factor) -> depends on LT-002 (node loss rate)
FN-003 (gaming detection) -> must deploy with FN positive reinforcement
FN-004 (transport layer) -> informs FN-002 sync doctrine
GI-002 (energetic discharge) -> blocks first operational Intake run
GI-003 (augmented detection) -> blocks first unsupervised Intake run
GI-001 (reference database) -> informs GI-003 detection protocol
GI-004 (tagging schema) -> depends on Ship_of_Theseus grain system
GI-005 (pre-Intake protocol) -> depends on GI-002 energetic doctrine
GR-002 (method selection) -> unblocks GR-001, GR-004, GR-005
GR-003 (waste disposal) -> no owner in repository — Critical gap
GR-001 (output envelope) -> depends on GR-002, feeds MG inputs
GR-004 (particulate) -> depends on GR-002, feeds Air_Scrubber sizing
GR-005 (automation criteria) -> depends on FL-001, GI-002, GI-003, GR-001, GR-004
GF-001 (wire diameter) -> depends on welding process selection, feeds SC-004
GF-002 (precision ceiling) -> feeds all fabrication tolerance claims
GF-005 (Utilization gap) -> Gate_07_Utilization.md needs creation
```

---

## Active Unknowns Index

### Energy & Power

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EV-001 | Forge power demand uncharacterized | `energy_v0.md` | In Progress | Blocking |

### Leviathan / Autonomy

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| LT-001 | Power envelope — no placeholder anchor | `leviathan_testing.md` | Open | Blocking |
| LT-002 | Deep-ocean storage degradation | `leviathan_testing.md` | Open | Blocking |
| LT-003 | Autonomy architecture unspecified | `leviathan_testing.md` | Open | Blocking |
| LT-004 | Trust model mechanism undefined | `leviathan_testing.md` | Open | Blocking |
| LT-005 | Priority propagation — no mechanism | `leviathan_testing.md` | Open | Blocking |
| LT-006 | Ethical log survival at depth | `leviathan_testing.md` | Open | Non-blocking |

### Gate Logic & Triage

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FL-001 | Gate logic determinism | `Lazarus_forge_v0_flow.md` | In Progress | Blocking |
| FL-002 | Reduction module unassigned — upstream dependency | `Architecture/Forge_flow.md` | Resolved | — |
| TS-001 | "Sufficient for forge duty" threshold | `Component_Triage_System.md` | In Progress | Blocking |
| TS-002 | Contamination routing protocol | `Component_Triage_System.md` | Open | Blocking |
| TS-003 | Gate determinism (downstream) | `Component_Triage_System.md` | In Progress | Blocking |
| CO-001 | Graduation Rule detection circularity | `Components.md` | In Progress | Blocking |

### Ethics & Governance

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EC-001 | "Sufficient confidence" threshold | `Ethical_Constraints.md` | Open | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Ethical_Constraints.md` | Open | Blocking |
| EC-003 | Human escalation path | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-004 | Governance failure modes lifecycle | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-006 | Ethical log survival under unit loss | `Ethical_Constraints.md` | Open | Non-blocking |
| EC-007 | Governance fail-safe | `Ethical_Constraints.md` | In Progress | Blocking |

### Governance & Verification

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| AP-001 | Auditor effectiveness metrics | `Auditor_Protocols.md` | Open | Blocking |
| AP-002 | Override vs. immutability boundary | `Auditor_Protocols.md` | In Progress | Blocking |
| AP-003 | Audit trail schema | `Auditor_Protocols.md` | Open | Blocking |

### Hardware Modules

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| SC-001 | RPM envelope not validated | `Spin_Chamber_v0.md` | In Progress | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Spin_Chamber_v0.md` | Open | Blocking |
| SC-003 | MHD damping effectiveness | `Spin_Chamber_v0.md` | Open | Exploratory |
| SC-004 | Wire extrusion nozzle design | `Spin_Chamber_v0.md` | Open | Exploratory |
| SC-005 | Drive system geometry — dynamic imbalance blocked | `Spin_Chamber_v0.md` | Open | Major |
| SC-006 | Siting and area-of-operation requirements | `Spin_Chamber_v0.md` | Open | Major |
| SC-007 | Extraction process may disrupt segregation gradients | `Spin_Chamber_v0.md` | Open | Major |
| SC-008 | Graphite crucible carbon pickup in alloy | `Spin_Chamber_v0.md` | Open | Major |
| MG-001 | Quantitative energy reduction not established | `Material_Separation_Gate_v0.md` | Open | Minor |
| MG-002 | Optimal RPM bands not characterized per feedstock | `Material_Separation_Gate_v0.md` | Open | Major |
| MG-003 | Confidence threshold not empirically validated | `Material_Separation_Gate_v0.md` | Open | Major |
| MG-004 | Geometry correction algorithm not specified | `Material_Separation_Gate_v0.md` | Open | Major |
| MG-005 | Aquatic biofouling impact on rotor balance | `Material_Separation_Gate_v0.md` | Open | Exploratory |
| MG-006 | Siting and area-of-operation requirements | `Material_Separation_Gate_v0.md` | Open | Major |
| MG-007 | Rotor jam and entanglement recovery undefined | `Material_Separation_Gate_v0.md` | Open | Major |
| MG-008 | Sensor fouling from conductive or abrasive fines | `Material_Separation_Gate_v0.md` | Open | Major |
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

| ID | Title | Owning File | Status | Priority (Promo) |
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

### Reduction

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GR-001 | Output envelope not validated against Gate_04 inputs | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-002 | Reduction method not selected | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-003 | Biological and chemical waste disposal doctrine not assigned | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GR-004 | Particulate generation rate and composition not characterized | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-005 | Automation introduction criteria not defined | `Operations/Gate_03_Reduction.md` | Open | Major |

### Fabrication

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GF-001 | Welding wire diameter specification not defined | `Operations/Gate_06_Fabrication.md` | Open | Major |
| GF-002 | Precision ceiling not characterized at v0 bootstrap | `Operations/Gate_06_Fabrication.md` | Open | Major |
| GF-003 | Material removal hardware not specified | `Operations/Gate_06_Fabrication.md` | Open | Minor |
| GF-004 | Fabrication energy consumption not characterized | `Operations/Gate_06_Fabrication.md` | Open | Minor |
| GF-005 | Utilization stage has no owning file | `Operations/Gate_06_Fabrication.md` | Open | Minor |

### Intake

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GI-001 | Reference database content and coverage not defined | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-002 | Energetic material discharge doctrine not defined | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-003 | Augmented hazard detection capability not specified | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-004 | Intake tagging schema not cross-validated against grain system | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-005 | Pre-Intake protocol for special handling not defined | `Operations/Gate_01_Intake.md` | Open | Major |

### Network

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FN-001 | Data validation criteria not defined | `Architecture/Forge_Net.md` | Open | Critical |
| FN-002 | Data replication factor not defined | `Architecture/Forge_Net.md` | Open | Major |
| FN-003 | Gaming detection criteria not defined | `Architecture/Forge_Net.md` | Open | Major |
| FN-004 | v0 Network transport layer not specified | `Architecture/Forge_Net.md` | Open | Major |
| FN-005 | Data privacy and access control not specified | `Architecture/Forge_Net.md` | Open | Critical |

### Trajectory

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| TR-001 | v1 profitability baseline | `Trajectories_LF.md` | Open | Blocking |

### Cross-Module

| ID | Title | Owning Files | Status | Priority |
|---|---|---|---|---|
| UNK-006 | Master safety registry — siting and clearance for all rotating and thermal modules | `Spin_Chamber_v0.md` SC-006, `Material_Separation_Gate_v0.md` MG-006 | Open | Major |
| UNK-007 | Reduction module unassigned — upstream dependency for Gate and flow document | `Architecture/Forge_flow.md` FL-002, `Operations/Gate_04_Separation_Mechanical.md` MG-007 | Resolved | — |
| UNK-008 | Welding wire specification and qualification — no owner assigned | `Spin_Chamber_v0.md` SC-004 | Open | Major |

### Future / Deferred

| ID | Title | Owning File | Status |
|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Auditor_Protocols.md` | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | `geck_forge_seed.md` | In Progress (stub added) |
| UNK-001 | Discovery.md Unknowns_LF.md entry | `Discovery.md` | In Progress |

---

## Expiry Watch

*Expiry Rule is active. Check this table at the opening of each audit cycle.*

No entries past two cycles at v1.1 — SC and MG entries are new this cycle.
FL-001 and several EC entries are In Progress from prior cycle — watch at next cycle.

---

## Resolved & Discharged Archive

| ID | Title | Resolution | Date |
|---|---|---|---|
| UNK-002 | Repo topology — Astroid-miner | Resolved — human confirmation; deferred to Leviathan milestone | May 2026 |
| UNK-004 | Expiry Rule enforcement | Discharged — Sidecar Model addresses structurally | May 2026 |
| UNK-022 | Full Stop Review trigger conditions | Resolved — added to Auditor_Protocols.md v0.5 | May 2026 |
| FL-002 | Reduction module unassigned | Resolved — Operations/Gate_03_Reduction.md created. Doctrine, prohibited inputs, output envelope, contamination protocol, and emergency shutdown defined | 2026-05-15 |
| UNK-007 | Reduction module upstream dependency | Resolved — Gate_03_Reduction.md creation closes the gap. Output envelope cross-validation with Gate_04 tracked under GR-001 | 2026-05-15 |
| GK-001 | Forge loop definition | Resolved — defined in geck_forge_seed.md Section III | May 2026 |

---

## Audit Trail

**v0.1–v0.91:** See prior version history. Full entry detail for all unknowns now migrated
to owning file sidecars per Auditor_Protocols.md v0.5 Sidecar Model.

**v1.0 — May 2026:**
First full audit cycle across all primary documents complete.
All unknowns migrated to owning file sidecars.
Global index restructured — summary tables only, full detail in owning files.
UNK-004 (Expiry Rule) activates — Expiry Watch section now live.
Electronics.md added — EL-001 through EL-004 logged.
Protocol Performance metrics begin collecting.
Preparatory framing lines drop from audit prompts from this version forward.

**v1.4 — 2026-05-15:**
Operations/Gate_03_Reduction.md created — only irreversible step,
doctrine before specification, three hard prerequisites, method
selection as keystone unknown. GR-001 through GR-005 added.
GR-003 (waste disposal) flagged Critical — no owner in repository.
Operations/Gate_06_Fabrication.md created — arc welding gatekeeper,
add-to-excess and mill-to-spec, precision ceiling ownership.
GF-001 through GF-005 added. GF-005 identifies Gate_07_Utilization.md
as next required file. FL-002 and UNK-007 updated to Resolved —
Gate_03_Reduction.md creation closes the Reduction module gap.
Dependency map updated. Discovery.md updated.

**v1.3 — 2026-05-15:**
Operations/Gate_01_Intake.md created — system entry point,
safety screening, identification, parts list generation,
fastener recovery, provenance tagging, unknown item protocol.
GI-001 through GI-005 added to Intake section.
GI-002 (energetic discharge) and GI-003 (augmented detection)
flagged as hard prerequisites for first operational Intake run.
Dependency map updated. Discovery.md updated.

**v1.2 — 2026-05-15:**
Architecture/Forge_Net.md created — decentralized network doctrine,
data and physical infrastructure, cluster governance emergence,
positive reinforcement, security threat model, privacy classification.
FN-001 through FN-005 added to Network section.
FN-001 (validation criteria) and FN-005 (privacy doctrine) flagged
as hard prerequisites for first forge-to-forge connection.
Dependency map updated. Discovery.md updated to include Forge_Net.md.
Spin_Chamber_v0.md and Material_Separation_Gate_v0.md retrofitted to
File_Template.md structure. Full audit passes completed by Claude,
Grok, and ChatGPT — three independent auditor convergence on core findings.
SC-001 through SC-008 added to Hardware Modules table.
SC-001 status updated to In Progress — RPM safety calculation completed,
safety factor ~32× confirmed, dynamic analysis deferred to SC-005.
Material Separation Gate prefix corrected from GK to MG to avoid
collision with geck_forge_seed.md prefix.
MG-001 through MG-008 added to Hardware Modules table.
FL-002 added to Gate Logic table — Reduction module unassigned.
UNK-006 through UNK-008 added as new cross-module unknowns.
DS-001 logged in Material_Separation_Gate_v0.md Active Disputes —
Purification stage terminology; owner Lazarus_forge_v0_flow.md.
Dependency map updated with SC, MG, and UNK entries.

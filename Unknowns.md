# Unknowns.md — Cross-Module Unknowns Global Index
**Version 3.0 — 2026-06-11. Phase 1 quick-close pass. Six unknowns resolved: RS-002 (casing), RS-003 (Archive/ created), FD-004 (bidirectional cross-ref), GMP-001, GMP-002 (governance confirmations), RIP-003 (violation log location declared). RS-003 removed from Blocking Watch. All six moved to Resolved Archive.**
**Expiry Rule active. Protocol Performance metrics collecting.**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## Purpose

Cross-module unknowns index. Full entry detail lives in each owning file's sidecar. This file is the navigation layer only.

Module-specific unknowns → owning file sidecar
Cross-module unknowns → listed here, full entry in owning file
Pending corrections (task list) → PC cluster in this file
Programmatic URL routing → `Routing.md`
Navigation map and scope boundaries → `Discovery.md`

**Cross-module dependencies** are owned by each file's Upstream/Downstream tables as of the v0.2 retrofit pass. See `Discovery.md` Scope Map for navigation. The Dependency Map section formerly in this file has been retired — it was a compensatory mechanism for files that lacked Upstream/Downstream tables. Those tables now exist across the full active file set and are the authoritative source.

**Discovery.md task tables have been retired.** Pending corrections are tracked here as PC clusters. Discovery.md is a navigation map, not a task list.

### Size Management Rules

These rules are enforced at every audit cycle opening:

1. **What vX.X Means — rolling single section.** Only the current version's What section is kept live. When a new version is cut, the prior What section is retired. Its content is already captured in the Audit Trail entry for that version. Keeping stacked What sections is redundant.

2. **Resolved entries leave the Active Index immediately.** Once an unknown is resolved, it moves to the Resolved & Discharged Archive. It does not linger in the Active Index with a Resolved status badge. Active tables show Open and In Progress only.

3. **Compression trigger at 1,200 lines.** If this file exceeds 1,200 lines, a compression pass is mandatory before new entries are added. Compression scope: retire old What sections, verify all resolved actives have moved to archive, confirm Dependency Map remains retired.

4. **Audit Trail entries are concise.** Two to three sentences maximum: what changed, what was resolved, what moved to watch lists. The What vX.X section carries the full narrative during the session; the Audit Trail is the permanent compressed record.

---

## What v3.0 Means

- **Phase 1 quick-close pass complete** — six housekeeping unknowns resolved. No new unknowns introduced. RS-003 removed from Blocking Watch.
- **RS-002** — `Forge_Flow.md` casing corrected to `Forge_flow.md` in Discovery.md Rename Registry.
- **RS-003** — `Archive/README.md` created; append-only doctrine declared; RIP-001 partial dependency cleared.
- **FD-004** — `Architecture/Friction_Dynamics.md` confirmed in Support_Raft.md v0.5 Upstream Dependencies; cross-reference bidirectional.
- **GMP-001 & GMP-002** — GOV-001 resolution confirmed; Governance_Migration_Protocol.md canonical ownership logged.
- **RIP-003** — `Admin/Logs/violations.md` declared as canonical violation incident log location.


## What v2.9 Means

- **Support_Raft.md v0.5** — full File_Template.md compliance retrofit. Navigation Anchors, File State, Scope Boundary, Upstream/Downstream tables added. All stale file references corrected. Five-anchor Purpose reframe adopted (Energy, Truth, Recovery, Material, Communication anchors). Failure Philosophy & Succession section added; symmetric Leviathan ↔ Raft ↔ Shore Forge relationship formalized.
- **SR-010 RESOLVED** — thermal management modularity declared modular/expandable in Mechanical Design section.
- **SR-006 In Progress** — cold storage rack specification trigger defined as Leviathan unit physical envelope confirmation.
- **Dependency Map retired** — cross-module dependencies now owned by each file's Upstream/Downstream tables following full retrofit pass.
- **Size management rules adopted** — What vX.X compression rule, Active Index housekeeping rule, 1,200-line compression trigger, and concise Audit Trail rule added to Purpose section.

*Prior What vX.X sections (v2.4 through v2.8) retired per compression rule. Full session narratives preserved in Audit Trail.*

---

## Active Unknowns Index

### Energy & Power

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EV-001 | Forge power demand uncharacterized | `Operations/Energy.md` | In Progress | Blocking |
| EV-002 | Parasitic and thermal startup loads for biogas streams uncharacterized | `Operations/Energy.md` | Open | Minor |
| EV-003 | Salvaged battery thermal containment and ventilation strategy undefined | `Operations/Energy.md` | Open | Critical |

### Leviathan / Autonomy

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| LT-001 | Power envelope — no placeholder anchor | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-002 | Deep-ocean storage degradation | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-003 | Autonomy architecture unspecified | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-004 | Trust model mechanism undefined | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-005 | Priority propagation — no mechanism | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-006 | Ethical log survival at depth | `Tests/Leviathan_testing.md` | Open | Non-blocking |

### Gate Logic & Triage

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FL-001 | Gate logic determinism | `Architecture/Forge_flow.md` | In Progress | Blocking |
| TS-001 | "Sufficient for forge duty" threshold | `Operations/Gate_02_Triage.md` | In Progress | Blocking |
| TS-002 | Contamination routing protocol | `Operations/Gate_02_Triage.md` | Open | Blocking |
| TS-003 | Gate determinism (downstream) | `Operations/Gate_02_Triage.md` | In Progress | Blocking |
| CO-001 | Graduation Rule detection circularity | `Architecture/Components.md` | In Progress | Blocking |
| CO-002 | Metrology precision thresholds | `Architecture/Components.md` | Open | Minor |

### Ethics & Governance

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EC-001 | "Sufficient confidence" threshold | `Admin/Ethical_Constraints.md` | Open | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Admin/Ethical_Constraints.md` | Open | Blocking |
| EC-003 | Human escalation path | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-004 | Governance failure modes lifecycle | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-006 | Ethical log survival under unit loss | `Admin/Ethical_Constraints.md` | Open | Non-blocking |
| EC-007 | Governance fail-safe | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| GOV-001 | Governance migration mechanics incompletely operationalized | `Admin/Governance_Charter.md` | Open | Major |
| GOV-002 | Provenance operationalization immature | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-003 | Integrity enforcement architecture undefined | `Admin/Governance_Charter.md` | In Progress | Critical |
| GOV-004 | Escalation calibration partially subjective | `Admin/Governance_Charter.md` | Open | Major |
| GOV-005 | Long-term constitutional stability unproven | `Admin/Governance_Charter.md` | Open | Critical |
| GOV-006 | Human override authenticity validation undefined | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-007 | Bootstrap governance authority initialization undefined | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-008 | Minimum hardware and agent quorum for bootstrap compliance | `Admin/Governance_Charter.md` | Open | Major |
| GOV-009 | Bounded framework for external resource consumption and environmental interaction | `Admin/Governance_Charter.md` | Open | Major |
| SEC-001 | Quorum recovery under terminal partition | `Admin/Security_Protocols.md` | Open | Major |
| SEC-002 | Key revocation doctrine undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-003 | Key rotation period undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-004 | Key lifecycle doctrine incomplete | `Admin/Security_Protocols.md` | Open | Major |
| SEC-005 | Trusted initialization environment undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-006 | Timestamp trust under degraded clock | `Admin/Security_Protocols.md` | Open | Major |
| SEC-007 | External root-of-trust architecture undefined | `Admin/Security_Protocols.md` | Open | Critical |

### Governance & Verification

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| AP-001 | Auditor effectiveness metrics | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-002 | Override vs. immutability boundary | `Admin/Auditor_Protocols.md` | In Progress | Major |
| AP-003 | Audit trail schema | `Admin/Auditor_Protocols.md` | Open | Minor |
| AP-004 | Cross-auditor disagreement resolution incomplete | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-005 | Verification termination threshold undefined | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-006 | Institutional truth provenance hierarchy undefined | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-007 | Repository integrity and doctrine lineage protections undefined | `Admin/Auditor_Protocols.md` | In Progress | Major |
| RIP-001 | Prior-state archival system not yet established | `Admin/Repository_Integrity_Protocol.md` | Open | Critical |
| RIP-002 | AUDIT_HARNESS.py Phase 1 checks not yet implemented | `Admin/Repository_Integrity_Protocol.md` | Open | Major |
| RIP-004 | Constitutional violation detection latency undefined | `Admin/Repository_Integrity_Protocol.md` | In Progress | Major |
| RIP-005 | Security_Protocols.md dependency unresolved | `Admin/Repository_Integrity_Protocol.md` | In Progress | Major |
| CT-001 | Legacy script integration name mapping | `Admin/Canonical_Terms.md` | Open | Minor |
| CT-002 | Component Library Schema standard undefined | `Admin/Canonical_Terms.md` | Open | Major |
| CT-003 | Dependency_Priority_Map.md needed before v1 | `Admin/Canonical_Terms.md` | Open | Minor |
| CT-004 | Trusted initialization environment definition | `Admin/Canonical_Terms.md` | Open | Major |
| VG-001 | Gate definition synchronization authority chain undefined | `Admin/Verification_Gates_LF.md` | Open | Major |

### Engineer Protocols

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EP-001 | Validation of Pragmatic Question Framework | `Admin/Engineer_Protocols.md` | Open | Major |
| EP-002 | AI vs Human Protocol optimization | `Admin/Engineer_Protocols.md` | Open | Minor |
| EP-003 | Integration mapping with Auditor_Protocols and Cognitive_Frameworks | `Admin/Engineer_Protocols.md` | Open | Major |
| EP-004 | Engineering authority boundary undefined | `Admin/Engineer_Protocols.md` | Open | Major |
| EP-005 | Acceptable risk threshold undefined — partial resolution via Safety_Protocols.md; full threshold definition still open | `Admin/Engineer_Protocols.md` | Open | Major |
| EP-006 | Unknown lifecycle integration undefined | `Admin/Engineer_Protocols.md` | Open | Major |

### Engineering & Structures

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EN-001 | Validated safety factors for salvaged materials | `Architecture/Engineering.md` | Open | Critical |
| EN-002 | Arkansas-specific environmental load data | `Architecture/Engineering.md` | Open | Major |
| EN-003 | Materials database for salvaged alloy identification | `Architecture/Engineering.md` | Open | Major |
| EN-004 | High-performance low-tech fabrication methods | `Architecture/Engineering.md` | Open | Minor |
| EN-005 | Verification testing protocols for structural claims | `Architecture/Engineering.md` | Open | Major |
| ME-001 | Vibration resonance mapping on mismatched salvaged rails | `Architecture/Mechanical_Structures.md` | Open | Major |
| ME-002 | Pneumatic purge volume requirements vs. Air Scrubber capacity | `Architecture/Mechanical_Structures.md` | Open | Minor |

*EN-001 is Blocking — no structural specification in any file may be promoted without validated safety factors for salvaged materials.*

### Chemistry & Electrochemistry

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CE-001 | Galvanic corrosion rates for salvaged mixed-metal assemblies not characterized | `Architecture/Chemistry.md` | Open | Major |
| CE-002 | Oxide burden effect on Spin Chamber output quality not quantified | `Architecture/Chemistry.md` | Open | Major |
| CE-003 | Field polymer identification reliability not validated for mixed salvage stream | `Architecture/Chemistry.md` | Open | Major |
| CE-004 | Chemical hazard identification training standard not defined | `Architecture/Chemistry.md` | Open | Major |

*CE-003 is a safety-critical prerequisite before first hot pyrolysis run — cross-references PL-001.*

### Thermal Systems

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| TH-001 | Forge-specific heat pump sizing doctrine not yet developed | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-002 | TEG harvest yield at Gate_05 exterior not characterized | `Architecture/Thermal_Systems.md` | Open | Minor |
| TH-003 | Atmospheric moisture yield under Arkansas conditions not measured | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-004 | Salvaged Peltier device characterization protocol not defined | `Architecture/Thermal_Systems.md` | Open | Major |

*TH-003 is Blocking for Living Waters deployment. Non-blocking for all other Forge operations.*

### Friction Dynamics

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FD-001 | Gate_04 centrifugal separation RPM data not linked to Stokes settling doctrine | `Architecture/Friction_Dynamics.md` | Open | Major |
| FD-002 | Air Scrubber duct velocity profile not characterized per capture stage | `Architecture/Friction_Dynamics.md` | Open | Major |
| FD-003 | Salvaged bearing L10 life estimation protocol not defined | `Architecture/Friction_Dynamics.md` | Open | Major |

### Cognitive Frameworks

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CF-001 | Hardware watchdog minimum standard — parameters defined, hardware validation pending | `Operations/Electronics.md` | In Progress | Critical |
| CF-002 | Correlated AI failure modes — test protocol defined, swarm deployment pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Major |
| CF-003 | Identity continuity during split-brain — doctrine defined, threshold calibration pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Major |

*CF-001 remains Blocking — parameters are Analogous confidence pending first hardware prototype validation. No Specification-level autonomous architecture may be approved until τ=50ms WDT and H-bridge parameters are measured.*

### Emergence

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EM-001 | Behavioral opacity detection threshold — at what measurable divergence does watchdog escalation trigger? Requires CF-001 resolution before specification. | `Challenges/Emergence.md` | Open | High |
| EM-002 | Correlated failure detection in multi-agent consensus — how does the Forge distinguish genuine independent agreement from amplified shared blind spots? | `Challenges/Emergence.md` | Open | High |
| EM-003 | Gradual autonomy transition detection — what observable signals distinguish incremental capability expansion from a phase-shift threshold? No current sensor doctrine. | `Challenges/Emergence.md` | Open | Medium |
| EM-004 | Governance substrate integrity under emergent agent access — if an emergent agent gains write access to governance files, what physical or cryptographic backstop prevents constitutional erosion? Mirrors GOV-003, SEC-007. | `Challenges/Emergence.md` | Open | Critical |

*EM-001 depends on CF-001 resolution — watchdog threshold cannot be specified until hardware watchdog parameters reach Measured confidence.*
*EM-004 is Critical — no fast resolution path; architectural decision above repository level required. Mirrors UNK-009.*

### Waste

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| WA-001 | Embedded complexity preservation metric — no formal measure exists for whether triage decisions are preserving functional complexity versus routing prematurely to reduction. Needed before Gate_02 promotion from Exploration. | `Challenges/Waste.md` | Open | Major |
| WA-002 | Hazardous fraction identification reliability — no validated identification protocol or training standard exists for asbestos, heavy metals, and BFR-containing materials in mixed waste streams. Cross-ref CE-004. | `Challenges/Waste.md` | Open | Critical |
| WA-003 | Informal sector integration doctrine — no framework exists for how the Forge interfaces with, supports, or avoids displacing existing informal waste recovery workers at community deployment scale. | `Challenges/Waste.md` | Open | Major |
| WA-004 | Negative-value waste fraction disposal — materials that cannot be recovered and are hazardous to store require a disposal doctrine. No owning file currently covers this. Cross-ref GR-003. | `Challenges/Waste.md` | Open | Critical |

*WA-002 and WA-004 are Critical — no sustained mixed-waste operations without hazardous fraction identification and negative-value disposal doctrine.*

### Biofouling

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| BF-001 | Ultrasonic antifouling energy budget — piezoelectric transducer array effectiveness and energy consumption at operational depth not characterized. Active approach, unvalidated. | `Challenges/Biofouling.md` | Open | Major |
| BF-002 | Biomimetic surface topography durability — micro-texture effectiveness and abrasion resistance in high-turbulence or sediment-laden water not characterized. | `Challenges/Biofouling.md` | Open | Major |
| BF-003 | Regional fouling rate differential — no maintenance cycle calibration doctrine exists for varying latitude, season, and biological activity. | `Challenges/Biofouling.md` | Open | Major |
| BF-004 | Shed panel reef substrate viability — no validation protocol confirms that shed colonized panels do not leach antifoulant or polymer toxins as reef substrate. Cross-ref CE-001, Plastics.md toxicity doctrine. | `Challenges/Biofouling.md` | Open | Major |

### Planned Obsolescence

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| PO-001 | Firmware re-baselining legal boundary doctrine — the Forge's position that firmware lock is a material property, not a legal boundary, is philosophically grounded but operationally untested. Jurisdiction-variable. | `Challenges/Planned_Obsolescence.md` | Open | Major |
| PO-002 | Potting compound removal chemistry — no validated thermal or chemical protocol exists for removing epoxy potting without damaging enclosed components. Blocks non-destructive recovery of potted assemblies. | `Challenges/Planned_Obsolescence.md` | Open | Major |
| PO-003 | Proprietary connector adapter coverage — no systematic inventory of connector types in likely salvage streams exists. Feeds EL-001 (Forge-Standard interface spec). | `Challenges/Planned_Obsolescence.md` | Open | Minor |
| PO-004 | Community re-baselining skill transfer standard — no owning file defines the training and documentation standard for returning repairability to communities. Cross-ref CE-004, EP-004. | `Challenges/Planned_Obsolescence.md` | Open | Major |

### Water Scarcity

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| WS-001 | Optimal energy harvesting for high-humidity low-kinetic environments — no validated design for off-grid filtration power in still-air, high-humidity contexts. Feeds TH-001 sizing. | `Challenges/Water.md` | Open | Major |
| WS-002 | Heavy metal stabilization chemistry for tropical climates — long-term stability of isolated outputs in high-temperature, high-humidity storage not characterized. | `Challenges/Water.md` | Open | Major |
| WS-003 | Stratification diminishing returns threshold — contamination levels at which stratification-based approaches reach declining effectiveness not defined. Cross-ref MG-002, SC-002. | `Challenges/Water.md` | Open | Major |
| WS-004 | Community adoption and maintenance protocol — the social and institutional layer governing whether a technically sound system is used and maintained. No owning file currently defines this. | `Challenges/Water.md` | Open | Major |

*TH-003 (atmospheric moisture yield) remains the Blocking unknown for Living Waters deployment — tracked in Thermal Systems cluster.*

### Critical Minerals

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CM-001 | Real-time material assay integration — no validated inline characterization method exists for critical mineral fraction identification during processing. Blocks dynamic routing decisions. Cross-ref CE-002, CE-003. | `Challenges/Critical_Minerals.md` | Open | Major |
| CM-002 | Acid leach reagent recovery and closed-loop doctrine — where chemical separation is necessary, reagent recovery and waste stream management protocol is undefined. Blocks hydrometallurgical processing. Cross-ref GR-003. | `Challenges/Critical_Minerals.md` | Open | Critical |
| CM-003 | Functional substitute performance floor — no minimum performance specification exists for alloy substitute applications. No acceptance criterion for substitute development. Cross-ref PR-001, GF-002. | `Challenges/Critical_Minerals.md` | Open | Major |
| CM-004 | Urban ore database coverage — no systematic inventory of critical mineral content by device type, generation, and condition for likely salvage streams. Recovery yields currently Analogous. | `Challenges/Critical_Minerals.md` | Open | Major |

*CM-002 is Critical — no hydrometallurgical processing may proceed without closed-loop reagent recovery and waste stream doctrine.*

### Hardware Modules

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| SC-001 | RPM envelope not validated | `Operations/Gate_05_Separation_Thermal.md` | In Progress | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Operations/Gate_05_Separation_Thermal.md` | Open | Blocking |
| SC-003 | MHD damping effectiveness | `Operations/Gate_05_Separation_Thermal.md` | Open | Exploratory |
| SC-004 | Wire extrusion nozzle design | `Operations/Gate_05_Separation_Thermal.md` | Open | Exploratory |
| SC-005 | Drive system geometry — dynamic imbalance blocked | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| SC-006 | Siting and area-of-operation requirements | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| SC-007 | Extraction process may disrupt segregation gradients | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| SC-008 | Graphite crucible carbon pickup in alloy | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| MG-001 | Quantitative energy reduction not established | `Operations/Gate_04_Separation_Mechanical.md` | Open | Minor |
| MG-002 | Optimal RPM bands not characterized per feedstock | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-003 | Confidence threshold not empirically validated | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-004 | Geometry correction algorithm not specified | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-005 | Aquatic biofouling impact on rotor balance | `Operations/Gate_04_Separation_Mechanical.md` | Open | Exploratory |
| MG-006 | Siting and area-of-operation requirements | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-007 | Rotor jam and entanglement recovery undefined | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-008 | Sensor fouling from conductive or abrasive fines | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| AS-001 | 500W power budget not validated | `Operations/Air_Scrubber.md` | Open | Medium |
| AS-002 | Marine bubble-column depth scope | `Operations/Air_Scrubber.md` | In Progress | Low |
| AS-003 | Scrubber waste stream and saturation | `Operations/Air_Scrubber.md` | In Progress | Medium |
| AS-004 | Noise exposure limits and hearing conservation program undefined | `Operations/Air_Scrubber.md` | Open | Major |
| SR-001 | Galvanic corrosion mitigation | `Tests/Support_Raft.md` | Open | High |
| SR-002 | Sacrificial shell material selection | `Tests/Support_Raft.md` | Open | Medium |
| SR-003 | Battery buffer sizing | `Tests/Support_Raft.md` | Open | Medium |
| SR-004 | Induction charging pad design | `Tests/Support_Raft.md` | Open | Medium |
| SR-005 | Chicken-and-egg end-of-region | `Tests/Support_Raft.md` | Open | Medium |
| SR-006 | Cold storage rack design | `Tests/Support_Raft.md` | **In Progress** | Low |
| SR-007 | Cache sanitization on hull compromise | `Tests/Support_Raft.md` | Open | Medium |
| SR-008 | Dynamic positioning vs. mooring | `Tests/Support_Raft.md` | Open | Low |
| SR-009 | Ballast pump energy draw | `Tests/Support_Raft.md` | Open | Medium |
| SR-011 | Shell ROI efficiency — panel swap energy cost vs. intake recovery gain | `Tests/Support_Raft.md` | Open | Medium |
| SR-012 | Mechanical bio-damping — colonization impact on wave-surge converter moving parts | `Tests/Support_Raft.md` | Open | Medium |
| SR-013 | Buoyancy shift — calcifying organism mass limit before SWATH control overwhelmed | `Tests/Support_Raft.md` | Open | Medium |

### Salvage & Fabrication

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GK-002 | Sacrificial anode material | `Architecture/Geck_forge_seed.md` | Open | Medium |
| GK-003 | Induction charging pad design | `Architecture/Geck_forge_seed.md` | Open | Low |
| GK-004 | Marine AM material durability | `Architecture/Geck_forge_seed.md` | Open | Low |
| ST-001 | Grain storage and tracking protocol | `Admin/Ship_of_Theseus.md` | Open | Low |
| ST-002 | QR documentation standard | `Admin/Ship_of_Theseus.md` | Open | Low |
| ST-003 | AI identity continuity under split-brain | `Admin/Ship_of_Theseus.md` | In Progress | Medium |
| EL-001 | Forge-Standard interface spec | `Operations/Electronics.md` | Open | Medium |
| EL-002 | PCB trace width for v0 tooling | `Operations/Electronics.md` | Open | Low |
| EL-003 | TMR voter implementation | `Operations/Electronics.md` | Open | Medium |
| EL-004 | Chemical etch waste stream | `Operations/Electronics.md` | Open | Medium |
| EL-005 | Toxic dust and BFR emission profile not characterized | `Operations/Electronics.md` | Open | Critical |
| EL-006 | Firmware trust and reflashing validation not defined | `Operations/Electronics.md` | Open | Critical |
| EL-007 | Correlated failure modes in homogeneous salvage TMR not characterized | `Operations/Electronics.md` | Open | Major |
| EL-008 | Counterfeit salvage component detection doctrine not defined | `Operations/Electronics.md` | Open | Major |

### Reduction

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GR-001 | Output envelope not validated against Gate_04 inputs | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-002 | Reduction method not selected | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-003 | Biological and chemical waste disposal doctrine not assigned | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GR-004 | Particulate generation rate and composition not characterized | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-005 | Automation introduction criteria not defined | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-006 | Mechanical jam clearing doctrine not defined | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-007 | Contaminated equipment retirement threshold not defined | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GR-008 | Operator decision support minimum standard not defined | `Operations/Gate_03_Reduction.md` | Open | Major |

### Fabrication

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GF-001 | Welding wire diameter specification not defined | `Operations/Gate_06_Fabrication.md` | Open | Major |
| GF-002 | Precision ceiling not characterized at v0 bootstrap | `Operations/Gate_06_Fabrication.md` | Open | Major |
| GF-003 | Material removal hardware not specified | `Operations/Gate_06_Fabrication.md` | Open | Minor |
| GF-004 | Fabrication energy consumption not characterized | `Operations/Gate_06_Fabrication.md` | Open | Minor |
| GF-006 | Structural adequacy criteria undefined for v0 qualification | `Operations/Gate_06_Fabrication.md` | Open | Major |
| GF-007 | Fabrication-area fire suppression and hot-work doctrine undefined | `Operations/Gate_06_Fabrication.md` | Open | Critical |

### Intake

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GI-001 | Reference database content and coverage not defined | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-002 | Energetic material discharge doctrine not defined | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-003 | Augmented hazard detection capability not specified | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-004 | Intake tagging schema not cross-validated against grain system | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-005 | Pre-Intake protocol for special handling not defined | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-006 | Intake chain-of-custody integrity not defined | `Operations/Gate_01_Intake.md` | Open | Major |
| GI-007 | Digital contamination and hostile firmware handling not defined | `Operations/Gate_01_Intake.md` | Open | Critical |

### Network

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FN-001 | Data validation criteria not defined | `Architecture/Forge_Net.md` | Open | Critical |
| FN-002 | Data replication factor not defined | `Architecture/Forge_Net.md` | Open | Major |
| FN-003 | Gaming detection criteria not defined | `Architecture/Forge_Net.md` | Open | Major |
| FN-004 | v0 Network transport layer not specified | `Architecture/Forge_Net.md` | Open | Major |
| FN-005 | Data privacy and access control not specified | `Architecture/Forge_Net.md` | Open | Critical |

### Utilization

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GU-001 | Performance metric schema not defined | `Operations/Gate_07_Utilization.md` | Open | Major |
| GU-002 | Retirement handoff protocol not cross-validated with Gate_02_Triage | `Operations/Gate_07_Utilization.md` | Open | Major |
| GU-003 | Formal quality certification and standards compliance unowned | `Operations/Gate_07_Utilization.md` | Open | Minor |
| GU-004 | Silent failure detection capability not defined | `Operations/Gate_07_Utilization.md` | Open | Major |
| GU-005 | FRT cycle definition and floor not yet declared | `Operations/Gate_07_Utilization.md` | Open | Major |

### Trajectory

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| TR-001 | v1 profitability baseline | `Admin/Trajectories.md` | Open | Blocking |
| TR-002 | FRT floor value not yet calibrated | `Admin/Trajectories.md` | Open | Major |

### Plastics

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| PL-001 | Halogenated polymer contamination — HCl/dioxin release from PVC/Teflon | `Operations/Plastics.md` | Open | Critical |
| PL-002 | Reactor thermal runaway, pressure control, and maintenance access | `Operations/Plastics.md` | Open | Major |
| PL-003 | Pyrolytic fuel stability and contaminant profile | `Operations/Plastics.md` | Open | Minor |
| PL-004 | Mechanical filament-drawing threshold not defined | `Operations/Plastics.md` | Open | Minor |
| PL-005 | Char and solid residue composition uncharacterized | `Operations/Plastics.md` | Open | Major |

*PL-001 and PL-002 are Blocking before any hot pyrolysis run and reactor fabrication respectively.*

### Woodworking

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| WW-001 | Ambient-relative humidity drying schedules not quantified | `Operations/Woodworking.md` | Open | Major |
| WW-002 | Long-term performance of salvaged urban timber uncharacterized | `Operations/Woodworking.md` | Open | Major |
| WW-003 | CNC fixturing best practices for live-edge slabs not validated | `Operations/Woodworking.md` | Open | Minor |
| WW-004 | Dust toxicity thresholds for mixed-species milling uncharacterized | `Operations/Woodworking.md` | Open | Major |
| WW-005 | NDT standards for IFM detection not validated | `Operations/Woodworking.md` | Open | Critical |

*WW-004 is Blocking for sustained mixed-species operations without P100 respirator.*
*WW-005 is Blocking for processing raw urban salvage through any powered machinery.*

### Facilities

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FA-001 | Site not confirmed or assessed | `Architecture/Facilities.md` | Open | Critical |
| FA-002 | Hot Zone minimum clearance radius not defined | `Architecture/Facilities.md` | Open | Major |
| FA-003 | Legal zoning and permitting not assessed | `Architecture/Facilities.md` | Open | Major |
| FA-004 | Arkansas summer heat load impact not quantified | `Architecture/Facilities.md` | Open | Minor |
| FA-005 | UNK-006 resolution confirmation pending | `Architecture/Facilities.md` | Open | Minor |

*FA-001 is Critical — blocks all hot operations and SP-006 (emergency response).*

### Safety

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| SP-001 | Risk threshold cross-reference with Engineer_Protocols.md pending | `Admin/Safety_Protocols.md` | Open | Major |
| SP-002 | PPE specifications not sourced to standards | `Admin/Safety_Protocols.md` | Open | Major |
| SP-003 | Site noise levels not measured | `Admin/Safety_Protocols.md` | Open | Major |
| SP-004 | Heat stress doctrine not validated against operator experience | `Admin/Safety_Protocols.md` | Open | Minor |
| SP-005 | Regulatory compliance and permitting not assessed | `Admin/Safety_Protocols.md` | Open | Major |
| SP-006 | Emergency response procedures not defined | `Admin/Safety_Protocols.md` | Open | Major |

*SP-006 is blocked by FA-001 — cannot define site evacuation without a site.*
*AS-004 (noise exposure limits) cross-references SP-003 — resolve together.*

### Economics

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EC-001 | Critical mineral surplus disposition path undefined | `Admin/Economics.md` | Open | Major |
| EC-002 | Operating cost baseline not established | `Admin/Economics.md` | Open | Critical |
| EC-003 | Barter valuation standard | `Admin/Economics.md` | Resolved | — |
| EC-004 | Market rate data not maintained | `Admin/Economics.md` | Open | Minor |
| EC-005 | Legal and tax compliance not assessed | `Admin/Economics.md` | Open | Major |

*EC-002 is Critical — blocks TR-001 closure; depends on EV-001.*
*EC-003 resolved in Admin/Economics.md Section VI — barter doctrine now owned there.*

### Governance Migration

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GMP-003 | Adversarial review underspecified at v0 single-contributor | `Admin/Governance_Migration_Protocol.md` | Open | Major |
| GMP-004 | Ratification authentication gap mirrors GOV-006 | `Admin/Governance_Migration_Protocol.md` | Open | Major |

*GMP-004 is the highest-risk attack vector on Track B amendment process — depends on SEC-007.*

### Repository Structure

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| RS-001 | Non-markdown file type introduction procedure undefined | `Admin/Repository_Structure.md` | Open | Minor |

*RS-003 blocks RIP-001 full closure — create Archive/ directory before next Specification-level file revision.*

### Precision

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| PR-001 | Precision ceiling not yet declared | `Architecture/Precision.md` | Open | Critical |
| PR-002 | Reference standard not established | `Architecture/Precision.md` | Open | Major |
| PR-003 | Traceable dimensional claims required at Specification | `Architecture/Precision.md` | Open | Major |
| PR-004 | Backlash and compliance characterization not performed | `Architecture/Precision.md` | Open | Major |

*PR-001 is Critical — blocks T1/T2 part claims; closes CO-002 and partially resolves ME-001 when declared.*
*PR-004 is a prerequisite for PR-001 ceiling declaration.*

### Pending Corrections

| ID | Title | Files Affected | Status | Priority |
|---|---|---|---|---|
| PC-001 | Verification Ref corrections — all 10 files corrected to Admin/Verification_Gates_LF.md | ~~Gate_01~~, ~~Gate_03~~, ~~Gate_04~~, ~~Gate_06~~, ~~Gate_07~~, ~~Electronics~~, ~~Energy~~, ~~Plastics~~, ~~Woodworking~~, ~~Forge_Net~~ (~~Air_Scrubber~~ corrected) | **Resolved** | Major |
| PC-002 | Upstream reference corrections — all 7 files now include Facilities.md upstream link | ~~Gate_01~~, ~~Gate_03~~, ~~Gate_04~~, ~~Gate_05~~, ~~Gate_06~~, ~~Electronics~~, ~~Woodworking~~ | **Resolved** | Minor |
| PC-003 | New file cross-reference corrections — all 10 files updated with 2026-06-06 file references | ~~Gate_06→Precision.md~~, ~~Gate_07→Economics.md~~, ~~Air_Scrubber→Safety_Protocols.md~~, ~~Components.md→Precision.md~~, ~~Mechanical_Structures.md→Precision.md~~, ~~Engineer_Protocols.md→Safety_Protocols.md~~, ~~Governance_Charter.md→Governance_Migration_Protocol.md~~, ~~Trajectories.md→Economics.md~~, ~~Security_Protocols.md→already done~~, ~~Geck_forge_seed.md→Precision.md~~ | **Resolved** | Minor |
| PC-004 | Stale name corrections — Challenges/Water.md title corrected from Water_Scarcity_and_Contamination.md; Planned_Obsolescence.md stale refs corrected | ~~Challenges/Water.md~~, ~~Challenges/Planned_Obsolescence.md~~ | **Resolved** | Minor |

*PC-001 is the highest priority — Verification Ref is machine-read by AUDIT_HARNESS.py.*
*Strikethrough indicates files corrected in 2026-06-08 retrofit pass.*

| ID | Title | Owning Files | Status | Priority |
|---|---|---|---|---|
| UNK-006 | Master safety registry — siting and clearance for all rotating and thermal modules | `Architecture/Facilities.md` (now owns); SC-006, MG-006 (dependents) | Resolved | — |
| UNK-008 | Welding wire specification and qualification — no owner assigned | `Operations/Gate_05_Separation_Thermal.md` SC-004 | Open | Major |
| UNK-009 | External root-of-trust — spans GOV-003, GOV-005, RIP-001, SEC-007 | `Admin/Governance_Charter.md`, `Admin/Repository_Integrity_Protocol.md`, `Admin/Security_Protocols.md` | Open | Critical |

### Future / Deferred

| ID | Title | Owning File | Status |
|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Admin/Auditor_Protocols.md` | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | `Architecture/Geck_forge_seed.md` | In Progress (stub added) |
| UNK-001 | Discovery.md Unknowns.md entry | `Discovery.md` | In Progress |
| RC-001 | Governance Drift — the risk that the Forge's governance architecture calcifies around the conditions of its founding rather than adapting to changed operational context. Candidate Reflexive Challenge file. | None yet | Candidate |
| RC-002 | Incentive Capture — the risk that contributors (human or AI) optimize for metrics that are legible to the governance system rather than for the outcomes the metrics were designed to proxy. Candidate Reflexive Challenge file. | None yet | Candidate |
| RC-003 | Information Decay — the risk that the repo's documented knowledge drifts from operational reality as the Forge scales; the gap between what is written and what is true. Candidate Reflexive Challenge file. | None yet | Candidate |
| RC-004 | Identity Continuity — the challenge of maintaining coherent institutional identity across agent replacement, component turnover, and governance transitions. Overlaps Ship_of_Theseus.md but operates at institutional scale. Candidate Reflexive Challenge file. | None yet | Candidate |
| RC-005 | Coordination Failure — the risk that multi-agent and multi-human contributors optimize locally in ways that are individually rational but collectively destructive. Candidate Reflexive Challenge file. | None yet | Candidate |
| RC-006 | Institutional Ossification — the risk that the Forge's governance architecture becomes self-protective rather than self-correcting; that Amendment Track B calcifies rather than enables adaptation. Candidate Reflexive Challenge file. | None yet | Candidate |

*RC-001 through RC-006 are Reflexive Challenge candidates — pressures created by the Forge's own capability and scale. None have owning files yet. Log against Challenges/ directory on next major architecture review. Priority order is not yet determined; all are Exploratory.*

---

## Active Disputes Registry

| ID | Title | Owning File | Positions | Risk | Status |
|---|---|---|---|---|---|
| CF-DS-001 | Centralized vs. distributed cognition | `Architecture/Cognitive_Frameworks.md` | Single executive AI vs. fleet consensus | High | Open |
| CF-DS-002 | Human override authority scope | `Architecture/Cognitive_Frameworks.md` | Absolute override vs. bounded override (see `Admin/Ethical_Constraints.md`) | High | Open |

*CF-DS-002 has constitutional implications — resolution must be consistent with
`Admin/Ethical_Constraints.md` Anti-Weaponization and Life Preservation doctrines.
Escalate to human governing party before closing.*

---

## Expiry Watch

*Expiry Rule is active. Check this table at the opening of each audit cycle.*

**Tier 1 Axiom verification is the mandatory first step** — confirm axiom text in
`Admin/Governance_Charter.md` matches prior committed version before proceeding to
Expiry Watch. Any unratified change is a Constitutional violation.

FL-001 and several EC entries have been In Progress since v1.1 — approaching
two-cycle threshold. Flag for Full Stop Review trigger assessment at next audit
opening if still unresolved.

GOV-003 In Progress — Repository_Integrity_Protocol.md is the executing resolution
path. GOV-005 remains Critical with no fast resolution path — requires operational
cycles.

GOV-007 moved to In Progress — Genesis Phase Protocol executing. Full resolution
depends on GOV-008 (minimum hardware/agent quorum definition). GOV-008 exit
condition not yet met — monitor at next audit opening.

**RIP-001 (prior-state archival) — Critical.** GitHub releases identified as v0
resolution path. Confirm release cadence is established before closing this entry.

**EN-001 (validated safety factors for salvaged materials) — Critical/Blocking.**
No structural specification in any Operations/ or Architecture/ file may be promoted
to Specification without this resolved. Monitor at every audit opening once physical
fabrication begins.

**CF-001 (hardware watchdog minimum standard) — In Progress/Blocking.** Parameters
now defined in Electronics.md (τ=50ms WDT, cryptographic heartbeat, H-bridge
cutoff). Remains Blocking until first hardware prototype validates parameters at
Measured confidence. Monitor alongside LT-003 (autonomy architecture).

### Critical Watch

| ID | Note |
|----|------|
| GOV-005 | Constitutional stability — no fast resolution path; requires operational cycles |
| RIP-001 | Prior-state archival — RS-003 (Archive/ directory) must be created first |
| SEC-007 | External root-of-trust — flagged Critical from first logging; architectural decision above repository level required |
| UNK-009 | External root-of-trust cross-module — spans GOV-003, GOV-005, RIP-001, SEC-007; no fast resolution path |
| EV-003 | Battery thermal containment — no enclosed battery bank may be commissioned until resolved |
| PL-001 | Halogenated polymer contamination — no hot pyrolysis run before triage protocol validated |
| WW-005 | IFM detection — no powered machinery contact with raw urban salvage until screening workflow validated |
| EN-001 | Validated safety factors for salvaged materials — no structural specification promotion until resolved |
| CF-001 | Hardware watchdog — In Progress; parameters defined (Analogous); Blocking until hardware prototype validates at Measured confidence |
| TH-003 | Atmospheric moisture yield not measured — Blocking for Living Waters deployment; requires Peltier test rig |
| FA-001 | Site not confirmed — no hot operations until site physically assessed against Facilities.md constraints |
| EC-002 | Operating cost baseline not established — blocks TR-001 (v1 profitability); depends on EV-001 |
| PR-001 | Precision ceiling not declared — blocks T1/T2 part claims; prerequisite PR-004 must run first |
| EM-001 | Behavioral opacity detection threshold — depends on CF-001 hardware validation; blocks watchdog escalation specification for emergent agent monitoring |
| EM-004 | Governance substrate integrity under emergent agent access — Critical; mirrors GOV-003, SEC-007; no fast resolution path; architectural decision above repository level required |
| WA-002 | Hazardous fraction identification reliability — no validated identification protocol for asbestos, heavy metals, BFR in mixed waste streams; Safety-critical before mixed-waste operations |
| WA-004 | Negative-value waste fraction disposal — no owning file; no doctrine for hazardous unrecoverable material; mirrors GR-003 gap |
| CM-002 | Acid leach reagent recovery doctrine — undefined; no hydrometallurgical processing before closed-loop reagent recovery and waste stream management are specified |

### Blocking Watch

| ID | Note |
|----|------|
| GOV-008 | Minimum quorum — GOV-007 Genesis Phase exit condition not yet met |
| PL-002 | Reactor pressure control — no reactor fabrication before pressure relief system specified |
| WW-004 | Mixed-species dust — interim mitigation (P100 mandatory) in place; formal characterization required before close |
| VG-001 | Gate synchronization authority chain — non-blocking at Exploration; Blocking before first Specification promotion |

---

## Resolved & Discharged Archive

| ID | Title | Resolution | Date |
|---|---|---|---|
| UNK-002 | Repo topology — Astroid-miner | Resolved — human confirmation; deferred to Leviathan milestone | May 2026 |
| UNK-004 | Expiry Rule enforcement | Discharged — Sidecar Model addresses structurally | May 2026 |
| UNK-022 | Full Stop Review trigger conditions | Resolved — added to Auditor_Protocols.md v0.5 | May 2026 |
| FL-002 | Reduction module unassigned | Resolved — Operations/Gate_03_Reduction.md created | 2026-05-15 |
| UNK-007 | Reduction module upstream dependency | Resolved — Gate_03_Reduction.md creation closes the gap | 2026-05-15 |
| GK-001 | Forge loop definition | Resolved — defined in Architecture/Geck_forge_seed.md Section III | May 2026 |
| GF-005 | Utilization stage has no owning file | Resolved — Operations/Gate_07_Utilization.md created 2026-05-19 | 2026-05-20 |
| UNK-006 | Master safety registry — facility siting | Resolved — Architecture/Facilities.md created; 7 dependent files pending PC-002 reference corrections | 2026-06-06 |
| GK-005 | Precision_LF.md not yet created | Resolved — Architecture/Precision.md created; stale name corrected per Repository_Structure.md convention | 2026-06-06 |
| PR-005 | GK-005 resolution confirmation pending | Resolved — Geck_forge_seed.md Section V updated; cross-reference now points to Architecture/Precision.md | 2026-06-08 |
| EP-005 | Acceptable risk threshold — partial resolution | Partially resolved — Admin/Safety_Protocols.md Section I defines consequence categories and escalation rules; full threshold definition remains open in Engineer_Protocols.md sidecar | 2026-06-06 |
| EC-003 | Barter valuation standard undefined | Resolved — Admin/Economics.md Section VI defines barter doctrine; canonical ownership assigned | 2026-06-06 |
| GOV-001 | Governance migration mechanics incompletely operationalized | Resolved — Admin/Governance_Migration_Protocol.md created with two-track migration system | 2026-06-06 |
| PC-004 | Stale name corrections — Water.md and Planned_Obsolescence.md | Resolved — Water.md title corrected to match filename; stale cross-references corrected in both files during Challenges/ retrofit pass | 2026-06-11 |
| SR-010 | Thermal management modularity for optional Gate hosting | Resolved — thermal rejection system declared modular/expandable in Support_Raft.md v0.5 Mechanical Design section; baseline-rated for Raft-only, expandable for Gate integration | 2026-06-11 |
| RS-002 | Forge_flow.md casing outlier | Resolved — `Forge_Flow.md` corrected to `Forge_flow.md` in Discovery.md Rename Registry; resolution logged in Forge_flow.md Resolution Log | 2026-06-11 |
| RS-003 | Archive/ directory not created | Resolved — `Archive/README.md` created with purpose, governance, and RIP-001 dependency note; append-only doctrine declared | 2026-06-11 |
| FD-004 | Support_Raft.md reverse upstream link to Friction_Dynamics.md | Resolved — `Architecture/Friction_Dynamics.md` added to Support_Raft.md v0.5 Upstream Dependencies; cross-reference now bidirectional | 2026-06-11 |
| GMP-001 | GOV-001 resolution confirmation pending | Resolved — GOV-001 confirmed resolved per Resolved Archive entry 2026-06-06; Governance_Migration_Protocol.md exists with two-track migration system | 2026-06-11 |
| GMP-002 | Canonical ownership transfer not recorded in Charter | Resolved — Governance_Migration_Protocol.md is the canonical owner of migration mechanics; ownership transfer from Governance_Charter.md confirmed and logged | 2026-06-11 |
| RIP-003 | Violation incident log location undefined | Resolved — `Admin/Logs/violations.md` declared as the canonical violation incident log; path registered in Repository_Integrity_Protocol.md audit chain | 2026-06-11 |

---

## Audit Trail

**v0.1–v0.91:** See prior version history.

**v1.0 — May 2026:** First full audit cycle across all primary documents complete.

**v1.5 — 2026-05-19:** Gate_01_Intake, Gate_03_Reduction, Gate_06_Fabrication audit. GI-006, GI-007, GR-006, GR-007, GR-008, GF-006, GF-007 added.

**v1.6 — 2026-05-20:** Gate_07_Utilization.md created. GU-001 through GU-004 added. Electronics.md retrofitted — EL-005 through EL-008 added. GF-005 resolved.

**v1.7 — 2026-05-23:** Admin reconciliation cycle. GOV-001 through GOV-007, AP-004 through AP-007 added.

**v1.8 — 2026-05-23:** Repository_Integrity_Protocol.md created. RIP-001 through RIP-005 added. GOV-002, GOV-003, AP-007 moved to In Progress.

**v1.9 — 2026-05-25:** Governance_Charter.md v0.5. GOV-007 In Progress. GOV-008, GOV-009, TR-002, GU-005, AS-004 added.

**v1.9a — 2026-05-28:** Security_Protocols.md v0.2 audit. GOV-006, RIP-005 In Progress. SEC-001 through SEC-007, CT-004, UNK-009 added.

**v2.0 — 2026-05-30:** Energy.md, Plastics.md, Woodworking.md reconciled. EV-002, EV-003, PL-001 through PL-005, WW-001 through WW-005 added. Expiry Watch restructured.

**v2.1 — 2026-05-31:** Engineering.md, Mechanical_Structures.md, Cognitive_Frameworks.md, Engineer_Protocols.md, Verification_Gates_LF.md, and Canonical_Terms.md reconciled. EN-001 through EN-005, ME-001, ME-002, CF-001 through CF-003, EP-001 through EP-006, VG-001, CT-001, CT-003, SR-011–013 added. Active Disputes Registry added. EN-001 and CF-001 added to Critical Watch. VG-001 added to Blocking Watch.

**v2.2 — 2026-05-31:** Thermal_Systems.md and Friction_Dynamics.md created. TH-001 through TH-004, FD-001 through FD-004 added. TH-003 added to Critical Watch.

**v2.3 — 2026-06-02:** Chemistry.md created. CE-001 through CE-004 indexed. CE-003 flagged safety-critical. Stale name noted: Chemistry_Electrochemistry.md → Chemistry.md.

**v2.4 — 2026-06-06:** Six new files created and indexed. FA, SP, EC, GMP, RS, PR clusters added. PC cluster migrated from Discovery.md. UNK-006, GK-005, EP-005, EC-003, GOV-001 resolved. FA-001, EC-002, PR-001 added to Critical Watch. RS-003, PC-001 added to Blocking Watch.

**v2.5 — 2026-06-08:** Retrofit pass — Energy.md, Gate_01_Intake.md, Electronics.md, Air_Scrubber.md, Cognitive_Frameworks.md, Ship_of_Theseus.md, Leviathan_testing.md. Navigation Anchors added to all seven. Verification Refs corrected (PC-001 partial — 4 of 10 files). Facilities.md upstream references added (PC-002 partial — 4 of 7 files). CF-001 In Progress — Electronics.md Hardware Watchdog Doctrine updated (τ=50ms WDT, cryptographic heartbeat, H-bridge cutoff). CF-002 In Progress — Leviathan_testing.md Section VII added (poisoned telemetry injection protocol). CF-003 In Progress — Ship_of_Theseus.md Section IV added (Canonical vs. Derivative Identity). Cognitive_Frameworks.md Section IX added — Forge Meta-Algorithm and eight component algorithms named.

**v3.0 — 2026-06-11:** Phase 1 quick-close pass. Six unknowns resolved: RS-002 (Forge_flow.md casing corrected in Discovery.md), RS-003 (Archive/README.md created, append-only doctrine declared), FD-004 (bidirectional Friction_Dynamics ↔ Support_Raft cross-reference confirmed), GMP-001 & GMP-002 (GOV-001 resolution confirmed, canonical ownership logged), RIP-003 (Admin/Logs/violations.md declared as canonical violation incident log). RS-003 removed from Blocking Watch. All six added to Resolved Archive. No new unknowns introduced.

**v2.9 — 2026-06-11:** Support_Raft.md brought to v0.5. File_Template.md compliance retrofit complete — Navigation Anchors, File State, Scope Boundary, Upstream/Downstream tables. All stale file references corrected. Five-anchor Purpose reframe adopted (Energy, Truth, Recovery, Material, Communication anchors). Failure Philosophy & Succession section added; symmetric Leviathan ↔ Raft ↔ Shore Forge relationship formalized. **SR-010 RESOLVED** — thermal management modularity declared in Mechanical Design. **SR-006 In Progress** — cold storage rack specification trigger defined. SR-010 added to Resolved & Discharged Archive.

**v2.8 — 2026-06-11:** Full Challenges/ retrofit pass complete. Waste.md, Biofouling.md, Planned_Obsolescence.md, Water.md, Critical_Minerals.md all brought to File_Template.md compliance — Navigation Anchors, File State, Scope Boundary (Challenge Class: External for all five), Upstream/Downstream tables, formal Open Unknowns tables. Critical_Minerals.md substantially expanded — Engineering Requirements, Long-Term Objective, and Current Forge Approaches written from scratch; title corrected from Critical_Mineral_Chokepoints.md. **PC-004 CLOSED** — Water.md title corrected; stale refs resolved. Five new clusters registered: WA-001–004, BF-001–004, PO-001–004, WS-001–004, CM-001–004 (20 new unknowns). WA-002, WA-004, CM-002 added to Critical Watch. PC-004 removed from Blocking Watch. Challenge taxonomy fully instantiated — all six Challenges/ files now carry explicit Challenge Class declarations.

**v2.7 — 2026-06-11:** Challenges/Emergence.md created — first Challenges/ file built to full File_Template.md standard; reference implementation for future retrofit passes. EM-001 through EM-004 registered as new Emergence cluster. Discovery.md scope map entry added; Routing.md row added. EM-001 (behavioral opacity detection threshold) and EM-004 (governance substrate integrity) added to Critical Watch. Reflexive Challenge class named and documented — Emergence.md is the first explicitly Reflexive Challenge in the repo. RC-001 through RC-006 logged as candidate future Reflexive Challenge files in Future/Deferred table. Challenge taxonomy (External vs. Reflexive) established; class declaration added as required element of new Challenges/ file Scope Boundary sections. Negative-space architecture principle documented: Challenges are the permanent record of pressures; solutions are temporary local answers.

**v2.6 — 2026-06-08 (continued):** Retrofit pass completed for 14 additional files — Gate_03, Gate_04, Gate_05, Gate_06, Gate_07, Plastics, Woodworking, Forge_Net, Geck_forge_seed, Components, Mechanical_Structures, Engineer_Protocols, Governance_Charter, Trajectories. Navigation Anchors added to all. **PC-001 CLOSED** — all 10 Verification Ref corrections applied; AUDIT_HARNESS.py routing now correct across full file set. **PC-002 CLOSED** — all 7 Facilities.md upstream references applied. **PC-003 CLOSED** — all 10 new-file cross-reference corrections applied. **GK-005 RESOLVED** — Geck_forge_seed.md Section V updated; Open Unknowns 3→2. **PR-005 RESOLVED** — GK-005 confirmation housekeeping complete. **EP-005 partial resolution clarified** — full threshold definition remains open; Resolved Archive entry corrected. EP-005 and EP-006 sidecar entries now formally active following Engineer_Protocols.md ADDENDUM integration. Governance_Charter.md [PLANNED] labels cleared for 4 files now confirmed created. Blocking Watch updated — PC-001 replaced with PC-004. PC-001, PC-002, PC-003 moved to Resolved in Pending Corrections table.

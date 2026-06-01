# Unknowns.md — Cross-Module Unknowns Global Index
**Version 2.1 — Audit cycle 2026-05-31. Engineering.md, Mechanical_Structures.md, Cognitive_Frameworks.md, Engineer_Protocols.md, Verification_Gates_LF.md, and Canonical_Terms.md reconciled. EN-001 through EN-005, ME-001 through ME-002, CF-001 through CF-003, EP-001 through EP-006, VG-001, CT-001 and CT-003 added. SR-011 through SR-013 formally indexed. CF-DS-001 and CF-DS-002 added to Active Disputes registry. CO-002 and GK-005 confirmed present. Dependency map updated.**
**Expiry Rule active. Protocol Performance metrics collecting.**

---

## Purpose

Cross-module unknowns index. Full entry detail lives in each owning file's sidecar. This file is the navigation layer only.

Module-specific unknowns → owning file sidecar
Cross-module unknowns → listed here, full entry in owning file
Navigation unknowns → Discovery.md

---

## What v2.1 Means

- `Architecture/Engineering.md` reconciled — EN-001 through EN-005 indexed; EN-001
  (validated safety factors for salvaged materials) flagged Critical/Blocking; new
  Engineering section added
- `Architecture/Mechanical_Structures.md` reconciled — ME-001 (resonance mapping on
  mismatched salvaged rails, Medium) and ME-002 (pneumatic purge volume vs. Air Scrubber
  capacity, Low) indexed; new Mechanical Structures section added
- `Architecture/Cognitive_Frameworks.md` reconciled — CF-001 (hardware watchdog minimum
  standard, High/Blocking) and CF-002 (correlated AI failure modes, High) and CF-003
  (identity continuity during split-brain, Medium) indexed; new Cognitive Frameworks
  section added
- `Admin/Engineer_Protocols.md` reconciled — EP-001 through EP-006 indexed; new Engineer
  Protocols section added
- `Admin/Verification_Gates_LF.md` reconciled — VG-001 (gate definition synchronization
  authority chain) indexed; added to Governance & Verification section
- `Admin/Canonical_Terms.md` reconciled — CT-001 (legacy script integration name
  mapping, Minor) and CT-003 (dependency priority map needed before v1, Minor) added;
  CT-002 and CT-004 already present
- `Tests/Support_Raft.md` reconciled — SR-011 (shell ROI efficiency), SR-012 (mechanical
  bio-damping), SR-013 (buoyancy shift) formally indexed in Hardware Modules section
- Active Disputes registry added — CF-DS-001 and CF-DS-002 from Cognitive_Frameworks.md
  formally recorded
- CO-002 (metrology precision thresholds) and GK-005 (Precision_LF.md not yet created)
  confirmed present in prior version
- Dependency map updated with EN, ME, CF, EP, VG, and SR-011–013 entries

---

## Dependency Map

```
EV-001 (Operations/Energy.md) -> LT-001 (Tests/Leviathan_testing.md)
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

GOV-001 (governance migration mechanics) -> no blocking dependency; resolved by Governance_Migration_Protocol.md creation
GOV-002 (provenance operationalization) -> depends on AP-006 (truth provenance hierarchy)
GOV-003 (integrity enforcement architecture) -> In Progress — Repository_Integrity_Protocol.md created as resolution path; AP-007 (repository integrity doctrine) — distinct but linked
GOV-004 (escalation calibration) -> AP-004 (cross-auditor disagreement resolution)
GOV-005 (constitutional stability) -> discharge via Lessons Learned after stable migration cycles
GOV-006 (human override authenticity) -> depends on Security_Protocols.md (executing); interim authentication requirement now codified in Governance_Charter.md Human Override Doctrine
GOV-007 (bootstrap governance initialization) -> In Progress — Genesis Phase Protocol executing; full resolution depends on GOV-008 (minimum agent quorum definition)
GOV-008 (minimum hardware/agent quorum) -> GOV-007 exit condition; depends on Security_Protocols.md for attestation mechanism
GOV-009 (bounded resource consumption framework) -> cross-ref Tests/Leviathan_testing.md, Tests/Support_Raft.md for physical deployment constraints

AP-001 (auditor metrics) -> depends on AP-003 (audit schema)
AP-003 (audit trail schema) -> AP-001
AP-004 (cross-auditor disagreement) -> GOV-004 (escalation calibration); may merge
AP-005 (verification termination threshold) -> EC-001 (sufficient confidence threshold)
AP-006 (truth provenance hierarchy) -> FN-001 (validation criteria) / CF-002 (correlated AI failure modes)
AP-007 (repository integrity doctrine) -> FN-001 / AP-003 / Architecture/Forge_Net.md
AP-007 cross-ref GOV-003 — constitutional enforcement vs. operational auditor doctrine
RIP-001 (prior-state archival) -> blocks Phase 2 automation; GitHub releases satisfy at v0
RIP-002 (Phase 1 automation) -> depends on RIP-001 for comparison checks
RIP-004 (detection latency) -> In Progress — resolved by Forge_Audit_Kit.md Audit Opening Checklist axiom verification step
RIP-005 (Security_Protocols.md) -> GOV-006 (human override authenticity); GOV-008 (attestation mechanism); Phase 3 dependency

SEC-001 (quorum recovery) -> GOV-008 (minimum quorum definition) — blocking dependency
SEC-002 (key revocation) -> SEC-001 (partition affects propagation)
SEC-002 -> GOV-006 (override node revocation requires additional safeguards)
SEC-003 (key rotation) -> SEC-002 (rotation and revocation must be consistent)
SEC-004 (key lifecycle) -> SEC-002 / SEC-003 (all three form coherent lifecycle)
SEC-005 (trusted init environment) -> CT-004 (canonical definition required)
SEC-006 (timestamp trust) -> SEC-001 (partition is primary degraded-clock context)
SEC-007 (external root-of-trust) -> GOV-003 / GOV-005 / RIP-001 (cross-module Critical)
UNK-009 -> SEC-007 / GOV-003 / GOV-005 / RIP-001 (cross-module spanning)
CT-001 (legacy script name mapping) -> AUDIT_HARNESS.py; low risk, Minor
CT-002 (component library schema) -> Operations/Gate_02_Triage.md
CT-003 (dependency priority map) -> discharge via Admin/Trajectories.md v0->v1
CT-004 (trusted init environment) -> SEC-005 (resolution dependency)

TR-001 (v1 profitability) -> depends on EV-001
TR-002 (FRT floor calibration) -> depends on first operational cycle data; feeds TR-001

GU-005 (FRT cycle definition and floor) -> operator declaration at commissioning; feeds TR-002 and TR-001

AS-004 (noise exposure limits) -> depends on first operational SPL measurement; cross-ref planned Safety_Protocols.md

EL-001 (forge standard interface) -> depends on LT-001
EL-005 (toxic dust profile) -> feeds Air_Scrubber.md sizing and filter selection
EL-006 (firmware trust) -> prerequisite for first salvaged MCU integration
EL-007 (correlated TMR failure) -> depends on first TMR prototype
EL-008 (counterfeit detection) -> cross-reference EL-006 firmware trust

SC-001 (RPM envelope) -> SC-005 (drive system geometry)
SC-002 (segregation effectiveness) — primary Gen-0 validation target
SC-006 (siting) -> UNK-006 (master safety registry)
MG-006 (siting) -> UNK-006 (master safety registry)
UNK-007 (reduction module) -> Resolved
UNK-008 (welding wire) -> SC-004
FN-001 (validation criteria) -> blocks first network connection
FN-005 (privacy doctrine) -> blocks first network connection
FN-002 (replication factor) -> depends on LT-002 (node loss rate)
FN-003 (gaming detection) -> must deploy with FN positive reinforcement
FN-004 (transport layer) -> informs FN-002 sync doctrine
GI-002 (energetic discharge) -> blocks first operational Intake run
GI-003 (augmented detection) -> blocks first unsupervised Intake run
GI-001 (reference database) -> informs GI-003 detection protocol
GI-004 (tagging schema) -> depends on Admin/Ship_of_Theseus.md grain system
GI-005 (pre-Intake protocol) -> depends on GI-002 energetic doctrine
GI-006 (chain of custody) -> depends on GI-004 tagging schema
GI-007 (digital contamination) -> depends on Architecture/Forge_Net.md FN-001, Operations/Electronics.md
GR-002 (method selection) -> unblocks GR-001, GR-004, GR-005, GR-006
GR-003 (waste disposal) -> no owner in repository — Critical gap
GR-001 (output envelope) -> depends on GR-002, feeds MG inputs
GR-004 (particulate) -> depends on GR-002, feeds Air_Scrubber sizing
GR-005 (automation criteria) -> depends on FL-001, GI-002, GI-003, GR-001, GR-004
GR-006 (jam clearing) -> depends on GR-002 method selection
GR-007 (equipment retirement) -> depends on GR-003 waste disposal
GR-008 (operator decision support) -> compensates for GI-002, GI-003 until resolved
GF-001 (wire diameter) -> depends on welding process selection, feeds SC-004
GF-002 (precision ceiling) -> feeds all fabrication tolerance claims
GF-005 (Utilization gap) -> Resolved — Gate_07_Utilization.md created
GF-006 (structural adequacy) -> depends on GF-002 precision ceiling
GF-007 (fire suppression) -> seed for UNK-006 facility siting file
GU-001 (performance metric schema) -> depends on FN-001 Forge_Net contribution format
GU-002 (retirement handoff) -> depends on Operations/Gate_02_Triage.md intake requirements
GU-004 (silent failure detection) -> depends on GF-006 safety-critical flagging, Architecture/Components.md Baseline Observability

EV-002 (biogas parasitic loads) -> ASM-003 in Energy.md; feeds EV-001 net demand calculation
EV-003 (battery thermal containment) -> blocks enclosed battery bank commissioning;
        cross-ref Operations/Air_Scrubber.md for outgassing capture

PL-001 (halogenated polymer contamination) -> blocks first hot pyrolysis run;
        cross-ref Operations/Air_Scrubber.md AS-003 alkaline buffering stage
PL-002 (reactor pressure control and maintenance access) -> blocks reactor fabrication
PL-003 (fuel stability) -> feeds Operations/Energy.md motor-generator fuel input
PL-005 (char residue) -> routes to Operations/Gate_02_Triage.md for classification;
        cross-ref Operations/Gate_03_Reduction.md GR-003 hazardous waste disposal

WW-001 (drying schedules) -> feeds ASM-005 in Woodworking.md
WW-002 (urban timber performance) -> gates structural use of salvaged urban timber
WW-003 (CNC fixturing) -> depends on first operational CNC cycle data
WW-004 (mixed-species dust) -> Blocking; cross-ref Operations/Air_Scrubber.md
        source capture requirements
WW-005 (IFM detection) -> Blocking before any powered cut on urban salvage;
        cross-ref IFM Screening Protocol in Operations/Woodworking.md Section 1

EN-001 (validated safety factors for salvaged materials) -> Blocking; gates all
        structural specification in Architecture/Mechanical_Structures.md and
        Operations/ fabrication files; no structural spec may be promoted without this
EN-002 (Arkansas environmental load data) -> feeds EN-001 safety factor validation;
        non-blocking but informs all climate-derated design decisions
EN-003 (materials database) -> feeds EN-001 and GF-002 precision ceiling
EN-004 (high-performance low-tech methods) -> Exploratory; informs fabrication
        method selection in Gate_06
EN-005 (verification testing protocols) -> feeds EN-001 validation pathway

ME-001 (vibration resonance mapping) -> makes kinematic interlock thresholds in
        Mechanical_Structures.md provisional; blocks promotion of interlock matrix
        from Analogous to Measured confidence label
ME-002 (pneumatic purge volume vs. Air Scrubber) -> depends on Air_Scrubber.md
        back-pressure spec; Low risk, non-blocking

CF-001 (hardware watchdog minimum standard) -> Blocking for all Specification-level
        autonomous architecture; owner Electronics.md; gates CF frameworks B through G
CF-002 (correlated AI failure modes) -> depends on LT multi-unit swarm test data;
        cross-ref AP-006 (truth provenance hierarchy)
CF-003 (identity continuity during split-brain) -> cross-ref
        Admin/Ship_of_Theseus.md ST-003; non-blocking

EP-003 (integration mapping with Auditor_Protocols and Cognitive_Frameworks) ->
        cross-ref CF-001, AP-007; governance integration gap
EP-004 (engineering authority boundary) -> cross-ref GOV-004 escalation calibration;
        governance gap
EP-005 (acceptable risk threshold) -> cross-ref EC-001 confidence threshold
EP-006 (unknown lifecycle integration) -> cross-ref AP-003 audit trail schema

VG-001 (gate definition synchronization authority chain) -> Non-blocking at
        Exploration; Blocking before any Specification promotion across repository;
        source of truth chain: Auditor_Protocols.md -> Verification_Gates_LF.md ->
        Forge_Audit_Kit.md must be enforced

SR-011 (shell ROI efficiency) -> depends on SR-004 (induction charging pad design);
        energy budget comparison
SR-012 (mechanical bio-damping) -> feeds SR-001 (galvanic corrosion); biofouling
        load on wave-surge converter moving parts
SR-013 (buoyancy shift) -> depends on SR-002 (sacrificial shell material selection);
        SWATH buoyancy control limit
```

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
| FL-002 | Reduction module unassigned — upstream dependency | `Architecture/Forge_flow.md` | Resolved | — |
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
| RIP-003 | Violation incident log location undefined | `Admin/Repository_Integrity_Protocol.md` | Open | Major |
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
| EP-005 | Acceptable risk threshold undefined | `Admin/Engineer_Protocols.md` | Open | Major |
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

### Cognitive Frameworks

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CF-001 | Hardware watchdog minimum standard undefined | `Architecture/Cognitive_Frameworks.md` | Open | Critical |
| CF-002 | Correlated AI failure modes insufficiently modeled | `Architecture/Cognitive_Frameworks.md` | Open | Major |
| CF-003 | Identity continuity during split-brain unresolved | `Architecture/Cognitive_Frameworks.md` | Open | Major |

*CF-001 is Blocking — no Specification-level autonomous architecture may be approved without a defined hardware watchdog minimum standard.*

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
| SR-006 | Cold storage rack design | `Tests/Support_Raft.md` | Open | Low |
| SR-007 | Cache sanitization on hull compromise | `Tests/Support_Raft.md` | Open | Medium |
| SR-008 | Dynamic positioning vs. mooring | `Tests/Support_Raft.md` | Open | Low |
| SR-009 | Ballast pump energy draw | `Tests/Support_Raft.md` | Open | Medium |
| SR-010 | Thermal management modularity | `Tests/Support_Raft.md` | Open | Low |
| SR-011 | Shell ROI efficiency — panel swap energy cost vs. intake recovery gain | `Tests/Support_Raft.md` | Open | Medium |
| SR-012 | Mechanical bio-damping — colonization impact on wave-surge converter moving parts | `Tests/Support_Raft.md` | Open | Medium |
| SR-013 | Buoyancy shift — calcifying organism mass limit before SWATH control overwhelmed | `Tests/Support_Raft.md` | Open | Medium |

### Salvage & Fabrication

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GK-001 | Forge loop definition | `Architecture/Geck_forge_seed.md` | Resolved | — |
| GK-002 | Sacrificial anode material | `Architecture/Geck_forge_seed.md` | Open | Medium |
| GK-003 | Induction charging pad design | `Architecture/Geck_forge_seed.md` | Open | Low |
| GK-004 | Marine AM material durability | `Architecture/Geck_forge_seed.md` | Open | Low |
| GK-005 | Precision_LF.md home document not yet created | `Architecture/Geck_forge_seed.md` | Open | Minor |
| ST-001 | Grain storage and tracking protocol | `Admin/Ship_of_Theseus.md` | Open | Low |
| ST-002 | QR documentation standard | `Admin/Ship_of_Theseus.md` | Open | Low |
| ST-003 | Legal applicability by jurisdiction | `Admin/Ship_of_Theseus.md` | Open | Medium |
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
| GF-005 | Utilization stage has no owning file | `Operations/Gate_06_Fabrication.md` | Resolved | — |
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

### Cross-Module

| ID | Title | Owning Files | Status | Priority |
|---|---|---|---|---|
| UNK-006 | Master safety registry — siting and clearance for all rotating and thermal modules | `Operations/Gate_05_Separation_Thermal.md` SC-006, `Operations/Gate_04_Separation_Mechanical.md` MG-006 | Open | Major |
| UNK-007 | Reduction module unassigned — upstream dependency for Gate and flow document | `Architecture/Forge_flow.md` FL-002, `Operations/Gate_04_Separation_Mechanical.md` MG-007 | Resolved | — |
| UNK-008 | Welding wire specification and qualification — no owner assigned | `Operations/Gate_05_Separation_Thermal.md` SC-004 | Open | Major |
| UNK-009 | External root-of-trust — spans GOV-003, GOV-005, RIP-001, SEC-007 | `Admin/Governance_Charter.md`, `Admin/Repository_Integrity_Protocol.md`, `Admin/Security_Protocols.md` | Open | Critical |

### Future / Deferred

| ID | Title | Owning File | Status |
|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Admin/Auditor_Protocols.md` | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | `Architecture/Geck_forge_seed.md` | In Progress (stub added) |
| UNK-001 | Discovery.md Unknowns.md entry | `Discovery.md` | In Progress |

---

## Active Disputes Registry

Disputes are positions in active conflict within a file. They are not unknowns —
the question is defined; the answer is contested. Full dispute entries live in
the owning file's Active Disputes section.

| ID | Title | Owning File | Positions | Risk | Status |
|---|---|---|---|---|---|
| CF-DS-001 | Centralized vs. distributed cognition | `Architecture/Cognitive_Frameworks.md` | Single executive AI vs. fleet consensus | High | Open |
| CF-DS-002 | Human override authority scope | `Architecture/Cognitive_Frameworks.md` | Absolute override vs. bounded override (see `Admin/Ethical_Constraints.md`) | High | Open |

*CF-DS-002 has constitutional implications — the resolution must be consistent with
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

**CF-001 (hardware watchdog minimum standard) — Critical/Blocking.** No
Specification-level autonomous architecture approval may proceed without a defined
watchdog minimum. Monitor alongside LT-003 (autonomy architecture).

### Critical Watch

| ID | Note |
|----|------|
| GOV-005 | Constitutional stability — no fast resolution path; requires operational cycles |
| RIP-001 | Prior-state archival — confirm GitHub release cadence established |
| SEC-007 | External root-of-trust — flagged Critical from first logging; architectural decision above repository level required |
| UNK-009 | External root-of-trust cross-module — spans GOV-003, GOV-005, RIP-001, SEC-007; no fast resolution path |
| EV-003 | Battery thermal containment — no enclosed battery bank may be commissioned until resolved |
| PL-001 | Halogenated polymer contamination — no hot pyrolysis run before triage protocol validated |
| WW-005 | IFM detection — no powered machinery contact with raw urban salvage until screening workflow validated |
| EN-001 | Validated safety factors for salvaged materials — no structural specification promotion until resolved |
| CF-001 | Hardware watchdog minimum standard — no Specification-level autonomous architecture until resolved |

### Blocking Watch

| ID | Note |
|----|------|
| GOV-008 | Minimum quorum — GOV-007 Genesis Phase exit condition not yet met |
| PL-002 | Reactor pressure control — no reactor fabrication before pressure relief system specified |
| WW-004 | Mixed-species dust — interim mitigation (P100 mandatory) in place; formal characterization required before close |
| VG-001 | Gate synchronization authority chain — non-blocking at Exploration; Blocking before first Specification promotion |

GF-005 resolved in v1.6 — removed from watch.

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

---

## Audit Trail

**v0.1–v0.91:** See prior version history. Full entry detail for all unknowns now
migrated to owning file sidecars per Auditor_Protocols.md v0.5 Sidecar Model.

**v1.0 — May 2026:** First full audit cycle across all primary documents complete.

**v1.5 — 2026-05-19:** Gate_01_Intake, Gate_03_Reduction, Gate_06_Fabrication audit.
GI-006, GI-007, GR-006, GR-007, GR-008, GF-006, GF-007 added.

**v1.6 — 2026-05-20:** Gate_07_Utilization.md created. GU-001 through GU-004 added.
Electronics.md retrofitted — EL-005 through EL-008 added. GF-005 resolved.

**v1.7 — 2026-05-23:** Admin reconciliation cycle. GOV-001 through GOV-007, AP-004
through AP-007 added.

**v1.8 — 2026-05-23:** Repository_Integrity_Protocol.md created. RIP-001 through
RIP-005 added. GOV-002, GOV-003, AP-007 moved to In Progress.

**v1.9 — 2026-05-25:** Governance_Charter.md v0.5. GOV-007 In Progress. GOV-008,
GOV-009, TR-002, GU-005, AS-004 added.

**v1.9a — 2026-05-28:** Security_Protocols.md v0.2 audit. GOV-006, RIP-005 In
Progress. SEC-001 through SEC-007, CT-004, UNK-009 added.

**v2.0 — 2026-05-30:** Energy.md, Plastics.md, Woodworking.md reconciled. EV-002,
EV-003, PL-001 through PL-005, WW-001 through WW-005 added. Expiry Watch
restructured.

**v2.1 — 2026-05-31:** Engineering.md, Mechanical_Structures.md, Cognitive_Frameworks.md,
Engineer_Protocols.md, Verification_Gates_LF.md, and Canonical_Terms.md reconciled.
EN-001 through EN-005 added (Engineering & Structures section — new). ME-001 and
ME-002 added (Engineering & Structures section). CF-001 through CF-003 added
(Cognitive Frameworks section — new). EP-001 through EP-006 added (Engineer
Protocols section — new). VG-001 added to Governance & Verification section. CT-001
and CT-003 added to Governance & Verification section (CT-002 and CT-004 already
present). SR-011, SR-012, SR-013 formally indexed in Hardware Modules section.
CO-002 and GK-005 confirmed present from prior version. Active Disputes Registry
added — CF-DS-001 and CF-DS-002 from Cognitive_Frameworks.md formally recorded.
EN-001 and CF-001 added to Critical Watch. VG-001 added to Blocking Watch.
Dependency map updated with all new cluster entries.

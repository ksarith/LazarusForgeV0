# Unknowns.md — Cross-Module Unknowns Global Index
**Version 3.5 — 2026-06-19. Nine new unknowns registered across three files: SEC-008 through SEC-011 (Security_Protocols.md v0.5 audit), RIP-006 and RIP-007 (Repository_Integrity_Protocol.md v0.2 audit), GMP-006 through GMP-008 (Governance_Migration_Protocol.md v0.2 audit). RIP-004 discharged — Tier 1 Axiom Verification already implemented in Forge_Audit_Kit.md v1.1 Step 1. GMP-001 resolved. RIP-005 status updated to In Progress. Four files revised this session: Security_Protocols.md v0.5, Repository_Integrity_Protocol.md v0.2, Governance_Migration_Protocol.md v0.2, Unknowns.md v3.5.**
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

## What v3.5 Means

- **9 new unknowns registered** from 2026-06-19 session audit pass across three files:
  - SEC-008 (Signature replay protection undefined), SEC-009 (Compromise detection criteria undefined), SEC-010 (Cryptographic algorithm migration doctrine undefined), SEC-011 (Long-duration cryptographic continuity undefined) — from `Admin/Security_Protocols.md` v0.5 four-agent audit
  - RIP-006 (Archive retention policy undefined), RIP-007 (Integrity incident ownership undefined) — from `Admin/Repository_Integrity_Protocol.md` v0.2 audit
  - GMP-006 (Concurrent amendment handling undefined), GMP-007 (Amendment withdrawal procedure undefined), GMP-008 (Stale proposal expiration policy undefined) — from `Admin/Governance_Migration_Protocol.md` v0.2 audit
- **RIP-004 discharged** — Tier 1 Axiom Verification already implemented in `Admin/Forge_Audit_Kit.md` v1.1 Step 1; detection latency now bounded to one audit cycle. Moved to archive.
- **GMP-001 resolved** — GOV-001 In Progress confirmed; `Admin/Governance_Migration_Protocol.md` exists as executing resolution path.
- **RIP-005 status updated** to In Progress — `Admin/Security_Protocols.md` now exists at v0.5; description updated to reflect maturity gap rather than file non-existence.
- **Four files revised** this session: `Admin/Security_Protocols.md` v0.5, `Admin/Repository_Integrity_Protocol.md` v0.2, `Admin/Governance_Migration_Protocol.md` v0.2.

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
| EC-008 | Inferred authorization doctrine undefined | `Admin/Ethical_Constraints.md` | Open | Major |
| EC-009 | Human authority conflict resolution undefined | `Admin/Ethical_Constraints.md` | Open | Major |
| EC-010 | Jurisdiction conflict hierarchy undefined — cross-ref GOV-010; both converge on planned `Admin/Environmental_Constraints.md` | `Admin/Ethical_Constraints.md` | Open | Minor |
| EC-011 | Human governance adversary model undefined | `Admin/Ethical_Constraints.md` | Open | Major |
| GOV-001 | Governance migration mechanics incompletely operationalized — `Admin/Governance_Migration_Protocol.md` created; not yet audited against charter constraints | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-002 | Provenance operationalization immature | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-003 | Integrity enforcement architecture undefined | `Admin/Governance_Charter.md` | In Progress | Critical |
| GOV-004 | Escalation calibration partially subjective | `Admin/Governance_Charter.md` | Open | Major |
| GOV-005 | Long-term constitutional stability unproven | `Admin/Governance_Charter.md` | Open | Critical |
| GOV-006 | Human override authenticity validation undefined — GOV-006-A: interim authentication rules are declarative-only; zero automated resistance until `Admin/Security_Protocols.md` reaches Provisional Spec | `Admin/Governance_Charter.md` | Open | Major |
| GOV-007 | Bootstrap governance authority initialization undefined | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-008 | Minimum hardware and agent quorum for bootstrap compliance | `Admin/Governance_Charter.md` | Open | Major |
| GOV-009 | Bounded framework for external resource consumption and environmental interaction | `Admin/Governance_Charter.md` | Open | Major |
| GOV-010 | Jurisdictional and regulatory compliance friction for physical forge deployment — cross-ref EC-010; both converge on planned `Admin/Environmental_Constraints.md` | `Admin/Governance_Charter.md` | Open | Minor |
| SEC-001 | Quorum recovery under terminal partition | `Admin/Security_Protocols.md` | Open | Major |
| SEC-002 | Key revocation doctrine undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-003 | Key rotation period undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-004 | Key lifecycle doctrine incomplete | `Admin/Security_Protocols.md` | Open | Major |
| SEC-005 | Trusted initialization environment undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-006 | Timestamp trust under degraded clock | `Admin/Security_Protocols.md` | Open | Major |
| SEC-007 | External root-of-trust architecture undefined | `Admin/Security_Protocols.md` | Open | Critical |
| SEC-008 | Signature replay protection mechanism undefined — nonce/counter/block-hash binding required before operational deployment | `Admin/Security_Protocols.md` | Open | Major |
| SEC-009 | Compromise detection criteria undefined — no doctrine for generating suspicion; blocks revocation trigger definition | `Admin/Security_Protocols.md` | Open | Major |
| SEC-010 | Cryptographic algorithm migration doctrine undefined — no procedure if Ed25519/SHA-256 deprecated or compromised | `Admin/Security_Protocols.md` | Open | Major |
| SEC-011 | Long-duration cryptographic continuity undefined — entropy exhaustion, operator succession, algorithm migration at Leviathan-class timescales | `Admin/Security_Protocols.md` | Open | Major |

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
| RIP-005 | Security_Protocols.md Phase 3 dependency — file exists at v0.5; cryptographic implementation not yet operational | `Admin/Repository_Integrity_Protocol.md` | In Progress | Major |
| RIP-006 | Archive retention policy undefined — duration, scope, compression strategy not defined | `Admin/Repository_Integrity_Protocol.md` | Open | Minor |
| RIP-007 | Integrity incident ownership undefined — no doctrine for who closes Minor/Major/Constitutional incidents | `Admin/Repository_Integrity_Protocol.md` | Open | Major |
| CT-001 | Legacy script integration name mapping | `Admin/Canonical_Terms.md` | Open | Minor |
| CT-002 | Component Library Schema standard undefined | `Admin/Canonical_Terms.md` | Open | Major |
| CT-003 | Dependency_Priority_Map.md needed before v1 | `Admin/Canonical_Terms.md` | Open | Minor |
| CT-004 | Trusted initialization environment definition | `Admin/Canonical_Terms.md` | Open | Major |
| CT-005 | Ethical and authorization term placeholders pending canonicalization — six terms (EC-001, EC-002, EC-004, EC-007, EC-008 dependencies); close when all six have binding definitions | `Admin/Canonical_Terms.md` | Open | Major |
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
| EN-002 | Deployment-specific environmental load data not compiled | `Architecture/Engineering.md` | Open | Major |
| EN-003 | Materials database for salvaged alloy identification | `Architecture/Engineering.md` | Open | Major |
| EN-004 | High-performance low-tech fabrication methods | `Architecture/Engineering.md` | Open | Minor |
| EN-005 | Verification testing protocols for structural claims | `Architecture/Engineering.md` | Open | Major |
| EN-006 | Advanced engineering section drift risk (topology, composites) | `Architecture/Engineering.md` | Open | Minor |
| ME-001 | Vibration resonance mapping on mismatched salvaged rails | `Architecture/Mechanical_Structures.md` | Open | Major |
| ME-002 | Pneumatic purge volume requirements vs. Air Scrubber capacity | `Architecture/Mechanical_Structures.md` | Open | Minor |
| ME-003 | Structural creep and damp-fill aging not characterized | `Architecture/Mechanical_Structures.md` | Open | Major |
| ME-004 | Calibration values not separated from doctrine sections | `Architecture/Mechanical_Structures.md` | Open | Minor |

*EN-001 is Blocking — no structural specification in any file may be promoted without validated safety factors for salvaged materials.*

### Chemistry & Electrochemistry

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CE-001 | Galvanic corrosion rates for salvaged mixed-metal assemblies not characterized | `Architecture/Chemistry.md` | Open | Major |
| CE-002 | Oxide burden effect on Spin Chamber output quality not quantified | `Architecture/Chemistry.md` | Open | Major |
| CE-003 | Field polymer identification reliability not validated for mixed salvage stream | `Architecture/Chemistry.md` | Open | Critical |
| CE-004 | Chemical Operator Minimum Competency — Appendix A created in Chemistry.md | `Architecture/Chemistry.md` | In Progress | Major |
| CE-005 | Solution chemistry and precipitation doctrine not established | `Architecture/Chemistry.md` | Open | Major |

*CE-003 is a safety-critical prerequisite before first hot pyrolysis run — cross-references PL-001.*

### Thermal Systems

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| TH-001 | Forge-specific heat pump sizing doctrine not yet developed | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-002 | TEG harvest yield at Gate_05 exterior not characterized | `Architecture/Thermal_Systems.md` | Open | Minor |
| TH-003 | Atmospheric moisture yield under deployment conditions not measured | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-004 | Salvaged Peltier device characterization protocol not defined | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-005 | Thermal interface material doctrine undefined | `Architecture/Thermal_Systems.md` | Open | Major |
| TH-006 | TEG absolute efficiency range not validated for salvage stock | `Architecture/Thermal_Systems.md` | Open | Minor |

*TH-003 is Blocking for Living Waters deployment. Non-blocking for all other Forge operations.*

### Friction Dynamics

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FD-001 | Gate_04 centrifugal separation RPM data not linked to Stokes settling doctrine | `Architecture/Friction_Dynamics.md` | Open | Major |
| FD-002 | Air Scrubber duct velocity profile not characterized per capture stage | `Architecture/Friction_Dynamics.md` | Open | Major |
| FD-003 | Salvaged bearing L10 life estimation protocol not defined | `Architecture/Friction_Dynamics.md` | Open | Major |
| FD-005 | Fluid-Structure Interaction (FSI) not formally bridged | `Architecture/Friction_Dynamics.md` | Open | Major |

### Cognitive Frameworks

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CF-001 | Hardware watchdog minimum standard — parameters defined, hardware validation pending | `Operations/Electronics.md` | In Progress | Critical |
| CF-002 | Correlated AI failure modes — test protocol defined, swarm deployment pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Major |
| CF-003 | Identity continuity during split-brain — doctrine defined, threshold calibration pending | `Architecture/Cognitive_Frameworks.md` | In Progress | Major |

*CF-001 remains Blocking — parameters are Analogous confidence pending first hardware prototype validation.*

### Emergence

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EM-001 | Behavioral opacity detection threshold — depends on CF-001 resolution | `Challenges/Emergence.md` | Open | High |
| EM-002 | Correlated failure detection in multi-agent consensus | `Challenges/Emergence.md` | Open | High |
| EM-003 | Gradual autonomy transition detection — no current sensor doctrine | `Challenges/Emergence.md` | Open | Medium |
| EM-004 | Governance substrate integrity under emergent agent access — mirrors GOV-003, SEC-007 | `Challenges/Emergence.md` | Open | Critical |

*EM-001 depends on CF-001 resolution.*
*EM-004 is Critical — no fast resolution path; architectural decision above repository level required.*

### Waste

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| WA-001 | Embedded complexity preservation metric undefined | `Challenges/Waste.md` | Open | Major |
| WA-002 | Hazardous fraction identification reliability — no validated identification protocol | `Challenges/Waste.md` | Open | Critical |
| WA-003 | Informal sector integration doctrine undefined | `Challenges/Waste.md` | Open | Major |
| WA-004 | Negative-value waste fraction disposal doctrine undefined | `Challenges/Waste.md` | Open | Critical |

*WA-002 and WA-004 are Critical — no sustained mixed-waste operations without hazardous fraction identification and negative-value disposal doctrine.*

### Biofouling

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| BF-001 | Ultrasonic antifouling energy budget not characterized | `Challenges/Biofouling.md` | Open | Major |
| BF-002 | Biomimetic surface topography durability not characterized | `Challenges/Biofouling.md` | Open | Major |
| BF-003 | Regional fouling rate differential — no maintenance cycle calibration | `Challenges/Biofouling.md` | Open | Major |
| BF-004 | Shed panel reef substrate viability — toxin leach unvalidated | `Challenges/Biofouling.md` | Open | Major |

### Planned Obsolescence

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| PO-001 | Firmware re-baselining legal boundary doctrine — operationally untested | `Challenges/Planned_Obsolescence.md` | Open | Major |
| PO-002 | Potting compound removal chemistry — no validated protocol | `Challenges/Planned_Obsolescence.md` | Open | Major |
| PO-003 | Proprietary connector adapter coverage — no systematic inventory | `Challenges/Planned_Obsolescence.md` | Open | Minor |
| PO-004 | Community re-baselining skill transfer standard undefined | `Challenges/Planned_Obsolescence.md` | Open | Major |

### Water Scarcity

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| WS-001 | Optimal energy harvesting for high-humidity low-kinetic environments | `Challenges/Water.md` | Open | Major |
| WS-002 | Heavy metal stabilization chemistry for tropical climates | `Challenges/Water.md` | Open | Major |
| WS-003 | Stratification diminishing returns threshold | `Challenges/Water.md` | Open | Major |
| WS-004 | Community adoption and maintenance protocol undefined | `Challenges/Water.md` | Open | Major |

*TH-003 remains the Blocking unknown for LW-005 atmospheric harvesting.*

### Living Waters

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| LW-UNK-001 | Volatile co-distillation characterization for LW-001 | `Tests/Living_Waters.md` | Partially Addressed — LW-TEST-102 defines test approach; empirical validation pending | Critical |
| LW-UNK-002 | Membrane survivability for LW-003 at sustained operational depth | `Tests/Living_Waters.md` | Open | Major |
| LW-UNK-003 | Lumen structural integrity limits for LW-003 under deep pressure | `Tests/Living_Waters.md` | Partially Addressed — implosion threshold characterized; salvage material validation pending | Critical |
| LW-UNK-004 | Biofouling rate characterization for LW-003 in target deployment zones | `Tests/Living_Waters.md` | Open | Major |
| LW-UNK-005 | Energy balance: LW-001 with MVR vs. LW-002 surface RO | `Tests/Living_Waters.md` | Partially Addressed — energy profiles established; empirical validation pending | Major |
| LW-UNK-006 | Salvage-compatible membrane sourcing for any RO pathway | `Tests/Living_Waters.md` | Open | Major |
| LW-UNK-007 | Draw solution regeneration chemistry and energy cost for LW-007 | `Tests/Living_Waters.md` | Open | Major |
| LW-UNK-008 | Site characterization → pathway selection decision framework | `Tests/Living_Waters.md` | Declared — formal framework not yet written | Minor |
| LW-UNK-009 | Salvage sourcing path for fence-mounted AWG variant (LW-005a) | `Tests/Living_Waters.md` | Open | Minor |

*LW-UNK-001 CRITICAL — distillate may be concentrated toxin stream; blocks potable output claim from LW-001.*
*LW-UNK-003 CRITICAL — 4.9 MPa net crush load at 500 m; standard salvage tubing will fail.*

### Trophic Forge

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| TF-001 | Phototaxis yield at Forge scale unvalidated | `Tests/Trophic_Forge.md` | Open | Critical |
| TF-002 | Prior art search incomplete | `Tests/Trophic_Forge.md` | Partially Addressed | Major |
| TF-003 | Fish nutrient output at Forge stocking density uncharacterized | `Tests/Trophic_Forge.md` | Open | Major |
| TF-004 | Fish species selection not determined | `Tests/Trophic_Forge.md` | Open | Major |
| TF-005 | Phytoremediation loop closure unvalidated | `Tests/Trophic_Forge.md` | Open | Major |
| TF-006 | Non-target insect capture rate — Ethical_Constraints escalation candidate | `Tests/Trophic_Forge.md` | Partially Addressed — draft nocturnal protocol defined; empirical validation pending | High — Ethical_Constraints escalation candidate |
| TF-007 | Single node failure propagation uncharacterized | `Tests/Trophic_Forge.md` | Open | Major |
| TF-008 | Minimum viable loop scale unknown | `Tests/Trophic_Forge.md` | Open | Major |
| TF-009 | Interaction boundary with Living_Waters.md at pond node undefined | `Tests/Trophic_Forge.md` + `Tests/Living_Waters.md` | Open | Minor |
| TF-010 | Seasonal and climatic variability uncharacterized | `Tests/Trophic_Forge.md` | Open | Major |

*TF-001 Critical/Blocking — entire organizing principle rests on phototaxis yield.*
*TF-006 ethical unknown — halt expansion if non-target capture threshold cannot be bounded.*

### Solar Descent

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| SD-UNK-001 | Flux delivery at Forge-scale salvage fiber unvalidated | `Tests/Solar_Descent.md` | Open | Critical |
| SD-UNK-002 | Achievable underground temperature at Forge build quality unknown | `Tests/Solar_Descent.md` | Open | Critical |
| SD-UNK-003 | Molten tin termination (SD-001a) viability unconfirmed | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-004 | Host geology fracturing threshold unknown — blocks all excavation | `Tests/Solar_Descent.md` | Open | Critical — parallels FA-001 |
| SD-UNK-005 | Working fluid salvage sourcing for SD-002 unconfirmed | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-006 | Parasitic pump load for SD-002 uncharacterized | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-007 | Chamber self-discharge rate unknown | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-008 | Stirling engine salvage availability at required scale unconfirmed | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-009 | Excavation feasibility at Forge scale unassessed | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-010 | Waste heat cascade interface with Living_Waters.md undefined | `Tests/Solar_Descent.md` + `Tests/Living_Waters.md` | Open | Minor |
| SD-UNK-011 | Receiver material survivability uncharacterized | `Tests/Solar_Descent.md` | Open | Major |
| SD-UNK-012 | Dust and alignment stability uncharacterized | `Tests/Solar_Descent.md` | Open | Major |

*SD-UNK-004 carries same governance weight as FA-001 — no excavation without geomechanical assessment.*
*SD-UNK-002 Critical — all power conversion planning must assume conservative lower bound (~500°C).*

### Critical Minerals

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| CM-001 | Real-time material assay integration undefined | `Challenges/Critical_Minerals.md` | Open | Major |
| CM-002 | Acid leach reagent recovery and closed-loop doctrine undefined | `Challenges/Critical_Minerals.md` | Open | Critical |
| CM-003 | Functional substitute performance floor undefined | `Challenges/Critical_Minerals.md` | Open | Major |
| CM-004 | Urban ore database coverage insufficient | `Challenges/Critical_Minerals.md` | Open | Major |

*CM-002 Critical — no hydrometallurgical processing before closed-loop reagent recovery specified.*

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
| SR-006 | Cold storage rack design | `Tests/Support_Raft.md` | In Progress | Low |
| SR-007 | Cache sanitization on hull compromise | `Tests/Support_Raft.md` | Open | Medium |
| SR-008 | Dynamic positioning vs. mooring | `Tests/Support_Raft.md` | Open | Low |
| SR-009 | Ballast pump energy draw | `Tests/Support_Raft.md` | Open | Medium |
| SR-011 | Shell ROI efficiency | `Tests/Support_Raft.md` | Open | Medium |
| SR-012 | Mechanical bio-damping | `Tests/Support_Raft.md` | Open | Medium |
| SR-013 | Buoyancy shift — calcifying organism mass limit | `Tests/Support_Raft.md` | Open | Medium |

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

*WW-004 Blocking for sustained mixed-species operations without P100 respirator.*
*WW-005 Blocking for processing raw urban salvage through any powered machinery.*

### Facilities

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| FA-001 | Site not confirmed or assessed | `Architecture/Facilities.md` | Open | Critical |
| FA-002 | Hot Zone minimum clearance radius not defined | `Architecture/Facilities.md` | Open | Major |
| FA-003 | Legal zoning and permitting not assessed | `Architecture/Facilities.md` | Open | Major |
| FA-004 | RDC heat load impact on operator safety not quantified | `Architecture/Facilities.md` | Open | Minor |

*FA-001 Critical — blocks all hot operations and SP-006 (emergency response).*

### Safety

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| SP-001 | Risk threshold cross-reference with Engineer_Protocols.md pending | `Admin/Safety_Protocols.md` | Open | Major |
| SP-002 | PPE specifications not sourced to standards | `Admin/Safety_Protocols.md` | Open | Major |
| SP-003 | Site noise levels not measured | `Admin/Safety_Protocols.md` | Open | Major |
| SP-004 | Heat stress doctrine not validated against operator experience | `Admin/Safety_Protocols.md` | Open | Minor |
| SP-005 | Regulatory compliance and permitting not assessed | `Admin/Safety_Protocols.md` | Open | Major |
| SP-006 | Emergency response procedures not defined | `Admin/Safety_Protocols.md` | Open | Major |

*SP-006 blocked by FA-001 — cannot define site evacuation without a site.*

### Economics

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| EC-001 | Critical mineral surplus disposition path undefined | `Admin/Economics.md` | Open | Major |
| EC-002 | Operating cost baseline not established | `Admin/Economics.md` | Open | Critical |
| EC-004 | Market rate data not maintained | `Admin/Economics.md` | Open | Minor |
| EC-005 | Legal and tax compliance not assessed | `Admin/Economics.md` | Open | Major |

*EC-002 Critical — blocks TR-001 closure; depends on EV-001.*

### Governance Migration

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| GMP-003 | Adversarial review underspecified at v0 single-contributor | `Admin/Governance_Migration_Protocol.md` | Open | Major |
| GMP-004 | Ratification authentication gap mirrors GOV-006 | `Admin/Governance_Migration_Protocol.md` | Open | Major |
| GMP-005 | Track A / Track B boundary insufficient for interpretive Tier 1 capture via lower-tier docs — partially resolved in v0.2 via expanded Track identification rule | `Admin/Governance_Migration_Protocol.md` | In Progress | Major |
| GMP-006 | Concurrent amendment handling undefined — serialization, merging, and blocking rules absent | `Admin/Governance_Migration_Protocol.md` | Open | Major |
| GMP-007 | Amendment withdrawal procedure undefined — no explicit abandon state | `Admin/Governance_Migration_Protocol.md` | Open | Minor |
| GMP-008 | Stale proposal expiration policy undefined — proposals could persist indefinitely | `Admin/Governance_Migration_Protocol.md` | Open | Minor |

*GMP-004 highest-risk attack vector on Track B amendment process — depends on SEC-007.*

### Repository Structure

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| RS-001 | Non-markdown file type introduction procedure undefined | `Admin/Repository_Structure.md` | Open | Minor |

### Precision

| ID | Title | Owning File | Status | Priority (Promo) |
|---|---|---|---|---|
| PR-001 | Precision ceiling not yet declared | `Architecture/Precision.md` | Open | Critical |
| PR-002 | Reference standard not established | `Architecture/Precision.md` | Open | Major |
| PR-003 | Traceable dimensional claims required at Specification | `Architecture/Precision.md` | Open | Major |
| PR-004 | Backlash and compliance characterization not performed | `Architecture/Precision.md` | Open | Major |

*PR-001 Critical — blocks T1/T2 part claims; PR-004 is a prerequisite.*

### Pending Corrections

| ID | Title | Files Affected | Status | Priority |
|---|---|---|---|---|
| PC-001 | Verification Ref corrections | All 10 files corrected to `Admin/Verification_Gates_LF.md` | Resolved | Major |
| PC-002 | Upstream reference corrections | All 7 files corrected | Resolved | Minor |
| PC-003 | New file cross-reference corrections | All 10 files corrected | Resolved | Minor |
| PC-004 | Stale name corrections — Challenges/Water.md and Planned_Obsolescence.md | Both files corrected | Resolved | Minor |

### Cross-Module

| ID | Title | Owning Files | Status | Priority |
|---|---|---|---|---|
| UNK-008 | Welding wire specification and qualification — no owner assigned | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| UNK-009 | External root-of-trust — spans GOV-003, GOV-005, RIP-001, SEC-007 | `Admin/Governance_Charter.md`, `Admin/Repository_Integrity_Protocol.md`, `Admin/Security_Protocols.md` | Open | Critical |

### Future / Deferred

| ID | Title | Owning File | Status |
|---|---|---|---|
| UNK-003 | Cross-repo assumption contracts | `Admin/Auditor_Protocols.md` | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | `Architecture/Geck_forge_seed.md` | In Progress (stub added) |
| UNK-001 | Discovery.md Unknowns.md entry | `Discovery.md` | In Progress |
| RC-001 | Governance Drift | None yet | Candidate |
| RC-002 | Incentive Capture | None yet | Candidate |
| RC-003 | Information Decay | None yet | Candidate |
| RC-004 | Identity Continuity | None yet | Candidate |
| RC-005 | Coordination Failure | None yet | Candidate |
| RC-006 | Institutional Ossification | None yet | Candidate |

*RC-001 through RC-006 are Reflexive Challenge candidates — log against Challenges/ on next major architecture review.*

---

## Active Disputes Registry

| ID | Title | Owning File | Positions | Risk | Status |
|---|---|---|---|---|---|
| CF-DS-001 | Centralized vs. distributed cognition | `Architecture/Cognitive_Frameworks.md` | Single executive AI vs. fleet consensus | High | Open |
| CF-DS-002 | Human override authority scope | `Architecture/Cognitive_Frameworks.md` | Absolute override vs. bounded override (see `Admin/Ethical_Constraints.md`) | High | Open |

*CF-DS-002 has constitutional implications — resolution must be consistent with `Admin/Ethical_Constraints.md` Anti-Weaponization and Life Preservation doctrines. Escalate to human governing party before closing.*

---

## Expiry Watch

*Expiry Rule is active. Check this table at the opening of each audit cycle.*

**Tier 1 Axiom verification is the mandatory first step** — confirm axiom text in `Admin/Governance_Charter.md` matches prior committed version before proceeding. Any unratified change is a Constitutional violation.

FL-001 and several EC entries have been In Progress since v1.1 — approaching two-cycle threshold. Flag for Full Stop Review trigger assessment at next audit opening if still unresolved.

GOV-003 In Progress — `Admin/Repository_Integrity_Protocol.md` is the executing resolution path. GOV-005 remains Critical with no fast resolution path. GOV-007 In Progress — Genesis Phase Protocol executing; full resolution depends on GOV-008. GOV-008 exit condition not yet met.

**RIP-001 Critical** — GitHub releases identified as v0 resolution path. Confirm release cadence established before closing.

**EN-001 Critical/Blocking** — no structural specification may be promoted without validated safety factors for salvaged materials.

**CF-001 In Progress/Blocking** — parameters defined (τ=50ms WDT). Remains Blocking until first hardware prototype validates at Measured confidence.

### Critical Watch

| ID | Note |
|----|------|
| GOV-005 | Constitutional stability — no fast resolution path; requires operational cycles |
| RIP-001 | Prior-state archival — confirm GitHub release cadence before closing |
| SEC-007 | External root-of-trust — architectural decision above repository level required |
| UNK-009 | External root-of-trust cross-module — spans GOV-003, GOV-005, RIP-001, SEC-007 |
| EC-008 | Inferred authorization — softest point in permission model; interim default (no material alteration) in place; formal resolution required before operational deployment |
| EC-011 | Human governance adversary model — load-bearing assumption under "capability never outruns permission"; no protection if permission source is compromised |
| EV-003 | Battery thermal containment — no enclosed battery bank until resolved |
| PL-001 | Halogenated polymer contamination — no hot pyrolysis run before triage protocol validated |
| WW-005 | IFM detection — no powered machinery contact with raw urban salvage until screening validated |
| EN-001 | Validated safety factors for salvaged materials — no structural specification promotion until resolved |
| CF-001 | Hardware watchdog — In Progress; Blocking until hardware prototype validates at Measured confidence |
| TH-003 | Atmospheric moisture yield — Blocking for Living Waters deployment |
| FA-001 | Site not confirmed — no hot operations until site physically assessed |
| EC-002 | Operating cost baseline not established — blocks TR-001; depends on EV-001 |
| PR-001 | Precision ceiling not declared — blocks T1/T2 part claims; PR-004 prerequisite |
| EM-001 | Behavioral opacity detection threshold — depends on CF-001 hardware validation |
| EM-004 | Governance substrate integrity under emergent agent access — Critical; mirrors GOV-003, SEC-007 |
| WA-002 | Hazardous fraction identification reliability — safety-critical before mixed-waste operations |
| WA-004 | Negative-value waste fraction disposal — no owning file; mirrors GR-003 gap |
| CM-002 | Acid leach reagent recovery doctrine — no hydrometallurgical processing before closed-loop specified |
| CE-003 | Field polymer identification reliability — Critical; blocks first hot pyrolysis run |
| TF-006 | Non-target insect capture — Ethical_Constraints escalation candidate; halt expansion if threshold cannot be bounded |
| SD-UNK-004 | Host geology fracturing threshold — no excavation without geomechanical assessment; parallels FA-001 |
| LW-UNK-001 | Volatile co-distillation in LW-001 — CRITICAL safety gap; blocks potable output claim |
| LW-UNK-003 | LW-003 lumen implosion — CRITICAL; 4.9 MPa net crush load at 500 m |

### Blocking Watch

| ID | Note |
|----|------|
| GOV-008 | Minimum quorum — GOV-007 Genesis Phase exit condition not yet met |
| PL-002 | Reactor pressure control — no reactor fabrication before pressure relief specified |
| WW-004 | Mixed-species dust — interim mitigation (P100 mandatory); formal characterization required |
| VG-001 | Gate synchronization authority chain — Blocking before first Specification promotion |

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
| GF-005 | Utilization stage has no owning file | Resolved — Operations/Gate_07_Utilization.md created | 2026-05-20 |
| UNK-006 | Master safety registry — facility siting | Resolved — Architecture/Facilities.md created | 2026-06-06 |
| GK-005 | Precision_LF.md not yet created | Resolved — Architecture/Precision.md created | 2026-06-06 |
| PR-005 | GK-005 resolution confirmation pending | Resolved — Geck_forge_seed.md Section V updated | 2026-06-08 |
| EP-005 | Acceptable risk threshold — partial resolution | Partially resolved — Safety_Protocols.md Section I defines consequence categories; full threshold remains open in Engineer_Protocols.md sidecar | 2026-06-06 |
| EC-003 | Barter valuation standard undefined | Resolved — Admin/Economics.md Section VI defines barter doctrine | 2026-06-06 |
| GOV-001 | Governance migration mechanics | **Archive entry premature — un-archived 2026-06-18.** `Admin/Governance_Migration_Protocol.md` created 2026-06-06 as resolution path but has not been audited against charter constraints. Status returned to In Progress in active index. | 2026-06-06 / corrected 2026-06-18 |
| PC-004 | Stale name corrections | Resolved — corrections applied during Challenges/ retrofit pass | 2026-06-11 |
| FA-005 | UNK-006 resolution confirmation pending | Resolved — Facilities.md confirmed as owning file | 2026-06-11 |
| SR-010 | Thermal management modularity | Resolved — declared modular/expandable in Support_Raft.md v0.5 | 2026-06-11 |
| RS-002 | Forge_flow.md casing outlier | Resolved — corrected in Discovery.md Rename Registry | 2026-06-11 |
| RS-003 | Archive/ directory not created | Resolved — Archive/README.md created with append-only doctrine | 2026-06-11 |
| FD-004 | Support_Raft.md reverse upstream link | Resolved — bidirectional cross-reference confirmed | 2026-06-11 |
| GMP-001 | GOV-001 resolution confirmation pending | Resolved — GOV-001 confirmed resolved; GMP ownership confirmed | 2026-06-11 |
| GMP-002 | Canonical ownership transfer not recorded in Charter | Resolved — ownership transfer confirmed and logged | 2026-06-11 |
| RIP-003 | Violation incident log location undefined | Resolved — Admin/Logs/violations.md declared as canonical violation incident log | 2026-06-11 |
| RIP-004 | Constitutional violation detection latency undefined | Resolved — Tier 1 Axiom Verification implemented as Step 1 of mandatory Audit Opening Checklist in `Admin/Forge_Audit_Kit.md` v1.1; detection latency bounded to one audit cycle | 2026-06-19 |
| GMP-001 | GOV-001 resolution confirmation pending | Resolved — GOV-001 In Progress confirmed; `Admin/Governance_Migration_Protocol.md` exists as executing resolution path; Unknowns.md v3.4/v3.5 reflects corrected status | 2026-06-19 |

---

## Audit Trail

**v0.1–v0.91:** See prior version history.
**v1.0 — May 2026:** First full audit cycle across all primary documents complete.
**v1.5 — 2026-05-19:** Gate_01_Intake, Gate_03_Reduction, Gate_06_Fabrication audit. GI-006, GI-007, GR-006–008, GF-006–007 added.
**v1.6 — 2026-05-20:** Gate_07_Utilization.md created. GU-001–004 added. EL-005–008 added. GF-005 resolved.
**v1.7 — 2026-05-23:** Admin reconciliation cycle. GOV-001–007, AP-004–007 added.
**v1.8 — 2026-05-23:** Repository_Integrity_Protocol.md created. RIP-001–005 added. GOV-002, GOV-003, AP-007 In Progress.
**v1.9 — 2026-05-25:** Governance_Charter.md v0.5. GOV-007 In Progress. GOV-008, GOV-009, TR-002, GU-005, AS-004 added.
**v1.9a — 2026-05-28:** Security_Protocols.md v0.2 audit. SEC-001–007, CT-004, UNK-009 added.
**v2.0 — 2026-05-30:** Energy.md, Plastics.md, Woodworking.md reconciled. EV-002, EV-003, PL-001–005, WW-001–005 added.
**v2.1 — 2026-05-31:** Engineering.md, Mechanical_Structures.md, Cognitive_Frameworks.md, Engineer_Protocols.md, Verification_Gates_LF.md, Canonical_Terms.md reconciled. EN-001–005, ME-001–002, CF-001–003, EP-001–006, VG-001, CT-001, CT-003, SR-011–013 added. EN-001 and CF-001 added to Critical Watch.
**v2.2 — 2026-05-31:** Thermal_Systems.md and Friction_Dynamics.md created. TH-001–004, FD-001–004 added. TH-003 added to Critical Watch.
**v2.3 — 2026-06-02:** Chemistry.md created. CE-001–004 indexed. CE-003 flagged safety-critical.
**v2.4 — 2026-06-06:** Six new files created and indexed. FA, SP, EC, GMP, RS, PR clusters added. PC cluster migrated from Discovery.md. UNK-006, GK-005, EP-005, EC-003, GOV-001 resolved. FA-001, EC-002, PR-001 added to Critical Watch.
**v2.5 — 2026-06-08:** Retrofit pass — seven files. CF-001–003 moved to In Progress.
**v2.6 — 2026-06-08:** Retrofit pass completed for 14 additional files. PC-001–003 closed.
**v2.7 — 2026-06-11:** Challenges/Emergence.md created. EM-001–004 registered. EM-001, EM-004 added to Critical Watch.
**v2.8 — 2026-06-11:** Full Challenges/ retrofit pass. WA-001–004, BF-001–004, PO-001–004, WS-001–004, CM-001–004 registered. WA-002, WA-004, CM-002 added to Critical Watch.
**v2.9 — 2026-06-11:** Support_Raft.md v0.5. SR-010 resolved. Dependency Map retired.
**v3.0 — 2026-06-11:** Six resolved: RS-002, RS-003, FD-004, GMP-001, GMP-002, RIP-003.
**v3.1 — 2026-06-11:** Location abstraction pass. TH-003, EN-002, FA-004 retitled to deployment-generic framing.
**v3.2 — 2026-06-11:** Architecture audit integration pass. ME-003, ME-004, TH-005, TH-006, CE-005, EN-006, FD-005 added. CE-003 elevated to Critical Watch. CE-004 In Progress. FA-005 resolved.
**v3.3 — 2026-06-14:** Three new Tests/ file clusters registered. LW (9), TF (10), SD (12) unknowns. TF-006 and SD-UNK-004 added to Critical Watch. DS-001 closed. 31 total new unknowns.
**v3.4 — 2026-06-18:** Six new unknowns registered: EC-008, EC-009, EC-010, EC-011 (Ethical_Constraints.md v0.9 audit), GOV-010 (Governance_Charter.md v0.8), CT-005 (Canonical_Terms.md v0.3). GOV-001 un-archived — premature; returned to In Progress pending GMP audit against charter constraints. GOV-006-A declarative-only notice logged. EC-008 and EC-011 added to Critical Watch. EC-010 and GOV-010 cross-referenced to planned Environmental_Constraints.md.
**v3.5 — 2026-06-19:** Nine new unknowns registered: SEC-008–011 (Security_Protocols.md v0.5), RIP-006–007 (Repository_Integrity_Protocol.md v0.2), GMP-006–008 (Governance_Migration_Protocol.md v0.2). RIP-004 discharged — Tier 1 Axiom Verification in Forge_Audit_Kit.md v1.1 Step 1 executes resolution path. GMP-001 resolved. RIP-005 updated to In Progress. GMP-005 In Progress (partial resolution via expanded Track identification rule).

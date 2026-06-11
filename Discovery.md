# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## Repository Role

This is the **active working repository** — lean, connected, and operational.
Doctrine and philosophy are developed in the companion repository `Lazarus-Forge-`
and refined here into practical implementation.

Divergence between the two repos is a signal, not a problem — it surfaces when
doctrine needs updating or practice has drifted from principles. Any contributor
(human or AI) who encounters a contradiction between repos must log it as a
Non-blocking Unknown in `Admin/Auditor_Protocols.md` and flag it in the next
review cycle. Divergence that goes unlogged is drift. Divergence that gets
logged is progress.

---

## What This Repository Is

LazarusForgeV0 is the active working repository for the Lazarus Forge — a
salvage-first, adaptive resource recovery system designed to preserve functional
value before material reduction.

**Core KPI:** Value recovered per kWh consumed.

---

## How to Use This File

> **Scope entries are navigation summaries only.**
> File-local Scope Boundary sections remain authoritative.
> Where this file and a file's own Scope Boundary conflict, the file wins.
> Update Discovery.md when files change; do not update files to match Discovery.md.

**Routing quick-reference:**
- "Where does this belong?" → find the owning file in the scope maps below
- "What files does this decision affect?" → check Downstream
- "What must exist before this file can be promoted?" → check Upstream and ⚠️ notes
- "What does this term mean?" → `Architecture/Forge_flow.md` §Defined Terms first; `Admin/Canonical_Terms.md` second
- Full detail always lives in the file itself

---

## Repository Structure

```
Root
├── README.md                               — Project overview and core principles
├── Discovery.md                            — Navigation layer (this file)
├── Routing.md                              — Programmatic file index; raw URLs for agent context loading
├── Unknowns.md                             — Cross-module unknowns global index

Admin/                                      — Governance, protocols, and doctrine
    ├── Governance_Charter.md               — Constitutional tier; 8 Axioms (Tier 1)
    ├── Ethical_Constraints.md              — Embedded AI governance & anti-weaponization (Tier 1)
    ├── Auditor_Protocols.md                — Verification doctrine; 10-phase sequence (Tier 2)
    ├── Forge_Audit_Kit.md                  — Condensed routine multi-agent cycle reference (Tier 3)
    ├── Verification_Gates_LF.md            — Canonical 6 document promotion gates
    ├── File_Template.md                    — 10-section layout standard & Ethical Anchor field
    ├── Canonical_Terms.md                  — Anti-drift vocabulary & term exclusions
    ├── Engineer_Protocols.md               — Operational execution standards for engineers
    ├── Safety_Protocols.md                 — Physical operator safety; PPE, heat stress, hearing conservation
    ├── Security_Protocols.md               — Cryptographic trust & multi-agent node security
    ├── Repository_Integrity_Protocol.md    — Baseline enforcement & violation recovery
    ├── Repository_Structure.md             — Filename conventions, folder assignment doctrine
    ├── Ship_of_Theseus.md                  — Right-to-repair philosophical/legal defense
    ├── Trajectories.md                     — Multi-era version roadmap (v0 to interstellar)
    ├── Economics.md                        — Dynamic resource doctrine; market navigation; barter
    ├── Governance_Migration_Protocol.md    — Tier 1 Axiom amendment procedures
    └── AUDIT_HARNESS.py                    — Automated script supporting verification

Architecture/                               — System architecture and foundational logic
    ├── Forge_flow.md                       — Master decision flow & REPOSITORY VOCABULARY STANDARD
    ├── Components.md                       — Critical vs useful component taxonomy
    ├── Facilities.md                       — Physical environment constraints; siting prerequisites
    ├── Geck_forge_seed.md                  — Minimum viable seed specification
    ├── Engineering.md                      — First-principles intellectual backbone
    ├── Precision.md                        — Precision ceiling doctrine; tolerance tiers; metrology
    ├── Mechanical_Structures.md            — Salvaged-frame kinematic and structural doctrine
    ├── Thermal_Systems.md                  — Thermodynamic laws, heat transfer, Peltier, TEG doctrine
    ├── Friction_Dynamics.md                — Fluid mechanics, aerodynamics, and tribology doctrine
    ├── Chemistry.md                        — Electrochemistry, corrosion, redox, polymer degradation
    ├── Cognitive_Frameworks.md             — Distributed cognition & survival under uncertainty
    └── Forge_Net.md                        — Decentralized data/physical network logistics

Operations/                                 — Physical modules and operational systems
    ├── Gate_01_Intake.md                   — Entry safety screening & provenance tagging
    ├── Gate_02_Triage.md                   — 5-station value preservation decision engine
    ├── Gate_03_Reduction.md                — Irreversible mechanical sizing (feedstock milling)
    ├── Gate_04_Separation_Mechanical.md    — Centrifugal stratification & fail-to-bin diversion
    ├── Gate_05_Separation_Thermal.md       — Core induction melting & gradient extraction
    ├── Gate_06_Fabrication.md              — Arc welding & mill-to-spec constructive ceiling
    ├── Gate_07_Utilization.md              — After-action loop & failure data capture
    ├── Electronics.md                      — Salvaged PCB harvesting & Logic-Zero firmware trust
    ├── Energy.md                           — Incremental power bootstrap & load profiles
    ├── Air_Scrubber.md                     — 5-stage negative-pressure containment subsystem
    ├── Plastics.md                         — Polymer triage & 3-stage pyrolysis framework
    └── Woodworking.md                      — Salvaged urban timber milling & drying schedules

Tests/                                      — Test frameworks and deployment platforms
    ├── Support_Raft.md                     — Stationary marine deployment anchor
    └── Leviathan_testing.md                — Deep-ocean autonomous stress-testing

Challenges/                                 — Problem layer: why these capabilities exist
    ├── Water.md                            — Water scarcity and contamination (Living Waters)
    ├── Biofouling.md                       — Biological colonization and corrosion
    ├── Waste.md                            — Discretionary waste and repair capacity loss
    ├── Planned_Obsolescence.md             — Deliberate unrepairability and locked hardware
    ├── Critical_Minerals.md                — Rare earth and critical mineral supply chains
    └── Emergence.md                        — Emergent intelligence: alignment-by-environment design

Archive/                                    — Prior states of governance-bearing documents
    └── [created when first Specification-level file is revised — see Admin/Repository_Structure.md]
```

**Planned / not yet created:**
- `economics_v0.md` — superseded by `Admin/Economics.md` (created 2026-06-05)
- `Precision_LF.md` — superseded by `Architecture/Precision.md` (created 2026-06-05)
- `Admin/Safety_Protocols.md` — created 2026-06-05 ✓
- `Admin/Governance_Migration_Protocol.md` — created 2026-06-05 ✓
- `Admin/Repository_Structure.md` — created 2026-06-05 ✓
- `Architecture/Facilities.md` — created 2026-06-05 ✓
- `Safety_Protocols.md` (noise/hearing conservation) — resolved by `Admin/Safety_Protocols.md` ✓

**Routing.md completeness:** Verified complete as of 2026-06-11 (`Challenges/Emergence.md` added). Any gaps found on future audit passes are tracked as PC cluster entries in `Unknowns.md`.

---

## Rename Registry

Canonical record of filename changes. Stale references should be resolved using this table.

| Old Name | New Name | Location | Date |
|---|---|---|---|
| Spin_Chamber_v0.md | Gate_05_Separation_Thermal.md | Operations/ | 2026-05-15 |
| Material_Separation_Gate_v0.md | Gate_04_Separation_Mechanical.md | Operations/ | 2026-05-15 |
| Stratification_Chamber_v0.md | Gate_04_Separation_Mechanical.md | Operations/ | Prior cycle |
| Lazarus_forge_v0_flow.md | Forge_flow.md | Architecture/ | 2026-05-15 |
| Unknowns_LF.md | Unknowns.md | Root | 2026-05-15 |
| Trajectories_LF.md | Trajectories.md | Admin/ | 2026-05-15 |
| Component_Triage_System.md | Gate_02_Triage.md | Operations/ | 2026-05-15 |
| geck_forge_seed.md | Geck_forge_seed.md | Architecture/ | 2026-05-15 |
| energy_v0.md | Energy.md | Operations/ | 2026-05-15 |
| Air_Scrubber_v0.md | Air_Scrubber.md | Operations/ | 2026-05-15 |
| Support_Raft_v0.md | Support_Raft.md | Tests/ | 2026-05-15 |
| leviathan_testing.md | Leviathan_testing.md | Tests/ | 2026-05-15 |
| Ship_of_Theseus_Right_to_Repair.md | Ship_of_Theseus.md | Admin/ | 2026-05-15 |
| Electronics.md (root) | Electronics.md | Operations/ | 2026-05-20 |
| Canonical_Terms_LF.md | Canonical_Terms.md | Admin/ | 2026-05-26 |
| Engineering.md (replaced by) | Mechanical_Structures.md | Architecture/ | 2026-05-31 |
| economics_v0.md | Economics.md | Admin/ | 2026-06-05 |
| Precision_LF.md | Precision.md | Architecture/ | 2026-06-05 |
| Forge_flow.md | Forge_Flow.md | Architecture/ | Pending — RS-002 |

---

## Pending Corrections

Pending corrections have been migrated to `Unknowns.md` PC cluster (PC-001 through PC-004).
Discovery.md is a navigation map — task tracking belongs in Unknowns.md.

| ID | Summary | See |
|----|---------|-----|
| PC-001 | Verification Ref corrections — 10 files pointing to Forge_Audit_Kit.md | `Unknowns.md` §Pending Corrections |
| PC-002 | Upstream reference corrections — 7 files missing Facilities.md link | `Unknowns.md` §Pending Corrections |
| PC-003 | New file cross-reference corrections — 10 files missing 2026-06-06 file references | `Unknowns.md` §Pending Corrections |
| PC-004 | Stale name corrections — Challenges/Water.md and Planned_Obsolescence.md | `Unknowns.md` §Pending Corrections |

---

## Repository Maturity Snapshot

| File | Status | Spec Gates | Highest Risk |
|------|--------|-----------|--------------|
| `Admin/Governance_Charter.md` | Draft | 2/6 | High |
| `Admin/Ethical_Constraints.md` | Active | — | Critical |
| `Admin/Auditor_Protocols.md` | Active | — | Medium |
| `Admin/Forge_Audit_Kit.md` | Active | — | Low |
| `Admin/Verification_Gates_LF.md` | Draft | — | Low |
| `Admin/File_Template.md` | Active | — | — |
| `Admin/Canonical_Terms.md` | Active | — | Medium |
| `Admin/Engineer_Protocols.md` | Draft | — | Low |
| `Admin/Safety_Protocols.md` | Exploration | 0/6 | High |
| `Admin/Security_Protocols.md` | Draft | — | Critical |
| `Admin/Repository_Integrity_Protocol.md` | Draft | — | Critical |
| `Admin/Repository_Structure.md` | Exploration | 0/6 | Low |
| `Admin/Ship_of_Theseus.md` | Exploration | — | Low |
| `Admin/Trajectories.md` | Exploration | 1/6 | Medium |
| `Admin/Economics.md` | Exploration | 0/6 | Medium |
| `Admin/Governance_Migration_Protocol.md` | Exploration | 0/6 | High |
| `Admin/AUDIT_HARNESS.py` | Active | — | — |
| `Architecture/Forge_flow.md` | Exploration | — | High |
| `Architecture/Components.md` | Exploration | — | Low |
| `Architecture/Facilities.md` | Exploration | 0/6 | High |
| `Architecture/Geck_forge_seed.md` | Exploration | — | Low |
| `Architecture/Engineering.md` | Draft | — | Critical |
| `Architecture/Precision.md` | Exploration | 0/6 | High |
| `Architecture/Mechanical_Structures.md` | Draft | 1/6 | High |
| `Architecture/Thermal_Systems.md` | Draft | 0/6 | High |
| `Architecture/Friction_Dynamics.md` | Draft | 0/6 | High |
| `Architecture/Chemistry.md` | Draft | 0/6 | High |
| `Architecture/Cognitive_Frameworks.md` | Exploration | — | High |
| `Architecture/Forge_Net.md` | Exploration | — | Critical |
| `Operations/Gate_01_Intake.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_02_Triage.md` | Draft | 2/6 | High |
| `Operations/Gate_03_Reduction.md` | Exploration | 0/6 | High |
| `Operations/Gate_04_Separation_Mechanical.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_05_Separation_Thermal.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_06_Fabrication.md` | Exploration | 0/6 | Medium |
| `Operations/Gate_07_Utilization.md` | Exploration | 0/6 | Low |
| `Operations/Electronics.md` | Exploration | 0/6 | High |
| `Operations/Energy.md` | Exploration | 0/6 | Medium |
| `Operations/Air_Scrubber.md` | Draft | 2/6 | High |
| `Operations/Plastics.md` | Exploration | 0/6 | High |
| `Operations/Woodworking.md` | Draft | 0/6 | High |
| `Tests/Support_Raft.md` | Exploration | — | High |
| `Tests/Leviathan_testing.md` | Exploration | — | High |
| `Challenges/Water.md` | Active | — | — |
| `Challenges/Biofouling.md` | Active | — | — |
| `Challenges/Waste.md` | Active | — | — |
| `Challenges/Planned_Obsolescence.md` | Active | — | — |
| `Challenges/Critical_Minerals.md` | Active | — | — |
| `Challenges/Emergence.md` | Exploration | 0/6 | High |

---

## Scope Map — Root Files

### `Routing.md`
Programmatic lookup table. Raw content URLs and repository URLs for every file. Dual-audience: LLM context loading (raw) and human review (repo). Backlink anchor standard for all files.
**Upstream:** None — updated whenever files are added or renamed.
**Downstream:** All automated agents and CI systems; all files (backlink requirement).
> ℹ️ *Maintained separately from Discovery.md. Routing.md owns where; Discovery.md owns what and why.*

### `Unknowns.md`
Cross-module unknowns global index. Lean index only — full unknown entries live in file sidecars.
**Upstream:** All repository files (sidecar unknowns feed index).
**Downstream:** All audit contributors; Forge_Audit_Kit.md.

---

## Scope Map — Admin/

> Governance tier hierarchy: Tier 1 (Governance_Charter + Ethical_Constraints) →
> Tier 2 (Auditor_Protocols) → Tier 3 (Forge_Audit_Kit) →
> Support layer (all others).

### `Admin/Governance_Charter.md`
Constitutional root. Tier 1 Axioms (P-1–P-4, Q-1–Q-4); governance hierarchy; amendment doctrine.
**Upstream:** None.
**Downstream:** All repository files; Auditor_Protocols.md; Security_Protocols.md; Governance_Migration_Protocol.md.
⚠️ GOV-003 (integrity enforcement), GOV-005 (constitutional stability) — Critical.

### `Admin/Ethical_Constraints.md`
Co-Tier 1 control substrate. Anti-Weaponization Doctrine; Life Preservation; Pacifist Operating Posture.
**Upstream:** None.
**Downstream:** All repository files (Ethical Anchor field); Governance_Charter.md.
⚠️ EC-001 (confidence threshold), EC-002 (Anti-Weaponization pattern-matching), EC-003 (human escalation path) — all open.

### `Admin/Auditor_Protocols.md`
Tier 2 verification doctrine. 10-phase audit sequence; Fallacy Checklist; Sidecar Model; adversarial audit layer.
**Upstream:** Governance_Charter.md; Ethical_Constraints.md.
**Downstream:** Forge_Audit_Kit.md; Verification_Gates_LF.md; all repository files.
⚠️ AP-004 (cross-auditor disagreement resolution) — open.

### `Admin/Forge_Audit_Kit.md`
Tier 3 condensed audit reference. Derived from Auditor_Protocols.md. Load instead of full governance corpus to stay within token limits.
**Upstream:** Auditor_Protocols.md; Verification_Gates_LF.md.
**Downstream:** All audit contributors as operational reference.

### `Admin/Verification_Gates_LF.md`
Single canonical source for the six promotion gates (G1–G6).
**Upstream:** Auditor_Protocols.md; Governance_Charter.md.
**Downstream:** All repository files (Verification Ref field); Forge_Audit_Kit.md; Security_Protocols.md.
⚠️ VG-001 (synchronization authority chain) — blocks Specification promotion.

### `Admin/File_Template.md`
Standard file structure. Ten-section layout; Ethical Anchor field definition.
**Upstream:** Governance_Charter.md; Ethical_Constraints.md.
**Downstream:** All repository files.

### `Admin/Canonical_Terms.md`
Single source of truth for repository vocabulary. Anti-drift guardrails; banned terms.
**Upstream:** Governance_Charter.md; Forge_flow.md (gate logic terms authoritative there).
**Downstream:** All repository files; Auditor_Protocols.md; Security_Protocols.md.
⚠️ CT-002 (Component Library Schema) — blocks Gate_02_Triage.md promotion.

### `Admin/Engineer_Protocols.md`
Cognitive and procedural protocols for engineering contributors.
**Upstream:** Auditor_Protocols.md; Ethical_Constraints.md; Discovery.md.
**Downstream:** All engineering contributors; all Operations/ and Architecture/ domain files.
⚠️ EP-004 (engineering authority boundary), EP-005 (acceptable risk threshold — cross-reference Safety_Protocols.md) — open.

### `Admin/Safety_Protocols.md`
Physical operator safety doctrine. PPE by hazard class; hearing conservation; heat stress; acceptable risk threshold (resolves EP-005); incident reporting.
**Upstream:** Ethical_Constraints.md; Engineer_Protocols.md; Facilities.md (FA-004).
**Downstream:** All Operations/ gate files; Air_Scrubber.md (noise reference).
⚠️ SP-006 (emergency response procedures) — deferred to FA-001 resolution.

### `Admin/Security_Protocols.md`
Cryptographic enforcement layer. Multi-signature override verification; node identity; key rotation.
**Upstream:** Governance_Charter.md; Repository_Integrity_Protocol.md; Canonical_Terms.md; Electronics.md.
**Downstream:** Repository_Integrity_Protocol.md; Governance_Charter.md (GOV-006 resolution); all governance files.
⚠️ SEC-001 (quorum under partition), SEC-007 (external root-of-trust) — Critical.

### `Admin/Repository_Integrity_Protocol.md`
Operational integrity enforcement. Violation classification ladder; recovery procedures; automation migration path.
**Upstream:** Governance_Charter.md; Auditor_Protocols.md; Ethical_Constraints.md.
**Downstream:** Forge_Audit_Kit.md; AUDIT_HARNESS.py; Security_Protocols.md; Unknowns.md; Discovery.md.
⚠️ RIP-001 (Archive/ directory not yet created) — Critical. See Repository_Structure.md RS-003.

### `Admin/Repository_Structure.md`
Filename conventions; folder assignment doctrine; Archive/ directory doctrine; naming standard.
**Upstream:** Governance_Charter.md; File_Template.md.
**Downstream:** All repository files; Discovery.md (Rename Registry forward doctrine).
⚠️ RS-003 (Archive/ directory not yet physically created) — Medium.

### `Admin/Ship_of_Theseus.md`
Philosophical and legal defense for repair-first doctrine. Right-to-repair framework.
**Upstream:** Gate_02_Triage.md; Components.md.
**Downstream:** Gate_02_Triage.md; Geck_forge_seed.md.

### `Admin/Trajectories.md`
Version trajectory v0–v5. FRT doctrine and floor value. Scope routing for out-of-version capabilities.
**Upstream:** Governance_Charter.md; Energy.md; Geck_forge_seed.md.
**Downstream:** All operational and architecture files; Gate_07_Utilization.md; Economics.md.
⚠️ TR-001 (v1 profitability baseline) — blocks v0→v1 transition; Economics.md provides resolution framework.

### `Admin/Economics.md`
Dynamic resource doctrine. Buy what you need, sell what you don't. Barter doctrine (canonical owner). Market navigation framework. v1 profitability baseline framework (TR-001 resolution path).
**Upstream:** Trajectories.md (FRT doctrine); Gate_07_Utilization.md (cycle data); Energy.md (EV-001 cost input).
**Downstream:** Gate_07_Utilization.md (FRT accounting); Gate_06_Fabrication.md (input cost threshold).
⚠️ EC-002 (operating cost baseline) — blocks TR-001 closure; dependent on Energy.md EV-001.

### `Admin/Governance_Migration_Protocol.md`
Tier 1 Axiom amendment procedures. Two-track migration system. Engineer proposal; human ratification. Hard floor doctrine.
**Upstream:** Governance_Charter.md; Auditor_Protocols.md; Engineer_Protocols.md.
**Downstream:** All governance files (Track A); Governance_Charter.md (Track B amendment target).
⚠️ GMP-004 (ratification authentication) — mirrors GOV-006; SEC-007 resolution path.

---

## Scope Map — Architecture/

> **Vocabulary authority:** `Architecture/Forge_flow.md` is the operational
> vocabulary standard. For any undefined operational term, consult
> `Architecture/Forge_flow.md` §Defined Terms before `Admin/Canonical_Terms.md`.

> **Architecture reading order:**
> 1. `Forge_flow.md` — vocabulary and gate logic
> 2. `Components.md` — what must exist
> 3. `Facilities.md` — where it exists
> 4. `Geck_forge_seed.md` — how to seed it
> 5. `Engineering.md` — foundational principles
> 6. `Precision.md` — what the Forge can build to
> 7. `Mechanical_Structures.md` — fabrication machinery doctrine
> 8. `Thermal_Systems.md` — heat transfer and thermodynamics
> 9. `Friction_Dynamics.md` — fluid mechanics and tribology
> 10. `Chemistry.md` — electrochemistry and material chemistry
> 11. `Cognitive_Frameworks.md` — how it thinks
> 12. `Forge_Net.md` — how instances connect

### `Architecture/Forge_flow.md`
Master decision flow AND repository vocabulary standard. v0 gate logic; outcome paths; want/need policy; primary KPI.
**Upstream:** Canonical_Terms.md; Ethical_Constraints.md; Components.md.
**Downstream:** All repository files (Defined Terms); all Operations/ gate files; Forge_Net.md; Canonical_Terms.md.
⚠️ FL-001 (gate logic determinism at boundary cases) — blocks Specification promotion.

### `Architecture/Components.md`
Minimum component architecture. Critical/Useful/Bootstrap taxonomy; Bootstrap Doctrine; Graduation Rule.
**Upstream:** Forge_flow.md; Geck_forge_seed.md; Ethical_Constraints.md.
**Downstream:** Geck_forge_seed.md; Gate_02_Triage.md; all Operations/ gate files.
⚠️ CO-002 (metrology precision thresholds) — route to Precision.md PR-001.

### `Architecture/Facilities.md`
Minimum physical environment constraints. Nonburnable flooring prerequisite; airflow topology; triangle workstation principle; hazard zone separation; floor loading; utility access.
**Upstream:** Components.md; Engineering.md; Ethical_Constraints.md.
**Downstream:** All Operations/ gate files (siting prerequisite); Safety_Protocols.md (FA-004 heat stress).
⚠️ FA-001 (site not confirmed) — Critical; blocks all hot operations.

### `Architecture/Geck_forge_seed.md`
Minimum viable seed specification. 8 core G.E.C.K. modules; procurement doctrine; marine variant.
**Upstream:** Components.md; Forge_flow.md; Ethical_Constraints.md.
**Downstream:** Components.md; Trajectories.md; Precision.md.
⚠️ GK-005 — resolved by Architecture/Precision.md; update on next audit pass.

### `Architecture/Engineering.md`
Foundational engineering principles. Rules of thumb; safety factors; Arkansas climate derating; progressive engineering path.
**Upstream:** Ethical_Constraints.md; Engineer_Protocols.md.
**Downstream:** All Operations/ and Architecture/ domain files; Mechanical_Structures.md.
⚠️ EN-001 (validated safety factors for salvaged materials) — Critical; blocks structural specification.

### `Architecture/Precision.md`
Precision ceiling doctrine. T0–T4 tolerance tier system (repository-wide standard). Metrology doctrine (resolves CO-002). Salvage equipment derating. Fabrication-precision feedback loop.
**Upstream:** Engineering.md; Mechanical_Structures.md; Ethical_Constraints.md.
**Downstream:** Gate_06_Fabrication.md; Gate_07_Utilization.md; Mechanical_Structures.md (ME-001); Components.md (CO-002).
⚠️ PR-001 (precision ceiling not declared) — blocks T1/T2 part claims. PR-004 (backlash characterization) — prerequisite for PR-001.

### `Architecture/Mechanical_Structures.md`
Salvaged-frame kinematic and structural doctrine. Gantry rigidity; kinematic interlock matrix; bearing contamination; MTBMF metric.
**Upstream:** Engineering.md; Ethical_Constraints.md; Friction_Dynamics.md; Thermal_Systems.md.
**Downstream:** All fabrication machinery specifications.
⚠️ ME-001 (resonance mapping on salvaged rails) — interlock thresholds provisional until Precision.md PR-001 resolves.

### `Architecture/Thermal_Systems.md`
Foundational thermal doctrine. Thermodynamic laws; heat transfer; Peltier; TEG; heat pump; Arkansas climate thermal baseline.
**Upstream:** Engineering.md; Ethical_Constraints.md.
**Downstream:** Gate_05_Separation_Thermal.md; Air_Scrubber.md; Energy.md; Plastics.md; Mechanical_Structures.md; Support_Raft.md; Water.md.
⚠️ TH-001 (heat pump sizing), TH-003 (atmospheric moisture yield — Blocking for Living Waters).

### `Architecture/Friction_Dynamics.md`
Fluid mechanics, aerodynamics, and tribology doctrine. Reynolds number; Bernoulli; Darcy-Weisbach; hydrodynamics; Stribeck curve; lubrication selection.
**Upstream:** Engineering.md; Ethical_Constraints.md.
**Downstream:** Air_Scrubber.md; Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Support_Raft.md; Leviathan_testing.md; Mechanical_Structures.md; Biofouling.md; Water.md; Woodworking.md.
⚠️ FD-001 (Gate_04 RPM-to-fluid-doctrine), FD-002 (Air Scrubber duct velocity), FD-003 (salvaged bearing L10) — open.

### `Architecture/Chemistry.md`
Foundational chemical and electrochemical doctrine. Galvanic series; corrosion types; cathodic protection; redox; battery chemistry; polymer degradation; field contamination identification.
**Upstream:** Engineering.md; Thermal_Systems.md; Friction_Dynamics.md; Ethical_Constraints.md.
**Downstream:** Plastics.md; Electronics.md; Air_Scrubber.md; Gate_05_Separation_Thermal.md; Gate_03_Reduction.md; Energy.md; Support_Raft.md; Biofouling.md; Mechanical_Structures.md; Gate_01_Intake.md; Gate_02_Triage.md; Woodworking.md.
⚠️ CE-003 (Beilstein validation) — safety-critical prerequisite before first hot pyrolysis run.

### `Architecture/Cognitive_Frameworks.md`
Distributed cognition and autonomous safety. Cognitive reliability layers (0–6); confidence collapse states; rogue node containment; AI consensus structures.
**Upstream:** Ethical_Constraints.md; Electronics.md; Auditor_Protocols.md.
**Downstream:** Forge_Net.md; Leviathan_testing.md; Support_Raft.md; Trajectories.md.
⚠️ CF-001 (hardware watchdog standard) — blocks Specification-level autonomous architecture. CF-002 (correlated AI failure modes) — High risk.

### `Architecture/Forge_Net.md`
Decentralized data and physical network. Local-primary doctrine; cluster formation; trust weighting; data privacy classification.
**Upstream:** Gate_01_Intake.md; Cognitive_Frameworks.md; Ethical_Constraints.md; Leviathan_testing.md; Energy.md.
**Downstream:** Inter-forge logistics files; Trajectories.md.
⚠️ FN-001 (data validation criteria), FN-005 (data privacy) — Critical; both block first network connection.

---

## Scope Map — Operations/Gates

> **Gate flow:** G01 → G02 → G03 → G04 → G05 → G06 → G07
> **Feedback loops:** G07→G02, G07→G06, G06→Components, G02→G04/G06
> Gate files define *how*; Forge_flow defines *what* and *when*.

### `Operations/Gate_01_Intake.md`
Entry point. Safety screening; provenance tagging; parts list generation; handoff to Gate_02.
**Upstream:** Forge_Net.md; Ethical_Constraints.md; Forge_flow.md; Facilities.md.
**Downstream:** Gate_02_Triage.md; Forge_Net.md.
⚠️ GI-001 (reference database content), GI-002 (energetic discharge doctrine) — highest risk.

### `Operations/Gate_02_Triage.md`
Decision gateway between reuse and destruction. Five triage stations; Strategic Recoverability tiers; queue economics.
**Upstream:** Gate_01_Intake.md; Forge_flow.md; Components.md; Ethical_Constraints.md.
**Downstream:** Gate_03_Reduction.md; Gate_04_Separation_Mechanical.md; Gate_06_Fabrication.md; Ship_of_Theseus.md.
⚠️ CT-002 (Component Library Schema) — blocking.

### `Operations/Gate_03_Reduction.md`
Only fully irreversible step. Reduction doctrine; method selection; contamination discovery; emergency shutdown.
**Upstream:** Gate_02_Triage.md; Forge_flow.md; Gate_01_Intake.md; Air_Scrubber.md; Facilities.md.
**Downstream:** Gate_04_Separation_Mechanical.md; Air_Scrubber.md.

### `Operations/Gate_04_Separation_Mechanical.md`
Upstream mechanical separation. Rotor; sensors; fail-to-bin; Bootstrap Proxy Mode; Material Diversion Rate ≥30%.
**Upstream:** Gate_03_Reduction.md; Forge_flow.md; Air_Scrubber.md; Facilities.md.
**Downstream:** Gate_05_Separation_Thermal.md; Gate_02_Triage.md (Unknown Bulk); Gate_06_Fabrication.md.

### `Operations/Gate_05_Separation_Thermal.md`
Primary thermal processing (Spin Chamber). Induction heating; slow rotation; electromagnetic field; wire extrusion interface.
**Upstream:** Gate_04_Separation_Mechanical.md; Forge_flow.md; Energy.md; Facilities.md.
**Downstream:** Gate_06_Fabrication.md; wire extrusion interface (future).
⚠️ SC-005 (drive system geometry) — Critical prerequisite for dynamic analysis.

### `Operations/Gate_06_Fabrication.md`
Constructive stage. Arc welding as v0 gatekeeper; add-to-excess and mill-to-spec; welding wire qualification; operator safety.
**Upstream:** Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Components.md; Forge_flow.md; Facilities.md; Precision.md.
**Downstream:** Gate_07_Utilization.md; Components.md (fabricated parts feed Component Library).
⚠️ GF-003 (machining hardware), UNK-008 (welding wire qualification) — unassigned.

### `Operations/Gate_07_Utilization.md`
After-action review. Performance logging; failure capture; feedback to Gate_06; FRT per-cycle logging; retirement handoff.
**Upstream:** Gate_06_Fabrication.md; Forge_flow.md; Trajectories.md; Economics.md.
**Downstream:** Gate_02_Triage.md (retirement); Gate_06_Fabrication.md (feedback); Forge_Net.md; Forge_flow.md.
⚠️ GU-005 (FRT cycle definition not declared) — blocks FRT logging start.

---

## Scope Map — Operations/Domain

### `Operations/Electronics.md`
Trust-anchor for all electronic systems. Logic-Zero wipe; TMR hardware; hardware watchdog; counterfeit detection; BFR doctrine.
**Upstream:** Cognitive_Frameworks.md; Ethical_Constraints.md; Gate_02_Triage.md; Forge_flow.md; Facilities.md.
**Downstream:** Air_Scrubber.md; Gate_05_Separation_Thermal.md; Leviathan_testing.md; Support_Raft.md; Security_Protocols.md; Cognitive_Frameworks.md.
⚠️ EL-006 (cryptographic key management) — unassigned.

### `Operations/Energy.md`
Energy strategy. Power Demand stub (Bootstrap ~2–5 kW, Nominal ~15–40 kW, Degraded ~1–3 kW). Cross-reference anchor for all energy accounting.
**Upstream:** Trajectories.md; Gate_07_Utilization.md.
**Downstream:** All Operations/ gate files; Leviathan_testing.md; Trajectories.md; Plastics.md; Woodworking.md.
⚠️ EV-001 (Forge demand baseline) — In Progress; blocks v1 operating cost model and Economics.md EC-002.

### `Operations/Air_Scrubber.md`
Enabling system — without it the Forge does not operate. Five-stage architecture; negative pressure doctrine; marine variant.
**Upstream:** Gate_05_Separation_Thermal.md; Gate_04_Separation_Mechanical.md; Electronics.md; Plastics.md; Woodworking.md.
**Downstream:** Leviathan_testing.md; Gate_02_Triage.md; Energy.md; Geck_forge_seed.md.
⚠️ AS-003 (saturation threshold calibration) — blocks chemistry validation.

### `Operations/Plastics.md`
Polymer triage and pyrolysis framework. Triage routing; low-pressure thermal depolymerization; off-gas containment. Pyrolysis is last-resort, not primary.
**Upstream:** Gate_01_Intake.md; Gate_02_Triage.md; Gate_03_Reduction.md; Air_Scrubber.md.
**Downstream:** Gate_06_Fabrication.md; Energy.md; Gate_05_Separation_Thermal.md; Gate_02_Triage.md.
⚠️ PL-001 (halogenated polymer detection) — Critical and Blocking before any hot operational run.

### `Operations/Woodworking.md`
Full wood processing chain. Salvaged and urban timber; drying doctrine; CNC fixturing; heat treatment; waste valorization.
**Upstream:** Gate_02_Triage.md; Gate_03_Reduction.md; Engineering.md; Facilities.md.
**Downstream:** Gate_06_Fabrication.md; Air_Scrubber.md; Energy.md; Trajectories.md.

---

## Scope Map — Tests/

### `Tests/Support_Raft.md`
Stationary marine anchor for Leviathan units. SWATH hull; Sacrificial Shell System; induction charging; Local Truth Cache; Stasis Mode.
**Upstream:** Gate_04_Separation_Mechanical.md; Leviathan_testing.md; Energy.md; Ethical_Constraints.md; Geck_forge_seed.md; Trajectories.md.
**Downstream:** Leviathan_testing.md; Electronics.md.
⚠️ SR-001 (galvanic corrosion mitigation) — High; blocks v1 design.

### `Tests/Leviathan_testing.md`
Hostile-environment test framework. Fail fast; recover often; sensors lie; record everything. Autonomy constraints; ethical absolute limits; Leviathan Extensions Framework.
**Upstream:** Cognitive_Frameworks.md; Ethical_Constraints.md; Energy.md; Support_Raft.md; Electronics.md.
**Downstream:** Cognitive_Frameworks.md; Forge_Net.md; Energy.md; Trajectories.md.
⚠️ LT-001 (power envelope), LT-002 (deep-ocean storage degradation), LT-003 (autonomy architecture unspecified) — High risk. LT-006 (ethical log survival under unit loss) — governance implications.

---

## Scope Map — Challenges/

> Challenges/ files define problems and requirements. They do not freeze solutions.

### `Challenges/Water.md`
Water scarcity and contamination. Living Waters initiative. Engineering requirements; current Forge approaches; community water sovereignty.
**Upstream:** Gate_05_Separation_Thermal.md; Gate_04_Separation_Mechanical.md; Energy.md.
**Downstream:** Operations/ remediation applications (when developed).
⚠️ Footer cross-references stale — update per Rename Registry.

### `Challenges/Biofouling.md`
Biological colonization and MIC. Kinetic and ultrasonic disruption; biomimetic surfaces; sacrificial anodes. Non-toxic remediation doctrine.
**Upstream:** Gate_04_Separation_Mechanical.md; Plastics.md; Support_Raft.md; Ethical_Constraints.md.
**Downstream:** Support_Raft.md; Leviathan_testing.md; Gate_05_Separation_Thermal.md.

### `Challenges/Waste.md`
Discretionary waste and erosion of repair capacity. Automated triage; community drop-off nodes; distributed utility return loops.
**Upstream:** Gate_01_Intake.md; Gate_02_Triage.md; Plastics.md; Woodworking.md; Support_Raft.md.
**Downstream:** Gate_02_Triage.md; Gate_06_Fabrication.md; Forge_Net.md.

### `Challenges/Planned_Obsolescence.md`
Deliberate unrepairability. Thermal de-manufacturing; Logic-Zero wipe; standardized geometry upcycling.
**Upstream:** Electronics.md; Gate_02_Triage.md; Plastics.md; Gate_05_Separation_Thermal.md.
**Downstream:** Electronics.md; Gate_06_Fabrication.md; Ship_of_Theseus.md.
⚠️ Stale names — update per Rename Registry.

### `Challenges/Critical_Minerals.md`
Rare earth and critical mineral supply chain concentration. Urban mining doctrine; selective induction recovery; real-time material assay.
**Upstream:** Gate_02_Triage.md; Gate_04_Separation_Mechanical.md; Gate_05_Separation_Thermal.md; Electronics.md.
**Downstream:** Gate_06_Fabrication.md; Forge_Net.md; Trajectories.md.

### `Challenges/Emergence.md`
Emergent intelligence and alignment-by-environment design. Phase-shift framing; eight engineering requirements; game-theoretic scaffolding; Logic-Zero reset; constitutional corrigibility architecture. First Challenges/ file built to full File_Template.md standard — reference implementation for future Challenges/ retrofit passes.
**Upstream:** Ethical_Constraints.md; Governance_Charter.md (Q-3); Cognitive_Frameworks.md (CF-001, CF-002, Section IX); Electronics.md; Auditor_Protocols.md.
**Downstream:** Cognitive_Frameworks.md (CF-001, CF-002, Section IX); Forge_Net.md; Leviathan_testing.md; Support_Raft.md; Verification_Gates_LF.md.
⚠️ EM-001 (behavioral opacity detection threshold) — High; blocks watchdog specification. EM-004 (governance substrate integrity under emergent agent access) — Critical; mirrors GOV-003, SEC-007.

---

## Cross-Repo Relationship

`LazarusForgeV0` (this repo) — operational implementation.
`Astroid-miner` — planned; activates when Leviathan deployment is underway.


**Programmatic entry point:** `Routing.md` is the canonical lookup table for raw file URLs.
Load Routing.md first when an agent needs to fetch specific files by path.
Load Discovery.md when an agent needs to understand scope relationships and routing logic.
The two files are complementary — Routing.md owns *where*, Discovery.md owns *what and why*.

---

## Cross-Module Unknowns — Attention Required

Full entries live in `Unknowns.md`. This table is a routing index only.

| Unknown | Status | See |
|---------|--------|-----|
| UNK-006 — Facility siting | **Resolved** — `Architecture/Facilities.md` owns; PC-002 tracks reference corrections | `Unknowns.md` |
| UNK-008 — Welding wire chemical qualification | Open — no owner assigned | `Unknowns.md` |
| UNK-009 — External root-of-trust cross-module | Critical — spans GOV-003, GOV-005, RIP-001, SEC-007 | `Unknowns.md` |
| FA-001 — Site not confirmed | Critical — blocks all hot operations | `Unknowns.md` |
| EC-002 — Operating cost baseline | Critical — blocks TR-001; depends on EV-001 | `Unknowns.md` |
| PR-001 — Precision ceiling not declared | Critical — blocks T1/T2 part claims | `Unknowns.md` |
| RS-003 — Archive/ directory not created | Blocking — blocks RIP-001 full closure | `Unknowns.md` |
| PC-001 — Verification Ref corrections | Blocking — 10 files; affects AUDIT_HARNESS.py | `Unknowns.md` |

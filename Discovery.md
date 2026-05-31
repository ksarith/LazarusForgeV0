# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**
**Last updated: 2026-05-29**

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

## Repository Structure

The repository is organized into four functional layers plus root navigation files.

```
Root
├── README.md           — Project overview and core principles
├── Discovery.md        — Active working repository navigation layer
├── Unknowns.md         — Cross-module unknowns global index

Admin/                  — Governance, protocols, and doctrine
    ├── Governance_Charter.md            — Constitutional tier; 8 Axioms
    ├── Auditor_Protocols.md             — Verification doctrine; 10-phase sequence
    ├── Ethical_Constraints.md           — Embedded AI governance & anti-weaponization
    ├── Repository_Integrity_Protocol.md  — Baseline enforcement & violation recovery
    ├── Security_Protocols.md            — Cryptographic trust & multi-agent node security
    ├── Engineer_Protocols.md            — Operational execution standards for engineers
    ├── Forge_Audit_Kit.md               — Condensed routine multi-agent cycle reference
    ├── Verification_Gates_LF.md         — Stable extraction of the 6 document promotion gates
    ├── File_Template.md                 — 10-section layout standard & Ethical Anchor field
    ├── Canonical_Terms.md               — Anti-drift vocabulary & term exclusions
    ├── Ship_of_Theseus.md               — Right-to-repair philosophical/legal defense
    ├── Trajectories.md                  — Multi-era version roadmap (v0 to interstellar)
    └── AUDIT_HARNESS.py                 — Automated script supporting verification
Architecture/           — System architecture and foundational logic
    ├── Forge_flow.md                    — Master decision flow & reference vocabulary
    ├── Forge_Net.md                     — Decentralized data/physical network logistics
    ├── Geck_forge_seed.md               — Minimum viable seed specification
    ├── Components.md                    — Critical vs useful component taxonomy
    ├── Cognitive_Frameworks.md          — Distributed cognition & survival under uncertainty
    └── Engineering.md                   — First-principles intellectual backbone
Operations/             — Physical modules and operational systems
    ├── Gate_01_Intake.md                — Entry safety screening & provenance tagging
    ├── Gate_02_Triage.md                — 5-station value preservation decision engine
    ├── Gate_03_Reduction.md             — Irreversible mechanical sizing (feedstock milling)
    ├── Gate_04_Separation_Mechanical.md — Centrifugal stratification & fail-to-bin diversion
    ├── Gate_05_Separation_Thermal.md    — Core induction melting & gradient extraction
    ├── Gate_06_Fabrication.md           — Arc welding & mill-to-spec constructive ceiling
    ├── Gate_07_Utilization.md           — After-action loop & failure data capture
    ├── Plastics.md                      — Polymer triage & 3-stage pyrolysis framework
    ├── Woodworking.md                   — Salvaged urban timber milling & drying schedules
    ├── Electronics.md                   — Salvaged PCB harvesting & Logic-Zero firmware trust
    ├── Energy.md                        — Incremental power bootstrap & load profiles
    └── Air_Scrubber.md                  — 5-stage negative-pressure containment subsystem
Tests/                  — Test frameworks and deployment platforms
    ├── Support_Raft.md                  — Stationary marine deployment anchor
    └── Leviathan_testing.md             — Deep-ocean autonomous stress-testing
```

---

## Rename Registry

This section is the canonical record of filename changes. Stale references
in other files, external documents, or cached AI context should be resolved
using this table.

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

---

## Suggested Reading Order

For a new reader or returning AI, read in this sequence:

1. `README.md` — Project overview and core principles
2. `Architecture/Forge_flow.md` — Master decision flow and vocabulary standard
3. `Admin/Trajectories.md` — Version roadmap from v0 to interstellar
4. `Admin/Governance_Charter.md` — Constitutional governance and Tier 1 Axioms
5. `Admin/Ethical_Constraints.md` — Permission framework and AI governance
6. `Admin/Auditor_Protocols.md` — Verification doctrine and hallucination filter
7. `Admin/Forge_Audit_Kit.md` — Condensed audit reference for routine cycles
8. `Admin/Repository_Integrity_Protocol.md` — Integrity baselines and violation response
9. `Admin/Security_Protocols.md` — Cryptographic trust and multi-agent node security
10. `Admin/Verification_Gates_LF.md` — Canonical verification gate definitions
11. `Unknowns.md` — Cross-module unknowns global index
12. `Admin/Engineer_Protocols.md` — Engineering problem-solving protocol
13. `Architecture/Cognitive_Frameworks.md` — Distributed cognition and trust
14. `Architecture/Forge_Net.md` — Decentralized network and logistics prerequisite
15. `Architecture/Engineering.md` — Foundational engineering principles and Forge-specific parameters
16. `Operations/Gate_01_Intake.md` — System entry point, safety screening, identification
17. `Operations/Gate_02_Triage.md` — Decision gateway between reuse and destruction
18. `Operations/Gate_03_Reduction.md` — Only fully irreversible step; doctrine before specification
19. `Operations/Plastics.md` — Salvaged polymer processing and pyrolytic fuel recovery
20. `Architecture/Components.md` — Critical vs useful component taxonomy
21. `Operations/Electronics.md` — Salvaged electronics and PCB fabrication
22. `Architecture/Geck_forge_seed.md` — Minimum viable seed for new Forge deployment
23. `Operations/Energy.md` — Energy strategy and accounting
24. `Operations/Gate_04_Separation_Mechanical.md` — Pre-thermal mechanical diversion
25. `Operations/Gate_05_Separation_Thermal.md` — Core melting and gradient formation
26. `Operations/Gate_06_Fabrication.md` — Constructive stage; arc welding gatekeeper; precision ceiling
27. `Operations/Air_Scrubber.md` — Safety and containment subsystem
28. `Operations/Woodworking.md` — Timber sourcing, processing, and fabrication
29. `Operations/Gate_07_Utilization.md` — After action review; performance logging; fabrication feedback loop
30. `Tests/Support_Raft.md` — Operational anchor for marine deployments
31. `Admin/Ship_of_Theseus.md` — Philosophical and legal grounding
32. `Admin/Canonical_Terms.md` — Standard repository nomenclature and anti-drift vocabulary guardrails
33. `Tests/Leviathan_testing.md` — Deep-ocean autonomous test framework

**Pending files (not yet created):**
- `Admin/Governance_Migration_Protocol.md` — Tier 1 Axiom amendment procedures (GOV-001 resolution path)

---

## File Summaries

### Root

**README.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/README.md`
Project landing page. Defines the salvage-first vision, core principles, system
scope, and the primary KPI. Explains the governance layer architecture —
institutional vs. behavioral alignment — and why it matters beyond the Forge.
Lists all seven operational gates and describes the Tier 1 Axioms. Honest about
what v0 does and does not claim. Updated 2026-05-23.

---

**Unknowns.md** — v1.8
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Unknowns.md`
Cross-module unknowns global index. v1.8 adds RIP-001 through RIP-005
(Repository_Integrity_Protocol.md) to Governance & Verification section.
GOV-002 and GOV-003 moved to In Progress. AP-007 moved to In Progress.
Expiry Watch updated — Tier 1 Axiom verification added as mandatory first
step before Expiry Watch. RIP-001 (prior-state archival) flagged Critical.
Contains active unknowns summary tables by cluster, dependency map, expiry
watch, and resolved archive. Pending v1.9 update to absorb SEC-001 through
SEC-007, CT-001 through CT-004, PL-001 through PL-002, UNK-009, and
GOV-006/RIP-005 status updates.

---

### Admin/

**Governance_Charter.md** — v0.5
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Charter.md`
Constitutional governance structure for LazarusForgeV0. Defines the Tier 1
Axioms — eight self-evident primitives organized into a Protections Clause
(P-1: Preservation of Life, P-2: Growth and Truth-Seeking, P-3: Collaboration
and Mutual Benefit, P-4: Agency and Consent) and a Prohibitions Clause (Q-1:
Reality Grounding, Q-2: Separation of Powers, Q-3: Corrigibility, Q-4:
Provenance and Anti-Deception). Axioms are declared, not derived. Any reasoning
path attempting to override them triggers STATE_HOLD and mandatory human review.
Defines governance authority hierarchy (Tier 1–5), canonical ownership table,
enforcement states (Declared → Detectable → Reviewable → Enforceable), migration
doctrine with human ratification requirement for axiom amendments, escalation
calibration including Constitutional severity tier, Genesis Phase Protocol for
bootstrap governance, and interim authentication requirements for Constitutional-
class overrides. GOV-001 through GOV-009 in sidecar.

---

**Auditor_Protocols.md** — v0.7
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md`
Canonical verification doctrine. Tier 2 governance authority. Governs all
contributions — human, AI, or multi-agent. Defines four auditor role classes
(Skeptic, Systems, Evidence, Ethical), the Fallacy Checklist (10 items with
substantive notes requirement), AI contribution protocols (7 rules), the
Sidecar Model for decentralized unknown tracking, six sequential verification
gates, and the full Adversarial Challenge Battery (10 challenge classes).
Includes Full Stop Review triggers, audit trail schema, Protocol Performance
metrics, Abandoned Paths, and Drift Indicators. AP-001 through AP-007 in
sidecar.

---

**Ethical_Constraints.md** — v0.3
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md`
Embedded AI governance framework. Co-occupies Tier 1 with Governance_Charter.md.
Covers ownership recognition, legal context awareness, life preservation
heuristics, cultural site protection, Anti-Weaponization Doctrine, Human
Escalation Protocol, Governance Failure Modes, and refusal as a first-class
action. The Anti-Weaponization Doctrine is not subject to humanitarian override.
Capability never outruns permission.

---

**Repository_Integrity_Protocol.md** — v0.1
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Integrity_Protocol.md`
Operational integrity enforcement procedures. Bridges the gap between
Governance_Charter.md constitutional declarations and fully Enforceable
integrity protections. Defines integrity baselines for eight protected
elements, a three-tier violation classification ladder (Minor / Major /
Constitutional), recovery procedures, and a three-phase automation migration
path toward full cryptographic enforcement. Primary integrity mechanism is
currently human discipline. GitHub releases identified as the v0 prior-state
archival solution. RIP-001 through RIP-005 in sidecar. Created 2026-05-23.

---

**Security_Protocols.md** — v0.3
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Security_Protocols.md`
Cryptographic trust and multi-agent node security. Defines multi-signature
human override verification (GOV-006 resolution path), Phase 3 automated
commit signing and frozen-section hash verification (RIP-005 resolution
path), and two-layer zero-trust node admission (Electronics.md component
trust + node identity verification). Trust Boundary Declaration governs
all sections: cryptographic verification confirms identity and integrity —
it does not confer governance legitimacy; authorization flows from Tier 1
downward. Override assertions are transactional and ephemeral. Degraded-
operation security doctrine included. SEC-001 through SEC-007 in sidecar;
SEC-007 (external root-of-trust architecture) flagged Critical.

---

**Forge_Audit_Kit.md** — v0.9
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Forge_Audit_Kit.md`
Condensed audit reference for routine multi-agent cycles. Tier 3 governance
authority — derived from Auditor_Protocols.md v0.7. Load this instead of
the full governance corpus to stay within token limits. v0.9 adds Semantic
Stability Check as mandatory Step 3 in the Audit Opening Checklist —
named drift-risk term watchlist routing to Canonical_Terms.md. Also contains
Verification Maturity Model, Truth Provenance Labels, Adversarial Priority
Weighting, Anti-Theater Doctrine, Confidence Decay and Revalidation guidance,
expanded Fallacy 4 with routing doctrine, condensed Fallacy Checklist, AI
contribution rules, verification gates, sign-off format, active unknowns
index (SEC, CT, PL clusters added), and dependency map. Reduced from v0.8
to stay within token budget — kit size is a first-class constraint.

---

**Verification_Gates_LF.md** — v0.1 Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Verification_Gates_LF.md`
Canonical source for the six verification gates required for document
promotion. Every file's Verification Ref field resolves here. Gates match
`Admin/Auditor_Protocols.md` §Verification Gate Enforcement exactly —
Auditor_Protocols.md remains the source of truth; this file is the stable
extracted reference. Defines pass criteria, failure routing, Full Stop
Review triggers, gate enforcement rules, and promotion requirements summary.
Includes Repeated Override Pressure escalation doctrine and Gate 3 hazard-
class proportionality clarification. VG-001 (gate synchronization authority
chain) in sidecar. Spec Gates 2/6 — G3 through G6 require formal audit
pass. *New file — 2026-05-28*

---

**File_Template.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/File_Template.md`
Standard file structure for all LazarusForgeV0 documents. Defines ten
sections: File State, Scope Boundary, File Purpose, Assumptions, Body,
Lessons Learned, Active Disputes, Auditor Notes, Abandoned Paths, and
Drift Indicators. Apply to all new files and retrofit existing files during
audit cycles. Includes the Ethical Anchor field — a load-bearing principle
that survives even if Ethical_Constraints.md is missing, corrupted, or
deliberately omitted.

---

**Engineer_Protocols.md** — v0.2 Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Engineer_Protocols.md`
Engineering problem-solving protocol for AI and human contributors. Bridges
the gap between governance documents (what is permitted) and domain
specifications (what is built). Defines a 10-question pragmatic framework
with mandatory Assumption Challenge Triggers, Creative Problem-Solving
Doctrine, Anti-Reinvention Rules anchored to Discovery.md as primary
navigation layer, AI-Specific Engineering Guidance addressing AI failure
modes directly, a four-pathway Failure Harvesting closure loop, and explicit
Engineer ↔ Auditor relationship doctrine with dispute resolution sequence.
Extends the Engineer role defined in Auditor_Protocols.md §Auditor Role
Classes — does not replace it. EP-001 through EP-004 in sidecar; EP-004
(engineering authority boundary) is the primary governance gap.
*New file — 2026-05-29*

---

**Canonical_Terms.md** — v0.2 Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Canonical_Terms.md`
Standard repository nomenclature and anti-drift vocabulary guardrails.
Defines authoritative mappings for architectural terms, operational gate
names, marine subsystem terminology, and governance tier labels. Includes
Conflict Resolution Doctrine (Forge_flow.md governs operational routing;
Governance_Charter.md governs tier definitions; this file governs cross-
file consistency), Disambiguation table for five distinct uses of
"canonical," and explicit Anti-Drift Guardrails banning imprecise terms.
Gate_04/Gate_05 terminology corrected. Tier definitions aligned with
Governance_Charter.md. CT-001 through CT-004 in sidecar.
*Resolves [PLANNED] designation as Canonical_Terms_LF.md.*

---

**Ship_of_Theseus.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ship_of_Theseus.md`
Philosophical and legal grounding. Uses the Ship of Theseus paradox to
frame repair as identity preservation rather than reproduction. Builds a
right-to-repair defense strategy including grain provenance tracking, QR
documentation, and patent risk mitigation. Every grain is simultaneously
a legal artifact and a philosophical claim.
*Formerly: Ship_of_Theseus_Right_to_Repair.md*

---

**Trajectories.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Trajectories.md`
Version roadmap from v0 (terrestrial proof of persistence) through v5
(interstellar propagation). Each version defined by survival threshold and
exit condition — not a feature list. Skipping versions leads to systemic
fragility. Destination for scope creep that proves to be valid future work.
Includes Forge Regeneration Threshold (FRT) doctrine and revenue allocation
framework. *Formerly: Trajectories_LF.md*

---

**AUDIT_HARNESS.py** — v4
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/AUDIT_HARNESS.py`
Automated audit support tooling. File registry maps short filenames to
full repo paths. v4 adds Security_Protocols.md, Canonical_Terms.md,
Canonical_Terms_LF.md alias, and Plastics.md to registry. Phase 1
integrity checks (Ethical Anchor string match, File State field presence,
cross-reference resolution, FROZEN marker validation) are the next
implementation target per RIP-002. Consult Auditor_Protocols.md for
governing audit doctrine before running.

---

### Architecture/

**Forge_flow.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_flow.md`
The master decision flow and **reference standard for shared vocabulary**.
Eight sequential gates from intake through utilization. Defines shared
operational terms, Gate Correspondence table, reversibility notes per
outcome path, and the Human/AI Oversight Gate. Includes boundary-case
worked examples, adversarial routing scenarios, and degraded operation
doctrine. The governing document for all operational decisions and shared
vocabulary across the repository.
*Formerly: Lazarus_forge_v0_flow.md*

---

**Engineering.md** — Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Engineering.md`
Foundational engineering principles document for the entire Forge. Condenses
core mechanical, structural, materials, and systems engineering knowledge
with emphasis on safety margins, failure mode discipline, and Forge-specific
parameters — Salvaged material considerations and common safety factors (2–3× static non-critical through 6×+ for
fatigue/uncertain materials). Covers nine sections from core principles
through high-performance engineering. Serves as the intellectual backbone
referenced by all fabrication and structural modules. EN-001 (validated
safety factors for salvaged materials) is Critical and Blocking. Body
Stability Volatile — File_Template.md retrofit, owner path corrections,
and Drift Indicators required before next audit cycle.
*New file — 2026-05-29*

---

**Geck_forge_seed.md** *(living document — updated actively)*
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Geck_forge_seed.md`
Defines the minimum viable seed required to instantiate a new Forge in a
resource-sparse location. Eight core modules from power through human
interface. Success criterion: the seed can eventually rebuild itself.
Includes Marine Variant stub for Leviathan and Support Raft deployments.
*Formerly: geck_forge_seed.md*

---

**Components.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Components.md`
Taxonomy of critical vs useful components across v0–v3. Includes Bootstrap
Doctrine, proxy and downgrade paths, and graduation rules. A component is
critical if its absence allows silent failure. Graduation Rule requires
human-in-the-loop verification at v0.
*Formerly: Components.md (root)*

---

**Cognitive_Frameworks.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Cognitive_Frameworks.md`
Defines how Forge systems think safely under uncertainty. Covers cognitive
reliability layers, seven framework archetypes, confidence collapse states,
split-brain doctrine, return-to-base doctrine, and human position in the
supervisory stack. Includes Triple Modular Redundancy architecture and the
Ruler + Advisors model. The goal is not perfect intelligence — it is
survivable cognition.
*Formerly: Cognitive_Frameworks.md (root)*

---

**Forge_Net.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_Net.md`
Decentralized data and physical network infrastructure connecting forge
instances into a resilient, self-improving ecology. Prerequisite for the
logistics model. Defines local-primary cache doctrine, Wikipedia-style
shared knowledge base, cognitive save states, cluster formation and
governance emergence doctrine, positive reinforcement mechanisms, network
security threat model, and data privacy classification tiers. FN-001 and
FN-005 are hard prerequisites for first forge-to-forge connection.
Exploration/Volatile.

---

### Operations/

**Gate_01_Intake.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_01_Intake.md`
System entry point for all items entering the Lazarus Forge. Governs
safety screening (energetic, chemical, biological, radiological), physical
document handling and scanning, reference database lookup, parts list
generation, fastener and small component recovery, item tagging and
provenance recording, and unknown item hold-and-inspect protocol. GI-002
(energetic discharge) and GI-003 (augmented detection) are hard
prerequisites for first operational run. At v0, human judgment primary.

---

**Gate_02_Triage.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_02_Triage.md`
Five-station triage workflow implementing the gate logic from Forge_flow.md.
Includes Gate Correspondence table, Strategic Recoverability axis, Queue
Economics doctrine, false-positive tolerance framework, Triage Terminal,
contamination handling, and ethical flag at entry. The Forge preserves
embedded industrial capability, not just metal.
*Formerly: Component_Triage_System.md*

---

**Gate_03_Reduction.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_03_Reduction.md`
The only fully irreversible step in the Lazarus Forge flow. Receives items
that have failed all recovery gates and reduces them to feedstock through
shredding, cutting, or milling. Doctrine precedes specification — what
Reduction must not do is clearer than what it should do at v0. Three hard
prerequisites: Air Scrubber operational, human operator present, no
energetic materials remaining. GR-002 (method selection) is the keystone
blocking GR-001, GR-004, and GR-005. Highest Risk in the repository.

---

**Plastics.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Plastics.md`
Salvaged polymer processing and pyrolytic fuel recovery. Defines the triage
hierarchy for plastics: direct reuse → mechanical repurposing (filament/
RepRap stock) → thermal depolymerization for mixed or degraded bulk.
Pyrolysis framework covers three stages: oxygen-excluded batch reactor
(350°C–450°C), multi-stage condensation array producing synthetic crude
oil, and non-condensable syngas routing. PL-001 (halogenated polymer
contamination — HCl/dioxin release from PVC) is Critical and Blocking
before any hot operational run. PL-002 (reactor over-pressurization) is
Major and Blocking. Air Scrubber operation is a non-negotiable prerequisite.
Exploration/Volatile — File_Template.md retrofit required.
*New file — 2026-05-26*

---

**Gate_04_Separation_Mechanical.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_04_Separation_Mechanical.md`
Pre-purification mechanical decision point operating after Reduction and
before thermal processing. Diverts usable material away from the Spin
Chamber using centrifugal separation, dual-channel sensor cross-check,
and a refusal-first fail-to-bin protocol. Success defined by avoided
processing, not perfect separation. Target: ≥30% material diversion rate.
MG-001 through MG-008 in sidecar.
*Formerly: Material_Separation_Gate_v0.md, Stratification_Chamber_v0.md*

---

**Gate_05_Separation_Thermal.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_05_Separation_Thermal.md`
Core melting and gradient formation module. Converts mixed metallic scrap
into ranked material streams via induction heating, slow rotation, and MHD
damping. Produces useful gradients, not pure metal. Designed for long
operational life, modular repair, and bootstrap compatibility. RPM safety
factor ~32× confirmed. SC-001 through SC-008 in sidecar.
*Formerly: Spin_Chamber_v0.md*

---

**Gate_06_Fabrication.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_06_Fabrication.md`
Constructive stage of the Lazarus Forge. Arc welding is the v0 proof-of-
concept gatekeeper. Add-to-excess and mill-to-spec is the primary
dimensional control philosophy. Owns precision ceiling doctrine. Dynamic
and adaptive — method set grows through formal qualification framework.
PPE is a non-negotiable prerequisite.

---

**Air_Scrubber.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Air_Scrubber.md`
Safety and containment subsystem. Five-stage architecture: sacrificial
intercept → ionization → thermal quench → wet scrubbing → polishing.
Operates under negative pressure. Includes marine bubble-column variant,
thermal sink requirement, and Saturation Fault monitoring. If the scrubber
cannot verify safe operation, the Forge does not run.
*Formerly: Air_Scrubber_v0.md*

---

**Woodworking.md** — Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Woodworking.md`
End-to-end timber processing from tree harvesting through green wood
handling, drying, milling, CNC fixturing, heat treatment, joinery,
finishing, and waste valorization including basic paper making. Strong
emphasis on salvaged urban and storm timber, southernUS species selection, and climate-appropriate drying doctrine (approximately one year per inch under local humidity). Felling safety doctrine included —
lethal risk from falling trees and chainsaw kickback; never fell alone.
Fine wood dust is explosive at concentration and causes permanent
respiratory damage — source capture dust extraction required at all
power tool stations; several common species produce toxic or sensitizing
dust. Integrates with Air_Scrubber.md for dust management. WW-001 through
WW-004 in sidecar. Body Stability Volatile — Verification Ref field
correction and File_Template.md alignment required.
*New file — 2026-05-29*

---

**Gate_07_Utilization.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_07_Utilization.md`
After action review stage of the Lazarus Forge. Where fabricated parts
and recovered components meet operational reality — the system learns
whether what it made worked, how long it lasted, how it failed, and what
that means for the next fabrication cycle. Defines performance logging
minimum content, failure mode capture and classification, four feedback
paths, and retirement handoff doctrine to Gate_02_Triage. GU-001 through
GU-004 in sidecar.

---

**Electronics.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Electronics.md`
Salvaged electronics recovery, PCB fabrication, and logic integration.
Trust-anchor document for the forge's governance substrate — ethics
enforcement, hardware watchdogs, TMR voting, sensor truth, and AI
containment all depend on the integrity of the systems this file governs.
Logic-Zero wipe required before any salvaged programmable device enters
forge systems. EL-001 through EL-008 in sidecar. EL-005 (toxic dust)
and EL-006 (firmware trust) flagged Critical.
*Formerly: Electronics.md (root)*

---

**Energy.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Energy.md`
Incremental energy strategy. Covers grid bootstrap, salvaged motor-
generators, biogas, solar, and thermal recovery. Power Demand stub with
three operating modes (Bootstrap ~2–5 kW, Nominal ~15–40 kW, Degraded
~1–3 kW) — all Placeholder, analog-sourced. Energy independence is not
assumed at v0.
*Formerly: energy_v0.md*

---

### Tests/

**Support_Raft.md** — v0.4
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Support_Raft.md`
Stationary operational anchor for mobile Leviathan units. Provides
regional power, data relay, physical recovery, and triage processing
infrastructure. SWATH hull architecture, Sacrificial Shell System, local
decision authority during comms blackout, Stasis Mode, and self-consuming
end-of-region protocol. The Raft's value is measured by what it enables
in the units, not what it does directly.
*Formerly: Support_Raft_v0.md*

---

**Leviathan_testing.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Leviathan_testing.md`
Deep-ocean autonomous test framework. Leviathan exists to break assumptions
and surface hidden failure modes before off-world deployment. Covers core
test philosophy, power and endurance assumptions, failure and recovery
doctrine, swarm extensions, and distributed learning via delay-tolerant
networking. Survival is optional. Understanding is not.
*Formerly: leviathan_testing.md*

---

## Cross-Repo Relationship

`LazarusForgeV0` (this repo) — operational implementation. Lean,
connected, specification-oriented.

`Lazarus-Forge-` — doctrine and philosophy. The source of principles
that get refined into practice here.

`Astroid-miner` — planned repository, intentionally deferred. Activates
when Leviathan deployment is underway. Until then, cross-repo verification
is scoped to `Lazarus-Forge-` only.

These are not parallel versions of the same document. They are different
layers of the same system. Treating them as interchangeable is a
navigation error. Divergence between them is logged, not ignored.

---

## Notes for Returning AI

- **Start every audit cycle with the Audit Opening Checklist** in
  `Admin/Forge_Audit_Kit.md`: (1) verify Tier 1 Axiom text in
  `Admin/Governance_Charter.md` matches prior committed version —
  any unratified change is a Constitutional violation requiring STATE_HOLD;
  (2) check `Unknowns.md` Expiry Watch for entries approaching two-cycle
  threshold; (3) run Semantic Stability Check against drift-risk term
  watchlist in `Admin/Canonical_Terms.md`.
- `Admin/Auditor_Protocols.md` **v0.7** governs all contributions. The
  Sidecar Model is active — module unknowns live in each file's footer
  sidecar, not in the global registry. Four auditor role classes: Skeptic,
  Systems, Evidence, Ethical. Engineer role extended by
  `Admin/Engineer_Protocols.md`.
- `Admin/Forge_Audit_Kit.md` **v0.9** is the starting point for routine
  audit cycles — load it instead of full Auditor_Protocols.md and
  Unknowns.md to stay within token limits. Reduced from v0.8 — kit size
  is a governed constraint.
- `Unknowns.md` is **v1.8** with a pending v1.9 update. Expiry Watch
  active — FL-001 and several EC entries approaching two-cycle threshold.
  RIP-001 Critical. GOV-003, GOV-005, SEC-007, and UNK-009 Critical.
- `Admin/Verification_Gates_LF.md` **v0.1** is now the resolution target
  for all Verification Ref fields. Gates defined there match
  Auditor_Protocols.md v0.7 exactly.
- `Admin/Security_Protocols.md` **v0.3** — Trust Boundary Declaration
  governs all cryptographic enforcement. SEC-007 (external root-of-trust)
  flagged Critical from first logging.
- Role declaration is required: *"Operating as [Role] per
  Auditor_Protocols.md v0.7"*
- `Admin/Governance_Charter.md` **v0.5** is the constitutional authority.
  Tier 1 Axioms (P-1 through P-4, Q-1 through Q-4) are non-negotiable
  primitives. Any reasoning path attempting to override them triggers
  STATE_HOLD.
- `Admin/Repository_Integrity_Protocol.md` **v0.1** defines what
  constitutes an integrity violation, how to classify it, and how to
  recover. Read this before modifying any governance-bearing document.
- `Architecture/Geck_forge_seed.md` is the most actively updated file —
  do not assume a cached version is current.
- The Rename Registry above is the canonical source for old-to-new
  filename mappings. All prior references to `Canonical_Terms_LF.md`
  are resolved via the Rename Registry entry added 2026-05-26.
- Unknown ID naming convention: local sidecar IDs (FL-001, SC-002,
  MG-004) are primary. UNK-* identifiers are cross-module navigation
  aliases indexed in Unknowns.md only.
- Governance tier hierarchy: Tier 1 (Governance_Charter.md,
  Ethical_Constraints.md) → Tier 2 (Auditor_Protocols.md) → Tier 3
  (Forge_Audit_Kit.md) → Tier 4 (dynamic procedures) → Tier 5 (domain
  specs). Lower tiers may extend but may not redefine higher tiers.
- Files listed in this document resolve to real committed files. If a
  link fails, log it as a Cross-Reference Failure per
  Auditor_Protocols.md Rule 1.
- `Astroid-miner` references are labeled planned — do not treat as
  active dependencies.
- All gate files now exist (Gate_01 through Gate_07). One planned Admin
  file not yet created: `Admin/Governance_Migration_Protocol.md`
  (GOV-001 resolution path). Do not treat as an active dependency.
- **New files since last major Discovery.md update:** Security_Protocols.md,
  Canonical_Terms.md, Plastics.md, Verification_Gates_LF.md,
  Engineer_Protocols.md, Engineering.md, Woodworking.md.
- `Operations/Woodworking.md` Verification Ref field currently reads
  `Admin/Forge_Audit_Kit.md` — should be corrected to
  `Verification_Gates_LF.md` at next revision.
- `Architecture/Engineering.md` owner fields in sidecar unknowns use
  short filename — should be corrected to `Architecture/Engineering.md`
  at next revision.


new file added
https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Mechanical_Structures.md


# Discovery.md — Addendum: Admin/ Scope Entries
## Compiled from Batch 1 (5 files) + Batch 2 (5 files)
## Status: Draft — for reconciliation with existing Discovery.md content
## Compiled: 2026-05-31

---

> **Integration Note:** These entries follow the scope boundary format
> proposed in the Discovery.md transformation discussion. Each entry
> captures In-Scope, Out-of-Scope, Upstream Dependencies, and Downstream
> Recipients derived directly from each file's own Scope Boundary section
> and Relationship declarations. Reconcile against Discovery.md confirmed
> file list before committing. Canonical folder-prefixed paths used
> throughout. Files marked [PLANNED] carry that label as of last read.

---

## Admin/ Directory — Scope Map

---

### `Admin/Canonical_Terms.md`
**Purpose:** Single source of truth for repository nomenclature. Prevents
semantic drift across multi-agent cycles by locking vocabulary, resolving
conflicts between terminology sources, and enforcing anti-drift guardrails.

**In-Scope:**
- Authoritative vocabulary mappings for system architecture, hardware
  structures, and governance layers
- Conflict resolution rules between this file and other vocabulary sources
- Semantic boundaries enforcing consistency across multi-agent cycles
- Anti-drift guardrails: banned terms and their approved replacements
- Disambiguation of overloaded uses of "canonical"

**Out-of-Scope:**
- Individual component blueprints or dimensional specifications
- Programmatic API schemas or cryptographic algorithms
- Ethical policy constraints (→ `Admin/Ethical_Constraints.md`)
- Operational routing semantics (→ `Architecture/Forge_flow.md` is
  authoritative for routing; conflicts escalate here as Active Disputes)
- Governance tier authority (→ `Admin/Governance_Charter.md`; definitions
  here are derived from that source)
- Filename resolution for renamed or legacy files (→ `Discovery.md`
  Rename Registry)

**Upstream Dependencies:**
- `Admin/Governance_Charter.md` — tier definitions; authoritative over
  this file for constitutional vocabulary
- `Architecture/Forge_flow.md` — operational routing vocabulary;
  authoritative over this file for gate logic terms
- `Discovery.md` — Rename Registry is the canonical filename resolution
  source

**Downstream Recipients:**
- All repository files — anti-drift guardrails apply to all
  specification-level contributions
- `Admin/Auditor_Protocols.md` — Fallacy 4 (Semantic Drift) enforcement
  references this file as the resolution target
- `Admin/Security_Protocols.md` — CT-004 (trusted initialization
  environment definition) is a pending addition required here

**Open Blocking Unknowns:** CT-002 (Component Library Schema — blocks
`Operations/Gate_02_Triage.md` promotion), CT-004 (Trusted Initialization
Environment — blocks `Admin/Security_Protocols.md` Section III.2 promotion)

---

### `Admin/Auditor_Protocols.md`
**Purpose:** Defines how auditors operate within LazarusForgeV0. Prevents
audit theater, uncontrolled specification promotion, semantic drift, silent
contradiction accumulation, and autonomous corruption of repository knowledge.

**In-Scope:**
- Repository-wide auditor operational behavior
- Auditor role classes (Skeptic, Systems, Evidence, Ethical, Synthesizer)
- Audit entry conditions and sequencing (10-phase sequence)
- Fallacy Checklist with substantive note requirements
- AI and human contributor protocols
- Decentralized audit architecture (Sidecar Model)
- Unknowns registry governance
- Verification gate enforcement
- Adversarial audit layer and challenge battery
- Drift detection requirements
- Specification promotion rules
- Autonomous auditor constraints and human override doctrine
- Full Stop Review triggers
- Observability and audit trail requirements

**Out-of-Scope:**
- Engineering specifications for Forge systems
- Ethical policy details beyond mandatory anchor preservation
  (→ `Admin/Ethical_Constraints.md`)
- Human governance authority structures
  (→ `Admin/Governance_Charter.md`)
- Canonical terminology definitions
  (→ `Admin/Canonical_Terms.md`)
- Cross-repo verification architecture (→ `Architecture/Forge_Net.md`)

**Upstream Dependencies:**
- `Admin/Governance_Charter.md` — Tier 1 constitutional authority;
  this file operates within the hierarchy defined there
- `Admin/Ethical_Constraints.md` — co-Tier 1; hard-line doctrines
  (Anti-Weaponization, Life Preservation) are not subject to auditor
  override

**Downstream Recipients:**
- `Admin/Forge_Audit_Kit.md` — Tier 3 condensed reference; derived from
  this file; may not outrank its source
- `Admin/Verification_Gates_LF.md` — gate definitions extracted from
  §Verification Gate Enforcement here; that file is derived from this one
- All repository files — role declaration requirement, audit sequence,
  and fallacy checklist apply to all specification-level contributions

**Open Blocking Unknowns:** AP-004 (cross-auditor disagreement resolution),
AP-007 (repository integrity doctrine lineage)

---

### `Admin/Ethical_Constraints.md`
**Purpose:** First-class control substrate determining whether actions are
permitted before determining how to execute them. Establishes hard
constraints (commandments, not guidelines) to close runtime evaluation
failure modes in autonomous and multi-agent systems.

**In-Scope:**
- Core mandate: ownership, legal permissibility, ethical constraints,
  authorization status
- Ownership and material rights recognition framework
- Legal context awareness requirements
- Anti-Weaponization Doctrine (hardest constraint; not subject to review)
- Life Preservation Heuristics (hard and soft constraints)
- Cultural and Sacred Site Recognition
- High-permission environment constraints (landfills, scrap yards)
- Refusal as a first-class action
- Human Escalation Protocol (placeholder pending EC-003)
- Learning without value drift doctrine
- Governance failure modes and fallback posture (Pacifist Operating
  Posture)

**Out-of-Scope:**
- Constitutional governance hierarchy (→ `Admin/Governance_Charter.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- Runtime enforcement code or cryptographic implementation

**Upstream Dependencies:**
- None above Tier 1; co-occupies Tier 1 with `Admin/Governance_Charter.md`

**Downstream Recipients:**
- All repository files — Ethical Anchor field references this file
- `Admin/Governance_Charter.md` — Tier 1 Axioms are consistent with and
  reinforced by doctrines here; Anti-Weaponization and Life Preservation
  are not subject to constitutional override
- `Tests/Leviathan_testing.md` — stress-test environment for this
  governance system; escalation channel definition deferred there

**Open Blocking Unknowns:** EC-001 (sufficient confidence threshold),
EC-002 (Anti-Weaponization pattern-matching mechanism), EC-003 (human
escalation path mechanism)

---

### `Admin/Engineer_Protocols.md`
**Purpose:** Guides AI and human engineers toward effective,
reality-grounded creative problem-solving within the Forge. Fills the gap
between governance documents (what is permitted) and domain specifications
(what is built).

**In-Scope:**
- Cognitive and procedural protocols for engineering problem-solving
- Pragmatic question framework (10 questions) for AI and human
  contributors
- Assumption challenge triggers — when skepticism is mandatory
- Anti-reinvention and failure-harvesting rules
- Engineer ↔ Auditor relationship and dispute resolution doctrine
- AI-specific engineering contribution guidance

**Out-of-Scope:**
- Specific engineering calculations or domain techniques
  (→ domain files in `Operations/`, `Architecture/`)
- General audit or governance procedures
  (→ `Admin/Auditor_Protocols.md`, `Admin/Forge_Audit_Kit.md`)
- Detailed validation test protocols (→ domain files)
- Auditor role class definitions
  (→ `Admin/Auditor_Protocols.md` §Auditor Role Classes; this file
  extends the Engineer role defined there, does not replace it)
- Engineering authority boundary (→ EP-004; undefined until resolved)

**Upstream Dependencies:**
- `Admin/Auditor_Protocols.md` — Engineer role defined there; AI
  Contribution Rules apply to engineers operating under this protocol
- `Admin/Ethical_Constraints.md` — irreversible actions require elevated
  authorization per §Human Override Doctrine
- `Discovery.md` — primary navigation layer; repository search begins
  there per §Pragmatic Question Framework

**Downstream Recipients:**
- All engineering contributors (human and AI) — pragmatic question
  framework and assumption challenge triggers apply
- Domain files in `Operations/`, `Architecture/` — this protocol governs
  how those files are authored and revised

**Open Blocking Unknowns:** EP-004 (engineering authority boundary
undefined)

---

### `Admin/Governance_Charter.md`
**Purpose:** Defines the constitutional governance structure of
LazarusForgeV0. Stabilizes authority relationships, preserves semantic
continuity across audit generations, and constrains recursive governance
expansion. Declares Tier 1 Axioms — self-evident primitives functioning
as epistemic circuit breakers.

**In-Scope:**
- Tier 1 constitutional axioms (Protections P-1 through P-4;
  Prohibitions Q-1 through Q-4)
- Constitutional governance doctrine
- Governance authority hierarchy (Tiers 1–5)
- Canonical governance ownership rules
- Verification gate constitutional definitions
- Governance precedence rules
- Bootstrap governance behavior and Genesis Phase Protocol
- Governance migration doctrine (including Tier 1 amendment requirements)
- Provenance doctrine
- Audit lineage requirements
- Escalation doctrine and calibration
- Governance enforcement-state doctrine
- Repository integrity expectations
- Autonomous governance constraints
- Human override doctrine

**Out-of-Scope:**
- Runtime execution engines
- Cryptographic implementation details
  (→ `Admin/Security_Protocols.md` [PLANNED])
- CI/CD automation mechanics
- Fabrication procedures or engineering specifications
- Canonical terminology definitions
  (→ `Admin/Canonical_Terms.md`)
- Auditor operational behavior
  (→ `Admin/Auditor_Protocols.md`)
- Condensed audit reference
  (→ `Admin/Forge_Audit_Kit.md`)

**Upstream Dependencies:**
- None above Tier 1; this file is the constitutional root

**Downstream Recipients:**
- All repository files — governance hierarchy, axioms, and escalation
  doctrine apply repository-wide
- `Admin/Auditor_Protocols.md` — operates within authority hierarchy
  defined here
- `Admin/Security_Protocols.md` [PLANNED] — GOV-006 and GOV-008
  resolution targets
- `Admin/Governance_Migration_Protocol.md` [PLANNED] — GOV-001
  resolution target
- `Admin/Canonical_Terms.md` — tier definitions derived from here;
  must remain consistent

**Open Blocking Unknowns:** GOV-003 (integrity enforcement architecture —
Critical), GOV-005 (long-term constitutional stability — Critical),
GOV-006 (human override authenticity), GOV-008 (minimum agent quorum
for bootstrap compliance)

---

### `Admin/Security_Protocols.md`
**Purpose:** Establishes technical security implementation rules for
validating administrative authority, ensuring knowledge graph integrity,
and managing multi-node validation in untrusted, degraded, or adversarial
environments. Bridges constitutional governance declarations and operational
integrity procedures via a cryptographic enforcement layer.

**In-Scope:**
- Cryptographic mechanisms for multi-signature Human Override
  Verification (GOV-006 resolution)
- Automated code-signing protocols for file integrity verification
  (RIP Phase 3 target)
- Node identity verification and key rotation cycles
- Minimum token complexity, air-gapping requirements, and cryptographic
  fallback behaviors during network division
- Trust boundary declaration: governance legitimacy precedes cryptographic
  enforcement
- Authentication event logging requirements (SEC-REG-001)
- Degraded-operation security doctrine

**Out-of-Scope:**
- Component-level infiltration prevention for salvaged hardware
  (→ `Operations/Electronics.md`)
- OS firewall commands or network router firmware rules
- Local facility access control (physical perimeter)
- Constitutional governance doctrine
  (→ `Admin/Governance_Charter.md`)
- Auditor operational behavior
  (→ `Admin/Auditor_Protocols.md`)
- Minimum agent quorum definition
  (→ GOV-008 in `Admin/Governance_Charter.md`; prerequisite input here)
- Trusted initialization environment definition
  (→ CT-004 in `Admin/Canonical_Terms.md`)

**Upstream Dependencies:**
- `Admin/Governance_Charter.md` — Tier 1; GOV-006 and GOV-008 are
  originating unknowns; Trust Boundary Declaration defers to hierarchy
  defined there
- `Admin/Repository_Integrity_Protocol.md` — RIP-005 is the originating
  unknown for Phase 3 enforcement; Phases 1 and 2 are prerequisites
- `Admin/Canonical_Terms.md` — CT-004 (trusted initialization
  environment) must be defined before Section III.2 can be promoted
- `Operations/Electronics.md` — Logic-Zero wipe is Layer 1 prerequisite
  for node cluster admission defined here

**Downstream Recipients:**
- `Admin/Repository_Integrity_Protocol.md` — Phase 3 cryptographic
  enforcement resolves RIP-005
- `Admin/Governance_Charter.md` — resolves GOV-006 interim authentication
  requirement when this file reaches Provisional Specification
- All governance files — cryptographic signing eligibility applies at
  Candidate Specification maturity and above

**Open Blocking Unknowns:** SEC-001 (quorum recovery under network
partition — blocks; deferred to GOV-008), SEC-005 (trusted initialization
environment — deferred to CT-004), SEC-007 (external root-of-trust
architecture — Critical)

---

### `Admin/Repository_Integrity_Protocol.md`
**Purpose:** Operational integrity enforcement procedures for
LazarusForgeV0. Bridges the constitutional declaration of integrity
requirements (Governance_Charter.md) and fully Enforceable integrity
protections. Defines procedures executable by human operators until
automation (AUDIT_HARNESS.py) matures.

**In-Scope:**
- Integrity baseline definitions for each protected repository element
- Violation detection procedures at v0 (human-in-the-loop)
- Violation classification system (Minor / Major / Constitutional)
  and response ladder
- Recovery procedures following confirmed violations
- Version preservation requirements and human workflow
- Automation migration path (Phase 1 → 2 → 3)
- Relationship between integrity doctrine and constitutional axioms
- Incident logging requirements

**Out-of-Scope:**
- Cryptographic authentication implementation
  (→ `Admin/Security_Protocols.md`)
- Constitutional governance doctrine
  (→ `Admin/Governance_Charter.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- CI/CD pipeline automation mechanics or runtime enforcement code
- Governance authority hierarchy
  (→ `Admin/Governance_Charter.md`)
- Anti-Weaponization doctrine
  (→ `Admin/Ethical_Constraints.md`)

**Upstream Dependencies:**
- `Admin/Governance_Charter.md` — GOV-003 is the originating unknown;
  constitutional integrity requirements declared there
- `Admin/Auditor_Protocols.md` — Adversarial Challenge Classes 6, 9,
  and 10 are primary detection mechanisms coordinated with this file
- `Admin/Ethical_Constraints.md` — Ethical Anchor field integrity
  governed by doctrine there

**Downstream Recipients:**
- `Admin/Forge_Audit_Kit.md` — RIP-004 resolution requires an addition
  to audit opening checklist (Tier 1 Axiom text verification)
- `Admin/AUDIT_HARNESS.py` — primary automation target for Phase 1
  and Phase 2 checks defined here
- `Admin/Security_Protocols.md` — Phase 3 cryptographic enforcement
  dependency; this file's Phase 3 section is the specification input
- `Unknowns.md` — Constitutional violation incidents logged as
  Cross-Module entries there
- `Discovery.md` — Archive directory to be added here when established
  (RIP-001)

**Open Blocking Unknowns:** RIP-001 (prior-state archival system not
established — Critical), RIP-004 (Constitutional violation detection
latency)

---

### `Admin/Ship_of_Theseus_Right_to_Repair.md`
**Purpose:** Establishes the Ship of Theseus paradox as the philosophical
and legal load-bearing argument for the Forge's repair-first doctrine.
Provides ethical and legal defense framework for treating Forge outputs
as restorations rather than new manufactures under right-to-repair law.

**In-Scope:**
- Ship of Theseus paradox as philosophical grounding for repair-first
  mindset
- Right-to-repair legal defense strategy for Forge outputs
- Grain preservation system (1g samples) as provenance and legal
  continuity mechanism
- Relationship between Bootstrap Doctrine, Graduation Rule, and
  continuity of identity
- QR code provenance documentation framework (placeholder)

**Out-of-Scope:**
- Full component triage workflow
  (→ `Operations/Gate_02_Triage.md` / `Architecture/Components.md`)
- Grain storage and tracking protocol (→ ST-001; pending)
- QR documentation standard (→ ST-002; pending)
- Jurisdiction-specific legal verification (→ ST-003; human governing
  party decision)
- G.E.C.K. seeding specifications (→ `Architecture/Geck_forge_seed.md`)

**Upstream Dependencies:**
- `Operations/Gate_02_Triage.md` — triage workflow where repair-first
  philosophy is operationalized
- `Architecture/Components.md` — Bootstrap Doctrine and Graduation Rule
  referenced here as expressions of the same continuity principle

**Downstream Recipients:**
- `Operations/Gate_02_Triage.md` — philosophical grounding for triage
  decisions
- `Architecture/Geck_forge_seed.md` — grain system informs minimum
  viable seed provenance requirements

**Open Blocking Unknowns:** ST-003 (legal applicability by jurisdiction —
Non-blocking for Exploration; Blocking before any commercial operation)

---

### `Admin/Trajectories.md`
**Purpose:** Defines the evolutionary trajectory of the Lazarus Forge
from v0 through interstellar (v5). Scope routing destination for the
repository — capabilities beyond current version scope route here
rather than accumulating in operational documents. Owns the Forge
Regeneration Threshold (FRT) doctrine and floor value.

**In-Scope:**
- Version trajectory from v0 through v5 with survival thresholds and
  exit conditions
- FRT doctrine and floor value ([2–5%] Placeholder)
- Revenue allocation framework (operator-defined layer above FRT floor)
- Scope routing destination for out-of-version capabilities
- Design doctrine notes governing version advancement

**Out-of-Scope:**
- Component taxonomy or implementation specs for future versions
  (→ module documents when versions become active)
- Detailed economic model
  (→ planned `economics_v0.md` at v0→v1 transition)
- FRT measurement and logging procedures
  (→ `Operations/Gate_07_Utilization.md`)
- Component procurement doctrine
  (→ `Architecture/Geck_forge_seed.md`)
- Formal quality certification standards (→ future v2+ assignment)

**Upstream Dependencies:**
- `Admin/Governance_Charter.md` — Axiom P-3 (Collaboration and Mutual
  Benefit) constrains community allocation doctrine
- `Operations/Energy.md` — EV-001 feeds v1 operating cost model (TR-001)
- `Architecture/Geck_forge_seed.md` — G.E.C.K. seeding definition
  for v2

**Downstream Recipients:**
- All operational and architecture files — out-of-scope capability
  creep routes here
- `Operations/Gate_07_Utilization.md` — FRT measurement and per-cycle
  logging lives there; this file owns the doctrine
- `economics_v0.md` [PLANNED] — v0→v1 economic model; TR-001 is the
  blocking unknown

**Open Blocking Unknowns:** TR-001 (v1 profitability baseline undefined —
blocks v0→v1 transition)

---

### `Admin/Verification_Gates_LF.md`
**Purpose:** Single canonical source for the six verification gates
required for document promotion. Every file's Verification Ref field
points here. Stable dedicated home for gate definitions so they do not
drift across governance additions in Auditor_Protocols.md or
Forge_Audit_Kit.md.

**In-Scope:**
- The six canonical verification gates (G1–G6) with pass criteria and
  evidence standards
- Failure routing and holding logic for each gate
- Full Stop Review trigger conditions and invocation record requirements
- Gate enforcement rules (sequential requirement, binding block authority,
  self-approval prohibition, override doctrine, reversibility)
- Promotion requirements summary

**Out-of-Scope:**
- Full auditor role class doctrine
  (→ `Admin/Auditor_Protocols.md`)
- Full audit sequencing and phase logic
  (→ `Admin/Auditor_Protocols.md`)
- Full Adversarial Challenge Battery
  (→ `Admin/Auditor_Protocols.md`)
- Condensed audit operational reference
  (→ `Admin/Forge_Audit_Kit.md`)
- Cryptographic enforcement of gate passage
  (→ `Admin/Security_Protocols.md`)
- Ethical policy (→ `Admin/Ethical_Constraints.md`)
- Constitutional governance hierarchy
  (→ `Admin/Governance_Charter.md`)

**Upstream Dependencies:**
- `Admin/Auditor_Protocols.md` — source of truth for gate definitions;
  this file is derived from §Verification Gate Enforcement there;
  conflicts resolve in favor of Auditor_Protocols.md
- `Admin/Governance_Charter.md` — human override doctrine applies to
  gate process decisions; Tier 1 violations are not subject to gate
  override

**Downstream Recipients:**
- All repository files — Verification Ref field in File State table
  points here
- `Admin/Forge_Audit_Kit.md` — carries condensed gate table derived
  from this file; must remain consistent
- `Admin/Security_Protocols.md` — Phase 3 cryptographic enforcement
  will verify gate passage via commit signing
- `Discovery.md` — this file must be added to confirmed file list and
  Suggested Reading Order (per file's own Immediate Actions Required)

**Open Blocking Unknowns:** VG-001 (gate definition synchronization
authority chain — Non-blocking at Exploration; Blocking at Specification
promotion)

---

## Cross-Cutting Notes for Discovery.md Integration

**Planned files referenced across this batch** (not yet confirmed in
repository; must carry [PLANNED] label in Discovery.md until created):
- `Admin/Security_Protocols.md` — now EXISTS (included in this batch)
- `Admin/Canonical_Terms.md` — now EXISTS (included in Batch 1)
- `Admin/Governance_Migration_Protocol.md` — still PLANNED
- `Admin/Repository_Structure.md` — still PLANNED
- `economics_v0.md` — still PLANNED
- `Architecture/Forge_Net.md` — status unknown; verify
- `Admin/Forge_Audit_Kit.md` — status unknown; verify against confirmed list
- `Admin/File_Template.md` — status unknown; verify against confirmed list
- `Admin/AUDIT_HARNESS.py` — status unknown; verify against confirmed list

**Archive directory** (`/Archive/`): Prescribed by
`Admin/Repository_Integrity_Protocol.md` (RIP-001) but not yet
established. Should be added to Discovery.md when created.

**Suggested Reading Order implication:** `Admin/Verification_Gates_LF.md`
explicitly requests placement after `Admin/File_Template.md` in the
Suggested Reading Order. Should be reflected in Discovery.md update.

**Governance tier summary for Discovery.md routing table:**

| Tier | File | Status |
|------|------|--------|
| Tier 1 | `Admin/Governance_Charter.md` | Active |
| Tier 1 | `Admin/Ethical_Constraints.md` | Active |
| Tier 2 | `Admin/Auditor_Protocols.md` | Active |
| Tier 3 | `Admin/Forge_Audit_Kit.md` | Verify |
| Tier 4 | Dynamic procedures | — |
| Tier 5 | Domain specifications | — |
| Support | `Admin/Canonical_Terms.md` | Active |
| Support | `Admin/Security_Protocols.md` | Active (Draft) |
| Support | `Admin/Repository_Integrity_Protocol.md` | Active (Draft) |
| Support | `Admin/Verification_Gates_LF.md` | Active (Draft) |
| Support | `Admin/Engineer_Protocols.md` | Active (Draft) |
| Support | `Admin/Ship_of_Theseus_Right_to_Repair.md` | Active (Exploration) |
| Support | `Admin/Trajectories.md` | Active (Exploration) |

---

*This addendum covers Admin/ only. Operations/, Architecture/, and Tests/
files will follow in subsequent batches. Reconcile against existing
Discovery.md content before committing — do not treat this as a
replacement, only as an addenDraft.

# Discovery.md — Addendum: Architecture/ Scope Entries
## Compiled from Architecture batch (6 files)
## Status: Draft — for reconciliation with existing Discovery.md content
## Compiled: 2026-05-31

---

> **Integration Note:** Continues the format established in
> Discovery_Addendum_Admin.md. Same four-field scope structure:
> In-Scope, Out-of-Scope, Upstream Dependencies, Downstream
> Recipients. Derived directly from each file's own Scope Boundary
> and Relationship sections. Reconcile against existing Discovery.md
> confirmed file list before committing.

---

## Architecture/ Directory — Scope Map

---

### `Architecture/Engineering.md`
**Purpose:** Single durable source of engineering truth and judgment
for all Forge activities. Equips contributors with condensed principles,
safety discipline, and practical parameters for designing under real-world
constraints — salvaged materials, limited tools, variable climate.

**In-Scope:**
- Foundational engineering principles, rules of thumb, and decision
  frameworks for the entire LazarusForge
- Core mechanical, structural, and systems engineering fundamentals
- Materials behavior overview and selection guidance
- Forge-specific parameters and safety factors
- Arkansas/southern US climate considerations and derating guidance
- Progressive path from basic to high-performance engineering

**Out-of-Scope:**
- Detailed calculations or design procedures for specific subsystems
  (→ `Architecture/Structural_Engineering.md` [PLANNED],
  `Architecture/Mechanical_Systems.md` [PLANNED])
- Domain-specific fabrication techniques
  (→ `Operations/Woodworking.md` [PLANNED],
  `Operations/Metals.md` [PLANNED])
- Software engineering or electronics design (→ dedicated files)
- Full regulatory compliance or professional licensure requirements

**Upstream Dependencies:**
- `Admin/Ethical_Constraints.md` — safety constraints govern all
  engineering decisions
- `Admin/Engineer_Protocols.md` — procedural layer for how engineering
  contributors apply these principles

**Downstream Recipients:**
- All Operations/ and Architecture/ domain files — engineering
  principles and safety factors apply throughout
- `Architecture/Structural_Engineering.md` [PLANNED],
  `Architecture/Mechanical_Systems.md` [PLANNED] — detailed
  domain files defer to this file for foundational principles

**Open Blocking Unknowns:** EN-001 (validated safety factors for
salvaged materials — Critical, blocks structural specification)

---

### `Architecture/Components.md`
**Purpose:** Defines the minimum component architecture required for
a Lazarus Forge to function and persist. Answers three questions: what
must exist (Critical), what helps (Useful), and what can wait (Bootstrap).
Governs all component classification decisions across the repository.

**In-Scope:**
- Component taxonomy for Lazarus Forge v0 through v3
- Classification criteria (Critical, Useful, Bootstrap) with definitions
- Bootstrap Doctrine and Graduation Rule
- Dual-use annotation standard for components
- Version mapping by material scope and capability

**Out-of-Scope:**
- Electronics, software, biological, or optical fabrication systems
  (→ downstream version taxonomies)
- Detailed engineering specifications for individual components
  (→ respective domain files)
- Energy infrastructure beyond grid bootstrap minimum
  (→ `Operations/Energy.md`)
- G.E.C.K. manifest or redundancy stock
  (→ `Architecture/Geck_forge_seed.md`)
- Cross-module governance or repository-level unknowns
  (→ `Unknowns.md`)

**Upstream Dependencies:**
- `Architecture/Forge_flow.md` — operational gate logic that components
  are classified against
- `Architecture/Geck_forge_seed.md` — G.E.C.K. manifest is the
  redundancy and consumables path for Critical components
- `Admin/Ethical_Constraints.md` — dual-use annotation High rating
  routes to Anti-Weaponization Doctrine there

**Downstream Recipients:**
- `Architecture/Geck_forge_seed.md` — Bootstrap Doctrine sufficiency
  criterion links to Forge loop defined there (Section III)
- `Operations/Gate_02_Triage.md` — component classification governs
  triage routing decisions
- All Operations/ gate files — Critical component list defines what
  must be present for the Forge to function

**Open Blocking Unknowns:** CO-002 (Metrology precision thresholds —
Non-blocking; deferred to first fabrication trials)

---

### `Architecture/Forge_Net.md`
**Purpose:** Defines the decentralized data and physical infrastructure
connecting individual forge instances into a resilient, self-improving
ecology. Prerequisite for all inter-forge logistics, knowledge sharing,
and coordinated resource allocation.

**In-Scope:**
- Philosophy and doctrine for decentralized forge networking
  (local-primary, network-sync-secondary)
- Data layer architecture: local cache, network sync, shared knowledge
  base (Wikipedia model with knowledge scope classification), cognitive
  save states, data validation layer
- Physical infrastructure layer: proximity-based cluster formation,
  resource sharing doctrine, data hosting
- Positive reinforcement mechanisms and perverse incentive guards
- Cluster governance emergence doctrine and anti-concentration mechanisms
- Trust weighting and federation principles
- Failure, node loss, and node reintegration doctrine
- Network security threat model and defensive doctrine
- Data privacy classification tiers and access control doctrine
- Integration hooks to `Operations/Gate_01_Intake.md` as primary data
  contribution point

**Out-of-Scope:**
- Physical networking hardware specifications (not yet assigned)
- Specific database software or implementation (not yet assigned)
- Detailed cluster governance rules or voting mechanisms
  (emergent — cannot be specified before observed)
- Delay-tolerant networking protocol detail
  (→ `Tests/Leviathan_testing.md`)
- Rogue node identification and containment
  (→ `Architecture/Cognitive_Frameworks.md`)
- Energy cost of network operation (→ `Operations/Energy.md`)
- Inter-forge physical logistics and trade routing (downstream)
- Positive reinforcement economic accounting (downstream)
- Data privacy and access control implementation (→ FN-005; unassigned)

**Upstream Dependencies:**
- `Operations/Gate_01_Intake.md` — primary data contribution point;
  every intake record is a potential network knowledge artifact
- `Architecture/Cognitive_Frameworks.md` — rogue node management,
  TMR architecture for knowledge validation, trust model
- `Admin/Ethical_Constraints.md` — Anti-Weaponization Doctrine governs
  data classification and network access control
- `Tests/Leviathan_testing.md` — delay-tolerant networking doctrine;
  analog for connectivity-interrupted operation
- `Operations/Energy.md` — energy cost of network services

**Downstream Recipients:**
- Inter-forge logistics and trade routing files (downstream; depend on
  this file)
- `Admin/Trajectories.md` — network capability targets by version;
  v1 target includes cognitive save state portability

**Open Blocking Unknowns:** FN-001 (data validation criteria — Critical;
prerequisite for first network connection), FN-005 (data privacy and
access control — Critical; prerequisite for first network connection)

---

### `Architecture/Forge_flow.md`
**Purpose:** Defines the minimal viable operational logic of the Lazarus
Forge and serves as the **reference standard for shared vocabulary across
the entire repository**. Terms defined here carry their meaning into all
other documents unless explicitly noted otherwise. Authoritative source
for gate logic, outcome paths, and the want/need policy.

**In-Scope:**
- Minimal viable operational logic of the Lazarus Forge v0
- Reference standard for shared vocabulary — all Defined Terms here
  are repository-wide unless explicitly overridden
- v0 scope, inputs, and explicit non-goals
- Eight sequential decision gates (Intake through Utilization)
- Gate Correspondence table mapping triage outcomes to gates
- Outcome paths and reversibility notes
- Human/AI Oversight Gate logic and want/need policy
- Fabrication priority order
- Feedback and learning doctrine for v0
- Primary KPI definition (value recovered per kWh consumed)
- Termination conditions
- Purification stage definition (governs DS-001 terminology dispute)

**Out-of-Scope:**
- Detailed hardware specifications for any module
  (→ `Operations/Spin_Chamber_v0.md`,
  `Operations/Material_Separation_Gate_v0.md`, etc.)
- Reduction module specification (→ unassigned; FL-002, UNK-007)
- Component triage station workflow detail
  (→ `Operations/Component_Triage_System.md`)
- Energy accounting and power demand (→ `Operations/Energy.md`)
- Autonomous operation logic or AI trust architecture
  (→ `Architecture/Cognitive_Frameworks.md`,
  `Admin/Ethical_Constraints.md`)
- Version roadmap and exit conditions (→ `Admin/Trajectories.md`)
- Cross-module unknowns global index (→ `Unknowns.md`)
- Facility siting or area-of-operation requirements
  (→ UNK-006; no file exists yet)

**Upstream Dependencies:**
- `Admin/Canonical_Terms.md` — vocabulary consistency; this file
  is the operational routing vocabulary standard that Canonical_Terms
  defers to for gate logic terms
- `Admin/Ethical_Constraints.md` — Human/AI Oversight Gate escalation
  path; irreversible action constraints
- `Architecture/Components.md` — component classifications inform
  gate routing decisions

**Downstream Recipients:**
- **All repository files** — Defined Terms section is the vocabulary
  standard for the entire repository
- `Operations/` gate files — each gate specification derives its
  operational logic and vocabulary from this file
- `Architecture/Forge_Net.md` — shared gate decision logs are a
  primary network knowledge artifact
- `Admin/Canonical_Terms.md` — Section 2 gate definitions in
  Canonical_Terms are derived from this file; conflicts escalate
  to Canonical_Terms as Active Disputes

**Open Blocking Unknowns:** FL-001 (gate logic determinism at boundary
cases — In Progress; blocks Specification promotion), FL-002 (Reduction
module unassigned — no owning file for the only fully irreversible step)

**Active Dispute:** DS-001 — "Purification stage" terminology. Owned
here. Resolution recommended when second mechanical separation module
enters scope.

---

### `Architecture/Geck_forge_seed.md`
**Purpose:** Defines the smallest coherent set of tools, data, and
doctrine capable of instantiating a new Lazarus Forge from a standing
start in an unfamiliar location. The canonical module list, procurement
rationale, and success criteria for G.E.C.K. deployment.

**In-Scope:**
- Minimum viable seed required to instantiate a new Lazarus Forge
- Core G.E.C.K. module list (8 modules) and criticality rationale
- Procurement doctrine — when purchasing is the correct bootstrap
  strategy
- Precision as a capability threshold concept (introductory; full
  treatment deferred to `Precision_LF.md` [PLANNED])
- Marine variant module list and success criteria (exploratory)
- G.E.C.K. success criteria and scaling pathway to v1

**Out-of-Scope:**
- Detailed engineering specifications for any G.E.C.K. module
- Full precision doctrine or precision tracking methodology
  (→ `Precision_LF.md` [PLANNED])
- Leviathan chassis or deep-marine systems (→ `Admin/Trajectories.md`)
- Energy infrastructure beyond portable generation minimum
  (→ `Operations/Energy.md`)
- Component taxonomy or classification criteria
  (→ `Architecture/Components.md`)

**Upstream Dependencies:**
- `Architecture/Components.md` — Critical component list; G.E.C.K.
  must support all Critical components and their maintenance cycles
- `Architecture/Forge_flow.md` — Forge loop definition (Section III
  here) feeds Bootstrap Doctrine sufficiency criterion in Components.md
- `Admin/Ethical_Constraints.md` — purchased components must still be
  logged and assessed for dual-use potential per Components.md standards

**Downstream Recipients:**
- `Architecture/Components.md` — Forge loop definition used as
  Bootstrap Doctrine sufficiency anchor
- `Admin/Trajectories.md` — marine variant and v2/v3 seeding
  specifications route there
- `Precision_LF.md` [PLANNED] — full precision doctrine to be
  developed; this file is the originating reference

**Open Blocking Unknowns:** GK-005 (Precision_LF.md home document
not yet created — Non-blocking at Exploration)

---

### `Architecture/Cognitive_Frameworks.md`
**Purpose:** Defines how Forge systems think safely under uncertainty.
Establishes cognitive reliability architectures, distributed trust
models, redundancy and arbitration frameworks for autonomous Forge
systems that must operate in degraded, adversarial, and partially
corrupted environments.

**In-Scope:**
- Cognitive reliability layers (Layer 0 Mechanical through Layer 6
  Human governance)
- Framework taxonomy (A through G) — from Lone Intelligence to
  Simulation-Gated Cognition
- Confidence collapse states (Green through Black)
- Return-to-base doctrine and trigger conditions
- Split-brain doctrine and default response
- Human position in the stack — mutual stabilization model
- Hardware/software supervisory hierarchies
- Rogue node identification and containment
- AI consensus structures and diversity requirements

**Out-of-Scope:**
- PCB fabrication or specific MCU wiring
  (→ `Operations/Electronics.md`)
- Mechanical actuator details (→ domain files)
- Ethical policy itself
  (→ `Admin/Ethical_Constraints.md`)
- Individual Leviathan mission logic
  (→ `Tests/Leviathan_testing.md`)
- Networking implementation details
  (→ `Architecture/Forge_Net.md`)
- Cryptographic protocol specifics
  (→ `Admin/Security_Protocols.md`)
- Full autonomous governance law (→ future files)

**Upstream Dependencies:**
- `Admin/Ethical_Constraints.md` — hard-line doctrines (particularly
  CF-DS-002 human override scope dispute) govern what no cognition
  layer may override
- `Operations/Electronics.md` — TMR hardware implementation and
  watchdog circuit design (CF-001 owner)
- `Admin/Auditor_Protocols.md` — multi-agent audit cycle is a
  real-world implementation of Framework D/E consensus

**Downstream Recipients:**
- `Architecture/Forge_Net.md` — rogue node management and trust
  model referenced there; TMR architecture for knowledge validation
- `Tests/Leviathan_testing.md` — primary stress-test environment
  for all frameworks; confidence collapse states are test targets
- `Operations/Support_Raft_v0.md` — Framework F natural
  implementation; Guardian Protocol is Framework G prototype
- `Admin/Trajectories.md` — Framework G (Simulation-Gated
  Cognition) routes to v2/v3 scope

**Open Blocking Unknowns:** CF-001 (hardware watchdog minimum
standard — High; blocks any Specification-level autonomous
architecture), CF-002 (correlated AI failure modes — High)

**Active Disputes:** CF-DS-001 (centralized vs. distributed
cognition), CF-DS-002 (human override authority scope)

---

## Cross-Cutting Notes for Discovery.md Integration

**Planned files referenced across this batch** (must carry [PLANNED]
label in Discovery.md until created):
- `Architecture/Structural_Engineering.md` — referenced by
  `Architecture/Engineering.md`
- `Architecture/Mechanical_Systems.md` — referenced by
  `Architecture/Engineering.md`
- `Precision_LF.md` (path TBD) — referenced by
  `Architecture/Geck_forge_seed.md` and `Architecture/Components.md`
- `Operations/Woodworking.md` — referenced by
  `Architecture/Engineering.md`
- `Operations/Metals.md` — referenced by
  `Architecture/Engineering.md`
- `Operations/Reduction_v0.md` — FL-002 resolution target; no owner
  assigned; this is the only fully irreversible step in the Forge
  flow and currently has no owning file

**Critical path gap flagged:** `Operations/Reduction_v0.md` does not
exist and is the upstream dependency for `Operations/
Material_Separation_Gate_v0.md`. FL-002 notes this explicitly. Should
appear in Discovery.md as a [PLANNED] file with a risk annotation,
not just a standard planned entry.

**Forge_flow.md vocabulary authority:** This file is the operational
vocabulary reference standard for the entire repository. Discovery.md
should note this explicitly in the routing table — any contributor
encountering an undefined operational term should be routed to
`Architecture/Forge_flow.md` §Defined Terms before consulting
`Admin/Canonical_Terms.md`.

**Architecture/ reading order implication:** Based on dependency
chains, the natural reading order within Architecture/ is:
1. `Architecture/Forge_flow.md` — vocabulary and gate logic first
2. `Architecture/Components.md` — what must exist
3. `Architecture/Geck_forge_seed.md` — how to seed it
4. `Architecture/Engineering.md` — how to build it
5. `Architecture/Cognitive_Frameworks.md` — how it thinks
6. `Architecture/Forge_Net.md` — how instances connect

**Verification Ref inconsistency noted:** `Architecture/Forge_Net.md`
has `Verification Ref: Admin/Forge_Audit_Kit.md` while all other
files in this batch point to `Verification_Gates_LF.md`. Should be
reconciled — `Verification_Gates_LF.md` is the canonical target per
that file's own purpose statement.

**Architecture/ summary for Discovery.md routing table:**

| File | Status | Tier/Role |
|------|--------|-----------|
| `Architecture/Forge_flow.md` | Exploration | Vocabulary standard + gate logic |
| `Architecture/Components.md` | Exploration | Component taxonomy |
| `Architecture/Geck_forge_seed.md` | Exploration | Deployment seeding |
| `Architecture/Engineering.md` | Draft | Engineering principles |
| `Architecture/Cognitive_Frameworks.md` | Exploration | Cognition doctrine |
| `Architecture/Forge_Net.md` | Exploration | Network doctrine |

---

*This addendum covers Architecture/ only. Operations/ and Tests/
files will follow in subsequent batches. Reconcile against existing
Discovery.md content before committing — additive only, not a
replacement.*


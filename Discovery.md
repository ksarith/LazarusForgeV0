# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**

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

**Unknowns.md** 
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

**Governance_Charter.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Governance_Charter.md`


---

**Auditor_Protocols.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md`


---

**Ethical_Constraints.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md`

---

**Repository_Integrity_Protocol.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Integrity_Protocol.md`
Operational integrity enforcement 

---

**Security_Protocols.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Security_Protocols.md`


---

**Forge_Audit_Kit.md** — 
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

**Verification_Gates_LF.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Verification_Gates_LF.md`


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

**Engineer_Protocols.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Engineer_Protocols.md`


---

**Canonical_Terms.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Canonical_Terms.md`


---

**Ship_of_Theseus.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ship_of_Theseus.md`

---

**Trajectories.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Trajectories.md`
*Formerly: Trajectories_LF.md*

---

**AUDIT_HARNESS.py**
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
*Formerly: Lazarus_forge_v0_flow.md*

---

**Engineering.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Engineering.md`


---

**Geck_forge_seed.md** 
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Geck_forge_seed.md`


---

**Components.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Components.md`


---

**Cognitive_Frameworks.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Cognitive_Frameworks.md`


---

**Forge_Net.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_Net.md`


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



new file added
https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Mechanical_Structures.md


# Discovery.md — Addendum: Admin/ Scope Entries
## Status: Draft — for reconciliation with existing Discovery.md content
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
  (→ `Admin/Security_Protocols.md`)
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

## Status: Draft — for reconciliation with existing Discovery.md content


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

# Discovery.md — Consolidated Scope Addendum
## Covers: Admin/ (10 files) · Architecture/ (7 files) · Operations/Gates (7 files)
## Status: Draft — attach as addendum; reconcile before committing to Discovery.md
## Compiled: 2026-05-31

---

> **Preamble — Single Source of Truth Rule**
> Scope entries in this addendum are navigation summaries only.
> File-local Scope Boundary sections remain authoritative.
> Where this addendum and a file's own Scope Boundary conflict,
> the file wins. Update this addendum when files change; do not
> update files to match this addendum.

---

> **How to use this addendum**
> "Where does this belong?" → find the owning file here.
> "What files does this decision affect?" → check Downstream Recipients.
> "What must exist before this file can be promoted?" → check Upstream
> Dependencies and Open Blocking notes.
> Full detail always lives in the file itself.

---

## Section 1 — Admin/

---

### `Admin/Governance_Charter.md`
**Purpose:** Constitutional root. Defines governance hierarchy, Tier 1
Axioms, authority relationships, and amendment doctrine.
**In-Scope:** Tier 1 axioms (P-1–P-4, Q-1–Q-4); governance tiers 1–5;
bootstrap and genesis doctrine; escalation and migration doctrine;
autonomous governance constraints; human override doctrine.
**Out-of-Scope:** Runtime execution; cryptographic implementation
(→ `Admin/Security_Protocols.md`); canonical terminology
(→ `Admin/Canonical_Terms.md`); auditor behavior
(→ `Admin/Auditor_Protocols.md`).
**Upstream:** None — constitutional root.
**Downstream:** All repository files; `Admin/Auditor_Protocols.md`;
`Admin/Security_Protocols.md`; `Admin/Governance_Migration_Protocol.md`
[PLANNED]; `Admin/Canonical_Terms.md`.
> ⚠️ *GOV-003 (integrity enforcement), GOV-005 (constitutional stability),
> GOV-006 (human override authenticity) are Critical open unknowns.*

---

### `Admin/Ethical_Constraints.md`
**Purpose:** Co-Tier 1 control substrate. Determines whether actions are
permitted before determining how to execute them. Hard constraints only —
commandments, not guidelines.
**In-Scope:** Anti-Weaponization Doctrine (hardest constraint); Life
Preservation Heuristics; ownership and legal permissibility framework;
high-permission environment constraints; refusal as first-class action;
Pacifist Operating Posture fallback.
**Out-of-Scope:** Constitutional hierarchy (→ `Admin/Governance_Charter.md`);
auditor behavior (→ `Admin/Auditor_Protocols.md`); runtime enforcement code.
**Upstream:** None — co-Tier 1 with Governance_Charter.
**Downstream:** All repository files (Ethical Anchor field);
`Admin/Governance_Charter.md`; `Tests/Leviathan_testing.md`.
> ⚠️ *EC-001 (confidence threshold), EC-002 (Anti-Weaponization
> pattern-matching), EC-003 (human escalation path) all open.*

---

### `Admin/Auditor_Protocols.md`
**Purpose:** Tier 2 operational doctrine for how auditors behave.
Prevents audit theater, scope creep, semantic drift, and silent
contradiction accumulation.
**In-Scope:** Auditor role classes; 10-phase audit sequence; Fallacy
Checklist; decentralized Sidecar Model; Unknowns governance; verification
gate enforcement; adversarial audit layer; Full Stop Review triggers;
autonomous auditor constraints.
**Out-of-Scope:** Engineering specifications; ethical policy detail
(→ `Admin/Ethical_Constraints.md`); governance authority structure
(→ `Admin/Governance_Charter.md`); canonical terms
(→ `Admin/Canonical_Terms.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** `Admin/Forge_Audit_Kit.md`; `Admin/Verification_Gates_LF.md`;
all repository files.
> ⚠️ *AP-004 (cross-auditor disagreement resolution) open.*

---

### `Admin/Verification_Gates_LF.md`
**Purpose:** Single canonical source for the six promotion gates (G1–G6).
Every file's Verification Ref field points here.
**In-Scope:** Gate definitions G1–G6 with pass criteria; failure routing;
Full Stop Review triggers; enforcement rules (sequential, binding,
self-approval prohibition).
**Out-of-Scope:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`);
full adversarial battery (→ `Admin/Auditor_Protocols.md`); condensed audit
reference (→ `Admin/Forge_Audit_Kit.md`); cryptographic gate enforcement
(→ `Admin/Security_Protocols.md`).
**Upstream:** `Admin/Auditor_Protocols.md` (source of truth; conflicts
resolve there); `Admin/Governance_Charter.md`.
**Downstream:** All repository files (Verification Ref field);
`Admin/Forge_Audit_Kit.md`; `Admin/Security_Protocols.md` (Phase 3).
> ⚠️ *VG-001 (synchronization authority chain) blocks Specification
> promotion. Suggested Reading Order: place after `Admin/File_Template.md`.*
> ⚠️ **Verification Ref fix needed:** Several gate files still point to
> `Admin/Forge_Audit_Kit.md` — correct target is this file.

---

### `Admin/Canonical_Terms.md`
**Purpose:** Single source of truth for repository vocabulary.
Prevents semantic drift across multi-agent cycles.
**In-Scope:** Authoritative vocabulary mappings; conflict resolution rules;
anti-drift guardrails; banned terms and approved replacements.
**Out-of-Scope:** Component blueprints; API schemas; ethical policy
(→ `Admin/Ethical_Constraints.md`); operational routing semantics
(→ `Architecture/Forge_flow.md` is authoritative for gate logic terms;
conflicts escalate here as Active Disputes); governance tier authority
(→ `Admin/Governance_Charter.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Architecture/Forge_flow.md`;
`Discovery.md` Rename Registry.
**Downstream:** All repository files; `Admin/Auditor_Protocols.md`
(Fallacy 4 enforcement); `Admin/Security_Protocols.md` (CT-004 pending).
> ⚠️ *CT-002 (Component Library Schema) blocks
> `Operations/Gate_02_Triage.md` promotion.
> CT-004 (Trusted Initialization Environment) blocks
> `Admin/Security_Protocols.md` Section III.2 promotion.*

---

### `Admin/Engineer_Protocols.md`
**Purpose:** Cognitive and procedural protocols for engineering
contributors. Fills the gap between governance (what is permitted)
and domain specifications (what is built).
**In-Scope:** Pragmatic question framework; assumption challenge triggers;
anti-reinvention rules; failure-harvesting doctrine; Engineer ↔ Auditor
dispute resolution.
**Out-of-Scope:** Specific engineering calculations (→ domain files);
audit procedures (→ `Admin/Auditor_Protocols.md`); auditor role classes
(→ `Admin/Auditor_Protocols.md`).
**Upstream:** `Admin/Auditor_Protocols.md`; `Admin/Ethical_Constraints.md`;
`Discovery.md`.
**Downstream:** All engineering contributors; all Operations/ and
Architecture/ domain files.
> ⚠️ *EP-004 (engineering authority boundary) undefined.*

---

### `Admin/Security_Protocols.md`
**Purpose:** Cryptographic enforcement layer. Bridges constitutional
governance declarations and operational integrity procedures.
**In-Scope:** Multi-signature human override verification (GOV-006
resolution); automated code-signing protocols; node identity verification;
key rotation cycles; degraded-operation security doctrine; authentication
event logging (SEC-REG-001).
**Out-of-Scope:** Component infiltration prevention for salvaged hardware
(→ `Operations/Electronics.md`); OS firewall or network firmware rules;
physical facility access; constitutional doctrine
(→ `Admin/Governance_Charter.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Admin/Repository_Integrity_Protocol.md`;
`Admin/Canonical_Terms.md` (CT-004 prerequisite);
`Operations/Electronics.md` (Logic-Zero wipe prerequisite).
**Downstream:** `Admin/Repository_Integrity_Protocol.md` (Phase 3);
`Admin/Governance_Charter.md` (GOV-006 resolution);
all governance files (signing eligibility).
> ⚠️ *SEC-001 (quorum under network partition), SEC-007 (external
> root-of-trust architecture) are Critical. CT-004 blocks Section III.2.*

---

### `Admin/Repository_Integrity_Protocol.md`
**Purpose:** Operational integrity enforcement procedures. Bridges
constitutional integrity requirements and fully enforced protections.
**In-Scope:** Integrity baseline definitions; violation detection
(human-in-the-loop at v0); violation classification (Minor/Major/
Constitutional) and response ladder; recovery procedures; automation
migration path (Phase 1→2→3); incident logging.
**Out-of-Scope:** Cryptographic authentication implementation
(→ `Admin/Security_Protocols.md`); constitutional doctrine
(→ `Admin/Governance_Charter.md`); CI/CD automation mechanics.
**Upstream:** `Admin/Governance_Charter.md` (GOV-003 originating unknown);
`Admin/Auditor_Protocols.md` (Challenge Classes 6, 9, 10);
`Admin/Ethical_Constraints.md`.
**Downstream:** `Admin/Forge_Audit_Kit.md` (RIP-004 addition to opening
checklist); `Admin/AUDIT_HARNESS.py`; `Admin/Security_Protocols.md`
(Phase 3); `Unknowns.md`; `Discovery.md` (Archive directory — RIP-001).
> ⚠️ *RIP-001 (prior-state archival system not established) is Critical.
> Archive directory has not yet been created — add [PLANNED] entry to
> Discovery.md when established.*

---

### `Admin/Ship_of_Theseus_Right_to_Repair.md`
**Purpose:** Philosophical and legal load-bearing argument for the
Forge's repair-first doctrine. Ethical and legal defense framework for
treating Forge outputs as restorations.
**In-Scope:** Ship of Theseus paradox as repair-first grounding;
right-to-repair legal defense strategy; grain preservation system as
provenance mechanism; Bootstrap Doctrine and Graduation Rule continuity;
QR code provenance framework (placeholder).
**Out-of-Scope:** Full triage workflow (→ `Operations/Gate_02_Triage.md`);
grain storage protocol (→ ST-001 pending); QR standard (→ ST-002 pending);
jurisdiction-specific legal verification (→ ST-003 — human decision);
G.E.C.K. seeding specs (→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Operations/Gate_02_Triage.md`; `Architecture/Components.md`.
**Downstream:** `Operations/Gate_02_Triage.md`;
`Architecture/Geck_forge_seed.md`.
> ⚠️ *ST-003 (legal applicability by jurisdiction) blocks commercial
> operation. Non-blocking for Exploration.*

---

### `Admin/Trajectories.md`
**Purpose:** Defines the evolutionary trajectory v0 through v5. Scope
routing destination for all out-of-version capabilities.
**In-Scope:** Version trajectory with survival thresholds and exit
conditions; FRT doctrine and floor value ([2–5%] placeholder); revenue
allocation framework; scope routing destination for future capabilities.
**Out-of-Scope:** Component taxonomy for future versions (→ module files
when versions become active); detailed economic model
(→ `economics_v0.md` [PLANNED]); FRT measurement
(→ `Operations/Gate_07_Utilization.md`); component procurement
(→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Operations/Energy.md`;
`Architecture/Geck_forge_seed.md`.
**Downstream:** All operational and architecture files (scope routing);
`Operations/Gate_07_Utilization.md`; `economics_v0.md` [PLANNED].
> ⚠️ *TR-001 (v1 profitability baseline) blocks v0→v1 transition.*

---

## Section 2 — Architecture/

---

> **Vocabulary authority note:** `Architecture/Forge_flow.md` is the
> operational vocabulary standard for the entire repository. For any
> undefined operational term, consult `Architecture/Forge_flow.md`
> §Defined Terms before `Admin/Canonical_Terms.md`. This is the only
> file in the repository that is simultaneously an operational document
> and a vocabulary standard for all others.

---

### `Architecture/Forge_flow.md`
**Purpose:** Minimal viable operational logic of the Lazarus Forge AND
repository-wide vocabulary reference standard. Authoritative for gate
logic, outcome paths, and the want/need policy.
**In-Scope:** v0 gate logic (8 sequential decision gates); Gate
Correspondence table; outcome paths and reversibility; Human/AI Oversight
Gate logic; want/need policy; fabrication priority order; primary KPI
definition; termination conditions; all Defined Terms (repository-wide).
**Out-of-Scope:** Hardware specifications (→ individual Operations/ files);
Reduction module specification (→ FL-002 — no owning file yet); component
triage workflow (→ `Operations/Gate_02_Triage.md`); energy accounting
(→ `Operations/Energy.md`); autonomous logic (→ `Architecture/Cognitive_Frameworks.md`);
version roadmap (→ `Admin/Trajectories.md`).
**Upstream:** `Admin/Canonical_Terms.md`; `Admin/Ethical_Constraints.md`;
`Architecture/Components.md`.
**Downstream:** All repository files (Defined Terms); all Operations/ gate
files; `Architecture/Forge_Net.md`; `Admin/Canonical_Terms.md`.
> ⚠️ *FL-001 (gate logic determinism at boundary cases) blocks
> Specification promotion.*
> ⚠️ *FL-002 (Reduction module — no owning file) is a critical gap:
> the only fully irreversible step in the flow has no owning specification.
> See `Operations/Gate_03_Reduction.md` — now exists as Exploration.
> FL-002 should be reviewed for resolution.*

---

### `Architecture/Components.md`
**Purpose:** Minimum component architecture for a functioning and
persistent Lazarus Forge. Governs all component classification decisions.
**In-Scope:** Component taxonomy (Critical, Useful, Bootstrap) with
definitions; Bootstrap Doctrine and Graduation Rule; dual-use annotation
standard; version mapping v0–v3.
**Out-of-Scope:** Electronics, software, biological, or optical systems
(→ downstream versions); detailed engineering specs (→ domain files);
energy infrastructure (→ `Operations/Energy.md`); G.E.C.K. manifest
(→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Architecture/Forge_flow.md`; `Architecture/Geck_forge_seed.md`;
`Admin/Ethical_Constraints.md`.
**Downstream:** `Architecture/Geck_forge_seed.md`;
`Operations/Gate_02_Triage.md`; all Operations/ gate files.
> ⚠️ *CO-002 (metrology precision thresholds) deferred to first
> fabrication trials.*

---

### `Architecture/Geck_forge_seed.md`
**Purpose:** Smallest coherent set of tools, data, and doctrine capable
of instantiating a new Lazarus Forge from a standing start.
**In-Scope:** Minimum viable seed definition; 8 core G.E.C.K. modules
and criticality rationale; procurement doctrine; precision as capability
threshold (introductory); marine variant module list (exploratory);
success criteria and scaling pathway.
**Out-of-Scope:** Detailed engineering specs for any G.E.C.K. module;
full precision doctrine (→ `Precision_LF.md` [PLANNED]);
Leviathan chassis (→ `Admin/Trajectories.md`); energy infrastructure
(→ `Operations/Energy.md`); component taxonomy (→ `Architecture/Components.md`).
**Upstream:** `Architecture/Components.md`; `Architecture/Forge_flow.md`;
`Admin/Ethical_Constraints.md`.
**Downstream:** `Architecture/Components.md` (Bootstrap Doctrine anchor);
`Admin/Trajectories.md`; `Precision_LF.md` [PLANNED].
> ⚠️ *GK-005 (Precision_LF.md not yet created) non-blocking at Exploration.*

---

### `Architecture/Engineering.md`
**Purpose:** Single durable source of foundational engineering truth and
judgment for all Forge activities. Broad principles layer.
**In-Scope:** Foundational engineering principles; rules of thumb;
core mechanical, structural, and systems engineering fundamentals;
materials behavior overview; Forge-specific safety factors; Arkansas
climate derating; progressive engineering path.
**Out-of-Scope:** Detailed calculations for specific subsystems;
CNC kinematic protection protocols or salvaged gantry rigidity doctrine
(→ `Architecture/Mechanical_Structures.md`); fabrication techniques
(→ domain files); software or electronics design (→ dedicated files).
**Upstream:** `Admin/Ethical_Constraints.md`; `Admin/Engineer_Protocols.md`.
**Downstream:** All Operations/ and Architecture/ domain files;
`Architecture/Mechanical_Structures.md`.
> ⚠️ *EN-001 (validated safety factors for salvaged materials) is Critical
> — blocks structural specification.*
> ℹ️ *Reciprocal scope note needed in this file: add
> `Architecture/Mechanical_Structures.md` to its Out-of-Scope section.*

---

### `Architecture/Mechanical_Structures.md`
**Purpose:** Structural, mechanical, and kinematic engineering doctrine
for salvaged-component fabrication machinery. Extends
`Architecture/Engineering.md` principles into the specific constraints
of salvaged frames, mismatched rails, and abrasive Forge environments.
**In-Scope:** Gantry rigidity and damp-filling criteria; thermal expansion
compensation rules; kinematic interlock matrix (Kinematic Fault 01,
Resonance Mitigation, E-Stop Lockout, Alignment Fault); bearing
contamination protection doctrine; sacrificial shear coupling mandate;
positive-pressure spindle purge; falsifiable MTBMF metric.
**Out-of-Scope:** Foundational engineering principles and safety factor
doctrine (→ `Architecture/Engineering.md`); G-code or part geometries;
motor driver schematics (→ `Operations/Electronics.md` [PLANNED]);
chemistry profiles (→ `Operations/Air_Scrubber.md`); Air Scrubber
back-pressure specs (→ `Operations/Air_Scrubber.md`).
**Upstream:** `Architecture/Engineering.md`; `Admin/Ethical_Constraints.md`;
`Admin/Mechanical_Structures.md` (Verification Ref:
`Admin/Verification_Gates_LF.md`).
**Downstream:** All fabrication machinery specifications that require
gantry or kinematic doctrine.
> ⚠️ *ME-001 (resonance mapping on mismatched rails) makes interlock
> thresholds provisional — tagged in matrix.*
> ℹ️ *Replaces the planned `Architecture/Structural_Engineering.md` and
> `Architecture/Mechanical_Systems.md` entries — those planned files
> should be retired from Discovery.md.*

---

### `Architecture/Cognitive_Frameworks.md`
**Purpose:** Defines how Forge systems think safely under uncertainty.
Cognitive reliability architectures, distributed trust, and redundancy
frameworks for autonomous systems in degraded or adversarial environments.
**In-Scope:** Cognitive reliability layers (Layer 0–6); framework taxonomy
(A–G); confidence collapse states (Green–Black); return-to-base doctrine;
split-brain doctrine; rogue node identification and containment; AI
consensus structures and diversity requirements.
**Out-of-Scope:** PCB fabrication (→ `Operations/Electronics.md`);
ethical policy itself (→ `Admin/Ethical_Constraints.md`); individual
Leviathan mission logic (→ `Tests/Leviathan_testing.md`); networking
implementation (→ `Architecture/Forge_Net.md`); cryptographic protocols
(→ `Admin/Security_Protocols.md`).
**Upstream:** `Admin/Ethical_Constraints.md`; `Operations/Electronics.md`;
`Admin/Auditor_Protocols.md`.
**Downstream:** `Architecture/Forge_Net.md`; `Tests/Leviathan_testing.md`;
`Operations/Support_Raft_v0.md`; `Admin/Trajectories.md`.
> ⚠️ *CF-001 (hardware watchdog minimum standard) blocks any
> Specification-level autonomous architecture.*
> ⚠️ *CF-DS-001 (centralized vs. distributed cognition) and CF-DS-002
> (human override authority scope) are active disputes.*

---

### `Architecture/Forge_Net.md`
**Purpose:** Decentralized data and physical infrastructure connecting
forge instances into a resilient, self-improving ecology.
**In-Scope:** Local-primary/network-sync-secondary doctrine; data layer
architecture (local cache, shared knowledge base, cognitive save states,
validation layer); cluster formation and resource sharing; trust weighting
and federation; failure, loss, and reintegration doctrine; network security
threat model; data privacy classification tiers.
**Out-of-Scope:** Physical networking hardware specs (not yet assigned);
specific database software; detailed cluster governance rules (emergent);
delay-tolerant networking protocol detail (→ `Tests/Leviathan_testing.md`);
rogue node management (→ `Architecture/Cognitive_Frameworks.md`);
energy cost of network operation (→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_01_Intake.md`; `Architecture/Cognitive_Frameworks.md`;
`Admin/Ethical_Constraints.md`; `Tests/Leviathan_testing.md`;
`Operations/Energy.md`.
**Downstream:** Inter-forge logistics files (downstream, depend on this);
`Admin/Trajectories.md`.
> ⚠️ *FN-001 (data validation criteria) and FN-005 (data privacy and
> access control) are Critical — both block first network connection.*
> ℹ️ *Verification Ref in this file points to `Admin/Forge_Audit_Kit.md`
> — should be corrected to `Admin/Verification_Gates_LF.md`.*

---

## Section 3 — Operations/Gates

> **Gate flow reading order:** G01 → G02 → G03 → G04 → G05 → G06 → G07
> All gate logic and shared vocabulary derives from
> `Architecture/Forge_flow.md`. Gate files define how; Forge_flow defines
> what and when.

---

### `Operations/Gate_01_Intake.md`
**Purpose:** Entry point for all items entering the Forge. Makes
information available for downstream recovery decisions — does not make
recovery decisions itself.
**In-Scope:** Entry protocol for all incoming items; safety screening
(hazards, energetics, biological, chemical, radiological); physical
document handling; reference database lookup doctrine; item tagging and
provenance recording; parts list generation; fastener and small component
recovery; unknown item hold-and-inspect protocol; handoff to Gate_02.
**Out-of-Scope:** Classification and triage workflow
(→ `Operations/Gate_02_Triage.md`); reference database content or schema
(→ `Architecture/Forge_Net.md`); network sync protocol
(→ `Architecture/Forge_Net.md`); energetic material disposal doctrine
(→ GI-002 — not yet assigned); air handling (→ `Operations/Air_Scrubber.md`);
facility siting (→ UNK-006 — no file exists yet).
**Upstream:** `Architecture/Forge_Net.md` (reference database);
`Admin/Ethical_Constraints.md`; `Architecture/Forge_flow.md`.
**Downstream:** `Operations/Gate_02_Triage.md`; `Architecture/Forge_Net.md`
(intake records as network knowledge artifacts).
> ⚠️ *7 open unknowns. GI-001 (reference database content) and GI-002
> (energetic discharge doctrine) are highest risk.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Gate_02_Triage.md`
**Purpose:** Decision gateway between reuse and destruction. Determines
whether a component can still function or be restored at lower cost than
fabricating new.
**In-Scope:** Triage principles and philosophy; false-positive tolerance
doctrine; Strategic Recoverability tier classification; Gate Correspondence
table; queue economics doctrine; five triage stations (Station 0–4);
Triage Terminal and Human/AI Oversight Gate behavior; failure modes and
mitigations; minimum viable triage configuration.
**Out-of-Scope:** Master gate logic and shared vocabulary
(→ `Architecture/Forge_flow.md`); decontamination and air handling
(→ `Operations/Air_Scrubber.md`); electrical component harvesting
(→ `Operations/Electronics.md`); material recovery and reduction methods
(→ `Operations/Gate_03_Reduction.md`); Anti-Weaponization pattern-matching
(→ `Admin/Ethical_Constraints.md`); component taxonomy
(→ `Architecture/Components.md`); FRT reinvestment accounting
(→ `Operations/Gate_07_Utilization.md`).
**Upstream:** `Operations/Gate_01_Intake.md`; `Architecture/Forge_flow.md`;
`Architecture/Components.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** `Operations/Gate_03_Reduction.md`;
`Operations/Gate_04_Separation_Mechanical.md`;
`Operations/Gate_06_Fabrication.md`;
`Admin/Ship_of_Theseus_Right_to_Repair.md`.
> ⚠️ *CT-002 (Component Library Schema) is a blocking unknown.
> 1 active dispute. Highest Risk: High.*

---

### `Operations/Gate_03_Reduction.md`
**Purpose:** The only fully irreversible step in the Forge operational
flow. Receives items that have exhausted all recovery paths and reduces
them to feedstock. Irreversibility governs every design decision here.
**In-Scope:** Reduction doctrine — when permitted and what prerequisites
must be met; output envelope; prohibited inputs; method selection doctrine
(shredding, cutting, milling); contamination discovery protocol; dust and
particulate handling; emergency shutdown doctrine and safe states; handoff
to Gate_04; integration with Air Scrubber.
**Out-of-Scope:** Gate logic routing items to Reduction
(→ `Architecture/Forge_flow.md`); upstream hazard screening
(→ `Operations/Gate_01_Intake.md`); specific machine selection
(→ GR-002 — not yet assigned); dust collection hardware
(→ `Operations/Air_Scrubber.md`); purification processing of output
(→ `Operations/Gate_04_Separation_Mechanical.md`,
`Operations/Gate_05_Separation_Thermal.md`); energy accounting
(→ `Operations/Energy.md`); facility siting (→ UNK-006);
biological or chemical waste disposal beyond containment
(→ GR-003 — not yet assigned).
**Upstream:** `Operations/Gate_02_Triage.md`; `Architecture/Forge_flow.md`;
`Operations/Gate_01_Intake.md`; `Operations/Air_Scrubber.md`.
**Downstream:** `Operations/Gate_04_Separation_Mechanical.md`;
`Operations/Air_Scrubber.md`.
> ⚠️ *5 open unknowns. Highest Risk: High. FL-002 resolution candidate —
> this file may now satisfy the "no owning file for Reduction" gap.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Gate_04_Separation_Mechanical.md`
**Purpose:** Upstream mechanical decision point in the Purification stage.
Diverts usable material away from the energy-intensive Spin Chamber where
possible. Refusal-first: uncertain material is held, not passed downstream.
**In-Scope:** Design intent and operating philosophy; physical subsystem
descriptions (rotor, sensors, collection zones, fail-to-bin protocol);
RPM exploration band and stratification behavior; sensor cross-check and
confidence scoring; output classification (Class A, B, C, Unknown Bulk,
Fail); falsifiable performance metrics (Material Diversion Rate, Unknown
Bulk Rate); Bootstrap Proxy Mode; lifecycle and degraded operation behavior.
**Out-of-Scope:** Upstream feedstock reduction (→ `Operations/Gate_03_Reduction.md`);
thermal processing of Class C output
(→ `Operations/Gate_05_Separation_Thermal.md`); component triage of
Unknown Bulk (→ `Operations/Gate_02_Triage.md`); air handling
(→ `Operations/Air_Scrubber.md`); energy accounting
(→ `Operations/Energy.md`); marine thermal sink integration
(→ `Operations/Support_Raft_v0.md`); electromagnetic field bias
(→ `Admin/Trajectories.md` — future version); detailed sensor specs
(→ not yet assigned); powder feedstock handling (explicit non-goal,
all versions).
**Upstream:** `Operations/Gate_03_Reduction.md`; `Architecture/Forge_flow.md`;
`Operations/Air_Scrubber.md`.
**Downstream:** `Operations/Gate_05_Separation_Thermal.md`;
`Operations/Gate_02_Triage.md` (Unknown Bulk);
`Operations/Gate_06_Fabrication.md` (Class A direct path).
> ⚠️ *8 open unknowns. 1 active dispute. Verification Ref points to
> `Forge_Audit_Kit.md` — correct to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Gate_05_Separation_Thermal.md`
**Purpose:** Primary thermal processing module (Spin Chamber). Converts
metallic feedstock into ranked material streams through induction heating,
slow rotation, and electromagnetic field stabilization.
**In-Scope:** Operating principle and design intent; physical geometry and
scale envelope (v0); materials selection (crucible and outer shell);
rotation system parameters; heating strategy and thermal operating bands;
electromagnetic field approach; atmosphere control; extraction interfaces
and output categories; wire extrusion interface (planned — welding wire
pathway); instrumentation and control philosophy; failure philosophy.
**Out-of-Scope:** Upstream feedstock preparation
(→ `Operations/Gate_03_Reduction.md`); mechanical separation decisions
(→ `Operations/Gate_04_Separation_Mechanical.md`); wire extrusion nozzle
design (→ `Admin/Trajectories.md` — future version); welding wire
qualification (→ downstream, not yet assigned); self-replication
architecture (→ `Architecture/Forge_flow.md`,
`Architecture/Geck_forge_seed.md`); facility siting (→ SC-006 — UNK-006);
MHD auxiliary coil detail (→ `Admin/Trajectories.md`); drive system
geometry (→ SC-005 prerequisite); energy accounting
(→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md`;
`Architecture/Forge_flow.md`; `Operations/Energy.md`.
**Downstream:** `Operations/Gate_06_Fabrication.md`; wire extrusion
interface (future).
> ⚠️ *5 open unknowns including one Critical (SC-005 — drive system
> geometry prerequisite for dynamic analysis).*

---

### `Operations/Gate_06_Fabrication.md`
**Purpose:** Constructive stage — where recovered and purified material
becomes functional parts, tools, and infrastructure. Arc welding is the
v0 proof-of-concept gatekeeper and entry point for all subsequent
fabrication method introduction.
**In-Scope:** Fabrication doctrine and priority order; arc welding as v0
proof-of-concept gatekeeper; add-to-excess and mill-to-spec philosophy;
welding wire feedstock requirements and qualification criteria; precision
ceiling doctrine; operator safety (PPE, shielding, ventilation); method
introduction and qualification criteria; feedback loop to Component
Library; integration with upstream Gate_04 and Gate_05 outputs.
**Out-of-Scope:** Wire extrusion nozzle design
(→ `Operations/Gate_05_Separation_Thermal.md`); welding wire chemical
qualification (→ UNK-008 — not yet assigned); laser/powder welding,
casting, pressing, forging (→ `Admin/Trajectories.md` — future versions);
machining and milling hardware specification (→ GF-003 — not yet assigned);
energy accounting (→ `Operations/Energy.md`); facility siting beyond
operator PPE (→ UNK-006); Component Library specification
(→ `Architecture/Components.md`); utilization performance metrics
(→ `Operations/Gate_07_Utilization.md`).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md`;
`Operations/Gate_05_Separation_Thermal.md`; `Architecture/Components.md`;
`Architecture/Forge_flow.md`.
**Downstream:** `Operations/Gate_07_Utilization.md`;
`Architecture/Components.md` (fabricated parts feed Component Library).
> ⚠️ *7 open unknowns. 1 active dispute. GF-003 (machining hardware)
> and UNK-008 (wire qualification) are unassigned.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Gate_07_Utilization.md`
**Purpose:** After-action review stage. Where fabricated parts and
recovered components meet operational reality. Produces the record
that makes all future decisions better.
**In-Scope:** After-action review doctrine; performance logging minimum
content; failure mode capture and routing; maintenance frequency tracking;
feedback to Gate_06_Fabrication (precision ceiling improvement); feedback
to Forge_Net (network knowledge); feedback to Forge_flow (classification
rule improvement); retirement handoff doctrine to Gate_02_Triage; FRT
per-cycle logging (measurement only — doctrine in Trajectories.md); part
lifecycle termination conditions.
**Out-of-Scope:** Retirement routing decisions
(→ `Operations/Gate_02_Triage.md`); fabrication methods or precision
ceiling (→ `Operations/Gate_06_Fabrication.md`); component taxonomy
(→ `Architecture/Components.md`); network contribution validation
(→ `Architecture/Forge_Net.md`); gate logic
(→ `Architecture/Forge_flow.md`); energy accounting
(→ `Operations/Energy.md`); formal quality certification (→ GU-003 —
not yet assigned).
**Upstream:** `Operations/Gate_06_Fabrication.md`; `Architecture/Forge_flow.md`;
`Admin/Trajectories.md` (FRT doctrine).
**Downstream:** `Operations/Gate_02_Triage.md` (retirement re-entry);
`Operations/Gate_06_Fabrication.md` (feedback loop);
`Architecture/Forge_Net.md` (utilization data as network knowledge);
`Architecture/Forge_flow.md` (classification rule improvement).
> ⚠️ *5 open unknowns. 1 active dispute. TR-001 (v1 profitability
> baseline) blocks FRT model refinement.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

## Cross-Cutting Notes for Discovery.md Integration

### Planned Files — Status Summary

| File | Status | Notes |
|------|--------|-------|
| `Admin/Governance_Migration_Protocol.md` | PLANNED | GOV-001 resolution target |
| `Admin/Repository_Structure.md` | PLANNED | — |
| `Admin/Forge_Audit_Kit.md` | Verify exists | Referenced by many files |
| `Admin/File_Template.md` | Verify exists | Referenced by Verification_Gates_LF |
| `Admin/AUDIT_HARNESS.py` | Verify exists | RIP Phase 1/2 automation target |
| `economics_v0.md` | PLANNED | TR-001 blocks; v0→v1 transition |
| `Precision_LF.md` | PLANNED | Path TBD; GK-005 originator |
| `Architecture/Structural_Engineering.md` | **RETIRE** | Absorbed by Mechanical_Structures.md |
| `Architecture/Mechanical_Systems.md` | **RETIRE** | Absorbed by Mechanical_Structures.md |
| `Operations/Air_Scrubber.md` | PLANNED/verify | Referenced by Gates 01–04 |
| `Operations/Electronics.md` | PLANNED/verify | Referenced by multiple files |
| `Operations/Energy.md` | PLANNED/verify | Referenced by all gate files |
| `Operations/Support_Raft_v0.md` | PLANNED/verify | Referenced by Cognitive_Frameworks |
| `Operations/Component_Triage_System.md` | PLANNED/verify | Referenced by Gate_04 |
| `/Archive/` directory | NOT YET CREATED | RIP-001 Critical — add when established |

---

### Verification Ref Corrections Required

The following files have Verification Ref pointing to `Admin/Forge_Audit_Kit.md`
rather than the canonical `Admin/Verification_Gates_LF.md`. Flag for correction
on next audit pass:

- `Operations/Gate_01_Intake.md`
- `Operations/Gate_03_Reduction.md`
- `Operations/Gate_06_Fabrication.md`
- `Operations/Gate_07_Utilization.md`
- `Architecture/Forge_Net.md`

Additionally: `Operations/Gate_04_Separation_Mechanical.md` points to
`Forge_Audit_Kit.md` (missing `Admin/` path prefix).

---

### UNK-006 — Facility Siting

Referenced as unresolved by Gates 01, 03, 04, 05, and 06. No file exists.
Should be logged in `Unknowns.md` as a cross-module unknown with those
five gates as dependents if not already tracked.

---

### Governance Tier Summary

| Tier | File | Status |
|------|------|--------|
| Tier 1 | `Admin/Governance_Charter.md` | Active |
| Tier 1 | `Admin/Ethical_Constraints.md` | Active |
| Tier 2 | `Admin/Auditor_Protocols.md` | Active |
| Tier 3 | `Admin/Forge_Audit_Kit.md` | Verify |
| Support | `Admin/Canonical_Terms.md` | Active |
| Support | `Admin/Verification_Gates_LF.md` | Active (Draft) |
| Support | `Admin/Security_Protocols.md` | Active (Draft) |
| Support | `Admin/Repository_Integrity_Protocol.md` | Active (Draft) |
| Support | `Admin/Engineer_Protocols.md` | Active (Draft) |
| Support | `Admin/Ship_of_Theseus_Right_to_Repair.md` | Exploration |
| Support | `Admin/Trajectories.md` | Exploration |

### Architecture Reading Order

1. `Architecture/Forge_flow.md` — vocabulary and gate logic first
2. `Architecture/Components.md` — what must exist
3. `Architecture/Geck_forge_seed.md` — how to seed it
4. `Architecture/Engineering.md` — foundational principles
5. `Architecture/Mechanical_Structures.md` — fabrication machinery doctrine
6. `Architecture/Cognitive_Frameworks.md` — how it thinks
7. `Architecture/Forge_Net.md` — how instances connect

### Operations Gate Flow

`Gate_01` → `Gate_02` → `Gate_03` → `Gate_04` → `Gate_05` → `Gate_06` → `Gate_07`
*(with feedback loops: G07→G02, G07→G06, G06→Components, G02→G04/G06)*

---

*This addendum covers Admin/, Architecture/, and Operations/Gates.
Remaining Operations/ domain files and Tests/ will follow in subsequent
batches. Reconcile against existing Discovery.md before committing —
additive only, not a replacement. File-local Scope Boundary sections
remain authoritative where conflicts exist.*

# Discovery.md — Addendum Section 4: Operations/Domain & Tests/
## Covers: Electronics · Energy · Air_Scrubber · Plastics · Woodworking · Support_Raft · Leviathan_testing
## Status: Draft — append to Discovery_Addendum_Consolidated.md before reconciliation
## Compiled: 2026-05-31

---

> **Preamble — Single Source of Truth Rule** (repeat for standalone use)
> Scope entries here are navigation summaries only. File-local Scope
> Boundary sections remain authoritative. Where this addendum and a
> file's own Scope Boundary conflict, the file wins.

---

## Section 4 — Operations/Domain Files

---

### `Operations/Electronics.md`
**Purpose:** Trust-anchor document for all electronic systems in the
Forge. Governs recovery, validation, fabrication, and integration of
electronic components. Ethics enforcement, hardware watchdogs, TMR
voting, sensor truth, and AI containment all depend on the integrity
of what this file governs. Treats salvaged electronics as potential
threat vectors, not just convenient parts.
**In-Scope:** Non-destructive harvesting protocols and desoldering
standards; firmware trust doctrine and Logic-Zero wipe protocol;
PCB fabrication methods at v0 (CNC milling, laser etching, toner
transfer, dead-bug wiring); soldering standards; Forge-Standard
interface adapter layer; TMR hardware implementation (wiring, voter
circuit, component selection, architectural diversity requirement);
hardware watchdog doctrine (heartbeat enforcement, neutral-state
enforcement); dual-use awareness and annotation standard; toxic
dust and BFR emission profile doctrine; counterfeit and remarked
component detection doctrine.
**Out-of-Scope:** TMR as architectural philosophy or framework
taxonomy (→ `Architecture/Cognitive_Frameworks.md` Framework D);
ethical policy governing dual-use escalation
(→ `Admin/Ethical_Constraints.md`); confidence collapse states and
split-brain doctrine (→ `Architecture/Cognitive_Frameworks.md`);
air scrubber hardware specification or waste stream chemistry
(→ `Operations/Air_Scrubber.md`); component taxonomy
(→ `Architecture/Components.md`); Leviathan mission logic
(→ `Tests/Leviathan_testing.md`); cryptographic key management
(→ EL-006 — not yet assigned); Forge-Net implementation
(→ `Architecture/Forge_Net.md`); facility siting for electronics
work areas (→ UNK-006).
**Upstream:** `Architecture/Cognitive_Frameworks.md` (CF-001, CF-002);
`Admin/Ethical_Constraints.md`; `Operations/Gate_02_Triage.md`
(Station 1 — electrical triage); `Architecture/Forge_flow.md`.
**Downstream:** `Operations/Air_Scrubber.md` (etch waste, flux fumes,
BFR dust, milling particulate); `Operations/Gate_05_Separation_Thermal.md`
(recovered copper and trace metals); `Tests/Leviathan_testing.md`
(TMR and fault response as primary test targets); `Operations/Support_Raft.md`
(fault response integration); `Admin/Security_Protocols.md`
(Logic-Zero wipe is Layer 1 prerequisite for node cluster admission);
`Architecture/Cognitive_Frameworks.md` (CF-001 watchdog standard).
> ⚠️ *8 open unknowns. Highest Risk: High. EL-006 (cryptographic key
> management) unassigned.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Energy.md`
**Purpose:** Energy strategy for the Lazarus Forge at v0. Defines an
incremental path from external grid dependency toward partial
self-sufficiency. Primary function is as a cross-reference anchor —
the Power Demand stub allows all other files to integrate energy
accounting against a common baseline before actual figures are measured.
**In-Scope:** Energy lifecycle progression and design philosophy;
energy source categories and their v0 roles; energy storage doctrine;
Power Demand stub with three operating modes (cross-reference anchor);
primary and secondary performance metrics; explicit non-goals for v0.
**Out-of-Scope:** Hardware specifications for generators, solar arrays,
or battery banks; biogas digester engineering or sizing; battery
thermal containment or fire suppression
(→ EV-003; `Operations/Air_Scrubber.md`); Leviathan power envelope
(→ `Tests/Leviathan_testing.md` LT-001); deep-environment battery
degradation (→ `Tests/Leviathan_testing.md` LT-002); per-module
energy accounting (→ each owning Operations/ file); grid connection
or utility interface specifications.
**Upstream:** `Admin/Trajectories.md` (EV-001 feeds v1 cost model);
`Operations/Gate_07_Utilization.md` (operational energy data).
**Downstream:** All Operations/ gate files (Power Demand stub is the
shared energy accounting baseline); `Tests/Leviathan_testing.md`
(LT-001 depends on this stub existing); `Admin/Trajectories.md`
(TR-001 v1 profitability model); `Operations/Plastics.md`
(pyrolytic oil and syngas as candidate energy inputs);
`Operations/Woodworking.md` (biochar and wood gas as candidate inputs).
> ⚠️ *3 open unknowns. EV-001 (Forge demand baseline) In Progress —
> blocks v1 operating cost model.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Air_Scrubber.md`
**Purpose:** Enabling system for all Forge operations. Without it,
the Forge does not operate. Defines doctrine, functional architecture,
and operational requirements preventing release or accumulation of
hazardous airborne byproducts generated during Forge operation.
**In-Scope:** Air Scrubber design philosophy and doctrine; five-stage
functional architecture (Stages A–E); wet capture variants (Variant
0–4); Saturation Fault and Thermal Fault monitoring requirements;
negative pressure safety boundary doctrine; noise hazard acknowledgment;
energy awareness and power budget estimates; waste as a managed output;
integration hooks to upstream and downstream modules; marine
shallow-water variant (Variant 4, v0 scope).
**Out-of-Scope:** Spin Chamber exhaust heat load
(→ `Operations/Gate_05_Separation_Thermal.md`); Forge power budget
and demand baseline (→ `Operations/Energy.md`); deep-sea compression
module (→ `Admin/Trajectories.md` v2/v3); contamination routing and
waste stream final disposition (→ `Operations/Gate_02_Triage.md`);
scrubber bootstrap minimum for remote deployment
(→ `Architecture/Geck_forge_seed.md`); saturation threshold
calibration values (Placeholder — requires operational data); noise
exposure limits and hearing conservation program
(→ planned `Safety_Protocols.md` [PLANNED]).
**Upstream:** `Operations/Gate_05_Separation_Thermal.md` (primary
exhaust source); `Operations/Gate_04_Separation_Mechanical.md`
(pre-purification exhaust); `Operations/Electronics.md` (etch waste,
flux fumes, BFR dust, milling particulate);
`Operations/Plastics.md` (off-gas, syngas combustion stage, HCl);
`Operations/Woodworking.md` (dust, toxic species off-gas).
**Downstream:** `Tests/Leviathan_testing.md` (shallow-water marine
variant testbed); `Operations/Gate_02_Triage.md` (scrubber chemistry
feedback); `Operations/Energy.md` (thermal sink power demand);
`Architecture/Geck_forge_seed.md` (bootstrap minimal scrubber).
> ⚠️ *3 open unknowns. Highest Risk: High. AS-003 (saturation
> threshold calibration) blocks chemistry validation.*
> ✓ *Verification Ref correctly set to `Verification_Gates_LF.md`.
> Spec Gates: 2/6 — most advanced gate file in Operations/.*

---

### `Operations/Plastics.md`
**Purpose:** Processing path for salvaged plastics. Defines the triage
hierarchy routing polymers toward highest-value recovery, and the
pyrolytic fuel recovery framework for what mechanical repurposing
cannot handle. Pyrolysis is positioned as last-resort recovery, not
primary recycling method.
**In-Scope:** Triage routing doctrine for salvaged industrial and
consumer polymers; conceptual framework for low-pressure, oxygen-free
thermal depolymerization (pyrolysis); high-level design requirements
for batch-fed reaction chamber and condenser array; safety and chemical
containment boundaries for off-gas treatment; char and solid residue
handling doctrine.
**Out-of-Scope:** Precise temperature profiles for individual polymer
blends; mechanical blueprints for extrusion screws or filament-drawing
rigs; refining or fractional distillation specifications; Air Scrubber
hardware or alkaline buffering stage design
(→ `Operations/Air_Scrubber.md`); energetic or radiological hazard
screening (→ `Operations/Gate_01_Intake.md`); contamination routing
beyond plastic stream identification
(→ `Operations/Gate_02_Triage.md`); energy accounting for pyrolysis
operation (→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_01_Intake.md` (halogenated polymer
detection); `Operations/Gate_02_Triage.md` (upstream routing decision
for all plastics); `Operations/Gate_03_Reduction.md` (bulk plastic
shredding before reactor loading); `Operations/Air_Scrubber.md`
(primary safety dependency — off-gas capture, HCl neutralization,
syngas combustion upstream of scrubber inlet).
**Downstream:** `Operations/Gate_06_Fabrication.md` (filament drawing
— mechanical repurposing path); `Operations/Energy.md` (pyrolytic oil
and syngas as candidate energy inputs); `Operations/Gate_05_Separation_Thermal.md`
(waste heat from Spin Chamber as candidate bootstrap heat source);
`Operations/Gate_02_Triage.md` (char residue classification).
> ⚠️ *5 open unknowns. One Critical priority (PL-001 — halogenated
> polymer detection at triage). Highest Risk: High.*
> ⚠️ *Syngas combustion upstream of Air Scrubber inlet is permanent
> doctrine — direct routing is an abandoned path logged as a
> Lessons Learned entry.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

### `Operations/Woodworking.md`
**Purpose:** Full processing chain for wood within the Lazarus Forge —
from standing tree or salvage source through to finished functional or
structural object. Emphasizes salvaged and urban timber, irregular and
green stock, and low-to-high technology methods for self-reliant
fabrication in variable high-humidity environments.
**In-Scope:** Timber sourcing hierarchy (salvage, urban, storm-fall,
standing tree); felling and chainsaw safety doctrine; green wood
handling, rough dimensioning, anisotropic behavior, and drying
doctrine; structural deployment of woodgrain; power tool and hand tool
milling workflows for irregular salvage stock; CNC/router fixturing for
slabs and live-edge material; heat treatment and surface modification;
joinery, adhesive selection, and assembly doctrine; finishing doctrine
for indoor and outdoor applications; waste valorization hierarchy
through to basic papermaking; dust and species-specific hazard doctrine
by climate zone.
**Out-of-Scope:** CNC toolpath generation, G-code, or CAM software
workflows; full shop-wide dust extraction system design
(→ `Operations/Air_Scrubber.md`); structural engineering calculations
for load-bearing wooden members; commercial lumber grading standards
or large-scale industrial forestry.
**Upstream:** `Operations/Gate_02_Triage.md` (salvage timber condition
assessment follows triage logic); `Operations/Gate_03_Reduction.md`
(low-value wood waste routing to biochar or compost);
`Architecture/Engineering.md` (foundational structural principles).
**Downstream:** `Operations/Gate_06_Fabrication.md` (wood as
fabrication feedstock); `Operations/Air_Scrubber.md` (dust extraction,
toxic species off-gas management); `Operations/Energy.md` (biochar and
wood gas as candidate energy inputs); `Admin/Trajectories.md`
(gasification, large-scale processing, structural engineering
calculations — v1+ scope).
> ⚠️ *4 open unknowns. Highest Risk: High. Draft status, 0/6 gates.*
> ℹ️ *Verification Ref points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*
> ℹ️ *This file was previously listed as [PLANNED] in
> Architecture/Engineering.md Out-of-Scope — now exists. Update
> Engineering.md reference accordingly.*

---

## Section 5 — Tests/

---

### `Operations/Support_Raft.md`
*(Note: File is `Support_Raft_v0.md` internally — confirm canonical
filename for Discovery.md. Listed under Operations/ based on file
location; may belong under Tests/ given Leviathan relationship.
Confirm directory placement.)*

**Purpose:** Stationary operational anchor for mobile Leviathan units
operating in open-ocean or high-flow environments. Provides regional
power, data relay, physical recovery, and triage processing
infrastructure — offloading complexity from mobile units so they remain
lightweight and mission-focused. The Raft does not move. Leviathan
units do. Complexity that lives on the Raft stays off the units.
**In-Scope:** SWATH hull architecture and variable draft doctrine;
Sacrificial Shell System (biofouling management via deployable
colonization panels); induction charging dock array and charging
doctrine; Local Truth Cache architecture and local decision authority
during comms blackout; Stasis Mode doctrine and cold storage rack;
power generation hierarchy (wave-surge, solar, thermal gradient);
infrastructure overhead and bootstrap-honest energy accounting;
Material Separation Gate as optional hosted module; marine-specific
challenges (biofouling, corrosion, depth pressure, storm survival);
end-of-region lifecycle and self-consuming protocol; foundational
claim: net positive energy and data surplus to the swarm.
**Out-of-Scope:** Leviathan unit internal architecture
(→ `Tests/Leviathan_testing.md`); Marine GECK seed specification
(→ `Architecture/Geck_forge_seed.md`); detailed Material Separation
Gate operation (→ `Operations/Gate_04_Separation_Mechanical.md`);
storm-survival protocol and multi-Raft coordination
(→ `Admin/Trajectories.md` v1+); swarm-scale coordination logic
(→ `Tests/Leviathan_testing.md` Extensions).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md` (optional
hosted module); `Tests/Leviathan_testing.md` (stress-test environment
for docking, panel swap, biofouling); `Operations/Energy.md` (baseline
energy philosophy); `Admin/Ethical_Constraints.md` (cached and
governing; marine regulatory unknowns route here);
`Architecture/Geck_forge_seed.md` (marine GECK seed variant);
`Admin/Trajectories.md` (v1+ coordination).
**Downstream:** `Tests/Leviathan_testing.md` (Raft as TMR resolution
infrastructure and recovery anchor); `Operations/Electronics.md`
(fault response integration).
> ⚠️ *10 open unknowns across Low–High risk range. SR-001 (galvanic
> corrosion mitigation) is High priority — blocks v1 design.*
> ⚠️ *SR-011, SR-012, SR-013 logged in final audit summary but not
> yet in main unknown registry — confirm they are in sidecar.*
> ℹ️ *Uses older audit health format rather than standard File State
> table — consider template retrofit on next audit pass.*
> ℹ️ *Induction loss estimate corrected from 12% (laboratory) to
> 20–40% (real subsea conditions) — logged in Lessons Learned.*

---

### `Tests/Leviathan_testing.md`
**Purpose:** Hostile-environment test framework for Lazarus Forge–class
autonomous industrial systems. Exists to break assumptions, surface
hidden failure modes, and force autonomous systems to operate under
sustained uncertainty before off-world deployment is attempted.
Leviathan is a filter, not a product. Failure is expected. Learning
is mandatory.
**In-Scope:** Core test philosophy (fail fast, recover often; sensors
lie; record everything worth regretting); power and endurance test
doctrine; failure and recovery requirements; autonomy and control
test objectives (long-horizon execution, fault detection, graceful
degradation, constraint refusal); sensor and environmental interaction
doctrine; ethical and environmental constraints for test operations;
success criteria (reduced uncertainty, identified failure modes,
invalidated assumptions); Leviathan Extensions Framework (A: distributed
units; B: cross-unit learning; networking and communication guidelines;
knowledge classification tiers 1–3; anti-pattern safeguards);
relationship to Lazarus Forge (findings inform architecture, not become
the architecture).
**Out-of-Scope:** Production system design or space-optimized
architecture; mining platform design; surveillance or coercive
capabilities (explicit prohibition); one-shot demonstrator design;
full trust model mechanism for Extension B (→ LT-004 — routes to
`Admin/Trajectories.md`); priority propagation enforcement mechanism
(→ LT-005 — routes to `Admin/Trajectories.md`); swarm-scale
(100s–1000s) coordination specification (→ `Admin/Trajectories.md`);
Raft architecture (→ `Operations/Support_Raft.md`); delay-tolerant
networking protocol detail (referenced by `Architecture/Forge_Net.md`
as a dependency here).
**Upstream:** `Architecture/Cognitive_Frameworks.md` (frameworks under
test; confidence collapse states are test targets);
`Admin/Ethical_Constraints.md` (ethical constraints govern test
operations absolutely — experiment aborted if conflict arises);
`Operations/Energy.md` (LT-001 depends on Power Demand stub);
`Operations/Support_Raft.md` (Raft as recovery and TMR resolution
infrastructure); `Operations/Electronics.md` (TMR and fault response
are primary test targets).
**Downstream:** `Architecture/Cognitive_Frameworks.md` (findings
inform autonomy architecture); `Architecture/Forge_Net.md`
(delay-tolerant networking doctrine); `Operations/Energy.md`
(LT-002 feeds battery degradation data back to storage section);
`Admin/Trajectories.md` (trust model and priority propagation
mechanism design — LT-004, LT-005).
> ⚠️ *6 open unknowns. LT-001 (power envelope — no placeholder
> anchor) and LT-002 (deep-ocean storage degradation) are High risk
> and load-bearing for all autonomy claims.*
> ⚠️ *LT-003 (autonomy architecture unspecified) is High risk —
> without a named decision-making paradigm under test, the framework
> risks producing data without insight.*
> ⚠️ *LT-006 (ethical log survival under unit loss) is Medium risk
> with governance implications — refusal logs may be lost with unit.*
> ℹ️ *Uses older audit health format — consider template retrofit
> on next audit pass.*
> ℹ️ *No Lessons Learned entries yet — pre-deployment.*

---

## Section 6 — Complete Repository Status Summary

*For Discovery.md routing table. Compiled across all batches.*

### Verification Ref Corrections Required
All files below point to `Admin/Forge_Audit_Kit.md` instead of the
canonical `Admin/Verification_Gates_LF.md`:

| File | Current Ref |
|------|-------------|
| `Operations/Gate_01_Intake.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Gate_03_Reduction.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Gate_04_Separation_Mechanical.md` | Forge_Audit_Kit.md (also missing Admin/ prefix) |
| `Operations/Gate_06_Fabrication.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Gate_07_Utilization.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Electronics.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Energy.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Plastics.md` | Admin/Forge_Audit_Kit.md |
| `Operations/Woodworking.md` | Admin/Forge_Audit_Kit.md |
| `Architecture/Forge_Net.md` | Admin/Forge_Audit_Kit.md |

**Recommended:** Single batch correction pass across all ten files.

---

### Planned / Unverified Files — Final Status

| File | Status | Blocking |
|------|--------|----------|
| `Admin/Governance_Migration_Protocol.md` | PLANNED | GOV-001 |
| `Admin/Repository_Structure.md` | PLANNED | — |
| `Admin/Forge_Audit_Kit.md` | Verify exists | Many Verification Refs point here |
| `Admin/File_Template.md` | Verify exists | VG suggested reading order |
| `Admin/AUDIT_HARNESS.py` | Verify exists | RIP Phase 1/2 automation |
| `economics_v0.md` | PLANNED | TR-001 blocks v0→v1 |
| `Precision_LF.md` | PLANNED | GK-005 — path TBD |
| `Safety_Protocols.md` | PLANNED | AS noise/hearing conservation |
| `Architecture/Structural_Engineering.md` | **RETIRE** | Absorbed by Mechanical_Structures.md |
| `Architecture/Mechanical_Systems.md` | **RETIRE** | Absorbed by Mechanical_Structures.md |
| `/Archive/` directory | NOT YET CREATED | RIP-001 Critical |
| `Operations/Component_Triage_System.md` | Verify exists | Referenced by Gate_04 |
| `Operations/Spin_Chamber_v0.md` | Verify exists | Referenced by Gate_04 scope |
| `Operations/Material_Separation_Gate_v0.md` | Verify exists | Referenced by Gate_04/05 |

---

### Cross-Module Unknowns Requiring `Unknowns.md` Entries

| Unknown | Referenced By | Status |
|---------|--------------|--------|
| UNK-006 — Facility siting | Gates 01, 03, 04, 05, 06, Electronics, Woodworking | No owning file — 7 dependents |
| UNK-008 — Welding wire chemical qualification | Gate_06 | Not yet assigned |
| FL-002 — Reduction module no owning file | Forge_flow, Gate_04 | Gate_03 may resolve — verify |
| EC-002 — Anti-Weaponization pattern-matching | Ethical_Constraints, Gate_02 | No mechanism defined |
| EL-006 — Cryptographic key management for electronics | Electronics | Not yet assigned |
| GF-003 — Machining and milling hardware specification | Gate_06 | Not yet assigned |

---

### Repository-Wide Maturity Snapshot

| File | Status | Spec Gates | Highest Risk |
|------|--------|-----------|--------------|
| `Admin/Governance_Charter.md` | Active | — | Critical (GOV-003, 005) |
| `Admin/Ethical_Constraints.md` | Active | — | Critical (EC-001, 002, 003) |
| `Admin/Auditor_Protocols.md` | Active | — | Medium |
| `Admin/Verification_Gates_LF.md` | Draft | — | Low |
| `Admin/Canonical_Terms.md` | Active | — | Medium |
| `Admin/Engineer_Protocols.md` | Draft | — | Low |
| `Admin/Security_Protocols.md` | Draft | — | Critical (SEC-007) |
| `Admin/Repository_Integrity_Protocol.md` | Draft | — | Critical (RIP-001) |
| `Admin/Ship_of_Theseus.md` | Exploration | — | Low |
| `Admin/Trajectories.md` | Exploration | — | Medium |
| `Architecture/Forge_flow.md` | Exploration | — | High (FL-001, FL-002) |
| `Architecture/Components.md` | Exploration | — | Low |
| `Architecture/Geck_forge_seed.md` | Exploration | — | Low |
| `Architecture/Engineering.md` | Draft | — | Critical (EN-001) |
| `Architecture/Mechanical_Structures.md` | Draft | 1/6 | High |
| `Architecture/Cognitive_Frameworks.md` | Exploration | — | High (CF-001, CF-002) |
| `Architecture/Forge_Net.md` | Exploration | — | Critical (FN-001, FN-005) |
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
| `Operations/Support_Raft.md` | Exploration | — | High |
| `Tests/Leviathan_testing.md` | Exploration | — | High |
| `Challenges/Water.md` | New | — | — |

---

*This completes the full repository scope addendum across all known
files. Append to Discovery_Addendum_Consolidated.md or integrate
directly into Discovery.md after reconciliation.*
*File-local Scope Boundary sections remain authoritative in all cases.*

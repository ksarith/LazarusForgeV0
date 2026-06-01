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

## How to Use This File

> **Scope entries are navigation summaries only.**
> File-local Scope Boundary sections remain authoritative.
> Where this file and a file's own Scope Boundary conflict, the file wins.
> Update Discovery.md when files change; do not update files to match Discovery.md.

**Routing quick-reference:**
- "Where does this belong?" → find the owning file in the scope maps below
- "What files does this decision affect?" → check Downstream Recipients
- "What must exist before this file can be promoted?" → check Upstream Dependencies and ⚠️ notes
- "What does this term mean?" → `Architecture/Forge_flow.md` §Defined Terms first; `Admin/Canonical_Terms.md` second
- Full detail always lives in the file itself

---

## Repository Structure

```
Root
├── README.md                            — Project overview and core principles
├── Discovery.md                         — Active working repository navigation layer (this file)
├── Unknowns.md                          — Cross-module unknowns global index

Admin/                                   — Governance, protocols, and doctrine
    ├── Governance_Charter.md            — Constitutional tier; 8 Axioms (Tier 1)
    ├── Ethical_Constraints.md           — Embedded AI governance & anti-weaponization (Tier 1)
    ├── Auditor_Protocols.md             — Verification doctrine; 10-phase sequence (Tier 2)
    ├── Forge_Audit_Kit.md               — Condensed routine multi-agent cycle reference (Tier 3)
    ├── Verification_Gates_LF.md         — Canonical 6 document promotion gates
    ├── File_Template.md                 — 10-section layout standard & Ethical Anchor field
    ├── Canonical_Terms.md               — Anti-drift vocabulary & term exclusions
    ├── Engineer_Protocols.md            — Operational execution standards for engineers
    ├── Security_Protocols.md            — Cryptographic trust & multi-agent node security
    ├── Repository_Integrity_Protocol.md — Baseline enforcement & violation recovery
    ├── Ship_of_Theseus.md               — Right-to-repair philosophical/legal defense
    ├── Trajectories.md                  — Multi-era version roadmap (v0 to interstellar)
    ├── AUDIT_HARNESS.py                 — Automated script supporting verification
    └── Governance_Migration_Protocol.md — [PLANNED] Tier 1 Axiom amendment procedures

Architecture/                            — System architecture and foundational logic
    ├── Forge_flow.md                    — Master decision flow & REPOSITORY VOCABULARY STANDARD
    ├── Components.md                    — Critical vs useful component taxonomy
    ├── Geck_forge_seed.md               — Minimum viable seed specification
    ├── Engineering.md                   — First-principles intellectual backbone
    ├── Mechanical_Structures.md         — Salvaged-frame kinematic and structural doctrine
    ├── Cognitive_Frameworks.md          — Distributed cognition & survival under uncertainty
    └── Forge_Net.md                     — Decentralized data/physical network logistics

Operations/                              — Physical modules and operational systems
    ├── Gate_01_Intake.md                — Entry safety screening & provenance tagging
    ├── Gate_02_Triage.md                — 5-station value preservation decision engine
    ├── Gate_03_Reduction.md             — Irreversible mechanical sizing (feedstock milling)
    ├── Gate_04_Separation_Mechanical.md — Centrifugal stratification & fail-to-bin diversion
    ├── Gate_05_Separation_Thermal.md    — Core induction melting & gradient extraction
    ├── Gate_06_Fabrication.md           — Arc welding & mill-to-spec constructive ceiling
    ├── Gate_07_Utilization.md           — After-action loop & failure data capture
    ├── Electronics.md                   — Salvaged PCB harvesting & Logic-Zero firmware trust
    ├── Energy.md                        — Incremental power bootstrap & load profiles
    ├── Air_Scrubber.md                  — 5-stage negative-pressure containment subsystem
    ├── Plastics.md                      — Polymer triage & 3-stage pyrolysis framework
    └── Woodworking.md                   — Salvaged urban timber milling & drying schedules

Tests/                                   — Test frameworks and deployment platforms
    ├── Support_Raft.md                  — Stationary marine deployment anchor
    └── Leviathan_testing.md             — Deep-ocean autonomous stress-testing

Challenges/                              — Problem layer: why these capabilities exist
    ├── Water.md                         — Water scarcity and contamination (Living Waters)
    ├── Biofouling.md                    — Biological colonization and corrosion in autonomous systems
    ├── Waste.md                         — Discretionary waste, throwaway culture, repair capacity loss
    ├── Planned_Obsolescence.md          — Deliberate unrepairability and locked hardware ecosystems
    └── Critical_Minerals.md             — Rare earth and critical mineral supply chain chokepoints
```

**Planned / not yet created:**
- `Admin/Governance_Migration_Protocol.md` — GOV-001 resolution target
- `economics_v0.md` — TR-001 blocks; required at v0→v1 transition
- `Precision_LF.md` — path TBD; GK-005 originator
- `Safety_Protocols.md` — noise/hearing conservation (AS reference)
- `/Archive/` directory — RIP-001 Critical; add entry here when created

**Retired planned files** (absorbed by `Architecture/Mechanical_Structures.md`):
- `Architecture/Structural_Engineering.md` — no longer needed
- `Architecture/Mechanical_Systems.md` — no longer needed

---

## Rename Registry

Canonical record of filename changes. Stale references in other files,
external documents, or cached AI context should be resolved using this table.

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

---

## Pending Verification Ref Corrections

The following files have `Verification Ref: Admin/Forge_Audit_Kit.md` —
the canonical target is `Admin/Verification_Gates_LF.md`.
Correct on next audit pass for each file:

| File |
|------|
| `Operations/Gate_01_Intake.md` |
| `Operations/Gate_03_Reduction.md` |
| `Operations/Gate_04_Separation_Mechanical.md` *(also missing `Admin/` prefix)* |
| `Operations/Gate_06_Fabrication.md` |
| `Operations/Gate_07_Utilization.md` |
| `Operations/Electronics.md` |
| `Operations/Energy.md` |
| `Operations/Plastics.md` |
| `Operations/Woodworking.md` |
| `Architecture/Forge_Net.md` |

---

## Repository Maturity Snapshot

| File | Status | Spec Gates | Highest Risk |
|------|--------|-----------|--------------|
| `Admin/Governance_Charter.md` | Active | — | Critical (GOV-003, 005) |
| `Admin/Ethical_Constraints.md` | Active | — | Critical (EC-001–003) |
| `Admin/Auditor_Protocols.md` | Active | — | Medium |
| `Admin/Forge_Audit_Kit.md` | Active | — | Low |
| `Admin/Verification_Gates_LF.md` | Draft | — | Low |
| `Admin/File_Template.md` | Active | — | — |
| `Admin/Canonical_Terms.md` | Active | — | Medium |
| `Admin/Engineer_Protocols.md` | Draft | — | Low |
| `Admin/Security_Protocols.md` | Draft | — | Critical (SEC-007) |
| `Admin/Repository_Integrity_Protocol.md` | Draft | — | Critical (RIP-001) |
| `Admin/Ship_of_Theseus.md` | Exploration | — | Low |
| `Admin/Trajectories.md` | Exploration | — | Medium |
| `Admin/AUDIT_HARNESS.py` | Active | — | — |
| `Architecture/Forge_flow.md` | Exploration | — | High (FL-001) |
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
| `Challenges/Water.md` | Active | — | — |
| `Challenges/Biofouling.md` | Active | — | — |
| `Challenges/Waste.md` | Active | — | — |
| `Challenges/Planned_Obsolescence.md` | Active | — | — |
| `Challenges/Critical_Minerals.md` | Active | — | — |

---

## Scope Map — Admin/

> Governance tier hierarchy: Tier 1 (Charter + Ethical_Constraints) →
> Tier 2 (Auditor_Protocols) → Tier 3 (Forge_Audit_Kit) →
> Support layer (all others below).

---

### `Admin/Governance_Charter.md`
**Purpose:** Constitutional root. Defines governance hierarchy, Tier 1 Axioms,
authority relationships, and amendment doctrine.
**In-Scope:** Tier 1 axioms (P-1–P-4, Q-1–Q-4); governance tiers 1–5; bootstrap
and genesis doctrine; escalation and migration doctrine; autonomous governance
constraints; human override doctrine.
**Out-of-Scope:** Runtime execution; cryptographic implementation
(→ `Admin/Security_Protocols.md`); canonical terminology
(→ `Admin/Canonical_Terms.md`); auditor behavior (→ `Admin/Auditor_Protocols.md`).
**Upstream:** None — constitutional root.
**Downstream:** All repository files; `Admin/Auditor_Protocols.md`;
`Admin/Security_Protocols.md`; `Admin/Canonical_Terms.md`;
`Admin/Governance_Migration_Protocol.md` [PLANNED].
> ⚠️ *GOV-003 (integrity enforcement), GOV-005 (constitutional stability),
> GOV-006 (human override authenticity) are Critical open unknowns.*

---

### `Admin/Ethical_Constraints.md`
**Purpose:** Co-Tier 1 control substrate. Determines whether actions are
permitted before determining how to execute them. Hard constraints —
commandments, not guidelines.
**In-Scope:** Anti-Weaponization Doctrine (hardest constraint; not subject to
review); Life Preservation Heuristics; ownership and legal permissibility
framework; high-permission environment constraints; refusal as first-class
action; Pacifist Operating Posture fallback.
**Out-of-Scope:** Constitutional hierarchy (→ `Admin/Governance_Charter.md`);
auditor behavior (→ `Admin/Auditor_Protocols.md`); runtime enforcement code.
**Upstream:** None — co-Tier 1.
**Downstream:** All repository files (Ethical Anchor field);
`Admin/Governance_Charter.md`; `Tests/Leviathan_testing.md`.
> ⚠️ *EC-001 (confidence threshold), EC-002 (Anti-Weaponization
> pattern-matching), EC-003 (human escalation path) all open.*

---

### `Admin/Auditor_Protocols.md`
**Purpose:** Tier 2 operational doctrine for how auditors behave. Prevents
audit theater, scope creep, semantic drift, and silent contradiction
accumulation.
**In-Scope:** Auditor role classes; 10-phase audit sequence; Fallacy Checklist;
decentralized Sidecar Model; Unknowns governance; verification gate enforcement;
adversarial audit layer; Full Stop Review triggers; autonomous auditor constraints.
**Out-of-Scope:** Engineering specifications; ethical policy detail
(→ `Admin/Ethical_Constraints.md`); governance authority structure
(→ `Admin/Governance_Charter.md`); canonical terms
(→ `Admin/Canonical_Terms.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** `Admin/Forge_Audit_Kit.md`; `Admin/Verification_Gates_LF.md`;
all repository files.
> ⚠️ *AP-004 (cross-auditor disagreement resolution) open.*

---

### `Admin/Forge_Audit_Kit.md`
**Purpose:** Condensed routine multi-agent cycle reference. Tier 3 governance
authority — derived from Auditor_Protocols.md. Load this instead of the full
governance corpus to stay within token limits.
**In-Scope:** Condensed audit opening checklist (including Semantic Stability
Check as mandatory Step 3); Verification Maturity Model; Truth Provenance
Labels; Adversarial Priority Weighting; Anti-Theater Doctrine; Confidence Decay
guidance; condensed Fallacy Checklist; AI contribution rules; condensed
verification gates; active unknowns index; dependency map.
**Out-of-Scope:** Full auditor role class doctrine (→ `Admin/Auditor_Protocols.md`);
full adversarial battery (→ `Admin/Auditor_Protocols.md`); full gate definitions
(→ `Admin/Verification_Gates_LF.md`). May not outrank its source files.
**Upstream:** `Admin/Auditor_Protocols.md`; `Admin/Verification_Gates_LF.md`.
**Downstream:** All audit contributors (human and AI) as operational reference.
> ℹ️ *Kit size is a first-class constraint — keep within token budget.*

---

### `Admin/Verification_Gates_LF.md`
**Purpose:** Single canonical source for the six promotion gates (G1–G6).
Every file's Verification Ref field points here.
**In-Scope:** Gate definitions G1–G6 with pass criteria; failure routing; Full
Stop Review triggers; enforcement rules (sequential, binding, self-approval
prohibition).
**Out-of-Scope:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`);
full adversarial battery (→ `Admin/Auditor_Protocols.md`); condensed reference
(→ `Admin/Forge_Audit_Kit.md`); cryptographic gate enforcement
(→ `Admin/Security_Protocols.md`).
**Upstream:** `Admin/Auditor_Protocols.md` (source of truth; conflicts resolve
there); `Admin/Governance_Charter.md`.
**Downstream:** All repository files (Verification Ref field);
`Admin/Forge_Audit_Kit.md`; `Admin/Security_Protocols.md` (Phase 3).
> ⚠️ *VG-001 (synchronization authority chain) blocks Specification promotion.*
> ℹ️ *Suggested Reading Order: place after `Admin/File_Template.md`.*

---

### `Admin/File_Template.md`
**Purpose:** Standard file structure for all LazarusForgeV0 documents. Defines
ten sections and the Ethical Anchor field.
**In-Scope:** Ten-section layout standard (File State, Scope Boundary, File
Purpose, Assumptions, Body, Lessons Learned, Active Disputes, Auditor Notes,
Abandoned Paths, Drift Indicators); Ethical Anchor field definition.
**Out-of-Scope:** Content of any specific file; governance authority hierarchy.
**Upstream:** `Admin/Governance_Charter.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** All repository files — retrofit existing files during audit cycles.
> ℹ️ *Support_Raft.md and Leviathan_testing.md use older audit health format —
> template retrofit recommended on next audit pass for both.*

---

### `Admin/Canonical_Terms.md`
**Purpose:** Single source of truth for repository vocabulary. Prevents semantic
drift across multi-agent cycles.
**In-Scope:** Authoritative vocabulary mappings; conflict resolution rules;
anti-drift guardrails; banned terms and approved replacements.
**Out-of-Scope:** Component blueprints; API schemas; ethical policy
(→ `Admin/Ethical_Constraints.md`); operational routing semantics
(→ `Architecture/Forge_flow.md` is authoritative for gate logic terms; conflicts
escalate here as Active Disputes); governance tier authority
(→ `Admin/Governance_Charter.md`); filename resolution (→ this file's Rename
Registry).
**Upstream:** `Admin/Governance_Charter.md`; `Architecture/Forge_flow.md`
(gate logic terms authoritative there); `Discovery.md` (Rename Registry).
**Downstream:** All repository files; `Admin/Auditor_Protocols.md` (Fallacy 4
enforcement); `Admin/Security_Protocols.md` (CT-004 pending).
> ⚠️ *CT-002 (Component Library Schema) blocks `Operations/Gate_02_Triage.md`
> promotion. CT-004 (Trusted Initialization Environment) blocks
> `Admin/Security_Protocols.md` Section III.2.*

---

### `Admin/Engineer_Protocols.md`
**Purpose:** Cognitive and procedural protocols for engineering contributors.
Fills the gap between governance (what is permitted) and domain specifications
(what is built).
**In-Scope:** Pragmatic question framework (10 questions); assumption challenge
triggers; anti-reinvention and failure-harvesting rules; Engineer ↔ Auditor
dispute resolution; AI-specific engineering contribution guidance.
**Out-of-Scope:** Specific engineering calculations (→ domain files); audit
procedures (→ `Admin/Auditor_Protocols.md`); auditor role classes
(→ `Admin/Auditor_Protocols.md`).
**Upstream:** `Admin/Auditor_Protocols.md`; `Admin/Ethical_Constraints.md`;
`Discovery.md`.
**Downstream:** All engineering contributors; all Operations/ and Architecture/
domain files.
> ⚠️ *EP-004 (engineering authority boundary) undefined.*

---

### `Admin/Security_Protocols.md`
**Purpose:** Cryptographic enforcement layer. Bridges constitutional governance
declarations and operational integrity procedures.
**In-Scope:** Multi-signature human override verification (GOV-006 resolution);
automated code-signing protocols; node identity verification; key rotation cycles;
degraded-operation security doctrine; authentication event logging (SEC-REG-001).
**Out-of-Scope:** Component infiltration prevention for salvaged hardware
(→ `Operations/Electronics.md`); OS firewall or network firmware rules; physical
facility access; constitutional doctrine (→ `Admin/Governance_Charter.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Admin/Repository_Integrity_Protocol.md`;
`Admin/Canonical_Terms.md` (CT-004 prerequisite);
`Operations/Electronics.md` (Logic-Zero wipe prerequisite).
**Downstream:** `Admin/Repository_Integrity_Protocol.md` (Phase 3);
`Admin/Governance_Charter.md` (GOV-006 resolution); all governance files
(signing eligibility at Candidate Specification and above).
> ⚠️ *SEC-001 (quorum under network partition) and SEC-007 (external
> root-of-trust architecture) are Critical. CT-004 blocks Section III.2.*

---

### `Admin/Repository_Integrity_Protocol.md`
**Purpose:** Operational integrity enforcement procedures. Bridges constitutional
integrity requirements and fully enforced protections.
**In-Scope:** Integrity baseline definitions; violation detection
(human-in-the-loop at v0); violation classification (Minor/Major/Constitutional)
and response ladder; recovery procedures; automation migration path (Phase 1→2→3);
incident logging.
**Out-of-Scope:** Cryptographic authentication (→ `Admin/Security_Protocols.md`);
constitutional doctrine (→ `Admin/Governance_Charter.md`); CI/CD automation
mechanics.
**Upstream:** `Admin/Governance_Charter.md` (GOV-003 originating unknown);
`Admin/Auditor_Protocols.md` (Challenge Classes 6, 9, 10);
`Admin/Ethical_Constraints.md`.
**Downstream:** `Admin/Forge_Audit_Kit.md` (RIP-004 — Tier 1 Axiom text
verification addition); `Admin/AUDIT_HARNESS.py`; `Admin/Security_Protocols.md`
(Phase 3); `Unknowns.md`; `Discovery.md` (Archive directory — RIP-001).
> ⚠️ *RIP-001 (prior-state archival system not established) is Critical.
> Archive directory must be added to Discovery.md when created.*

---

### `Admin/Ship_of_Theseus.md`
**Purpose:** Philosophical and legal load-bearing argument for the Forge's
repair-first doctrine. Defense framework for treating Forge outputs as
restorations under right-to-repair law.
**In-Scope:** Ship of Theseus paradox as repair-first grounding; right-to-repair
legal defense strategy; grain preservation system (1g samples) as provenance
mechanism; Bootstrap Doctrine and Graduation Rule continuity; QR code provenance
framework (placeholder).
**Out-of-Scope:** Full triage workflow (→ `Operations/Gate_02_Triage.md`); grain
storage protocol (→ ST-001 pending); QR standard (→ ST-002 pending);
jurisdiction-specific legal verification (→ ST-003 — human decision);
G.E.C.K. seeding specs (→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Operations/Gate_02_Triage.md`; `Architecture/Components.md`.
**Downstream:** `Operations/Gate_02_Triage.md`; `Architecture/Geck_forge_seed.md`.
> ⚠️ *ST-003 (legal applicability by jurisdiction) blocks commercial operation.
> Non-blocking for Exploration.*

---

### `Admin/Trajectories.md`
**Purpose:** Defines the evolutionary trajectory v0 through v5. Scope routing
destination for all out-of-version capabilities. Owns FRT doctrine.
**In-Scope:** Version trajectory with survival thresholds and exit conditions;
FRT doctrine and floor value ([2–5%] Placeholder); revenue allocation framework;
scope routing destination for future capabilities.
**Out-of-Scope:** Component taxonomy for future versions (→ module files when
versions become active); detailed economic model (→ `economics_v0.md` [PLANNED]);
FRT measurement (→ `Operations/Gate_07_Utilization.md`); component procurement
(→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Admin/Governance_Charter.md`; `Operations/Energy.md`;
`Architecture/Geck_forge_seed.md`.
**Downstream:** All operational and architecture files (scope routing for future
capabilities); `Operations/Gate_07_Utilization.md`; `economics_v0.md` [PLANNED].
> ⚠️ *TR-001 (v1 profitability baseline) blocks v0→v1 transition.*

---

## Scope Map — Architecture/

> **Vocabulary authority:** `Architecture/Forge_flow.md` is the operational
> vocabulary standard for the entire repository. For any undefined operational
> term, consult `Architecture/Forge_flow.md` §Defined Terms before
> `Admin/Canonical_Terms.md`. This is the only file that is simultaneously
> an operational document and a vocabulary standard for all others.

> **Architecture reading order:**
> 1. `Forge_flow.md` — vocabulary and gate logic
> 2. `Components.md` — what must exist
> 3. `Geck_forge_seed.md` — how to seed it
> 4. `Engineering.md` — foundational principles
> 5. `Mechanical_Structures.md` — fabrication machinery doctrine
> 6. `Cognitive_Frameworks.md` — how it thinks
> 7. `Forge_Net.md` — how instances connect

---

### `Architecture/Forge_flow.md`
**Purpose:** Minimal viable operational logic of the Lazarus Forge AND
repository-wide vocabulary reference standard. Authoritative for gate logic,
outcome paths, and the want/need policy.
**In-Scope:** v0 gate logic (8 sequential decision gates); Gate Correspondence
table; outcome paths and reversibility; Human/AI Oversight Gate logic; want/need
policy; fabrication priority order; primary KPI definition; termination conditions;
all Defined Terms (repository-wide scope).
**Out-of-Scope:** Hardware specifications (→ individual Operations/ files); energy
accounting (→ `Operations/Energy.md`); autonomous logic
(→ `Architecture/Cognitive_Frameworks.md`); version roadmap
(→ `Admin/Trajectories.md`); cross-module unknowns index (→ `Unknowns.md`);
facility siting (→ UNK-006 — no file yet).
**Upstream:** `Admin/Canonical_Terms.md`; `Admin/Ethical_Constraints.md`;
`Architecture/Components.md`.
**Downstream:** All repository files (Defined Terms); all Operations/ gate files;
`Architecture/Forge_Net.md`; `Admin/Canonical_Terms.md`.
> ⚠️ *FL-001 (gate logic determinism at boundary cases) blocks Specification
> promotion.*
> ℹ️ *FL-002 (Reduction module — no owning file): Gate_03_Reduction.md now
> exists as Exploration — review FL-002 for resolution.*

---

### `Architecture/Components.md`
**Purpose:** Minimum component architecture for a functioning and persistent
Lazarus Forge. Governs all component classification decisions.
**In-Scope:** Component taxonomy (Critical, Useful, Bootstrap) with definitions;
Bootstrap Doctrine and Graduation Rule; dual-use annotation standard; version
mapping v0–v3.
**Out-of-Scope:** Electronics, software, biological, or optical systems
(→ downstream versions); detailed engineering specs (→ domain files); energy
infrastructure (→ `Operations/Energy.md`); G.E.C.K. manifest
(→ `Architecture/Geck_forge_seed.md`).
**Upstream:** `Architecture/Forge_flow.md`; `Architecture/Geck_forge_seed.md`;
`Admin/Ethical_Constraints.md`.
**Downstream:** `Architecture/Geck_forge_seed.md`; `Operations/Gate_02_Triage.md`;
all Operations/ gate files.
> ⚠️ *CO-002 (metrology precision thresholds) deferred to first fabrication trials.*

---

### `Architecture/Geck_forge_seed.md`
**Purpose:** Smallest coherent set of tools, data, and doctrine capable of
instantiating a new Lazarus Forge from a standing start.
**In-Scope:** Minimum viable seed definition; 8 core G.E.C.K. modules and
criticality rationale; procurement doctrine; precision as capability threshold
(introductory); marine variant module list (exploratory); success criteria and
scaling pathway.
**Out-of-Scope:** Detailed engineering specs for any module; full precision
doctrine (→ `Precision_LF.md` [PLANNED]); Leviathan chassis
(→ `Admin/Trajectories.md`); energy infrastructure (→ `Operations/Energy.md`);
component taxonomy (→ `Architecture/Components.md`).
**Upstream:** `Architecture/Components.md`; `Architecture/Forge_flow.md`;
`Admin/Ethical_Constraints.md`.
**Downstream:** `Architecture/Components.md` (Bootstrap Doctrine anchor);
`Admin/Trajectories.md`; `Precision_LF.md` [PLANNED].
> ⚠️ *GK-005 (Precision_LF.md not yet created) non-blocking at Exploration.*

---

### `Architecture/Engineering.md`
**Purpose:** Single durable source of foundational engineering truth and judgment
for all Forge activities. Broad principles layer — the why behind the how.
**In-Scope:** Foundational engineering principles and rules of thumb; core
mechanical, structural, and systems engineering fundamentals; materials behavior
overview; Forge-specific safety factors; Arkansas/southern US climate derating;
progressive engineering path.
**Out-of-Scope:** CNC kinematic protection protocols or salvaged gantry rigidity
doctrine (→ `Architecture/Mechanical_Structures.md`); detailed calculations for
specific subsystems; fabrication techniques (→ domain files); software or
electronics design (→ dedicated files).
**Upstream:** `Admin/Ethical_Constraints.md`; `Admin/Engineer_Protocols.md`.
**Downstream:** All Operations/ and Architecture/ domain files;
`Architecture/Mechanical_Structures.md`.
> ⚠️ *EN-001 (validated safety factors for salvaged materials) is Critical —
> blocks structural specification.*
> ℹ️ *Reciprocal scope note needed: add `Architecture/Mechanical_Structures.md`
> to Out-of-Scope section in the file itself.*

---

### `Architecture/Mechanical_Structures.md`
**Purpose:** Structural, mechanical, and kinematic engineering doctrine for
salvaged-component fabrication machinery. Extends `Architecture/Engineering.md`
principles into the specific constraints of salvaged frames, mismatched rails,
and abrasive Forge environments.
**In-Scope:** Gantry rigidity and damp-filling criteria (80:20 sand/epoxy);
thermal expansion compensation rules; kinematic interlock matrix (Kinematic
Fault 01, Resonance Mitigation, E-Stop Lockout, Alignment Fault); bearing
contamination protection doctrine; sacrificial shear coupling mandate (125%
torque ceiling); positive-pressure spindle purge; falsifiable MTBMF metric
(≥250 hours).
**Out-of-Scope:** Foundational engineering principles and safety factor doctrine
(→ `Architecture/Engineering.md`); G-code or part geometries; motor driver
schematics (→ `Operations/Electronics.md`); chemistry profiles
(→ `Operations/Air_Scrubber.md`); Air Scrubber back-pressure specs
(→ `Operations/Air_Scrubber.md`).
**Upstream:** `Architecture/Engineering.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** All fabrication machinery specifications requiring gantry or
kinematic doctrine.
> ⚠️ *ME-001 (resonance mapping on mismatched salvaged rails) makes interlock
> thresholds provisional — annotated in interlock matrix.*
> ℹ️ *Replaces planned `Architecture/Structural_Engineering.md` and
> `Architecture/Mechanical_Systems.md` — both retired.*

---

### `Architecture/Cognitive_Frameworks.md`
**Purpose:** Defines how Forge systems think safely under uncertainty. Cognitive
reliability architectures, distributed trust, and redundancy frameworks for
autonomous systems in degraded or adversarial environments.
**In-Scope:** Cognitive reliability layers (Layer 0–6); framework taxonomy (A–G);
confidence collapse states (Green–Black); return-to-base doctrine; split-brain
doctrine; rogue node identification and containment; AI consensus structures and
diversity requirements.
**Out-of-Scope:** PCB fabrication (→ `Operations/Electronics.md`); ethical policy
itself (→ `Admin/Ethical_Constraints.md`); individual Leviathan mission logic
(→ `Tests/Leviathan_testing.md`); networking implementation
(→ `Architecture/Forge_Net.md`); cryptographic protocols
(→ `Admin/Security_Protocols.md`).
**Upstream:** `Admin/Ethical_Constraints.md`; `Operations/Electronics.md`
(CF-001 watchdog standard); `Admin/Auditor_Protocols.md`.
**Downstream:** `Architecture/Forge_Net.md`; `Tests/Leviathan_testing.md`;
`Operations/Support_Raft.md`; `Admin/Trajectories.md`.
> ⚠️ *CF-001 (hardware watchdog minimum standard) blocks any Specification-level
> autonomous architecture. CF-002 (correlated AI failure modes) High risk.*
> ⚠️ *CF-DS-001 (centralized vs. distributed cognition) and CF-DS-002 (human
> override authority scope) are active disputes.*

---

### `Architecture/Forge_Net.md`
**Purpose:** Decentralized data and physical infrastructure connecting forge
instances into a resilient, self-improving ecology.
**In-Scope:** Local-primary/network-sync-secondary doctrine; data layer
architecture (local cache, shared knowledge base, cognitive save states,
validation layer); cluster formation and resource sharing; trust weighting and
federation; failure, loss, and reintegration doctrine; network security threat
model; data privacy classification tiers.
**Out-of-Scope:** Physical networking hardware specs (not yet assigned); specific
database software; detailed cluster governance rules (emergent); delay-tolerant
networking protocol (→ `Tests/Leviathan_testing.md`); rogue node management
(→ `Architecture/Cognitive_Frameworks.md`); energy cost of network operation
(→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_01_Intake.md`; `Architecture/Cognitive_Frameworks.md`;
`Admin/Ethical_Constraints.md`; `Tests/Leviathan_testing.md`;
`Operations/Energy.md`.
**Downstream:** Inter-forge logistics files (downstream; depend on this);
`Admin/Trajectories.md`.
> ⚠️ *FN-001 (data validation criteria) and FN-005 (data privacy and access
> control) are Critical — both block first network connection.*
> ℹ️ *Verification Ref in file points to `Admin/Forge_Audit_Kit.md` — correct
> to `Admin/Verification_Gates_LF.md`.*

---

## Scope Map — Operations/Gates

> **Gate flow:** G01 → G02 → G03 → G04 → G05 → G06 → G07
> **Feedback loops:** G07→G02, G07→G06, G06→Components, G02→G04/G06
> All gate logic and shared vocabulary derives from `Architecture/Forge_flow.md`.
> Gate files define *how*; Forge_flow defines *what* and *when*.

---

### `Operations/Gate_01_Intake.md`
**Purpose:** Entry point for all items entering the Forge. Makes information
available for downstream recovery decisions — does not make recovery decisions
itself.
**In-Scope:** Entry protocol for all incoming items; safety screening (hazards,
energetics, biological, chemical, radiological); physical document handling;
reference database lookup doctrine; item tagging and provenance recording; parts
list generation; fastener and small component recovery; unknown item
hold-and-inspect protocol; handoff to Gate_02.
**Out-of-Scope:** Classification and triage workflow
(→ `Operations/Gate_02_Triage.md`); reference database content or schema
(→ `Architecture/Forge_Net.md`); energetic material disposal doctrine
(→ GI-002 — not yet assigned); air handling (→ `Operations/Air_Scrubber.md`);
facility siting (→ UNK-006 — no file yet).
**Upstream:** `Architecture/Forge_Net.md` (reference database);
`Admin/Ethical_Constraints.md`; `Architecture/Forge_flow.md`.
**Downstream:** `Operations/Gate_02_Triage.md`; `Architecture/Forge_Net.md`
(intake records as network knowledge artifacts).
> ⚠️ *7 open unknowns. GI-001 (reference database content) and GI-002
> (energetic discharge doctrine) highest risk.*

---

### `Operations/Gate_02_Triage.md`
**Purpose:** Decision gateway between reuse and destruction. Determines whether a
component can still function or be restored at lower cost than fabricating new.
**In-Scope:** Triage principles and philosophy; false-positive tolerance doctrine;
Strategic Recoverability tier classification; Gate Correspondence table; queue
economics doctrine; five triage stations (Station 0–4); Triage Terminal and
Human/AI Oversight Gate behavior; failure modes and mitigations; minimum viable
triage configuration.
**Out-of-Scope:** Master gate logic and vocabulary (→ `Architecture/Forge_flow.md`);
decontamination and air handling (→ `Operations/Air_Scrubber.md`); electrical
component harvesting (→ `Operations/Electronics.md`); material recovery and
reduction methods (→ `Operations/Gate_03_Reduction.md`); Anti-Weaponization
pattern-matching (→ `Admin/Ethical_Constraints.md`); component taxonomy
(→ `Architecture/Components.md`); FRT reinvestment accounting
(→ `Operations/Gate_07_Utilization.md`).
**Upstream:** `Operations/Gate_01_Intake.md`; `Architecture/Forge_flow.md`;
`Architecture/Components.md`; `Admin/Ethical_Constraints.md`.
**Downstream:** `Operations/Gate_03_Reduction.md`;
`Operations/Gate_04_Separation_Mechanical.md`;
`Operations/Gate_06_Fabrication.md`; `Admin/Ship_of_Theseus.md`.
> ⚠️ *CT-002 (Component Library Schema) is a blocking unknown. 1 active dispute.
> Highest Risk: High.*

---

### `Operations/Gate_03_Reduction.md`
**Purpose:** The only fully irreversible step in the Forge operational flow.
Receives items that have exhausted all recovery paths and reduces them to
feedstock. Irreversibility governs every design decision here.
**In-Scope:** Reduction doctrine — when permitted and prerequisites; output
envelope; prohibited inputs; method selection doctrine (shredding, cutting,
milling); contamination discovery protocol; dust and particulate handling;
emergency shutdown doctrine and safe states; handoff to Gate_04; Air Scrubber
integration.
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
> review for closure.*

---

### `Operations/Gate_04_Separation_Mechanical.md`
**Purpose:** Upstream mechanical decision point in the Purification stage.
Diverts usable material away from the energy-intensive Spin Chamber where
possible. Refusal-first: uncertain material is held, not passed downstream.
**In-Scope:** Design intent and operating philosophy; physical subsystem
descriptions (rotor, sensors, collection zones, fail-to-bin protocol); RPM
exploration band and stratification behavior; sensor cross-check and confidence
scoring; output classification (Class A, B, C, Unknown Bulk, Fail); falsifiable
performance metrics (Material Diversion Rate ≥30%, Unknown Bulk Rate);
Bootstrap Proxy Mode; lifecycle and degraded operation behavior.
**Out-of-Scope:** Upstream feedstock reduction (→ `Operations/Gate_03_Reduction.md`);
thermal processing of Class C output
(→ `Operations/Gate_05_Separation_Thermal.md`); component triage of Unknown Bulk
(→ `Operations/Gate_02_Triage.md`); air handling
(→ `Operations/Air_Scrubber.md`); energy accounting (→ `Operations/Energy.md`);
marine thermal sink (→ `Operations/Support_Raft.md`); electromagnetic field bias
(→ `Admin/Trajectories.md` — future); detailed sensor specs (→ not yet assigned);
powder feedstock (explicit non-goal — all versions).
**Upstream:** `Operations/Gate_03_Reduction.md`; `Architecture/Forge_flow.md`;
`Operations/Air_Scrubber.md`.
**Downstream:** `Operations/Gate_05_Separation_Thermal.md`;
`Operations/Gate_02_Triage.md` (Unknown Bulk);
`Operations/Gate_06_Fabrication.md` (Class A direct path).
> ⚠️ *8 open unknowns. 1 active dispute.*

---

### `Operations/Gate_05_Separation_Thermal.md`
**Purpose:** Primary thermal processing module (Spin Chamber). Converts metallic
feedstock into ranked material streams through induction heating, slow rotation,
and electromagnetic field stabilization.
**In-Scope:** Operating principle and design intent; physical geometry and scale
envelope (v0); materials selection (crucible and outer shell); rotation system
parameters; heating strategy and thermal operating bands; electromagnetic field
approach; atmosphere control; extraction interfaces and output categories; wire
extrusion interface (planned — welding wire pathway); instrumentation and control
philosophy; failure philosophy.
**Out-of-Scope:** Upstream feedstock preparation
(→ `Operations/Gate_03_Reduction.md`); mechanical separation decisions
(→ `Operations/Gate_04_Separation_Mechanical.md`); wire extrusion nozzle design
(→ `Admin/Trajectories.md` — future); welding wire qualification
(→ downstream, not yet assigned); self-replication architecture
(→ `Architecture/Forge_flow.md`, `Architecture/Geck_forge_seed.md`); facility
siting (→ UNK-006); MHD auxiliary coil detail (→ `Admin/Trajectories.md`);
drive system geometry (→ SC-005 prerequisite); energy accounting
(→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md`;
`Architecture/Forge_flow.md`; `Operations/Energy.md`.
**Downstream:** `Operations/Gate_06_Fabrication.md`; wire extrusion interface
(future).
> ⚠️ *5 open unknowns. SC-005 (drive system geometry) is Critical — prerequisite
> for dynamic analysis.*

---

### `Operations/Gate_06_Fabrication.md`
**Purpose:** Constructive stage — where recovered and purified material becomes
functional parts, tools, and infrastructure. Arc welding is the v0
proof-of-concept gatekeeper and entry point for all subsequent fabrication method
introduction.
**In-Scope:** Fabrication doctrine and priority order; arc welding as v0
gatekeeper; add-to-excess and mill-to-spec philosophy; welding wire feedstock
requirements and qualification criteria; precision ceiling doctrine; operator
safety (PPE, shielding, ventilation); method introduction and qualification
criteria; feedback loop to Component Library.
**Out-of-Scope:** Wire extrusion nozzle design
(→ `Operations/Gate_05_Separation_Thermal.md`); welding wire chemical
qualification (→ UNK-008 — not yet assigned); laser/powder welding, casting,
pressing, forging (→ `Admin/Trajectories.md` — future); machining and milling
hardware specification (→ GF-003 — not yet assigned); energy accounting
(→ `Operations/Energy.md`); facility siting beyond operator PPE (→ UNK-006);
Component Library specification (→ `Architecture/Components.md`).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md`;
`Operations/Gate_05_Separation_Thermal.md`; `Architecture/Components.md`;
`Architecture/Forge_flow.md`.
**Downstream:** `Operations/Gate_07_Utilization.md`; `Architecture/Components.md`
(fabricated parts feed Component Library).
> ⚠️ *7 open unknowns. 1 active dispute. GF-003 and UNK-008 unassigned.*

---

### `Operations/Gate_07_Utilization.md`
**Purpose:** After-action review stage. Where fabricated parts and recovered
components meet operational reality. Produces the record that makes all future
decisions better.
**In-Scope:** After-action review doctrine; performance logging minimum content;
failure mode capture and routing; maintenance frequency tracking; feedback to
Gate_06 (precision ceiling); feedback to Forge_Net (network knowledge); feedback
to Forge_flow (classification rule improvement); retirement handoff doctrine to
Gate_02; FRT per-cycle logging (measurement only — doctrine in Trajectories.md);
part lifecycle termination conditions.
**Out-of-Scope:** Retirement routing decisions
(→ `Operations/Gate_02_Triage.md`); fabrication methods or precision ceiling
(→ `Operations/Gate_06_Fabrication.md`); component taxonomy
(→ `Architecture/Components.md`); network contribution validation
(→ `Architecture/Forge_Net.md`); gate logic (→ `Architecture/Forge_flow.md`);
energy accounting (→ `Operations/Energy.md`); formal quality certification
(→ GU-003 — not yet assigned).
**Upstream:** `Operations/Gate_06_Fabrication.md`; `Architecture/Forge_flow.md`;
`Admin/Trajectories.md` (FRT doctrine).
**Downstream:** `Operations/Gate_02_Triage.md` (retirement re-entry);
`Operations/Gate_06_Fabrication.md` (feedback loop);
`Architecture/Forge_Net.md` (utilization data as network knowledge);
`Architecture/Forge_flow.md` (classification rule improvement).
> ⚠️ *5 open unknowns. 1 active dispute. TR-001 blocks FRT model refinement.*

---

## Scope Map — Operations/Domain

---

### `Operations/Electronics.md`
**Purpose:** Trust-anchor document for all electronic systems in the Forge.
Ethics enforcement, hardware watchdogs, TMR voting, sensor truth, and AI
containment all depend on the integrity of what this file governs. Treats
salvaged electronics as potential threat vectors, not just convenient parts.
**In-Scope:** Non-destructive harvesting protocols and desoldering standards;
firmware trust doctrine and Logic-Zero wipe protocol; PCB fabrication methods at
v0 (CNC milling, laser etching, toner transfer, dead-bug wiring); soldering
standards; Forge-Standard interface adapter layer; TMR hardware implementation
(wiring, voter circuit, component selection, architectural diversity); hardware
watchdog doctrine (heartbeat enforcement, neutral-state enforcement); dual-use
awareness and annotation standard; toxic dust and BFR emission profile doctrine;
counterfeit and remarked component detection doctrine.
**Out-of-Scope:** TMR as architectural philosophy
(→ `Architecture/Cognitive_Frameworks.md` Framework D); ethical policy governing
dual-use escalation (→ `Admin/Ethical_Constraints.md`); confidence collapse states
(→ `Architecture/Cognitive_Frameworks.md`); air scrubber hardware
(→ `Operations/Air_Scrubber.md`); component taxonomy
(→ `Architecture/Components.md`); Leviathan mission logic
(→ `Tests/Leviathan_testing.md`); cryptographic key management
(→ EL-006 — not yet assigned); Forge-Net implementation
(→ `Architecture/Forge_Net.md`); facility siting (→ UNK-006).
**Upstream:** `Architecture/Cognitive_Frameworks.md` (CF-001, CF-002);
`Admin/Ethical_Constraints.md`; `Operations/Gate_02_Triage.md` (Station 1);
`Architecture/Forge_flow.md`.
**Downstream:** `Operations/Air_Scrubber.md` (etch waste, flux fumes, BFR dust);
`Operations/Gate_05_Separation_Thermal.md` (recovered copper and trace metals);
`Tests/Leviathan_testing.md` (TMR and fault response — primary test targets);
`Operations/Support_Raft.md` (fault response integration);
`Admin/Security_Protocols.md` (Logic-Zero wipe — Layer 1 prerequisite for node
cluster admission); `Architecture/Cognitive_Frameworks.md` (CF-001 watchdog).
> ⚠️ *8 open unknowns. Highest Risk: High. EL-006 (cryptographic key management)
> unassigned.*

---

### `Operations/Energy.md`
**Purpose:** Energy strategy for the Lazarus Forge at v0. Primary function is as
a cross-reference anchor — the Power Demand stub (Bootstrap ~2–5 kW, Nominal
~15–40 kW, Degraded ~1–3 kW) allows all other files to integrate energy accounting
against a common baseline before actual figures are measured.
**In-Scope:** Energy lifecycle progression and design philosophy; energy source
categories and v0 roles; energy storage doctrine; Power Demand stub with three
operating modes; primary and secondary performance metrics; explicit v0 non-goals.
**Out-of-Scope:** Hardware specifications for generators, solar arrays, or battery
banks; biogas digester engineering; battery thermal containment or fire suppression
(→ EV-003; `Operations/Air_Scrubber.md`); Leviathan power envelope
(→ `Tests/Leviathan_testing.md` LT-001); deep-environment battery degradation
(→ `Tests/Leviathan_testing.md` LT-002); per-module energy accounting
(→ each owning Operations/ file); grid connection or utility interface
specifications.
**Upstream:** `Admin/Trajectories.md` (EV-001 feeds v1 cost model);
`Operations/Gate_07_Utilization.md` (operational energy data).
**Downstream:** All Operations/ gate files (Power Demand stub — shared energy
accounting baseline); `Tests/Leviathan_testing.md` (LT-001 depends on this stub);
`Admin/Trajectories.md` (TR-001 v1 profitability model); `Operations/Plastics.md`
(pyrolytic oil and syngas as candidate inputs); `Operations/Woodworking.md`
(biochar and wood gas as candidate inputs).
> ⚠️ *3 open unknowns. EV-001 (Forge demand baseline) In Progress —
> blocks v1 operating cost model.*

---

### `Operations/Air_Scrubber.md`
**Purpose:** Enabling system for all Forge operations. Without it, the Forge does
not operate. Prevents release or accumulation of hazardous airborne byproducts
generated during Forge operation.
**In-Scope:** Air Scrubber design philosophy and doctrine; five-stage functional
architecture (Stages A–E: sacrificial intercept → ionization → thermal quench →
wet scrubbing → polishing); wet capture variants (Variant 0–4); Saturation Fault
and Thermal Fault monitoring; negative pressure safety boundary doctrine; noise
hazard acknowledgment; energy awareness and power budget estimates; waste as a
managed output; marine shallow-water variant (Variant 4, v0 scope).
**Out-of-Scope:** Spin Chamber exhaust heat load
(→ `Operations/Gate_05_Separation_Thermal.md`); Forge power budget
(→ `Operations/Energy.md`); deep-sea compression module
(→ `Admin/Trajectories.md` v2/v3); contamination routing and waste stream final
disposition (→ `Operations/Gate_02_Triage.md`); scrubber bootstrap minimum for
remote deployment (→ `Architecture/Geck_forge_seed.md`); saturation threshold
calibration values (Placeholder — requires operational data); noise exposure
limits and hearing conservation program (→ `Safety_Protocols.md` [PLANNED]).
**Upstream:** `Operations/Gate_05_Separation_Thermal.md` (primary exhaust);
`Operations/Gate_04_Separation_Mechanical.md` (pre-purification exhaust);
`Operations/Electronics.md` (etch waste, flux fumes, BFR dust);
`Operations/Plastics.md` (off-gas, syngas combustion stage, HCl);
`Operations/Woodworking.md` (dust, toxic species off-gas).
**Downstream:** `Tests/Leviathan_testing.md` (shallow-water marine variant
testbed); `Operations/Gate_02_Triage.md` (scrubber chemistry feedback);
`Operations/Energy.md` (thermal sink power demand);
`Architecture/Geck_forge_seed.md` (bootstrap minimal scrubber).
> ⚠️ *3 open unknowns. Highest Risk: High. AS-003 (saturation threshold
> calibration) blocks chemistry validation.*
> ✓ *Verification Ref correctly set to `Verification_Gates_LF.md`.
> Most advanced gate file in Operations/ at 2/6 spec gates.*

---

### `Operations/Plastics.md`
**Purpose:** Processing path for salvaged plastics. Defines the triage hierarchy
routing polymers toward highest-value recovery, and the pyrolytic fuel recovery
framework for what mechanical repurposing cannot handle. Pyrolysis is last-resort
recovery, not primary recycling method.
**In-Scope:** Triage routing doctrine for salvaged industrial and consumer
polymers; conceptual framework for low-pressure, oxygen-free thermal
depolymerization (pyrolysis, 350°C–450°C); high-level design requirements for
batch-fed reaction chamber and condenser array; safety and chemical containment
boundaries for off-gas treatment; char and solid residue handling doctrine.
**Out-of-Scope:** Precise temperature profiles for individual polymer blends;
mechanical blueprints for extrusion screws or filament-drawing rigs; refining or
fractional distillation specifications; Air Scrubber hardware or alkaline
buffering stage design (→ `Operations/Air_Scrubber.md`); energetic or radiological
hazard screening (→ `Operations/Gate_01_Intake.md`); contamination routing beyond
plastic stream identification (→ `Operations/Gate_02_Triage.md`); energy
accounting for pyrolysis operation (→ `Operations/Energy.md`).
**Upstream:** `Operations/Gate_01_Intake.md` (halogenated polymer detection);
`Operations/Gate_02_Triage.md` (upstream routing decision for all plastics);
`Operations/Gate_03_Reduction.md` (bulk plastic shredding before reactor
loading); `Operations/Air_Scrubber.md` (primary safety dependency — off-gas
capture, HCl neutralization, syngas combustion upstream of scrubber inlet).
**Downstream:** `Operations/Gate_06_Fabrication.md` (filament drawing);
`Operations/Energy.md` (pyrolytic oil and syngas as candidate energy inputs);
`Operations/Gate_05_Separation_Thermal.md` (waste heat as candidate bootstrap
heat source); `Operations/Gate_02_Triage.md` (char residue classification).
> ⚠️ *5 open unknowns. PL-001 (halogenated polymer detection) is Critical and
> Blocking before any hot operational run. Highest Risk: High.*
> ⚠️ *Syngas combustion upstream of Air Scrubber inlet is permanent doctrine —
> direct routing is an abandoned path. Never reverse.*

---

### `Operations/Woodworking.md`
**Purpose:** Full processing chain for wood within the Lazarus Forge — from
standing tree or salvage source through to finished functional or structural
object. Emphasizes salvaged and urban timber, irregular and green stock, and
low-to-high technology methods for self-reliant fabrication in variable
high-humidity environments.
**In-Scope:** Timber sourcing hierarchy (salvage, urban, storm-fall, standing
tree); felling and chainsaw safety doctrine; green wood handling, rough
dimensioning, anisotropic behavior, and drying doctrine; structural deployment
of woodgrain; power tool and hand tool milling workflows for irregular salvage
stock; CNC/router fixturing for slabs and live-edge material; heat treatment and
surface modification; joinery, adhesive selection, and assembly doctrine;
finishing doctrine for indoor and outdoor applications; waste valorization
hierarchy through to basic papermaking; dust and species-specific hazard doctrine
by climate zone.
**Out-of-Scope:** CNC toolpath generation, G-code, or CAM software workflows;
full shop-wide dust extraction system design (→ `Operations/Air_Scrubber.md`);
structural engineering calculations for load-bearing wooden members; commercial
lumber grading standards or large-scale industrial forestry.
**Upstream:** `Operations/Gate_02_Triage.md` (salvage timber condition assessment
follows triage logic); `Operations/Gate_03_Reduction.md` (low-value wood waste
routing to biochar or compost); `Architecture/Engineering.md` (foundational
structural principles).
**Downstream:** `Operations/Gate_06_Fabrication.md` (wood as fabrication
feedstock); `Operations/Air_Scrubber.md` (dust extraction, toxic species
off-gas); `Operations/Energy.md` (biochar and wood gas as candidate inputs);
`Admin/Trajectories.md` (gasification, large-scale processing — v1+ scope).
> ⚠️ *4 open unknowns. Highest Risk: High. Draft, 0/6 gates.*
> ℹ️ *Was listed as [PLANNED] in `Architecture/Engineering.md` — now exists.
> Update Engineering.md Out-of-Scope reference accordingly.*

---

## Scope Map — Tests/

---

### `Tests/Support_Raft.md`
**Purpose:** Stationary operational anchor for mobile Leviathan units operating
in open-ocean or high-flow environments. Provides regional power, data relay,
physical recovery, and triage processing infrastructure. The Raft does not move.
Leviathan units do. Complexity that lives on the Raft stays off the units.
Foundational claim: net positive energy and data surplus to the swarm.
**In-Scope:** SWATH hull architecture and variable draft doctrine; Sacrificial
Shell System (biofouling management via deployable colonization panels); induction
charging dock array; Local Truth Cache and local decision authority during comms
blackout; Stasis Mode doctrine and cold storage rack; power generation hierarchy
(wave-surge, solar, thermal gradient); bootstrap-honest energy accounting;
Material Separation Gate as optional hosted module; marine-specific challenges
(biofouling, galvanic corrosion, storm survival); end-of-region lifecycle and
self-consuming protocol.
**Out-of-Scope:** Leviathan unit internal architecture
(→ `Tests/Leviathan_testing.md`); marine GECK seed specification
(→ `Architecture/Geck_forge_seed.md`); detailed Material Separation Gate
operation (→ `Operations/Gate_04_Separation_Mechanical.md`); storm-survival
protocol and multi-Raft coordination (→ `Admin/Trajectories.md` v1+);
swarm-scale coordination logic (→ `Tests/Leviathan_testing.md` Extensions).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md` (optional hosted
module); `Tests/Leviathan_testing.md` (stress-test environment for docking,
panel swap, biofouling); `Operations/Energy.md`; `Admin/Ethical_Constraints.md`
(cached and governing); `Architecture/Geck_forge_seed.md` (marine GECK variant);
`Admin/Trajectories.md` (v1+ coordination).
**Downstream:** `Tests/Leviathan_testing.md` (Raft as TMR resolution
infrastructure and recovery anchor); `Operations/Electronics.md` (fault response
integration).
> ⚠️ *10 open unknowns. SR-001 (galvanic corrosion mitigation) is High —
> blocks v1 design. SR-011, SR-012, SR-013 logged in audit summary — confirm
> in sidecar.*
> ℹ️ *Uses older audit health format — template retrofit recommended.*
> ℹ️ *Induction loss estimate corrected from 12% to 20–40% (real subsea
> conditions) — see Lessons Learned.*

---

### `Tests/Leviathan_testing.md`
**Purpose:** Hostile-environment test framework for Lazarus Forge–class autonomous
industrial systems. Exists to break assumptions and surface hidden failure modes
before off-world deployment. Leviathan is a filter, not a product. Failure is
expected. Learning is mandatory.
**In-Scope:** Core test philosophy (fail fast, recover often; sensors lie; record
everything worth regretting); power and endurance test doctrine; failure and
recovery requirements; autonomy and control test objectives (long-horizon
execution, fault detection, graceful degradation, constraint refusal); sensor and
environmental interaction doctrine; ethical and environmental constraints (absolute
— experiment aborted if conflict arises); success criteria (reduced uncertainty,
identified failure modes, invalidated assumptions); Leviathan Extensions Framework
(A: distributed units; B: cross-unit learning; networking and communication
guidelines; knowledge classification tiers 1–3; anti-pattern safeguards).
**Out-of-Scope:** Production system design or space-optimized architecture; mining
platform design; surveillance or coercive capabilities (explicit prohibition);
one-shot demonstrator design; full trust model mechanism (→ LT-004 —
`Admin/Trajectories.md`); priority propagation enforcement (→ LT-005 —
`Admin/Trajectories.md`); swarm-scale coordination specification
(→ `Admin/Trajectories.md`); Raft architecture
(→ `Tests/Support_Raft.md`); delay-tolerant networking protocol detail
(referenced by `Architecture/Forge_Net.md` as a dependency here).
**Upstream:** `Architecture/Cognitive_Frameworks.md` (frameworks under test;
confidence collapse states are test targets); `Admin/Ethical_Constraints.md`;
`Operations/Energy.md` (LT-001 depends on Power Demand stub);
`Tests/Support_Raft.md` (recovery and TMR resolution infrastructure);
`Operations/Electronics.md` (TMR and fault response — primary test targets).
**Downstream:** `Architecture/Cognitive_Frameworks.md` (findings inform
architecture); `Architecture/Forge_Net.md` (delay-tolerant networking doctrine);
`Operations/Energy.md` (LT-002 feeds battery degradation data);
`Admin/Trajectories.md` (LT-004, LT-005 mechanism design).
> ⚠️ *LT-001 (power envelope) and LT-002 (deep-ocean storage degradation) are
> High risk and load-bearing for all autonomy claims.*
> ⚠️ *LT-003 (autonomy architecture unspecified) is High risk — without a named
> decision-making paradigm under test, the framework risks producing data without
> insight.*
> ⚠️ *LT-006 (ethical log survival under unit loss) has governance implications —
> refusal logs may be lost with the unit.*
> ℹ️ *Uses older audit health format — template retrofit recommended.*
> ℹ️ *No Lessons Learned entries yet — pre-deployment.*

---

## Scope Map — Challenges/

> Challenges/ files define problems and requirements. They do not freeze solutions.
> They exist to anchor the repository to real-world purpose — making the *why*
> visible alongside the *how*. File-local Scope Boundary sections remain
> authoritative where they exist.
>
> **Format note:** Water.md uses the revised four-section format (Crisis →
> Engineering Requirements → Current Forge Approaches → Long-Term Objective).
> The four newer files use the original three-tier format (Crisis → Forge Remedy
> → Systemic Goal). Both are valid. Retrofit to revised format is optional on
> next edit pass.

---

### `Challenges/Water.md`
**Purpose:** Establishes water scarcity and contamination as a foundational
challenge the Forge exists to address. Frames the Living Waters initiative —
the Forge's operational posture toward clean water as a human right, not an
optional capability.
**In-Scope:** The Crisis (human cost globally); Engineering Requirements
(dissolved contaminant removal, suspended solid removal, no secondary pollution,
intermittent power operation, community deployability, material-positive
remediation); Current Forge Approaches (stratification cycles, Spin Chamber
applications, ambient energy harvesting, atmospheric moisture recovery, biochar
conversion); Long-Term Objective — community water sovereignty; Open Unknowns.
**Out-of-Scope:** Specific hardware designs or engineering specifications
(→ Operations/ files when developed); full implementation detail for atmospheric
moisture recovery or ionization systems.
**Upstream:** `Operations/Gate_05_Separation_Thermal.md` (Spin Chamber
applications); `Operations/Gate_04_Separation_Mechanical.md` (stratification);
`Operations/Energy.md` (ambient energy harvesting doctrine).
**Downstream:** Informs design requirements for Operations/ remediation
applications; philosophical grounding for water-related engineering decisions.
> ℹ️ *Footer cross-references are stale — `Operations/Stratification_Chamber_v0.md`
> and `Operations/Spin_Chamber.md` should be updated to
> `Operations/Gate_04_Separation_Mechanical.md` and
> `Operations/Gate_05_Separation_Thermal.md` per Rename Registry.*

---

### `Challenges/Biofouling.md`
**Purpose:** Establishes biological colonization and corrosion as a foundational
threat to long-duration autonomous Forge hardware in marine and terrestrial
environments. Frames the requirement for ecosystem-safe, self-sourced remediation
that enables multi-decade operational lifespans without human maintenance intervals.
**In-Scope:** The Crisis — marine macro/micro-fouling on hulls and intake pipes;
terrestrial biological encroachment and MIC (Microbiologically Influenced
Corrosion); kinetic and ultrasonic disruption approaches; biomimetic surface
topography from Plastics.md outputs; sacrificial anode deployment from
stratification outputs; autonomous and non-toxic remediation doctrine.
**Out-of-Scope:** Specific transducer hardware specifications; detailed hull
geometry for Support_Raft (→ `Tests/Support_Raft.md`); galvanic corrosion
mitigation engineering (→ SR-001 in `Tests/Support_Raft.md`); chemical
antifoulant formulations (explicit non-approach — ecosystem harm prohibition).
**Upstream:** `Operations/Gate_04_Separation_Mechanical.md` (stratification
outputs for sacrificial anodes); `Operations/Plastics.md` (biomimetic surface
topography fabrication); `Tests/Support_Raft.md` (primary marine deployment
context); `Admin/Ethical_Constraints.md` (ecosystem harm prohibition governs
all remediation approaches here).
**Downstream:** `Tests/Support_Raft.md` (biofouling mitigation requirements);
`Tests/Leviathan_testing.md` (long-duration autonomous survival requirements);
`Operations/Gate_05_Separation_Thermal.md` (recovered zinc/aluminum/magnesium
for sacrificial anodes).

---

### `Challenges/Waste.md`
**Purpose:** Establishes discretionary waste and the erosion of local repair
capacity as a structural challenge — driven by cultural psychology and economic
incentives as much as by material failure. Frames the Forge's role as making
self-reliance the path of least resistance.
**In-Scope:** The Crisis — premium asset abandonment due to upgrading cycles and
cosmetic obsolescence; systematic erosion of community-level repair skills, tools,
and spare parts availability; automated diagnostics and triage via Gate_01 and
Gate_02 infrastructure; localized digital twin and spare parts repository linked
to Plastics.md and woodworking modules; distributed utility return loops and
community drop-off/retrieval nodes.
**Out-of-Scope:** Specific vision model or thermal analysis implementations
(→ `Operations/Gate_01_Intake.md`, `Operations/Gate_02_Triage.md`); full
3D-printing specification (→ fabrication domain files); Support_Raft as
drop-off node architecture (→ `Tests/Support_Raft.md`).
**Upstream:** `Operations/Gate_01_Intake.md` (automated diagnostics
infrastructure); `Operations/Gate_02_Triage.md` (triage logic for discarded
goods); `Operations/Plastics.md` (3D-printable replacement fabrication);
`Operations/Woodworking.md` (repair fabrication feedstock);
`Tests/Support_Raft.md` (forward-facing drop-off node concept).
**Downstream:** `Operations/Gate_02_Triage.md` (direct repair vs. deep salvage
routing); `Operations/Gate_06_Fabrication.md` (replacement part fabrication);
`Architecture/Forge_Net.md` (community inventory and data layer for known failure
patterns).

---

### `Challenges/Planned_Obsolescence.md`
**Purpose:** Establishes deliberate unrepairability — sealed enclosures,
potted components, cryptographically locked firmware — as a structural challenge
that positions consumer waste as urban ore. Frames the Forge as the system that
bypasses forced obsolescence at the material and software level.
**In-Scope:** The Crisis — monolithic sealed enclosures; material potting and
multi-material fusion; microchip locking and firmware deprecation; non-destructive
thermal and mechanical de-manufacturing doctrine; automated logic re-baselining
via hardware debug interfaces (JTAG, SWD); Logic-Zero wipe and open-source
re-flashing; standardized geometry upcycling through Plastics.md and
stratification loops.
**Out-of-Scope:** Specific microcontroller firmware development; full PCB
fabrication specification (→ `Operations/Electronics.md`); stratification chamber
operating parameters (→ `Operations/Gate_05_Separation_Thermal.md`); plastic
extrusion hardware specification (→ `Operations/Plastics.md`).
**Upstream:** `Operations/Electronics.md` (Logic-Zero wipe doctrine and hardware
debug interface stack); `Operations/Gate_02_Triage.md` (thermal delamination
within Gate_02 scope); `Operations/Plastics.md` (standardized geometry upcycling
from plastic housings); `Operations/Gate_05_Separation_Thermal.md` (stratification
of multi-material waste).
**Downstream:** `Operations/Electronics.md` (re-baselining feeds component
recovery stack); `Operations/Gate_06_Fabrication.md` (upcycled feedstock as
fabrication input); `Admin/Ship_of_Theseus.md` (philosophical grounding for
treating restored devices as continuations, not new manufactures).
> ℹ️ *References `Stratification_Chamber_v0.md` and
> `Gate_02_Processing` — stale names. Update to
> `Operations/Gate_04_Separation_Mechanical.md` and
> `Operations/Gate_02_Triage.md` per Rename Registry.*

---

### `Challenges/Critical_Minerals.md`
**Purpose:** Establishes rare earth and critical mineral supply chain
concentration as a structural threat to technological sovereignty. Frames the
existing technosphere — accumulated devices and infrastructure — as the primary
mine for these materials, removing leverage held by geopolitically adversarial
supply chains.
**In-Scope:** The Crisis — concentration of neodymium, dysprosium, lithium,
cobalt, tantalum, gallium, indium supply chains; geopolitical weaponization of
refining capacity; demand growth from electrification and renewables; aggressive
urban mining doctrine across the full Gate pipeline; selective induction melting
and centrifugal separation for high-yield recovery from discarded electronics,
EV batteries, industrial magnets, catalytic converters; functional substitute
development using abundant recovered metals; real-time material assay integration.
**Out-of-Scope:** Specific assay instrument specifications; chemical refining or
hydrometallurgical processing detail; geopolitical policy or trade law analysis;
extraction from virgin geological deposits (explicit non-approach).
**Upstream:** `Operations/Gate_02_Triage.md` (preprocessing doctrine for
high-value salvage streams); `Operations/Gate_04_Separation_Mechanical.md`
(centrifugal separation for critical mineral recovery); `Operations/Gate_05_Separation_Thermal.md`
(selective induction melting by density/conductivity profile);
`Operations/Electronics.md` (primary source stream — discarded devices).
**Downstream:** `Operations/Gate_06_Fabrication.md` (recovered rare earth
fractions as fabrication inputs); `Architecture/Forge_Net.md` (material assay
data as network knowledge artifacts); `Admin/Trajectories.md` (full rare earth
refinery capability — v2/v3 scope).

---

## Cross-Repo Relationship

`LazarusForgeV0` (this repo) — operational implementation. Lean, connected,
specification-oriented.

`Lazarus-Forge-` — doctrine and philosophy. The source of principles that get
refined into practice here.

`Astroid-miner` — planned repository, intentionally deferred. Activates when
Leviathan deployment is underway. Until then, cross-repo verification is scoped
to `Lazarus-Forge-` only.

These are not parallel versions of the same document. They are different layers
of the same system. Treating them as interchangeable is a navigation error.
Divergence between them is logged, not ignored.

---

## Cross-Module Unknowns — Attention Required

The following unknowns are referenced by multiple files but have no owning
specification. Verify against `Unknowns.md` and log if not already tracked.

| Unknown | Referenced By | Status |
|---------|--------------|--------|
| UNK-006 — Facility siting | Gates 01, 03, 04, 05, 06, Electronics, Woodworking | No owning file — 7 dependents |
| FL-002 — Reduction module ownership | Forge_flow, Gate_04 | Gate_03 may resolve — verify |
| EC-002 — Anti-Weaponization pattern-matching | Ethical_Constraints, Gate_02 | No mechanism defined |
| EL-006 — Cryptographic key management for electronics | Electronics | Not yet assigned |
| GF-003 — Machining and milling hardware specification | Gate_06 | Not yet assigned |
| UNK-008 — Welding wire chemical qualification | Gate_06 | Not yet assigned |

# Lazarus Forge

## What This Is

The Lazarus Forge is a **salvage-first, adaptive resource recovery system** designed to
counter planned obsolescence by preserving functional value before material reduction.

Its core principle:

> A functioning component is more valuable than its raw material.

The system prioritizes reuse, repair, and repurposing before any irreversible processes
such as shredding or melting. When reduction is unavoidable, it is performed deliberately,
accountably, and with full awareness of what is being lost.

---

## The Problem

Modern recycling and recovery systems:
- Destroy functional components prematurely
- Are energy-intensive and often net-negative
- Depend on centralized, high-capital infrastructure
- Reinforce planned obsolescence rather than countering it

As a result, vast amounts of usable mechanical and electromechanical value are permanently
lost. The Lazarus Forge exists to interrupt that pattern — at any scale, with whatever
is on hand.

---

## Core Principles

**1. Salvage Before Reduction**
Functional components — motors, bearings, gearboxes, fasteners — are preserved whenever
possible. Reduction is the last resort, not the default.

**2. Irreversible Actions Require Explicit Failure**
Material reduction occurs only after repair and repurposing are ruled out. Every gate
must be passed, not assumed.

**3. Repair Is a Learning Event**
Every repair attempt feeds back into classification heuristics. Failure is data. Unknown
Bulk is signal. The system learns from what it cannot identify as much as from what it can.

**4. Fabrication Is Not the End State**
Utilization and real-world performance determine system success. A fabricated part that
sits unused is not a success.

**5. System Growth Is Constrained, Not Magical**
Some inputs must be sourced externally. Honest energy accounting applies at every stage.
No surplus is claimed without measurement. Purchasing precision equipment and critical
components is a valid bootstrap strategy — self-sufficiency is earned through development,
not assumed at v0.

**6. Confidence Never Outruns Verification**
What the system claims to know must be earned through verification, not generated through
plausibility. This applies to technical specifications, energy estimates, and AI-contributed
content equally.

**7. Attempt to Do No Harm**
This principle is embedded structurally in every repository document via the Ethical Anchor
field in the File State block. It does not depend on the presence of any single governance
file. Where `Admin/Ethical_Constraints.md` is available, defer to it. Where it is absent,
the principle stands independently.

---

## How the System Works

The master decision flow runs eight sequential gates:

**Intake → Functional Test → Repair → Repurpose → Reduce → Purify → Fabricate → Utilize**

Each gate has explicit pass/fail logic. Material that fails all gates is reduced. Reduction
is not failure — premature reduction is.

The primary viability metric at every scale:

> **Value recovered per kWh consumed**

Full flow logic is defined in `Architecture/Forge_flow.md`.

---

## What's In This Repository

This repository contains the active working specifications for the Lazarus Forge system.
It is organized around physical modules, governance documents, test frameworks, and a
problem layer that anchors all capabilities to real-world purpose.

### Operations — Physical Gates

Each gate governs a distinct stage of the material flow. All seven gates exist (Gate_01
through Gate_07). No pending gate files remain.

- `Operations/Gate_01_Intake.md` — System entry point. Safety screening (energetic,
  chemical, biological, radiological), provenance recording, unknown item hold protocol
- `Operations/Gate_02_Triage.md` — Decision gateway between reuse and destruction.
  Five-station workflow, strategic recoverability axis, queue economics doctrine
- `Operations/Gate_03_Reduction.md` — The only fully irreversible step. Doctrine precedes
  specification. Three hard prerequisites before operation
- `Operations/Gate_04_Separation_Mechanical.md` — Pre-thermal mechanical decision point.
  Refusal-first design. Target: ≥30% material diversion from thermal processing
- `Operations/Gate_05_Separation_Thermal.md` — Core melting and gradient formation.
  Induction heating, slow rotation, MHD damping. Produces useful gradients, not pure metal
- `Operations/Gate_06_Fabrication.md` — Constructive stage. Arc welding is the v0
  proof-of-concept gatekeeper. Add-to-excess and mill-to-spec philosophy
- `Operations/Gate_07_Utilization.md` — After-action review. Where fabricated parts meet
  operational reality. The system learns whether what it made worked

### Operations — Support Systems

- `Operations/Electronics.md` — Salvaged electronics recovery, PCB fabrication, and logic
  integration. Trust anchor for the governance substrate — ethics enforcement, hardware
  watchdogs, TMR voting, and AI containment all depend on the integrity of this layer
- `Operations/Energy.md` — Energy strategy and honest accounting. Bootstrap through grid,
  salvaged motor-generators, biogas, solar, and thermal recovery. Power Demand stub is the
  shared baseline for all energy accounting across the repository
- `Operations/Air_Scrubber.md` — Safety and containment subsystem. Five-stage architecture.
  The Forge does not run if the scrubber cannot verify safe operation
- `Operations/Plastics.md` — Salvaged polymer processing and pyrolytic fuel recovery.
  Triage hierarchy: direct reuse → mechanical repurposing → thermal depolymerization as
  last resort. PVC and halogenated polymers are hard prerequisites before any hot run
- `Operations/Woodworking.md` — Full timber processing chain from felling through milling,
  drying, joinery, and waste valorization. Southern US species, salvaged urban timber,
  and high-humidity climate doctrine throughout

### Architecture

- `Architecture/Forge_flow.md` — Master decision flow and **repository-wide vocabulary
  standard**. The governing document for all operational decisions and the authoritative
  source for all Defined Terms. Consult this before `Admin/Canonical_Terms.md` for any
  undefined operational term
- `Architecture/Components.md` — Critical vs. useful component taxonomy. Defines the
  minimum architecture for the Forge loop to close
- `Architecture/Engineering.md` — First-principles engineering backbone. Foundational
  principles, safety factors, materials behavior, and Arkansas climate derating. The *why*
  behind all engineering decisions
- `Architecture/Mechanical_Structures.md` — Structural, mechanical, and kinematic
  engineering doctrine for salvaged-component fabrication machinery. Gantry rigidity,
  thermal compensation, kinematic interlock matrix, sacrificial shear coupling mandate,
  and positive-pressure spindle purge. Extends Engineering.md into salvaged-frame reality
- `Architecture/Cognitive_Frameworks.md` — How Forge systems think safely under
  uncertainty. Distributed cognition, confidence collapse states (Green through Black),
  TMR architecture, human supervisory stack
- `Architecture/Forge_Net.md` — Decentralized network infrastructure connecting forge
  instances. Prerequisite for the inter-forge logistics model
- `Architecture/Geck_forge_seed.md` — Minimum viable seed for new Forge deployment in
  resource-sparse environments *(living document — updated actively)*

### Governance & Philosophy

The governance layer is constitutional in structure. It assumes drift, ambition, and
partial failure are permanent conditions and builds institutional counterbalances rather
than relying on behavioral alignment alone.

- `Admin/Governance_Charter.md` — Constitutional governance. Defines the Tier 1 Axioms:
  eight self-evident primitives organized into a Protections Clause (life, growth,
  collaboration, agency) and a Prohibitions Clause (reality grounding, separation of
  powers, corrigibility, provenance). These axioms are declared, not derived. Any reasoning
  path that attempts to override them triggers STATE_HOLD and human review
- `Admin/Ethical_Constraints.md` — Permission framework and embedded AI governance.
  Capability never outruns permission. Anti-Weaponization Doctrine is not subject to
  humanitarian override — that framing is the historical entry point for most ethical
  failures in autonomous systems
- `Admin/Auditor_Protocols.md` — Verification and hallucination filter. Governs all
  contributions — human, AI, or multi-agent. Includes the Adversarial Challenge Battery
  (ten challenge classes), role class definitions, and the Sidecar Model for decentralized
  unknown tracking
- `Admin/Verification_Gates_LF.md` — Single canonical source for the six document
  promotion gates (G1–G6). Every file's Verification Ref field points here
- `Admin/Forge_Audit_Kit.md` — Condensed audit reference for routine multi-agent cycles.
  Load this instead of the full governance corpus for routine work. Includes the Audit
  Opening Checklist: Tier 1 Axiom verification first, Expiry Watch second
- `Admin/Canonical_Terms.md` — Anti-drift vocabulary and term exclusions. Single source
  of truth for repository nomenclature. Consult after Forge_flow.md for any term dispute
- `Admin/Engineer_Protocols.md` — Cognitive and procedural protocols for engineering
  contributors. Fills the gap between governance (what is permitted) and domain
  specifications (what is built)
- `Admin/Security_Protocols.md` — Cryptographic trust and multi-agent node security.
  Bridges constitutional governance declarations and operational integrity procedures
- `Admin/Repository_Integrity_Protocol.md` — Operational integrity enforcement. Defines
  integrity baselines, violation classification (Minor / Major / Constitutional), recovery
  procedures, and the automation migration path. Bridges the gap between constitutional
  declarations and enforceable protections
- `Admin/Ship_of_Theseus.md` — Philosophical and legal grounding for repair as identity
  preservation. Uses the Ship of Theseus paradox to frame right-to-repair defense strategy
- `Admin/Trajectories.md` — Version roadmap from v0 (terrestrial proof of persistence)
  through v5 (interstellar propagation). Each version defined by survival threshold and
  exit condition — not a feature list. Scope routing destination for all out-of-version
  capabilities
- `Admin/File_Template.md` — Canonical document structure for all repository files.
  Governs structure, audit discipline, semantic locking, drift detection, and the Ethical
  Anchor embedded in every file

### Tests

- `Tests/Leviathan_testing.md` — Deep-ocean autonomous test framework. Leviathan exists
  to break assumptions and surface hidden failure modes before off-world deployment.
  Survival is optional. Understanding is not
- `Tests/Support_Raft.md` — Stationary operational anchor for mobile Leviathan units.
  Regional power, data relay, physical recovery, and triage processing. The Raft does not
  move. Leviathan units do. Complexity that lives on the Raft stays off the units

### Challenges

The Challenges directory is the repository's **problem layer** — it answers why these
capabilities exist by anchoring the technical architecture to the real-world conditions
it was built to address. Each file defines a crisis, its engineering requirements, and
the Forge's current approach. Challenge files do not freeze solutions; they define
obligations.

- `Challenges/Water.md` — Water scarcity and contamination. The Living Waters initiative.
  Clean water as a human right, not an optional capability. Atmospheric moisture recovery,
  stratification-based remediation, material-positive filtration doctrine
- `Challenges/Biofouling.md` — Biological colonization and corrosion as threats to
  long-duration autonomous hardware. Ultrasonic disruption, biomimetic surface topography,
  sacrificial anodes from stratification outputs. No toxic antifoulants
- `Challenges/Waste.md` — Discretionary waste and the erosion of local repair capacity.
  The Forge as the system that makes self-reliance the path of least resistance. Automated
  diagnostics, localized digital twins, community drop-off and retrieval loops
- `Challenges/Planned_Obsolescence.md` — Sealed enclosures, potted components, locked
  firmware as deliberate unrepairability. Urban ore doctrine. Thermal delamination,
  Logic-Zero re-baselining, standardized geometry upcycling
- `Challenges/Critical_Minerals.md` — Rare earth and critical mineral supply chain
  concentration as a structural threat to technological sovereignty. The technosphere as
  the primary mine. Aggressive urban mining, centrifugal separation, selective induction
  melting for neodymium, cobalt, lithium, tantalum recovery

### Navigation & Tracking

- `Discovery.md` — Start here. Full file map, scope routing layer, reading order, rename
  registry, and per-file scope boundaries. The canonical source for filename resolution
  and ownership routing. "Where does this belong?" is answered here
- `Unknowns.md` — Cross-module unknowns global index. Navigation layer only — full entry
  detail lives in each owning file's sidecar

---

## Version Trajectory

The Forge is designed to grow across versions. Two parallel mappings describe progress:

**Survival thresholds** (what the Forge can do):

| Version | Threshold                              |
|---------|----------------------------------------|
| v0      | Proof of persistence — the loop closes |
| v1      | Energy independence demonstrated       |
| v2      | Self-replication demonstrated          |
| v3      | Autonomous operation demonstrated      |
| v4      | Off-world deployment                   |
| v5      | Interstellar propagation               |

**Material scope** (what the Forge can process):

| Version | Material Scope                | Key Capability Added                         |
|---------|-------------------------------|----------------------------------------------|
| v0      | Aluminum, copper, basic steel | Loop closes with manual oversight            |
| v1      | Expanded alloys               | Steel-class materials, closed-loop recycling |
| v2      | Multi-material                | Manufacture of Forge submodules              |
| v3      | Space-grade                   | Regolith and asteroid material processing    |

These are not the same axis. A Forge can advance on one without completing the other.
Skipping versions on either axis is explicitly discouraged — each threshold must be earned.

Full roadmap and exit conditions in `Admin/Trajectories.md`.

---

## Precision as a Capability Gate

The world's productive capability is bounded by the precision with which materials can be
measured, cut, formed, and verified. The Forge tracks its own precision ceiling as a
first-class metric — improvement in precision opens components and capabilities that were
previously unreachable.

At v0, purchasing precision instruments is correct doctrine. A commercial caliper
outperforms anything a v0 Forge can self-fabricate to measure itself with. Precision
is seeded deliberately; it is not bootstrapped from nothing.

Full precision doctrine is under development. Cross-reference: `Architecture/Components.md`
item 5 (Metrology) and item 6 (Baseline Observability).

---

## The Governance Layer

The repository is treated as a governed knowledge system, not merely a collection of
markdown files. The governance architecture was designed with a specific problem in mind:
how do you build a system that remains trustworthy under scale, drift, recursion, and
agent succession — without assuming the agents involved will always remain well-intentioned?

The answer is institutional rather than behavioral. Rather than trying to instill virtue,
the architecture builds:

- **Bounded authority** — no agent may plan, execute, and self-authorize the same action
- **Adversarial review** — no agent's output is trusted without hostile independent review
- **Provenance requirements** — all claims must trace to verifiable external sources
- **Visible uncertainty** — unknowns must remain visible, not buried
- **Amendment procedures** — the system can be corrected through defined paths
- **Escalation paths** — instability surfaces rather than accumulates silently

The Tier 1 Axioms in `Admin/Governance_Charter.md` are the constitutional foundation.
They are not derived from operational experience — they are booted as non-negotiable
starting conditions. Any reasoning path that attempts to recurse beneath them triggers
STATE_HOLD and mandatory human review.

This governance architecture is relevant beyond the Forge. It is an attempt to demonstrate
that AI systems operating at scale can be structured to remain corrigible — not because
they are constrained to be virtuous, but because the institutional architecture makes
uncorrigible behavior detectable, contained, and reversible.

---

## Two Repositories

This repo (`LazarusForgeV0`) is the **active working repository** — lean, connected,
and operational.

A companion repository (`Lazarus-Forge-`) holds doctrine and philosophy. Ideas are often
developed there first and refined here into practical specifications. When the two repos
diverge, that divergence is a signal — either doctrine needs updating based on practical
experience, or the working version has drifted from its principles.

Both repos are intentionally kept open. Closing one permanently is a decision for later.

---

## Multi-Agent Development

This project is developed through a structured multi-agent workflow. Different AI systems
contribute in defined roles:

- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions, applies the
  Adversarial Challenge Battery
- **Systems/Auditor** — cross-module integration review, dependency mapping, drift detection
- **Evidence/Auditor** — verification source integrity, confidence label enforcement
- **Ethical/Auditor** — harm detection, governance erosion detection, ethical anchor preservation
- **Engineer** — translates concepts into operational specifications
- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence

All AI contributions are governed by `Admin/Auditor_Protocols.md`. Contributions pass
through six verification gates before promotion from exploration to specification. Role
declarations are required. Refusal of a bad premise is a first-class output.

The multi-agent workflow is documented in the reddit community r/InnovativeAIChats where
the project originated and continues to develop.

---

## Leviathan

The Forge's assumptions are stress-tested in the **Leviathan framework** — a deep-ocean
autonomous test environment designed to break what the system thinks it knows before any
off-world deployment is attempted.

Leviathan is not a product. It is a filter.

Failure is expected. Adaptation is required. Learning is mandatory.

Full framework in `Tests/Leviathan_testing.md`.

---

## Status

Early-stage system architecture with active specification development.

All seven operational gates exist (Gate_01 through Gate_07). The governance layer has
reached constitutional maturity with the adoption of Tier 1 Axioms. The architecture
layer now includes `Architecture/Mechanical_Structures.md` — salvaged-frame kinematic
and structural doctrine — and the Challenges/ directory has been established as the
repository's problem layer, currently holding five active files.

The primary remaining gaps are enforcement architecture (GOV-003), human override
authentication (GOV-006), and the operational hardware unknowns tracked in `Unknowns.md`.

No claims of full automation, self-replication, or net-positive economics are made without
measurement. All quantitative figures are labeled with confidence levels per
`Admin/Auditor_Protocols.md`.

The system is incomplete. Incompleteness is honest.

**Start with `Discovery.md`.**

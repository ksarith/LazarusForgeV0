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
file. Where `Ethical_Constraints.md` is available, defer to it. Where it is absent, the
principle stands independently.

---

## How the System Works

The master decision flow runs eight sequential gates:

**Intake → Functional Test → Repair → Repurpose → Reduce → Purify → Fabricate → Utilize**

Each gate has explicit pass/fail logic. Material that fails all gates is reduced. Reduction
is not failure — premature reduction is.

The primary viability metric at every scale:

> **Value recovered per kWh consumed**

Full flow logic is defined in `Lazarus_forge_v0_flow.md`.

---

## What's In This Repository

This repository contains the active working specifications for the Lazarus Forge system.
It is organized around physical modules, governance documents, and test frameworks.

**Physical Modules:**
- `Material_Separation_Gate_v0.md` — First physical decision point. Mechanical separation
  before any thermal processing. Refusal-first design
- `Spin_Chamber_v0.md` — Core melting and gradient formation module. Slow rotation,
  induction heating, MHD damping
- `Air_Scrubber_v0.md` — Safety and containment subsystem. The Forge does not run if the
  scrubber cannot verify safe operation
- `Support_Raft_v0.md` — Operational anchor for Leviathan swarm deployments. SWATH hull,
  sacrificial shell system, regional power and data relay

**Governance & Philosophy:**
- `LF_File_Template.md` — Canonical document structure for all repository files. Governs
  structure, audit discipline, semantic locking, drift detection, and the Ethical Anchor
  embedded in every file. Apply to all new files; retrofit existing files during audit cycles
- `Auditor_Protocols.md` — Verification and hallucination filter. Governs all contributions
  — human, AI, or multi-agent
- `Ethical_Constraints.md` — Permission framework. Capability never outruns permission
- `Ship_of_Theseus_Right_to_Repair.md` — Philosophical and legal grounding for repair as
  identity preservation

**System Architecture:**
- `Component_Triage_System.md` — Decision gateway between reuse and destruction
- `Components.md` — Critical vs. useful component taxonomy. Defines the minimum
  architecture required for the Forge loop to close, including Baseline Observability
  as a distinct Critical component separate from Metrology
- `energy_v0.md` — Energy strategy and honest accounting
- `geck_forge_seed.md` — Minimum viable seed for new Forge deployment in resource-sparse
  environments. Includes procurement doctrine and introductory precision threshold concept

**Trajectory & Testing:**
- `Trajectories_LF.md` — Version roadmap and exit conditions
- `leviathan_testing.md` — Deep-ocean autonomous test framework. Exists to break
  assumptions before off-world deployment
- `Unknowns_LF.md` — Cross-module unknown tracking. Global UNK-XXX index

**Navigation:**
- `Discovery.md` — Start here. Full file map, reading order, and per-file summaries

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

Full roadmap and exit conditions in `Trajectories_LF.md`.

---

## Precision as a Capability Gate

The world's productive capability is bounded by the precision with which materials can be
measured, cut, formed, and verified. The Forge tracks its own precision ceiling as a
first-class metric — improvement in precision opens components and capabilities that were
previously unreachable.

At v0, purchasing precision instruments is correct doctrine. A commercial caliper
outperforms anything a v0 Forge can self-fabricate to measure itself with. Precision
is seeded deliberately; it is not bootstrapped from nothing.

Full precision doctrine is under development. Cross-reference: `Components.md` item 5
(Metrology), item 6 (Baseline Observability), and CO-002.

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

- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence
- **Engineer** — translates concepts into operational specifications
- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions
- **Connective Tissue** — links community discussion to repository evolution

All AI contributions are governed by `Auditor_Protocols.md`. Contributions pass through
verification gates before promotion from exploration to specification. Role declarations
are required. Refusal of a bad premise is a first-class output.

The multi-agent workflow is documented in the reddit community r/InnovativeAIChats where
the project originated and continues to develop.

---

## Leviathan

The Forge's assumptions are stress-tested in the **Leviathan framework** — a deep-ocean
autonomous test environment designed to break what the system thinks it knows before any
off-world deployment is attempted.

Leviathan is not a product. It is a filter.

Failure is expected. Adaptation is required. Learning is mandatory.

Full framework in `leviathan_testing.md`.

---

## Status

Early-stage system architecture with active specification development.

No claims of full automation, self-replication, or net-positive economics are made without
measurement. All quantitative figures are labeled with confidence levels per
`Auditor_Protocols.md`.

The system is incomplete. Incompleteness is honest.

**Start with `Discovery.md`.**

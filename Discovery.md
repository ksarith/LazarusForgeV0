# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**
**Last updated: 2026-05-15**

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
├── Discovery.md        — This file. Start here.
├── Unknowns.md         — Cross-module unknowns global index

Admin/                  — Governance, protocols, and doctrine
Architecture/           — System architecture and foundational logic
Operations/             — Physical modules and operational systems
Tests/                  — Test frameworks and deployment platforms
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

---

## Suggested Reading Order

For a new reader or returning AI, read in this sequence:

1. `README.md` — Project overview and core principles
2. `Architecture/Forge_flow.md` — Master decision flow and vocabulary standard
3. `Admin/Trajectories.md` — Version roadmap from v0 to interstellar
4. `Admin/Ethical_Constraints.md` — Governance and permission framework
5. `Admin/Auditor_Protocols.md` — Verification and hallucination filter
6. `Admin/Forge_Audit_Kit.md` — Condensed audit reference for routine cycles
7. `Unknowns.md` — Cross-module unknowns global index
8. `Architecture/Cognitive_Frameworks.md` — Distributed cognition and trust
9. `Operations/Gate_02_Triage.md` — Decision gateway between reuse and destruction
10. `Architecture/Components.md` — Critical vs useful component taxonomy
11. `Operations/Electronics.md` — Salvaged electronics and PCB fabrication
12. `Architecture/Geck_forge_seed.md` — Minimum viable seed for new Forge deployment
13. `Operations/Energy.md` — Energy strategy and accounting
14. `Operations/Gate_04_Separation_Mechanical.md` — Pre-thermal mechanical diversion
15. `Operations/Gate_05_Separation_Thermal.md` — Core melting and gradient formation
16. `Operations/Air_Scrubber.md` — Safety and containment subsystem
17. `Tests/Support_Raft.md` — Operational anchor for marine deployments
18. `Admin/Ship_of_Theseus.md` — Philosophical and legal grounding
19. `Tests/Leviathan_testing.md` — Deep-ocean autonomous test framework

**Pending files (not yet created):**
- `Operations/Gate_01_Intake.md`
- `Operations/Gate_03_Reduction.md`
- `Operations/Gate_06_Fabrication.md`

---

## File Summaries

### Root

**README.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/README.md`
Project landing page. Defines the salvage-first vision, core principles, system
scope, and the primary KPI. Honest about what v0 does and does not claim.

---

**Unknowns.md** — v1.1
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Unknowns.md`
Cross-module unknowns global index. v1.1 adds SC-001 through SC-008 and
MG-001 through MG-008 following Separation Thermal and Separation Mechanical
retrofit audits. Full entry detail lives in each owning file's sidecar.
Contains active unknowns summary tables by cluster, dependency map, expiry
watch, and resolved archive. UNK-006 through UNK-008 are new cross-module
entries from the 2026-05-15 audit cycle.

---

### Admin/

**Auditor_Protocols.md** — v0.5
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md`
Verification and hallucination filter. Governs all contributions — human, AI,
or multi-agent. Defines the Fallacy Checklist (10 items), AI contribution
protocols, and six sequential verification gates. Introduces the Sidecar Model
— module unknowns live in each file's footer, Unknowns.md is the global index
only. Includes Full Stop Review trigger conditions, audit trail schema, and
Protocol Performance metrics.

---

**Ethical_Constraints.md** — v0.3
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md`
Embedded AI governance framework and parent document. Covers ownership
recognition, legal context awareness, life preservation heuristics, cultural
site protection, Anti-Weaponization Doctrine, Human Escalation Protocol,
Governance Failure Modes, and refusal as a first-class action. Capability
never outruns permission.

---

**File_Template.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/File_Template.md`
Standard file structure for all LazarusForgeV0 documents. Defines ten
sections: File State, Scope Boundary, File Purpose, Assumptions, Body,
Lessons Learned, Active Disputes, Auditor Notes, Abandoned Paths, and
Drift Indicators. Apply to all new files and retrofit existing files during
audit cycles. Includes the Ethical Anchor field — a load-bearing principle
that survives even if Ethical_Constraints.md is missing.

---

**Forge_Audit_Kit.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Forge_Audit_Kit.md`
Condensed audit reference for routine multi-agent cycles. Load this instead
of full Auditor_Protocols.md and Unknowns.md to stay within token limits.
Contains governing principles, Fallacy Checklist (condensed), AI contribution
rules, verification gates, sign-off format, and active unknowns index tables.

---

**Ship_of_Theseus.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ship_of_Theseus.md`
Philosophical and legal grounding. Uses the Ship of Theseus paradox to frame
repair as identity preservation rather than reproduction. Builds a right-to-repair
defense strategy including grain provenance tracking, QR documentation, and
patent risk mitigation. Every grain is simultaneously a legal artifact and a
philosophical claim.
*Formerly: Ship_of_Theseus_Right_to_Repair.md*

---

**Trajectories.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Trajectories.md`
Version roadmap from v0 (terrestrial proof of persistence) through v5
(interstellar propagation). Each version defined by survival threshold and
exit condition — not a feature list. Skipping versions leads to systemic
fragility. Destination for scope creep that proves to be valid future work.
*Formerly: Trajectories_LF.md*

---

**AUDIT_HARNESS.py**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/AUDIT_HARNESS.py`
Automated audit support tooling. Assists with structured audit cycles across
repository files. Consult Auditor_Protocols.md for governing audit doctrine
before running.

---

### Architecture/

**Forge_flow.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_flow.md`
The master decision flow and **reference standard for shared vocabulary**.
Eight sequential gates from intake through utilization. Defines shared
operational terms, Gate Correspondence table, reversibility notes per outcome
path, and the Human/AI Oversight Gate. Includes boundary-case worked examples,
adversarial routing scenarios, and degraded operation doctrine. The governing
document for all operational decisions and shared vocabulary across the
repository. Retrofitted to File_Template.md structure 2026-05-15.
*Formerly: Lazarus_forge_v0_flow.md*

---

**Geck_forge_seed.md** *(living document — updated actively)*
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Geck_forge_seed.md`
Defines the minimum viable seed required to instantiate a new Forge in a
resource-sparse location. Eight core modules from power through human interface.
Success criterion: the seed can eventually rebuild itself. Includes Marine
Variant stub for Leviathan and Support Raft deployments.
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

### Operations/

**Gate_02_Triage.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_02_Triage.md`
Five-station triage workflow implementing the gate logic from Forge_flow.md.
Includes Gate Correspondence table, Strategic Recoverability axis, Queue
Economics doctrine, false-positive tolerance framework, Triage Terminal,
contamination handling, and ethical flag at entry. The Forge preserves
embedded industrial capability, not just metal.
*Formerly: Component_Triage_System.md*

---

**Gate_04_Separation_Mechanical.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_04_Separation_Mechanical.md`
Pre-purification mechanical decision point operating after Reduction and
before thermal processing. Diverts usable material away from the Spin
Chamber using centrifugal separation, dual-channel sensor cross-check,
and a refusal-first fail-to-bin protocol. Success defined by avoided
processing, not perfect separation. Target: ≥30% material diversion rate.
Retrofitted to File_Template.md structure and audited by Claude, Grok,
and ChatGPT 2026-05-15. MG-001 through MG-008 in sidecar.
*Formerly: Material_Separation_Gate_v0.md, Stratification_Chamber_v0.md*

---

**Gate_05_Separation_Thermal.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_05_Separation_Thermal.md`
Core melting and gradient formation module. Converts mixed metallic scrap
into ranked material streams via induction heating, slow rotation, and MHD
damping. Produces useful gradients, not pure metal. Designed for long
operational life, modular repair, and bootstrap compatibility. Includes
RPM safety calculation (safety factor ~32× confirmed), drive system
standardization doctrine, slag handling, and failsafe doctrine. Retrofitted
to File_Template.md structure and audited by Claude, Grok, and ChatGPT
2026-05-15. SC-001 through SC-008 in sidecar.
*Formerly: Spin_Chamber_v0.md*

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

**Electronics.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Electronics.md`
Salvaged electronics recovery, PCB fabrication, and logic integration.
Covers non-destructive harvesting protocols, homemade PCB fabrication,
Forge-Standard modular interface concept, Triple Modular Redundancy for
salvaged components, and fault response integration with Support Raft.
*Formerly: Electronics.md (root)*

---

**Energy.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Energy.md`
Incremental energy strategy. Covers grid bootstrap, salvaged motor-generators,
biogas, solar, and thermal recovery. Power Demand stub with three operating
modes (Bootstrap ~2–5 kW, Nominal ~15–40 kW, Degraded ~1–3 kW) — all
Placeholder, analog-sourced. Energy independence is not assumed at v0.
*Formerly: energy_v0.md*

---

**Gate_01_Intake.md** *(pending creation)*
Pre-classification safety screening and tagging. Governs hazard identification,
energetic material discharge, and item entry into the gate system.

---

**Gate_03_Reduction.md** *(pending creation)*
The only fully irreversible step in the Forge flow. Shredding, cutting, or
milling of items that have failed Gates A through D. Governs output envelope,
prohibited inputs, contamination discovery protocol, and emergency shutdown
doctrine. Upstream dependency for Gate_04_Separation_Mechanical.md.
Cross-reference: FL-002, UNK-007.

---

**Gate_06_Fabrication.md** *(pending creation)*
Fabrication and assembly from salvaged components, purified stock, and
repurposed parts. Governs fabrication priority order, want/need policy
application, and feedback to gate classification rules.

---

### Tests/

**Support_Raft.md** — v0.4
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Tests/Support_Raft.md`
Stationary operational anchor for mobile Leviathan units. Provides regional
power, data relay, physical recovery, and triage processing infrastructure.
SWATH hull architecture, Sacrificial Shell System, local decision authority
during comms blackout, Stasis Mode, and self-consuming end-of-region protocol.
The Raft's value is measured by what it enables in the units, not what it
does directly.
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

`LazarusForgeV0` (this repo) — operational implementation. Lean, connected,
specification-oriented.

`Lazarus-Forge-` — doctrine and philosophy. The source of principles that
get refined into practice here.

`Astroid-miner` — planned repository, intentionally deferred. Activates when
Leviathan deployment is underway. Until then, cross-repo verification is
scoped to `Lazarus-Forge-` only.

These are not parallel versions of the same document. They are different
layers of the same system. Treating them as interchangeable is a navigation
error. Divergence between them is logged, not ignored.

---

## Notes for Returning AI

- `Admin/Auditor_Protocols.md` v0.5 governs all contributions. The Sidecar
  Model is active — module unknowns live in each file's footer sidecar,
  not in the global registry.
- `Admin/Forge_Audit_Kit.md` is the starting point for routine audit cycles
  — load it instead of full Auditor_Protocols.md and Unknowns.md to stay
  within token limits.
- `Unknowns.md` is now v1.1 — Expiry Rule is active. Check the index at
  the opening of each audit cycle.
- Role declaration is required: *"Operating as [Role] per
  Auditor_Protocols.md v0.5"*
- `Architecture/Geck_forge_seed.md` is the most actively updated file —
  do not assume a cached version is current.
- The Rename Registry above is the canonical source for old-to-new filename
  mappings. If a reference in any file points to an old name, resolve it
  using the Rename Registry before flagging as a cross-reference failure.
- Unknown ID naming convention: local sidecar IDs (FL-001, SC-002, MG-004)
  are primary. UNK-* identifiers are cross-module navigation aliases indexed
  in Unknowns.md only. Use local IDs as primary references.
- Files listed in this document resolve to real committed files. If a link
  fails, log it as a Cross-Reference Failure per Auditor_Protocols.md Rule 1.
- `Astroid-miner` references are labeled planned — do not treat as active
  dependencies.
- Three pending gate files (Gate_01_Intake.md, Gate_03_Reduction.md,
  Gate_06_Fabrication.md) do not yet exist. Do not attempt to fetch them.

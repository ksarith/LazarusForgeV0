# Discovery.md — LazarusForgeV0
**Navigation layer for the active working repository.**
**Last updated: 2026-05-27**

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
    ├── Forge_Net.md    — Decentralized network prerequisite for logistics
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
10. `Unknowns.md` — Cross-module unknowns global index
11. `Architecture/Cognitive_Frameworks.md` — Distributed cognition and trust
12. `Architecture/Forge_Net.md` — Decentralized network and logistics prerequisite
13. `Operations/Gate_01_Intake.md` — System entry point, safety screening, identification
14. `Operations/Gate_02_Triage.md` — Decision gateway between reuse and destruction
15. `Operations/Gate_03_Reduction.md` — Only fully irreversible step; doctrine before specification
16. `Operations/Plastics.md` — Salvaged polymer processing and pyrolytic fuel recovery
17. `Architecture/Components.md` — Critical vs useful component taxonomy
18. `Operations/Electronics.md` — Salvaged electronics and PCB fabrication
19. `Architecture/Geck_forge_seed.md` — Minimum viable seed for new Forge deployment
20. `Operations/Energy.md` — Energy strategy and accounting
21. `Operations/Gate_04_Separation_Mechanical.md` — Pre-thermal mechanical diversion
22. `Operations/Gate_05_Separation_Thermal.md` — Core melting and gradient formation
23. `Operations/Gate_06_Fabrication.md` — Constructive stage; arc welding gatekeeper; precision ceiling
24. `Operations/Air_Scrubber.md` — Safety and containment subsystem
25. `Operations/Gate_07_Utilization.md` — After action review; performance logging; fabrication feedback loop
26. `Tests/Support_Raft.md` — Operational anchor for marine deployments
27. `Admin/Ship_of_Theseus.md` — Philosophical and legal grounding
28. `Admin/Canonical_Terms.md` — Standard repository nomenclature and anti-drift vocabulary guardrails
29. `Tests/Leviathan_testing.md` — Deep-ocean autonomous test framework

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
GOV-002 and GOV-003 moved to In Progress following Governance_Charter.md
constitutional adoption and Repository_Integrity_Protocol.md creation.
AP-007 moved to In Progress. Expiry Watch updated — Tier 1 Axiom verification
added as mandatory first step before Expiry Watch. RIP-001 (prior-state
archival) flagged Critical. Contains active unknowns summary tables by cluster,
dependency map, expiry watch, and resolved archive.

---

### Admin/

**Governance_Charter.md** — v0.4
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
doctrine with human ratification requirement for axiom amendments, and escalation
calibration including Constitutional severity tier. GOV-001 through GOV-007 in
sidecar. Updated 2026-05-23.

---

**Auditor_Protocols.md** — v0.7
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Auditor_Protocols.md`
Canonical verification doctrine. Tier 2 governance authority. Governs all
contributions — human, AI, or multi-agent. v0.7 merges v0.6 depth with
prior draft's role class structure and 10-phase audit sequence. Defines four
auditor role classes (Skeptic, Systems, Evidence, Ethical), the Fallacy
Checklist (10 items with substantive notes requirement), AI contribution
protocols (7 rules), the Sidecar Model for decentralized unknown tracking,
six sequential verification gates, and the full Adversarial Challenge Battery
(10 challenge classes). Includes Full Stop Review triggers, audit trail schema,
Protocol Performance metrics, Abandoned Paths, and Drift Indicators. Fitted
to File_Template.md structure. AP-001 through AP-007 in sidecar.

---

**Ethical_Constraints.md** — v0.3
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Ethical_Constraints.md`
Embedded AI governance framework. Co-occupies Tier 1 with Governance_Charter.md.
Covers ownership recognition, legal context awareness, life preservation
heuristics, cultural site protection, Anti-Weaponization Doctrine, Human
Escalation Protocol, Governance Failure Modes, and refusal as a first-class
action. The Anti-Weaponization Doctrine is not subject to humanitarian override
— that framing is the historical entry point for most ethical failures in
autonomous systems. Capability never outruns permission.

---

**Repository_Integrity_Protocol.md** — v0.1
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Repository_Integrity_Protocol.md`
Operational integrity enforcement procedures. Bridges the gap between
Governance_Charter.md constitutional declarations (Declared/Detectable state)
and fully Enforceable integrity protections. Defines integrity baselines for
eight protected elements (Tier 1 Axiom text, Resolution Logs, Frozen Sections,
Canonical Cross-References, Audit Lineage, Ethical Anchor Field, Sidecar
Entries, Multi-Agent Contribution Continuity), a three-tier violation
classification ladder (Minor / Major / Constitutional), recovery procedures
for both "prior state available" and "prior state unavailable" scenarios, and
a three-phase automation migration path toward full cryptographic enforcement.
Honest v0 acknowledgment: primary integrity mechanism is currently human
discipline. GitHub releases identified as the v0 prior-state archival solution.
RIP-001 through RIP-005 in sidecar. Created 2026-05-23.

---

**Security_Protocols.md** — v0.1 Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Security_Protocols.md`
Cryptographic trust and multi-agent node security. Defines multi-signature
human override verification requirements (GOV-006 resolution path), Phase 3
automated commit signing and frozen-section hash verification (RIP-005
resolution path), and zero-trust firmware baseline for salvaged logic units
(EL-006 cross-reference). Requires dual-token or multi-party hardware
confirmation for any Tier 1 Constitutional Axiom override — no single-operator
bypass permitted. Override assertions are transactional and ephemeral; they do
not persist across agent sessions. SEC-001 (quorum recovery under terminal
network partition) is Blocking. Body Stability Volatile — key revocation
doctrine, Relationship section, and standard Drift Indicators require addition
before next audit cycle.
*Resolves [PLANNED] designation from Governance_Charter.md and
Repository_Integrity_Protocol.md.*

---

**Forge_Audit_Kit.md** — v0.8
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Forge_Audit_Kit.md`
Condensed audit reference for routine multi-agent cycles. Tier 3 governance
authority — derived from Auditor_Protocols.md v0.7. Load this instead of
the full governance corpus to stay within token limits. v0.8 adds the Audit
Opening Checklist: (1) Tier 1 Axiom text verification in Governance_Charter.md
— Constitutional violations trigger STATE_HOLD immediately; (2) Expiry Watch
review. Also contains Verification Maturity Model (five states from Exploration
to Hardened Doctrine), institutional Truth Provenance Labels (Internally
Derived through Operationally Hardened), Adversarial Priority Weighting,
Anti-Theater Doctrine, Confidence Decay and Revalidation guidance, expanded
sign-off format, condensed Fallacy Checklist, AI contribution rules, verification
gates, active unknowns index (GOV, AP, RIP clusters added), and dependency map.
FAK-001 through FAK-003 and RIP-001 through RIP-005 in unknowns index.

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

**Canonical_Terms.md** — v0.1 Draft
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Admin/Canonical_Terms.md`
Standard repository nomenclature and anti-drift vocabulary guardrails.
Defines authoritative mappings for architectural terms, operational gate
names, marine subsystem terminology, and governance tier labels. Includes
explicit term exclusions to prevent semantic creep across multi-agent cycles
— "Recycling" is banned in favor of "Value Preservation" or "Material
Recovery" depending on context; "Autonomous Decision-Making" requires bounding
clauses. CT-001 (legacy script name mapping against AUDIT_HARNESS.py) and
CT-002 (Component Library schema standard, Blocking at Gate 2 promotion) in
sidecar. Body Stability Volatile — Gate_04/Gate_05 terminology requires
correction, Tier 4 definition requires alignment with Governance_Charter.md,
Lessons Learned table format and standard Drift Indicators require retrofit
before next audit cycle.
*Resolves [PLANNED] designation as Canonical_Terms_LF.md in
Governance_Charter.md, Forge_Audit_Kit.md, and Auditor_Protocols.md.*

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
before running. Phase 1 integrity checks (Ethical Anchor string match, File
State field presence, cross-reference resolution, FROZEN marker validation)
are the next implementation target per RIP-002.

---

### Architecture/

**Forge_Net.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Architecture/Forge_Net.md`
Decentralized data and physical network infrastructure connecting forge
instances into a resilient, self-improving ecology. Prerequisite for the
logistics model. Defines local-primary cache doctrine, Wikipedia-style shared
knowledge base, cognitive save states, cluster formation and governance
emergence doctrine, positive reinforcement mechanisms, network security threat
model, and data privacy classification tiers. FN-001 and FN-005 are hard
prerequisites for first forge-to-forge connection. Exploration/Volatile —
governance cannot be specified before first clusters form.

---

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

**Gate_01_Intake.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_01_Intake.md`
System entry point for all items entering the Lazarus Forge.
Governs safety screening (energetic, chemical, biological,
radiological), physical document handling and scanning,
reference database lookup, parts list generation, fastener
and small component recovery, item tagging and provenance
recording, and unknown item hold-and-inspect protocol.
GI-002 (energetic discharge) and GI-003 (augmented detection)
are hard prerequisites for first operational run. At v0,
human judgment primary — automation is a future capability.

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
The only fully irreversible step in the Lazarus Forge flow.
Receives items that have failed all recovery gates and reduces
them to feedstock through shredding, cutting, or milling.
Doctrine precedes specification — what Reduction must not do
is clearer than what it should do at v0. Three hard prerequisites:
Air Scrubber operational, human operator present, no energetic
materials remaining. GR-002 (method selection) is the keystone
that unblocks GR-001, GR-004, and indirectly GR-005. Highest
Risk in the repository — irreversibility is the defining
characteristic.

---

**Plastics.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Plastics.md`
Salvaged polymer processing and pyrolytic fuel recovery. Defines the triage
hierarchy for plastics: direct reuse → mechanical repurposing (filament/RepRap
stock) → thermal depolymerization for mixed or degraded bulk. Pyrolysis
framework covers three stages: oxygen-excluded batch reactor (350°C–450°C),
multi-stage condensation array producing synthetic crude oil, and non-condensable
syngas routing. PL-001 (halogenated polymer contamination — HCl/dioxin release
from PVC) is Critical and Blocking before any hot operational run. PL-002
(reactor over-pressurization) is Major and Blocking. Air Scrubber operation
is a non-negotiable prerequisite. Exploration/Volatile — integration hooks,
Assumptions table format, and Lessons Learned format require retrofit to
File_Template.md standard before next audit cycle.
*New file — 2026-05-26*

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

**Gate_06_Fabrication.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_06_Fabrication.md`
Constructive stage of the Lazarus Forge. Arc welding is the v0 proof-of-concept
gatekeeper. Add-to-excess and mill-to-spec is the primary dimensional control
philosophy. Owns precision ceiling doctrine. Dynamic and adaptive — method set
grows through formal qualification framework. PPE is a non-negotiable prerequisite.
GF-005 resolved — Gate_07_Utilization.md now exists.

---

**Gate_07_Utilization.md**
`https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Operations/Gate_07_Utilization.md`
After action review stage of the Lazarus Forge. Where fabricated parts and
recovered components meet operational reality — the system learns whether what
it made worked, how long it lasted, how it failed, and what that means for the
next fabrication cycle. Defines performance logging minimum content, failure
mode capture and classification, four feedback paths (Gate_06_Fabrication,
Forge_Net, Forge_flow classification rules, Components.md), and retirement
handoff doctrine to Gate_02_Triage. A part in service without a utilization
record is an opportunity lost. GU-001 through GU-004 in sidecar. Audited by
Claude (Retrofit/Auditor) 2026-05-19 and ChatGPT (Skeptic/Auditor) 2026-05-20.

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
Trust-anchor document for the forge's governance substrate — ethics
enforcement, hardware watchdogs, TMR voting, sensor truth, and AI
containment all depend on the integrity of the systems this file governs.
Covers non-destructive harvesting protocols and firmware trust doctrine
(Logic-Zero wipe required before any salvaged programmable device enters
forge systems), homemade PCB fabrication, Forge-Standard modular interface,
TMR hardware implementation with architectural diversity requirement,
hardware watchdog doctrine (discrete hardware, no programmable firmware),
MAC vs TMR distinction, dual-use awareness, and fault response integration
with Support Raft. EL-001 through EL-008 in sidecar. Retrofitted to
File_Template.md structure — multi-agent audit 2026-05-09, actioned 2026-05-19.
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

- **Start every audit cycle with the Audit Opening Checklist** in
  `Admin/Forge_Audit_Kit.md`: (1) verify Tier 1 Axiom text in
  `Admin/Governance_Charter.md` matches prior committed version —
  any unratified change is a Constitutional violation requiring STATE_HOLD;
  (2) check `Unknowns.md` Expiry Watch for entries approaching two-cycle
  threshold.
- `Admin/Auditor_Protocols.md` **v0.7** governs all contributions. The
  Sidecar Model is active — module unknowns live in each file's footer
  sidecar, not in the global registry. Four auditor role classes: Skeptic,
  Systems, Evidence, Ethical.
- `Admin/Forge_Audit_Kit.md` **v0.8** is the starting point for routine
  audit cycles — load it instead of full Auditor_Protocols.md and
  Unknowns.md to stay within token limits.
- `Unknowns.md` is now **v1.8** — Expiry Watch active. FL-001 and several
  EC entries approaching two-cycle threshold. RIP-001 (prior-state archival)
  flagged Critical. GOV-003 and GOV-005 are active Critical watches.
- Role declaration is required: *"Operating as [Role] per
  Auditor_Protocols.md v0.7"*
- `Admin/Governance_Charter.md` **v0.4** is the constitutional authority.
  Tier 1 Axioms (P-1 through P-4, Q-1 through Q-4) are non-negotiable
  primitives. Any reasoning path attempting to override them triggers
  STATE_HOLD.
- `Admin/Repository_Integrity_Protocol.md` **v0.1** defines what constitutes
  an integrity violation, how to classify it, and how to recover. Read this
  before modifying any governance-bearing document.
- `Architecture/Geck_forge_seed.md` is the most actively updated file —
  do not assume a cached version is current.
- The Rename Registry above is the canonical source for old-to-new filename
  mappings. If a reference in any file points to an old name, resolve it
  using the Rename Registry before flagging as a cross-reference failure.
  All prior references to `Canonical_Terms_LF.md` are resolved via the
  Rename Registry entry added 2026-05-26.
- Unknown ID naming convention: local sidecar IDs (FL-001, SC-002, MG-004)
  are primary. UNK-* identifiers are cross-module navigation aliases indexed
  in Unknowns.md only. Use local IDs as primary references.
- Governance tier hierarchy: Tier 1 (Governance_Charter.md,
  Ethical_Constraints.md) → Tier 2 (Auditor_Protocols.md) → Tier 3
  (Forge_Audit_Kit.md) → Tier 4 (dynamic procedures) → Tier 5 (domain specs).
  Lower tiers may extend but may not redefine higher tiers.
- Files listed in this document resolve to real committed files. If a link
  fails, log it as a Cross-Reference Failure per Auditor_Protocols.md Rule 1.
- `Astroid-miner` references are labeled planned — do not treat as active
  dependencies.
- All gate files now exist (Gate_01 through Gate_07). No pending gate files
  remain.
- `Admin/Security_Protocols.md` and `Admin/Canonical_Terms.md` now exist —
  see Admin/ summaries above. One planned Admin file not yet created:
  `Admin/Governance_Migration_Protocol.md` (GOV-001 resolution path).
  Do not treat as an active dependency.

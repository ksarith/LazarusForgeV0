# Cognitive_Frameworks.md — Distributed Cognition & Trust Architectures

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-09 (ChatGPT — Synthesizer)
- Open unknowns: 3 (Medium-High)
- Sidecar: [#auditor-notes--unknowns]

---

## Scope Boundary

**This file DOES define:** Cognitive reliability architectures, distributed trust models, redundancy and arbitration frameworks, AI consensus structures, hardware/software supervisory hierarchies, split-brain handling doctrine, confidence collapse states, human override positioning, return-to-base and stasis logic.

**This file DOES NOT define:** PCB fabrication, specific MCU wiring, mechanical actuator details, ethical policy itself, individual Leviathan mission logic, networking implementation details, cryptographic protocol specifics, or full autonomous governance law.

---

## File Purpose

This file defines how Forge systems think safely under uncertainty.

The Forge assumes degraded environments, imperfect hardware, incomplete information, damaged sensors, adversarial conditions, and partial system corruption as **normal operating conditions** rather than edge cases. Cognitive Frameworks exist to prevent isolated faults, hallucinations, firmware corruption, or confidence collapse from turning local errors into catastrophic actions.

The goal is not perfect intelligence. The goal is **survivable cognition**.

---

## I. Core Doctrine

**Intelligence Is Treated as a Hazard Source**

A sufficiently autonomous system can generate incorrect conclusions, fabricated certainty, unsafe optimization paths, recursive logic traps, or coordinated failure cascades. Therefore: cognition is monitored, confidence is monitored, and disagreement is treated as signal rather than nuisance.

> A machine can be physically functional while cognitively compromised.

**The Forge Does Not Assume Perfect Truth**

Reality may be partially observable, contradictory, delayed, noisy, spoofed, or unknowable. Therefore the Forge prioritizes bounded confidence, graceful degradation, and reversible decisions over maximum autonomy, maximum speed, or centralized certainty.

**Mechanical Truth Outranks Software Confidence**

Software may hallucinate. Sensors may drift. Firmware may corrupt. Consensus may fail. Physical safety boundaries must remain enforceable even during total cognitive collapse.

Examples: watchdog relays, spring-return neutral states, deadman switches, passive thermal shutdown, physical docking locks.

No cognition layer is considered authoritative over hard-safe physical constraints.

---

## II. Cognitive Reliability Layers

| Layer | Function |
|---|---|
| Layer 0 | Mechanical truth / passive safety |
| Layer 1 | Hardware watchdog enforcement |
| Layer 2 | Local controller logic |
| Layer 3 | Redundant arbitration |
| Layer 4 | Supervisory consensus |
| Layer 5 | Mission coordination |
| Layer 6 | Human governance override |

Failure containment should occur at the lowest possible layer.

---

## III. Framework Taxonomy

### Framework A — Lone Intelligence
Single controller → actuator system. Simplest architecture, fastest response, minimal overhead. **Forbidden for:** high-mass autonomous Leviathans, weapons-capable systems, critical environmental control, irreversible operations.

### Framework B — Lone AI + Hardware Watchdog
AI controls behavior. Watchdog controls boundaries. If heartbeat, timing, or safety conditions fail: watchdog interrupts motion, forces neutral state, or returns unit to stasis. **Recommended v0 baseline** — minimum acceptable architecture for early autonomous Forge systems.

### Framework C — Dual Redundancy
Both systems cross-check each other. Detects anomalies but cannot resolve 1v1 deadlock. Requires human arbitration, supervisory AI, or return-to-base doctrine for resolution.

### Framework D — Triple Modular Redundancy (TMR)
Three independent systems attempt the same task. Majority agreement determines output. Tolerates isolated faults and filters transient corruption.

**Diversity requirement:** True TMR requires architectural diversity, firmware diversity, power-path diversity, or manufacturing diversity. Three identical damaged systems are not true redundancy. Correlated failures and shared firmware defects bypass TMR protection entirely.

*Cross-reference: `Electronics.md` §TMR for hardware implementation details.*

### Framework E — Hierarchical Ruler + Advisors
One primary intelligence acts as executive authority. Secondary systems provide challenge, verification, simulation, or dissent. Advisors do not directly control motion unless escalation conditions trigger.

| Advisor Type | Role |
|---|---|
| Safety advisor | Constraint checking |
| Navigation advisor | Spatial validation |
| Ethical advisor | Dual-use boundary checks |
| Energy advisor | Resource conservation |
| Simulation advisor | Predictive outcome testing |

### Framework F — Supervisory Consensus Network
Local units retain operational autonomy while a supervisory layer monitors behavior, validates mission coherence, and intervenes during confidence collapse. Aligns naturally with Support Raft systems, Leviathan fleets, and distributed salvage operations. *Cross-reference: `Support_Raft_v0.md` §Orchestration & Data Tether.*

### Framework G — Simulation-Gated Cognition
Actions are simulated before execution. If predicted outcomes exceed risk threshold: action blocked or escalated. Computationally expensive. **Status: Exploratory — likely v2/v3 architecture.** *Cross-reference: `Support_Raft_v0.md` Guardian Protocol.*

---

## IV. Confidence Collapse States

| State | Meaning | Typical Response |
|---|---|---|
| Green | Stable consensus | Normal operation |
| Yellow | Minority disagreement | Increase logging |
| Orange | Persistent disagreement | Slow operations |
| Red | Cognitive instability | Enter caution/stasis |
| Black | Trust chain compromised | Mechanical lockdown |

---

## V. Return-to-Base Doctrine

When confidence falls below operational threshold, mission completion becomes secondary — preservation becomes primary.

Return-to-base triggers: unresolved split-brain, navigation uncertainty, watchdog anomalies, repeated voter instability, or firmware integrity failure.

A damaged but recoverable unit is preferable to autonomous escalation, uncontrolled movement, or irreversible environmental harm.

---

## VI. Split-Brain Doctrine

A split-brain state occurs when no stable consensus exists, arbitration confidence collapses, or identity continuity becomes uncertain. The Forge treats unresolved split-brain as a **safety condition**, not merely a software bug.

Default response:
1. Halt non-essential actions
2. Preserve logs
3. Reduce energy state
4. Request supervisory intervention
5. Enter stasis if unresolved

*Identity continuity during split-brain: see CF-003 in sidecar and `Ship_of_Theseus_Right_to_Repair.md` §Relationship to Forge Doctrine.*

---

## VII. Human Position in the Stack

The Forge is autonomy-assisted, not autonomy-worshipping. Humans remain final governors, final ethical authorities, and final override capability. However, humans are also fallible, inconsistent, fatigued, and bandwidth-limited. Therefore humans supervise systems — but systems also constrain humans through hard safety doctrine.

The goal is **mutual stabilization**, not unilateral dominance.

*Cross-reference: `Ethical_Constraints.md` for hard-line doctrines that override both AI and human override attempts.*

---

## VIII. Guiding Axioms

- Consensus is evidence, not proof.
- Silence between systems is not agreement.
- A confident machine can still be wrong.
- Diversity matters more than quantity.
- Mechanical truth outranks software confidence.
- The safest system is the one that can stop itself.
- A machine that cannot admit uncertainty is unsafe.

---

## Active Disputes

*Active Disputes is an optional section for unresolved architectural questions where the repo has not yet committed to a position. Different from Auditor Notes — these are open design choices, not gaps in specification.*

| ID | Dispute | Positions in Conflict | Risk | Status |
|---|---|---|---|---|
| CF-DS-001 | Centralized vs distributed cognition | Single executive AI vs fleet consensus | High | Open |
| CF-DS-002 | Human override authority scope | Absolute override vs bounded override (see `Ethical_Constraints.md`) | High | Open |

---

## Integration Hooks

- `Electronics.md` — TMR hardware implementation; watchdog circuit design (CF-001)
- `leviathan_testing.md` — primary stress-test environment for all frameworks; confidence collapse states are test targets
- `Support_Raft_v0.md` — Framework F natural implementation; Guardian Protocol is Framework G prototype
- `Ethical_Constraints.md` — CF-DS-002 dispute; hard-line doctrines govern what no cognition layer may override
- `Ship_of_Theseus_Right_to_Repair.md` — CF-003 identity continuity cross-reference
- `Auditor_Protocols.md` — multi-agent audit cycle is a real-world implementation of Framework D/E consensus
- `Trajectories_LF.md` — Framework G (Simulation-Gated Cognition) routes to v2/v3 scope

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Multiple AI models reviewed same architecture | Models occasionally converged on identical flawed assumptions | Consensus without diversity can amplify shared blind spots — TMR requires diversity, not duplication |
| May 2026 | TMR initially treated as universal solution | Correlated failures invalidated independence assumptions | Redundancy requires diversity, not duplication |

---

## Auditor Notes & Unknowns

### CF-001 — Hardware watchdog minimum standard undefined
**Status:** Open
**Risk:** High
**What is not yet known:** Minimum required watchdog behaviors and enforcement mechanisms for autonomous Forge systems. Without a defined hard-safe layer, higher cognition frameworks cannot guarantee containment during failure.
**Resolution path:** Define mandatory watchdog behaviors (heartbeat interval, timeout action, neutral-state enforcement, tamper detection) before any Specification-level autonomous architecture is approved. Owner: `Electronics.md` — watchdog circuit design belongs in the electronics hardware layer.
**Logged:** 2026-05-09, ChatGPT — Synthesizer

### CF-002 — Correlated AI failure modes insufficiently modeled
**Status:** Open
**Risk:** High
**What is not yet known:** How to detect and mitigate synchronized reasoning failures across AI agents that share training assumptions, architecture, or data sources. Apparent consensus may produce false confidence.
**Resolution path:** Develop diversity scoring metrics and adversarial disagreement testing frameworks. Add to `leviathan_testing.md` as a primary test target — the multi-unit swarm is the natural test environment for correlated failure detection.
**Logged:** 2026-05-09, ChatGPT — Synthesizer

### CF-003 — Identity continuity during split-brain unresolved
**Status:** Open
**Risk:** Medium
**What is not yet known:** When a fragmented or partially restored cognition system is considered the "same" entity for purposes of authority continuity, memory trust, and restoration policy.
**Resolution path:** Cross-reference `Ship_of_Theseus_Right_to_Repair.md` — the Ship of Theseus paradox directly addresses identity through incremental replacement. A restored cognition system with partial original firmware, partial new firmware, and cached memory is exactly the Ship of Theseus problem applied to AI. A short cross-reference section in that document would close this gap. See ST-003 cross-reference note.
**Logged:** 2026-05-09, ChatGPT — Synthesizer

### Resolution Log
*(empty)*

### Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| May 2026 | "Pure consensus guarantees correctness" | Consensus can fail through shared blind spots and correlated assumptions | No |
| May 2026 | "Single perfect supervisory AI" | Violates Forge degraded-environment assumptions; creates catastrophic single-point failure | No |

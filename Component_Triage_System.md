# Lazarus Forge — Component Triage System

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Multi-model — Claude, Gemini, Grok, ChatGPT)
- Open unknowns: 3 (Medium)
- Sidecar: [#auditor-notes--unknowns]

> Role: Decision gateway between reuse and destruction.

The Component Triage System exists to answer one question with speed, honesty, and minimal energy:

**Can this component or subassembly still function — or be restored to function — at lower total cost than fabricating a new one?**

Everything that passes triage is preserved as embodied complexity. Everything that fails triage enters material recovery. Triage always occurs before any material enters destructive processing.

*Note: This document implements the gate logic defined in `Lazarus_forge_v0_flow.md`, which is the reference standard for shared vocabulary. Where this document uses terms like "functional," "repair queue," or "scrap," those terms carry the meanings defined there.*

---

## I. Core Principles

**1. Non-Destructive First**
Never destroy or disassemble a component if a non-invasive test can establish viability.

**2. Progressive Depth**
Begin with the fastest, lowest-energy test. Escalate only when value is plausible.

**3. Human–Machine Hybrid**
Human judgment informs classification — it does not bypass the Gate A–D routing sequence defined in `Lazarus_forge_v0_flow.md`.

**4. Energy & Time Accounting**
Each test has a known energy/time cost. A component must justify deeper testing.

**5. Traceability**
Every triaged item receives a physical provenance tag at final disposition. Tag must record: component type, source, triage date, station outcomes, and final routing decision.

**6. Ethical Flag at Entry**
Components matching known dual-use or weaponization patterns must be flagged at Station 0 for Oversight review per `Ethical_Constraints.md` before entering the Component Library.

---

## II. Gate Correspondence

Triage stations map to the gate logic in `Lazarus_forge_v0_flow.md`:

| Triage Outcome | Flow Gate | Routing |
|---|---|---|
| Station pass — original function confirmed | Gate A pass | Component Library |
| Station pass — function only in reduced/different application | Gate C pass | Repurpose |
| Station partial — failure localized, within current tooling | Gate B pass | Repair & Learn queue |
| Station partial — failure exceeds current tooling capability | Gate B fail → Gate C | Assess for downgrade or Triage Terminal |
| Station fail — no function, material recovery value present | Gate D | Material Recovery (Reduction path) |
| Station fail — no function, no material recovery value | Gate D + Human/AI Oversight | Triage Terminal |

*Note on "sufficient for forge duty": this phrase means the component can perform a useful function within the Forge's current operational context, not necessarily its original application. If it only functions in a reduced application, it routes as Gate C, not Gate A. See TS-001 for threshold definition tracking.*

*Worked example:* A pump motor rated 500W runs at 320W (64%) under standard pump load — Gate A fail. The same motor runs adequately driving a ventilation fan at 40% duty — Gate C pass (repurpose to ventilation duty).

---

## III. Modular Triage Stations

### Station 0 — Visual & Basic Mechanical

**Purpose:** Rapid rejection of obvious failures. Contamination check. Dual-use flag.

- Visual inspection for cracks, burns, deformation, corrosion
- Manual spin, shake, and resistance checks
- Electrical continuity check where applicable
- **Contamination check:** Identify chemical or biological contamination. Contaminated items tagged and routed to decontamination hold before further triage. See TS-002.
- **Dual-use flag:** Flag components matching known high-risk patterns for Oversight review per Principle 6.

Decision time: < 2 minutes per item

Bins: Good / Maybe / Scrap / Contaminated / Flag

*"Scrap" means Material Recovery — the component enters the Reduction path. It does not mean disposal.*

---

### Station 1 — Electrical & Electronic Components

Priority items: motors, transformers, batteries, inverters, PCBs, solenoids

**Motor Test Bench**
- DC or AC supply, variable load
- Measures: no-load current, stall torque (approximate), winding resistance, insulation resistance

**Pass Guidance:**
≥ ~70% of expected performance or "sufficient for forge duty" *(Placeholder — see TS-001)*

*Gate A vs Gate C distinction:* A motor at ≥70% performance in its original application context is a Gate A pass. A motor that only meets the threshold in a reduced forge application is a Gate C disposition — routes to Repurpose, not Component Library.

**Battery Test**
- Charge–discharge cycle
- Accept partial capacity for stationary use *(Placeholder — minimum threshold pending operational data)*

**Electronics Screening**
- ESR and capacitance checks
- Visual inspection for thermal damage

---

### Station 2 — Mechanical Components

Priority items: bearings, gears, linear rails, pumps, structural members

**Bearing Spin Rig**
- Motorized spindle, vibration sensor (MEMS acceptable), audible and spectral noise assessment
- *Note: Acoustic assessment requires separation from active Reduction zones — ambient noise produces false failure readings.*

**Structural Metal**
- Ultrasonic thickness measurement or bend/load testing jigs
- *Ultrasonic gauges non-trivial to source at Gen-1 — load testing jigs are acceptable substitute*

---

### Station 3 — Functional Subassembly Test

Targets: gearboxes, power tools, pumps, fans

Runtime: 5–15 minutes *(Placeholder — to be refined from Gen-1 operational data)*

| Result | Condition | Routing |
|---|---|---|
| Pass | Performs original or equivalent function | Component Library (Gate A) |
| Partial | Failure localized, within current tooling | Repair & Learn (Gate B) |
| Partial | Failure exceeds current tooling | Assess for downgrade (Gate C) |
| Fail | No function, material has recovery value | Material Recovery — Reduction (Gate D) |
| Fail | No function, no recovery value | Triage Terminal |

*Gate B condition:* "Within current tooling capability" means the Forge can actually perform the repair with present equipment. A conceptually possible repair that exceeds current tooling fails Gate B.

---

### Station 4 — Assisted Borderline Evaluation (Later-Stage Forge)

Introduced gradually as data accumulates. Refines borderline calls from earlier stations. Does not override clear Pass or clear Fail outcomes from Stations 0–3. Borderline reclassifications must be logged with rationale.

---

## IV. Triage Terminal

**Every item reaching Material Recovery disposition must pass a structured hold review before irreversible processing begins.**

This is the Human/AI Oversight Gate from `Lazarus_forge_v0_flow.md` applied at the triage exit.

- If a credible, active use case exists: assign with a defined review date
- If no genuine need exists: Material Recovery proceeds

*Re-triage note:* Components that pass triage, enter service, and subsequently fail within the Forge re-enter triage at Station 0 with a provenance tag indicating prior service history.

---

## V. Data & Learning Loop

Each triage event records: component type, source, tests performed, energy/time spent, decision outcome, eventual fate.

Numeric thresholds (70% performance, 5–15 min runtime) are Placeholder values — candidates for revision after N≥50 consistent triage decisions on similar component classes.

---

## VI. Minimum Viable Triage (Gen-1 Forge)

A first-generation forge can operate with:
- One skilled human operator
- Multimeter
- 12V / 48V battery bank
- Salvaged loads (lights, heaters, pumps)
- Handwritten performance board for known-good components

---

## VII. Guiding Axioms

- Test cheap. Destroy expensive.
- A marginal component today beats a perfect ingot tomorrow.
- Doubt means test deeper. Certainty means move fast.
- Scrap means material recovery, not disposal.
- Triage serves the gate logic — it does not replace it.

> Triage is not about hoarding. It is about respecting embodied work already paid for by the universe.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | "Scrap" used as terminal bin label | Semantically drifted from flow document — operators may interpret as disposal rather than material recovery | Replaced with "Material Recovery" throughout; vocabulary note added; Scrap bin relabeled |
| May 2026 | Station 3 routed Fail directly to disassembly/scrap | Missing the Human/AI Oversight Gate — items reached irreversible processing without structured review | Triage Terminal section added as mandatory hold before any Material Recovery begins |

---

## Auditor Notes & Unknowns

### TS-001 — "Sufficient for forge duty" threshold undefined
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** A quantitative or contextual definition of acceptable degraded performance for components assigned to forge duty rather than original application. The 70% threshold in Station 1 does not distinguish Gate A (original function) from Gate C (reduced function).
**Resolution path:** Bootstrap Doctrine in Components.md offers candidate: "A component is sufficient if it allows the Forge loop to close." The Forge loop is now defined in geck_forge_seed.md Section III (intake → triage → process → verify → learn → repeat). This makes the sufficiency criterion falsifiable. Next step: define as application-specific thresholds once Gen-1 operational data is available. Populate Baseline Performance Table after N≥50 observations per component class.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-024 in Unknowns_LF.md*

### TS-002 — Contamination routing protocol incomplete
**Status:** Open
**Risk:** Medium
**What is not yet known:** How chemically or biologically contaminated components are handled through the triage station sequence — decontamination criteria, routing for components that cannot be decontaminated, and provenance tag requirements for contamination status.
**Resolution path:** Station 0 contamination check and Contaminated bin added (this revision). Full decontamination protocol still needed. Cross-reference `Air_Scrubber_v0.md` for chemical handling — the waste stream gap there and contamination handling here are the same problem from different directions.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-025 in Unknowns_LF.md*

### TS-003 — Gate logic determinism at boundary cases
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Whether gate logic produces deterministic routing for all item types at the Gate A/C and Gate C/D boundaries.
**Resolution path:** Gate Correspondence table added (this revision). Motor worked example added. See FL-001 in Lazarus_forge_v0_flow.md for the primary tracking entry — this entry is a downstream instance of the same gap.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-012 in Unknowns_LF.md*

### Resolution Log
- May 2026: Gate Correspondence table added — maps station outcomes to Gates A–D explicitly.
- May 2026: Motor worked example added to Station 1 — 65% torque → Gate A fail, Gate C pass.
- May 2026: Triage Terminal section added — Human/AI Oversight Gate now exists in this document.
- May 2026: "Scrap" vocabulary replaced with "Material Recovery" throughout.
- May 2026: Contamination check added to Station 0.
- May 2026: Ethical Flag added as Principle 6.
- May 2026: Re-triage path for in-service failures added to Triage Terminal.

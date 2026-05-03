# Lazarus Forge — Component Triage System

> Role: Decision gateway between reuse and destruction.

The Component Triage System exists to answer one question with speed, honesty, and minimal energy:

**Can this component or subassembly still function — or be restored to function — at lower total cost than fabricating a new one?**

Everything that passes triage is preserved as embodied complexity.
Everything that fails triage enters material recovery.

Triage always occurs before any material enters destructive processing.

*Note: This document implements the gate logic defined in `Lazarus_forge_v0_flow.md`, which is the reference standard for shared vocabulary. Where this document uses terms like "functional," "repair queue," or "scrap," those terms carry the meanings defined there. See Gate Correspondence section below.*

---

## I. Core Principles

**1. Non-Destructive First**
Never destroy or disassemble a component if a non-invasive test can establish viability.

**2. Progressive Depth**
Begin with the fastest, lowest-energy test. Escalate only when value is plausible.

**3. Human–Machine Hybrid**
Early forges rely on human judgment. Automation increases only after repeatable patterns emerge. Human judgment informs classification — it does not bypass the Gate A–D routing sequence defined in `Lazarus_forge_v0_flow.md`.

**4. Energy & Time Accounting**
Each test has a known energy/time cost. A component must justify deeper testing.

**5. Traceability**
Every triaged item receives a physical provenance tag (QR, RFID, etched mark, or paint code) at final disposition. Tag must record: component type, source, triage date, station outcomes, and final routing decision.

**6. Ethical Flag at Entry**
Components matching known dual-use or weaponization patterns (high-torque motors, precision timing circuits, pressure vessels, high-energy power electronics) must be flagged at Station 0 for Oversight review per `Ethical_Constraints.md` before entering the Component Library. Flagging does not block triage — it adds a review requirement before fabrication assignment.

---

## II. Triage Workflow Overview

Incoming material is pre-sorted by humans or crude mechanical means (size, magnetism, bulk type).

Components then pass through modular triage stations. Stations may be skipped if earlier results are decisive.

### Gate Correspondence

Triage stations map to the gate logic in `Lazarus_forge_v0_flow.md` as follows:

| Triage Outcome | Flow Gate | Routing |
|---|---|---|
| Station pass — original function confirmed | Gate A pass | Component Library |
| Station pass — function only in reduced/different application | Gate C pass | Repurpose / Lower-Precision Component |
| Station partial — failure is localized, within current tooling | Gate B pass | Repair & Learn queue |
| Station partial — failure exceeds current tooling capability | Gate B fail → Gate C | Assess for downgrade or Triage Terminal |
| Station fail — no function, material recovery value present | Gate D | Material Recovery (Reduction path) |
| Station fail — no function, no material recovery value | Gate D + Human/AI Oversight | Triage Terminal |

*Note on "sufficient for forge duty" (Station 1 pass guidance): this phrase means the component can perform a useful function within the Forge's current operational context, not necessarily its original application. If it only functions in a reduced application, it routes as Gate C (repurpose), not Gate A (original function confirmed). See UNK-024 in `Unknowns_LF.md` for threshold definition tracking.*

---

## III. Modular Triage Stations

### Station 0 — Visual & Basic Mechanical (Human + Simple Tools)

**Purpose:** Rapid rejection of obvious failures. Dual-use flag check.

- Visual inspection for cracks, burns, deformation, corrosion
- Manual spin, shake, and resistance checks
- Electrical continuity check (where applicable)
- **Contamination check:** Identify chemical contamination (oils, solvents, reactive materials) or biological contamination. Contaminated items are tagged and routed to a decontamination hold before further triage. Do not pass contaminated items through electrical or mechanical stations without decontamination. See UNK-025 in `Unknowns_LF.md` for contamination routing protocol tracking.
- **Dual-use flag:** Flag components matching known high-risk patterns for Oversight review (see Principle 6).

Decision time: < 2 minutes per item

Tools:
- Flashlight
- Multimeter
- Marker / paint pen
- Bins labeled: Good / Maybe / Scrap / Contaminated / Flag

*Vocabulary note: "Scrap" bin in this document means Material Recovery — the component enters the Reduction path per `Lazarus_forge_v0_flow.md`. It does not mean disposal. A component in the Scrap bin retains material recovery value and must pass the Triage Terminal before irreversible processing.*

---

### Station 1 — Electrical & Electronic Components

Priority Items:
- Motors
- Transformers
- Batteries
- Inverters
- PCBs
- Solenoids

**Test Rigs:**

*Motor Test Bench*
- DC or AC supply
- Variable load (resistive bank, dynamo, or friction brake)
- Measures: No-load current, stall torque (approximate), winding resistance, insulation resistance

**Pass Guidance:**
≥ ~70% of expected performance or "sufficient for forge duty" *(Placeholder — basis to be established from Gen-1 operational data or analog motor testing literature. See UNK-024.)*

*Gate A vs Gate C distinction:* A motor at ≥70% performance in its **original application context** is a Gate A pass. A motor that only meets the threshold in a **reduced forge application** (different duty, lower load) is a Gate C disposition — it routes to Repurpose, not Component Library. The 70% threshold does not distinguish these; operator judgment applies until UNK-024 is resolved.

*Worked example:* A pump motor rated 500W runs at 320W (64%) under standard pump load — Gate A fail. The same motor runs adequately driving a ventilation fan at 40% duty — Gate C pass (repurpose to ventilation duty). Both decisions are valid; the routing is different.

*Battery Test*
- Charge–discharge cycle
- Accept partial capacity for stationary use *(Placeholder — minimum acceptable capacity threshold pending operational data)*

*Electronics Screening*
- ESR and capacitance checks
- Visual inspection for thermal damage

---

### Station 2 — Mechanical Components

Priority Items:
- Bearings
- Gears
- Linear rails
- Pumps
- Structural members

**Methods:**

*Bearing Spin Rig*
- Motorized spindle
- Vibration sensor (MEMS accelerometer acceptable)
- Audible and spectral noise assessment
- *Note: Acoustic assessment requires separation from active Reduction zones (shredding, milling). Ambient noise from those operations will produce false failure readings. Station 2 should be physically isolated or testing scheduled during Reduction downtime at Gen-1 forges.*

*Gears & Linkages*
- Visual wear comparison charts
- Go/no-go gauges (forge-made)
- Lubricant inspection (color, smell, particulates)

*Structural Metal*
- Ultrasonic thickness measurement *(Note: ultrasonic gauges are non-trivial to source at Gen-1. Bend/load testing jigs are an acceptable substitute where gauge availability is limited.)*
- Simple bend or load testing jigs

---

### Station 3 — Functional Subassembly Test

Targets:
- Gearboxes
- Power tools
- Pumps
- Fans

**Method:**
- Standardized plug-and-play harnesses
- Known loads (water column, inertia wheel, resistive load)
- Runtime: 5–15 minutes *(Placeholder — runtime bounds to be refined from Gen-1 operational data)*

**Outcomes:**

| Result | Condition | Routing |
|---|---|---|
| Pass | Performs original or equivalent function | Component Library (Gate A) |
| Partial | Failure localized, within current tooling capability | Repair & Learn queue (Gate B) |
| Partial | Failure exceeds current tooling capability | Assess for downgrade (Gate C) |
| Fail | No function, material has recovery value | Material Recovery — Reduction path (Gate D) |
| Fail | No function, no recovery value | Triage Terminal — Human/AI Oversight Gate required |

*Gate B condition:* "Within current tooling capability" means the Forge can actually perform the repair with its present equipment. A repair that is conceptually possible but exceeds current tooling fails Gate B and routes to Gate C assessment before disassembly. See `Lazarus_forge_v0_flow.md` Gate B definition.

---

### Station 4 — Assisted Borderline Evaluation (Later-Stage Forge)

Introduced gradually as data accumulates.

- Vision-based crack and wear detection
- Acoustic analysis of motor hum
- Comparison against historical triage outcomes
- Predictive lifespan estimation

This station refines borderline calls from earlier stations. It does not override clear Pass or clear Fail outcomes from Stations 0–3. Borderline reclassifications by Station 4 must be logged with rationale.

---

## IV. Triage Terminal

**Every item reaching a Scrap / Material Recovery disposition must pass a structured hold review before irreversible processing begins.**

This is the Human/AI Oversight Gate from `Lazarus_forge_v0_flow.md`, applied at the triage exit. Its purpose: prevent premature destruction where no current need has been evaluated, and prevent hoarding where no genuine need exists.

**Evaluation standard:** Does a credible, active use case exist for this item or its sub-components?
- If yes: assign to that use with a defined review date
- If no: Material Recovery proceeds

Components that fail the Triage Terminal **do not enter fabrication or the Component Library**. They route directly to Reduction. A component in Reduction may still yield useful material through Purification — "scrap" is not "waste."

*Re-triage note:* Components that pass triage and enter service, then subsequently fail within the Forge, re-enter triage at Station 0 with a provenance tag indicating prior service history. Repeated borderline passes trigger Human/AI Oversight review before re-entry into the Component Library.

---

## V. Data & Learning Loop

Each triage event records:
- Component type
- Source object
- Tests performed
- Energy/time spent testing
- Decision outcome
- Eventual fate (used, repaired, scrapped)

Early systems may log on paper. Later systems digitize and aggregate.

This data refines:
- Pass/fail thresholds
- Test ordering
- Repair vs replace heuristics

*Threshold updates:* Numeric thresholds (70% performance, 5–15 min runtime) are Placeholder values. They are candidates for revision after N≥50 consistent triage decisions on similar component classes produce a reliable operational baseline. Do not revise thresholds on fewer observations — early data is noisy.

---

## VI. Minimum Viable Triage (Gen-1 Forge)

A first-generation forge can operate with:
- One skilled human operator
- Multimeter
- 12V / 48V battery bank
- Salvaged loads (lights, heaters, pumps)
- Handwritten performance board for known-good components

This alone preserves the motors, bearings, and power hardware required to bootstrap the Forge.

---

## VII. Guiding Axioms

- Test cheap. Destroy expensive.
- A marginal component today beats a perfect ingot tomorrow.
- Doubt means test deeper. Certainty means move fast.
- Scrap means material recovery, not disposal.
- Triage serves the gate logic — it does not replace it.

---

> Triage is not about hoarding. It is about respecting embodied work already paid for by the universe.

This document evolves only with demonstrated operational need.

---

## Audit Status

Reviewed under Auditor_Protocols.md v0.4, Component_Triage_System.md first audit cycle, May 2026.
Status: Exploration. Multi-model audit pass: Claude, Gemini, Grok, ChatGPT.
Key changes from prior version: Added Gate Correspondence table; clarified Gate A/C boundary in Station 1 with worked example; added Gate B tooling condition to Station 3; added Triage Terminal section (Gate D / Human/AI Oversight Gate); replaced "Scrap" vocabulary with Material Recovery throughout; added contamination handling at Station 0; added Ethical Flag principle and Station 0 dual-use check; added re-triage path for in-service failures; added acoustic isolation note for Station 2; labeled numeric thresholds as Placeholder.
Open unknowns: UNK-012 (gate determinism — partially addressed by Gate Correspondence table and worked example), UNK-014 (weaponization pattern detection — hook added at Station 0 and Principle 6), UNK-024 (forge duty threshold definition), UNK-025 (contamination routing protocol). See `Unknowns_LF.md`.

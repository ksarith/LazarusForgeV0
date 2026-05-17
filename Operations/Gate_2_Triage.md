# Lazarus Forge — Component Triage System

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-09 (ChatGPT — Synthesizer; Claude — Engineer)
- Open unknowns: 3 (Medium)
- Sidecar: [#auditor-notes--unknowns]

> Role: Decision gateway between reuse and destruction.
> The Forge is preserving machine work, precision, process history, and infrastructure inheritance — not just metal.

The Component Triage System exists to answer one question with speed, honesty, and minimal energy:

**Can this component or subassembly still function — or be restored to function — at lower total cost than fabricating a new one?**

Everything that passes triage is preserved as embodied complexity. Everything that fails triage enters material recovery. Triage always occurs before any material enters destructive processing.

*Note: This document implements the gate logic defined in `Lazarus_forge_v0_flow.md`, which is the reference standard for shared vocabulary.*

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
Every triaged item receives a physical provenance tag at final disposition recording: component type, source, triage date, station outcomes, final routing decision, and any prior service or repair history.

**6. Ethical Flag at Entry**
Components matching known dual-use or weaponization patterns must be flagged at Station 0 for Oversight review per `Ethical_Constraints.md` before entering the Component Library.

**7. Queues Are Active Allocations, Not Passive Storage**
Triage queues are prioritized operational allocations competing for finite Forge resources: time, energy, tooling, storage volume, and operator attention. Queue priority should favor actions most likely to improve closure of the current Forge operational loop. Inactive queue items eventually consume more Forge resources than material recovery would reclaim.

**8. Strategic Recoverability Is a Triage Axis**
Triage operates on two axes simultaneously:
- *Operational utility* — does this component help now?
- *Strategic recoverability* — could this become impossible or extremely expensive to recreate later?

Components requiring rare materials, specialized tooling, high precision manufacturing, or fragile supply chains should require higher confidence before irreversible material recovery is authorized.

---

## II. Triage Philosophy

**What the Forge is optimizing for:**
Preservation of recoverable industrial capability under constrained conditions — not salvage quantity, not efficiency alone.

**False-positive doctrine:**
The Forge preferentially tolerates false-positive retention (preserving a bad component) over false-negative destruction (destroying a recoverable one) during bootstrap phases. As the Forge matures, destruction confidence thresholds tighten.

| Forge Stage | Preferred Error |
|---|---|
| Bootstrap | False-positive retention |
| Transitional | Balanced |
| Mature Industrial | False-negative rejection tolerance increases |

Irreversible destruction should require higher confidence than temporary retention. This is not a hoarding doctrine — it is a calibrated asymmetry that acknowledges the cost of irreversibility during early-stage operations.

**Forge-duty sufficiency:**
A component is sufficient for Forge duty if it materially contributes to closure of the current operational loop, not whether it meets original manufacturer specifications. *(See TS-001)*

**Embedded industrial capability:**
The more advanced the artifact, the more condensed civilization may be inside it. A precision harmonic drive, a failed semiconductor component, or a rare alloy casting may be operationally useless today but strategically irreplaceable later. The operator is not merely evaluating component condition — they are evaluating embedded industrial capability.

---

## III. Strategic Recoverability Tiers

| Tier | Meaning | Triage Implication |
|---|---|---|
| Common | Easily reproduced locally | Standard gate routing |
| Constrained | Reproducible with moderate infrastructure | Elevated retention tolerance |
| Strategic | Requires advanced tooling or supply chains | High confidence required before material recovery |
| Critical | Currently irreproducible within Forge capability | Preservation strongly preferred; escalate to Human/AI Oversight Gate |

These tiers influence queue priority, destruction authorization, provenance retention depth, and repurpose restrictions — without making the system bureaucratic.

---

## IV. Gate Correspondence

Triage stations map to the gate logic in `Lazarus_forge_v0_flow.md`:

| Triage Outcome | Flow Gate | Routing |
|---|---|---|
| Station pass — original function confirmed | Gate A pass | Component Library |
| Station pass — function only in reduced/different application | Gate C pass | Repurpose |
| Station partial — failure localized, within current tooling | Gate B pass | Repair & Learn queue |
| Station partial — failure exceeds current tooling capability | Gate B fail → Gate C | Assess for downgrade or Triage Terminal |
| Station fail — no function, material recovery value present | Gate D | Material Recovery (Reduction path) |
| Station fail — no function, no material recovery value | Gate D + Oversight | Triage Terminal |

*Worked example:* A pump motor rated 500W runs at 320W under standard pump load — Gate A fail. The same motor drives a ventilation fan at 40% duty — Gate C pass (repurpose to ventilation duty).

---

## V. Queue Economics

Triage queues are not passive storage. They are dynamic resource-allocation decisions under constrained energy, time, and tooling conditions.

**Queue entry requirements:**
Every component entering a repair or repurpose queue must carry:
- Entry date
- Estimated recovery value (qualitative at v0: Low / Medium / High / Strategic)
- Reassessment interval
- Downgrade criteria (conditions under which the item drops to a lower queue or proceeds to material recovery)

**Queue saturation behavior:**
If a queue reaches capacity, the lowest-value items are reassessed before new items are admitted. Queue saturation is a signal that the Forge's repair or repurpose throughput is insufficient — log it as a Forge health indicator.

**Queue decay:**
Items that exceed their reassessment interval without action are automatically flagged for Human/AI Oversight Gate review. The default downgrade path is: repair queue → repurpose queue → material recovery. Human judgment required to hold above the default path.

**Provenance granularity:**
Provenance chains should preserve enough history to identify recurring failure patterns without imposing unsustainable logging burden. Minimum at v0: original source, triage date, station outcomes, any repair events. Richer provenance for Strategic and Critical tier components.

---

## VI. Modular Triage Stations

### Station 0 — Visual & Basic Mechanical

**Purpose:** Rapid rejection of obvious failures. Strategic tier assessment. Contamination check. Dual-use flag.

- Visual inspection for cracks, burns, deformation, corrosion
- Initial strategic recoverability assessment — assign preliminary tier
- Contamination check: chemical or biological contamination routes to decontamination hold before further triage *(see TS-002)*
- Dual-use flag: components matching known high-risk patterns route to Oversight review

Bins: Good / Maybe / Scrap / Contaminated / Flag / Strategic Hold

*"Scrap" means Material Recovery — Reduction path. Not disposal.*

Decision time: < 2 minutes per item

---

### Station 1 — Electrical & Electronic Components

Priority items: motors, transformers, batteries, inverters, PCBs, solenoids

*Cross-reference: `Electronics.md` for detailed harvesting, desoldering, and integrity check protocols.*

**Pass Guidance:**
≥ ~70% of expected performance or "sufficient for forge duty" *(Placeholder — see TS-001)*

Gate A vs Gate C distinction: performance in original application = Gate A. Performance only in reduced application = Gate C.

Strategic tier override: a motor at 40% performance that requires rare-earth magnets may warrant Strategic Hold regardless of functional gate outcome.

---

### Station 2 — Mechanical Components

Priority items: bearings, gears, linear rails, pumps, structural members

Acoustic assessment requires separation from active Reduction zones — ambient noise produces false failure readings.

Ultrasonic thickness gauges non-trivial to source at Gen-1 — load testing jigs are acceptable substitute.

---

### Station 3 — Functional Subassembly Test

Runtime: 5–15 minutes *(Placeholder)*

| Result | Condition | Routing |
|---|---|---|
| Pass | Performs original or equivalent function | Component Library (Gate A) |
| Partial | Failure localized, within current tooling | Repair & Learn (Gate B) |
| Partial | Failure exceeds current tooling | Assess for downgrade (Gate C) |
| Fail | No function, material has recovery value | Material Recovery — Reduction (Gate D) |
| Fail | No function, no recovery value | Triage Terminal |
| Any | Strategic or Critical tier | Escalate to Human/AI Oversight Gate regardless of functional result |

---

### Station 4 — Assisted Borderline Evaluation (Later-Stage Forge)

Refines borderline calls. Does not override clear Pass or clear Fail from Stations 0–3.

**Anti-overfitting protection:** Assisted evaluation systems may recommend classifications but must preserve auditable reasoning paths and periodic human validation sampling. Historical bias reinforcement — bad historical classifications confirmed by pattern-matching — is a known failure mode. Require human review samples at defined intervals.

---

## VII. Triage Terminal

Every item reaching Material Recovery disposition must pass a structured hold review before irreversible processing begins. This is the Human/AI Oversight Gate from `Lazarus_forge_v0_flow.md` at the triage exit.

- If a credible, active use case exists: assign with defined review date
- If Strategic or Critical tier: require explicit human authorization before material recovery proceeds
- If no genuine need exists: Material Recovery proceeds

*Re-triage:* Components that fail in Forge service re-enter triage at Station 0 with provenance tag indicating prior service history. Recurring failures on same component type trigger pattern logging.

---

## VIII. Failure Modes

| Failure Mode | Description | Mitigation |
|---|---|---|
| Contamination bypass | Contaminated component passes to electrical/mechanical stations | Station 0 contamination check mandatory before escalation |
| Misclassified fatigue damage | Visually acceptable component fails under load | Station 3 runtime testing; provenance history review |
| Queue saturation | Backlog exceeds Forge capacity to process | Queue decay protocol; reassessment triggers |
| False functional validation | Component passes test but fails in service | Re-triage protocol; provenance pattern logging |
| Unsafe repurpose routing | Component repurposed beyond safe degradation threshold | Strategic tier override at Triage Terminal |
| Provenance loss | Component history lost between triage events | Mandatory tag system; re-triage if tag absent |

---

## IX. Data & Learning Loop

Each triage event records: component type, source, strategic tier, tests performed, energy/time spent, decision outcome, eventual fate.

Numeric thresholds (70% performance, 5–15 min runtime) are Placeholder — revise after N≥50 consistent decisions on similar component classes.

Recurring failure patterns on specific component types are flagged for classification rule updates.

---

## X. Minimum Viable Triage (Gen-1 Forge)

- One skilled human operator
- Multimeter
- 12V / 48V battery bank
- Salvaged loads for testing
- Handwritten performance board for known-good components
- Strategic tier log (even a notebook column) for components assessed as Constrained or above

---

## XI. Guiding Axioms

- Test cheap. Destroy expensive.
- A marginal component today beats a perfect ingot tomorrow.
- Doubt means test deeper. Certainty means move fast.
- Scrap means material recovery, not disposal.
- Triage serves the gate logic — it does not replace it.
- The rarer the capability embedded, the higher the confidence required to destroy it.
- Queues are not storage. They are decisions deferred under resource constraint.

> Triage is not about hoarding. It is about respecting embodied work already paid for by the universe.

---

## Interfaces

| Interface | Direction | What crosses |
|---|---|---|
| Intake | → Triage | Raw salvage items with basic safety screening |
| Material Recovery | Triage → | Failed items routed to Reduction path |
| Component Library | Triage → | Passed items cataloged for Fabrication |
| Repair & Learn queue | Triage ↔ | Partially functional items; outcomes feed back |
| Ethical Constraints | Triage → | Dual-use flags escalate here |
| Forge Flow | Reference | Gate logic and terminology standard |
| Electronics.md | Reference | Electrical component harvesting protocols |
| Air Scrubber | → Triage | Contamination handling; chemical waste from decontamination |

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | "Scrap" used as terminal bin label | Operators may interpret as disposal rather than material recovery | Replaced with "Material Recovery"; vocabulary note added |
| May 2026 | Station 3 routed Fail directly to disassembly | Missing Human/AI Oversight Gate | Triage Terminal added as mandatory hold |
| May 2026 | Queues treated as passive storage | Risk of latent hoarding, decision fatigue, dead inventory | Queues are active allocations with decay, saturation behavior, and reassessment triggers |

---

## Auditor Notes & Unknowns

### TS-001 — "Sufficient for forge duty" threshold undefined
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Quantitative or contextual definition of acceptable degraded performance for forge-duty components.
**Resolution path:** Working definition added: "A component is sufficient if it materially contributes to closure of the current operational loop, not whether it meets original manufacturer specifications." Populate Baseline Performance Table after N≥50 observations per component class.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-024 in Unknowns_LF.md*

### TS-002 — Contamination routing protocol incomplete
**Status:** Open
**Risk:** Medium
**What is not yet known:** Full decontamination criteria, routing for components that cannot be decontaminated, and provenance tag requirements for contamination status.
**Resolution path:** Station 0 contamination check and Contaminated bin added. Full decontamination protocol still needed. Cross-reference `Air_Scrubber_v0.md` AS-003.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-025 in Unknowns_LF.md*

### TS-003 — Gate logic determinism at boundary cases
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Deterministic routing for all item types at Gate A/C and Gate C/D boundaries.
**Resolution path:** Gate Correspondence table added. Motor worked example added. Strategic tier override adds a new routing path that may create additional boundary cases — needs worked examples.
**Logged:** Component_Triage_System.md multi-model audit cycle, May 2026
*Cross-module reference: UNK-012 in Unknowns_LF.md*

### Resolution Log
- May 2026: Gate Correspondence table added.
- May 2026: Motor worked example added to Station 1.
- May 2026: Triage Terminal added — Human/AI Oversight Gate now present.
- May 2026: "Scrap" replaced with "Material Recovery" throughout.
- May 2026: Contamination check added to Station 0.
- May 2026: Ethical Flag added as Principle 6.
- May 2026: Re-triage path for in-service failures added.
- May 2026: Queue Economics section added — queues as active allocations.
- May 2026: Strategic Recoverability axis added — dual triage axes, tier classification.
- May 2026: False-positive doctrine added — bootstrap asymmetry.
- May 2026: Failure Modes section added.
- May 2026: Interfaces section added.
- May 2026: Station 4 anti-overfitting protection added.

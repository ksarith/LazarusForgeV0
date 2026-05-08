# Lazarus Forge — v0 Operational Flow

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 1 (Blocking at promotion)
- Sidecar: [#auditor-notes--unknowns]

This document defines the **minimal viable operational logic** of the Lazarus Forge and is the **reference standard for shared vocabulary** across the repository. Terms defined or used here carry their meaning into all other documents unless explicitly noted otherwise.

It is not a claim of full automation. It is a falsifiable flow that can be executed manually, semi-automatically, or automated later.

---

## v0 Scope and Assumptions

**Input (v0):**
- Small appliances
- Tools
- Mechanical/electromechanical assemblies
- Mixed metals with attached components

**Explicit Non-Goals (v0):**
- Fully autonomous operation
- Zero external inputs
- Net-positive energy claims without measurement
- Perfect material purity

---

## Defined Terms

**Functional** — Performs a useful role in a specific application context. An item is functional at Gate A if it works in its original application. An item is functional at Gate C if it can work in a reduced application.

**Equivalent function (Gate A)** — Performing the same task as the original in the same application context. If function is only achievable in a different or reduced application, the item does not pass Gate A — it routes to Gate C.

**Within tooling capability (Gate B)** — Evaluated against the Forge's current tooling inventory, not projected future capability.

**Contamination level** — Type and degree of contamination sufficient to affect downstream processing. Relevant categories at v0: chemical, biological, and embedded materials requiring separation before reduction or purification.

**Inert waste** — Material with no remaining functional, structural, or material recovery value, sorted for conventional disposal.

**Want vs. Need (policy term)** — A want becomes a need when its absence limits a higher-priority function. This distinction governs the Human/AI Oversight Gate and Fabrication priority order.

---

## Gate Correspondence

Triage station outcomes map to these gates. See `Component_Triage_System.md` for the full mapping table.

| Gate | Test | Routes to |
|---|---|---|
| A | Original function in original context? | Component Library |
| B | Repairable within current tooling? | Repair & Learn |
| C | Useful in reduced/different application? | Repurpose |
| D | Material recovery value remaining? | Reduction |
| Oversight | Any credible active need? | Hold or Reduction |

---

## 1. Intake

**Purpose:** Introduce salvage items into the system with minimal preprocessing.

**Actions:**
- Visual inspection
- Basic safety screening (hazards, pressure, charge)
- Tagging (manual or digital)

**Outputs:** Item enters Classification

---

## 2. Classification & Triage

**Purpose:** Determine the highest-value path before irreversible action.

**Classification Attributes (v0):**
- Mechanical integrity
- Electrical continuity
- Contamination level (see Defined Terms)
- Known failure modes

Classification may be **overridden by human operator**.

---

## 3. Decision Gates (Ordered, Mandatory)

### Gate A — Still Functional?
**Test:** Performs original function, or equivalent function in the same application context
**If YES →** Component Library
**If NO →** Gate B

### Gate B — Repairable?
**Test:** Failure is localized, accessible, and within current tooling capability
**If YES →** Repair & Learn
**If NO →** Gate C

### Gate C — Graceful Downgrade Possible?
**Test:** Can the item serve a useful function in a different or reduced application?
**If YES →** Repurpose as Lower-Precision Component
**If NO →** Gate D

*Note: Gate C tests functional downgrade potential. Gate D tests material integrity. These are distinct tests.*

### Gate D — Truly Exhausted?
**Test:** Structural, chemical, or thermal damage prevents any functional use AND material is not recoverable through Purification
**If YES →** Reduction
**If NO →** Human/AI Oversight Gate

### Human/AI Oversight Gate
Review items that failed Gates A–D but where reduction feels premature. Evaluate against active needs only — not hypothetical future uses. Apply the want/need policy (see Defined Terms).

- If a genuine need exists: assign with a defined review date
- If no genuine need exists: Reduction proceeds

This gate prevents both hoarding and premature destruction.

---

## 4. Outcome Paths

### Component Library
- Catalog reusable parts
- Track provenance and test results
- Feeds Fabrication directly
- *Reversibility: components remain individually recoverable*

### Repair & Learn
- Attempt repair
- Log failure mode and fix
- Update heuristics
- Outputs to Component Library or Repurpose
- *Reversibility: disassembly may affect calibration or tolerances — log pre-repair state*

### Repurpose (Lower Precision)
- Assign to reduced-spec use cases
- Examples: jigs, fixtures, structural members
- Feeds Fabrication

### Reduction
**Irreversible step — point of no return for the item as a discrete object**
- Shredding, cutting, or milling
- Size reduction only (no melting yet)
- *This is the only fully irreversible step in the flow*

### Purification
- Spin chamber or any mechanism achieving comparable separation output
- Pass / fail logic
- Fallback to powder or bulk stock if needed
- *Equivalence criteria defined in `Spin_Chamber_v0.md`*

---

## 5. Fabrication / Assembly

**Inputs:** Salvaged components, purified stock, repurposed parts

**Outputs:** Tools, fixtures, replacement components, infrastructure for future Forge growth

Fabrication is **not terminal**.

Priority order: (1) tools or components the Forge currently lacks, (2) infrastructure that expands Forge capability, (3) output for external use or exchange.

Priority is evaluated using the want/need policy (see Defined Terms).

---

## 6. Utilization

**Purpose:** Test real-world performance.

**Metrics Captured:** Runtime, failure modes, load tolerance, maintenance frequency

---

## 7. Feedback & Learning

**Feedback Targets:** Classification rules, repair heuristics, tolerance thresholds, tooling priorities

**Learning Mode (v0):** Human-readable logs, simple rule updates, no ML required

---

## v0 Key Performance Indicator (KPI)

**Primary KPI:** Value recovered per kWh consumed

If this metric is not competitive at small scale, scaling is invalid.

*KPI definition is Placeholder pending: (a) definition of "value" in measurable units; (b) accounting method for different recovery paths; (c) demand baseline from `energy_v0.md`.*

---

## Termination Conditions

An item exits the system only when:
- It is in active use
- It is stored as stock
- It is reduced to inert waste after all prior gates fail (see Defined Terms)

---

## Notes

This flow is intentionally conservative. Irreversibility is delayed. Human judgment is explicit. Automation is optional, not assumed.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Gate A "equivalent function" left undefined | Created overlap with Gate C — same item could route to either | Gate A requires function in original application context; Gate C handles all reduced/different applications |
| May 2026 | Gate C and Gate D described with near-identical language | Boundary between them was ambiguous | Gate C = functional downgrade test; Gate D = material integrity test. Explicitly distinct. |

---

## Auditor Notes & Unknowns

### FL-001 — Gate logic determinism unverified at boundary cases
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Whether gate logic (A→B→C→D) produces deterministic routing for all item types. Key boundary cases: Gate A/C (item functional in reduced but not original application), Gate C/D (no function but material recovery value), Human/AI Oversight Gate edge cases.
**Resolution path:** Gate Correspondence table added (this revision). Motor worked example added to Component_Triage_System.md (65% torque → Gate A fail, Gate C pass). Remaining: Gate C/D boundary worked example and Oversight Gate edge case still needed. Forge loop definition in geck_forge_seed.md Section III feeds the sufficiency criterion. See also TS-001 (forge duty threshold) in Component_Triage_System.md.
**Logged:** Lazarus_forge_v0_flow.md audit cycle, May 2026
*Cross-module reference: UNK-012 in Unknowns_LF.md*

### Resolution Log
- May 2026: Gate A "equivalent function" defined — requires original application context. Gate C/D boundary clarified — functional vs. material integrity tests. Defined Terms section added. Reversibility notes added per outcome path. KPI labeled Placeholder.

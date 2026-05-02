# Lazarus Forge — v0 Operational Flow

This document defines the **minimal viable operational logic** of the Lazarus Forge.
It is not a claim of full automation. It is a falsifiable flow that can be executed
manually, semi-automatically, or automated later.

This document is the **reference standard for shared vocabulary** across the repository.
Terms defined or used here carry their meaning into all other documents unless explicitly
noted otherwise.

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

The following terms are used with specific meaning throughout this document and the repository.

**Functional** — Performs a useful role in a specific application context. An item is functional at Gate A if it works in its *original* application. An item is functional at Gate C if it can work in a *reduced* application. An item that is only functional in a completely different application than either routes through Gate C regardless.

**Equivalent function (Gate A)** — Performing the same task as the original in the same application context, even if efficiency or precision is reduced within acceptable bounds. If function is only achievable in a different or reduced application, the item does not pass Gate A — it routes to Gate C.

**Within tooling capability (Gate B)** — Evaluated against the Forge's *current* tooling inventory, not projected future capability. A repair that exceeds current tooling fails Gate B even if it would pass at a later version.

**Contamination level** — Type and degree of contamination sufficient to affect downstream processing. Relevant categories at v0: chemical contamination (oils, solvents, reactive materials), biological contamination, and embedded materials requiring separation before reduction or purification.

**Inert waste** — Material with no remaining functional, structural, or material recovery value, sorted and staged for conventional disposal. Inert waste does not require further processing by the Forge. Achieving inert status may require Reduction, Purification, or both — whichever leaves the material non-reactive and non-recoverable.

**Want vs. Need (policy term)** — A want is a desired capability or resource. A want becomes a need when its absence limits a higher-priority function. This distinction governs the Human/AI Oversight Gate and Fabrication priority order. It is a decision rule, not a preference — items and fabrication tasks are evaluated against active, demonstrable limitations, not hypothetical future uses.

---

## 1. Intake

**Purpose:**
Introduce salvage items into the system with minimal preprocessing.

**Actions:**
- Visual inspection
- Basic safety screening (hazards, pressure, charge)
- Tagging (manual or digital)

**Outputs:**
- Item enters Classification

---

## 2. Classification & Triage

**Purpose:**
Determine the highest-value path before irreversible action.

**Classification Attributes (v0):**
- Mechanical integrity
- Electrical continuity
- Contamination level (see Defined Terms)
- Known failure modes

Classification may be **overridden by human operator**.

---

## 3. Decision Gates (Ordered, Mandatory)

Gates are evaluated in sequence. An item proceeds to the next gate only after failing the current one.

---

### Gate A — Still Functional?
**Test:** Performs original function, or equivalent function in the same application context (see Defined Terms)
**If YES →** Component Library
**If NO →** Gate B

---

### Gate B — Repairable?
**Test:** Failure is localized, accessible, and within *current* tooling capability (see Defined Terms)
**If YES →** Repair & Learn
**If NO →** Gate C

---

### Gate C — Graceful Downgrade Possible?
**Test:** Can the item serve a useful function at lower precision, tolerance, or duty cycle in a *different or reduced* application?
**If YES →** Repurpose as Lower-Precision Component
**If NO →** Gate D

*Note: Gate C tests functional downgrade potential — whether the item can still do useful work in any application. Gate D tests material integrity — whether the item retains recoverable material value even if all functional use is exhausted. These are distinct tests.*

---

### Gate D — Truly Exhausted?
**Test:** Structural, chemical, or thermal damage prevents *any* functional use AND material is not recoverable through Purification
**If YES →** Reduction (or direct to inert waste if reduction adds no recovery value)
**If NO →** Human/AI Oversight Gate

*Note: An item that has no functional value but retains material recovery value (e.g., intact metal stock with chemical contamination) should not reach Gate D — it routes to Reduction → Purification. Gate D is specifically for items where both functional and material recovery have been exhausted.*

---

### Human/AI Oversight Gate

Review items that failed Gates A–D but where reduction feels premature. This gate exists because the gate logic cannot anticipate every edge case — human judgment fills the gap.

**Evaluation standard:** Active needs only — not hypothetical future uses. Apply the want/need policy (see Defined Terms): does a credible, current use case exist?

**If a genuine need exists:** Assign to that need with a defined review date. The item is not in limbo — it has a committed use or it proceeds.
**If no genuine need exists:** Reduction proceeds without guilt.

This gate prevents both hoarding ("maybe someday") and premature destruction. It is not a reprieve — it is a structured decision with a defined outcome.

---

## 4. Outcome Paths

### Component Library
- Catalog reusable parts
- Track provenance and test results
- Feeds Fabrication directly
- *Reversibility note: Components remain individually recoverable. Library items can be re-evaluated if needs change.*

---

### Repair & Learn
- Attempt repair
- Log failure mode and fix
- Update heuristics
- Outputs to Component Library or Repurpose
- *Reversibility note: Disassembly may affect calibration, coatings, or tolerances. Repair is partially irreversible — log pre-repair state.*

---

### Repurpose (Lower Precision)
- Assign to reduced-spec use cases
- Examples: jigs, fixtures, structural members
- Feeds Fabrication
- *Reversibility note: Repurposed items may be recoverable to Component Library if original function is later demonstrated.*

---

### Reduction
**Irreversible step — point of no return for the item as a discrete object**
- Shredding, cutting, or milling
- Size reduction only (no melting yet)
- Output feeds Purification or bulk stock
- *Reversibility note: Once reduced, the item cannot be restored as a discrete component. This is the only fully irreversible step in the flow.*

---

### Purification
- Spin chamber or any mechanism achieving comparable separation output
- *"Equivalent" here means achieving similar separation efficiency and material purity for the target output stream. Specific equivalence criteria are defined in `Spin_Chamber_v0.md` — (Placeholder pending that document's specification).*
- Pass / fail logic
- Fallback to powder or bulk stock if needed

---

## 5. Fabrication / Assembly

**Inputs:**
- Salvaged components
- Purified stock
- Repurposed parts

**Outputs:**
- Tools
- Fixtures
- Replacement components
- Infrastructure for future Forge growth

Fabrication is **not terminal**.

Fabrication priority order: (1) tools or components the Forge currently lacks, (2) infrastructure that expands Forge capability, (3) output for external use or exchange.

Priority is evaluated using the want/need policy (see Defined Terms): a want becomes a need when its absence limits a higher-priority function.

---

## 6. Utilization

**Purpose:**
Test real-world performance.

**Metrics Captured:**
- Runtime
- Failure modes
- Load tolerance
- Maintenance frequency

---

## 7. Feedback & Learning

**Feedback Targets:**
- Classification rules
- Repair heuristics
- Tolerance thresholds
- Tooling priorities

**Learning Mode (v0):**
- Human-readable logs
- Simple rule updates
- No ML required

---

## v0 Key Performance Indicator (KPI)

**Primary KPI:**
> Value recovered per kWh consumed

If this metric is not competitive at small scale, scaling is invalid.

*KPI definition is Placeholder pending:*
- *(a) Definition of "value" in measurable units — monetary, functional, or material mass equivalent*
- *(b) Accounting method for different recovery paths — a repaired component and a kg of purified stock count differently*
- *(c) Demand baseline from UNK-011 in `Unknowns_LF.md`*

*The KPI concept is sound and correctly orients the system toward efficiency. The measurement definition is deferred to specification stage.*

---

## Termination Conditions

An item exits the system only when:
- It is in active use
- It is stored as stock
- It is reduced to inert waste after all prior gates fail (see Defined Terms for inert waste definition)

---

## Notes

This flow is intentionally conservative.
Irreversibility is delayed.
Human judgment is explicit.
Automation is optional, not assumed.

---

## Audit Status

Reviewed under Auditor_Protocols.md v0.3, Lazarus_forge_v0_flow.md audit cycle, May 2026.
Status: Exploration. Five promotion blockers identified and addressed in this revision.
Auditor: Claude (Sonnet 4.6), Skeptic/Auditor role.
UNK-012 logged in `Unknowns_LF.md` as result of this cycle.
Key changes: Added Defined Terms section; clarified Gate A/C boundary; clarified Gate C/D boundary distinction (functional vs. material); added reversibility notes per outcome path; labeled KPI as Placeholder with explicit pending items; elevated want/need rule to defined policy term; clarified Purification equivalence as pending Spin_Chamber_v0.md specification.

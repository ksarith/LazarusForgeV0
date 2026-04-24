# Lazarus Forge — v0 Operational Flow

This document defines the **minimal viable operational logic** of the Lazarus Forge.
It is not a claim of full automation. It is a falsifiable flow that can be executed
manually, semi-automatically, or automated later.

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

## High-Level Flow

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
- Contamination level
- Known failure modes

Classification may be **overridden by human operator**.

---

## 3. Decision Gates (Ordered, Mandatory)

### Gate A — Still Functional?
**Test:** Performs original or equivalent function  
**If YES →** Component Library  
**If NO →** Gate B

---

### Gate B — Repairable?
**Test:** Failure is localized, accessible, and within tooling capability  
**If YES →** Repair & Learn  
**If NO →** Gate C

---

### Gate C — Graceful Downgrade Possible?
**Test:** Can function at lower precision, tolerance, or duty cycle  
**If YES →** Repurpose as Lower-Precision Component  
**If NO →** Gate D

---

### Gate D — Truly Exhausted?
**Test:** Structural, chemical, or thermal damage prevents function  
**If YES →** Reduction  
**If NO →** Human/AI Oversight Gate


Human/AI Oversight Gate: Review items that failed Gates A–D but where reduction feels premature. Evaluate against active needs only — not hypothetical future uses. If a credible use case exists, assign it with a defined review date. If none, authorize reduction. If no genuine need exists, reduction proceeds without guilt. The gate prevents both hoarding ("maybe someday") and premature destruction.

---

## 4. Outcome Paths

### Component Library
- Catalog reusable parts
- Track provenance and test results
- Feeds Fabrication directly

---

### Repair & Learn
- Attempt repair
- Log failure mode and fix
- Update heuristics
- Outputs to Component Library or Repurpose

---

### Repurpose (Lower Precision)
- Assign to reduced-spec use cases
- Examples: jigs, fixtures, structural members
- Feeds Fabrication

---

### Reduction
**Irreversible step**
- Shredding, cutting, or milling
- Size reduction only (no melting yet)

---

### Purification
- Spin chamber or equivalent
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

Fabrication is driven by the needs of the Forge itself before external output. Priority order: (1) tools or components the Forge currently lacks, (2) infrastructure that expands Forge capability, (3) output for external use or exchange. A want becomes a need when its absence limits a higher-priority function.

Fabrication is **not terminal**.

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

---

## Termination Conditions

An item exits the system only when:
- It is in active use
- It is stored as stock
- It is reduced to inert waste after all prior gates fail

---

## Notes

This flow is intentionally conservative.
Irreversibility is delayed.
Human judgment is explicit.
Automation is optional, not assumed.
A want becomes a need when its absence limits a higher-priority function.

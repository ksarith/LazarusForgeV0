# Air Scrubber v0 — Environmental & Operator Safety Module

## Purpose

The Air Scrubber exists to **prevent harm** during Lazarus Forge operations.
It captures particulates, fumes, and off-gassing produced during
irreversible or abrasive processes.

This module is **infrastructure**, not innovation.

If the Air Scrubber is absent or non-functional, downstream operation is invalid.

---

## Design Philosophy

- Safety is non-negotiable
- Known methods are preferred over novel ones
- Inspection and maintenance must be simple
- Environmental controls are separate from material logic

The Air Scrubber does not increase material value.
It enables the system to operate responsibly.

---

## Position in System Flow

The Air Scrubber operates **in parallel** with:

- Reduction (cutting, shredding, milling)
- Stratification (solid-state triage)
- Melt-based refinement (Spin Chamber, purification)
- Fabrication and joining

It is not a gate, classifier, or decision system.

---

## Contaminants Addressed (v0 Scope)

- Particulates (metal dust, plastics, ceramics)
- Combustion byproducts
- Off-gassing from coatings, oils, adhesives
- Thermal decomposition fumes (limited)

The v0 system does **not** attempt to handle:
- Unknown chemical weapons
- Large-scale industrial emissions
- Continuous toxic gas production

---

## Core Subsystems (v0)

### 1. Intake & Ducting

- Localized capture near emission source
- Negative pressure preferred
- Avoids whole-room dilution strategies

---

### 2. Particulate Filtration

- Mechanical filters (coarse → fine stages)
- Replaceable and inspectable
- Designed to fail visibly, not silently

---

### 3. Wet or Adsorptive Stage (Optional)

- Water-based scrubbing OR
- Activated carbon / adsorption media

Selection depends on:
- Material mix
- Availability
- Maintenance capability

---

### 4. Exhaust / Vent

- Filtered exhaust routed safely
- No claims of zero-emission operation
- Compliance with local regulations assumed

---

## Operational Rules

- Air Scrubber must be active during:
  - Reduction
  - Any thermal process
  - Any unknown-material handling
- Scrubber status is logged
- Bypass operation is explicitly disallowed

---

## Maintenance & Inspection

- Filters are consumables
- Wet stages require periodic cleaning
- Adsorption media requires replacement

A neglected scrubber is considered a system failure.

---

## Metrics (Sanity Checks, Not Optimization)

- Visible dust escape (should be zero)
- Filter loading rate
- Operator exposure indicators
- Maintenance interval stability

No attempt is made to optimize efficiency beyond safety requirements.

---

## Explicit Non-Goals

- Novel air chemistry
- Energy recovery from exhaust
- Full industrial-scale compliance modeling
- Invisible or self-healing systems

---

## Notes

- This module exists to protect people and learning
- It is intentionally uninteresting
- Its success is measured by absence of incidents

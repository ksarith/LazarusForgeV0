## Purpose

The Material Separation Gate is a **pre-purification decision module** within the Lazarus Forge. Its goal is to **divert material away from energy-intensive melting and refinement** by recovering usable fractions earlier in the process.

It is not a smelter, refinery, or guarantee of purity.

Success is defined by *avoided processing*, not perfect separation.

---

## Revision Note

v0.2 — Renamed from `Stratification_Chamber_v0.md` to `Material_Separation_Gate_v0.md`. Name change reflects function over method — the gate separates material by mechanical means regardless of specific implementation. Additional revisions: RPM range reframed as exploration band, stratification emergent behavior note added, geometry correction clause added to sensor section, sensor degraded mode clause, magnetic bearing v0 proxy, Unknown Bulk loop closure, Bootstrap Proxy Mode, Contamination Risk statement, energy claim tightened to directional improvement. Core philosophy and performance metrics unchanged. `Spin_Chamber_v0.md` remains the downstream thermal/melting module; this gate is the upstream mechanical decision point.

---

## Position in System Flow

The Material Separation Gate operates **after Reduction** (cutting/shredding) and **before Purification**. It is the first physical decision point — material that passes here avoids the energy cost of the Spin Chamber entirely.

---

## Design Philosophy

- Preserve function before destroying structure
- Prefer classification over purification
- Allow explicit "unknown" and "fail" outputs — the system must always be able to say no
- Optimize for learning and tunability, not peak throughput
- Replicate gates to scale, do not over-enlarge
- Refusal of ambiguous material is a success condition, not a failure

---

## Inputs

- Reduced metallic feedstock (non-powdered)
- Mixed alloys, fasteners, coatings, or contamination allowed
- Known upstream envelope (particle size, mass range)

---

## Core Subsystems (v0)

### 1. Rotational Drum / Rotor

- Variable-speed rotor operating across tunable RPM bands
- v0 exploration band: **~1,000–5,000 RPM** [Estimated — to be empirically mapped per feedstock profile; system behavior depends heavily on fragment geometry, ductility, size distribution, and contamination]
- Stepped-diameter drum geometry encourages stratification by density and inertia

**Stratification Logic:**
- **Outer Rim** — High-density metallic fragments (iron, nickel, dense alloys)
- **Mid-Tier** — Silicates, mixed oxides, intermediate-density materials
- **Inner Core** — Low-density polymers, organics, light composites

*Note: Separation is influenced not only by density, but also by geometry, surface area, ductility, and aerodynamic drag. Stratification bands represent emergent behavior, not strict material classes. All band assignments are treated as probabilistic heuristics, not deterministic rules. Thin steel vs. thick aluminum can invert expected radial positions — do not treat band assignments as guarantees.*

---

### 2. Friction & Thermal Management

[Friction Blindness Check — addressed explicitly]

- Preferred: Passive magnetic or low-contact bearings to reduce wear
- v0 Proxy: Conventional bearings with monitored wear and vibration tracking
- Air and fluid drag at operating RPM generates measurable heat — not ignored
- Heat generated is routed via heat pipe to the Support Raft's thermal sink where available, or dissipated locally in terrestrial configurations
- Bearing wear rate is a primary maintenance metric and scaling trigger

---

### 3. Sensor Cross-Check

- Onboard density measurement and spectroscopy provide dual-channel material identification
- Cross-check reduces false classification from single-sensor error
- Confidence scoring is required before any fraction is routed to a downstream path
- Sensors must cross-reference inertia with optical geometry to ensure light-but-dense materials are not prematurely diverted to the polymer stream. Example: aluminum foil can exhibit drag behavior similar to low-density polymer — geometry correction prevents silent misclassification into the wrong recovery stream

**Degraded Mode:**
If one sensing channel fails or drifts out of calibration, the chamber may operate in single-sensor mode with elevated confidence thresholds and increased routing to Unknown Bulk. Degraded mode does not suspend operation — it tightens refusal criteria.

---

### 4. Fail-to-Bin Protocol

In accordance with the refusal-first ethos of the Forge and `Auditor_Protocols.md`:

- If sensor cross-check confidence is **< 90%**, material is ejected to the **Unknown Bulk** bin
- Unknown Bulk is not discarded — it is logged, held, and routed to `Component_Triage_System.md` or Synthesizer review at next available cycle
- Unknown Bulk that remains unresolved after triage may be reprocessed through reduction with adjusted parameters, or routed to Class C for controlled thermal processing
- Attempting to process unknown material risks furnace contamination and downstream cascade failures
- Refusal is a first-class output, not a system fault

---

### 5. Optional Field Bias (Deferred)

- Magnetic or electromagnetic biasing may be added in later versions
- Not required for v0 validation
- Must never force separation beyond observable stability

---

### 6. Collection Zones

- Radial or axial bins aligned to stratification bands
- Capture fractions that stabilize under rotation
- Geometry favors repeatable, low-chaos trajectories

---

## Outputs

- **Class A:** Usable components or near-components — prioritize fasteners, simple shapes, and identifiable geometry before bulk metal recovery. Preserve function before destroying structure
- **Class B:** Downgraded material (repurpose / lower-precision use)
- **Class C:** Mixed bulk → Spin Chamber for thermal processing
- **Unknown Bulk:** Ambiguous or low-confidence material → Component_Triage_System review → reduction retry or Class C routing
- **Fail:** Unclassifiable after review → Reduction or discard

---

## Contamination Risk

Incorrect classification at this stage can introduce contaminants into thermal systems downstream, resulting in alloy degradation, slag instability, equipment fouling, and increased energy cost. The gate is therefore biased toward refusal over misclassification. The <90% confidence threshold exists to protect the Spin Chamber and everything downstream from decisions made under uncertainty.

---

## Energy Position

[Energy Density Paradox Check]

The primary energy value of this gate is derived from **avoided thermal processing**. Sorted metal recovery via mechanical separation is energy-positive relative to processing the same material through the Spin Chamber. Polymer diversion is currently energy-neutral but justified as a lifecycle necessity — preventing microplastic contamination downstream and in marine Leviathan contexts.

Quantitative energy reduction is expected but not required for v0 validation. Directional improvement is sufficient. Specific reduction estimates are deferred to experimental baseline against `energy_v0.md` kWh/kg metric.

[Logged as Non-blocking Unknown — see Unknowns Registry]

---

## Bootstrap Proxy Mode

The Material Separation Gate may be approximated in early Forge implementations using:

- Inclined vibrating tables or gravity sorting rigs
- Magnetic separation for ferrous bias
- Manual classification assisted by simple jigs

These proxies do not replicate full centrifugal behavior but allow early-stage material diversion and learning. The goal is not equivalence, but preservation of the decision loop. An imperfect gate that runs is more valuable than a perfect one that doesn't exist yet.

---

## Scaling Strategy

- Multiple small gates are preferred over single large units
- Scaling occurs by replication, not enlargement
- Gates may be tuned for specific material classes

Scaling triggers include:
- Input backlog exceeding dwell capacity
- Wear rate exceeding maintenance window
- Declining classification confidence
- Unknown Bulk accumulation rate exceeding review capacity

---

## Falsifiable Performance Metric (Primary)

**Material Diversion Rate**

Target for v0 exploration (not a guarantee):
- ≥ 30% diversion indicates viability
- < 10% indicates redesign or removal

**Secondary metric:**
- **Unknown Bulk Rate** — proportion of intake routed to Unknown Bulk bin. High rates indicate sensor calibration issues or upstream reduction inconsistency, not gate failure. Rising Unknown Bulk rate is diagnostic signal, not system fault.

---

## Lifecycle & Failure Modes

[Lifecycle Truncation Check — addressed]

**Degraded Operation** — At reduced RPM or single-sensor operation, classification confidence thresholds tighten automatically. Gate continues at lower throughput rather than passing ambiguous material downstream.

**Failure Modes & Detection** — Bearing wear presents as vibration signature changes before catastrophic failure. Spectroscopy drift presents as rising Unknown Bulk rate. Both are detectable before failure if monitored.

**Maintenance Access** — Bearing replacement and collection zone clearing are primary service tasks. Modular drum design allows hot-swap in swarm configurations.

**End-of-Life / Recycling Path** — Gate components are themselves candidates for Forge intake. Magnetic bearing assemblies are Class A salvage priority.

---

## Unknowns Registry

**Non-blocking:**
- Quantitative energy reduction estimate requires experimental baseline against `energy_v0.md`. Resolution path: Leviathan test cycle data or terrestrial pilot run
- Optimal RPM exploration bands for mixed municipal vs. industrial scrap profiles not yet characterized. Resolution path: incremental RPM sweep during v0 testing
- Confidence threshold calibration (< 90% rule) requires empirical validation against known feedstock samples. Resolution path: controlled classification trials
- Geometry correction algorithm for inertia/optical cross-reference not yet specified. Resolution path: analog centrifuge separation literature review, then prototype sensor calibration

**Exploratory:**
- Long-term aquatic bio-fouling impact on rotor balance and bearing performance in Leviathan deployments. Route to `leviathan_testing.md`
- Electromagnetic field bias integration for later versions. Route to `Trajectories_LF.md`

---

## Explicit Non-Goals (v0)

- Achieving high-purity metal output
- Replacing smelting or electrorefining
- Handling powdered feedstock
- Solving all alloy separation problems

---

## Integration Hooks

- `Spin_Chamber_v0.md` — receives Class C bulk output; this gate reduces its thermal load
- `Component_Triage_System.md` — receives Unknown Bulk for human or assisted review
- `Air_Scrubber_v0.md` — receives exhaust from high-RPM operation
- `energy_v0.md` — energy reduction claims require cross-validation
- `leviathan_testing.md` — aquatic deployment unknowns routed here
- `Support_Raft_v0.md` — thermal sink for heat pipe output in marine configurations

---

## Notes

- The Material Separation Gate is a *decision amplifier*, not a solution by itself
- Its value increases as upstream reduction and downstream logic improve
- Honest failure improves system learning
- Unknown Bulk accumulation is diagnostic signal, not waste
- Final versions often aren't final
- You didn't design a separator. You designed a refusal engine that protects the rest of the Forge from bad decisions.

---

Ready for the repo. The reference sweep needed across other files:

- `Discovery.md` — update file name, summary, and reading order entry
- `Lazarus_forge_v0_flow.md` — update any reference to Stratification Chamber
- `Air_Scrubber_v0.md` — Integration Hooks section references this file
- `Spin_Chamber_v0.md` — likely references Stratification Chamber as upstream module
- `Auditor_Protocols.md` — no direct reference but Discovery.md update covers it
- `Astroid-miner` repo — check for any cross-repo references

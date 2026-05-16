# Material Separation Gate (v0)

> ⚠️ **Operational Safety Advisory**
> The Material Separation Gate operates a high-RPM rotating drum
> with mixed, unknown-geometry feedstock. Fragment ejection,
> rotor imbalance, and bearing failure are credible failure modes
> at operating speeds of 1,000–5,000 RPM. The drum enclosure is
> designed as a closed system — the operating area must remain
> clear of personnel and sensitive components during all rotating
> states. Enclosure integrity is a design requirement, not an
> optional feature. Siting and clearance requirements are not yet
> governed by a facility or area-of-operation document — see GK-006.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Forge_Audit_Kit.md                                                  |
| Last Audit       | 2026-05-15                                                          |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 6                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Design intent and operating philosophy of the Material
  Separation Gate
- Physical subsystem descriptions for v0 (rotor, sensors,
  collection zones, fail-to-bin protocol)
- RPM exploration band and stratification behavior at v0 scale
- Sensor cross-check architecture and confidence scoring logic
- Fail-to-bin protocol and Unknown Bulk handling
- Output classification system (Class A, B, C, Unknown Bulk, Fail)
- Falsifiable performance metrics (Material Diversion Rate,
  Unknown Bulk Rate)
- Scaling strategy and replication doctrine
- Bootstrap Proxy Mode for early Forge implementations
- Lifecycle, failure modes, and degraded operation behavior
- Integration hooks to downstream and upstream modules
- Contamination risk statement and refusal-first design rationale

**This file DOES NOT define:**
- Upstream feedstock reduction or shredding
  (Reduction module — not yet assigned)
- Thermal processing of Class C output
  (Spin_Chamber_v0.md)
- Component triage and human review of Unknown Bulk
  (Component_Triage_System.md)
- Air handling and exhaust management from high-RPM operation
  (Air_Scrubber_v0.md)
- Energy accounting and kWh/kg metrics
  (energy_v0.md)
- Marine thermal sink integration beyond integration hook
  (Support_Raft_v0.md)
- Aquatic biofouling impact on rotor and bearing performance
  (leviathan_testing.md)
- Electromagnetic field bias for future versions
  (deferred — Trajectories_LF.md)
- Facility siting, clearance, and area-of-operation requirements
  (GK-006 — no file exists yet)
- Detailed sensor specifications or spectroscopy hardware
  (not yet assigned)
- Powder feedstock handling
  (explicit non-goal — out of scope for all versions until
  stated otherwise)

---

## File Purpose

The Material Separation Gate is the upstream mechanical decision
point within the Purification stage of the Lazarus Forge
operational flow. Operating after feedstock reduction and before
thermal processing, it uses mechanical separation to divert
usable material away from the energy-intensive Spin Chamber
where possible. Its primary value is avoided processing — every
kilogram diverted here is a kilogram that does not consume Spin
Chamber energy and time.

The gate is designed around a refusal-first philosophy: when
material cannot be classified with sufficient confidence, it is
held for review rather than passed downstream. Incorrect
classification at this stage contaminates thermal systems,
degrades alloy consistency, and increases energy cost across
the entire Forge. The gate protects everything downstream from
decisions made under uncertainty.

The gate is not a purifier, a smelter, or a guarantee of
separation quality. It is a decision amplifier — its value
grows as upstream reduction and downstream logic improve. If
this file disappeared, the Forge would lose its primary
mechanical diversion stage and route all feedstock directly
to thermal processing, significantly increasing energy
consumption and contamination risk.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Reduced feedstock arrives with a known upstream envelope — particle size and mass range are characterized before reaching the gate | Inputs section — stated but not defined | Medium | Upstream reduction module defines and tracks output envelope |
| ASM-002 | Dual-channel sensor cross-check technology (density measurement and spectroscopy) is available at bootstrap through purchase, salvage, or inter-forge trade | Sensor section; purchase-what-cannot-be-produced doctrine | Low | Sensor procurement confirmed or bootstrap proxy validated |
| ASM-003 | 90% confidence threshold is the correct refusal criterion for routing decisions | Fail-to-bin protocol — stated as rule, not yet validated | Low | Controlled classification trials against known feedstock confirm or revise threshold |
| ASM-004 | v0 operating environment is terrestrial | No marine provisions in v0 spec; Leviathan deferred | Medium | Marine or off-world deployment enters scope |
| ASM-005 | Manual operator or Component Triage System capacity exists to process Unknown Bulk output without backlog | Fail-to-bin routes to review — assumes review capacity | Medium | Unknown Bulk accumulation rate exceeds review capacity — scaling trigger activates |
| ASM-006 | Replication is preferable to enlargement for scaling — multiple small gates are assumed to behave better than a single large one at v0 scale | Scaling doctrine; failure mode distribution logic | Medium | Replication produces coordination problems, resource contention, or interference between units that enlargement would not — or replication pressure forces component evolution that changes the preferred architecture |
| ASM-007 | Mechanical separation is energy-positive relative to thermal processing for the same diverted material — the gate saves more energy than it consumes | Energy Position section; directional improvement assumed | Low | Quantitative energy baseline established against energy_v0.md — directional assumption confirmed or revised |

*Low confidence assumptions reflect unvalidated operational parameters
and sensor procurement uncertainty. ASM-003 and ASM-007 are the most
load-bearing — the confidence threshold governs every routing decision
and the energy-positive claim is the gate's core economic justification.
Both require experimental validation before the gate can be promoted
beyond Exploration. Purchase-what-cannot-be-produced doctrine applies
to ASM-002. See README.md and Trajectories_LF.md for forge ecology context.*

---

## Purpose

The Material Separation Gate is a **pre-purification decision module**
within the Lazarus Forge. Its goal is to **divert material away from
energy-intensive melting and refinement** by recovering usable fractions
earlier in the process.

It is not a smelter, refinery, or guarantee of purity.

Success is defined by *avoided processing*, not perfect separation.

---

## Position in System Flow

The Material Separation Gate operates **after Reduction** and **before
Purification** within the Lazarus Forge operational flow
(Lazarus_forge_v0_flow.md). It is the upstream mechanical decision
point — material that passes here avoids the energy cost of the Spin
Chamber entirely.

---

## Design Philosophy

- Preserve function before destroying structure
- Prefer classification over purification
- Allow explicit "unknown" and "fail" outputs — the system must
  always be able to say no
- Optimize for learning and tunability, not peak throughput
- Replicate gates to scale, do not over-enlarge
- Refusal of ambiguous material is a success condition, not a failure

---

## Inputs

- Reduced metallic feedstock (non-powdered)
- Mixed alloys, fasteners, coatings, or contamination allowed
- Known upstream envelope (particle size, mass range) — see ASM-001

---

## Core Subsystems (v0)

### 1. Rotational Drum / Rotor

- Variable-speed rotor operating across tunable RPM bands
- v0 exploration band: **~1,000–5,000 RPM** *(Analogous — derived
  from centrifugal separator and rotary classifier equipment at
  similar scale; requires empirical mapping per feedstock profile.
  System behavior depends heavily on fragment geometry, ductility,
  size distribution, and contamination. Do not treat as validated
  operating parameters.)*
- Stepped-diameter drum geometry encourages stratification by
  density and inertia

**Stratification Logic:**
- **Outer Rim** — High-density metallic fragments (iron, nickel,
  dense alloys)
- **Mid-Tier** — Silicates, mixed oxides, intermediate-density
  materials
- **Inner Core** — Low-density polymers, organics, light composites

Band position assignments are *(Analogous — inferred from
centrifugal separation literature and density differential
principles. Empirical validation required per feedstock class
before treating as reliable routing heuristics.)*

*Note: Separation is influenced not only by density, but also by
geometry, surface area, ductility, and aerodynamic drag.
Stratification bands represent emergent behavior, not strict
material classes. All band assignments are treated as probabilistic
heuristics, not deterministic rules. Thin steel vs. thick aluminum
can invert expected radial positions — do not treat band assignments
as guarantees.*

---

### 2. Friction & Thermal Management

- Preferred: Passive magnetic or low-contact bearings to reduce wear
- v0 Proxy: Conventional bearings with monitored wear and vibration
  tracking
- Air and fluid drag at operating RPM generates measurable heat —
  not ignored
- Heat generated is routed via heat pipe to the Support Raft's
  thermal sink where available, or dissipated locally in terrestrial
  configurations
- Bearing wear rate is a primary maintenance metric and scaling
  trigger
- Component standardization required — bearing sizes, shaft
  diameters, and fastener standards must be drawn from a minimal
  shared set to support inter-forge interchangeability and repair.
  A bearing that can be sourced, replaced, or traded between forges
  is worth more than an optimal but bespoke one.

---

### 3. Sensor Cross-Check

- Onboard density measurement and spectroscopy provide dual-channel
  material identification
- Cross-check reduces false classification from single-sensor error
- Confidence scoring is required before any fraction is routed to
  a downstream path
- Sensors must cross-reference inertia with optical geometry to
  ensure light-but-dense materials are not prematurely diverted to
  the polymer stream. Example: aluminum foil can exhibit drag
  behavior similar to low-density polymer — geometry correction
  *(Placeholder — correction algorithm not yet specified; see GK-004)*
  prevents silent misclassification into the wrong recovery stream

**Degraded Mode:**
If one sensing channel fails or drifts out of calibration, the
chamber may operate in single-sensor mode with elevated confidence
thresholds and increased routing to Unknown Bulk. Degraded mode
does not suspend operation — it tightens refusal criteria.

---

### 4. Fail-to-Bin Protocol

In accordance with the refusal-first ethos of the Forge and
Auditor_Protocols.md:

- If sensor cross-check confidence is **< 90%** *(Placeholder —
  threshold not yet validated against known feedstock samples;
  see GK-003)*, material is ejected to the **Unknown Bulk** bin
- Unknown Bulk is not discarded — it is logged, held, and routed
  to Component_Triage_System.md or Synthesizer review at next
  available cycle
- Unknown Bulk that remains unresolved after triage may be
  reprocessed through reduction with adjusted parameters, or
  routed to Class C for controlled thermal processing
- Attempting to process unknown material risks furnace
  contamination and downstream cascade failures
- Refusal is a first-class output, not a system fault

---

### 5. Optional Field Bias (Deferred)

- Magnetic or electromagnetic biasing may be added in later versions
- Not required for v0 validation
- Must never force separation beyond observable stability
- Deferred to Trajectories_LF.md

---

### 6. Collection Zones

- Radial or axial bins aligned to stratification bands
- Capture fractions that stabilize under rotation
- Geometry favors repeatable, low-chaos trajectories

---

## Outputs

- **Class A:** Usable components or near-components — prioritize
  fasteners, simple shapes, and identifiable geometry before bulk
  metal recovery. Preserve function before destroying structure
- **Class B:** Downgraded material (repurpose / lower-precision use)
- **Class C:** Mixed bulk → Spin Chamber for thermal processing
- **Unknown Bulk:** Ambiguous or low-confidence material →
  Component_Triage_System review → reduction retry or Class C routing
- **Fail:** Unclassifiable after review → Reduction or discard

---

## Contamination Risk

Incorrect classification at this stage can introduce contaminants
into thermal systems downstream, resulting in alloy degradation,
slag instability, equipment fouling, and increased energy cost.
The gate is therefore biased toward refusal over misclassification.
The <90% confidence threshold exists to protect the Spin Chamber
and everything downstream from decisions made under uncertainty.

---

## Energy Position

The primary energy value of this gate is derived from **avoided
thermal processing**. Sorted metal recovery via mechanical
separation is energy-positive relative to processing the same
material through the Spin Chamber *(Placeholder — directional
improvement expected but not yet quantified against energy_v0.md
baseline)*. Polymer diversion is currently energy-neutral
*(Placeholder — lifecycle justification is contamination
prevention, not energy recovery)*.

Quantitative energy reduction is expected but not required for
v0 validation. Directional improvement is sufficient. Specific
reduction estimates are deferred to experimental baseline against
energy_v0.md kWh/kg metric.

---

## Bootstrap Proxy Mode

The Material Separation Gate may be approximated in early Forge
implementations using:

- Inclined vibrating tables or gravity sorting rigs
- Magnetic separation for ferrous bias
- Manual classification assisted by simple jigs

These proxies do not replicate full centrifugal behavior but allow
early-stage material diversion and learning. The goal is not
equivalence, but preservation of the decision loop. An imperfect
gate that runs is more valuable than a perfect one that doesn't
exist yet.

---

## Scaling Strategy

- Multiple small gates are preferred over single large units
- Scaling occurs by replication, not enlargement — see ASM-006
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
- ≥ 30% diversion indicates viability *(Placeholder — target
  derived from design intent, not operational data)*
- < 10% indicates redesign or removal *(Placeholder)*

**Secondary metric:**
- **Unknown Bulk Rate** — proportion of intake routed to Unknown
  Bulk bin. High rates indicate sensor calibration issues or
  upstream reduction inconsistency, not gate failure. Rising
  Unknown Bulk rate is diagnostic signal, not system fault.

---

## Lifecycle & Failure Modes

**Degraded Operation** — At reduced RPM or single-sensor operation,
classification confidence thresholds tighten automatically. Gate
continues at lower throughput rather than passing ambiguous material
downstream.

**Failure Modes & Detection** — Bearing wear presents as vibration
signature changes before catastrophic failure. Spectroscopy drift
presents as rising Unknown Bulk rate. Both are detectable before
failure if monitored.

**Maintenance Access** — Bearing replacement and collection zone
clearing are primary service tasks. Modular drum design allows
hot-swap in swarm configurations.

**End-of-Life / Recycling Path** — Gate components are themselves
candidates for Forge intake. Magnetic bearing assemblies are
Class A salvage priority.

---

## Explicit Non-Goals (v0)

- Achieving high-purity metal output
- Replacing smelting or electrorefining
- Handling powdered feedstock
- Solving all alloy separation problems

---

## Integration Hooks

- Lazarus_forge_v0_flow.md — governing operational flow; gate
  operates within Purification stage
- Spin_Chamber_v0.md — receives Class C bulk output; this gate
  reduces its thermal load
- Component_Triage_System.md — receives Unknown Bulk for human
  or assisted review
- Air_Scrubber_v0.md — receives exhaust from high-RPM operation
- energy_v0.md — energy reduction claims require cross-validation
- leviathan_testing.md — aquatic deployment unknowns routed here
- Support_Raft_v0.md — thermal sink for heat pipe output in
  marine configurations

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | File operated under name Stratification_Chamber_v0.md | Name implied a specific physical method (stratification) rather than the function being performed (mechanical separation decision) | Renamed to Material_Separation_Gate_v0.md. Name change reflects function over method — the gate separates material by mechanical means regardless of specific implementation. Stale references to Stratification_Chamber_v0.md in other files should be updated; see cross-reference list at bottom of original document | Analogous | No — rename is complete; cross-references require sweep |
| 2026-05-15 | Audit Review | RPM range framed as defined operating band | Implied false precision — actual behavior depends heavily on feedstock geometry, ductility, and contamination | RPM range reframed as exploration band. Stratification noted as emergent behavior, not deterministic output. Band assignments treated as probabilistic heuristics | Analogous | Yes — empirical RPM sweep during v0 testing |
| 2026-05-15 | Audit Review | Unknown Bulk treated as failure output | Created pressure to minimize Unknown Bulk routing, risking downstream contamination | Unknown Bulk loop closure added — unresolved Unknown Bulk routes to Component_Triage_System.md or reduction retry. Unknown Bulk accumulation is diagnostic signal, not system fault | Analogous | No |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts are currently active. Design tensions
exist (optimal confidence threshold, replication vs. enlargement
scaling, sensor technology selection) but all are deferred pending
operational data. Tracked as unknowns in sidecar, not disputes.
Revisit after first operational run.*

---

## Auditor Notes & Unknowns

### GK-001 — Quantitative energy reduction estimate not established

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-05-15                                       |

**Description:** Quantitative energy reduction from mechanical
separation vs. thermal processing has not been established.
Directional improvement is assumed but not measured.

**Why It Matters:** The gate's core economic justification is
avoided thermal processing. Without a quantitative baseline,
the energy-positive claim cannot be verified or falsified.

**Resolution Path:**
- Deferred to experimental baseline against energy_v0.md
  kWh/kg metric.
- Resolution requires Leviathan test cycle data or terrestrial
  pilot run with instrumented energy measurement.
- Payment via Specification — once baseline established, move
  quantified claim to Body as Measured.

---

### GK-002 — Optimal RPM exploration bands not characterized per feedstock

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-05-15                                       |

**Description:** Optimal RPM bands for mixed municipal vs.
industrial scrap profiles have not been characterized. The
1,000–5,000 RPM exploration band is Analogous, not validated.

**Why It Matters:** RPM band selection directly governs
stratification behavior. An incorrect band produces poor
separation and elevated Unknown Bulk rates without revealing
the cause. Feedstock variation means a single RPM band may
not be optimal across all input classes.

**Resolution Path:**
- Incremental RPM sweep during v0 testing against known
  feedstock samples.
- Map separation quality vs. RPM for at least three distinct
  feedstock classes (ferrous, aluminum-class, mixed).
- Payment via Specification — once optimal bands per feedstock
  class are characterized, move to Body as Measured.

---

### GK-003 — Confidence threshold calibration not empirically validated

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-05-15                                       |

**Description:** The 90% confidence threshold for Unknown Bulk
routing has not been validated against known feedstock samples.
The threshold is a design intent value, not an empirically
derived one.

**Why It Matters:** The confidence threshold governs every
routing decision the gate makes. A threshold set too high
floods Unknown Bulk with recoverable material. A threshold
set too low passes ambiguous material downstream, risking
contamination. This is the most operationally sensitive
parameter in the gate.

**Resolution Path:**
- Controlled classification trials against known feedstock
  samples with ground-truth composition data.
- Sweep threshold from 70% to 95% and measure false
  positive and false negative rates at each level.
- Select threshold that minimizes downstream contamination
  risk while maintaining acceptable Unknown Bulk rate.
- Payment via Specification — once empirically validated,
  move confirmed threshold to Body as Measured.

---

### GK-004 — Geometry correction algorithm not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-05-15                                       |

**Description:** The inertia/optical cross-reference algorithm
for geometry correction — preventing misclassification of
light-but-dense or heavy-but-thin materials — is not yet
specified. The need is identified but the implementation
is undefined.

**Why It Matters:** Without geometry correction, materials
like aluminum foil can be silently routed to the polymer
stream. This is a known failure mode that the sensor
cross-check is supposed to prevent — but cannot prevent
without a specified algorithm.

**Resolution Path:**
- Analog centrifuge separation literature review to identify
  existing correction approaches.
- Prototype sensor calibration trials with known edge-case
  materials (aluminum foil, thin steel sheet, dense polymer).
- Algorithm specification is a prerequisite for sensor
  cross-check to function as designed.
- Payment via Specification — once algorithm is specified
  and validated, move to Body as Measured.

---

### GK-005 — Long-term aquatic biofouling impact on rotor balance

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md                   |
| First Logged  | 2026-05-15 (migrated from prose registry)        |
| Last Reviewed | 2026-05-15                                       |

**Description:** Long-term aquatic biofouling impact on rotor
balance and bearing performance in Leviathan deployments has
not been characterized.

**Why It Matters:** Biofouling creates asymmetric mass
accumulation on rotating components — a direct imbalance
source at operating RPM. In marine deployments this could
progressively degrade separation quality and accelerate
bearing failure without obvious external symptoms.

**Resolution Path:**
- Discharge via Trajectory — route to leviathan_testing.md
  for marine deployment test framework.
- Not relevant to terrestrial v0 validation.

---

### GK-006 — Operational siting and area-of-operation requirements not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Ethical                              |
| Blocking      | No                                               |
| Owner         | Material_Separation_Gate_v0.md (seed entry)      |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** No facility, siting, or area-of-operation
document exists to govern physical separation requirements,
clearance zones, or operator safety protocols during
high-RPM rotating states.

**Why It Matters:** The gate operates at 1,000–5,000 RPM
with unknown-geometry feedstock. Fragment ejection and
rotor failure are credible hazards. The safety advisory
states the enclosure requirement but no governing document
defines clearance distances, enclosure specifications, or
operator protocols.

**Resolution Path:**
- Seed entry for future master safety registry — mirrors
  SC-006 in Spin_Chamber_v0.md.
- Not blocking v0 specification work but must be resolved
  before any operational run.
- Recommend escalating to cross-module UNK entry in
  Unknowns_LF.md alongside SC-006 — siting requirements
  affect all rotating and thermal modules in the Forge.
- Discharge via Trajectory for marine and off-world variants.
- Payment via Specification for terrestrial v0 baseline
  once siting document exists.

---

### Resolution Log

- 2026-05-15: GK-001 through GK-005 — Migrated from prose
  Unknowns Registry to structured sidecar format. Content
  preserved; format updated to template standard.
- 2026-05-15: GK-006 — New entry. Siting and safety
  requirements gap identified during retrofit audit.
  Mirrors SC-006 in Spin_Chamber_v0.md. Recommend
  cross-module UNK escalation.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | File named Stratification_Chamber_v0.md | Name implied a specific physical method rather than the function being performed. Caused semantic confusion about what the module owned and how it related to the Spin Chamber | No — rename to Material_Separation_Gate_v0.md is permanent |
| 2026-05-15 | Electromagnetic field bias in v0 spec | Adds complexity without validated benefit at v0 scale and power budget. Correctly deferred — must never force separation beyond observable stability | Reconsider at v1+ when power budget and field geometry can be specified |
| 2026-05-15 | Single large gate as scaling strategy | Enlargement creates single point of failure, increases maintenance burden, and reduces tunability per feedstock class. Replication preserves modularity and forces component standardization | Reconsider if replication produces coordination or interference problems at swarm scale — see ASM-006 |
| 2026-05-15 | Powder feedstock handling | Requires fundamentally different separation physics — aerodynamic and electrostatic rather than centrifugal and inertial. Out of scope for all v0 rotating drum implementations | Reconsider only as a distinct module, never as an extension of this gate |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of this file.
All canonical drift indicators from File_Template.md apply.
The following are additional local triggers specific to the
Material Separation Gate:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| GK-003 remains unreviewed after first operational run | Confidence threshold governs every routing decision — operational data must feed back immediately |
| RPM band revised without GK-002 resolution | Empirical RPM mapping is prerequisite for any band change |
| Bearing or rotor specified with non-standard components without documented justification | Standardization doctrine applies — bespoke components require explicit override |
| Safety Advisory conditions change without GK-006 update | Enclosure requirements and advisory must stay synchronized |
| Unknown Bulk rate rises without sensor calibration review | Rising Unknown Bulk is diagnostic signal — must trigger GK-003 and GK-004 review before operational changes |
| Feedstock class expands beyond non-powdered reduced metallic without assumptions review | ASM-001 expiry trigger — particle envelope, RPM bands, and sensor calibration all change with feedstock class |
| Replication scaling abandoned in favor of enlargement without ASM-006 review | Core scaling doctrine — override requires explicit audit and documented justification |
| Geometry correction algorithm advanced without GK-004 resolution | Sensor cross-check cannot function as designed without specified algorithm |

### Canonical Drift Triggers

*All mandatory re-audit conditions from File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*

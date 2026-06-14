# Living_Waters.md
*Tests/Living_Waters.md*

---

## File State

| Field | Value |
|---|---|
| Version | v0.3 |
| Status | Active — Experimental |
| Folder | Tests/ |
| Last Updated | 2026-06-14 |
| Authors | James (Owner), Claude (Synthesizer), Gemini (Auditor), ChatGPT (Synthesizer), Grok (Synthesizer) |
| Depends On | Energy.md, Safety_Protocols.md, Unknowns.md, Economics.md |
| Feeds Into | Operations/ (pending validation) |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Purpose

The Living Waters Initiative explores methods of producing potable and process water from contaminated, saline, atmospheric, or waste streams.

This file lives in Tests/ because neither primary pathway has been validated at Forge scale. Assumptions are not permitted to harden into doctrine until experimental data supports promotion to Operations/.

The initiative investigates pressure-driven, thermal, biological, and electrochemical separation approaches while preserving compatibility with Forge philosophy:

- Salvage-first.
- Energy-aware.
- Scalable from household to distributed network operation.
- Resilient under degraded conditions.
- Favoring repairability over consumable dependence.

**Declared Trajectory:** Living Waters is intended to evolve into the hydrological counterpart to Energy.md — eventually covering purification, storage, atmospheric harvesting, wastewater recycling, mineral recovery, biological treatment, and closed-loop water architecture. This file is the seed of that scope, not its ceiling.

**Sequencing Doctrine:** Purification precedes moisture farming. Atmospheric harvesting brings in variable-quality input streams — microplastics, industrial residues, biological aerosols. A validated purification baseline must exist before atmospheric yields can be safely processed. Moisture farming is supplemental until that baseline is established.

---

## Governing Principle

Water purification is fundamentally the separation of water molecules from everything else.

The Forge recognizes four major separation mechanisms:

| Mechanism | Separation Driver |
|---|---|
| Thermal | Boiling and condensation |
| Pressure | Vacuum or membrane gradients |
| Phase Change | Freezing, evaporation, sublimation |
| Chemical / Biological | Adsorption, ion exchange, metabolism |

**Unifying Observation:** LW-001 and LW-003 share a common underlying principle — changing pressure changes the phase behavior of water. This suggests a broader category: **Pressure-Driven Water Separation**. Nature provides atmospheric pressure, vacuum, and hydrostatic pressure. Civilization normally adds pumps to create pressure differentials. Living Waters investigates whether naturally occurring pressure environments can substitute for mechanical complexity.

---

## Water Hierarchy

The Forge recognizes that not all water requires drinking quality. Producing unnecessarily pure water for low-grade uses is avoidable energy expenditure. Quality requirements must match intended use.

| Tier | Use | Purity Requirement |
|---|---|---|
| 1 | Potable / drinking | Highest — pathogen and contaminant free |
| 2 | Food preparation | High |
| 3 | Hygiene | Moderate |
| 4 | Process water | Application-dependent |
| 5 | Cooling water | Low — scaling and corrosion control only |
| 6 | Irrigation | Low — pathogen aware |
| 7 | Non-contact utility | Minimal |

This hierarchy parallels the degraded modes logic in Energy.md. Purification effort scales to use. Potable-grade production is reserved for potable-grade need.

---

## Site Context

**The answer for different Forges will naturally vary. Location is the key determination.**

Pathway selection is site-conditioned, not universal. A Forge that knows where it is can focus experimental resources on viable pathways and flag inapplicable ones without wasting test cycles.

| Site Condition | Favored Pathways | Notes |
|---|---|---|
| Coastal / ocean access | LW-003 (DSRO), LW-001 | Primary candidates. Depth and seawater availability. |
| Inland / surface water | LW-001, LW-004, LW-006 | Contaminated rivers, aquifers, industrial runoff. |
| Arid / desert | LW-005 accelerated, LW-001 | Moisture farming pressure higher; purification baseline still first. |
| Arctic / cold climate | LW-004 competitive as primary | Freeze separation viable where energy is scarce and cold is abundant. |
| High waste-heat availability | LW-006, LW-008 | Membrane distillation and multi-effect distillation benefit directly. |
| Dense salvage environment | LW-001 | Refrigeration compressors, condensers, pressure vessels most recoverable. |

**Site Characterization Inputs (pre-pathway selection):**
- Proximity to ocean, surface water, or groundwater.
- Climate zone and seasonal variation.
- Elevation and atmospheric pressure baseline.
- Salvage availability and component inventory.
- Energy profile (see Energy.md).
- Known contaminant classes in local water sources.

*A formal Site Characterization → Pathway Selection decision framework is a declared future addition to this file.*

---

## Experimental Pathways

### LW-001 — Vacuum Distillation

**Concept**

Reducing chamber pressure lowers water's boiling point. At sufficiently low pressure, evaporation occurs at ambient temperatures. The resulting vapor is condensed into purified water, leaving dissolved solids and most contaminants behind.

**Advantages**
- Removes salts and heavy metals.
- Compatible with low-grade or waste heat.
- Works with seawater and heavily contaminated sources.
- Tolerant of salvaged components.
- No chemical inputs required.

**Challenges**
- Vacuum pump durability under sustained operation.
- Seal integrity — micro-leak accumulation degrades vacuum depth over time.
- **Volatile co-distillation [CRITICAL]:** Low-boiling organics (fuels, solvents, benzene, ethanol, gasoline fractions, some biological metabolites) will co-distill with or ahead of water vapor under vacuum. In salvage-context sources where input stream composition is unpredictable, initial distillate may be a concentrated toxin stream, not potable water. Fractional staging is required. See LW-UNK-001 and LW-TEST-102.
- **Energy cost [CRITICAL]:** Without latent heat recycling, vacuum distillation consumes approximately 628 kWh/m³ — the full latent heat of vaporization. This is unviable for the Forge energy budget. Heat recycling is not optional; it is a design requirement. See LW-UNK-005 and LW-TEST-101.
- Scaling behavior unknown.

**Energy Profile**

| Configuration | Specific Energy Consumption |
|---|---|
| No heat recycling | ~628 kWh/m³ — **unviable** |
| With Mechanical Vapor Recompression (MVR) or Multi-Effect Design | 10–25 kWh/m³ |
| Surface RO baseline (industrial, with energy recovery) | 2.5–4.0 kWh/m³ |
| Surface RO (salvaged pump, no energy recovery) | 8–12 kWh/m³ |

LW-001 with MVR is less efficient than industrial RO but may be more achievable from salvage. The energy gap narrows further when waste heat is available as input.

**Potential Salvage Components**
- Refrigeration compressors (vacuum source and MVR).
- Stainless pressure vessels.
- Automotive condensers.
- Solar thermal collectors (low-grade heat input).

**Volatile Fractionation Staging**

Input streams containing VOCs require a two-stage decompression cycle:

```
[Contaminated Feed]
      ↓
[Stage 1 — Mild Vacuum ~10–15 kPa]
      → VOC vapor → Reject / fuel storage line
      ↓
[Stage 2 — Deep Vacuum <4.5 kPa]
      → Water vapor → Condenser → Potable output
```

Stage 1 strips high-volatility compounds before water recovery begins. This prevents distillate contamination without chemical consumables.

**Proposed Test Parameters**
- **LW-TEST-101 (MVR Efficiency):** Measure compressor electrical input against volumetric output. Reject configurations exceeding 25 kWh/m³.
- **LW-TEST-102 (Volatile Fractionation):** Validate two-stage decompression cycle. Stage 1 (~10–15 kPa) strips volatiles to waste/fuel line. Stage 2 (<4.5 kPa) recovers water. Confirm fractionation valve presence and first-stage rejection routing.
- **LW-TEST-103 (Seal Degradation Tolerance):** Simulate micro-leak at +0.5 kPa/hr. Establish failure threshold at which boiling ceases and thermal input would be required.
- **LW-TEST-104 (Latent Heat Recycling):** Validate that condensation heat is routed back to pre-heat incoming feed-water.

**Status:** Experimental — No design assumptions permitted.

---

### LW-002 — Conventional Reverse Osmosis

**Concept**

Pressure forces water through a semi-permeable membrane while rejecting dissolved salts and contaminants.

**Advantages**
- Mature, well-documented technology.
- High throughput.
- No phase change energy losses.

**Challenges**
- Membrane fouling and consumable dependence conflict with Forge repairability doctrine.
- High mechanical pressure requirements (5.5–7.0 MPa for seawater).
- Less compatible with salvage sourcing than LW-001 or LW-003.

**Status:** Reference pathway. Included as comparative baseline. Not a primary Forge candidate without membrane sourcing solution. See LW-UNK-006.

---

### LW-003 — Pressure-Assisted Deep Water Osmosis (DSRO)

**Concept**

The ocean contains enormous ambient hydrostatic pressure. At depth:

| Depth | Approximate Pressure |
|---|---|
| 100 m | ~10 bar (1.0 MPa) |
| 300 m | ~30 bar (3.0 MPa) |
| 500 m | ~50 bar (5.0 MPa) |
| 1000 m | ~100 bar (10.0 MPa) |

Osmotic pressure of seawater is approximately 2.7 MPa. At 300–500 m depth, ambient hydrostatic pressure exceeds osmotic pressure without mechanical pumping. The energy cost shifts from pressurizing feed-water to lifting product water to the surface — significantly lower.

**Research Question:** Can ambient hydrostatic pressure substitute for mechanical high-pressure pumps in reverse osmosis?

**Flux Model**

`J = A(ΔP − Δπ)`

Where A is membrane permeability, ΔP is hydrostatic pressure differential, and Δπ is osmotic pressure differential. Target deployment window: 400–600 m depth, where ΔP reliably exceeds Δπ without excessive membrane compaction risk.

**Lift Energy Note**

The freshwater lumen interior is at or near atmospheric pressure. If osmotic flux generates sufficient internal head pressure, product water rises partway or fully to the surface without high-pressure pumping — requiring only a low-pressure surface skim pump. This is a significant energy advantage over surface RO that requires explicit validation.

**Advantages**
- Major reduction in energy input vs. surface RO.
- Consistent feedwater quality (cold, low-organics, low-algae at depth).
- No high-pressure pump infrastructure required.

**Challenges**
- Membrane survivability at sustained depth pressure.
- Biofouling at the membrane surface.
- **Lumen implosion risk [CRITICAL]:** At 500 m depth, exterior hydrostatic pressure is ~5.0 MPa. Interior freshwater lumen is at ~0.1 MPa atmospheric. Net crushing load: ~4.9 MPa. Standard PVC and thin-walled salvage tubing will implode. Salvage targets: HDPE SDR-9 pipe, thick-walled steel tubing, or hydraulic hose sleeves rated for >5.5 MPa external crush load. See LW-UNK-003 and LW-TEST-301.
- Recovery and maintenance logistics at depth.
- Mooring and tether management.
- Brine disposal and marine impact unknown.

**External Reference:** Flocean-style submerged RO systems have explored this concept as prototypes. Treat as observational only — compatibility with Forge salvage and repairability doctrine has not been assessed.

**Proposed Test Parameters**
- **LW-TEST-301 (Crush Depth Simulation):** Calculate and test implosion threshold of freshwater conduit. Minimum structural rating: >5.5 MPa external load at target deployment depth.
- **LW-TEST-302 (Osmotic Equilibrium Depth):** Verify deployment depth held strictly between 400–600 m. Below 600 m risks membrane compaction; above 400 m risks insufficient ΔP margin.
- **LW-TEST-303 (Biofouling and Flow Decay):** Measure flux decay over simulated time blocks. Establish maintenance interval and evaluate acoustic anti-fouling pulse cycle effectiveness.
- **LW-TEST-304 (Lift Energy Characterization):** Measure actual pumping energy required to surface product water. Validate whether passive artesian rise reduces or eliminates surface pump requirement.

**Status:** Unknown / Experimental — No design assumptions permitted.

---

### LW-004 — Freeze Separation

**Concept**

Ice formation preferentially excludes dissolved salts and many contaminants. Repeated freeze-thaw cycles progressively concentrate contaminants in the liquid phase while producing cleaner ice.

**Advantages**
- Low complexity.
- No membrane consumables.
- In arctic or cold-climate Forges, ambient cold substitutes for refrigeration energy — potentially making this a primary rather than supplemental pathway.

**Challenges**
- Slow cycle times.
- Multiple cycles required for meaningful purification.
- Contaminant carryover in ice crystal boundaries.
- Limited throughput in temperate climates.

**Status:** Supplemental in temperate contexts. Primary candidate in arctic / cold-climate Forges.

---

### LW-005 — Atmospheric Water Harvesting

**Concept**

Capture of water vapor from ambient air via:
- Passive radiative cooling and condensation.
- Desiccant adsorption/desorption cycles.
- Fog net interception.
- Active refrigeration condensation (see LW-005a).

**Constraint**

Atmospheric harvesting is supplemental until a reliable purification baseline exists. Harvested condensate carries airborne contaminants — microplastics, industrial aerosols, biological particulates — and requires treatment before entering closed-loop storage. In arid Forges where no surface water exists, sequencing pressure may force earlier deployment; purification integration must be planned from the start in those cases.

**Status:** Supplemental — dependent on LW-001 or LW-003 validation first. May be accelerated in desert-context Forges.

---

### LW-005a — Refrigeration-Based Atmospheric Condensation (Active AWG)

**Concept**

Forced humid air across a chilled heat exchanger surface causes water vapor to condense. Unlike passive methods, active refrigeration provides reliable condensation independent of ambient radiative conditions. This is the highest-yield atmospheric pathway under high-humidity conditions and the most compatible with salvage-sourced components.

This sub-pathway was developed from iterative design work across two implementation forms:
- **Vertical downward-venting units** — freestanding, centralized refrigeration, higher output density.
- **Fence-mounted distributed units** — modular deployment along fence lines, solar or grid powered.

The vertical unit architecture is the primary Forge candidate due to greater compatibility with salvaged components and centralized refrigeration efficiency.

**Vertical Unit Architecture (Primary)**

Five-unit array, each unit 1–1.5 m tall, designed for deployment in a defined perimeter area.

*Per unit:*
- Inner core: 5–8 cm diameter aluminum mesh tube with helical impeller or static vanes producing vortex airflow.
- Outer heat exchanger: 20–25 cm diameter tube with copper coils or plates (~2.5–3 m² surface area), enhanced with crinkled aluminum foil and fins, hydrophobic coated.
- Airflow: Top-mounted angled fans (0.1–0.2 m³/s per unit) driving humid air downward through core and across chilled surface.
- Cooling: Centralized 5–7 kW vapor-compression refrigeration unit (target COP 3–4) chilling circulating water to 5–10°C, keeping heat exchanger surface at 10–15°C.
- Heat rejection: Single vertical shaft (20–30 cm diameter) with blower venting condenser heat upward.
- Ionization: High-voltage DC enhancement (+20–25 kV on core, −15 to −20 kV on tube surface) to improve droplet nucleation. See shared electrical architecture note below.
- Collection: Condensate drains to bottom trays and collects in tanks or buckets.

*Proposed performance parameters (unvalidated — empirical testing required):*

| Parameter | Proposed Value | Confidence |
|---|---|---|
| Condensate per unit | 4.5–10 L/hour | Low — modeling estimate |
| Power per unit | 0.37–0.75 kW | Low — modeling estimate |
| Energy intensity | ~0.3–0.5 kWh/L | Plausible — consistent with commercial AWG benchmarks at high humidity |
| Five-unit array total | 22.5–50 L/hour | Low — unvalidated aggregate |
| Local RH reduction (2000 ft² area) | 70% → 40–50% | Very Low — modeling only; atmospheric dynamics unconfirmed |

**Note on energy intensity:** Commercial atmospheric water generators under favorable conditions (>70% RH, warm air) typically achieve 0.3–0.5 kWh/L. The proposed parameters are consistent with this range but have not been validated at Forge build quality or with salvaged components. Degraded performance should be assumed for initial test planning.

**Note on RH reduction claim:** Local humidity reduction in a bounded area is plausible as a secondary effect but is not a design target for this pathway. Water production is the Forge-relevant objective. Atmospheric-scale effects are out of scope at current development interval.

**Fence-Mounted Variant (Alternative Deployment)**

Two form factors developed:
- *2 ft solar unit:* 24" × 10" × 7", 5–7 lbs, 10–15W solar, 110–230 CFM airflow, ~3–4.5 kg/hour output. Cost target: $650–$900 new manufacture.
- *8 ft rollable grid unit:* 96" × 10" × 1" unrolled, 15–20 lbs, 120V grid → 24V DC (14–22W), 90–180 CFM, ~6–9 kg/hour output. Cost target: $700–$925 new manufacture.

**Forge compatibility assessment:** Fence-mounted units assume new manufacture at defined cost targets. This conflicts with salvage-first doctrine. These variants are noted as reference designs for context; they are not primary Forge build candidates unless component sourcing from salvage can be demonstrated. See LW-UNK-009.

**Shared Electrical Architecture Note**

The high-voltage ionization system in LW-005a (+20–25 kV DC) uses the same general electrode configuration as the ionization enhancement explored in LW-001 (vacuum distillation volatility management). A shared high-voltage supply architecture may be feasible across both pathways where both are deployed. This is a declared synergy candidate, not a confirmed design.

**Salvage Component Targets**
- Vapor-compression refrigeration unit: commercial refrigeration compressors (abundant in salvage stream).
- Copper coils: HVAC evaporator coils, refrigerator evaporators.
- Aluminum fins and mesh: window AC units, salvaged heat exchangers.
- Fans: salvaged computer server fans, HVAC blower assemblies.
- High-voltage supply: salvaged neon sign transformers, flyback transformers (requires qualification).

**Proposed Test Parameters**
- **LW-TEST-501 (Condensation Rate vs. RH):** Measure actual condensate output per unit at varying ambient humidity levels. Establish minimum viable RH threshold for positive water yield.
- **LW-TEST-502 (Energy Intensity Validation):** Measure kWh consumed per liter produced across humidity and temperature range. Compare against 0.3–0.5 kWh/L commercial benchmark.
- **LW-TEST-503 (Ionization Enhancement Delta):** Measure condensate yield with and without HV ionization active. Quantify improvement or confirm negligible effect at this scale.
- **LW-TEST-504 (Salvage Component COP):** Measure actual COP of salvaged refrigeration compressor in this configuration. Reject configurations below COP 2.0 as energy-unviable.
- **LW-TEST-505 (Condensate Quality):** Test condensate for airborne contaminants — particulates, biological matter, VOCs. Confirm purification requirements before potable use classification.

**Status:** Exploratory — proposed parameters unvalidated. Salvage compatibility partially confirmed by component availability. Empirical testing required before yield claims can be made.

---

### LW-006 — Membrane Distillation

**Concept**

Combines heat gradients with hydrophobic membranes to transport water vapor while rejecting liquid-phase contaminants.

**Potential Synergies**
- Solar thermal heat input.
- Waste heat from Forge operational systems.
- Biogas combustion byproduct heat.

**Status:** Exploratory. Synergy potential with existing Forge thermal systems warrants further investigation. See LW-008 for multi-effect extension.

---

### LW-007 — Forward Osmosis

**Concept**

Uses osmotic concentration gradients rather than high-pressure pumps to draw water across a semi-permeable membrane into a concentrated draw solution. The draw solution is subsequently regenerated to release purified water.

**Advantages**
- Lower mechanical stress than pressure-driven RO.
- Lower energy requirements at the membrane stage.
- Potential synergy with solar regeneration of draw solution.

**Challenges**
- Draw solution regeneration adds process complexity.
- Regeneration energy cost must be accounted for in full system balance.
- Salvage-compatible draw solution chemistry not yet identified.

**Status:** Exploratory — draw solution regeneration is the key unknown before test design is possible.

---

### LW-008 — Multi-Effect Vacuum Distillation

**Concept**

A direct descendant of LW-001. Rather than wasting condensation heat from a single distillation stage, successive stages operate at progressively lower pressures. Each stage uses the latent heat released by the previous stage's condensation to drive the next stage's evaporation.

**Advantages**
- Substantially improved energy efficiency over single-effect LW-001.
- Compatible with waste heat input at the first effect.
- Strong synergy with Energy.md thermal management.
- Reduces MVR compressor dependency.

**Relationship to LW-001**

LW-001 must be validated first. LW-008 is the efficiency evolution of a proven concept, not an independent research track.

**Status:** Declared future pathway. Dependent on LW-001 validation.

---

### LW-009 — Constructed Wetlands / Biological Polishing

**Concept**

Uses microbial action, plant uptake, and sedimentation in engineered wetland systems for wastewater recovery and secondary treatment.

**Advantages**
- Very low energy requirement.
- Resilient and self-repairing under normal operating conditions.
- No membrane consumables.
- Produces biomass as secondary output.

**Challenges**
- Pathogen control — biological systems require monitoring.
- Seasonal variation in treatment efficiency.
- Land area requirements.
- Not suitable as primary purification for heavily contaminated streams.

**Role in Closed Loop**

LW-009 is a polishing and recovery stage, not a primary purification pathway. It belongs downstream of LW-001 or LW-003, processing secondary effluent and returning treated water to the irrigation or process tier.

**Status:** Exploratory — most applicable to Forges with available land and an established primary purification stage.

---

### LW-010 — Mineral Recovery

**Concept**

Purification processes produce brine and concentrate streams as waste. LW-010 treats these as feedstock rather than disposal problems.

**Potential Outputs (location-dependent)**
- Sodium chloride (table salt, preservation, chemical feedstock).
- Magnesium compounds.
- Gypsum.
- Lithium-bearing brines (specific geological contexts).
- Calcium and potassium salts.

**Relationship to Economics.md**

Brine-as-resource transforms a waste disposal problem into a production line. The economic value is site-dependent and must be assessed against local market and barter conditions. See Economics.md.

**Status:** Exploratory — dependent on primary purification pathway producing consistent brine output.

---

## Open Unknowns

| ID | Description | Status |
|---|---|---|
| LW-UNK-001 | Volatile co-distillation characterization for LW-001 across salvage-context input stream types | Partially addressed — LW-TEST-102 defines test approach. Empirical validation pending. |
| LW-UNK-002 | Membrane survivability for LW-003 at sustained operational depth | Open |
| LW-UNK-003 | Lumen structural integrity limits for LW-003 freshwater conduit under deep pressure | Partially addressed — implosion threshold characterized. Salvage material validation pending. |
| LW-UNK-004 | Biofouling rate characterization for LW-003 in target deployment zones | Open |
| LW-UNK-005 | Energy balance: LW-001 with MVR vs. LW-002 surface RO at equivalent throughput | Partially addressed — energy profiles established. Empirical validation at Forge scale pending. |
| LW-UNK-006 | Salvage-compatible membrane sourcing for any RO pathway | Open |
| LW-UNK-007 | Draw solution regeneration chemistry and energy cost for LW-007 forward osmosis | Open |
| LW-UNK-008 | Site characterization → pathway selection decision framework | Declared — formal framework not yet written |
| LW-UNK-009 | Salvage sourcing path for fence-mounted AWG variant (LW-005a) — required before Forge build candidacy | Open |

*Candidates for migration to Unknowns.md pending triage.*

---

## Long-Term Vision

```
Water Source
      ↓
Site Characterization (input stream typing, location context)
      ↓
Pathway Selection (site-conditioned)
      ↓
Purification (primary pathway)
      ↓
Biological Polishing (LW-009, where applicable)
      ↓
Storage
      ↓
Monitoring
      ↓
Reuse / Redistribution (tiered by Water Hierarchy)
      ↓
Recovery (wastewater as feedstock → LW-009 → LW-010)
      ↓
Mineral Recovery (LW-010)
```

Living Waters ultimately seeks a closed-loop water architecture where:

- Wastewater becomes feedstock.
- Salt becomes recoverable resource.
- Humidity becomes reservoir.
- Reliability exceeds abundance.

**Four-Domain Observation:** Energy and water are tightly coupled. Energy produces water. Water stores and transports heat. Water enables biology. Biology produces waste streams. Waste streams become feedstock. Living Waters, Energy.md, and future files covering atmosphere and biology may form four major resource domains around which the rest of the Forge organizes. This is a declared long-horizon observation, not a current commitment.

---

## Promotion Criteria

This file may be considered for partial promotion to Operations/ when:

1. At least one primary pathway (LW-001 or LW-003) has produced validated purification output at bench or pilot scale.
2. LW-UNK-001 (volatile co-distillation) has been characterized and a safe operating envelope defined.
3. Energy budget for the validated pathway has been documented against Forge operational constraints in Energy.md.
4. A salvage-compatible component list for the validated pathway has been confirmed.
5. Water Hierarchy has been applied — purification target tier is specified, not assumed to be Tier 1 for all uses.

Promotion is partial and pathway-specific. Unvalidated pathways remain in Tests/.

---

## Cross-References

- `Energy.md` — Power sourcing for vacuum pumps, thermal inputs, MVR compressors, and product water lifting.
- `Safety_Protocols.md` — PPE and handling doctrine for contaminated input streams and VOC rejection staging.
- `Unknowns.md` — LW-UNK entries pending migration.
- `Ethical_Constraints.md` — Governs marine deployment impact assessment for LW-003; brine disposal doctrine.
- `Economics.md` — Resource valuation of recovered salt and mineral byproducts (LW-010).

---

*Civilizations rise where water becomes reliable. The first harvest is not food. The first harvest is trust in the water.*

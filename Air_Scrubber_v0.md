# Air Scrubber v0 — Design Doctrine

## Purpose

The Air Scrubber is a core stewardship subsystem of the Lazarus Forge. Its purpose is to prevent the release, accumulation, or uncontrolled transformation of hazardous airborne byproducts generated during Forge operation. The scrubber is not an accessory or afterthought; it is an enabling system without which the Forge shall not operate.

The Air Scrubber exists to:
- Protect operators, nearby systems, and environments
- Prevent secondary hazard creation (e.g., toxic reaction products)
- Capture, stabilize, and channel byproducts into managed streams
- Provide diagnostic insight into Forge chemistry and health

---

## Design Philosophy

**1. Capture Is Part of Production**
All Forge processes assume byproduct generation. The Air Scrubber is designed as a continuation of the production path, not a cleanup step performed after the fact. No Forge mode assumes "clean exhaust." Every mode assumes containment.

**2. Interaction Is Forced, Not Hoped For**
The system does not rely on dilution, dispersion, or passive escape. Airflow is deliberately manipulated to increase residence time, increase molecular and particulate interaction, and convert mobile hazards into capturable forms. The scrubber biases physics toward capture.

**3. Charge, Cool, Then Capture**
Hazardous species are most difficult to manage when they are hot, fast-moving, and neutral. The scrubber architecture follows a consistent logic: charge airborne species to encourage attachment and agglomeration, cool the gas stream to reduce volatility and stabilize intermediates, then capture contaminants into liquid or solid phases. This ordering is intentional and forms the backbone of the system.

**4. Negative Pressure as a Safety Boundary**
The Air Scrubber operates under slight negative pressure relative to its surroundings. Leaks draw air inward rather than expelling contaminants. Loss of airflow is treated as a critical fault. The Forge defaults to shutdown rather than uncontrolled exhaust. Containment is maintained even during partial failure.

---

## Functional Architecture

**Stage A — Sacrificial Mechanical Intercept**
Intent: Protect downstream stages and define a human-safe interaction point.
- Captures coarse particulates and debris
- Prevents fouling of ionization and wet stages
- Designed for frequent replacement or servicing

This stage is treated as expendable by design.

**Stage B — Ionization / Electrostatic Conditioning**
Intent: Convert poorly behaved contaminants into cooperative ones.
- Imparts charge to particulates, aerosols, and vapors
- Encourages agglomeration and surface attachment
- Increases downstream capture efficiency

Ionization energy is moderated; the goal is interaction, not destruction. Ozone or unintended reactive species are considered fault conditions and must be monitored.

**Stage C — Thermal Quench / Cooling Zone**
Intent: Reduce mobility, volatility, and reaction rates.

- Rapidly lowers gas temperature
- Encourages condensation of semi-volatile compounds
- Stabilizes charged species long enough for capture

Cooling may be active or passive but must be explicit in design.

**Stage D — Wet Scrubbing / Water Column**
Intent: Perform bulk removal and phase transfer.
- Absorbs soluble gases
- Captures charged and agglomerated particulates
- Condenses vapors into liquid form
- Removes heat from the exhaust stream

Water is operated in a recirculating loop with monitoring. The scrubber assumes that captured material is hazardous until proven otherwise.

**Stage E — Polishing / Last-Chance Capture**
Intent: Avoid reliance on any single mechanism.
- Captures residual contaminants that escape primary stages
- Provides redundancy against upstream variability
- Serves as a final barrier before release

The specific method is modular and may evolve without changing upstream philosophy.

---

## Waste as a Managed Output

Captured materials are not treated as disposable nuisances.
- Liquids, sludges, and solids are routed into controlled handling paths
- Composition is monitored as a diagnostic signal
- Outputs may become future feedstock or require immobilization

The Air Scrubber doubles as a sensor system for Forge chemistry.

---

## Wet Capture Variants

All variants share the same intent: maximize gas–liquid interaction without creating uncontrolled backpressure or complexity. Selection is based on maturity, available materials, and hazard profile.

**Variant 1 — Aerated Pond-Style Bubbler (Baseline)**
Simple tank with submerged porous diffuser. Gas forced through water via fine bubbles into scrubbing liquid. Aeration media increases bubble surface area and residence time. Prioritizes simplicity, robustness, and ease of inspection.

**Variant 2 — Packed Column with Recirculation (Intermediate)**
Vertical column with random packing or salvaged scrub media. Counter-current gas–liquid contact provides higher efficiency with modest increase in pressure drop.

**Variant 3 — Conditioned Intake + Wet Polish (Future)**
Upstream ionization or conditioning stage feeds a wet stage used primarily for capture and quench. Reserved for higher-energy or higher-uncertainty processes.

**Variant 4 — High-Pressure / Underwater Bubble-Column (Leviathan-Compatible)**

*Environmental & Marine Extension:* While the baseline scrubber is designed for Forge fume and dust hazards, the bubble-column architecture naturally extends to marine environments. This enables in-situ oxygenation and volatile capture testing, validation under pressure and corrosion conditions, and feedback loops relevant to orbital volatile handling. All extensions remain subordinate to the core negative-pressure safety boundary and modest energy ethos.

For deployment in hypoxic or dead-zone environments:
- Inject compressed air or oxygen-enriched mix through pressure-rated submerged diffusers (10–100 atm range)
- In reverse-scrubbing mode, bubbles aerate low-DO water and capture volatiles (H₂S, CO₂) for surface analysis
- Integrate onboard sensors for real-time pH, DO, turbidity, and gas composition
- Target bubble sizes 80–500 μm for optimal mass transfer; adjust column depth (1–3 m) to balance efficiency and pressure drop
- Periodic back-flush or low-concentration surfactant dosing to counter biofouling

Quantitative targets: 10–30% DO saturation increase in <2 mg/L hypoxic water; energy draw <100 W per 1–2 m³ plume.

This variant turns the scrubber into a dual-purpose tool: hazard containment in Forge operations and environmental remediation in marine contexts.

---

## Energy Awareness

Conceptual ballpark ranges (non-binding, Earth surface standard conditions):
- Fan/compressor draw: 50–150 W
- Ionization stage: 10–30 W
- Wet-stage recirculation: 20–80 W

Under high-pressure underwater loads, expect 20–50% uplift in air movement draw due to compression. Goal: stay below 500 W total system draw even in worst-case variants. Scrubber runtime may be logged per session as a diagnostic and optimization signal.

---

## Monitoring & Failure Doctrine

The scrubber is instrumented to detect:
- Loss of airflow or pressure balance
- Excessive ionization byproducts
- Water chemistry drift
- Overflow, carryover, or uncontrolled misting
- Detection of unintended reactive byproducts

Indicators may be simple, redundant, and low-cost. Precision is less important than clarity.

**Design rule:** If the scrubber cannot verify safe operation, the Forge does not run. A scrubber that cannot demonstrate containment is assumed unsafe.

---

## Compatibility With Autonomous Operation

The Air Scrubber is designed to operate continuously without manual tuning, provide clear health signals to supervisory systems, and fail into containment rather than release.

Human oversight is optional; stewardship is not.

---

## Integration Hooks

The Air Scrubber receives exhaust directly from the Spin Chamber, Stratification Chamber, and any enclosure where hazardous aerosols or vapors may form.

Feedback from scrubber behavior is actionable intelligence — not noise:
- Rapid fouling implies upstream particulate overload
- Water chemistry shifts imply unexpected feedstock reactions

**Cross-module links:**
- `Spin_Chamber_v0.md` / `Stratification_Chamber_v0.md` — primary exhaust sources; potential centrifugal pre-separation before scrubbing
- `leviathan_testing.md` — testbed for underwater variants and swarm-scale aeration
- `Component_Triage_System.md` — scrubber chemistry feedback refines classification heuristics
- `energy_v0.md` — aggregate data refines draw estimates under variable loads
- `geck_forge_seed.md` — bootstrap minimal scrubber seeds for remote deployment
- `Ship_of_Theseus_Right_to_Repair.md` — scrubber as preservation enabler during artifact recovery

---

## Next Steps

- Prototype pressure-rated diffuser payloads for Leviathan proxies
- Simulate bubble dynamics via open-source hydro tools before field deployment
- Field test small-scale bubble-column in controlled tank or lake environment to baseline mass transfer rates
- Explore integration with electrolytic stages for combined gas scrubbing and metal ion capture

---

## Summary Doctrine

The Air Scrubber is not a filter.

It is a boundary system that forces hazardous matter into managed forms, prevents accidental chemistry, and makes responsible operation possible at scale.

A Forge that cannot clean up after itself is incomplete by definition.

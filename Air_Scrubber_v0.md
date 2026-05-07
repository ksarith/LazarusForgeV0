# Air Scrubber v0 — Design Doctrine

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-06 (Gemini Flash 3 — Skeptic/Auditor)
- Open unknowns: 3 (Low-Medium)
- Sidecar: [#auditor-notes--unknowns]

---

## Purpose

The Air Scrubber is a core stewardship subsystem of the Lazarus Forge. Its purpose is to prevent the release, accumulation, or uncontrolled transformation of hazardous airborne byproducts generated during Forge operation. The scrubber is not an accessory or afterthought; it is an enabling system without which the Forge shall not operate.

The Air Scrubber exists to:
- Protect operators, nearby systems, and environments
- Prevent secondary hazard creation (e.g., toxic reaction products)
- Capture, stabilize, and channel byproducts into managed streams
- Provide diagnostic insight into Forge chemistry and health

The same pressure-differential principle that makes this system work also applies in reverse: **positive pressure** protects an enclosure by pushing air outward through every gap, preventing dust and contaminants from entering. Both directions of the same physics. See Variant 0.

---

## Design Philosophy

**1. Capture Is Part of Production**
All Forge processes assume byproduct generation. The Air Scrubber is a continuation of the production path, not a cleanup step. Every mode assumes containment.

**2. Interaction Is Forced, Not Hoped For**
Airflow is deliberately manipulated to increase residence time and convert mobile hazards into capturable forms.

**3. Charge, Cool, Then Capture**
Charge airborne species to encourage agglomeration → cool the gas stream to reduce volatility → capture into liquid or solid phases. This ordering is intentional.

**4. Negative Pressure as a Safety Boundary**
The scrubber operates under slight negative pressure relative to surroundings. Leaks draw air inward. Loss of airflow is a critical fault. The Forge defaults to shutdown rather than uncontrolled exhaust.

**5. Know When the Bucket Is Full**
A scrubbing system that has reached saturation while reporting "Airflow OK" is not a scrubber — it is a bypass. The system must monitor scrubbing liquid quality (pH, conductivity, turbidity) and trigger a Saturation Fault before chemical bypass occurs.

---

## Functional Architecture

**Stage A — Sacrificial Mechanical Intercept**
Captures coarse particulates and debris. Protects downstream stages. Designed for frequent replacement — treated as expendable by design.

**Stage B — Ionization / Electrostatic Conditioning**
Imparts charge to particulates, aerosols, and vapors. Encourages agglomeration and surface attachment. Ionization energy is moderated. Ozone or unintended reactive species are fault conditions and must be monitored.

**Stage C — Thermal Quench / Cooling Zone**
Rapidly lowers gas temperature. Encourages condensation of semi-volatile compounds. Stabilizes charged species long enough for capture. Cooling may be active or passive but must be explicit in design.

**Stage D — Wet Scrubbing / Water Column**
Absorbs soluble gases. Captures charged and agglomerated particulates. Water is operated in a recirculating loop with continuous monitoring.

*Thermal sink requirement:* Hot exhaust from the Spin Chamber transfers heat to scrubbing water. Without a thermal rejection path, the water heats until it can no longer quench incoming gas. Stage D requires an explicit **thermal sink interface** — heat exchanger, radiator, or passive cooling surface — sized to the expected exhaust heat load. This is not optional.

*Saturation monitoring requirement:* The scrubbing liquid must be monitored for pH shift, conductivity change, and turbidity. When values exceed defined thresholds, a **Saturation Fault** is triggered — scrubbing liquid must be replaced or regenerated before operations continue. A saturated scrubbing liquid is not a functioning scrubber. See AS-003.

**Stage E — Polishing / Last-Chance Capture**
Captures residual contaminants that escape primary stages. Provides redundancy. Serves as a final barrier before release.

---

## Waste as a Managed Output

Captured materials are not disposable nuisances.
- Liquids, sludges, and solids are routed into controlled handling paths
- Composition is monitored as a diagnostic signal
- Outputs may become future feedstock or require immobilization

The Air Scrubber doubles as a sensor system for Forge chemistry.

---

## Wet Capture Variants

**Variant 0 — Positive Pressure Enclosure Protection (Simplest)**

The pressure-differential principle works in both directions. Where the scrubber uses negative pressure to contain hazards inside an enclosure, positive pressure protects a clean space by pushing air outward through every gap — dust and contaminants must fight the outward flow to enter.

Applications:
- Operator cab or control room in a dusty Forge environment
- Critical electronics enclosures in high-particulate areas
- Any sealed space where dust infiltration reduces reliability or safety

*Implementation:* A blower draws outside air through a multi-stage filter (coarse pre-filter protecting a finer main filter) and pressurizes the protected space. The pre-filter is the sacrificial intercept — replaced frequently and cheaply so the main filter lasts. The protected space needs controlled exits (door seals, pressure relief vents) to maintain differential without over-pressurizing.

*Field observation:* Cabin filters in vehicles operating in high-dust environments fail rapidly because unfiltered dust infiltrates through pressure differentials. A positive pressure system with a sacrificial pre-filter dramatically extends main filter life and protects both occupants and electronics. Standard practice in agricultural and construction equipment — proven at small scale.

This is the lowest-complexity, highest-immediate-value variant for Forge operators working in dusty environments.

---

**Variant 1 — Aerated Pond-Style Bubbler (Baseline)**
Simple tank with submerged porous diffuser. Gas forced through water via fine bubbles. Prioritizes simplicity, robustness, and ease of inspection. **Primary v0 baseline.**

**Variant 2 — Packed Column with Recirculation (Intermediate)**
Vertical column with random packing or salvaged scrub media. Counter-current gas–liquid contact provides higher efficiency with modest increase in pressure drop.

**Variant 3 — Conditioned Intake + Wet Polish (Future)**
Upstream ionization stage feeds a wet stage used primarily for capture and quench. Reserved for higher-energy or higher-uncertainty processes.

**Variant 4 — Shallow-Depth Marine Bubble-Column (Near-Term Marine)**

*Depth scope corrected per Gemini audit — previous claim of 10–100 atm is physically untenable at v0 power budgets. Compressing gas to 100 atm (1000m depth) requires massive compression work that a 100–150W system cannot provide. Variant 4 is scoped to shallow water (<5 atm / ~50m depth) for v0. Deep-sea variants (>50m) route to Trajectories_LF.md as a separate power-class problem.*

For shallow-water deployment (<5 atm):
- Inject compressed air through pressure-rated submerged diffusers
- Aerate low-DO water and capture volatiles (H₂S, CO₂) at surface
- Integrate onboard sensors for real-time pH, DO, turbidity, and gas composition
- Target bubble sizes 80–500 μm *(Analogous — marine aeration literature)*
- Column depth 1–3 m

Quantitative targets: 10–30% DO saturation increase in <2 mg/L hypoxic water *(Analogous)*; energy draw <100 W per 1–2 m³ plume *(Analogous)*.

*Deep-sea Variant 4+ (>50m):* Requires a dedicated high-output compression module, pressure-rated hull integration, and power class beyond v0 budget. Route to Trajectories_LF.md v2/v3 scope.

---

## Energy Awareness

Conceptual ballpark ranges — non-binding, Earth surface standard conditions:
- Fan/compressor draw: 50–150 W *(Analogous)*
- Ionization stage: 10–30 W *(Analogous)*
- Wet-stage recirculation: 20–80 W *(Analogous)*
- Thermal sink (heat exchanger / radiator): *(Placeholder — depends on Spin Chamber exhaust heat load; must be sized before Stage D specification)*

Goal: stay below 500 W total system draw for surface and shallow-water variants *(Placeholder — not yet validated against Forge power budget; cross-reference `energy_v0.md` UNK-011)*. Deep-sea variants are a separate power class and not bounded by this figure.

---

## Monitoring & Failure Doctrine

The scrubber is instrumented to detect:
- Loss of airflow or pressure balance
- Excessive ionization byproducts (ozone)
- **Scrubbing liquid saturation** (pH shift, conductivity, turbidity) — triggers Saturation Fault
- **Scrubbing liquid temperature** — triggers Thermal Fault if Stage D heat load exceeds sink capacity
- Water chemistry drift beyond baseline
- Overflow, carryover, or uncontrolled misting

**Saturation Fault:** Operations suspend until scrubbing liquid is replaced or regenerated. A saturated system reporting "Airflow OK" is a false negative — the most dangerous failure mode for a scrubber.

**Design rule:** If the scrubber cannot verify safe operation, the Forge does not run.

---

## Compatibility With Autonomous Operation

The Air Scrubber is designed to operate continuously without manual tuning, provide clear health signals to supervisory systems, and fail into containment rather than release.

Human oversight is optional; stewardship is not.

---

## Integration Hooks

- `Spin_Chamber_v0.md` — primary exhaust source; thermal load on Stage D sized to Spin Chamber output
- `Material_Separation_Gate_v0.md` — pre-purification separation exhaust source
- `leviathan_testing.md` — testbed for shallow-water marine variants
- `Component_Triage_System.md` — scrubber chemistry feedback refines classification heuristics; contamination handling (UNK-025)
- `energy_v0.md` — aggregate data refines draw estimates; thermal sink power not yet included in demand baseline
- `geck_forge_seed.md` — bootstrap minimal scrubber for remote deployment
- `Ship_of_Theseus_Right_to_Repair.md` — scrubber as preservation enabler during artifact recovery

*Note: Stratification_Chamber_v0.md has been removed. Material_Separation_Gate_v0.md is its functional successor.*

---

## Summary Doctrine

The Air Scrubber is not a filter.

It is a boundary system that forces hazardous matter into managed forms, prevents accidental chemistry, and makes responsible operation possible at scale.

A Forge that cannot clean up after itself is incomplete by definition.

And a scrubber that does not know when it is full is not a scrubber — it is a liability.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Variant 4 marine claimed 10–100 atm range with 20–50% power uplift | Physically untenable — isothermal compression to 100 atm requires massive work; 150W compressor cannot overcome ambient hydrostatic pressure at 1000m | Deep-sea compression is a separate power class. Always calculate compression work before claiming depth range. v0 marine variants cap at <5 atm |
| May 2026 | Stage D described without thermal sink | Hot exhaust from Spin Chamber heats scrubbing liquid until it cannot quench — hidden failure mode | Thermal sink is not optional; must be explicitly sized to exhaust heat load |
| May 2026 | Positive pressure insight from dusty-environment cab filtration | Cabin filters fail rapidly under high dust load | Sacrificial pre-filter protecting main filter dramatically extends service life; positive pressure enclosure protection is Variant 0 — simplest and most immediately useful configuration |

---

## Auditor Notes & Unknowns

### AS-001 — 500W power budget not validated against Forge demand baseline
**Status:** Open
**Risk:** Medium
**What is not yet known:** Whether 500W worst-case scrubber draw (surface/shallow variants) is compatible with Forge power budget at bootstrap and nominal modes. Thermal sink power not yet included in this estimate.
**Resolution path:** Cross-reference against energy_v0.md Power Demand stub. Flag if scrubber + thermal sink exceeds 20% of bootstrap budget.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor
*Cross-module reference: UNK-011 in Unknowns_LF.md*

### AS-002 — Marine bubble-column depth scope corrected; deep-sea variant deferred
**Status:** In Progress
**Risk:** Low
**What is not yet known:** Detailed specification for deep-sea Variant 4+ (>50m / >5 atm). Shallow-water scope (<50m) is now defined for v0.
**Resolution path:** Deep-sea variant routes to Trajectories_LF.md v2/v3 as a separate power-class problem requiring dedicated compression module. Shallow-water v0 variant is Analogous-grounded and physically sound.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor; updated 2026-05-06, Gemini Flash 3

### AS-003 — Scrubber waste stream and saturation fault
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Saturation thresholds for scrubbing liquid (pH, conductivity, turbidity limits that trigger Saturation Fault); waste stream decision tree for captured material (feedstock vs. immobilization vs. disposal); thermal sink sizing for Stage D.
**Resolution path:** Saturation Fault monitoring requirement added to Stage D and Monitoring sections (v0 revision). Threshold values are Placeholder — require first operational chemistry data to calibrate. Thermal sink sizing requires Spin Chamber exhaust heat load characterization. Waste stream decision tree: (1) test captured material for reuse potential; (2) if hazardous, immobilize per applicable regulations; (3) if inert, route to bulk material recovery. Cross-reference Component_Triage_System.md contamination handling (UNK-025).
**Logged:** 2026-05-04, Claude — Skeptic/Auditor; upgraded to In Progress 2026-05-06, Gemini Flash 3
*Cross-module reference: UNK-025 in Unknowns_LF.md*

### Resolution Log
- 2026-05-04: Stratification_Chamber_v0.md reference removed. Material_Separation_Gate_v0.md substituted.
- 2026-05-06: Variant 4 depth scope corrected from 10–100 atm to <5 atm for v0. Deep-sea variants routed to Trajectories_LF.md. Magic Energy fallacy resolved for v0 scope.
- 2026-05-06: Thermal sink requirement added to Stage D. Hidden thermal failure mode closed.
- 2026-05-06: Saturation Fault monitoring requirement added to Stage D and Monitoring sections. Chemical bypass failure mode named and addressed.
- 2026-05-06: Variant 0 (Positive Pressure Enclosure Protection) added. Derived from field observation — cab filtration in high-dust environment. Sacrificial pre-filter doctrine applied.

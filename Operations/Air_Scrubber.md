# Air_Scrubber.md

> ⚠️ **Operational Safety Advisory**
> The Air Scrubber handles toxic, corrosive, and carcinogenic airborne byproducts
> generated during Forge operation. Saturated scrubbing liquid passes contaminants
> directly to exhaust — a Saturation Fault while reporting "Airflow OK" is the most
> dangerous failure mode. Continuous fan and compressor operation produces sustained
> noise levels capable of causing permanent hearing damage and masking fault signals;
> hearing protection is required during operation and maintenance. The scrubber
> operates under negative pressure — loss of airflow draws hazardous air outward.
> Saturation thresholds remain Placeholder (AS-003); apply most conservative
> interpretation until calibrated. **When in doubt, shut down. The Forge does not
> run if the scrubber cannot verify safe operation.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-06                                                          |
| Auditor          | Gemini Flash 3 — Skeptic/Auditor                                    |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Air Scrubber design philosophy and doctrine
- Five-stage functional architecture (Stages A through E)
- Wet capture variants (Variant 0 through Variant 4)
- Saturation Fault and Thermal Fault monitoring requirements
- Negative pressure safety boundary doctrine
- Noise hazard acknowledgment and hearing protection requirement
- Energy awareness and power budget estimates
- Monitoring and failure doctrine
- Waste as a managed output
- Integration hooks to upstream and downstream modules
- Marine shallow-water variant (Variant 4, v0 scope)

**This file DOES NOT define:**
- Spin Chamber exhaust heat load (→ `Operations/Gate_05_Separation_Thermal.md`)
- Forge power budget and demand baseline (→ `Operations/Energy.md`)
- Deep-sea compression module (→ `Admin/Trajectories.md` v2/v3)
- Contamination routing and waste stream final disposition (→ `Operations/Gate_02_Triage.md`)
- Scrubber bootstrap minimum for remote deployment (→ `Architecture/Geck_forge_seed.md`)
- Saturation threshold calibration values (Placeholder — requires operational data)
- Noise exposure limits and hearing conservation program (→ planned Safety_Protocols.md)

---

## File Purpose

This file defines the design doctrine, functional architecture, and operational
requirements for the Air Scrubber subsystem of the Lazarus Forge. The scrubber
is an enabling system — without it, the Forge does not operate. Its purpose is
to prevent release, accumulation, or uncontrolled transformation of hazardous
airborne byproducts generated during Forge operation. If this file disappeared,
operators would lack the doctrine required to design, operate, and maintain the
safety boundary that makes all other Forge operations permissible.

---

## Assumptions

| ID      | Assumption                                                                 | Basis                              | Confidence | Expiry Trigger                                         |
|---------|----------------------------------------------------------------------------|------------------------------------|------------|--------------------------------------------------------|
| ASM-001 | Surface and shallow-water variants operate within 500W total system draw   | Analogous — industrial scrubbers   | Medium     | First measured power draw from operational prototype   |
| ASM-002 | Variant 4 marine scope is limited to <5 atm / <50m depth at v0 power class | Compression work calculation       | High       | Dedicated high-output compression module available     |
| ASM-003 | Negative pressure operation is achievable with salvaged fan/compressor hardware | Analogous — industrial practice | Medium     | First prototype demonstrates achievable differential   |
| ASM-004 | Thermal sink can be sized to Spin Chamber exhaust load at v0               | Placeholder — exhaust load unknown | Low        | Gate_05_Separation_Thermal.md exhaust characterization |
| ASM-005 | Noise from continuous fan/compressor operation exceeds safe exposure limits without PPE | Analogous — industrial fan noise levels | High | Measured SPL confirms otherwise |

---

## Design Philosophy

**1. Capture Is Part of Production**
All Forge processes assume byproduct generation. The Air Scrubber is a
continuation of the production path, not a cleanup step. Every mode assumes
containment.

**2. Interaction Is Forced, Not Hoped For**
Airflow is deliberately manipulated to increase residence time and convert
mobile hazards into capturable forms.

**3. Charge, Cool, Then Capture**
Charge airborne species to encourage agglomeration → cool the gas stream to
reduce volatility → capture into liquid or solid phases. This ordering is
intentional.

**4. Negative Pressure as a Safety Boundary**
The scrubber operates under slight negative pressure relative to surroundings.
Leaks draw air inward. Loss of airflow is a critical fault. The Forge defaults
to shutdown rather than uncontrolled exhaust.

**5. Know When the Bucket Is Full**
A scrubbing system that has reached saturation while reporting "Airflow OK" is
not a scrubber — it is a bypass. The system must monitor scrubbing liquid quality
(pH, conductivity, turbidity) and trigger a Saturation Fault before chemical
bypass occurs.

**6. Noise Is a Hazard, Not a Side Effect**
Continuous fan and compressor operation produces sustained noise levels capable
of causing permanent hearing damage and masking critical fault signals. Hearing
protection is required during all scrubber operation and maintenance. Fault
signal audibility must be verified against ambient noise floor — an alarm that
cannot be heard over the scrubber has not been installed.

---

## Functional Architecture

**Stage A — Sacrificial Mechanical Intercept**
Captures coarse particulates and debris. Protects downstream stages. Designed
for frequent replacement — treated as expendable by design.

**Stage B — Ionization / Electrostatic Conditioning**
Imparts charge to particulates, aerosols, and vapors. Encourages agglomeration
and surface attachment. Ionization energy is moderated. Ozone or unintended
reactive species are fault conditions and must be monitored.

**Stage C — Thermal Quench / Cooling Zone**
Rapidly lowers gas temperature. Encourages condensation of semi-volatile
compounds. Stabilizes charged species long enough for capture. Cooling may be
active or passive but must be explicit in design.

**Stage D — Wet Scrubbing / Water Column**
Absorbs soluble gases. Captures charged and agglomerated particulates. Water
is operated in a recirculating loop with continuous monitoring.

*Thermal sink requirement:* Hot exhaust from the Spin Chamber transfers heat to
scrubbing water. Without a thermal rejection path, the water heats until it can
no longer quench incoming gas. Stage D requires an explicit **thermal sink
interface** — heat exchanger, radiator, or passive cooling surface — sized to
the expected exhaust heat load. This is not optional. See ASM-004 and AS-003.

*Saturation monitoring requirement:* The scrubbing liquid must be monitored for
pH shift, conductivity change, and turbidity. When values exceed defined
thresholds, a **Saturation Fault** is triggered — scrubbing liquid must be
replaced or regenerated before operations continue. A saturated scrubbing liquid
is not a functioning scrubber. Thresholds are Placeholder pending first
operational data. See AS-003.

**Stage E — Polishing / Last-Chance Capture**
Captures residual contaminants that escape primary stages. Provides redundancy.
Serves as a final barrier before release.

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

The pressure-differential principle works in both directions. Where the scrubber
uses negative pressure to contain hazards inside an enclosure, positive pressure
protects a clean space by pushing air outward through every gap — dust and
contaminants must fight the outward flow to enter.

Applications:
- Operator cab or control room in a dusty Forge environment
- Critical electronics enclosures in high-particulate areas
- Any sealed space where dust infiltration reduces reliability or safety

*Implementation:* A blower draws outside air through a multi-stage filter (coarse
pre-filter protecting a finer main filter) and pressurizes the protected space.
The pre-filter is the sacrificial intercept — replaced frequently and cheaply so
the main filter lasts. The protected space needs controlled exits (door seals,
pressure relief vents) to maintain differential without over-pressurizing.

*Field observation:* Cabin filters in vehicles operating in high-dust environments
fail rapidly because unfiltered dust infiltrates through pressure differentials.
A positive pressure system with a sacrificial pre-filter dramatically extends main
filter life and protects both occupants and electronics. Standard practice in
agricultural and construction equipment — proven at small scale.

This is the lowest-complexity, highest-immediate-value variant for Forge operators
working in dusty environments.

---

**Variant 1 — Aerated Pond-Style Bubbler (Baseline)**
Simple tank with submerged porous diffuser. Gas forced through water via fine
bubbles. Prioritizes simplicity, robustness, and ease of inspection.
**Primary v0 baseline.**

**Variant 2 — Packed Column with Recirculation (Intermediate)**
Vertical column with random packing or salvaged scrub media. Counter-current
gas–liquid contact provides higher efficiency with modest increase in pressure drop.

**Variant 3 — Conditioned Intake + Wet Polish (Future)**
Upstream ionization stage feeds a wet stage used primarily for capture and quench.
Reserved for higher-energy or higher-uncertainty processes.

**Variant 4 — Shallow-Depth Marine Bubble-Column (Near-Term Marine)**

*Depth scope corrected per Gemini audit — previous claim of 10–100 atm is
physically untenable at v0 power budgets. Compressing gas to 100 atm (1000m
depth) requires massive compression work that a 100–150W system cannot provide.
Variant 4 is scoped to shallow water (<5 atm / ~50m depth) for v0. Deep-sea
variants (>50m) route to `Admin/Trajectories.md` as a separate power-class
problem.*

For shallow-water deployment (<5 atm):
- Inject compressed air through pressure-rated submerged diffusers
- Aerate low-DO water and capture volatiles (H₂S, CO₂) at surface
- Integrate onboard sensors for real-time pH, DO, turbidity, and gas composition
- Target bubble sizes 80–500 μm *(Analogous — marine aeration literature)*
- Column depth 1–3 m

Quantitative targets: 10–30% DO saturation increase in <2 mg/L hypoxic water
*(Analogous)*; energy draw <100 W per 1–2 m³ plume *(Analogous)*.

*Deep-sea Variant 4+ (>50m):* Requires a dedicated high-output compression module,
pressure-rated hull integration, and power class beyond v0 budget. Route to
`Admin/Trajectories.md` v2/v3 scope.

---

## Energy Awareness

Conceptual ballpark ranges — non-binding, Earth surface standard conditions:
- Fan/compressor draw: 50–150 W *(Analogous)*
- Ionization stage: 10–30 W *(Analogous)*
- Wet-stage recirculation: 20–80 W *(Analogous)*
- Thermal sink (heat exchanger / radiator): *(Placeholder — depends on
  `Operations/Gate_05_Separation_Thermal.md` exhaust heat load; must be sized
  before Stage D specification)*

Goal: stay below 500 W total system draw for surface and shallow-water variants
*(Placeholder — not yet validated against Forge power budget; cross-reference
`Operations/Energy.md`)*. Deep-sea variants are a separate power class and not
bounded by this figure. See AS-001.

---

## Monitoring & Failure Doctrine

The scrubber is instrumented to detect:
- Loss of airflow or pressure balance
- Excessive ionization byproducts (ozone)
- **Scrubbing liquid saturation** (pH shift, conductivity, turbidity) —
  triggers Saturation Fault
- **Scrubbing liquid temperature** — triggers Thermal Fault if Stage D heat
  load exceeds sink capacity
- Water chemistry drift beyond baseline
- Overflow, carryover, or uncontrolled misting
- **Ambient noise floor** — fault alarms must be audible above scrubber
  operating noise; verify signal-to-noise margin at commissioning

**Saturation Fault:** Operations suspend until scrubbing liquid is replaced or
regenerated. A saturated system reporting "Airflow OK" is a false negative —
the most dangerous failure mode for a scrubber.

**Noise Fault Masking:** If fault alarms cannot be heard over continuous
scrubber noise, the alarm system has failed its purpose. Audibility must be
verified at commissioning and after any hardware change.

**Design rule:** If the scrubber cannot verify safe operation, the Forge does
not run.

---

## Compatibility With Autonomous Operation

The Air Scrubber is designed to operate continuously without manual tuning,
provide clear health signals to supervisory systems, and fail into containment
rather than release.

Human oversight is optional; stewardship is not.

---

## Integration Hooks

- `Operations/Gate_05_Separation_Thermal.md` — primary exhaust source; thermal
  load on Stage D sized to Spin Chamber output
- `Operations/Gate_04_Separation_Mechanical.md` — pre-purification separation
  exhaust source
- `Tests/Leviathan_testing.md` — testbed for shallow-water marine variants
- `Operations/Gate_02_Triage.md` — scrubber chemistry feedback refines
  classification heuristics; contamination handling cross-reference
- `Operations/Energy.md` — aggregate data refines draw estimates; thermal sink
  power not yet included in demand baseline
- `Architecture/Geck_forge_seed.md` — bootstrap minimal scrubber for remote
  deployment
- `Admin/Ship_of_Theseus.md` — scrubber as preservation enabler during artifact
  recovery

---

## Summary Doctrine

The Air Scrubber is not a filter.

It is a boundary system that forces hazardous matter into managed forms, prevents
accidental chemistry, and makes responsible operation possible at scale.

A Forge that cannot clean up after itself is incomplete by definition.

And a scrubber that does not know when it is full is not a scrubber — it is a
liability.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                                        | What Failed                                                                                              | What Was Learned                                                                                                                             | Confidence | Revalidation Needed |
|----------|---------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Modeling      | Variant 4 marine claimed 10–100 atm range with 20–50% power uplift   | Physically untenable — isothermal compression to 100 atm requires massive work; 150W compressor cannot overcome ambient hydrostatic pressure at 1000m | Deep-sea compression is a separate power class. Always calculate compression work before claiming depth range. v0 marine variants cap at <5 atm | Analogous  | Yes                 |
| May 2026 | Audit Review  | Stage D described without thermal sink                                | Hot exhaust from Spin Chamber heats scrubbing liquid until it cannot quench — hidden failure mode        | Thermal sink is not optional; must be explicitly sized to exhaust heat load                                                                  | Analogous  | Yes                 |
| May 2026 | Anecdotal     | Positive pressure insight from dusty-environment cab filtration       | Cabin filters fail rapidly under high dust load without pre-filter                                       | Sacrificial pre-filter protecting main filter dramatically extends service life; positive pressure enclosure protection is Variant 0 — simplest and most immediately useful | Analogous | Yes |
| 2026-05-23 | Audit Review | Noise hazard absent from prior versions                             | Continuous fan/compressor noise omitted from safety doctrine despite known industrial hearing damage risk and fault-masking potential | Noise added to Safety Advisory, Design Philosophy, and Monitoring sections. Fault alarm audibility verification added as commissioning requirement | Analogous | Yes |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date     | Path                                                        | Why Abandoned                                                                               | Reconsider? |
|----------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------|-------------|
| May 2026 | Variant 4 deep-sea scope at v0 power class                  | Compression work to 100 atm is physically untenable at 100–150W; separate power class required | Yes — at v2/v3 |
| May 2026 | Stage D without explicit thermal sink specification         | Hidden failure mode — water heats to ineffectiveness without thermal rejection path         | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Saturation Fault monitoring requirement removed or made optional
- Negative pressure safety boundary doctrine weakened or removed
- Thermal sink requirement removed from Stage D
- Noise hazard removed from Safety Advisory, Design Philosophy, or Monitoring sections
- Fault alarm audibility verification requirement removed
- 500W power budget claimed as validated without measurement
- Variant 4 depth scope expanded beyond <5 atm without dedicated compression module
- Integration hooks reference stale flat filenames rather than canonical folder-prefixed paths
- Ethical Anchor field absent, altered, or does not match canonical string
- Design rule "If the scrubber cannot verify safe operation, the Forge does not run" removed or softened

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### AS-001 — 500W power budget not validated against Forge demand baseline

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Air_Scrubber.md     |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-05-23                     |

**Description:** Whether 500W worst-case scrubber draw (surface/shallow variants)
is compatible with Forge power budget at bootstrap and nominal modes. Thermal sink
power not yet included in this estimate.

**Why It Matters:** Scrubber is a prerequisite for Forge operation — if it exceeds
available power budget, the Forge cannot run safely.

**Resolution Path:** Cross-reference against `Operations/Energy.md` Power Demand
stub. Flag if scrubber + thermal sink exceeds 20% of bootstrap budget.

---

### AS-002 — Marine bubble-column depth scope corrected; deep-sea variant deferred

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Air_Scrubber.md     |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-05-06                     |

**Description:** Detailed specification for deep-sea Variant 4+ (>50m / >5 atm)
remains undefined. Shallow-water scope (<50m) is defined for v0.

**Why It Matters:** Leviathan deployment may eventually require deep-sea scrubbing
capability beyond current scope.

**Resolution Path:** Deep-sea variant routes to `Admin/Trajectories.md` v2/v3 as
a separate power-class problem requiring dedicated compression module.

---

### AS-003 — Scrubber waste stream and saturation fault thresholds undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Air_Scrubber.md     |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-05-23                     |

**Description:** Saturation thresholds for scrubbing liquid (pH, conductivity,
turbidity limits that trigger Saturation Fault) remain Placeholder. Waste stream
decision tree and thermal sink sizing also undefined.

**Why It Matters:** Without calibrated thresholds, Saturation Fault cannot be
reliably triggered — the most dangerous scrubber failure mode goes undetected.

**Resolution Path:** Threshold values require first operational chemistry data to
calibrate. Thermal sink sizing requires `Operations/Gate_05_Separation_Thermal.md`
exhaust heat load characterization. Waste stream: (1) test for reuse potential;
(2) if hazardous, immobilize per applicable regulations; (3) if inert, route to
bulk material recovery.

---

### AS-004 — Noise exposure limits and hearing conservation program undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical / Governance         |
| Blocking      | No                             |
| Owner         | Operations/Air_Scrubber.md     |
| First Logged  | 2026-05-23                     |
| Last Reviewed | 2026-05-23                     |

**Description:** Continuous fan and compressor noise levels have not been
characterized. No hearing conservation program, exposure limits, or PPE
specification exists for scrubber operation.

**Why It Matters:** Sustained exposure above 85 dBA causes permanent hearing
damage. Noise also masks fault alarms — a critical safety dependency. Both
risks are unmitigated at v0.

**Resolution Path:** Payment via Specification — measure SPL at operator
positions during scrubber operation. Define hearing protection requirement.
Verify fault alarm audibility against measured noise floor. Formal hearing
conservation program routes to planned `Admin/Security_Protocols.md` or a
dedicated `Admin/Safety_Protocols.md`.

---

### Resolution Log

- 2026-05-04: Stratification_Chamber_v0.md reference removed. Material_Separation_Gate_v0.md substituted.
- 2026-05-06: Variant 4 depth scope corrected from 10–100 atm to <5 atm for v0. Deep-sea variants routed to Trajectories.md. Magic Energy fallacy resolved for v0 scope.
- 2026-05-06: Thermal sink requirement added to Stage D. Hidden thermal failure mode closed.
- 2026-05-06: Saturation Fault monitoring requirement added to Stage D and Monitoring sections. Chemical bypass failure mode named and addressed.
- 2026-05-06: Variant 0 (Positive Pressure Enclosure Protection) added. Derived from field observation — cab filtration in high-dust environment. Sacrificial pre-filter doctrine applied.
- 2026-05-23: Retrofit to File_Template.md structure. File State table, Scope Boundary, Assumptions, Abandoned Paths, Drift Indicators sections added. Noise hazard added to Safety Advisory, Design Philosophy Principle 6, Monitoring section, and AS-004 sidecar entry. All integration hook references updated to canonical folder-prefixed paths. Lessons Learned table reformatted with Evidence Type and Confidence columns.

# Energy.md

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Salvaged electrochemical batteries with unknown state-of-health present catastrophic thermal runaway and toxic hydrofluoric acid outgassing risks. Containment and isolation protocols are mandatory before any salvaged battery bank is commissioned (EV-003). Do not install salvaged storage in unventilated or uninsulated enclosures. Air Scrubber operation is strictly required during any battery handling, charging, or thermal failure event. **When in doubt, isolate the battery bank and do not proceed.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-31                                                          |
| Auditor          | Gemini                                                              |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Design philosophy for incremental energy integration at v0
- Energy lifecycle progression from external grid reliance to partial thermal/waste recovery
- Real-world generation interlocks for syngas and biomass loops
- Calibrated power mode envelopes and actionable voltage sag protocols
- Hard-coded physical protection parameters and isolation boundaries for salvaged batteries
- Primary and secondary falsifiable performance metrics

**This file DOES NOT define:**
- Deep-environment battery degradation physics modeling (→ `Tests/Leviathan_testing.md` LT-002)
- Leviathan power envelope specification (→ `Tests/Leviathan_testing.md` LT-001)
- Mechanical drawings for battery containment structures
- Detailed chemistry sorting algorithms for unknown cells (→ `Operations/Gate_02_Triage.md`)

---

## File Purpose

This file defines the energy strategy for the Lazarus Forge at v0. The Forge is energy-intensive by nature — reduction, thermal separation, and fabrication all draw significant power. This document provides a plausible, incremental path from external grid dependency toward partial self-sufficiency through salvaged and waste energy sources, without claiming energy independence that has not been demonstrated.

Its primary function as a cross-reference anchor is the Power Demand stub — a demand-side placeholder that allows Leviathan power envelope scoping and per-module energy accounting to integrate against a common reference point, even before actual figures are measured. If this file disappeared, the repository would have no shared energy accounting baseline and no demand-side anchor for cross-module power budgeting.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Grid power is available at v0 bootstrap site | v0 terrestrial deployment context | Medium | Off-grid or remote deployment confirmed — bootstrap strategy changes |
| ASM-002 | Salvaged motor-generators can be back-driven to produce usable electricity | Standard electromechanical reversibility principle | Medium | First salvaged motor-generator characterized for output efficiency |
| ASM-003 | Biogas output can overcome parasitic overheads via thermal recovery | Bound to 35°C digestate tank rule | Medium | EV-002 baseline measurements prove net-negative balance |
| ASM-004 | Salvaged batteries retain sufficient usable capacity to serve as energy buffer | Common salvage practice; SoH unknown | Low | First salvaged battery bank characterized for SoH and cycle capacity |
| ASM-005 | Waste heat from Spin Chamber and other thermal processes is available for opportunistic reuse | `Operations/Gate_05_Separation_Thermal.md` exhaust profile | Low | SC-007 resolved — exhaust heat load characterized |

---

## Design Philosophy

- **Energy demand is acknowledged, not hidden:** Power budgets must reflect real electromechanical and thermal loads, not idealized values.
- **Early stages prioritize learning over efficiency:** Robust, basic containment and crude power transformation trump high-efficiency micro-grids at v0 bootstrap.
- **Salvage-first applies to power systems as well:** Repurposing industrial automotive alternator blocks and salvaged battery cells is the primary hardware path.
- **Multiple small contributors are preferred over single large sources:** Spreading generation across solar, syngas, and grid links prevents single-point failure cascades.

---

## Energy Lifecycle

```
[Stage 1: Bootstrap] ──► Primary reliance on external Grid Power / Watchdog Loops
         │
         ▼
[Stage 2: Supplement] ──► Modular Solar Integration + Salvaged Motor-Generators
         │
         ▼
[Stage 3: Recovery]  ──► Regulated Biogas Digestion + Syngas Generation
         │
         ▼
[Stage 4: Loop Close]──► Opportunistic Thermal Recovery (Gate 05 Heat Sink Exchanger)
```

---

## Energy Sources & Generation Interlocks (v0 Scope)

### 1. Grid Power (Bootstrap)

Primary early-stage energy source. Enables primary reduction, separation, and control systems. Treated as a temporary dependency, not a permanent fixture.

### 2. Salvaged Motor-Generators

Recovered motors repurposed as generators back-driven via turbines, belts, or engines.

> ⚙️ **Real-World Interlock — The Tar Minimization Rule**
> Open-loop biomass gasification is strictly prohibited for raw processing unless a multi-stage mechanical particulate filter and oil-bubbler quenching system are placed inline. Unscrubbed syngas will gum internal combustion valves within less than 12 operational hours, triggering a critical mechanical power failure cascade.

### 3. Anaerobic Digestion (Biogas)

Organic waste converted into methane-rich gas to drive generators or provide process heat.

> ⚙️ **Real-World Interlock — The Parasitic Biogas Threshold [Ref: EV-002]**
> Biogas generation cannot be accounted for as a net-positive primary energy source unless the ambient thermal temperature of the digestate tank exceeds 35°C via passive solar or thermal recovery streams. The electrical cost of continuous mechanical mixing and gas compression must not exceed 22% of the total calculated methane output value.

### 4. Solar (Supplemental)

Modular photovoltaic panels with direct DC routing where possible. Offsets control and daytime utility loads to minimize peak grid draw spikes.

### 5. Thermal Recovery (Opportunistic)

Waste heat reused to stabilize or preheat incoming feedstocks. Not counted as a primary grid input. Cross-reference: `Operations/Gate_05_Separation_Thermal.md` exhaust profile (SC-007).

---

## Superconductivity Horizons (Exploratory / v1+)

### Philosophy & Strategic Value
Superconductivity represents a high-leverage multiplier for the Forge's core metric: **Value recovered per kWh**. Zero-resistance transmission, high-field magnets, efficient motors, and lossless energy storage could dramatically lower parasitic loads across reduction, fabrication, and Leviathan-scale operations. However, per the Forge doctrine, we treat this as an engineering target rather than a speculative miracle.

Key guiding principles drawn from disciplined analysis:
- **Superconductivity is a phase transition, not gradual resistance reduction.** Simply purifying materials or lowering scattering does not automatically produce a Cooper-paired condensate. This distinction guards against intuitive but unproductive optimization paths. [](grok_render_citation_card_json={"cardIds":["bde569"]})
- **Ambient-pressure progress is the priority.** Cryogenic solutions have limited bootstrap utility in salvage/remote contexts. Records such as the 151 K ambient-pressure milestone (Hg-1223 metastable phase) highlight meaningful engineering headroom without extreme infrastructure. [](grok_render_citation_card_json={"cardIds":["cb3628"]})
- **Shift from discovery to architecture/engineering.** Quantum geometry, deliberate strain, and controlled metastable phases offer more practical levers than multi-element "cocktail" doping, which often leads to segregation, instability, or insulating byproducts. [](grok_render_citation_card_json={"cardIds":["d3263c"]})
- **Space metallurgy as a long-horizon enabler.** Microgravity and vacuum conditions can stabilize structures difficult on Earth, but they will not magically create superconductors — only enable deliberate engineering of candidate materials. [](grok_render_citation_card_json={"cardIds":["08d9ba"]})

### Integration Pathways for the Forge
1. **Transmission & Distribution**  
   Lossless or near-lossless power routing between gates and modules would improve overall energy accounting and enable distributed Leviathan deployments.

2. **Magnetic Systems**  
   Stronger, more efficient magnets for separation (eddy currents, induction melting), motors/generators, and potential maglev internal logistics.

3. **Energy Storage & Recovery**  
   Persistent current loops or high-efficiency SMES (Superconducting Magnetic Energy Storage) as buffers, complementing salvaged battery protocols.

### v0–v1 Guardrails & Falsifiable Gates
- **No dedicated R&D budget at v0.** Monitor external progress and salvage opportunities only.
- **Test any candidate materials** via simple four-point probe resistance + basic susceptibility checks before integration.
- **Maintain fallback to conventional conductors.** All designs must support graceful degradation to copper/aluminum baselines.
- **Unknowns to Track** (link to main Unknowns.md):
  - SC-H1: Practical ambient-pressure materials viable below 200 K under Forge bootstrap constraints.
  - SC-H2: Salvage-compatible fabrication routes for superconducting wire/joints.
  - SC-H3: Net system-level kWh benefit after accounting for cooling/strain infrastructure.

### Cross-References & Migration Path
- Strong empirical or prototype success → migrate detailed implementation to **Engineering.md** (pragmatic fabrication focus).
- Ties to: Gate_05_Separation_Thermal.md (induction efficiency), Leviathan testing, Critical_Minerals.md (rare-earth magnet alternatives), and Cognitive_Frameworks.md (emergent optimization of energy loops).

**Drift Indicator:** Treating superconductivity as assumed or near-term rather than exploratory triggers re-audit and potential removal of optimistic language.

---

## Electrochemical Battery Containment Protocol [Ref: EV-003]

Salvaged battery state-of-health (SoH), cycle history, and remaining capacity are uncharacterized at v0. To safely leverage these assets without risking catastrophic structural fires, the following physical containment rules apply:

- **Physical Isolation:** Salvaged lithium-ion or lead-acid cell packs must reside in an isolated, external, pressure-vented enclosure separated from primary computational nodes and volatile feedstocks by a minimum 2-hour fire-rated containment barrier.
- **The Over-Extraction Guard:** Discharge cut-off parameters must be locked via hard-coded physical voltage dividers at 3.0V per cell for lithium-class chemistry. This suppresses internal copper shunting and subsequent self-heating runaway during sub-nominal recharge cycles.
- **The Scrubber Prerequisite:** If any cell temperature probe registers greater than 55°C, the main battery disconnect relay must open immediately via hardware trip, and the `Operations/Air_Scrubber.md` variant 0 positive-pressure loop must automatically lock into max-flow mode to purge hydrofluoric acid gas byproducts away from human operators.

---

## Hardware Power Mode Profiles [Ref: EV-001]

To prevent logic-loop crashes from supply-rail sag, all autonomous processing actions must align with verified hardware power envelopes.

| Operational Mode | Target Consumption Floor | Tolerable Voltage Ripple | Mandated Power Source Allocation | Actionable Sag Protocol |
|---|---|---|---|---|
| **Logic / Watchdog** | Less than 15 W baseline | ±1% | Primary TEG Bank / Small Isolated Lead-Acid Buffer | Maintain state indefinitely; broadcast keep-alive telemetry |
| **Mechanical Milling** | 1.5 kW peak | ±5% | Active Hydro-Engine / Main Battery Bank (SoH > 70%) | Cycle spindle speed down 50%; halt axis travel stepper logic |
| **Nominal Mode** | 15–40 kW nominal range | ±5% | Grid Power / Scaled Generator Blocks + Air Scrubber | Throttle material feed rates; pause secondary processing axes |
| **Thermal Melt (G5)** | 8.0 kW burst | ±10% | Direct Generator / Dedicated Biomass Syngas Loop | Trigger immediate safety clamp; dump molten charge to dry safe crucible |

---

## Metrics (Falsifiable)

Primary metric: **kWh consumed per kg of recovered usable output**

*"Usable output" definition:* Material recovered to a condition suitable for direct reuse or further processing without additional sorting. Minimum threshold requirement: passes `Operations/Gate_02_Triage.md` electrical or mechanical verification checks.

Secondary indicators:
- % energy supplied by recovered/salvaged sources
- Internal combustion generator uptime logs
- Storage capacity degradation slope

---

## Explicit Non-Goals (v0)

- Total energy self-sufficiency or immediate off-grid autonomy
- Zero-greenhouse-emission operating targets
- Novel or experimental power generation physics
- Industrial-scale conversion efficiency optimization

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-31 | Field / Audit Data | Raw syngas combustion routing | Valve gumming and internal carbon fouling within 12 hours | Multi-stage particulate filtration and oil-bubbler quenching are mandatory prerequisites | High | No |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet | — |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Power Demand mode definitions revised without updating the hardware power envelope limits
- Biogas counted as a net-positive source if digestate core temp drops below 35°C for sustained periods
- Salvaged battery storage commissioned in an enclosed space without a verified 2-hour fire barrier or independent ventilation routing
- Hard-coded lithium voltage cutoff shifted below 3.0V via software override patches
- The falsifiable primary metric (kWh per kg) is replaced with non-measurable efficiency targets

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### EV-001 — Forge power demand uncharacterized at any operating mode

| Field         | Value                                                               |
|---------------|---------------------------------------------------------------------|
| Status        | In Progress                                                         |
| Risk          | Medium                                                              |
| Priority      | Major                                                               |
| Type          | Technical                                                           |
| Blocking      | Yes — blocks v1 operating cost model and `Admin/Economics.md` EC-002 |
| Owner         | `Operations/Energy.md`                                              |
| First Logged  | 2026-05-27                                                          |
| Last Reviewed | 2026-05-31                                                          |

**Description:** Actual consumption of the physical bootstrap hardware remains an estimate based on industrial analogs. No measured data exists for any operational mode.

**Why It Matters:** EV-001 is the demand-side anchor for all cross-module energy accounting. Without measured figures, every power budget claim in the repository carries Placeholder confidence. Blocks `Admin/Economics.md` EC-002 (operating cost baseline) and `Admin/Trajectories.md` TR-001 (v1 profitability).

**Resolution Path:** Power Demand stub bound to concrete operational mode envelopes (Logic, Milling, Nominal, Thermal Melt). Replace analog values with real shunt-resistor telemetry as hardware validation completes. Payment via Specification once measured figures replace Placeholder values.

---

### EV-002 — Parasitic and thermal startup loads for biogas streams uncharacterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | `Operations/Energy.md`                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-05-31                                       |

**Description:** Total net energy yield of anaerobic digestion loops is unmeasured under cold-start conditions.

**Why It Matters:** If parasitic loads exceed 22% of methane output value under cold-start conditions, biogas cannot be counted as a net-positive source. ASM-003 expiry trigger depends on this data.

**Resolution Path:** Enforced the 35°C thermal interlock threshold and 22% maximum compressor energy rule. Next step: capture gas-flow meter data against input feedstock mass vectors during initial operational loops. Payment via Specification once first operational cycle data characterizes net yield under cold-start.

---

### EV-003 — Salvaged battery thermal containment and ventilation strategy undefined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | Yes — before enclosed battery bank commissioning |
| Owner         | `Operations/Energy.md`                           |
| First Logged  | 2026-05-27                                       |
| Last Reviewed | 2026-05-31                                       |

**Description:** Unknown state-of-health battery modules present catastrophic thermal runaway vectors. Full containment and ventilation doctrine not yet physically validated.

**Why It Matters:** Uncontrolled lithium battery thermal runaway in an enclosed space produces fire, explosion, and toxic HF outgassing. This is a life-safety unknown, not an optimization question.

**Resolution Path:** Physical isolation rules, locked 3.0V per cell hard-guards, and Air Scrubber Max-Flow auto-trigger coupling now codified in body. Move to resolved once the external fire-rated enclosure physical build passes cold safety audit. Payment via Specification once enclosure build is physically verified.

---

### Resolution Log

- 2026-05-27: EV-001 reformatted to structured sidecar format. Corrected stale `Unknowns_LF.md` reference to `Unknowns.md`. Added EV-002 and EV-003 tracking.
- 2026-05-31: Restructured document to achieve Spec Gate 1 baseline. Integrated Tar Minimization interlock and the 35°C/22% Biogas efficiency threshold into core Energy Sources layer. Bound EV-001 to specific hardware envelope profile table. Fully codified physical isolation boundaries and automated air scrubber max-flow overrides for EV-003. Cleaned double-hash tracking headers.
- 2026-06-08: Navigation Anchors block added. Verification Ref corrected from `Admin/Forge_Audit_Kit.md` to `Admin/Verification_Gates_LF.md` (PC-001). Sidecar entries expanded to full field table format per `Admin/File_Template.md`. Formatting normalized — horizontal rules added between all major sections.

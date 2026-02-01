# Air_Scrubber_v0.md

**Purpose**  
Primary safety module for Lazarus Forge: capture fumes, dust, volatiles, and aerosols generated during salvage processing (grinding, thermal steps, chemical exposure, spin/strat chambers) before they escape into the workspace or environment.  
Core doctrine: **Capture is production** — captured material is feedstock, not waste.

**Design Philosophy**  
- Negative pressure containment boundary at all times  
- Forced interaction between gas and capture medium (no passive settling)  
- Modest energy draw — prioritize low-power fans/compressors over high-throughput  
- Multi-stage progression: Charge → Cool → Capture  
- Prefer wet methods for most streams (superior particle adhesion, cooling, and chemical trapping)  
- Design for easy maintenance and media refresh using salvaged components  

### Environmental & Marine Extension Potential

While primarily designed for Forge fume/dust hazards (e.g., from Spin_Chamber or Stratification_Chamber exhaust), the bubble-column architecture naturally extends to marine applications via reverse-flow aeration in low-DO ocean zones. This enables:  
- In-situ oxygenation and volatile capture testing  
- Validation of scrubber robustness under pressure, corrosion, and biofouling  
- Feedback loops for orbital volatile handling analogs (Astroid-miner synergies)  

All extensions remain subordinate to the core negative-pressure safety boundary and modest energy ethos.

**Functional Architecture (Baseline)**  
1. **Charge Stage** — Ionization or electrostatic preconditioning to charge particles (optional but effective for sub-micron fines)  
2. **Cool Stage** — Heat exchanger or mist quench to condense vapors and reduce gas temperature (prevents evaporation loss in wet stage)  
3. **Capture Stage** — Bubble-column wet scrubber (preferred) or packed-bed variant  
   - Gas forced upward through liquid pool with fine bubbles  
   - High surface area contact → efficient trapping of particulates, acids, VOCs  

**Preferred Methods & Variants**

**Variant 1 — Baseline Bubble-Column (Aerated Pond Style)**  
- Simple tank with submerged porous diffuser  
- Air compressor forces gas through fine bubbles into scrubbing liquid (water + additives)  
- Overflow or skimmer removes captured sludge  

**Variant 2 — Packed Column with Recirculation**  
- Gas rises through packed media (Raschig rings, pall rings, or salvaged plastic scraps) wetted by recirculating liquid  
- Higher efficiency for soluble gases; higher pressure drop  

**Variant 3 — Venturi Scrubber (High-Energy Option)**  
- High-velocity throat atomizes liquid into gas stream  
- Used only for very fine or sticky aerosols when bubble column insufficient  

**Variant 4 — High-Pressure / Underwater Bubble-Column Extension (Leviathan-Compatible)**  
For deep-ocean or high-humidity testing environments (e.g., Leviathan platform deployments in hypoxic/dead zones), adapt the baseline aerated pond-style bubbler into a reverse-flow or in-situ configuration:  

- Inject compressed air (or oxygen-enriched mix) through submerged diffusers to create rising bubble plumes that enhance gas–liquid exchange.  
- In "reverse scrubbing" mode, bubbles aerate low-DO water, capturing volatiles (e.g., H₂S, CO₂) into the gas phase for surface off-gassing analysis, or dissolving O₂ to test oxygenation efficiency.  
- Key adaptations: Pressure-rated diffusers (porous hoses or fine-pore membranes) to match ambient depths (10–100 atm); recirculating loops if needed for closed-system tests; integration with onboard sensors for real-time pH, DO, turbidity, and gas composition.  
- Rationale: Validates bubble efficiency under pressure/corrosive conditions analogous to salvage fume processing; provides data on residence time, mass transfer rates, and energy per m³ aerated.  
- Quantitative targets (initial benchmarks from analogs): Achieve 10–30% DO saturation increase in <2 mg/L hypoxic water; bubble sizes 80–500 μm for optimal transfer; energy draw scaled to Leviathan nuclear/battery output (e.g., <100 W per 1–2 m³ plume).  
- **Bubble Size Optimization**: Target 80–500 μm range for peak mass transfer coefficient (higher interfacial area without excessive coalescence); finer pores for deeper ops, coarser for energy savings in shallow tests.  
- **Residence Time & Height Tuning**: Adjust column/submerged depth (1–3 m typical) to balance transfer efficiency vs. pressure drop; monitor via swarm sensors for real-time refinement.  
- **Fouling Mitigation**: Periodic back-flush or additive dosing (e.g., low-concentration surfactants) to counter marine biofouling; test divergent variants in parallel.  

This variant turns the scrubber into a dual-purpose tool: hazard containment in Forge ops and environmental remediation/testing in marine contexts.

**Energy Awareness**  
Conceptual ballpark ranges (Earth surface, standard conditions):  
- Fan/compressor draw: 50–150 W (baseline bubble column)  
- Ionization stage: 10–30 W  
- Recirculation pump (if used): 20–80 W  
Under high-pressure underwater loads, expect 20–50% uplift in air movement draw due to compression; swarm data will refine these estimates.  
Goal: Stay well below 500 W total system draw even in worst-case variants.

**Testing Extensions & Divergent Validation (Leviathan Integration)**

To falsify assumptions and accelerate refinement, incorporate high-throughput, parallel testing via Leviathan swarm proxies:  

- **Aeration Field Experiments** — Deploy 10–100+ miniaturized scrubber variants in mostly lifeless ocean zones (e.g., oxygen minimum zones). High-pressure air systems create controlled bubble plumes mid-water (avoiding sediment resuspension), churning for vertical mixing while monitoring air off-gassing quality (VOCs, CO₂) and water parameters (DO gradients, pH shifts, turbidity).  
- **Divergent Setups** — Run simultaneous A/B/n variants: bubble-column vs. packed column; fine vs. coarse diffusers; ionization preconditioning on/off; different electrolytes/additives. Quantify KPIs: DO increase per kWh, mass transfer coefficient, fouling rates, and failure propagation across swarm.  
- **Value & Metrics** — Generate terabytes of spatial/temporal data for statistical modeling; benchmark against analogs (e.g., 3–100× efficiency gains via optimized bubble size/hydrodynamic effects). Feed results into energy accounting (value recovered per kWh) and upstream triage adjustments.  
- **Safety & Ethics** — Limit to hypoxic areas with low biodiversity; enforce autonomous shutdown on chemistry drift or unintended byproducts; open-source plume data for community remediation studies.  

These extensions provide falsifiable, quantitative validation in extreme conditions, bridging Earth-bound salvage to potential orbital/volatile-capture applications.

**Cross-Module & Leviathan Tie-ins**

- `leviathan_testing.md` — Primary testbed: underwater bubble-column variants, swarm-scale divergent aeration/recovery ops, sensor fusion for plume monitoring.  
- `Component_Triage_System.md` — Feedback from scrubber chemistry (e.g., captured volatiles/particulates) refines classification heuristics for marine artifacts.  
- `Trajectories_LF.md` — Updated paths for gas/liquid byproducts during lift-bag assisted recovery or in-situ electrolysis.  
- `energy_v0.md` — Aggregate swarm data refines modest-draw estimates (50–150 W baseline) under pressure-variable loads.  
- `Spin_Chamber_v0.md` / `Stratification_Chamber_v0.md` — Exhaust routing tests in wet environments; potential centrifugal pre-separation before scrubbing.  
- `geck_forge_seed.md` — Bootstrap minimal scrubber seeds for swarm self-deployment in remote tests.  
- `Ship_of_Theseus_Right_to_Repair.md` — Scrubber as a "preservation enabler" during marine artifact recovery, delaying irreversible corrosion.

**Next Steps / Planned**

- Prototype pressure-rated diffuser payloads for Leviathan proxies.  
- Simulate bubble dynamics (e.g., via open-source hydro tools) before lake/ocean drops near Jonesboro-area watersheds.  
- Open issues for community input on fine-bubble variants or electrolytic preconditioning add-ons.  
- Field test small-scale bubble-column in controlled tank/lake environment to baseline mass transfer rates.  
- Explore integration with electrolytic stages for combined gas scrubbing + metal ion capture.

Last updated: February 01, 2026

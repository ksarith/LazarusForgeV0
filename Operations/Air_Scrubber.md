# Air_Scrubber.md
> ⚠️ **Operational Safety Advisory**
> The Air Scrubber handles toxic, corrosive, and carcinogenic airborne byproducts generated during Forge operation. Saturated scrubbing liquid passes contaminants directly to exhaust — a Saturation Fault while reporting "Airflow OK" is the most dangerous failure mode. Continuous fan and compressor operation produces sustained noise levels capable of causing permanent hearing damage and masking fault signals; hearing protection is required during operation and maintenance. The scrubber operates under negative pressure — loss of airflow draws hazardous air outward. Saturation thresholds are bound to the differential sensor matrix; apply the most conservative interpretation until calibrated. **When in doubt, shut down. The Forge does not run if the scrubber cannot verify safe operation.**
> 
## File State
| Field | Value |
|---|---|
| Status | Draft |
| Body Stability | Transitional |
| Spec Gates | 3/6 |
| Verification Ref | Verification_Gates_LF.md |
| Last Audit | 2026-05-31 |
| Auditor | Gemini |
| Open Unknowns | 3 |
| Active Disputes | 0 |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
## Scope Boundary
**This file DOES define:**
 * Air Scrubber design philosophy and doctrine.
 * Five-stage functional architecture (Stages A through E) augmented with fractional condensation and chemisorption layers.
 * Wet capture variants (Variant 0 through Variant 4) including positive pressure variants.
 * Saturation Fault, Particulate Blinding, and Thermal Fault monitoring matrices.
 * Automated interlock and E-Stop triggers for safety boundaries.
 * Negative pressure safety boundary doctrine and flashback mitigation.
 * Noise hazard acknowledgment and hearing protection requirements.
 * Energy awareness and power budget estimates.
 * Waste as a managed output.
 * Integration hooks to upstream and downstream modules.
**This file DOES NOT define:**
 * Spin Chamber exhaust heat load (→ Operations/Gate_05_Separation_Thermal.md).
 * Forge power budget and demand baseline (→ Operations/Energy.md).
 * Deep-sea compression modules (→ Admin/Trajectories.md v2/v3).
 * Contamination routing and waste stream final disposition (→ Operations/Gate_02_Triage.md).
 * Scrubber bootstrap minimum for remote deployment (→ Architecture/Geck_forge_seed.md).
 * Noise exposure limits and formal hearing conservation program (→ planned Safety_Protocols.md).
## File Purpose
This file defines the design doctrine, functional architecture, and operational requirements for the Air Scrubber subsystem of the Lazarus Forge. The scrubber is an enabling system — without it, the Forge does not operate. Its purpose is to prevent release, accumulation, or uncontrolled transformation of hazardous airborne byproducts generated during Forge operation. If this file disappeared, operators would lack the doctrine required to design, operate, and maintain the safety boundary that makes all other Forge operations permissible.
## Assumptions
| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Surface and shallow-water variants operate within 500W total system draw | Analogous — industrial scrubbers | Medium | First measured power draw from operational prototype |
| ASM-002 | Variant 4 marine scope is limited to less than 5 atm / 50m depth at v0 power class | Compression work calculation | High | Dedicated high-output compression module available |
| ASM-003 | Negative pressure operation is achievable with salvaged fan/compressor hardware | Analogous — industrial practice | Medium | First prototype demonstrates achievable differential |
| ASM-004 | Thermal sink can be sized to Spin Chamber exhaust load at v0 | Placeholder — exhaust load unknown | Low | Gate_05_Separation_Thermal.md exhaust characterization |
| ASM-005 | Noise from continuous fan/compressor operation exceeds safe exposure limits without PPE | Analogous — industrial fan noise levels | High | Measured SPL confirms otherwise |
## Design Philosophy
**1. Capture Is Part of Production**
All Forge processes assume byproduct generation. The Air Scrubber is a continuation of the production path, not a cleanup step. Every mode assumes containment.
**2. Interaction Is Forced, Not Hoped For**
Airflow is deliberately manipulated to increase residence time and convert mobile hazards into capturable forms.
**3. Condense, Charge, Cool, Then Capture**
Drop heavy fractions via fractional condensation loops to protect downstream media → impart a charge to airborne species to encourage agglomeration → cool the gas stream to reduce volatility → capture into liquid or solid phases.
**4. Negative Pressure as a Safety Boundary**
The scrubber operates under slight negative pressure relative to surroundings. Leaks draw air inward. Loss of airflow is a critical fault. The Forge defaults to shutdown rather than uncontrolled exhaust.
**5. Defeat the Bypass (True Saturation Monitoring)**
A scrubbing system that has reached saturation while reporting "Airflow OK" is not a scrubber — it is a bypass. The system must monitor scrubbing liquid quality alongside differential gas-phase analysis (Pre- vs. Post-filter) to trigger automated interlocks before chemical bypass occurs.
**6. Noise Is a Hazard, Not a Side Effect**
Continuous fan and compressor operation produces sustained noise levels capable of causing permanent hearing damage and masking critical fault signals. Hearing protection is required during all scrubber operation and maintenance. Fault signal audibility must be verified against ambient noise floor.
## Functional Architecture
```
[Incoming Gas Stream] 
        │
        ▼
 ┌───────────────┐
 │    Stage A    │ ──► Sacrificial Mechanical Intercept (Coarse Particulates / Cyclones)
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage B    │ ──► Ionization / Electrostatic Conditioning
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage C    │ ──► Thermal Quench / Fractional Condensation Loop
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage D    │ ──► Wet Scrubbing / Water Column (Requires explicit Thermal Sink Interface)
 └───────────────┘
        │
        ▼
 ┌───────────────┐
 │    Stage E    │ ──► Polishing / Chemisorption Media (Activated GAC + KMnO₄ Bed)
 └───────────────┘
        │
        ▼
 [Safe Exhaust]

```
### Stage A — Sacrificial Mechanical Intercept
Captures coarse particulates and debris. Protects downstream stages. Designed for frequent replacement and treated as expendable. Includes mechanical cyclone separation when dealing with high particulate loads.
### Stage B — Ionization / Electrostatic Conditioning
Imparts charge to particulates, aerosols, and vapors to encourage agglomeration and surface attachment. Ionization energy is moderated. Ozone or unintended reactive species are monitored as fault conditions.
### Stage C — Thermal Quench / Fractional Condensation Zone
Rapidly lowers gas temperature to encourage condensation of semi-volatile compounds.
> 🧪 **Hardware Precedent — The Condensation Prerequisite**
> Hardware deployment data indicates that direct-to-carbon routing of pyrolysis outgassing causes instantaneous tar blinding of the filter media. A multi-stage fractional condensation loop (cyclone separator or chilled fluid condenser) **must** precede the chemical scrubbing phase to drop out heavy oil fractions, paraffins, and waxes.
> 
### Stage D — Wet Scrubbing / Water Column
Absorbs soluble gases and captures charged/agglomerated particulates. Water is operated in a recirculating loop with continuous chemical monitoring.
 * **Thermal Sink Requirement:** Hot exhaust from the Spin Chamber transfers heat to scrubbing water. Stage D requires an explicit, ruggedized **thermal sink interface** (heat exchanger, radiator, or passive cooling surface) sized to the expected exhaust heat load.
 * **Corrosion Isolation:** Wet venturi or water-bubbler stages handling exhaust from halogenated materials must utilize heavy-walled high-density polyethylene (HDPE) or 316L stainless steel hulls to resist accelerated hydrochloric acid pitting.
### Stage E — Polishing / Last-Chance Chemisorption Bed
Captures residual contaminants that escape primary stages.
> 🧪 **Hardware Precedent — Chemisorption Overrides**
> Standard granular activated carbon (GAC) exhibits poor retention for light-fraction toxic syngas components (e.g., carbon monoxide, formaldehydes, methane). Where high-temperature reduction or synthetic polymer processing is active, the final stage dry-bed **must** integrate an active chemisorbent media, such as alumina impregnated with potassium permanganate (KMnO_4), to permanently chemically neutralize low-molecular-weight VOCs.
> 
## Mechanical & Physical Safety Additions
 * **Anti-Flashback Assemblies:** All lines routing non-condensable syngas or pyrolysis outgassing back into process furnaces or flares must feature a verified dual-mesh inline explosion-proof flashback arrestor to prevent flame propagation back into the air scrubber assembly.
 * **Containment Enclosure:** All high-pressure fittings and liquid sumps must reside inside a co-contained workspace pan to capture liquid overflow or secondary gas leakages.
## Wet Capture Variants
### Variant 0 — Positive Pressure Enclosure Protection (Simplest)
The pressure-differential principle works in both directions. Where primary scrubbing uses negative pressure to contain hazards inside a process box, positive pressure protects a clean operator or instrument space by pushing air outward through every structural gap — dust and contaminants must fight the outward velocity to enter.
 * **Applications:** Operator cab or control room in a dusty Forge environment; critical electronics enclosures.
 * **Implementation:** A blower draws ambient air through a multi-stage filter (coarse pre-filter protecting a finer main filter) and pressurizes the protected space. The protected space utilizes controlled exits (door seals, pressure relief vents) to maintain differential without over-pressurizing.
### Variant 1 — Aerated Pond-Style Bubbler (Baseline)
Simple tank with a submerged porous diffuser. Gas is forced through water via fine bubbles. Prioritizes simplicity, robustness, and ease of inspection. **Primary v0 baseline.**
### Variant 2 — Packed Column with Recirculation (Intermediate)
Vertical column with random packing or salvaged scrub media. Counter-current gas–liquid contact provides higher efficiency with a modest increase in system pressure drop.
### Variant 3 — Conditioned Intake + Wet Polish (Future)
Upstream ionization stage feeds a wet stage used primarily for capture and quench. Reserved for high-energy or highly variable feeds.
### Variant 4 — Shallow-Depth Marine Bubble-Column (Near-Term Marine)
Scoped strictly to shallow water (less than 5 atm / ~50m depth) for v0. Deep-sea variants route directly to Trajectories target milestones.
 * Inject compressed air through pressure-rated submerged diffusers.
 * Aerate low-dissolved-oxygen (DO) water and capture volatiles (H_2S, CO_2) at the surface.
 * Onboard sensors track real-time pH, DO, turbidity, and gas composition.
 * Target bubble sizes: 80–500 μm.
 * Column depth: 1–3 m.
 * **Quantitative Targets:** 10–30% DO saturation increase in less than 2 mg/L hypoxic water; energy draw less than 100 W per 1–2 m³ plume.
## Energy Awareness
Conceptual ballpark ranges (non-binding, Earth surface standard conditions):
 * Fan/compressor draw: 50–150 W
 * Ionization stage: 10–30 W
 * Wet-stage recirculation: 20–80 W
 * Thermal sink (heat exchanger / radiator): Sized dynamically to Spin Chamber exhaust heat load.
**Goal:** Maintain less than 500 W total system draw for surface and shallow-water variants. Deep-sea variants are a separate power class.
## Sensor Layout & Automated Failure Interlocks
The scrubber uses a multi-point differential diagnostic grid. If the scrubber cannot verify safe operation via this matrix, the Forge core triggers an automated shutdown sequence.
| Diagnostic Metric | Detection Method | Actionable System Threshold | Automated Interlock Trigger |
|---|---|---|---|
| **Media Saturation** | Dual VOC PID Sensors (Pre- vs. Post-Filter Differential) | Efficiency drop to less than 85% capture | Trigger **System Fault 04**; Halt downstream heating elements; Force auxiliary air bypass. |
| **Particulate Blinding** | Differential Pressure (\Delta P) Transducers across HEPA/Carbon pack | \Delta P \ge 450 \text{ Pa} over clean baseline | Trigger **Filter Restriction Alert**; Initiate automated mechanical shaker or lock out milling spindle. |
| **Acidic Ingress (HCl/HF)** | Post-scrubber electrochemical gas sensor / pH probe in wet sumps | Sump pH less than 5.5 or Exhaust greater than 5 ppm | Instantaneous **E-Stop Lockout** of Pyrolysis Reactor core. |
| **Thermal Saturation** | Thermocouples in Stage D liquid core | Temperature exceeds rated fluid threshold | Trigger **Thermal Fault**; Divert feedstocks away from primary thermal reduction units. |
| **Noise Fault Masking** | Ambient microphone calibration check | Alarm audio margin less than 10 dB above operating noise floor | Flash high-intensity visual strobes; Flag system failure to supervisory network layer. |
## Waste as a Managed Output
Captured materials are not disposable nuisances.
 * Liquids, sludges, and solids are routed into controlled handling paths.
 * Sump chemical composition is monitored as a primary diagnostic signal.
 * **Disposition:** (1) test for reuse potential; (2) if hazardous, immobilize per applicable regulations; (3) if inert, route to bulk material recovery.
## Compatibility With Autonomous Operation
The Air Scrubber is designed to operate continuously without manual tuning, provide clear health signals to supervisory systems, and fail into containment rather than release. Human oversight is optional; stewardship is not.
## Integration Hooks
 * Operations/Gate_05_Separation_Thermal.md — Primary exhaust source; thermal load on Stage D sized to Spin Chamber output.
 * Operations/Gate_04_Separation_Mechanical.md — Pre-purification separation exhaust source.
 * Tests/Leviathan_testing.md — Testbed for shallow-water marine variants.
 * Operations/Gate_02_Triage.md — Scrubber chemistry feedback refines classification heuristics; contamination handling cross-reference.
 * Operations/Energy.md — Aggregate data refines draw estimates; thermal sink power inclusion.
 * Architecture/Geck_forge_seed.md — Bootstrap minimal scrubber for remote deployment.
 * Admin/Ship_of_Theseus.md — Scrubber as preservation enabler during artifact recovery.
## Summary Doctrine
The Air Scrubber is not a filter. It is a boundary system that forces hazardous matter into managed forms, prevents accidental chemistry, and makes responsible operation possible at scale.
A Forge that cannot clean up after itself is incomplete by definition. And a scrubber that does not know when it is full is a liability.
## Lessons Learned
| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| May 2026 | Modeling | Variant 4 marine claimed 10–100 atm range with 20–50% power uplift | Physically untenable — isothermal compression to 100 atm requires massive work; 150W compressor cannot overcome hydrostatic pressure | Deep-sea compression is a separate power class. v0 marine variants cap at less than 5 atm. | Analogous | Yes |
| May 2026 | Audit Review | Stage D described without thermal sink | Hot exhaust heats scrubbing liquid until it cannot quench — hidden failure mode | Thermal sink is not optional; must be explicitly sized to exhaust heat load | Analogous | Yes |
| May 2026 | Anecdotal | Positive pressure insight from dusty-environment cab filtration | Cabin filters fail rapidly under high dust load without pre-filter | Sacrificial pre-filter protecting main filter dramatically extends service life; positive pressure enclosure protection is Variant 0 | Analogous | Yes |
| 2026-05-23 | Audit Review | Noise hazard absent from prior versions | Continuous fan/compressor noise omitted from safety doctrine despite known industrial hearing damage risk | Noise added to Safety Advisory, Design Philosophy, and Monitoring sections. Fault alarm audibility verification added | Analogous | Yes |
| 2026-05-31 | Field Data / Audit | Raw direct-to-carbon routing of pyrolysis outgassing | Instantaneous tar blinding of activated carbon media from heavy oil fractions, paraffins, and waxes | A multi-stage fractional condensation loop must precede chemical scrubbing to knock down heavy fractions. | Empirical | No |
## Active Disputes
| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| — | No active disputes | — | — | — | — |
## Abandoned Paths
| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| May 2026 | Variant 4 deep-sea scope at v0 power class | Compression work to 100 atm is physically untenable at 100–150W; separate power class required | Yes — at v2/v3 |
| May 2026 | Stage D without explicit thermal sink specification | Hidden failure mode — water heats to ineffectiveness without thermal rejection path | No |
## Drift Indicators
Mandatory re-audit conditions for this document:
 * Saturation Fault monitoring requirement removed, bypassed, or decoupled from the differential PID sensor matrix.
 * Negative pressure safety boundary doctrine weakened or removed.
 * Flashback arrestor requirements omitted from combustible outgassing lines.
 * Thermal sink requirement removed from Stage D.
 * Noise hazard removed from Safety Advisory, Design Philosophy, or Monitoring sections.
 * 500W power budget claimed as validated without active power measurement data.
 * Variant 4 depth scope expanded beyond less than 5 atm without an autonomous power class reallocation.
**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.
## Auditor Notes & Unknowns
### AS-001 — 500W power budget not validated against Forge demand baseline
 * **Status:** Open | **Risk:** Medium | **Priority:** Major
 * **Description:** Whether 500W worst-case scrubber draw (surface/shallow variants) is compatible with Forge power budget at bootstrap and nominal modes. Thermal sink power is not yet validated in this loop.
 * **Resolution Path:** Cross-reference against Operations/Energy.md Power Demand stub. Flag if scrubber + thermal sink exceeds 20% of bootstrap budget.
### AS-002 — Marine bubble-column depth scope corrected; deep-sea variant deferred
 * **Status:** In Progress | **Risk:** Low | **Priority:** Minor
 * **Description:** Detailed specification for deep-sea Variant 4+ (greater than 50m / 5 atm) remains undefined.
 * **Resolution Path:** Deep-sea variant routes to Admin/Trajectories.md v2/v3 as a separate power-class problem requiring a dedicated compression module.
### AS-003 — Scrubber waste stream and sensor thresholds finalized
 * **Status:** In Progress | **Risk:** Medium | **Priority:** Major
 * **Description:** Saturation thresholds have been successfully bound to a multi-point differential diagnostic grid (PID VOC, \Delta P, and Sump pH). Real-world chemical baseline data is now required to clamp the operational float margins.
 * **Resolution Path:** Run automated calibration sweeps during first hot-pyrolysis validation testing to map clean baseline deltas.
### AS-004 — Noise exposure limits and hearing conservation program undefined
 * **Status:** Open | **Risk:** Medium | **Priority:** Major
 * **Description:** Continuous fan and compressor noise levels have not been empirically characterized. No formal hearing conservation program or exposure metrics exist for scrubber operations.
 * **Resolution Path:** Measure SPL at operator positions during scrubber operation. Verify fault alarm audibility against measured noise floors. Formal hearing conservation program routes to planned Admin/Security_Protocols.md or a dedicated Admin/Safety_Protocols.md.
## Resolution Log
 * **2026-05-04:** Stratification_Chamber_v0.md reference removed. Material_Separation_Gate_v0.md substituted.
 * **2026-05-06:** Variant 4 depth scope corrected from 10–100 atm to less than 5 atm for v0. Deep-sea variants routed to Trajectories.md. Magic Energy fallacy resolved for v0 scope. Thermal sink requirement added to Stage D. Saturation Fault monitoring requirement added to Stage D and Monitoring sections. Variant 0 (Positive Pressure Enclosure Protection) added.
 * **2026-05-23:** Retrofit to File_Template.md structure. File State table, Scope Boundary, Assumptions, Abandoned Paths, Drift Indicators sections added. Noise hazard added to Safety Advisory, Design Philosophy Principle 6, Monitoring section, and AS-004 sidecar entry. All integration hook references updated to canonical folder-prefixed paths.
 * **2026-05-31:** Integrated Amendment and Field Note addenda into core body. Stage C updated with fractional condensation prerequisite; Stage E updated with chemisorption media mandates (KMnO_4). Bound AS-003 to an explicit automated interlock sensor matrix. Added flashback arrestors and corrosion isolation material updates. Cleaned double-hash headers. Promoted Spec Gate tracking to 3/6.


---


To advance Air_Scrubber.md toward **Spec Gate 4 (Component-Level Cold Verification)**, we must transition from conceptual thresholds to an explicit, step-by-step physical testing protocol. This harness treats the sensor matrix as an adversarial system — we must intentionally simulate worst-case failures under zero-process conditions to verify that the software loops and hardware relays perform as fail-safes before hot operation is permitted.
# Air Scrubber Cold Verification Harness (Gate 4 Protocol)
This protocol governs the physical and logical verification of the differential diagnostic grid defined in Air_Scrubber.md. Testing must be performed in sequence, using non-hazardous surrogates, with the primary Forge heating elements and feedstock intake mechanically and electrically isolated.
## Pre-Test Safety & Harness Setup
Before executing any sensor verification loop:
 1. **Isolate Power Hooks:** Physically disconnect the main power lines to the Pyrolysis Reactor core heaters and the milling spindle. Verify air scrubber fan/compressor power is routed through the secondary safety relay loop.
 2. **PPE Baseline:** Full face shield and nitrile gloves are mandatory during wet sump adjustments.
 3. **Log Initialization:** Initialize AUDIT_HARNESS.py in listen-only mode to capture real-time state transitions on the local bus.
## 1. Step-by-Step Verification Checklist
### Protocol 1.1 — Media Saturation Interlock (VOC PID)
This test verifies the dual photoionization detector (PID) differential capture logic without generating toxic outgassing.
 * [ ] **Step 1 (Baseline Verification):** Power on the primary air scrubber fan. Verify that Sensor_VOC_Pre and Sensor_VOC_Post settle within \pm 2\% of each other in ambient air. Check that the control layer reads System Status: Nominal.
 * [ ] **Step 2 (Surrogate Injection):** Introduce a controlled hydrocarbon surrogate (e.g., exposing an open container of isopropyl alcohol near Stage A's intake manifold).
 * [ ] **Step 3 (Differential Calibration):** Monitor the live bus telemetry. Confirm that Sensor_VOC_Pre spikes immediately while Sensor_VOC_Post remains flat, proving the downstream polishing media is active.
 * [ ] **Step 4 (Fault Simulation):** Artificially force a saturation bypass state. Place a secondary surrogate source directly at the Stage E exhaust sensor to simulate breakthrough efficiency dropping below 85%.
 * [ ] **Step 5 (Interlock Check):** Verify that the system registers **System Fault 04** within < 500\text{ ms}. Confirm that the control loop opens the primary safety relay, immediately cutting simulation power to downstream heating elements.
### Protocol 1.2 — Particulate Blinding Interlock (\Delta P)
This test verifies that the differential pressure transducers accurately flag filter restriction before an over-pressure event occurs.
 * [ ] **Step 1 (Upstream / Downstream Baseline):** Read the static pressure across the HEPA/Carbon pack with the fan running at max RPM. Record the clean baseline differential (\Delta P_{clean}).
 * [ ] **Step 2 (Restriction Simulation):** Restrict airflow to Stage E by gradually blocking the face of the filter chamber using an inert, non-porous template plate.
 * [ ] **Step 3 (Alert Threshold):** Monitor the pressure transudcer output. Verify that when \Delta P increases to \ge 450\text{ Pa} over \Delta P_{clean}, a **Filter Restriction Alert** fires on the local operator display.
 * [ ] **Step 4 (Actuator Loopback):** Confirm that the system automatically sends a pulse train to the automated mechanical shaker assembly (if equipped) or flags an immediate lockout command to the milling spindle bus.
 * [ ] **Step 5 (Reset Check):** Remove the restriction template. Verify the differential pressure drops back to baseline and the alert state auto-clears within 3\text{ seconds}.
### Protocol 1.3 — Acidic Ingress Interlock (Sump pH & Gas Phase)
This test verifies that the system can protect its own structural hull from chemical degradation caused by halogenated polymers.
 * [ ] **Step 1 (Sump Calibration):** Calibrate the Stage D wet sump pH probe using standard reference buffer solutions (\text{pH } 4.0 and \text{pH } 7.0). Re-insert the probe into the recirculating fluid loop.
 * [ ] **Step 2 (Acid Injection):** Using a precision pipette, slowly introduce a 0.1\text{M } HCl solution directly into the Stage D sampling well to simulate acidic bypass.
 * [ ] **Step 3 (E-Stop Trigger):** Observe the telemetry bus. The moment the reading dips below \text{pH } 5.5, the system must execute an instantaneous **E-Stop Lockout**.
 * [ ] **Step 4 (Line Isolation):** Verify via multimeter that the Pyrolysis Reactor core main power contactor has dropped open. The contactor must open physically and latch into a locked state; software-only overrides are a failure.
 * [ ] **Step 5 (Neutralization Test):** Add an alkaline buffering agent (e.g., sodium carbonate) to return the sump to \text{pH } 7.0. Verify that the system *prohibits* a clear-fault command until a manual operator attestation code is entered.
### Protocol 1.4 — Noise Fault Masking Interlock
This test ensures that acoustic alarms remain completely audible above the massive ambient drone of the high-velocity fan and compressor units.
 * [ ] **Step 1 (Noise Floor Measurement):** Fire up all fan, pump, and compressor modules to maximum operating velocity. Place a calibrated sound level meter at the primary operator station. Record the baseline dBA level.
 * [ ] **Step 2 (Acoustic Injection):** Use an integrated test function to fire the audible emergency alarm horn.
 * [ ] **Step 3 (Audibility Check):** Measure the combined acoustic output. The alarm signal must maintain a strict minimum margin of \ge 10\text{ dBA} above the operating noise floor recorded in Step 1.
 * [ ] **Step 4 (Optical Redundancy):** While the alarm is firing, verify that high-intensity visual strobes activate across all facility quadrants simultaneously.
 * [ ] **Step 5 (Supervisor Attestation):** Unplug the primary horn to simulate an acoustic alarm failure mode. Verify that the local microphone detects the missing signal, instantly flagging a network supervisor warning.
## 2. Test Execution Matrix
Use this table to record physical verification cycles before updating the file state metadata to Spec Gate 4.
| Test ID | Targeted Interlock | Expected Software State | Hardware Action Verified? | Response Latency | Pass / Fail |
|---|---|---|---|---|---|
| **V4-AS-01** | VOC Breakthrough (<85\%) | System Fault 04 | Heating Relay Drops Open | ________ ms | [ ] P  [ ] F |
| **V4-AS-02** | Pressure Blinding (\ge 450\text{ Pa}) | Filter Restriction Alert | Spindle Lockout Active | ________ ms | [ ] P  [ ] F |
| **V4-AS-03** | Sump Acid Ingress (\text{pH } < 5.5) | Core E-Stop Lockout | Contactors Mechanically Tripped | ________ ms | [ ] P  [ ] F |
| **V4-AS-04** | Alarm Audibility Margin (<10\text{ dB}) | Acoustic Masking Warning | Visual Strobes Triggered | ________ ms | [ ] P  [ ] F |
## 3. Post-Verification Action
If all four protocols achieve a **Pass** status:
 1. Append this verified checklist data to the Verification_Gates_LF.md log tracking repository.
 2. Update the Spec Gates field in the Air_Scrubber.md header from 3/6 to 4/6.
 3. Shift the document's body stability classification from Transitional to Frozen.

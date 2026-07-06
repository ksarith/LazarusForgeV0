# Challenges/Closed_Loop_Feedstock.md

## Navigation Anchors
* **Context Core:** [Discovery.md](../Discovery.md)
* **Network Routing:** [Routing.md](../Routing.md)
* **Manifest Link:** [Manifest.md](../Manifest.md)

## File State
| Attribute | Value |
| :--- | :--- |
| **Status** | Active / Core Doctrinal |
| **Version** | v0.2.0 |
| **Ethical Anchor** | Anti-fragility via localized material agency |
| **Highest Risk** | Epistemic failure leading to toolhead destruction |
| **Last Audit** | 2026-07-06 |

---

> *"The Forge optimizes for the closure of loops, not the purity of outputs. A crude loop that stays closed is infinitely superior to a pristine process that relies on a ghost supply chain."*

## 1. The Crisis: The Illusion of Material Autonomy
Every advanced fabrication node in the legacy industrial paradigm relies on a hyper-optimized, low-entropy upstream supply chain. 3D printers demand highly geometric, chemically pure filaments; machining centers require precisely alloyed bars. 

If the Forge requires pristine, pre-refined inputs to operate, its External Flux ($\Phi_{\text{ext}}$) remains fatally high. True persistence requires closing the material loop locally, transforming unpredictable salvage into functional inputs while minimizing the consumption of internal resources.

## 2. Scope Boundary
* **What This File Owns:** The definition of the Persistence Yield ($Y_p$) telemetry model, cross-gate coordination heuristics, and the overarching engineering pressures governing salvage conversion.
* **What This File Defers:** Specific mechanical sorting mechanisms (defers to `Gate_04/05_Separation`), toolpath generation adjustments (defers to `Architecture/Characterization.md`), and specific thermal melt parameters (defers to `Architecture/Thermal_Systems.md`).

## 3. System Dependencies

| Upstream Dependencies | Downstream Targets |
| :--- | :--- |
| `Architecture/Characterization.md` (What is this?) | `Operations/Gate_06_Fabrication.md` |
| `Gate_03_Reduction.md` (Physical breakdown) | `Operations/Plastics.md` (Filament/Pellets) |
| `Architecture/Chemistry.md` (Reagent limits) | `Operations/Metals.md` (Wire/Ingot/Wire-arc) |

## 4. Telemetry: The Persistence Yield ($Y_p$)
Progress toward true autonomy is tracked by the product of material independence and process sustainability:

$$Y_p = FIR \times PIR$$

### A. Feedstock Independence Ratio (FIR)
$$FIR = \frac{M_{\text{salvaged}}}{M_{\text{total}}}$$
Measures the percentage of absolute material mass derived from salvaged, un-refined streams vs. virgin imports.

### B. Process Independence Ratio (PIR)
Measures what the regeneration process itself consumes. A high PIR indicates zero chemical dependencies, minimal tool wear, low human labor overhead, and entirely localized energy harvesting.

The Forge dynamically balances its operational profiles to maximize $Y_p$. High-purity processes that drain finite chemical stores are systematically deprioritized in favor of robust, "good-enough" mechanical loops.

## 5. The First Recursive Loop: Epistemic Ascent
The foundational loop of the Forge is not manufacturing—it is **measurement**. The architecture progressively improves its capability via an information feedback loop:

1. **Characterize:** Utilize low-tier sensors to assay unknown salvage.
2. **Reduce & Process:** Extrude or cast a "good enough" feedstock batch based on low-certainty data.
3. **Fabricate:** Build higher-fidelity sensors, optical array components, and testing rigs using Generation-N feedstock.
4. **Upgrade:** Integrate those new sensors back into the `Architecture/Characterization.md` pipeline to drastically tighten the certainty profiles of Generation-N+1 salvage loops.

## 6. Open Unknowns (Registered via Unknowns.md)
* **UNK-021:** Blending ratios and thermal stabilizer baselines for un-refined, mixed-source polymer streams.
* **UNK-022:** Minimal viable open-source reagents for non-destructive chemical spot testing of copper and aluminum alloys.
* **UNK-023:** Wear-tolerances of printed polymer nozzles when handling high-variance, particulate-heavy salvage feedstocks.

---
*Challenges/ files define problems and requirements. They do not freeze solutions. The Forge's answer to this challenge will evolve. The obligation it names will not.*

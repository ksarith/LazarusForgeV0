# Trophic_Forge.md
*Tests/Trophic_Forge.md*

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field | Value |
|---|---|
| Status | Exploration |
| Body Stability | Volatile |
| Spec Gates | 0/6 |
| Verification Ref | Admin/Verification_Gates_LF.md |
| Last Audit | 2026-06-14 |
| Auditor | Claude (Synthesizer), Gemini (Auditor), ChatGPT (Synthesizer), Grok (Synthesizer) |
| Open Unknowns | 9 |
| Active Disputes | 1 |
| Highest Risk | High |
| Sidecar Link | #auditor-notes--unknowns |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Trophic Forge concept and its organizing principle.
- The base loop architecture and node properties.
- Bootstrap sequence doctrine for salvage-first deployment.
- Proposed test parameters for each node.
- Open unknowns requiring resolution before any promotion consideration.
- Naming rationale and prior art questions.

**This file DOES NOT define:**
- Detailed LED array electrical specifications (see Operations/Energy.md and Electronics.md).
- Water purification doctrine for pond or condensate streams (see Tests/Living_Waters.md).
- Fish species selection as confirmed doctrine — proposed only, pending site context.
- Crop selection or agronomic practice — out of scope at current development interval.
- Atmospheric-scale effects of moisture extraction (explicitly out of scope).
- Any claim of tornado or severe weather mitigation — out of scope at all intervals.

---

## File Purpose

The Trophic Forge is a biological cascade architecture in which each system node performs a productive transformation and passes its outputs — including byproducts previously treated as waste — as inputs to one or more adjacent nodes. The system does not recycle waste; it has no waste category by design. Every output is a resource at a different trophic level.

This file exists to develop and test that concept within the Lazarus Forge philosophy: salvage-first, low external input, resilient under degraded conditions, scalable from minimal bootstrap to field-scale operation. It currently lives in Tests/ because the bootstrap sequence is unvalidated, prior art questions are open, and the minimum viable loop has not been demonstrated empirically. If validation succeeds, this file is the seed of a Biology/ domain analogous to Energy.md and Living_Waters.md.

Without this file, the biological dimension of resource recovery has no home in the repository and the four-domain resource architecture (energy, water, biology, atmosphere) cannot develop.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Phototactic insect yield from LED array is sufficient to meaningfully supplement fish feed | Analogous — commercial fish light studies show measurable biomass; Forge-scale unvalidated | Low | TF-001 empirical test result |
| ASM-002 | Fish waste N/P/K output is sufficient to produce measurable crop fertilization effect | Analogous — aquaponics literature; specific species and stocking density unconfirmed | Low | TF-003 nutrient measurement |
| ASM-003 | Edge vegetation phytoremediation closes the water loop without auxiliary filtration | Analogous — rice-fish systems, constructed wetlands literature | Low | TF-005 water quality test |
| ASM-004 | Salvaged LED arrays can be configured to target UV/blue spectrum at adequate intensity | Analogous — salvaged hardware feasibility; wavelength tunability unconfirmed | Medium | Component audit of available salvage stream |
| ASM-005 | Loop degrades gracefully under single-node failure rather than collapsing | Structural inference from network topology; not empirically tested | Low | Stress test TF-007 |

---

## Body

### Organizing Principle

A Trophic Forge is a directed biological network, not a linear cascade and not a simple closed loop. Flows have preferred directions, but feedback paths exist at every node. Each node is independently productive. The failure of any single node degrades system output but does not propagate to collapse — this is the resilience claim that most requires empirical validation.

The defining property that distinguishes a Trophic Forge from standard aquaponics, tri-trophic systems, or closed-loop agriculture:

> **The system ignites at the light node.** Energy enters as light; wild insect biomass exits as the first harvest. No purchased feed input is required from day one. Every subsequent node is fueled by the productive output of the previous node with no external supplementation at steady state.

This is an architectural claim, not a validated fact. It is the hypothesis the Tests/ phase exists to test.

---

### The Base Loop

```
Light (UV/blue LED array — ignition node)
      ↓
Insect biomass (phototaxis harvest — free protein, pest suppression byproduct)
      ↓
Fish production (insect → feed; zero purchased feed at steady state target)
      ↓
Nutrient-rich water (fish waste → N, P, K)
      ↓
Crop fertilization + irrigation (pond water → field)
      ↓
Phytoremediation (crops + edge vegetation → filtered return water)
      ↓
Pond replenishment ←─────────────────────────────────────────────────────┘
```

---

### Node Properties

| Node | Primary Output | Secondary Output | Salvage Entry Point |
|---|---|---|---|
| Light array | Insect attraction and harvest | Pest pressure reduction in adjacent fields | Salvaged LEDs, wiring, small power source |
| Insect harvest | Fish feed biomass | Poultry supplement; compost input | Mesh collection surfaces, salvaged screen |
| Fish production | Harvestable protein | Nutrient-rich water | Pond liner (salvaged HDPE or tarp) |
| Nutrient water | Crop fertilization | Reduced synthetic input cost | Salvaged irrigation pipe |
| Crop + edge vegetation | Food / fiber | Filtered return water | Existing field infrastructure |
| Filtered water | Pond replenishment | Cleaner local water table | Gravity return or minimal pump |

---

### Bootstrap Sequence

The loop is not built all at once. Each node provides leverage to justify the next. In a salvage-first, resource-constrained Forge context, the correct build order is:

**Stage 1 — Light → Insect node**
Minimal salvage requirement: LEDs, wiring, small power source (battery or solar panel fragment). Can be operational within days of decision. Immediately yields free high-protein biomass. Proves the phototaxis harvest concept before any further investment is committed.

**Stage 2 — Insect → Fish node**
Demonstrated biomass yield from Stage 1 justifies pond construction and fish stocking. The feed problem is solved before fish arrive. Pond liner from salvaged HDPE sheet or reinforced tarp. Native or locally available species preferred over purchased stock.

**Stage 3 — Fish → Nutrient node**
Once fish are producing waste at measurable rates, irrigation infrastructure follows demonstrated nutrient yield. Avoids building irrigation for a fertilization effect that has not yet been confirmed at Forge scale.

**Stage 4 — Nutrient → Crop → Filtration → Pond**
Closes the loop. Edge vegetation phytoremediation returns water to the pond. Full loop operation begins. Stage 4 is the first point at which the Trophic Forge claim — zero external feed input at steady state — can be evaluated empirically.

Each stage is independently useful before the next stage exists. Value accrues at every construction step, not only at loop completion.

---

### Distinction from Prior Art

| System Type | Feed Input | Light Node | Forge Compatibility |
|---|---|---|---|
| Standard aquaponics | Purchased pellet feed | No | Low — consumable dependence |
| Black Soldier Fly tri-trophic | Organic waste feedstock | No | Medium — waste-stream dependent |
| Rice-fish systems | Supplemental feed common | No | Medium — crop-specific |
| **Trophic Forge** | **Zero at steady state (target)** | **Yes — ignition node** | **High — salvage-first throughout** |

The LED/phototaxis ignition node is the architecturally distinctive claim. It is also the least validated element. Empirical test of this node is the highest priority in the test sequence.

---

### Proposed Test Parameters

**TF-TEST-001 — Phototaxis Yield Baseline**
Measure actual insect biomass captured per night per unit of LED power input (kg/kWh) across species composition, humidity, temperature, and moon phase conditions. Establish minimum viable yield threshold required to sustain target fish population without supplemental feed.
*Confidence target: Measured.*

**TF-TEST-002 — LED Wavelength Optimization**
Compare insect capture yield across UV (365 nm), blue (450 nm), and mixed spectrum arrays. Characterize non-target capture rate (pollinators, beneficial predators). Establish optimal wavelength or combination that maximizes pest-species yield while minimizing beneficial species impact.
*Confidence target: Measured.*

**TF-TEST-003 — Fish Nutrient Output Characterization**
Measure N, P, K concentration in pond water as a function of fish species, stocking density, and feed input rate. Establish whether nutrient output at Forge-scale stocking is sufficient to produce measurable crop yield improvement over unfertilized control.
*Confidence target: Measured.*

**TF-TEST-004 — Zero External Feed Threshold**
Determine minimum insect biomass yield (kg/night) required to maintain fish population at stable weight with zero supplemental feed. This is the empirical test of the core Trophic Forge claim.
*Confidence target: Measured — this is the gate test for the organizing principle.*

**TF-TEST-005 — Phytoremediation Return Water Quality**
Measure water quality (N, P, biological oxygen demand, pathogen indicators) of pond return water after passage through edge vegetation filtration. Confirm whether phytoremediation alone closes the loop or whether auxiliary filtration is required.
*Confidence target: Measured.*

**TF-TEST-006 — Minimum Viable Loop Scale**
Determine the smallest pond area, LED array size, and crop border length at which the full loop is self-sustaining. This defines the floor for Forge deployment planning.
*Confidence target: Simulated initially; target Measured.*

**TF-TEST-007 — Single Node Failure Propagation**
Simulate or induce failure of each node in turn (power loss to LED array, fish population loss, drought, crop failure). Measure how rapidly failure propagates to adjacent nodes and at what degradation level the loop can no longer recover without external input.
*Confidence target: Simulated initially; target Field Test.*

---

### Relationship to Repository Domains

The Trophic Forge is the biological analogue of the mechanical and thermal transformation systems elsewhere in the repository.

| Domain | File | Transformation Type |
|---|---|---|
| Energy | Operations/Energy.md | Electrical and thermal |
| Water | Tests/Living_Waters.md | Hydrological and chemical |
| Biology | Tests/Trophic_Forge.md (this file) | Biological and trophic |
| Atmosphere | *(declared future domain)* | Atmospheric |

**Interaction with Living_Waters.md:** The fish pond is a water system. Pond water quality, phytoremediation return, and condensate from LW-005a (atmospheric AWG) may all interact. The Trophic Forge does not own water purification doctrine — that remains with Living_Waters.md. Cross-reference is required at the pond node interface.

**Interaction with Energy.md:** The LED array is the ignition node and the primary ongoing power draw. Power sourcing, load profile, and degraded-mode operation of the light array are governed by Energy.md. The Trophic Forge owns the biological outputs of the light node; it does not own the electrical inputs.

**Declared Trajectory:** If Tests/ validation succeeds, this file promotes to a Biology/ domain folder. Biology/Trophic_Forge.md would anchor that domain the way Forge_flow.md anchors Architecture/. That promotion requires passage of all six spec gates and human ratification per Governance_Migration_Protocol.md doctrine.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|---|---|---|---|---|---|---|
| — | — | — | — | No entries yet — file is pre-empirical | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|---|---|---|---|---|---|
| DS-001 | Naming: Trophic Forge vs. Cascade Agriculture vs. Metabolic Agriculture | ChatGPT favors Metabolic (emphasizes matter cycling); Grok favors Cascade (emphasizes sequential conversion); Claude favors Trophic Forge (emphasizes biological transformation engine parallel to mechanical Forge). Prior art search not yet complete. | Low | Open | This file |

---

## Auditor Notes & Unknowns

### TF-001 — Phototaxis yield at Forge scale unvalidated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical |
| Blocking | Yes — blocks organizing principle validation |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** No empirical measurement exists of wild insect biomass yield per unit LED power input at Forge deployment scale.

**Why It Matters:** The entire Trophic Forge architecture rests on the claim that the light node produces sufficient biomass to sustain the fish node without purchased feed. If this claim fails, the organizing principle fails with it.

**Resolution Path:** Payment via Specification — TF-TEST-001 and TF-TEST-004 empirical results move to Body as committed parameters once measured.

---

### TF-002 — Prior art search incomplete

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** No search has been conducted for prior art under the names Trophic Forge, Metabolic Agriculture, Cascade Conversion Farming, or LED-ignited tri-trophic closed-loop aquaponics.

**Why It Matters:** If substantial prior art exists, the Trophic Forge may be a named concept with established literature, which would either validate or constrain the current architecture.

**Resolution Path:** Payment via Specification — search results incorporated into Distinction from Prior Art section; confirmed novel elements documented.

---

### TF-003 — Fish nutrient output at Forge stocking density uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — does not block Stage 1–2 bootstrap |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** N/P/K output from fish waste at expected Forge-scale stocking density has not been measured or modeled for target species.

**Why It Matters:** If nutrient output is insufficient to replace synthetic fertilizer inputs, Stage 3–4 of the bootstrap sequence requires external supplementation, weakening the zero-external-input claim.

**Resolution Path:** Payment via Specification — TF-TEST-003 measurement results.

---

### TF-004 — Species selection not determined

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks Stage 2 optimization, not Stage 1 |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Fish species for the production node has not been selected. Native species, tilapia, catfish, and perch all have different feed conversion ratios, nutrient output profiles, temperature tolerances, and regulatory constraints by location.

**Why It Matters:** Species selection determines nutrient output, feed conversion efficiency, and legal viability in a given Forge location. Site context governs this decision — there is no universal answer.

**Resolution Path:** Discharge via Trajectory — species selection is site-conditioned. A decision matrix will be added to Body once site context is known. Remains open until first deployment site is confirmed.

---

### TF-005 — Phytoremediation loop closure unvalidated

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No — blocks Stage 4 only |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** Whether edge vegetation phytoremediation alone can return water to pond-suitable quality has not been tested. Auxiliary filtration may be required, adding complexity and potential consumable dependence.

**Why It Matters:** If phytoremediation is insufficient, the loop does not fully close without external filtration infrastructure. This interacts directly with Living_Waters.md — the water purification pathway may need to own this stage.

**Resolution Path:** Payment via Specification — TF-TEST-005 results. If auxiliary filtration is required, cross-reference Living_Waters.md for pathway selection.

---

### TF-006 — Non-target insect capture rate unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Ethical |
| Blocking | No — blocks wavelength optimization, not initial test |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The LED array will attract non-target species including pollinators (bees, moths that pollinate crops) and beneficial predators (lacewings, ground beetles). Capture rate of non-target species across wavelength configurations is unknown.

**Why It Matters:** Systematic capture of pollinators and beneficial predators could undermine the crop node and cause net ecological harm — a direct conflict with the Ethical Anchor. This is an ethical unknown, not merely a technical one.

**Resolution Path:** Payment via Specification — TF-TEST-002 wavelength optimization results. Operating protocol must include non-target capture thresholds. If thresholds cannot be met, LED operating hours must be restricted to minimize pollinator exposure (nocturnal operation preferred; pollinator activity peaks at dawn/dusk).

---

### TF-007 — Single node failure propagation uncharacterized

| Field | Value |
|---|---|
| Status | Open |
| Risk | High |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The resilience claim — that node failure degrades but does not collapse the system — has not been tested or simulated. Propagation dynamics are unknown.

**Why It Matters:** If the system is brittle rather than resilient, the Trophic Forge fails its core design requirement. A fish population collapse, for example, might propagate to algal bloom in the pond from accumulated waste, then to water quality failure, then to crop loss — a cascade failure rather than graceful degradation.

**Resolution Path:** Payment via Specification — TF-TEST-007 stress test results.

---

### TF-008 — Minimum viable loop scale unknown

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The smallest pond area, LED array size, and crop border length at which the full loop is self-sustaining has not been determined.

**Why It Matters:** Without a minimum viable scale, Forge deployment planning cannot begin. A loop that requires 5 acres to function is architecturally different from one that functions at 500 m².

**Resolution Path:** Payment via Specification — TF-TEST-006 results. Simulation acceptable as initial estimate; field test required for confirmation.

---

### TF-009 — Interaction boundary with Living_Waters.md at pond node undefined

| Field | Value |
|---|---|
| Status | Open |
| Risk | Medium |
| Priority | Minor |
| Type | Architectural |
| Blocking | No |
| Owner | Tests/Trophic_Forge.md + Tests/Living_Waters.md |
| First Logged | 2026-06-14 |
| Last Reviewed | 2026-06-14 |

**Description:** The pond node is a water system. The boundary between Trophic Forge doctrine (biological outputs of the pond) and Living_Waters.md doctrine (water quality and purification) at this interface has not been defined.

**Why It Matters:** Without a clear ownership boundary, both files may attempt to define pond water quality standards independently, producing contradictory doctrine.

**Resolution Path:** Joint resolution — a shared interface definition to be added to both files on next audit pass. Living_Waters.md owns water quality standards; Trophic_Forge.md owns biological productivity standards. Where they interact, Living_Waters.md governs.

---

### Resolution Log

*(empty — no unknowns resolved at time of first draft)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|---|---|---|---|
| 2026-06-14 | Atmospheric-scale dew point reduction as a design objective | Scale required (millions of units) is v5+ territory. Causal chain from localized moisture extraction to tornado suppression involves atmospheric dynamics outside Forge validation capacity. Water production is the Forge-relevant objective. | No — reopen only with peer-reviewed atmospheric modeling at regional scale |
| 2026-06-14 | "Closed Loop Agriculture" as primary name | Accurate but overused. Does not communicate the node-productive, light-ignited architecture that distinguishes this concept. | No |
| 2026-06-14 | "Cascade Agriculture" as primary name | Implies linear flow without feedback. Directionally correct but structurally incomplete. | No — elements of cascade framing may return in section headings but not as the organizing name |

---

## Drift Indicators

Standard mandatory re-audit conditions per File_Template.md apply.

**Additional file-specific drift indicators:**

- ASM-001 (phototaxis yield assumption) remains unchallenged for more than 90 days without TF-TEST-001 initiation → mandatory re-audit.
- TF-006 (non-target insect capture) reaches Critical status without an operating protocol in Body → halt expansion, escalate to Ethical_Constraints.md review.
- DS-001 (naming dispute) persists beyond three audit cycles without prior art search completion → escalate to Unknowns.md for repository-level resolution.
- Body content references atmospheric mitigation effects of any kind → immediate human review required. This is a hard scope violation.

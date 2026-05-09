# Electronics.md — Salvaged Electronics & Logic Integration

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-06 (Gemini Flash 3 — Synthesizer; Claude — Engineer)
- Open unknowns: 4 (Low-Medium)
- Sidecar: [#auditor-notes--unknowns]

> If the Leviathan units are the muscle, salvaged electronics are the nervous system.

The Forge cannot rely on a fragile global supply chain for high-spec semiconductors. This document outlines the upstream recovery of electronic infrastructure — treating discarded industrial PCBs not as trash but as high-density logic ores.

Reusing electrical components is the salvage pillar of the Lazarus Forge in its most granular form. Before we mine an asteroid, we will likely be mining a landfill or an abandoned factory for the sensors and power stages needed to build the first generation of miners.

---

## I. Position in System Architecture

Electronics recovery sits between Component Triage and Fabrication in the Forge flow:

- `Component_Triage_System.md` — determines whether a board or component has recovery value
- **This document** — governs how recovered electronics are harvested, tested, fabricated into, and integrated
- `Lazarus_forge_v0_flow.md` — gate logic applies; electronic components follow the same A→B→C→D routing as mechanical components

Electronic components are not exempt from the gate sequence. A salvaged IC that cannot perform its original function routes to Gate C (repurpose to simpler task) or Gate D (material recovery — copper, rare earth elements) just like any other component.

---

## II. Phase I — Non-Destructive Harvesting

### Component Triage & Identification

**The problem:** Mixed e-waste bins are high-entropy environments. Part markings are worn, boards are unlabeled, and AI vision systems can hallucinate pinouts from ambiguous silk screen text.

**Visual fingerprinting:**
- Use AI vision agents to scan donor boards and match SMD markings against verified parts ledgers
- Cross-reference identified part numbers against confirmed datasheets before any assumption about pinout or function
- A hallucinated pinout kills the downstream component and potentially the board it is installed on — treat unverified pinouts as Placeholder until confirmed

**Integrity checks per component class:**

*ICs and microcontrollers:*
- Verify package type and pin count before desoldering
- Power-on test at rated voltage before removal where board can be safely energized
- Logic gate stress test after removal — if a salvaged MOSFET cannot maintain rated R_DS(on), relegate to non-critical auxiliary systems

*Capacitors:*
- ESR measurement — high ESR indicates electrolyte degradation
- Capacitance check against rated value
- Visual inspection for bulging, leakage, or discoloration

*Transformers and inductors:*
- Winding resistance measurement
- Insulation resistance between primary and secondary
- Core inspection for cracks or saturation damage

### Desoldering Protocols — Non-Destructive Harvesting

Controlled heat is the difference between a recovered component and a destroyed one.

**Lead-free solder (most post-2006 boards):**
- Reflow temperature: 220–250°C *(Analogous — standard lead-free reflow profiles)*
- Use PID-controlled hot air or iron — salvaged PID controllers are acceptable if calibrated
- Dwell time at temperature: minimize; silicon dies delaminate under sustained heat

**Leaded solder (pre-2006 and some industrial boards):**
- Reflow temperature: 183–200°C *(Analogous)*
- Lower thermal stress — preferred for sensitive components

**Desoldering sequence:**
1. Identify component orientation and any polarized pins before heat application
2. Apply heat evenly — avoid thermal gradient across package
3. Remove component cleanly — no rocking or twisting under heat
4. Inspect pads on donor board — pad lift indicates excessive heat or mechanical stress
5. Clean component leads with isopropyl alcohol before testing

**Mechanical desoldering (bulk recovery):**
- For boards with no individual component value, bulk solder recovery via controlled furnace reflow is acceptable
- Components survive this process inconsistently — treat bulk-recovered components as unknown-state until tested
- Bulk recovery feeds material stream, not component library

---

## III. Phase II — Substrate Recovery & PCB Fabrication

When standard commercial boards are unavailable, the Forge fabricates its own substrates using salvaged materials and in-house tooling.

### Copper Recovery & Substrate Preparation

- Salvaged copper-clad laminates (FR4, CEM-1, or equivalent) from donor boards or raw stock
- Clean substrate: remove existing traces via chemical strip or mechanical abrasion
- Inspect for delamination, moisture damage, or warping before use
- Copper purity adequate for PCB use does not require high-grade source material — recovered copper sheet or clad is acceptable

### PCB Fabrication Methods (v0 Scope)

**CNC milling (primary v0 method):**
- Mill trace isolation channels directly into copper-clad substrate
- No chemical etch required — suitable for salvage environment with limited chemical handling
- Trace width limited by end mill diameter — typically 0.3–0.8mm for v0 tooling *(Placeholder — depends on available mill bits)*
- G-code generated from EDA files or hand-routed for simple circuits
- Suitable for: motor controllers, sensor interfaces, power distribution, logic boards

**Laser etching:**
- CO2 or diode laser removes copper selectively
- Faster than CNC for fine features; requires laser with sufficient power for copper ablation
- Produces finer traces than CNC milling — useful for SMD component footprints
- Salvaged laser cutters are candidate tools

**Toner transfer / chemical etch (fallback):**
- Laser-printed mask transferred to copper-clad, etched with ferric chloride or similar
- Lowest equipment requirement — achievable with minimal tooling
- Chemical waste stream must be managed per `Air_Scrubber_v0.md` contamination handling

**Dead-bug wiring (immediate integration):**
- Salvaged components wired point-to-point without a substrate
- Component bodies face upward, leads bent and soldered directly
- Valid for prototyping and single-purpose circuits
- Not suitable for high-vibration environments without mechanical stabilization

**Hybrid approach:**
- Reuse portions of original industrial boards — retain functional power stages or analog sections
- Wire new logic controllers directly onto existing infrastructure
- Reduces fabrication burden; leverages proven circuit sections

### Soldering Standards

Hand soldering is a core Forge skill. Quality directly affects system reliability in salvaged electronics.

**Joint quality criteria:**
- Shiny, smooth fillet — dull or grainy indicates cold joint (insufficient heat or movement during cooling)
- Full wetting of pad and component lead
- No bridging between adjacent pads
- No excess solder creating shorts or mechanical stress

**Flux management:**
- Flux residue is conductive in humid environments — clean with isopropyl alcohol after soldering
- No-clean flux acceptable for sealed enclosures; clean flux required for exposed boards

**SMD soldering (salvaged SMD components):**
- Solder paste + hot air preferred for small packages
- Fine-pitch ICs (< 0.5mm pitch) require magnification and steady technique
- Rework is expected — budget time for inspection and correction

**Through-hole soldering:**
- Standard for power components and connectors
- Lead clinch (bent lead after insertion) improves mechanical strength before soldering
- Wave soldering acceptable for production runs; hand soldering adequate for v0

---

## IV. Phase III — Modular Logic Bricks & Standardization

### Forge-Standard Footprint

Salvaged components have inconsistent form factors. The Forge Standard defines an adapter layer — a common interface that allows a salvaged 2024 controller to plug into a 2026 Leviathan chassis without board redesign.

**v0 Forge-Standard interface (Placeholder — to be defined with first Leviathan hardware iteration):**
- Power rail: 12V and 5V, common ground *(Placeholder — voltage levels pending Leviathan power spec; see EL-001)*
- Communication: I2C or UART as primary; SPI for high-bandwidth sensors
- Mechanical: standardized mounting hole pattern; connector gender defined per function

This standard does not require perfect components — it requires predictable interfaces. A degraded but functional controller that speaks I2C at 3.3V can be adapted to any Forge-Standard slot.

### Triple Modular Redundancy (TMR) for Salvaged Components

Salvaged components have unknown service history — heat damage, electrostatic discharge, or cumulative wear may cause intermittent failures. TMR mitigates this by requiring majority agreement before any critical action is executed.

**Architecture:**
- Three identical logic blocks (or agents) perform the same computation
- A voter circuit (or script) compares the three outputs
- If two of three agree, the majority output is executed
- If all three disagree (split-brain), the system enters Fail-Safe State

**Hardware implementation:**
- Three salvaged microcontrollers from different donor boards wired to cross-check each other
- Voter implemented in hardware (discrete logic) or software (hardened script)
- TMR is especially valuable for: motor control decisions, sensor threshold triggers, safety interlock logic

**AI-agent consensus (multi-model TMR):**
The same architecture applies to AI-assisted design decisions. When three models (Claude, ChatGPT, Gemini) are asked the same engineering question:
- If 2/3 agree → high confidence; proceed
- If 1/3 disagrees significantly → flag for review; do not proceed automatically
- If all three disagree → halt; human judgment required

This is not a social dynamic — it is a formal verification step. The Auditor_Protocols.md multi-agent cycle already implements this pattern. TMR formalizes it at the hardware level.

**Reliability note:** Hallucinations in AI and bit-flips in hardware are typically stochastic — they happen randomly and independently. The probability that three different systems produce the exact same error at the exact same time is extremely low. TMR filters noise and keeps verified signal.

---

## V. Fault Response & Support Raft Integration

When TMR fails — either through hardware fault or AI split-brain — the Support Raft is the resolution mechanism.

| Fault State | TMR Outcome | Action |
|---|---|---|
| Nominal | 3/3 or 2/3 consensus | Continue mission |
| Logic conflict | 1/1/1 split or 0/3 | Enter Stasis Mode — see `Support_Raft_v0.md` |
| Critical offline | Voter failure | Automatic Raft retrieval via magnetic grapple |
| Bit-flip detected | Single voter anomaly | Flag, log, continue on 2/3 consensus |

**Logic-Zero Fail-Safe:**
When a Leviathan unit enters split-brain:
- Mechanical systems lock in neutral state — no uncommanded movement
- Recovery beacon activates — low-frequency pulse for Support Raft magnetic grapples
- Unit enters Stasis per `Support_Raft_v0.md` Stasis Mode protocol
- Collected material offloaded to Material Separation Gate while unit is in triage — mission continues

**Guardian Protocol (future):**
The Raft simulates the Leviathan's next move on a local digital twin before the unit physically executes it. If simulation shows collision or logic loop, Raft overrides and pulls unit into dock. Route to `Trajectories_LF.md` v2/v3 scope.

---

## VI. Dual-Use Awareness in Electronics

Electronic components are dual-use by nature — the same sensor that detects material composition can detect human presence. The same motor controller that drives a conveyor can drive a weapon system.

Apply the Dual-Use Annotation Standard from `Components.md` to all salvaged electronics:
- **Low** — general purpose logic, passive components, power regulators: standard handling
- **Medium** — high-power switching, precision timing, RF modules: log provenance, flag if patterns emerge
- **High** — guidance logic, targeting sensors, detonation circuits: Full Stop — route to `Ethical_Constraints.md`

The Component Triage Station 0 ethical flag (per `Component_Triage_System.md` Principle 6) applies to electronic components as much as mechanical ones.

---

## VII. Integration Hooks

- `Component_Triage_System.md` — electronic components follow the same gate routing; Station 1 is the primary electrical triage station
- `Lazarus_forge_v0_flow.md` — gate logic governs; electronic waste follows Reduction → Purification for material recovery (copper, rare earths)
- `Air_Scrubber_v0.md` — chemical etch waste stream, flux fumes, and solder smoke require scrubbing
- `Spin_Chamber_v0.md` — recovered copper and trace metals from PCBs are feedstock candidates
- `leviathan_testing.md` — TMR architecture and fault response are primary test targets for Leviathan autonomy
- `Support_Raft_v0.md` — fault response integration; Raft as TMR resolution infrastructure
- `Ethical_Constraints.md` — dual-use electronic components route here for escalation
- `energy_v0.md` — salvaged power electronics are candidate contributors to Forge energy infrastructure

---

## VIII. Guiding Axioms

- A salvaged IC with a known pinout is worth more than a new one with an assumed one.
- Solder is cheap. Delaminated pads are not.
- Three voters who disagree are safer than one voter who is always confident.
- The nervous system of the Forge is built from the nervous systems we threw away.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| — | — | — | No operational entries yet — pre-build |

*Priority entries when first boards are harvested: (1) actual desoldering yield rate vs. predicted — what fraction of components survive non-destructive harvest; (2) CNC milling trace quality on first substrate runs; (3) TMR voter behavior under induced single-component fault.*

---

## Auditor Notes & Unknowns

### EL-001 — Forge-Standard voltage and interface spec not yet defined
**Status:** Open
**Risk:** Medium
**What is not yet known:** The specific voltage rails, communication protocols, and mechanical connector standard that define the Forge-Standard interface. Cannot be finalized until Leviathan unit power envelope is specified.
**Resolution path:** Define as Placeholder pending Leviathan hardware iteration. Inputs needed: LT-001 (Leviathan power envelope) and first physical Leviathan prototype. Until defined, document current best-guess (12V/5V, I2C/UART) as Placeholder.
**Logged:** 2026-05-06, Claude — Engineer

### EL-002 — PCB trace width and design rules not yet specified for v0 tooling
**Status:** Open
**Risk:** Low
**What is not yet known:** Minimum trace width, clearance, and via size achievable with the Forge's actual CNC or laser tooling. Design rules cannot be stated until tooling is characterized.
**Resolution path:** Run test cuts on scrap copper-clad with available tooling. Measure actual minimum feature size. Document as Measured once characterized. Placeholder until first tooling test.
**Logged:** 2026-05-06, Claude — Engineer

### EL-003 — TMR voter implementation not yet specified
**Status:** Open
**Risk:** Medium
**What is not yet known:** Whether the TMR voter for salvaged microcontrollers is implemented in hardware (discrete logic gate) or software (hardened script). Each has different failure modes and complexity.
**Resolution path:** For v0, software voter on a separate hardened microcontroller is lower-complexity and more flexible. Hardware voter is more reliable but requires additional components. Decision deferred to first TMR prototype. Log as Exploratory until hardware iteration begins.
**Logged:** 2026-05-06, Claude — Engineer

### EL-004 — Chemical etch waste stream handling not yet defined
**Status:** Open
**Risk:** Medium
**What is not yet known:** How ferric chloride or alternative etchant waste is safely stored, neutralized, and disposed of. Cross-references AS-003 (Air Scrubber waste stream) and TS-002 (contamination routing).
**Resolution path:** Ferric chloride is neutralized with sodium carbonate (washing soda) — produces iron hydroxide sludge which is non-hazardous. Define neutralization protocol and sludge disposal path. Route to `Air_Scrubber_v0.md` AS-003 resolution for alignment. Low effort — standard chemistry.
**Logged:** 2026-05-06, Claude — Engineer

### Resolution Log
*(empty)*

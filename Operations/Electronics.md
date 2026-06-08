# Electronics.md — Salvaged Electronics & Logic Integration

---

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

> ⚠️ **Operational Safety Advisory**
> Electronics.md governs the trust boundary for all
> autonomous forge systems. A salvaged component that
> passes electrical testing may still carry compromised
> firmware, backdoored logic, or covert surveillance
> capability. Hardware supply chain compromise is a
> documented real-world threat — not a theoretical one.
> No salvaged MCU, controller, or programmable device
> enters forge systems without a Logic-Zero wipe and
> firmware provenance log. See EL-006.
>
> CNC milling of old PCBs produces fiberglass
> microdust, copper particulate, BFR (Brominated Flame
> Retardant) dust, and resin decomposition products.
> Respiratory protection and Air Scrubber operation
> are required during all PCB milling operations.
> See EL-005 and `Operations/Air_Scrubber.md`.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-09 (multi-agent), actioned 2026-05-19                       |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*High risk reflects hardware supply chain compromise
as a documented threat, not a theoretical one. Salvage
electronics from unknown provenance — including consumer
electronics, discarded industrial equipment, and imported
hardware with unknown firmware — are credible attack
vectors for embedded malicious logic, backdoored
controllers, and covert surveillance capability. A
compromised salvaged MCU integrated into forge systems
propagates to every autonomous decision, ethical
constraint, and watchdog behavior the forge depends on.
Electronics.md is the trust-anchor document for the
entire governance substrate.*

---

## Scope Boundary

**This file DOES define:**
- Non-destructive harvesting protocols for salvaged
  electronic components — desoldering standards,
  integrity checks, component identification
- Firmware trust doctrine — reflashing requirements,
  provenance logging, Logic-Zero wipe protocols
  before integration into forge systems
- PCB fabrication methods at v0 — CNC milling,
  laser etching, toner transfer, dead-bug wiring
- Soldering standards for both salvaged component
  integration and new fabrication
- Forge-Standard interface adapter layer — common
  interface enabling salvaged components to
  integrate across forge generations
- TMR hardware implementation — wiring, voter
  circuit, component selection, architectural
  diversity requirement
- Hardware watchdog doctrine — minimum behaviors,
  heartbeat enforcement, neutral-state enforcement
- Dual-use awareness for electronic components —
  annotation standard and escalation paths
- Fault response and Support Raft integration
- Toxic dust and BFR emission profile doctrine
- Counterfeit and remarked component detection
  doctrine

**This file DOES NOT define:**
- TMR as architectural philosophy or framework
  taxonomy (`Architecture/Cognitive_Frameworks.md`
  Framework D)
- Ethical policy governing dual-use escalation
  (`Admin/Ethical_Constraints.md`)
- Confidence collapse states and split-brain
  doctrine (`Architecture/Cognitive_Frameworks.md`)
- Air scrubber hardware specification or waste
  stream chemistry (`Operations/Air_Scrubber.md`)
- Component taxonomy and graduation rules
  (`Architecture/Components.md`)
- Leviathan mission logic or autonomy architecture
  (`Tests/Leviathan_testing.md`)
- Cryptographic key management or root-of-trust
  infrastructure (not yet assigned — EL-006)
- Full autonomous governance law
  (`Admin/Ethical_Constraints.md`)
- Forge-Net network implementation
  (`Architecture/Forge_Net.md`)
- Facility siting for electronics work areas
  (`Architecture/Facilities.md` — FA-001)

---

## File Purpose

Electronics.md governs the recovery, validation,
fabrication, and integration of electronic
components within the Lazarus Forge. It is the
trust-anchor document for the forge's governance
substrate — ethics enforcement, hardware watchdogs,
TMR voting, sensor truth, and AI containment all
depend on the integrity of the electronic systems
this file governs.

The document treats salvaged electronics not as
convenient parts but as potential threat vectors.
A salvaged integrated circuit that passes electrical
testing may still carry compromised firmware,
backdoored logic, or covert surveillance capability
embedded during manufacture. Hardware supply chain
compromise is a documented real-world threat, not
a theoretical one. The forge processes electronics
from unknown provenance — discarded industrial
equipment, imported consumer hardware, and mixed
e-waste — and must treat all of it as potentially
hostile until validated.

At v0, Electronics.md establishes three foundational
capabilities: non-destructive harvesting of salvaged
components with integrity verification, in-house PCB
fabrication when commercial boards are unavailable,
and a TMR architecture with hardware watchdog
enforcement that constrains autonomous behavior even
during total cognitive collapse. Firmware trust
doctrine — requiring Logic-Zero wipes and provenance
logging before any salvaged MCU enters forge systems
— is the primary security boundary between recovered
hardware and trusted infrastructure.

The forge also acknowledges that electronic component
production is a future capability trajectory. As
forges grow and specialize, some will develop
electronics manufacturing capability. The high
specificity of that work means individual forge
instances will naturally diverge in capability based
on local environment and community needs. This file
governs the current recovery and integration scope.
Manufacturing capability is a trajectory item for
later versions.

If this file disappeared, the forge would have no
doctrine for validating salvaged electronics before
integration, no hardware watchdog standard, no TMR
implementation guidance, and no firmware trust
boundary. Every autonomous system the forge builds
would rest on unvalidated hardware of unknown
provenance.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Electrical and functional testing detects component damage and degradation — not firmware compromise or embedded malicious logic | Component triage doctrine; electrical testing standard practice | Low | Firmware trust doctrine (EL-006) fully defined and validated — electrical testing acknowledged as insufficient alone |
| ASM-002 | Salvaged microcontrollers from different donor boards are sufficiently architecturally diverse for TMR independence — shared silicon errata or thermal history does not invalidate independence | TMR doctrine; diversity requirement stated but not yet validated | Low | First TMR prototype characterizes actual independence — correlated failure testing required per EL-007 |
| ASM-003 | AI agents using different models provide sufficient diversity for multi-agent consensus — training data overlap does not produce systematic correlated errors on forge-relevant engineering questions | Multi-agent consensus doctrine; model diversity assumed | Low | Correlated AI failure mode study completed per CF-002 — actual overlap in engineering reasoning characterized |
| ASM-004 | Salvaged components entered the waste stream through legitimate use rather than targeted placement — the salvage stream is not actively seeded with compromised hardware | Threat model; salvage assumed passive not targeted | Low | High-value forge operations attract targeted hardware supply chain attacks — threat model must be reassessed |
| ASM-005 | The hardware watchdog timer is itself uncompromised — a discrete hardware implementation is assumed architecturally simple enough to resist firmware attack | Watchdog doctrine; hardware implementation assumed trustworthy | Medium | Watchdog compromise detected or design found to include programmable elements vulnerable to firmware attack |
| ASM-006 | Chemical etch waste, BFR dust, and solder fumes can be safely managed with available Air Scrubber and containment capability | PCB fabrication doctrine; cross-reference `Operations/Air_Scrubber.md` | Medium | EL-005 toxic dust profile characterized — containment capability confirmed or found insufficient |
| ASM-007 | Desoldering yield rates justify the harvesting overhead — sufficient components survive non-destructive harvest to make the process economically viable | Harvesting doctrine; yield rates unknown at v0 | Low | First operational harvesting cycle characterizes actual yield rate per component class |
| ASM-008 | Forge-Standard interface voltage levels and protocols are achievable with available salvaged components | Forge-Standard doctrine; interface compatibility assumed | Low | First Leviathan hardware iteration characterizes actual salvage compatibility with Forge-Standard spec |

*ASM-001 and ASM-004 are the most dangerous hidden
assumptions in this file. Electrical testing does not
detect firmware compromise — a perfectly functional
component with backdoored logic passes every electrical
test. Targeted hardware supply chain attacks plant
compromised components in expected salvage pathways.
ASM-002 and ASM-003 reflect the correlated failure
risk identified in CF-002 — diversity must be
demonstrated, not assumed. ASM-005 highlights the
recursive trust problem: a watchdog used to detect
compromise must itself be uncompromised. Discrete
hardware implementation with no programmable firmware
is the primary mitigation.*

---

> If the Leviathan units are the muscle, salvaged
> electronics are the nervous system — and the nervous
> system must be trusted before it is connected.

---

## I. Position in System Architecture

Electronics recovery sits between Component Triage
and Fabrication in the Forge flow:

- `Operations/Gate_02_Triage.md` — determines
  whether a board or component has recovery value
- **This document** — governs how recovered
  electronics are harvested, validated, fabricated
  into, and integrated
- `Architecture/Forge_flow.md` — gate logic applies;
  electronic components follow the same A→B→C→D
  routing as mechanical components

Electronic components are not exempt from the gate
sequence. A salvaged IC that cannot perform its
original function routes to Gate C (repurpose to
simpler task) or Gate D (material recovery — copper,
rare earth elements) just like any other component.

**Electronics as trust-anchor:**
Electronics.md governs more than salvage logistics.
The integrity of every autonomous decision, ethical
constraint enforcement, watchdog behavior, and TMR
vote depends on the hardware this file governs.
Compromise here propagates everywhere.

---

## II. Phase I — Non-Destructive Harvesting

### Component Triage & Identification

**The problem:** Mixed e-waste bins are high-entropy
environments. Part markings are worn, boards are
unlabeled, and AI vision systems can hallucinate
pinouts from ambiguous silk screen text.

**Visual fingerprinting:**
- Use AI vision agents to scan donor boards and
  match SMD markings against verified parts ledgers
- Cross-reference identified part numbers against
  confirmed datasheets before any assumption about
  pinout or function
- A hallucinated pinout kills the downstream
  component and potentially the board it is
  installed on — treat unverified pinouts as
  Placeholder until confirmed

**Integrity checks per component class:**

*ICs and microcontrollers:*
- Verify package type and pin count before
  desoldering
- Power-on test at rated voltage before removal
  where board can be safely energized
- Logic gate stress test after removal — if a
  salvaged MOSFET cannot maintain rated R_DS(on),
  relegate to non-critical auxiliary systems
- **Electrical testing detects damage, not
  compromise.** A component that passes all
  electrical tests may still carry malicious
  firmware or backdoored logic. See firmware
  trust doctrine below.

*Capacitors:*
- ESR measurement — high ESR indicates electrolyte
  degradation
- Capacitance check against rated value
- Visual inspection for bulging, leakage, or
  discoloration

*Transformers and inductors:*
- Winding resistance measurement
- Insulation resistance between primary and
  secondary
- Core inspection for cracks or saturation damage

**Counterfeit and remarked component detection:**
Salvage streams include counterfeit components —
recycled parts relabeled as higher-spec versions,
cloned chips with altered ROM behavior, and
fraudulent components with falsified datasheets.
Electrical testing alone does not detect counterfeits.

- Inspect date codes and lot markings for
  consistency — mismatched markings indicate
  remarking
- Cross-reference package markings against known
  manufacturer formatting — font, spacing, and
  logo details differ between genuine and
  counterfeit
- Test performance at rated limits — a counterfeit
  MOSFET labeled for higher current will fail
  at the genuine part's rated operating point
- Treat components from high-counterfeit-risk
  sources (certain market sectors, certain
  geographic origins) with elevated scrutiny
- See EL-008 for unresolved counterfeit detection
  doctrine

### Firmware Trust Doctrine

**Physical recovery of a chip does not guarantee
the integrity of its embedded logic.**

This is the primary security boundary for salvaged
electronics. A salvaged MCU, controller, or
programmable device that passes every electrical
test may still execute malicious firmware, contain
backdoored bootloaders, or perform covert
surveillance. Hardware supply chain compromise
has been documented in industrial controllers,
networking equipment, and consumer electronics
from multiple origins.

**Logic-Zero wipe protocol:**
Before any salvaged programmable device enters
forge systems:
1. Identify device as programmable — any MCU,
   FPGA, DSP, or controller with embedded firmware
2. Attempt full flash erase — confirm erase
   completes successfully
3. Reflash with known-good forge firmware from
   verified source
4. Verify flash contents match expected firmware
   hash before integration
5. Log provenance — device identifier, donor board
   source, wipe date, firmware version installed,
   operator

**Devices that cannot be wiped:**
Some devices have locked bootloaders, write-protected
flash, or hardware-enforced firmware. These cannot
be trusted for forge system integration.

- Locked bootloader devices route to material
  recovery (copper, rare earths) not component
  library
- Document locked device encounter — feed to
  EL-006 resolution path
- Do not attempt to bypass locked bootloaders
  in forge context — the risk of introducing
  exploit tools into the forge environment
  exceeds the component value

**Signed firmware (future — EL-006):**
Full cryptographic firmware signing and root-of-trust
verification is a future capability. At v0, hash
verification of known-good firmware images is the
minimum acceptable practice. Cryptographic
infrastructure is a trajectory item. See EL-006.

### Desoldering Protocols — Non-Destructive Harvesting

Controlled heat is the difference between a
recovered component and a destroyed one.

**Lead-free solder (most post-2006 boards):**
- Reflow temperature: 220–250°C *(Analogous —
  standard lead-free reflow profiles)*
- Use PID-controlled hot air or iron — salvaged
  PID controllers are acceptable if calibrated
- Dwell time at temperature: minimize; silicon
  dies delaminate under sustained heat

**Leaded solder (pre-2006 and some industrial
boards):**
- Reflow temperature: 183–200°C *(Analogous)*
- Lower thermal stress — preferred for sensitive
  components

**Desoldering sequence:**
1. Identify component orientation and any polarized
   pins before heat application
2. Apply heat evenly — avoid thermal gradient
   across package
3. Remove component cleanly — no rocking or
   twisting under heat
4. Inspect pads on donor board — pad lift indicates
   excessive heat or mechanical stress
5. Clean component leads with isopropyl alcohol
   before testing

**Mechanical desoldering (bulk recovery):**
- For boards with no individual component value,
  bulk solder recovery via controlled furnace
  reflow is acceptable
- Components survive this process inconsistently
  — treat bulk-recovered components as
  unknown-state until tested
- Bulk recovery feeds material stream, not
  component library
- **Toxic emissions warning:** Bulk furnace
  reflow of old PCBs produces BFR outgassing,
  lead fumes, and resin decomposition products.
  Air Scrubber must be operational. Operator
  respiratory protection required. See EL-005.

---

## III. Phase II — Substrate Recovery & PCB Fabrication

### Copper Recovery & Substrate Preparation

- Salvaged copper-clad laminates (FR4, CEM-1,
  or equivalent) from donor boards or raw stock
- Clean substrate: remove existing traces via
  chemical strip or mechanical abrasion
- Inspect for delamination, moisture damage, or
  warping before use
- Copper purity adequate for PCB use does not
  require high-grade source material — recovered
  copper sheet or clad is acceptable

### PCB Fabrication Methods (v0 Scope)

**CNC milling (primary v0 method):**
- Mill trace isolation channels directly into
  copper-clad substrate
- No chemical etch required — suitable for salvage
  environment with limited chemical handling
- Trace width limited by end mill diameter —
  typically 0.3–0.8mm for v0 tooling *(Placeholder
  — depends on available mill bits)*
- G-code generated from EDA files or hand-routed
  for simple circuits
- Suitable for: motor controllers, sensor
  interfaces, power distribution, logic boards
- **Toxic dust warning:** CNC milling of old PCBs
  produces fiberglass microdust, copper particulate
  aerosol, BFR dust, and resin decomposition
  products. Respiratory protection and Air Scrubber
  operation required during all milling operations.
  Cross-reference: `Operations/Air_Scrubber.md`,
  EL-005.

**Laser etching:**
- CO2 or diode laser removes copper selectively
- Faster than CNC for fine features; requires
  laser with sufficient power for copper ablation
- Produces finer traces than CNC milling — useful
  for SMD component footprints
- Salvaged laser cutters are candidate tools
- **Fume warning:** Laser ablation of PCB material
  produces similar toxic byproducts to CNC milling.
  Air Scrubber operation required.

**Toner transfer / chemical etch (fallback):**
- Laser-printed mask transferred to copper-clad,
  etched with ferric chloride or similar
- Lowest equipment requirement — achievable with
  minimal tooling
- Chemical waste stream must be managed per
  `Operations/Air_Scrubber.md` contamination handling
- Ferric chloride neutralization: sodium carbonate
  (washing soda) produces iron hydroxide sludge
  — non-hazardous. Define neutralization protocol
  before first use. See EL-004.

**Dead-bug wiring (immediate integration):**
- Salvaged components wired point-to-point without
  a substrate
- Component bodies face upward, leads bent and
  soldered directly
- Valid for prototyping and single-purpose circuits
- Not suitable for high-vibration environments
  without mechanical stabilization

**Hybrid approach:**
- Reuse portions of original industrial boards —
  retain functional power stages or analog sections
- Wire new logic controllers directly onto existing
  infrastructure
- Reduces fabrication burden; leverages proven
  circuit sections

### Soldering Standards

Hand soldering is a core Forge skill. Quality
directly affects system reliability in salvaged
electronics.

**Joint quality criteria:**
- Shiny, smooth fillet — dull or grainy indicates
  cold joint (insufficient heat or movement during
  cooling)
- Full wetting of pad and component lead
- No bridging between adjacent pads
- No excess solder creating shorts or mechanical
  stress

**Flux management:**
- Flux residue is conductive in humid environments
  — clean with isopropyl alcohol after soldering
- No-clean flux acceptable for sealed enclosures;
  clean flux required for exposed boards

**SMD soldering (salvaged SMD components):**
- Solder paste + hot air preferred for small packages
- Fine-pitch ICs (< 0.5mm pitch) require
  magnification and steady technique
- Rework is expected — budget time for inspection
  and correction

**Through-hole soldering:**
- Standard for power components and connectors
- Lead clinch (bent lead after insertion) improves
  mechanical strength before soldering
- Wave soldering acceptable for production runs;
  hand soldering adequate for v0

---

## IV. Phase III — Modular Logic Bricks & Standardization

### Forge-Standard Footprint

Salvaged components have inconsistent form factors.
The Forge Standard defines an adapter layer — a
common interface that allows a salvaged 2024
controller to plug into a 2026 Leviathan chassis
without board redesign.

**v0 Forge-Standard interface (Placeholder — to
be defined with first Leviathan hardware iteration):**
- Power rail: 12V and 5V, common ground *(Placeholder
  — voltage levels pending Leviathan power spec;
  see EL-001)*
- Communication: I2C or UART as primary; SPI for
  high-bandwidth sensors
- Mechanical: standardized mounting hole pattern;
  connector gender defined per function

This standard does not require perfect components
— it requires predictable interfaces. A degraded
but functional controller that speaks I2C at 3.3V
can be adapted to any Forge-Standard slot.

### Hardware TMR Implementation

TMR implementation in hardware is this file's
domain. TMR as architectural philosophy and
framework taxonomy belongs to
`Architecture/Cognitive_Frameworks.md` Framework D.

**Architecture:**
- Three independent logic blocks wired to
  cross-check each other
- A voter circuit compares the three outputs
- If two of three agree, the majority output
  is executed
- If all three disagree (split-brain), the system
  enters Fail-Safe State

**Architectural diversity requirement:**
True TMR requires that the three systems fail
independently. Three identical damaged systems
are not true redundancy — they share failure
modes.

Diversity mechanisms:
- **Silicon diversity** — different MCU families
  (ARM vs AVR vs PIC) have different silicon
  errata and failure modes
- **Firmware diversity** — different firmware
  implementations of the same logic reduce
  shared code vulnerability
- **Power-path diversity** — independent power
  supplies prevent common-mode power failure
- **Thermal diversity** — different physical
  locations reduce shared thermal stress
- **Procurement diversity** — components from
  different donor boards reduce shared batch
  defects and firmware lineage

**Correlated failure risk:**
Salvage-derived TMR systems are especially
vulnerable to hidden common-mode failures:
- Same production batch → same silicon errata
- Same donor equipment → same thermal history
- Same firmware source → same vulnerability
- Same geographic origin → same supply chain
  compromise risk

The false independence claim — that three systems
from different boards are automatically independent
— has been removed. Independence must be
demonstrated through adversarial testing, not
assumed from physical separation. See EL-007.

**Voter implementation:**
- Hardware voter (discrete logic gates) — more
  reliable, harder to compromise, less flexible
- Software voter (hardened script on separate MCU)
  — more flexible, lower component count, vulnerable
  to MCU compromise
- v0 recommendation: software voter on a separate
  dedicated MCU that has undergone Logic-Zero wipe
  and firmware verification per EL-006
- Hardware voter is the v1+ target for
  safety-critical applications

### Hardware Watchdog Doctrine

The hardware watchdog is the final backstop when
all software and firmware fails. It must be
independently trustworthy — see ASM-005.

**Minimum watchdog behaviors (CF-001):**
- Heartbeat signal required from logic board at
  defined interval *(Placeholder — interval defined
  per application)*
- If heartbeat fails: force mechanical neutral
  state via relay or spring-return mechanism
- Watchdog timer implemented in discrete hardware
  — no programmable firmware that can be corrupted
- Watchdog cannot be disabled by software
- Watchdog state is physically observable —
  LED indicator or mechanical flag

**Discrete hardware implementation:**
A watchdog implemented as a simple RC timer and
relay circuit has no firmware to compromise. If
no heartbeat pulse resets the timer, the relay
opens and cuts motor drive or forces spring-return
neutral. This is the mechanical enforcement of
Layer 0 in `Architecture/Cognitive_Frameworks.md`.

*A compromised watchdog that appears functional
is worse than no watchdog — it provides false
assurance while removing the last safety backstop.
Discrete implementation with no programmable
elements is the primary mitigation.*

Cross-reference: `Architecture/Cognitive_Frameworks.md`
CF-001, Layer 0 mechanical truth doctrine.

### Multi-Agent Consensus (MAC)

MAC is distinct from hardware TMR. Conflating
the two produces false confidence in both.

**Hardware TMR:** Three physical systems with
independent silicon, firmware, and power paths.
Tolerates random hardware faults and transient
corruption. Vulnerable to correlated failures
from shared manufacturing origin or firmware.

**Multi-Agent Consensus (MAC):** Three AI models
asked the same engineering question. Majority
agreement increases confidence. Does not tolerate
correlated reasoning failures from shared training
data. Not a substitute for hardware safety systems.

MAC is a verification step, not a safety mechanism.
It improves the quality of engineering decisions
before implementation. Hardware TMR constrains
behavior after implementation. Both are needed.
Neither replaces the other.

**MAC limitations:**
- Three models trained on overlapping data share
  blind spots — consensus on a wrong answer is
  still a wrong answer
- MAC operates pre-implementation; hardware TMR
  operates during execution
- MAC requires human review when models disagree
  significantly — disagreement is signal, not noise
- MAC cannot substitute for physical safety
  constraints (Layer 0)

Cross-reference: `Architecture/Cognitive_Frameworks.md`
Framework D, CF-002 correlated AI failure modes.

---

## V. Fault Response & Support Raft Integration

When TMR fails — either through hardware fault or
split-brain — the Support Raft is the resolution
mechanism.

| Fault State | TMR Outcome | Action |
|---|---|---|
| Nominal | 3/3 or 2/3 consensus | Continue mission |
| Logic conflict | 1/1/1 split or 0/3 | Enter Stasis Mode — see `Tests/Support_Raft.md` |
| Critical offline | Voter failure | Automatic Raft retrieval via magnetic grapple |
| Bit-flip detected | Single voter anomaly | Flag, log, continue on 2/3 consensus |
| Firmware integrity failure | Hash mismatch detected | Halt all autonomous action — Logic-Zero and reflash before restart |

**Logic-Zero Fail-Safe:**
When a Leviathan unit enters split-brain:
- Mechanical systems lock in neutral state via
  hardware watchdog relay — no uncommanded movement
- Recovery beacon activates — low-frequency pulse
  for Support Raft magnetic grapples
- Unit enters Stasis per `Tests/Support_Raft.md`
  Stasis Mode protocol
- Collected material offloaded to Material
  Separation Gate while unit is in triage —
  mission continues

**Guardian Protocol (future):**
The Raft simulates the Leviathan's next move on
a local digital twin before the unit physically
executes it. If simulation shows collision or
logic loop, Raft overrides and pulls unit into
dock. Route to `Admin/Trajectories.md` v2/v3 scope.

---

## VI. Dual-Use Awareness in Electronics

Electronic components are dual-use by nature —
the same sensor that detects material composition
can detect human presence. The same motor
controller that drives a conveyor can drive a
weapon system.

Apply the Dual-Use Annotation Standard from
`Architecture/Components.md` to all salvaged
electronics:
- **Low** — general purpose logic, passive
  components, power regulators: standard handling
- **Medium** — high-power switching, precision
  timing, RF modules: log provenance, flag if
  patterns emerge
- **High** — guidance logic, targeting sensors,
  detonation circuits: Full Stop — route to
  `Admin/Ethical_Constraints.md`

The Component Triage Station 0 ethical flag
(per `Operations/Gate_02_Triage.md` Principle 6)
applies to electronic components as much as
mechanical ones.

---

## VII. Integration Hooks

- `Operations/Gate_02_Triage.md` — electronic
  components follow the same gate routing;
  Station 1 is the primary electrical triage
  station
- `Architecture/Forge_flow.md` — gate logic
  governs; electronic waste follows Reduction →
  Purification for material recovery
- `Operations/Air_Scrubber.md` — chemical etch
  waste stream, flux fumes, solder smoke, BFR
  dust, and CNC milling particulate require
  scrubbing
- `Operations/Gate_05_Separation_Thermal.md` —
  recovered copper and trace metals from PCBs
  are feedstock candidates
- `Tests/Leviathan_testing.md` — TMR architecture
  and fault response are primary test targets
  for Leviathan autonomy
- `Tests/Support_Raft.md` — fault response
  integration; Raft as TMR resolution
  infrastructure
- `Admin/Ethical_Constraints.md` — dual-use
  electronic components route here for escalation
- `Operations/Energy.md` — salvaged power
  electronics are candidate contributors to
  Forge energy infrastructure
- `Architecture/Cognitive_Frameworks.md` —
  TMR philosophy (Framework D), CF-001 watchdog
  standard, CF-002 correlated failure modes

---

## VIII. Guiding Axioms

- A salvaged IC with a known pinout is worth
  more than a new one with an assumed one.
- Solder is cheap. Delaminated pads are not.
- Physical recovery of a chip does not guarantee
  the integrity of its embedded logic.
- Three voters who disagree are safer than one
  voter who is always confident.
- Diversity matters more than quantity in
  redundancy.
- The watchdog must be trusted before it can
  be trusted to protect.
- The nervous system of the Forge is built from
  the nervous systems we threw away — but it
  must be verified before it is connected.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| — | — | — | — | No operational entries yet — pre-build | — | — |
| 2026-05-09 | Audit Review | TMR presented as providing statistical independence for salvaged components from different donor boards | Salvaged components may share production batch, thermal history, firmware lineage, or supply chain origin — independence is not guaranteed by physical separation | Architectural diversity requirement made explicit — silicon, firmware, power-path, thermal, and procurement diversity all required for true TMR independence. Correlated failure risk logged as EL-007 | Analogous | Yes — first TMR prototype must include adversarial correlated failure testing |
| 2026-05-09 | Audit Review | AI multi-agent consensus treated as equivalent to hardware TMR | MAC and hardware TMR are distinct mechanisms with different failure modes and different operating stages. Conflating them produces false confidence in both | MAC section separated from hardware TMR section. MAC is a pre-implementation verification step. Hardware TMR is a runtime safety constraint. Neither replaces the other | Analogous | No — distinction is permanent doctrine |
| 2026-05-09 | Audit Review | Electrical testing treated as sufficient validation for salvaged programmable components | A component passing all electrical tests may carry compromised firmware, backdoored logic, or covert surveillance capability | Firmware trust doctrine added — Logic-Zero wipe and firmware hash verification required before any salvaged programmable device enters forge systems. EL-006 logged | Analogous | Yes — validate Logic-Zero protocol against first salvaged MCU batch |
| 2026-05-09 | Audit Review | Hardware watchdog treated as a software concern | If the watchdog itself is compromised or programmable, it provides false assurance while removing the last safety backstop | Discrete hardware watchdog implementation specified — no programmable firmware. RC timer and relay circuit as the minimum architecture. ASM-005 documents the recursive trust problem | Analogous | Yes — validate watchdog hardware design before first autonomous operation |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

*No interpretation conflicts currently active.
Design tensions exist (hardware vs software voter,
discrete vs programmable watchdog, v0 hash
verification vs full cryptographic signing) but
all are deferred pending first hardware prototype.
Tracked as unknowns, not disputes. Revisit after
first TMR prototype operational.*

---

## Auditor Notes & Unknowns

### EL-001 — Forge-Standard voltage and interface spec not yet defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Architectural                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The specific voltage rails,
communication protocols, and mechanical connector
standard that define the Forge-Standard interface
are not yet defined. Cannot be finalized until
Leviathan unit power envelope is specified.

**Why It Matters:** Without a defined standard,
salvaged components cannot be validated for
Forge-Standard compatibility. Every integration
requires custom adaptation rather than
plug-compatible assembly.

**Resolution Path:**
- Define as Placeholder pending Leviathan hardware
  iteration. Inputs needed: LT-001 (Leviathan
  power envelope) and first physical prototype.
- Until defined, document current best-guess
  (12V/5V, I2C/UART) as Placeholder.
- Payment via Specification — once Leviathan
  hardware iteration defines power envelope,
  move to body as Analogous.

---

### EL-002 — PCB trace width and design rules not yet specified for v0 tooling

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Minimum trace width, clearance,
and via size achievable with actual v0 CNC or
laser tooling are unknown. Design rules cannot
be stated until tooling is characterized.

**Resolution Path:**
- Run test cuts on scrap copper-clad with
  available tooling. Measure actual minimum
  feature size.
- Document as Measured once characterized.
  Placeholder until first tooling test.
- Payment via Specification — once tooling is
  characterized, move to Section III as Measured.

---

### EL-003 — TMR voter implementation not yet specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The voter circuit that arbitrates
between three TMR logic blocks has not been
specified beyond the conceptual level. Hardware
voter vs. software voter choice is unresolved.

**Why It Matters:** The voter is the single point
of failure in a TMR system — if the voter fails
or is compromised, the redundancy benefit is lost.
The implementation choice (hardware vs. software)
determines the trust properties of the entire
architecture.

**Resolution Path:**
- First Leviathan prototype defines the voter
  implementation. v0 recommendation: software
  voter on dedicated, Logic-Zero'd MCU.
- Hardware voter is v1+ target for safety-critical.
- Payment via Specification — once first TMR
  prototype is built and voter tested, move to
  Section IV as Analogous.

---

### EL-004 — Chemical etch waste stream management not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-06                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Ferric chloride and other etch
chemistries produce hazardous waste streams that
require neutralization and disposal protocols
not yet defined.

**Why It Matters:** Improperly disposed etch waste
contaminates water and soil. Neutralization is
simple but must be defined before first use.

**Resolution Path:**
- Define neutralization protocol: sodium carbonate
  to iron hydroxide sludge (non-hazardous).
- Define disposal path for neutralized sludge.
- Cross-reference `Operations/Air_Scrubber.md`
  waste stream handling.
- Payment via Specification — once protocol
  defined and first use validates it, move to
  Section III as Analogous.

---

### EL-005 — Toxic dust and BFR emission profile not characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Safety                               |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Actual particulate composition and
BFR emission rates during CNC milling and bulk
furnace reflow of salvaged PCBs have not been
characterized. Current doctrine relies on analogous
industrial data.

**Why It Matters:** BFR dust and fiberglass
microdust are serious respiratory hazards. If
actual emissions exceed what the Air Scrubber can
handle, current PPE and scrubber doctrine is
insufficient — unknown until characterized.

**Resolution Path:**
- Characterize emissions during first CNC milling
  and bulk reflow operations.
- Cross-reference `Operations/Air_Scrubber.md`
  capacity against measured emission profile.
- Payment via Specification — once characterized,
  move PPE and scrubber requirements to Section II
  as Measured.

---

### EL-006 — Firmware trust and reflashing validation not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | High                                             |
| Priority      | Critical                                         |
| Type          | Technical / Security                             |
| Blocking      | Yes — prerequisite for first salvaged MCU integration |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The cryptographic key management
infrastructure and root-of-trust architecture
required for full firmware signing and verification
are not defined. Current practice (hash verification
of known-good images) is the minimum interim
standard.

**Why It Matters:** Hash verification is better
than nothing but is not a full root-of-trust. A
compromised known-good image produces a matching
hash. Full cryptographic signing with hardware key
storage is the v1+ target. Until then, the firmware
trust boundary has a known gap.

**Resolution Path:**
- Define minimum v0 practice: hash verification
  from trusted source, provenance log mandatory.
- Define v1+ target: cryptographic firmware signing,
  hardware key storage, root-of-trust architecture.
- Cross-reference `Admin/Security_Protocols.md`
  for key management infrastructure.
- Payment via Specification — once v0 minimum
  practice is validated against first MCU batch,
  move to Section II as Analogous. Full resolution
  deferred to v1+ cryptographic infrastructure.

---

### EL-007 — Correlated failure modes in homogeneous salvage TMR not characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-09                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** The independence assumption in
hardware TMR — that three systems from different
donor boards fail independently — has not been
validated. Salvage-derived components may share
production batch, thermal history, firmware
lineage, or supply chain origin, creating
correlated failure modes that bypass TMR
protection.

**Why It Matters:** TMR only works if failures
are independent. Correlated failures produce
simultaneous incorrect outputs that appear as
consensus. Three components that fail the same
way at the same time produce a confident wrong
answer rather than a detectable disagreement.

**Resolution Path:**
- First TMR prototype must include adversarial
  correlated failure testing — deliberately
  induce failure in one system and verify others
  remain independent.
- Characterize actual diversity between selected
  components — silicon family, firmware source,
  thermal history.
- Cross-reference `Architecture/Cognitive_Frameworks.md`
  CF-002 for AI consensus correlated failure
  parallel.
- Payment via Specification — once independence
  is demonstrated through adversarial testing,
  move to Section IV as Measured.

---

### EL-008 — Counterfeit salvage component detection doctrine not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical / Security                             |
| Blocking      | No                                               |
| Owner         | Operations/Electronics.md                        |
| First Logged  | 2026-05-19                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Counterfeit and remarked
components — recycled parts relabeled as higher
spec, cloned chips with altered ROM behavior,
fraudulent components with falsified datasheets
— are present in salvage streams. Detection
criteria and doctrine beyond provisional guidance
in Section II are not yet defined.

**Why It Matters:** A counterfeit MOSFET labeled
for higher current than it can handle fails under
load in ways that may not be immediately apparent.
A cloned MCU with altered ROM behavior may pass
electrical testing while executing subtly different
logic. Counterfeit components undermine the
reliability assumptions the forge's TMR and
watchdog systems depend on.

**Resolution Path:**
- Define detection criteria per component class
  — marking inspection protocols, performance
  testing at rated limits, cross-reference with
  known counterfeit databases.
- Define high-risk source categories — certain
  market sectors and geographic origins have
  higher counterfeit prevalence. Document and
  apply elevated scrutiny.
- Cross-reference EL-006 firmware trust doctrine
  — counterfeit MCUs with altered ROM are a
  distinct threat class from firmware compromise
  but require similar mitigation.
- Payment via Specification — once detection
  criteria are defined and validated against
  first operational harvesting cycle, move to
  Section II as Analogous.

---

### Resolution Log

- 2026-05-19: EL-001 through EL-004 — Reformatted
  from prose to structured sidecar table format.
  Content preserved, provenance dates maintained.
- 2026-05-19: EL-005, EL-006, EL-007 — Migrated
  from multi-agent audit 2026-05-09. Reformatted
  to structured tables.
- 2026-05-19: EL-008 — New entry. Counterfeit
  component detection doctrine gap identified
  in meta-audit. Provisional detection guidance
  added to Section II.
- 2026-06-08: Navigation Anchors block added.
  Verification Ref corrected from `Admin/Forge_Audit_Kit.md`
  to `Admin/Verification_Gates_LF.md` (PC-001).
  Scope Boundary UNK-006 reference updated to
  `Architecture/Facilities.md` FA-001 (PC-002).

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-09 | Electrical testing treated as sufficient for component validation | A component passing all electrical tests may carry compromised firmware, backdoored logic, or covert surveillance capability. Electrical testing detects damage, not compromise | No — firmware trust doctrine is permanent. Electrical testing is necessary but not sufficient |
| 2026-05-09 | TMR independence assumed from physical separation of donor boards | Components from different boards may share production batch, thermal history, firmware lineage, or supply chain origin. Physical separation does not guarantee statistical independence | No — architectural diversity requirement is permanent. Independence must be demonstrated |
| 2026-05-09 | MAC (multi-agent AI consensus) conflated with hardware TMR | MAC and hardware TMR are distinct mechanisms with different failure modes and different operating stages. Conflating them produces false confidence in both | No — permanent distinction. MAC is pre-implementation verification. Hardware TMR is runtime safety |
| 2026-05-09 | Software watchdog treated as equivalent to hardware watchdog | A software watchdog can be compromised by the same firmware failure it is meant to detect. It provides false assurance while removing the last safety backstop | No — discrete hardware watchdog is permanent doctrine for safety-critical applications |
| 2026-05-19 | Salvage stream treated as passive — not actively seeded with compromised hardware | Hardware supply chain compromise has been documented in industrial controllers, networking equipment, and consumer electronics. High-value forge operations are credible targets | Reconsider threat model as forge operations grow in strategic value — threat level scales with target value |

---

## Drift Indicators

The following conditions trigger mandatory re-audit
of this file. All canonical drift indicators from
`Admin/File_Template.md` apply. The following are
additional local triggers specific to Electronics.md:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Salvaged programmable device integrated without Logic-Zero wipe and firmware verification | Permanently abandoned path — EL-006 prerequisite. Physical recovery does not guarantee firmware integrity |
| TMR implemented with components from same production batch or firmware source without diversity verification | Independence must be demonstrated, not assumed. Correlated failure risk bypasses TMR protection |
| MAC results used as safety system substitute rather than pre-implementation verification | MAC and hardware TMR are permanently distinct. MAC cannot substitute for runtime physical safety constraints |
| Hardware watchdog implemented with programmable firmware rather than discrete hardware | Discrete hardware implementation is permanent doctrine for safety-critical watchdog — programmable watchdog creates recursive trust problem |
| CNC milling or bulk furnace reflow performed without Air Scrubber operation and respiratory protection | EL-005 Critical — BFR dust and fiberglass microdust are serious health hazards. Air Scrubber prerequisite |
| Dual-use High components processed without escalation to `Admin/Ethical_Constraints.md` | Dual-use escalation is mandatory — no local override permitted |
| Counterfeit detection skipped for components from high-risk source categories | EL-008 — elevated scrutiny is doctrine for high-risk sources, not optional |
| Forge-Standard interface revised without cross-validation against EL-001 and LT-001 | Interface standard changes propagate to all connected forge instances — unilateral revision creates hidden incompatibility |
| Locked-bootloader devices routed to component library rather than material recovery | Locked bootloader devices cannot be firmware-verified — they cannot be trusted for forge integration |
| Electronics.md scope expands to include cryptographic key management without EL-006 resolution | Key management infrastructure has no owner — absorbing it here without resolution creates specification pressure on an Exploration document |

### Canonical Drift Triggers

*All mandatory re-audit conditions from
`Admin/File_Template.md` Section 11 apply without
exception. Local triggers above are additive,
not substitutes.*

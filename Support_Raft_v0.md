# Support_Raft_v0.md — Operational Anchor
**Version 0.3**

---

## Purpose

The Support Raft is the stationary operational anchor for mobile Leviathan units operating in open-ocean or high-flow environments. It provides regional power, data relay, physical recovery, and triage processing infrastructure — offloading complexity from mobile units so they remain lightweight and mission-focused.

The Raft does not move. The Leviathan units do.

This division of labor is intentional: a stationary node can carry heavier infrastructure, longer-duration storage, and higher-bandwidth communications than any mobile unit in the swarm. Complexity that lives on the Raft stays off the units. That tradeoff must be preserved as the system evolves.

---

## Revision Note

v0.3 — Major structural revision incorporating adversarial audit feedback. Added Scale & Operating Envelope section, SWATH hull architecture, Sacrificial Shell System, marine-specific challenges section, significantly more conservative energy accounting, corrected induction loss estimate, addressed infrastructure overhead omission, resolved Stasis Mode single-point-of-failure contradiction, clarified Material Separation Gate hosting decision, added local decision authority during comms blackout, cache versioning note, and expanded Unknowns Registry. File reference corrected throughout from `Pre_Spin_Separation_v0.md` to `Material_Separation_Gate_v0.md`. Storm-survival protocol remains deferred to `Trajectories_LF.md` per v0.1 Auditor note — partially addressed by hull architecture.

---

## Position in System Architecture

The Support Raft is **regional infrastructure**, not a Leviathan unit. It operates at the surface or shallow subsurface layer, anchored or dynamically positioned within a defined operational cell.

It is the fixed reference point Leviathan units return to — for power, data sync, maintenance, and recovery. It does not direct unit behavior. It supports it.

---

## Scale & Operating Envelope (v0 Placeholder)

[Placeholder — Non-blocking Unknown pending deployment design]

All energy, docking, and storage sizing in this document assumes the following placeholder ranges. These are starting assumptions for v0 design, not validated targets:

- **Operational cell:** ~50–200 km² [Analogous — based on research vessel support zone conventions]
- **Supported unit count:** 8–40 Leviathan units [Placeholder — scales with hull energy capacity]
- **Unit revisit frequency:** Every 12–72 hours depending on mission depth and duration [Placeholder]
- **Satellite uplink availability:** 2–6 windows per day [Analogous — LEO constellation coverage]

These figures are the minimum needed to make energy, docking, and storage claims meaningful. They must be revised as Leviathan unit specifications mature. All downstream claims that depend on these figures inherit their Placeholder status.

---

## Hull Architecture — SWATH Platform

The Support Raft uses a **Small Waterplane Area Twin Hull (SWATH)** configuration — the same architecture used by oceanographic research vessels for platform stability in open water.

**Why SWATH:**
- Two submerged hulls provide buoyancy below the wave action zone
- Narrow struts connecting hulls to the working platform transfer minimal wave energy upward
- Platform motion is dramatically reduced compared to monohull or catamaran designs
- Proven in real-world research and survey vessel deployments — not experimental at the hull level

**Hull interior layout:**
- Power storage, ballast systems, and critical electronics housed in submerged hulls — below waterline, protected from wave loading and surface weather
- Working platform above struts houses docking ports, solar arrays, satellite comms, and Material Separation Gate when active
- Strut geometry designed to isolate Material Separation Gate vibration from hull structure

**Variable draft:**
- Ballast tanks in each hull allow draft adjustment
- Calm conditions: higher draft for solar harvest and docking access
- Storm conditions: increased ballast lowers profile, reduces wave-induced motion
- Extreme conditions: critical systems already below waterline in hull sections — storm mode is a reconfiguration, not an emergency

**Anchoring philosophy:**
- Primary: Conventional mooring for stable deployments
- Secondary: Dynamic positioning for environments where mooring is impractical
- Storm survival design philosophy: survive by reducing profile, not by fighting wave energy

Dynamic positioning vs. mooring is a significant complexity and energy cost difference — choice is deployment-specific and logged as a Non-blocking Unknown pending site characterization.

---

## Sacrificial Shell System

**The Problem Reframed:**
Biofouling on stationary marine structures is inevitable. Fighting it entirely requires continuous energy, toxic coatings, and maintenance burden. The alternative is to design for it — accept colonization on designated surfaces and manage the cycle deliberately.

**The weapon of the environment becomes a tool of the system.**

**Design Concept:**
The SWATH hull outer surface below the waterline is a modular **sacrificial shell** — an outer layer designed for intentional colonization, planned shedding, and rapid replacement. The load-bearing inner hull is protected and never directly exposed to marine growth.

**Shell Architecture:**
- Modular panels mounted on quick-release fixtures along hull and strut geometry
- Panel geometry designed for predictable organism attachment and even growth distribution
- Panels are structurally independent of the inner hull — shedding one does not affect structural integrity
- Replacement panels snap into vacated mounts without dry-dock or human diver requirement

**Material Selection Criteria** [Exploratory — see Unknowns Registry]:
Candidate materials must satisfy:
- Supports natural marine organism attachment without toxic leaching
- Structurally separable from inner hull without load-bearing function
- Transitions cleanly to artificial reef substrate when shed — no contamination risk
- Ideally fabricated from Forge output materials — closing the loop
- Predictable degradation rate under expected fouling pressure

Current candidate classes under exploration:
- **Mineral-based composites** — calcium carbonate or cement-based panels. Natural colonization substrate, benign reef transition, potentially castable from Forge reduction outputs
- **Recycled aggregate panels** — crushed glass, ceramic, or salvaged mineral waste. Forge-native fabrication path, good reef substrate
- **Sacrificial mineral alloys** — selected to provide controlled mineral release supporting calcifying organisms while protecting inner hull. Corrosion is the feature

No candidate material is specified at v0. Material selection is the primary open research thread for this subsystem.

**The Shedding Cycle:**
- Fouling accumulation rate is monitored as a Tier 2 knowledge signal per `leviathan_testing.md` classification
- When accumulation reaches defined threshold, affected panels are flagged for replacement
- Leviathan units are the intended replacement agents — panel swap is a candidate task for Extension A swarm coordination per `leviathan_testing.md`
- Shed panels are either deposited as structured reef substrate in designated zones, or routed to `Material_Separation_Gate_v0.md` if composition warrants recovery
- Panel composition and organism profile logged as water chemistry diagnostic — the shell doubles as a long-duration environmental sensor

**The Reef Transition:**
Shed panels deposited as reef substrate are not waste — they are environmental contribution. The Raft actively improves its operating environment over time. This is consistent with `Ethical_Constraints.md` operating philosophy and creates a positive feedback loop between the Forge's presence and local ecosystem health.

This framing must not become romantic. The reef contribution is a designed outcome, not a marketing claim. Ecological impact must be monitored and logged honestly. If the contribution proves neutral or negative, the design is revised.

---

## Energy Harvesting & Trace

[Magic Energy Check — addressed. Energy section intentionally conservative.]

All power within the regional cell must be traced to the Raft's intake. No power is assumed available without accounting for source, storage, and conversion losses. Marine energy harvesting is difficult, variable, and lower-density than terrestrial equivalents. All figures below are order-of-magnitude estimates, likely pessimistic, and subject to significant revision.

**Intake Methods:**
- Hybrid solar-capture arrays — modular photovoltaic on working platform. Variable output, weather-dependent, zero output at night. DC-direct where possible
- Oscillating wave-surge converters — supplemental only. Wave energy has poor capacity factors and high maintenance burden in real deployments. Treated as bonus input, never assumed reliable
- Neither source is constant or sufficient alone — redundancy is the design intent, not sufficiency

**Infrastructure Overhead** [previously omitted — now addressed]:
The Raft itself consumes power continuously:
- Ballast pump operation: [Placeholder — depends on hull sizing and draft adjustment frequency]
- Onboard computing and sensor suite: [Placeholder]
- Satellite communications: [Estimated — 50–200W during active uplink windows, Analogous to comparable marine research systems]
- Material Separation Gate when active: [Estimated — per `Material_Separation_Gate_v0.md` energy figures]
- Heartbeat monitoring and recovery beacon: [Placeholder — design target: minimal, <10W continuous]

Infrastructure overhead is not optional and must be subtracted from available swarm charge budget before any unit charging is calculated. The Raft is an energy consumer as well as a producer.

**Storage:**
- Solid-state battery buffers [Estimated — target 150% of standard swarm-cycle charge plus Raft overhead; actual sizing depends on swarm count and revisit frequency — Placeholder pending Scale section validation]
- Salvaged battery banks acceptable at v0 per Bootstrap Doctrine in `energy_v0.md`

**Distribution:**
- Leviathan units dock at induction charging pads on submerged hull sections
- Induction loss budget: [Estimated — 20–40% under real subsea conditions accounting for seawater conductivity, alignment variance, and biofouling on pad surfaces. Previous 12% estimate was laboratory-optimistic and has been corrected]
- Regional transmission loss: [Analogous — 5%, based on comparable marine power distribution]

**Stasis Mode:**
If energy reserves fall below 20% of capacity, the Raft enters Stasis Mode:
- Material Separation Gate suspended — first non-essential load shed
- Data Tether and satellite uplink suspended
- Docking charging suspended
- Ballast active positioning suspended — Raft holds last stable draft
- Unit-recovery beacon and Heartbeat monitor maintained at minimal power

**Stasis Mode Single Point of Failure — addressed:**
The original design had a contradiction: the Raft enters Stasis precisely when storm damage or power depletion is most likely — the same conditions under which units most need recovery. Resolution:

- Recovery beacon and passive mechanical recovery capability (tethers, magnetic grapples) remain active in Stasis regardless of energy state — these are passive or near-passive systems by design
- Units are not dependent on the Raft for autonomous survival — per `leviathan_testing.md` Core principles, each unit must remain operationally independent when network connectivity is lost
- Stasis is a Raft constraint, not a swarm constraint — units continue operating on internal power and local autonomy

---

## Orchestration & Data Tether

The Raft serves as the regional knowledge relay node for the Leviathan swarm, operating in Relay-Based Synchronization mode per `leviathan_testing.md` Extensions Framework.

**Local Truth Cache:**
- Read-only copies of `Auditor_Protocols.md`, `Ethical_Constraints.md`, and `Discovery.md` stored locally
- Cache enables offline auditing during satellite outages
- Cache is not editable by Leviathan units — reference material only, not mutable state
- Versioning: Cache is updated only during verified satellite uplink sessions. Version hash stored alongside cached documents. Units querying cache receive version identifier alongside content — allows detection of stale cache after extended outage
- Tampering detection: Hash verification on cache read. Corrupted or mismatched cache triggers Tier 1 alert and falls back to unit-local copies where available

**Local Decision Authority During Comms Blackout:**
The Raft must be able to operate autonomously during extended satellite outage. Defined autonomous authorities:
- May continue charging operations within normal parameters
- May execute Stasis Mode trigger at defined threshold
- May execute unit recovery on heartbeat loss
- May shed panels per defined accumulation threshold
- May NOT update cached reference documents
- May NOT modify swarm-wide operating parameters
- May NOT authorize operations outside defined ethical constraints — `Ethical_Constraints.md` cached copy governs

**Knowledge Tier Routing** (per `leviathan_testing.md`):
- **Tier 1 — Critical Failures:** Safety violations, irrecoverable loss patterns, cache integrity failures — immediate flag, priority uplink queue, wide swarm distribution on next sync
- **Tier 2 — Degradation Patterns:** Biofouling accumulation, power decay trends, sensor drift, induction loss creep — opportunistic propagation, context-dependent adoption
- **Tier 3 — Optimizations:** Efficiency improvements, panel swap scheduling, path planning — slow, selective propagation, experimental adoption only

**Unknown Bulk Triage Hub:**
- Receives and batches Unknown Bulk logs from `Material_Separation_Gate_v0.md` operations
- Units dump ambiguous material, log it, and return to the loop — no stalling
- Synthesizer/Auditor agents review during next satellite uplink
- Unresolved unknowns after two review cycles escalated per `Auditor_Protocols.md` Expiry Rule

**Signal Buffer:**
- Satellite uplink filters and compresses unit telemetry before transmission
- Transmits deltas, not full models — per Leviathan bandwidth doctrine
- Uplink windows opportunistic, not assumed continuous
- During extended blackout, Raft queues outbound telemetry in compressed store-and-forward buffer

---

## Mechanical Design & Resilience

**Modular Docking:**
- Universal docking ports on working platform and submerged hull sections
- Standardized interface accommodates Leviathan unit variants without Raft modification
- Passive capture sufficient for recovery of non-operational units
- Docking port design explicitly accommodates sacrificial shell panel swap operations by Leviathan units

**Passive Recovery:**
- Mechanical tethers and magnetic grapples for lost-heartbeat unit retrieval
- Recovery triggered automatically — no human intervention required
- Passive and near-passive systems — functional in Stasis Mode
- Retrieved units isolated from swarm network pending fault assessment per Tier 1 protocol

**Platform Stability:**
- SWATH hull geometry provides primary stability — wave energy passes through struts, not into platform
- Active ballast provides secondary stability adjustment and storm draft reconfiguration
- Stability is structural, not powered — active ballast supplements, does not substitute
- Material Separation Gate mounted on platform with vibration isolation — high-RPM rotor operations isolated from hull structure

---

## Material Separation Gate Hosting

The Support Raft may host a `Material_Separation_Gate_v0.md` instance for processing material recovered by Leviathan units before bulk transfer to shore-based Forge infrastructure.

**Decision criteria — host on Raft when:**
- Unit-to-shore transfer mass cost exceeds mass reduction from pre-separation
- Swarm scale generates sufficient throughput to justify dedicated gate capacity
- Bootstrap material for next-generation Raft construction is needed locally

**At v0:** Gate hosting is optional infrastructure. The Raft functions without it. The gate instance is not included in baseline Raft energy or space budgeting — it is an additive capability, not a core dependency.

If hosted, the Raft provides power draw, thermal sink for heat pipe output, and Unknown Bulk logging relay. Gate operations are the first non-essential load shed under power constraint.

---

## Marine-Specific Challenges

The ocean is not a benign operating environment. The following challenges are first-class design constraints, not deferred afterthoughts.

**Biofouling:**
Managed through the Sacrificial Shell System rather than suppressed. Accumulation rate is a monitored diagnostic signal. Shell system converts the dominant maintenance challenge into a designed output cycle.

**Galvanic Corrosion:**
Mixed metals in seawater with induced currents from induction charging creates aggressive galvanic corrosion potential. This is elevated from Non-blocking to **high-priority Non-blocking Unknown**. Mitigation strategies require marine engineering input before v1.0 specification. Inner hull material selection must account for electrochemical compatibility with charging infrastructure and seawater exposure.

**Storm Loading:**
Partially addressed by SWATH hull variable draft — storm mode lowers profile and moves critical systems further below wave action. Full storm-survival protocol (submersion depth, anchor-load limits, breakaway anchoring philosophy) deferred to `Trajectories_LF.md`. Design philosophy committed: survive by reducing profile, not by resisting wave energy.

**Pressure and Depth:**
Hull sections operating below waterline must be rated for expected depth range. Pressure specifications are Placeholder pending Scale section validation and deployment site characterization.

**Marine Regulatory Environment:**
Operating autonomous marine infrastructure in open ocean involves maritime law, environmental permitting, and potentially international waters governance. Not addressed at v0. Logged as Exploratory Unknown — route to `Ethical_Constraints.md` for governance framework expansion.

---

## Lifecycle & Failure Modes

[Lifecycle Truncation Check — addressed]

**Degraded Operation:**
Partial solar or wave intake loss reduces charge rate without suspending operations unless Stasis threshold is reached. Docking queue managed by available pad capacity. Material Separation Gate is first non-essential load shed. Sacrificial shell monitoring continues in all non-Stasis modes.

**Failure Modes & Detection:**
- Induction loss rising above 40% baseline indicates charging pad biofouling or alignment fault — Tier 2 signal
- Wave converter declining output over time indicates mechanical degradation — Tier 2 signal
- Ballast system fault presents as platform tilt — onboard inclinometer, Tier 1 if acute
- Cache hash mismatch on read — Tier 1 alert, fall back to unit-local copies
- Satellite uplink loss — normal operating condition, not a fault. Extended loss triggers store-and-forward mode

**Maintenance Access:**
- Charging pads, wave converters, and docking ports designed for Leviathan unit servicing where possible
- Sacrificial shell panel replacement is primary routine maintenance — designed for autonomous execution by swarm units
- Modular component design allows hot-swap of degraded units without full Raft shutdown

**End-of-Region Protocol — Self-Consuming Base:**
Once the operational area is cleared and Leviathan units are recovered or redeployed:
- All recoverable electronics and high-value components extracted as Class A salvage
- Sacrificial shell panels in good condition redeployed as structured reef substrate
- Structural members and chassis fed into `Material_Separation_Gate_v0.md` of next-generation platform
- The logistical requirement: next-generation platform must be present or nearby before end-of-region protocol begins — chicken-and-egg risk is real and logged as Non-blocking Unknown

The Raft's final act is enabling its successor. Nothing is wasted.

---

## Auditor Gate 1 Pass — Fallacy Notes

**Magic Energy:** Addressed. Dual intake methods traced with conservative loss estimates. Infrastructure overhead now included. Stasis Mode protects against energy deficit cascades. All figures labeled with confidence level.

**Friction Blindness:** Addressed. Induction losses corrected upward to real-world range (20–40%). Wave converter variability acknowledged. Ballast energy cost logged as Placeholder. Galvanic corrosion elevated to high-priority.

**Energy Density Paradox:** The energy cost of maintaining the Raft is justified by the infrastructure it provides. Quantitative offset calculation remains Non-blocking Unknown — directional case is sound, specific figures await `energy_v0.md` experimental baseline. Not claimed as verified.

**Incomplete by Omission:** Marine regulatory environment added. Galvanic corrosion elevated. Storm survival philosophy committed even though full protocol deferred. Infrastructure overhead explicitly accounted.

**Lifecycle Truncation:** Addressed. Degraded operation, failure modes, maintenance, and end-of-life all defined. Chicken-and-egg end-of-region risk explicitly logged.

---

## Unknowns Registry

**Blocking:**
- None at v0

**Non-blocking (High Priority):**
- Galvanic corrosion mitigation strategy for mixed-metal hull with induction charging infrastructure in seawater. Resolution path: marine engineering analog review and materials consultation before v1.0
- Sacrificial shell material selection — must satisfy colonization, separation, reef transition, and Forge fabrication criteria simultaneously. Resolution path: marine materials literature review, prototype panel field testing

**Non-blocking:**
- Battery buffer sizing requires swarm count, mission duration, and depth profile. Resolution path: Leviathan unit specs and trial deployment data
- Induction charging pad design for 20–40% loss range with biofouling compensation. Resolution path: subsea charging system analog review
- Raft infrastructure overhead power budget requires detailed component specifications. Resolution path: component selection phase
- Dynamic positioning vs. anchored mooring trade-off. Resolution path: deployment site characterization
- Scale envelope validation (unit count, cell size, revisit frequency). Resolution path: Leviathan deployment planning
- Chicken-and-egg end-of-region logistics — next-generation platform availability before Raft decommission. Resolution path: operational sequencing planning
- Hull pressure rating for submerged sections. Resolution path: deployment depth specification

**Exploratory:**
- Bio-fouling accumulation rate modeling for candidate shell materials. Route to `leviathan_testing.md`
- Storm-survival protocol including submersion depth and anchor-load limits. Route to `Trajectories_LF.md`
- Multi-Raft coordination protocols for large-area operations. Route to `Trajectories_LF.md`
- Marine regulatory and permitting framework for autonomous open-ocean infrastructure. Route to `Ethical_Constraints.md`
- Leviathan-executed panel swap as swarm coordination task. Route to `leviathan_testing.md` Extension A
- Marine GECK seed — minimal bootstrap configuration for Raft instantiation. Route to `geck_forge_seed.md`

---

## Explicit Non-Goals (v0)

- Directing or overriding Leviathan unit behavior
- Achieving energy self-sufficiency for the regional cell
- Replacing shore-based Forge infrastructure
- Operating as a production system
- Guaranteeing reef contribution quality without monitoring

---

## Integration Hooks

- `Material_Separation_Gate_v0.md` — optional hosted module; Raft provides power and thermal sink when active
- `leviathan_testing.md` — stress-test environment for docking, knowledge tier routing, panel swap coordination, and bio-fouling progression
- `energy_v0.md` — baseline energy philosophy and kWh/kg metric; Raft energy figures inherit bootstrap-honest approach
- `Auditor_Protocols.md` — Local Truth Cache stores this; Unknown Bulk escalation follows Expiry Rule; Raft autonomous authority bounded by this document
- `Ethical_Constraints.md` — cached and governing; marine regulatory unknowns route here
- `Ship_of_Theseus_Right_to_Repair.md` — philosophical grounding for self-consuming end-of-life and sacrificial shell cycle
- `leviathan_testing.md` Extension A — panel swap as swarm coordination candidate task
- `Trajectories_LF.md` — storm-survival protocol, multi-Raft coordination, positioning trade-offs
- `geck_forge_seed.md` — marine GECK seed variant informed by minimal Raft bootstrap configuration

---

## Notes

- The Raft's value is measured by what it enables in the units, not what it does directly
- Complexity that lives on the Raft stays off the units — preserve this tradeoff as the system evolves
- The sacrificial shell system converts the dominant marine maintenance burden into a designed output cycle
- The self-consuming end-of-region protocol is not a compromise — it is the design
- The ocean punishes poor assumptions quickly and repeatedly — per `leviathan_testing.md`
- Final versions often aren't final

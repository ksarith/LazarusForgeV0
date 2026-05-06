# Support_Raft_v0.md — Operational Anchor
**Version 0.4**

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-06 (Gemini Flash 3 — Skeptic/Auditor)
- Open unknowns: 10 (Low-High)
- Sidecar: [#auditor-notes--unknowns]

> The Raft's value is measured by what it enables in the units, not what it does directly.

---

## Purpose

The Support Raft is the stationary operational anchor for mobile Leviathan units operating in open-ocean or high-flow environments. It provides regional power, data relay, physical recovery, and triage processing infrastructure — offloading complexity from mobile units so they remain lightweight and mission-focused.

The Raft does not move. The Leviathan units do.

This division of labor is intentional: a stationary node can carry heavier infrastructure, longer-duration storage, and higher-bandwidth communications than any mobile unit in the swarm. Complexity that lives on the Raft stays off the units. That tradeoff must be preserved as the system evolves.

**Foundational claim** *(per Gemini audit Gate 10 check):* The Support Raft must provide a net positive energy and data surplus to the Leviathan swarm that exceeds the energy cost of its own hull maintenance and infrastructure overhead.

---

## Revision Note

v0.4 — Template retrofit, sidecar migration, Gemini audit findings integrated. Previous v0.3 changes: Major structural revision incorporating adversarial audit feedback. Added Scale & Operating Envelope, SWATH hull architecture, Sacrificial Shell System, marine-specific challenges, conservative energy accounting, corrected induction loss estimate, Stasis Mode contradiction resolved, Material Separation Gate hosting decision, local decision authority during comms blackout, cache versioning. File reference corrected from `Pre_Spin_Separation_v0.md` to `Material_Separation_Gate_v0.md` throughout.

---

## Position in System Architecture

The Support Raft is **regional infrastructure**, not a Leviathan unit. It operates at the surface or shallow subsurface layer, anchored or dynamically positioned within a defined operational cell.

It is the fixed reference point Leviathan units return to — for power, data sync, maintenance, and recovery. It does not direct unit behavior. It supports it.

---

## Scale & Operating Envelope (v0 Placeholder)

All energy, docking, and storage sizing assumes the following placeholder ranges:

- **Operational cell:** ~50–200 km² *(Analogous — research vessel support zone conventions)*
- **Supported unit count:** 8–40 Leviathan units *(Placeholder — scales with hull energy capacity)*
- **Unit revisit frequency:** Every 12–72 hours *(Placeholder)*
- **Satellite uplink availability:** 2–6 windows per day *(Analogous — LEO constellation coverage)*

All downstream claims that depend on these figures inherit their Placeholder status.

---

## Hull Architecture — SWATH Platform

The Support Raft uses a **Small Waterplane Area Twin Hull (SWATH)** configuration.

- Two submerged hulls provide buoyancy below the wave action zone
- Narrow struts transfer minimal wave energy upward to the working platform
- Platform motion dramatically reduced vs. monohull or catamaran designs
- Proven in real-world research and survey vessel deployments

**Hull interior layout:**
- Power storage, ballast systems, and critical electronics housed in submerged hulls
- Working platform above struts houses docking ports, solar arrays, satellite comms, and Material Separation Gate when active
- Strut geometry designed to isolate Material Separation Gate vibration from hull structure

**Variable draft:**
- Calm conditions: higher draft for solar harvest and docking access
- Storm conditions: increased ballast lowers profile, reduces wave-induced motion
- Extreme conditions: critical systems already below waterline — storm mode is a reconfiguration, not an emergency

**Anchoring:** Primary conventional mooring; secondary dynamic positioning where mooring is impractical. Choice is deployment-specific — logged as SR-008.

**Thermal management note** *(Gemini audit finding):* The Raft's thermal rejection system (heat exchangers) must be either expandable or baseline-rated for Material Separation Gate heat loads, since the Gate is an optional hosted module. Thermal architecture must be modular — not sized to Gate-absent baseline only. See SR-010.

---

## Sacrificial Shell System

**The Problem Reframed:**
Biofouling on stationary marine structures is inevitable. The alternative to fighting it is to design for it — accept colonization on designated surfaces and manage the cycle deliberately.

**Design Concept:**
The SWATH hull outer surface below the waterline is a modular **sacrificial shell** — an outer layer designed for intentional colonization, planned shedding, and rapid replacement. The load-bearing inner hull is protected and never directly exposed to marine growth.

**Shell Architecture:**
- Modular panels on quick-release fixtures along hull and strut geometry
- Panels are structurally independent of the inner hull — shedding one does not affect structural integrity
- Replacement panels snap into vacated mounts without dry-dock or human diver requirement

**Material Selection Criteria** *(see SR-002)*:
Candidate materials must: support natural marine organism attachment without toxic leaching; be structurally separable from inner hull; transition cleanly to artificial reef substrate when shed; ideally be fabricated from Forge output materials.

Current candidate classes: mineral-based composites, recycled aggregate panels, sacrificial mineral alloys. No candidate material is specified at v0.

**The Shedding Cycle:**
- Fouling accumulation rate monitored as Tier 2 knowledge signal per `leviathan_testing.md`
- Leviathan units are the intended replacement agents — panel swap is a candidate task for Extension A swarm coordination
- Shed panels deposited as structured reef substrate or routed to `Material_Separation_Gate_v0.md` if composition warrants recovery
- Panel composition and organism profile logged as water chemistry diagnostic

**The Reef Transition:**
Shed panels deposited as reef substrate are environmental contribution, not waste. This must not become romantic — ecological impact must be monitored and logged honestly. If the contribution proves neutral or negative, the design is revised.

---

## Energy Harvesting & Trace

*Magic Energy check — addressed. All figures labeled with confidence level. Infrastructure overhead included.*

**Intake Methods:**
- Hybrid solar-capture arrays — variable output, weather-dependent, zero output at night
- Oscillating wave-surge converters — supplemental only, never assumed reliable

**Infrastructure Overhead:**
- Ballast pump operation: *(Analogous — see SR-009; ballast pumping in SWATH/semi-submersible designs typically 5–50 kW during active draft adjustment; Placeholder pending hull sizing)*
- Onboard computing and sensor suite: *(Placeholder)*
- Satellite communications: *(Estimated — 50–200W during active uplink windows, Analogous to comparable marine research systems)*
- Material Separation Gate when active: *(Estimated — per `Material_Separation_Gate_v0.md` energy figures)*
- Heartbeat monitoring and recovery beacon: *(Placeholder — design target <10W continuous)*

Infrastructure overhead must be subtracted from available swarm charge budget before any unit charging is calculated.

**Storage:**
- Solid-state battery buffers *(Estimated — target 150% of standard swarm-cycle charge plus Raft overhead; Placeholder pending Scale section validation)*
- Salvaged battery banks acceptable at v0 per Bootstrap Doctrine

**Distribution:**
- Leviathan units dock at induction charging pads on submerged hull sections
- Induction loss budget: *(Estimated — 20–40% under real subsea conditions accounting for seawater conductivity, alignment variance, and biofouling. Previous 12% estimate was laboratory-optimistic and has been corrected)*
- Regional transmission loss: *(Analogous — 5%)*

**Stasis Mode:**
If energy reserves fall below 20% of capacity:
- Material Separation Gate suspended (first non-essential load shed)
- Data Tether and satellite uplink suspended
- Docking charging suspended
- Ballast active positioning suspended — Raft holds last stable draft
- Unit-recovery beacon and Heartbeat monitor maintained at minimal power

*Stasis Mode docking clarification (Gemini audit finding):* Units recovered via passive mechanical means during Stasis are routed to a **cold storage rack** — physically secured but not occupying active induction docking ports. This prevents a dead-unit-clog scenario where non-functional units block active docking capacity. See SR-006.

*Stasis Mode single point of failure — resolved:* Recovery beacon and passive mechanical recovery remain active in Stasis regardless of energy state. Units are not dependent on the Raft for autonomous survival — per `leviathan_testing.md` Core principles, each unit remains operationally independent when network connectivity is lost.

---

## Orchestration & Data Tether

**Local Truth Cache:**
- Read-only copies of `Auditor_Protocols.md`, `Ethical_Constraints.md`, and `Discovery.md` stored locally
- Cache is not editable by Leviathan units — reference only
- Cache updated only during verified satellite uplink sessions; version hash stored alongside documents
- Hash verification on cache read — corrupted or mismatched cache triggers Tier 1 alert

*Cache sanitization risk (Gemini audit finding):* If a Raft is physically compromised, the Local Truth Cache exposes internal governance logic. See SR-007.

**Local Decision Authority During Comms Blackout:**
- May: continue charging, execute Stasis Mode, execute unit recovery, shed panels per threshold
- May NOT: update cached reference documents, modify swarm-wide operating parameters, authorize operations outside `Ethical_Constraints.md`

**Knowledge Tier Routing:**
- Tier 1 — Critical Failures: immediate flag, priority uplink queue, wide distribution
- Tier 2 — Degradation Patterns: opportunistic propagation, context-dependent adoption
- Tier 3 — Optimizations: slow, selective propagation, experimental adoption only

---

## Mechanical Design & Resilience

**Modular Docking:**
- Universal docking ports on working platform and submerged hull sections
- Passive capture sufficient for recovery of non-operational units
- Cold storage rack for units recovered during Stasis (see Stasis Mode above)

**Passive Recovery:**
- Mechanical tethers and magnetic grapples for lost-heartbeat unit retrieval
- Passive and near-passive systems — functional in Stasis Mode
- Retrieved units isolated from swarm network pending fault assessment

**Platform Stability:**
- SWATH hull geometry provides primary stability
- Active ballast provides secondary adjustment
- Material Separation Gate mounted with vibration isolation

---

## Material Separation Gate Hosting

Optional hosted capability. The Raft functions without it. Not included in baseline energy or space budgeting.

**Host when:** unit-to-shore transfer mass cost exceeds mass reduction from pre-separation; swarm scale generates sufficient throughput; bootstrap material for next-generation Raft construction is needed locally.

If hosted, the Raft provides power draw, thermal sink for heat pipe output, and Unknown Bulk logging relay. Gate operations are the first non-essential load shed under power constraint.

---

## Marine-Specific Challenges

**Biofouling:** Managed through Sacrificial Shell System. Accumulation rate is a monitored diagnostic signal.

**Galvanic Corrosion:** Mixed metals in seawater with induced currents from induction charging creates aggressive galvanic corrosion potential. Elevated to **high-priority Non-blocking Unknown** — see SR-001. Requires marine engineering input before v1.0 specification.

**Storm Loading:** SWATH variable draft partially addresses this. Full storm-survival protocol deferred to `Trajectories_LF.md`. Design philosophy: survive by reducing profile, not by resisting wave energy.

**Pressure and Depth:** Hull sections below waterline must be rated for expected depth range. Placeholder pending Scale section validation — see SR-008.

**Marine Regulatory Environment:** Not addressed at v0. Exploratory Unknown — route to `Ethical_Constraints.md`.

---

## Lifecycle & Failure Modes

**Degraded Operation:** Partial intake loss reduces charge rate without suspending operations unless Stasis threshold is reached. Material Separation Gate is first non-essential load shed.

**Failure Modes & Detection:**
- Induction loss rising above 40% baseline — Tier 2 signal (pad biofouling or alignment fault)
- Wave converter declining output — Tier 2 signal (mechanical degradation)
- Ballast system fault — onboard inclinometer, Tier 1 if acute
- Cache hash mismatch — Tier 1 alert, fall back to unit-local copies
- Satellite uplink loss — normal operating condition, not a fault

**Maintenance Access:** Charging pads, docking ports, and sacrificial shell panels designed for Leviathan unit servicing where possible. Panel replacement is primary routine maintenance — designed for autonomous swarm execution.

**End-of-Region Protocol:**
- All recoverable electronics and high-value components extracted as Class A salvage
- Sacrificial shell panels in good condition redeployed as structured reef substrate
- Structural members fed into `Material_Separation_Gate_v0.md` of next-generation platform
- Chicken-and-egg risk: next-generation platform must be present before end-of-region protocol begins — see SR-005

The Raft's final act is enabling its successor. Nothing is wasted.

---

## Explicit Non-Goals (v0)

- Directing or overriding Leviathan unit behavior
- Achieving energy self-sufficiency for the regional cell
- Replacing shore-based Forge infrastructure
- Operating as a production system
- Guaranteeing reef contribution quality without monitoring

---

## Integration Hooks

- `Material_Separation_Gate_v0.md` — optional hosted module
- `leviathan_testing.md` — stress-test environment for docking, knowledge tier routing, panel swap, biofouling progression
- `energy_v0.md` — baseline energy philosophy; Raft energy figures inherit bootstrap-honest approach
- `Auditor_Protocols.md` — Local Truth Cache stores this; governs Unknown Bulk escalation
- `Ethical_Constraints.md` — cached and governing; marine regulatory unknowns route here
- `Ship_of_Theseus_Right_to_Repair.md` — philosophical grounding for self-consuming end-of-life and sacrificial shell cycle
- `Trajectories_LF.md` — storm-survival protocol, multi-Raft coordination
- `geck_forge_seed.md` — marine GECK seed variant informed by minimal Raft bootstrap configuration

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Induction loss estimated at 12% | Laboratory-optimistic; real subsea conditions with seawater conductivity, alignment variance, and biofouling push losses to 20–40% | Always use field analog data for marine energy estimates, not laboratory figures |
| May 2026 | Stasis Mode suspended all docking without cold storage rack | Created dead-unit-clog scenario — recovered but uncharged units blocking active docking ports | Passive recovery and active charging docks must be architecturally separated |

---

## Auditor Notes & Unknowns

### SR-001 — Galvanic corrosion mitigation strategy (HIGH PRIORITY)
**Status:** Open
**Risk:** High
**What is not yet known:** How to mitigate galvanic corrosion in a mixed-metal hull with induction charging infrastructure operating in seawater. Inner hull material selection must account for electrochemical compatibility.
**Resolution path:** Marine engineering analog review and materials consultation before v1.0. Sacrificial anode placement, hull material selection, and charging infrastructure isolation are the three design levers.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-002 — Sacrificial shell material selection
**Status:** Open
**Risk:** Medium
**What is not yet known:** Which material satisfies colonization, separation, reef transition, and Forge fabrication criteria simultaneously.
**Resolution path:** Marine materials literature review and prototype panel field testing. Three candidate classes identified: mineral-based composites, recycled aggregate panels, sacrificial mineral alloys.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-003 — Battery buffer sizing
**Status:** Open
**Risk:** Medium
**What is not yet known:** Exact buffer sizing requires swarm count, mission duration, and depth profile.
**Resolution path:** Leviathan unit specs and trial deployment data. Current target: 150% of standard swarm-cycle charge plus Raft overhead — Placeholder.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-004 — Induction charging pad design for 20–40% loss range
**Status:** Open
**Risk:** Medium
**What is not yet known:** Pad design with biofouling compensation that maintains acceptable efficiency across the 20–40% loss range.
**Resolution path:** Subsea charging system analog review. Existing AUV docking station programs (MBARI, WHOI) have relevant data.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-005 — Chicken-and-egg end-of-region logistics
**Status:** Open
**Risk:** Medium
**What is not yet known:** How to ensure next-generation platform is present before end-of-region protocol begins. Sequential deployment logic not yet defined.
**Resolution path:** Operational sequencing planning — define minimum overlap period between generations. Route to Trajectories_LF.md for v1 operational planning.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-006 — Cold storage rack design for Stasis Mode recovery
**Status:** Open
**Risk:** Low
**What is not yet known:** Physical design of cold storage rack — how many units, securing mechanism, separation from active induction docks.
**Resolution path:** Define rack capacity as a fixed multiple of supported unit count (e.g., 10% of swarm as cold storage). Rack design follows from Leviathan unit physical envelope once specified.
**Logged:** 2026-05-06, Gemini Flash 3 — Skeptic/Auditor

### SR-007 — Local Truth Cache sanitization on hull compromise
**Status:** Open
**Risk:** Medium
**What is not yet known:** Encryption and physical-access-zeroing protocols for Local Truth Cache in the event of unauthorized boarding or hull breach.
**Resolution path:** Standard maritime security practices apply — encrypted storage with remote-wipe capability triggered by hull breach sensor or loss-of-heartbeat. Log as Non-blocking; design before v1.0 deployment.
**Logged:** 2026-05-06, Gemini Flash 3 — Skeptic/Auditor

### SR-008 — Dynamic positioning vs. mooring trade-off
**Status:** Open
**Risk:** Low
**What is not yet known:** Which anchoring strategy is appropriate for target deployment sites. Significant complexity and energy cost difference.
**Resolution path:** Deployment site characterization. Exploratory until first site is selected.
**Logged:** 2026-05-04, Multi-model audit cycle

### SR-009 — Ballast pump energy draw
**Status:** Open
**Risk:** Medium
**What is not yet known:** Precise ballast pump energy draw during storm-mode draft reconfiguration. Currently Placeholder — a primary energy consumer in SWATH designs.
**Resolution path:** Analogous data from semi-submersible and research vessel ballast systems. Typical range 5–50 kW during active adjustment — add as Analogous estimate pending hull sizing. Must be included before total energy trace can be validated.
**Logged:** 2026-05-06, Gemini Flash 3 — Skeptic/Auditor

### SR-010 — Thermal management modularity for optional Gate hosting
**Status:** Open
**Risk:** Low
**What is not yet known:** Whether Raft thermal rejection system (heat exchangers) is expandable or must be baseline-rated for Gate-integrated heat loads even when Gate is absent.
**Resolution path:** Define thermal architecture as modular — expandable heat exchanger capacity rather than fixed sizing. Add note to Mechanical Design confirming this. Low effort, closes the cross-ref gap Gemini identified.
**Logged:** 2026-05-06, Gemini Flash 3 — Skeptic/Auditor

### Resolution Log
- 2026-05-04: Induction loss estimate corrected from 12% (laboratory) to 20–40% (real subsea conditions). Logged in Lessons Learned.
- 2026-05-04: Stasis Mode single-point-of-failure contradiction resolved — recovery beacon and passive mechanical recovery remain active regardless of energy state.
- 2026-05-06: Cold storage rack concept added to Stasis Mode section — resolves dead-unit-clog contradiction identified by Gemini audit.
- 2026-05-06: Foundational claim sentence added to Purpose section — addresses Gemini Gate 10 finding.
- 2026-05-06: Ballast pump Analogous estimate added to Infrastructure Overhead — partial resolution of SR-009.

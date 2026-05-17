# Lazarus Forge — G.E.C.K.
**(Genesis / General Environmental Construction Kit)**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                           |
| Last Audit       | 2026-05-04                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Minimum viable seed required to instantiate a new Lazarus Forge in a fresh location
- Core G.E.C.K. module list and criticality rationale
- Procurement doctrine — when purchasing is the correct bootstrap strategy
- Precision as a capability threshold concept (introductory — full treatment deferred)
- Marine variant module list and success criteria (exploratory)
- G.E.C.K. success criteria and scaling pathway to v1

**This file DOES NOT define:**
- Detailed engineering specifications for any G.E.C.K. module
- Full precision doctrine or precision tracking methodology (see future Precision_LF.md)
- Leviathan chassis or deep-marine systems (see Trajectories_LF.md)
- Energy infrastructure beyond portable generation minimum (see energy_v0.md)
- Component taxonomy or classification criteria (see Components.md)

---

## File Purpose

This file defines the smallest coherent set of tools, data, and doctrine capable of
instantiating a new Lazarus Forge from a standing start in an unfamiliar location. It
answers: what must be in the seed, why each piece earns its place, and how the seed grows
into a functioning Forge. If this file disappeared, new deployments would lose the
canonical module list, the procurement rationale, and the criteria for declaring a G.E.C.K.
deployment successful.

---

## Assumptions

| ID      | Assumption                                                              | Basis                            | Confidence | Expiry Trigger                                      |
|---------|-------------------------------------------------------------------------|----------------------------------|------------|-----------------------------------------------------|
| ASM-001 | Deployment site has some access to commercial supply chains at v0       | Procurement doctrine foundation  | Medium     | Fully off-grid deployment with zero resupply confirmed |
| ASM-002 | Salvage is more abundant than new manufacturing at target sites         | G.E.C.K. use-case definition     | Medium     | Site survey contradicts salvage availability        |
| ASM-003 | Human operator present and trained during initial deployment            | v0 bootstrap condition           | High       | Autonomous deployment capability demonstrated       |
| ASM-004 | Terrestrial deployment is the primary v0 context                        | Scope definition                 | High       | Marine or orbital deployment becomes primary target |

---

## I. Definition

A G.E.C.K. is the smallest coherent set of tools, data, and doctrine that can:

1. Preserve embodied complexity (triage before destruction)
2. Create replacement parts for itself
3. Bootstrap power, motion, and fabrication capability
4. Retain memory across generations of artifacts

If a deployed kit cannot eventually rebuild itself, it is not a true seed.

---

## II. When a G.E.C.K. Is Deployed

A G.E.C.K. is appropriate when:

- Infrastructure is sparse, damaged, or absent
- Supply chains are unreliable or nonexistent
- Salvage is abundant relative to new manufacturing
- Human presence is limited or temporary

Typical scenarios:
- Remote terrestrial locations
- Disaster recovery zones
- Frontier industrial sites
- Early orbital / lunar deployments
- Marine deployments (see Marine Variant — Section IX)

---

## III. G.E.C.K. Capability Threshold (v0 → v1 Bridge)

A G.E.C.K. must support v0 Forge operations immediately, and enable growth toward v1
using local means.

The Forge loop that defines sufficiency: **intake → triage → process → verify → learn →
repeat.** A G.E.C.K. is sufficient if it allows this loop to close, even in degraded or
partial form. Components that allow the loop to close in a reduced application are Gate C
passes — useful, not critical. Components whose absence breaks the loop entirely are
critical.

---

## IV. Procurement Doctrine

**Purchasing equipment is a valid and often correct bootstrap strategy.**

The G.E.C.K. is a capability seed, not a proof of self-sufficiency. Self-sufficiency is
earned through Forge development over time — it is a v1 and v2 property, not a v0
requirement. At v0, the correct question is not "can we fabricate this?" but "does
fabricating this serve the Forge better than purchasing it?"

**When procurement is the correct path:**

- The component cannot be reliably fabricated at v0 capability levels
- Fabrication cost in time, material, and iteration exceeds commercial availability
- The component requires precision levels the v0 Forge cannot yet achieve
- The component is a known commercial commodity with established reliability data

**Examples of valid v0 procurement targets:** digital calipers, multimeters, servo drives,
induction heaters, quality bearings, precision lead screws, surge protectors, durable
storage media.

**Procurement does not exempt a component from triage.** Purchased components must still
be logged, provenance-tracked, and assessed for dual-use potential per Components.md
annotation standards.

**Precision and procurement are linked.** Some precision cannot be bootstrapped at v0. A
commercially available measuring instrument will outperform anything a v0 Forge can produce
to measure itself with. Purchasing precision tools early is an investment in the Forge's
ability to verify its own output — which is a Critical function. See Section V (Precision
Threshold) and Components.md item 5 (Metrology).

---

## V. Precision Threshold (Introductory)

*Full treatment deferred to Precision_LF.md — not yet written. This section establishes
the concept and its connection to G.E.C.K. seeding.*

**Precision is a capability gate.** The world's productive capability is bounded by the
precision with which materials can be measured, cut, formed, and verified. A Forge limited
to coarse tolerances cannot produce components that require fine tolerances — and those
components may include the Forge's own upgrade path.

**Precision must be monitored as a Forge metric.** At each version stage, the Forge should
be able to answer: what is our current precision ceiling, and what does it prevent us from
building? Improvement in precision ceiling is a graduation criterion, not merely a
performance optimization.

**The G.E.C.K. seeds precision capability deliberately.** The Sensing & Metrology Module
(Section VI.6) is not generic instrumentation — it is the Forge's initial precision floor.
What the G.E.C.K. brings determines what the v0 Forge can verify, and therefore what it
can reliably produce.

*Cross-reference: Components.md CO-002 (Metrology Precision Thresholds). Full precision
doctrine to be developed in Precision_LF.md and cross-referenced from Components.md,
Version Mapping, and Graduation Rule.*

---

## VI. Core G.E.C.K. Modules (Critical)

### 1. Power & Energy Module
- Portable generation (engine, solar, or hybrid)
- Energy storage (batteries, capacitors)
- Power conditioning and distribution
- **Minimum at v0: surge protection on all sensor, compute, and memory circuits**

*Reason: No power, no learning. Power instability that corrupts Artifact Memory or
Baseline Observability defeats two Critical components simultaneously.*

---

### 2. Triage & Salvage Module
- Multimeter
- Basic electrical loads
- Hand tools
- Marking and tagging system

*Reason: The Forge must recognize value before it destroys it.*

---

### 3. Motion & Actuation Module
- At least one reliable motor
- Linear motion components (rails, screws, belts)
- Basic bearings and couplings

*Reason: Motion enables every other capability.*

---

### 4. Fabrication Module (Minimal)
- Small metal AM system or CNC / hybrid tool
- Manual machining tools (drill press, grinder)
- Welding or joining capability

*Reason: The seed must be able to repair and extend itself.*

---

### 5. Thermal Module
- Heat source capable of controlled temperatures
- Basic temperature measurement
- Insulation and containment

*Reason: Metallurgy begins with heat control.*

---

### 6. Sensing & Metrology Module
- Calipers and micrometers
- Scale
- Simple optical inspection

*Reason: Discernment requires measurement. This module establishes the v0 precision
floor — what the Forge can verify determines what it can reliably produce. Precision
instruments are a valid and recommended procurement target; commercial metrology tools
at v0 will outperform anything the Forge can self-fabricate. See Section V.*

---

### 7. Memory & Doctrine Module
- Local compute
- Durable storage media
- Core Lazarus Forge documents
- Artifact and triage logs (digital or paper)

*Reason: Without memory, growth resets every generation. Doctrine allows a newly
instantiated Forge to inherit prior lessons, operational heuristics, failure
classifications, and survival instincts without rediscovering them physically.*

---

### 8. Human Interface Module
- Manual overrides
- Clear labeling
- Simple operator instructions

*Reason: Early Forges are taught, not autonomous.*

---

## VII. What a G.E.C.K. Deliberately Does NOT Include

- High-throughput automation
- Exotic alloys
- Full autonomy
- Space-rated hardware (unless mission-specific)

These emerge through growth, not seeding.

---

## VIII. G.E.C.K. Success Criteria

A deployed G.E.C.K. is considered successful when it can:

- Replace its own failed components
- Upgrade at least one module using local material
- Generate surplus value through repair or fabrication
- Preserve and transfer its operational memory
- Demonstrate measurable precision floor for at least one output class *(Placeholder — metric not yet defined; see CO-002 in Components.md)*

---

## IX. Scaling Beyond the Seed

Once self-replacement is proven, the Forge graduates:

- G.E.C.K. → v1 Forge: Closed-loop material recycling
- v1 → v2: Reduced human dependency
- v2 → v3: In-situ resource utilization

---

## X. Marine Variant (Exploratory)

*Status: Exploratory — not binding for v0 terrestrial demonstration. Routes to
Trajectories_LF.md v1/v2 scope for full specification. See GK-003 and GK-004.*

A marine G.E.C.K. seeds a Leviathan unit or Support Raft deployment from minimal
resources in an open-ocean or coastal environment. The terrestrial module list applies
with the following modifications and additions.

**Shared with terrestrial G.E.C.K. (largely unchanged):**
- Memory & Doctrine Module — waterproofed, pressure-tolerant storage
- Human Interface Module — simplified for intermittent operator contact
- Sensing & Metrology Module — corrosion-resistant instruments

**Modified modules:**

*Power & Energy Module (marine):*
- Primary: sealed battery bank, pressure-rated
- Supplemental: solar panels with marine-grade mounting, wave energy if available
- No combustion engines in submerged configurations
- Induction charging pad for Leviathan unit recharge *(Placeholder — pad design not yet
  specified; see GK-003)*

*Triage & Salvage Module (marine):*
- Waterproof multimeter and test equipment
- Marine salvage tools (cutting, lifting, retrieval)
- Contamination assessment for marine-recovered materials (biofouling, salt, corrosion)
- Tagging system rated for submersion

*Fabrication Module (marine):*
- Corrosion-resistant tooling preferred
- Welding capability adapted for humid/salt environment
- 3D printing materials must resist salt and UV degradation *(Placeholder — see GK-004)*

**Marine-specific additions:**

*Hull & Buoyancy Module (marine-critical):*
- Minimum viable hull sufficient to support module payload
- Passive buoyancy reserve — unit must surface safely without power
- SWATH or pontoon configuration preferred for stability
- Sacrificial anode system for galvanic corrosion protection *(Placeholder — material
  selection not yet specified; see GK-002)*

*Biofouling Management Module (marine-critical):*
- Sacrificial Shell System: designed colonization zones, scheduled shedding, structured
  reef substrate contribution per Support_Raft_v0.md doctrine
- Fouling monitoring — detect colonization growth rate
- Shedding mechanism — mechanical, chemical, or biological *(Placeholder — mechanism
  not yet specified)*

**Marine G.E.C.K. success criteria:**
- Unit remains positively buoyant under degraded conditions
- Triage loop closes using marine-salvaged material
- Self-replacement demonstrated for at least one hull-exposed component
- Operational memory survives one full biofouling cycle

**Marine G.E.C.K. explicit non-goals (v0):**
- Full underwater operation — surface or near-surface only
- Deep pressure tolerance — Leviathan-class depth is a separate program
- Full energy independence — grid or tender-assisted charging acceptable at v0

---

## XI. Guiding Axioms

- A seed that cannot grow is cargo.
- Tools matter less than the order they are used.
- Memory is the most compact machine.
- A marine seed that cannot float is not a seed.
- Purchasing precision is not a failure of doctrine — it is triage applied to the seed itself.

---

> The G.E.C.K. is not meant to impress. It is meant to survive.

This document defines the minimal conditions for Forge genesis and should change only
with demonstrated field experience.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|----------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review  | Forge loop left implicit in prior versions | Sufficiency criterion in Bootstrap Doctrine had no falsifiable anchor | Forge loop explicitly defined: intake → triage → process → verify → learn → repeat | Anecdotal | No |
| —        | —             | —              | —           | No operational entries yet — document is pre-deployment | — | — |

*Priority entries to capture when marine variant is first deployed: (1) which terrestrial
modules transferred cleanly vs. required significant modification; (2) actual biofouling
cycle timeline vs. predicted; (3) which hull configuration provided adequate stability at
minimum cost.*

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### GK-001 — Forge loop not explicitly defined in prior versions

| Field         | Value         |
|---------------|---------------|
| Status        | Resolved      |
| Risk          | Low           |
| Priority      | Major         |
| Type          | Architectural |
| Blocking      | No            |
| Owner         | geck_forge_seed.md |
| First Logged  | 2026-05-04    |
| Last Reviewed | 2026-05-14    |

**Description:** The Forge loop was not explicitly defined, leaving the sufficiency
criterion in Bootstrap Doctrine without a falsifiable anchor.

**Why It Matters:** Without a defined loop, no component classification decision could be
verified as correct.

**Resolution Path:** Payment via Specification — Forge loop defined in Section III:
intake → triage → process → verify → learn → repeat. Feeds UNK-024 resolution and
UNK-026 (Graduation Rule detection circularity).

---

### GK-002 — Sacrificial anode material selection for marine hull

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Medium             |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** Anode material (zinc, aluminum, magnesium) for the marine G.E.C.K. hull
is not yet selected.

**Why It Matters:** Wrong anode selection accelerates galvanic corrosion of the hull in
deployment environment.

**Resolution Path:** Discharge via Trajectory — standard marine engineering selection
criteria apply (zinc for saltwater, magnesium for freshwater, aluminum general-purpose).
Add material selection table to marine variant when first deployment environment is
confirmed.

---

### GK-003 — Induction charging pad design for Leviathan unit recharge

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** Pad geometry, power transfer efficiency, alignment tolerance, and depth
rating for the induction charging interface between Support Raft and Leviathan units are
not yet defined.

**Why It Matters:** Without a defined interface, Leviathan units cannot be reliably
recharged from the Support Raft in operational conditions.

**Resolution Path:** Discharge via Trajectory — depends on Leviathan unit power envelope
(UNK-006) and hull design. Route full specification to Trajectories_LF.md v1/v2 scope.

---

### GK-004 — Marine 3D printing material durability in salt/UV environment

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Technical          |
| Blocking      | No                 |
| Owner         | geck_forge_seed.md |
| First Logged  | 2026-05-04         |
| Last Reviewed | 2026-05-14         |

**Description:** AM materials suitable for parts exposed to salt spray, UV, and biofouling
pressure in a marine deployment context have not been identified.

**Why It Matters:** Parts that degrade faster than the Forge can replace them break the
loop.

**Resolution Path:** Discharge via Lessons Learned — literature review of marine-grade
polymers used in existing ocean buoy and AUV programs (MBARI, WHOI specs are publicly
available analog data). Placeholder until first marine deployment selects a specific AM
system.

---

### GK-005 — Precision doctrine home document not yet created

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | Low                |
| Priority      | Minor              |
| Type          | Architectural      |
| Blocking      | No                 |
| Owner         | geck_forge_seed.md |
| First Logged  | 2026-05-14         |
| Last Reviewed | 2026-05-14         |

**Description:** Section V introduces precision as a capability gate and Forge metric but
defers full treatment to Precision_LF.md, which does not yet exist.

**Why It Matters:** Without a home document, the precision insight remains introductory
and cannot be cross-referenced with full force from Components.md, Graduation Rule, or
Version Mapping.

**Resolution Path:** Payment via Specification — create Precision_LF.md covering: precision
as a capability gate, precision ceiling as a tracked Forge metric, precision improvement
as a graduation criterion, and procurement of precision instruments as a seeding strategy.
Cross-reference from Components.md Metrology (item 5), CO-002, and Version Mapping.

---

### Resolution Log

- 2026-05-04: **GK-001** — Resolved. Forge loop explicitly defined in Section III.
- 2026-05-04: **UNK-005** — Partially resolved. Marine G.E.C.K. variant stub added
  (Section X). Full specification deferred to Trajectories_LF.md v1/v2 scope.
- 2026-05-14: File retrofitted to canonical LF_File_Template structure. File State, Scope
  Boundary, File Purpose, Assumptions, Procurement Doctrine (Section IV), Precision
  Threshold introduction (Section V), Active Disputes, structured unknown tables, and
  Abandoned Paths added.
- 2026-05-14: **GK-005** logged — Precision_LF.md identified as needed home document for
  full precision doctrine.

---

## Abandoned Paths

| Date     | Path | Why Abandoned | Reconsider? |
|----------|------|---------------|-------------|
| May 2026 | Treating purchased equipment as outside G.E.C.K. doctrine | Procurement is triage applied to the seed. Excluding it created an implicit assumption that bootstrap realism requires fabricating everything from salvage, which is false and counterproductive at v0. | No |

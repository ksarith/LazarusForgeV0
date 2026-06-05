# Facilities.md — LazarusForgeV0

> ⚠️ **Operational Safety Advisory**
> This file governs the physical environment in which arc welding, induction heating,
> pyrolysis-adjacent processes, and powered reduction equipment operate. An inadequate
> facility is not a degraded-mode problem — it is a silent prerequisite failure that
> makes every other module unsafe by default. Combustible flooring beneath a welding
> station, inadequate airflow topology, or uncontrolled egress paths cannot be
> compensated for by process-level precautions alone. Open unknown FA-001 (site
> confirmation) means no specific facility has been validated against these constraints.
> When in doubt about site adequacy, hold — do not begin hot operations until flooring,
> airflow, and egress have been physically verified.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-05                                                          |
| Auditor          | Claude — Architect/Auditor                                          |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Minimum physical environment constraints for v0 Forge operations
- Nonburnable flooring as a hard prerequisite for hot operations
- Airflow topology doctrine (negative pressure zones, exhaust routing hierarchy)
- Triangle workstation layout principle
- Environmental baseline — Arkansas climate context (heat, humidity, seasonal variation)
- Utility access doctrine (grid power, water, egress)
- Hazard zone separation principles
- Floor loading classification guidance for heavy equipment
- Bootstrap facility proxy — operating with available space under stated constraints

**This file DOES NOT define:**
- Air Scrubber hardware specifications or staging (→ `Operations/Air_Scrubber.md`)
- Safety program, PPE requirements, or hearing conservation (→ `Admin/Safety_Protocols.md` [PLANNED])
- Energy infrastructure beyond grid connection requirements (→ `Operations/Energy.md`)
- Specific module layouts or equipment footprints (→ owning gate files)
- Noise exposure limits (→ `Admin/Safety_Protocols.md` [PLANNED])
- Legal zoning compliance or permitting (→ FA-003 — human decision)
- Marine or off-site deployment environments (→ `Tests/Support_Raft.md`, `Tests/Leviathan_testing.md`)

---

## File Purpose

This file exists to resolve UNK-006 — the facility siting unknown referenced by seven
repository files with no owning document. Its purpose is not to specify a particular
building or layout, but to define the minimum physical environment constraints that any
v0 site must satisfy before hot operations begin. Without this file, every module that
depends on physical space assumptions is operating on undeclared premises. If this file
disappeared, no principled site assessment could be made and the repository would have
no record of what the facility is expected to provide versus what individual modules
are responsible for providing themselves.

---

## Assumptions

| ID      | Assumption                                                                   | Basis                                      | Confidence | Expiry Trigger                                              |
|---------|------------------------------------------------------------------------------|--------------------------------------------|------------|-------------------------------------------------------------|
| ASM-001 | Grid power available at v0 bootstrap site                                    | Inherited from Components.md ASM-001       | Medium     | Off-grid deployment confirmed — route to Energy.md          |
| ASM-002 | Covered indoor or semi-enclosed space available                              | Arkansas climate — humidity, storm exposure | Medium     | Site survey contradicts covered space availability          |
| ASM-003 | Nonburnable flooring available or installable at acceptable cost             | Concrete slab common in industrial/garage  | Medium     | Site survey shows combustible-only flooring with no remedy  |
| ASM-004 | Adequate natural or forced airflow achievable at v0 bootstrap                | Air_Scrubber.md negative pressure doctrine | Medium     | Airflow modeling shows inadequate exhaust path              |
| ASM-005 | Human operator physically present during all hot operations at v0            | Bootstrap Doctrine — inherited from Components.md | High  | Autonomous operation capability demonstrated and validated  |
| ASM-006 | Arkansas climate baseline applies (hot-humid summers, mild winters, storm exposure) | Geographic context                   | High       | Site located outside Arkansas climate zone                  |

---

## I. Core Constraint — Nonburnable Flooring

Nonburnable flooring is the single hardest facility constraint at v0. It is not a
preference, a best practice, or a future upgrade path. It is a prerequisite for any
hot operation — arc welding, induction heating, pyrolysis staging, or reduction
equipment with spark potential.

**What qualifies:**
- Poured concrete slab (preferred — common in garages, warehouses, agricultural buildings)
- Concrete block or brick over packed earth (acceptable with inspection)
- Bare compacted earth with no embedded combustibles (marginal — document and review)

**What disqualifies:**
- Wood subfloor or plywood decking, regardless of surface treatment
- OSB, particle board, or engineered wood panel
- Rubber matting or foam underlayment as the primary floor surface over combustibles
- Carpet, vinyl, or laminate over combustible substrate

**Bootstrap proxy:** If a site has partial nonburnable flooring, hot operations are
restricted to the nonburnable zone. Combustible-floor areas may support intake, storage,
triage, and cold assembly only. Document the boundary. Do not let the boundary drift.

**Upgrade path:** Poured concrete overlay is achievable over existing slabs and some
subfloors. Route to FA-001 for site-specific assessment.

---

## II. Airflow Topology Doctrine

This file owns the spatial logic of airflow through the facility. Hardware specifications
for capture, filtration, and scrubbing belong to `Operations/Air_Scrubber.md`. What this
file defines is where exhaust goes, how zones relate to each other, and what the negative
pressure hierarchy looks like at the facility level.

### Negative Pressure Hierarchy

Hot process zones (arc welding, induction, pyrolysis staging, reduction) must operate
at negative pressure relative to adjacent areas. This means:

- Exhaust paths must exit the building, not recirculate to occupied or storage zones
- Fresh air supply enters from the cleanest available direction (away from exhaust outlets)
- Triage, intake, and storage zones sit upstream (positive pressure side) of process zones
- Human operator positions are always on the fresh-air side of any process exhaust plume

### Minimum Airflow Topology at Bootstrap

At v0 with minimal equipment, the minimum acceptable configuration is:
1. At least one dedicated exhaust path from the hot process zone to outside
2. Makeup air available (open door, vent, or window) on the opposite side of the space
3. No recirculation of process exhaust through HVAC into occupied areas

Forced ventilation (fans, blowers) supplements but does not replace directional topology.
A powerful fan exhausting in the wrong direction is worse than no fan.

### Arkansas Climate Consideration

High summer humidity (regularly 70–90% RH) affects airflow planning:
- Humid makeup air accelerates corrosion on exposed metal stock — storage zones need
  separation from process exhaust makeup air paths where possible
- Summer heat load inside enclosed spaces demands airflow even when process exhaust
  is not the primary concern — operator heat stress is a real failure mode
- Storm season (spring, early summer) means exhaust penetrations need weather protection
  — an exhaust path that floods during rain is an airflow path that fails when most needed

---

## III. Triangle Workstation Layout Principle

The triangle workstation principle applies where human operators coordinate multiple
process steps in sequence. The core idea: the three most frequently accessed positions
in a work sequence form a triangle, minimizing travel distance and keeping the operator
oriented without turning their back on active processes.

**Application to Forge layout:**

A v0 Forge workstation triangle typically connects:
1. Intake / staging position (where material arrives)
2. Active process position (welding, triage, assembly)
3. Output / verification position (where finished or processed material exits)

**Constraints:**
- Triangle vertices must all be on nonburnable flooring if any vertex involves hot work
- No vertex should place the operator between an active process exhaust and a fresh air
  supply — the operator should never be downwind of their own process exhaust
- The triangle should not cross a hazard zone boundary — a triangle that spans a welding
  zone and a storage zone without a clear boundary is a layout error, not a layout

**Bootstrap realism:** At v0, the triangle may be implicit rather than designed. The
principle is a check against layouts that force unnecessary travel, back-turning on
active equipment, or crossing of hazard zone boundaries repeatedly. If the natural
working pattern already satisfies these constraints, no redesign is needed.

---

## IV. Hazard Zone Separation

The facility contains zones with different hazard profiles. Separation prevents cascade
failures where an incident in one zone compromises another.

### Zone Classes

**Hot Zone** — Arc welding, induction heating, pyrolysis staging, reduction equipment.
Requires: nonburnable flooring, negative pressure airflow, clear egress, no combustible
storage within defined radius (FA-002 — radius not yet defined).

**Warm Zone** — Electronics harvesting, soldering, chemical handling (flux, acids,
cleaning agents). Requires: ventilated but not necessarily negative-pressure; nonburnable
or protected flooring; no open flame within the zone.

**Cold Zone** — Intake, triage, storage, cold assembly, artifact memory and compute.
Requires: covered space, humidity management (Arkansas context), physical separation
from Hot Zone exhaust.

**Egress Corridor** — Unobstructed path from any zone to outside. Must remain clear
at all times. Not a storage location. Not a workspace. Not a temporary staging area.

### Separation Logic

Zones need not be separate rooms — a single open space can contain multiple zones if
the boundaries are marked, respected, and documented. Separation is functional, not
architectural. What matters:
- A zone boundary is defined
- Hot Zone exhaust does not cross into Cold Zone
- Egress corridors do not pass through Hot Zone
- Combustible storage does not occur in or adjacent to Hot Zone

---

## V. Floor Loading

Heavy equipment at v0 (reduction mill, induction unit, large compressor) may exceed
the load capacity of some floors. This is a site-assessment item, not a specification
item — the Forge works with available space.

**Minimum guidance:**
- Poured concrete residential slab: typically 40–50 lbs/sq ft distributed load
- Commercial or industrial slab: typically 125–250 lbs/sq ft
- Equipment with concentrated load points (single feet, skids) requires local
  assessment — a 500 lb machine on four 2-inch pads concentrates load significantly

**Bootstrap proxy:** If floor loading is uncertain, distribute equipment weight across
the largest practical footprint (plywood spreader plates over concrete are acceptable
for this purpose — the combustibility concern is the surface, not the substructure).
Document any equipment that exceeds estimated floor rating. Route to FA-001.

---

## VI. Utility Access Doctrine

### Grid Power

Grid power is assumed available at v0 (Components.md ASM-001). Minimum requirements:
- 240V single-phase service for arc welding (standard residential/light commercial)
- Surge protection on all sensor and compute circuits (Components.md Critical item 6/7)
- Circuit capacity sufficient for simultaneous operation of the expected hot process
  load — do not assume all processes run simultaneously at v0 bootstrap

**Bootstrap proxy:** If grid service is undersized, phase operations sequentially
rather than concurrently. Document the constraint. Route to Energy.md for load planning.

### Water

Water access for wet scrubbing (Air_Scrubber.md Variant 0–3) and general cleaning.
Minimum: outdoor hose bib or indoor utility sink within reasonable distance of scrubber
staging. Drain path required for wet scrubber effluent — do not discharge untreated
scrubber waste to surface water.

### Egress

Minimum two independent egress paths from the Hot Zone. At least one egress path must
be usable while carrying a person — not a roof hatch, not a window requiring a ladder.
Egress paths are marked, unobstructed, and reviewed at the start of each operating session.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### FA-001 — Site not yet confirmed or assessed

| Field         | Value              |
|---------------|--------------------|
| Status        | Open               |
| Risk          | High               |
| Priority      | Critical           |
| Type          | Operational        |
| Blocking      | Yes — blocks all hot operations |
| Owner         | Facilities.md      |
| First Logged  | 2026-06-05         |
| Last Reviewed | 2026-06-05         |

**Description:** No specific v0 site has been confirmed, surveyed, or assessed against
the constraints defined in this file.

**Why It Matters:** All hot operation assumptions — flooring, airflow, floor loading,
utility access — are unvalidated until a site is physically assessed. A site that fails
the nonburnable flooring constraint cannot be remediated by process-level precautions.

**Resolution Path:** Physical site survey against Section I (flooring), Section II
(airflow), Section IV (zone separation), Section V (floor loading), Section VI (utility
access). Document findings. Promote to Draft when at least one site has passed minimum
assessment.

---

### FA-002 — Hot Zone minimum radius not defined

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Major         |
| Type          | Technical     |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** The minimum clearance radius between active Hot Zone processes and
combustible storage has not been defined. Referenced in Section IV but left as a
placeholder.

**Why It Matters:** Without a defined radius, the zone separation doctrine has no
enforceable boundary. An operator can comply with the letter of zone separation while
storing combustibles too close to active welding.

**Resolution Path:** Cross-reference AWS welding safety standards and NFPA 51B for
hot work minimum clearances. Define as a Facilities.md constraint once sourced.
Human verification required — FA-003 may apply.

---

### FA-003 — Legal zoning and permitting not assessed

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Major         |
| Type          | Governance    |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** Local zoning, fire code compliance, and operating permits for
industrial hot work and chemical handling at a v0 site have not been assessed.

**Why It Matters:** Operating without required permits is a legal and safety risk.
Some jurisdictions require inspection of welding and pyrolysis operations regardless
of scale.

**Resolution Path:** Human decision. Scope is jurisdiction-specific and cannot be
resolved by AI audit. Assign to human operator at site selection. Not blocking for
Exploration — blocking for first hot operation.

---

### FA-004 — Arkansas summer heat load impact on operator safety not quantified

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Medium        |
| Priority      | Minor         |
| Type          | Technical     |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** Process heat from arc welding and induction combined with Arkansas
summer ambient conditions (heat index regularly exceeding 100°F) may create operator
heat stress conditions that affect safe operation. No threshold or mitigation doctrine
is defined.

**Why It Matters:** Operator impairment from heat stress is a silent failure mode —
the process continues but judgment degrades. This is relevant to the Human Override
Interface (Components.md Critical item 8) — an impaired operator is not a reliable
override mechanism.

**Resolution Path:** Route to `Admin/Safety_Protocols.md` [PLANNED] for heat stress
doctrine. At minimum, log as an assumption expiry trigger for ASM-005 (human operator
present and capable).

---

### FA-005 — Relationship between Facilities.md and UNK-006 resolution status

| Field         | Value         |
|---------------|---------------|
| Status        | Open          |
| Risk          | Low           |
| Priority      | Minor         |
| Type          | Governance    |
| Blocking      | No            |
| Owner         | Facilities.md |
| First Logged  | 2026-06-05    |
| Last Reviewed | 2026-06-05    |

**Description:** UNK-006 in Unknowns.md references facility siting as an open
cross-module unknown with 7 dependents. This file is the intended resolution target.
UNK-006 should be updated to reflect that Facilities.md now owns this domain, but
closure of UNK-006 requires confirming that all 7 dependent files accept this file
as their siting authority.

**Why It Matters:** If dependent files are not updated to reference Facilities.md,
UNK-006 remains partially open and the cross-module gap persists in Discovery.md's
Cross-Module Unknowns table.

**Resolution Path:** On next audit pass for each of the 7 dependent files
(Gate_01, Gate_03, Gate_04, Gate_05, Gate_06, Electronics, Woodworking), add
`Facilities.md` to their Upstream Dependencies and replace the UNK-006 placeholder
reference with a direct file reference. Update Unknowns.md UNK-006 status to
Resolved when all 7 are confirmed. Update Discovery.md Cross-Module Unknowns table.

---

### Resolution Log

*(empty — first version)*

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| 2026-06-05 | Prescribing a specific facility layout or floor plan | The Forge works with available space. A prescribed layout would be fictional at Exploration stage and would not survive first contact with an actual site. Constraints-based approach adopted instead. | No |
| 2026-06-05 | Deferring this file further due to lack of content | UNK-006 has 7 dependents. The cost of no file exceeds the cost of a thin Exploration file with honest assumptions. Minimum constraint doctrine is sufficient content to open the file. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional triggers
specific to this file:*

- A site is selected and operated without FA-001 being resolved
- Hot operations begin on a site with unverified flooring
- Zone separation boundaries are documented but not physically marked at the site
- Egress corridors are used for storage or staging
- FA-003 (zoning/permitting) is not assigned to a human owner before first hot operation

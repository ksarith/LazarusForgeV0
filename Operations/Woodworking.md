# Woodworking.md — Timber Sourcing, Processing & Fabrication

> ⚠️ **Operational Safety Advisory**
> Felling operations carry lethal risk from falling trees, barber-chair failures,
> and chainsaw kickback — never fell alone and always establish two escape routes
> before the first cut. Power tool operations produce blade ejection, kickback, and
> entanglement hazards that cause permanent injury in fractions of a second. Fine
> wood dust is explosive at sufficient airborne concentration and causes permanent
> respiratory damage from chronic exposure — source capture dust extraction is
> required at all power tool stations. Several common species (black walnut, cedar,
> yew) produce toxic or sensitizing dust; mixed-species milling has uncharacterized
> synergistic exposure effects — see WW-004. PPE (eye, ear, respiratory) and machine
> guarding are non-negotiable prerequisites before any powered operation begins.
> When in doubt, shut down. The cost of a stopped run is always recoverable.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Forge_Audit_Kit.md                                            |
| Last Audit       | 2026-05-29                                                          |
| Auditor          | Grok — Fabricator/Systems                                           |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Timber sourcing hierarchy — salvage, urban, storm-fall, and standing tree
- Felling and chainsaw safety doctrine for small-scale operations
- Green wood handling, rough dimensioning, and drying doctrine
- Power tool and hand tool milling workflows for irregular salvage stock
- CNC/router fixturing methods for slabs and live-edge material
- Heat treatment and surface modification methods
- Joinery and assembly doctrine
- Finishing doctrine for indoor and outdoor applications
- Waste valorization hierarchy through to basic paper making
- Dust and species-specific hazard doctrine
- Arkansas and humid southern US climate context throughout

**This file DOES NOT define:**
- CNC toolpath generation, G-code, or CAM software workflows
  (no dedicated file planned at v0 — inline guidance in Section 4 is sufficient)
- Full shop-wide dust extraction system design
  (→ `Operations/Air_Scrubber.md`)
- Structural engineering calculations for load-bearing wooden members
  (not yet assigned)
- Commercial lumber grading standards or large-scale forestry operations

---

## File Purpose

This file governs the full processing chain for wood within the Lazarus Forge —
from standing tree or salvage source through to finished functional or structural
object. Its emphasis is on salvaged and urban timber, irregular and green stock,
and low-to-high technology methods appropriate for a self-reliant fabrication
environment in humid climates like Arkansas.

Wood is one of the most immediately available fabrication materials in most
terrestrial deployments and one of the most mishandled — premature milling of
green stock, inadequate drying, improper fixturing of irregular slabs, and
uncontrolled dust exposure are recurring failure modes that destroy material
and injure operators. This file exists to prevent those failures by establishing
durable doctrine from the first cut to the finished surface.

If this file disappeared, operators would lack sourcing, drying, and milling
doctrine for salvage timber, repeat known failure modes with green stock, and
have no governing safety doctrine for dust exposure or felling operations.

---

## Assumptions

| ID      | Assumption                                                                                   | Basis                                              | Confidence | Expiry Trigger                                                        |
|---------|----------------------------------------------------------------------------------------------|----------------------------------------------------|------------|-----------------------------------------------------------------------|
| ASM-001 | Basic power tools and hand tools are available at v0 bootstrap                               | Typical fabrication shop context                   | Medium     | Fully off-grid or remote deployment confirmed — tool availability reassessed |
| ASM-002 | Local southern US species (oak, pine, hickory, cedar, sweetgum) dominate material supply     | Arkansas deployment context                        | High       | Relocation to significantly different biome                           |
| ASM-003 | Dust extraction and PPE are implemented per `Operations/Air_Scrubber.md` doctrine            | Cross-module dependency                            | Medium     | Independent shop air quality measurement validates or invalidates current approach |
| ASM-004 | Salvaged and urban timber is structurally usable after proper drying and defect assessment   | Analogous — urban timber salvage practice          | Low        | WW-002 resolved — long-term performance of salvaged urban timber characterized |
| ASM-005 | Air drying at approximately one year per inch of thickness is achievable under Arkansas humidity conditions | Analogous — regional woodworking practice | Medium     | WW-001 resolved — locally validated drying schedules established      |

---

## 1. Sourcing Hierarchy

Consistent with the Salvage Before Reduction principle, timber enters a sourcing
priority sequence:

1. **Salvaged urban and storm timber** — downed trees, demolition lumber, storm
   fall. Highest priority. Zero harvest cost, reduces waste stream.
2. **Pallet and packaging wood** — widely available, often kiln-dried, usable
   for smaller stock. Inspect for heat treatment stamps (HT) vs. methyl bromide
   treatment (MB — reject for indoor use).
3. **Standing tree harvest** — only when salvage sources are insufficient for
   the application. Requires felling doctrine below.
4. **Commercial lumber** — purchased per purchase-what-cannot-be-produced doctrine
   when salvage stock cannot meet dimensional or quality requirements.

**Species guidance for Arkansas and humid southern US:**

| Species     | Class     | Strengths                        | Notes                                      |
|-------------|-----------|----------------------------------|--------------------------------------------|
| White oak   | Hardwood  | Strength, rot resistance, finish | Excellent all-purpose structural and finish |
| Red oak     | Hardwood  | Workability, availability        | Less rot-resistant than white oak          |
| Hickory     | Hardwood  | Hardness, shock resistance       | Difficult to work; excellent for handles   |
| Black walnut | Hardwood | Finish quality, stability        | Juglone sensitizer — PPE required; toxic dust |
| Sweetgum    | Hardwood  | Availability, low cost           | Prone to warping — dry slowly and carefully |
| Shortleaf pine | Softwood | Structural use, availability  | Resinous; dries reasonably well            |
| Eastern red cedar | Softwood | Rot resistance, aroma     | Respiratory irritant dust — PPE required   |
| Osage orange | Hardwood | Extreme rot/insect resistance   | Very hard; excellent for outdoor and ground contact |

---

## 2. Felling and Chainsaw Doctrine

Felling is the highest-risk operation in this file. It is governed by a conservative
doctrine regardless of tree size.

**Never fell alone.** A second person is required for any felling operation —
not to assist with cutting, but to observe and call stop if conditions change
unexpectedly.

**Pre-fell assessment:**
- Identify the natural lean direction of the tree
- Identify two escape routes at 45° angles behind and away from the planned fall
  direction — clear these routes before the first cut
- Assess for widow-makers (dead branches overhead) — do not fell under them
- Assess for barber-chair risk: trees under tension, leaning trees, or trees
  with significant rot at the base can split vertically and kick the butt
  backward unpredictably. If barber-chair risk is present, do not fell without
  specialist assessment.
- Check fall zone for people, structures, and utility lines

**Cutting sequence:**
1. Face cut (notch) on the fall side — depth 1/4 to 1/3 of trunk diameter,
   angle 60–70°. This controls the fall direction.
2. Back cut on the opposite side — slightly above the bottom of the face cut.
   Leave a hinge of uncut wood. The hinge steers the fall.
3. Do not cut through the hinge. A severed hinge loses directional control.
4. When the tree begins to move, disengage the saw, set the brake, and move
   immediately along one of the pre-cleared escape routes — do not watch the tree fall.

**Chainsaw safety minimums:**
- Cut-resistant chaps or chainsaw trousers
- Helmet with face shield and integrated hearing protection
- Steel-toe boots
- Gloves
- Chain brake functional and tested before each session
- Never operate a chainsaw above shoulder height

**Limbing and bucking (sectioning the felled tree):**
- Work from the trunk outward on limbs
- Assess tension and compression in each limb before cutting — a branch under
  compression will pinch the bar; a branch under tension will kick
- Buck (cross-cut) into manageable sections at the felling site before transport
  — moving whole logs is a separate injury risk

---

## 3. Green Wood Handling and Drying

Green wood milled to final dimension will warp, check, and crack as it dries.
The correct sequence is: rough dimension → dry → final mill.

**Rough dimensioning before drying:**
- Crosscut to rough length (add 6–12 inches over final length for end checking)
- Rip to rough width (add 1–2 inches over final width)
- Do not plane or joint to final dimension while green
- End-seal all exposed end grain immediately after crosscutting — paint, wax,
  or commercial end-grain sealer. End grain dries 10–15× faster than face grain
  and is the primary checking site.

**Moisture content targets:**
- Outdoor structural use: 15–19% MC acceptable
- Indoor furniture and joinery: 6–8% MC
- Measurement: pin-type moisture meter minimum; 
  pinless preferred for non-destructive checking of drying progress

**Air drying:**
- Stack on stickers (1-inch square spacers) at 12–16 inch intervals across the width
- Stickers must be aligned vertically across the stack — misaligned stickers
  cause bowing
- Elevate the stack off the ground minimum 12 inches — ground moisture and
  air circulation both matter
- Cover the top only — sides must remain open for airflow
- Rule of thumb for Arkansas conditions: 1 year per inch of thickness *(Analogous
  — see WW-001 for locally validated schedules)*
- Sweetgum and other interlocked-grain species: dry more slowly and under
  restraint (weighted top) to limit warp

**Accelerated drying options:**
- Solar kiln: simple construction, significant time reduction, suitable for v0
- Dehumidifier kiln: faster, requires enclosure and power draw
- Do not accelerate drying beyond the wood's tolerance — surface checking
  and case-hardening (dry shell, wet core) both result from drying too fast

---

## 4. Milling — Hand Tools, Power Tools, and CNC

### Hand Tools

Hand tools are the baseline capability — they function without power, develop
operator material sense, and handle operations that power tools cannot safely
perform on irregular stock.

Core kit minimum: hand saw, jack plane, smoothing plane, chisels (1/4", 1/2",
3/4", 1"), marking gauge, combination square, mallet.

Hand tools are primary for: final fitting of joinery, working with short or
awkward pieces that cannot be safely fed through power tools, and finishing
surfaces where tearout from power tools is unacceptable.

### Power Tool Milling Sequence

For converting rough stock to dimensioned lumber:

1. **Jointer** — flatten one face (reference face)
2. **Planer** — flatten opposite face parallel to reference face; establish thickness
3. **Tablesaw or bandsaw** — rip to width with reference face against fence
4. **Crosscut saw or miter saw** — cut to final length

**Irregular and live-edge stock:**
Salvage timber frequently arrives without a flat reference face. The jointer
cannot safely process highly cupped, bowed, or live-edge stock without a sled.

- Router sled method: build a simple flat sled wider than the workpiece; secure
  the workpiece to the sled with wedges or screws into waste areas; run the
  router across the surface to establish a reference plane; flip and joint or plane
  the opposite face
- Bandsaw sled method: secure the workpiece to a flat sled; resaw to establish
  one flat face; proceed to planer

### CNC and Router Fixturing for Slabs and Irregular Stock

CNC routing of salvage slabs is the hardest fixturing problem in this file.
Irregular geometry, variable thickness, and live edges all work against
standard hold-down methods.

**Vacuum fixturing:**
- Effective for flat or near-flat stock with sufficient surface area
- Requires a vacuum pump and spoilboard with vacuum channels or grid
- Minimum surface area for reliable hold: approximately 50% of spoilboard
  coverage with the workpiece — irregular slabs with large voids or live edges
  may not achieve sufficient contact
- Test hold before running: attempt to shift the workpiece by hand before
  beginning the cut

**Mechanical fixturing for slabs:**
- Sacrifice screws into waste areas outside the finished boundary — most reliable
  method for highly irregular stock
- Locate screw positions before generating toolpaths — screws must not be in
  the path of any tool
- Toggle clamps or cam clamps at the perimeter where geometry allows
- Wedge packs under low corners to prevent rocking before clamping

**Surfacing irregular slabs (flattening):**
- First pass: large-diameter surfacing bit (spoilboard cutter or fly cutter),
  shallow passes (1–2mm), to establish a reference plane across the full slab
- Do not attempt to surface in a single deep pass — deflection and chatter
  increase with depth, and slab rocking under cut load is a real risk
- After first-face surfacing, flip and surface the second face parallel —
  this requires either a reference surface on the spoilboard or a thickness
  gauge to set the second-face pass depth

**Tooling for wood CNC:**
- Upcut spiral: good chip evacuation, but pulls fibers upward — tearout on
  top surface of through-cuts
- Downcut spiral: pushes fibers down — cleaner top surface, poorer chip
  evacuation, heat buildup in deep cuts
- Compression spiral: upcut geometry at tip, downcut above — clean top and
  bottom surfaces, best for sheet goods and shallow-profile work
- For live-edge preservation: climb-cutting the edge profile reduces tearout
  on irregular grain at the boundary — use with caution, requires firm hold-down

**Probing irregular surfaces:**
Where CNC controller supports it, touch-probe the slab surface at a grid of
points before running 3D toolpaths — this maps the actual surface topology
and compensates for residual bow or twist not fully removed by surfacing.
Manual shimming is the v0 alternative: shim the slab flat to the spoilboard
before fixturing, verify with straightedge.

---

## 5. Heat Treatment and Surface Modification

- **Steam bending:** Softens lignin for curves; requires a simple steam box
  and bending forms. Species matters — straight-grained green stock bends
  best; kiln-dried stock is brittle.
- **Shou Sugi Ban (charred finish):** Torch char the surface to a consistent
  depth; wire brush to remove loose char; oil finish seals. Provides genuine
  weather and insect resistance. Depth of char controls durability vs. aesthetics.
- **Oven stabilization:** Low-temperature oven treatment (200–250°F) drives
  residual moisture and can produce color change in some species. Not a
  substitute for proper drying — a wet core will still move after oven treatment.

---

## 6. Joinery and Assembly

**Traditional joinery** (mortise and tenon, dovetail, lap joint) requires no
consumables and produces strong, repairable joints. Skill-dependent but tool-minimal.

**Modern joinery** (pocket screws, biscuits, domino loose tenons) is faster
and more forgiving of minor dimensional variation — appropriate for utility work
and jigs.

**CNC-cut joinery:** Finger joints, box joints, and custom mortise and tenon
profiles are well-suited to CNC. Generates consistent, repeatable joints from
variable stock.

**Adhesive selection:**
- PVA (wood glue): standard for indoor work, excellent strength, water cleanup
- Epoxy: gap-filling, bonds dissimilar materials, waterproof — use for
  irregular fits, voids, and outdoor joinery
- Polyurethane: expands slightly during cure (gap-filling), waterproof,
  bonds to slightly damp surfaces — useful for green or partially dried stock

---

## 7. Finishing

**Surface preparation:**
- Sand through grits — do not skip grits. Typical progression: 80 → 120 → 150 → 180 → 220.
- Sand with the grain on final passes — cross-grain scratches telegraph through finish.
- Raise the grain with a damp cloth after 150 grit on water-based finishes;
  sand lightly at 220 after drying to remove raised fibers.

**Finish selection:**

| Application    | Recommended Finish                      | Notes                                      |
|----------------|-----------------------------------------|--------------------------------------------|
| Indoor furniture | Tung oil, danish oil, hardwax oil     | Penetrating — easy repair, low build       |
| Indoor structural | Varnish, polyurethane                | Film finish — durable, harder to repair    |
| Outdoor         | Marine varnish, teak oil + UV protectant | UV inhibitors critical in Arkansas sun   |
| Highly porous or punky wood | Epoxy stabilization first, then topcoat | Consolidates weak fiber before finishing |
| Charred (Shou Sugi Ban) | Linseed or tung oil seal       | Seals char; enhances weather resistance   |

---

## 8. Waste Valorization

Wood waste follows a hierarchy consistent with Salvage Before Reduction doctrine:

1. **Usable offcuts** — route to component storage; minimum useful size is
   application-dependent but a 12-inch square is a reasonable v0 threshold
2. **Chips and shavings** — animal bedding, garden mulch, compost amendment,
   smoking/BBQ fuel (species-appropriate)
3. **Firewood** — larger offcuts and poor-quality material not suitable for
   fabrication
4. **Biochar** — controlled incomplete combustion produces biochar for soil
   amendment; cross-reference `Operations/Energy.md` for integration with
   biogas and thermal systems
5. **Mushroom substrate** — hardwood chips and sawdust support oyster and
   shiitake cultivation; low-cost, high-value output
6. **Paper pulp** — retting and beating cellulose fiber into sheet form;
   viable for low-volume applications from clean softwood fiber

---

## 9. Dust and Species Hazard Doctrine

Wood dust is a respiratory hazard, a carcinogen at chronic exposure levels
for certain species, and an explosion risk at sufficient airborne concentration.
This is not optional PPE territory.

**Minimum PPE for all powered wood operations:**
- Dust mask: N95 minimum for general operations; P100 half-face respirator
  for known sensitizers (walnut, cedar, exotic species)
- Eye protection: safety glasses minimum; face shield for lathe and routing
- Hearing protection: foam plugs or earmuffs for all sustained power tool use

**Source capture dust collection:**
- Dust collector connected at the tool is more effective than ambient air
  filtration alone — capture at the source before dust becomes airborne
- Minimum: shop vac with HEPA filter at hand tools and router; dedicated
  dust collector at tablesaw, planer, and jointer
- Cross-reference `Operations/Air_Scrubber.md` for system-level air management

**Species-specific hazards:**

| Species         | Hazard                          | Additional PPE              |
|-----------------|---------------------------------|-----------------------------|
| Black walnut    | Juglone sensitizer; respiratory | P100 respirator             |
| Eastern red cedar | Respiratory irritant, sensitizer | P100 respirator           |
| Yew             | Toxic (taxine alkaloids)        | P100; avoid skin contact    |
| Osage orange    | Sensitizer in some individuals  | N95 minimum; monitor        |
| Unknown salvage | Unknown profile                 | P100 until species confirmed |

**Dust explosion risk:**
Fine wood dust suspended in air is explosive. Do not allow dust to accumulate
on surfaces — a sudden disturbance that raises accumulated dust into a cloud
creates an ignition risk. Empty dust collectors regularly. No open flames or
ignition sources in dust-generating areas. Cross-reference WW-004 for
mixed-species exposure threshold unknowns.

---

## Integration Hooks

- `Operations/Air_Scrubber.md` — dust extraction system design, toxic species
  off-gas management, source capture integration
- `Operations/Gate_02_Triage.md` — salvage timber condition assessment follows
  triage logic; defect classification and routing to fabrication vs. firewood
- `Operations/Gate_03_Reduction.md` — low-value wood waste that cannot be
  repurposed follows Reduction doctrine to biochar or compost
- `Operations/Gate_06_Fabrication.md` — wood is a fabrication feedstock;
  fixturing, joinery, and finishing doctrine connects to fabrication workflow
- `Operations/Energy.md` — biochar and wood gas (gasification) are candidate
  energy inputs; firewood and offcuts feed thermal systems
- `Admin/Trajectories.md` — gasification of wood waste as an energy source,
  large-scale timber processing, and structural engineering calculations are
  v1+ scope items

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                          | What Failed                                      | What Was Learned                                                                                   | Confidence | Revalidation Needed |
|------------|---------------|-----------------------------------------|--------------------------------------------------|----------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-29 | Anecdotal     | Immediate final milling of green stock  | Severe warping and cracking after milling to dimension | Always rough dimension first, then dry to target MC, then final mill. Green stock milled to final dimension will move. | Anecdotal  | Yes — validate drying schedule against Arkansas species per WW-001 |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### WW-001 — Locally validated drying schedules for Arkansas species not established

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Technical                          |
| Blocking      | No                                 |
| Owner         | Operations/Woodworking.md          |
| First Logged  | 2026-05-29                         |
| Last Reviewed | 2026-05-29                         |

**Description:** Precise air-drying and kiln schedules for common Arkansas species
under local humidity conditions have not been validated. The one-year-per-inch
rule of thumb is an analog estimate, not a locally measured figure.

**Why It Matters:** Improper drying leads to high material loss through checking,
warping, and case-hardening. Underdried stock in joinery causes joint failure
as the wood continues to move in service.

**Resolution Path:** Compile regional extension service data for Arkansas species;
cross-reference USDA Forest Products Laboratory drying schedules. Validate against
first operational drying stack with moisture meter tracking. Payment via
Specification once locally validated schedules are confirmed and moved to body.

---

### WW-002 — Long-term performance of salvaged urban timber uncharacterized

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Technical                          |
| Blocking      | No                                 |
| Owner         | Operations/Woodworking.md          |
| First Logged  | 2026-05-29                         |
| Last Reviewed | 2026-05-29                         |

**Description:** Durability differences between urban salvaged timber and
forest-grown timber are not characterized. Urban trees grow under different
stress conditions — pollutant uptake, asymmetric growth, soil compaction —
that may affect structural performance and finishing behavior.

**Why It Matters:** Routing urban salvage to structural applications without
understanding its performance profile introduces an uncharacterized failure
mode in load-bearing assemblies.

**Resolution Path:** Survey available literature on urban timber structural
performance. Flag salvaged urban timber as Analogous confidence for structural
use until local testing data exists. Payment via Specification once performance
data from first operational structural use cycle is available.

---

### WW-003 — CNC fixturing best practices for live-edge slabs not validated

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Low                                |
| Priority      | Minor                              |
| Type          | Technical                          |
| Blocking      | No                                 |
| Owner         | Operations/Woodworking.md          |
| First Logged  | 2026-05-29                         |
| Last Reviewed | 2026-05-29                         |

**Description:** Section 4 provides fixturing guidance for irregular slabs but
the methods have not been validated against actual live-edge slab operations.
Vacuum hold performance on high-void slabs is particularly uncertain.

**Why It Matters:** Workpiece movement during CNC routing damages tooling,
destroys the workpiece, and creates a projectile hazard at spindle speeds.

**Resolution Path:** Validate vacuum fixture hold-down force against representative
slab geometries during first operational CNC cycle. Document actual minimum
surface area requirements for reliable vacuum hold. Payment via Specification
once fixturing methods are validated against first operational run.

---

### WW-004 — Dust toxicity thresholds for mixed-species milling uncharacterized

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Technical / Safety                 |
| Blocking      | Yes (for sustained mixed-species   |
|               | operations without P100 respirator)|
| Owner         | Operations/Woodworking.md          |
| First Logged  | 2026-05-29                         |
| Last Reviewed | 2026-05-29                         |

**Description:** Precise exposure limits and synergistic effects when milling
mixed local species simultaneously are not characterized. Sensitizer species
(walnut, cedar) mixed with inert species may produce combined exposures that
exceed single-species thresholds at lower individual concentrations.

**Why It Matters:** Chronic wood dust exposure causes occupational asthma,
nasal cancer, and sensitization reactions that can become debilitating. Mixed
exposure profiles are harder to evaluate than single-species profiles.

**Resolution Path:** Until WW-004 is resolved, treat all mixed-species milling
as requiring P100 half-face respirator minimum — do not rely on N95 alone.
Cross-reference `Operations/Air_Scrubber.md` for source capture requirements.
Consult OSHA wood dust PEL (5 mg/m³ general, 1 mg/m³ for some species) as
minimum compliance baseline. Payment via Specification once mixed-species
exposure profile is characterized and documented.

---

### Resolution Log

*(empty)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet | —    |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

| Trigger | Reason |
|---------|--------|
| WW-004 remains unresolved and N95 masks used for mixed-species milling | Blocking unknown — P100 is the minimum until characterization is complete |
| Felling operations conducted without a second person present | Permanently required — never fell alone is non-negotiable doctrine |
| Green stock milled to final dimension without drying to target MC | Permanently abandoned path — always rough dimension, dry, then final mill |
| CNC operations begun without fixturing hold-down verified by hand | Workpiece movement at spindle speed is a projectile hazard — verify before running |
| Urban salvage timber used in structural applications before WW-002 is resolved | Uncharacterized structural performance — flag as Analogous confidence at minimum |
| Dust collector bypassed or disconnected at any power tool station | Source capture dust collection is non-negotiable — not an optional convenience |
| CNC_Router.md referenced as a dependency | No such file planned at v0 — inline CNC guidance in Section 4 is sufficient |
| Ethical Anchor field absent, altered, or does not match canonical string | Load-bearing integrity requirement — applies to all files |

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

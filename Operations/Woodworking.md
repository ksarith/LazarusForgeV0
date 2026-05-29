# Woodworking.md

> ⚠️ **Operational Safety Advisory**  
> Woodworking involves severe hazards including high-speed blade ejection, kickback from tablesaws/bandsaws, dust explosions from fine airborne particles, and toxic exposure from certain species (black walnut, cedar, yew). Chainsaw/felling operations carry lethal falling tree and chainsaw kickback risks.  
> Prerequisite: Full PPE (eye/ear protection, dust mask/respirator, push sticks, featherboards), proper machine guarding, and dust extraction at source. Never work fatigued or alone on felling.  
> When in doubt, hold and shut down power. The cost of a missed hazard is always higher than the cost of a hold.

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Body Stability | Volatile                                                            |
| Spec Gates     | 0/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                          |
| Last Audit     | 2026-05-29                                                          |
| Auditor        | Grok — Fabricator/Systems                                           |
| Open Unknowns  | 4                                                                   |
| Active Disputes| 0                                                                   |
| Highest Risk   | High                                                                |
| Sidecar Link   | #auditor-notes--unknowns                                            |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

## Scope Boundary

**This file DOES define:**
- Full chain from tree sourcing/harvesting through green wood handling, drying/aging, milling (hand, power, CNC/router), heat treatment, joinery, finishing, and waste valorization (including basic paper making)
- Safety doctrine, species selection guidance (with Arkansas/southern US emphasis), tool workflows, and material behavior principles
- Integration points with fabrication gates, dust management, and salvaged material strategies

**This file DOES NOT define:**
- Detailed CNC toolpath G-code or CAM software tutorials (see CNC_Router.md or specific Gate_06 submodules)
- Full shop-wide dust extraction system design (deferred to Air_Scrubber.md)
- Structural engineering calculations for load-bearing wooden members (see Structural_Engineering.md)
- Commercial lumber grading standards or large-scale forestry operations

## File Purpose

This file exists to provide a durable, end-to-end reference for processing wood from living tree to finished functional or structural object. It supports self-reliant fabrication by emphasizing salvaged/urban timber, low-to-high tech methods, and climate-appropriate techniques for humid regions like Arkansas. Its absence would lead to repeated beginner errors, material waste, safety incidents, and lost institutional knowledge about working with irregular, green, or reclaimed stock.

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Access to basic power tools and hand tools is available for most users | Typical maker/shop context in LazarusForge | Medium | Fully off-grid deployment confirmed |
| ASM-002 | Local southern US species (oak, pine, hickory, cedar, sweetgum) dominate material supply | Arkansas location context | High | Relocation to significantly different biome |
| ASM-003 | Dust extraction and PPE are implemented per Air_Scrubber.md | Cross-module dependency | Medium | Independent validation of shop air quality |

---

## Body

### 1. Sourcing & Harvesting
- Prioritize salvaged urban/storm timber, downed trees, and pallet wood for sustainability and cost.
- Species selection: 
  - Hardwoods (oak, hickory, maple) for strength/durability.
  - Softwoods (pine, cedar) for lightweight/construction.
  - Note toxicity: Black walnut (juglone) is allelopathic and sensitizing; cedar dust is respiratory irritant.
- Felling safety: Use proper chainsaw technique, escape paths, and wedge control. Consult local regulations.

### 2. Green Wood Handling & Drying
- Track moisture content (target <12-15% for indoor use; use moisture meter).
- Air drying: Sticker stacks with 1" spacing, elevated, covered but ventilated. Expect 1 year per inch of thickness in Arkansas humidity.
- Prevent defects: End-grain sealing, slow drying to minimize checking/warping.
- Kiln/solar drying options for acceleration.

### 3. Processing & Milling
**Hand Tools**: Essential for understanding material and fine work. Core kit: handsaws, planes, chisels, scrapers, mallets. Develop skills for repair and low-power scenarios.

**Power Tools**: 
- Rough milling: Bandsaw, jointer, planer, tablesaw.
- Fixturing irregular stock (slabs/live edge).

**CNC/Router Focus**:
- Excellent for salvaged timber: 3D scanning or probing irregular surfaces.
- Vacuum fixturing or screws/clamps for slabs.
- Tooling: Upcut/downcut spiral bits, compression bits for plywood.
- Strategies for live edge preservation and joinery.

### 4. Heat Treatment & Modification
- Steam bending for curves.
- Shou Sugi Ban (charred finish) for weather resistance.
- Oven heat treatment for stabilization and color change.

### 5. Joinery & Assembly
- Traditional: Mortise & tenon, dovetails, lap joints.
- Modern: Domino, pocket screws, biscuits, CNC-cut joinery.
- Adhesives: PVA, epoxy, polyurethane (consider moisture exposure).

### 6. Finishing
- Surface prep: Sanding progression (80-220 grit typical).
- Finishes: Tung oil, linseed, varnish, lacquer, epoxy stabilization for porous wood.
- Outdoor: Marine varnish or oil + UV protectant.

### 7. Waste Valorization
- Hierarchy: Usable offcuts → firewood → biochar → mushroom substrate → paper pulp.
- Basic paper making: Retting, beating pulp, sheet formation on mould/deckle.

### 8. Safety & Dust Doctrine
- Mandatory source capture dust collection.
- Species-specific hazards documented.
- Fire/explosion risk with fine dust accumulation.
(See Air_Scrubber.md for system implementation.)

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-29 | Anecdotal     | Immediate final milling of green wood | Severe warping and cracking | Always rough dimension and dry first | Anecdotal | Yes |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### WW-001 — Optimal drying schedules for Arkansas species

| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | Medium            |
| Priority      | Major             |
| Type          | Technical         |
| Blocking      | No                |
| Owner         | Woodworking       |
| First Logged  | 2026-05-29        |
| Last Reviewed | 2026-05-29        |

**Description:** Lack of precise, locally validated air-drying and kiln schedules for common Arkansas species under local humidity.

**Why It Matters:** Improper drying leads to high material loss and unstable finished goods.

**Resolution Path:** Payment via Specification — compile/test schedules and move to Body.

### WW-002 — Long-term performance of salvaged urban timber

| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | Medium            |
| Priority      | Major             |
| Type          | Technical         |
| Blocking      | No                |
| Owner         | Woodworking       |
| First Logged  | 2026-05-29        |
| Last Reviewed | 2026-05-29        |

**Description:** Unknown durability differences between urban salvaged vs. forest-grown timber (pollutants, growth stress).

**Why It Matters:** Affects structural and longevity decisions.

**Resolution Path:** Payment via Specification.

### WW-003 — CNC fixturing best practices for live-edge slabs

| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | Low               |
| Priority      | Minor             |
| Type          | Technical         |
| Blocking      | No                |
| Owner         | Woodworking       |
| First Logged  | 2026-05-29        |
| Last Reviewed | 2026-05-29        |

**Description:** Limited documented methods for securely holding highly irregular slabs during CNC operations.

**Why It Matters:** Risk of workpiece movement and tool damage.

**Resolution Path:** Payment via Specification.

### WW-004 — Dust toxicity thresholds for mixed species

| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | High              |
| Priority      | Major             |
| Type          | Technical         |
| Blocking      | Yes               |
| Owner         | Woodworking       |
| First Logged  | 2026-05-29        |
| Last Reviewed | 2026-05-29        |

**Description:** Precise exposure limits and synergistic effects when milling mixed local species.

**Why It Matters:** Direct operator health impact.

**Resolution Path:** Payment via Specification (cross-ref Air_Scrubber).

---

### Resolution Log
*(empty)*

---

## Abandoned Paths

| Date       | Path | Why Abandoned | Reconsider? |
|------------|------|---------------|-------------|
| —          | —    | —             | —           |

---

## Drift Indicators
- Body Stability remains Volatile pending practical testing.
- Multiple open unknowns in sidecar.
- Cross-module dependencies (Air_Scrubber.md, CNC_Router.md) require alignment.



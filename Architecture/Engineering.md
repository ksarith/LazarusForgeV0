# Engineering.md

---
## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)
---

> ⚠️ **Operational Safety Advisory**
> Engineering decisions directly govern physical systems that can fail catastrophically
> (structural collapse, energetic release, mechanical failure, fire, or loss of control).
> Incorrect assumptions, inadequate safety margins, or unvalidated models can cause
> injury, death, or total system loss.
> Prerequisite: Apply explicit safety factors, perform failure mode analysis, validate
> with testing, and never bypass calculations with "it should be fine." Cross-reference
> domain-specific files for thermal systems (Thermal_Systems.md), fluid mechanics and
> tribology (Friction_Dynamics.md), salvaged-frame fabrication (Mechanical_Structures.md),
> chemical and electrochemical processes (Chemistry.md), and materials processing
> (Woodworking.md, Plastics.md, etc.).
> When in doubt, increase margin or hold the design. The cost of a missed failure mode
> is always higher than the cost of conservative engineering.

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-11                                                          |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Upstream Dependencies

| File | Dependency |
|---|---|
| `Admin/Ethical_Constraints.md` | Life Preservation; operator safety as foundational constraint |
| `Admin/Safety_Protocols.md` | Safety factors cross-reference; PPE doctrine for structural operations |
| `Architecture/Facilities.md` | Site constraints; RDC climate baseline — substitute your deployment parameters via `Facilities.md` §VII Site Initialization Checklist |

---

## Downstream Dependents

| File | Dependency |
|---|---|
| `Architecture/Mechanical_Structures.md` | Structural safety factors and margin doctrine inherited from this file |
| `Architecture/Thermal_Systems.md` | Systems engineering integration principles |
| `Architecture/Friction_Dynamics.md` | Peer file — broad engineering principles apply across all domains |
| `Architecture/Chemistry.md` | Peer file — materials behavior and derating doctrine |
| `Operations/Gate_06_Fabrication.md` | Forge-specific safety factors and tolerance standards |
| `Operations/Woodworking.md` | Wood derating and moisture behavior doctrine |
| `Operations/Plastics.md` | Materials behavior and failure mode analysis |
| `Architecture/Components.md` | Safety factors for salvaged component graduation |
| `Tests/Leviathan_testing.md` | Engineering principles for autonomous system structural design |

## Scope Boundary

**This file DOES define:**
- Foundational engineering principles, rules of thumb, and decision frameworks for
  the entire LazarusForge
- Core mechanical, structural, and systems engineering fundamentals
- Materials behavior overview and selection guidance
- Forge-specific parameters, safety factors, and climate considerations
  — values use the **Reference Deployment Context (RDC)**; substitute your deployment
  parameters via `Architecture/Facilities.md` §VII Site Initialization Checklist
- Progressive path from basic to high-performance engineering

**This file DOES NOT define:**
- CNC kinematic protection protocols, salvaged gantry rigidity doctrine, or
  fabrication machinery structural specifics
  (→ `Architecture/Mechanical_Structures.md` — peer file)
- Heat transfer, thermodynamic laws, heat pump doctrine, Peltier or TEG systems
  (→ `Architecture/Thermal_Systems.md` — peer file)
- Fluid mechanics, aerodynamics, lubrication regimes, or tribology
  (→ `Architecture/Friction_Dynamics.md` — peer file)
- Chemical and electrochemical principles, corrosion doctrine, contamination
  identification, polymer degradation chemistry, or battery chemistry
  (→ `Architecture/Chemistry.md` — peer file)
- Domain-specific fabrication techniques
  (→ `Operations/Woodworking.md`, `Operations/Plastics.md`, etc.)
- Software engineering or electronics design (→ dedicated files)
- Full regulatory compliance or professional licensure requirements

**Peer file relationship:** `Architecture/Mechanical_Structures.md`,
`Architecture/Thermal_Systems.md`, `Architecture/Friction_Dynamics.md`, and
`Architecture/Chemistry.md` are peer files — same authority level, each owning
a distinct domain. This file owns broad engineering principles. Where a question
is thermal, fluid, tribological, or chemical in nature, the relevant peer file
governs. Conflicts escalate to a human contributor.

## File Purpose

This file exists to provide a single, durable source of engineering truth and
judgment for all Forge activities. It equips builders with condensed principles,
safety discipline, and practical parameters so that designs are safe, effective,
and improvable under real-world constraints including salvaged materials, limited
tools, and variable conditions. Without it, the Forge would suffer repeated design
failures, safety incidents, and inefficient reinvention of fundamental knowledge.

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | Builders have basic math and physics literacy (algebra, geometry, forces) | Typical maker/engineer entry level | Medium | Confirmed lower skill baseline |
| ASM-002 | Access to basic measurement tools and ability to prototype/test | Standard Forge shop capability | High | Fully resource-constrained deployment |
| ASM-003 | Reference Deployment Context (RDC) climate baseline applies — high humidity, thunderstorms, occasional freezes. Builders outside this climate zone must substitute their own parameters via `Architecture/Facilities.md` §VII. | RDC baseline — see `Architecture/Facilities.md` §VII | Medium | Deployment confirmed outside RDC climate zone — substitute via Facilities.md §VII |

---

## Body

### 1. Core Engineering Principles
- **First Principles Thinking**: Break problems down to fundamental physics (forces,
  energy, material properties) rather than analogy or tradition.
- **Margin of Safety**: Apply minimum 2×–4× factors depending on application (higher
  for critical/human-occupied structures, fatigue, or uncertainty).
- **Fail Safe vs Fail Operational**: Design so that failures lead to safe states.
- **Murphy's Law Discipline**: Assume what can go wrong will — design accordingly.
- **Iterate Fast, Fail Small**: Prototype → test → refine before scaling.

**Rule of Thumb**: If you haven't identified at least three ways it can fail, you
haven't thought about it enough.

### 2. Mechanical Engineering Fundamentals
- **Stress & Strain**: Stress = Force/Area. Strain = deformation. Understand Young's
  Modulus, yield strength, ultimate strength.
- **Forces & Moments**: Statics (sum of forces/moments = 0), dynamics, torque.
- **Mechanisms**: Levers, linkages, gears, bearings, fasteners. For tribology
  (friction, wear, lubrication) see `Architecture/Friction_Dynamics.md` §7.
- **Energy & Power**: Conservation, efficiency losses, thermal management. For
  thermal management detail see `Architecture/Thermal_Systems.md`.

### 3. Structural Engineering Basics
- Loads: Dead, live, environmental (wind, seismic, snow — consult your deployment
  region's load data; see `Architecture/Facilities.md` §VII and EN-002).
- Beams, columns, trusses, connections.
- Buckling, deflection, shear, bending moment.
- **Key Formula Reference**: Simple beam deflection, Euler buckling, etc.
  (use FEA sparingly, validate with hand calcs).

### 4. Materials Selection & Behavior
- Key properties: Strength, stiffness, toughness, fatigue resistance, corrosion,
  density, cost, workability.
- Common Forge materials cross-reference: Wood (anisotropic, moisture sensitive),
  metals (ductile vs brittle), plastics, composites.
- Derating: Reduce allowable stresses for temperature, moisture, fatigue, defects
  in salvaged stock.
- **RDC Note**: High humidity (RDC baseline) accelerates rot in wood and corrosion
  in metals — favor rot-resistant species and protective coatings. Arid deployments
  reduce this risk but increase dust and thermal cycling concerns. Substitute your
  climate via `Architecture/Facilities.md` §VII.

### 5. Systems Engineering & Integration
- Define requirements → architecture → interfaces → verification.
- Interface management (mechanical, electrical, thermal).
- Reliability, maintainability, scalability.

### 6. Design & Analysis Methods
- Sketching → CAD → FEA → Physical prototype → Testing.
- Failure Modes & Effects Analysis (FMEA).
- Tolerance analysis (worst-case vs statistical).
- Documentation discipline: Drawings, BOMs, revision control.

### 7. High-Performance Engineering
- Lightweighting (strength-to-weight optimization).
- Topology optimization, lattice structures, composites.
- Extreme environment design (thermal, vibration, corrosion).
- Efficiency & sustainability (energy, material, lifecycle).

### 8. Forge-Specific Parameters & Standards
**Common Safety Factors**:
- Static non-critical: 2–3×
- Structural/human load: 4×
- Fatigue/impact/uncertain materials: 6×+

**Units**: Default to metric (mm, N, MPa) with imperial soft conversions.
Be explicit.

**Tolerances**: ±0.5 mm general fabrication; tighter for bearings/interfaces.

**Environmental Derating** *(RDC baseline — substitute your deployment values via `Architecture/Facilities.md` §VII)*:
- Wood strength: Reduce 20–30% for sustained high humidity (RDC). Arid deployments
  may use lesser derating; tropical deployments should verify against local species data.
- Fastener corrosion allowance: specify galvanized or stainless in wet/humid environments.

**Measurement Standards**: Calibrate tools regularly. Use moisture meters for
wood, torque wrenches for critical fasteners.

### 9. Measurement, Testing & Validation
- Always test to failure on non-critical samples when possible.
- Non-destructive testing (visual, tap, deflection).
- Data-driven iteration: Record loads, failures, conditions.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|--------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-29 | Anecdotal | Relying solely on intuition for safety margins | Near-miss structural issues | Explicit calculation + margin is non-negotiable | Anecdotal | Yes |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| — | — | — | — |

---

## Drift Indicators
- High number of open unknowns reflecting the foundational nature of this file.
- Body Stability Volatile — expected during initial population and cross-module
  alignment.
- Scope boundary revised to absorb thermal, fluid, tribology, or chemical
  doctrine from peer files without logging a dispute — trigger re-audit.
- Verification Ref changed away from `Admin/Verification_Gates_LF.md`.

---

## Auditor Notes & Unknowns

### EN-001 — Validated safety factors for salvaged materials

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | High |
| Priority | Critical |
| Type | Technical |
| Blocking | Yes |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-05-29 |

**Description:** Lack of Forge-specific tested safety factor guidelines when using
urban salvaged or reclaimed materials with unknown history.

**Why It Matters:** Direct impact on structural integrity and safety. No structural
specification in any file may be promoted without this resolved.

**Resolution Path:** Develop tested safety factor table for common salvaged material
categories (structural steel, aluminum extrusion, salvaged timber, unknown alloy).
Promote to Specification when validated against at least one destructive test series.

---

### EN-002 — Deployment-specific environmental load data not compiled

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Engineering.md` |
| First Logged | 2026-05-29 |
| Last Reviewed | 2026-06-11 |

**Description:** Precise local wind, snow, seismic, and humidity derating values for
the deployment region have not been compiled into a structured table. The RDC baseline
provides starting values but is not a substitute for deployment-specific data.

**Why It Matters:** Affects all outdoor and structural designs. A builder in a high
wind or seismic zone using RDC baseline values will be under-margined.

**Resolution Path:** Each deploying builder should compile from their regional
equivalent of ASCE 7 and local meteorological data. A structured table template
will be added to `Architecture/Facilities.md` §VII when EN-002 advances to
In Progress. The `Facilities.md` Site Initialization Checklist Climate Parameters
section (§VII.A) is the interim capture mechanism.

*(Additional unknowns: EN-003 Materials database, EN-004 High-performance low-tech
methods, EN-005 Verification testing protocols — full entries in sidecar.)*

---

### Resolution Log

- 2026-06-11: Navigation Anchors block added. Upstream Dependencies and Downstream
  Dependents tables added. All Arkansas/location-specific references converted to
  Reference Deployment Context (RDC) abstraction with pointer to `Architecture/
  Facilities.md` §VII Site Initialization Checklist. ASM-003 updated to RDC framing.
  EN-002 retitled and description updated to deployment-generic framing. Last Audit
  updated.
- 2026-05-31: Scope boundary updated — peer file references to
  `Architecture/Mechanical_Structures.md`, `Architecture/Thermal_Systems.md`, and
  `Architecture/Friction_Dynamics.md` added. Stale references to retired planned
  files (`Structural_Engineering.md`, `Mechanical_Systems.md`) removed. Verification
  Ref corrected to `Admin/Verification_Gates_LF.md`. Safety advisory cross-references
  updated. Peer file relationship doctrine added to Scope Boundary. Drift Indicators
  section added.

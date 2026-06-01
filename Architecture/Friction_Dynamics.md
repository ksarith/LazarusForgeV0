# Friction_Dynamics.md

> ⚠️ **Operational Safety Advisory**
> Fluid systems under pressure present burst, jet, and whipping hazards. Compressed
> air lines, hydraulic circuits, and pressurized water systems can fail catastrophically
> without warning — particularly when fabricated from salvaged fittings with unknown
> pressure histories. Aerodynamic loads on structures and rotating components at speed
> can exceed static design loads by large multiples; never assume a structure safe at
> speed based only on static testing. Tribological failures — bearing seizure, shaft
> galling, lubrication starvation — typically occur suddenly and without warning, and
> can destroy irreplaceable salvaged components in seconds.
> **Never pressurize a salvaged fluid circuit without a verified pressure relief path
> and a staged proof-pressure test. Never operate rotating machinery above its design
> speed without characterizing the aerodynamic load envelope first.**

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-05-31                                                          |
| Auditor          | Claude — Systems/Engineer                                           |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Foundational fluid mechanics doctrine — properties of fluids, pressure, flow regimes,
  Bernoulli's principle, continuity equation, pipe flow, and hydraulic design rules
- Aerodynamics doctrine — drag, lift, boundary layers, Reynolds number, and airflow
  design for Forge systems (ducting, ventilation, rotating components, hull forms)
- Tribology doctrine — friction, wear mechanisms, lubrication theory, and surface
  interaction for salvaged mechanical components
- Reynolds number as the universal flow regime classifier across all three domains
- Forge integration map — how this doctrine applies to Air Scrubber, Support Raft,
  Leviathan, Gate_04/05 rotating components, and Mechanical_Structures
- Arkansas/southern US climate baseline for fluid and aerodynamic operating conditions

**This file DOES NOT define:**
- Foundational engineering principles, safety factors, or general materials behavior
  (→ `Architecture/Engineering.md` — peer file)
- Thermal properties of fluids or heat transfer in flow systems
  (→ `Architecture/Thermal_Systems.md` — peer file; convective heat transfer
  coefficients live there)
- Air Scrubber hardware specifications, filter selection, or stage sizing
  (→ `Operations/Air_Scrubber.md`)
- Gate_04 rotor geometry, RPM envelope, or sensor specifications
  (→ `Operations/Gate_04_Separation_Mechanical.md`)
- Gate_05 crucible rotation parameters or electromagnetic field design
  (→ `Operations/Gate_05_Separation_Thermal.md`)
- Support Raft SWATH hull structural design or buoyancy calculations
  (→ `Tests/Support_Raft.md`)
- Leviathan mission logic or depth pressure specifications
  (→ `Tests/Leviathan_testing.md`)
- Salvaged bearing dimensional specifications or part numbers
  (→ `Architecture/Components.md`)
- Lubrication product specifications or brand recommendations

---

## File Purpose

This file establishes the fluid mechanics, aerodynamics, and tribology doctrine for
the Lazarus Forge — three domains that appear distinct but share a common foundation:
all three describe what happens at the interface between surfaces and the materials
that flow past or between them.

The Forge encounters these domains constantly and simultaneously. The Air Scrubber
moves contaminated airflow through staged capture — fluid mechanics and aerodynamics
govern every stage. Gate_04's centrifugal rotor operates in a fluid medium and
generates aerodynamic forces on its surfaces. Gate_05's rotating crucible experiences
fluid drag from the molten charge it contains. The Support Raft's SWATH hull is
designed around hydrodynamic drag reduction. Salvaged bearings, shafts, and gearboxes
live or die by tribological conditions. And every pneumatic purge, cooling water loop,
and duct in the facility is a fluid system.

Without a common doctrine layer, each domain file makes its own flow assumptions,
uses inconsistent friction coefficients, and misses cross-domain interactions —
the aerodynamic load on a bearing, the viscosity change of a lubricant with
temperature, the Reynolds number transition that determines whether a duct flows
smoothly or turbulently.

**Relationship to peer Architecture files:** `Architecture/Engineering.md` owns
broad engineering principles; `Architecture/Thermal_Systems.md` owns heat transfer
and thermal energy conversion. This file owns flow, drag, and surface interaction.
All three are peers. Where domains intersect — convective heat transfer in a
fluid loop, thermal expansion affecting bearing clearance — both relevant files
apply and neither overrides the other. Conflicts escalate to a human contributor.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|----|------------|-------|------------|----------------|
| FD-ASM-001 | Arkansas summer ambient conditions: air density ~1.17 kg/m³ at 35°C, 1 atm | Standard atmospheric model | High | Forge relocated to significantly different altitude or climate |
| FD-ASM-002 | Salvaged pipe and fittings have unknown pressure history; derate rated pressure by 50% until hydrostatically tested | Conservative salvage doctrine | High | Hydrostatic proof test completed at 1.5× operating pressure |
| FD-ASM-003 | Salvaged bearing lubricant is contaminated or degraded; strip and repack before any operational use | Bearing life data for contaminated grease | High | Bearing inspected and repacked with verified lubricant |
| FD-ASM-004 | Reynolds number governs flow regime for all fluids in Forge systems; laminar/turbulent transition at Re ≈ 2300 for pipe flow | Established fluid mechanics | High | Flow in non-circular or unusual-geometry passages where standard Re criteria do not apply |

---

## Body

### Section 1 — Fluid Properties and the Continuum Model

A fluid is any substance that deforms continuously under shear stress — both liquids
and gases qualify. The Forge works with both: air in ventilation and pneumatic
systems, water in cooling loops and marine contexts, molten metal in Gate_05, and
various process fluids in the scrubber and pyrolysis systems.

**Key fluid properties:**

**Density (ρ, kg/m³)** — mass per unit volume. Determines inertial forces in flow.
For air at 35°C: ρ ≈ 1.17 kg/m³. For water at 20°C: ρ ≈ 998 kg/m³. For molten
aluminum at 700°C: ρ ≈ 2380 kg/m³.

**Dynamic viscosity (μ, Pa·s)** — resistance to shear deformation. Determines
whether flow is laminar or turbulent and governs pressure drop in pipes.
For air at 35°C: μ ≈ 1.87 × 10⁻⁵ Pa·s. For water at 20°C: μ ≈ 1.0 × 10⁻³ Pa·s.
Viscosity of liquids decreases with temperature; viscosity of gases increases
with temperature — this counterintuitive gas behavior matters for hot duct design.

**Kinematic viscosity (ν = μ/ρ, m²/s)** — the ratio of dynamic viscosity to
density. Used in Reynolds number calculations. For air at 35°C: ν ≈ 1.60 × 10⁻⁵ m²/s.

**Compressibility** — gases are compressible; liquids are effectively incompressible
at Forge operating pressures. Below Mach 0.3 (~100 m/s in air), compressibility
effects are negligible and incompressible flow equations apply to air systems.
No Forge system at v0 approaches this speed.

**Surface tension (σ, N/m)** — relevant for condensation systems, small-diameter
fluid pathways, and the Air Scrubber wet capture stages. Water surface tension at
20°C: σ ≈ 0.073 N/m. Reduced by surfactants, elevated temperature, and contamination.

---

### Section 2 — Pressure, Hydrostatics, and the Pressure Equation

**Static pressure** in a fluid at rest varies with depth:

```
P = P₀ + ρ·g·h
```

Where P₀ is surface pressure, ρ is fluid density, g is gravitational acceleration
(9.81 m/s²), and h is depth below the surface.

*Forge implication — Leviathan/Support Raft:* At 100m depth, hydrostatic pressure
is approximately 10 bar (≈145 psi) above atmospheric. At 1000m depth: ~100 bar.
Every sealed compartment on a deep-operating Leviathan unit must be designed for
the full hydrostatic pressure at maximum operating depth. There is no partial credit
for "close enough."

*Forge implication — Air Scrubber negative pressure:* The scrubber operates below
ambient pressure to prevent outward leakage of contaminated air. The pressure
differential is typically small (50–500 Pa) but the direction is critical. Any
seal failure admits contaminated air outward into the workspace rather than
drawing clean air inward — the wrong direction.

**Gauge pressure vs. absolute pressure:** Gauge pressure is measured relative to
ambient (a car tyre at "35 psi" is 35 psi above atmospheric). Absolute pressure
includes atmospheric (35 psi gauge = ~50 psia at sea level). Always clarify which
convention is in use when specifying pressure limits. For safety-critical components,
use absolute pressure.

---

### Section 3 — The Reynolds Number and Flow Regimes

The Reynolds number is the single most important dimensionless group in fluid
mechanics. It predicts whether flow is smooth and ordered (laminar) or chaotic
and mixing (turbulent):

```
Re = ρ · V · L / μ = V · L / ν
```

Where:
- `ρ` = fluid density (kg/m³)
- `V` = characteristic velocity (m/s)
- `L` = characteristic length (pipe diameter, chord length, particle size)
- `μ` = dynamic viscosity (Pa·s)
- `ν` = kinematic viscosity (m²/s)

**Flow regime thresholds for pipe flow:**

| Re | Regime | Characteristics |
|----|--------|-----------------|
| < 2,300 | Laminar | Smooth, ordered, predictable; low friction; poor mixing |
| 2,300 – 4,000 | Transitional | Unstable; may flip between regimes |
| > 4,000 | Turbulent | Chaotic, high mixing, higher friction; better heat and mass transfer |

**The Reynolds number is universal** — it applies equally to liquids and gases,
to pipe flow and external aerodynamics, to bearing oil films and particle settling.
Any time a flow problem appears, computing Re is the first step.

*Worked example — Air Scrubber duct:*
Air at 35°C (ν = 1.60 × 10⁻⁵ m²/s), duct diameter 150mm, velocity 3 m/s:

```
Re = (3 × 0.15) / 1.60 × 10⁻⁵ = 28,125
```

Fully turbulent. Good for mixing and particulate capture; higher pressure drop
than laminar flow. Design the fan accordingly.

---

### Section 4 — Bernoulli's Principle and the Energy Equation

For steady, incompressible, inviscid flow along a streamline, total mechanical
energy is conserved:

```
P + ½ρV² + ρgh = constant
```

The three terms represent pressure energy, kinetic energy (dynamic pressure), and
potential energy (gravitational head). As velocity increases, static pressure
decreases — this is the Venturi effect, the principle behind carburetors, spray
nozzles, and flow measurement.

**Continuity equation** (conservation of mass for incompressible flow):

```
A₁ · V₁ = A₂ · V₂
```

Flow rate is conserved: if a duct narrows, velocity increases proportionally.
If it widens, velocity decreases. This governs duct tapering, nozzle design,
and the behavior of flow through the Air Scrubber stages.

*Forge implication — Air Scrubber design:* Velocity must be matched to each
capture stage. Particulate capture in the sacrificial intercept stage requires
sufficient velocity for impaction. The polishing stage requires lower velocity
for diffusion capture. Duct cross-sections should be sized for the target
velocity at each stage, not sized uniformly throughout.

*Forge implication — Venturi scrubbing:* A Venturi section accelerates contaminated
airflow to high velocity, then introduces scrubbing liquid at the throat where
static pressure is lowest. The low pressure draws liquid in without a pump.
This is a viable low-complexity wet scrubber design for the Air Scrubber marine
variant using only a fan and a liquid reservoir.

**Pressure drop in pipes and ducts** — the Darcy-Weisbach equation:

```
ΔP = f · (L/D) · (ρV²/2)
```

Where `f` is the Darcy friction factor (depends on Re and surface roughness),
`L` is pipe length, `D` is diameter. For turbulent flow in smooth pipes,
the Moody chart or Colebrook equation gives `f`. A useful rough estimate for
turbulent flow in clean steel pipe: `f ≈ 0.02`.

*Salvage implication:* Corroded, scaled, or internally fouled salvaged pipe has
significantly higher effective roughness than clean pipe — `f` may be 0.03–0.06.
Always assume worst-case roughness for salvaged fluid circuits unless cleaned
and inspected.

---

### Section 5 — Aerodynamics: Drag, Lift, and Boundary Layers

Aerodynamics is fluid mechanics applied to gases — primarily air — with emphasis
on forces generated by relative motion between objects and the surrounding fluid.

#### 5.1 Drag

Drag is the aerodynamic force opposing motion through a fluid:

```
F_drag = ½ · ρ · V² · C_D · A
```

Where:
- `ρ` = air density (kg/m³)
- `V` = relative velocity (m/s)
- `C_D` = drag coefficient (dimensionless — depends on geometry)
- `A` = reference area (m²)

**Note the V² dependence** — doubling speed quadruples drag force. This is why
aerodynamic drag dominates at high speed and is negligible at low speed.

**Drag coefficient benchmarks:**

| Shape | C_D | Context |
|-------|-----|---------|
| Sphere | 0.47 | Droplets, particles, rough approximation for many objects |
| Cylinder (axis perpendicular to flow) | 1.0–1.2 | Pipes, struts, exposed round members |
| Flat plate (perpendicular to flow) | 1.28 | Worst case; broadside-on structures |
| Streamlined body (teardrop) | 0.04–0.08 | Hull forms, Leviathan chassis target |
| SWATH hull (submerged pontoons) | 0.10–0.15 | Support Raft underwater cross-sections |
| Spinning cylinder (Magnus effect) | Variable | Gate_04 rotor in fluid medium |

*Forge implication — Support Raft and Leviathan:* The SWATH (Small Waterplane
Area Twin Hull) design explicitly minimizes the waterplane area to reduce wave-
making resistance. The submerged pontoons are designed as low-C_D streamlined
bodies. Any departure from the streamlined form — barnacle growth, biofouling,
damage — raises C_D and increases drag on the wave-surge conversion system,
reducing power generation efficiency (→ `Challenges/Biofouling.md`).

*Forge implication — Gate_04 rotor:* The centrifugal separation rotor operates
in an air/particulate medium. Aerodynamic drag on the rotor surface consumes
power and generates heat. At high RPM the V² term dominates — rotor drag power
scales as V³ (drag force × velocity). Minimizing rotor surface roughness and
optimizing cross-sectional geometry reduces parasitic power demand.

#### 5.2 Boundary Layers

When fluid flows over a surface, a thin layer of fluid near the surface is slowed
by viscosity — this is the boundary layer. Within the boundary layer, velocity
transitions from zero at the wall (no-slip condition) to the free-stream velocity.

Boundary layers are either **laminar** (smooth, thin, low drag, susceptible to
separation) or **turbulent** (thicker, higher drag, more resistant to separation).
The transition depends on the local Reynolds number based on distance from the
leading edge.

*Forge implication — Air Scrubber impaction stages:* Particulate capture by
inertial impaction depends on particles having sufficient momentum to cross
streamlines near a surface. Turbulent boundary layers enhance this. Baffle
designs in impaction stages should promote turbulence near capture surfaces.

*Forge implication — Leviathan hull design:* Maintaining laminar boundary layer
flow over the hull reduces drag. Biofouling disrupts the smooth surface and
trips the boundary layer to turbulent, increasing drag. This is a quantifiable
performance loss — see SR-012 in `Tests/Support_Raft.md`.

#### 5.3 Lift

Lift is the aerodynamic force perpendicular to the flow direction, generated by
asymmetric pressure distributions around a body:

```
F_lift = ½ · ρ · V² · C_L · A
```

*Forge implication:* At v0, lift is primarily relevant as an unwanted force.
Flat panel structures (gates, covers, solar panels) experience aerodynamic lift
in wind — a flat plate at angle of attack develops lift that can overturn or
carry away unsecured panels. Design attachment points for structures exposed
to wind with aerodynamic uplift in mind. At Arkansas wind speeds (typical
maximum ~25 m/s in severe weather), a 1m² flat panel experiences up to
~375N of aerodynamic force.

#### 5.4 Airflow in Ducts and Ventilation Systems

For duct design, the key parameters are:

**Volume flow rate** Q = A · V (m³/s) — determines fan sizing.

**Fan laws** (scaling relationships for centrifugal and axial fans):
```
Q ∝ N          (flow rate proportional to RPM)
ΔP ∝ N²        (pressure rise proportional to RPM²)
Power ∝ N³     (power proportional to RPM³)
```

Doubling fan speed doubles flow but multiplies power by eight. This makes
fan selection a critical efficiency decision — oversized fans running at
partial speed waste power; undersized fans cannot achieve required flow.

*Forge implication — Air Scrubber fan sizing:* The fan must overcome the total
pressure drop through all scrubber stages (sum of Darcy-Weisbach losses,
fitting losses, and filter media resistance) while delivering the required
volume flow for safe dilution of the highest-concentration contaminant scenario.
Size for the worst case. Then verify the operating point falls on the fan curve
in a stable region (away from surge and stall).

---

### Section 6 — Hydrodynamics for Marine Systems

Water is ~800× denser than air. The same velocity produces ~800× more dynamic
pressure in water than air. This single fact governs all marine hydrodynamic
design decisions.

**Wave-making resistance** — a surface vessel moving through water creates waves.
The energy in those waves is extracted from the vessel's propulsion system. The
SWATH design minimizes waterplane area (the cross-section at the water surface)
and places displaced volume in deeply submerged pontoons, dramatically reducing
wave-making resistance at cruising speeds. This is the primary reason SWATH hulls
are efficient in rough water.

**Froude number** governs wave-making resistance, analogously to Reynolds number
governing viscous resistance:

```
Fr = V / √(g · L)
```

Where V is vessel speed and L is hull length. At Fr > 0.4, wave-making resistance
grows rapidly. SWATH hulls are designed to operate at moderate Froude numbers
where their submerged-pontoon configuration provides maximum advantage.

**Cavitation** — when local fluid pressure drops below vapor pressure, the liquid
flashes to vapor, forming bubbles that collapse violently when pressure recovers.
Cavitation erodes metal surfaces (propellers, pump impellers, valve seats) and
creates noise and vibration. Avoid by keeping fluid velocities in constrictions
below cavitation onset (depends on fluid temperature and vapor pressure).
At 20°C, water vapor pressure is 2.3 kPa absolute — significant margin below
atmospheric. At 80°C it rises to 47 kPa — cavitation becomes a real risk in
hot water circuits.

**Particle settling velocity (Stokes' Law)** — for small spherical particles
settling in a fluid:

```
V_s = (2/9) · (ρ_particle − ρ_fluid) · g · r² / μ
```

Where r is particle radius. *Forge implication — Gate_04:* The centrifugal
separation rotor exploits the same physics as Stokes settling, but substitutes
centrifugal acceleration (ω²r) for gravitational acceleration (g). Higher RPM =
higher effective g = faster separation of denser particles. This is why RPM
characterization (MG-002) is critical to Gate_04 performance.

---

### Section 7 — Tribology: Friction, Wear, and Lubrication

Tribology is the science of interacting surfaces in relative motion — friction,
wear, and lubrication. It is the least glamorous engineering domain and one of
the most practically important. Bearing failures, shaft seizures, and premature
wear of salvaged components are tribological events.

#### 7.1 Friction

**Static friction** — force required to initiate sliding between surfaces:
```
F_static = μ_s · N
```

**Kinetic friction** — force required to maintain sliding:
```
F_kinetic = μ_k · N
```

Where N is normal force and μ is the coefficient of friction. μ_s > μ_k — it
takes more force to start sliding than to maintain it.

**Friction coefficient benchmarks:**

| Surface Pair | Condition | μ_s | μ_k |
|-------------|-----------|-----|-----|
| Steel on steel | Dry | 0.7–0.8 | 0.5–0.6 |
| Steel on steel | Lubricated | 0.1–0.2 | 0.05–0.1 |
| Steel on PTFE | Dry | 0.04–0.1 | 0.04–0.05 |
| Rubber on concrete | Dry | 0.6–0.8 | 0.5–0.7 |
| Ball bearing | Rolling | 0.001–0.003 | — |

*Forge implication:* The difference between lubricated and unlubricated steel-on-
steel is a factor of ~8 in friction coefficient. Lubrication is not optional for
any steel-on-steel bearing surface in the Forge. A salvaged gearbox run without
lubrication will destroy itself in minutes.

#### 7.2 Wear Mechanisms

Four primary wear mechanisms govern component life in salvaged machinery:

**Adhesive wear** — material transfers from one surface to another when asperities
weld and shear. Common in metal-on-metal contacts under high load without adequate
lubrication. Produces a characteristic scored surface finish.

**Abrasive wear** — a harder particle or surface scratches the softer surface.
The dominant wear mode in the Forge's abrasive processing environment. Hard
particulate (silica, metal fines, slag) that enters bearing clearances or shaft
seals acts as a lapping compound, accelerating wear by 10–100×.
(→ `Architecture/Mechanical_Structures.md` §Contamination & Bearing Protection
for the physical seal doctrine that prevents this.)

**Fatigue wear** — cyclic stress causes surface and sub-surface crack initiation
and propagation. Rolling element bearings fail by fatigue wear — the race develops
spalling after a calculable number of stress cycles (L10 bearing life).

**Corrosive wear** — chemical attack of the surface in combination with mechanical
contact. Prevalent in the marine environment (→ `Tests/Support_Raft.md` SR-001)
and in the Air Scrubber wet stages where acid condensate contacts metal components.

#### 7.3 Lubrication Regimes

The Stribeck curve describes three lubrication regimes as a function of speed,
load, and viscosity:

**Boundary lubrication** — surfaces are in direct asperity contact despite
lubricant presence. Load is carried by asperity contacts. High friction and wear.
Occurs at low speed, high load, or lubricant starvation.

**Mixed lubrication** — partial fluid film with some asperity contact.
Transitional regime. Friction and wear intermediate.

**Hydrodynamic (full film) lubrication** — a continuous fluid film fully separates
the surfaces. Load is carried entirely by the fluid pressure. Very low friction
(approaching rolling element bearing values). This is the target operating regime
for all plain bearings in the Forge.

**Film parameter (Lambda ratio)** determines which regime applies:

```
Λ = h_min / √(Ra₁² + Ra₂²)
```

Where h_min is minimum film thickness and Ra is surface roughness. Λ > 3 indicates
full film lubrication. Λ < 1 indicates boundary lubrication. For salvaged bearings
with unknown surface finish, assume Λ is low until proven otherwise — design for
boundary lubrication conditions as the baseline, not hydrodynamic.

#### 7.4 Lubricant Selection Doctrine

The correct lubricant depends on speed, load, temperature, contamination
environment, and material compatibility. At v0, three lubricant types cover
most Forge applications:

**ISO VG 68 way oil (or equivalent)** — high-viscosity oil with anti-stick additives.
Primary lubricant for linear guideways and sliding surfaces in the fabrication
environment. (→ `Architecture/Mechanical_Structures.md` §Contamination & Bearing
Protection.) The high viscosity maintains film thickness against the squeegee
action of contaminated wipers.

**NLGI 2 lithium grease** — general-purpose grease for rolling element bearings,
sealed applications, and slow-speed plain bearings. Widely available, compatible
with most metals, repels water. Do not mix with other grease types — incompatible
thickeners can cause the mixture to liquefy and drain from the bearing.

**Dry lubricant (PTFE, MoS₂, graphite)** — for applications where oil or grease
would attract contamination, degrade in high-temperature zones, or be expelled by
centrifugal action. Gate_04 rotor bearing faces exposed to abrasive feedstock may
benefit from PTFE-coated surfaces over oil-lubricated ones in the long term.

**Salvage lubricant rule:** Strip and repack all salvaged bearings before operational
use. Unknown lubricant history, contamination, and degradation make any inherited
lubrication condition unsafe for Forge operation. (See FD-ASM-003.)

---

### Section 8 — Forge Integration Map

| Downstream File | Relevant Sections | Dependency |
|----------------|-------------------|------------|
| `Operations/Air_Scrubber.md` | §3 (Re for duct flow regime), §4 (Bernoulli, duct sizing, fan laws), §5.4 (airflow in ducts) | All airflow design through scrubber stages depends on these principles |
| `Operations/Gate_04_Separation_Mechanical.md` | §3 (Re for rotor in fluid medium), §5.1 (drag on rotor surfaces), §6 (Stokes settling — centrifugal equivalent) | Separation physics and RPM characterization are fluid dynamics problems |
| `Operations/Gate_05_Separation_Thermal.md` | §1 (molten metal fluid properties), §6 (fluid drag on rotating crucible charge) | Molten charge in rotation behaves as a dense fluid; viscosity changes with temperature |
| `Tests/Support_Raft.md` | §5.1 (SWATH hull drag coefficients), §5.2 (boundary layer and biofouling), §6 (wave-making, Froude, cavitation) | Hull performance is a hydrodynamics problem; all SR unknowns with flow dimensions trace here |
| `Tests/Leviathan_testing.md` | §2 (hydrostatic pressure at depth), §5.1 (drag on unit hull), §5.2 (boundary layer management) | Depth pressure and drag determine power budget and structural requirements |
| `Architecture/Mechanical_Structures.md` | §7.1 (friction coefficients for mechanical contacts), §7.3 (lubrication regimes for guideways), §7.4 (way oil doctrine) | Kinematic interlock and bearing protection doctrine has tribological foundations |
| `Challenges/Biofouling.md` | §5.1 (drag increase from fouling), §5.2 (boundary layer disruption), §7.2 (abrasive wear from biofouling debris) | Quantifies the hydrodynamic cost of fouling and wear mechanisms it introduces |
| `Challenges/Water.md` | §4 (Venturi scrubbing principle), §5.3 (aerodynamic forces on exposed condensation structures) | Atmospheric moisture recovery depends on airflow management around condensation surfaces |
| `Operations/Woodworking.md` | §5.4 (dust transport in ventilation), §3 (Re determines laminar vs turbulent duct flow for dust capture) | Dust extraction system effectiveness depends on airflow regime and velocity |

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|--------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-31 | Modeling / doctrine | — | — | File created; no operational lessons yet | — | At first operational fluid system commissioning |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|----------------|----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-31 | Split into Fluid_Dynamics.md + Aerodynamics.md | Doctrine overlap too significant to split cleanly; Bernoulli, Reynolds number, and boundary layer theory apply equally to both | If file grows beyond practical token budget |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Any downstream file specifies duct velocities, pipe pressure drops, or bearing
  lubrication without referencing this file's doctrine
- Friction coefficients used in mechanical design files deviate from the benchmarks
  in Section 7.1 without logging a dispute here
- Drag coefficient values used for rotor or hull design contradict Section 5.1
  without a logged justification
- Support Raft or Leviathan pressure specifications omit hydrostatic depth pressure
  calculations based on Section 2
- Lubrication specifications in any file contradict the lubricant selection doctrine
  in Section 7.4
- The integration map (Section 8) loses coverage of a file that has introduced
  fluid, aerodynamic, or tribological design decisions

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### FD-001 — Gate_04 centrifugal separation RPM characterization not linked to fluid doctrine

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical — cross-module |
| Blocking | No |
| Owner | `Architecture/Friction_Dynamics.md` |
| First Logged | 2026-05-31 |

**Description:** Gate_04's RPM characterization unknown (MG-002) will produce
empirical RPM-vs-separation data. That data should be interpreted against the
Stokes settling equivalent (Section 6 centrifugal extension) to extract
particle density and size information from the RPM response curves. Without
this interpretation layer, empirical RPM data cannot be generalized to
new feedstock compositions.

**Resolution Path:** When MG-002 generates first empirical RPM-separation data,
develop a worked example in Section 6 of this file that translates measured
separation thresholds into implied particle density/size parameters. This
converts Gate_04 empirical data into generalizable fluid dynamics knowledge.

---

### FD-002 — Air Scrubber duct velocity profile not characterized per stage

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical — cross-module |
| Blocking | No |
| Owner | `Architecture/Friction_Dynamics.md` |
| First Logged | 2026-05-31 |

**Description:** Section 5.4 establishes fan laws and duct velocity doctrine.
`Operations/Air_Scrubber.md` defines five capture stages but does not specify
target velocities at each stage or cross-sectional areas. Without velocity
targets, the scrubber design cannot be validated for capture efficiency at
the particulate sizes and densities generated by each Forge process.

**Resolution Path:** As AS-003 (scrubber waste stream characterization) resolves,
use the particulate size distribution data as input to an impaction efficiency
calculation for each stage. Back-calculate required velocity from target
collection efficiency. Document as a sizing worksheet in Section 5.4 of this
file and cross-reference from Air_Scrubber.md.

---

### FD-003 — Salvaged bearing L10 life estimation protocol not defined

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Technical |
| Blocking | No |
| Owner | `Architecture/Friction_Dynamics.md` |
| First Logged | 2026-05-31 |

**Description:** Section 7.2 introduces fatigue wear and L10 bearing life as
a concept. However, estimating remaining L10 life in a salvaged bearing with
unknown operating history is a non-trivial problem. Without a protocol, the
Forge has no systematic way to decide when a salvaged bearing is safe to
deploy versus when it should be reduced to material.

**Resolution Path:** Define a conservative salvaged bearing acceptance protocol:
(1) visual and tactile inspection (pitting, spalling, rough rotation); (2)
radial and axial play measurement against datasheet limits; (3) conservative
life derating — treat any salvaged bearing as having consumed 50% of its L10
life by default unless evidence suggests otherwise. Append as a subsection to
Section 7.2.

---

### FD-004 — SWATH hydrodynamic performance validation not cross-referenced here

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Low |
| Priority | Minor |
| Type | Cross-reference |
| Blocking | No |
| Owner | `Architecture/Friction_Dynamics.md` |
| First Logged | 2026-05-31 |

**Description:** Section 5.1 and Section 6 provide the hydrodynamic doctrine
for SWATH hull design. `Tests/Support_Raft.md` contains the specific SWATH
geometry and SR unknowns. The cross-reference exists in the integration map
but the reverse link (Support_Raft.md referencing this file for hull drag
doctrine) does not yet exist.

**Resolution Path:** On next audit of Support_Raft.md, add `Architecture/
Friction_Dynamics.md` to its Upstream Dependencies in the Scope Boundary.
Non-blocking; housekeeping.

---

### Resolution Log

- 2026-05-31: File created as `Architecture/Friction_Dynamics.md` — peer
  Architecture file alongside Engineering.md and Thermal_Systems.md. Sections
  1–8 drafted covering fluid properties, pressure and hydrostatics, Reynolds
  number and flow regimes, Bernoulli and duct design, aerodynamics (drag, lift,
  boundary layers, duct airflow), hydrodynamics for marine systems, tribology
  (friction, wear mechanisms, lubrication regimes and selection), and Forge
  integration map. Abandoned path logged for the considered split into two
  files. FD-001 through FD-004 logged. Spec Gate 0/6 — Exploration status.
  Verification Ref set to `Admin/Verification_Gates_LF.md`.

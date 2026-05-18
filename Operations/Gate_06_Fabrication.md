# Gate_06_Fabrication

> ⚠️ **Operational Safety Advisory**
> Arc welding produces UV radiation, infrared, and arc
> flash hazards that cause permanent eye damage in
> seconds without proper shielding. Arc eye gives no
> immediate pain warning — operators do not realize
> they have been injured until hours later. A welding
> helmet with appropriate shade lens, flame-resistant
> gloves, and protective clothing are non-negotiable
> prerequisites before the first arc is struck. Welding
> fumes from unknown alloy base metal — particularly
> galvanized or zinc-coated material — cause metal fume
> fever. Ventilation is not optional. PPE is a
> prerequisite, not a preference.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Forge_Audit_Kit.md                                            |
| Last Audit       | 2026-05-15                                                          |
| Auditor          | Claude — Retrofit/Auditor                                           |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 1                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

*Medium risk reflects operator safety exposure from arc
welding — UV radiation, infrared, and arc flash are
credible hazards requiring PPE and physical shielding.
Fabrication failures are recoverable — parts can be
remade, welds can be ground out, excess material
accommodates rework. Risk is operator-facing, not
process-irreversible. Distinct from Gate_03_Reduction
High risk which reflects process irreversibility.*

---

## Scope Boundary

**This file DOES define:**
- Fabrication doctrine and priority order
- Arc welding as the v0 proof-of-concept gatekeeper
  capability and the entry point for all subsequent
  fabrication method introduction
- Add-to-excess and mill-to-spec as the primary
  dimensional control philosophy
- Welding wire feedstock requirements and
  qualification criteria
- Precision ceiling doctrine — how the forge tracks
  its current precision capability and how precision
  improvement unlocks new fabrication capabilities
- Operator safety requirements for arc welding —
  PPE, shielding, ventilation
- Method introduction and qualification criteria —
  how new fabrication methods enter the system
- Fabrication priority order — what gets made first
  and why
- Feedback loop to gate classification rules —
  fabricated parts feed back into Component Library
  and repair capability
- Integration with upstream material outputs from
  Gate_04_Separation_Mechanical.md and
  Gate_05_Separation_Thermal.md
- Integration with Utilization as the downstream
  performance validation stage

**This file DOES NOT define:**
- Wire extrusion nozzle design and draw speed
  control (Operations/Gate_05_Separation_Thermal.md
  — SC-004)
- Welding wire chemical qualification beyond
  functional performance testing
  (not yet assigned — UNK-008)
- Laser welding specification
  (deferred — Admin/Trajectories.md)
- Powder welding specification
  (deferred — Admin/Trajectories.md)
- Machining and milling hardware specification
  (not yet assigned — GF-003)
- Casting, pressing, or forging methods
  (deferred — Admin/Trajectories.md)
- Energy accounting for fabrication operations
  (Operations/Energy.md)
- Facility siting and fabrication area safety
  beyond operator PPE doctrine
  (UNK-006 — no file exists yet)
- Component Library specification and management
  (Architecture/Components.md)
- Utilization performance metrics
  (downstream — GF-005, not yet assigned)

---

## File Purpose

Gate_06_Fabrication is the constructive stage of the
Lazarus Forge — the point where recovered and purified
material becomes functional parts, tools, and
infrastructure. Every upstream gate exists to deliver
material here in a condition suitable for fabrication.
Every downstream stage depends on what fabrication
produces.

Arc welding is the v0 proof-of-concept capability and
the gatekeeper for all subsequent fabrication method
introduction. It was chosen because it has the lowest
overhead path to joining metal parts, requires no
precision machining or expensive tooling to begin, and
produces structural capability from variable-quality
feedstock. Once arc welding works, the forge can
fabricate, repair, and begin closing the self-replication
loop. Subsequent methods — powder welding, laser
welding, casting, pressing — are introduced through
the method qualification framework this file defines,
not independently.

The primary dimensional control philosophy is
add-to-excess and mill-to-spec. Fabrication builds
or joins with intentional material surplus. Material
removal — grinding, milling, filing — achieves final
dimensions. This approach accommodates variable
feedstock quality and imprecise forming methods by
separating the joining step from the precision step.
The weld gets close. The mill finds the truth.

Precision is tracked as a first-class capability
metric. The forge's current precision ceiling
determines which components and capabilities are
within reach. Precision improvement — through better
tooling, better metrology, better process control —
opens fabrication paths that were previously
unavailable. Gate_06 owns this tracking because
fabrication is where the precision ceiling gets
tested against real part requirements.

If this file disappeared, the forge would have no
governing doctrine for its constructive stage. Arc
welding would have no qualification pathway. New
fabrication methods would have no introduction
criteria. The precision ceiling would have no owner.
The self-replication loop would have no fabrication
doctrine to close against.

---

## Assumptions

| ID | Assumption | Basis | Confidence | Expiry Trigger |
|---|---|---|---|---|
| ASM-001 | Welding wire produced by Gate_05_Separation_Thermal.md extrusion path is of sufficient quality for structural arc welding — external wire sourcing may be required at bootstrap if internal production is not yet validated | SC-004 wire extrusion planned path; purchase-what-cannot-be-produced doctrine covers bootstrap gap | Low | SC-004 wire extrusion validated and first arc weld with internally produced wire demonstrates structural adequacy |
| ASM-002 | Add-to-excess is achievable — forming methods consistently produce sufficient material surplus for mill-to-spec removal to reach final dimensions | Dimensional control philosophy; analog fabrication practice | Medium | First operational fabrication cycle characterizes how much excess is achievable and whether removal tooling can reach final dimensions |
| ASM-003 | Material removal capability exists at v0 bootstrap — angle grinder, file, or equivalent available before precision milling equipment | Mill-to-spec step; purchase-what-cannot-be-produced doctrine | Medium | Precision milling equipment acquired — removal capability upgrades from manual to machine |
| ASM-004 | The forge's current precision ceiling is measurable — metrology capability exists to determine what tolerances are currently achievable | Precision ceiling doctrine; Architecture/Components.md Metrology item | Low | Metrology capability specified and validated — precision ceiling becomes a measured value rather than an estimate |
| ASM-005 | Arc welding on variable-quality Spin Chamber output alloys produces structurally adequate welds for v0 applications — alloy composition variation does not prevent functional joining | Arc welding with gradient output; weldability varies by alloy | Low | First arc welding trials characterize weldability of actual Spin Chamber output — acceptable alloy range defined |
| ASM-006 | Fabricated parts meeting v0 functional requirements are sufficient to begin closing the self-replication loop — precision parts are not required at v0 | Self-replication pathway; bootstrap doctrine | Medium | Self-replication loop requires precision parts that v0 fabrication cannot produce — precision ceiling becomes a blocking constraint |
| ASM-007 | Operator PPE for arc welding is available at bootstrap — welding helmet with appropriate shade, gloves, and protective clothing can be sourced before first weld | Operator safety doctrine; purchase-what-cannot-be-produced | Medium | PPE sourcing confirmed before first arc welding operation — non-negotiable prerequisite |

*ASM-001 and ASM-005 are the most technically load-bearing
— wire quality and base metal weldability together determine
whether the arc welding proof-of-concept closes at v0 with
internally produced wire or requires external wire sourcing
at bootstrap. ASM-004 is quietly critical — an unmeasurable
precision ceiling cannot be tracked or improved. Both connect
to Architecture/Components.md Metrology and Baseline
Observability items. Purchase-what-cannot-be-produced doctrine
covers bootstrap gaps in wire, PPE, and metrology equipment.
See README.md.*

---

## 1. Fabrication Doctrine

Fabrication is the constructive stage. Its purpose
is to convert recovered and purified material into
functional parts, tools, and infrastructure that
serve the forge and the ecology it belongs to.

**Priority order:**
1. Tools or components the forge currently lacks
   and cannot obtain through other means
2. Infrastructure that expands forge capability —
   repairs, upgrades, and improvements to existing
   modules
3. Components for inter-forge trade and ecology
   support
4. Output for external use or exchange

This priority order follows Architecture/Forge_flow.md
want/need policy — fabrication serves demonstrated
needs, not hypothetical future uses.

**Fabrication is not terminal:**
A fabricated part that sits unused is not a success.
Utilization and real-world performance are the
validation stage. Fabrication produces candidates
for use — Utilization determines whether they are
fit for purpose.

**The forge fabricates to its current capability:**
Do not attempt fabrication that requires precision
beyond the current ceiling. A part that cannot be
made to spec at current capability waits until
capability improves — it does not get made badly
and used anyway. See Section 5.

**Dynamic and adaptive:**
The fabrication method set is not fixed. Arc welding
opens the door. Operational experience, capability
growth, and network knowledge determine what comes
next. New methods enter through the qualification
framework in Section 6 — not through informal
adoption.

---

## 2. Operator Safety

Arc welding produces hazards that are not visible
until damage is done. UV radiation causes permanent
eye damage — arc eye — from exposures measured in
seconds. Infrared causes skin burns. Fumes from
base metal and coatings are respiratory hazards.
Spatter creates fire and burn risk.

**Minimum PPE for arc welding at v0:**
- Welding helmet with appropriate shade lens —
  shade 10 minimum for MMA/stick welding.
  Auto-darkening preferred. Not optional.
- Leather or flame-resistant welding gloves
- Flame-resistant clothing — no synthetic fabrics
  that melt rather than char
- Closed-toe leather footwear
- Respiratory protection if working with coated,
  painted, or unknown alloy base metal

**Physical shielding:**
- Welding screen or curtain required — protect
  bystanders and equipment from arc flash
- No bystanders within arc flash range without
  appropriate eye protection
- Fire-resistant work surface or welding table

**Fume ventilation:**
- Cross-reference Operations/Air_Scrubber.md —
  welding fumes must be captured or exhausted
- Unknown alloy base metal warrants enhanced
  ventilation — galvanized metal produces zinc
  fumes that cause metal fume fever
- Never weld galvanized, zinc-coated, or
  lead-painted metal without respiratory
  protection and forced ventilation

**PPE is a prerequisite, not a preference:**
First arc welding operation does not begin until
PPE is confirmed available and fitted. See ASM-007.
Cross-reference: UNK-006 siting requirements.

---

## 3. Arc Welding as Gatekeeper

Arc welding is the v0 proof-of-concept fabrication
capability. It gates access to all subsequent
fabrication method introduction.

**Why arc welding first:**
- Lowest overhead path to joining metal parts
- No precision machining or expensive tooling
  required to begin
- Produces structural capability from variable-
  quality feedstock
- Equipment is purchasable at bootstrap —
  basic MMA (stick) welder is commercially
  available at low cost
- Skill is learnable — operator can develop
  competency through practice on scrap material
  before fabricating functional parts

**Arc welding qualification criteria (v0):**
Arc welding is considered qualified when:
1. Operator can consistently produce welds that
   pass visual inspection — no visible porosity,
   cracks, or incomplete fusion on test pieces
2. Destructive test of sample weld demonstrates
   adequate strength for v0 structural applications
   — weld fails in base metal, not at weld joint
3. Wire feedstock is confirmed — internally
   produced from SC-004 or externally sourced
   per purchase-what-cannot-be-produced doctrine
4. PPE confirmed available and operator trained
   in its use
5. Ventilation confirmed adequate per
   Operations/Air_Scrubber.md

**What arc welding qualification unlocks:**
- Structural fabrication from Spin Chamber output
- Equipment repair capability within the forge
- Self-replication pathway becomes operational
- Method introduction framework opens for
  subsequent methods — see Section 6

*Arc welding qualification is the single most
important milestone in v0 fabrication. Everything
else in this file depends on it.*

---

## 4. Add-to-Excess and Mill-to-Spec

The primary dimensional control philosophy of
Gate_06_Fabrication. Fabrication builds or joins
with intentional material surplus. Material removal
achieves final dimensions. The forming step gets
close. The removal step finds the truth.

**Why this approach:**
- Variable feedstock quality means forming precision
  is inherently limited — alloy composition, surface
  condition, and thermal behavior all vary
- Arc welding distortion is real and predictable —
  parts move during welding. Building to excess
  accommodates distortion and allows correction.
- Material removal is more precise than material
  addition at v0 capability levels
- A part with too much material can be corrected.
  A part with too little cannot.

**Add-to-excess doctrine:**
- Design fabrication to produce intentional surplus
  — typically 1–3mm on surfaces requiring dimensional
  accuracy *(Placeholder — excess allowance defined
  by material and process during first operational
  cycle)*
- Weld buildup on worn or damaged surfaces adds
  material before removal to spec
- Cast or formed parts include machining allowance
  in the design

**Mill-to-spec doctrine:**
- Final dimensions achieved through material removal
  — angle grinder, file, lathe, mill in order of
  increasing precision
- Match removal method to required tolerance:
  - Angle grinder — rough shaping, >1mm tolerance
  - File — intermediate, 0.5–1mm tolerance
  - Lathe/mill — precision, <0.5mm tolerance
    *(Placeholder — tolerance ranges defined by
    first operational capability assessment.
    See GF-002)*
- Stop when spec is reached — do not remove beyond
  spec chasing a better surface finish
- If removal overshoots spec: add material and
  restart removal, or assess whether the part
  still meets functional requirements with
  reduced dimensions

**Standardization note:**
Tooling for material removal should be selected
from standardized stock — grinding discs, cutting
wheels, lathe tooling — that can be sourced,
shared, or traded between forge instances.
Bespoke tooling creates single-forge dependencies.

---

## 5. Precision Ceiling

The precision ceiling is the tightest tolerance the
forge can currently achieve and verify. It is a
first-class capability metric — tracked, reported,
and actively improved.

**Why precision ceiling matters:**
- Components and capabilities are gated by precision.
  A bearing seat that requires 0.01mm tolerance
  cannot be fabricated by a forge whose ceiling
  is 0.5mm — the part waits until capability
  improves.
- Attempting fabrication beyond the current ceiling
  produces parts that appear correct but fail in
  service. Silent failure is worse than acknowledged
  limitation.
- Precision improvement is a force multiplier —
  raising the ceiling opens fabrication paths that
  were previously unreachable.

**Precision ceiling components:**
- **Metrology** — what can be measured. A tolerance
  that cannot be measured cannot be held. The
  precision ceiling cannot exceed metrology
  capability. Cross-reference: Architecture/
  Components.md Metrology item.
- **Process control** — what can be repeatably
  produced. Metrology reveals what was made.
  Process control determines what can be made
  again.
- **Tooling** — what the available equipment can
  achieve. A file has a different ceiling than
  a CNC mill.

**Precision ceiling doctrine:**
- Do not fabricate parts requiring tolerance beyond
  the current ceiling — acknowledge the limitation
  and either source the part externally or wait
  for capability improvement
- Purchase precision instruments at bootstrap —
  a commercial caliper outperforms anything a v0
  forge can self-fabricate to measure itself with.
  Per README.md: precision is seeded deliberately,
  not bootstrapped from nothing.
- Track the ceiling explicitly — what is the
  tightest tolerance currently achievable and
  verified? Update when capability changes.
- Report ceiling honestly in fabrication records —
  a part made to 0.5mm tolerance should say so,
  not claim tighter tolerance it was not verified
  to hold

**Precision ceiling at v0 bootstrap (Placeholder):**
- Metrology: commercial caliper — ±0.02mm
  measurement capability *(Analogous)*
- Process: manual grinding and filing —
  ±0.5mm achievable with care *(Analogous)*
- Tooling ceiling: lathe if available —
  ±0.1mm with skilled operator *(Analogous)*

*These are starting estimates. First operational
cycle establishes actual v0 ceiling. See GF-002.*

---

## 6. Method Introduction and Qualification

New fabrication methods enter the system through
a qualification framework. Informal adoption —
using a method before it is qualified — is not
permitted. An unqualified method has unknown
capability, unknown failure modes, and unknown
safety requirements.

**Qualification prerequisites for any new method:**
1. Safety requirements identified and PPE confirmed
   available before first operation
2. Operator training completed — not self-taught
   on functional parts. Practice on scrap first.
3. Capability characterization — what tolerances
   can the method achieve? What materials does it
   suit? What are its failure modes?
4. Integration with existing workflow confirmed —
   how does the method interact with upstream
   material preparation and downstream finishing?
5. Energy requirements characterized and cross-
   referenced to Operations/Energy.md budget

**Method introduction sequence:**
1. Identify need — what fabrication capability
   gap does this method address?
2. Assess prerequisites — is upstream material
   preparation compatible? Is PPE available?
3. Practice qualification — operator demonstrates
   competency on scrap material
4. Capability characterization — produce test
   pieces, measure outcomes, document ceiling
5. First functional use — supervised, on a
   non-critical part
6. Log outcomes — feed back to Lessons Learned
   and Architecture/Forge_Net.md

**Deferred methods (Exploration-level notes):**
- Powder welding — requires powder feedstock
  production capability and laser or plasma
  energy source. Higher precision than arc
  welding. Route to Admin/Trajectories.md v1+.
- Laser welding — requires precision laser
  source and controlled atmosphere. Very high
  precision, low heat input. Route to
  Admin/Trajectories.md v2+.
- Casting — requires mold fabrication capability
  and controlled pour. Lower precision than
  machining but good for complex geometry.
  Route to Admin/Trajectories.md v1+.
- Pressing and forging — requires tooling and
  force application infrastructure. Good for
  high-strength parts. Route to
  Admin/Trajectories.md v2+.

*Each deferred method becomes available when
arc welding qualification is complete and the
relevant upstream capability exists. The system
is dynamic and adaptive — the method set grows
with the forge.*

---

## 7. Welding Wire Feedstock

Welding wire is the consumable that enables arc
welding. At v0, wire sourcing follows a defined
priority path.

**Wire sourcing priority:**
1. Internally produced — Gate_05_Separation_Thermal
   wire extrusion path (SC-004) when validated
2. Externally sourced — commercial welding wire
   purchased per purchase-what-cannot-be-produced
   doctrine until internal production is validated
3. Inter-forge trade — wire produced by another
   forge instance in the ecology

**Wire qualification for arc welding:**
Wire is considered qualified for v0 structural
arc welding when:
- Consistent diameter within acceptable range
  for selected welding process *(Placeholder —
  diameter spec defined by welding process
  selection. See GF-001)*
- No visible surface contamination, oxidation,
  or moisture
- Test weld produces acceptable fusion and
  bead profile on representative base metal
- Destructive test confirms weld strength
  adequate for v0 structural applications

**Wire quality and alloy composition:**
Internally produced wire from Spin Chamber
output will have variable alloy composition.
Variable alloy wire is acceptable for structural
applications where precise mechanical properties
are not required. It is not acceptable for:
- Pressure-bearing applications
- Safety-critical structural members
- Applications requiring known conductivity

For these applications, externally sourced wire
with known composition is required until internal
wire qualification improves.
Cross-reference: UNK-008, SC-004, ASM-001, ASM-005.

---

## 8. Fabrication Feedback Loop

Fabrication is not a terminal process. Every
fabrication event produces data that improves
the system.

**Feedback targets:**
- Gate classification rules — fabricated parts
  reveal what recovered components are actually
  useful for. Classification heuristics improve
  with fabrication experience.
- Precision ceiling tracking — fabrication outcomes
  update the documented ceiling. A part successfully
  made to tighter tolerance raises the ceiling.
  A part that failed to hold tolerance confirms
  the current limit.
- Wire quality characterization — weld quality
  correlates with wire alloy composition. Outcomes
  feed back to Spin Chamber operating parameters
  and SC-002 segregation effectiveness evaluation.
- Method qualification — every use of a method
  produces data on its capability, failure modes,
  and appropriate applications.
- Network contribution — fabrication logs,
  method outcomes, and wire quality data
  contributed to Architecture/Forge_Net.md
  reference database. One forge's fabrication
  experience becomes every forge's knowledge.

**Fabrication record minimum content:**
- Part identifier and description
- Material source — which gate output, which
  forge instance
- Method used
- Wire feedstock source and qualification status
- Dimensional outcome — target vs. achieved
- Precision ceiling applied
- Weld quality assessment if applicable
- Operator identifier
- Outcome — passed, failed, reworked

*A fabrication record that documents a failure
is more valuable than one that documents a
success without detail. Failures teach. Successes
without records teach nothing.*

---

## 9. Integration Hooks

- `Architecture/Forge_flow.md` — governing flow;
  Fabrication is the constructive outcome path
- `Operations/Gate_04_Separation_Mechanical.md`
  — upstream material source; mechanical
  separation output feeds fabrication stock
- `Operations/Gate_05_Separation_Thermal.md`
  — upstream material source and wire extrusion
  path; SC-004 wire feeds arc welding directly
- `Operations/Air_Scrubber.md` — welding fume
  capture and ventilation; required operational
  during arc welding
- `Operations/Energy.md` — fabrication energy
  not yet characterized; welding power draw
  feeds energy accounting
- `Architecture/Components.md` — Metrology
  and Baseline Observability items; precision
  ceiling references component taxonomy
- `Architecture/Forge_Net.md` — fabrication
  logs and method outcomes contributed to
  network reference database
- `Admin/Trajectories.md` — deferred methods
  (powder welding, laser welding, casting,
  pressing) routed here for version targeting
- `Admin/Ship_of_Theseus.md` — fabricated
  parts that enter service begin their own
  grain provenance record
- `Unknowns.md` — GF-001 through GF-005
  indexed once logged

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| 2026-05-15 | Audit Review | Fabrication conceived as terminal endpoint — material goes in, parts come out, process ends | Fabrication without a feedback loop produces parts but no learning. Classification rules, precision ceiling, wire quality, and method capability all improve through fabrication data | Fabrication is a data-generating stage, not just a production stage. Every outcome — success or failure — feeds back to upstream gates, network knowledge, and precision ceiling tracking. A fabrication record that documents a failure is more valuable than one that documents a success without detail | Analogous | No — feedback loop doctrine is correct |
| 2026-05-15 | Audit Review | Wire production assumed to close self-replication loop automatically once SC-004 is validated | Wire quality from variable-alloy Spin Chamber output may not be sufficient for all arc welding applications. External wire sourcing at bootstrap is a valid and expected path | Purchase-what-cannot-be-produced doctrine applies to welding wire at bootstrap. Internal wire production is the goal, not the prerequisite. Arc welding with externally sourced wire still validates the fabrication capability even if wire is not yet internally produced | Analogous | Yes — validate internal wire quality against arc welding requirements once SC-004 is operational |
| 2026-05-15 | Audit Review | Precision ceiling treated as fixed background condition — assumed known without active tracking | An untracked precision ceiling produces parts that appear correct but fail in service when actual ceiling is lower than assumed. Silent failure from overconfident tolerance claims is worse than acknowledged limitation | Precision ceiling is a first-class tracked metric, not a background assumption. It cannot exceed metrology capability. It must be documented honestly in fabrication records. Purchasing precision instruments at bootstrap is correct doctrine — precision is seeded deliberately, not bootstrapped from nothing | Analogous | Yes — establish actual v0 precision ceiling during first operational fabrication cycle |
| 2026-05-15 | Audit Review | Add-to-excess framed as workaround for imprecise forming | Add-to-excess is not a workaround — it is the correct philosophy for a system working with variable feedstock and inherently imprecise forming methods | The weld gets close. The mill finds the truth. This is not a limitation to overcome — it is the correct approach for v0 capability levels. The philosophy should be stated as doctrine, not as a compromise | Analogous | No — add-to-excess and mill-to-spec is permanent v0 doctrine |
| 2026-05-15 | Audit Review | Arc welding operator safety treated as assumed knowledge | UV radiation causes permanent eye damage in seconds without proper shielding. Fumes from unknown alloy base metal cause metal fume fever. These hazards are not obvious to operators without prior welding experience | Arc welding PPE is a non-negotiable prerequisite before first operation. Helmet shade, gloves, flame-resistant clothing, and ventilation must be confirmed available and fitted before the first arc is struck. Operator training on hazards precedes operator training on technique | Analogous | Yes — validate PPE availability and operator hazard training before first arc welding operation |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| DS-001 | Whether internally produced wire from Spin Chamber output is sufficient for v0 arc welding without external sourcing at bootstrap | Position A: Internal wire production from SC-004 is the goal and should be validated before arc welding qualification begins — using external wire delays the self-replication proof of concept. Position B: External wire sourcing at bootstrap is correct doctrine per purchase-what-cannot-be-produced — arc welding qualification should not wait on SC-004 validation, which is itself unvalidated | Low | Open | Operations/Gate_06_Fabrication.md |

*DS-001 is a sequencing dispute, not a technical one.
Both positions agree that internal wire production is
the goal. The disagreement is whether arc welding
qualification should wait for internal wire or proceed
with external wire. Position B is the current standing
doctrine — purchase-what-cannot-be-produced applies,
and delaying arc welding qualification to wait for
SC-004 validation unnecessarily gates two unresolved
unknowns on each other. Revisit when SC-004 produces
first wire samples and quality can be assessed against
arc welding requirements.*

---

## Auditor Notes & Unknowns

### GF-001 — Welding wire diameter specification
not defined

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Wire diameter specification for v0
arc welding has not been defined. Wire diameter
determines amperage range, deposition rate, and
suitable base metal thickness. SC-004 draw speed
controls diameter — without a target diameter,
draw speed cannot be set.

**Why It Matters:** Wire diameter is the primary
parameter connecting SC-004 wire extrusion to arc
welding process selection. An undefined diameter
means the extrusion path cannot be configured and
welding process parameters cannot be established.

**Resolution Path:**
- Select v0 arc welding process — MMA stick welding
  requires no wire; MIG/GMAW requires wire feed.
  If MIG is selected, wire diameter must be
  specified before SC-004 draw speed can be set.
- Common v0 MIG wire diameters for steel:
  0.6mm, 0.8mm, 0.9mm, 1.0mm *(Analogous)*
- Common v0 MIG wire diameters for aluminum:
  0.8mm, 1.0mm, 1.2mm *(Analogous)*
- Select diameter based on available welding
  equipment wire feed capability and target
  base metal thickness range.
- Cross-reference: SC-004 in
  Operations/Gate_05_Separation_Thermal.md,
  UNK-008.
- Payment via Specification — once welding
  process and wire diameter are selected, move
  to Section 7 as Analogous.

---

### GF-002 — Precision ceiling not characterized
at v0 bootstrap

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The actual precision ceiling —
tightest tolerance achievable and verifiable at
v0 bootstrap — has not been characterized. Section
5 provides Analogous estimates but these are not
measured values.

**Why It Matters:** An uncharacterized precision
ceiling produces overconfident fabrication claims.
Parts made to an assumed tolerance that hasn't
been verified may fail in service silently.

**Resolution Path:**
- Establish metrology baseline — confirm available
  measurement tools and their resolution.
  Commercial caliper is the minimum v0 instrument.
- Produce test pieces using each available removal
  method — angle grinder, file, lathe if available.
- Measure achieved dimensions against targets
  across multiple attempts.
- Document actual achievable tolerance range per
  method — this becomes the characterized ceiling.
- Update Section 5 from Analogous estimates to
  Measured values.
- Cross-reference: Architecture/Components.md
  Metrology item, ASM-004.
- Payment via Specification — once ceiling is
  characterized through test pieces, move to
  Section 5 as Measured.

---

### GF-003 — Material removal hardware not specified

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Specific material removal equipment
for the mill-to-spec step has not been specified
for v0 bootstrap.

**Why It Matters:** Material removal capability
determines the precision ceiling. The add-to-excess
and mill-to-spec philosophy depends on removal
capability being available before fabrication begins.

**Resolution Path:**
- Minimum v0 removal capability: angle grinder
  and hand files. Purchasable at bootstrap.
  *(Analogous)*
- Preferred v0 removal capability: bench grinder
  plus angle grinder plus file set.
- Precision v0 removal capability: manual lathe
  if available. Purchase per purchase-what-cannot-
  be-produced doctrine if budget allows.
- Standardized consumables selected from common
  stock for inter-forge parts sharing.
- Payment via Specification — once removal
  equipment is confirmed at bootstrap, move to
  Section 4 as Analogous.
- Cross-reference: GF-002, ASM-003.

---

### GF-004 — Fabrication energy consumption not
characterized

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical                                        |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** Energy consumption of arc welding
and material removal operations has not been
characterized or cross-referenced to
Operations/Energy.md power budget.

**Why It Matters:** Arc welding draws significant
peak power — a basic MMA welder draws 2–5kW at
operating current. If fabrication competes with
Spin Chamber operation for available power,
scheduling conflicts arise.

**Resolution Path:**
- Characterize welding power draw for selected
  welding process and typical operating current.
  *(Analogous — commercial welder specifications)*
- Characterize material removal power draw —
  angle grinder 1–2kW, lathe 1–3kW typical.
  *(Analogous)*
- Cross-reference Operations/Energy.md bootstrap
  power budget — can fabrication and Spin Chamber
  operate simultaneously or must they be sequenced?
- Payment via Specification — once power draw
  is characterized and cross-referenced to
  Energy.md, move to Section 9 as Analogous.
- Cross-reference: Operations/Energy.md.

---

### GF-005 — Utilization stage has no owning file

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Architectural                                    |
| Blocking      | No                                               |
| Owner         | Operations/Gate_06_Fabrication.md                |
| First Logged  | 2026-05-15                                       |
| Last Reviewed | 2026-05-15                                       |

**Description:** The Utilization stage — where
fabricated parts enter service and real-world
performance is validated — has no owning
specification file in the repository.

**Why It Matters:** Fabrication produces candidates
for use. Utilization determines whether they are
fit for purpose. Without a Utilization specification,
performance feedback has no governance and the
learning loop that improves fabrication quality
over time has no closing mechanism.

**Resolution Path:**
- Create Gate_07_Utilization.md — minimum content:
  performance metrics captured, failure mode
  logging, maintenance frequency tracking, and
  feedback path to Gate_06 fabrication records
  and Architecture/Forge_Net.md.
- At v0, Utilization may be as simple as a
  logging discipline — record what was made,
  how it performed, and what failed.
- The feedback loop in Section 8 assumes
  Utilization data exists — GF-005 is the
  prerequisite for that assumption to be grounded.
- Recommend creating Gate_07_Utilization.md
  as the next file after Gate_06 is loaded.
- Cross-reference: Architecture/Forge_flow.md
  Section 6 Utilization.

---

### Resolution Log

*(empty — no entries resolved yet)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-05-15 | Fabrication as terminal endpoint — material goes in, parts come out, process ends | Fabrication without a feedback loop produces parts but no learning. Classification rules, precision ceiling, wire quality, and method capability all improve through fabrication data. A terminal fabrication stage breaks the learning loop that the entire system depends on | No — feedback loop doctrine is permanent |
| 2026-05-15 | Waiting for internal wire production to be validated before beginning arc welding qualification | Gates two unresolved unknowns on each other — SC-004 and arc welding qualification are both unvalidated. Delaying arc welding qualification until SC-004 produces qualified wire means neither advances. External wire sourcing at bootstrap per purchase-what-cannot-be-produced doctrine allows arc welding to qualify independently | Reconsider if SC-004 produces wire samples before arc welding equipment is sourced — opportunistic parallel validation is valid if both happen to be available simultaneously. See DS-001 |
| 2026-05-15 | Single precision ceiling for all fabrication methods | Different methods have different ceilings — an angle grinder and a lathe operate at fundamentally different precision levels. A single ceiling overclaims what rough tools can achieve or underclaims what precision tools can achieve | No — method-specific precision ceiling tracking is correct |
| 2026-05-15 | Achieving dimensional accuracy through forming precision alone | Variable feedstock and inherent forming imprecision make first-pass dimensional accuracy unreliable. Attempting to hit spec on the forming step produces parts that are sometimes correct and sometimes not, with no consistent path to correction | No — add-to-excess and mill-to-spec is permanent doctrine |
| 2026-05-15 | Introducing fabrication methods informally before qualification | Informal method adoption means unknown capability, unknown failure modes, and unknown safety requirements operating on real parts. An unqualified method that produces a structural failure on a critical component sets back the entire fabrication program | No — formal method introduction is permanent doctrine |
| 2026-05-15 | Treating PPE as optional or operator-discretionary for arc welding | Arc eye from UV exposure occurs in seconds. The damage is permanent and not immediately painful — operators do not realize they have been injured until hours later. Making PPE discretionary means relying on operators to self-protect against a hazard that gives no immediate warning signal | No — PPE as prerequisite is permanent doctrine |
| 2026-05-15 | Powder welding and laser welding as v0 fabrication methods | Both require upstream capabilities that do not exist at v0 — powder feedstock production, precision laser sources, controlled atmosphere. Introducing them before arc welding is qualified adds complexity without the baseline capability that justifies the complexity | Reconsider powder welding at v1+ when powder feedstock production is demonstrated. Reconsider laser welding at v2+ when precision energy delivery is validated. Route both to Admin/Trajectories.md |

---

## Drift Indicators

The following conditions trigger mandatory re-audit of
this file. All canonical drift indicators from
Admin/File_Template.md apply. The following are
additional local triggers specific to Gate_06_Fabrication:

### Local Drift Triggers

| Trigger | Reason |
|---------|--------|
| Arc welding operation begins without PPE confirmed available and fitted | PPE is a non-negotiable prerequisite — arc eye from UV exposure is permanent and gives no immediate warning. No exceptions. |
| Arc welding qualification bypassed to begin fabricating functional parts | Qualification on scrap before functional parts is permanent doctrine — an unqualified weld on a structural component has unknown failure mode |
| Precision ceiling claimed without GF-002 characterization completed | Uncharacterized ceiling produces overconfident fabrication claims — parts made to assumed tolerance may fail in service silently |
| Fabrication records not kept for operational runs | Fabrication without records breaks the feedback loop — precision ceiling, wire quality, and method capability cannot improve without outcome data |
| New fabrication method introduced without qualification framework completion | Informal method adoption is a permanently abandoned path — unknown capability and unknown failure modes operating on real parts |
| Wire feedstock used for structural arc welding without qualification status confirmed | Unqualified wire of unknown alloy composition may produce brittle, porous, or cracked welds — wire qualification status must be known before structural use |
| Add-to-excess philosophy abandoned in favor of first-pass dimensional accuracy | Permanently correct doctrine for v0 capability levels — abandonment requires demonstrated forming precision that makes excess unnecessary, supported by GF-002 data |
| DS-001 resolved without SC-004 wire quality assessment | Wire sequencing dispute resolution must include actual wire quality data — resolving DS-001 by assumption rather than evidence reopens the unknown |
| Powder or laser welding introduced before arc welding qualification is complete | Arc welding is the gatekeeper — higher methods require the baseline to be established first. Abandoned path with version-specific reconsider conditions |
| Utilization feedback loop broken — fabricated parts enter service without performance logging | Section 8 feedback doctrine requires Utilization data — if parts enter service without logging, the learning loop closes and precision ceiling cannot improve. GF-005 prerequisite |
| PPE requirements reduced for welding on known clean base metal | Arc flash UV hazard exists regardless of base metal composition — PPE reduction based on material class is not valid. Helmet shade and gloves are always required |

### Canonical Drift Triggers

*All mandatory re-audit conditions from Admin/File_Template.md
Section 10 apply without exception. Local triggers above are
additive, not substitutes.*

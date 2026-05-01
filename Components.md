# Lazarus Forge — Components Taxonomy
**Version 0.3**

---

## Purpose

Define what a Forge must have to operate safely and truthfully (Critical), versus what amplifies capability, efficiency, or autonomy (Useful).

This document supports v0–v5 navigation, procurement planning, and honest self-assessment.

---

## Framing

Metal fabrication is the first milestone because it is the only self-sustaining path to structural capability. Once a Forge can produce reliable metal components from salvaged feedstock, every other physical system becomes constructable — the Support Raft hull, the Material Separation Gate rotor, the Leviathan chassis, the GECK seed structural components. None of them exist without this capability coming first.

This document defines the minimum viable component set required to achieve that capability. It is not a complete description of the Forge ecosystem. It describes the enabling layer upon which all downstream systems depend. The scope is intentional, not incomplete.

---

## Definitions

**Critical Components**
Absence prevents safe operation, learning, or truthful output.
Without these, the system is not a Lazarus Forge.

**Useful Components**
Increase throughput, resilience, autonomy, or scope.
Absence does not invalidate the Forge, only limits it.

---

## Bootstrap Doctrine

### Purpose

The Bootstrap Doctrine defines how a Lazarus Forge may begin operation **before** ideal components, refined materials, or industrial precision are available.

It formalizes imperfect beginnings as a valid and expected state.

---

### Core Principle

> A component is sufficient if it allows the Forge loop to close.
> A component is critical if its absence permits silent failure.

Perfection is not required. **Closure is.**

---

### Tier −1: Bootstrap / Seed Components

Bootstrap components are not optimized, durable, or efficient.
They exist solely to **enable the first self-improving loop**.

Typical sources include:
- Salvaged tools and appliances
- Discarded electronics
- Improvised mechanical assemblies
- Manually operated systems

Common examples:
- High-torque DC motors or steppers (printers, tools)
- Bearings, gears, rails, and fasteners from scrap
- Repurposed power supplies, UPS units, or battery packs
- Microcontrollers or single-board computers
- Basic sensors (temperature, current, limit switches)

These components are **expected to fail** and **expected to be replaced**.

Failure is not a defect — **silence is**.

---

### Proxy Components & Downgrade Paths

For every ideal component listed in this document, a Forge may begin with:

- Lower-precision analogs
- Manual or semi-manual processes
- Open-loop control where closed-loop is unavailable
- Human-in-the-loop verification

Examples:
- Laser metal deposition → MIG/TIG wire deposition
- Inert gas chamber → sealed glove-box or purge bag
- Automated handling → manual fixtures with jigs
- Inline metrology → destructive testing and observation

Each proxy exists to be **measured, understood, and replaced**, not immortalized.

---

### Graduation Rule

A component graduates from bootstrap status when the Forge can:

1. Detect its degradation or failure
2. Repair or replace it using internal capabilities
3. Improve its successor based on logged performance

Once graduated, it becomes a normal Critical or Useful component.

---

### Energy Awareness (Minimal v0 Rule)

At bootstrap stage:
- Exact efficiency is not required
- **Energy visibility is**

If energy draw cannot be observed or estimated, the Forge does not yet understand the component.

---

### Relationship to GECK

The GECK defines the **minimum viable seed** required to initiate this doctrine.

Components listed here represent:
- One possible implementation path
- Not a mandate
- Not an assumption of industrial access

Over time, GECK becomes primary; this document becomes reference.

---

## I. Critical Components (Non-Negotiable)

### 1. Material Intake & Reduction
- Scrap reduction tools (cutting, crushing, shredding)
- Powderization method (mill / atomization / equivalent)
- Particle size classification (sieves or classifiers)
- Inert handling capability (argon or nitrogen)

**Why critical:** Without controlled feedstock, artifacts inherit unknown failure.
**Dual-Use: Low** — Reduction tools are broadly industrial; no specific weapons application.

---

### 2. Atmosphere Control
- Controlled build chamber (O₂ monitoring)
- Inert gas supply and purge capability
- Sealed powder handling containers

**Why critical:** Oxidation is silent corruption, especially for steel and titanium.
**Dual-Use: Low** — Atmosphere control is process-specific and protective in nature.

---

### 3. Metal Additive Manufacturing Core
- Metal AM system with open parameter access
- Stable laser / energy source
- Repeatable motion system

**Why critical:** Closed systems block learning and invalidate lineage.
**Dual-Use: Medium** — High-energy directed systems and precision motion have broader application potential. Open parameter access increases this risk slightly — log any capability expansion against `Ethical_Constraints.md` dual-use indicators.

---

### 4. Thermal Processing
- Heat treatment furnace (material-appropriate range)
- Controlled cooldown / quench capability
- Thermal logging (thermocouples + record)

**Why critical:** Printed ≠ finished. Thermal history is part of the artifact.
**Dual-Use: Low** — Thermal processing is standard industrial practice with no specific weapons application at this scale.

---

### 5. Metrology & Verification
- Dimensional measurement (scanner + hand tools)
- Mass measurement (precision scale)
- Surface inspection (optical microscopy)
- Basic mechanical verification (hardness or proxy)

**Why critical:** Discernment depends on detecting almost right.
**Dual-Use: Low** — Measurement and verification capability is broadly applicable but not specifically enabling for harmful use.

---

### 6. Artifact Memory & Data Spine

- Local compute capable of long-term storage
- Artifact ID system (physical ↔ digital binding)
- Versioned parameter records
- Failure retention (never auto-delete)

**Why critical:** Without memory, resurrection collapses into repetition.
**Dual-Use: Medium** — Artifact tracking and versioned records could be adapted for surveillance or targeting systems. Ensure data spine is scoped to Forge artifacts only and does not accumulate personal or location data about individuals.

---

### 7. Human Override & Discernment Interface
- Manual abort and override controls
- Parameter bounds with operator authority
- Failure annotation capability

**Why critical:** Early discernment is human-taught, not inferred.
**Dual-Use: Low** — Override interfaces reduce autonomous capability; this is the opposite of weaponization risk.

---

## II. Useful Components (Capability Multipliers)

### A. Automation & Handling
- Robotic arms or gantries
- Interchangeable end-effectors
- Automated powder recycling loops

**Value:** Consistency, reduced exposure, extended runtimes.
**Dual-Use: Medium** — Robotic manipulation systems are broadly applicable. Flag any end-effector designs that increase kinetic or precision delivery capability against `Ethical_Constraints.md` dual-use indicators.

---

### B. Advanced Sensing
- Melt-pool monitoring
- Acoustic or vibration sensing
- In-process optical inspection

**Value:** Early anomaly detection and richer learning signals.
**Dual-Use: Low** — Process-specific sensing with limited transferability to harmful applications.

---

### C. Material Characterization
- XRF / LIBS access (in-house or partner)
- Particle morphology analysis
- Contamination detection

**Value:** Faster material progression and safer alloy exploration.
**Dual-Use: Low** — Characterization capability is analytical and broadly scientific.

---

### D. Energy Infrastructure
- Energy storage (UPS / batteries)
- Waste-heat recovery
- Power quality conditioning

**Value:** Process stability and off-grid potential.
**Dual-Use: Low** — Energy storage and conditioning are general infrastructure with no specific weapons application.

---

### E. Network & Collaboration Layer
- Secure data sharing between Forges
- Anonymized failure signature exchange
- Reputation and capability signaling

**Value:** Distributed learning without centralization.
**Dual-Use: Medium** — Networked capability signaling could be adapted for coordination of harmful activities. Ensure network layer is scoped to Forge-to-Forge learning exchange and does not enable command-and-control of external systems.

---

### F. Environmental Hardening (v2+)
- Vacuum-tolerant components
- Radiation-tolerant electronics
- Extreme thermal cycling design

**Value:** Enables remote, orbital, and lunar deployment.
**Dual-Use: Medium** — Hardened autonomous systems operating in remote environments have obvious dual-use potential. Environmental hardening capability expansion should be reviewed against `Ethical_Constraints.md` before deployment in contested or sensitive zones.

---

## III. Gateway to Downstream Capability Classes

The metal fabrication core unlocks the ability to construct systems requiring:

- Structural load-bearing assemblies
- Rotational and fluid-handling machinery
- Pressure-resistant enclosures
- Modular frames and chassis systems
- Mechanically coupled multi-component assemblies
- Marine and subsurface structural components
- Orbital and vacuum-rated hardware

These represent capability classes, not specific implementations. This document does not define those systems. It defines the minimum viable substrate that makes them physically realizable.

Downstream systems currently specified elsewhere:

| System | File | Dependency on Metal Core |
|---|---|---|
| Material Separation Gate | `Material_Separation_Gate_v0.md` | Rotor, drum, bearing assemblies |
| Spin Chamber | `Spin_Chamber_v0.md` | Induction coil housing, MHD chamber |
| Air Scrubber | `Air_Scrubber_v0.md` | Stage housings, wet column vessel |
| Support Raft | `Support_Raft_v0.md` | SWATH hull structure, struts, docking ports |
| Leviathan Units | `leviathan_testing.md` | Chassis, pressure housings, manipulator arms |
| GECK Seed | `geck_forge_seed.md` | All structural seed components |

This table is illustrative and will grow. It introduces no requirements into this document.

---

## IV. Version Mapping

| Version | Milestone |
|---|---|
| v0 | Sections I.1–I.7 minimally satisfied (single material) |
| v1 | Steel-class materials + closed-loop recycling |
| v2 | Multi-material + unattended operation + networking |
| v3 | In-situ resource processing + off-world operation |
| v4 | Off-world deployment — fabrication in non-terrestrial environment |
| v5 | Interstellar propagation — self-replicating seed capability |

Full trajectory rationale in `Trajectories_LF.md`.

---

## V. Operating Principle

> A component is critical if its absence allows silent failure.

Everything else is useful.

---

## VI. Dual-Use Annotation Standard

All components carry a dual-use annotation:

**Dual-Use: [Low | Medium | High]**
**Rationale:** brief justification

**Purpose:**
- Surface ambiguity without restricting development
- Enable downstream ethical review per `Ethical_Constraints.md`
- Maintain awareness of capability transfer risk

**Escalation:**
- Low — no action required; standard logging
- Medium — flag any capability expansion against `Ethical_Constraints.md` dual-use indicators before deployment
- High — route to Full Stop Review before proceeding

Absence of a flag does not imply absence of risk. No current component in this document is rated High — that rating would trigger immediate review before the component was included.

---

## VII. Notes for Builders

- Start with fewer materials, not fewer measurements
- Preserve failures aggressively
- Sell artifacts, not promises
- Promote honestly by capability age, not hype
- The gateway is metal — everything else follows from it

---

*This document is intended to evolve. Amend only with demonstrated capability.*

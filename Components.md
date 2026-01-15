Lazarus Forge — Components Taxonomy

> Purpose: Define what a Forge must have to operate safely and truthfully (Critical), versus what amplifies capability, efficiency, or autonomy (Useful).

This document supports v0–v3 navigation, procurement planning, and honest self‑assessment.




---

Definitions

Critical Components

Absence prevents safe operation, learning, or truthful output.

Without these, the system is not a Lazarus Forge.


Useful Components

Increase throughput, resilience, autonomy, or scope.

Absence does not invalidate the Forge, only limits it.



## Bootstrap Doctrine

### Purpose

The Bootstrap Doctrine defines how a Lazarus Forge may begin operation **before** ideal components, refined materials, or industrial precision are available.

It formalizes imperfect beginnings as a valid and expected state.

---

### Core Principle

> **A component is sufficient if it allows the Forge loop to close.  
> A component is critical if its absence permits silent failure.**

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

For every “ideal” component listed in this document, a Forge may begin with:

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

Once graduated, it becomes a normal *Critical* or *Useful* component.

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

I. Critical Components (Non‑Negotiable)

1. Material Intake & Reduction

Scrap reduction tools (cutting, crushing, shredding)

Powderization method (mill / atomization / equivalent)

Particle size classification (sieves or classifiers)

Inert handling capability (argon or nitrogen)


Why critical: Without controlled feedstock, artifacts inherit unknown failure.


---

2. Atmosphere Control

Controlled build chamber (O₂ monitoring)

Inert gas supply and purge capability

Sealed powder handling containers


Why critical: Oxidation is silent corruption, especially for steel and titanium.


---

3. Metal Additive Manufacturing Core

Metal AM system with open parameter access

Stable laser / energy source

Repeatable motion system


Why critical: Closed systems block learning and invalidate lineage.


---

4. Thermal Processing

Heat treatment furnace (material‑appropriate range)

Controlled cooldown / quench capability

Thermal logging (thermocouples + record)


Why critical: Printed ≠ finished. Thermal history is part of the artifact.


---

5. Metrology & Verification

Dimensional measurement (scanner + hand tools)

Mass measurement (precision scale)

Surface inspection (optical microscopy)

Basic mechanical verification (hardness or proxy)


Why critical: Discernment depends on detecting almost right.


---

6. Artifact Memory & Data Spine

Local compute capable of long‑term storage

Artifact ID system (physical ↔ digital binding)

Versioned parameter records

Failure retention (never auto‑delete)


Why critical: Without memory, resurrection collapses into repetition.


---

7. Human Override & Discernment Interface

Manual abort and override controls

Parameter bounds with operator authority

Failure annotation capability


Why critical: Early discernment is human‑taught, not inferred.


---

II. Useful Components (Capability Multipliers)

A. Automation & Handling

Robotic arms or gantries

Interchangeable end‑effectors

Automated powder recycling loops


Value: Consistency, reduced exposure, extended runtimes.


---

B. Advanced Sensing

Melt‑pool monitoring

Acoustic or vibration sensing

In‑process optical inspection


Value: Early anomaly detection and richer learning signals.


---

C. Material Characterization

XRF / LIBS access (in‑house or partner)

Particle morphology analysis

Contamination detection


Value: Faster material progression and safer alloy exploration.


---

D. Energy Infrastructure

Energy storage (UPS / batteries)

Waste‑heat recovery

Power quality conditioning


Value: Process stability and off‑grid potential.


---

E. Network & Collaboration Layer

Secure data sharing between Forges

Anonymized failure signature exchange

Reputation and capability signaling


Value: Distributed learning without centralization.


---

F. Environmental Hardening (v2+)

Vacuum‑tolerant components

Radiation‑tolerant electronics

Extreme thermal cycling design


Value: Enables remote, orbital, and lunar deployment.


---

III. Version Mapping (Quick Reference)

v0: Sections I.1–I.7 minimally satisfied (single material)

v1: Steel‑class materials + closed‑loop recycling

v2: Multi‑material + unattended operation + networking

v3: In‑situ resource processing + off‑world operation



---

IV. Operating Principle

> A component is critical if its absence allows silent failure.



Everything else is useful.


---

V. Notes for Builders

Start with fewer materials, not fewer measurements

Preserve failures aggressively

Sell artifacts, not promises

Promote honestly by capability age, not hype



---

This document is intended to evolve. Amend only with demonstrated capability.

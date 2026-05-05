# Lazarus Forge — Spin Chamber (v0)

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 4 (Medium)
- Sidecar: [#auditor-notes--unknowns]

> **Design doctrine:** slow, steady, methodical work beats speed. The Spin Chamber favors time, stability, and survivability over peak throughput.

---

## 1. Purpose

The Spin Chamber is the keystone module of Lazarus Forge. It converts mixed metallic scrap into **ranked material streams** using overlapping physical biases (heat, rotation, and electromagnetic fields). The goal is *progressive enrichment* and *capability replication*, not single-pass purity.

This v0 design prioritizes:

- Long operational life
- Predictable behavior
- Modular repair
- Bootstrap compatibility (built from salvage, improves itself over generations)

---

## 2. Operating Principle

1. **Induction melting** homogenizes incoming scrap
2. **Slow rotation** biases the melt radially by density
3. **Magnetohydrodynamic (MHD) damping** stabilizes flow and suppresses turbulence
4. **Time under bias** allows impurities to migrate and segregate
5. **Selective extraction** (tapping / extrusion) routes material by role

The chamber does not aim to produce "pure metal." It produces **useful gradients**.

---

## 3. System Overview

**Stationary outer shell**
- Structural containment
- Thermal insulation
- Houses coils and sensors

**Rotating inner crucible**
- Contains molten metal
- Provides centrifugal bias

**External induction coils**
- Heat source
- Optional MHD field shaping

**Drive module**
- Low RPM rotation
- High tolerance to imbalance

**Extraction interfaces**
- Slag skim
- Radial taps (optional)
- Centerline wire extrusion (future-ready)

---

## 4. Scale & Geometry (v0 Envelope)

- **Internal diameter:** 200–250 mm *(Analogous — derived from small induction furnace commercial offerings)*
- **Internal height:** 200–300 mm *(Analogous)*
- **Melt volume:** 5–10 L *(Analogous)*
- **Batch mass:** ~10–25 kg Al class *(Analogous)*

**Crucible geometry:**
- Rounded conical or shallow paraboloid bottom
- No flat surfaces
- Generous radii to avoid dead zones

**Wall thickness:**
- Graphite: 10–15 mm *(Analogous)*
- Ceramic: 15–25 mm *(Analogous)*

---

## 5. Materials

**Crucible (v0):**
- Graphite (preferred; sacrificial, forgiving)
- Alumina / mullite ceramics (acceptable)

**Outer shell:**
- Refractory liner
- Insulation layer
- Structural steel jacket

**Design note:** Wear is acceptable. Sudden failure is not.

---

## 6. Rotation System

- **Operating RPM:** 50–300 *(Placeholder — bounds derived from first principles, not tested)*
- **Nominal RPM:** 100–150 *(Placeholder)*
- **Never exceed (v0):** 400 *(Placeholder — safety margin not yet validated)*

**Drive philosophy:**
- External motor
- Belt or chain drive
- Slip or clutch preferred
- Alignment by geometry, not precision machining

---

## 7. Heating & Thermal Strategy

**Heating:**
- External induction coils
- Single zone acceptable for v0
- Power range: 5–15 kW *(Analogous — small induction furnace data)*

**Temperature bands (Al class):**
- Hot idle: 500–550 °C *(Analogous)*
- Processing: 650–720 °C *(Analogous)*

**Thermal doctrine:**
- Maintain near-constant elevated temperature
- Avoid full thermal cycling
- Stop rotation before cooling

This dramatically extends crucible and coil life.

---

## 8. Electromagnetic Fields (v0)

- No electrodes in melt
- No electrochemical assumptions
- Induction fields provide heating and incidental MHD effects
- Optional auxiliary coils for millitesla-scale flow damping

Purpose is **stability**, not forceful separation.

---

## 9. Atmosphere Control

- Passive reducing environment preferred
- Charcoal bed or inert purge if available
- Oxygen ingress minimized, not eliminated

Precision gas chemistry is out of scope for v0.

---

## 10. Extraction & Outputs

**Primary outputs:**
- Slag / oxide layer (skimmed)
- Bulk structural alloy
- Composition-biased inner fraction

**Wire extrusion (planned path):**
- Centerline bottom tap
- Heated, replaceable nozzle
- Diameter controlled by draw speed

Wire is the preferred first product for self-replication.

---

## 11. Instrumentation & Control

**Required sensing:**
- Temperature (2–3 points)
- Motor current
- Induction power draw
- Vibration (coarse accelerometer acceptable)

**Control philosophy:**
- Thresholds and states
- Slow ramps
- Long dwell times

Example rule:
> If vibration increases for 10 minutes, reduce RPM.

---

## 12. Operating Mode

- Batch operation
- Long holds (hours, not minutes)
- Hot idle between runs

Speed is never a success metric.

---

## 13. Expected Outcomes (v0)

**Expect:**
- Predictable segregation trends
- Improved consistency over time
- Learnable wear patterns

**Do not expect:**
- High purity
- High throughput
- Cosmetic perfection

If behavior is stable and repeatable, the chamber is successful.

---

## 14. Failure Philosophy

Acceptable:
- Crucible wear
- Slag buildup
- Gradual vibration drift

Unacceptable:
- Runaway RPM
- Melt breach
- Explosive failure

Design to fail **slowly and visibly**.

---

## 15. Role in Self-Replicating Foundry Logic

The Spin Chamber is a **material router**. Its outputs feed:
- Structural fabrication
- Coil and motor upgrades
- Thermal and refractory improvements

Each generation improves the next. Older chambers remain useful.

---

## 16. Summary

The Spin Chamber is not a purifier. It is a patient system that nudges matter toward order using time, gravity, and fields.

> **Slow spin. Hot idle. Long life.**

This is the tortoise.

---

## Lessons Learned

Operational wisdom from building, testing, and running the Spin Chamber.

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| — | — | — | No operational entries yet — design is pre-build |

*This section will grow with Gen-0 operational data. The most valuable entries will be about what the useful gradients actually look like vs. what was predicted, and what RPM/temperature combinations produced stable vs. unstable behavior.*

---

## Auditor Notes & Unknowns

### SC-001 — RPM envelope not validated
**Status:** Open
**Risk:** Medium
**What is not yet known:** Whether the 50–400 RPM operating range is safe and effective for the specified geometry and melt mass. The never-exceed of 400 RPM carries no safety analysis.
**Resolution path:** Back-of-envelope centrifugal force calculation for worst-case melt mass at 400 RPM against crucible wall tensile strength. Label as Estimated once calculated. Physical test with cold water analog before first hot run.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor

### SC-002 — Segregation effectiveness at v0 scale unverified
**Status:** Open
**Risk:** Medium
**What is not yet known:** Whether meaningful density-based segregation is achievable at 5–10L melt volume and 100–150 RPM. The operating principle is physically sound at larger scales — the v0 scale analog data is absent.
**Resolution path:** Literature search for small-scale centrifugal casting and rotary furnace data at similar volumes. If no analog exists, flag as Placeholder until first operational run. This is the most important validation for the chamber's core claim.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor

### SC-003 — MHD damping effectiveness at auxiliary coil power levels unverified
**Status:** Open
**Risk:** Low
**What is not yet known:** Whether millitesla-scale auxiliary fields provide meaningful flow damping vs. negligible effect at v0 scale and power budget.
**Resolution path:** This is Exploratory — MHD damping is described as optional. If it adds no measurable benefit at v0 scale, remove from spec and route to Trajectories_LF.md for higher-power future versions. Label as Placeholder until tested.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor

### SC-004 — Wire extrusion nozzle design not specified
**Status:** Open
**Risk:** Low
**What is not yet known:** Nozzle material, geometry, replacement interval, and draw speed control method for the centerline wire extrusion path.
**Resolution path:** Wire extrusion is marked "future-ready" — this is correctly deferred. Log as Exploratory, route to Trajectories_LF.md v1 scope. Nozzle design is a specification task for the version where wire becomes a primary output.
**Logged:** 2026-05-04, Claude — Skeptic/Auditor

### Resolution Log
*(empty — no entries resolved yet)*

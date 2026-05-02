# Energy Systems v0 — Powering the Lazarus Forge

## Purpose

The Lazarus Forge is an energy-intensive system.
This document defines **plausible, incremental energy strategies**
that allow the Forge to operate, learn, and reduce net energy cost over time.

Energy independence is not assumed at v0.

---

## Design Philosophy

- Energy demand is acknowledged, not hidden
- Early stages prioritize learning over efficiency
- Salvage-first applies to power systems as well
- Multiple small contributors are preferred over single large sources
- Net energy trajectory matters more than initial balance

---

## Energy Lifecycle

1. External energy enables early operation
2. Salvaged systems begin contributing power
3. Waste streams produce partial energy
4. Overall energy cost per recovered unit decreases

---

## Energy Sources (v0 Scope)

*Note: Conversion losses are uncharacterized for all sources below at v0. Each source description reflects intended role, not verified output. All contribution estimates are Placeholder pending characterization.*

---

### 1. Grid Power (Bootstrap)

- Primary early-stage energy source
- Enables reduction, stratification, and control systems
- Treated as temporary dependency

---

### 2. Salvaged Motor-Generators

**Description:**
- Recovered motors repurposed as generators
- Back-driven via turbines, belts, or engines
- Electromechanical conversion efficiency: uncharacterized at v0 (Placeholder)

**Role:**
- Supplemental power
- Testbed for electromechanical reuse
- Educational and diagnostic value

---

### 3. Anaerobic Digestion (Biogas)

**Description:**
- Organic waste converted into methane-rich gas
- Gas drives generators or provides heat
- Output is variable and feedstock-dependent, not steady
- Startup and parasitic costs (thermal input for digester, mixing, pumping) are uncharacterized at v0 (Placeholder) — net energy contribution unverified

**Role:**
- Variable, baseline-level power contribution
- Converts disposal burden into partial energy input at steady state

---

### 4. Solar (Supplemental)

**Description:**
- Modular photovoltaic panels
- Direct DC usage where possible
- Derating factors (temperature, soiling, inverter losses) uncharacterized at v0 (Placeholder)

**Role:**
- Offsets control and daytime loads
- Reduces peak grid draw

---

### 5. Thermal Recovery (Opportunistic)

- Waste heat reused where practical
- Not counted as primary energy source
- Used to stabilize or preheat processes

---

## Energy Storage (v0)

- Salvaged batteries preferred
- Mechanical storage acceptable
- Storage treated as required infrastructure

*Note: Salvaged battery state-of-health, cycle history, and remaining capacity are uncharacterized at v0. Degradation behavior under operating conditions — including temperature and duty cycle — is not yet modeled. See UNK-007 in `Unknowns_LF.md` for deep-environment storage degradation tracking.*

---

## Power Demand (v0 Stub)

*This section establishes the demand-side anchor required for cross-referencing with `leviathan_testing.md` and for scoping the Leviathan power envelope (UNK-006, UNK-011 in `Unknowns_LF.md`). All figures are Placeholder, derived from order-of-magnitude analogs. Accuracy is not claimed — the integration point must exist.*

---

### Operating Modes

**Bootstrap Mode** — Minimum to sustain triage and control only. Processing suspended.
- Estimated demand: ~2–5 kW (Placeholder — analogous to small industrial sorting line control systems)
- Systems active: intake triage, sensors, logging, communication
- Systems suspended: Spin Chamber, Stratification Chamber, Air Scrubber thermal systems

**Nominal Mode** — Full triage plus partial processing. Air Scrubber active.
- Estimated demand: ~15–40 kW (Placeholder — analogous to small-scale metal shredder + conveyor line)
- Systems active: all triage stations, partial Spin Chamber, Air Scrubber, control
- Grid or hybrid supply assumed at v0

**Degraded Mode** — Triage only. Processing suspended. Reduced sensor load.
- Estimated demand: ~1–3 kW (Placeholder)
- Systems active: visual triage, logging, safety monitoring
- Target: achievable on salvaged storage alone for short durations

---

### Analog Basis

Placeholder figures above are informed by:
- Small industrial shredder operations: typically 7.5–30 kW motor draw (public spec data)
- Sorting conveyor control systems: typically 1–5 kW
- AUV hotel load comparisons (for Degraded Mode floor): typically 50–300 W for sensors and control

These are order-of-magnitude anchors, not engineering estimates. They are sufficient to unblock UNK-006 scoping and will be replaced by measured or modeled values before any specification is committed.

---

## Metrics (Falsifiable)

Primary metric:
**kWh consumed per kg of recovered usable output**

*"Usable output" definition (v0): material recovered to a condition suitable for direct reuse or further processing without additional sorting. Minimum threshold: passes Component_Triage_System.md electrical or mechanical evaluation. This definition is provisional — label: Placeholder — and must be formalized before the metric can be calculated.*

Secondary indicators:
- % energy supplied by recovered sources
- Generator uptime
- Storage stability

Improvement over time is the success condition.

---

## Explicit Non-Goals (v0)

- Energy self-sufficiency
- Zero-emission claims
- Novel power generation physics
- Industrial-scale optimization

---

## Notes

- Energy is a constraint, not a flaw
- Honest accounting preserves credibility
- The Forge's value increases as energy efficiency improves
- Conversion losses, parasitic loads, and degradation rates are known unknowns at v0 — they are tracked in `Unknowns_LF.md`, not ignored

---

## Audit Status

Reviewed under Auditor_Protocols.md v0.3, energy_v0.md audit cycle, May 2026.
Status: Exploration. Five promotion blockers identified and addressed in this revision.
Auditor: Claude (Sonnet 4.6), Skeptic/Auditor role.
UNK-011 logged in `Unknowns_LF.md` as result of this cycle.

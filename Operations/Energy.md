# Energy Systems v0 — Powering the Lazarus Forge

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 1 (Medium)
- Sidecar: [#auditor-notes--unknowns]

---

## Purpose

The Lazarus Forge is an energy-intensive system. This document defines **plausible, incremental energy strategies** that allow the Forge to operate, learn, and reduce net energy cost over time.

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

### 1. Grid Power (Bootstrap)
- Primary early-stage energy source
- Enables reduction, separation, and control systems
- Treated as temporary dependency

### 2. Salvaged Motor-Generators
- Recovered motors repurposed as generators
- Back-driven via turbines, belts, or engines
- Electromechanical conversion efficiency: uncharacterized at v0 *(Placeholder)*
- Role: supplemental power, testbed for electromechanical reuse

### 3. Anaerobic Digestion (Biogas)
- Organic waste converted into methane-rich gas
- Gas drives generators or provides heat
- Output is variable and feedstock-dependent, not steady
- Startup and parasitic costs (thermal input, mixing, pumping) uncharacterized *(Placeholder)*
- Role: variable, baseline-level power contribution at steady state

### 4. Solar (Supplemental)
- Modular photovoltaic panels; direct DC usage where possible
- Derating factors (temperature, soiling, inverter losses) uncharacterized *(Placeholder)*
- Role: offsets control and daytime loads, reduces peak grid draw

### 5. Thermal Recovery (Opportunistic)
- Waste heat reused where practical
- Not counted as primary energy source
- Used to stabilize or preheat processes

---

## Energy Storage (v0)

- Salvaged batteries preferred
- Mechanical storage acceptable
- Storage treated as required infrastructure

*Note: Salvaged battery state-of-health, cycle history, and remaining capacity are uncharacterized at v0. Degradation behavior under operating conditions is not yet modeled. See LT-002 in `leviathan_testing.md` for deep-environment storage degradation tracking.*

---

## Power Demand (v0 Stub)

*Demand-side anchor required for cross-referencing with Leviathan power envelope. All figures are Placeholder, derived from order-of-magnitude analogs. Accuracy is not claimed — the integration point must exist. See EV-001 in sidecar.*

**Bootstrap Mode** — Minimum to sustain triage and control only. Processing suspended.
- Estimated demand: ~2–5 kW *(Placeholder — analogous to small industrial sorting line control systems)*

**Nominal Mode** — Full triage plus partial processing. Air Scrubber active.
- Estimated demand: ~15–40 kW *(Placeholder — analogous to small-scale metal shredder + conveyor line)*

**Degraded Mode** — Triage only. Processing suspended.
- Estimated demand: ~1–3 kW *(Placeholder)*

*Analog basis: Small industrial shredder operations typically 7.5–30 kW motor draw; sorting conveyor control typically 1–5 kW; AUV hotel load comparisons for Degraded Mode floor typically 50–300 W.*

---

## Metrics (Falsifiable)

Primary metric: **kWh consumed per kg of recovered usable output**

*"Usable output" definition (v0 — Placeholder): material recovered to a condition suitable for direct reuse or further processing without additional sorting. Minimum threshold: passes Component_Triage_System.md electrical or mechanical evaluation.*

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
- Conversion losses, parasitic loads, and degradation rates are known unknowns at v0 — tracked in this file's sidecar, not ignored

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| — | — | — | No operational entries yet — pre-build |

---

## Auditor Notes & Unknowns

### EV-001 — Forge power demand uncharacterized at any operating mode
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** What the terrestrial Lazarus Forge actually consumes at bootstrap, nominal, and degraded operating modes — even at order-of-magnitude resolution. Supply-side descriptions exist without a demand side to calibrate against.
**Resolution path:** Power Demand stub added to this document with three operating modes and Placeholder figures from analog systems. Next step: replace Placeholder figures as hardware selection proceeds. The integration point now exists for Leviathan power envelope scoping.
**Logged:** energy_v0.md audit cycle, May 2026
*Cross-module reference: UNK-011 in Unknowns_LF.md*

### Resolution Log
*(empty)*

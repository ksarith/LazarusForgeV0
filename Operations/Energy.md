# Energy Systems v0 — Powering the Lazarus Forge

> ⚠️ **Operational Safety Advisory**
> Salvaged electrochemical batteries with unknown state-of-health present thermal
> runaway and toxic outgassing risks in enclosed Forge environments. Containment
> strategy for salvaged battery banks is unresolved at v0 — see EV-003. Do not
> install salvaged battery storage in unventilated enclosures. Air Scrubber
> operation is required during any battery handling, charging, or failure event.
> When in doubt, isolate the battery bank and do not proceed.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Forge_Audit_Kit.md                                            |
| Last Audit       | 2026-05-27                                                          |
| Auditor          | Gemini — Skeptic/Auditor                                            |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Design philosophy for incremental energy strategy at v0
- Energy lifecycle progression from external dependency toward partial recovery
- Energy source categories and their roles at v0 scope
- Energy storage doctrine and known unknowns
- Power demand stub with three operating modes as a cross-reference anchor
- Primary and secondary performance metrics
- Explicit non-goals for v0

**This file DOES NOT define:**
- Hardware specifications for generators, solar arrays, or battery banks
- Biogas digester engineering or sizing
- Battery thermal containment or fire suppression specifications
  (→ EV-003; cross-reference `Operations/Air_Scrubber.md`)
- Leviathan power envelope
  (→ `Tests/Leviathan_testing.md` LT-001)
- Deep-environment battery degradation modeling
  (→ `Tests/Leviathan_testing.md` LT-002)
- Per-module energy accounting
  (→ each owning Operations/ file)
- Grid connection or utility interface specifications

---

## File Purpose

This file defines the energy strategy for the Lazarus Forge at v0. The Forge is
energy-intensive by nature — reduction, thermal separation, and fabrication all
draw significant power. This document provides a plausible, incremental path from
external grid dependency toward partial self-sufficiency through salvaged and waste
energy sources, without claiming energy independence that has not been demonstrated.

Its primary function as a cross-reference anchor is the Power Demand stub — a
demand-side placeholder that allows Leviathan power envelope scoping and per-module
energy accounting to integrate against a common reference point, even before actual
figures are measured. If this file disappeared, the repository would have no shared
energy accounting baseline and no demand-side anchor for cross-module power budgeting.

---

## Assumptions

| ID      | Assumption                                                                              | Basis                                              | Confidence | Expiry Trigger                                                        |
|---------|-----------------------------------------------------------------------------------------|----------------------------------------------------|------------|-----------------------------------------------------------------------|
| ASM-001 | Grid power is available at v0 bootstrap site                                            | v0 terrestrial deployment context                  | Medium     | Off-grid or remote deployment confirmed — bootstrap strategy changes  |
| ASM-002 | Salvaged motor-generators can be back-driven to produce usable electricity              | Standard electromechanical reversibility principle | Medium     | First salvaged motor-generator characterized for output efficiency    |
| ASM-003 | Biogas output from organic waste streams is net-positive after parasitic loads          | Analogous — agricultural micro-digester data       | Low        | EV-002 resolved — parasitic load profile characterized                |
| ASM-004 | Salvaged batteries retain sufficient usable capacity to serve as energy buffer          | Common salvage practice; SoH unknown               | Low        | First salvaged battery bank characterized for SoH and cycle capacity  |
| ASM-005 | Waste heat from Spin Chamber and other thermal processes is available for opportunistic reuse | Gate_05_Separation_Thermal.md exhaust profile  | Low        | SC-007 resolved — exhaust heat load characterized                     |

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

*Note: Conversion losses are uncharacterized for all sources below at v0. Each
source description reflects intended role, not verified output. All contribution
estimates are Placeholder pending characterization.*

### 1. Grid Power (Bootstrap)
- Primary early-stage energy source
- Enables reduction, separation, and control systems
- Treated as a temporary dependency, not a permanent fixture

### 2. Salvaged Motor-Generators
- Recovered motors repurposed as generators
- Back-driven via turbines, belts, or engines
- Electromechanical conversion efficiency: uncharacterized at v0 *(Placeholder)*
- Role: supplemental power, testbed for electromechanical reuse

### 3. Anaerobic Digestion (Biogas)
- Organic waste converted into methane-rich gas
- Gas drives generators or provides heat
- Output is variable and feedstock-dependent, not steady
- Startup and parasitic costs (thermal input, mixing, pumping) uncharacterized
  *(Placeholder — see EV-002)*
- Role: variable, baseline-level power contribution at steady state

### 4. Solar (Supplemental)
- Modular photovoltaic panels; direct DC usage where possible
- Derating factors (temperature, soiling, inverter losses) uncharacterized *(Placeholder)*
- Role: offsets control and daytime loads, reduces peak grid draw

### 5. Thermal Recovery (Opportunistic)
- Waste heat reused where practical
- Not counted as a primary energy source
- Used to stabilize or preheat processes
- Cross-reference: `Operations/Gate_05_Separation_Thermal.md` exhaust profile (SC-007)

---

## Energy Storage (v0)

- Salvaged batteries preferred where available
- Mechanical storage acceptable as alternative
- Storage treated as required infrastructure, not optional

*Salvaged battery state-of-health, cycle history, and remaining capacity are
uncharacterized at v0. Degradation behavior under operating conditions is not yet
modeled. See LT-002 in `Tests/Leviathan_testing.md` for deep-environment storage
degradation tracking.*

*Thermal runaway and toxic outgassing risks from salvaged electrochemical packs
with unknown SoH are unmitigated at v0. A containment and ventilation strategy
for salvaged battery installations is required before any enclosed battery bank
is commissioned. See EV-003 and `Operations/Air_Scrubber.md`.*

---

## Power Demand (v0 Stub)

*Demand-side anchor required for cross-referencing with Leviathan power envelope.
All figures are Placeholder, derived from order-of-magnitude analogs. Accuracy is
not claimed — the integration point must exist. See EV-001 in sidecar.*

*Truth Provenance: Internally Derived / Analogous External — all three mode
definitions below are structural states derived from analog system comparisons,
not measured Forge data.*

**Bootstrap Mode** — Minimum to sustain triage and control only. Processing suspended.
- Estimated demand: ~2–5 kW *(Placeholder — analogous to small industrial sorting
  line control systems)*

**Nominal Mode** — Full triage plus partial processing. Air Scrubber active.
- Estimated demand: ~15–40 kW *(Placeholder — analogous to small-scale metal
  shredder + conveyor line)*

**Degraded Mode** — Triage only. Processing suspended.
- Estimated demand: ~1–3 kW *(Placeholder)*

*Analog basis: Small industrial shredder operations typically 7.5–30 kW motor draw;
sorting conveyor control typically 1–5 kW; AUV hotel load comparisons for Degraded
Mode floor typically 50–300 W.*

---

## Metrics (Falsifiable)

Primary metric: **kWh consumed per kg of recovered usable output**

*"Usable output" definition (v0 — Placeholder): material recovered to a condition
suitable for direct reuse or further processing without additional sorting. Minimum
threshold: passes `Operations/Gate_02_Triage.md` electrical or mechanical evaluation.*

Secondary indicators:
- % energy supplied by recovered sources
- Generator uptime
- Storage health trend *(Placeholder — measurement method not yet defined)*

Improvement over time is the success condition.

---

## Explicit Non-Goals (v0)

- Energy self-sufficiency
- Zero-emission claims
- Novel power generation physics
- Industrial-scale optimization

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No operational entries yet — pre-build | — | — |

---

## Active Disputes

| ID | Dispute Summary    | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Auditor Notes & Unknowns

### EV-001 — Forge power demand uncharacterized at any operating mode

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | In Progress                    |
| Risk          | Medium                         |
| Priority      | Major                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Energy.md           |
| First Logged  | 2026-05-04                     |
| Last Reviewed | 2026-05-27                     |

**Description:** What the terrestrial Lazarus Forge actually consumes at bootstrap,
nominal, and degraded operating modes is unknown — even at order-of-magnitude
resolution. Supply-side descriptions exist without a demand side to calibrate against.

**Why It Matters:** Without a demand baseline, the Forge cannot determine whether
available power sources are sufficient for any operating mode, or whether the Air
Scrubber draw (AS-001) plus processing loads exceed bootstrap budget.

**Resolution Path:** Power Demand stub added with three operating modes and Placeholder
figures from analog systems. Next step: replace Placeholder figures as hardware
selection proceeds. The integration point now exists for Leviathan power envelope
scoping. Cross-module reference: `Unknowns.md` (EV-001 cluster).

---

### EV-002 — Parasitic and thermal startup loads for biogas streams uncharacterized

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | Low                            |
| Priority      | Minor                          |
| Type          | Technical                      |
| Blocking      | No                             |
| Owner         | Operations/Energy.md           |
| First Logged  | 2026-05-27                     |
| Last Reviewed | 2026-05-27                     |

**Description:** The total net energy yield of the anaerobic digestion subsystem
when accounting for internal heating elements, slurry pumping, and mechanical mixing
is unknown. The body text identifies this as Placeholder but no sidecar entry existed
to track it.

**Why It Matters:** Without characterizing parasitic loads, the biogas source may be
net-negative at small scale — consuming more energy to operate than it produces. This
would eliminate it as a viable v0 energy source and affect the energy lifecycle model.

**Resolution Path:** Identify standard agricultural scaling models for micro-digesters
and cross-reference against expected feedstock availability at v0 Forge scale. Update
from Placeholder to Analogous External when characterized. Payment via Specification
once first operational digester run produces measured net yield data.

---

### EV-003 — Salvaged battery thermal containment and ventilation strategy undefined

| Field         | Value                          |
|---------------|--------------------------------|
| Status        | Open                           |
| Risk          | High                           |
| Priority      | Critical                       |
| Type          | Technical / Safety             |
| Blocking      | Yes (before enclosed battery   |
|               | bank commissioning)            |
| Owner         | Operations/Energy.md           |
| First Logged  | 2026-05-27                     |
| Last Reviewed | 2026-05-27                     |

**Description:** Salvaged electrochemical batteries with unknown state-of-health
present thermal runaway and toxic outgassing risks. No containment strategy,
ventilation requirement, or failure response doctrine exists for salvaged battery
installations in enclosed Forge environments.

**Why It Matters:** Thermal runaway in an enclosed space with other combustible
materials is a credible catastrophic failure mode. Outgassing from lithium or
lead-acid batteries produces toxic and potentially explosive vapor. This risk is
unmitigated at v0 and blocks commissioning of any enclosed salvaged battery bank.

**Resolution Path:** Define minimum containment requirements for salvaged battery
installations — physical separation from combustibles, forced ventilation path,
temperature monitoring, and failure isolation protocol. Cross-reference
`Operations/Air_Scrubber.md` for outgassing capture requirements. A formal battery
safety doctrine may warrant its own file or a dedicated section in a future
`Admin/Safety_Protocols.md`. Payment via Specification once containment strategy
is defined and validated against first battery installation.

---

### Resolution Log

- 2026-05-27: EV-001 — Reformatted from prose to structured sidecar table format.
  Stale cross-reference `UNK-011 in Unknowns_LF.md` corrected to `Unknowns.md`.
  Content and status preserved.
- 2026-05-27: EV-002 — New entry. Biogas parasitic load gap identified in Gemini
  Skeptic/Auditor audit 2026-05-27. Body text placeholder promoted to tracked unknown.
- 2026-05-27: EV-003 — New entry. Salvaged battery thermal runaway and outgassing
  hazard identified in Gemini Skeptic/Auditor audit 2026-05-27. Flagged Critical and
  Blocking before enclosed battery bank commissioning.

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| —    | —    | No abandoned paths yet — pre-build | — |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Power Demand mode definitions revised without EV-001 cross-validation against
  hardware selection data
- Biogas listed as a net-positive source without EV-002 resolution
- Salvaged battery storage commissioned in an enclosed space before EV-003 is resolved
- Energy independence claimed without measurement
- Thermal recovery from Gate_05 counted as primary energy source before SC-007 is resolved
- Metrics section revised to remove the falsifiable primary metric
  (kWh per kg recovered usable output)
- Stale filename `Component_Triage_System.md` reintroduced in Metrics section
  (canonical reference is `Operations/Gate_02_Triage.md`)
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

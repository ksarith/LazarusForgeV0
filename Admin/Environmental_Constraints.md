# Environmental_Constraints.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 1/6 (G1 cleared — fallacy checklist applied at creation)            |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| Last Audit       | 2026-06-19                                                          |
| Auditor          | Grok — Systems Integrator; Claude — Synthesizer                     |
| Open Unknowns    | 9                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Site-specific and regional environmental parameters that materially affect Forge operations
- Regulatory, climatic, ecological, and jurisdictional constraint categories
- Bootstrap environmental risk assessment and mitigation priorities
- Integration interlocks between environmental conditions and core operational metrics
- Graceful degradation triggers tied to environmental conditions
- Junction point for EC-010 (jurisdiction conflict), GOV-010 (regulatory compliance friction), and related cross-module convergences

**This file DOES NOT define:**
- Detailed engineering specifications for facilities or equipment (→ `Architecture/Facilities.md`, `Operations/`)
- Physical site safety margins, PPE, heat stress, emergency response (→ `Admin/Safety_Protocols.md`)
- Constitutional governance doctrine (→ `Admin/Governance_Charter.md`)
- Specific material processing procedures (→ `Operations/`)
- Long-term climate modeling or environmental activism
- Jurisdiction conflict resolution hierarchy — pending ENV-003
- Human authority conflict resolution in contested jurisdictions — pending `Admin/Ethical_Constraints.md` EC-009

---

## File Purpose

This file establishes the environmental boundary conditions within which the Lazarus Forge must operate. It exists to prevent optimistic assumptions about "standard conditions" from undermining bootstrap viability, regulatory survival, or ecological accountability. Without it, deployments risk catastrophic mismatch between doctrine and physical reality — leading to mission failure, legal friction, or unintended environmental harm.

This file is also the planned resolution junction for EC-010 (`Admin/Ethical_Constraints.md` — jurisdiction conflict hierarchy) and GOV-010 (`Admin/Governance_Charter.md` — regulatory compliance friction for physical deployment). Both unknowns explicitly converge here at v1 transition. This file is created now so those unknowns have a resolution target and so site-specific context can accumulate before it is urgently needed.

**Honest v0 acknowledgment:** At current maturity, environmental constraints are documented as doctrine categories, not validated operational parameters. Site-specific values must be substituted from the Reference Deployment Context (RDC) when deployment begins. No claim in this file should be treated as operationally hardened until local site data replaces the placeholder anchors.

---

## Assumptions

| ID         | Assumption                                                                                    | Basis                              | Confidence | Expiry Trigger                                              |
|------------|-----------------------------------------------------------------------------------------------|------------------------------------|------------|-------------------------------------------------------------|
| ASM-EC-001 | Reference Deployment Context (RDC) provides a usable baseline for environmental parameters   | `Architecture/Facilities.md` checklist — Internally Derived | Medium | Specific site initialization with locally measured data |
| ASM-EC-002 | Local regulatory frameworks are navigable with sufficient documentation and good-faith operation | Historical salvage operations — Analogous External | Low | Evidence of prohibitive or hostile regulatory regime confirmed |
| ASM-EC-003 | Climate parameters change slowly enough for v0–v1 manual adjustment cycles                   | Current operational horizon — Internally Derived | Medium | Rapid non-linear change observed at deployment site |
| ASM-EC-004 | Community environments encountered at bootstrap will not be actively hostile to salvage operations | General salvage-context experience — Analogous External | Low | Confirmed hostile social environment at deployment site |

---

## Body

### Core Doctrine

Environmental constraints are treated as **non-negotiable boundary conditions**, not obstacles to be optimized away. The Forge adapts to the environment; it does not demand the environment adapt to the Forge. All major decisions — site selection, gate sequencing, energy strategy, material triage — must route through these constraints before execution.

**Primary Interlock:** Every environmental factor must ultimately be evaluated against Value Recovered per kWh and graceful degradation capacity. A solution that functions under controlled conditions but fails under real local conditions (dust, humidity, temperature extremes, regulatory hostility, community friction) is rejected. The environment is the test, not the lab.

**No externalized entropy:** The Forge's salvage-first philosophy extends to environmental impact. Do not solve internal resource problems by externalizing waste, contamination, or entropy into the surrounding environment. This is both a practical doctrine (regulatory risk, community trust) and an ethical requirement under Axiom P-1 (Preservation of Life) and Axiom P-3 (Collaboration and Mutual Benefit).

---

### Constraint Category 1 — Climatic and Physical

These are the environmental realities of the physical site. They change slowly but determine the operational envelope for every gate.

**Key parameters (Placeholder — substitute from site assessment):**
- Temperature range (operating and storage extremes)
- Humidity range (affects electronics, corrosion, dust behavior)
- Precipitation pattern (flooding risk, drainage requirements, water availability)
- Wind loading (structural requirements, dust transport)
- Seismic risk classification
- Dust and particulate environment (affects Air Scrubber demand, electronics handling)
- Biological activity (biofouling rate for marine deployments, pest pressure for land sites)
- UV exposure and weathering rate

**Operational implications:**
- High humidity → elevated corrosion rate in salvaged materials; elevated BFR release risk in electronics processing
- Temperature extremes → battery thermal management constraints (cross-ref EV-003), Peltier device operating range (cross-ref TH-004)
- High dust → Air Scrubber demand increase, sensor fouling (cross-ref MG-008, FD-002)
- Seismic risk → structural safety factors for salvaged frames (cross-ref EN-001, EN-002)

**Primary reference:** `Architecture/Facilities.md` Site Initialization Checklist is the mandatory local substitution document for all Placeholder values above.

---

### Constraint Category 2 — Regulatory and Jurisdictional

Legal and regulatory constraints determine what the Forge may do at a given site. They are treated as hard external inputs, not optimization variables.

**Key domains:**
- Permitting requirements for waste handling, thermal processing, and metal recovery
- Emissions limits (particulate, VOC, thermal)
- Hazardous material handling regulations (asbestos, heavy metals, BFR-containing materials — cross-ref WA-002, CE-003)
- Environmental protection statutes (water discharge, soil contamination)
- Zoning and land use restrictions
- Labor and occupational safety regulations (cross-ref `Admin/Safety_Protocols.md`)
- Maritime law and salvage rights (relevant for Leviathan-class deployments)
- Cultural heritage protections (cross-ref `Admin/Ethical_Constraints.md` §Cultural and Sacred Site Recognition)

**Bootstrap operating doctrine:**
Where regulatory frameworks are ambiguous or incomplete, the Forge may operate in legal gray zones **only when** all of the following conditions are met:
1. Human safety is not compromised
2. Documentation of all relevant decisions and their rationale is maintained for later normalization
3. No irreversible environmental harm is caused
4. Operations cease if a regulatory authority issues a clear prohibition

**Jurisdiction conflicts:** When laws are mutually incompatible (maritime vs. national, environmental vs. salvage rights, multiple sovereign claims), escalate to human review per `Admin/Ethical_Constraints.md` §Legal Context Awareness. Until ENV-003 (jurisdiction conflict hierarchy) is resolved, "escalate to human review" is the operative instruction. For Leviathan-class deployments, assume multi-jurisdiction environments as the default condition, not the exception.

**Regulatory compliance unknown tracking:** FA-003 (zoning and permitting), SP-005 (regulatory compliance), EC-010 (jurisdiction conflict), GOV-010 (compliance friction) all feed this category. See sidecar.

---

### Constraint Category 3 — Ecological and Resource

The Forge's material recovery mission intersects with local ecological systems. These constraints govern that intersection.

**Resource availability:**
- Local water availability and quality (cross-ref `Challenges/Water.md`, `Tests/Living_Waters.md`)
- Salvage stream density and composition (urban ore concentration, device type mix)
- Critical mineral access via salvage vs. extraction trade-offs (cross-ref `Challenges/Critical_Minerals.md`)
- Renewable energy availability (solar, wind, tidal, thermal gradient — cross-ref `Operations/Energy.md`)

**Ecological impact:**
- Biodiversity sensitivity of deployment site (protected species, habitat corridors)
- Water discharge quality requirements (cross-ref `Challenges/Water.md` WS-002, WS-004)
- Soil contamination risk from operations (cross-ref `Challenges/Waste.md` WA-004)
- Marine ecosystem impact for aquatic deployments (cross-ref `Challenges/Biofouling.md` BF-004, `Tests/Trophic_Forge.md` TF-006)
- Carbon and thermal budget of operations vs. value recovered

**Doctrine:** Net-positive material recovery preferred. Externalizing entropy — dumping processing waste into surrounding ecology to simplify internal operations — is prohibited under the no-externalized-entropy principle above and under Axiom P-1.

---

### Constraint Category 4 — Human and Social

Physical and ecological constraints are well-defined. Human and social constraints are harder to measure but equally capable of ending operations.

**Key dimensions:**
- Community acceptance of salvage operations (noise, truck traffic, visual impact, perceived contamination risk)
- Labor availability and skill base in the deployment region
- Security environment (theft risk for salvaged materials and equipment, operator safety)
- Competing land and resource use claims
- Informal sector relationships (cross-ref `Challenges/Waste.md` WA-003 — informal waste recovery worker integration)
- Community adoption capacity for outputs (cross-ref `Challenges/Water.md` WS-004, `Challenges/Planned_Obsolescence.md` PO-004)

**v0 guidance:** Community friction is most often generated by opacity, not by operations themselves. Early, honest communication about what the Forge does and does not do reduces friction more reliably than technical mitigation. This is both pragmatically sound and consistent with Axiom P-3 (Collaboration and Mutual Benefit).

---

### Graceful Degradation Rules

When environmental constraints tighten, the Forge degrades gracefully rather than failing hard or bypassing safety.

| Condition | Degradation Response |
|-----------|---------------------|
| Regulatory uncertainty increases | Reduce operational scope to lowest-risk activities; maintain documentation; pause contested operations |
| Climate conditions exceed design envelope | Reduce throughput; increase human oversight; defer thermal operations in high fire-risk conditions |
| Community opposition escalates | Pause operations; escalate to human governing party; do not attempt to operate through active community opposition |
| Ecological impact detected | Halt the contributing operation; assess and document; do not resume until impact pathway is understood |
| Jurisdictional conflict unresolvable by human review | Default to non-action per `Admin/Ethical_Constraints.md` §Core Mandate |

**Hard rule:** Never sacrifice Tier 1 Axioms to meet environmental targets, throughput goals, or regulatory pressure. If a regulatory authority demands an action that would violate Axiom P-1 or the Anti-Weaponization Doctrine, compliance is refused and the situation is escalated to the human governing party.

---

### Integration Map

| System | Environmental Interlock |
|--------|------------------------|
| `Operations/Energy.md` | Cooling/heating loads, solar/wind viability, thermal recovery efficiency — all site-dependent |
| `Operations/Gate_05_Separation_Thermal.md` | Thermal operations subject to fire-risk season constraints and local emissions limits |
| `Architecture/Facilities.md` | Site Initialization Checklist is the primary local substitution document for all Placeholder values |
| `Admin/Safety_Protocols.md` | Operator heat stress, hearing, and emergency response all require site-specific calibration |
| `Admin/Ethical_Constraints.md` | Jurisdiction conflicts and human authority questions route here; EC-010 and EC-009 cross-reference |
| `Admin/Governance_Charter.md` | GOV-010 regulatory compliance friction convergence point |
| `Challenges/Waste.md` | Hazardous fraction handling subject to local regulatory constraints |
| `Challenges/Water.md` | Water availability and discharge quality are site-dependent |
| `Challenges/Biofouling.md` | Fouling rate and species composition vary by latitude, season, biological activity |
| `Tests/Leviathan_testing.md` | Multi-jurisdiction maritime environment is the primary stress-test context |
| `Tests/Trophic_Forge.md` | TF-006 (non-target insect capture) and ecological impact are site-specific |

---

## Upstream / Downstream

**Upstream (constrains this file):**
- `Admin/Governance_Charter.md` — Tier 1 Axioms P-1, P-3 are the ethical floor for all environmental decisions
- `Admin/Ethical_Constraints.md` — Anti-Weaponization, Life Preservation, and jurisdiction escalation doctrine
- `Architecture/Facilities.md` — Site Initialization Checklist provides the baseline parameter substitution source
- `Admin/Safety_Protocols.md` — operator safety constraints must remain consistent with environmental doctrine

**Downstream (depends on this file):**
- `Admin/Ethical_Constraints.md` EC-010 — jurisdiction conflict hierarchy resolution path leads here
- `Admin/Governance_Charter.md` GOV-010 — regulatory compliance friction resolution path leads here
- `Architecture/Facilities.md` FA-003 — zoning and permitting assessment references environmental constraint categories
- `Admin/Safety_Protocols.md` SP-005 — regulatory compliance assessment references this file
- `Challenges/Waste.md` WA-003, WA-004 — informal sector integration and disposal doctrine have environmental dimensions
- `Challenges/Water.md` WS-002, WS-004 — water quality and community adoption reference this file
- `Challenges/Biofouling.md` BF-003 — regional fouling rate calibration references local ecological parameters
- `Tests/Leviathan_testing.md` — multi-jurisdiction maritime context is the primary deployment stress environment
- `Tests/Trophic_Forge.md` TF-006 — ecological impact assessment references this file

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-19 | Deferring this file to v1 transition | EC-010 and GOV-010 have no resolution target without this file; downstream audit friction accumulates with each cycle it is absent; better to create a minimal compliant version now than to defer and accumulate drift | No |
| 2026-06-19 | Merging environmental constraints into Facilities.md | Facilities.md governs physical workspace prerequisites and equipment siting; environmental constraints are a broader category that includes regulatory, ecological, and social dimensions that Facilities.md does not own | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Environmental constraints reframed as "to be engineered away" rather than non-negotiable boundary conditions
- Reference Deployment Context used as final answer rather than substitution baseline
- Throughput or capability targets cited as justification for bypassing regulatory compliance
- No-externalized-entropy principle qualified or removed
- Graceful degradation rules weakened to allow operations through active community opposition or detected ecological impact
- Tier 1 Axiom compliance cited as optional when in conflict with environmental or regulatory pressure
- EC-010 and GOV-010 closed without updating this file as their resolution record
- Site-specific values promoted to Specification without local data replacing Placeholder anchors
- Ethical Anchor field absent, altered, or does not match canonical string
- Verification Ref field changed from `Admin/Verification_Gates_LF.md`
- Upstream/Downstream table loses any of the eight downstream dependents listed without a corresponding unknown or correction entry

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### ENV-001 — Site-specific climate parameter baseline not established

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | High                                   |
| Priority      | Major                                  |
| Type          | Operational / Physical                 |
| Blocking      | Yes (for any site-specific gate calibration) |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** All climatic and physical parameters in Constraint Category 1 are Placeholder values. No site-specific measurements exist for temperature range, humidity, dust load, seismic classification, or biological activity at any candidate deployment site.

**Why It Matters:** Every gate calibration that depends on environmental conditions — thermal process scheduling, Air Scrubber sizing, battery thermal management, structural safety factors — remains site-generic until this is resolved. Site-generic values are better than nothing; they are not sufficient for Specification promotion of dependent systems.

**Resolution Path:** Conduct site assessment per `Architecture/Facilities.md` Site Initialization Checklist at first candidate deployment site. Record measured values here, replacing Placeholder anchors. Update dependent files as each value is confirmed.

---

### ENV-002 — Regulatory compliance framework for bootstrap site not assessed

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | High                                   |
| Priority      | Major                                  |
| Type          | Regulatory / Legal                     |
| Blocking      | Yes (for operations in regulated environments) |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** No regulatory compliance assessment has been conducted for any candidate bootstrap site. Permitting requirements, emissions limits, waste handling regulations, and zoning constraints are all unknown for the first deployment context.

**Why It Matters:** Regulatory non-compliance can halt operations with no recovery path. The bootstrap operating doctrine (gray zones with documentation) is a temporary posture, not a sustainable one. Regulatory mapping must occur before sustained operations begin.

**Resolution Path:** Conduct regulatory landscape assessment for first candidate site. Map applicable regulations against Constraint Category 2 above. Log specific unknowns or blockers as sub-entries. Cross-reference FA-003 (zoning and permitting) and SP-005 (regulatory compliance) — those may resolve concurrently.

---

### ENV-003 — Jurisdiction conflict hierarchy undefined

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Medium                                 |
| Priority      | Minor                                  |
| Type          | Regulatory / Governance                |
| Blocking      | No                                     |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** When laws are mutually incompatible across jurisdictions (maritime vs. national law, environmental law vs. salvage rights, multiple sovereign claims in international waters), the Forge currently escalates to human review. No resolution hierarchy exists beyond that escalation.

**Why It Matters:** Leviathan-class deployments will encounter multi-jurisdiction environments as a default condition. "Escalate to human review" is a valid interim instruction but is not sufficient when human review is unavailable or when conflicts are structural and persistent. Cross-references EC-010 (`Admin/Ethical_Constraints.md`) and GOV-010 (`Admin/Governance_Charter.md`) — both converge here.

**Resolution Path:** Define minimum jurisdiction conflict hierarchy at v1 transition. Minimum doctrine: when jurisdictions conflict and human review is unavailable, default to the more restrictive interpretation of each constraint (cross-ref `Admin/Ethical_Constraints.md` §Legal Context Awareness). Full hierarchy definition deferred until first Leviathan-class or maritime deployment is planned.

---

### ENV-004 — Ecological impact assessment protocol undefined

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Medium                                 |
| Priority      | Major                                  |
| Type          | Ecological / Operational               |
| Blocking      | No                                     |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** The graceful degradation rules specify "halt the contributing operation" when ecological impact is detected, but no assessment protocol exists for detecting impact in the first place. Detection methods, monitoring cadence, threshold criteria, and responsible assessment agent are all undefined.

**Why It Matters:** "Halt when impact detected" is only as strong as the detection mechanism. Without a monitoring protocol, impact may go undetected until it is severe. Cross-references TF-006 (non-target insect capture), BF-004 (shed panel reef toxin leach), WA-004 (negative-value waste disposal).

**Resolution Path:** Define minimum ecological monitoring protocol at Draft or above. Minimum viable version: designated observation check at each audit opening for any active deployment; threshold criteria for three impact dimensions (water discharge quality, soil condition, local species behavior). Cross-reference `Tests/Trophic_Forge.md` and `Challenges/Biofouling.md` for domain-specific impact indicators.

---

### ENV-005 — Community engagement protocol undefined

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Medium                                 |
| Priority      | Major                                  |
| Type          | Social / Operational                   |
| Blocking      | No                                     |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** Constraint Category 4 notes that community friction is most often generated by opacity, and that early honest communication reduces friction. No formal protocol exists for when to engage, what to communicate, or how to manage escalating community concerns.

**Why It Matters:** Community opposition can halt operations as effectively as regulatory prohibition, and with less predictable timeline. A protocol that engages proactively is cheaper than reactive crisis management. Cross-references WA-003 (informal sector integration), PO-004 (community re-baselining skill transfer), WS-004 (community adoption).

**Resolution Path:** Define minimum community engagement protocol at Draft or above. Minimum doctrine: pre-operation disclosure to directly affected community before any sustained salvage operations begin; designated point of contact for community questions; documented response log for concerns raised.

---

### ENV-006 — No-externalized-entropy doctrine not operationalized

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Medium                                 |
| Priority      | Major                                  |
| Type          | Ecological / Governance                |
| Blocking      | No                                     |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** The no-externalized-entropy principle is declared as doctrine but has no operational definition — no metric, no detection mechanism, and no threshold for what constitutes "externalizing entropy" in practice versus acceptable waste generation.

**Why It Matters:** Without operationalization, the principle is aspirational rather than enforceable. "Do not externalize entropy" must eventually become a checkable condition — probably tied to waste stream accounting per gate cycle, similar to how Value Recovered per kWh ties throughput to energy.

**Resolution Path:** Define minimum operationalization at Draft or above. Candidate metric: waste-out-to-material-in ratio per operating cycle, with a threshold above which operations trigger review. Cross-reference `Challenges/Waste.md` WA-004 (negative-value disposal) and `Operations/Gate_03_Reduction.md` GR-003 (biological and chemical waste disposal doctrine).

---

### ENV-007 — Environmental constraint integration with AUDIT_HARNESS.py undefined

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Low                                    |
| Priority      | Minor                                  |
| Type          | Technical / Governance                 |
| Blocking      | No                                     |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** This file is not yet referenced in `Admin/AUDIT_HARNESS.py` file registry or EXTRA_FILES comment block. Environmental constraint context is not loadable in standard audit sessions.

**Why It Matters:** Audits of downstream files (Facilities.md, Safety_Protocols.md, Ethical_Constraints.md, Waste.md) that reference environmental constraints cannot load this file as context until the harness is updated.

**Resolution Path:** Add `Environmental_Constraints.md` to AUDIT_HARNESS.py FILE_REGISTRY under Admin/ path and add to EXTRA_FILES comment block with description: "load when site constraints, regulatory compliance, jurisdiction conflicts, or ecological impact are relevant to the audit." Also add to `Routing.md` and `Discovery.md`.

---

### ENV-008 — File not yet registered in Routing.md, Discovery.md, or Unknowns.md

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | Medium                                 |
| Priority      | Major                                  |
| Type          | Governance / Navigation                |
| Blocking      | Yes (until registered)                 |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** This file does not yet appear in `Routing.md` (programmatic URL routing), `Discovery.md` (navigation map and confirmed file list), or `Unknowns.md` (ENV- cluster). Until registered, it is invisible to the audit harness and to agents loading standard navigation context.

**Why It Matters:** An unregistered file cannot be fetched by AUDIT_HARNESS.py, cannot be cross-referenced reliably, and does not benefit from the canonical path resolution that `Discovery.md` provides.

**Resolution Path:** At commit: (1) add `Environmental_Constraints.md` → `Admin/Environmental_Constraints.md` to `Routing.md`; (2) add to `Discovery.md` confirmed file list and scope map; (3) register ENV-001 through ENV-008 in `Unknowns.md` under a new ENV cluster; (4) add to `Admin/AUDIT_HARNESS.py` FILE_REGISTRY. These four actions close ENV-008.

---

### ENV-009 — No site has been assessed against this file's constraints

| Field         | Value                                  |
|---------------|----------------------------------------|
| Status        | Open                                   |
| Risk          | High                                   |
| Priority      | Critical                               |
| Type          | Operational                            |
| Blocking      | Yes (for any operational deployment)   |
| Owner         | `Admin/Environmental_Constraints.md`   |
| First Logged  | 2026-06-19                             |
| Last Reviewed | 2026-06-19                             |

**Description:** This file defines the constraint framework but no deployment site has been evaluated against it. All four constraint categories carry Placeholder values. The file is a doctrine target, not an operational record.

**Why It Matters:** The gap between doctrine and operational reality is the highest-risk condition in the Forge's governance architecture. A file that exists but has never been applied to a real site is not yet validated as useful or complete.

**Resolution Path:** At first candidate site assessment, apply all four constraint categories as a structured checklist. Record findings as site-specific entries. Update Placeholder values with Measured or Estimated data. Log findings that reveal gaps in the constraint framework as new ENV- unknowns. This unknown closes when the first site assessment is complete and recorded here.

---

### Resolution Log

- 2026-06-19: File created (v0.1). Drafted by Grok (Systems Integrator), revised to File_Template.md compliance by Claude (Synthesizer). Four constraint categories established: Climatic/Physical, Regulatory/Jurisdictional, Ecological/Resource, Human/Social. Core doctrine, graceful degradation rules, integration map, and upstream/downstream table added. ENV-001 through ENV-009 logged. EC-010 and GOV-010 convergence point declared. ENV-008 (registration) is the first priority action before any downstream audit references this file.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 Axioms P-1 (Preservation of Life) and P-3 (Collaboration and Mutual Benefit) are the ethical floor for all environmental decisions; GOV-010 (regulatory compliance friction) resolution path leads here
- `Admin/Ethical_Constraints.md` — EC-010 (jurisdiction conflict hierarchy) and EC-009 (human authority conflict) resolution paths lead here; Life Preservation and Anti-Weaponization doctrines apply when environmental pressure conflicts with Tier 1 constraints
- `Architecture/Facilities.md` — Site Initialization Checklist is the primary local substitution document for all Placeholder values in Constraint Category 1; FA-003 (zoning and permitting) cross-references Constraint Category 2
- `Admin/Safety_Protocols.md` — operator safety constraints must be calibrated against local environmental conditions; SP-005 (regulatory compliance) cross-references this file
- `Operations/Energy.md` — energy strategy is directly shaped by local renewable availability and thermal recovery efficiency
- `Operations/Gate_05_Separation_Thermal.md` — thermal operations subject to fire-risk season and emissions constraints
- `Challenges/Waste.md` — hazardous fraction handling (WA-002, WA-004) subject to local regulatory constraints; informal sector integration (WA-003) has community dimension
- `Challenges/Water.md` — water availability and discharge quality are site-specific; WS-002 and WS-004 reference environmental and community conditions
- `Challenges/Biofouling.md` — BF-003 (regional fouling rate) and BF-004 (shed panel ecological impact) are site-specific
- `Challenges/Critical_Minerals.md` — local mineral access via salvage vs. extraction trade-offs reference this file
- `Tests/Leviathan_testing.md` — multi-jurisdiction maritime environment is the primary stress-test context for all four constraint categories
- `Tests/Trophic_Forge.md` — TF-006 (non-target insect capture) and TF-010 (seasonal variability) reference local ecological conditions
- `Unknowns.md` — ENV-001 through ENV-009 to be registered at next Unknowns.md update; EC-010 and GOV-010 cross-references already in v3.5
- `Discovery.md` — this file must be added to confirmed file list and scope map (ENV-008)
- `Routing.md` — this file must be added to programmatic routing table (ENV-008)
- `Admin/AUDIT_HARNESS.py` — this file must be added to FILE_REGISTRY and EXTRA_FILES comment block (ENV-007, ENV-008)

---

## Status

Version 0.1 — Initial compliant draft (2026-06-19).

**First priority action before downstream use:** Register this file in `Routing.md`, `Discovery.md`, `Unknowns.md`, and `Admin/AUDIT_HARNESS.py` per ENV-008. Until registered, cross-references to this file from other documents are navigation dead-ends.

**What must remain constant:**

**The Forge adapts to the environment. The environment does not adapt to the Forge.**

**No externalized entropy. No compliance theater.**

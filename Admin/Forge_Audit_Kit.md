# Forge_Audit_Kit.md
**Condensed audit reference for LazarusForgeV0 multi-agent cycles.**
**Replaces loading Auditor_Protocols.md + Unknowns_LF.md in routine audit prompts.**
**Current as of: Auditor_Protocols v0.5 / Unknowns_LF v1.0 — May 2026**

Full reference files: `Auditor_Protocols.md` | `Unknowns_LF.md`

---

## GOVERNING PRINCIPLES

> Capability never outruns permission. — `Ethical_Constraints.md`
> Confidence never outruns verification. — `Auditor_Protocols.md`

**Scope boundary:** Human override rights apply to verification process decisions only. They do not extend to hard-line doctrines in `Ethical_Constraints.md` (Anti-Weaponization, Life Preservation).

**Sidecar Model (v0.5):** Module-specific unknowns live in each file's own `## Auditor Notes & Unknowns` footer. This index lists cross-module unknowns only. Full entry detail is in the owning file's sidecar.

---

## EXPLORATION vs. SPECIFICATION

**Exploration** — incomplete, speculative, loosely connected. Do not over-police.
**Specification** — must pass all gates. Claims binding, cross-refs must resolve, numbers must be labeled.
**Loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

*Full reference: `Auditor_Protocols.md` §Exploration vs. Specification*

---

## FALLACY CHECKLIST

Apply to all specification-level claims. Bare checkmarks are not verification — substantive notes required for non-trivial claims.

**1. Magic Energy** — Every watt needs a traceable origin. Cross-ref `energy_v0.md`.
**2. Friction Blindness** — Account for mechanical resistance, thermal losses, fluid drag, wear. Real systems degrade.
**3. Energy Density Paradox** — Does a recovery step cost more than it produces? Justify as enabling investment or flag.
**4. Semantic Drift** — Terms must mean the same thing everywhere. Cross-check against `Lazarus_forge_v0_flow.md`.
**5. Scope Creep** — New capabilities belong in `Trajectories_LF.md`, not silently in v0 specs.
**6. Hallucinated Files** — All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified even when not loaded in the current prompt.
**7. Confidence Without Basis** — All numbers must be labeled: **Measured** / **Estimated** / **Analogous** / **Placeholder**. Unlabeled = Placeholder.
**8. Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life path.
**9. Incomplete by Omission** — What critical subsystem is missing? Heat dissipation, waste streams, power draw, human interface?
**10. The Turd Problem** — Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this.

*Full reference: `Auditor_Protocols.md` §The Fallacy Checklist*

---

## AI CONTRIBUTION RULES

**Role declaration required:** *"Operating as [Role] per Auditor_Protocols.md v0.5"*
**Roles:** Synthesizer | Engineer | Skeptic/Auditor | Connective Tissue

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed.
**Rule 2 — Role Awareness:** Name role shifts before proceeding.
**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.
**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them.
**Rule 5 — Confidence Labeling:** Use the four-label system. Unlabeled = Placeholder.
**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."*

*Full reference: `Auditor_Protocols.md` §AI Contribution Protocols*

---

## VERIFICATION GATES

Sequential. Auditor has binding block authority. Self-approval loops not permitted.

| Gate | Test | Fail → |
|---|---|---|
| 1 — Fallacy Check | Fallacy Checklist actively applied with substantive notes? | Return to author |
| 2 — Verification Artifacts | At least one falsifiable artifact per significant claim? | Return for artifact generation |
| 3 — Adversarial Pass | At least one concrete failure scenario tested? | Must undergo adversarial testing |
| 4 — Scope Alignment | Fits current version, or future trajectory? | Route to `Trajectories_LF.md` |
| 5 — Cross-Reference Integrity | All file refs resolve? Cross-repo deps bidirectional? | Hold at draft |
| 6 — Conflict Check | Contradicts existing committed specs? | Resolve conflict before committing |

**Full Stop Review:** Trigger conditions: (1) same foundational claim blocked across two separate cycles; (2) new finding invalidates a previously promoted spec; (3) pattern of overrides eroding a governance principle. Log: triggering agent, one falsifiable sentence, date, outcome.

*Full reference: `Auditor_Protocols.md` §Verification Gates / §Full Stop Review*

---

## SIGN-OFF FORMAT

```
Document: [filename] ([status] audit, [date])
Auditor: [Role] — [Agent]
Gates cleared: [list]
Gates blocked: [list with reason]
Unknowns logged: [IDs]
Overrides: [none / list with justification]
Sign-off: [one sentence summary]
```

---

## EXPIRY WATCH

Open this section at the start of each audit cycle.

**Version cycle definition:** One completed multi-agent audit pass with findings logged.
**Expiry check owner:** Skeptic/Auditor role, at cycle opening.
**Status: ACTIVE at v1.0** — check global index for entries approaching two cycles.

*(No entries past two cycles at v1.0.)*

---

## SIDECAR ID REFERENCE

Unknowns now use local IDs in owning file sidecars. Cross-module unknowns are indexed here.

| Prefix | Owning File |
|---|---|
| EV- | `energy_v0.md` |
| LT- | `leviathan_testing.md` |
| FL- | `Lazarus_forge_v0_flow.md` |
| TS- | `Component_Triage_System.md` |
| CO- | `Components.md` |
| EC- | `Ethical_Constraints.md` |
| AP- | `Auditor_Protocols.md` |
| SC- | `Spin_Chamber_v0.md` |
| AS- | `Air_Scrubber_v0.md` |
| SR- | `Support_Raft_v0.md` |
| GK- | `geck_forge_seed.md` |
| ST- | `Ship_of_Theseus_Right_to_Repair.md` |
| EL- | `Electronics.md` |
| CF- | `Cognitive_Frameworks.md` |
| TR- | `Trajectories_LF.md` |

---

## ACTIVE UNKNOWNS INDEX

*Full entry detail in owning file sidecars. Full registry: `Unknowns_LF.md`*

### Energy & Power

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| EV-001 | Forge power demand uncharacterized | `energy_v0.md` | In Progress | Blocking |
| LT-001 | Leviathan power envelope | `leviathan_testing.md` | Open | Blocking |
| LT-002 | Deep-ocean storage degradation | `leviathan_testing.md` | Open | Blocking |

### Leviathan / Autonomy

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| LT-003 | Autonomy architecture unspecified | `leviathan_testing.md` | Open | Blocking |
| LT-004 | Trust model mechanism undefined | `leviathan_testing.md` | Open | Blocking |
| LT-005 | Priority propagation — no mechanism | `leviathan_testing.md` | Open | Blocking |
| LT-006 | Ethical log survival at depth | `leviathan_testing.md` | Open | Non-blocking |

### Gate Logic & Triage

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| FL-001 | Gate logic determinism | `Lazarus_forge_v0_flow.md` | In Progress | Blocking |
| TS-001 | "Sufficient for forge duty" threshold | `Component_Triage_System.md` | In Progress | Blocking |
| TS-002 | Contamination routing protocol | `Component_Triage_System.md` | Open | Blocking |
| CO-001 | Graduation Rule detection circularity | `Components.md` | In Progress | Blocking |

### Ethics & Governance

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| EC-001 | "Sufficient confidence" threshold | `Ethical_Constraints.md` | Open | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Ethical_Constraints.md` | Open | Blocking |
| EC-003 | Human escalation path | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-004 | Governance failure modes | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Ethical_Constraints.md` | In Progress | Blocking |
| EC-006 | Ethical log survival under unit loss | `Ethical_Constraints.md` | Open | Non-blocking |
| EC-007 | Governance fail-safe | `Ethical_Constraints.md` | In Progress | Blocking |

### Governance & Verification

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| AP-001 | Auditor effectiveness metrics | `Auditor_Protocols.md` | Open | Blocking |
| AP-002 | Override vs. immutability boundary | `Auditor_Protocols.md` | In Progress | Blocking |
| AP-003 | Audit trail schema | `Auditor_Protocols.md` | Open | Blocking |

### Cognition

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| CF-001 | Hardware watchdog minimum standard | `Cognitive_Frameworks.md` | Open | High |
| CF-002 | Correlated AI failure modes | `Cognitive_Frameworks.md` | Open | High |
| CF-003 | Identity continuity during split-brain | `Cognitive_Frameworks.md` | Open | Medium |

### Hardware Modules

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| SC-001 | RPM envelope not validated | `Spin_Chamber_v0.md` | Open | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Spin_Chamber_v0.md` | Open | Blocking |
| AS-001 | 500W power budget not validated | `Air_Scrubber_v0.md` | Open | Medium |
| AS-003 | Scrubber waste stream and saturation | `Air_Scrubber_v0.md` | In Progress | Medium |
| SR-001 | Galvanic corrosion mitigation | `Support_Raft_v0.md` | Open | High |
| SR-002 | Sacrificial shell material selection | `Support_Raft_v0.md` | Open | Medium |

### Salvage & Fabrication

| ID | Title | Owning File | Status | Priority |
|---|---|---|---|---|
| GK-002 | Sacrificial anode material | `geck_forge_seed.md` | Open | Medium |
| ST-003 | Legal applicability by jurisdiction | `Ship_of_Theseus_Right_to_Repair.md` | Open | Medium |
| EL-001 | Forge-Standard interface spec | `Electronics.md` | Open | Medium |
| EL-003 | TMR voter implementation | `Electronics.md` | Open | Medium |
| TR-001 | v1 profitability baseline | `Trajectories_LF.md` | Open | Blocking |

---

## DEPENDENCY MAP (condensed)

```
EV-001 -> LT-001 -> LT-003 -> LT-004 / LT-005
LT-002 -> feeds LT-001 (parallel)
CO-001 -> feeds FL-001
TS-001 -> feeds FL-001
EC-001 -> LT-003 / EC-007
EC-004 -> EC-007
CF-001 -> Electronics.md (watchdog design)
CF-003 -> Ship_of_Theseus_Right_to_Repair.md (identity continuity)
TR-001 -> depends on EV-001
EL-001 -> depends on LT-001
AP-001 -> AP-003 (metrics need schema first)
```

*Full map: `Unknowns_LF.md` §Dependency Map*

---

## HOW TO USE THIS FILE

**In Colab Cell 2:**
```python
FILES = [
    "[document_to_audit]",
    "Forge_Audit_Kit.md",     # ~10k chars
]
```

**When to load full files instead:**
- Auditing `Auditor_Protocols.md` itself → load `Auditor_Protocols.md`
- Auditing `Unknowns_LF.md` itself → load `Unknowns_LF.md`
- Onboarding a new agent → load both full files
- Need full unknown entry detail → load owning file or `Unknowns_LF.md`

**Confirmed files in repository** (per `Discovery.md`):
README.md, Lazarus_forge_v0_flow.md, Trajectories_LF.md, Ethical_Constraints.md, Auditor_Protocols.md, Forge_Audit_Kit.md, Unknowns_LF.md, Cognitive_Frameworks.md, Component_Triage_System.md, Components.md, Electronics.md, geck_forge_seed.md, energy_v0.md, Spin_Chamber_v0.md, Material_Separation_Gate_v0.md, Air_Scrubber_v0.md, Support_Raft_v0.md, Ship_of_Theseus_Right_to_Repair.md, leviathan_testing.md, File_Template.md, AUDIT_HARNESS.py

**Maintenance:** Update when `Unknowns_LF.md` version increments — update active unknowns tables, sidecar ID reference, version header, and Expiry Watch note. Fallacy Checklist, Gates, and Rules only change when `Auditor_Protocols.md` is revised.

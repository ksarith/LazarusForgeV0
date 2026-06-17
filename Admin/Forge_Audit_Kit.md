# Forge_Audit_Kit.md
**Version 1.0**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Last Audit       | 2026-06-16                                                          |
| Auditor          | Claude — Synthesizer                                                |
| Open Unknowns    | 4                                                                   |
| Highest Risk     | Medium                                                              |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.7 | `Unknowns.md` v3.3 | `Admin/Repository_Integrity_Protocol.md` v0.1 | `Admin/Security_Protocols.md` v0.2 | `Admin/Canonical_Terms.md` v0.2

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Audit opening checklist · Governing principles summary · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Anti-Theater doctrine · Fallacy checklist stubs · AI contribution rules stubs · Verification gates · Sign-off format · Active unknowns index (Critical and Blocking only) · Sidecar ID reference · Dependency map (condensed)

**DOES NOT define:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`) · Full Adversarial Battery (→ `Admin/Auditor_Protocols.md`) · Full unknown detail (→ owning sidecars) · Full unknown registry (→ `Unknowns.md`) · Constitutional hierarchy (→ `Admin/Governance_Charter.md`) · Ethical policy (→ `Admin/Ethical_Constraints.md`) · Canonical vocabulary (→ `Admin/Canonical_Terms.md`)

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`
> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`
> Verification seeks sufficient falsifiability, not exhaustive certainty.
> The kit must remain small enough to be useful.

Infinite audit recursion is a governance failure mode. Human override applies to process decisions only — not to `Admin/Ethical_Constraints.md` hard floors. Sidecar Model: module unknowns live in each file's footer. Index below is cross-module summary — Critical and Blocking only.

---

## Verification Maturity Model

Exploration → Candidate Spec → Provisional Spec → Operational Spec → Hardened Doctrine. Promotion rule: assumptions narrow, unknowns shrink, external validation expands.

---

## Truth Provenance Labels

**Quantitative:** Measured | Estimated | Analogous | Placeholder — Unlabeled = Placeholder.
**Institutional:** Internally Derived | Analogous External | Experimentally Verified | Operationally Hardened. No internally-derived claim may be represented as operationally hardened without external validation.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high: Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure | Governance Authority. Partial Battery allowed for Exploration-stage if deferred classes are documented and no safety-critical claims are present.

---

## Anti-Theater Doctrine

Target: plausible failure pathways, energy-bearing systems, historically observed failures, governance exploitability, hidden coupling, silent corruption. Weak findings: rhetorical edge cases, unconstrained hypotheticals, impossible-state speculation without operational consequence.

---

## Audit Opening Checklist

Execute before every document review.

**1. Tier 1 Axiom Verification** — Confirm all eight axioms (P-1–P-4, Q-1–Q-4) match prior committed version in `Admin/Governance_Charter.md`. Any unratified wording change = Constitutional violation → STATE_HOLD immediately.

**2. Expiry Watch** — Check `Unknowns.md` for Blocking entries approaching two-cycle threshold. Escalate to Systemic Risk or demote dependent module.

Current watch (v3.3): EC cluster approaching threshold · GOV-003 / GOV-005 Critical, no fast path · RIP-001 Critical, GitHub releases are v0 resolution path · CF-001 In Progress, hardware prototype required · SEC-007 Critical, above-repository architectural decision required · TF-006 Ethical_Constraints escalation candidate — expansion halts if non-target insect capture unbounded.

**3. Semantic Stability Check** — Scan for high-drift-risk terms. Flag as [FALLACY 4 — Semantic Drift]. Route to `Admin/Canonical_Terms.md`.

| Term | Risk |
|------|------|
| Recycling | Use Value Preservation or Material Recovery |
| Autonomous Decision-Making (unbound) | Obscures Axiom P-4 override visibility |
| High-RPM (on Gate_04) | Terminology bleed from Gate_05 |
| Canonical (unqualified) | Five distinct usages |
| Safe / Contained / Stable / Sufficient | Context-dependent — tighten or log |
| Scrap | Conflates material states |
| Specification (on Exploration content) | Implicit promotion |

---

## Fallacy Checklist

Substantive notes required — bare checkmarks are not verification. Full text: `Admin/Auditor_Protocols.md`.

1. **Magic Energy** — Every watt needs a traceable origin. Cross-ref `Operations/Energy.md`.
2. **Friction Blindness** — Real systems degrade. Account for losses and wear.
3. **Energy Density Paradox** — Does recovery cost more than it produces?
4. **Semantic Drift** — Terms must match across all files and sessions. Route conflicts to `Admin/Canonical_Terms.md`.
5. **Scope Creep** — New capabilities belong in `Admin/Trajectories.md`.
6. **Hallucinated Files** — All cross-references must resolve against `Discovery.md`. Aspirational = labeled *planned*.
7. **Confidence Without Basis** — Label all numbers. Unlabeled = Placeholder.
8. **Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life.
9. **Incomplete by Omission** — What critical subsystem is missing?
10. **The Turd Problem** — Strip to one falsifiable sentence. Do not rename this.

---

## AI Contribution Rules

Role declaration required: *"Operating as [Role] per Auditor_Protocols.md v0.7"*
Valid roles: Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

1. No Invented Files — confirm against `Discovery.md`.
2. Role Declaration — declare before contributing; declare shifts before proceeding.
3. Lineage Tracking — note what changed, why, what it replaces.
4. Refusal is Valid — flag flawed premises; do not refine them.
5. Confidence Labeling — four-label system. Unlabeled = Placeholder.
6. Inter-Agent Consistency — open with Assumption Extraction.
7. Repository Structure Awareness — use canonical folder-prefixed paths.

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass by different agent to override.

| Gate | Test | Fail → |
|------|------|--------|
| G1 | Fallacy Checklist actively applied with substantive notes? | Return to author |
| G2 | Physical plausibility — no violation of known constraints? | Return for revision |
| G3 | Adversarial Battery applied proportional to coupling/risk? | Return for adversarial analysis |
| G4 | Scope alignment — fits current version or trajectory? | Route to `Admin/Trajectories.md` |
| G5 | Cross-reference integrity — all paths use canonical folder-prefixed names? | Hold at draft |
| G6 | Conflict check — no contradiction with existing committed specs? | Resolve before committing |

**Full Stop Review triggers:** Same claim blocked across two cycles · New finding invalidates core premise of a promoted spec · Pattern of overrides eroding a governance principle · Multiple Adversarial Battery findings converging on the same structural gap.

---

## Sign-Off Format

```
Document: [filename] ([status] audit, [date])
Auditor: [Role] — [Agent]
Verification maturity: [state]
Truth basis: [provenance level]
Adversarial classes applied: [list]
Adversarial classes deferred: [list + reason]
Highest-risk finding: [one sentence]
Gates cleared: [list]
Gates blocked: [list with reason]
Unknowns logged: [IDs]
Overrides: [none / list with justification]
Sign-off: [one sentence summary]
```

---

## Sidecar ID Reference

| Prefix | Owning File | Prefix | Owning File |
|--------|-------------|--------|-------------|
| AP-  | `Admin/Auditor_Protocols.md` | ME-  | `Architecture/Mechanical_Structures.md` |
| AS-  | `Operations/Air_Scrubber.md` | MG-  | `Operations/Gate_04_Separation_Mechanical.md` |
| BF-  | `Challenges/Biofouling.md` | PL-  | `Operations/Plastics.md` |
| CE-  | `Architecture/Chemistry.md` | PO-  | `Challenges/Planned_Obsolescence.md` |
| CF-  | `Architecture/Cognitive_Frameworks.md` | PR-  | `Architecture/Precision.md` |
| CM-  | `Challenges/Critical_Minerals.md` | RIP- | `Admin/Repository_Integrity_Protocol.md` |
| CO-  | `Architecture/Components.md` | RS-  | `Admin/Repository_Structure.md` |
| CT-  | `Admin/Canonical_Terms.md` | SC-  | `Operations/Gate_05_Separation_Thermal.md` |
| EC-  | `Admin/Ethical_Constraints.md` | SD-  | `Tests/Solar_Descent.md` |
| EL-  | `Operations/Electronics.md` | SEC- | `Admin/Security_Protocols.md` |
| EM-  | `Challenges/Emergence.md` | SP-  | `Admin/Safety_Protocols.md` |
| EN-  | `Architecture/Engineering.md` | SR-  | `Tests/Support_Raft.md` |
| EP-  | `Admin/Engineer_Protocols.md` | ST-  | `Admin/Ship_of_Theseus.md` |
| EV-  | `Operations/Energy.md` | TF-  | `Tests/Trophic_Forge.md` |
| FA-  | `Architecture/Facilities.md` | TH-  | `Architecture/Thermal_Systems.md` |
| FAK- | `Admin/Forge_Audit_Kit.md` | TR-  | `Admin/Trajectories.md` |
| FD-  | `Architecture/Friction_Dynamics.md` | TS-  | `Operations/Gate_02_Triage.md` |
| FL-  | `Architecture/Forge_flow.md` | UNK- | `Unknowns.md` (cross-module) |
| FN-  | `Architecture/Forge_Net.md` | VG-  | `Admin/Verification_Gates_LF.md` |
| GF-  | `Operations/Gate_06_Fabrication.md` | WA-  | `Challenges/Waste.md` |
| GI-  | `Operations/Gate_01_Intake.md` | WW-  | `Operations/Woodworking.md` |
| GK-  | `Architecture/Geck_forge_seed.md` | GM-  | `Admin/Governance_Migration_Protocol.md` |
| GOV- | `Admin/Governance_Charter.md` | GR-  | `Operations/Gate_03_Reduction.md` |
| GU-  | `Operations/Gate_07_Utilization.md` | LT-  | `Tests/Leviathan_testing.md` |
| LW-  | `Tests/Living_Waters.md` | | |

*Legacy flat filenames are aliases — resolve via Discovery.md Rename Registry.*

---

## Active Unknowns Index

*Critical and Blocking only. Full registry: `Unknowns.md` v3.3*

### Safety-Critical (Pre-Operational Blockers)

| ID | Title | Owning File | Status |
|----|-------|-------------|--------|
| LW-UNK-001 | Volatile co-distillation — distillate may be concentrated toxin; blocks potable output claim | `Tests/Living_Waters.md` | Open |
| LW-UNK-003 | LW-003 lumen implosion at 500 m — salvage tubing will fail at 4.9 MPa | `Tests/Living_Waters.md` | Open |
| CE-003 | Field polymer ID unreliable — false negative produces HCl/dioxins | `Architecture/Chemistry.md` | Open |
| PL-001 | Halogenated polymer contamination — blocks first hot pyrolysis run | `Operations/Plastics.md` | Open |
| GI-002 | Energetic material discharge doctrine undefined | `Operations/Gate_01_Intake.md` | Open |
| EL-005 | Toxic dust and BFR emission profile undefined | `Operations/Electronics.md` | Open |
| GF-007 | Fire suppression and hot-work doctrine undefined | `Operations/Gate_06_Fabrication.md` | Open |
| WA-002 | Hazardous fraction ID reliability — blocks mixed-waste operations | `Challenges/Waste.md` | Open |
| SD-UNK-004 | Host geology fracturing threshold — blocks excavation | `Tests/Solar_Descent.md` | Open |
| FA-001 | Site unconfirmed — blocks all hot operations | `Architecture/Facilities.md` | Open |

### Governance / Constitutional

| ID | Title | Owning File | Status |
|----|-------|-------------|--------|
| SEC-007 | External root-of-trust undefined — circular self-certification risk | `Admin/Security_Protocols.md` | Open |
| GOV-003 | Integrity enforcement architecture undefined | `Admin/Governance_Charter.md` | In Progress |
| GOV-005 | Long-term constitutional stability unproven | `Admin/Governance_Charter.md` | Open |
| EM-004 | Governance substrate integrity under emergent agent access | `Challenges/Emergence.md` | Open |
| RIP-001 | Prior-state archival not established — GitHub releases are v0 path | `Admin/Repository_Integrity_Protocol.md` | Open |
| UNK-009 | External root-of-trust cross-module — spans GOV-003, GOV-005, RIP-001, SEC-007 | Cross-module | Open |

### Autonomy / Structural

| ID | Title | Owning File | Status |
|----|-------|-------------|--------|
| CF-001 | Hardware watchdog — τ=50ms defined; Blocking until hardware prototype validates | `Architecture/Cognitive_Frameworks.md` | In Progress |
| EN-001 | Validated safety factors for salvaged materials — blocks all structural spec promotion | `Architecture/Engineering.md` | Open |
| PR-001 | Precision ceiling undeclared — blocks T1/T2 part claims | `Architecture/Precision.md` | Open |

### Operational Blockers

| ID | Title | Owning File | Status |
|----|-------|-------------|--------|
| FL-001 | Gate logic determinism | `Architecture/Forge_flow.md` | In Progress |
| EV-001 | Forge power demand uncharacterized | `Operations/Energy.md` | In Progress |
| TH-003 | Atmospheric moisture yield — blocks Living Waters deployment | `Architecture/Thermal_Systems.md` | Open |
| CM-002 | Acid leach reagent recovery — blocks hydrometallurgical processing | `Challenges/Critical_Minerals.md` | Open |
| TF-006 | Non-target insect capture — Ethical_Constraints escalation candidate | `Tests/Trophic_Forge.md` | Open |
| FN-001 | Data validation criteria — blocks first network connection | `Architecture/Forge_Net.md` | Open |
| FN-005 | Data privacy and access control — blocks first network connection | `Architecture/Forge_Net.md` | Open |

---

## Dependency Map (Condensed)

```
EV-001 -> LT-001 -> LT-003 -> LT-004 / LT-005
CO-001 -> FL-001 <- TS-001 / TS-002 / TS-003
EC-001 -> LT-003 / EC-007
RIP-001 -> blocks Phase 2 automation
SEC-007 -> GMP-004 (Track B amendment attack vector)
CF-001 -> EM-001 (watchdog validation prerequisite)
EN-001 -> blocks all structural spec promotion
CE-003 -> PL-001 (polymer ID prerequisite for pyrolysis)
TH-003 -> LW deployment
LW-UNK-001 -> blocks potable output claim in LW-001
SD-UNK-004 -> blocks excavation
GI-002 -> blocks first Intake run
FN-001 / FN-005 -> block first network connection
FA-001 -> blocks hot operations
```

*Full map: `Unknowns.md` §Dependency Map*

---

## Drift Indicators

Mandatory re-audit conditions:

- Unknowns index diverges from `Unknowns.md` without documented reason
- Derivation statement references a superseded `Unknowns.md` version
- Sidecar ID reference missing prefixes present in `Unknowns.md`
- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- Expiry Watch not updated at `Unknowns.md` version increment
- Kit character count exceeds 20,000 — flag for reduction pass (threshold scales with repository; see FAK-003)
- Ethical Anchor absent or altered
- Kit version references a superseded `Auditor_Protocols.md` version

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

**FAK-001** — Kit version maintenance trigger not formally owned. Resolution Path: maintenance trigger added to scope boundary (v1.0). Formal ownership assignment still needed. Status: Open.

**FAK-003** — Kit size as governed constraint. Ceiling revised from 12,000 to 20,000 chars in v1.0 — original threshold predated repository reaching 50+ sidecar prefixes and 25+ critical unknowns. Sidecar table + unknowns index alone consume ~5,700 chars at current scale. 20,000 provides working margin without the bloat risk the original ceiling was designed to prevent. v1.0 actual: ~17,000 chars. Status: Resolved.

**FAK-004** — Index triage policy not formally ratified. v1.0 adopts Critical and Blocking as threshold. Resolution Path: ratify in next audit cycle. Status: Open.

### Resolution Log

- v0.7: Verification Maturity Model, Truth Provenance, Anti-Theater, adversarial weighting, sign-off format added.
- v0.8: Audit Opening Checklist Steps 1–2 added. RIP cluster added. Derivation → Unknowns.md v1.8.
- v0.9: Reduction pass. Kit size as first-class constraint. Semantic Stability Check added. Fallacy 4 routing expanded. SEC-, CT-, PL- prefixes added.
- v1.0: Reduction pass (31k → 17k chars). Ceiling revised 12k → 20k (FAK-003 resolved — threshold predated current sidecar/unknowns scale). Derivation → Unknowns.md v3.3. Sidecar ID expanded (BF-, CM-, EM-, EN-, EP-, FA-, FD-, GM-, LW-, ME-, PO-, PR-, RS-, SD-, SP-, TF-, TH-, VG-, WA-, WW- added). Resolved entries removed from index. New critical clusters added (LW, SD, TF, EM, CE, WA, CM). Expiry Watch updated to v3.3 state. Fallacy checklist compressed to single-line stubs. FAK-002 resolved and removed. FAK-004 logged.


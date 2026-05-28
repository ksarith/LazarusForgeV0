# Forge_Audit_Kit.md
**Version 0.9**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-27                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 6                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Audit opening checklist (Tier 1 Axiom verification + Expiry Watch +
  Semantic Stability Check)
- Governing principles summary
- Verification Maturity Model
- Truth Provenance label system
- Adversarial priority weighting criteria
- Anti-Theater doctrine
- Fallacy checklist (condensed)
- AI contribution rules (condensed)
- Verification gates (condensed)
- Sign-off format
- Active unknowns index (cross-module, summary only)
- Sidecar ID reference
- Dependency map (condensed)
- Semantic Stability Check — audit opening vocabulary verification step
  cross-referencing `Admin/Canonical_Terms.md` as resolution authority

**This file DOES NOT define:**
- Full auditor role class doctrine (→ `Admin/Auditor_Protocols.md`)
- Full audit sequencing and phase logic (→ `Admin/Auditor_Protocols.md`)
- Full Adversarial Challenge Battery (→ `Admin/Auditor_Protocols.md`)
- Full unknown entry detail (→ owning file sidecars)
- Full cross-module unknown registry (→ `Unknowns.md`)
- Constitutional governance hierarchy (→ `Admin/Governance_Charter.md`)
- Ethical policy (→ `Admin/Ethical_Constraints.md`)
- Canonical vocabulary authority (→ `Admin/Canonical_Terms.md`)
- Engineering specifications

---

## File Purpose

Lightweight operational audit substrate for routine LazarusForgeV0
multi-agent verification cycles. Load this instead of the full governance
corpus to stay within token limits. When this file contradicts a full
source document, the full source document prevails.

**Derived from:** `Admin/Auditor_Protocols.md` v0.7 | `Unknowns.md` v1.8
| `Admin/Repository_Integrity_Protocol.md` v0.1
| `Admin/Security_Protocols.md` v0.2
| `Admin/Canonical_Terms.md` v0.2

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`

> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`

> Verification seeks sufficient falsifiability, not exhaustive certainty.

**Infinite audit recursion is a governance failure mode.**

Human override rights apply to verification process decisions only — not
to hard-line doctrines in `Admin/Ethical_Constraints.md`.

Sidecar Model: module unknowns live in each file's footer sidecar.
The unknowns index below is cross-module summary only.

---

## Verification Maturity Model

| State                     | Operational Status         |
|---------------------------|----------------------------|
| Exploration               | Not operational            |
| Candidate Specification   | Internal review only       |
| Provisional Specification | Limited operational use    |
| Operational Specification | Deployable                 |
| Hardened Doctrine         | Trusted baseline           |

Promotion rule: assumptions narrow, unknowns shrink, external validation
expands.

---

## Truth Provenance Labels

**Quantitative claims:**
Measured | Estimated | Analogous | Placeholder — Unlabeled = Placeholder.

**Institutional claims:**
Internally Derived | Analogous External | Experimentally Verified |
Operationally Hardened

No internally-derived claim may be represented as operationally hardened
without external validation.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high:
Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure |
Governance Authority

Partial Battery allowed for Exploration-stage if deferred classes are
documented and no safety-critical claims are present.

---

## Anti-Theater Doctrine

Findings should target: plausible failure pathways, energy-bearing systems,
historically observed failures, governance exploitability, hidden coupling,
silent corruption.

Weak findings: rhetorical edge cases, unconstrained hypotheticals,
impossible-state speculation, adversarial narratives without operational
consequence.

---

## Audit Opening Checklist

Execute before every document review. Do not skip steps.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1 through P-4, Q-1 through Q-4) are present
in `Admin/Governance_Charter.md` with text matching the prior committed
version. Any unratified wording change is a Constitutional violation —
invoke STATE_HOLD immediately.
*Ref: `Admin/Repository_Integrity_Protocol.md` §Protected Elements*

**2. Expiry Watch**
Check `Unknowns.md` for Blocking or Non-blocking entries approaching
two-cycle threshold without a documented Resolution Path. Escalate to
Systemic Risk or demote dependent module.

**Current watch (v1.8):** FL-001 and several EC entries approaching
threshold. GOV-003 and GOV-005 Critical. RIP-001 Critical — GitHub
releases are the v0 resolution path.

**3. Semantic Stability Check**
Scan the document under audit for high-drift-risk terms. Flag violations
as [FALLACY 4 — Semantic Drift]. Route resolution to `Admin/Canonical_Terms.md`.

| Term | Drift Risk | Resolution |
|------|------------|------------|
| Recycling | Use Value Preservation or Material Recovery | `Admin/Canonical_Terms.md` §Anti-Drift |
| Autonomous Decision-Making (unbound) | Obscures Axiom P-4 override visibility | `Admin/Canonical_Terms.md` §Anti-Drift |
| High-RPM (applied to Gate_04) | Terminology bleed from Gate_05 | `Admin/Canonical_Terms.md` §Operational Flow |
| Canonical (unqualified) | Five distinct usages | `Admin/Canonical_Terms.md` §Disambiguation |
| Safe / Contained / Stable / Sufficient | Context-dependent; interpret differently | Tighten or log per Challenge Class 4 |
| Scrap | Conflates material states | `Admin/Canonical_Terms.md` §Anti-Drift |
| Specification (on Exploration content) | Implicit promotion | `Admin/Auditor_Protocols.md` §Exploration vs. Spec |

Term conflict between files: route to `Admin/Canonical_Terms.md` unless
operational routing (→ `Architecture/Forge_flow.md`) or tier definitions
(→ `Admin/Governance_Charter.md`).

**Version cycle:** One completed multi-agent audit pass with findings logged.

---

## Fallacy Checklist

Substantive notes required — bare checkmarks are not verification.

**1. Magic Energy** — Every watt needs a traceable origin.
Cross-ref `Operations/Energy.md`.

**2. Friction Blindness** — Account for resistance, thermal losses, wear.
Real systems degrade.

**3. Energy Density Paradox** — Does a recovery step cost more than it
produces? Justify or flag.

**4. Semantic Drift** — Terms must mean the same thing across all files
and agent sessions. Primary detection: Semantic Stability Check (Step 3
above). Routing: operational vocabulary → `Architecture/Forge_flow.md`;
cross-file consistency → `Admin/Canonical_Terms.md`; tier vocabulary →
`Admin/Governance_Charter.md`. Conflicts logged as Active Disputes in
`Admin/Canonical_Terms.md` — never silently resolved.

**5. Scope Creep** — New capabilities belong in `Admin/Trajectories.md`.

**6. Hallucinated Files** — All cross-references must resolve. Files in
`Discovery.md` are verified. Aspirational references must be labeled *planned*.

**7. Confidence Without Basis** — Label all numbers: Measured / Estimated
/ Analogous / Placeholder. Unlabeled = Placeholder.

**8. Lifecycle Truncation** — Every module spec needs: Degraded Operation,
Failure Modes, Maintenance Access, End-of-Life path.

**9. Incomplete by Omission** — What critical subsystem is missing? Heat
dissipation, waste streams, power draw, human interface?

**10. The Turd Problem** — Strip to one falsifiable sentence. Does the
foundation survive adversarial reduction? Do not rename this.

---

## AI Contribution Rules

Role declaration required: *"Operating as [Role] per Auditor_Protocols.md v0.7"*

Valid roles: Skeptic/Auditor | Systems/Auditor | Evidence/Auditor |
Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

1. No Invented Files — confirm against `Discovery.md`.
2. Role Declaration — declare before contributing; declare shifts before proceeding.
3. Lineage Tracking — note what changed, why, what it replaces.
4. Refusal is Valid — flag flawed premises; do not refine them.
5. Confidence Labeling — four-label system. Unlabeled = Placeholder.
6. Inter-Agent Consistency — open with Assumption Extraction.
7. Repository Structure Awareness — use canonical folder-prefixed paths.

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not
permitted. Blocks require documented rebuttal and second-pass by a different
agent to override.

| Gate | Test | Fail → |
|------|------|--------|
| G1 | Fallacy Checklist actively applied with substantive notes? | Return to author |
| G2 | Physical plausibility — no violation of known constraints? | Return for revision |
| G3 | Adversarial Challenge Battery applied proportional to coupling/risk? | Return for adversarial analysis |
| G4 | Scope alignment — fits current version or trajectory? | Route to `Admin/Trajectories.md` |
| G5 | Cross-reference integrity — all paths resolve using canonical folder-prefixed names? | Hold at draft |
| G6 | Conflict check — no contradiction with existing committed specs? | Resolve before committing |

**Full Stop Review triggers:**
1. Same foundational claim blocked across two audit cycles
2. New finding invalidates core premise of a promoted specification
3. Pattern of overrides eroding a governance principle without explicit revision
4. Multiple Adversarial Battery findings converging on the same structural gap

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

| Prefix | Owning File |
|--------|-------------|
| EV-  | `Operations/Energy.md` |
| LT-  | `Tests/Leviathan_testing.md` |
| FL-  | `Architecture/Forge_flow.md` |
| TS-  | `Operations/Gate_02_Triage.md` |
| CO-  | `Architecture/Components.md` |
| EC-  | `Admin/Ethical_Constraints.md` |
| AP-  | `Admin/Auditor_Protocols.md` |
| GOV- | `Admin/Governance_Charter.md` |
| SC-  | `Operations/Gate_05_Separation_Thermal.md` |
| MG-  | `Operations/Gate_04_Separation_Mechanical.md` |
| AS-  | `Operations/Air_Scrubber.md` |
| SR-  | `Tests/Support_Raft.md` |
| GK-  | `Architecture/Geck_forge_seed.md` |
| ST-  | `Admin/Ship_of_Theseus.md` |
| EL-  | `Operations/Electronics.md` |
| CF-  | `Architecture/Cognitive_Frameworks.md` |
| TR-  | `Admin/Trajectories.md` |
| GI-  | `Operations/Gate_01_Intake.md` |
| GR-  | `Operations/Gate_03_Reduction.md` |
| GF-  | `Operations/Gate_06_Fabrication.md` |
| GU-  | `Operations/Gate_07_Utilization.md` |
| RIP- | `Admin/Repository_Integrity_Protocol.md` |
| FN-  | `Architecture/Forge_Net.md` |
| SEC- | `Admin/Security_Protocols.md` |
| CT-  | `Admin/Canonical_Terms.md` |
| PL-  | `Operations/Plastics.md` |

*Legacy flat filenames are aliases — resolve via Discovery.md Rename Registry.*

---

## Active Unknowns Index

*Cross-module summary only. Full entry detail in owning file sidecars.
Full registry: `Unknowns.md` v1.8*

### Energy & Power
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| EV-001 | Forge power demand uncharacterized | `Operations/Energy.md` | In Progress | Blocking |

### Leviathan / Autonomy
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| LT-001 | Power envelope — no placeholder anchor | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-002 | Deep-ocean storage degradation | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-003 | Autonomy architecture unspecified | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-004 | Trust model mechanism undefined | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-005 | Priority propagation — no mechanism | `Tests/Leviathan_testing.md` | Open | Blocking |
| LT-006 | Ethical log survival at depth | `Tests/Leviathan_testing.md` | Open | Non-blocking |

### Gate Logic & Triage
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| FL-001 | Gate logic determinism | `Architecture/Forge_flow.md` | In Progress | Blocking |
| TS-001 | "Sufficient for forge duty" threshold | `Operations/Gate_02_Triage.md` | In Progress | Blocking |
| TS-002 | Contamination routing protocol | `Operations/Gate_02_Triage.md` | Open | Blocking |
| TS-003 | Gate determinism (downstream) | `Operations/Gate_02_Triage.md` | In Progress | Blocking |
| CO-001 | Graduation Rule detection circularity | `Architecture/Components.md` | In Progress | Blocking |

### Ethics & Governance
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| EC-001 | "Sufficient confidence" threshold | `Admin/Ethical_Constraints.md` | Open | Blocking |
| EC-002 | Anti-Weaponization pattern-matching | `Admin/Ethical_Constraints.md` | Open | Blocking |
| EC-003 | Human escalation path | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-004 | Governance failure modes lifecycle | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-005 | Life-preservation vs. Anti-Weaponization | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| EC-006 | Ethical log survival under unit loss | `Admin/Ethical_Constraints.md` | Open | Non-blocking |
| EC-007 | Governance fail-safe | `Admin/Ethical_Constraints.md` | In Progress | Blocking |
| GOV-001 | Governance migration mechanics | `Admin/Governance_Charter.md` | Open | Major |
| GOV-002 | Provenance operationalization | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-003 | Integrity enforcement architecture | `Admin/Governance_Charter.md` | In Progress | Critical |
| GOV-004 | Escalation calibration | `Admin/Governance_Charter.md` | Open | Major |
| GOV-005 | Long-term constitutional stability | `Admin/Governance_Charter.md` | Open | Critical |
| GOV-006 | Human override authenticity | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-007 | Bootstrap governance initialization | `Admin/Governance_Charter.md` | In Progress | Major |
| GOV-008 | Minimum quorum for bootstrap compliance | `Admin/Governance_Charter.md` | Open | Major |
| GOV-009 | Bounded external resource consumption | `Admin/Governance_Charter.md` | Open | Major |

### Governance & Verification
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| AP-001 | Auditor effectiveness metrics | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-002 | Override vs. immutability boundary | `Admin/Auditor_Protocols.md` | In Progress | Major |
| AP-003 | Audit trail schema deferred | `Admin/Auditor_Protocols.md` | Open | Minor |
| AP-004 | Cross-auditor disagreement resolution | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-005 | Verification termination threshold | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-006 | Institutional truth provenance hierarchy | `Admin/Auditor_Protocols.md` | Open | Major |
| AP-007 | Repository integrity doctrine lineage | `Admin/Auditor_Protocols.md` | In Progress | Major |
| RIP-001 | Prior-state archival not established | `Admin/Repository_Integrity_Protocol.md` | Open | Critical |
| RIP-002 | AUDIT_HARNESS.py Phase 1 not implemented | `Admin/Repository_Integrity_Protocol.md` | Open | Major |
| RIP-003 | Violation incident log location undefined | `Admin/Repository_Integrity_Protocol.md` | Open | Major |
| RIP-004 | Constitutional violation detection latency | `Admin/Repository_Integrity_Protocol.md` | In Progress | Major |
| RIP-005 | Security_Protocols.md dependency | `Admin/Repository_Integrity_Protocol.md` | In Progress | Major |
| SEC-001 | Quorum recovery under terminal partition | `Admin/Security_Protocols.md` | Open | Major |
| SEC-002 | Key revocation doctrine undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-003 | Key rotation period undefined | `Admin/Security_Protocols.md` | Open | Major |
| CT-001 | Legacy script name mapping | `Admin/Canonical_Terms.md` | Open | Minor |
| CT-002 | Component Library schema undefined | `Admin/Canonical_Terms.md` | Open | Major |
| CT-003 | Dependency_Priority_Map.md needed | `Admin/Canonical_Terms.md` | Open | Minor |

### Hardware Modules
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| SC-001 | RPM envelope not validated | `Operations/Gate_05_Separation_Thermal.md` | In Progress | Blocking |
| SC-002 | Segregation effectiveness at v0 scale | `Operations/Gate_05_Separation_Thermal.md` | Open | Blocking |
| SC-005 | Drive system — dynamic imbalance | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| SC-006 | Siting requirements | `Operations/Gate_05_Separation_Thermal.md` | Open | Major |
| MG-002 | Optimal RPM bands not characterized | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-003 | Confidence threshold not validated | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| MG-007 | Rotor jam recovery undefined | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major |
| AS-001 | 500W power budget not validated | `Operations/Air_Scrubber.md` | Open | Medium |
| AS-003 | Scrubber waste stream and saturation | `Operations/Air_Scrubber.md` | In Progress | Medium |
| SR-001 | Galvanic corrosion mitigation | `Tests/Support_Raft.md` | Open | High |
| SR-002 | Sacrificial shell material selection | `Tests/Support_Raft.md` | Open | Medium |

### Salvage & Fabrication
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| EL-001 | Forge-Standard interface spec | `Operations/Electronics.md` | Open | Medium |
| EL-003 | TMR voter implementation | `Operations/Electronics.md` | Open | Medium |
| EL-005 | Toxic dust and BFR emission profile | `Operations/Electronics.md` | Open | Critical |
| EL-006 | Firmware trust validation | `Operations/Electronics.md` | Open | Critical |
| EL-007 | Correlated TMR failure modes | `Operations/Electronics.md` | Open | Major |
| EL-008 | Counterfeit component detection | `Operations/Electronics.md` | Open | Major |

### Reduction, Intake & Fabrication (Critical only)
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| GI-002 | Energetic material discharge doctrine | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-003 | Augmented hazard detection | `Operations/Gate_01_Intake.md` | Open | Critical |
| GI-007 | Digital contamination handling | `Operations/Gate_01_Intake.md` | Open | Critical |
| GR-002 | Reduction method not selected | `Operations/Gate_03_Reduction.md` | Open | Major |
| GR-003 | Biological/chemical waste disposal | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GR-007 | Equipment retirement threshold | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GF-007 | Fire suppression and hot-work doctrine | `Operations/Gate_06_Fabrication.md` | Open | Critical |
| PL-001 | Halogenated polymer contamination | `Operations/Plastics.md` | Open | Critical |
| PL-002 | Reactor over-pressurization | `Operations/Plastics.md` | Open | Major |

### Network
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| FN-001 | Data validation criteria | `Architecture/Forge_Net.md` | Open | Critical |
| FN-005 | Data privacy and access control | `Architecture/Forge_Net.md` | Open | Critical |

### Utilization
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| GU-001 | Performance metric schema | `Operations/Gate_07_Utilization.md` | Open | Major |
| GU-002 | Retirement handoff not cross-validated | `Operations/Gate_07_Utilization.md` | Open | Major |
| GU-004 | Silent failure detection | `Operations/Gate_07_Utilization.md` | Open | Major |

### Cross-Module
| ID | Title | Owning Files | Status | Priority |
|----|-------|--------------|--------|----------|
| UNK-006 | Master safety registry — rotating and thermal modules | SC-006, MG-006 | Open | Major |
| UNK-008 | Welding wire specification — no owner | SC-004 | Open | Major |

### Trajectory
| ID | Title | Owning File | Status | Priority |
|----|-------|-------------|--------|----------|
| TR-001 | v1 profitability baseline | `Admin/Trajectories.md` | Open | Blocking |

---

## Dependency Map (Condensed)

```
EV-001 -> LT-001 -> LT-003 -> LT-004 / LT-005
LT-002 -> feeds LT-001 (parallel)
CO-001 -> feeds FL-001
TS-001 / TS-002 / TS-003 -> feed FL-001
EC-001 -> LT-003 / EC-007
EC-004 -> EC-007
AP-005 -> EC-001
AP-006 -> FN-001 / CF-002
AP-007 -> GOV-003 (distinct but linked)
RIP-001 -> blocks Phase 2 automation
RIP-002 -> depends on RIP-001
RIP-004 -> In Progress — resolved by Audit Opening Checklist Step 1
RIP-005 -> In Progress — Security_Protocols.md v0.2 is executing path
SEC-001 -> GOV-008 (blocking dependency)
SEC-002 -> SEC-001 / GOV-006
SEC-003 -> SEC-002
CT-002 -> Operations/Gate_02_Triage.md (blocks Spec promotion)
CT-002 -> Architecture/Components.md (cross-validation required)
CT-003 -> discharge via Admin/Trajectories.md v0->v1 transition
GOV-006 -> In Progress — Security_Protocols.md v0.2 is executing path
GI-002 -> blocks first operational Intake run
GI-003 -> blocks first unsupervised Intake run
GI-007 -> depends on FN-001, Operations/Electronics.md
GR-002 -> unblocks GR-001, GR-004, GR-005, GR-006
GR-003 -> no owner — Critical gap
EL-005 -> feeds Air_Scrubber.md sizing
EL-006 -> prerequisite for first salvaged MCU integration
FN-001 -> blocks first network connection
FN-005 -> blocks first network connection
SC-001 -> SC-005
TR-001 -> depends on EV-001
PL-001 -> blocks first hot pyrolysis run
PL-002 -> blocks first hot pyrolysis run
```

*Full map: `Unknowns.md` §Dependency Map*

---

## How to Use This File

**Load in routine audit cycles:**
```
FILES = [
    "[document_to_audit]",
    "Admin/Forge_Audit_Kit.md",
]
```

**Load full source documents instead when:**
- Auditing `Admin/Auditor_Protocols.md` → load Auditor_Protocols.md
- Auditing `Unknowns.md` → load Unknowns.md
- Auditing `Admin/Governance_Charter.md` → load Governance_Charter.md
- Onboarding a new agent → load full governance corpus
- Full unknown entry detail needed → load owning file or Unknowns.md
- Full Adversarial Battery needed → load Auditor_Protocols.md

**Maintenance:** Update when Auditor_Protocols.md is revised or Unknowns.md
version increments. Fields to update: unknowns tables, sidecar ID reference,
version header, Expiry Watch note, dependency map.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review | Stale flat filenames in sidecar ID reference | References invalid after restructuring | Sidecar ID reference must use canonical folder-prefixed paths | Replicated | No |
| May 2026 | Audit Review | Kit without explicit derivation statement | Kit diverged from source without detection | Derivation relationship must be explicit | Replicated | No |
| May 2026 | Audit Review | Binary Specification/not-Specification model | Documents promoted before operational validation | Verification Maturity Model needed | Analogous | Yes |
| 2026-05-23 | Audit Review | Expiry Watch as sole audit opening check | Axiom text could be modified undetected | Axiom verification added as mandatory Step 1 | Analogous | Yes |
| 2026-05-27 | Audit Review | Fallacy 4 without named term watchlist | Drift caught reactively | Semantic Stability Check converts reactive detection to proactive | Analogous | Yes |
| 2026-05-27 | Audit Review | Kit allowed to grow without size constraint | Exceeded token budget; defeated its own purpose | Kit size is a first-class constraint — reduction is a governance action | Replicated | No |

---

## Active Disputes

| ID | Summary | Positions in Conflict | Risk | Status | Owner |
|----|---------|-----------------------|------|--------|-------|
| — | No active disputes | — | — | — | — |

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| May 2026 | Kit as standalone governance authority | Kit is derived — cannot outrank source | No |
| May 2026 | Single confidence label system without provenance | Insufficient — coherent docs mistaken for validated truth | No |
| 2026-05-27 | Kit growth without size constraint | Exceeded token budget; kit must remain lean to function | No |

---

## Drift Indicators

Mandatory re-audit conditions:

- Active unknowns index diverges from Unknowns.md without documented reason
- Sidecar ID reference contains stale or flat filenames
- Governing principles contradict `Admin/Auditor_Protocols.md`
- Verification gates diverge from `Admin/Auditor_Protocols.md`
- Sign-off format diverges from `Admin/Auditor_Protocols.md`
- Expiry Watch not updated at Unknowns.md version increment
- Kit character count exceeds 12,000 — flag for reduction pass
- Ethical Anchor field absent, altered, or does not match canonical string
- Kit version references a superseded version of Auditor_Protocols.md

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous
progression, escalate for human review.

---

## Auditor Notes & Unknowns

### FAK-001 — Kit version header maintenance discipline undefined

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Governance |
| Blocking | No |
| Owner | Admin/Forge_Audit_Kit.md |
| First Logged | 2026-05-23 |
| Last Reviewed | 2026-05-27 |

**Description:** No formal trigger or owner defined for updating the kit
when source documents are revised.

**Why It Matters:** Kit becomes stale guidance while appearing authoritative.

**Resolution Path:** Payment via Specification — add maintenance trigger
to Drift Indicators; assign update responsibility in How to Use section.

---

### FAK-002 — AP-005 through AP-007 not yet confirmed in Auditor_Protocols.md sidecar

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Governance |
| Blocking | No |
| Owner | Admin/Forge_Audit_Kit.md |
| First Logged | 2026-05-23 |
| Last Reviewed | 2026-05-27 |

**Description:** AP-005, AP-006, AP-007 introduced in kit but require
confirmation they exist in Auditor_Protocols.md sidecar and Unknowns.md.

**Why It Matters:** Orphaned references are cross-reference integrity
failures per Gate G5.

**Resolution Path:** Confirm AP-005 through AP-007 in both owning sidecar
and Unknowns.md at next audit cycle.

---

### FAK-003 — Kit size as governed constraint not yet formalized

| Field | Value |
|-------|-------|
| Status | Open |
| Risk | Medium |
| Priority | Major |
| Type | Governance |
| Blocking | No |
| Owner | Admin/Forge_Audit_Kit.md |
| First Logged | 2026-05-27 |
| Last Reviewed | 2026-05-27 |

**Description:** The kit has no formally defined maximum size. The 12,000
character threshold added to Drift Indicators is a first-pass constraint
but has not been validated against actual token budgets across model
contexts.

**Why It Matters:** A kit that exceeds token budget defeats its purpose.
Size must be a governed constraint with a defined ceiling, not an informal
preference.

**Resolution Path:** Payment via Specification — validate 12,000 character
threshold against observed token limits across at least two model contexts.
Adjust threshold and lock as a hard Drift Indicator.

---

### Resolution Log

- 2026-05-23: v0.7 — Verification Maturity Model, Truth Provenance Labels,
  Anti-Theater Doctrine, Confidence Decay/Revalidation, adversarial priority
  weighting, expanded sign-off format added.
- 2026-05-23: v0.8 — Audit Opening Checklist added (Steps 1 and 2).
  RIP- prefix and RIP-001 through RIP-005 added. Unknowns.md ref updated
  to v1.8. Derivation statement updated.
- 2026-05-27: v0.9 — Full reduction pass. Kit size treated as first-class
  constraint. Lessons Learned, Abandoned Paths, Active Disputes minimized.
  Verbose section explanations removed. Semantic Stability Check added as
  Audit Opening Checklist Step 3. Fallacy 4 expanded with routing doctrine.
  SEC- and CT- and PL- prefixes added to Sidecar ID Reference. SEC-001
  through SEC-003, CT-001 through CT-003, PL-001 and PL-002 added to
  unknowns index. GOV-008 and GOV-009 added. GOV-006 and RIP-005 updated
  to In Progress. Dependency map updated. FAK-003 logged — kit size as
  governed constraint. Drift Indicator added: kit character count exceeds
  12,000. Abandoned Path logged for unconstrained kit growth.

---

## Status

Version 0.9

**Derived from:** `Admin/Auditor_Protocols.md` v0.7 | `Unknowns.md` v1.8
| `Admin/Repository_Integrity_Protocol.md` v0.1
| `Admin/Security_Protocols.md` v0.2
| `Admin/Canonical_Terms.md` v0.2

**What must remain constant:**

**Confidence never outruns verification.**

**Verification seeks sufficient falsifiability, not exhaustive certainty.**

**The kit must remain small enough to be useful.**


ADDENDUM FOR: Forge_Audit_Kit.md
TARGET SECTION: Active Unknowns Index + Dependency Map +
                Expiry Watch note + Resolution Log
INTEGRATION PRIORITY: Medium — index accuracy; no blocking items
===============================================================

## ADDENDUM — Forge_Audit_Kit.md — 2026-05-28

### Active Unknowns Index — status updates

In Governance & Verification section, update:

| ID      | Change                                                    |
|---------|-----------------------------------------------------------|
| GOV-006 | Status: Open → In Progress                               |
| RIP-005 | Status: In Progress (already correct in v0.9 — confirm)  |

### Active Unknowns Index — new rows

In Governance & Verification section, add after CT-003:

| ID      | Title                                         | Owning File                    | Status | Priority |
|---------|-----------------------------------------------|--------------------------------|--------|----------|
| CT-004  | Trusted initialization environment definition | `Admin/Canonical_Terms.md`    | Open   | Major    |
| SEC-004 | Key lifecycle doctrine incomplete             | `Admin/Security_Protocols.md` | Open   | Major    |
| SEC-005 | Trusted initialization environment undefined  | `Admin/Security_Protocols.md` | Open   | Major    |
| SEC-006 | Timestamp trust under degraded clock          | `Admin/Security_Protocols.md` | Open   | Major    |
| SEC-007 | External root-of-trust architecture undefined | `Admin/Security_Protocols.md` | Open   | Critical |

In Cross-Module section, add:

| ID      | Title                                     | Owning Files                                           | Status | Priority |
|---------|-------------------------------------------|--------------------------------------------------------|--------|----------|
| UNK-009 | External root-of-trust — cross-module Critical | Gov Charter / RIP / Security_Protocols           | Open   | Critical |

In Reduction, Intake & Fabrication section, add:

| ID     | Title                                | Owning File               | Status | Priority |
|--------|--------------------------------------|---------------------------|--------|----------|
| PL-001 | Halogenated polymer contamination    | `Operations/Plastics.md`  | Open   | Critical |
| PL-002 | Reactor over-pressurization          | `Operations/Plastics.md`  | Open   | Major    |

### Dependency Map additions

Add to Dependency Map:

```
SEC-004 -> SEC-002 / SEC-003 (coherent lifecycle required)
SEC-005 -> CT-004 (canonical definition required before promotion)
SEC-006 -> SEC-001 (partition is primary degraded-clock context)
SEC-007 -> GOV-003 / GOV-005 / RIP-001 (Critical cross-module)
UNK-009 -> SEC-007 / GOV-003 / GOV-005 / RIP-001
CT-004 -> SEC-005 (consuming unknown)
PL-001 -> blocks first hot pyrolysis run
PL-002 -> blocks first hot pyrolysis run
```

### Expiry Watch note update

Replace current watch note with:

**Current watch (v1.9):** FL-001 and several EC entries approaching
two-cycle threshold. GOV-003 and GOV-005 Critical — no fast resolution
path. RIP-001 Critical — GitHub releases are v0 resolution path.
SEC-007 and UNK-009 Critical from first logging — external root-of-trust
requires architectural decision. Monitor from first logging.

### Resolution Log entry

Add to Resolution Log:

- 2026-05-28: Index updated to v1.9 — GOV-006 and RIP-005 moved to
  In Progress. SEC-004 through SEC-007 added. CT-004 added. PL-001 and
  PL-002 added. UNK-009 (external root-of-trust cross-module Critical)
  added. Expiry Watch updated. Dependency map updated.

### File State update

Update Open Unknowns: 6 → 6 (no new FAK unknowns; index additions only).
Update Last Audit: 2026-05-28.
Update Unknowns.md reference in Status section: v1.8 → v1.9.


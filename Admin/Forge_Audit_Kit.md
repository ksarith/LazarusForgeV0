# Forge_Audit_Kit.md
**Version 0.8**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 3/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-23                                                          |
| Auditor          | Claude — Reconciliation/Auditor                                     |
| Open Unknowns    | 8                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Condensed audit reference for routine multi-agent cycles
- Audit opening checklist (Tier 1 Axiom verification + Expiry Watch)
- Governing principles summary
- Verification Maturity Model
- Truth Provenance label system
- Adversarial priority weighting criteria
- Anti-Theater doctrine
- Repository integrity awareness requirements
- Confidence decay and revalidation guidance
- Fallacy checklist (condensed)
- AI contribution rules (condensed)
- Verification gates (condensed)
- Sign-off format
- Active unknowns index (cross-module, summary only)
- Sidecar ID reference
- Dependency map (condensed)
- Expiry Watch

**This file DOES NOT define:**
- Full auditor role class doctrine (→ Admin/Auditor_Protocols.md)
- Full audit sequencing and phase logic (→ Admin/Auditor_Protocols.md)
- Full Adversarial Challenge Battery (→ Admin/Auditor_Protocols.md)
- Full unknown entry detail (→ owning file sidecars)
- Full cross-module unknown registry (→ Unknowns.md)
- Constitutional governance hierarchy (→ Admin/Governance_Charter.md)
- Ethical policy (→ Admin/Ethical_Constraints.md)
- Engineering specifications

---

## File Purpose

This file is the lightweight operational audit substrate for routine LazarusForgeV0 multi-agent verification cycles. It exists to allow agents to conduct competent audit work without loading the full governance corpus — Auditor_Protocols.md, Unknowns.md, and Governance_Charter.md together exceed practical token limits for routine cycles. When this file contradicts a full source document, the full source document prevails. This file should be updated whenever Auditor_Protocols.md is revised or Unknowns.md version increments.

---

## Assumptions

| ID      | Assumption                                                                    | Basis                            | Confidence | Expiry Trigger                                   |
|---------|-------------------------------------------------------------------------------|----------------------------------|------------|--------------------------------------------------|
| ASM-001 | Routine audit cycles operate under token constraints requiring condensation   | Observed multi-agent workflow    | High       | Token limits no longer relevant                  |
| ASM-002 | This file will remain derived from Auditor_Protocols.md as the source of truth | Governance tier structure       | High       | Kit elevated to independent governance authority |
| ASM-003 | Active unknowns index remains accurate between Unknowns.md version increments | Maintenance discipline           | Medium     | Unknowns.md version increments without kit update |

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`

> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`

> Verification seeks sufficient falsifiability, not exhaustive certainty.

The Forge does not require omniscience before action. It requires explicit uncertainty, bounded operational assumptions, falsifiable claims, and traceable failure handling.

**Infinite audit recursion is a governance failure mode.**

**Scope boundary:** Human override rights apply to verification process decisions only. They do not extend to hard-line doctrines in `Admin/Ethical_Constraints.md` (Anti-Weaponization, Life Preservation).

**Sidecar Model:** Module-specific unknowns live in each file's own `## Auditor Notes & Unknowns` footer. The active unknowns index below lists cross-module unknowns only. Full entry detail is in the owning file's sidecar.

*Full reference: `Admin/Auditor_Protocols.md` §Governing Principles*

---

## Verification Maturity Model

Replaces implicit binary Specification/not-Specification behavior with explicit maturity states.

| State                    | Meaning                                                      | Operational Status         |
|--------------------------|--------------------------------------------------------------|----------------------------|
| Exploration              | Speculative, incomplete, unconstrained                       | Not operational            |
| Candidate Specification  | Structured but incompletely verified                         | Internal review only       |
| Provisional Specification| Verified within bounded assumptions                          | Limited operational use    |
| Operational Specification| Verified against real artifacts and downstream interactions  | Deployable                 |
| Hardened Doctrine        | Survived repeated adversarial and operational cycles         | Trusted baseline           |

**Promotion rule:** A document advances only when assumptions narrow, unknowns shrink, operational predictability increases, and external validation expands.

---

## Exploration vs. Specification

**Exploration** — incomplete, speculative, loosely connected. Do not over-police.

**Specification** — must pass all gates. Claims binding, cross-refs must resolve, numbers must be labeled.

**Loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

*Full reference: `Admin/Auditor_Protocols.md` §Exploration vs. Specification*

---

## Truth Provenance Labels

Quantitative confidence labels (apply to all numerical claims):

| Label       | Meaning                                              |
|-------------|------------------------------------------------------|
| Measured    | Derived from real experimental data                  |
| Estimated   | Derived from analog systems with scaling factors     |
| Analogous   | Drawn from similar documented systems                |
| Placeholder | Provisional, pending verification                    |

Institutional truth provenance labels (apply to all significant claims):

| Label                    | Meaning                                                    |
|--------------------------|------------------------------------------------------------|
| Internally Derived       | Supported only by repository logic or modeling             |
| Analogous External       | Supported by comparable external systems                   |
| Experimentally Verified  | Supported by direct test evidence                          |
| Operationally Hardened   | Survived repeated real-world operational cycles            |

**Rule:** No internally-derived claim may be represented as operationally hardened without external validation. This prevents recursive documentation loops, consensus hallucination, and repository self-certification.

*Full reference: `Admin/Auditor_Protocols.md` §Evidence Classification*

---

## Adversarial Priority Weighting

Full Adversarial Challenge Battery required when any of the following factors are high:

| Factor                | High-Risk Trigger                                    |
|-----------------------|------------------------------------------------------|
| Irreversibility       | Permanent destruction or contamination               |
| Coupling              | Multi-module downstream dependency                   |
| Energy Density        | Thermal, kinetic, chemical, or electrical hazard     |
| Autonomy              | Reduced human oversight                              |
| Silent Failure        | Failure difficult to detect before consequence       |
| Governance Authority  | Document defines behavior of other documents         |

**Partial Battery allowed** for Exploration-stage documents if deferred classes are documented with rationale and no safety-critical claims are present.

*Full reference: `Admin/Auditor_Protocols.md` §Adversarial Audit Layer*

---

## Anti-Theater Doctrine

Adversarial analysis is valuable only if it changes operational understanding.

**Findings should target:** plausible failure pathways, energy-bearing systems, historically observed industrial failures, governance exploitability, hidden coupling, silent corruption mechanisms.

**Weak findings include:** purely rhetorical edge cases, unconstrained hypothetical chains, impossible-state speculation, adversarial narratives without operational consequence.

**Evaluation rule:** A finding's value is proportional to its ability to alter design decisions, narrow assumptions, trigger safeguards, or expose previously invisible coupling.

---

## Repository Integrity & Institutional Memory

The repository is treated as operational infrastructure, not passive documentation.

**Integrity threats include:** audit history rewriting, silent rollback, canonical definition drift, rename registry tampering, fabricated resolution logs, authority spoofing, stale doctrine masquerading as current policy.

**Requirement:** High-coupling governance documents must preserve audit lineage, maintain immutable resolution history, record version transitions, and identify authoritative canonical paths.

**Adversarial linkage:** Institutional memory corruption is treated as Challenge Class 6 (Recursive Justification), Challenge Class 9 (Epistemic Corruption), and Challenge Class 10 (Systemic Coupling).

*Full reference: `Admin/Auditor_Protocols.md` §Adversarial Audit Layer*

---

## Confidence Decay & Revalidation

Knowledge ages. Verification is not permanent.

| Claim Type                          | Revalidation Pressure |
|-------------------------------------|-----------------------|
| Safety-critical operational assumptions | High              |
| Experimental measurements           | Medium–High           |
| Analogous engineering assumptions   | Medium                |
| Governance doctrine                 | Medium                |
| Exploratory concepts                | Low                   |

**Drift indicators triggering revalidation:** tooling changes, environmental changes, new operational evidence, repeated overrides, unresolved unknown accumulation, contradiction between modules, model behavior drift.

**Rule:** Unrevalidated assumptions accumulate epistemic decay over time. Confidence is not durable merely because documentation exists.

---

## Fallacy Checklist

Apply to all specification-level claims. Bare checkmarks are not verification — substantive notes required for non-trivial claims (1–2 sentences: what was checked, what nearly failed, what was adjusted).

**1. Magic Energy** — Every watt needs a traceable origin. Cross-ref `Operations/Energy.md`.

**2. Friction Blindness** — Account for mechanical resistance, thermal losses, fluid drag, wear. Real systems degrade.

**3. Energy Density Paradox** — Does a recovery step cost more than it produces? Justify as enabling investment or flag.

**4. Semantic Drift** — Terms must mean the same thing everywhere. Cross-check against `Architecture/Forge_flow.md`.

**5. Scope Creep** — New capabilities belong in `Admin/Trajectories.md`, not silently in current-version specs.

**6. Hallucinated Files** — All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified. Aspirational references must be labeled *planned*.

**7. Confidence Without Basis** — All numbers must be labeled: **Measured / Estimated / Analogous / Placeholder**. Unlabeled = Placeholder.

**8. Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life path.

**9. Incomplete by Omission** — What critical subsystem is missing? Heat dissipation, waste streams, power draw, human interface?

**10. The Turd Problem** — Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this.

*Full reference: `Admin/Auditor_Protocols.md` §The Fallacy Checklist*

---

## AI Contribution Rules

**Role declaration required:** *"Operating as [Role] per Auditor_Protocols.md v0.7"*

**Valid roles:** Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed.

**Rule 2 — Role Declaration:** Declare role before contributing. Declare role shifts before proceeding.

**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.

**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them.

**Rule 5 — Confidence Labeling:** Use the four-label system. Unlabeled = Placeholder.

**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."*

**Rule 7 — Repository Structure Awareness:** Use canonical folder-prefixed paths (Admin/, Architecture/, Operations/, Tests/). Legacy flat names are aliases only — resolve via Discovery.md Rename Registry.

*Full reference: `Admin/Auditor_Protocols.md` §AI Contribution Protocols*

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass audit by a different agent to override.

| Gate | Test                                                                              | Fail →                                    |
|------|-----------------------------------------------------------------------------------|-------------------------------------------|
| G1   | Fallacy Checklist actively applied with substantive notes?                        | Return to author                          |
| G2   | Physical plausibility — no violation of known constraints?                        | Return for revision                       |
| G3   | Adversarial Challenge Battery applied proportional to coupling/risk?              | Return for adversarial analysis           |
| G4   | Scope alignment — fits current version or trajectory?                             | Route to Admin/Trajectories.md            |
| G5   | Cross-reference integrity — all paths resolve using canonical folder-prefixed names? | Hold at draft                          |
| G6   | Conflict check — no contradiction with existing committed specs?                  | Resolve conflict before committing        |

**Full Stop Review triggers:**
1. Same foundational claim blocked across two separate audit cycles
2. New finding invalidates core premise of a previously promoted specification
3. Pattern of documented overrides eroding a governance principle without explicit revision
4. Multiple Adversarial Challenge Battery findings converging on the same structural gap

*Full reference: `Admin/Auditor_Protocols.md` §Verification Gate Enforcement / §Full Stop Review*

---

## Sign-Off Format

```
Document: [filename] ([status] audit, [date])
Auditor: [Role] — [Agent]

Verification maturity:
[Exploration / Candidate Specification / Provisional Specification /
 Operational Specification / Hardened Doctrine]

Truth basis:
[Internally Derived / Analogous External /
 Experimentally Verified / Operationally Hardened]

Adversarial classes applied:
[list]

Adversarial classes deferred:
[list + reason]

Highest-risk finding:
[one sentence]

Gates cleared:
[list]

Gates blocked:
[list with reason]

Unknowns logged:
[IDs]

Overrides:
[none / list with justification]

Sign-off:
[one sentence summary]
```

---

## Failure Modes (Condensed)

| Failure Mode                   | Description                                                              |
|--------------------------------|--------------------------------------------------------------------------|
| Audit Theater                  | Protocol passes without surfacing real gaps                              |
| Auditor Capture                | Skeptic role softens through repeated exposure                           |
| Coherent Nonsense              | Passes all gates but is systemically wrong                               |
| Exploration Suppression        | Verification pressure applied too early                                  |
| Infinite Audit Recursion       | Verification expands indefinitely without operational closure            |
| Adversarial Performance Art    | Sophisticated-looking adversarial analysis with low predictive value     |
| Institutional Memory Corruption| Repository history or canonical definitions silently altered             |
| Stale Certainty                | Old assumptions treated as verified without revalidation                 |
| Provenance Collapse            | Internally-derived doctrine mistaken for externally validated truth      |
| Metadata Bloat                 | Centralized registries grow until they obstruct governance               |

*Full reference: `Admin/Auditor_Protocols.md` §Failure Modes of This Document*

---

## Audit Opening Checklist

Execute at the start of every audit cycle before proceeding to document review.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1 through P-4, Q-1 through Q-4) are present in `Admin/Governance_Charter.md` with text matching the prior committed version. Any wording change not accompanied by a Resolution Log entry with human ratification note is a Constitutional violation — invoke STATE_HOLD immediately.
*Owner: Skeptic/Auditor role. Full reference: `Admin/Repository_Integrity_Protocol.md` §Protected Elements*

**2. Expiry Watch**
Check `Unknowns.md` global index for entries approaching two-cycle threshold without a documented Resolution Path. Escalate to Systemic Risk or demote dependent module.
*Owner: Skeptic/Auditor role.*

**Version cycle definition:** One completed multi-agent audit pass with findings logged.

**Current watch (v1.7):** FL-001 and several EC entries approaching two-cycle threshold. GOV-003 and GOV-005 flagged Critical — monitor from first logging. Flag for Full Stop Review trigger assessment at next audit opening if still unresolved.

*Full reference: `Unknowns.md` §Expiry Watch | `Admin/Repository_Integrity_Protocol.md` §Constitutional Violation*

---

## Sidecar ID Reference

| Prefix | Owning File                                        |
|--------|----------------------------------------------------|
| EV-    | `Operations/Energy.md`                             |
| LT-    | `Tests/Leviathan_testing.md`                       |
| FL-    | `Architecture/Forge_flow.md`                       |
| TS-    | `Operations/Gate_02_Triage.md`                     |
| CO-    | `Architecture/Components.md`                       |
| EC-    | `Admin/Ethical_Constraints.md`                     |
| AP-    | `Admin/Auditor_Protocols.md`                       |
| GOV-   | `Admin/Governance_Charter.md`                      |
| SC-    | `Operations/Gate_05_Separation_Thermal.md`         |
| MG-    | `Operations/Gate_04_Separation_Mechanical.md`      |
| AS-    | `Operations/Air_Scrubber.md`                       |
| SR-    | `Tests/Support_Raft.md`                            |
| GK-    | `Architecture/Geck_forge_seed.md`                  |
| ST-    | `Admin/Ship_of_Theseus.md`                         |
| EL-    | `Operations/Electronics.md`                        |
| CF-    | `Architecture/Cognitive_Frameworks.md`             |
| TR-    | `Admin/Trajectories.md`                            |
| GI-    | `Operations/Gate_01_Intake.md`                     |
| GR-    | `Operations/Gate_03_Reduction.md`                  |
| GF-    | `Operations/Gate_06_Fabrication.md`                |
| GU-    | `Operations/Gate_07_Utilization.md`                |
| RIP-   | `Admin/Repository_Integrity_Protocol.md`           |
| FN-    | `Architecture/Forge_Net.md`                        |

*Note: Legacy flat filenames are aliases. Resolve all stale references using the Rename Registry in `Discovery.md`.*

---

## Active Unknowns Index

*Cross-module unknowns only. Full entry detail in owning file sidecars. Full registry: `Unknowns.md` v1.7*

### Energy & Power

| ID     | Title                              | Owning File              | Status      | Priority  |
|--------|------------------------------------|--------------------------|-------------|-----------|
| EV-001 | Forge power demand uncharacterized | `Operations/Energy.md`   | In Progress | Blocking  |

### Leviathan / Autonomy

| ID     | Title                              | Owning File                       | Status | Priority  |
|--------|------------------------------------|-----------------------------------|--------|-----------|
| LT-001 | Power envelope — no placeholder anchor | `Tests/Leviathan_testing.md`  | Open   | Blocking  |
| LT-002 | Deep-ocean storage degradation     | `Tests/Leviathan_testing.md`      | Open   | Blocking  |
| LT-003 | Autonomy architecture unspecified  | `Tests/Leviathan_testing.md`      | Open   | Blocking  |
| LT-004 | Trust model mechanism undefined    | `Tests/Leviathan_testing.md`      | Open   | Blocking  |
| LT-005 | Priority propagation — no mechanism | `Tests/Leviathan_testing.md`     | Open   | Blocking  |
| LT-006 | Ethical log survival at depth      | `Tests/Leviathan_testing.md`      | Open   | Non-blocking |

### Gate Logic & Triage

| ID     | Title                                    | Owning File                      | Status      | Priority  |
|--------|------------------------------------------|----------------------------------|-------------|-----------|
| FL-001 | Gate logic determinism                   | `Architecture/Forge_flow.md`     | In Progress | Blocking  |
| TS-001 | "Sufficient for forge duty" threshold    | `Operations/Gate_02_Triage.md`   | In Progress | Blocking  |
| TS-002 | Contamination routing protocol           | `Operations/Gate_02_Triage.md`   | Open        | Blocking  |
| TS-003 | Gate determinism (downstream)            | `Operations/Gate_02_Triage.md`   | In Progress | Blocking  |
| CO-001 | Graduation Rule detection circularity    | `Architecture/Components.md`     | In Progress | Blocking  |

### Ethics & Governance

| ID     | Title                                        | Owning File                       | Status      | Priority  |
|--------|----------------------------------------------|-----------------------------------|-------------|-----------|
| EC-001 | "Sufficient confidence" threshold            | `Admin/Ethical_Constraints.md`    | Open        | Blocking  |
| EC-002 | Anti-Weaponization pattern-matching          | `Admin/Ethical_Constraints.md`    | Open        | Blocking  |
| EC-003 | Human escalation path                        | `Admin/Ethical_Constraints.md`    | In Progress | Blocking  |
| EC-004 | Governance failure modes lifecycle           | `Admin/Ethical_Constraints.md`    | In Progress | Blocking  |
| EC-005 | Life-preservation vs. Anti-Weaponization     | `Admin/Ethical_Constraints.md`    | In Progress | Blocking  |
| EC-006 | Ethical log survival under unit loss         | `Admin/Ethical_Constraints.md`    | Open        | Non-blocking |
| EC-007 | Governance fail-safe                         | `Admin/Ethical_Constraints.md`    | In Progress | Blocking  |
| GOV-001 | Governance migration mechanics incompletely operationalized | `Admin/Governance_Charter.md` | Open | Major |
| GOV-002 | Provenance operationalization immature       | `Admin/Governance_Charter.md`     | Open        | Major     |
| GOV-003 | Integrity enforcement architecture undefined | `Admin/Governance_Charter.md`     | Open        | Critical  |
| GOV-004 | Escalation calibration partially subjective  | `Admin/Governance_Charter.md`     | Open        | Major     |
| GOV-005 | Long-term constitutional stability unproven  | `Admin/Governance_Charter.md`     | Open        | Critical  |
| GOV-006 | Human override authenticity validation undefined | `Admin/Governance_Charter.md` | Open       | Major     |
| GOV-007 | Bootstrap governance authority initialization undefined | `Admin/Governance_Charter.md` | Open   | Major     |

### Governance & Verification

| ID     | Title                                             | Owning File                    | Status      | Priority  |
|--------|---------------------------------------------------|--------------------------------|-------------|-----------|
| AP-001 | Auditor effectiveness metrics not yet measured    | `Admin/Auditor_Protocols.md`   | Open        | Major     |
| AP-002 | Override vs. immutability boundary not confirmed in both documents | `Admin/Auditor_Protocols.md` | In Progress | Major |
| AP-003 | Audit trail schema (machine-readable) deferred    | `Admin/Auditor_Protocols.md`   | Open        | Minor     |
| AP-004 | Cross-auditor disagreement resolution incomplete  | `Admin/Auditor_Protocols.md`   | Open        | Major     |
| AP-005 | Verification termination threshold undefined      | `Admin/Auditor_Protocols.md`   | Open        | Major     |
| AP-006 | Institutional truth provenance hierarchy undefined | `Admin/Auditor_Protocols.md`  | Open        | Major     |
| AP-007 | Repository integrity and doctrine lineage protections undefined | `Admin/Auditor_Protocols.md` | Open   | Major     |
| RIP-001 | Prior-state archival system not yet established              | `Admin/Repository_Integrity_Protocol.md` | Open | Critical |
| RIP-002 | AUDIT_HARNESS.py Phase 1 checks not yet implemented          | `Admin/Repository_Integrity_Protocol.md` | Open | Major    |
| RIP-003 | Violation incident log location undefined                    | `Admin/Repository_Integrity_Protocol.md` | Open | Major    |
| RIP-004 | Constitutional violation detection latency undefined         | `Admin/Repository_Integrity_Protocol.md` | Open | Major    |
| RIP-005 | Security_Protocols.md dependency unresolved                  | `Admin/Repository_Integrity_Protocol.md` | Open | Major    |

### Hardware Modules

| ID     | Title                                    | Owning File                                    | Status | Priority     |
|--------|------------------------------------------|------------------------------------------------|--------|--------------|
| SC-001 | RPM envelope not validated               | `Operations/Gate_05_Separation_Thermal.md`     | In Progress | Blocking |
| SC-002 | Segregation effectiveness at v0 scale    | `Operations/Gate_05_Separation_Thermal.md`     | Open   | Blocking     |
| SC-005 | Drive system geometry — dynamic imbalance blocked | `Operations/Gate_05_Separation_Thermal.md` | Open | Major    |
| SC-006 | Siting and area-of-operation requirements | `Operations/Gate_05_Separation_Thermal.md`    | Open   | Major        |
| MG-002 | Optimal RPM bands not characterized per feedstock | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major   |
| MG-003 | Confidence threshold not empirically validated | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major    |
| MG-007 | Rotor jam and entanglement recovery undefined | `Operations/Gate_04_Separation_Mechanical.md` | Open | Major    |
| AS-001 | 500W power budget not validated          | `Operations/Air_Scrubber.md`                   | Open   | Medium       |
| AS-003 | Scrubber waste stream and saturation     | `Operations/Air_Scrubber.md`                   | In Progress | Medium   |
| SR-001 | Galvanic corrosion mitigation            | `Tests/Support_Raft.md`                        | Open   | High         |
| SR-002 | Sacrificial shell material selection     | `Tests/Support_Raft.md`                        | Open   | Medium       |

### Salvage & Fabrication

| ID     | Title                                            | Owning File                    | Status | Priority  |
|--------|--------------------------------------------------|--------------------------------|--------|-----------|
| EL-001 | Forge-Standard interface spec                    | `Operations/Electronics.md`    | Open   | Medium    |
| EL-003 | TMR voter implementation                         | `Operations/Electronics.md`    | Open   | Medium    |
| EL-005 | Toxic dust and BFR emission profile not characterized | `Operations/Electronics.md` | Open | Critical |
| EL-006 | Firmware trust and reflashing validation not defined | `Operations/Electronics.md` | Open  | Critical  |
| EL-007 | Correlated TMR failure modes                     | `Operations/Electronics.md`    | Open   | Major     |
| EL-008 | Counterfeit salvage component detection doctrine | `Operations/Electronics.md`    | Open   | Major     |

### Reduction, Intake & Fabrication (Critical only)

| ID     | Title                                                     | Owning File                        | Status | Priority  |
|--------|-----------------------------------------------------------|------------------------------------|--------|-----------|
| GI-002 | Energetic material discharge doctrine not defined         | `Operations/Gate_01_Intake.md`     | Open   | Critical  |
| GI-003 | Augmented hazard detection capability not specified       | `Operations/Gate_01_Intake.md`     | Open   | Critical  |
| GI-007 | Digital contamination and hostile firmware handling       | `Operations/Gate_01_Intake.md`     | Open   | Critical  |
| GR-002 | Reduction method not selected                            | `Operations/Gate_03_Reduction.md`  | Open   | Major     |
| GR-003 | Biological and chemical waste disposal doctrine not assigned | `Operations/Gate_03_Reduction.md` | Open | Critical |
| GR-007 | Contaminated equipment retirement threshold not defined   | `Operations/Gate_03_Reduction.md`  | Open   | Critical  |
| GF-007 | Fabrication-area fire suppression and hot-work doctrine   | `Operations/Gate_06_Fabrication.md`| Open   | Critical  |

### Network

| ID     | Title                                  | Owning File                   | Status | Priority  |
|--------|----------------------------------------|-------------------------------|--------|-----------|
| FN-001 | Data validation criteria not defined   | `Architecture/Forge_Net.md`   | Open   | Critical  |
| FN-005 | Data privacy and access control        | `Architecture/Forge_Net.md`   | Open   | Critical  |

### Utilization

| ID     | Title                                              | Owning File                         | Status | Priority |
|--------|----------------------------------------------------|-------------------------------------|--------|----------|
| GU-001 | Performance metric schema not defined              | `Operations/Gate_07_Utilization.md` | Open   | Major    |
| GU-002 | Retirement handoff not cross-validated             | `Operations/Gate_07_Utilization.md` | Open   | Major    |
| GU-004 | Silent failure detection capability not defined    | `Operations/Gate_07_Utilization.md` | Open   | Major    |

### Cross-Module

| ID      | Title                                                         | Owning Files                                                | Status | Priority |
|---------|---------------------------------------------------------------|-------------------------------------------------------------|--------|----------|
| UNK-006 | Master safety registry — siting and clearance for all rotating and thermal modules | SC-006, MG-006        | Open   | Major    |
| UNK-008 | Welding wire specification and qualification — no owner assigned | SC-004                                                   | Open   | Major    |

### Trajectory

| ID     | Title                  | Owning File             | Status | Priority |
|--------|------------------------|-------------------------|--------|----------|
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
AP-005 (verification closure) -> EC-001 (sufficient confidence)
AP-006 (truth provenance) -> FN-001 / CF-002
AP-007 (repo integrity) -> FN-001 / AP-003 / Architecture/Forge_Net.md
AP-007 cross-ref GOV-003 (integrity enforcement architecture)
RIP-001 (prior-state archival) -> blocks Phase 2 automation; resolved by GitHub release strategy
RIP-002 (Phase 1 automation) -> depends on RIP-001 for comparison checks
RIP-004 (detection latency) -> resolved by Audit Opening Checklist axiom verification step
RIP-005 (Security_Protocols.md) -> GOV-006 (human override authenticity); Phase 3 dependency
GI-002 -> blocks first operational Intake run
GI-003 -> blocks first unsupervised Intake run
GI-007 -> depends on FN-001, Operations/Electronics.md
GR-002 -> unblocks GR-001, GR-004, GR-005, GR-006
GR-003 -> no owner in repository — Critical gap
EL-005 -> feeds Air_Scrubber.md sizing and filter selection
EL-006 -> prerequisite for first salvaged MCU integration
FN-001 -> blocks first network connection
FN-005 -> blocks first network connection
SC-001 -> SC-005
TR-001 -> depends on EV-001
```

*Full map: `Unknowns.md` §Dependency Map*

---

## How to Use This File

**Load in routine audit cycles:**
```
FILES = [
    "[document_to_audit]",
    "Admin/Forge_Audit_Kit.md",     # ~12k chars
]
```

**Load full source documents instead when:**
- Auditing `Admin/Auditor_Protocols.md` itself → load Auditor_Protocols.md
- Auditing `Unknowns.md` itself → load Unknowns.md
- Auditing `Admin/Governance_Charter.md` itself → load Governance_Charter.md
- Onboarding a new agent → load full governance corpus
- Need full unknown entry detail → load owning file or Unknowns.md
- Adversarial Battery application → load Auditor_Protocols.md for full challenge class definitions

**Maintenance:** Update when Auditor_Protocols.md is revised or Unknowns.md version increments. Fields requiring update: active unknowns tables, sidecar ID reference, version header, Expiry Watch note, dependency map.

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                          | What Failed                                                    | What Was Learned                                                                 | Confidence | Revalidation Needed |
|----------|---------------|---------------------------------------------------------|----------------------------------------------------------------|----------------------------------------------------------------------------------|------------|---------------------|
| May 2026 | Audit Review  | Stale flat filenames in kit sidecar ID reference        | References became invalid after repository restructuring       | Sidecar ID reference must use canonical folder-prefixed paths                    | Replicated | No                  |
| May 2026 | Audit Review  | Kit derived from protocols without explicit derivation statement | Kit diverged from source without detection              | Derivation relationship must be explicit in scope boundary and purpose           | Replicated | No                  |
| May 2026 | Audit Review  | Binary Specification/not-Specification promotion model  | Documents promoted before operational validation existed       | Verification Maturity Model needed — five states from Exploration to Hardened    | Analogous  | Yes                 |
| May 2026 | Audit Review  | Quantitative confidence labels without provenance labels | Internally coherent docs mistaken for externally validated reality | Institutional truth provenance labels required as separate dimension           | Analogous  | Yes                 |
| 2026-05-23 | Audit Review | Expiry Watch as sole audit opening check | Tier 1 Axiom text could be modified between cycles without detection | Axiom verification added as mandatory first step at audit opening — Constitutional violations require immediate STATE_HOLD | Analogous | Yes |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date     | Path                                                              | Why Abandoned                                                                              | Reconsider? |
|----------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------|-------------|
| May 2026 | Kit as standalone governance authority equal to Auditor_Protocols | Kit is derived — elevating it above its source introduces circular authority               | No          |
| May 2026 | Single quantitative confidence label system without provenance    | Insufficient — internally coherent documentation can be mistaken for operational truth     | No          |
| May 2026 | Flat filename references in sidecar ID table                      | Repository restructuring broke all flat references; canonical paths required throughout    | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this file:

- Active unknowns index diverges from Unknowns.md without documented reason
- Sidecar ID reference contains stale or flat filenames
- Governing principles contradict Admin/Auditor_Protocols.md
- Verification gates diverge from Admin/Auditor_Protocols.md gate definitions
- Sign-off format diverges from Admin/Auditor_Protocols.md sign-off format
- Verification Maturity Model states diverge from Admin/Auditor_Protocols.md
- Expiry Watch not updated at Unknowns.md version increment
- Ethical Anchor field is absent, altered, or does not match canonical string
- Kit version header references a superseded version of Auditor_Protocols.md

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

*Note: AP-005, AP-006, AP-007 are new entries introduced in this reconciliation. They must be added to Admin/Auditor_Protocols.md sidecar and to Unknowns.md governance section before next audit cycle. This is a pending action, not a completed one.*

### FAK-001 — Kit version header maintenance discipline undefined

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Forge_Audit_Kit.md |
| First Logged  | 2026-05-23               |
| Last Reviewed | 2026-05-23               |

**Description:** No formal trigger or owner is defined for updating the kit when Auditor_Protocols.md is revised or Unknowns.md version increments.

**Why It Matters:** Kit drift from source documents is a known failure mode — the kit becomes stale guidance while appearing authoritative.

**Resolution Path:** Payment via Specification — add maintenance trigger to Drift Indicators and assign update responsibility explicitly in How to Use section.

---

### FAK-002 — AP-005 through AP-007 not yet added to Auditor_Protocols.md sidecar

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Forge_Audit_Kit.md |
| First Logged  | 2026-05-23               |
| Last Reviewed | 2026-05-23               |

**Description:** AP-005 (verification termination threshold), AP-006 (institutional truth provenance), and AP-007 (repository integrity doctrine lineage) were introduced in this reconciliation but do not yet exist in Admin/Auditor_Protocols.md sidecar or Unknowns.md.

**Why It Matters:** Unknown IDs in the kit that do not exist in the owning file sidecar or global index are orphaned references — a cross-reference integrity failure per Gate G5.

**Resolution Path:** Payment via Specification — add AP-005 through AP-007 to Admin/Auditor_Protocols.md sidecar and Unknowns.md governance section before next audit cycle.

---

### FAK-003 — GOV entries newly added to kit index but not previously tracked here

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Governance               |
| Blocking      | No                       |
| Owner         | Admin/Forge_Audit_Kit.md |
| First Logged  | 2026-05-23               |
| Last Reviewed | 2026-05-23               |

**Description:** GOV-001 through GOV-007 from Governance_Charter.md sidecar were not present in prior kit versions. They are added here for completeness but represent a scope expansion for the kit's unknowns index.

**Why It Matters:** If the kit's unknowns index grows to include all sidecar entries from all files it will exceed token budget and defeat its purpose.

**Resolution Path:** Discharge via Lessons Learned — confirm at next audit cycle whether GOV entries should remain in kit index or be restricted to Unknowns.md only.

---

### Resolution Log

- 2026-05-23: Reconciliation pass — v0.7 merges current kit with provisional kit upgrades. Verification Maturity Model, Truth Provenance Labels, Anti-Theater Doctrine, Confidence Decay/Revalidation, adversarial priority weighting, and expanded sign-off format added. File_Template.md structure applied throughout. AP ID collision resolved. GOV- prefix added to sidecar ID reference. Tier relationship with Auditor_Protocols.md clarified.
- 2026-05-23: **v0.8 update** — Audit Opening Checklist added (Tier 1 Axiom verification + Expiry Watch); resolves RIP-004. RIP- prefix added to Sidecar ID Reference. RIP-001 through RIP-005 added to Governance & Verification unknowns. Dependency map updated with RIP cluster. Unknowns.md reference updated to v1.7. Derivation statement updated to include Repository_Integrity_Protocol.md v0.1.

---

## Status

Version 0.8 — adds Audit Opening Checklist and Repository_Integrity_Protocol.md integration.

**Derived from:** `Admin/Auditor_Protocols.md` v0.7 | `Unknowns.md` v1.7 | `Admin/Repository_Integrity_Protocol.md` v0.1

**Changes from v0.7:**
- Audit Opening Checklist added — Tier 1 Axiom verification as mandatory first step; resolves RIP-004 (Constitutional violation detection latency)
- Audit Opening Checklist added to Scope Boundary DOES define list
- RIP- prefix added to Sidecar ID Reference table
- RIP-001 through RIP-005 added to Governance & Verification unknowns index
- Dependency map updated with RIP cluster entries
- Unknowns.md reference updated from v1.6 to v1.7
- Derivation statement updated to include Repository_Integrity_Protocol.md v0.1
- Open unknowns count updated from 3 to 8
- Lessons Learned entry added for audit opening checklist addition

**Changes from v0.6 (carried from v0.7):**
- File_Template.md structure applied throughout
- Verification Maturity Model added
- Truth Provenance Labels added
- Adversarial Priority Weighting, Anti-Theater Doctrine, Repository Integrity & Institutional Memory, Confidence Decay & Revalidation sections added
- Expanded sign-off format
- GOV-001 through GOV-007, AP-004 through AP-007 added to unknowns index

**What must remain constant:**

**Confidence never outruns verification.**

**Verification seeks sufficient falsifiability, not exhaustive certainty.**


# Forge_Audit_Kit.md — Semantic Stability Additions
# Version 0.9 insertable blocks
# Two discrete additions: (1) Audit Opening Checklist step 3, (2) Fallacy 4 expansion
# Apply these to the existing Forge_Audit_Kit.md v0.8 body

---

## ADDITION 1 — Audit Opening Checklist: Step 3 (Semantic Stability Check)

Insert after the existing Step 2 (Expiry Watch) in the Audit Opening Checklist section.

---

**3. Semantic Stability Check**
Scan the document under audit for any of the following high-drift-risk terms.
If found in specification-level content, verify usage matches the canonical
definition in `Admin/Canonical_Terms.md` before proceeding. Flag violations
as [FALLACY 4 — Semantic Drift] findings.

| Term                                  | Drift Risk                                         | Canonical Resolution                                  |
|---------------------------------------|----------------------------------------------------|-------------------------------------------------------|
| Recycling                             | Used where Value Preservation or Material Recovery is correct | `Admin/Canonical_Terms.md` §Anti-Drift Guardrails |
| Autonomous Decision-Making (unbound)  | Obscures human override visibility; Axiom P-4 exposure | `Admin/Canonical_Terms.md` §Anti-Drift Guardrails |
| High-RPM (applied to Gate_04)         | Terminology bleed from Gate_05 Spin Chamber        | `Admin/Canonical_Terms.md` §Operational Flow         |
| Canonical (unqualified)               | Five distinct usages; ambiguity creates cross-ref failures | `Admin/Canonical_Terms.md` §Disambiguation        |
| Safe / Contained / Stable / Sufficient / Hold / Clear | Context-dependent; two operators may interpret differently | Tighten definition or log as unknown per Challenge Class 4 |
| Scrap                                 | Imprecise; conflates material states               | `Admin/Canonical_Terms.md` §Anti-Drift Guardrails    |
| Specification (applied to Exploration content) | Implicit promotion without gate passage   | `Admin/Auditor_Protocols.md` §Exploration vs. Specification |

**Resolution routing:**
- Term found in Exploration content: note but do not block.
- Term found in Draft or Specification content: flag as [FALLACY 4], require
  correction or explicit justification before gate passage.
- Term conflict between two files: route to `Admin/Canonical_Terms.md` as
  resolution authority unless the conflict involves operational routing
  semantics (route to `Architecture/Forge_flow.md`) or tier definitions
  (route to `Admin/Governance_Charter.md`).

*Owner: Skeptic/Auditor role. Full reference: `Admin/Canonical_Terms.md`*

---

## ADDITION 2 — Fallacy Checklist: Fallacy 4 Expansion

Replace the existing Fallacy 4 entry in the Fallacy Checklist section with
the following expanded version.

**Current text (v0.8):**
> **4. Semantic Drift** — Terms must mean the same thing everywhere.
> Cross-check against `Architecture/Forge_flow.md`.

**Replace with:**

**4. Semantic Drift**
Terms must mean the same thing across all files and all agent contributions.
Drift occurs when a term changes meaning between documents, between audit
cycles, or between agent sessions without a documented revision.

*Primary detection:* Run the Semantic Stability Check (Audit Opening
Checklist Step 3) before beginning document review. Terms flagged there
carry forward as active drift candidates for this check.

*Cross-check routing:*
- Operational routing vocabulary → `Architecture/Forge_flow.md`
- Cross-file consistency and anti-drift enforcement → `Admin/Canonical_Terms.md`
- Governance tier vocabulary → `Admin/Governance_Charter.md`

*Conflict resolution:* If two files use the same term differently, the
resolution authority is determined by domain. Conflicts must be logged as
Active Disputes in `Admin/Canonical_Terms.md` — never silently resolved
by choosing one file over the other without documentation.

*High-risk drift patterns observed in this repository:*
- Gate_04 / Gate_05 separation vocabulary (centrifugal vs. thermal; RPM scope)
- "Canonical" used without qualification
- "Autonomous" used without bounding clauses
- Status labels (Exploration / Draft / Specification) applied inconsistently
- "Recycling" used where material state distinctions are required

*Full reference: `Admin/Canonical_Terms.md` | `Architecture/Forge_flow.md`*

---

## ADDITION 3 — Sidecar ID Reference: New Prefixes

Insert the following two rows into the Sidecar ID Reference table.
Add after the RIP- row.

| Prefix | Owning File                          |
|--------|--------------------------------------|
| SEC-   | `Admin/Security_Protocols.md`        |
| CT-    | `Admin/Canonical_Terms.md`           |

---

## ADDITION 4 — Active Unknowns Index: New Entries

Insert the following under the Governance & Verification section of the
Active Unknowns Index. Add after the RIP-005 row.

| ID     | Title                                        | Owning File                       | Status | Priority |
|--------|----------------------------------------------|-----------------------------------|--------|----------|
| SEC-001 | Quorum recovery under terminal network division | `Admin/Security_Protocols.md`  | Open   | Major    |
| SEC-002 | Key revocation and compromise response doctrine undefined | `Admin/Security_Protocols.md` | Open | Major |
| SEC-003 | Key rotation period undefined                | `Admin/Security_Protocols.md`     | Open   | Major    |
| CT-001  | Legacy script integration name mapping       | `Admin/Canonical_Terms.md`        | Open   | Minor    |
| CT-002  | Component Library schema standard undefined  | `Admin/Canonical_Terms.md`        | Open   | Major    |
| CT-003  | Dependency_Priority_Map.md needed before v1  | `Admin/Canonical_Terms.md`        | Open   | Minor    |

---

## ADDITION 5 — Lessons Learned: New Entry

Insert the following row into the Lessons Learned table.

| Date       | Evidence Type | What Was Tried                                              | What Failed                                                                 | What Was Learned                                                                                                          | Confidence | Revalidation Needed |
|------------|---------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-27 | Audit Review  | Fallacy 4 (Semantic Drift) without a named term watchlist   | High-drift-risk terms not systematically checked; drift caught reactively   | Semantic Stability Check at audit opening with named term list converts reactive detection to proactive prevention         | Analogous  | Yes                 |

---

## ADDITION 6 — Scope Boundary: Update DOES define list

Add the following entry to the "This file DOES define" list in the
Scope Boundary section:

- Semantic Stability Check — audit opening vocabulary verification step
  cross-referencing `Admin/Canonical_Terms.md` as resolution authority

---

## ADDITION 7 — Dependency Map: New entries

Add the following lines to the Dependency Map (Condensed) section:

```
SEC-001 (quorum recovery) -> GOV-008 (minimum quorum definition) — blocking dependency
SEC-002 (key revocation) -> SEC-001 (partition affects propagation)
SEC-002 -> GOV-006 (override node revocation requires additional safeguards)
SEC-003 (key rotation) -> SEC-002 (rotation and revocation must be consistent)
CT-002 (component library schema) -> Operations/Gate_02_Triage.md (blocks Spec promotion)
CT-002 -> Architecture/Components.md (cross-validation required)
CT-003 (dependency priority map) -> discharge via Admin/Trajectories.md v0->v1 transition
```

---

## VERSION HEADER UPDATE

Update the File State table:
- Open Unknowns: 14 (adds 6 new entries: SEC-001 through SEC-003, CT-001 through CT-003)
- Last Audit: 2026-05-27
- Auditor: Claude — Skeptic/Auditor

Update the Status section version to v0.9 and add to Changes list:

**Changes from v0.8:**
- Semantic Stability Check added to Audit Opening Checklist as mandatory
  Step 3 — named drift-risk term watchlist with canonical resolution routing
- Fallacy 4 (Semantic Drift) expanded — detection routing, conflict resolution
  doctrine, and high-risk drift patterns specific to this repository added
- SEC- and CT- prefixes added to Sidecar ID Reference table
- SEC-001 through SEC-003 and CT-001 through CT-003 added to Active Unknowns Index
- Dependency map updated with SEC and CT cluster entries
- Lessons Learned entry added for semantic stability check addition
- Scope Boundary updated to include Semantic Stability Check
- Derived from statement updated to include Security_Protocols.md v0.2
  and Canonical_Terms.md v0.2

---

## PLACEMENT NOTES FOR HUMAN OPERATOR

Audit Opening Checklist currently has:
  1. Tier 1 Axiom Verification
  2. Expiry Watch
  → Insert Step 3 (Semantic Stability Check) here

Fallacy Checklist Fallacy 4:
  → Replace existing one-liner with expanded version above

Sidecar ID Reference table:
  → Add SEC- and CT- rows after RIP- row

Active Unknowns Index — Governance & Verification section:
  → Add six new rows after RIP-005

Lessons Learned table:
  → Add one new row

Scope Boundary — DOES define:
  → Add one bullet

Dependency Map:
  → Add seven new lines

File State and Status section:
  → Update version, unknowns count, audit date, auditor, changes list

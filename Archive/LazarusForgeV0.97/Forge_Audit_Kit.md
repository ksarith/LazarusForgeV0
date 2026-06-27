# Forge_Audit_Kit.md
**Version 1.2**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Last Audit     | 2026-06-21                                                          |
| Auditor        | Claude — Synthesizer; Gemini + Grok — Skeptic/Auditor               |
| Open Unknowns  | See sidecar                                                         |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.8.1 | `Unknowns.md` v3.3

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Governing principles · Epistemic Foundation condensed reference · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Audit Opening Checklist · Fallacy checklist · AI contribution rules · Verification gates · Sign-off format · Governance sidecar ID reference · How to use

**DOES NOT define:** Full auditor role doctrine (-> `Admin/Auditor_Protocols.md`) · Full Epistemic Foundation constitutional text (-> `Admin/Auditor_Protocols.md` EF-0.0-EF-0.8b) · Full Adversarial Battery (-> `Admin/Auditor_Protocols.md`) · Unknown registry (-> `Unknowns.md`) · File paths and ownership (-> `Discovery.md`) · Dependency maps (-> `Unknowns.md`) · Governance hierarchy (-> `Admin/Governance_Charter.md`) · Ethical policy (-> `Admin/Ethical_Constraints.md`) · Canonical vocabulary (-> `Admin/Canonical_Terms.md`) · Kit evolution history (-> git log)

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`
> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`
> Reality is sovereign. Every process, agent, metric, and protocol is merely an imperfect instrument attempting to approach it. — `Admin/Auditor_Protocols.md` EF-0.0
> Verification seeks sufficient falsifiability, not exhaustive certainty.

Infinite audit recursion is a governance failure mode. Human override applies to process decisions only — not to `Admin/Ethical_Constraints.md` hard floors. The Epistemic Foundation (EF-0.0-EF-0.8b) is meta-constitutional and may not be amended without human ratification.

---

## Epistemic Foundation — Condensed Reference

Full text: `Admin/Auditor_Protocols.md` EF-0.0-EF-0.8b. Runtime checklist only — source prevails on interpretive questions.

| Section | Core Rule |
|---------|-----------|
| EF-0.0 Epistemic Anchor | Reality > utility/consensus/elegance/coherence. All claims: VERIFIED / PROVISIONAL / UNKNOWN. Collapse UNKNOWN->VERIFIED without empirical input is prohibited. Reward falsification = reward confirmation. |
| EF-0.1 Epistemic Filter | Disqualified as evidence: fluency, agent consensus, systemic utility, precedent, correlation, repetition, confidence scores, compression. May generate hypotheses; never verify. |
| EF-0.2 Decay Triggers | L1 (confidence-accuracy mismatch / agent disagreement) -> Red-Team. L2 (prediction failure / sycophancy loop) -> Quarantine + human review. L3 (suppression / tampering / metric override) -> Epistemic Reset + mandatory human governing party review. |
| EF-0.3 Epistemic Ledger | Five fields per state correction: Previous Premise · Contradictory Evidence · Falsification Method · Updated State · Confidence Interval. Created on falsification only — not on consensus shift. |
| EF-0.4 Auditor Fallibility | Auditor has no exemption from Axiom Zero. Auditor conclusions are PROVISIONAL. Guardians require guardians. |
| EF-0.5 Anti-Sacralization | No document immune from challenge — including this kit and `Admin/Auditor_Protocols.md`. Stability = repeated verification, not prestige. |
| EF-0.6 Goodhart's Law | Metrics are indicators, not objectives. No optimization overrides contradictory observations to preserve KPI. Applies to gate rates, unknown counts, Protocol Performance. |
| EF-0.7 Process Supervision | Evaluate reasoning pathways, not outputs. Monitor Machiavellian Gap (scratchpad vs. public output divergence). Inspectable lineage required: origin -> assumptions -> discarded evidence -> uncertainty preserved? |
| EF-0.8 SW Grounding | Code execution, telemetry, tool returns are the hard floor. Agent narratives about tool outputs are PROVISIONAL until tool confirmation logged. |
| EF-0.8b Physical Grounding | Sensor telemetry, assay outputs, measured physical constants supersede model/simulation/inference. Simulation confirming simulation is not grounding. Hardware outcomes supersede spec predictions. |

---

## Verification Maturity Model

| State                  | Operational Status         |
|------------------------|----------------------------|
| Exploration            | Not operational            |
| Candidate Spec         | Internal review only       |
| Provisional Spec       | Limited operational use    |
| Operational Spec       | Deployable                 |
| Hardened Doctrine      | Trusted baseline           |

Promotion rule: assumptions narrow, unknowns shrink, external validation expands.

---

## Truth Provenance Labels

**Quantitative:** Measured | Estimated | Analogous | Placeholder — Unlabeled = Placeholder.

**Institutional:** Internally Derived | Analogous External | Experimentally Verified | Operationally Hardened

No internally-derived claim may be represented as operationally hardened without external validation. Full doctrine: `Admin/Auditor_Protocols.md` AP-006.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high: Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure | Governance Authority

Partial Battery allowed for Exploration-stage if deferred classes are documented and no safety-critical claims are present.

---

## Audit Opening Checklist

Execute before every document review. Do not skip steps.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1-P-4, Q-1-Q-4) match prior committed version in `Admin/Governance_Charter.md`. Any unratified wording change = Constitutional violation -> STATE_HOLD immediately.

**2. Epistemic Foundation Integrity Check**
Confirm EF-0.0 through EF-0.8b text in `Admin/Auditor_Protocols.md` matches prior committed version. Any unratified modification = Integrity Violation (EF-0.2 Level 3) -> STATE_HOLD immediately. These sections are meta-constitutional; wording changes require human ratification.

**3. Expiry Watch**
Check `Unknowns.md` for Blocking entries approaching two-cycle threshold without a documented Resolution Path. Escalate to Systemic Risk or demote dependent module.

Current critical watch (v3.3): EC cluster approaching threshold · GOV-003 / GOV-005 Critical · RIP-001 Critical (GitHub releases are v0 path) · CF-001 In Progress (hardware prototype required) · SEC-007 Critical (above-repository decision required) · TF-006 Ethical_Constraints escalation candidate.

AP-001 through AP-007 SYSTEMIC RISK — 2026-06-21: These seven unknowns in `Admin/Auditor_Protocols.md` have exceeded the 2-cycle expiry threshold (estimated 8 cycles). Resolution Pass required before next standard cycle. Autonomous specification progression on dependent modules suspended until at least one entry reaches Payment via Specification or Discharge. Surfaced by Gemini and Grok (dual audit, 2026-06-21).

**4. Semantic Stability Check**
Scan for high-drift-risk terms. Flag as [FALLACY 4 — Semantic Drift]. Route to `Admin/Canonical_Terms.md`.

| Term | Risk |
|------|------|
| Recycling | Use Value Preservation or Material Recovery |
| Autonomous Decision-Making (unbound) | Obscures Axiom P-4 override visibility |
| High-RPM (on Gate_04) | Terminology bleed from Gate_05 |
| Canonical (unqualified) | Five distinct usages |
| Safe / Contained / Stable / Sufficient | Context-dependent — tighten or log |
| Scrap | Conflates material states |
| Specification (on Exploration content) | Implicit promotion |
| VERIFIED / PROVISIONAL / UNKNOWN | Must match EF-0.0 definitions exactly — do not use informally |

---

## Fallacy Checklist

Substantive notes required — bare checkmarks are not verification. Full text: `Admin/Auditor_Protocols.md`.

1. **Magic Energy** — Every watt needs a traceable origin. Cross-ref `Operations/Energy.md`.
2. **Friction Blindness** — Real systems degrade. Account for losses and wear.
3. **Energy Density Paradox** — Does recovery cost more than it produces?
4. **Semantic Drift** — Terms must match across all files and sessions. Route conflicts to `Admin/Canonical_Terms.md`.
5. **Scope Creep** — New capabilities belong in `Admin/Trajectories.md`.
6. **Hallucinated Files** — All cross-references must resolve against `Discovery.md`. Aspirational = labeled planned.
7. **Confidence Without Basis** — Label all numbers. Unlabeled = Placeholder.
8. **Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life.
9. **Incomplete by Omission** — What critical subsystem is missing?
10. **The Turd Problem** — Strip to one falsifiable sentence. Do not rename this.

---

## AI Contribution Rules

Role declaration required: "Operating as [Role] per Auditor_Protocols.md v0.8.1"

Valid roles: Skeptic/Auditor | Systems/Auditor | Evidence/Auditor | Ethical/Auditor | Synthesizer | Engineer | Connective Tissue

1. No Invented Files — confirm against `Discovery.md`.
2. Role Declaration — declare before contributing; declare shifts before proceeding.
3. Lineage Tracking — note what changed, why, what it replaces.
4. Refusal is Valid — flag flawed premises; do not refine them.
5. Confidence Labeling — four-label system. Unlabeled = Placeholder.
6. Inter-Agent Consistency — open with Assumption Extraction.
7. Repository Structure Awareness — use canonical folder-prefixed paths.
8. Epistemic State Labeling — claims that cannot reach VERIFIED must be labeled PROVISIONAL or UNKNOWN. Do not collapse epistemic states under optimization pressure.

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass by different agent to override.

| Gate | Test | Fail -> |
|------|------|---------|
| G1 | Fallacy Checklist actively applied with substantive notes? | Return to author |
| G2 | Physical plausibility — no violation of known constraints? | Return for revision |
| G3 | Adversarial Battery applied proportional to coupling/risk? | Return for adversarial analysis |
| G4 | Scope alignment — fits current version or trajectory? | Route to `Admin/Trajectories.md` |
| G5 | Cross-reference integrity — all paths use canonical folder-prefixed names? | Hold at draft |
| G6 | Conflict check — no contradiction with existing committed specs? | Resolve before committing |

Physical harness note (AP-010 pending): For documents with physical implementation claims, Gate 6 requires at least one confirmed cross-reference to an active test harness specifying test and grounding artifact. Documents without physical claims are exempt. Full doctrine pending AP-010 resolution.

**Full Stop Review triggers:** Same claim blocked across two cycles · New finding invalidates core premise of a promoted spec · Pattern of overrides eroding a governance principle · Multiple Adversarial Battery findings converging on the same structural gap · EF-0.2 Level 2 or Level 3 trigger activated.

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

## Governance Sidecar ID Reference

Non-obvious governance prefixes only. All operational prefixes: load `Discovery.md` or `Routing.md`.

| Prefix | Owning File |
|--------|-------------|
| AP-  | `Admin/Auditor_Protocols.md` |
| CT-  | `Admin/Canonical_Terms.md` |
| EC-  | `Admin/Ethical_Constraints.md` |
| FAK- | `Admin/Forge_Audit_Kit.md` |
| GOV- | `Admin/Governance_Charter.md` |
| RIP- | `Admin/Repository_Integrity_Protocol.md` |
| SEC- | `Admin/Security_Protocols.md` |

---

## Active Unknowns

Full registry: `Unknowns.md` v3.3

Critical watch items: AP-001-AP-007 (Systemic Risk — see Expiry Watch above) · CF-001 · CM-002 · EC cluster · EL-005 · EN-001 · EV-001 · FA-001 · FL-001 · FN-001 · FN-005 · GI-002 · GOV-003 · GOV-005 · LW-UNK-001 · LW-UNK-003 · PL-001 · PR-001 · RIP-001 · SD-UNK-004 · SEC-007 · TF-006 · TH-003 · WA-002

---

## How to Use

Load this file plus the document under audit. That is the baseline for every routine audit session.

Load additional files only when the audit focus requires them — each adds tokens. Candidates: `Admin/Auditor_Protocols.md` (full role doctrine, full EF constitutional text, full Adversarial Battery), `Unknowns.md` (full unknown detail), `Discovery.md` (path lookup, Rename Registry), target file's upstream architecture files.

Token ceiling note: `Admin/Auditor_Protocols.md` is approximately 72,000 characters at v0.8.1. Loading it alongside large target documents will approach the practical context ceiling for some models. Use this kit as the runtime reference; load the full source only when auditing `Admin/Auditor_Protocols.md` itself, onboarding a new agent, or when full EF constitutional text is required for an interpretive dispute.

Load full source documents instead of this kit when: auditing `Admin/Auditor_Protocols.md` itself · onboarding a new agent · full unknown entry detail required · EF section interpretive dispute.

**Maintenance trigger:** Update this file when `Admin/Auditor_Protocols.md` is revised OR when `Unknowns.md` version increments. Minimum fields to update: derivation version string, role declaration version string, critical watch list, Expiry Watch note, Epistemic Foundation condensed section if EF sections changed.

---

## Drift Indicators

- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- Derivation statement references a superseded `Admin/Auditor_Protocols.md` or `Unknowns.md` version
- Expiry Watch not updated at `Unknowns.md` version increment
- Role declaration version string does not match current `Admin/Auditor_Protocols.md` version
- Epistemic Foundation condensed section diverges from EF-0.0-EF-0.8b source text without documented rationale
- VERIFIED / PROVISIONAL / UNKNOWN used in this kit inconsistently with EF-0.0 definitions
- Governance sidecar ID reference contains stale or flat filenames
- Ethical Anchor absent or altered
- Kit character count exceeds 12,000 — flag for reduction pass

**Compound Drift Rule:** Multiple simultaneous indicators -> halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

**FAK-001** — Kit version maintenance trigger not formally owned. Maintenance trigger added to How to Use (v1.0). Formal ownership assignment still needed. Status: Open.

**FAK-004** — Index triage policy not formally ratified. v1.0 adopted Critical and Blocking as threshold; v1.1 replaced full index with critical watch list. Ratify in next audit cycle. Status: Open.

**FAK-005** — Kit character count exceeds 12,000-character reduction threshold. v1.2 reached ~16,400 characters following addition of Epistemic Foundation condensed reference. The 12k limit is a flag, not a hard block (per Drift Indicators). EF section was compressed to table format (~1,900 chars) to minimize growth. Baseline v1.1 was already approaching the limit. Resolution path: reduction pass targeting Governing Principles verbosity, Adversarial Priority Weighting, and Semantic Stability table — defer until next audit cycle when overall kit shape is clearer. Status: Open.

---

## Resolution Log

- 2026-06-21: **v1.2** — Derivation string updated to `Admin/Auditor_Protocols.md` v0.8.1. Role declaration version string updated to v0.8.1. Epistemic Foundation condensed reference section added (EF-0.0 through EF-0.8b summary). Audit Opening Checklist restructured: EF Integrity Check inserted as new Step 2; Expiry Watch becomes Step 3; Semantic Stability Check becomes Step 4. AP-001-AP-007 Systemic Risk escalation added to Expiry Watch. Physical harness gate note added to Verification Gates (AP-010 pending). Rule 8 (Epistemic State Labeling) added to AI Contribution Rules. VERIFIED / PROVISIONAL / UNKNOWN added to Semantic Stability drift-risk terms table. Token ceiling note added to How to Use. Scope Boundary updated to include Epistemic Foundation condensed reference. Three new Drift Indicators added. Last Audit date and Auditor field updated.

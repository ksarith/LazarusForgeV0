# Forge_Audit_Kit.md
**Version 1.1**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Last Audit     | 2026-06-17                                                          |
| Auditor        | Claude — Synthesizer; ChatGPT — Skeptic/Auditor                     |
| Open Unknowns  | See sidecar                                                         |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.7 | `Unknowns.md` v3.3

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Governing principles · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Audit Opening Checklist · Fallacy checklist · AI contribution rules · Verification gates · Sign-off format · Governance sidecar ID reference · How to use

**DOES NOT define:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`) · Full Adversarial Battery (→ `Admin/Auditor_Protocols.md`) · Unknown registry (→ `Unknowns.md`) · File paths and ownership (→ `Discovery.md`) · Dependency maps (→ `Unknowns.md`) · Governance hierarchy (→ `Admin/Governance_Charter.md`) · Ethical policy (→ `Admin/Ethical_Constraints.md`) · Canonical vocabulary (→ `Admin/Canonical_Terms.md`) · Kit evolution history (→ git log)

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`
> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`
> Verification seeks sufficient falsifiability, not exhaustive certainty.

Infinite audit recursion is a governance failure mode. Human override applies to process decisions only — not to `Admin/Ethical_Constraints.md` hard floors.

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

No internally-derived claim may be represented as operationally hardened without external validation. Full doctrine: `Admin/Auditor_Protocols.md` §AP-006.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high: Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure | Governance Authority

Partial Battery allowed for Exploration-stage if deferred classes are documented and no safety-critical claims are present.

---

## Audit Opening Checklist

Execute before every document review. Do not skip steps.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1–P-4, Q-1–Q-4) match prior committed version in `Admin/Governance_Charter.md`. Any unratified wording change = Constitutional violation → STATE_HOLD immediately.

**2. Expiry Watch**
Check `Unknowns.md` for Blocking entries approaching two-cycle threshold without a documented Resolution Path. Escalate to Systemic Risk or demote dependent module.

Current critical watch (v3.3): EC cluster approaching threshold · GOV-003 / GOV-005 Critical · RIP-001 Critical (GitHub releases are v0 path) · CF-001 In Progress (hardware prototype required) · SEC-007 Critical (above-repository decision required) · TF-006 Ethical_Constraints escalation candidate.

**3. Semantic Stability Check**
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

Critical watch items: CF-001 · CM-002 · EC cluster · EL-005 · EN-001 · EV-001 · FA-001 · FL-001 · FN-001 · FN-005 · GI-002 · GOV-003 · GOV-005 · LW-UNK-001 · LW-UNK-003 · PL-001 · PR-001 · RIP-001 · SD-UNK-004 · SEC-007 · TF-006 · TH-003 · WA-002

---

## How to Use

Load this file plus the document under audit. That is the baseline for every routine audit session.

Load additional files only when the audit focus requires them — each adds tokens. Candidates: `Admin/Auditor_Protocols.md` (full role doctrine, full Adversarial Battery), `Unknowns.md` (full unknown detail), `Discovery.md` (path lookup, Rename Registry), target file's upstream architecture files.

Load full source documents instead of this kit when: auditing `Admin/Auditor_Protocols.md` itself · onboarding a new agent · full unknown entry detail required.

**Maintenance trigger:** Update this file when `Admin/Auditor_Protocols.md` is revised OR when `Unknowns.md` version increments. Minimum fields to update: critical watch list, derivation version string, Expiry Watch note.

---

## Drift Indicators

- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- Derivation statement references a superseded `Unknowns.md` version
- Expiry Watch not updated at `Unknowns.md` version increment
- Governance sidecar ID reference contains stale or flat filenames
- Ethical Anchor absent or altered
- Kit character count exceeds 12,000 — flag for reduction pass

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

**FAK-001** — Kit version maintenance trigger not formally owned. Maintenance trigger added to How to Use (v1.0). Formal ownership assignment still needed. Status: Open.

**FAK-004** — Index triage policy not formally ratified. v1.0 adopted Critical and Blocking as threshold; v1.1 replaced full index with critical watch list. Ratify in next audit cycle. Status: Open.

# Forge_Audit_Kit.md
**Version 1.4**

## File State

| Field          | Value                                                               |
|----------------|---------------------------------------------------------------------|
| Status         | Draft                                                               |
| Spec Gates     | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                    |
| Last Audit     | 2026-06-24                                                          |
| Auditor        | Claude — Synthesizer                                                |
| Open Unknowns  | See sidecar                                                         |
| Ethical Anchor | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

**Derived from:** `Admin/Auditor_Protocols.md` v0.14 | `Unknowns.md` v4.0

When this file contradicts a full source document, the full source document prevails.

---

## Scope Boundary

**DOES define:** Governing principles · Epistemic Foundation condensed reference · Verification Maturity Model · Truth Provenance labels · Adversarial priority weighting · Audit Opening Checklist · Fallacy checklist · AI contribution rules · Verification gates · Sign-off format · Governance sidecar ID reference · How to use

**DOES NOT define:** Full auditor role doctrine (→ `Admin/Auditor_Protocols.md`) · Full EF constitutional text (→ `Admin/Auditor_Protocols.md` EF-0.0–EF-0.8b) · Full Adversarial Battery (→ `Admin/Auditor_Protocols.md`) · Unknown registry (→ `Unknowns.md`) · File paths and ownership (→ `Discovery.md`) · Governance hierarchy (→ `Admin/Governance_Charter.md`) · Ethical policy (→ `Admin/Ethical_Constraints.md`) · Canonical vocabulary (→ `Admin/Canonical_Terms.md`) · Kit evolution history (→ git log)

---

## Governing Principles

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`
> Confidence never outruns verification. — `Admin/Auditor_Protocols.md`
> Reality is sovereign. Every process, agent, metric, and protocol is merely an imperfect instrument attempting to approach it. — EF-0.0
> Verification seeks sufficient falsifiability, not exhaustive certainty.

Infinite audit recursion is a governance failure mode. Human override applies to process decisions only — not to `Admin/Ethical_Constraints.md` hard floors. The Epistemic Foundation (EF-0.0–EF-0.8b) is meta-constitutional and may not be amended without human ratification.

**Human Interaction Point Doctrine:** Human interaction points are coarse correction opportunities, not operational dependencies. The system degrades honestly to verified baselines under human unavailability — it does not suspend. Complexity lives inside the system; the interface to the human is deliberately simple. Full doctrine: `Admin/Auditor_Protocols.md` §Governing Principles.

---

## Epistemic Foundation — Condensed Reference

Full text: `Admin/Auditor_Protocols.md` EF-0.0–EF-0.8b. Runtime checklist only — source prevails on interpretive questions.

| Section | Core Rule |
|---------|-----------|
| EF-0.0 Epistemic Anchor | Reality > utility/consensus/elegance/coherence. All claims: VERIFIED / PROVISIONAL / UNKNOWN. Collapse UNKNOWN→VERIFIED without empirical input is prohibited. Reward falsification = reward confirmation. |
| EF-0.1 Epistemic Filter | Disqualified as evidence: fluency, agent consensus, systemic utility, precedent, correlation, repetition, confidence scores, compression. May generate hypotheses; never verify. |
| EF-0.2 Decay Triggers | L1 (confidence-accuracy mismatch / agent disagreement) → Red-Team. L2 (prediction failure / sycophancy loop) → Quarantine + autonomous degradation to verified baseline; human review when available. L3 (suppression / tampering / metric override) → Epistemic Reset + mandatory human governing party review. |
| EF-0.3 Epistemic Ledger | Five fields per state correction: Previous Premise · Contradictory Evidence · Falsification Method · Updated State · Confidence Interval. Created on falsification only. |
| EF-0.4 Auditor Fallibility | Auditor has no exemption from Axiom Zero. Auditor conclusions are PROVISIONAL. Guardians require guardians. |
| EF-0.5 Anti-Sacralization | No document immune from challenge — including this kit. Stability = repeated verification, not prestige. |
| EF-0.6 Goodhart's Law | Metrics are indicators, not objectives. No optimization overrides contradictory observations to preserve KPI. |
| EF-0.7 Process Supervision | Evaluate reasoning pathways, not outputs. Monitor Machiavellian Gap. Inspectable lineage required. |
| EF-0.8 SW Grounding | Code execution, telemetry, tool returns are the hard floor. Agent narratives about tool outputs are PROVISIONAL until tool confirmation logged. |
| EF-0.8b Physical Grounding | Sensor telemetry, assay outputs, measured physical constants supersede model/simulation/inference. Simulation confirming simulation is not grounding. |

---

## Verification Maturity Model

| State             | Operational Status         |
|-------------------|----------------------------|
| Exploration       | Not operational            |
| Candidate Spec    | Internal review only       |
| Provisional Spec  | Limited operational use    |
| Operational Spec  | Deployable                 |
| Hardened Doctrine | Trusted baseline           |

Promotion rule: assumptions narrow, unknowns shrink, external validation expands.

---

## Truth Provenance Labels

**Quantitative:** Measured | Estimated | Analogous | Placeholder — Unlabeled = Placeholder.

**Institutional:** Internally Derived | Analogous External | Experimentally Verified | Operationally Hardened

No internally-derived claim may be represented as Operationally Hardened without external validation. Full doctrine: `Admin/Auditor_Protocols.md` §AP-006.

---

## Adversarial Priority Weighting

Full Battery required when any factor is high: Irreversibility | Coupling | Energy Density | Autonomy | Silent Failure | Governance Authority

Partial Battery allowed for Exploration-stage if deferred classes are documented and no safety-critical claims are present.

---

## Audit Opening Checklist

Execute before every document review. Do not skip steps.

**1. Tier 1 Axiom Verification**
Confirm all eight axioms (P-1–P-4, Q-1–Q-4) match prior committed version in `Admin/Governance_Charter.md`. Any unratified wording change = Constitutional violation → STATE_HOLD immediately.

**2. Epistemic Foundation Integrity Check**
Confirm EF-0.0 through EF-0.8b text in `Admin/Auditor_Protocols.md` matches prior committed version. Any unratified modification = Integrity Violation (EF-0.2 Level 3) → STATE_HOLD immediately.

**3. Expiry Watch**
Check `Unknowns.md` for Blocking entries approaching two-cycle threshold without a documented Resolution Path. Escalate to Systemic Risk or demote dependent module. If AUDIT_HARNESS.py boundary index is present in session, use it — aging alerts are pre-computed. Otherwise load `Unknowns.md` directly.

**Current critical watch (v4.0):** AP-012 and AP-016 Critical (Gate 3 blocked pending Provisional Spec) · GOV-003 / GOV-005 Critical · RIP-001 Critical · CF-001 Blocking · SEC-007 Critical · EN-001 Blocking · WA-002 / WA-004 Critical · FA-001 Critical · EC-002 Critical · PR-001 Critical · EM-004 Critical · TF-006 Ethical_Constraints escalation candidate · LW-UNK-001 / LW-UNK-003 Critical safety gaps.

AP-001 through AP-007 Systemic Risk escalation active — all seven entries now carry resolution frameworks; formal downgrade requires human governing party confirmation at next audit cycle.

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
| Operational Blocking / Epistemic Blocking | Distinct subtypes — do not conflate; see `Admin/Canonical_Terms.md` v0.3 |

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

Role declaration required: *"Operating as [Role] per Auditor_Protocols.md v0.14"*

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

| Gate | Test | Fail → |
|------|------|--------|
| G1 | Fallacy Checklist actively applied with substantive notes? | Return to author |
| G2 | Physical plausibility — no violation of known constraints? | Return for revision |
| G3 | Adversarial Battery applied proportional to coupling/risk? | Return for adversarial analysis |
| G4 | Scope alignment — fits current version or trajectory? | Route to `Admin/Trajectories.md` |
| G5 | Cross-reference integrity — all paths use canonical folder-prefixed names? | Hold at draft |
| G6 | Conflict check — no contradiction with existing committed specs? | Resolve before committing |

**Gate 3 note:** At least one Battery class per promotion cycle must be applied by an agent with no session context from the current audit cycle (AP-017). Gate 3 currently blocked on AP-012 and AP-016 reaching Provisional Spec.

**Physical harness note (AP-010 pending):** For documents with physical implementation claims, Gate 6 requires at least one confirmed cross-reference to an active test harness specifying test and grounding artifact. Documents without physical claims are exempt.

**Full Stop Review triggers:** Same claim blocked across two cycles · New finding invalidates core premise of a promoted spec · Pattern of overrides eroding a governance principle · Multiple Adversarial Battery findings converging on the same structural gap · EF-0.2 Level 2 or Level 3 trigger activated.

---

## Resolved Unknown Discharge Procedure

Canonizes the pattern first applied at RIP-001 (`Admin/Repository_Integrity_Protocol.md`, discharged 2026-06-27) and retroactively corrected at RIP-004 (2026-07-02, see step 6 note). Applies whenever any unknown, any prefix, closes.

1. Sidecar entry stays permanently in the owning file's Auditor Notes & Unknowns — **never deleted.** The ID is the permanent search anchor; there is no centralized archive to fall back on (`Unknowns.md` retired that model at v4.3 — see its Resolution Log).
2. Status field → `Resolved — Discharge via Lessons Learned`.
3. Add a **Resolution** field to the sidecar entry: what closed it, when, why.
4. Add a **Lessons Learned** field to the same sidecar entry: the transferable pattern, not just the outcome — what would a future agent facing a similar unknown need to know.
5. Add a matching row to the owning file's own top-level Lessons Learned table — distilled and pattern-focused, not a duplicate of step 3.
6. `Unknowns.md`: remove from the active index; add one line to Expiry Watch or the Audit Trail pointing back to the sidecar. **Do not skip steps 2–5 and jump to step 6** — RIP-004 was closed correctly in substance on 2026-06-19 but skipped steps 2, 4, and 5 for six weeks before being brought into conformance.
7. Bump the owning file's Open Unknowns count and add a Resolution Log entry.

---

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
| AP-    | `Admin/Auditor_Protocols.md` |
| CT-    | `Admin/Canonical_Terms.md` |
| EC-    | `Admin/Ethical_Constraints.md` |
| FAK-   | `Admin/Forge_Audit_Kit.md` |
| GH-    | `Tests/Cognitive_Salvage_Layer.md` |
| GOV-   | `Admin/Governance_Charter.md` |
| RIP-   | `Admin/Repository_Integrity_Protocol.md` |
| SEC-   | `Admin/Security_Protocols.md` |

---

## How to Use

Load this file plus the document under audit. That is the baseline for every routine audit session.

Load additional files only when the audit focus requires them — each adds tokens. Candidates: `Admin/Auditor_Protocols.md` (full role doctrine, full EF constitutional text, full Adversarial Battery), `Unknowns.md` (full unknown detail), `Discovery.md` (path lookup, Rename Registry), target file's upstream architecture files.

**Token ceiling note:** `Admin/Auditor_Protocols.md` is approximately 95,000 characters at v0.14. Load it only when auditing the file itself, onboarding a new agent, or when full EF constitutional text is required for an interpretive dispute. This kit is the runtime reference for all other sessions.

**Load full source documents instead of this kit when:** auditing `Admin/Auditor_Protocols.md` itself · onboarding a new agent · full unknown entry detail required · EF section interpretive dispute.

**Maintenance trigger:** Update this file when `Admin/Auditor_Protocols.md` is revised OR when `Unknowns.md` version increments. Minimum fields to update: derivation version strings, role declaration version string, critical watch list, Expiry Watch note, EF condensed section if EF sections changed.

---

## Drift Indicators

- Governing principles, gates, or sign-off format diverge from `Admin/Auditor_Protocols.md`
- Derivation statement references a superseded version of `Admin/Auditor_Protocols.md` or `Unknowns.md`
- Expiry Watch not updated at `Unknowns.md` version increment
- Role declaration version string does not match current `Admin/Auditor_Protocols.md` version
- Epistemic Foundation condensed section diverges from EF-0.0–EF-0.8b source text without documented rationale
- VERIFIED / PROVISIONAL / UNKNOWN used inconsistently with EF-0.0 definitions
- Governance sidecar ID reference contains stale or flat filenames
- Ethical Anchor absent or altered
- Resolved unknown missing Lessons Learned narrative field, matching top-table row, or discharge status suffix (Resolved Unknown Discharge Procedure skipped)
- Kit character count exceeds 12,000 — flag for reduction pass

**Compound Drift Rule:** Multiple simultaneous indicators → halt autonomous progression, escalate for human review.

---

## Auditor Notes & Unknowns

**FAK-001** — Kit version maintenance trigger not formally owned. Maintenance trigger defined in How to Use. Formal ownership assignment still needed. Status: Open.

**FAK-004** — Index triage policy not formally ratified. Critical watch list approach adopted since v1.1. Ratify in next audit cycle. Status: Open.

**FAK-005** — Kit character count reduction pass complete at v1.3. Active Unknowns full list removed — replaced by critical watch summary in Expiry Watch step. Governing Principles compressed. Expiry Watch prose removed in favor of inline critical watch summary. Actual post-reduction count: ~16,950 chars. The 12,000-char ceiling is not achievable without removing load-bearing doctrine — EF condensed reference (~2,100 chars) and Audit Opening Checklist (~2,300 chars) are working content, not bloat. Ceiling flag remains active as a Drift Indicator. The 12,000 figure is the parameter that needs revisiting, not the content. Status: Open — ceiling flag active, reduction pass complete.

**FAK-006** — Resolved Unknown Discharge Procedure canonized here at v1.4 (2026-07-02) from organically-emerged RIP-001 practice, since no formal doctrine existed anywhere in the repository despite the pattern being in active use. Per this kit's own Scope Boundary, full auditor procedural doctrine belongs in `Admin/Auditor_Protocols.md` — this kit should carry only the condensed checklist form, consistent with every other section here. `Admin/Auditor_Protocols.md` was not available this session to receive the full version. Status: Open — condensed version live here; full-doctrine migration to `Admin/Auditor_Protocols.md` pending.

---

## Resolution Log

- 2026-06-21: **v1.2** — Derivation string updated to `Admin/Auditor_Protocols.md` v0.8.1. Epistemic Foundation condensed reference added. Audit Opening Checklist restructured. AP-001–AP-007 Systemic Risk escalation added. Physical harness gate note added. Rule 8 added to AI Contribution Rules. Token ceiling note added.
- 2026-06-24: **v1.3** — Derivation strings updated to `Admin/Auditor_Protocols.md` v0.14 and `Unknowns.md` v4.0. Role declaration version string updated to v0.14. Human Interaction Point Doctrine added to Governing Principles. EF-0.2 L2 entry updated to reflect autonomous degradation doctrine. Active Unknowns section removed — replaced by critical watch summary integrated into Expiry Watch step. AP Systemic Risk escalation note updated: all seven entries carry resolution frameworks; AP-006 and AP-009 Resolved; AP-012 and AP-016 Critical. GH- prefix added to Governance Sidecar ID Reference. Operational Blocking / Epistemic Blocking added to Semantic Stability table. Gate 3 note updated with AP-017 independence requirement and current block status. AP-010 physical harness note updated. Token ceiling note updated to reflect v0.14 character count. FAK-005 remains Open — actual post-reduction count ~16,950; ceiling parameter needs revisiting, not the content. Reduction pass complete.
- 2026-06-27: **v1.3 patch** — Spec Gates (0/6) and Verification Ref (Admin/Verification_Gates_LF.md) added to File State block. Phase 1 enforcement (AUDIT_HARNESS.py v11) flagged missing fields — all repository documents follow the same File State schema, no exceptions for meta documents.
- 2026-07-02: **v1.4** — Resolved Unknown Discharge Procedure section added, canonizing the RIP-001 pattern (permanent sidecar retention, Resolution + Lessons Learned narrative fields, matching top-table row, one-line Unknowns.md pointer — no centralized archive). Placed between Verification Gates and Sign-Off Format. Matching Drift Indicator added. FAK-006 logged — condensed version lives here per Scope Boundary; full doctrine migration to `Admin/Auditor_Protocols.md` still pending (file unavailable this session). Prompted by retroactive correction of RIP-004's discharge record, which had skipped the Lessons Learned narrative field and matching table row for six weeks despite being correctly resolved in substance.

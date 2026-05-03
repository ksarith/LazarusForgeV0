# Forge_Audit_Kit.md
**Condensed audit reference for LazarusForgeV0 multi-agent cycles.**
**Replaces loading Auditor_Protocols.md + Unknowns_LF.md in routine audit prompts.**
**Current as of: Auditor_Protocols v0.4 / Unknowns_LF v0.8 — May 2026**

Full reference files: `Auditor_Protocols.md` | `Unknowns_LF.md`

---

## GOVERNING PRINCIPLES

> Capability never outruns permission. — `Ethical_Constraints.md`
> Confidence never outruns verification. — `Auditor_Protocols.md`

**Scope boundary:** Human override rights apply to verification process decisions only. They do not extend to hard-line doctrines in `Ethical_Constraints.md` (Anti-Weaponization, Life Preservation).

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
**6. Hallucinated Files** — All cross-references must resolve to real files. Aspirational = labeled planned.
**7. Confidence Without Basis** — All numbers must be labeled: **Measured** / **Estimated** / **Analogous** / **Placeholder**. Unlabeled = Placeholder.
**8. Lifecycle Truncation** — Every module spec needs: Degraded Operation, Failure Modes, Maintenance Access, End-of-Life path.
**9. Incomplete by Omission** — What critical subsystem is missing? Heat dissipation, waste streams, power draw, human interface?
**10. The Turd Problem** — Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this.

*Full reference: `Auditor_Protocols.md` §The Fallacy Checklist*

---

## AI CONTRIBUTION RULES

**Role declaration required:** *"Operating as [Role] per Auditor_Protocols.md v0.4"*
**Roles:** Synthesizer | Engineer | Skeptic/Auditor | Connective Tissue

**Rule 1 — No Invented Files:** Never reference unconfirmed files. State uncertainty explicitly.
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

**Full Stop Review:** Invoke if a spec passes all gates but exhibits systemic inconsistency. Trigger conditions: (1) same foundational claim blocked across two separate cycles; (2) new finding invalidates a previously promoted spec; (3) pattern of overrides eroding a governance principle. Log: triggering agent, one falsifiable sentence, date, outcome.

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

Open this section at the start of each audit cycle. Check for entries past two cycles.

**Version cycle definition:** One completed multi-agent audit pass with findings logged.
**Expiry check owner:** Skeptic/Auditor role, at cycle opening.

*(No entries flagged at v0.8 — all within first or second cycle.)*

---

## ACTIVE UNKNOWNS — Open / In Progress

*Deferred and Resolved entries omitted. Full registry: `Unknowns_LF.md`*

---

### Governance & Verification Cluster

| ID | Title | Owner | Priority (Promo) | Status |
|---|---|---|---|---|
| UNK-001 | Discovery.md update pending for Unknowns_LF.md | Connective Tissue | Non-blocking | Open |
| UNK-004 | Expiry Rule enforcement mechanism | Skeptic/Auditor | Blocking | Deferred (post-audit-cycle) |
| UNK-020 | Auditor effectiveness metrics | Skeptic/Auditor | Blocking | In Progress |
| UNK-021 | Override vs. immutability reconciliation | Skeptic/Auditor | Blocking | In Progress |
| UNK-023 | Audit trail schema | Engineer | Blocking | In Progress |

---

### Ethics & Governance Cluster

| ID | Title | Owner | Priority (Promo) | Status |
|---|---|---|---|---|
| UNK-013 | "Sufficient confidence" threshold undefined | Skeptic/Auditor | Blocking | Open |
| UNK-014 | Anti-Weaponization pattern-matching undefined | Engineer | Blocking | In Progress |
| UNK-015 | Human escalation path undefined | Autonomy/Engineer | Blocking | In Progress |
| UNK-016 | Governance failure modes unspecified | Skeptic/Auditor | Blocking | In Progress |
| UNK-017 | Life-preservation vs. Anti-Weaponization priority | Human governing party | Blocking | In Progress |
| UNK-018 | Ethical log survival at depth | Engineer | Non-blocking | Open |
| UNK-019 | Governance fail-safe behavior | Skeptic/Auditor | Blocking | In Progress |

---

### Gate Logic & Triage Cluster

| ID | Title | Owner | Priority (Promo) | Status |
|---|---|---|---|---|
| UNK-012 | Gate logic determinism | Engineer | Blocking | In Progress |
| UNK-022 | Full Stop Review trigger conditions | Skeptic/Auditor | Blocking | Resolved |
| UNK-024 | "Sufficient for forge duty" threshold | Engineer | Blocking | Open |
| UNK-025 | Contamination routing protocol | Engineer | Blocking | Open |

---

### Energy & Power Cluster

| ID | Title | Owner | Priority (Promo) | Status |
|---|---|---|---|---|
| UNK-011 | Forge power demand uncharacterized | Energy | Blocking | In Progress |
| UNK-007 | Deep-ocean storage degradation unacknowledged | Energy | Blocking | Open |

---

### Leviathan / Autonomy Cluster

| ID | Title | Owner | Priority (Promo) | Status |
|---|---|---|---|---|
| UNK-006 | Leviathan power envelope — no placeholder | Energy | Blocking | Open |
| UNK-008 | Leviathan autonomy architecture unspecified | Autonomy | Blocking | Open |
| UNK-009 | Trust model mechanism undefined | Autonomy | Blocking | Open |
| UNK-010 | Priority propagation has no mechanism | Autonomy | Blocking | Open |

---

### Future / Deferred Cluster

| ID | Title | Status |
|---|---|---|
| UNK-003 | Cross-repo assumption contracts | Deferred (Leviathan milestone) |
| UNK-005 | Marine G.E.C.K. seed variant | Open (Exploratory) |

---

## DEPENDENCY MAP (condensed)

```
UNK-011 → UNK-006 → UNK-008 → UNK-009 / UNK-010 / UNK-015
UNK-007 → feeds UNK-006 (parallel)
UNK-024 → feeds UNK-012 resolution
UNK-013 → UNK-008 / UNK-019
UNK-016 → UNK-019
UNK-023 → UNK-020
UNK-004 → UNK-020 / UNK-023
```

*Full map with descriptions: `Unknowns_LF.md` §Dependency Map*

---

## HOW TO USE THIS FILE

**In Colab Cell 2, replace:**
```python
FILES = [
    "[document_to_audit]",
    "Auditor_Protocols.md",   # 25k chars
    "Unknowns_LF.md",         # 32k chars
]
```

**With:**
```python
FILES = [
    "[document_to_audit]",
    "Forge_Audit_Kit.md",     # ~8k chars
]
```

**When to load full files instead:**
- Auditing `Auditor_Protocols.md` itself → load `Auditor_Protocols.md`
- Auditing `Unknowns_LF.md` itself → load `Unknowns_LF.md`
- Onboarding a new agent or contributor → load both full files
- Any finding that needs full unknown entry detail → load `Unknowns_LF.md`

**Maintenance:** Update this file when `Unknowns_LF.md` version increments. Changes needed: update active unknowns tables, move resolved entries to Resolved column, update version header. The Fallacy Checklist, Gates, and Rules sections only change when `Auditor_Protocols.md` is revised.

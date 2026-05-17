# Auditor_Protocols.md — Verification & Hallucination Filter
**Version 0.5**

**Audit Health:**
- Status: Specification (governing document)
- Last audit: 2026-05-04 (Multi-model — Claude, ChatGPT, Gemini, Grok)
- Open unknowns: 3 (Medium) — see sidecar
- Sidecar: [#auditor-notes--unknowns]

---

## Purpose

This document defines the verification protocols for all contributors to the Lazarus Forge — human, AI, or multi-agent workflow. Its purpose is to ensure that what enters the repository as specification has been pressure-tested, not merely generated.

Polished outputs are a known failure mode. Unverified content is not eligible for specification.

This file governs how claims are checked, how contributions are audited, and how the multi-agent workflow maintains integrity across sessions and contributors.

**This document is subject to its own protocols.** The gate logic, checklist, and audit trail requirements apply to revisions of this document as much as to any other.

---

## Governing Principle

> Capability never outruns permission. — `Ethical_Constraints.md`

The auditor equivalent:

> Confidence never outruns verification.

These two principles operate in parallel. One governs what the Forge is allowed to do. The other governs what the Forge is allowed to claim.

**Scope boundary:** Human override rights under this protocol apply to verification process decisions only. They do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in `Ethical_Constraints.md`.

---

## Exploration vs. Specification

**Exploration** — Allowed to be incomplete, speculative, and loosely connected. Do not over-police.

**Specification** — Must pass all verification gates before commit. Claims are binding, cross-references must resolve, and quantitative values must be labeled.

**The loophole guard:** Exploratory documents making implicit performance claims must be treated as specification candidates for those claims. The Exploration label does not shield implicit guarantees.

**Design rule:** These protocols apply only when promoting content toward specification. Misapplying verification pressure to exploratory thinking is itself a failure mode.

---

## The Fallacy Checklist

Apply to all specification-level claims. Bare checkmarks are not verification — substantive notes required for non-trivial claims (1–2 sentences minimum stating what was checked, what nearly failed, and what was adjusted).

**1. Magic Energy**
Does the design assume energy is available without accounting for its source, storage, or conversion losses? Every watt must have a traceable origin. Cross-reference `energy_v0.md`.

**2. Friction Blindness**
Does the design ignore mechanical resistance, thermal losses, fluid drag, or interface wear? Real systems degrade. Specifications that assume ideal conditions are not specifications — they are wishes.

**3. Energy Density Paradox**
Does any recovery, recycling, or bootstrapping step consume more than it produces? Justify as enabling investment or flag. Recovery that costs more than it recovers is reduction dressed as progress.

**4. Semantic Drift**
Has a term changed meaning between documents without a documented revision? Cross-check against `Lazarus_forge_v0_flow.md` as the reference standard.

**5. Scope Creep Disguised as Refinement**
Does a revision quietly expand claimed capabilities beyond what the current version can demonstrate? New capabilities belong in `Trajectories_LF.md`.

**6. Hallucinated Files or Cross-References**
Does the document reference a file that does not exist? All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified. Aspirational references must be labeled planned.

**7. Confidence Without Basis**
All quantitative claims must carry one of four labels:
- **Measured** — derived from real experimental data
- **Estimated** — derived from analog systems with documented scaling factors
- **Analogous** — drawn from similar documented systems
- **Placeholder** — provisional, pending verification

Unlabeled numbers are assumed Placeholder. False precision labeled "estimated" is still a violation.

**8. Lifecycle Truncation**
Every module specification must include: Degraded Operation, Failure Modes & Detection, Maintenance Access, End-of-Life / Recycling Path. A specification describing only the working state is incomplete.

**9. Incomplete by Omission**
What critical subsystem is missing? Common omissions: heat dissipation, waste stream management, human interface requirements, power draw under load. Absence of mention is not evidence of absence of need.

**10. The Turd Problem**
Strip to one falsifiable sentence. Does the foundation survive adversarial reduction? Do not rename this. It is memorable and functionally precise.

---

## AI Contribution Protocols

**Role declaration required:**
> *"Operating as [Role] per Auditor_Protocols.md v0.5"*

Roles: **Synthesizer** | **Engineer** | **Skeptic/Auditor** | **Connective Tissue**

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed. State uncertainty for anything else.

**Rule 2 — Role Awareness:** Name role shifts before proceeding.

**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.

**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them. Refusal is a success of the protocol.

**Rule 5 — Confidence Labeling:** Use the four-label system. Unlabeled = Placeholder.

**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades.

**Trust the process, not the predecessor.**

---

## Human Contributor Protocols

- Label estimates as estimates. "I think it works" is not a specification claim.
- Resolve all cross-references before committing. Planned files must be explicitly labeled.
- Overrides of AI auditor flags must be documented with reasoning. Undocumented overrides are indistinguishable from ignored warnings.
- Override rights apply to verification process decisions — not to Ethical_Constraints hard-line doctrines.
- Lifecycle template (Fallacy #8) applies to human-authored module specs.

---

## Decentralized Audit Architecture (Sidecar Model)

*Introduced v0.5. Addresses metadata bloat and token-limit failures.*

### The Problem

A centralized unknowns registry that stores full entry detail grows without bound. When it exceeds practical token limits, the governance system fails the thing it governs.

### Local Ledgers + Global Index

**Local Ledger (Sidecar):** Every specification file contains an `## Auditor Notes & Unknowns` section at the footer. Module-specific unknowns live here.

**Global Index:** `Unknowns_LF.md` is a cross-module index only — summary table, dependency map, systemic risks spanning multiple files, audit trail, resolved archive. Full entry detail lives in the owning file's sidecar.

### Audit Health Header

Every file carries an Audit Health Header immediately below the title:

```
**Audit Health:**
- Status: [Exploration | Draft | Specification]
- Last audit: [YYYY-MM-DD] ([Agent — Role])
- Open unknowns: [N] ([Low | Medium | High])
- Sidecar: [#auditor-notes--unknowns]
```

### Sidecar Format

```markdown
---

## Auditor Notes & Unknowns

### [FILE-PREFIX-NNN] — Short title
**Status:** Open | In Progress | Resolved
**Risk:** Low | Medium | High
**What is not yet known:** [one sentence]
**Resolution path:** [one sentence]
**Logged:** [YYYY-MM-DD, Agent — Role]

### Resolution Log
- [YYYY-MM-DD]: [FILE-PREFIX-NNN] — [one-line resolution description]
```

Local IDs use file abbreviation + three digits: `AP-001` (Auditor Protocols), `SC-001` (Spin Chamber), `EC-001` (Ethical Constraints), etc. Cross-module unknowns use global `UNK-XXX` format and are indexed in `Unknowns_LF.md`.

### The 10-Entry Rule

More than 10 distinct open entries in a sidecar flags the file for a Resolution Pass before the next audit cycle.

### Metadata Guardrail

If sidecar content exceeds 20% of total document word count, flag for Resolution Pass before auditing. Flag is strong — not a hard refusal. Proceed if human contributor explicitly acknowledges.

### Resolution and Expungement

- **Payment via Specification** — content moves into the document body as committed spec; entry moves to Resolution Log
- **Discharge via Trajectory** — out of current version scope; route to `Trajectories_LF.md`; note in Resolution Log
- **Discharge via Lessons Learned** — resolved by operational experience; lesson moves to Lessons Learned section; entry closes

**Crystallization principle:** Every unknown that moves from sidecar into specification body makes the document more deterministic. A shrinking sidecar is a maturing document.

---

## Unknowns Registry

*In v0.5, this section governs global index behavior. Local sidecar format is defined above.*

**Where unknowns live:**
- Module-specific — in the file's own sidecar
- Cross-module — in `Unknowns_LF.md` global index, owning file noted
- Navigation — in `Discovery.md`

**Global index format:**

| ID | Title | Owning file | Status | Priority (Promotion) |
|---|---|---|---|---|
| UNK-XXX | Short title | `filename.md` | Open/In Progress/Deferred | Blocking/Non-blocking |

**Priority tags:** Blocking | Non-blocking | Exploratory

**The Expiry Rule** is retained as a backstop for cross-module unknowns in the global index. It is no longer the primary mechanism for managing unknown accumulation — the Sidecar Model's 10-entry rule and metadata guardrail address that structurally. For global index entries: if a Blocking or Non-blocking unknown remains without a documented Resolution Path for more than two audit cycles, escalate to Systemic Risk or demote the dependent module.

**Expiry check:** Skeptic/Auditor role opens each audit cycle by reviewing the global index for entries approaching two cycles.

A verification pass that surfaces no unknowns on a complex document should itself be treated with suspicion.

---

## Cross-Repo Verification

*Astroid-miner is a planned repository, intentionally deferred until Leviathan deployment is underway. Cross-repo verification applies to `Lazarus-Forge-` now; Astroid-miner activates at that milestone.*

Any cross-repo dependency must be documented in both repositories with a stated assumption contract. The dependency is not verified until both sides acknowledge it.

---

## Verification Gates

Sequential. Auditor has binding block authority. Self-approval loops not permitted. Blocks require documented rebuttal and second-pass audit by a different agent to override.

| Gate | Test | Fail → |
|---|---|---|
| 1 — Fallacy Check | Checklist actively applied with substantive notes? | Return to author |
| 2 — Verification Artifacts | At least one falsifiable artifact per significant claim? | Return for artifact generation |
| 3 — Adversarial Pass | At least one concrete failure scenario tested? | Must undergo adversarial testing |
| 4 — Scope Alignment | Fits current version or future trajectory? | Route to `Trajectories_LF.md` |
| 5 — Cross-Reference Integrity | All file refs resolve? Cross-repo deps bidirectional? | Hold at draft |
| 6 — Conflict Check | Contradicts existing committed specs? | Resolve conflict before committing |

---

## Full Stop Review

Invoke when a spec passes all gates but exhibits systemic inconsistency or unclear real-world viability. Resets to Gate 1 with focus on foundational premise.

**Trigger conditions:**
1. Same foundational claim blocked across two separate audit cycles
2. New finding invalidates core premise of a previously promoted specification
3. Pattern of documented overrides eroding a governance principle without explicit revision

**Invocation record:** Triggering agent, triggering concern (one falsifiable sentence), date and document version, outcome. Record belongs in the document's sidecar audit trail.

---

## Observability & Audit Trail

**Required audit trail fields:**
- Document audited and version
- Auditor role and agent identity
- Date or audit cycle identifier
- Gates cleared (list)
- Gates blocked (list with reason)
- Unknowns logged (IDs)
- Overrides recorded (with justification)
- Sign-off statement

**Standard sign-off:**
> *"Verified under Auditor_Protocols v0.5 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides. Auditor: [Role/Agent]"*

*Note: Machine-readable audit trail schema (JSON/YAML) is deferred — see AP-003 in sidecar.*

---

## Protocol Performance (Placeholder)

*Metrics are Placeholder pending first full audit cycle completion.*

**Target metrics:**
- Productive block ratio — fraction of blocks resulting in documented improvement
- False-positive refusal rate — blocks overridden with documented justification
- Drift incidents detected per cycle

**Anti-Auditor-Capture:** For high-stakes documents, rotate the Auditor role to a different agent model across successive cycles. An auditor reviewing the same document repeatedly without finding new issues warrants the same suspicion as a verification pass surfacing no unknowns.

---

## Failure Modes of This Document

**Checklist Theater** — Verification becomes ritual. Mitigated by requiring substantive notes.

**Auditor Capture** — Skeptic role softens. Mitigated by binding block authority, documented rebuttal, second-pass requirement, and Auditor rotation.

**Version Freeze** — Document stops updating. Mitigated by explicit revision triggers and self-application of gates.

**Exploration Suppression** — Verification pressure applied too early. Mitigated by the Exploration vs. Specification distinction.

**Over-Engineering the Audit** — If a verification cycle takes longer than writing the contribution, the protocol has failed. Simplicity is a design constraint.

**Coherent Nonsense** — Passes all gates but is systemically wrong. Mitigated by Full Stop Review.

**Metadata Bloat** — Centralized registries grow without bound and become obstacles. Mitigated by the Sidecar Model introduced in v0.5.

**Meta-Recursion Gap** — The protocol cannot fully audit its own enforcement. Mitigated by self-application of gates on revision, Protocol Performance metrics, and Auditor rotation. Acknowledged as an irreducible residual risk.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Centralized Unknowns_LF.md as full-entry store | File grew past token limits; audit prompts failed | Unknowns must live locally in owning files; central registry is index only |
| May 2026 | Expiry Rule as primary accumulation mechanism | Rule had no enforcement path; unknowns aged silently | Structural constraints (10-entry rule, sidecar) work better than procedural rules |
| May 2026 | Preparatory framing lines in audit prompts | Softened auditor findings; masked genuine gaps | Documents must stand on their own; scaffolding that stays up becomes load-bearing |

---

## Auditor Notes & Unknowns

### AP-001 — Auditor effectiveness metrics not yet measured
**Status:** Open
**Risk:** Medium
**What is not yet known:** How to measure whether the audit process is actually adding value — productive block ratio, false-positive refusal rate, drift incidents detected per cycle.
**Resolution path:** Metrics defined as Placeholder in Protocol Performance section. Activate measurement after first full audit cycle completes. Collect via sidecar audit trail entries across all documents.
**Logged:** 2026-05-04, Multi-model audit cycle

### AP-002 — Override vs. immutability boundary not yet confirmed in both documents
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** Whether the clarification that human override rights do not extend to Ethical_Constraints hard-line doctrines is explicitly stated in both documents in a mutually consistent way.
**Resolution path:** Scope boundary added to this document (v0.5 Governing Principle section). Requires confirmation that matching language exists in Ethical_Constraints.md v0.3. Close when both documents are committed with consistent language.
**Logged:** 2026-05-04, Multi-model audit cycle

### AP-003 — Audit trail schema (machine-readable) deferred
**Status:** Open
**Risk:** Low
**What is not yet known:** A machine-readable format (JSON/YAML) for recording gate passages, blocks, and overrides that can be queried and compared across audit cycles.
**Resolution path:** Structured markdown format (required fields + example) added to Observability section. JSON/YAML deferred until tooling exists to consume it. Exploratory priority — activate when first cross-cycle pattern analysis is needed.
**Logged:** 2026-05-04, Multi-model audit cycle

### Resolution Log

- 2026-05-04: **UNK-004 (Expiry Rule enforcement mechanism)** — Discharged. Sidecar Model (v0.5) addresses the underlying accumulation problem structurally. Expiry Rule retained as backstop for global index only, where it functions without needing a separate enforcement mechanism. No longer requires implementation.
- 2026-05-04: **UNK-022 (Full Stop Review trigger conditions)** — Resolved. Three specific trigger conditions and invocation record format added to Full Stop Review section.

---

## Relationship to Existing Documents

- `Ethical_Constraints.md` — parent document; governs permission; hard-line doctrines not subject to override by this protocol
- `Lazarus_forge_v0_flow.md` — structural model; reference standard for shared terminology
- `Trajectories_LF.md` — destination for scope creep that proves to be valid future work
- `leviathan_testing.md` — primary stress-test environment; where Protocol Performance metrics will first be collected
- `Discovery.md` — navigation layer; confirmed file list
- `Unknowns_LF.md` — global index for cross-module unknowns (index only as of v0.5)
- `Forge_Audit_Kit.md` — condensed audit reference for routine multi-agent cycles
- `LF_File_Template.md` — standard file structure for all repository documents
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

Version 0.5 — consolidates all additions from v0.4 and Sidecar Amendment.

**Changes from v0.3:**
- Added scope clarification: human override rights do not extend to Ethical_Constraints hard-line doctrines
- Added version cycle definition and Expiry check to Unknowns Registry (now backstop only)
- Added Assumption Extraction requirement to Rule 6
- Added Full Stop Review trigger conditions and invocation record format
- Added required fields to Observability & Audit Trail
- Added Protocol Performance section as Placeholder
- Added Decentralized Audit Architecture (Sidecar Model) — local ledgers, Audit Health Header, 10-entry rule, metadata guardrail, Resolution and Expungement
- Added Lessons Learned section
- Added sidecar with AP-001, AP-002, AP-003 migrated from global registry
- Discharged UNK-004 (Expiry Rule) and UNK-022 (Full Stop Review triggers) in Resolution Log
- Unknowns Registry updated to govern global index behavior only
- Relationship section updated: Unknowns_LF.md role clarified, Forge_Audit_Kit.md and LF_File_Template.md added
- Added Metadata Bloat and Meta-Recursion Gap to Failure Modes
- Fallacy Checklist condensed without losing substance

**What must remain constant:**

**Confidence never outruns verification.**

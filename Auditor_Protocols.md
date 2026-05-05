# Auditor_Protocols.md — Verification & Hallucination Filter
**Version 0.5**

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

**Scope of this document:** This document governs verification of contributions. It does not govern the ethical constraints defined in `Ethical_Constraints.md`. Human override rights under this protocol apply to verification process decisions — they do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in the parent governance document.

---

## Exploration vs. Specification

Not everything in this repository is heading toward specification. This distinction must be explicit before any verification gate is applied.

**Exploration** — Allowed to be incomplete, speculative, and loosely connected. Exploratory content is generative and should not be over-policed. Discovery.md energy lives here.

**Specification** — Must pass all verification gates before commit. Claims are binding, cross-references must resolve, and quantitative values must be labeled.

**The loophole guard:** Exploratory documents that make implicit performance claims or system guarantees must be treated as specification candidates and routed through verification gates. The exploration label does not shield a document that is already making spec-level claims.

**Design rule:** These protocols apply only when promoting content toward specification. They do not constrain early-stage exploration. Misapplying verification pressure to exploratory thinking is itself a failure mode.

---

## The Fallacy Checklist

Before any technical claim, specification, or design decision is committed to the repository, it must be checked against this list. A single unresolved item is sufficient grounds to hold the document at draft status.

Checking means active engagement — not passive agreement. For non-trivial claims or when promoting to specification, each item must include a brief note (1–2 sentences minimum, substantive) stating what was checked, what nearly failed, and what was adjusted if anything. A bare checkmark is not verification.

**1. Magic Energy**
Does the design assume energy is available without accounting for its source, storage, or conversion losses? Every watt must have a traceable origin. Cross-reference `energy_v0.md`.

**2. Friction Blindness**
Does the design ignore mechanical resistance, thermal losses, fluid drag, or interface wear? Real systems degrade. Specifications that assume ideal conditions are not specifications — they are wishes.

**3. Energy Density Paradox**
Does any recovery, recycling, or bootstrapping step consume more energy, compute, or resources than the usable value it produces in the target loop? If so, it must be explicitly justified as an enabling investment for a larger closed system — not presented as net-positive on its own. Recovery that costs more than it recovers is reduction dressed as progress.

**4. Semantic Drift**
Has a term changed meaning between documents without a documented revision? Terms must mean the same thing everywhere they appear, or differences must be explicitly noted. Cross-check shared vocabulary against `Lazarus_forge_v0_flow.md` as the reference standard.

**5. Scope Creep Disguised as Refinement**
Does a proposed revision quietly expand the system's claimed capabilities beyond what the current version can demonstrate? New capabilities belong in `Trajectories_LF.md` as future versions, not embedded silently into v0 specifications. Exception: if a refinement adds optionality or modularity without increasing claimed performance, it may remain in v0 — but must be explicitly marked as non-binding for current demonstration requirements.

**6. Hallucinated Files or Cross-References**
Does the document reference a file, module, or specification that does not exist in the repository? All cross-references must resolve to real files. Aspirational references must be labeled explicitly as planned. Files confirmed in `Discovery.md` are treated as verified. The Discovery.md raw link architecture exists to prevent this failure mode — use it.

**7. Confidence Without Basis**
Does the document state quantitative targets without citing a source, analog system, or experimental basis? All quantitative claims must carry one of four labels:
- **Measured** — derived from real experimental data
- **Estimated** — derived from analog systems with documented scaling factors; must include order-of-magnitude justification or bounding ranges, not single-point values
- **Analogous** — drawn from similar terrestrial or documented systems where direct measurement is unavailable
- **Placeholder** — provisional, pending verification

Unlabeled numbers are assumed to be placeholders. False precision labeled as "estimated" is still a violation.

**8. Lifecycle Truncation**
Does the design account for failure, maintenance, end-of-life, and waste streams? A specification that describes only the working state is incomplete. Every module specification must include at minimum:

- Degraded Operation — what happens as the module ages or partially fails
- Failure Modes & Detection — how failure presents and how it is caught
- Maintenance Access — what servicing looks like
- End-of-Life / Recycling Path — where the module goes when it is truly exhausted

**9. Incomplete by Omission**
Does the document imply a complete system while silently omitting critical subsystems? Common omissions include heat dissipation, waste stream management, human interface requirements, and power draw under load. If a document describes a system without accounting for what surrounds it, the Auditor must flag it as incomplete by omission. Absence of mention is not evidence of absence of need.

**10. The Turd Problem**
Does the document take a fundamentally flawed premise and develop it with increasing sophistication? Sophisticated presentation does not redeem a bad foundation. It has been said, "You can't polish a turd!"

Test: Strip away all engineering detail and state the core claim in a single falsifiable sentence. Present that sentence to a skeptical domain expert or adversarial prompt. If the foundation cannot survive that reduction, no amount of downstream refinement recovers it.

Do not rename this. It is memorable and functionally precise.

---

## AI Contribution Protocols

When any AI model contributes content — whether Claude, Gemini, Grok, ChatGPT, or any future system — the following rules apply.

**Role Declaration (Required)**
Every significant AI-generated contribution must open with a brief role declaration:
> *"Operating as [Role] per Auditor_Protocols.md v0.5"*

This creates an audit hook and prevents silent role drift. Roles are not rigid but shifts must be named, not suppressed.

Assigned roles:

- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence
- **Engineer** — translates concepts into operational specifications
- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions, adversarial testing
- **Connective Tissue** — links community discussion to repository evolution

**Rule 1 — No Invented Files**
AI models must not reference, summarize, or describe files that have not been confirmed to exist in the repository. Files listed in `Discovery.md` are confirmed. If uncertain about any other file, state uncertainty explicitly.

**Rule 2 — Role Awareness**
Operate within the declared role. If operating outside it, name the shift explicitly before proceeding.

**Rule 3 — Lineage Tracking**
Significant changes must note what changed, why it changed, and what prior version it replaces. This is the audit trail that distinguishes a living document from a drifting one.

**Rule 4 — Refusal is Valid**
A model that identifies a flawed premise must flag it rather than refine it. Refusal is not a failure of the AI — it is a success of the protocol. A model that refuses to polish a bad foundation has cleared Gate 1. The workflow must prioritize redirection over completion of the original task.

**Rule 5 — Confidence Labeling**
All quantitative claims must use the four-label system defined in the Fallacy Checklist. Unlabeled numbers are placeholders by default.

**Rule 6 — Inter-Agent Consistency**
At handoff between agents, the receiving agent must explicitly query prior contributions for unstated assumptions before proceeding. Open with a brief Assumption Extraction statement: *"Prior contributions assumed: [list key assumptions]. These are carried forward unless contradicted by new findings."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades.

**Trust the process, not the predecessor.**

---

## Human Contributor Protocols

These protocols apply equally to human contributors. The document governs contributions, not contributor type.

- Humans must label estimates as estimates. "I think it works" is not sufficient basis for a specification claim.
- Humans must resolve all cross-references before committing. Linking to a planned file requires an explicit planned label.
- Humans may override AI auditor flags — but overrides must be documented with reasoning. An undocumented override is indistinguishable from an ignored warning.
- Human override rights apply to verification process decisions. They do not extend to hard-line doctrines defined in `Ethical_Constraints.md`.
- The lifecycle template in Fallacy Checklist item 8 applies to human-authored module specs as well.

---

## Decentralized Audit Architecture (Sidecar Model)

*Added v0.5. Addresses metadata bloat and token-limit failures in multi-agent audit cycles.*

### The Problem

A centralized `Unknowns_LF.md` that stores full entry detail for all unknowns grows without bound as audit cycles accumulate. When this file exceeds practical token limits, the audit system fails — the file that governs verification becomes an obstacle to verification.

### The Solution: Local Ledgers + Global Index

**Local Ledger (Sidecar):** Every technical specification file must contain an `## Auditor Notes & Unknowns` section at the footer. Module-specific unknowns live here, not in the global registry.

**Global Index:** `Unknowns_LF.md` is repurposed as a cross-module index. It contains:
- A summary table of all active unknowns (ID, title, owning file, status, priority)
- The dependency map
- Systemic risks that span multiple files
- Audit trail
- Resolved archive

Full entry detail lives in the owning document's sidecar. The global index points to it.

### Audit Health Header

Every file must include an Audit Health Header immediately below the title:

```
**Audit Health:**
- Status: [Exploration | Draft | Specification]
- Last audit: [date] ([Agent-Role])
- Open unknowns: [N] ([risk level: Low | Medium | High])
- Sidecar: [#auditor-notes-unknowns]
```

This allows agents to assess a file's audit state without reading the full document, and to jump directly to the sidecar when needed.

### Sidecar Format

```markdown
---

## Auditor Notes & Unknowns

### [LOCAL-ID] — Short title
**Status:** Open | In Progress | Resolved
**Risk:** Low | Medium | High
**What is not yet known:** [one sentence]
**Resolution path:** [one sentence]
**Logged:** [date, agent]

### Resolution Log
- [date]: [LOCAL-ID] resolved — [one-line description of how it was resolved]
```

Local IDs use the document abbreviation + number (e.g., `SR-001` for Support_Raft, `EC-001` for Ethical_Constraints). Cross-module unknowns that affect multiple files use the global `UNK-XXX` format and are indexed in `Unknowns_LF.md`.

### The 10-Entry Rule

If a file's sidecar contains more than 10 distinct open entries, the file is flagged for a **Resolution Pass** before the next audit cycle proceeds. A Resolution Pass moves resolved unknowns to the Resolution Log and promotes qualifying unknowns into the main document body as Specified or Placeholder content.

### Metadata Guardrail

If an AI agent receives a file where the sidecar section exceeds 20% of the total word count, the agent must flag this before auditing: *"Sidecar exceeds 20% of document length — Resolution Pass recommended before audit proceeds."* This is a strong flag, not a hard refusal. The audit may continue if the human contributor explicitly acknowledges the flag and directs the agent to proceed.

### Resolution and Expungement

An unknown is not a permanent fixture. It is a tracked debt.

**Payment via Specification:** An unknown is expunged when its content is integrated into the main document body as committed specification. The sidecar entry is deleted and a one-line Resolution Trace is added to the Resolution Log.

**Discharge via Trajectory:** An unknown deemed non-critical for the current version is moved to `Trajectories_LF.md` and removed from the active sidecar. The Resolution Log notes: *"[LOCAL-ID] — discharged to Trajectories_LF.md v[N] scope."*

**Crystallization principle:** Every time an unknown moves from the sidecar into the specification body, the document becomes more deterministic. The goal is a sidecar that shrinks toward zero as a document matures toward specification.

---

## Unknowns Registry

*In v0.5, the Unknowns Registry section governs the global index behavior. Local sidecar format is defined in the Decentralized Audit Architecture section above.*

Uncertainty is a first-class output, not a failure. Unknowns are tracked frontiers.

**Where unknowns live:**
- **Module-specific unknowns** — in the file's own sidecar (`## Auditor Notes & Unknowns`)
- **Cross-module unknowns** — in `Unknowns_LF.md` global index, with owning file noted
- **Navigation unknowns** — in `Discovery.md`

**Global index format** (for `Unknowns_LF.md`):

| ID | Title | Owning file | Status | Priority (Promotion) |
|---|---|---|---|---|
| UNK-XXX | Short title | `filename.md` | Open/In Progress/Deferred | Blocking/Non-blocking |

**Priority tags:**
- **Blocking** — prevents specification; dependent module cannot advance until resolved
- **Non-blocking** — can proceed but must be revisited before v1.0
- **Exploratory** — relevant for future trajectories; route to `Trajectories_LF.md`

**The Expiry Rule:**
If a Blocking or Non-blocking unknown remains in the registry for more than two version cycles without a documented Resolution Path, it must be escalated to Systemic Risk status — or the dependent module must be moved back from Specification to Exploration.

**Version cycle definition:** One completed multi-agent audit pass with findings logged.

**Expiry check responsibility:** The Skeptic/Auditor role must open each new audit cycle by reviewing the active unknowns index for entries approaching or past two cycles.

A verification pass that surfaces no unknowns on a complex document should itself be treated with suspicion.

---

## Cross-Repo Verification

The Lazarus Forge and companion repositories share philosophical foundations but operate at different scales and environments. Claims in one repo must not silently contradict the other.

*Note: Astroid-miner is a planned repository, intentionally deferred until Leviathan deployment is underway. Cross-repo verification requirements apply to `Lazarus-Forge-` now and to Astroid-miner when that milestone is reached.*

**Bidirectional Linking Requirement**
Any cross-repo dependency must be documented in both repositories with a stated assumption contract. The dependency is not verified until both sides acknowledge it.

---

## Verification Gates

Contributions pass through sequential verification before promotion from exploration to committed specification. The Auditor role has binding authority to block promotion at any gate. A block cannot be overridden without explicit documented rebuttal and a second-pass audit performed by a different agent — human or AI — or a role-shifted re-evaluation explicitly declared. Self-approval loops are not permitted.

### Gate 1 — Fallacy Check
Has the contribution been actively checked against the Fallacy Checklist, with substantive notes for non-trivial claims?
**If NO →** Return to author
**If YES →** Gate 2

### Gate 2 — Active Verification Artifacts
Does at least one of the following exist for each significant claim, and is it sufficient to potentially falsify the claim — not merely illustrate it?
- A back-of-the-envelope calculation
- A comparison to a real-world analog system with documented scaling factors
- A falsification attempt with described failure conditions

Decorative math and irrelevant analogies do not satisfy this gate. Artifacts must do work.
**If NO →** Return for artifact generation
**If YES →** Gate 3

### Gate 3 — Adversarial Pass
Has the contribution been actively challenged by a Skeptic/Auditor role or adversarial prompt? The challenge must include at least one concrete failure scenario or stress condition — not a general observation.
**If NO →** Must undergo adversarial testing before proceeding
**If YES →** Gate 4

### Gate 4 — Scope Alignment
Does the contribution fit current version scope, or does it belong in a future trajectory?
**If future scope →** Route to `Trajectories_LF.md`
**If current scope →** Gate 5

### Gate 5 — Cross-Reference Integrity
Do all file references, module links, and quantitative citations resolve correctly?
**If NO →** Flag unresolved references, hold at draft
**If YES →** Gate 6

### Gate 6 — Conflict Check
Does the contribution contradict existing committed specifications?
**If YES →** Resolve conflict explicitly before committing
**If NO →** Approved for commit

---

## Full Stop Review

Any contributor — human or AI — may invoke a Full Stop Review if a specification passes all gates but exhibits systemic inconsistency or unclear real-world viability.

A Full Stop Review resets the contribution to Gate 1 with explicit focus on the foundational premise.

**Trigger conditions:**
1. The same foundational claim is blocked across two separate audit cycles
2. A new finding invalidates the core premise of a previously promoted specification
3. A pattern of documented overrides is eroding a governance principle without an explicit revision process

**Invocation record:** Triggering agent, triggering concern (one falsifiable sentence), date and document version, outcome. Record belongs in the document's audit trail.

---

## Observability & Audit Trail

Verification must be documentable, not just performed.

**Required audit trail fields:**
- Document audited and version
- Auditor role and agent identity
- Date or audit cycle identifier
- Gates cleared (list)
- Gates blocked (list with reason per gate)
- Unknowns logged (IDs or local IDs)
- Overrides recorded (with justification)
- Sign-off statement

**Standard sign-off format:**
> *"Verified under Auditor_Protocols v0.5 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides recorded. Auditor: [Role/Agent]"*

A future contributor must be able to reconstruct what was checked, who checked it, and what was found. An audit that leaves no trace is indistinguishable from no audit.

*Note: A machine-readable audit trail schema (JSON/YAML) is deferred to a future version. See global unknowns index.*

---

## Protocol Performance (Placeholder)

*Metrics are Placeholder pending first full audit cycle completion (registry v1.0).*

**Target metrics:**
- Productive block ratio — fraction of Auditor blocks resulting in documented document improvement
- False-positive refusal rate — blocks overridden with documented justification
- Drift incidents detected per cycle

**Anti-Auditor-Capture:** For high-stakes documents, the Auditor role should rotate to a different agent model across successive audit cycles.

---

## Failure Modes of This Document

**Checklist Theater** — Mitigated by requiring substantive notes, not bare checkmarks.

**Auditor Capture** — Mitigated by binding block authority, documented rebuttal requirement, independent second-pass audits, and Auditor rotation for high-stakes documents.

**Version Freeze** — Mitigated by explicit revision triggers.

**Exploration Suppression** — Mitigated by the Exploration vs. Specification distinction and the loophole guard.

**Over-Engineering the Audit** — If running a verification cycle takes longer than writing the original contribution, the protocol has failed. Simplicity is a design constraint.

**Coherent Nonsense** — Mitigated by the Full Stop Review mechanism.

**Metadata Bloat** — Mitigated by the Sidecar Model. Centralized unknowns registries that grow without bound become obstacles to the verification they govern. The Sidecar Model was introduced in v0.5 specifically to address this failure mode.

**Meta-Recursion Gap** — The protocol audits contributions but cannot fully audit its own enforcement. Mitigated by self-application of gates on revision, Protocol Performance metrics once active, and Auditor rotation.

---

## Relationship to Existing Documents

- `Ethical_Constraints.md` — parent document; governs permission, this document governs verification; hard-line doctrines not subject to override by this protocol
- `Lazarus_forge_v0_flow.md` — structural model; reference standard for shared terminology
- `Trajectories_LF.md` — destination for scope creep that proves to be valid future work
- `leviathan_testing.md` — primary stress-test environment; where Protocol Performance metrics will first be collected
- `Discovery.md` — navigation layer; confirmed file list
- `Unknowns_LF.md` — global index for cross-module unknowns (repurposed in v0.5 from full-entry store to index)
- `Forge_Audit_Kit.md` — condensed audit reference for routine multi-agent cycles
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

Version 0.5 — consolidates v0.4 additions and Sidecar Amendment (v0.5).

**Changes from v0.3:**
- Added scope clarification: human override rights do not extend to Ethical_Constraints hard-line doctrines
- Added version cycle definition and Expiry check responsibility to Unknowns Registry
- Added Assumption Extraction requirement to Rule 6
- Added Full Stop Review trigger conditions and invocation record format
- Added required fields to Observability & Audit Trail with example
- Added Protocol Performance section as Placeholder
- Added Meta-Recursion Gap and Metadata Bloat to Failure Modes
- Auditor Capture updated to reference rotation principle
- **Added Decentralized Audit Architecture (Sidecar Model)** — local ledgers, Audit Health Header, 10-entry rule, metadata guardrail, Resolution and Expungement
- Unknowns Registry section updated to govern global index behavior
- Relationship section updated: Unknowns_LF.md role clarified, Forge_Audit_Kit.md added

This document is expected to remain incomplete and wrong in places. What must remain constant:

**Confidence never outruns verification.**

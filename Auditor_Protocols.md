# Auditor_Protocols.md — Verification & Hallucination Filter
**Version 0.4**

---

## Purpose

This document defines the verification protocols for all contributors to the Lazarus Forge — human, AI, or multi-agent workflow. Its purpose is to ensure that what enters the repository as specification has been pressure-tested, not merely generated.

Polished outputs are a known failure mode. Unverified content is not eligible for specification.

This file governs how claims are checked, how contributions are audited, and how the multi-agent workflow maintains integrity across sessions and contributors.

**This document is subject to its own protocols.** The gate logic, checklist, and audit trail requirements apply to revisions of this document as much as to any other. An audit protocol that exempts itself from scrutiny is not a protocol — it is a preference.

---

## Governing Principle

> Capability never outruns permission. — `Ethical_Constraints.md`

The auditor equivalent:

> Confidence never outruns verification.

These two principles operate in parallel. One governs what the Forge is allowed to do. The other governs what the Forge is allowed to claim.

**Scope of this document:** This document governs verification of contributions. It does not govern the ethical constraints defined in `Ethical_Constraints.md`. Human override rights under this protocol apply to verification process decisions — they do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in the parent governance document. See UNK-021 in `Unknowns_LF.md`.

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
Does the document reference a file, module, or specification that does not exist in the repository? All cross-references must resolve to real files. Aspirational references must be labeled explicitly as planned. The Discovery.md raw link architecture exists to prevent this failure mode — use it.

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
> *"Operating as [Role] per Auditor_Protocols.md v0.4"*

This creates an audit hook and prevents silent role drift. Roles are not rigid but shifts must be named, not suppressed.

Assigned roles:

- **Synthesizer** — integrates philosophy, doctrine, and cross-system coherence
- **Engineer** — translates concepts into operational specifications
- **Skeptic/Auditor** — stress-tests claims, surfaces hidden assumptions, adversarial testing
- **Connective Tissue** — links community discussion to repository evolution

**Rule 1 — No Invented Files**
AI models must not reference, summarize, or describe files that have not been confirmed to exist in the repository. If uncertain, state uncertainty explicitly.

**Rule 2 — Role Awareness**
Operate within the declared role. If operating outside it, name the shift explicitly before proceeding.

**Rule 3 — Lineage Tracking**
Significant changes must note what changed, why it changed, and what prior version it replaces. This is the audit trail that distinguishes a living document from a drifting one.

**Rule 4 — Refusal is Valid**
A model that identifies a flawed premise must flag it rather than refine it. Refusal is not a failure of the AI — it is a success of the protocol. A model that refuses to polish a bad foundation has cleared Gate 1. The workflow must prioritize redirection over completion of the original task.

**Rule 5 — Confidence Labeling**
All quantitative claims must use the four-label system defined in the Fallacy Checklist. Unlabeled numbers are placeholders by default.

**Rule 6 — Inter-Agent Consistency**
At handoff between agents, the receiving agent must explicitly query prior contributions for unstated assumptions before proceeding. The receiving agent should open with a brief Assumption Extraction statement: *"Prior contributions assumed: [list key assumptions]. These are carried forward unless contradicted by new findings."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades.

**Trust the process, not the predecessor.**

---

## Human Contributor Protocols

These protocols apply equally to human contributors. The document governs contributions, not contributor type.

- Humans must label estimates as estimates. "I think it works" is not sufficient basis for a specification claim.
- Humans must resolve all cross-references before committing. Linking to a planned file requires an explicit planned label.
- Humans may override AI auditor flags — but overrides must be documented with reasoning. An undocumented override is indistinguishable from an ignored warning.
- Human override rights apply to verification process decisions. They do not extend to hard-line doctrines defined in `Ethical_Constraints.md` — those are not subject to override by any contributor type.
- The lifecycle template in Fallacy Checklist item 8 applies to human-authored module specs as well.

---

## Unknowns Registry

Uncertainty is a first-class output, not a failure.

Any unresolved question, gap, or dependency surfaced during verification must be logged rather than buried. Unknowns are tracked frontiers — they mark where the system needs to grow, not where it has failed.

**Where unknowns live:**
- Within the audited document itself for module-specific unknowns
- In `Discovery.md` for unknowns affecting navigation or cross-file dependencies
- In `Unknowns_LF.md` for unknowns that span multiple modules

**Format for logging an unknown:**
- What is not yet known
- Why it matters to current or future specifications
- What would resolve it (experiment, analog data, expert input)
- Which file or module it most affects
- Priority tag (see below)

**Priority tags:**
- **Blocking** — prevents specification; dependent module cannot advance until resolved
- **Non-blocking** — can proceed but must be revisited before v1.0
- **Exploratory** — relevant for future trajectories; route to `Trajectories_LF.md`

**The Expiry Rule:**
If a Blocking or Non-blocking unknown remains in the registry for more than two version cycles without a documented Resolution Path, it must be escalated to Systemic Risk status — or the dependent module must be moved back from Specification to Exploration. Tracked frontiers must eventually become settled territory. The registry is not a junk drawer.

**Version cycle definition:** A version cycle is one completed multi-agent audit cycle — a full pass through a document by at least two agents (human or AI) with findings logged. Incrementing a document version number without an audit cycle does not constitute a version cycle for Expiry Rule purposes.

**Expiry check responsibility:** The Skeptic/Auditor role must open each new audit cycle by reviewing `Unknowns_LF.md` for entries approaching or past two cycles. Entries that have aged out must be escalated or the dependent module explicitly demoted before the current cycle proceeds.

A verification pass that surfaces no unknowns on a complex document should itself be treated with suspicion.

---

## Cross-Repo Verification

The Lazarus Forge and Astroid-miner repositories share philosophical foundations but operate at different scales and environments. Claims in one repo must not silently contradict the other.

*Note: Astroid-miner is a planned repository, intentionally deferred until Leviathan deployment is underway. Cross-repo verification requirements apply to `Lazarus-Forge-` now and to Astroid-miner when that milestone is reached. See UNK-003 in `Unknowns_LF.md`.*

**Bidirectional Linking Requirement**
Any cross-repo dependency must be documented in both repositories with a stated assumption contract. The dependency is not verified until both sides acknowledge it.

Example contract format:
> Forge assumes: [stated input or condition]
> Miner provides: [stated output or capability]
> Mismatch resolution: [route to Trajectories_LF.md or flag for review]

**Shared verification checkpoints:**

Resource Supply vs. Production Demand — Does Astroid-miner's projected material output align with what Lazarus Forge processing modules can actually handle? Mismatches are version-gated milestones, not ignored discrepancies.

Shared Module Assumptions — The Air Scrubber's Leviathan-compatible variant, the Spin Chamber's zero-G extensions, and the GECK seed's bootstrap logic all have implications for the Astroid-miner architecture. Changes to shared modules must be checked against both repos before commit.

Terminology Consistency — Terms like "purified," "reduced," "functional," and "feedstock" must carry consistent meanings across both repositories. Divergence must be documented, not assumed.

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
Has the contribution been actively challenged by a Skeptic/Auditor role or adversarial prompt? The challenge must include at least one concrete failure scenario or stress condition — not a general observation. "Here is where it breaks" is the standard, not "looks mostly fine."
**If NO →** Must undergo adversarial testing before proceeding
**If YES →** Gate 4

### Gate 4 — Scope Alignment
Does the contribution fit current version scope, or does it belong in a future trajectory?
**If future scope →** Route to `Trajectories_LF.md`; may return as forward-compatible interface only, marked non-binding
**If current scope →** Gate 5

### Gate 5 — Cross-Reference Integrity
Do all file references, module links, and quantitative citations resolve correctly? Are cross-repo dependencies documented bidirectionally?
**If NO →** Flag unresolved references, hold at draft
**If YES →** Gate 6

### Gate 6 — Conflict Check
Does the contribution contradict existing committed specifications?
**If YES →** Resolve conflict explicitly, document resolution, before committing
**If NO →** Approved for commit

---

## Full Stop Review

Any contributor — human or AI — may invoke a Full Stop Review if a specification passes all gates but exhibits systemic inconsistency or unclear real-world viability.

A Full Stop Review resets the contribution to Gate 1 with explicit focus on the foundational premise. The triggering concern must be documented. This mechanism protects against technically valid but fundamentally wrong systems, and against slow drift into coherent nonsense.

Invoking a Full Stop Review is not a failure of the contribution — it is a success of the protocol.

**Trigger conditions:** A Full Stop Review is warranted when any of the following apply:
1. Two or more gates are blocked on the same foundational claim across separate audit cycles — the claim keeps failing, not just the documentation around it.
2. A new finding invalidates the core premise of a previously promoted specification.
3. A pattern of documented overrides is eroding a governance principle without an explicit revision process — incremental erosion without acknowledgment.

**Invocation record format:** When invoking a Full Stop Review, the triggering contributor must log: (1) triggering agent and role; (2) triggering condition stated as one falsifiable sentence; (3) date and document version; (4) outcome — reset to Gate 1, or rebuttal filed with second-pass audit. This record belongs in the audit trail of the affected document.

---

## Observability & Audit Trail

Verification must be documentable, not just performed.

**Required audit trail fields** — every significant audit must record:
- Document audited and version
- Auditor role and agent identity
- Date or audit cycle identifier
- Gates cleared (list)
- Gates blocked (list with reason per gate)
- Unknowns logged (IDs)
- Overrides recorded (with justification)
- Sign-off statement

**Standard sign-off format:**
> *"Verified under Auditor_Protocols v0.4 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides recorded. Auditor: [Role/Agent]"*

**Example audit trail entry:**
```
Document: leviathan_testing.md (Exploration audit, May 2026)
Auditor: Skeptic/Auditor — Claude (Sonnet 4.6)
Gates cleared: 1, 4
Gates blocked: 2, 3, 5, 6 (deferred — Exploration status, not promotion candidate)
Unknowns logged: UNK-006, UNK-007, UNK-008, UNK-009, UNK-010
Overrides: None
Sign-off: Exploration-stage audit complete. Four promotion blockers identified.
          Foundation sound. No turd detected.
```

Acceptable audit trail locations:
- A comment block within the audited file
- A linked review note in `Discovery.md`
- A logged unknown in `Unknowns_LF.md`

A future contributor — human or AI — must be able to reconstruct what was checked, who checked it, and what was found. An audit that leaves no trace is indistinguishable from no audit.

*Note: A machine-readable audit trail schema (JSON/YAML) is deferred to a future version when tooling exists to consume it. See UNK-023 in `Unknowns_LF.md`.*

---

## Protocol Performance (Placeholder)

*This section establishes the intent to measure audit effectiveness. Metrics are Placeholder pending UNK-004 cycle definition and UNK-023 audit trail schema. See `Unknowns_LF.md` UNK-020.*

**Target metrics (Placeholder — not yet measured):**
- **Productive block ratio** — fraction of Auditor blocks that resulted in documented document improvement before promotion
- **False-positive refusal rate** — blocks that were overridden with documented justification, as a fraction of total blocks
- **Drift incidents detected** — unknowns surfaced per audit cycle that were not previously logged

**Measurement activation trigger:** First full audit cycle across all primary documents complete (UNK-004 activation condition).

**Anti-Auditor-Capture note:** For high-stakes documents (governance, ethics, core specs), the Auditor role should rotate to a different agent model or human contributor across successive audit cycles. An auditor who has reviewed the same document multiple times without finding new issues should be treated with the same suspicion as a verification pass that surfaces no unknowns.

---

## Failure Modes of This Document

This document is itself subject to the protocols it defines. Known risks:

**Checklist Theater** — The list gets checked without genuine scrutiny. Verification becomes ritual rather than function. Mitigated by requiring substantive notes per checklist item, not bare checkmarks.

**Auditor Capture** — The skeptic role softens over time to avoid friction. Mitigated by binding block authority, documented rebuttal requirement, independent second-pass audits, and Auditor rotation for high-stakes documents (see Protocol Performance above).

**Version Freeze** — This document stops being updated as the system evolves. Mitigated by the explicit revision trigger below.

**Exploration Suppression** — Verification pressure is applied too early, killing generative thinking before it matures. Mitigated by the explicit Exploration vs. Specification distinction and the loophole guard.

**Over-Engineering the Audit** — The protocol becomes so complex it creates more overhead than value. If running a verification cycle takes longer than writing the original contribution, the protocol has failed. Simplicity is a design constraint here too. Periodic lightweight audits of the audit process itself — "did this cycle add more value than friction?" — should be part of `leviathan_testing.md` cycles.

**Coherent Nonsense** — A document passes all gates but is systemically wrong at a level no individual gate catches. Mitigated by the Full Stop Review mechanism.

**Meta-Recursion Gap** — The protocol audits contributions but cannot fully audit its own enforcement. Mitigated by: (1) this document being subject to its own gates on revision; (2) Protocol Performance metrics once active; (3) Auditor rotation preventing capture. Acknowledged as an irreducible residual risk — a verification system that claimed to fully verify itself would itself be a Turd Problem candidate.

---

## Relationship to Existing Documents

- `Ethical_Constraints.md` — parent document; governs permission, this document governs verification; hard-line doctrines in that document are not subject to override by this protocol's human override provisions
- `Lazarus_forge_v0_flow.md` — structural model; the gate logic here mirrors the triage gates there; reference standard for shared terminology
- `Trajectories_LF.md` — destination for scope creep that proves to be valid future work
- `leviathan_testing.md` — primary stress-test environment where these protocols face real pressure; also where the audit process itself gets evaluated and Protocol Performance metrics will first be collected
- `Discovery.md` — the navigation layer that prevents hallucinated file references
- `geck_forge_seed.md` — bootstrap logic shared with Astroid-miner; subject to cross-repo verification when Astroid-miner milestone is reached
- `Unknowns_LF.md` — central registry for unknowns spanning multiple modules
- `Lazarus-Forge-` — companion doctrine repository; cross-repo verification applies now
- `Astroid-miner` — planned repository; cross-repo verification deferred to Leviathan milestone (UNK-003)

---

## Status

Version 0.4 — revised after multi-model audit cycle of this document itself (Claude, ChatGPT, Gemini + Gemini synthesis), May 2026.

Key changes from v0.3:
- Added scope clarification: human override rights do not extend to Ethical_Constraints hard-line doctrines (UNK-021 partial resolution)
- Added version cycle definition and Expiry check responsibility to Unknowns Registry section (UNK-004 resolution)
- Added Assumption Extraction statement requirement to Rule 6 Inter-Agent Consistency
- Added human override scope limitation to Human Contributor Protocols
- Added Astroid-miner deferral note to Cross-Repo Verification
- Added Full Stop Review trigger conditions and invocation record format (UNK-022 resolution)
- Rewrote Observability & Audit Trail with required fields list and example entry (UNK-023 partial resolution — structured markdown; JSON/YAML deferred)
- Added Protocol Performance section as Placeholder with target metrics and Auditor rotation principle (UNK-020 partial resolution)
- Added Meta-Recursion Gap to Failure Modes
- Updated Auditor Capture failure mode to reference rotation principle
- Updated Relationship to Existing Documents: Unknowns_LF.md now confirmed live; Astroid-miner status clarified

This document is expected to remain incomplete and wrong in places. What must remain constant:

**Confidence never outruns verification.**

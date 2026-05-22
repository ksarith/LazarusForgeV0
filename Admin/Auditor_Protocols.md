# Auditor_Protocols.md — Verification & Hallucination Filter
**Version 0.6**

**Audit Health:**
- Status: Specification (governing document)
- Last audit: 2026-05-19 (Multi-model — Claude, ChatGPT, Gemini, Grok)
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

> Capability never outruns permission. — `Admin/Ethical_Constraints.md`

The auditor equivalent:

> Confidence never outruns verification.

These two principles operate in parallel. One governs what the Forge is allowed to do. The other governs what the Forge is allowed to claim.

**Scope boundary:** Human override rights under this protocol apply to verification process decisions only. They do not extend to the hard-line doctrines (Anti-Weaponization, Life Preservation) defined in `Admin/Ethical_Constraints.md`.

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
Does the design assume energy is available without accounting for its source, storage, or conversion losses? Every watt must have a traceable origin. Cross-reference `Operations/Energy.md`.

**2. Friction Blindness**
Does the design ignore mechanical resistance, thermal losses, fluid drag, or interface wear? Real systems degrade. Specifications that assume ideal conditions are not specifications — they are wishes.

**3. Energy Density Paradox**
Does any recovery, recycling, or bootstrapping step consume more than it produces? Justify as enabling investment or flag. Recovery that costs more than it recovers is reduction dressed as progress.

**4. Semantic Drift**
Has a term changed meaning between documents without a documented revision? Cross-check against `Architecture/Forge_flow.md` as the reference standard.

**5. Scope Creep Disguised as Refinement**
Does a revision quietly expand claimed capabilities beyond what the current version can demonstrate? New capabilities belong in `Admin/Trajectories.md`.

**6. Hallucinated Files or Cross-References**
Does the document reference a file that does not exist? All cross-references must resolve to real files. Files confirmed in `Discovery.md` are treated as verified. Aspirational references must be labeled planned. Repository uses folder-prefixed paths — do not flag folder-prefixed canonical names as failures.

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
> *"Operating as [Role] per Auditor_Protocols.md v0.6"*

Roles: **Synthesizer** | **Engineer** | **Skeptic/Auditor** | **Connective Tissue**

**Rule 1 — No Invented Files:** Never reference unconfirmed files. Files listed in `Discovery.md` are confirmed. State uncertainty for anything else.

**Rule 2 — Role Awareness:** Name role shifts before proceeding.

**Rule 3 — Lineage Tracking:** Note what changed, why, and what it replaces.

**Rule 4 — Refusal is Valid:** Flag flawed premises — do not refine them. Refusal is a success of the protocol.

**Rule 5 — Confidence Labeling:** Use the four-label system. Unlabeled = Placeholder.

**Rule 6 — Inter-Agent Consistency:** Open with Assumption Extraction: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* Failure to re-evaluate prior assumptions is a primary cause of multi-agent hallucination cascades.

**Rule 7 — Repository Structure Awareness:** The repository uses folder-based structure (Admin/, Architecture/, Operations/, Tests/). Legacy flat filenames are aliases documented in the Rename Registry in `Discovery.md`. Use canonical folder-prefixed paths in all new contributions.

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

**Global Index:** `Unknowns.md` is a cross-module index only — summary table, dependency map, systemic risks spanning multiple files, audit trail, resolved archive. Full entry detail lives in the owning file's sidecar.

### Audit Health Header

Every file carries a File State table immediately below the title per `Admin/File_Template.md`. The File State table replaces the legacy Audit Health Header format.

### Sidecar Format

Full sidecar format is defined in `Admin/File_Template.md` Section 8. Summary:

```markdown
---

## Auditor Notes & Unknowns

### [FILE-PREFIX-NNN] — Short title

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open / In Progress / Resolved |
| Risk          | Low / Medium / High      |
| Priority      | Minor / Major / Critical |
| Type          | Technical / Ethical / Architectural / Governance |
| Blocking      | Yes / No                 |
| Owner         | Owning file              |
| First Logged  | YYYY-MM-DD               |
| Last Reviewed | YYYY-MM-DD               |

**Description:** One sentence stating the reality gap.
**Why It Matters:** One sentence on consequence if unresolved.
**Resolution Path:** Concrete closure criteria.

---

### Resolution Log
- YYYY-MM-DD: [FILE-PREFIX-NNN] — one-line resolution description
```

Local IDs use file abbreviation + three digits: `AP-001` (Auditor Protocols), `SC-001` (Separation Thermal), `GI-001` (Gate Intake), etc. Cross-module unknowns use global `UNK-XXX` format and are indexed in `Unknowns.md`.

### The 10-Entry Rule

More than 10 distinct open entries in a sidecar flags the file for a Resolution Pass before the next audit cycle.

### Metadata Guardrail

If sidecar content exceeds 20% of total document word count, flag for Resolution Pass before auditing. Flag is strong — not a hard refusal. Proceed if human contributor explicitly acknowledges.

### Resolution and Expungement

- **Payment via Specification** — content moves into the document body as committed spec; entry moves to Resolution Log
- **Discharge via Trajectory** — out of current version scope; route to `Admin/Trajectories.md`; note in Resolution Log
- **Discharge via Lessons Learned** — resolved by operational experience; lesson moves to Lessons Learned section; entry closes

**Crystallization principle:** Every unknown that moves from sidecar into specification body makes the document more deterministic. A shrinking sidecar is a maturing document.

---

## Unknowns Registry

*In v0.5+, this section governs global index behavior. Local sidecar format is defined above and in `Admin/File_Template.md`.*

**Where unknowns live:**
- Module-specific — in the file's own sidecar
- Cross-module — in `Unknowns.md` global index, owning file noted
- Navigation — in `Discovery.md`

**Global index format:**

| ID | Title | Owning file | Status | Priority (Promotion) |
|---|---|---|---|---|
| UNK-XXX | Short title | `folder/filename.md` | Open/In Progress/Deferred | Blocking/Non-blocking |

**Priority tags:** Blocking | Non-blocking | Exploratory

**The Expiry Rule** is retained as a backstop for cross-module unknowns in the global index. For global index entries: if a Blocking or Non-blocking unknown remains without a documented Resolution Path for more than two audit cycles, escalate to Systemic Risk or demote the dependent module.

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
| 3 — Adversarial Pass | Adversarial Challenge Battery applied? At least one failure scenario per challenge class tested? | Must undergo adversarial testing — see Adversarial Audit Layer |
| 4 — Scope Alignment | Fits current version or future trajectory? | Route to `Admin/Trajectories.md` |
| 5 — Cross-Reference Integrity | All file refs resolve using canonical folder-prefixed paths? Cross-repo deps bidirectional? | Hold at draft |
| 6 — Conflict Check | Contradicts existing committed specs? | Resolve conflict before committing |

**Gate 3 is now formally gated on the Adversarial Audit Layer.** One concrete failure scenario was the prior bar — it is insufficient. The Adversarial Challenge Battery below defines the minimum requirement.

---

## Adversarial Audit Layer

*Introduced v0.6. Upgrades the auditor role from checklist verifier to institutional immune system.*

### Purpose

The adversarial layer exists to challenge hidden assumptions, institutional blind spots, semantic ambiguity, operator incentives, recursive self-validation, and failure propagation pathways. Its purpose is not criticism for its own sake — it is resilience hardening.

> A protocol is not considered robust until it has survived deliberate hostile analysis.

The strongest audit systems are not optimized to prove correctness. They are optimized to discover how reality can still break the model despite apparent correctness.

### When to Apply

The full Adversarial Challenge Battery is required for:
- Any document being considered for Specification promotion
- Any document governing irreversible actions (Gate_03_Reduction.md, Ethical_Constraints.md)
- Any document in the trust chain for autonomous systems (Electronics.md, Cognitive_Frameworks.md)
- Any document that has passed Gate 1 and Gate 2 but still feels wrong

Partial application (selected challenge classes) is acceptable for Exploration-stage documents. Document which classes were applied and why others were deferred.

### The Adversarial Challenge Battery

Ten challenge classes. Each requires at least one concrete scenario, not a general acknowledgment.

---

**Challenge Class 1 — Assumption Inversion**

Tests whether a protocol only works because hidden assumptions remain true.

Ask: *What if the operator is wrong? What if the sensor data is fabricated? What if the environment is hostile instead of cooperative?*

Many Forge gates implicitly assume:
- Accurate classification
- Honest reporting
- Stable materials
- Intact tooling
- Rational operators

An adversarial audit deliberately removes those assumptions and asks whether the protocol survives.

*Minimum requirement:* Name three hidden assumptions in the document and describe what happens when each fails.

---

**Challenge Class 2 — Failure Amplification**

Instead of asking "Can this fail?" ask "How does this fail catastrophically?"

Examples:
- A misidentified capacitor becomes an arc flash
- Contaminated aluminum poisons a melt batch
- Mislabeled alloys propagate downstream unnoticed

This reveals cascading failures, hidden coupling, and latent propagation pathways. A protocol that survives only isolated failures is fragile.

*Minimum requirement:* Trace one failure from its origin through at least two downstream consequences.

---

**Challenge Class 3 — Incentive Corruption**

Audits whether the protocol breaks when participants optimize for the wrong thing.

Examples:
- Throughput over safety
- "Passing audit" over actual integrity
- Hiding uncertainty to avoid delays
- Fabricating confidence metrics to meet targets

Ask: *How could a smart operator game this protocol while appearing compliant?*

If that answer exists and no countermeasure exists, the protocol is vulnerable.

*Minimum requirement:* Identify one incentive corruption path and name the countermeasure or log it as an unknown.

---

**Challenge Class 4 — Semantic Drift Attacks**

Tests whether terminology degrades over time.

Terms that commonly drift:
- "Safe" / "contained" / "stable" / "acceptable" / "hazard removed"
- "Structural" / "functional" / "adequate" / "sufficient"
- "Hold" / "quarantine" / "clear" / "flag"

Ask: *Can two operators interpret this differently and still claim compliance?*

If yes, doctrine drift exists, audit reproducibility weakens, and institutional memory corrodes.

*Minimum requirement:* Identify one term in the document that could be interpreted differently by two operators. Either tighten the definition or log the ambiguity as an unknown.

---

**Challenge Class 5 — Unknown Unknown Pressure Tests**

Protocols often fail not from known hazards but from unmodeled conditions.

Ask: *What would this system do if it encountered a material, process, or state it has never seen before?*

This matters heavily in:
- Salvage intake (unknown provenance)
- Mixed waste streams (unknown composition)
- Experimental fabrication (unknown material behavior)
- Autonomous classification (unknown item type)

A resilient protocol degrades safely under uncertainty rather than failing catastrophically or routing unknowns forward as knowns.

*Minimum requirement:* Describe what the protocol does when it encounters a condition outside its defined envelope. If the answer is "undefined," log it as an unknown.

---

**Challenge Class 6 — Recursive Justification Loops**

One of the most dangerous institutional failure modes.

Example loop:
- Protocol says system is safe
- System passed protocol
- Therefore system is safe

The audit itself becomes the evidence. Documentation replaces reality. Audit theater develops.

Ask: *What external reality check exists beyond self-reference?*

*Minimum requirement:* Identify one claim in the document that is validated only by other repository documents. Either ground it in external reality or label it explicitly as internally derived.

---

**Challenge Class 7 — Human Fatigue and Cognitive Erosion**

Many procedures only work under ideal cognition. Real systems are operated by fatigued, distracted, overloaded humans.

Challenge questions:
- Does this protocol remain safe after 12 hours of repetition?
- Does it survive shift handoff without verbal briefing?
- Does it survive high backlog and throughput pressure?
- Does it survive an operator who is new, undertrained, or temporarily impaired?

Normalization of deviance — where slightly wrong becomes the new normal through repetition — is a documented cause of major industrial incidents.

*Minimum requirement:* Identify one step in the protocol that degrades under sustained operation. Either add a safeguard or log it as an unknown.

---

**Challenge Class 8 — Malicious Actor Simulation**

Distinct from incompetence — this is intentional abuse by a knowledgeable actor.

Examples:
- Conceal hazardous material at intake
- Falsify intake records
- Bypass lockouts
- Poison melt streams with known contaminants
- Inject corrupt documentation into the network
- Sabotage calibration without detection
- Plant compromised hardware in salvage stream

Ask: *What prevents a knowledgeable hostile actor from weaponizing this process?*

This is especially important for:
- Gate_01_Intake.md — falsified provenance
- Operations/Electronics.md — hardware supply chain compromise
- Architecture/Forge_Net.md — network data poisoning
- Admin/Ethical_Constraints.md — anti-weaponization bypass attempts

*Minimum requirement:* Identify one malicious actor scenario relevant to the document and name the countermeasure or log it as an unknown.

---

**Challenge Class 9 — Epistemic Corruption**

Distinct from malicious actors — this is systematic degradation of shared knowledge through well-intentioned but incorrect contributions.

Examples:
- Consensus weighting suppresses a truthful minority contribution
- High-confidence entries decay without revalidation and become stale certainty
- Goodhart's Law — measurable contribution metrics become optimization targets rather than truth targets
- Locally correct knowledge gets rejected as globally anomalous
- Three AI models with overlapping training data converge on the same wrong answer

Ask: *How does this system distinguish confident truth from confident error?*

This challenge class was introduced following the Forge_Net.md audit which identified epistemic corruption as more dangerous than deliberate attack for knowledge-based systems.

*Minimum requirement:* Identify one mechanism by which incorrect information could achieve high confidence in this system. Name the countermeasure or log it as an unknown.

---

**Challenge Class 10 — Systemic Coupling and Cascade**

Tests whether the document understands its failure propagation footprint.

Ask: *If this module fails, what fails with it? What fails second? What fails third?*

High-coupling documents require higher adversarial scrutiny because their failure footprint is disproportionate to their size.

Current high-coupling documents in the repository:
- `Admin/Auditor_Protocols.md` — failure here degrades all other files
- `Operations/Electronics.md` — failure here compromises the trust anchor
- `Architecture/Forge_flow.md` — failure here corrupts all gate routing
- `Architecture/Forge_Net.md` — failure here propagates across the ecology

*Minimum requirement:* Trace this document's failure footprint through at least two levels of downstream dependency. If the footprint is larger than expected, consider whether the document's scope should be narrowed or its governance frequency increased.

---

### Adversarial Audit Sign-Off Format

In addition to the standard sign-off, adversarial audits must record:

```
Adversarial Challenge Battery:
- Classes applied: [list]
- Classes deferred: [list with reason]
- Findings per class: [ID or "None"]
- New unknowns from adversarial pass: [list]
- Highest-risk finding: [one sentence]
```

---

### Anti-Patterns the Adversarial Layer Exists to Prevent

| Anti-Pattern | Description | Challenge Class |
|---|---|---|
| Audit theater | Protocol passes without surfacing real gaps | 6 — Recursive justification |
| Specification cosplay | Exploratory content dressed as operational spec | 1 — Assumption inversion |
| Confident wrongness | High consensus on incorrect answer | 9 — Epistemic corruption |
| Throughput pressure override | Safety bypassed under operational load | 3 — Incentive corruption |
| Silent failure accumulation | Failures not logged because minor or embarrassing | 7 — Human fatigue |
| Semantic compliance | Letter of protocol followed, spirit violated | 4 — Semantic drift |
| Single-point doctrine | Protocol only works if one assumption holds | 5 — Unknown unknowns |
| Cascade blindness | Local fix that creates downstream failure | 10 — Systemic coupling |

---

## Full Stop Review

Invoke when a spec passes all gates but exhibits systemic inconsistency or unclear real-world viability. Resets to Gate 1 with focus on foundational premise.

**Trigger conditions:**
1. Same foundational claim blocked across two separate audit cycles
2. New finding invalidates core premise of a previously promoted specification
3. Pattern of documented overrides eroding a governance principle without explicit revision
4. Multiple Adversarial Challenge Battery findings converging on the same structural gap

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
- Adversarial Challenge Battery summary (v0.6+)
- Sign-off statement

**Standard sign-off:**
> *"Verified under Auditor_Protocols v0.6 — gates [list] cleared, gates [list] blocked ([reason]), [N] unknowns logged, [N] overrides. Adversarial classes applied: [list]. Auditor: [Role/Agent]"*

*Note: Machine-readable audit trail schema (JSON/YAML) is deferred — see AP-003 in sidecar.*

---

## Protocol Performance (Placeholder)

*Metrics are Placeholder pending first full audit cycle completion.*

**Target metrics:**
- Productive block ratio — fraction of blocks resulting in documented improvement
- False-positive refusal rate — blocks overridden with documented justification
- Drift incidents detected per cycle
- Adversarial findings per document — tracks whether adversarial layer is surfacing real gaps

**Anti-Auditor-Capture:** For high-stakes documents, rotate the Auditor role to a different agent model across successive cycles. An auditor reviewing the same document repeatedly without finding new issues warrants the same suspicion as a verification pass surfacing no unknowns.

---

## Failure Modes of This Document

**Checklist Theater** — Verification becomes ritual. Mitigated by requiring substantive notes.

**Auditor Capture** — Skeptic role softens. Mitigated by binding block authority, documented rebuttal, second-pass requirement, and Auditor rotation.

**Version Freeze** — Document stops updating. Mitigated by explicit revision triggers and self-application of gates.

**Exploration Suppression** — Verification pressure applied too early. Mitigated by the Exploration vs. Specification distinction.

**Over-Engineering the Audit** — If a verification cycle takes longer than writing the contribution, the protocol has failed. Simplicity is a design constraint. The Adversarial Challenge Battery is a minimum, not an exhaustive test suite.

**Coherent Nonsense** — Passes all gates but is systemically wrong. Mitigated by Full Stop Review and Adversarial Challenge Class 6 (Recursive Justification).

**Metadata Bloat** — Centralized registries grow without bound and become obstacles. Mitigated by the Sidecar Model introduced in v0.5.

**Meta-Recursion Gap** — The protocol cannot fully audit its own enforcement. Mitigated by self-application of gates on revision, Protocol Performance metrics, and Auditor rotation. Acknowledged as an irreducible residual risk.

**Adversarial Theater** — The adversarial layer becomes a checkbox like the fallacy checklist. Mitigated by requiring concrete scenarios per challenge class, not general acknowledgments, and by logging all findings as unknowns rather than dismissing them.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| May 2026 | Audit Review | Centralized Unknowns_LF.md as full-entry store | File grew past token limits; audit prompts failed | Unknowns must live locally in owning files; central registry is index only | Analogous | No |
| May 2026 | Audit Review | Expiry Rule as primary accumulation mechanism | Rule had no enforcement path; unknowns aged silently | Structural constraints (10-entry rule, sidecar) work better than procedural rules | Analogous | No |
| May 2026 | Audit Review | Preparatory framing lines in audit prompts | Softened auditor findings; masked genuine gaps | Documents must stand on their own; scaffolding that stays up becomes load-bearing | Analogous | No |
| 2026-05-19 | Audit Review | Gate 3 Adversarial Pass defined as one concrete failure scenario | Bar was too low — single scenario leaves most failure modes untested. Audit theater risk high | Adversarial Challenge Battery introduced with ten challenge classes. Gate 3 now formally requires battery application, not a single scenario | Analogous | Yes — validate battery against first full adversarial audit cycle |
| 2026-05-19 | Audit Review | Consensus treated as truth in multi-agent audit cycles | Epistemic corruption — ten nodes agreeing on a wrong answer produces confident wrongness. Goodhart's Law applies to contribution metrics as much as to engineering claims | Adversarial Challenge Class 9 (Epistemic Corruption) added. Confidence decay, minority-report preservation, and contradiction logging added to Forge_Net.md validation doctrine | Analogous | Yes — validate against first live network audit |

---

## Auditor Notes & Unknowns

### AP-001 — Auditor effectiveness metrics not yet measured

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Governance                                       |
| Blocking      | No                                               |
| Owner         | Admin/Auditor_Protocols.md                       |
| First Logged  | 2026-05-04                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** How to measure whether the audit
process is actually adding value — productive block
ratio, false-positive refusal rate, drift incidents
detected per cycle — remains undefined.

**Why It Matters:** Without measurement, the audit
protocol cannot demonstrate its own effectiveness.
Adversarial Challenge Class 6 (Recursive Justification)
applies to the protocol itself — it cannot be its
own evidence.

**Resolution Path:**
- Metrics defined as Placeholder in Protocol
  Performance section.
- Activate measurement after first full audit
  cycle with Adversarial Battery completes.
- Add adversarial findings per document as a
  fourth metric.
- Payment via Specification — once first full
  cycle data exists, move metrics to Measured.

---

### AP-002 — Override vs. immutability boundary not yet confirmed in both documents

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | In Progress                                      |
| Risk          | Medium                                           |
| Priority      | Major                                            |
| Type          | Governance                                       |
| Blocking      | No                                               |
| Owner         | Admin/Auditor_Protocols.md                       |
| First Logged  | 2026-05-04                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** Whether the clarification that
human override rights do not extend to
Ethical_Constraints hard-line doctrines is
explicitly stated in both documents in a mutually
consistent way.

**Why It Matters:** Inconsistency between the two
documents creates an exploit path — a contributor
could claim the boundary doesn't exist because it
only appears in one file.

**Resolution Path:**
- Scope boundary added to this document.
- Requires confirmation that matching language
  exists in Admin/Ethical_Constraints.md v0.3.
- Close when both documents are committed with
  consistent language.

---

### AP-003 — Audit trail schema (machine-readable) deferred

| Field         | Value                                            |
|---------------|--------------------------------------------------|
| Status        | Open                                             |
| Risk          | Low                                              |
| Priority      | Minor                                            |
| Type          | Technical / Governance                           |
| Blocking      | No                                               |
| Owner         | Admin/Auditor_Protocols.md                       |
| First Logged  | 2026-05-04                                       |
| Last Reviewed | 2026-05-19                                       |

**Description:** A machine-readable format
(JSON/YAML) for recording gate passages, blocks,
and overrides that can be queried and compared
across audit cycles does not yet exist.

**Why It Matters:** Cross-cycle pattern analysis
— detecting whether the same issues recur, whether
blocks result in improvements, whether adversarial
findings cluster around specific document types
— requires structured data, not free text.

**Resolution Path:**
- Structured markdown format (required fields +
  example) already in Observability section.
- JSON/YAML deferred until tooling exists to
  consume it.
- Activate when first cross-cycle pattern
  analysis is needed.
- Discharge via Trajectory if tooling never
  materializes — structured markdown remains
  the permanent format.

---

### Resolution Log

- 2026-05-04: **UNK-004 (Expiry Rule enforcement mechanism)** — Discharged. Sidecar Model (v0.5) addresses the underlying accumulation problem structurally.
- 2026-05-04: **UNK-022 (Full Stop Review trigger conditions)** — Resolved. Three specific trigger conditions and invocation record format added to Full Stop Review section.
- 2026-05-19: **Gate 3 Adversarial Pass** — Upgraded from single-scenario requirement to full Adversarial Challenge Battery (ten classes). New failure mode "Adversarial Theater" added. Fourth Full Stop trigger added. Protocol Performance metrics expanded to include adversarial findings per document.

---

## Relationship to Existing Documents

- `Admin/Ethical_Constraints.md` — parent document; governs permission; hard-line doctrines not subject to override by this protocol
- `Architecture/Forge_flow.md` — structural model; reference standard for shared terminology
- `Admin/Trajectories.md` — destination for scope creep that proves to be valid future work
- `Tests/Leviathan_testing.md` — primary stress-test environment; where Protocol Performance metrics will first be collected
- `Discovery.md` — navigation layer; confirmed file list; Rename Registry for legacy filename aliases
- `Unknowns.md` — global index for cross-module unknowns (index only as of v0.5)
- `Admin/Forge_Audit_Kit.md` — condensed audit reference for routine multi-agent cycles
- `Admin/File_Template.md` — standard file structure for all repository documents
- `Lazarus-Forge-` — companion doctrine repository
- `Astroid-miner` — planned repository; deferred to Leviathan milestone

---

## Status

Version 0.6 — introduces the Adversarial Audit Layer.

**Changes from v0.5:**
- Added Rule 7 to AI Contribution Protocols — repository structure awareness, folder-prefixed canonical paths
- Gate 3 upgraded — now formally gated on Adversarial Challenge Battery, not single scenario
- **Adversarial Audit Layer added** — ten challenge classes, application criteria, sign-off format, anti-patterns table
- Fourth Full Stop trigger added — multiple adversarial findings converging on same structural gap
- Adversarial findings per document added to Protocol Performance metrics
- Adversarial Theater added to Failure Modes
- Observability section updated — adversarial summary now required in audit trail
- Lessons Learned expanded — two new entries on Gate 3 upgrade and epistemic corruption
- Sidecar unknowns reformatted to structured table format per File_Template.md v0.6
- Cross-references updated to canonical folder-prefixed paths throughout
- Unknowns.md reference updated (was Unknowns_LF.md)

**What must remain constant:**

**Confidence never outruns verification.**

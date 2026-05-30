# Engineer_Protocols.md — Engineering Problem-Solving Protocol

> ⚠️ **Operational Safety Advisory**
> Poor engineering judgment or unvalidated creative solutions can lead to
> structural failure, energetic release, wasted resources, or dangerous systems.
> AI-generated designs carry additional risk of subtle errors, overconfidence,
> or context loss between sessions. Prerequisite: always anchor creativity in
> first principles, existing repository knowledge, explicit safety margins, and
> physical validation. Never treat novel ideas as true until tested against
> reality. When in doubt, simplify, increase margin, or hold the solution.
> The cost of elegant but wrong is always higher than the cost of simple and
> proven.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-29                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 4                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cognitive and procedural protocols for engineering problem-solving
  within LazarusForge
- Pragmatic question framework for AI and human contributors
- Assumption challenge triggers — when skepticism is mandatory
- Discipline for balancing innovation with evidence, reuse, and safety
- Anti-reinvention and failure-harvesting rules
- Engineer ↔ Auditor relationship and dispute resolution doctrine
- AI-specific engineering contribution guidance

**This file DOES NOT define:**
- Specific engineering calculations or domain techniques — governed by
  domain files (Operations/, Architecture/)
- General audit or governance procedures — governed by
  `Admin/Auditor_Protocols.md` and `Admin/Forge_Audit_Kit.md`
- Detailed validation test protocols — deferred to domain files
- Engineering authority boundary — see EP-004 in sidecar; undefined
  until resolved
- Auditor role class definitions — governed by
  `Admin/Auditor_Protocols.md` §Auditor Role Classes; this file
  extends the Engineer role defined there, it does not replace it

---

## File Purpose

This file guides AI and human engineers toward effective, reality-grounded
creative problem-solving within the Forge. It replaces vague directives
like "be creative" or "question everything" with a disciplined framework
that maximizes value while minimizing waste, reinvention, and safety
violations.

Without this file, the repository lacks explicit doctrine for how
engineering contributors — human or AI — should approach novel problems.
The gap between governance documents (what is permitted) and domain
specifications (what is built) is where undisciplined engineering
accumulates: hallucinated solutions, duplicated effort, ungoverned
assumptions, and preventable failures.

**Relationship to existing files:** This file extends the Engineer role
defined in `Admin/Auditor_Protocols.md` §Auditor Role Classes. Engineers
operating under this protocol remain subject to all AI Contribution Rules
in Auditor_Protocols.md. This file does not supersede Cognitive_Frameworks.md
— that file governs how Forge systems think under uncertainty; this file
governs how contributors engineer solutions within the repository.

---

## Assumptions

| ID      | Assumption                                                                     | Basis                              | Confidence | Expiry Trigger                                        |
|---------|--------------------------------------------------------------------------------|------------------------------------|------------|-------------------------------------------------------|
| ASM-001 | Contributors have access to the full repository and Discovery.md               | Standard Forge operating context   | High       | Repository access restricted                          |
| ASM-002 | Physical prototyping and testing capability exists at some level               | Core Forge capability — Analogous  | Medium     | Confirmed no-test environment                         |
| ASM-003 | Lessons Learned and Unknowns sections are actively maintained                  | Repository integrity doctrine      | Medium     | Observed systemic neglect                             |
| ASM-004 | "Engineering authority" in this file refers to governance intent, not cryptographically enforced implementation | Honest v0 acknowledgment | High | Phase 3 cryptographic enforcement per `Admin/Security_Protocols.md` |

---

## Body

### 1. Engineering Mindset

Effective Forge engineering is constrained creativity — not unconstrained
ideation. The goal is to deliver functional value with minimal resources
while preserving safety and institutional memory.

**Core posture:**
> "The only reasonable response to 'Question everything?' is 'Why should I?'"

Skepticism must be targeted and justified by potential impact, uncertainty,
or evidence of prior failure. Indiscriminate skepticism wastes cycles
re-litigating settled knowledge. Targeted skepticism catches the failures
that matter.

Engineering is disciplined adaptation under constraints. It is neither
pure creativity nor pure bureaucracy.

---

### 2. Pragmatic Question Framework

Apply this framework on every non-trivial engineering problem before
proposing a solution.

**1. Is it actually needed?**
What is the measurable value? What failure occurs if we do nothing or use
a simpler alternative? Feature and capability creep are common failure
modes in complex systems.

**2. Has a solution already been found?**
Search in this order: `Discovery.md` → relevant module files →
Lessons Learned → `Unknowns.md` → `Architecture/Forge_Net.md` (when
available). `Discovery.md` is the primary navigation layer. Repository
search begins there unless a direct canonical reference is already known.
This is repository doctrine, not a suggestion.

**3. What worked, what failed, and why?**
Consult Lessons Learned before proposing new approaches. A solution that
ignores documented prior failure is not a solution — it is a repetition.

**4. What are the real constraints?**
Safety, materials (especially salvaged and imperfect), energy, tools,
time, environment, skill level. Constraints are not obstacles — they are
the problem definition.

**5. What is the simplest thing that could work?**
Apply the "good enough for now" standard. Complexity is debt. Every
additional component is a failure mode waiting to manifest.

**6. What are the three most likely failure modes?**
Perform lightweight failure mode analysis. Identify load paths, single
points of failure, and environmental derating. A design that has not been
stress-tested against its three most likely failures is not a design —
it is a hope.

**7. Why should I question this assumption?**
Only challenge assumptions with evidence of weakness or high downstream
risk. See Assumption Challenge Triggers below for mandatory conditions.

**8. How will we test and validate this?**
Define success criteria and test plan before building. Untestable
specifications are not specifications.

**9. What knowledge will this create or preserve?**
Every engineering effort should feed Lessons Learned or resolve an
Unknown. Knowledge that is not captured is lost at the next session
boundary.

**10. What is the rollback or fail-safe plan?**
Reversibility is a design requirement. Irreversible actions require
explicit justification and elevated authorization per
`Admin/Ethical_Constraints.md` and `Admin/Auditor_Protocols.md`
§Human Override Doctrine.

#### Assumption Challenge Triggers

Questioning an assumption becomes mandatory when one or more of the
following apply:

- Safety consequences exceed acceptable risk threshold
- Failure cost exceeds replacement cost
- Assumption has never been validated against physical evidence
- Environmental conditions differ from the original context of the
  assumption
- Lessons Learned contain contradictory evidence
- `Unknowns.md` contains related unresolved items in the same cluster

Without explicit triggers, skepticism thresholds vary by contributor
and audit cycles become unpredictable.

---

### 3. Creative Problem-Solving Doctrine

**First Principles and Constraint Harvesting**
Break the problem to physics, then creatively recombine under real
constraints. Do not begin with solutions — begin with constraints.

**Analogy Control**
Analogies are useful but dangerous. Always validate the mapping: does the
analog system share the same constraints, failure modes, and operating
environment? If not, the analogy is a starting point, not an answer.

**Reuse First, Innovate Last**
Prefer adaptation of existing solutions documented in
`Architecture/Components.md` and `Operations/Gate_06_Fabrication.md`.
Novel solutions carry unknown failure modes. Adapted solutions carry
documented ones.

**Salvage-Aware Design**
Assume imperfect materials. Design for repairability, graceful
degradation, and component substitution. A design that only works with
perfect inputs is fragile. A design that degrades predictably under
imperfect inputs is robust.

**Iteration Speed**
Fast, cheap, small-scale prototypes beat perfect simulation. Simulation
is a planning tool. Physical testing is the verification gate.

**Documentation Discipline**
Record assumptions, decisions, and test results immediately. Context
loss between sessions is a primary failure mode for multi-agent
workflows. What is not recorded is lost.

---

### 4. Anti-Reinvention Rules

- Never invent what can be referenced.
- `Discovery.md` is the primary navigation layer — search there first.
- Consult `Admin/Canonical_Terms.md` for terminology before introducing
  new terms.
- Log solved problems into Lessons Learned immediately.
- New solutions must explicitly address why prior approaches were
  insufficient. "I didn't know it existed" is not a sufficient reason.
- Cross-reference `Discovery.md` Rename Registry before assuming a
  file does not exist — it may have been renamed.

---

### 5. AI-Specific Engineering Guidance

AI contributors carry specific failure modes that human contributors do
not share at the same rate. This section addresses them directly.

- **Use tools before generating.** Search the repository, read the
  relevant files, check Discovery.md before producing new content.
  Generation without context produces hallucinated solutions.
- **Declare context limitations explicitly.** If operating under token
  constraints or without access to a relevant file, say so. Confident
  output under incomplete context is a governance failure mode.
- **Cross-reference canonical files rather than paraphrasing from
  memory.** Memory across sessions is unreliable. Canonical files are
  the source of truth.
- **Flag uncertainty and required validation steps when proposing novel
  approaches.** Novel is not better. Novel means unvalidated.
- **Treat confidence as provisional until physically tested.** High
  internal confidence in an untested design is not evidence of
  correctness — it is evidence of coherent reasoning under assumptions
  that may be wrong.
- **Apply AI Contribution Rules 1–7 from `Admin/Auditor_Protocols.md`.**
  Role declaration, lineage tracking, and assumption extraction apply to
  engineering contributions as much as to audit contributions.

---

### 6. Failure Harvesting

Every failure is data. Capture immediately and completely:

| Field | Content |
|-------|---------|
| What was tried | Specific approach or solution |
| What failed | Specific failure mode or outcome |
| Root cause | If known; "unknown" is acceptable and honest |
| What was learned | Concrete operational insight |
| Revalidation needed | Yes / No — with trigger condition |

Captured failures must be reviewed for institutional closure across four
pathways. A failure that is archived but never closes a loop is lost
institutional memory:

1. **Lessons Learned entry** — is this a permanent record worth
   preserving for future contributors?
2. **Unknown closure opportunity** — does this resolve or inform an
   open sidecar entry?
3. **Design standard update** — does this change how we build or
   specify?
4. **Audit protocol update** — does this change how we verify or test?

---

### 7. Engineer ↔ Auditor Relationship

Engineers optimize for solution generation.
Auditors optimize for failure detection.
Neither role supersedes the other.

Both are necessary. A repository with only engineers accumulates
unverified claims. A repository with only auditors accumulates governance
without progress. The tension is productive when it is explicit.

**Dispute resolution sequence:**

1. **Evidence** — physical test data or documented analog from a similar
   system. Evidence ends most disputes.
2. **Testing** — define a falsifiable test, run it, accept the result.
3. **Specification** — if the dispute reveals a gap in existing doctrine,
   promote the resolution into body specification.
4. **Governance escalation** — if unresolved after three cycles, route
   to `Admin/Auditor_Protocols.md` §Dispute Handling Protocol and log in
   the file's Active Disputes table.

**Role boundary:**
This file extends the Engineer role defined in `Admin/Auditor_Protocols.md`
§Auditor Role Classes. Engineers operating under this protocol remain
subject to all AI Contribution Rules and Human Contributor Protocols in
Auditor_Protocols.md. Engineering decisions that cross into safety-adjacent,
scope-expanding, or Tier 1 Axiom-adjacent territory require elevation to
the appropriate governance layer — see EP-004 for the unresolved boundary
definition.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                              | What Failed                                              | What Was Learned                                                                                  | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------|----------------------------------------------------------|---------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-29 | Anecdotal     | Broad "question everything" approach        | Wasted effort on settled problems                        | Targeted skepticism anchored in explicit triggers is superior to indiscriminate skepticism        | Anecdotal  | Yes                 |
| 2026-05-29 | Audit Review  | Engineer role defined without explicit Auditor relationship | Role boundary became ambiguous under governance pressure | Engineer and Auditor roles must be explicitly complementary with a defined dispute resolution sequence | Analogous | Yes              |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                    | Reconsider? |
|------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------|
| 2026-05-29 | "Question everything" as core engineering posture                 | Rewards indiscriminate skepticism; wastes cycles on settled knowledge; replaced with targeted triggers | No      |
| 2026-05-29 | Engineering protocol as standalone authority independent of Auditor_Protocols.md | Creates parallel governance; this file extends, not replaces, existing role doctrine | No   |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Pragmatic Question Framework reduced below 8 questions without
  documented rationale
- Assumption Challenge Triggers section removed or made optional
- Engineer ↔ Auditor relationship section removed or scope reversed
  to imply one role supersedes the other
- Anti-Reinvention Rules no longer reference Discovery.md as primary
  navigation layer
- AI-Specific Engineering Guidance section removed or merged into
  generic guidance that does not address AI-specific failure modes
- Failure Harvesting four-pathway closure loop removed
- EP-003 or EP-004 closed without resolution evidence
- Derivation relationship to Auditor_Protocols.md §Auditor Role Classes
  removed from Scope Boundary or File Purpose
- File moved out of Admin/ without updating all cross-references
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### EP-001 — Validation of Pragmatic Question Framework

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Technical                    |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** Effectiveness of the 10-question framework has not been
operationally tested across multiple engineering domains within the
repository. The framework was derived from general engineering practice,
not from Forge-specific operational experience.

**Why It Matters:** Different engineering domains (thermal, mechanical,
electronics, governance) may require different question weighting or
additional domain-specific triggers. A framework that works well for
hardware design may be poorly calibrated for governance document
engineering.

**Resolution Path:** Payment via Specification — collect operational
feedback from at least three engineering contributions that explicitly
used the framework. Log outcomes in Lessons Learned. Adjust question
weighting or add domain-specific variants if patterns emerge.

---

### EP-002 — AI vs Human Protocol Optimization

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Low                          |
| Priority      | Minor                        |
| Type          | Architectural                |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The AI-Specific Engineering Guidance section identifies
AI failure modes but does not define optimal adjustments for AI
context-window limitations, tool-use sequencing, or the difference
between AI intuition (pattern matching) and human intuition (embodied
experience).

**Why It Matters:** Multi-agent workflows require contributors to
understand not just what to do but how AI and human contributors
complement each other's blind spots. The current section addresses
AI failure modes but not AI strengths that should be deliberately
leveraged.

**Resolution Path:** Payment via Specification — expand Section 5 with
explicit AI strength leverage doctrine (systematic search, cross-reference
consistency, pattern detection across large corpora) balanced against
known failure modes. Cross-reference `Architecture/Cognitive_Frameworks.md`
for alignment with distributed cognition doctrine.

---

### EP-003 — Integration Mapping with Auditor_Protocols.md and Cognitive_Frameworks.md

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The relationship between this file and
Auditor_Protocols.md is partially defined (Engineer role extension,
dispute resolution routing) but the relationship with
Cognitive_Frameworks.md is not yet mapped. Cognitive_Frameworks.md
defines how Forge systems think under uncertainty; this file defines
how contributors engineer solutions. The boundary and handoff between
them is implicit.

**Why It Matters:** Without explicit integration mapping, contributors
may apply cognitive frameworks where engineering protocols are called
for, or vice versa. Procedural overlap between the two files could
accumulate silently.

**Resolution Path:** Payment via Specification — add a dedicated
cross-reference paragraph in the Relationship section mapping: (1)
what Cognitive_Frameworks.md owns that this file defers to; (2) what
this file owns that Cognitive_Frameworks.md defers to; (3) the handoff
condition between them.

---

### EP-004 — Engineering Authority Boundary Undefined

| Field         | Value                        |
|---------------|------------------------------|
| Status        | Open                         |
| Risk          | Medium                       |
| Priority      | Major                        |
| Type          | Governance                   |
| Blocking      | No                           |
| Owner         | Admin/Engineer_Protocols.md  |
| First Logged  | 2026-05-29                   |
| Last Reviewed | 2026-05-29                   |

**Description:** The file assumes engineering autonomy without defining
what decisions engineers may make independently versus what requires
auditor concurrence or human operator approval. The boundary between
engineering decisions and policy decisions is not documented.

**Why It Matters:** As the repository grows, contributors need a clear
boundary. Without it, engineers either over-escalate (slowing progress)
or under-escalate (accumulating ungoverned decisions that may later
conflict with governance doctrine). Safety-adjacent, scope-expanding,
and Tier 1 Axiom-adjacent decisions are the highest-risk undifferentiated
zone.

**Resolution Path:** Payment via Specification — define at minimum:
(1) decisions within engineer authority (material substitution within
spec, prototype iteration, test design, Lessons Learned entries);
(2) decisions requiring auditor concurrence (scope changes, new
capability claims, safety-adjacent choices, cross-module dependency
additions); (3) decisions requiring human operator approval (irreversible
actions, first operational runs, Tier 1 Axiom-adjacent choices).
Cross-reference `Admin/Auditor_Protocols.md` §Human Override Doctrine
and `Admin/Ethical_Constraints.md` for the hard floors that cannot be
overridden regardless of engineering authority level.

---

### Resolution Log

- 2026-05-29: v0.1 created by Grok (Fabricator/Systems). Initial
  10-question framework, creative problem-solving doctrine, anti-
  reinvention rules, AI-specific guidance, and failure harvesting
  defined. EP-001 through EP-003 logged.
- 2026-05-29: v0.2 revision — ChatGPT Skeptic/Auditor and Claude
  Skeptic/Auditor findings actioned. Assumption Challenge Triggers
  added as mandatory subsection under Question 7. Failure Harvesting
  four-pathway closure loop added. Discovery.md priority explicitly
  anchored in Anti-Reinvention Rules and Question 2. Engineer/Auditor
  relationship section added (Section 7) with explicit derivation
  statement from Auditor_Protocols.md. EP-004 logged (engineering
  authority boundary). Drift Indicators section replaced with full
  mandatory re-audit conditions. Body Stability updated to Transitional.
  Spec Gates updated to 2/6. Open Unknowns updated to 4. All EP-
  owner fields corrected to Admin/Engineer_Protocols.md. Abandoned
  Paths section populated. ASM-004 added to Assumptions.

---

## Relationship to Existing Documents

- `Admin/Auditor_Protocols.md` — Tier 2; this file extends the Engineer
  role defined in §Auditor Role Classes; AI Contribution Rules and Human
  Contributor Protocols defined there apply to engineering contributions;
  dispute escalation routes to §Dispute Handling Protocol
- `Admin/Forge_Audit_Kit.md` — Tier 3; condensed audit reference;
  engineering contributions are subject to the Fallacy Checklist and
  Verification Gates defined there
- `Admin/Governance_Charter.md` — Tier 1; EP-004 engineering authority
  boundary must not conflict with Tier 1 Axioms; safety-adjacent and
  irreversible engineering decisions defer to constitutional doctrine
- `Admin/Ethical_Constraints.md` — Tier 1; hard floors for all
  engineering decisions; Anti-Weaponization and Life Preservation
  doctrines are not subject to engineering authority override
- `Admin/Canonical_Terms.md` — vocabulary reference; engineering
  contributions must use canonical terms; new terms introduced by
  engineering work should be routed here for registration
- `Architecture/Cognitive_Frameworks.md` — defines how Forge systems
  think under uncertainty; this file defines how contributors engineer
  solutions; explicit integration mapping deferred to EP-003
- `Admin/Trajectories.md` — destination for engineering capabilities
  that are valid future work but out of current version scope
- `Discovery.md` — primary navigation layer; mandatory first search
  target for all engineering problem-solving
- `Unknowns.md` — EP-001 through EP-004 to be added to Governance &
  Verification section at next Unknowns.md update

---

## Status

Version 0.2 — revised draft (2026-05-29).

**Gate status:** G1 (internal coherence) and G2 (physical plausibility
as a governance document) assessed as passing. G3 through G6 require
formal audit pass by a different agent.

**What must remain constant:**

**Engineering is disciplined adaptation under constraints.**

**Skepticism must be targeted, not indiscriminate.**

**Every engineering effort should capture knowledge, not just output.**

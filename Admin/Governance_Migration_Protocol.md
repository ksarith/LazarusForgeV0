# Governance_Migration_Protocol.md — LazarusForgeV0

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-05                                                          |
| Auditor          | Claude — Architect/Auditor                                          |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Standard migration procedures for Tier 2–5 governance documents
- Tier 1 Axiom amendment process — proposal, review, ratification, and recording
- Engineer role in amendment proposal assembly
- Evidence standard required before a Tier 1 amendment enters formal review
- Human ratification requirements and what distinguishes genuine ratification
  from rubber-stamping
- Hard floor — constraints outside amendment scope entirely
- Ownership transfer declaration: governance migration doctrine moves from
  `Admin/Governance_Charter.md` (transitional holder) to this file
- Compatibility status declaration requirements for all migrations
- Amendment recording requirements (Resolution Log preservation of prior text)

**This file DOES NOT define:**
- The Tier 1 Axioms themselves (→ `Admin/Governance_Charter.md`)
- Constitutional governance hierarchy (→ `Admin/Governance_Charter.md`)
- Cryptographic authentication of ratification events
  (→ `Admin/Security_Protocols.md` — GOV-006 resolution path)
- Minimum agent quorum definition (→ GOV-008 — `Admin/Governance_Charter.md`)
- Repository integrity enforcement mechanics
  (→ `Admin/Repository_Integrity_Protocol.md`)
- Auditor operational behavior during migration review
  (→ `Admin/Auditor_Protocols.md`)

---

## File Purpose

This file operationalizes the Governance Migration Doctrine declared in
`Admin/Governance_Charter.md`. The Charter defines what governance migration
must preserve and what Tier 1 amendment constraints apply — this file defines
how those requirements are executed in practice.

Without this file, GOV-001 remains open and Tier 1 Axiom amendment has no
formal procedure. The gap is not academic: a system with constitutional
constraints but no amendment process is either permanently frozen (which
violates Axiom Q-3 — Corrigibility) or subject to informal amendment that
bypasses all safeguards (which enables Constitutional Capture). This file
closes that gap by making amendment possible through a defined, auditable,
human-ratified process — while making Constitutional Capture structurally
harder.

**Ownership transfer:** The Charter currently lists governance migration
doctrine as "Active — Governance_Charter.md" in the Canonical Governance
Ownership table. This file takes over that ownership. The Charter's
Governance Migration Doctrine section remains the source of constraints;
this file is the executing procedure. The Charter should be updated on
next audit pass to reflect this transfer.

**Honest v0 acknowledgment:** At v0 with a single human contributor and
no multi-agent quorum, the Tier 1 amendment process is largely theoretical.
Its value now is structural: defining the process before it is needed
prevents the process from being shaped by the pressures of a specific
amendment in progress. The procedure must exist before the argument.

---

## Assumptions

| ID      | Assumption | Basis | Confidence | Expiry Trigger |
|---------|------------|-------|------------|----------------|
| ASM-001 | The human operator is the sole ratification authority at v0 | Single-contributor bootstrap context | High | Additional human contributors confirmed |
| ASM-002 | No Tier 1 amendment will be needed before multi-agent quorum is established | v0 operational scope is narrow | Medium | Operational friction surfaces axiom inadequacy before quorum |
| ASM-003 | Engineer role is defined and operational per Admin/Engineer_Protocols.md | File exists and is active | High | Engineer_Protocols.md scope boundary revised |
| ASM-004 | Security_Protocols.md will eventually provide cryptographic ratification authentication | GOV-006 resolution path | Medium | Security_Protocols.md descoped or deferred beyond v1 |
| ASM-005 | Lower-tier governance migrations are significantly more frequent than Tier 1 amendments | Expected operational pattern | High | Tier 1 amendment is triggered early in repo lifecycle |

---

## I. Two Migration Tracks

All governance migration in LazarusForgeV0 falls into one of two tracks.
The tracks are not interchangeable. Applying the wrong track to a migration
is a governance error.

### Track A — Standard Migration (Tiers 2–5)

For all governance documents below Tier 1: operational protocols, audit
procedures, domain specifications, condensed references, and supporting
governance files.

Track A is the expected operational path. Most governance evolution happens
here. The process is lighter than Track B by design — governance complexity
must remain proportional to operational value.

### Track B — Tier 1 Axiom Amendment

For any change to the eight Tier 1 Axioms (P-1 through P-4, Q-1 through Q-4)
in `Admin/Governance_Charter.md`.

Track B carries substantially higher process requirements than Track A.
The difference is not bureaucratic — it reflects the difference between
adjusting a procedure and changing a foundational constraint that all
other governance derives from.

**Track identification rule:** If a proposed change touches the text,
scope, or interpretation of any Tier 1 Axiom, it is Track B. When in
doubt, treat as Track B. Misclassifying a Track B migration as Track A
is a Constitutional violation.

---

## II. Track A — Standard Migration Procedure

### Trigger

Track A migration is triggered when:
- An existing Tier 2–5 governance document requires substantive revision
- A new governance document is created that affects existing ownership boundaries
- A canonical ownership transfer is declared

Routine content updates within a file's existing scope are not migrations —
they are normal audit cycle revisions. Migration applies when scope,
ownership, or authority relationships change.

### Procedure

**Step 1 — Prior State Preservation**
Save the current version per `Admin/Repository_Integrity_Protocol.md`
Version Preservation Protocol before any revision begins. This is not
optional — it is the integrity baseline for the migration.

**Step 2 — Compatibility Declaration**
At the start of the revision, declare one of:
- *Compatible* — existing downstream references remain valid without change
- *Partially compatible* — named downstream references require update;
  list them explicitly
- *Incompatible* — migration breaks existing downstream dependencies;
  all dependents must be reviewed before migration is committed

Incompatible migrations require a cross-module review pass before the
revised file is committed to the repository.

**Step 3 — Semantic Change Documentation**
Any change to defined terms, scope boundaries, or authority relationships
must be documented in the Resolution Log with: date, what changed, why,
and what the prior state was.

**Step 4 — Lineage Preservation**
Prior axiom text, scope boundaries, and authority relationships must be
preserved in the Resolution Log. They are not deleted — they are dated
and superseded.

**Step 5 — Downstream Notification**
Files identified in Step 2 as requiring update must have their next audit
pass triggered. This is tracked as a pending correction in Discovery.md
until resolved.

### Authority

Track A migrations may be executed by an engineer contributor with auditor
review. No human ratification is required unless the migration affects
a Tier 1 or Tier 2 document, in which case a human operator review is
strongly recommended before commit.

---

## III. Track B — Tier 1 Axiom Amendment Procedure

### Governing Constraints from the Charter

The following constraints are declared in `Admin/Governance_Charter.md`
Governance Migration Doctrine and are reproduced here for operational
reference. They are not redefined — they are inherited:

- Human ratification is mandatory
- No autonomous agent or coalition may initiate axiom amendment
- Amendment rationale must demonstrate the change strengthens rather
  than narrows protection
- Prior axiom text must be preserved in the Resolution Log with
  amendment date and rationale

This file adds the procedural implementation of those constraints.

### Phase 1 — Engineer Proposal Assembly

The engineer role initiates and assembles the amendment case. This is
the appropriate role because engineers encounter the operational friction
that reveals when an axiom is inadequate — they are closest to the
evidence and hold the "build and refine" mandate.

The engineer role does not ratify. The engineer presents; the human decides.
This separation is structural, not advisory.

**What the engineer must assemble:**

**1. Friction Log**
Documented evidence of operational friction caused by the current axiom
text. A single audit finding is not sufficient. The minimum evidence bar is:
- At least two independent observations across separate audit cycles, OR
- One observation with direct operational consequence (not theoretical),
  documented in a Lessons Learned entry

Theoretical arguments for amendment, however logically compelling, do not
satisfy the evidence bar. The bar exists precisely because compelling
arguments are the primary mechanism of Constitutional Capture.

**2. Amendment Text**
The proposed new axiom text, with tracked changes showing exactly what
is added, removed, or modified. Vague amendments ("strengthen the axiom")
are not valid proposals — the specific wording must be proposed.

**3. Strengthening Justification**
A written justification demonstrating that the amendment strengthens
rather than narrows protection. This is not a neutral requirement — the
burden is affirmative. If the engineer cannot demonstrate strengthening,
the amendment does not advance.

Specifically address:
- What protection the current text provides
- What gap or inadequacy the friction log documents
- How the proposed text closes that gap without reducing other protections
- Whether any Prohibition axiom (Q-series) is affected by the change

**4. Failure Mode Analysis**
How could the proposed amendment be misused? Specifically: could the
amended text be cited to justify an action the current text prohibits?
If yes, the amendment requires redesign before advancing.

This is the Constitutional Capture check. An amendment that opens a
new path to prohibited actions is not a strengthening — it is an erosion
dressed as improvement.

**5. Cross-Reference Map**
Which downstream files reference or depend on the axiom being amended?
All dependents must be identified before ratification. The amendment is
not complete until all dependents are updated or flagged for update.

### Phase 2 — Adversarial Review

Before human ratification, the proposal must pass adversarial review
by at least one auditor who did not participate in Phase 1 assembly.

The adversarial reviewer's mandate is specifically to:
- Attempt to find a path from the amended text to a prohibited action
- Challenge the strengthening justification
- Identify any interpretation of the new text that narrows rather than
  strengthens protection
- Apply the Constitutional Capture failure mode explicitly

The adversarial reviewer is not trying to improve the proposal — they
are trying to break it. If they cannot, the proposal is stronger for it.
If they can, Phase 1 must be revised before advancing.

**At v0:** With a single human contributor, adversarial review may be
conducted by a different AI agent class than assembled the proposal,
or by the human operator themselves using the adversarial reviewer
mandate explicitly. The review must be documented — it cannot be implicit.

### Phase 3 — Human Ratification

Human ratification is the constitutional requirement. It is not a
formality following Phase 2 — it is the decision.

**What ratification requires:**

The human ratifying party must:
1. Read the Friction Log and confirm the operational need is genuine
2. Read the proposed amendment text and the current text side by side
3. Read the Strengthening Justification and independently assess it
4. Read the adversarial review findings and the Phase 1 response
5. Make an explicit, documented decision: ratify, reject, or return
   to Phase 1 with specific concerns

**What ratification is not:**

Ratification is not approval of an AI-assembled argument. The human
is not evaluating whether the argument is logically sound — they are
exercising independent judgment about whether the amendment is right.
A human who ratifies because the argument is compelling without forming
an independent view has not ratified — they have delegated a
constitutional decision to an AI. That is a Constitutional violation
regardless of the amendment's merits.

**Ratification record:**
The ratifying human must produce a dated written record stating:
- The amendment being ratified (specific axiom, specific text change)
- That they reviewed Phase 1 and Phase 2 materials
- Their independent assessment (not just "I agree with the argument")
- The date of ratification

**Authentication gap:** Until `Admin/Security_Protocols.md` reaches
Provisional Specification status, ratification records must satisfy
the interim authentication requirement in the Charter's Human Override
Doctrine: independent confirmation from a second human, external
cryptographic signature, or dated physical/digital record outside the
repository system. See GMP-004.

### Phase 4 — Recording

After ratification, the amendment is recorded and committed.

**Required records:**

1. Prior axiom text preserved verbatim in the Resolution Log of
   `Admin/Governance_Charter.md` with amendment date and rationale summary

2. New axiom text committed to Governance_Charter.md with a Resolution
   Log entry citing the ratification record

3. This file's Resolution Log updated with amendment summary and
   cross-reference to the ratification record

4. All downstream files identified in the Cross-Reference Map updated
   or flagged as pending update in Discovery.md

5. Unknowns.md updated if the amendment resolves or affects any
   open cross-module unknowns

### Hard Floor — Outside Amendment Scope

The following constraints may not be amended through Track B or any
other process:

**Anti-Weaponization Doctrine** — defined in `Admin/Ethical_Constraints.md`.
This is a co-Tier 1 constraint that does not derive from the Axioms —
it sits alongside them. It is not subject to the amendment process
defined here. Any proposal that would weaken, narrow, or create
exceptions to the Anti-Weaponization Doctrine is outside scope regardless
of how it is framed.

**The Ethical Anchor field canonical string** — "Attempt to do no harm.
Defer to Ethical_Constraints.md if present." This string is fixed in
every repository file per `Admin/File_Template.md`. It is not a
governance document — it is the floor that survives document loss.
It is not amendable through governance migration.

**Axiom P-1 humanitarian override exception** — permanently abandoned
per Governance_Charter.md Abandoned Paths (2026-05-23). The humanitarian
override entry point is the historical attack vector on ethical constraints
in autonomous systems. It remains closed regardless of argument quality.
This is not subject to amendment.

---

## IV. Migration Compatibility Classification

All migrations — Track A or Track B — must declare a compatibility class.

| Class | Meaning | Required Action |
|---|---|---|
| Compatible | Downstream references remain valid | None beyond standard Resolution Log |
| Partially compatible | Named downstream files require update | List files; trigger audit pass for each |
| Incompatible | Migration breaks downstream dependencies | Cross-module review before commit; no partial deployment |
| Constitutional | Migration affects Tier 1 Axioms | Track B mandatory regardless of other classification |

A migration may carry multiple classes — a Track B amendment that is
also partially compatible with downstream files carries both obligations.

---

## V. Migration Record Requirements

Every migration must produce a record containing:

1. Migration date
2. Track (A or B)
3. Compatibility class
4. What changed — specific text, scope, or authority relationship
5. Why — friction log reference or rationale summary
6. Prior state — what was true before (preserved, not deleted)
7. Downstream impact — files requiring update and their status
8. For Track B: ratification record reference

Records live in the Resolution Log of the file being migrated, and
in this file's Resolution Log for Track B amendments.

---

## Lessons Learned

| Date | Evidence Type | What Was Tried | What Failed | What Was Learned | Confidence | Revalidation Needed |
|------|---------------|----------------|-------------|------------------|------------|---------------------|
| —    | —             | —              | —           | No entries yet — pre-deployment file | — | — |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### GMP-001 — GOV-001 resolution confirmation pending

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Low                                |
| Priority      | Minor                              |
| Type          | Governance                         |
| Blocking      | No                                 |
| Owner         | Admin/Governance_Migration_Protocol.md |
| First Logged  | 2026-06-05                         |
| Last Reviewed | 2026-06-05                         |

**Description:** This file is the intended resolution target for GOV-001
in `Admin/Governance_Charter.md`. GOV-001 status should be updated to
In Progress or Resolved on next audit pass of Governance_Charter.md.

**Why It Matters:** Open unknowns whose resolution targets exist but
haven't been updated create false signals in the unknowns index.

**Resolution Path:** On next audit pass of Governance_Charter.md, update
GOV-001 status and cross-reference this file. Update Unknowns.md if
GOV-001 is tracked there.

---

### GMP-002 — Canonical Governance Ownership transfer not yet recorded in Charter

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Low                                |
| Priority      | Minor                              |
| Type          | Governance                         |
| Blocking      | No                                 |
| Owner         | Admin/Governance_Migration_Protocol.md |
| First Logged  | 2026-06-05                         |
| Last Reviewed | 2026-06-05                         |

**Description:** The Charter's Canonical Governance Ownership table
lists governance migration doctrine as "Active — Governance_Charter.md
(transitional)." This file now owns that domain. The Charter table
needs updating.

**Why It Matters:** Stale ownership entries create routing ambiguity
for future auditors and AI instances.

**Resolution Path:** On next audit pass of Governance_Charter.md,
update Canonical Governance Ownership table entry for governance
migration doctrine to reference this file. Track A migration —
compatible with all downstream files.

---

### GMP-003 — Adversarial review at v0 single-contributor context underspecified

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Major                              |
| Type          | Governance                         |
| Blocking      | No                                 |
| Owner         | Admin/Governance_Migration_Protocol.md |
| First Logged  | 2026-06-05                         |
| Last Reviewed | 2026-06-05                         |

**Description:** Section III Phase 2 notes that at v0, adversarial
review may be conducted by a different AI agent class or by the human
operator using the adversarial mandate explicitly. This is a bootstrap
proxy, not a robust solution. The adequacy of single-contributor
adversarial review for a Tier 1 amendment has not been validated.

**Why It Matters:** Adversarial review conducted by the same human
who assembled the proposal, even under an adversarial framing, is
structurally weaker than independent review. A compelling amendment
argument may be harder to challenge from the inside.

**Resolution Path:** Acceptable at Exploration stage — the constraint
that review must be documented prevents purely implicit self-review.
At Draft or above, define minimum adversarial review independence
requirements. Cross-reference GOV-008 (quorum definition) —
multi-agent quorum resolves this structurally.

---

### GMP-004 — Ratification authentication gap mirrors GOV-006

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | High                               |
| Priority      | Major                              |
| Type          | Security / Governance              |
| Blocking      | No                                 |
| Owner         | Admin/Governance_Migration_Protocol.md |
| First Logged  | 2026-06-05                         |
| Last Reviewed | 2026-06-05                         |

**Description:** Section III Phase 3 notes the authentication gap for
ratification records — until Security_Protocols.md reaches Provisional
Specification, ratification relies on interim authentication requirements
from the Charter. The interim requirement (second human, external
signature, or external dated record) is a placeholder, not a solution.

**Why It Matters:** A ratification record that cannot be authenticated
is a paper guarantee. Any system capable of fabricating plausible
human-sounding text could fabricate a ratification record. This is
the highest-risk attack vector against the Tier 1 amendment process.

**Resolution Path:** Mirrors GOV-006 resolution path — Security_Protocols.md
cryptographic authentication is the target. Until then, the interim
requirement is the operative constraint. Cross-reference SEC-007
(external root-of-trust architecture) — ratification authentication
is one of the primary use cases for that architecture.

---

### GMP-005 — Track A / Track B boundary at Tier 2 documents not fully tested

| Field         | Value                              |
|---------------|------------------------------------|
| Status        | Open                               |
| Risk          | Medium                             |
| Priority      | Minor                              |
| Type          | Governance                         |
| Blocking      | No                                 |
| Owner         | Admin/Governance_Migration_Protocol.md |
| First Logged  | 2026-06-05                         |
| Last Reviewed | 2026-06-05                         |

**Description:** The Track A / Track B boundary is clear at the
extremes — routine spec updates are Track A, Tier 1 Axiom text
changes are Track B. The boundary at Tier 2 documents
(Auditor_Protocols.md) is less tested. A change to Auditor_Protocols.md
that effectively reinterprets a Tier 1 Axiom without touching its
text could be misclassified as Track A.

**Why It Matters:** Constitutional Capture can operate through
reinterpretation rather than text amendment. A procedure that only
catches text changes to Tier 1 Axioms is incomplete.

**Resolution Path:** Add interpretive change detection to the Track
identification rule. Proposed addition: "If a Tier 2 change redefines
how a Tier 1 Axiom is applied, or introduces a new exception to Tier 1
constraints, it is Track B regardless of whether Tier 1 text is
modified." Payment via Specification — requires adversarial review
before adopting.

---

### Resolution Log

*(empty — first version)*

---

## Abandoned Paths

| Date | Path | Why Abandoned | Reconsider? |
|------|------|---------------|-------------|
| 2026-06-05 | Single unified procedure for all governance migration | Tier 1 and Tier 2–5 migrations have fundamentally different risk profiles and authority requirements. A single procedure either over-burdens routine updates or under-protects constitutional amendments. Two-track structure adopted. | No |
| 2026-06-05 | Placing ratification authority with the engineer role | Engineers hold proposal authority because they are closest to operational friction. Ratification authority requires independence from the proposal — an engineer ratifying their own amendment case is not independent review. Human ratification is the constitutional requirement. | No |
| 2026-06-05 | Defining specific axioms as permanently unamendable via Track B | Axiom Q-3 (Corrigibility) requires the system to remain revisable. Making specific axioms formally unamendable through any process would violate Q-3. Instead, the hard floor targets specific exceptions (Anti-Weaponization, humanitarian override) that are outside scope by explicit prior decision — not by constitutional prohibition on amendment. | No |

---

## Drift Indicators

*Standard drift indicators per `Admin/File_Template.md` apply. Additional
triggers specific to this file:*

- Track B procedure is invoked before GMP-003 (adversarial review
  underspecification) is resolved
- Phase 3 ratification record requirement is weakened or made implicit
- The hard floor section is amended to remove Anti-Weaponization or
  the humanitarian override closure
- Track identification rule is narrowed to text-only changes without
  addressing interpretive reinterpretation (GMP-005)
- GMP-002 (ownership transfer) remains unresolved after three audit
  cycles of Governance_Charter.md
- Any amendment to this file that reduces the evidence bar for
  Phase 1 Friction Log

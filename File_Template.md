# LF_File_Template.md

**Standard file structure for LazarusForgeV0 documents.**
**Apply to all new files and retrofit to existing files during audit cycles.**

---

## Structure Overview

Every file in LazarusForgeV0 follows this structure:

```
1. FILE STATE             — Machine-readable metadata table, top of file
2. SCOPE BOUNDARY         — Hard limits on what this file owns
3. FILE PURPOSE           — One paragraph of human-readable intent
4. BODY                   — Clean content, no audit noise
5. LESSONS LEARNED        — Operational memory, cumulative, never deleted
6. ACTIVE DISPUTES        — Interpretation conflicts, separate from unknowns
7. AUDITOR NOTES          — Active unknowns sidecar, shrinks toward zero
8. ABANDONED PATHS        — Graveyard for dead ideas (optional)
```

The **Body** must stand alone. Footer sections are additive and never corrupt the content.
A Specification-level body should be fully understandable without its footer.

---

## 1. File State (Machine-Readable)

Place immediately after the file title, before any content.

```markdown
## File State

| Field          | Value                                      |
|----------------|--------------------------------------------|
| Status         | Exploration / Draft / Specification        |
| Body Stability | Volatile / Transitional / Stable           |
| Spec Gates     | 0/6                                        |
| Last Audit     | YYYY-MM-DD                                 |
| Auditor        | [Agent — Role]                             |
| Open Unknowns  | N (Low / Medium / High)                    |
| Highest Risk   | Low / Medium / High                        |
| Sidecar Link   | #auditor-notes--unknowns                   |
```

**Status definitions:**
- **Exploration** — Incomplete by design; ideas in progress; not yet pressured toward specification
- **Draft** — Content is substantive; promotion to Specification is being actively worked
- **Specification** — Has passed all six verification gates; claims are binding

**Body Stability definitions:**
- **Volatile** — Expected to change significantly; aggressive restructuring is acceptable
- **Transitional** — Stabilizing but still under revision; preserve intent, not wording
- **Stable** — Wording should be preserved unless there is critical need to change it

**Spec Gates:** Tracks progress toward Specification. A file cannot be promoted to Specification
without passing all six gates. Prevents premature promotion.

The File State table is the first thing an agent reads. It determines whether to load the full
file, jump to the sidecar, or flag for a Resolution Pass before proceeding.

---

## 2. Scope Boundary

Place immediately after File State. This is the second thing an agent reads.

```markdown
## Scope Boundary

**This file DOES define:**
- ...

**This file DOES NOT define:**
- ...
```

This section is the primary defense against specification bleed, duplicate ownership, and
infinite document expansion. When in doubt about whether content belongs here, consult the
Scope Boundary first. If it is not listed under DOES, it does not belong in this file's Body.

---

## 3. File Purpose

```markdown
## File Purpose

One clear paragraph explaining what this file exists to do and why it matters to the Forge.
```

Write this as if explaining to a new auditor who has never seen the repository. No jargon,
no forward references. Just purpose.

---

## 4. Body

The document's actual content. Written as if the footer sections do not exist.

**Rules:**
- No audit notes, unknown references, or governance discussion in the Body
- No dispute framing or philosophical argument — those go in Active Disputes
- Cross-references to other Forge files use full GitHub raw URLs per Discovery.md convention
- Quantitative claims carry confidence labels: **(Measured / Estimated / Simulated / Analogous / Placeholder)**
- The Body must be readable and useful without the footer

**Frozen content:** Once a section of the Body has passed a Specification gate and its claims
are binding, mark it with a comment immediately above:

```markdown
<!-- FROZEN: GATE 3 — 2026-05-07 — Do not edit without full audit cycle -->
```

Autonomous agents must not rewrite FROZEN sections. Human auditors must document the reason
and reset the gate status if a FROZEN section must change.

---

## 5. Lessons Learned

Placed after the Body, before Active Disputes. Separated by a horizontal rule.

```markdown
---

## Lessons Learned

Operational memory from building, testing, and failing with this module.
Not governance. This is the Forge's record of what actually happened.

| Date       | Evidence Type                          | What was tried       | What failed              | What was learned              | Confidence                              |
|------------|----------------------------------------|----------------------|--------------------------|-------------------------------|-----------------------------------------|
| YYYY-MM-DD | Bench Test / Field Test / Simulation / Modeling / Anecdotal | [description] | [what went wrong] | [the actual insight] | Measured / Replicated / Simulated / Anecdotal |
```

**Evidence Type** records *how* the finding was generated.
**Confidence** records *how much to trust* the finding.

**What belongs here:**
- Physical test outcomes — a thing was built, it behaved unexpectedly, here is why
- Design decisions that were reversed and the reason for reversal
- Material substitutions that worked or did not work
- Operational conditions that were not anticipated

**What does not belong here:**
- Governance findings → Auditor Notes
- Future plans → Trajectories_LF.md
- Unresolved questions → Auditor Notes sidecar
- Interpretation conflicts → Active Disputes

Lessons Learned is **permanent and cumulative.** Entries are never deleted.
A module with no Lessons Learned entries is either brand new or has never been tested.

---

## 6. Active Disputes

Placed after Lessons Learned. Omit the section entirely only if there are zero disputes.
If there are no current disputes, include the header with an empty table — the category
must remain visible to prompt auditors to actively check for it rather than skip it.

```markdown
---

## Active Disputes

Interpretation conflicts, competing architectural positions, unresolved design disagreements,
and ethical disagreements. Distinct from Unknowns, which are reality gaps.

> Unknowns = reality gap (we do not yet know what is true)
> Disputes = interpretation conflict (we disagree about what is true or right)

| ID     | Dispute Summary | Positions in Conflict | Risk   | Status      | Owner  |
|--------|-----------------|-----------------------|--------|-------------|--------|
| DS-001 | [summary]       | [position A vs B]     | Medium | Open        | [file] |
```

Disputes that remain open across three consecutive audits must be escalated to the
cross-module Unknowns_LF.md for repository-level resolution.

---

## 7. Auditor Notes & Unknowns

The sidecar. Placed after Active Disputes, last before Abandoned Paths.

```markdown
---

## Auditor Notes & Unknowns

### [FILE-PREFIX-NNN] — Short descriptive title

| Field         | Value                                              |
|---------------|----------------------------------------------------|
| Status        | Open / In Progress / Resolved                      |
| Risk          | Low / Medium / High                                |
| Type          | Technical / Ethical / Architectural / Governance   |
| Blocking      | Yes / No                                           |
| Owner         | Module or file responsible for resolution          |
| First Logged  | YYYY-MM-DD                                         |
| Last Reviewed | YYYY-MM-DD                                         |

**Description:** One sentence stating the reality gap.

**Why It Matters:** One sentence on the consequence if left unresolved.

**Resolution Path:** Concrete closure criteria. One of:
- *Payment via Specification* — unknown resolved; content moves into Body as committed spec
- *Discharge via Trajectory* — real but out of scope; route to Trajectories_LF.md
- *Discharge via Lessons Learned* — resolved by operational experience; lesson moves to LL

---

### Resolution Log

- YYYY-MM-DD: [FILE-PREFIX-NNN] — One-line description of how it was resolved or discharged
```

**Local ID format:** File abbreviation + three-digit number.
Examples: `SC-001` (Spin Chamber), `EC-001` (Ethical Constraints), `SR-001` (Support Raft).

**Cross-module unknowns** use the global `UNK-XXX` format and are indexed in `Unknowns_LF.md`.
Reference them here but do not duplicate the full entry.

**The 10-entry rule:** If open entries exceed 10, the file requires a Resolution Pass before
the next audit cycle. Resolved entries move to the Resolution Log — they are not deleted.

**Sidecar size guardrail:** If the sidecar exceeds 20% of total document word count, flag
for Resolution Pass before auditing further.

---

## 8. Abandoned Paths (Optional but strongly recommended)

Place last. Omit if the file is brand new and no paths have been explored yet.

```markdown
---

## Abandoned Paths

Rejected architectures, failed approaches, and disproven assumptions.
Prevents cyclical rediscovery of dead ideas.

| Date       | Path                   | Why Abandoned                    | Reconsider? |
|------------|------------------------|----------------------------------|-------------|
| YYYY-MM-DD | [description of path]  | [reason for abandonment]         | Yes / No    |
```

An entry marked `Reconsider: No` is a hard stop. An agent may not resurrect it without
explicit human authorization and a new dated entry explaining the reason for reconsideration.

---

## Drift Indicators

The following conditions should trigger a mandatory re-audit flag regardless of scheduled
audit cycle:

- Body content contradicts an entry in Lessons Learned
- Open unknown count increases across three consecutive audits
- Any unknown entry remains unreviewed for more than 90 days
- A Specification-level claim lacks an evidence confidence label
- Sidecar exceeds 20% of total document word count
- A FROZEN section has been modified without a dated justification comment
- Active Disputes table has entries older than two audit cycles without escalation

Drift Indicators are not a checklist to complete — they are automatic triggers. Any agent
performing an audit must check these before beginning and halt if multiple indicators are
active simultaneously, flagging for human review.

---

## Retrofit Checklist

When adding this structure to an existing file:

- [ ] Add File State table below the title
- [ ] Add Scope Boundary — be honest about what the file does and does not own
- [ ] Add File Purpose paragraph
- [ ] Review Body for inline audit notes — move to Auditor Notes sidecar
- [ ] Review Body for inline "we tried X" notes — move to Lessons Learned
- [ ] Review Body for interpretation conflicts — move to Active Disputes
- [ ] Mark any Specification-gate-passing content with FROZEN comments
- [ ] Set Status honestly — most existing files are Exploration
- [ ] Set Body Stability honestly — most existing files are Volatile
- [ ] Set Spec Gates to reflect actual verification progress
- [ ] Populate Lessons Learned (empty table is valid initially)
- [ ] Populate Active Disputes (empty table is valid; do not omit the section)
- [ ] Create initial Auditor Notes for all known open unknowns
- [ ] Populate Abandoned Paths if applicable
- [ ] Update File State with today's date and auditor

---

## Minimal Valid File Example

```markdown
# Module Name

## File State

| Field          | Value                         |
|----------------|-------------------------------|
| Status         | Exploration                   |
| Body Stability | Volatile                      |
| Spec Gates     | 0/6                           |
| Last Audit     | 2026-05-07                    |
| Auditor        | Claude — Skeptic/Auditor      |
| Open Unknowns  | 2 (Low)                       |
| Highest Risk   | Low                           |
| Sidecar Link   | #auditor-notes--unknowns      |

## Scope Boundary

**This file DOES define:**
- Core concept and initial requirements for this module

**This file DOES NOT define:**
- Detailed engineering drawings, control software, or cross-module interfaces

## File Purpose

Brief paragraph explaining what this file exists to do and why it matters.

---

[Body content here]

---

## Lessons Learned

| Date | Evidence Type | What was tried | What failed | What was learned | Confidence |
|------|---------------|----------------|-------------|------------------|------------|
| —    | —             | —              | —           | No entries yet   | —          |

---

## Active Disputes

| ID | Dispute Summary | Positions in Conflict | Risk | Status | Owner |
|----|-----------------|-----------------------|------|--------|-------|
| —  | No active disputes | — | — | — | — |

---

## Auditor Notes & Unknowns

### MN-001 — Example unknown

| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | Low               |
| Type          | Technical         |
| Blocking      | No                |
| Owner         | This module       |
| First Logged  | 2026-05-07        |
| Last Reviewed | 2026-05-07        |

**Description:** One sentence stating what is not yet known.

**Why It Matters:** One sentence on consequence if unresolved.

**Resolution Path:** Payment via Specification — once X is tested and confirmed, move to Body.

---

### Resolution Log

*(empty)*
```

---

**This template integrates structural machine-readability (File State, Scope Boundary, Drift
Indicators), operational memory (Lessons Learned with evidence provenance), clean dispute
separation (Active Disputes vs. Unknowns), protection against zombie ideas (Abandoned Paths),
and semantic locking (FROZEN markers) — while preserving the resolution path taxonomy and
lean audit discipline of the original.**

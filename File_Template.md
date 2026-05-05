# LF_File_Template.md
**Standard file structure for LazarusForgeV0 documents.**
**Apply to all new files and retrofit to existing files during audit cycles.**

---

## Structure Overview

Every file in LazarusForgeV0 follows this four-part structure:

```
1. AUDIT HEALTH HEADER    — 5 lines, top of file, machine-scannable
2. BODY                   — clean content, no audit noise
3. LESSONS LEARNED        — operational wisdom, cumulative, never deleted
4. AUDITOR NOTES          — active unknowns sidecar, shrinks toward zero
```

The body stands alone. The footer sections are additive and never corrupt the content.

---

## 1. Audit Health Header

Place immediately below the file title, before any content.

```markdown
**Audit Health:**
- Status: [Exploration | Draft | Specification]
- Last audit: [YYYY-MM-DD] ([Agent — Role])
- Open unknowns: [N] ([Low | Medium | High])
- Sidecar: [#auditor-notes--unknowns]
```

**Status definitions:**
- **Exploration** — incomplete by design; ideas in progress; not yet pressured toward specification
- **Draft** — content is substantive; promotion to specification is being actively worked
- **Specification** — has passed all six verification gates; claims are binding

The Audit Health Header is the first thing an AI agent reads. It determines whether to load the full file or jump to the sidecar.

---

## 2. Body

The document's actual content. Written as if the footer sections do not exist.

Rules:
- No audit notes, unknown references, or governance tags in the body
- Cross-references to other files use raw GitHub URLs per Discovery.md convention
- Quantitative claims carry confidence labels (Measured / Estimated / Analogous / Placeholder)
- The body should be readable and useful without the footer

A document body that requires its footer to be understood is not ready for specification.

---

## 3. Lessons Learned

Placed after the body, before the Auditor Notes sidecar. Separated by a horizontal rule.

```markdown
---

## Lessons Learned

Operational wisdom from building, testing, and failing with this module.
Not governance — this is the forge's memory of what actually happened.

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| YYYY-MM-DD | [brief description] | [what went wrong] | [the actual insight] |
```

**What belongs here:**
- Physical test outcomes (a thing was built, it behaved unexpectedly, here's why)
- Design decisions that were reversed and why
- Material substitutions that worked or didn't
- Operational conditions that weren't anticipated

**What does not belong here:**
- Governance findings (those go in Auditor Notes)
- Future plans (those go in Trajectories_LF.md)
- Unknown questions (those go in the sidecar)

Lessons Learned is **permanent and cumulative**. Entries are never deleted. Even when a module reaches Specification, its Lessons Learned section stays — it's the forge's institutional memory. A module with no Lessons Learned entries is either brand new or has never been tested.

---

## 4. Auditor Notes & Unknowns

The sidecar. Placed last, after Lessons Learned.

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
- [YYYY-MM-DD]: [FILE-PREFIX-NNN] — [one-line description of how it was resolved or discharged]
```

**Local ID format:** File abbreviation + three-digit number.
Examples: `SC-001` (Spin Chamber), `ST-001` (Ship of Theseus), `EC-001` (Ethical Constraints), `SR-001` (Support Raft).

**Cross-module unknowns** (affecting multiple files) use the global `UNK-XXX` format and are indexed in `Unknowns_LF.md`. Reference them here but do not duplicate the full entry.

**The 10-entry rule:** If open entries exceed 10, the file needs a Resolution Pass before the next audit cycle. Resolved entries move to the Resolution Log — they are not deleted, just moved.

**Metadata guardrail:** If the sidecar exceeds 20% of the total document word count, flag for Resolution Pass before auditing.

**Resolution paths:**
- *Payment via Specification* — unknown resolved; content moves into the body as committed spec; entry moves to Resolution Log
- *Discharge via Trajectory* — unknown is real but out of scope for current version; route to Trajectories_LF.md and note in Resolution Log
- *Discharge via Lessons Learned* — unknown was resolved by operational experience; the lesson moves to Lessons Learned, the entry closes

---

## Retrofit Checklist

When adding this structure to an existing file:

- [ ] Add Audit Health Header below the title
- [ ] Review body for any inline audit notes — move to sidecar
- [ ] Review body for any inline lessons or "we tried X" notes — move to Lessons Learned
- [ ] Set Status honestly (most existing files are Exploration)
- [ ] Add Lessons Learned section (can be empty table initially)
- [ ] Add Auditor Notes section with any known open unknowns
- [ ] Update Audit Health Header with today's date and agent

---

## Example: Minimal Valid File

```markdown
# Module Name

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 2 (Low)
- Sidecar: [#auditor-notes--unknowns]

---

[Body content here]

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| — | — | — | No entries yet |

---

## Auditor Notes & Unknowns

### MN-001 — [Short title]
**Status:** Open
**Risk:** Low
**What is not yet known:** [one sentence]
**Resolution path:** [one sentence]
**Logged:** 2026-05-04, Claude — Skeptic/Auditor

### Resolution Log
*(empty)*
```

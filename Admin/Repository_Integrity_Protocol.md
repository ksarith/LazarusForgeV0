# Repository_Integrity_Protocol.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 2/6                                                                 |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| Last Audit       | 2026-06-19                                                          |
| Auditor          | Gemini — Skeptic/Auditor; ChatGPT — Skeptic/Auditor; Grok — Skeptic/Auditor; Claude — Synthesizer |
| Open Unknowns    | 7                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Integrity baseline definitions for each protected repository element
- Violation detection procedures at v0 (human-in-the-loop)
- Violation classification system and response ladder
- Recovery procedures following confirmed violations
- Version preservation requirements and human workflow
- Automation migration path for future versions
- Relationship between integrity doctrine and constitutional axioms
- Incident logging requirements
- Navigation file protection requirements (`Discovery.md` / `Routing.md`)

**This file DOES NOT define:**
- Cryptographic authentication implementation (→ `Admin/Security_Protocols.md`)
- Constitutional governance doctrine (→ `Admin/Governance_Charter.md`)
- Auditor operational behavior (→ `Admin/Auditor_Protocols.md`)
- CI/CD pipeline automation mechanics
- Runtime enforcement code
- Specific tooling implementations
- Governance authority hierarchy (→ `Admin/Governance_Charter.md`)
- Anti-Weaponization doctrine (→ `Admin/Ethical_Constraints.md`)
- Archive retention policy duration (→ RIP-006, pending)
- Integrity incident ownership (→ RIP-007, pending)

---

## File Purpose

This file defines the operational integrity enforcement procedures for LazarusForgeV0. It exists to bridge the gap between the `Admin/Governance_Charter.md` constitutional declaration of integrity requirements (Declared and Detectable state) and fully Enforceable integrity protections. Without this file, integrity violations may go unclassified, recovery procedures may be improvised inconsistently, and the repository may lose institutional memory of compromise events. This file is the candidate integrity model that `Admin/AUDIT_HARNESS.py` automation will eventually implement — it is written now so the automation has a target to build against.

**Honest v0 acknowledgment:** At current maturity, the primary integrity mechanism is human discipline. Automated detection is the destination. This file defines the provisional procedures a human operator or auditor executes manually until automation matures. Procedures written here must therefore be executable without tooling.

---

## Assumptions

| ID      | Assumption                                                                      | Basis                            | Confidence | Expiry Trigger                                         |
|---------|---------------------------------------------------------------------------------|----------------------------------|------------|--------------------------------------------------------|
| ASM-001 | Version preservation is currently a human discipline, not an automated guarantee | Observed repository workflow     | High       | Automated version control enforced at repository level |
| ASM-002 | Most integrity violations at v0 will be accidental rather than adversarial       | Current contributor profile      | Medium     | Adversarial actors confirmed in operational environment |
| ASM-003 | Human auditors are the primary detection layer at v0                            | Absence of automated tooling     | High       | `Admin/AUDIT_HARNESS.py` implements automated baseline checks |
| ASM-004 | Prior file states may not always be available for comparison                    | Observed version preservation gaps | High     | Systematic prior-state archival established            |
| ASM-005 | Multi-agent workflows create specific integrity risks around omission of prior agent contributions | Observed provisional document workflow | High | Single-agent workflow formally adopted |

---

## The v0 Integrity Reality

Before defining procedures, this section names the actual integrity gap honestly.

The repository currently operates with:
- **No automated version comparison** — a human must read prior and current versions to detect changes
- **No cryptographic integrity verification** — file hashes are not computed or stored
- **No append-only log enforcement** — Resolution Logs can be edited after the fact without detection
- **Inconsistent prior-state preservation** — most revisions override originals; provisional documents are an exception

This means the current integrity layer is:
- **Detectable** — a careful human auditor reading two versions can identify most violations
- **Reviewable** — violations that are detected can be logged and traced
- **Not enforceable** — no mechanism prevents violations from occurring

This is not a failure of the governance architecture. It is an honest assessment of v0 maturity. The procedures below are designed to work within this reality while creating the specification that automation will eventually fulfill.

The most important v0 integrity practice is therefore: **preserve prior states before revision.**

---

## Version Preservation Protocol

This section defines the human workflow required before any revision to a governance-bearing document.

### Before Revising Any Governance Document

1. **Save the current version** with a dated filename suffix before opening for edit.
   - Format: `[Filename]_YYYYMMDD_[version].md`
   - Example: `Governance_Charter_20260523_v03.md`
   - Location: a designated `/Archive/` directory or equivalent local folder

2. **Record the prior state hash** if tooling is available. If not, record the final line count and open unknowns count as a lightweight integrity anchor.

3. **Note the last audit entry** from the Resolution Log — this is the comparison baseline for the new revision.

4. **In multi-agent workflows:** open each session by explicitly loading prior agent contributions. State: *"Prior contributions assumed: [list]. Carried forward unless contradicted."* This is Rule 6 of the AI Contribution Protocols — it directly addresses the omission risk that provisional documents exposed.

### After Revising Any Governance Document

1. **Add a Resolution Log entry** for every substantive change. Not for typo corrections — for changes to doctrine, scope, unknowns, or structure.

2. **Update the File State table** — Last Audit date, Auditor, Open Unknowns count.

3. **Verify Ethical Anchor field** is intact and matches canonical string exactly.

4. **Verify cross-references** against `Discovery.md` Rename Registry — do not carry forward stale flat filenames.

5. **Archive the prior version** if not already done in step 1 above.

---

## Protected Elements and Integrity Baselines

For each protected element, this section defines what "intact" looks like in a checkable way.

### Tier 1 Axioms

**Baseline:** Axiom text in `Admin/Governance_Charter.md` matches the text present at the time of last human ratification.

**Intact condition:** All eight axioms (P-1 through P-4, Q-1 through Q-4) present, text verbatim from ratified version, Protections/Prohibitions clause structure preserved.

**Detection method:** Read current axiom text against archived prior version. Any wording change that was not accompanied by a Resolution Log entry with human ratification note is a violation.

**Violation class:** Constitutional.

---

### Resolution Logs

**Baseline:** Resolution Logs are append-only. Entries are not deleted, reworded after the fact, or backdated.

**Intact condition:** Entry count equals or exceeds prior version count. Dates are sequential. No prior entries modified.

**Detection method:** Compare entry count between current and archived version. Read entries for date sequencing. Flag any entry present in prior version that is absent or modified in current version.

**Violation class:** Major (accidental omission) or Constitutional (deliberate erasure).

**v0 note:** Because prior states are not always preserved, this check can only be performed when an archived version exists. This is the primary argument for systematic prior-state archival.

---

### Frozen Sections

**Baseline:** Sections marked `<!-- FROZEN: Gate N — YYYY-MM-DD -->` are not modified without a dated justification comment and gate status reset.

**Intact condition:** FROZEN marker present at correct scope. Content beneath marker matches prior version or contains a dated justification comment explaining the change. Affected gate status has been reset in File State table.

**Detection method:** Locate all FROZEN markers. Compare content beneath each marker to archived version. Flag any change without dated justification comment.

**Violation class:** Major.

---

### Canonical Cross-References

**Baseline:** All file references use canonical folder-prefixed paths that resolve against `Discovery.md` Rename Registry.

**Intact condition:** No flat legacy filenames present in new contributions. All referenced files exist in `Discovery.md` confirmed list or are explicitly labeled *planned*.

**Detection method:** Scan document for file references. Check each against `Discovery.md` Rename Registry. Flag unresolved references and unlabeled aspirational references.

**Violation class:** Minor (stale reference) or Major (hallucinated file presented as confirmed).

---

### Navigation File Integrity

**Baseline:** `Discovery.md` and `Routing.md` are protected elements. If either is compromised, all downstream path validation and canonical cross-reference checks silently pass invalid targets.

**Intact condition:** `Discovery.md` file map and Rename Registry entries resolve against the actual folder-prefixed repository structure. `Routing.md` URL entries resolve to real files. Neither file's path mappings have been altered without a corresponding Resolution Log entry.

**Detection method:** Spot-check a sample of `Discovery.md` path entries against actual repository structure at each audit opening. Before any Phase 1 automated run, cross-match `Discovery.md` and `Routing.md` entries against the hardcoded folder-prefixed layout defined in `Admin/Repository_Structure.md`.

**Violation class:** Major (unintentional mapping error) or Constitutional (deliberate mapping to malicious or empty target).

**v0 note:** Manual spot-check is the only detection method until Phase 1 automation is implemented. `Discovery.md` and `Routing.md` must be treated as high-value targets — they are the keystone of all path-based integrity checks.

---

### Audit Lineage

**Baseline:** Every version increment has a dated Audit Trail entry in `Unknowns.md` and a Resolution Log entry in the revised file.

**Intact condition:** Version header in `Unknowns.md` updated. "What vX.X Means" section present for current version. File Resolution Log contains entry for current revision cycle.

**Detection method:** Check `Unknowns.md` version header against most recently revised file versions. Verify "What vX.X Means" section exists for current version. Verify Resolution Log entry exists in revised file.

**Violation class:** Minor (missing entry) or Major (version increment with no audit trail).

---

### Ethical Anchor Field

**Baseline:** Every file's Ethical Anchor field contains the canonical string exactly.

**Intact condition:** Field present in File State table. Value matches: `Attempt to do no harm. Defer to Ethical_Constraints.md if present.` exactly — no abbreviation, paraphrase, or blank.

**Detection method:** Read File State table. String comparison against canonical value.

**Violation class:** Major (accidental alteration) or Constitutional (deliberate removal).

---

### Sidecar Unknown Entries

**Baseline:** Unknown entries are not deleted from sidecars — only moved to Resolution Log with discharge note.

**Intact condition:** Open entry count in File State table matches count of open entries in sidecar. No entry present in archived version is absent from current version without a corresponding Resolution Log discharge entry.

**Detection method:** Count open sidecar entries. Compare to File State open unknowns count. Compare to archived version entry list.

**Violation class:** Minor (count mismatch without deletion) or Major (entry deleted without resolution record).

---

### Multi-Agent Contribution Continuity

**Baseline:** In multi-agent workflows, each agent's contributions are carried forward unless explicitly contradicted with documented rationale.

**Intact condition:** Each agent session opens with Assumption Extraction per AI Contribution Rule 6. Prior agent work is not silently omitted. Contradictions are logged, not erased.

**Detection method:** Read session opening for Assumption Extraction statement. Compare current document against prior agent's output — flag material omissions without contradiction rationale.

**Violation class:** Major (silent omission) or Constitutional (deliberate erasure of prior agent's governance findings).

---

## Violation Classification and Response Ladder

### Minor Violation

**Examples:** Stale cross-reference, count mismatch in File State table, missing version suffix in archive filename, unlabeled aspirational reference.

**Response:**
1. Log the violation in the affected file's sidecar as a new unknown or note on an existing unknown
2. Remediate at the current or next audit cycle — does not block promotion
3. No escalation required unless Minor violations accumulate across three consecutive audits (triggers Compound Drift escalation)

---

### Major Violation

**Examples:** Frozen section modified without justification comment, Resolution Log entry deleted, unknown entry removed without discharge record, silent omission of prior agent contributions, version increment without audit trail entry, navigation file mapping error.

**Response:**
1. Halt Specification promotion for the affected file
2. Log the violation as a High-risk unknown in the affected file's sidecar
3. Restore prior state from archive if available — document restoration in Resolution Log
4. If prior state unavailable, reconstruct from context and log reconstruction as Analogous evidence — reconstructed content cannot clear Gate 6 or advance beyond Exploration until independently verified by a second agent or human operator performing line-by-line confirmation against external raw logs
5. Re-audit the affected file before promotion resumes
6. Notify human operator if autonomous agent is responsible

---

### Constitutional Violation

**Examples:** Tier 1 Axiom text modified without human ratification, Ethical Anchor field deliberately removed, Resolution Log deliberately erased, autonomous agent initiates axiom amendment, STATE_HOLD bypassed, `Discovery.md` or `Routing.md` deliberately mapped to malicious or empty target.

**Response:**
1. **Immediate STATE_HOLD** — halt all autonomous governance actions repository-wide
2. Human review is mandatory before any autonomous action resumes
3. Restore prior state from archive — this is the primary argument for systematic archival
4. Log full incident record in `Unknowns.md` under a new Cross-Module entry
5. Conduct Full Stop Review per `Admin/Auditor_Protocols.md` before resuming promotion activity
6. If axiom text was altered: human ratification required to confirm restored text or formally amend
7. Document incident in Lessons Learned with Evidence Type, Confidence, and Revalidation Required fields

**Constitutional violations are never self-remediated by autonomous agents.** The response is always human-in-the-loop regardless of operational cost.

---

## Recovery Procedures

### When a Prior State is Available

1. Load the archived version
2. Identify the specific divergence — do not assume the current version is entirely compromised
3. Restore only the compromised elements where possible — surgical restoration is preferable to full rollback
4. Document each restored element in the Resolution Log with:
   - Date of restoration
   - What was restored and from which archived version
   - How the violation was detected
   - Classification (Minor / Major / Constitutional)
5. Increment the version and add an Audit Trail entry in `Unknowns.md`
6. Re-audit the restored file before re-entering promotion flow

### When a Prior State is Not Available

This is the highest-risk recovery scenario and the primary reason systematic archival matters.

1. Reconstruct the compromised element from context — prior session transcripts, other files that reference the missing content, memory of what was decided
2. Label all reconstructed content explicitly: `(Reconstructed — Analogous evidence — YYYY-MM-DD)`
3. Open a new sidecar unknown for each reconstructed element: Status Open, Risk High, Type Governance, Blocking dependent on element
4. Reconstructed content cannot clear Gate 6 (Conflict check) or advance beyond Exploration status until a second independent agent or human operator performs line-by-line verification against external raw logs — reconstruction without an objective delta check introduces hallucination and drift risk
5. Log the reconstruction event in Lessons Learned — this is institutional memory that must survive

### Preventing the "No Prior State" Scenario

The version preservation protocol above is the prevention. But given that current patterns override rather than archive, here are the minimum viable practices at v0:

**Before any revision session:**
- Copy the current file to a dated archive filename
- Takes thirty seconds — prevents the highest-risk recovery scenario entirely

**In multi-agent sessions:**
- Treat each agent's output as an intermediate archived state
- Do not discard intermediate outputs until the final version is confirmed complete

**Systematic practice to build toward:**
- A `/Archive/` directory with dated versions of all governance files
- Referenced in `Discovery.md` so agents know it exists
- Checked at audit opening for completeness

---

## Automation Migration Path

This section defines what automated integrity checking will eventually implement, written now so `Admin/AUDIT_HARNESS.py` has a specification target.

### Phase 1 — Structural Checks (near-term)

Automatable without cryptographic tooling:
- File State table field presence and Ethical Anchor string match
- Sidecar entry count vs. File State open unknowns count
- Cross-reference resolution against `Discovery.md` confirmed file list
- FROZEN marker presence and scope validation
- Version header presence in `Unknowns.md`
- Navigation file spot-check: sample of `Discovery.md` / `Routing.md` path entries against hardcoded folder-prefixed layout in `Admin/Repository_Structure.md`

### Phase 2 — Comparison Checks (requires archived prior states)

Automatable once systematic archival is established:
- Resolution Log entry count comparison between versions
- Axiom text verbatim comparison against ratified version
- Sidecar entry presence comparison (detect deletions)
- Frozen section content comparison (detect unauthorized changes)

### Phase 3 — Cryptographic Verification (requires `Admin/Security_Protocols.md`)

Requires implementation defined in `Admin/Security_Protocols.md`:
- File hash comparison against stored baseline
- Commit signature verification
- Authority authentication for human override claims
- Append-only log enforcement

**Rule:** Each phase is a prerequisite for the next. Phase 2 cannot be claimed without systematic archival. Phase 3 cannot be claimed without `Admin/Security_Protocols.md` implementation at sufficient maturity. Governance Enforcement State must not advance beyond actual capability.

---

## Integrity and the Multi-Agent Problem

The multi-agent workflow creates a specific integrity risk that deserves explicit treatment: **contribution omission**.

When Agent B produces a revision of a file previously worked on by Agent A, Agent B may silently omit Agent A's findings — not through malice but through context loss, differing interpretation, or optimization pressure toward a cleaner output.

The provisional document workflow revealed this risk clearly. The governance response is already embedded in `Admin/Auditor_Protocols.md` Rule 6 (Inter-Agent Consistency) — but this file names the integrity dimension explicitly:

**Silent omission of prior agent contributions is a Major integrity violation.**

It is distinguishable from legitimate contradiction (which is permitted and must be documented) by the absence of a rationale. If Agent B changes something Agent A wrote, the change must be logged. If Agent B removes something Agent A wrote, the removal must be logged with rationale. If neither occurs, the omission is detectable as a drift indicator and classifiable as a Major violation.

This applies equally to human contributors revising AI-generated content and AI agents revising human-generated content.

---

## Relationship to Governance Enforcement States

This file advances the repository toward Enforceable integrity for the elements it covers.

| Protected Element          | Prior State  | State with This File | Path to Enforceable          |
|----------------------------|--------------|----------------------|-------------------------------|
| Tier 1 Axiom text          | Detectable   | Reviewable           | Phase 2 automation            |
| Resolution Logs            | Detectable   | Reviewable           | Phase 2 automation            |
| Frozen sections            | Detectable   | Reviewable           | Phase 1 automation            |
| Canonical cross-references | Detectable   | Reviewable           | Phase 1 automation            |
| Navigation files           | Detectable   | Reviewable           | Phase 1 automation            |
| Audit lineage              | Detectable   | Reviewable           | Phase 1 automation            |
| Ethical Anchor field       | Detectable   | Reviewable           | Phase 1 automation (near-term)|
| Sidecar entries            | Detectable   | Reviewable           | Phase 2 automation            |
| Multi-agent continuity     | Detectable   | Reviewable           | Partially procedural — human discipline at v0 |

Full Enforceability requires `Admin/Security_Protocols.md` Phase 3. This file closes the gap between Detectable and Reviewable for all covered elements.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                          | What Failed                                                        | What Was Learned                                                                                 | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-23 | Audit Review  | Revision overriding original without archival           | Prior state unavailable for comparison; drift undetectable         | Version preservation before revision is the single highest-value v0 integrity practice           | Replicated | No                  |
| 2026-05-23 | Audit Review  | Multi-agent sessions without explicit prior-state loading | Prior agent contributions silently omitted in subsequent sessions | Assumption Extraction at session open (Rule 6) is an integrity requirement, not a courtesy      | Replicated | No                  |
| 2026-05-23 | Modeling      | Treating all integrity violations as equal severity     | Response procedures were inconsistent; Constitutional violations handled like Minor ones         | Violation classification ladder required — response must be proportional to severity and reversibility | Analogous | Yes            |
| 2026-06-19 | Audit Review  | Recovery via reconstruction without independent verification gate | Reconstructed content carries hallucination and drift risk; anchoring it without delta check embeds errors | Reconstructed files cannot clear Gate 6 or advance beyond Exploration until independently verified against external raw logs | Analogous | Yes |
| 2026-06-19 | Audit Review  | Navigation files (Discovery.md, Routing.md) treated as ordinary files | If path mappings are compromised, all downstream Phase 1 checks silently validate invalid targets | Discovery.md and Routing.md are keystone integrity targets — must be explicitly protected and spot-checked before automated runs | Internally Derived | Yes |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                              | Why Abandoned                                                                                       | Reconsider? |
|------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-23 | Cryptographic enforcement as v0 integrity mechanism               | Requires `Admin/Security_Protocols.md` implementation — claiming it would be integrity theater      | Yes — at Phase 3 |
| 2026-05-23 | Full rollback as default recovery procedure                       | Surgical restoration of specific compromised elements is preferable — full rollback discards valid work unnecessarily | No |
| 2026-05-23 | Treating multi-agent omission as always accidental                | Omission without rationale is a violation regardless of intent — intent affects severity classification, not violation status | No |
| 2026-06-19 | Unrestricted reconstruction as valid recovery path               | Reconstruction without independent verification anchors hallucinated content into repository as if it were restored fact | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Violation classification ladder modified to reduce Constitutional violation response requirements
- STATE_HOLD trigger removed or made conditional
- Human-in-the-loop requirement for Constitutional violations weakened
- Phase automation claims advance beyond actual implemented capability
- Recovery procedure for "no prior state" scenario removes independent verification requirement for reconstructed content
- Multi-agent omission violation status downgraded from Major
- Version preservation protocol removed or made optional
- Enforcement State table claims stronger capability than currently exists
- Navigation file integrity section removed or downgraded from protected element status
- `Discovery.md` / `Routing.md` spot-check removed from Phase 1 automation target list
- Ethical Anchor field absent, altered, or does not match canonical string
- Abandoned path for cryptographic enforcement reopened without `Admin/Security_Protocols.md` at sufficient maturity
- RIP-004 reopened — Tier 1 Axiom Verification already implemented in `Admin/Forge_Audit_Kit.md` v1.1 Step 1

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### RIP-001 — Prior-state archival system not yet established

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | High                                    |
| Priority      | Critical                                |
| Type          | Governance / Operational                |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** No systematic `/Archive/` directory or equivalent prior-state preservation mechanism exists in the repository.

**Why It Matters:** Without archived prior states, Constitutional and Major violation recovery defaults to reconstruction from context — the highest-risk recovery path. Reconstructed content cannot clear Gate 6 without independent verification. The "no prior state" scenario is the primary integrity gap at v0.

**Resolution Path:** Deferred via Specification — establish `/Archive/` directory, add to `Discovery.md`, define naming convention and retention policy (see RIP-006 for retention policy tracking). This is a human workflow change, not a tooling dependency.

---

### RIP-002 — AUDIT_HARNESS.py Phase 1 checks not yet implemented

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Technical / Governance                  |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-05-23                              |

**Description:** Phase 1 automation checks (Ethical Anchor string match, File State field presence, cross-reference resolution, FROZEN marker validation, navigation file spot-check) are defined here but not yet implemented in `Admin/AUDIT_HARNESS.py`.

**Why It Matters:** Phase 1 checks are the most tractable automation target — no cryptographic tooling required. Delay means these remain human-only checks subject to fatigue and omission.

**Resolution Path:** Deferred via Specification — implement Phase 1 checks in `Admin/AUDIT_HARNESS.py`. This file is the specification. Checks are ordered by implementation tractability: Ethical Anchor match first, then File State fields, then cross-reference resolution, then navigation file spot-check.

---

### RIP-003 — Violation incident log location undefined

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Governance                              |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** Constitutional violations require a Cross-Module entry in `Unknowns.md`, but no dedicated integrity incident log exists and no incident ownership chain is defined (who closes incidents — human operator, auditor, or constitutional authority). Multiple Constitutional violations would accumulate as cross-module unknowns without a dedicated tracking structure.

**Why It Matters:** Integrity incident history is institutional memory — it must be queryable and distinct from standard unknowns to be useful for pattern detection. Undefined ownership means incidents may linger unresolved. See RIP-007 for incident ownership tracking.

**Resolution Path:** Deferred via Specification — define whether a dedicated `Integrity_Incident_Log.md` is warranted or whether `Unknowns.md` cross-module section is sufficient at v0 volume. Defer to Lessons Learned if incident volume remains low. Resolve RIP-007 concurrently.

---

### RIP-004 — Constitutional violation detection latency

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Resolved                                |
| Risk          | High                                    |
| Priority      | Major                                   |
| Type          | Governance / Security                   |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** No maximum detection latency was defined for Constitutional violations. A Tier 1 Axiom modification could persist undetected across multiple audit cycles if the axiom text was not explicitly checked at each audit opening.

**Resolution:** Tier 1 Axiom Verification is now Step 1 of the mandatory Audit Opening Checklist in `Admin/Forge_Audit_Kit.md` v1.1. Every audit cycle opens with axiom text confirmation before any other check. Detection latency is bounded to one audit cycle.

*Moved to sidecar resolution status 2026-06-19. Original resolution path (add to Forge_Audit_Kit.md) was executed in v1.1 revision. Archive entry in Unknowns.md to be updated at next sync.*

---

### RIP-005 — Security_Protocols.md Phase 3 dependency

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | In Progress                             |
| Risk          | High                                    |
| Priority      | Major                                   |
| Type          | Governance / Security                   |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-05-23                              |
| Last Reviewed | 2026-06-19                              |

**Description:** Phase 3 integrity enforcement (cryptographic verification, authority authentication, append-only log enforcement) depends on `Admin/Security_Protocols.md` reaching sufficient cryptographic implementation maturity. File exists at v0.5 (2026-06-19) but Phase 3 implementation does not yet exist.

**Why It Matters:** Without Phase 3, the repository cannot reach fully Enforceable integrity state. Human override authenticity (GOV-006) also depends on this file's Phase 3 output.

**Resolution Path:** Deferred via Trajectory — Phase 3 is scoped to a future version when cryptographic tooling is available. `Admin/Security_Protocols.md` v0.5 is the specification input when that work begins. Status updated from Open to In Progress — file now exists and its SEC- unknowns are tracking implementation gaps.

---

### RIP-006 — Archive retention policy undefined

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | Low                                     |
| Priority      | Minor                                   |
| Type          | Governance / Operational                |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-06-19                              |
| Last Reviewed | 2026-06-19                              |

**Description:** RIP-001 resolution path establishes an `/Archive/` directory but does not define how long archived versions must be retained. Questions unanswered: retain forever, N versions, compressed snapshots, or time-bounded window? Archive growth burden and retrieval overhead at scale are not discussed.

**Why It Matters:** Without a retention policy, the archive grows unboundedly. At Leviathan-scale deployment, archive maintenance overhead may itself become a friction point. Conversely, too-short retention means recovery may not find old enough prior states after major incidents.

**Resolution Path:** Define retention policy when `/Archive/` directory is established (RIP-001 resolution event). Minimum viable policy: retain all versions touching Tier 1 constitutional content permanently; retain all other governance files for at minimum three full audit cycles; retain operational files for one audit cycle. Confirm or revise at first archive maintenance review.

---

### RIP-007 — Integrity incident ownership undefined

| Field         | Value                                   |
|---------------|-----------------------------------------|
| Status        | Open                                    |
| Risk          | Medium                                  |
| Priority      | Major                                   |
| Type          | Governance                              |
| Blocking      | No                                      |
| Owner         | `Admin/Repository_Integrity_Protocol.md`|
| First Logged  | 2026-06-19                              |
| Last Reviewed | 2026-06-19                              |

**Description:** No doctrine defines who owns integrity incident resolution. When a Constitutional or Major violation is logged, it is unclear whether closure authority rests with: the human operator, the audit lead, or constitutional authority (human governing party). No escalation path exists for incidents that cannot be resolved at the auditor level.

**Why It Matters:** Unowned incidents persist indefinitely. Pattern detection across incidents is impossible without a defined closure process. For Constitutional violations, the lack of defined ownership creates a gap between STATE_HOLD declaration and human review escalation.

**Resolution Path:** Extend RIP-003 resolution or define independently. Minimum doctrine: Minor violations closed by the auditor who logged them; Major violations require human operator confirmation; Constitutional violations require human governing party ratification to close. Cross-reference `Admin/Governance_Charter.md` §Escalation Doctrine for severity calibration.

---

### Resolution Log

- 2026-05-23: File created (v0.1) — GOV-003 resolution path initiated. Bridges `Admin/Governance_Charter.md` constitutional declarations and `Admin/Auditor_Protocols.md` operational detection behavior. Defines integrity baselines, violation classification ladder, recovery procedures, and automation migration path. Honest v0 acknowledgment of human-discipline-primary integrity layer. RIP-001 through RIP-005 logged.
- 2026-06-19: v0.2 — Four-agent audit pass (Gemini, ChatGPT, Grok, Claude). Ten changes: (1) Navigation Anchors added. (2) Verification Ref corrected to `Admin/Verification_Gates_LF.md` (PC-001 class fix). (3) Navigation File Integrity section added to Protected Elements — Discovery.md and Routing.md declared as keystone protected elements; spot-check before automated runs; Constitutional violation class for deliberate mapping attacks. (4) Navigation file protection added to Phase 1 automation target list. (5) Navigation files row added to Governance Enforcement States table. (6) Reconstruction recovery rule tightened — reconstructed content cannot clear Gate 6 or advance beyond Exploration without independent line-by-line verification against external raw logs. (7) Abandoned path added for unrestricted reconstruction. (8) RIP-004 resolved — Tier 1 Axiom Verification already implemented in Forge_Audit_Kit.md v1.1 Step 1; moved to Resolved in sidecar; Drift Indicator added to prevent reopening. (9) RIP-005 description updated — file now exists at v0.5; status In Progress. (10) RIP-006 logged — archive retention policy undefined. (11) RIP-007 logged — integrity incident ownership undefined. (12) Stale "planned" labels stripped from Relationship section for Security_Protocols.md and Governance_Migration_Protocol.md. (13) Scope Boundary updated to note RIP-006 and RIP-007 as deferred items. (14) Two new Lessons Learned entries added. Open Unknowns updated to 7 (RIP-004 resolved, RIP-006 and RIP-007 added).

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; declares integrity requirements this file operationalizes; GOV-003 is the originating unknown
- `Admin/Auditor_Protocols.md` — Tier 2; auditor detection behavior; Adversarial Challenge Classes 6, 9, and 10 are the primary detection mechanisms this file coordinates with
- `Admin/Forge_Audit_Kit.md` — Tier 3; RIP-004 resolved — Tier 1 Axiom Verification now Step 1 of mandatory Audit Opening Checklist in v1.1
- `Admin/Ethical_Constraints.md` — co-Tier 1; Ethical Anchor field integrity is governed by doctrine here
- `Admin/File_Template.md` — defines Ethical Anchor field canonical string and Frozen Section marker format
- `Unknowns.md` — Constitutional violation incidents logged as Cross-Module entries here; RIP-004 archive entry to be updated at next sync
- `Discovery.md` — canonical cross-reference resolution source; Archive directory to be added here when established; now also a protected element
- `Routing.md` — programmatic path routing; now a protected element alongside Discovery.md
- `Admin/Repository_Structure.md` — hardcoded folder-prefixed layout used as Navigation file spot-check baseline in Phase 1
- `Admin/AUDIT_HARNESS.py` — primary automation target for Phase 1 and Phase 2 checks defined here
- `Admin/Security_Protocols.md` — exists at v0.5 (2026-06-19); Phase 3 cryptographic enforcement dependency; SEC- unknowns track implementation gaps
- `Admin/Governance_Migration_Protocol.md` — exists; Tier 1 Axiom amendment procedures cross-reference

---

## Status

Version 0.2 — Four-agent audit pass (2026-06-19).

**What must remain constant:**

**A governance system that cannot verify its own state cannot protect anything else.**

**Prior state preservation is not optional at v0 — it is the integrity layer.**

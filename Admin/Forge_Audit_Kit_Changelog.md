# Forge_Audit_Kit.md — Version History

Full changelog for `Admin/Forge_Audit_Kit.md`, relocated out of the
kit's own body as of v1.10 (2026-07-14). Newest entries first. Add new
entries here, not back into the kit.

────────────────────────────────────────────────────────────────────

- 2026-07-14: **v1.10 — Expiry Watch redesign (human-directed) + reduction
  pass + staleness correction.** Three changes, prompted by a Grok audit
  of `Governance_Charter.md` this session that inherited a stale DOC_STATUS
  assumption rather than checking the file's own File State table.

  *Expiry Watch redesign:* the "current critical watch" list (Audit
  Opening Checklist step 3) — a hand-curated duplicate of `Unknowns.md`'s
  Critical/Blocking table, refreshed piecemeal since v1.1 and the subject
  of FAK-004 (never formally ratified) and FAK-007 (went stale twice) —
  removed entirely. Rationale, human-directed: pre-loading an auditor with
  expected findings before it reads the target file undermines independent
  verification (EF-0.1 disqualifies precedent and consensus as evidence),
  and adds mental load pointed away from the file under audit. Expiry
  Watch is now file-scoped only — the target file's own sidecar, or the
  `AUDIT_HARNESS.py` boundary index if present. `Unknowns.md` registry
  cross-referencing moved to a new Post-Audit Cross-Reference section,
  performed only after independent findings are drafted from the file
  alone. FAK-004 and FAK-007 resolved as a consequence — the mechanism
  that could go stale no longer exists in the kit.

  *Reduction pass:* Resolution Log (this file's history, ~7,650 chars)
  externalized to `Admin/Forge_Audit_Kit_Changelog.md` — full history
  preserved verbatim below, add new entries there going forward, not back
  into the kit. Auditor Notes FAK-* entries trimmed to Status/Resolution/
  Lessons Learned per this kit's own Resolved Unknown Discharge Procedure
  (previously full incident narrative inline, much of it duplicating this
  Resolution Log's own entries for the same incidents — EF-0.5 applies to
  this kit same as any other document). Verification Gates section's
  process-note paragraph (2026-07-02 citation-routing incident, already
  covered by FAK-009 and the v1.6 entry below) removed from the kit,
  preserved here. FAK-005 updated with final character counts.

  *Staleness correction:* Truth Provenance Labels still listed the
  four-label system (Measured/Estimated/Analogous/Placeholder) retired by
  AP-021 on 2026-07-10 — corrected to the ratified five-label system
  (Measured/Replicated/Simulated/Analogous/Placeholder) with evidentiary
  thresholds. Verification Gates section gained a G2 evidentiary-backing
  note it had been missing since VG-002 activated the same day. Derived-
  from line corrected: `Auditor_Protocols.md` v0.18 → v0.20,
  `Verification_Gates_LF.md` v0.4 → v0.7, `Unknowns.md` v4.10 → v4.20 —
  all three had drifted since this kit's 2026-07-05 Last Audit. A full
  content re-sync against everything that changed across those version
  gaps was not attempted this pass — flagged as separate follow-up work,
  not assumed complete.

────────────────────────────────────────────────────────────────────

- 2026-07-05: **v1.9 — FAK-007 Resolved: full critical watch refresh.**
  Derivation string corrected `Unknowns.md` v4.9 → v4.10 (a second
  staleness had accumulated since the 2026-07-02 fix) and
  `Admin/Auditor_Protocols.md` v0.16 → v0.18. Critical watch summary (Audit
  Opening Checklist step 3) rebuilt from live `Unknowns.md` v4.10 data
  rather than patched — added explicit note that this is a curated
  highlight, not the exhaustive Critical list, and pointed to
  `Unknowns.md`'s own cross-reference table for completeness rather than
  attempting to duplicate ~35 Critical entries here (consistent with
  FAK-005's character-ceiling constraint). GOV-011's 2026-07-05 resolution
  reflected, with an explicit flag that `Unknowns.md`'s own global index
  has not yet been updated to match — that sync is separate outstanding
  work. Surfaced and flagged inline, rather than silently perpetuated: the
  `EC-002` reference in the prior critical watch summary was ambiguous
  without a file qualifier — confirmed as an actual, already-occurred `EC-`
  prefix collision between `Ethical_Constraints.md` and `Economics.md`
  (five colliding IDs total), escalated as CT-007 in
  `Admin/Canonical_Terms.md` rather than resolved here (this file doesn't
  own that fix). Expiry Watch step text now cross-references
  `Admin/Canonical_Terms.md` §4's Cycle definition per CT-011, distinguishing
  audit pass from calendar cycle. New Drift Indicator added for
  cycle-vs-pass conflation.

- 2026-06-21: **v1.2** — Derivation string updated to `Admin/Auditor_Protocols.md` v0.8.1. Epistemic Foundation condensed reference added. Audit Opening Checklist restructured. AP-001–AP-007 Systemic Risk escalation added. Physical harness gate note added. Rule 8 added to AI Contribution Rules. Token ceiling note added.
- 2026-06-24: **v1.3** — Derivation strings updated to `Admin/Auditor_Protocols.md` v0.14 and `Unknowns.md` v4.0. Role declaration version string updated to v0.14. Human Interaction Point Doctrine added to Governing Principles. EF-0.2 L2 entry updated to reflect autonomous degradation doctrine. Active Unknowns section removed — replaced by critical watch summary integrated into Expiry Watch step. AP Systemic Risk escalation note updated: all seven entries carry resolution frameworks; AP-006 and AP-009 Resolved; AP-012 and AP-016 Critical. GH- prefix added to Governance Sidecar ID Reference. Operational Blocking / Epistemic Blocking added to Semantic Stability table. Gate 3 note updated with AP-017 independence requirement and current block status. AP-010 physical harness note updated. Token ceiling note updated to reflect v0.14 character count. FAK-005 remains Open — actual post-reduction count ~16,950; ceiling parameter needs revisiting, not the content. Reduction pass complete.
- 2026-06-27: **v1.3 patch** — Spec Gates (0/6) and Verification Ref (Admin/Verification_Gates_LF.md) added to File State block. Phase 1 enforcement (AUDIT_HARNESS.py v11) flagged missing fields — all repository documents follow the same File State schema, no exceptions for meta documents.
- 2026-07-02: **v1.4** — Resolved Unknown Discharge Procedure section added, canonizing the RIP-001 pattern (permanent sidecar retention, Resolution + Lessons Learned narrative fields, matching top-table row, one-line Unknowns.md pointer — no centralized archive). Placed between Verification Gates and Sign-Off Format. Matching Drift Indicator added. FAK-006 logged — condensed version lives here per Scope Boundary; full doctrine migration to `Admin/Auditor_Protocols.md` still pending (file unavailable this session). Prompted by retroactive correction of RIP-004's discharge record, which had skipped the Lessons Learned narrative field and matching table row for six weeks despite being correctly resolved in substance.
- 2026-07-02: **v1.5** — Gate scope vs. promotion readiness clarification added to Verification Gates, sourced from `Admin/Auditor_Protocols.md` §Specification Promotion Rules and §Adversarial Audit Layer (file made available this session for the first time). Resolves the standing Grok/Gemini G3/G6 disagreement on `Admin/Security_Protocols.md`: gates test a document's own execution quality (check applied and documented, text non-contradictory); "open unknowns are non-blocking" is a separate, independently required promotion condition, not folded into G3 or G6. Flagged a legibility issue in the source: `Admin/Auditor_Protocols.md`'s own Gate 3 status entry blends "battery coverage complete" with "promotion blocked" in one line — correct in substance, ambiguous in phrasing. Gate 3 note rewritten to separate the two explicitly. `Unknowns.md` derivation string corrected from stale v4.0 to v4.5 (three missed maintenance-trigger updates). New Drift Indicator added for gate/promotion-status conflation. FAK-007 logged — critical watch summary still needs a full refresh against v4.0→v4.5 changes, not done this session. FAK-008 logged — dispute resolution recorded as Synthesizer-level, reversible, cross-referenced into `Admin/Security_Protocols.md` Active Disputes per `Admin/Auditor_Protocols.md` §Dispute Handling Protocol.
- 2026-07-02: **v1.6** — `Admin/Verification_Gates_LF.md` reconciliation.
  Derivation line corrected to include it (was citing `Auditor_Protocols.md`
  only, skipping the intermediate canonical layer this kit's gate table is
  actually derived from). Gate scope vs. promotion readiness note's citation
  corrected to route through Verification_Gates_LF.md §Gate 3/§Gate 6/
  §Promotion Requirements Summary; checked against it and confirmed
  independently consistent — no actual divergence, wrong citation path only.
  FAK-009 logged as the first concrete incident evidence for VG-001 (open
  since 2026-05-29, previously hypothetical risk). VG-001 remains Open —
  see Verification_Gates_LF.md Resolution Log for the full record.
- 2026-07-02: **v1.7** — Derivation line was stale within the same session
  that fixed it: v1.6 cited `Verification_Gates_LF.md v0.2` after that file
  had already been bumped to v0.3 in the same pass, and still cited
  `Unknowns.md v4.5` after Unknowns.md had moved to v4.6 then v4.7. Both
  corrected. Caught via a user-initiated live-repo check (Grok retrieval of
  File State fields across five files) following a file-management incident
  (accidental cloning, ~10% truncation of `Auditor_Protocols.md`, five
  duplicate `Unknowns.md` versions consolidated back to one). Check found
  no content loss — `Unknowns.md` confirmed v4.7, this file confirmed v1.6,
  `Security_Protocols.md` Open Unknowns confirmed at 12 (only possible if
  the SEC-007a/b split edit persisted) — but did catch this kit's own
  derivation-citation drift, a same-session recurrence of the exact pattern
  VG-001 and FAK-007 describe. Note: this check verified File State header
  fields only, not full body content (SEC-DS-001, EDL registry, RIP-004
  Lessons Learned fields, Discovery.md Objectives section unconfirmed by
  this pass).
- 2026-07-03: **v1.8** — Derivation line updated (`Auditor_Protocols.md`
  v0.14 → v0.16, `Verification_Gates_LF.md` v0.3 → v0.4, `Unknowns.md`
  v4.7 → v4.9). Gate 3 note corrected: AP-012 and AP-016 Resolved as of
  `Auditor_Protocols.md` v0.16 (2026-07-03, Payment via Specification,
  full multi-agent specification text verified against original blocking
  conditions) — was still citing them as blocking. Critical watch summary
  partially corrected for the same reason (AP-012/AP-016 removed, RIP-001
  and SEC-007 updated to current split/resolved state); full v4.0→v4.9
  refresh still not done, FAK-007 remains open.
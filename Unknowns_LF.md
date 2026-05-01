# Unknowns_LF.md — Cross-Module Unknowns Registry
**Central registry for unknowns that span multiple modules or affect system-wide navigation.**
**Version 0.1 — stub created from first formal audit cycle.**

---

## Purpose

This file captures unresolved questions, gaps, and dependencies that cannot be owned by a single module file. Module-specific unknowns live within their own documents. Unknowns that affect multiple modules, cross-repo dependencies, or the navigation layer itself live here.

Uncertainty is a first-class output. This file is not a junk drawer — it is a tracked frontier.

Format per `Auditor_Protocols.md` Unknowns Registry section.

---

## Entry Format

```
### [ID] — Short title
**What is not yet known:**
**Why it matters:**
**Resolution path:**
**Affected files:**
**Priority:** Blocking | Non-blocking | Exploratory
**Logged in version:** (document version or audit cycle identifier)
**Status:** Open | In Progress | Resolved
```

---

## Registry

---

### [UNK-001] — `Unknowns_LF.md` absence created governance gap
**What is not yet known:** N/A — this file now exists. Logging for audit trail completeness.
**Why it matters:** `Auditor_Protocols.md` references this file as the canonical location for cross-module unknowns. `Discovery.md` also routes cross-file unknowns here. While the file was absent, there was no functioning central registry and no location for unknowns surfaced during multi-agent audit cycles.
**Resolution path:** File created (this document). Add to Discovery.md reading order and file summaries. Add raw GitHub URL to Discovery.md entry.
**Affected files:** `Auditor_Protocols.md`, `Discovery.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** In Progress — file created, Discovery.md update pending

---

### [UNK-002] — Repository topology unclear: `Lazarus-Forge-` vs `Astroid-miner`
**What is not yet known:** Whether `Astroid-miner` is a third repository distinct from `Lazarus-Forge-`, a renamed version of the same repo, or a planned future repo. `Discovery.md` names `Lazarus-Forge-` as the companion doctrine repo. `Auditor_Protocols.md` references `Astroid-miner` as a peer-level cross-repo dependency with shared modules (Air Scrubber Leviathan variant, Spin Chamber zero-G extensions, GECK seed bootstrap logic). These imply different relationship types — hierarchical doctrine vs. peer operational integration — and may represent two distinct external repos that are currently undocumented as such.
**Why it matters:** The Cross-Repo Verification section of `Auditor_Protocols.md` requires bidirectional assumption contracts. Those contracts cannot be written until the repository topology is confirmed. If both repos exist and are distinct, `Discovery.md`'s Cross-Repo Relationship section is incomplete. If one is a renaming of the other, all references need updating.
**Resolution path:** Human confirmation of repo topology. If `Astroid-miner` exists as a separate repository, add its Discovery.md URL to `Discovery.md` Cross-Repo Relationship section and create stub assumption contracts per `Auditor_Protocols.md` format. If it does not yet exist, label it `(planned)` in all references.
**Affected files:** `Discovery.md`, `Auditor_Protocols.md`, `geck_forge_seed.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open — awaiting human clarification

---

### [UNK-003] — Cross-repo assumption contracts not yet documented
**What is not yet known:** Whether bidirectional assumption contracts exist in any form between LazarusForgeV0 and its companion repositories. `Auditor_Protocols.md` defines the requirement and format for these contracts but no contracts have been created or referenced anywhere in the repo.
**Why it matters:** Shared module assumptions (Air Scrubber marine variant, Spin Chamber zero-G, GECK bootstrap logic) currently exist as claims in one repo with no acknowledged counterpart in the other. Changes to shared modules cannot be safely verified without bidirectional documentation. This is a governance gap, not a technical one — the work may be coherent, but it is unverifiable from this side alone.
**Resolution path:** After UNK-002 is resolved and repo topology confirmed, create a stub `Assumption_Contracts.md` or equivalent in both repositories using the format defined in `Auditor_Protocols.md` §Cross-Repo Verification. Minimum viable contract: one entry per shared module naming what this repo assumes the other provides.
**Affected files:** `Auditor_Protocols.md`, `geck_forge_seed.md`, `Air_Scrubber_v0.md`, `Spin_Chamber_v0.md`
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open — blocked on UNK-002

---

### [UNK-004] — Expiry Rule has no enforcement mechanism
**What is not yet known:** What constitutes a "version cycle" for purposes of the Expiry Rule. `Auditor_Protocols.md` defines the rule (Blocking/Non-blocking unknowns unresolved after two version cycles escalate to Systemic Risk) but does not define what a version cycle is, does not require a timestamp or version tag on unknown entries, and does not assign responsibility for triggering the escalation check.
**Why it matters:** Without a definition of version cycle and an assigned enforcer, the Expiry Rule is aspirational. Unknowns can age indefinitely without triggering escalation. The registry becomes a junk drawer in slow motion.
**Resolution path:** Add to `Auditor_Protocols.md` Unknowns Registry section: (1) definition of version cycle — recommended: any commit that increments a module version number, or any completed multi-agent audit cycle; (2) "logged in version" as a required field in the unknown entry format (already included in this registry's format); (3) assignment of Expiry check to the Skeptic/Auditor role at the opening of each audit cycle.
**Affected files:** `Auditor_Protocols.md`, this file
**Priority:** Non-blocking
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

### [UNK-005] — Marine G.E.C.K. seed variant not yet defined
**What is not yet known:** The minimum viable seed configuration for instantiating a Support Raft or marine Forge deployment from minimal resources. `Support_Raft_v0.md` flags this as an Exploratory Unknown and routes it to `geck_forge_seed.md`. `geck_forge_seed.md` does not yet contain a marine variant or acknowledge the routing.
**Why it matters:** The terrestrial G.E.C.K. modules (power, triage, fabrication, thermal, etc.) do not map cleanly to a marine deployment context. Hull bootstrap, corrosion-resistant materials, induction charging infrastructure, and sacrificial shell system components require different minimum viable configurations. Without a marine variant, Leviathan and Support Raft deployments have no defined seed — they can grow but cannot be instantiated from scratch.
**Resolution path:** Add a marine variant section to `geck_forge_seed.md` drawing from `Support_Raft_v0.md` Unknowns Registry (galvanic corrosion, sacrificial shell material, induction pad design). This is Exploratory at v0 — a stub acknowledging the gap and listing the open questions is sufficient. Full spec routes to `Trajectories_LF.md` as a v1/v2 milestone.
**Affected files:** `geck_forge_seed.md`, `Support_Raft_v0.md`, `leviathan_testing.md`
**Priority:** Exploratory
**Logged in version:** Discovery.md v1.0 audit cycle, May 2026
**Status:** Open

---

## Expiry Watch

The following unknowns are approaching or past two version cycles without a documented resolution path. Review at next audit cycle.

*(None at v0.1 — all entries are new this cycle.)*

---

## Resolved Unknowns Archive

*(Empty at v0.1)*

---

## Audit Trail

**v0.1 — May 2026**
Created from findings of first formal Skeptic/Auditor cycle over `Discovery.md` and `Auditor_Protocols.md`.
Auditor: Claude (Sonnet 4.6), Skeptic/Auditor role per `Auditor_Protocols.md` v0.3.
Five unknowns logged: UNK-001 through UNK-005.
UNK-001 partially resolved by creation of this file.
UNK-003 blocked on UNK-002 resolution.
Verified under Auditor_Protocols v0.3 — stub creation satisfies Gate 5 Cross-Reference Integrity requirement for `Unknowns_LF.md` pending Discovery.md update.

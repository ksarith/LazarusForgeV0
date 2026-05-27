# Security_Protocols.md — Cryptographic Trust & Multi-Agent Node Security

> ⚠️ **Operational Safety Advisory**
> Physical security and digital authority are tightly coupled within the Forge.
> A compromise of cryptographic key material or human override tokens can bypass
> downstream safeguards, enabling malicious rewriting of operational files or
> unauthorized activation of high-energy machinery. Key infrastructure must be
> decoupled from standard runtime environments. Never store root cryptographic
> seed material in a standard agent-accessible workspace or online repository node.
> When in doubt about key material integrity, treat the affected authority chain
> as compromised and escalate to human review before proceeding.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                            |
| Last Audit       | 2026-05-27                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cryptographic mechanisms for multi-signature Human Override Verification
- Automated code-signing protocols for file integrity verification (RIP Phase 3)
- Node identity verification and key rotation cycles within the cluster environment
- Minimum token complexity, air-gapping requirements, and cryptographic fallback
  behaviors during network division
- Trust boundary declaration: the relationship between cryptographic enforcement
  and governance legitimacy
- Incident logging requirements for authentication events

**This file DOES NOT define:**
- Component-level infiltration prevention for salvaged hardware — governed by
  `Operations/Electronics.md`; this file references that doctrine and sits above
  it in the administrative authority layer
- Specific operating system firewall commands or network router firmware rules
- Local facility access control (locks, badges, physical perimeter barriers)
- Constitutional governance doctrine — governed by `Admin/Governance_Charter.md`
- Auditor operational behavior — governed by `Admin/Auditor_Protocols.md`
- Minimum agent quorum definition for bootstrap compliance — governed by
  GOV-008 in `Admin/Governance_Charter.md`; quorum threshold is a prerequisite
  input to the multi-signature requirements defined here

---

## File Purpose

This document establishes the technical security implementation rules for
validating administrative authority, ensuring the integrity of the active
knowledge graph, and managing multi-node validation in untrusted, degraded,
or adversarial deployment environments. It bridges the gap between the
constitutional governance declarations in `Admin/Governance_Charter.md` and
the operational integrity procedures in `Admin/Repository_Integrity_Protocol.md`
by defining the cryptographic enforcement layer that makes integrity protections
mechanically verifiable rather than procedurally dependent.

This file is the Phase 3 resolution target for `Admin/Repository_Integrity_Protocol.md`
(RIP-005) and the authentication mechanism resolution target for
`Admin/Governance_Charter.md` (GOV-006). It does not supersede either document —
it implements the enforcement capability they declare as necessary.

**Honest v0 acknowledgment:** At current maturity, cryptographic enforcement
is defined here as a specification target, not an operational reality. Phase 3
automation does not yet exist. This file defines what must be built so that
implementation has a governed target to build against.

---

## Assumptions

| ID          | Assumption                                                                       | Basis                          | Confidence | Expiry Trigger                                              |
|-------------|----------------------------------------------------------------------------------|--------------------------------|------------|-------------------------------------------------------------|
| SEC-ASM-001 | Human operators have secure local means to preserve physical tokens              | Standard security practice     | Medium     | Compromise confirmed in operational environment             |
| SEC-ASM-002 | Cryptographic standard libraries (Ed25519/SHA-256) remain robust                 | Current cryptographic consensus| Medium     | Algorithmic vulnerability published against these standards |
| SEC-ASM-003 | GOV-008 minimum quorum definition will precede Phase 3 implementation            | Dependency ordering            | Medium     | Phase 3 implementation proceeds without quorum definition   |
| SEC-ASM-004 | Electronics.md firmware trust doctrine remains the authoritative component layer | Scope boundary discipline      | High       | Electronics.md scope boundary revised to exclude firmware   |

---

## Trust Boundary Declaration

**This principle governs all sections of this document and must be read first.**

Cryptographic verification confirms identity and integrity. It does not confer
governance legitimacy.

A valid signature proves that a file was signed by a known key, and that the
file has not been altered since signing. It does not prove that the action
authorized by that signature was constitutionally permitted, ethically sound,
or within the scope of the signing authority.

Authorization flows from Tier 1 downward through the governance hierarchy
defined in `Admin/Governance_Charter.md`. No cryptographic mechanism substitutes
for that hierarchy. A signed instruction to override a Tier 1 Axiom is a
Constitutional violation regardless of the validity of the signature.

**The correct ordering:**
1. Governance legitimacy — defined by `Admin/Governance_Charter.md` Tier 1 Axioms
2. Authorization — granted through the human override doctrine defined there
3. Cryptographic enforcement — this file; verifies that authorized actions
   are executed with confirmed identity and integrity

Reversing this ordering — treating a valid signature as self-authorizing — is
the failure mode this file exists to prevent.

---

## Body

### I. Human Override Authentication & Verification (GOV-006)

**1. Multi-Signature Requirement**

No Tier 1 Constitutional Axiom or hard-line doctrine defined in
`Admin/Ethical_Constraints.md` may be overridden or suspended by a single
human operator. High-severity overrides require dual-token signature or a
multi-party hardware confirmation rule.

The specific minimum quorum threshold (number and diversity of independent
agents or hardware systems required) is defined by GOV-008 in
`Admin/Governance_Charter.md`. This file's multi-signature requirement
is not operational until GOV-008 provides that threshold. Until GOV-008
is resolved, the interim authentication requirement from
`Admin/Governance_Charter.md` §Human Override Doctrine applies:
independent confirmation from a second human operator, external cryptographic
signature from an orthogonal system, or a dated physical or digital record
created outside the repository system.

**2. Interim Bootstrap Authentication**

In the absence of an established public key infrastructure (Genesis Phase),
overrides must depend on physical air-gapped challenges — such as localized
split-secret tokens or pre-shared multi-party cryptographic pads — to prevent
local agent subversion. This is an interim procedure. It does not satisfy
Phase 3 requirements. It satisfies the current interim authentication
requirement while GOV-008 and the full PKI implementation remain unresolved.

**3. No Automated Session Continuance**

Override assertions are transactional and ephemeral. They do not persist
across multiple agent runtime sessions or automated multi-agent compilation
cycles. Every override requires a discrete signature event.

An agent that received override authorization in a prior session carries no
residual authority into a new session. This prevents authority accumulation
across session boundaries — a known attack vector in multi-agent systems where
session state is not fully cleared between runs.

**4. Authentication Event Logging**

All override attempts — successful or refused — must be logged with:
- Timestamp
- Identity of requesting agent or operator
- Scope of override requested
- Authentication method used
- Outcome (authorized / refused / escalated)

Logs are append-only. Override logs are subject to the Resolution Log
integrity requirements defined in `Admin/Repository_Integrity_Protocol.md`.

---

### II. Phase 3 Cryptographic Enforcement (RIP-005)

*All claims in this section are Placeholder — enforcement mechanisms defined
here do not yet exist. This section is the specification target for future
implementation.*

**1. Automated Commit Signing**

Transitioning from human audit logs to cryptographic assertions, all files
marked with status `Specification` must be signed using an approved node
key-pair. Unsigned Specification-status files are treated as unverified
regardless of their declared status.

**2. Frozen Section Verification**

Sections explicitly designated as `<!-- FROZEN -->` by governance files must
maintain static hashes. The automated audit script (`Admin/AUDIT_HARNESS.py`)
shall verify that local file content matches signed historic blocks before
triggering compilation or deployment pipelines. *(Placeholder — AUDIT_HARNESS.py
Phase 1 checks are not yet implemented per RIP-002. Phase 3 frozen-section
verification is a downstream dependency of Phase 1 completion.)*

**3. Phase Implementation Ordering**

Phase 3 cryptographic enforcement is the third phase of the automation
migration path defined in `Admin/Repository_Integrity_Protocol.md`. It cannot
be claimed before Phases 1 and 2 are complete:

| Phase | Prerequisite                                    | Status     |
|-------|-------------------------------------------------|------------|
| 1     | Structural checks in AUDIT_HARNESS.py           | Open — RIP-002 |
| 2     | Comparison checks requiring archived prior states | Open — RIP-001 |
| 3     | Cryptographic verification — this file          | Blocked by 1 and 2 |

Governance Enforcement State must not advance beyond actual implemented
capability. Claiming Phase 3 enforcement before Phases 1 and 2 are complete
is integrity theater.

---

### III. Salvaged Logic & Node Authentication (EL-006)

**Relationship to Electronics.md**

Component-level infiltration prevention for salvaged hardware — firmware
inspection protocols, Logic-Zero wipe procedures, and non-destructive
harvesting doctrine — is defined and owned by `Operations/Electronics.md`.
This section does not redefine that doctrine. It defines the administrative
authentication layer that sits above it: how nodes that have passed
Electronics.md validation are admitted into the trusted cluster.

A node that has passed Logic-Zero wipe and signature-verified bootstrap load
per Electronics.md doctrine is a candidate for cluster admission. Admission
itself requires the node identity verification procedures below.

**1. Zero-Trust Cluster Admission**

No salvaged or newly initialized node may join the local mesh or operational
network without completing both layers:
- Component-level trust: Logic-Zero wipe and signature-verified bootstrap
  load per `Operations/Electronics.md` EL-006 doctrine
- Node-level identity: key-pair registration and cluster admission handshake
  per this section

Passing one layer does not substitute for the other.

**2. Node Key-Pair Registration**

Each node must possess a unique key-pair generated within a trusted
initialization environment. Key generation must not occur on the node's
own hardware before that hardware has completed the Logic-Zero wipe and
bootstrap load. Key material generated on unverified hardware is untrusted
regardless of subsequent wipe procedures.

**3. Key Rotation Cycles**

Key rotation schedule is *(Placeholder — rotation period not yet defined;
log as SEC-002 pending resolution)*. Until defined, treat key material as
requiring rotation at each major version transition (v0→v1, v1→v2) at minimum.

**4. Admission Revocation**

A node whose key material is suspected compromised must be suspended from
cluster participation pending investigation. Suspension is reversible;
revocation is permanent. *(Full revocation doctrine is undefined — see
SEC-002.)*

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                                   | What Failed                                                              | What Was Learned                                                                                                     | Confidence | Revalidation Needed |
|------------|---------------|------------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Initial architecture without explicit trust boundary declaration | Implied "signature therefore authorized" logic left open as attack vector | Trust boundary must be declared explicitly before cryptographic mechanisms — governance legitimacy precedes enforcement | Analogous  | Yes                 |
| 2026-05-27 | Audit Review  | Firmware trust doctrine co-located with administrative security  | Duplicate ownership risk with Electronics.md; scope boundary became ambiguous | Electronics.md owns component-level infiltration prevention; Security_Protocols.md owns administrative authority layer above it | Replicated | No                 |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                                        | Why Abandoned                                                                                                           | Reconsider? |
|------------|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-26 | Firmware trust doctrine owned by Security_Protocols.md                      | Electronics.md already owns component-level infiltration prevention; dual ownership creates scope conflict               | No          |
| 2026-05-27 | SEC-001 quorum-under-partition resolved independently of GOV-008             | Minimum quorum definition is the same underlying problem approached from two angles; GOV-008 is the correct resolution owner | No — defer to GOV-008 |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Trust Boundary Declaration section removed, weakened, or moved below Body sections
- Multi-signature requirement simplified to single-key or software-only mechanism
  without corresponding update to `Admin/Governance_Charter.md`
- Phase 3 automation claims advanced beyond Placeholder status before RIP-001
  and RIP-002 are resolved
- Scope boundary revised to absorb firmware trust doctrine from Electronics.md
  without explicit Electronics.md scope boundary revision
- GOV-008 quorum definition referenced as resolved before GOV-008 is closed
- Node admission procedures removed or made optional
- Authentication event logging requirement removed or made non-append-only
- Abandoned path for SEC-001 independent resolution reopened without human
  ratification and GOV-008 resolution
- Ethical Anchor field absent, altered, or does not match canonical string
- Verification Ref field changed from Verification_Gates_LF.md

**Compound Drift Rule:** If multiple indicators activate simultaneously, halt
autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### SEC-001 — Quorum Recovery Under Terminal Network Division

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Architecture / Governance        |
| Blocking      | Yes                              |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-26                       |
| Last Reviewed | 2026-05-27                       |

**Description:** What cryptographic fallback procedure executes if a
multi-node swarm experiences a permanent communication partition, leaving
isolated clusters below the required multi-signature threshold for override
authorization.

**Why It Matters:** Bounded, local autonomy could stall indefinitely during
critical recovery operations if a quorum cannot legally be met. A fallback
that is too permissive creates a partition-exploitation attack vector; one
that is too restrictive freezes legitimate operations.

**Resolution Path:** Deferred to GOV-008 (`Admin/Governance_Charter.md`) —
minimum hardware and agent quorum definition is a prerequisite input to any
fallback procedure defined here. SEC-001 cannot be resolved before GOV-008
closes. Once GOV-008 defines the minimum quorum, revisit with a concrete
fallback proposal: time-locked decay window, hardware-level fallback protocol,
or escalation to human override via interim authentication. Cross-reference
RIP-001 (prior-state archival) — partition recovery may require archived
state access.

---

### SEC-002 — Key Revocation and Compromise Response Doctrine Undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Security / Governance            |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-27                       |
| Last Reviewed | 2026-05-27                       |

**Description:** The repository lacks defined procedures for key revocation
following confirmed or suspected compromise. Node admission suspension is
noted in the Body but the distinction between reversible suspension and
permanent revocation, the revocation authority chain, propagation to other
cluster nodes, and post-revocation re-admission criteria are all undefined.

**Why It Matters:** Without a revocation doctrine, a compromised key remains
nominally trusted until the next rotation cycle. In adversarial or degraded
environments this window may be operationally significant. Key compromise
without revocation doctrine is the cryptographic equivalent of a governance
system with no violation response ladder.

**Resolution Path:** Payment via Specification — define revocation authority
chain (who may initiate revocation, what evidence threshold is required),
propagation mechanism (how revocation is communicated to cluster nodes during
degraded connectivity), re-admission criteria (what a revoked node must
demonstrate to re-enter trusted status), and the distinction between
precautionary suspension and confirmed revocation. Cross-reference SEC-001 —
partition scenarios affect revocation propagation. Cross-reference GOV-006
(human override authenticity) — revocation of a node used for human override
authentication requires additional safeguards.

---

### SEC-003 — Key Rotation Period Undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Security / Technical             |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-27                       |
| Last Reviewed | 2026-05-27                       |

**Description:** No rotation period is defined for node key-pairs. The Body
currently defaults to version-transition rotation (v0→v1, v1→v2) as a
minimum, but no time-based or event-based rotation schedule exists.

**Why It Matters:** Indefinitely valid key material accumulates compromise
risk over time. Version-transition rotation is a floor, not a policy.
Without a defined schedule, rotation becomes ad hoc and audit verification
of rotation compliance is not possible.

**Resolution Path:** Payment via Specification — define rotation triggers:
time-based (calendar interval), event-based (version transition, personnel
change, suspected exposure), and condition-based (node hardware replacement,
Logic-Zero re-wipe). Cross-reference SEC-002 — rotation and revocation
procedures should be consistent.

---

### Resolution Log

- 2026-05-26: File created (v0.1) — initial architecture by Gemini
  (Engineer/Security). GOV-006 and RIP-005 resolution paths initiated.
  SEC-001 logged.
- 2026-05-27: v0.2 revision — Trust Boundary Declaration added as governing
  principle preceding Body. Scope boundary clarified: Electronics.md owns
  component-level doctrine, this file owns administrative authority layer.
  SEC-001 resolution path updated — deferred to GOV-008. SEC-002 (key
  revocation doctrine) and SEC-003 (key rotation period) logged. Relationship
  section added. Standard Drift Indicators added. Placeholder labels added
  to Phase 3 claims. Verification Ref corrected to Verification_Gates_LF.md.
  Lessons Learned and Abandoned Paths sections populated. Open Unknowns
  updated to 3.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; GOV-006
  (human override authenticity) and GOV-008 (minimum agent quorum) are the
  originating unknowns this file resolves; Trust Boundary Declaration defers
  to the governance hierarchy defined there; Tier 1 Axioms are not subject
  to cryptographic override
- `Admin/Repository_Integrity_Protocol.md` — RIP-005 (Security_Protocols.md
  dependency) is the originating unknown for Phase 3 enforcement; this file
  is the Phase 3 specification target; Phases 1 and 2 defined there are
  prerequisites to Phase 3 implementation here
- `Admin/Ethical_Constraints.md` — co-Tier 1; Anti-Weaponization and Life
  Preservation doctrines are not subject to override by any cryptographic
  mechanism regardless of signature validity
- `Admin/Auditor_Protocols.md` — Tier 2; authentication event logs are
  subject to the audit trail requirements defined there; override logs
  are governed by the Human Override Doctrine defined there
- `Admin/Forge_Audit_Kit.md` — Tier 3; SEC- sidecar prefix to be added to
  Sidecar ID Reference table at next kit update
- `Operations/Electronics.md` — component-level infiltration prevention
  owner; Logic-Zero wipe and firmware trust doctrine defined there are
  Layer 1 prerequisites for node admission procedures defined here; the
  two files are complementary layers, not overlapping owners
- `Unknowns.md` — GOV-006 and RIP-005 status should be updated to
  In Progress now that this file exists as an executing resolution path
- `Admin/Governance_Charter.md` GOV-008 — minimum quorum definition is
  a blocking prerequisite input to SEC-001 resolution and to the
  multi-signature threshold defined in Section I

---

## Status

Version 0.2 — structural revision pass (2026-05-27).

**Changes from v0.1:**
- Trust Boundary Declaration section added as governing principle — explicit
  statement that cryptographic verification does not confer governance
  legitimacy; authorization flows Tier 1 downward
- Scope boundary clarified — Electronics.md owns component-level infiltration
  prevention; this file owns administrative authority layer; dual ownership
  risk resolved
- Verification Ref field corrected from Admin/Forge_Audit_Kit.md to
  Verification_Gates_LF.md
- Section III rewritten — explicit two-layer admission model (Electronics.md
  component trust + node identity verification); firmware trust cross-reference
  formalized
- Phase 3 section claims labeled Placeholder throughout
- SEC-001 resolution path updated — deferred to GOV-008; independent
  resolution abandoned
- SEC-002 logged — key revocation and compromise response doctrine undefined
- SEC-003 logged — key rotation period undefined; Open Unknowns updated to 3
- Relationship to Existing Documents section added
- Standard Drift Indicators added per File_Template.md
- Abandoned Paths section populated
- Lessons Learned entries added for trust boundary and scope boundary decisions
- Safety Advisory updated — decision rule added per File_Template.md doctrine

**What must remain constant:**

**Cryptographic verification confirms identity and integrity.**
**It does not confer governance legitimacy.**
**Authorization flows from Tier 1 downward.**

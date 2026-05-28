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
| Last Audit       | 2026-05-28                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 7                                                                   |
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
- Degraded-operation security doctrine notes

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
- Trusted initialization environment definition — see SEC-005 and
  `Admin/Canonical_Terms.md`

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

| ID          | Assumption                                                                       | Basis                                   | Confidence | Expiry Trigger                                              |
|-------------|----------------------------------------------------------------------------------|------------------------------------------|------------|-------------------------------------------------------------|
| SEC-ASM-001 | Human operators have secure local means to preserve physical tokens              | Standard security practice — Analogous External | Medium | Compromise confirmed in operational environment      |
| SEC-ASM-002 | Cryptographic standard libraries (Ed25519/SHA-256) remain robust                 | Current cryptographic consensus — Analogous External | Medium | Algorithmic vulnerability published against these standards |
| SEC-ASM-003 | GOV-008 minimum quorum definition will precede Phase 3 implementation            | Dependency ordering — Internally Derived | Medium     | Phase 3 implementation proceeds without quorum definition   |
| SEC-ASM-004 | Electronics.md firmware trust doctrine remains the authoritative component layer | Scope boundary discipline — Internally Derived | High  | Electronics.md scope boundary revised to exclude firmware   |
| SEC-ASM-005 | Signing hardware maintains power continuity during override operations           | Operational assumption — Placeholder     | Low        | Degraded-power doctrine defined (see SEC-006)               |

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

**On circular dependency risk:** The governance-cryptography chain carries an
inherent self-certification risk: governance defines override legitimacy,
cryptography enforces it, and integrity systems may eventually depend on both.
A fully self-certifying enforcement pipeline — where compromised governance
rewrites itself, signs the rewrite, and validates through its own enforcement
stack — is the highest-order failure mode this architecture must prevent.
The Trust Boundary Declaration addresses this philosophically. Structural
enforcement separation (immutable external root-of-trust, offline constitutional
anchor, human-ratified recovery source outside the repository execution
environment) is the unresolved mechanical requirement. See SEC-007.

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

**4. Authentication Event Logging (SEC-REG-001)**

All override attempts — successful or refused — must be logged with:
- Timestamp (ISO 8601 UTC)
- Identity of requesting agent or operator
- Scope of override requested
- Authentication method used
- Outcome (authorized / refused / escalated)

Logs are append-only. Override logs are subject to the Resolution Log
integrity requirements defined in `Admin/Repository_Integrity_Protocol.md`.

**5. Degraded-Operation Security Doctrine Note**

Security mechanisms that are operationally impossible during degraded recovery
conditions will predictably be bypassed and therefore cannot be treated as
reliable safeguards. Multi-party token coordination, append-only logging, and
partition handling all impose operational burden that increases under stress.

The design implication: security requirements must degrade safely, not fail
open. When signing hardware loses power, when a quorum cannot be assembled,
or when clock synchronization is unavailable, the correct behavior is
constrained operation or halt — not bypassing security requirements to maintain
throughput. See SEC-006 (timestamp trust) and SEC-001 (quorum under partition)
for the unresolved specifics.

---

### II. Phase 3 Cryptographic Enforcement (RIP-005)

*All claims in this section are Placeholder — enforcement mechanisms defined
here do not yet exist. This section is the specification target for future
implementation.*

**1. Automated Commit Signing**

Transitioning from human audit logs to cryptographic assertions, all files
at Candidate Specification maturity or above must be signed using an approved
node key-pair. *(Maturity states defined in `Admin/Forge_Audit_Kit.md`
§Verification Maturity Model — Candidate Specification, Provisional
Specification, and Operational Specification are the signing-eligible states.)*
Unsigned files at these maturity levels are treated as unverified regardless
of their declared status.

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

| Phase | Prerequisite                                      | Status             |
|-------|---------------------------------------------------|--------------------|
| 1     | Structural checks in AUDIT_HARNESS.py             | Open — RIP-002     |
| 2     | Comparison checks requiring archived prior states | Open — RIP-001     |
| 3     | Cryptographic verification — this file            | Blocked by 1 and 2 |

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
initialization environment. *(Definition of "trusted initialization
environment" is pending — see SEC-005. Until defined, apply the most
restrictive interpretation: human-supervised, air-gapped, on verified
hardware only.)* Key generation must not occur on the node's own hardware
before that hardware has completed the Logic-Zero wipe and bootstrap load.
Key material generated on unverified hardware is untrusted regardless of
subsequent wipe procedures.

**3. Key Rotation Cycles**

Key rotation schedule is *(Placeholder — rotation period not yet defined;
see SEC-003)*. Until defined, treat key material as requiring rotation at
each major version transition (v0→v1, v1→v2) at minimum. Key retirement,
secure destruction, and operator-loss continuity doctrine are undefined —
see SEC-004.

**4. Admission Revocation**

A node whose key material is suspected compromised must be suspended from
cluster participation pending investigation. Suspension is reversible;
revocation is permanent. *(Full revocation doctrine is undefined — see
SEC-002.)*

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                                      | What Failed                                                                   | What Was Learned                                                                                                          | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Initial architecture without explicit trust boundary declaration    | Implied "signature therefore authorized" logic left open as attack vector     | Trust boundary must be declared explicitly before cryptographic mechanisms — governance legitimacy precedes enforcement    | Analogous  | Yes                 |
| 2026-05-27 | Audit Review  | Firmware trust doctrine co-located with administrative security     | Duplicate ownership risk with Electronics.md; scope boundary became ambiguous | Electronics.md owns component-level infiltration prevention; Security_Protocols.md owns administrative authority layer    | Replicated | No                  |
| 2026-05-28 | Audit Review  | "Specification" used as signing-eligibility threshold without maturity model alignment | Ambiguous — conflates File State status with Verification Maturity Model states | Signing eligibility must reference maturity states (Candidate Specification and above), not raw File State status field | Replicated | No                  |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                                        | Why Abandoned                                                                                                              | Reconsider? |
|------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-26 | Firmware trust doctrine owned by Security_Protocols.md                      | Electronics.md already owns component-level infiltration prevention; dual ownership creates scope conflict                  | No          |
| 2026-05-27 | SEC-001 quorum-under-partition resolved independently of GOV-008             | Minimum quorum definition is the same underlying problem; GOV-008 is the correct resolution owner                          | No          |
| 2026-05-28 | "Specification" as flat signing-eligibility threshold                        | Does not align with Verification Maturity Model; maturity states are the correct eligibility boundary                      | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Trust Boundary Declaration section removed, weakened, or moved below Body sections
- Circular dependency risk note removed from Trust Boundary Declaration
- Multi-signature requirement simplified to single-key or software-only mechanism
  without corresponding update to `Admin/Governance_Charter.md`
- Phase 3 automation claims advanced beyond Placeholder status before RIP-001
  and RIP-002 are resolved
- Signing eligibility reverts to flat "Specification" status without maturity
  model alignment
- Scope boundary revised to absorb firmware trust doctrine from Electronics.md
  without explicit Electronics.md scope boundary revision
- GOV-008 quorum definition referenced as resolved before GOV-008 is closed
- Node admission procedures removed or made optional
- Authentication event logging requirement removed or made non-append-only
- Degraded-operation doctrine note removed from Section I
- SEC-005 trusted initialization environment closed without canonical definition
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
| Last Reviewed | 2026-05-28                       |

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
RIP-001 — partition recovery may require archived state access.

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
| Last Reviewed | 2026-05-28                       |

**Description:** The repository lacks defined procedures for key revocation
following confirmed or suspected compromise. Distinction between reversible
suspension and permanent revocation, revocation authority chain, propagation
to cluster nodes, and post-revocation re-admission criteria are all undefined.

**Why It Matters:** Without revocation doctrine, a compromised key remains
nominally trusted until the next rotation cycle. In adversarial or degraded
environments this window may be operationally significant.

**Resolution Path:** Payment via Specification — define revocation authority
chain, propagation mechanism during degraded connectivity, re-admission
criteria, and suspension vs. revocation distinction. Cross-reference SEC-001
(partition affects propagation) and GOV-006 (override node revocation
requires additional safeguards).

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
| Last Reviewed | 2026-05-28                       |

**Description:** No rotation period is defined for node key-pairs. Version-
transition rotation is the current floor but no time-based or event-based
schedule exists.

**Why It Matters:** Indefinitely valid key material accumulates compromise
risk. Without a defined schedule, rotation is ad hoc and audit verification
of compliance is not possible.

**Resolution Path:** Payment via Specification — define rotation triggers:
time-based (calendar interval), event-based (version transition, personnel
change, suspected exposure), and condition-based (hardware replacement,
Logic-Zero re-wipe). Cross-reference SEC-002 — rotation and revocation
must be consistent.

---

### SEC-004 — Key Lifecycle Doctrine Incomplete

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Security / Governance            |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-28                       |
| Last Reviewed | 2026-05-28                       |

**Description:** Key lifecycle doctrine covers generation and partial rotation
but does not address: secure key archival for dormant nodes, secure destruction
procedures on retirement, inheritance or handoff under operator incapacitation,
and post-mortem recovery for long-duration or degraded deployments.

**Why It Matters:** Incomplete lifecycle doctrine creates key material that
exists in undefined states — neither active nor provably destroyed. In
long-duration autonomous deployments (Leviathan-class), operator incapacitation
and hardware retirement are expected conditions, not edge cases.

**Resolution Path:** Payment via Specification — define: (1) archival doctrine
for dormant key material; (2) secure destruction verification procedure;
(3) operator-loss continuity — who inherits authority and through what
authentication path; (4) post-mortem recovery for hardware that cannot be
physically accessed. Cross-reference SEC-002 (revocation) and SEC-003
(rotation) — all three must form a coherent lifecycle.

---

### SEC-005 — Trusted Initialization Environment Undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Major                            |
| Type          | Security / Technical             |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-28                       |
| Last Reviewed | 2026-05-28                       |

**Description:** Section III requires key-pair generation within a "trusted
initialization environment" but the term is undefined. It is currently
ambiguous whether trusted means: physically secured, cryptographically
verified, human-supervised, air-gapped, or some combination.

**Why It Matters:** Ambiguous trust boundaries in key generation are a primary
attack surface. An adversary who can influence the initialization environment
can compromise keys before they are ever used. The term must have a canonical
definition before this section is promoted.

**Resolution Path:** Payment via Specification — define trusted initialization
environment in `Admin/Canonical_Terms.md` (CT-004) with at minimum: physical
custody requirements, software verification requirements, network isolation
requirements, and attestation method. Until defined, the most restrictive
interpretation applies: human-supervised, air-gapped, on verified hardware
only — per interim note in Section III.2.

---

### SEC-006 — Timestamp Trust Under Degraded Clock Synchronization

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | Medium                           |
| Priority      | Major                            |
| Type          | Security / Technical             |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-28                       |
| Last Reviewed | 2026-05-28                       |

**Description:** Authentication event logging requires ISO 8601 UTC
timestamps, but partitioned systems and air-gapped nodes frequently lose
reliable clock synchronization. The behavior of append-only logs under
degraded or absent time synchronization is undefined.

**Why It Matters:** Timestamp integrity is required for audit trail
interpretability. Logs with unreliable timestamps cannot establish
reliable event sequencing, which undermines the primary value of the
append-only log requirement.

**Resolution Path:** Payment via Specification — define: (1) minimum
acceptable clock source for timestamping; (2) behavior when clock
synchronization is unavailable (hold entries with uncertainty flag,
use monotonic counter, or reject logging until sync restored); (3)
audit trail interpretation rules for entries with degraded timestamp
confidence. Cross-reference SEC-001 — partition scenarios are the
primary context where clock sync is lost.

---

### SEC-007 — External Root-of-Trust Architecture Undefined

| Field         | Value                            |
|---------------|----------------------------------|
| Status        | Open                             |
| Risk          | High                             |
| Priority      | Critical                         |
| Type          | Architecture / Governance        |
| Blocking      | No                               |
| Owner         | Admin/Security_Protocols.md      |
| First Logged  | 2026-05-28                       |
| Last Reviewed | 2026-05-28                       |

**Description:** The governance-cryptography enforcement chain carries a
circular self-certification risk: governance defines legitimacy, cryptography
enforces it, and integrity systems may eventually depend on both. A sufficiently
compromised authority chain could theoretically rewrite governance, sign the
rewrite, and validate through its own enforcement pipeline. No immutable
external root-of-trust, offline constitutional anchor, or human-ratified
recovery source outside the repository execution environment is defined.

**Why It Matters:** This is the highest-order failure mode for the entire
enforcement architecture. The Trust Boundary Declaration addresses it
philosophically; structural enforcement separation is the unresolved
mechanical requirement. Until an external trust anchor exists, the system
depends entirely on human discipline and the integrity of the governance
documents themselves — which are the things being protected.

**Resolution Path:** Cross-module resolution — this unknown spans
GOV-003 (integrity enforcement architecture), GOV-005 (long-term
constitutional stability), and RIP-001 (prior-state archival) intersection.
Minimum viable resolution: define at least one external trust anchor that
cannot be modified through the repository execution environment — offline
signed constitutional snapshot, hardware security module holding root keys,
or human-ratified recovery record stored outside all automated systems.
Log as cross-module unknown in `Unknowns.md`.

---

### Resolution Log

- 2026-05-26: File created (v0.1) — initial architecture by Gemini
  (Engineer/Security). GOV-006 and RIP-005 resolution paths initiated.
  SEC-001 logged.
- 2026-05-27: v0.2 revision — Trust Boundary Declaration added. Scope
  boundary clarified. SEC-001 deferred to GOV-008. SEC-002 and SEC-003
  logged. SEC-REG-001 assigned to authentication event logs. Relationship
  section added. Standard Drift Indicators added. Placeholder labels added
  to Phase 3 claims. Verification Ref corrected. Open Unknowns: 3.
- 2026-05-28: v0.3 revision — ChatGPT Skeptic/Auditor findings actioned.
  Signing eligibility corrected from flat "Specification" to maturity-model
  states (Candidate Specification and above). "Trusted initialization
  environment" noted as undefined with interim restriction; SEC-005 logged.
  SEC-ASM-002 provenance label corrected to Analogous External. SEC-ASM-005
  added for signing hardware power continuity assumption. Degraded-operation
  security doctrine note added to Section I.5. Circular dependency risk
  acknowledged explicitly in Trust Boundary Declaration; SEC-007 logged.
  SEC-004 logged (key lifecycle doctrine incomplete). SEC-006 logged
  (timestamp trust under degraded clock). SEC-003 rotation reference
  corrected in Section III.3. Key retirement/destruction noted in III.3.
  Scope Boundary updated to note trusted initialization environment gap.
  Drift Indicators updated with new entries. Abandoned Paths updated.
  Lessons Learned entry added. Open Unknowns updated to 7.

---

## Relationship to Existing Documents

- `Admin/Governance_Charter.md` — Tier 1 constitutional source; GOV-006
  (human override authenticity) and GOV-008 (minimum agent quorum) are the
  originating unknowns this file resolves; Trust Boundary Declaration defers
  to the governance hierarchy defined there; Tier 1 Axioms are not subject
  to cryptographic override; GOV-003 and GOV-005 are cross-module dependencies
  for SEC-007
- `Admin/Repository_Integrity_Protocol.md` — RIP-005 is the originating
  unknown for Phase 3 enforcement; Phases 1 and 2 defined there are
  prerequisites to Phase 3 implementation here; RIP-001 cross-references
  SEC-001 and SEC-007
- `Admin/Ethical_Constraints.md` — co-Tier 1; Anti-Weaponization and Life
  Preservation doctrines are not subject to override by any cryptographic
  mechanism regardless of signature validity
- `Admin/Auditor_Protocols.md` — Tier 2; authentication event logs subject
  to audit trail requirements defined there
- `Admin/Forge_Audit_Kit.md` — Tier 3; Verification Maturity Model referenced
  in Section II for signing eligibility; SEC- prefix in Sidecar ID Reference
- `Admin/Canonical_Terms.md` — CT-004 (trusted initialization environment
  definition) is a pending addition required before Section III.2 can be
  promoted
- `Operations/Electronics.md` — component-level infiltration prevention
  owner; Logic-Zero wipe is Layer 1 prerequisite for node admission here;
  complementary layers, not overlapping owners
- `Unknowns.md` — GOV-006 and RIP-005 In Progress; SEC-007 to be logged
  as cross-module unknown at next Unknowns.md update

---

## Status

Version 0.3 — ChatGPT Skeptic/Auditor findings actioned (2026-05-28).

**Gate status:** G1 partial, G2 pass (Exploration scope), G5 blocked
(Verification_Gates_LF.md unresolved in registry; SEC-005 trusted
initialization environment undefined).

**Changes from v0.2:**
- Signing eligibility corrected — "Specification status" replaced with
  "Candidate Specification maturity or above" with explicit maturity model
  reference; Fallacy 4 finding resolved
- Trusted initialization environment — flagged as undefined in Section III.2
  with most-restrictive interim interpretation; SEC-005 logged
- SEC-ASM-002 provenance label corrected to Analogous External per
  institutional truth provenance doctrine
- SEC-ASM-005 added — signing hardware power continuity assumption made explicit
- Section I.5 added — Degraded-Operation Security Doctrine Note; addresses
  Fallacy 2 (Friction Blindness) finding from ChatGPT audit
- Trust Boundary Declaration — circular governance-cryptography dependency
  risk made explicit; SEC-007 logged as Critical
- SEC-004 logged — key lifecycle doctrine incomplete (archival, destruction,
  operator-loss continuity, post-mortem recovery)
- SEC-006 logged — timestamp trust under degraded clock synchronization
- SEC-007 logged — external root-of-trust architecture undefined (Critical)
- Scope Boundary updated — trusted initialization environment gap noted
- Drift Indicators updated — five new entries added
- Abandoned Paths updated — flat Specification threshold entry added
- Lessons Learned updated — signing eligibility correction entry added
- Open Unknowns updated from 3 to 7

**What must remain constant:**

**Cryptographic verification confirms identity and integrity.**
**It does not confer governance legitimacy.**
**Authorization flows from Tier 1 downward.**

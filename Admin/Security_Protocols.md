# Security_Protocols.md — Cryptographic Trust & Multi-Agent Node Security

> ⚠️ **Operational Safety Advisory**
> Physical security and digital authority are tightly coupled within the Forge. 
> A compromise of cryptographic key material or human override tokens can bypass 
> down-stream safeguards, enabling the malicious rewriting of operational files 
> or unauthorized activation of high-energy machinery. Key infrastructure must be 
> decoupled from standard runtime environments. Never store root cryptographic seed 
> material in a standard agent-accessible workspace or online repository node.

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Forge_Audit_Kit.md                                            |
| Last Audit       | 2026-05-26                                                          |
| Auditor          | Gemini — Engineer/Security                                          |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | High                                                                |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Cryptographic mechanisms for multi-signature Human Override Verification.
- Automated code-signing protocols for file integrity verification (RIP Phase 3).
- Node identity verification and key rotation cycles within the cluster environment.
- Minimum token complexity, air-gapping requirements, and cryptographic fallback behaviors during network division.

**This file DOES NOT define:**
- Specific operating system firewall commands or network router firmware rules.
- Local facility access control (locks, badges, physical perimeter barriers).
- High-level ethical frameworks (governed exclusively by `Ethical_Constraints.md`).

---

## File Purpose

This document establishes the technical security implementation rules for validating administrative authority, ensuring the integrity of the active knowledge graph, and managing multi-node validation in untrusted, degraded, or adversarial deployment environments.

---

## Assumptions

| ID | Assumption | Impact if Invalid |
|----|------------|-------------------|
| SEC-ASM-001 | Human operators have secure local means to preserve physical tokens. | If compromise occurs, human overrides can be spoofed by unauthorized actors. |
| SEC-ASM-002 | Cryptographic standard libraries (Ed25519/SHA-256) remain robust. | Algorithmic compromise invalidates the underlying security substrate. |

---

## Body

### I. Human Override Authentication & Verification (GOV-006 / RIP-005)
1. **Multi-Signature Requirement:** No Tier 1 Constitutional Axiom or hard-line doctrine defined in `Ethical_Constraints.md` may be overridden or suspended by a single human operator. High-severity overrides require dual-token signature or a multi-party hardware confirmation rule.
2. **Interim Bootstrap Authentication:** In the absence of an established public key infrastructure (Genesis Phase), overrides must depend on physical air-gapped challenges (such as localized split-secret tokens or pre-shared multi-party cryptographic pads) to prevent local agent subversion.
3. **No Automated Session Continuance:** Override assertions are transactional and ephemeral. They do not persist across multiple agent runtime sessions or automated multi-agent compilation cycles. Every override requires a discrete signature event.

### II. Phase 3 Cryptographic Enforcement (RIP-005)
1. **Automated Commit Signing:** Transitioning from human audit logs to cryptographic assertions, all files marked with status `Specification` must be signed using an approved node key-pair.
2. **Frozen Section Verification:** Sections explicitly designated as `[FROZEN]` by governance files must maintain static hashes. The automated audit script (`AUDIT_HARNESS.py`) shall verify that local file content matches signed historic blocks before triggering compilation or deployment pipelines.

### III. Salvaged Logic & Node Authentication (EL-006 / FN-001)
1. **Zero-Trust Firmware Baseline:** No salvaged Microcontroller Unit (MCU) or single-board system may join the local mesh or operational network if it contains a locked bootloader or unverified firmware image.
2. **Logic-Zero Wipe:** Repurposed logic units must undergo a full flash erase and signature-verified bootstrap load using trusted local code repositories.

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| 2026-05-26 | Initial Architecture | — | Codified initial structural requirements linking RIP Phase 3 and Governance Charter override conditions to a centralized file. |

---

## Active Disputes

*(empty)*

---

## Auditor Notes & Unknowns

### SEC-001 — Quorum Recovery Under Terminal Division
| Field         | Value             |
|---------------|-------------------|
| Status        | Open              |
| Risk          | Medium            |
| Priority      | Major             |
| Type          | Architecture      |
| Blocking      | Yes               |
| Owner         | Security Module   |
| First Logged  | 2026-05-26        |
| Last Reviewed | 2026-05-26        |

**Description:** What cryptographic fallback procedure executes if a multi-node swarm experiences a permanent communication partition, leaving isolated clusters below the required multi-signature threshold.

**Why It Matters:** Bounded, local autonomy could stall indefinitely during critical recovery operations if a quorum cannot legally be met.

**Resolution Path:** Define a time-locked decay window or a hardware-level fallback protocol to safely handle structural degradation without enabling single-node compromise.

---

## Abandoned Paths

*(empty)*

---

## Drift Indicators

### Local Drift Triggers
- Any attempt to simplify human override constraints to a single-key or software-only mechanism without updating `Governance_Charter.md`.
- Promoting this document to `Specification` status before a functional Python execution test for Phase 3 signature checking is integrated into `AUDIT_HARNESS.py`.

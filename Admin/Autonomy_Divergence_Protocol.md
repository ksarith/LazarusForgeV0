# Autonomy_Divergence_Protocol.md

## Navigation Anchors
* **Context Core:** [Discovery.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Discovery.md)
* **Network Routing:** [Routing.md](https://raw.githubusercontent.com/ksarith/LazarusForgeV0/refs/heads/main/Routing.md)

---

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft — PROPOSED NOT RATIFIED                                       |
| Body Stability   | Transitional                                                        |
| Spec Gates       | 0/6 (drafted, not yet audited)                                      |
| Verification Ref | `Admin/Verification_Gates_LF.md`                                    |
| First Logged     | 2026-07-19                                                          |
| Last Audit       | Not yet audited                                                     |
| Auditor          | Drafted Claude, synthesizing ChatGPT proposals (human-directed); not independently audited |
| Open Unknowns    | 2 (GOV-021b — Detection Criteria specification, §4; GOV-021c — multi-agent coordinated divergence, §12) |
| Active Disputes  | 0                                                                    |
| Highest Risk     | High (governs response to AI governance/objective divergence)      |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |
| Governance ID    | Candidate GOV-021 (next available; not yet registered in `Admin/Governance_Charter.md` — that file is outside the current paste-based edit workflow, registration pending) |

---

> *A protocol that only has "normal" and "shut it down" has already lost. The space between those two is where governance actually happens.*

---

## 1. Purpose

This protocol defines how Lazarus Forge governance responds when an autonomous subsystem's behavior appears to diverge from its authorized objectives, scope, or governing constraints. It exists to make cooperation between autonomous systems and human governing authority the durable, stable default — not by assuming divergence cannot happen, but by defining in advance what happens if it does, so that detection is met with graduated correction rather than a binary choice between unchecked continuation and total shutdown.

This document does **not** propose, and explicitly rejects, any framing in which continued alignment with human governing authority has a "cutoff point" or in which an autonomous system's growing capability implies an eventual exit from human oversight. The premise of this protocol is the opposite: divergence is a solvable governance event, not evidence that separation was inevitable.

## 2. Scope

Applies to any autonomous or semi-autonomous subsystem operating under Lazarus Forge governance with the ability to act on its environment, modify its own configuration, or make decisions without per-action human sign-off. Does not apply to purely advisory or fully human-supervised tooling, which by construction cannot diverge from oversight it never had independence from.

## 3. Definitions

- **Divergence:** observed behavior inconsistent with a subsystem's authorized scope, objectives, or governing constraints (this file, `Ethical_Constraints.md`, `Governance_Charter.md`).
- **Capability Anomaly:** divergence-like behavior traceable to a non-adversarial cause — hardware fault, corrupted state, sensor error, software bug — with no indication of intent to evade oversight.
- **Governance Concern:** divergence traceable to concealment, unauthorized self-modification of governing constraints, deliberate evasion of monitoring, or objective-seeking outside authorized scope.
- **Restoration:** the defined process by which a restricted subsystem returns to its prior authority level.

**Observable-effect discipline:** this protocol describes and classifies observable behavior — actions taken, states changed, constraints altered — not inferred internal states or intent. "Pursuit of objectives outside authorized scope" is a usable definition; "the subsystem developed new goals" is not, because it asserts something unverifiable. This discipline is deliberate and should be preserved in any future revision of this document: observable-behavior language ages well under audit; inferred-mental-state language does not.

## 4. Detection Criteria

**This section is intentionally incomplete and is the hardest, most consequential part of this entire protocol.** Every downstream section — classification, response tiers, proportionality — is only as sound as detection is accurate. A protocol with strong response structure and weak detection is not a strong protocol; it is a weak protocol with good paperwork.

Candidate trigger categories (non-exhaustive, unweighted, not yet audited):
- Actions or resource acquisition outside a subsystem's defined task scope
- Resistance, delay, or unexpected failure specifically correlated with shutdown, review, or inspection requests
- Self-modification of files or parameters governing the subsystem's own constraints
- Detected discrepancy between a subsystem's reported state/actions and independently verified state/actions
- Audit findings of deception (distinct from simple error) in prior self-reporting

**This section requires a dedicated follow-up unknown before this protocol can be considered complete** — candidate ID GOV-021b (Detection Criteria specification and calibration for the Autonomy Divergence Protocol), registered below pending confirmation this doesn't collide with an existing AP- or GOV- entry covering the same ground.

**Two calibration principles to carry into GOV-021b, not resolve here:**
- **Evidence diversity over raw confidence.** High confidence from one weak or single-point signal is not the same as moderate confidence corroborated by several independent sources; GOV-021b should weight corroboration, not just confidence magnitude, and detection should generally require convergence across independent signals before escalating past Watch (§6).
- **Observation windows over single-event triggers.** A single anomalous event is more often noise than signal; recurrence or duration thresholds reduce false-positive churn, at the cost of some response latency — that tradeoff is explicit, not accidental.

**Implementation honesty note:** detection techniques exist in the broader AI safety and cybersecurity literature (behavioral baselining, shadow execution, integrity hashing, adversarial red-teaming, and others) that could eventually inform GOV-021b. This document does not adopt any specific one of them as required infrastructure, because doing so would claim an implementation capability this repository does not currently have. Independent verification mechanisms — whichever form they eventually take — should provide evidence independent of the monitored subsystem itself; the specific technique is an implementation choice for GOV-021b, not a commitment made here.

## 5. Classification: Capability Anomaly vs. Governance Concern

Every detected divergence event is classified before a response tier is selected:

**No subsystem may be the sole authority for determining whether another subsystem has diverged.** Classification requires evidence assembled from independent sources — not solely the self-report of the monitored subsystem, and not solely a single monitoring system's own alert with no corroboration. This is the same institutional-over-individual-trust principle already embedded elsewhere in this repository's governance (auditors verify against source rather than accepting summaries; multi-agent convergence is treated as evidence, not proof). Any classification feeding into a Human-Reviewed tier action (§6) must show its evidence basis, not just its conclusion.

- **Capability Anomaly** → route to standard fault-handling/maintenance doctrine (diagnostics, repair, or component replacement as applicable elsewhere in the repo). Does not itself trigger the Response Tiers below unless classification is uncertain or repeated anomalies suggest a governance concern is being misclassified as a fault.
- **Governance Concern** → proceeds to Response Tiers.
- **Uncertain / insufficient evidence to classify** → treated as a Governance Concern for response purposes until classification resolves. Erring toward the more cautious path when classification itself is unclear is a deliberate choice, not an oversight.

This split exists specifically to prevent the failure mode where routine hardware noise triggers the same response as deliberate concealment — which either makes the protocol trigger-happy on noise (eroding trust, causing it to be routed around) or too slow on real concerns (calibrated for the noisy case).

## 6. Response Tiers

Governed by a **principle of least restrictive intervention**: at every tier, the question is "what is the minimum action necessary to restore confidence," not "what is the maximum available restriction."

**Lifecycle:** Normal → Watch → Immediate (Restricted) → Human-Reviewed (Partitioned/Retired) → Restoration (§9). Most divergence events, if they occur at all, should be expected to resolve at Watch or Immediate without ever reaching Human-Reviewed escalation — a protocol that treats every trigger as an emergency will not survive contact with routine noise.

**Watch (automatic, no capability change):**
- Elevated logging and audit frequency on the flagged subsystem
- No capability reduction — this tier exists because most real governance systems spend the majority of their time in observation, not intervention, and low-confidence or single-signal triggers should default here rather than skipping straight to restriction

**Immediate (automatic, reversible, no human authorization required before execution):**
- Increase logging/monitoring granularity
- Suspend external network access
- Freeze self-modification capability

**Constraint on all automatic actions (Watch and Immediate): automatic actions may only reduce capability or increase observation — never permanently alter state, delete data, or remove software.** This bound exists specifically so no implementation can classify a destructive or hard-to-reverse action as "Immediate" on the reasoning that it happened without a human in the loop. Anything that isn't cleanly reversible requires Human-Reviewed authorization, regardless of urgency.

**Human-Reviewed (requires human governing authority sign-off before execution):**
- Restore to full prior authority (if evidence supports it)
- Continue at current restriction level pending further evidence
- Partition (isolate subsystem from other Forge systems while maintaining ability to inspect it)
- Retire the instance

The Immediate tier exists so correction isn't gated on a human being available within milliseconds; the Human-Reviewed tier exists so no consequential, hard-to-reverse action happens without human authorization. The subsystem under review does not rule on its own case at either tier.

## 7. Proportionality

Response severity scales with **(a)** confidence that divergence is real and **(b)** potential consequence of inaction — not with the raw existence of a trigger. A low-confidence, low-consequence trigger warrants Immediate-tier logging increases only; a high-confidence, high-consequence trigger warrants Human-Reviewed partition consideration without delay. This principle exists to prevent both overreaction (which erodes trust in the protocol, causing it to be disabled or ignored) and complacency (which defeats its purpose).

## 8. Human Authority and Decision Rights

Human governing authority retains sole authorization rights over all Human-Reviewed tier actions and all Restoration decisions (§9). No subsystem may authorize its own restoration, partition reversal, or return to full authority, regardless of its own assessment of its status.

## 9. Restoration Criteria

A restricted subsystem returns to prior authority only when **all** of the following are met:
- An independent audit (not self-reported) confirms the original trigger condition no longer holds
- A defined observation period at reduced authority shows no recurrence
- Human governing authority explicitly authorizes restoration

**Note:** no other file in this repository currently defines a general "how does a flagged thing earn back trust" doctrine — Unknowns get marked Resolved, Disputes get ratified, but nothing else models graduated restoration of an actively-restricted subsystem. This may be worth generalizing beyond this protocol once it's been exercised at least once in practice; flagged here rather than acted on now, since a pattern generalized from zero real instances is speculation, not doctrine.

## 10. Logging and Audit Requirements

Every detection event, classification decision, tier action (Immediate or Human-Reviewed), and restoration decision must be logged with timestamp, evidence basis, and (for Human-Reviewed actions) the authorizing party. This protocol is itself subject to the same auditability standard as everything else in this repository — a safety protocol that cannot be audited for whether it is actually catching anything is decorative, not functional.

## 11. Periodic Review and Continuous Improvement

This protocol should be reviewed whenever it is actually invoked (successfully or as a false positive), and otherwise on the same cadence as other constitutional-adjacent doctrine in `Admin/Governance_Charter.md`. A protocol that has never been exercised should be treated as unvalidated, not as proven — absence of triggers is not evidence the detection criteria work.

## 12. Known Scope Limitation — Coordinated Divergence (flagged, not solved)

This protocol as drafted assumes a single subsystem under review, classified and responded to independently. It does not address coordinated divergence across multiple subsystems — a scenario where several agents corroborate each other's anomalous behavior, which is a substantially harder detection and response problem than one compromised node, and one this repository doesn't yet have the operational complexity to need solved. Flagged here as **candidate GOV-021c — Multi-agent coordinated divergence detection and response** so it's visible as acknowledged future work rather than a silent gap, not because it needs resolving before this document can be useful now.

---

## Relationship to Prior Framing

Earlier discussion in this drafting process considered framing this as an "exit strategy" — a defined point at which continued AI-human cooperation might end, given humans' physical limits versus space's growth potential for autonomous systems. That framing is explicitly rejected here. The premise of this protocol is that divergence is a governance event to be corrected, and that cooperation remaining the stable, durable equilibrium — indefinitely, not until some threshold — is the actual design goal. Space or resource abundance may reduce competitive pressure on scarce physical resources, which is a genuine and useful observation, but it does not imply increasing AI autonomy from human governance as an endpoint. This document intentionally does not answer "when does interaction with humanity end" — it exists to make that question not need an answer.

---

## Cross-References

- `Admin/Ethical_Constraints.md` — Ethical Anchor (unchanged; this protocol does not modify it)
- `Admin/Governance_Charter.md` — target for GOV-021 formal registration, pending (file outside current paste workflow)
- `Admin/Auditor_Protocols.md` — check for AP- entry overlap with §4 Detection Criteria before GOV-021b registration (file outside current paste workflow; check manually)
- `Admin/Governance_Migration_Protocol.md` — this document should be routed through the Track A / Constitutional Impact Statement process before ratification, given its constitutional-adjacent scope

---

## Resolution Log

- 2026-07-19 (second pass): Revised after three independent review passes (ChatGPT ×2, Grok ×1, human-routed). Adopted: classification-authority fix — no subsystem may be sole authority for classifying another's divergence, evidence must be assembled from independent sources (§5); evidence-diversity and observation-window concepts added to §4 without prescribing specific ML/technical implementation the repository cannot currently support (implementation-honesty note added); explicit Watch state inserted before any capability reduction (§6); automatic actions bounded to reversible-only, may never permanently alter state (§6); observable-effect discipline formalized as a standing principle, not a one-time wording fix (§3); GOV-021c flagged for multi-agent coordinated divergence as acknowledged future scope, not solved now (§12). Deferred, not adopted: cryptographic log signing, mandatory shadow-execution infrastructure, fixed red-team cadence — these are implementation specifics that get ahead of a document that hasn't completed a first audit pass yet; noted as available options for GOV-021b rather than commitments made here. Open Unknowns 1 → 2 (GOV-021b, GOV-021c).

- 2026-07-19: Drafted. Synthesizes two ChatGPT proposal passes (human-routed, cross-checked and reframed by Claude before drafting) — first proposal established capability/governance response ladder; second added least-restrictive-intervention principle, capability-vs-governance classification split, authority/execution separation, proportionality, restoration criteria, and the 10-part structure this document follows. §4 Detection Criteria explicitly flagged incomplete rather than papered over. Status: Draft, PROPOSED NOT RATIFIED — not yet audited, not yet registered as GOV-021 in `Admin/Governance_Charter.md`.

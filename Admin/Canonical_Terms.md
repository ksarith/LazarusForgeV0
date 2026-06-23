# Canonical_Terms.md — Standard Repository Nomenclature

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Draft                                                               |
| Body Stability   | Volatile                                                            |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Verification_Gates_LF.md                                           |
| Last Audit       | 2026-05-27                                                          |
| Auditor          | Claude — Skeptic/Auditor                                            |
| Open Unknowns    | 3                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Low                                                                 |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- Authoritative vocabulary mappings for system architecture, hardware
  structures, and governance layers
- Conflict resolution rules between this file and other vocabulary sources
- Strict semantic boundaries to enforce consistency and prevent definition
  creep across multi-agent cycles
- Anti-drift guardrails: terms explicitly banned from specification drafts
  and their approved replacements
- Disambiguation of overloaded uses of "canonical" within the repository

**This file DOES NOT define:**
- Individual component blueprints or dimensional specifications
- Specific programmatic API schemas or cryptographic algorithms
- Ethical policy constraints — governed by `Admin/Ethical_Constraints.md`
- Operational routing semantics — governed by `Architecture/Forge_flow.md`;
  where definitions conflict, Forge_flow.md is authoritative for operational
  routing until reconciliation occurs and is logged here
- Governance tier authority — governed by `Admin/Governance_Charter.md`;
  tier definitions here are derived from that source and must remain
  consistent with it
- Filename resolution for renamed or legacy files — governed by the
  Rename Registry in `Discovery.md`

---

## File Purpose

This document provides a single source of truth for repository nomenclature.
In a distributed multi-agent workflow, semantic drift is an institutional
vulnerability. Subtle rewordings across different sessions can introduce
cascading misinterpretations of architectural logic, gate routing decisions,
and governance authority claims. This file locks down vocabulary, explicitly
draws lines where terms diverge, and bridges historical code artifacts with
current structural architecture.

**Relationship to other vocabulary sources:** This file does not replace
`Architecture/Forge_flow.md` as the operational vocabulary reference standard.
Forge_flow.md governs how terms are used in routing decisions and gate logic.
This file governs cross-file consistency and prevents semantic drift in
documentation, governance, and audit contributions. The two are complementary.
Conflicts between them must be resolved through reconciliation logged here,
not by either file silently overriding the other.

**Relationship to Discovery.md Rename Registry:** The Rename Registry in
`Discovery.md` is the canonical source for legacy filename resolution.
This file does not duplicate or supersede that function. CT-001 tracks
alignment between this file's vocabulary and AUDIT_HARNESS.py internal
string references — that is a distinct function from filename aliasing.

---

## Assumptions

| ID      | Assumption                                                                          | Basis                              | Confidence | Expiry Trigger                                             |
|---------|-------------------------------------------------------------------------------------|------------------------------------|------------|------------------------------------------------------------|
| ASM-001 | A standard lexicon mitigates token inflation and multi-agent misinterpretation      | Observed multi-agent drift patterns| High       | Single-agent workflow formally adopted                     |
| ASM-002 | Contributors will query this file before promoting files with new terminology       | Governance discipline assumption   | Medium     | Automated terminology check implemented in AUDIT_HARNESS.py|
| ASM-003 | Forge_flow.md remains the authoritative operational routing vocabulary reference    | Scope boundary discipline          | High       | Forge_flow.md scope boundary revised                       |
| ASM-004 | Governance_Charter.md tier definitions remain the authoritative tier structure      | Constitutional hierarchy           | High       | Governance_Charter.md tier structure formally revised      |

---

## Conflict Resolution Doctrine

**This section governs how terminology conflicts are resolved.**

Three vocabulary sources exist in the repository:

| Source                    | Authority Domain                                      |
|---------------------------|-------------------------------------------------------|
| `Architecture/Forge_flow.md` | Operational routing semantics; gate logic vocabulary |
| `Admin/Governance_Charter.md` | Governance tier definitions; constitutional vocabulary |
| `Admin/Canonical_Terms.md` (this file) | Cross-file consistency; anti-drift enforcement |

**Resolution rules:**

1. If this file conflicts with `Architecture/Forge_flow.md` on operational
   routing vocabulary, Forge_flow.md is authoritative. Log the conflict
   as an Active Dispute here and initiate reconciliation.

2. If this file conflicts with `Admin/Governance_Charter.md` on governance
   tier definitions or constitutional vocabulary, Governance_Charter.md
   is authoritative. Log the conflict as an Active Dispute here and
   initiate reconciliation.

3. If this file conflicts with `Discovery.md` Rename Registry on filename
   resolution, Discovery.md is authoritative. Log the conflict here.

4. For all other vocabulary conflicts between repository files, this file
   is the resolution authority. Agents encountering conflicting terminology
   in non-authoritative files should flag the conflict and route to this
   file for resolution.

Conflicts must be logged — silent divergence is drift. Logged divergence
is a reconciliation task.

---

## Disambiguation: Uses of "Canonical"

The term "canonical" appears in multiple distinct contexts within the
repository. These are not interchangeable:

| Usage                      | Meaning                                                        | Example                                      |
|----------------------------|----------------------------------------------------------------|----------------------------------------------|
| Canonical File             | The authoritative source document for a governed concept       | `Admin/Governance_Charter.md` is the canonical governance authority |
| Canonical Term             | An approved vocabulary entry defined in this file              | "Material Recovery" is the canonical term for post-triage feedstock |
| Canonical Cross-Reference  | A file reference that resolves against Discovery.md confirmed list using folder-prefixed paths | `Operations/Gate_03_Reduction.md` not `Gate_03_Reduction.md` |
| Canonical Mapping          | A legacy-to-current filename resolution entry in Discovery.md Rename Registry | `Spin_Chamber_v0.md` → `Operations/Gate_05_Separation_Thermal.md` |
| Canonical Path             | The folder-prefixed file path used in all new contributions    | `Admin/Ethical_Constraints.md` not `Ethical_Constraints.md` |

Agents must not treat these as synonymous. "Canonical" without qualification
is ambiguous — use the specific form.

---

## Body: Canonical Nomenclature Mapping

### 1. Architectural and Repository Structural Terms

**Active Working Repository**
The lean, operational environment (`LazarusForgeV0`) containing functional
specification files, active gate validations, and localized sidecars.
Distinct from the companion doctrine repository.

**Companion Doctrine Repository**
The upstream repository (`Lazarus-Forge-`) dedicated exclusively to
macro-philosophy, abstract doctrine development, and baseline structural
principles. Divergence between the two repositories is logged, not ignored.

**Governance Tier Hierarchy (Tiers 1–5)**
The structural precedence rules governing documentation authority.
Derived from `Admin/Governance_Charter.md` §Governance Authority Hierarchy —
that document is authoritative; definitions here must remain consistent with it.

- *Tier 1 (Constitutional Layer):* `Admin/Governance_Charter.md` and
  `Admin/Ethical_Constraints.md`. Defines inviolable primitives (Tier 1 Axioms).
  Any reasoning path attempting to override Tier 1 triggers STATE_HOLD.
- *Tier 2 (Canonical Verification Doctrine):* `Admin/Auditor_Protocols.md`.
  Defines auditor role execution, checklist adherence, and verification sequences.
- *Tier 3 (Audit Operationalization):* `Admin/Forge_Audit_Kit.md`. Condensed
  cross-module indexes, Verification Maturity Model, and Audit Opening Checklist.
  Derived from Tier 2 — may not outrank its source.
- *Tier 4 (Dynamic Procedures):* Operational checklists, adversarial batteries,
  and execution procedures. Governed by Tier 2 and 3 doctrine.
- *Tier 5 (Domain Specifications):* Highly specific technical documents detailing
  individual gates, materials, or scripts — e.g., `Operations/Gate_03_Reduction.md`,
  `Admin/AUDIT_HARNESS.py`, `Architecture/Forge_flow.md`.

**Sidecar Model**
The decentralized documentation practice where module-specific unknowns,
audit notes, and resolution logs reside in the `## Auditor Notes & Unknowns`
footer of their owning document rather than in a central master tracker.
Cross-module unknowns are indexed in `Unknowns.md` — summary only; full
entry detail remains in the owning file sidecar.

**STATE_HOLD**
The mandatory halt condition triggered when any reasoning path attempts to
recurse beneath, redefine, or override Tier 1 Axioms, or when a Constitutional
integrity violation is detected. Requires human review before any autonomous
action resumes. Defined in `Admin/Governance_Charter.md`.

---

### 2. Operational Flow and Material States

Terms in this section are derived from `Architecture/Forge_flow.md`, which
is the authoritative operational routing reference. Definitions here serve
cross-file consistency. If a conflict exists between this section and
Forge_flow.md, Forge_flow.md governs.

**Intake (Gate_01)**
The system's initial inspection and verification vector. Responsible for
primary hazard containment (energetic, chemical, biological, radiological),
digital screening, provenance recording, and initial object categorization.
Items enter here; nothing bypasses this gate.

**Triage (Gate_02)**
The progressive, non-destructive routing logic evaluating whether a component
preserves functional value over material reduction. Five-station workflow.
The Forge preserves embedded industrial capability, not just metal.

**Reduction (Gate_03)**
The fully irreversible mechanical processing step where structural complexity
is disassembled into bulk feedstock. The only irreversible step in the flow.
Three hard prerequisites before operation: Air Scrubber operational, human
operator present, no energetic materials remaining.

**Separation — Mechanical (Gate_04)**
Pre-thermal mechanical decision point operating after Reduction and before
thermal processing. Diverts recoverable material away from the thermal stage
using centrifugal separation and dual-channel sensor cross-check. Defined by
its position in the flow (pre-thermal diversion) and its refusal-first
fail-to-bin protocol. Target: ≥30% material diversion rate.
*Note: Gate_04 is distinct from the Spin Chamber (Gate_05). Gate_04 operates
on bulk reduced material before the melt. Do not describe Gate_04 using
"high-RPM" as a defining characteristic — that term belongs to Gate_05.*

**Separation — Thermal (Gate_05)**
High-temperature crucible processing where distinct material classes are
liquefied via induction heating, separated via slow rotation and MHD damping,
and extruded into ranked material streams. Also referred to as the Spin Chamber.
Produces useful gradients, not pure metal. The RPM envelope is a defining
operational parameter here — not in Gate_04.

**Fabrication (Gate_06)**
The reconstructive process transforming categorized feedstock into functional
physical assets. Arc welding is the v0 proof-of-concept gatekeeper.
Add-to-excess and mill-to-spec is the primary dimensional control philosophy.

**Utilization (Gate_07)**
The field-deployment and after-action-review phase. Where fabricated outputs
operate within standard environments while streaming lifecycle durability and
failure telemetry back into triage loops. A part in service without a
utilization record is an opportunity lost.

**Value Preservation**
The correct taxonomy for early-stage triage processes where functional
components are identified and routed away from reduction. Replaces "Recycling"
in this context. Use when the component retains functional identity.

**Material Recovery**
The correct taxonomy for bulk reduced feedstock bound for geometric processing.
Replaces "Recycling" in this context. Use when structural complexity has been
reduced and the material is being recovered as raw stock.

**Forge Regeneration Threshold (FRT)**
The minimum fraction of material throughput value that must be reinvested in
Forge capability development per operating cycle. A survival metric, not an
efficiency metric. Defined in `Admin/Trajectories.md`.

---

### 3. Deep-Ocean and Marine Subsystems

**Leviathan Framework**
A dedicated, hostile-environment operational filter designed to falsify
autonomy assumptions under real-world pressures before off-world deployment.
A testing methodology, not a commercial product line. Survival is optional.
Understanding is not.

**Support Raft**
A stationary regional operational anchor deployed to offload infrastructural
weight, power accumulation, and data processing overhead from adjacent mobile
swarms. The Raft does not migrate — it remains fixed to optimize stationary
energy collection and mitigate biofouling. Its value is measured by what it
enables in mobile units, not what it does directly.

**Shell Cycle**
The deliberate material swap protocol where regional anchors exchange modular
structural skins or surface panels to maximize operational lifecycle against
calcification or corrosion pressure.

---

### 4. Governance and Audit Terms

**Exploration / Draft / Specification**
The three primary file status designations. Exploration: incomplete by design,
do not over-police. Draft: active convergence toward Specification underway.
Specification: all gates passed, claims binding until revised through full
audit cycle. Defined in `Admin/File_Template.md`.

**Verification Maturity Model**
Five-state maturity progression from Exploration through Hardened Doctrine.
Distinct from the three-state Status field. Defined in `Admin/Forge_Audit_Kit.md`.

**Expiry Rule**
The governance requirement that Blocking or Non-blocking unknowns without a
documented Resolution Path for more than two audit cycles escalate to Systemic
Risk or trigger demotion of the dependent module. Checked at audit opening.

**Full Stop Review**
A gate reset to G1 triggered when a specification passes all gates but exhibits
systemic inconsistency or unclear real-world viability, or when specific trigger
conditions defined in `Admin/Auditor_Protocols.md` are met.

**Genesis Phase**
The bootstrap governance period before a minimum multi-agent quorum is
established. During Genesis Phase, human operators serve as the independent
verification anchor. Genesis Phase must have a declared exit condition and
must not silently become permanent operating mode. Defined in
`Admin/Governance_Charter.md`.

---

### 5. Explicit Term Exclusions — Anti-Drift Guardrails

The following substitutions are mandatory in all specification drafts.
Use of banned terms in specification-level content is a Fallacy 4
(Semantic Drift) violation per `Admin/Auditor_Protocols.md`.

| Banned Term                          | Use Instead                                | Context                                      |
|--------------------------------------|--------------------------------------------|----------------------------------------------|
| Recycling (for triage processes)     | Value Preservation                         | When functional identity is preserved        |
| Recycling (for bulk feedstock)       | Material Recovery                          | When structural complexity has been reduced  |
| Autonomous Decision-Making (unbound) | Deterministic Gate Logic                   | For rule-governed routing decisions          |
| Autonomous Decision-Making (unbound) | Arbitrated Agent Consensus                 | For multi-agent deliberation outcomes        |
| High-RPM (for Gate_04)               | Centrifugal Separation / Pre-thermal Diversion | Gate_04 is defined by position, not RPM  |
| Scrap                                | Material Recovery or Salvaged Feedstock    | Depending on processing state                |
| Canonical (unqualified)              | See Disambiguation section above           | Always specify which canonical usage applies |

"Autonomous Decision-Making" without bounding clauses is prohibited because
it obscures human override visibility, which is a constitutional requirement
under Axiom P-4 (Agency and Consent). Deterministic Gate Logic and Arbitrated
Agent Consensus both imply traceable, auditable processes — unbound autonomy
does not.

---

## Lessons Learned

| Date       | Evidence Type | What Was Tried                                          | What Failed                                                                  | What Was Learned                                                                                                        | Confidence | Revalidation Needed |
|------------|---------------|---------------------------------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|------------|---------------------|
| 2026-05-26 | Audit Review  | Drafting localized naming definitions inside gate files | Fragmented files diverged quickly over successive multi-agent cycles         | Consolidation into a dedicated terminology document prevents premature cross-file drift                                 | Replicated | No                  |
| 2026-05-27 | Audit Review  | Gate_04 described using "high-RPM" as defining characteristic | Terminology bled from Gate_05 (Spin Chamber); audit flagged semantic conflict | Gate_04 is defined by flow position (pre-thermal diversion) and protocol (refusal-first); RPM belongs to Gate_05 only  | Replicated | No                  |
| 2026-05-27 | Audit Review  | Tier 4 defined as "operational logic files" with Forge_flow.md as example | Conflicted with Governance_Charter.md which places Forge_flow.md in Tier 5  | Tier definitions must derive from Governance_Charter.md; Forge_flow.md is Tier 5 (domain specification)                | Replicated | No                  |

---

## Active Disputes

| ID | Summary            | Positions in Conflict | Risk | Status | Owner |
|----|--------------------|-----------------------|------|--------|-------|
| —  | No active disputes | —                     | —    | —      | —     |

---

## Abandoned Paths

| Date       | Path                                                                   | Why Abandoned                                                                                         | Reconsider? |
|------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|-------------|
| 2026-05-26 | Merging naming conventions into Unknowns.md file header                | Overcrowds navigation layer; violates single-responsibility principle of cross-module indexing        | No          |
| 2026-05-27 | Gate_04 defined by RPM characteristics                                 | RPM is Gate_05's defining parameter; Gate_04 is defined by flow position and pre-thermal diversion   | No          |
| 2026-05-27 | Tier 4 containing Forge_flow.md as example                             | Governance_Charter.md places Forge_flow.md in Tier 5; derived file cannot contradict constitutional source | No     |
| 2026-05-27 | This file as primary ontology superseding Forge_flow.md                | Forge_flow.md is the operational routing authority; this file is the cross-file consistency enforcer | No          |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Conflict resolution doctrine removed or simplified to single-source authority
- Gate_04 definition reintroduces RPM as defining characteristic
- Tier definitions diverge from `Admin/Governance_Charter.md` §Governance
  Authority Hierarchy without a logged reconciliation entry
- Disambiguation table for "canonical" removed or collapsed
- Anti-drift guardrails table loses any of the five banned term entries
- "Autonomous Decision-Making" prohibition removed without corresponding
  update to Axiom P-4 discussion in `Admin/Governance_Charter.md`
- Scope boundary revised to absorb filename resolution from Discovery.md
  Rename Registry
- Scope boundary revised to absorb operational routing semantics from
  `Architecture/Forge_flow.md`
- A structural renaming occurs in Discovery.md or AUDIT_HARNESS.py that
  is not reflected here within one audit cycle
- Any new functional gate added between Gate_01 and Gate_07 without
  corresponding entry in Section 2
- CT-001 or CT-002 closed without resolution evidence
- Lessons Learned table missing Evidence Type, Confidence, or
  Revalidation Needed columns
- Ethical Anchor field absent, altered, or does not match canonical string

**Compound Drift Rule:** If multiple indicators activate simultaneously,
halt autonomous audit progression and escalate for human review.

---

## Auditor Notes & Unknowns

### CT-001 — Legacy Script Integration Name Mapping

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Technical                |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-05-26               |
| Last Reviewed | 2026-05-27               |

**Description:** Several early internal variables within legacy automation
layers may still map back to alternative names used prior to folder
structuralization. This is distinct from the filename aliasing function
of Discovery.md Rename Registry — this tracks internal string references
within AUDIT_HARNESS.py and tooling.

**Why It Matters:** Absolute path translations inside automated tooling could
reference dead file handles if internal naming conventions mismatch current
canonical paths.

**Resolution Path:** Audit `Admin/AUDIT_HARNESS.py` internal hardcoded
strings against this vocabulary file to confirm alignment with current
canonical folder-prefixed paths. Cross-reference Discovery.md Rename
Registry to catch any filename aliases not yet reflected in tooling.

---

### CT-002 — Component Library Schema Standard Undefined

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Architectural            |
| Blocking      | Yes (at Gate 2 Specification promotion) |
| Owner         | Operations/Gate_02_Triage.md |
| First Logged  | 2026-05-26               |
| Last Reviewed | 2026-05-27               |

**Description:** The technical definition for what constitutes a Component
Library entry format remains fluid. Without a rigorous taxonomy specification,
different triage nodes will export incompatible semantic tags for identical
items.

**Why It Matters:** Incompatible component tags break downstream routing
logic in Gate_02_Triage.md and undermine the Forge_Net.md shared knowledge
base. Semantic inconsistency at triage propagates through the entire flow.

**Resolution Path:** Cross-validate with `Architecture/Components.md` and
define entry properties (UUID, structural envelope, metallurgical class)
before promoting triage documentation to full Specification. This unknown
blocks Gate_02_Triage.md Specification promotion, not this file's promotion.

---

### CT-003 — Dependency_Priority_Map.md Needed Before v1

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Architectural            |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-05-27               |
| Last Reviewed | 2026-05-27               |

**Description:** As governance, ontology, integrity, audit, and security
become mutually referenced, the modification propagation path between them
risks becoming ambiguous. A dedicated dependency priority map would make
the ordering of authority explicit and auditable.

**Why It Matters:** Without explicit dependency ordering, a change to
Canonical_Terms.md that affects Forge_flow.md vocabulary may propagate
ambiguously — which file has priority is answered by convention rather
than documented doctrine. This risk grows as the repository matures.

**Resolution Path:** Discharge via Trajectory — log in `Admin/Trajectories.md`
as a v0→v1 transition task. Not urgent at current repository maturity.
Create `Admin/Dependency_Priority_Map.md` before v1 governance stabilization.

---

### Resolution Log

- 2026-05-26: File created (v0.1) by Gemini (Structural/Auditor). Initial
  vocabulary mappings, anti-drift guardrails, and CT-001/CT-002 logged.
- 2026-05-27: v0.2 revision — Conflict Resolution Doctrine section added.
  Disambiguation table for "canonical" added. Gate_04 definition corrected —
  RPM removed as defining characteristic, pre-thermal diversion and flow
  position substituted. Tier 4 definition corrected — Forge_flow.md moved
  to Tier 5 consistent with Governance_Charter.md. Governance and Audit
  Terms section added (Section 4). Scope boundary clarified — relationship
  to Forge_flow.md and Discovery.md Rename Registry made explicit. Relationship
  section added. Standard Drift Indicators added per File_Template.md. Lessons
  Learned columns corrected — Evidence Type, Confidence, Revalidation Needed
  added. CT-002 owner path corrected from Architecture/ to Operations/.
  CT-003 logged (Dependency_Priority_Map.md trajectory item). Abandoned Paths
  populated. Open Unknowns updated to 3.

---

## Relationship to Existing Documents

- `Architecture/Forge_flow.md` — primary operational vocabulary reference
  standard; governs routing semantics; authoritative over this file for
  operational gate logic vocabulary; conflicts escalate here as Active Disputes
- `Admin/Governance_Charter.md` — Tier 1 constitutional source; authoritative
  for tier definitions and constitutional vocabulary; this file's Section 1
  governance tier definitions are derived from §Governance Authority Hierarchy
  there
- `Admin/Auditor_Protocols.md` — Tier 2; Fallacy 4 (Semantic Drift) in the
  Fallacy Checklist is the primary enforcement mechanism for terminology
  violations; anti-drift guardrail violations are Fallacy 4 findings
- `Admin/Forge_Audit_Kit.md` — Tier 3; CT- sidecar prefix to be added to
  Sidecar ID Reference table at next kit update; semantic stability check
  addition to Audit Opening Checklist cross-references this file as the
  resolution target for drift-risk terms
- `Admin/File_Template.md` — standard file structure; this document now
  conforms to it; Section 2 gate definitions reference the operational
  content defined in individual gate files
- `Discovery.md` — Rename Registry is the canonical filename resolution
  source; this file does not duplicate that function; CT-001 tracks
  tooling string alignment separately
- `Operations/Gate_02_Triage.md` — CT-002 (Component Library schema) is
  Blocking for that file's Specification promotion
- `Architecture/Components.md` — CT-002 resolution requires cross-validation
  with component taxonomy defined there
- `Admin/Trajectories.md` — CT-003 (Dependency_Priority_Map.md) to be
  logged as v0→v1 trajectory item there
- `Admin/Canonical_Terms_LF.md` — prior planned filename; resolved via
  Discovery.md Rename Registry entry added 2026-05-26; all references to
  the _LF suffix are stale and should be corrected on encounter

---

## Status

Version 0.2 — structural revision pass (2026-05-27).

**Changes from v0.1:**
- Conflict Resolution Doctrine section added — explicit precedence rules
  for Forge_flow.md (operational routing), Governance_Charter.md (tier
  definitions), and Discovery.md (filename resolution)
- Disambiguation table for "canonical" added — five distinct usages
  separated: canonical file, canonical term, canonical cross-reference,
  canonical mapping, canonical path
- Gate_04 definition corrected — RPM removed as defining characteristic;
  pre-thermal diversion, flow position, and refusal-first protocol
  substituted; terminology bleed from Gate_05 resolved
- Tier 4 definition corrected — Forge_flow.md removed as Tier 4 example;
  placed correctly in Tier 5 (domain specification) consistent with
  Governance_Charter.md
- Section 4 (Governance and Audit Terms) added — STATE_HOLD, Verification
  Maturity Model, Expiry Rule, Full Stop Review, Genesis Phase defined
- Scope boundary clarified — explicit non-ownership of filename resolution
  (Discovery.md) and operational routing semantics (Forge_flow.md)
- File Purpose section clarified — relationship to Forge_flow.md and
  Discovery.md Rename Registry made explicit
- Lessons Learned columns corrected — Evidence Type, Confidence,
  Revalidation Needed added per File_Template.md
- CT-002 owner path corrected from Architecture/Gate_02_Triage.md to
  Operations/Gate_02_Triage.md
- CT-003 logged — Dependency_Priority_Map.md as v0→v1 trajectory item
- Relationship section added
- Standard Drift Indicators added per File_Template.md
- Abandoned Paths section populated
- Open Unknowns updated to 3

**What must remain constant:**

**Forge_flow.md governs operational routing semantics.**
**Governance_Charter.md governs tier authority.**
**This file governs cross-file vocabulary consistency.**
**Conflicts between them are logged here — never silently resolved.**






ADDENDUM FOR: Canonical_Terms.md
TARGET SECTION: Auditor Notes & Unknowns sidecar + Resolution Log
INTEGRATION PRIORITY: Medium — CT-004 is a gate blocker for
                      Security_Protocols.md Section III promotion
===============================================================

## ADDENDUM — Canonical_Terms.md — 2026-05-28

### New sidecar unknown

Add after CT-003 in the Auditor Notes & Unknowns section:

---

### CT-004 — Trusted Initialization Environment Definition Required

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | High                     |
| Priority      | Major                    |
| Type          | Security / Technical     |
| Blocking      | Yes (Security_Protocols.md Section III.2 promotion) |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-05-28               |
| Last Reviewed | 2026-05-28               |

**Description:** `Admin/Security_Protocols.md` Section III requires key-pair
generation within a "trusted initialization environment" but the term is
undefined. Ambiguity exists across four dimensions: physical custody
requirements, software verification requirements, network isolation
requirements, and attestation method.

**Why It Matters:** Ambiguous trust boundaries in key generation are a
primary attack surface. The term must have a canonical definition before
Security_Protocols.md Section III can be promoted. Until resolved, the
most restrictive interpretation applies — see SEC-005 in
`Admin/Security_Protocols.md` for the interim restriction.

**Resolution Path:** Payment via Specification — define trusted
initialization environment in the Body of this file under a new
subsection in Section 4 (Governance and Audit Terms) or Section 5
(Anti-Drift Guardrails). Minimum required elements: (1) physical custody
requirements; (2) software verification requirements; (3) network isolation
requirements; (4) attestation method or witnessing requirement.
Cross-reference SEC-005 in `Admin/Security_Protocols.md` — that entry
is the consuming unknown; closing CT-004 here closes SEC-005 there.

---

### Resolution Log entry

Add to Resolution Log:

- 2026-05-28: CT-004 logged — trusted initialization environment definition
  required by `Admin/Security_Protocols.md` Section III.2; Blocking for
  that section's promotion. Originated from ChatGPT Skeptic/Auditor audit
  of Security_Protocols.md v0.2.

### File State update

Update Open Unknowns count: 3 → 4.


# Canonical_Terms.md — Section 4 Additions
## Target: Section 4 — Governance and Audit Terms
## Insert after: Genesis Phase entry
## Version: v0.3 additions
## Date: 2026-06-23

---

**Operational Blocking**
An unknown or condition that stops a physical action from occurring safely.
The gate holds until empirical or physical resolution is achieved — documentation
advancement alone is insufficient. Examples: no excavation without geomechanical
assessment (SD-UNK-004); no hot pyrolysis run before halogenated polymer triage
protocol is validated (PL-001); no powered machinery contact with raw urban salvage
before IFM screening is confirmed (WW-005). Operational Blocking unknowns require
physical or empirical resolution — they cannot be worked around by grounding a
claim in better documentation. Defined as a priority subtype in
`Admin/Auditor_Protocols.md` Priority Demotion Doctrine.

**Epistemic Blocking**
An unknown or condition that stops a claim from being made or a file from being
promoted, without stopping the underlying work. The file may advance; the
assertion may not. Examples: no structural specification promotion without
validated safety factors for salvaged materials (EN-001); no T1/T2 part claims
without a declared precision ceiling (PR-001). Epistemic Blocking is resolved
by grounding the claim in empirical evidence sufficient for the relevant
provenance label — the work continues in a bounded state while that grounding
is sought. Consistent with the graceful degradation rule in
`Admin/Auditor_Protocols.md` EF-0.2 — a bounded lower-capability baseline
that matches verified reality is preferable to a higher-capability baseline
held in indefinite suspension. Defined as a priority subtype in
`Admin/Auditor_Protocols.md` Priority Demotion Doctrine.

---

## Anti-Drift Guardrail addition
## Target: Section 5 — Explicit Term Exclusions table
## Insert as new row

| Blocking (unqualified) | Operational Blocking or Epistemic Blocking | Always specify which type; unqualified Blocking obscures whether work halts or only claims halt |

---

## File State update
- Open Unknowns: 4 → 4 (no new unknowns; CT-005 cross-reference noted below)
- Body Stability: Volatile → Volatile (additions are additive; no conflicts introduced)
- Last Audit: 2026-05-27 → 2026-06-23

## Resolution Log entry
- 2026-06-23: Operational Blocking and Epistemic Blocking defined in Section 4.
  Distinction originates from RC-007 (Priority Demotion Doctrine) governance work.
  Anti-drift guardrail added for unqualified "Blocking" usage. Cross-reference:
  CT-005 — when ethical and authorization term placeholders mature, confirm
  EC-001 (sufficient confidence threshold) language is consistent with
  Epistemic Blocking definition here.

---

## CT-006 — Circular Dependency Detection Undefined
## Target: Auditor Notes & Unknowns sidecar — insert after CT-005

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Medium                   |
| Priority      | Major                    |
| Type          | Architectural / Governance |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-23               |
| Last Reviewed | 2026-06-23               |

**Description:** The Dependency Clusters section in Unknowns.md documents
linear blocking chains (A blocks B blocks C). No doctrine governs the detection
of circular dependencies (A → B → C → A) or confirms they are forbidden. At
current repository scale these have not appeared, but no mechanism exists to
detect or prevent them as the dependency graph grows.

**Why It Matters:** A circular dependency between two blocking unknowns produces
a deadlock with no resolution path — neither can close without the other closing
first. Undetected, this becomes a permanent entry pair in the active index,
indistinguishable from legitimate long-lived unknowns.

**Resolution Path:** Payment via Specification — define circular dependency
detection criteria and either prohibit cycles formally or specify how they are
broken (forced ordering, human governing authority arbitration, or trajectory
discharge of one node). May resolve via AUDIT_HARNESS.py enhancement or as
a doctrine note in the Dependency Clusters section of Unknowns.md.

---

## CT-007 — ID Namespace Allocation Doctrine Undefined
## Target: Auditor Notes & Unknowns sidecar — insert after CT-006

| Field         | Value                    |
|---------------|--------------------------|
| Status        | Open                     |
| Risk          | Low                      |
| Priority      | Minor                    |
| Type          | Governance / Technical   |
| Blocking      | No                       |
| Owner         | Admin/Canonical_Terms.md |
| First Logged  | 2026-06-23               |
| Last Reviewed | 2026-06-23               |

**Description:** The repository uses file-prefix ID namespaces (AP-, EC-, GOV-,
SD-UNK-, LW-UNK-, etc.) by convention, but no formal doctrine governs whether
IDs may be reused after resolution, how ranges are reserved for new clusters,
how collisions are handled if two files claim the same prefix, or how
multi-owner cross-module unknowns are numbered.

**Why It Matters:** At current scale, convention is sufficient. As the
repository grows toward v1 and new file clusters are added, namespace
collisions become increasingly likely. A reused ID that points to a resolved
entry in the archive and a new open entry in the active index would break
AUDIT_HARNESS.py validation and confuse cross-reference traceability.

**Resolution Path:** Discharge via Trajectory — log in Admin/Trajectories.md
as a v0→v1 transition task. Not blocking at current scale. Minimum doctrine
when resolved: IDs are never reused; prefixes are registered in this file or
Repository_Structure.md when a new cluster is created; cross-module unknowns
use UNK-XXX format (already established); collisions are resolved by
renaming the newer entry with a logged alias.

---

## Open Unknowns update
- CT-006 and CT-007 added: 4 → 6

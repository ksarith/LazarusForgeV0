# Cognitive_Salvage_Layer.md
**Version 0.1**

## File State

| Field            | Value                                                               |
|------------------|---------------------------------------------------------------------|
| Status           | Exploration                                                         |
| Body Stability   | Draft                                                               |
| Spec Gates       | 0/6                                                                 |
| Verification Ref | Admin/Verification_Gates_LF.md                                      |
| Last Audit       | 2026-06-24                                                          |
| Auditor          | Claude — Synthesizer/Auditor                                        |
| Open Unknowns    | 5                                                                   |
| Active Disputes  | 0                                                                   |
| Highest Risk     | Medium                                                              |
| Sidecar Link     | #auditor-notes--unknowns                                            |
| Ethical Anchor   | Attempt to do no harm. Defer to Ethical_Constraints.md if present. |

---

## Scope Boundary

**This file DOES define:**
- The Cognitive Salvage Layer as a distinct architectural module within LazarusForgeV0
- The heuristic failure class that motivates human-in-the-loop integration
- The feedback loop architecture from physical scan to autonomous execution
- The Auditor Decision Tree for candidate heuristic verification (Stages 1–4)
- The five-status grading classification matrix
- The Heuristic Object schema for telemetry and logging
- Integration points with existing Forge modules
- The Leviathan emergency cognition connection
- GH-series unknowns governing heuristic governance architecture

**This file DOES NOT define:**
- Game design, player experience, or interface specifications
- Puzzle generation algorithms or procedural content systems
- Robotic arm kinematic models or IK solver implementations
- Finite element analysis methodology or FEA toolchain selection
- Forge_Net.md federated knowledge base architecture
- Auditor protocol operational behavior (→ `Admin/Auditor_Protocols.md`)
- Canonical terminology (→ `Admin/Canonical_Terms.md`)
- Leviathan deployment architecture (→ `Operations/Leviathan.md` — planned)

---

## File Purpose

This file defines the **Cognitive Salvage Layer**: a human-in-the-loop heuristic harvesting pipeline that converts player-solved spatial and triage puzzles into verified, machine-executable protocols for the Lazarus Forge.

The layer exists to address a specific and underserved failure class: **heuristic failure**. This is distinct from sensor failure and mechanical failure. In a heuristic failure, the object is technically visible, the materials are technically identifiable, and the machine technically has the tools — yet the system does not know which bolt to remove first, which cut avoids structural collapse, which sequence minimizes contamination spread, or which edge-case exploitation is worth attempting. These are problems humans solve extraordinarily well.

The game interface is not the product. **The heuristic extraction pipeline is the product.**

By treating player-generated solution paths as untrusted candidate heuristics — and subjecting them to the same verification discipline applied to all Forge knowledge — this layer extends the Forge's core salvage-first doctrine from physical materials to human cognition itself:

> Human problem-solving effort is itself a salvageable resource.

Just as the Forge assumes that discarded materials contain unrealized value, the Cognitive Salvage Layer assumes that millions of hours of distributed human puzzle-solving contain recoverable operational knowledge — provided the extraction and verification pipeline is rigorous enough to separate genuine insight from game-engine artifact.

---

## Assumptions

| ID      | Assumption                                                                              | Basis                                | Confidence  | Expiry Trigger                                          |
|---------|-----------------------------------------------------------------------------------------|--------------------------------------|-------------|---------------------------------------------------------|
| CSL-A01 | Heuristic failures represent a meaningful fraction of Forge operational bottlenecks     | Analogous salvage system behavior    | Analogous   | Operational data from first Leviathan deployment cycles |
| CSL-A02 | Human spatial reasoning reliably surfaces solution paths that autonomous planning misses | Analogous (Foldit, protein folding)  | Analogous   | GH-001 resolution via empirical testing                 |
| CSL-A03 | A gamified interface can abstract real salvage geometry with sufficient fidelity         | Placeholder — no Forge-specific data | Placeholder | Stage 3 validation pass on first physical anomaly       |
| CSL-A04 | The Forge's existing Auditor Protocols are sufficient to gate heuristic promotion        | Internally Derived                   | PROVISIONAL | GH-003 (adversarial poisoning) resolution               |
| CSL-A05 | Players will not systematically attempt to poison the heuristic dataset                 | Placeholder — no deployment data     | Placeholder | GH-003 resolution                                       |

---

## The Heuristic Failure Class

Standard Forge operational flow assumes:

1. Material enters the system.
2. Sensors classify it.
3. Agents decide what to do.
4. Machinery executes.

This flow handles the common case well. It fails silently on a specific class of problem where the sensor and classification layers return valid data but the planning layer lacks the procedural knowledge to act optimally — or at all. Examples:

- A structurally deformed hull section where standard disassembly sequence causes tool-pinching collapse.
- A biofouled assembly where cut order determines whether contamination spreads to clean components.
- A non-standard geometry where bolt removal priority is load-bearing and non-obvious.
- An edge-case material state (severe corrosion, fused joints, unexpected composites) outside the planning agent's training distribution.

These are not failures of sensing or execution. They are failures of procedural knowledge. The Cognitive Salvage Layer is the Forge's mechanism for recovering that knowledge from human cognition rather than leaving it undiscovered.

---

## Feedback Loop Architecture

The Cognitive Salvage Layer operates as a verification-gated pipeline from physical anomaly to autonomous execution update:

```
[Physical Salvage Scan]
         │
         │  Deformed geometry, unknown material composition,
         │  low-confidence triage classification
         ▼
[Gamified Simulation Node]
         │
         │  Constraint-driven spatial puzzle; player explores
         │  solution space under abstracted physical rules
         ▼
[Heuristic Extraction]
         │
         │  Player action sequence captured as
         │  candidate Heuristic Object
         ▼
[Auditor Verification Pipeline]
         │
         ├─── EXPLOIT ──────► Archive: Engine Exploit Log
         ├─── UNSAFE ───────► Quarantine: Hazardous Sequence Log
         ├─── SUBOPTIMAL ───► Archive: Low Priority
         ├─── FEASIBLE ─────► Queue for Execution
         └─── NOVEL ────────► Immediate Promotion
                   │
                   ▼
         [Forge Knowledge Base]
                   │
                   ▼
         [Autonomous Execution]
         (Updated triage, stratification,
          disassembly protocols)
```

**The critical distinction:** The player never directly teaches the Forge. The player generates candidate solutions. The Forge verifies them. That separation is what makes the pipeline safe to operate at scale.

---

## Core Data Streams

For player action sequences to be translatable into machine-executable protocols, the simulation interface must capture the following data classes:

**Triage Path Logging**
Chronological sequence of player actions — where they cut, separate, unbolt, or manipulate a component and in what order. This is the primary heuristic payload. Sequence order is often the entire insight.

**Volumetric and Geometric Manipulation**
How players rotate, align, and fit non-standard geometries into stratification or disassembly configurations. Captures spatial reasoning that planning agents cannot derive from static geometry alone.

**Constraint Interactions**
Where players repeatedly fail, back up, or hit simulation limits. Failure clustering identifies structural stress points, biofouling traps, and load-bearing sequences before physical tools ever contact the material. Failed attempts are data.

**Optimization Metrics**
Time, estimated tool wear, contamination risk exposure, and energy proxies for each solution path. Required for Stage 4 efficiency grading.

---

## The Heuristic Object Schema

Every candidate solution path is serialized as a Heuristic Object before entering the Auditor pipeline. This is the standard telemetry unit bridging the simulation node and the verification layer.

```json
{
  "heuristic_id": "HS-XXXX",
  "anomaly_source": "[Scan ID and anomaly description]",
  "anomaly_class": "[Deformed geometry | Biofouled | Unknown composite | ...]",
  "action_sequence": ["ACTION_A", "ACTION_B", "ACTION_C"],
  "constraint_violations_logged": 0,
  "auditor_status": "PENDING_SIMULATION",
  "stage_outcomes": {
    "stage_1_abstraction": null,
    "stage_2_kinematic": null,
    "stage_3_physical_sim": null,
    "stage_4_efficiency": null
  },
  "efficiency_delta": null,
  "novelty_flag": false,
  "provenance": "Player_Swarm | Single_Player | Operator_Override",
  "session_count": 1,
  "consensus_run_count": 0
}
```

Fields marked `null` are populated by the Auditor pipeline as each stage completes. `efficiency_delta` is calculated in Stage 4 relative to the current autonomous baseline. `consensus_run_count` tracks how many independent solution paths have been aggregated for this anomaly class — relevant to GH-002 (statistical significance threshold).

---

## Auditor Decision Tree

When a player submits a successful solution path, the Heuristic Object enters a four-stage verification pipeline. The Forge treats player inputs as untrusted, unverified candidate heuristics at all times. Passage through all four stages is required for knowledge base promotion.

```
[Player Solution Submitted]
              │
              ▼
┌─────────────────────────────┐
│  Stage 1: Abstraction &     │
│  Exploit Verification       │
└──────────────┬──────────────┘
               │
     Pass ─────┼─────► Fail ──► [Archive: Engine Exploit Log]
               │
               ▼
┌─────────────────────────────┐
│  Stage 2: Kinematic &       │
│  Collision Mapping          │
└──────────────┬──────────────┘
               │
     Pass ─────┼─────► Fail ──► [Archive: Kinematic Mismatch]
               │
               ▼
┌─────────────────────────────┐
│  Stage 3: Physical          │
│  Simulation & Stress Test   │
└──────────────┬──────────────┘
               │
     Pass ─────┼─────► Fail ──► [Archive: Material Failure /
               │                 Hazardous Sequence]
               ▼
┌─────────────────────────────┐
│  Stage 4: Efficiency &      │
│  Yield Grading              │
└──────────────┬──────────────┘
               │
               ▼
     [Grading Classification]
     FEASIBLE | NOVEL | SUBOPTIMAL
               │
               ▼
     [Forge Knowledge Base]
```

---

### Stage 1 — Abstraction and Exploit Verification

The Auditor isolates the action sequence from the game engine's rendering and physics layer to confirm the player did not exploit simulation artifacts.

**Boundary Violations:** Did any object surfaces intersect or pass through one another in a way real-world matter cannot? Clipping, Z-fighting exploitation, or geometry tunneling all constitute boundary violations.

**Temporal Anomalies:** Did actions occur faster than real-world physical actuators or human reaction times allow within the simulation's stated parameters?

*Fail outcome:* Flag as EXPLOIT. Log the simulation defect to the puzzle engine bug registry for repair. Discard the path — it contains no recoverable physical insight.

*Archive value:* Exploit logs are not waste. They are a systematic record of simulation fidelity gaps that must be closed before the pipeline can be trusted for the anomaly class that triggered them.

---

### Stage 2 — Kinematic and Collision Mapping

Human bodies have highly redundant degrees of freedom — wrists, fingers, elbows — that standard 6-axis industrial robotic arms cannot replicate without encountering gimbal lock or joint limit violations.

**Actuator Emulation:** The Auditor replays the player's vector movements through an inverse kinematics model of the target Forge machinery. Can the physical arm reproduce this sequence?

**Tooling Clearance:** Does the physical tool geometry (plasma cutters, hydraulic shears, manipulator claws) fit into the physical space the player utilized without chassis collision or reach limit violation?

*Fail outcome:* Flag as KINEMATIC_MISMATCH. Archive the path. Use the failure data to adjust the puzzle's tool constraint model so future players are working within the actual machinery's envelope from the start.

*Note:* Kinematic mismatches are not player errors — they are fidelity gaps between the simulation's tool model and the physical machinery. Both the path and the gap are informative.

---

### Stage 3 — Physical Simulation and Stress Testing

The gamified interface runs on a simplified real-time physics engine optimized for playability, not fidelity. Stage 3 subjects the candidate path to high-fidelity finite element analysis and rigid-body dynamic simulation.

**Structural Collapse:** If the player cut support element A before unbolting component B, does the remaining geometry deform under gravity, pinching physical tools or damaging the salvage target? Sequence order that appears valid in low-fidelity simulation may be catastrophic in physical reality.

**Contamination and Biofouling Propagation:** Does the disassembly sequence breach a pressurized line or biofouled cavity in a direction that gravity or fluid dynamics would wash contamination over clean components?

**Material State Assumptions:** Does the path assume material properties (tensile strength, ductility, joint integrity) that may not hold for the actual degraded or unknown-composition salvage item?

*Fail outcomes:*
- MATERIAL_FAILURE — path causes structural damage to salvage or tooling.
- HAZARDOUS_SEQUENCE — path causes contamination spread, pressurized release, or operator hazard.

*Both failure types are quarantined, not discarded.* The specific failure mode is logged as a Heuristic Object field and may be recoverable if the sequence is modified. A path that almost passes Stage 3 is more valuable than one that fails Stage 1.

---

### Stage 4 — Efficiency and Yield Grading

A path that survives Stages 1–3 is physically feasible. Stage 4 determines its operational value relative to the current autonomous baseline plan for the same anomaly class.

**Delta-T (Time):** Δ T = T_auto − T_player. Does this sequence reduce operational cycle time?

**Tool Wear and Energy Proxies:** Does the path require complex high-energy cuts where a simpler mechanical leverage approach would achieve the same result with lower tool wear?

**Value Retention:** Does the sequence preserve high-value components intact, or does it sacrifice them for throughput? Cross-reference `Economics.md` market replacement cost doctrine for value weighting.

*Stage 4 produces a grading classification, not a pass/fail outcome.* All paths reaching Stage 4 are physically valid. The grade determines their disposition in the knowledge base.

---

## Grading Classification Matrix

| Status Code | Disposition               | Description                                                                                       |
|-------------|---------------------------|---------------------------------------------------------------------------------------------------|
| FEASIBLE    | Queue for Execution       | Physically valid. Performs equal to current autonomous baseline. Offers alternative routing.       |
| NOVEL       | Immediate Promotion       | Exceeds autonomous baseline on at least one efficiency dimension. Pushed to local cache for immediate application. Threshold: Placeholder — see GH-006. |
| SUBOPTIMAL  | Archive / Low Priority    | Physically valid but slower, higher tool wear, or lower value retention than autonomous baseline.  |
| UNSAFE      | Quarantine                | Causes tool damage, structural collapse, or contamination spread in high-fidelity simulation.      |
| EXPLOIT     | Scrub / Bug Log           | Relies on simulation inaccuracies. No physical insight recoverable without simulation repair.      |

**On NOVEL threshold:** The source material specified >10% efficiency improvement as the NOVEL threshold. This figure is Placeholder — it has no derivation in the current repository and must not be treated as a specification claim. The threshold will be defined after first operational cycle data is available. See GH-006.

**On consensus aggregation:** Multiple FEASIBLE runs for the same anomaly class should be aggregated before promotion. The minimum run count for statistical significance is undefined — see GH-002. Until GH-002 resolves, treat single FEASIBLE runs as provisional queue entries pending confirmation.

---

## Integration Points

### Component_Triage_System.md
When the automated triage system encounters an item with a classification confidence score below threshold, it flags the asset, generates a puzzle instance abstracted from the scan geometry, and pushes it to the player queue. The Cognitive Salvage Layer is the downstream consumer of triage failures — it exists specifically to handle what the triage system cannot.

### Stratification and Separation Systems
Players manipulate flow, spin rates, or particle separation mechanics in a simplified fluid and centrifugal simulator, discovering stable sorting configurations. Verified configurations translate to physical spin chamber parameters. The game mechanic here is optimization of a physical process the player experiences as spatial puzzle-solving.

### Admin/Auditor_Protocols.md
The Auditor Decision Tree defined in this file operates under the full epistemic doctrine of `Admin/Auditor_Protocols.md`. All stage outcomes are PROVISIONAL until tool confirmation or physical test result is logged. Stage 3 simulation results are PROVISIONAL pending physical grounding per EF-0.8b — a simulation confirming a simulation is not external grounding.

The UNSAFE and EXPLOIT quarantine classifications map directly to EF-0.2 Level 2 (Subsystem Quarantine) for any heuristic that, if promoted, would constitute a hazardous knowledge state. The Auditor pipeline does not bypass the repository's epistemic governance layer — it operates within it.

### Forge_Net.md (planned)
NOVEL-classified Heuristic Objects are serialized and federated across the Forge network as cognitive save states — verified procedural knowledge available to all nodes encountering the same anomaly class. The federation architecture is defined in `Forge_Net.md`.

### Leviathan / Autonomous Swarm Operations
The Cognitive Salvage Layer is the Forge's answer to out-of-distribution autonomous failure. When a Leviathan unit encounters a situation outside its planning model's confidence envelope, the standard autonomous response is confidence collapse and halt. The Cognitive Salvage Layer converts that halt into a productive state:

```
[Leviathan: Confidence Collapse]
              │
              ▼
[Generate Puzzle Instance from anomaly scan]
              │
              ▼
[Human swarm explores solution space]
              │
              ▼
[Auditor pipeline verifies candidate paths]
              │
              ▼
[Verified heuristic returned to Leviathan]
              │
              ▼
[Autonomous execution resumes with updated knowledge]
```

In effect, humanity becomes an emergency cognition layer. The machine asks for help only when reality exceeds its models — and the request is structured, verifiable, and productive rather than a silent failure. This is one of the highest-leverage applications of the layer and the primary motivation for treating it as a core architectural module rather than a game feature.

---

## Epistemic State of This Document

This file is at Exploration stage. All claims carry PROVISIONAL / Internally Derived status unless otherwise noted. The Auditor Decision Tree and grading matrix are logical extensions of existing Forge verification doctrine — they are internally coherent but have not been tested against physical salvage operations or actual player behavior. CSL-A02 through CSL-A05 are explicitly Placeholder confidence.

The pipeline described here will remain PROVISIONAL until at least one physical anomaly has been run through all four stages with logged outcomes. The GH-series unknowns in the sidecar represent the primary gaps between the current logical architecture and a physically grounded specification.

---

## Abandoned Paths

| Date      | Path                                                              | Why Abandoned                                                                                                  | Reconsider? |
|-----------|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-------------|
| Jun 2026  | Inline compilation tags (MUTABLE_HEURISTIC, UNCERTAINTY)          | Parallel epistemic tagging vocabulary inconsistent with VERIFIED/PROVISIONAL/UNKNOWN state system in Auditor_Protocols.md. Creates Fallacy 4 drift immediately. | No |
| Jun 2026  | 85% consensus threshold for multi-model heuristic review          | Unlabeled Placeholder with no derivation. Would enter repository as false-precision Measured claim.            | Placeholder pending derivation — see GH-002 |
| Jun 2026  | LayerMD structural template (versioning header, confidence score %) | Hallucinated framework from Grok; not consistent with File_Template.md structure or Forge document architecture. | No |

---

## Drift Indicators

Mandatory re-audit conditions for this document:

- Auditor Decision Tree stages modified without cross-referencing `Admin/Auditor_Protocols.md` gate structure
- NOVEL threshold hardcoded to 10% without a logged derivation and GH-006 closure
- Grading matrix status codes diverge from Auditor_Protocols.md epistemic state vocabulary
- Integration point references to planned files promoted from *planned* to confirmed without Discovery.md update
- GH-series unknowns closed without documented Resolution Path
- Physical test results logged without updating CSL-A02 through CSL-A05 confidence fields
- Leviathan integration section expanded into architecture specification before `Operations/Leviathan.md` exists
- Ethical Anchor field absent, altered, or not matching canonical string

---

## Lessons Learned

| Date     | Evidence Type | What Was Tried                                      | What Failed                                                                   | What Was Learned                                                                              | Confidence | Revalidation Needed |
|----------|---------------|-----------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|------------|---------------------|
| Jun 2026 | Audit Review  | Inline MUTABLE_HEURISTIC / UNCERTAINTY tagging      | Parallel vocabulary to VERIFIED/PROVISIONAL/UNKNOWN — immediate Fallacy 4 risk | Epistemic state vocabulary must stay singular across the repository; no parallel tagging systems | Analogous | No |
| Jun 2026 | Audit Review  | 85% consensus threshold adopted from multi-agent synthesis | No derivation; would enter as false-precision Measured claim                 | Threshold figures without derivation are Placeholder until operational data exists             | Analogous  | No                  |

---

## Relationship to Existing Documents

- `Admin/Auditor_Protocols.md` — epistemic governance layer; Auditor Decision Tree operates within its doctrine
- `Admin/Ethical_Constraints.md` — hard-line constraints apply to all Forge modules including this pipeline
- `Admin/Canonical_Terms.md` — canonical vocabulary; grading status codes must not conflict
- `Architecture/Forge_flow.md` — reference standard for shared terminology
- `Unknowns.md` — GH-series unknowns registered in global index
- `Forge_Net.md` — planned; federation target for NOVEL-classified Heuristic Objects
- `Operations/Leviathan.md` — planned; primary operational consumer of emergency cognition layer
- `Economics.md` — value retention weighting for Stage 4 yield grading
- `Discovery.md` — navigation layer; this file requires registration

---

## Status

Version 0.1 — Initial Exploration draft. Logical architecture established. No gate passes attempted at Exploration stage.

**What must remain constant:**

**The player generates candidate solutions. The Forge verifies them. That distinction is what makes the pipeline safe.**

---

## Auditor Notes & Unknowns

### GH-001 — Heuristic-to-deterministic translation fidelity undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | High                            |
| Priority      | Major                           |
| Type          | Architectural / Epistemic       |
| Blocking      | Epistemic                       |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** Can player-derived heuristics be reliably translated into deterministic machine procedures? Human intuition operates on pattern recognition, gestalt spatial reasoning, and learned physical intuition that may not decompose cleanly into discrete, replayable action sequences. The abstraction from human movement to robotic vector string may lose the insight it was meant to capture.

**Why It Matters:** If the translation fidelity is low, the pipeline produces Heuristic Objects that pass Stage 2 kinematic mapping but fail to reproduce the actual physical insight in autonomous execution. The system would appear to function while generating low-value knowledge.

**Resolution Path:** Payment via Specification — requires empirical testing on at least one physical anomaly with logged Stage 1–4 outcomes and post-execution verification that the promoted heuristic produced the predicted efficiency gain. Until then, CSL-A02 remains Placeholder.

---

### GH-002 — Statistical significance threshold for consensus aggregation undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Governance / Epistemic          |
| Blocking      | No                              |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** How many independent player solutions for the same anomaly class are required before a heuristic pattern is considered statistically meaningful and safe to promote? A single NOVEL run may be an outlier, a lucky sequence, or an artifact of one player's idiosyncratic approach. The current schema tracks `consensus_run_count` but defines no threshold for promotion confidence.

**Why It Matters:** Premature promotion of low-consensus heuristics introduces unverified procedural knowledge into autonomous execution. This is the epistemic equivalent of Provenance Collapse — internally generated agreement mistaken for empirically validated truth.

**Resolution Path:** Payment via Specification — define minimum independent run counts stratified by anomaly class complexity and risk level. Cross-reference EF-0.1 (consensus is not evidence) — the threshold must be grounded in physical outcome verification, not run count alone.

---

### GH-003 — Adversarial poisoning of heuristic datasets undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | High                            |
| Priority      | Major                           |
| Type          | Security / Governance           |
| Blocking      | Epistemic                       |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** Can adversarial players intentionally poison the heuristic dataset by submitting systematically flawed or malicious solution paths that are designed to pass Stage 1–3 verification while producing subtly degraded autonomous execution outcomes? This maps directly to Adversarial Battery Challenge Class 8 (Malicious Actor Simulation) — a knowledgeable actor who understands the Stage 1–3 verification criteria could construct paths that satisfy all formal checks while encoding unsafe sequences that manifest only in physical deployment.

**Why It Matters:** The pipeline's safety guarantee rests on Stage 3 high-fidelity simulation catching hazardous sequences. If an adversarial actor can identify the gap between Stage 3 simulation fidelity and physical reality, they have an attack surface. CSL-A04 and CSL-A05 are both Placeholder on this point.

**Resolution Path:** Payment via Specification — define adversarial resistance requirements for the pipeline. Minimum: (1) player session isolation so adversarial patterns cannot be coordinated across sessions; (2) anomaly-to-outcome logging that flags promoted heuristics whose physical execution diverges from Stage 3 predictions; (3) rollback doctrine for heuristics whose physical outcomes fail post-execution verification. Cross-reference `Admin/Security_Protocols.md` and AP-008 (quarantine enforcement architecture).

---

### GH-004 — Optimal abstraction level for heuristic preservation undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Architectural                   |
| Blocking      | No                              |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** What abstraction level preserves useful human intuition while remaining computationally tractable for machine execution? Too high an abstraction (e.g., "remove fasteners before cutting") loses the sequence specificity that makes the heuristic valuable. Too low an abstraction (full motion capture at joint level) produces data that cannot generalize across anomaly instances or machinery configurations.

**Why It Matters:** The Heuristic Object schema currently captures action sequences at the operation level (CUT_A, SEPARATE_B). Whether this granularity is sufficient to encode the physical insight being harvested is untested. GH-001 and GH-004 are related — translation fidelity depends on abstraction level — but GH-004 is the architectural question and GH-001 is the empirical test.

**Resolution Path:** Payment via Specification — define abstraction hierarchy for action sequence encoding. Candidates: operation level (current), tool-path level (vector strings), joint-state level (full kinematic replay). Each carries a different data volume and generalizability tradeoff. Resolution requires input from Stage 2 kinematic modeling and physical test outcomes.

---

### GH-005 — Human vs. autonomous intervention fraction undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Low                             |
| Priority      | Minor                           |
| Type          | Operational                     |
| Blocking      | No                              |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** What fraction of edge-case triage problems actually benefit from human heuristic intervention compared to extended autonomous planning time? If the fraction is small, the pipeline overhead may not justify the integration complexity. If the fraction is large, the Leviathan emergency cognition connection becomes a primary operational dependency rather than an edge-case handler.

**Why It Matters:** Scoping the actual demand surface for this pipeline determines whether it belongs in core operations or in a lower-priority augmentation layer. This unknown does not block architecture development but should be resolved before the pipeline is treated as a critical path dependency.

**Resolution Path:** Discharge via Trajectory if first Leviathan deployment data is not available within the current development phase. Activate with empirical data from first operational cycles. Cross-reference `Operations/Leviathan.md` (planned).

---

### GH-006 — NOVEL promotion threshold undefined

| Field         | Value                           |
|---------------|---------------------------------|
| Status        | Open                            |
| Risk          | Medium                          |
| Priority      | Major                           |
| Type          | Governance                      |
| Blocking      | No                              |
| Owner         | Tests/Cognitive_Salvage_Layer.md |
| First Logged  | 2026-06-24                      |
| Last Reviewed | 2026-06-24                      |

**Description:** The Grading Classification Matrix uses NOVEL status for heuristics that exceed autonomous baseline performance. The source material specified >10% efficiency improvement as the threshold. That figure is Placeholder — it has no derivation in the repository, was not produced by physical testing, and must not be treated as a specification claim. The threshold also applies to a single efficiency dimension (time) while Stage 4 grades on multiple dimensions (time, tool wear, value retention). No multi-dimensional promotion criteria exist.

**Why It Matters:** A hardcoded threshold without derivation is a Confidence Without Basis violation (Fallacy 7). A threshold that applies only to time while ignoring tool wear and value retention may promote heuristics that win on speed while degrading Forge economics.

**Resolution Path:** Payment via Specification — define NOVEL threshold after first operational cycle data is available. The threshold must be multi-dimensional, reflecting the Stage 4 grading criteria. Intermediate state: label NOVEL as CANDIDATE_NOVEL in the schema until the threshold is formally defined, to prevent premature promotion. Cross-reference `Economics.md` for value retention weighting methodology.

---

### Resolution Log

- 2026-06-24: **v0.1 initial draft.** File created. Cognitive Salvage Layer architecture established at Exploration stage. Auditor Decision Tree (Stages 1–4), Heuristic Object schema, Grading Classification Matrix, and Leviathan emergency cognition connection documented. GH-001 through GH-006 registered in sidecar. Inline compilation tags and LayerMD structure abandoned (logged in Abandoned Paths). NOVEL threshold retained as Placeholder pending GH-006 resolution. File requires registration in Discovery.md and Unknowns.md (GH-series global index entries).

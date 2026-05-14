# Lazarus Forge — Components (v0)

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-14 (Gemini 3 Flash — Skeptic/Auditor)
- Open unknowns: 2 (CO-001 partially resolved; CO-002 open)
- Sidecar: [#auditor-notes--unknowns]

---

## Framing

This document defines the **component taxonomy** for Lazarus Forge v0 through v3. It answers: what must exist, what helps, and what can wait.

The scope is intentionally narrow: the metal fabrication enabling layer. Downstream systems (electronics, software, biological) are out of scope here. They have their own taxonomies.

---

## Definitions

**Critical** — Absence allows silent failure. The Forge cannot detect its own malfunction without this component. Loss is unrecoverable without outside intervention.

**Useful** — Absence limits the Forge but does not invalidate it. The Forge continues operating in a degraded state.

**Bootstrap** — A component present at genesis that is expected to fail, be replaced, and be improved upon. Bootstrap components are critical by function, not by quality.

---

## I. Critical Components (v0)

A component is critical if its absence allows **silent failure** — the Forge operates but cannot detect that it is operating incorrectly.

### 1. Feedstock Reduction
Shredder, cutter, or mill capable of reducing mixed metal scrap to processable size. Without this, no material enters the system.

### 2. Atmosphere Control
Enclosure and gas management preventing uncontrolled oxidation, toxic accumulation, or explosive atmosphere. Without this, thermal processes are unsafe.

### 3. Metal AM / Forming
At least one system capable of producing functional metal parts from Forge output stock. Without this, the Forge cannot replicate itself.

### 4. Thermal Processing
Controlled heat source capable of melting or sintering target materials. The Spin Chamber is the v0 implementation.

### 5. Metrology
Measurement capability sufficient to verify output quality. Without this, the Forge cannot confirm it is producing usable material.

*Metrology verifies output correctness. It is distinct from Baseline Observability, which verifies system state correctness. A Forge can produce bad parts while mechanically healthy, or produce good parts while internally degrading. Both failure modes require detection.*

### 6. Baseline Observability
Minimum instrumentation sufficient to detect unsafe process states and internal degradation. Examples: thermal probes, motor current sensing, airflow monitoring, cameras, encoder verification. Without this, the Forge cannot distinguish silent drift from normal operation.

*Baseline Observability verifies system state correctness. See note under Metrology (item 5) for distinction between the two.*

*Power dependency: Baseline Observability instrumentation requires stable power to function reliably. Minimum requirement at v0: surge protection on all sensor and compute circuits. Brownout or spike events that corrupt sensor state defeat the purpose of this component. See also Artifact Memory (item 7).*

### 7. Artifact Memory
Persistent storage of process parameters, outcomes, and component provenance. Without this, learning resets every generation.

*Power dependency: Artifact Memory is vulnerable to power instability. Minimum requirement at v0: surge protection and graceful write handling to prevent corruption on unexpected power loss. Corrupted memory that appears valid is worse than lost memory — a silent corruption is a silent failure. See Baseline Observability (item 6).*

### 8. Human Override Interface
Physical or digital mechanism for operator intervention at any process stage. Without this, autonomous failure cascades cannot be interrupted.

---

## II. Useful Components (Capability Amplifiers — Non-Critical)

Absence does not invalidate the Forge, only limits it.

### A. Closed-Loop Recycling
Internal recovery of process waste (slag, failed prints, spent powder). Reduces external feedstock dependency over time.

### B. Advanced Sensing & Diagnostics
Higher-order monitoring enabling predictive maintenance, autonomous quality assessment, and process optimization. Presupposes Baseline Observability (Critical item 6). Without the observability floor, advanced diagnostics have no validated baseline to reason from.

### C. Compute & Autonomy
Decision-making systems above basic threshold logic. Enables reduced human oversight over time.

### D. Energy Infrastructure
On-site generation, storage, and distribution beyond grid bootstrap. See `energy_v0.md`.

### E. Logistics & Transport
Material handling, sorting, and transfer automation. Enables higher throughput.

---

## III. Downstream Systems (Out of Scope v0)

- Electronics fabrication
- Software development environment
- Biological or chemical synthesis
- Precision optics

These emerge through growth, not seeding. They belong in future version taxonomies.

---

## IV. Version Mapping

| Version | Material Scope | Key Capability Added |
|---|---|---|
| v0 | Aluminum, copper, basic steel | Proof of persistence — the loop closes |
| v1 | Expanded alloys | Steel-class materials, closed-loop recycling |
| v2 | Multi-material | Manufacture of Forge submodules |
| v3 | Space-grade | Regolith and asteroid material processing |

*v3+ version milestones are trajectory markers — component taxonomy for those stages is not defined in this document.*

---

## V. Bootstrap Doctrine

**Core principle:** Imperfect beginnings are valid.

A v0 Forge built from salvage, with degraded components and manual oversight, is still a Forge. The Bootstrap Doctrine establishes:

- Bootstrap components are expected to fail
- Failure is not a defect — silence is
- Every failed bootstrap component is a learning event
- Never auto-delete a failed component record

**Sufficiency criterion:** A component is sufficient if it allows the Forge loop to close. The Forge loop: intake → triage → process → verify → learn → repeat. (Loop definition per `geck_forge_seed.md` Section III.)

**Wear and consumables:** Bootstrap components operate under high maintenance cadence. Blade dulling, nozzle clogging, bearing wear, and similar degradation are expected — not exceptional. Consumables, wear parts, and tooling redundancy are addressed in the G.E.C.K. manifest rather than this taxonomy. A G.E.C.K. is considered insufficient if it cannot support at least one full maintenance cycle for each Critical component. The taxonomy defines what must exist; the G.E.C.K. ensures it can keep existing.

**Proxy/Downgrade paths:** When a critical component is unavailable at spec, a lower-capability substitute is acceptable if it allows the loop to close in degraded form. Document the substitution.

**Graduation Rule:** A component graduates from Bootstrap to Specified when the Forge can: (1) detect its degradation, (2) repair or replace it internally, (3) improve its successor.

*At v0, graduation assessment uses Baseline Observability plus human operator verification together as the detection proxy. Baseline Observability (Critical item 6) provides the minimum instrumentation floor; human operators supply interpretive judgment above that floor. This is a defined v0 operating condition, not a gap. See CO-001.*

---

## VI. Dual-Use Annotation Standard

Components with known dual-use potential are annotated:

| Risk Level | Meaning | Action |
|---|---|---|
| Low | Minimal weaponization potential | No special handling |
| Medium | Dual-use possible with modification | Log provenance, flag if pattern emerges |
| High | Direct weaponization path exists | Full Stop — route to `Ethical_Constraints.md` |

*Note: No component in the current v0 taxonomy is rated High. High rating is expected to appear in downstream capability documents (Leviathan chassis, remote autonomous systems). Its absence here reflects current component scope, not a judgment that no Forge-adjacent capability warrants it.*

---

## VII. Operating Principle

> A component is critical if its absence allows silent failure.

This single sentence governs all classification decisions. When in doubt, ask: if this component fails, does the Forge know?

---

## Lessons Learned

| Date | What was tried | What failed | What was learned |
|---|---|---|---|
| May 2026 | Graduation Rule written without acknowledging detection dependency | At v0, Advanced Sensing is Useful not Critical — the Forge may not yet be able to detect its own component degradation | Human operator verification must be explicitly named as the v0 proxy for automated detection |
| May 2026 | Metrology and observability treated as a single category | Metrology verifies output correctness; Baseline Observability verifies system state correctness — these are distinct failure modes requiring separate detection | Split into two Critical items; distinction noted explicitly in both entries |
| May 2026 | Power conditioning omitted from critical component notes | Brownout or surge can corrupt Artifact Memory and defeat Baseline Observability — two Critical components rendered unreliable by an unstated infrastructure assumption | Added power dependency notes to items 6 and 7; minimum: surge protection at v0 |
| May 2026 | Wear and consumables left implicit in Bootstrap Doctrine | "Expected to fail" did not explicitly address maintenance cadence or where redundancy lives | Added explicit wear note to Bootstrap Doctrine; routed consumables and spare parts to G.E.C.K. manifest as the designated redundancy path |

---

## Auditor Notes & Unknowns

### CO-001 — Graduation Rule detection circularity at v0
**Status:** Partially Resolved
**Risk:** Low (downgraded from Medium)
**What was not known:** How the Graduation Rule's detection requirement is satisfied at v0, when Advanced Sensing (needed to detect component degradation) is classified as Useful rather than Critical. A component cannot graduate until the Forge can detect its degradation — but that detection capability may not exist when graduation decisions need to be made.
**Resolution path:** Two-part resolution:
1. Baseline Observability added as Critical item 6 — establishes a minimum instrumentation floor (thermal probes, current sensing, cameras, airflow, encoders) that must exist at v0. This is not Advanced Sensing; it is the detection substrate that Advanced Sensing builds upon.
2. Bootstrap Doctrine updated — graduation at v0 uses Baseline Observability plus human operator judgment together as the proxy. Human operators supply interpretive judgment above the instrumentation floor.
**Remaining:** Same note should be added to `Lazarus_forge_v0_flow.md` Bootstrap Doctrine reference. UNK-026 in `Unknowns_LF.md` should be updated to reflect partial resolution.
**Logged:** Components.md audit cycle, May 2026
*Cross-module reference: UNK-026 in Unknowns_LF.md*

### CO-002 — Metrology Precision Thresholds
**Status:** Open
**Risk:** Low
**What is not yet known:** The minimum viable tolerance required for a bootstrap part to be considered "functional enough" to continue the loop. Current wording ("sufficient to verify output quality") is correct in principle but unquantified. The threshold likely differs by material (aluminum vs. steel) and by part function (structural vs. non-structural).
**Resolution path:** Define minimum acceptable tolerance per material class and part category at v0. Likely expressed as a dimensional tolerance (e.g., ±X mm) plus a functional test criterion (does the part fit and hold under expected load). Defer precise values to first fabrication trials — tolerance requirements emerge from actual loop closure attempts, not pre-specification.
**Logged:** Gemini 3 Flash audit, 2026-05-14

### Resolution Log
- May 2026: Bootstrap Doctrine updated — sufficiency criterion linked to Forge loop definition in geck_forge_seed.md. Human proxy for graduation detection added explicitly.
- May 2026: v3+ trajectory marker note added to Version Mapping table.
- May 2026: Dual-use annotation note added explaining absence of High-rated components.
- May 2026: Metrology and Baseline Observability split into separate Critical items (5 and 6). Distinction between output verification and system-state verification made explicit. CO-001 partially resolved — detection circularity addressed structurally rather than procedurally.
- May 2026: Power conditioning notes added to Baseline Observability (item 6) and Artifact Memory (item 7). Addresses Gemini audit Gate 1 blocker — power stability omission. Resolved as inline notes rather than new Critical item; scope is "protect these two components" not a new category.
- May 2026: Wear and consumables note added to Bootstrap Doctrine. Explicitly routes redundancy and maintenance stock to G.E.C.K. manifest. Addresses Gemini audit Gate 1 blocker — friction/consumables omission. Clarifies division of labor: Components.md defines necessity, G.E.C.K. ensures continuity.
- May 2026: CO-002 (Metrology Precision Thresholds) logged per Gemini audit finding.

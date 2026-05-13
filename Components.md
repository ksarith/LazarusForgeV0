# Lazarus Forge — Components (v0)

**Audit Health:**
- Status: Exploration
- Last audit: 2026-05-04 (Claude — Skeptic/Auditor)
- Open unknowns: 1 (Blocking at promotion)
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
Measurement capability sufficient to verify output quality. Without this, the Forge cannot confirm it is producing usable material.  Baseline Observability
Minimum instrumentation sufficient to detect unsafe process states and internal degradation. Examples: thermal probes, motor current sensing, airflow monitoring, cameras, encoder verification. Without this, the Forge cannot distinguish silent drift from normal operation.

### 6. Artifact Memory
Persistent storage of process parameters, outcomes, and component provenance. Without this, learning resets every generation.

### 7. Human Override Interface
Physical or digital mechanism for operator intervention at any process stage. Without this, autonomous failure cascades cannot be interrupted.

---

## II. Useful Components (Capability Amplifiers — Non-Critical)

Absence does not invalidate the Forge, only limits it.

### A. Closed-Loop Recycling
Internal recovery of process waste (slag, failed prints, spent powder). Reduces external feedstock dependency over time.

### B. Advanced Sensing & Diagnostics — higher-order monitoring enabling predictive maintenance, autonomous quality assessment, and process optimization. Presupposes Baseline Observability.

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

**Proxy/Downgrade paths:** When a critical component is unavailable at spec, a lower-capability substitute is acceptable if it allows the loop to close in degraded form. Document the substitution.

**Graduation Rule:** A component graduates from Bootstrap to Specified when the Forge can: (1) detect its degradation, (2) repair or replace it internally, (3) improve its successor.

*At v0, graduation assessment requires human operator verification as a proxy for automated degradation detection — see CO-001.*

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

---

## Auditor Notes & Unknowns

### CO-001 — Graduation Rule detection circularity at v0
**Status:** In Progress
**Risk:** Medium
**What is not yet known:** How the Graduation Rule's detection requirement is satisfied at v0, when Advanced Sensing (needed to detect component degradation) is classified as Useful rather than Critical. A component cannot graduate until the Forge can detect its degradation — but that detection capability may not exist when graduation decisions need to be made.
**Resolution path:** Option chosen: explicitly state in Bootstrap Doctrine (Section V) that graduation decisions at v0 require human operator verification as a proxy for automated detection. This is a defined v0 operating condition, not a gap. One sentence added: "At v0, graduation assessment requires human operator verification as a proxy for automated degradation detection." Also noted in Trajectories_LF.md v0 exit condition (UNK-026 cross-ref). Remaining: same note should be added to Lazarus_forge_v0_flow.md Bootstrap Doctrine reference.
**Logged:** Components.md audit cycle, May 2026
*Cross-module reference: UNK-026 in Unknowns_LF.md*

### Resolution Log
- May 2026: Bootstrap Doctrine updated — sufficiency criterion linked to Forge loop definition in geck_forge_seed.md. Human proxy for graduation detection added explicitly.
- May 2026: v3+ trajectory marker note added to Version Mapping table.
- May 2026: Dual-use annotation note added explaining absence of High-rated components.

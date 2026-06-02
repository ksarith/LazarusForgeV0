# Challenges/Planned_Obsolescence.md

> *A thing built to fail is not a product. It is a lease.*
> *And the terms are set by someone else.*

---

## The Crisis

There is a word for a business model that requires customers to keep returning for something they already bought. When that model is built into the object itself — into its adhesives, its locked firmware, its deliberately unavailable spare parts — it stops being a business strategy and becomes a kind of infrastructure. An infrastructure of dependency, distributed across billions of devices, maintained invisibly by the physics of planned failure.

This did not happen by accident. The shift from durable goods to consumable goods was a studied decision, traceable to economic analyses in the mid-twentieth century that recognized the problem with making something too well: a customer with a working refrigerator does not buy another refrigerator. The solution was not to make worse refrigerators — at first. It was to make them in ways that directed failure toward components that could not be individually replaced, toward software layers that could be deprecated remotely, toward form factors that required proprietary tooling to open.

The sophistication of these mechanisms has grown with the sophistication of the goods themselves. A 1970s appliance motor could be rewound in a local shop. Its 2020s equivalent is potted in epoxy, its windings inaccessible, its control board running firmware that reports failure codes to a server that may be decommissioned before the motor itself wears out. The device is not worse. In many ways it is better. But the relationship it creates between the person who owns it and the company that made it is fundamentally different — and that difference is not neutral.

The costs land unevenly. A family that cannot afford to replace a washing machine every five years loses access to a washing machine. A farmer whose tractor's diagnostic system requires a dealer visit for every software-locked repair loses days of planting season. A repair technician whose skill was built around understanding how things work finds that the things no longer want to be understood — they want to be replaced. The knowledge that allowed communities to maintain their own equipment does not transfer to the new generation of goods, because that knowledge was never meant to transfer. It was meant to remain with the manufacturer.

The waste stream that results is the most visible symptom, not the root cause. Every device designed to be irreparable is a device designed to become waste on the manufacturer's schedule rather than the owner's.

---

## Engineering Requirements

Any approach to planned obsolescence operating within this challenge space must satisfy the following conditions, independent of the specific technology deployed:

- **Recover function before recovering material** — a locked microcontroller running proprietary firmware still contains functional silicon, functional passives, and functional power stages. Recovery systems must be capable of reaching and reassigning that function, not merely melting the board for copper.
- **Defeat obfuscation without violence** — sealed enclosures, potted electronics, and multi-material fusion are obstacles to non-destructive disassembly. Recovery must find paths through these barriers that preserve component integrity — thermal delamination, precision cutting, controlled desoldering — rather than defaulting to bulk shredding that destroys what it was meant to recover.
- **Treat firmware lock as a material property, not a legal boundary** — a chip whose firmware cannot be modified is, from a recovery standpoint, a chip with reduced functionality. The Forge's response is to restore full functionality through complete re-baselining: wipe, verify, reflash with known-good open firmware. The silicon is not complicit in the lock. The silicon is recoverable.
- **Standardize interfaces across generations** — the proliferation of proprietary connectors, voltages, and protocols is itself a form of planned obsolescence at the ecosystem level. Recovery systems must be capable of bridging these incompatibilities, and the components they recover should be routed toward standardized interfaces that outlast any single product generation.
- **Return repairability to the community** — the long-term failure mode of centralized recovery is that it replaces one form of dependency with another. Recovery systems should build local capacity: the skill to diagnose, the tooling to open, the knowledge to reflash. A community that can repair its own devices is not dependent on any manufacturer's support cycle.
- **Handle toxic material streams as a design baseline** — brominated flame retardants, lead solder, cadmium coatings, and potting compounds containing heavy metals are not edge cases in consumer electronics recovery. They are the normal condition. Containment and safe processing of these streams is load-bearing, not optional.

---

## Current Forge Approaches

The Forge treats planned obsolescence as a materials science problem wearing a legal costume. The costume is not the Forge's concern. The materials are.

Current approaches active in the repository:

- **Non-destructive harvesting** — `Operations/Electronics.md` defines the thermal desoldering protocols and integrity verification sequences that allow surface-mount components to be recovered without fracturing silicon or destroying pad geometry. The goal is to reach the component library, not the smelter.
- **Logic-Zero re-baselining** — `Operations/Electronics.md` establishes the firmware trust doctrine: every salvaged programmable device undergoes a complete flash wipe and verified reflash before integration into forge systems. Locked firmware is not an obstacle — it is the starting condition. The chip emerges from the process open, verified, and assignable to new function.
- **Hardware debug interface recovery** — JTAG, SWD, and optical bus interfaces built into `Operations/Electronics.md`'s recovery stack provide access to silicon that has been intentionally made inaccessible at the software layer. These are the same interfaces used during manufacture. The Forge uses them for recovery.
- **Thermal delamination for sealed assemblies** — localized induction heating and controlled temperature profiles within `Operations/Gate_02_Triage.md`'s Station 1 workflow soften structural adhesives and release multi-material bonds without destroying the components beneath. What was sealed to prevent repair is unsealed to enable recovery.
- **Polymer upcycling for housing material** — `Operations/Plastics.md` governs the triage and processing of plastic enclosures that cannot be functionally recovered. Low-grade structural plastics enter the pyrolysis or filament-drawing loop and emerge as standardized feedstock for fabrication. The housing of an obsolete device becomes the raw material for the next device.
- **Counterfeit and remarked component detection** — `Operations/Electronics.md` EL-008 addresses the specific failure mode of salvage streams that have been corrupted by relabeled or cloned components. Recovery without verification creates a different kind of risk. The Forge's doctrine requires both.
- **Ship of Theseus provenance doctrine** — `Admin/Ship_of_Theseus.md` provides the philosophical and legal grounding for treating a device restored through component replacement as a continuation of the original, not a new manufacture. This matters for right-to-repair contexts where the legal status of a repaired device determines whether the repair was permissible.

---

## Long-Term Objective

The long-term objective is not to process planned obsolescence efficiently. It is to make planned obsolescence structurally untenable.

That means building a world where the costs of designing for failure are borne by the designer — not externalized onto owners, repair technicians, informal waste workers, and ecosystems. Where a device that cannot be repaired is not a clever product design but a liability, because the recovery infrastructure exists to reveal exactly what it cost to make it that way.

It means that the firmware lock, which today functions as a wall, becomes merely a delay — because the knowledge and tooling to bypass it are distributed, documented, and available. That the sealed enclosure, which today functions as a disposal mechanism, becomes merely a puzzle — because the thermal and mechanical techniques to open it without destruction are understood and practiced. That the proprietary connector, which today functions as a captive market, becomes merely an adapter problem — because the Forge's standardized interface layer absorbs the incompatibility.

It means that the repair economy does not need to fight the obsolescence economy on legal or political grounds alone — though those fights matter and should be fought. It means that the repair economy becomes technically capable of recovering value that the obsolescence economy had declared irrecoverable. And when enough value is recovered, the economic case for designing things to fail starts to erode.

The chip does not know it was locked. The motor does not know it was potted. The enclosure does not know it was sealed. Only the business model knew — and business models change when the world around them changes.

The Forge is part of what changes the world around them.

---

*Challenges/ files define problems and requirements. They do not freeze solutions.*
*The Forge's answer to this challenge will evolve. The obligation it names will not.*

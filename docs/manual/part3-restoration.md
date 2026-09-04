# Part III — Restoration
### L&R Master Watch Cleaning Machine · Master · S/N 13505

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered and restored by Hobbs R.E., 2026, from direct physical work on specimen S/N 13505. For restoration reference only.

*Title block: Date June 12, 2026 · L&R Precision Cleaning Machine · Master · S/N 13505 · L&R MFG. CO. · Engineer Hobbs R.E.*

**About this part.** The original L&R manuals covered only *operation* and *maintenance*. This part documents what they never did — how to **restore** a seized, decades-old machine: assess it, take it apart without damage, recondition the parts, reassemble it, rewire it to modern safety standards, and bring it back to life. Procedures use canonical Part IDs (e.g. ARM-010, FLG-002) from the Parts Dictionary; dimensions carry their confidence label. Figures reference the project's bench photos (`photos/`) and engineering drawings (`drawings/`). Full as-performed detail — every product, tool, and caution — lives in the source logs (`restoration-log.md`, `teardown-log.md`); this chapter is the curated, readable version.

**Restoration philosophy.** Mechanical and visible parts were restored toward original appearance and function. The **electrical system was deliberately modernized** for safety and serviceability — the original was a 2-wire ungrounded design with a live "green" wire and no earth ground, and this specimen had prior amateur rework. Every deviation from original is documented so the record stays honest.

---

## III.0 — Assessment (as-found)

Document the machine's condition before touching it — it drives every later decision.

**Mechanical.** The motor housings (UH-001 / LH-001) carried decades of baked-on factory enamel, oil varnish, and grease crosslinked into the porous aluminum. The self-aligning spherical sleeve bearings (BRG-001 / BRG-002) were mechanically sound and reusable, but their **consumables were spent** — the wool-felt washers were brittle and broke apart on disassembly, and the reservoir yarn was bone-dry. The tapered rubber jar seal (PLT-002) was dried and near-degraded. Several parts had seized from age and required gentle freeing (never force).

**Electrical — the critical hazard.** The neck loom carries three wires (black / white / **green**). **The green wire is NOT a safety ground — it is a live, current-carrying motor branch.** Treat all three neck conductors as hot. The machine had no earth ground, and inspection showed **prior amateur rework** (nasty solder blobs, one switch contact failed on a bad joint, a non-original bulb). This confirmed the electrical system should be rebuilt rather than preserved.

**Previously modified / non-original.** Gasket-to-disk rivets (PLT-005) had to be drilled out to service the seal; the pilot bulb was a later replacement; the AC cord grommet had disintegrated.

*Fig. III-0: machine as-received — `photos/` (overall) + reference S/N 13645.*

---

## III.1 — Disassembly

Performed in the order below; reassembly (III.3) is essentially this in reverse. *Terminology note: where a prior bench recording said "stator/stator shaft" it meant the **armature/rotor**; "field coil" meant the **stator (STR-001)**. This text uses the canonical terms.*

### III.1.1 — Remove the basket and drive spindle
The basket and its drive spindle come off the motor as one "outer column." A single **set screw (SPN-005, ¼-20, slotted)** locks the basket drive spindle (**SPN-002**) to the armature's lower journal (**SHF-003**). Back the set screw out with a flat blade, then draw the spindle/basket assembly off the shaft. If seized from age, free it with **very light, deliberate taps of a rubber mallet** — gentle pressure only, never a hard strike.
*Fig. III-1: `drawings/components/SPN-002…`, `BSK-002…`.*

### III.1.2 — Understand the platform deck (before the housing bolts)
Beneath the motor is the jar-seal deck: a flat metal **platform disk (PLT-001)** carrying the tapered rubber **jar seal (PLT-002)**. The gasket is fixed to the disk by four **rivets (PLT-005)**; the remaining two holes pass the long **housing bolts (FLG-002)** — through **standoff tubes (PLT-004)** — which clamp the two motor-housing halves together. Knowing this prevents surprise when the next step releases several parts at once.
*Fig. III-2: `drawings/components/PLT-001…` + `photos/gasket/`.*

### III.1.3 — Separate the housings
Unscrew the **two long housing bolts (FLG-002)**. The lower housing (**LH-001**) drops away, and the **armature (ARM-001)** comes down with it (the rotor stays seated in the lower bearing, BRG-002). Support the dropping assembly so the commutator and windings are not knocked.
*Fig. III-3: bolt circle 2.300" — `drawings/exploded/EXP-001…`.*

### III.1.4 — Remove the lower thrust ring (ARM-010)
A stepped brass slinger/thrust washer (**ARM-010**) remains on the lower journal, just outside the housing face; it must come off before the armature will withdraw. **Do not pry it** — the ring is brass and bends easily. Instead, clamp the housing in a vise **raised on blocks** so the shaft hangs clear, tap the **top** of the shaft squarely with a rubber mallet to walk the ring a short way down the journal, then seat a small **gear/bearing puller** behind it and draw it off evenly.
> **CAUTION — keep all force axial.** Uneven pull or prying will distort the brass ring.
*Fig. III-4: `photos/bearings/`.*

### III.1.5 — Disconnect the electrical
A three-wire loom (black/white/green) runs from the control unit into the motor and lands on the **stator field coil (STR-001)**. Cut these leads at the coil to free the motor. On reassembly they are **replaced**, not re-spliced.
> **CAUTION — the GREEN wire is LIVE, not ground.** Treat all three as hot.
*Fig. III-5: `photos/stator-wiring/`.*

### III.1.6 — Remove the stator (field coil)
Remove the **two stator mount screws (STR-008)** and lift the field coil (**STR-001**) out of the upper housing. (The yoke's other two holes were the FLG-002 pass-throughs, already out.)
*Fig. III-6: `drawings/components/STR-001…`.*

### III.1.7 — Remove the sleeve bearings and springs
Each housing retains a self-aligning spherical sleeve bearing (**BRG-001** upper / **BRG-002** lower) held by a conical spring (**BRG-012**). *As performed:* face-down on a rubber/wood block, the bearing was tapped out of the spring, then the spring removed. This worked but may not be ideal — a better technique is an open question for this design.
> **Recommended candidates (untested here):** (1) release the conical spring first — it captures the ball; (2) warm the aluminum housing (~80–120 °C) to open the fit; (3) press (not hammer) with a drift on an open-bore fixture; (4) soft drift / blind-hole puller. Keep force axial; never pry the spherical socket.
*Fig. III-7: `drawings/components/BRG-001…`.*

**End state:** motor fully disassembled, all internals out, ready for cleaning and refinishing.

---

## III.2 — Component restoration

### III.2.1 — General cleaning & degrease (R-3)
As each sub-assembly came apart, small hardware (bearings, fasteners, collars, washers, the oil feed tube LH-006, small brackets) was degreased in an **ultrasonic tank with a diluted mild-soap solution**, then rinsed and dried. Mild/neutral chemistry was chosen deliberately — safe across the mixed materials (steel, brass, aluminum, phenolic). Oversized parts (housings, base casting, neck/pillar) were **cleaned by hand**. Some mesh basket pieces (BSK-002) carried baked-on chemical sludge and got a stronger **Citranox** clean.
> **CAUTIONS:** ultrasonic degreasing **strips all lubrication** — bearings must be re-oiled before/at reassembly (III.3); **dry parts promptly** (bare steel/aluminum flash-rusts); keep the chemistry mild.

### III.2.2 — Jar-seal gasket reconditioning (R-1)
The tapered rubber jar seal (**PLT-002**, molded with the maker's mark *U.S. PATENT 1,872,812*) was dried, stiff, and brittle. Restore it by: (1) a warm **Citranox** clean to remove the orange-brown chemical film; (2) a **16+ hour immersion soak in 100% silicone oil** (SEKODAY, a non-cracking silicone sold as treadmill-belt lubricant) to fully re-saturate the rubber; (3) a microfiber buff to a satin-black finish. Result: pliability fully restored, structurally sound again.
> **CAUTION — silicone only on rubber.** **WD-40 / petroleum distillates are ruled out** — they swell and degrade vintage elastomers.

### III.2.3 — Platform-deck refastening (R-6)
The gasket (PLT-002) was originally **riveted** to the platform disk (PLT-001) by four rivets (PLT-005), which had to be drilled out to service it. Restoration substitutes a **serviceable screw set**: per hole (×4), a **stainless M4-0.7 × 10 mm flat-head Phillips screw + hex nut**, reusing the **original flat washers (PLT-006)**. The countersunk head sits flush. The gasket is now removable for future service.
> *Drawings show the original rivet as the design of record, with a note citing this restoration substitution.*

### III.2.4 — Bearing-system materials (R-4)
The **bearings themselves (BRG-001/002) and the conical springs (BRG-012) were sound and reused** (cleaned per III.2.1). Only the spent consumables were replaced, mirroring the original wick/felt oiling scheme:
- **Reservoir yarn (BRG-008):** Estako Wool 98 — 100% Superwash Merino, **un-dyed** (won't leach dye or mat when oil-saturated).
- **Felt washers (BRG-009 large / BRG-010 small):** SAE F3 hard wool felt (dust block + oil containment).
- **Oil wick:** GE 1/8" vintage-fan wick (~1¼"), tied to the yarn.
- **Oil:** Bramec Zoom Spout turbine oil.

*(The Century Spring TA-2226CS was identified as the dimensional equivalent for BRG-012 if a spring is ever needed, but the originals were reused.)*

### III.2.5 — Motor-housing cosmetic refinishing (R-2)
Both housing halves (UH-001 / LH-001) carried crosslinked baked-on factory finish. Refinish sequence:
1. **Chemical strip:** coat with **Citristrip** gel (citrus-based, safe on aluminum), dwell, and work the softened finish out of the deep fins, chambers, and notches with brushes/picks. **Remove all residue and dry immediately** (bare aluminum flash-rusts).
2. **Prep & mask:** lightly scuff the exterior for primer tooth; precision-mask every running face, bore, and mating flange (FLG-001) with razor-trimmed high-temp tape.
3. **Final wipe + etch primer:** wipe with **99.9% IPA**, then **Rust-Oleum 249322 self-etching primer** in ultra-thin coats (matte olive-grey = proper anchor).
4. **VHT Wrinkle Plus topcoat:** 3 heavy crosshatched coats — **horizontal → vertical (5-min flash) → diagonal (5-min flash)** — a wrinkle finish needs a thick film with tight flash times to ripple.
5. **Thermal cure:** draw the texture with controlled heat (**~350 °F** heat gun and/or oven after the level window). **Pull the masking while the film is still warm** to preserve internal dimensions.

Result: tight, uniform heavy wrinkle grain matching the vintage L&R aesthetic, tolerances preserved.

### III.2.6 — Control-unit / base-casting refinishing
The cast-aluminum base body was stripped (Citristrip), and worn cast lettering ("OFF" on the tongue, the "L&R MASTER" relief) was rebuilt with **J-B Weld High Heat epoxy** on abraded bare metal (it survives the ~350 °F wrinkle bake, unlike polyester filler), then block-sanded flush and the lettering re-cut with a Dremel. The same **etch primer → VHT Wrinkle Plus** system as the housings was applied, inside and out, for a matching texture.
- **Cast lettering was left monochrome** (shot with the wrinkle, no color fill) — factory-correct, the relief reads by shadow.
- **Cure without an oven:** heat-gun draw to form the wrinkle, then a multi-hour cure in direct sun + a warm garage (48–72 hr undisturbed). Confirmed workable.
- **Chrome parts** (post NCK-001, clamp screw NCK-003) were cleaned and sent out for professional **re-chrome**.
> **CAUTION — bake-proof masking.** Ordinary painter's tape (~250 °F) scorches at the wrinkle bake; swap to high-temp masks (silicone plugs / stainless bolts / Kapton) before the topcoat. Keep fit surfaces (the BAS-006 post socket, screw holes) masked so wrinkle texture doesn't spoil the fit.

---

## III.3 — Reassembly

### III.3.1 — Bearings & lubrication, lower housing (R-7)
*No public instructions exist for this — the method reconstructs the original wick/felt capillary oiling.*
1. Cut ~1 ft of wool yarn (BRG-008) and ~1¼" of GE wick; **tie them together**.
2. **Route the yarn through the oil-wick port** — stiffen the floppy lead with a wrap of Scotch tape and pull it through with tweezers.
3. Place the **small felt (BRG-010) flush at the bottom of the bearing** (it contacts the incoming wick = how the lower felt gets oiled); route the yarn **up the side**, wrapping the **large felt (BRG-009)** at the top neck (oil wicks up to the upper felt).
4. **Seat the bearing (BRG-002)** — mind the **bottom notch** (one orientation only).
5. **Pre-oil** the felts + yarn with Zoom Spout; let it soak.
6. Insert the **conical spring (BRG-012)**.
7. Install the **retaining ring (BRG-011)** at the bottom (friction fit) — tap flush with a **brass punch + light rubber-mallet** taps, working evenly around.
8. Clean the bore (alcohol pads); **test-fit the armature** (good).
> **CAUTION — no steel tools under pressure.** Use brass punches; light, even, axial force only.

### III.3.2 — Bearings & lubrication, upper housing (R-8)
The harder of the two (15+ attempts). Key differences: the upper bearing (**BRG-001**) has an **internal slit** and the yarn rides **inside** it; the upper "small felt" is a **solid tab/pad** (pin-hole only) that sits at the very top under the **oil cap (UH-011)**; and there is **no bottom retaining ring**.
- **Working method:** tie the yarn around a small **~0.400" wood peg** with a hitch knot, slip that over the bearing's inner end, route the other end **through the internal slit**, wrap it tight at the top, and **anchor the terminal end with a dab of super glue** (the pliable felt detaches during seating otherwise). Thread the lead up through a poked hole in the top felt pad; seat the bearing; add the large felt; pre-oil; insert the spring; test-fit (spins fine); cap the oil port.
> **Open item (VERIFY):** the super-glue anchor's effect on long-term wicking is unknown — watch oil feed over time. It was a last resort with no manual to reference.

### III.3.3 — Armature + slinger, mechanical assembly (R-9 → R-11)
1. **Phenolic end-float washers:** stack the 4 washers on the lower journal — **ARM-012 (small) against the bearing, then ARM-011 ×3**. (These set the rotor's axial position so the fan clears the housing floor. A matching set, **ARM-013 ×4**, goes on the upper journal at final join.)
2. Set the lower housing onto the armature so the journal passes through BRG-002; invert into a press.
3. **Press the slinger (ARM-010) onto the journal with slow incremental axial pressure — do NOT bottom it out.** Leave a running gap ≈ **0.0255"** (a knife-blade width); gauge with a feeler as you go.
   - *Tool:* a bench **arbor press** with a **tubular driver / deep socket / fender washer** whose bore clears the shaft and whose face bears on the slinger. **Never hammer.** (The restorer improvised with a reloading press + a 3/8"×1¼" fender washer; the principle is the same.)
4. **Join the housings:** install the stator (STR-001, two STR-008 screws), drop the armature in from the top, fit the ARM-013 ×4 upper washers against BRG-001, and torque the **two FLG-002 tie-bolts** (which also clamp the platform deck via the PLT-004 tubes).
5. **Deck → spindle → basket:** platform deck (PLT-001/002) → basket drive spindle (SPN-002, SPN-005 set screw) → mesh basket (BSK-002) bayonets on + lid → brushes (UH-004 caps) → oil cap → mount to the body.

### III.3.4 — Electrical: modern grounded rewire (R-5)
The control unit was rewired to a **modern, safe, serviceable standard** per the restoration philosophy. The as-found circuit was meter-verified into a 6-node map (see `LR-ELEC-002`), and the rebuild follows the corrected grounded schematic **`LR-ELEC-003`**.
- **Wire:** 18 AWG silicone (200 °C) throughout; a new **3-conductor grounded cord** with NEMA 5-15P plug.
- **Color code:** BLACK = hot, WHITE = neutral, **GREEN = ground only**, RED = motor forward, BLUE = motor reverse, YELLOW = motor speed/common, **RED-with-band** = heater/lamp return.
- **Junctions:** **Wago 221 lever connectors** at the distribution nodes (hot 5-port, neutral 3-port, return 3-port); motor legs on serviceable 2-wire joins; component leads on crimp/heat-shrink terminals. The **rheostat's two solder lugs** are the only soldered joints.
- **Ground bond (W-6):** green ring lug under a star washer to bright bare aluminum on the casting.
- **Switches:** the failed plunger (S1) and frayed toggle (S2) were replaced (same node roles).
> **CAUTION — the motor loom's green lead is a LIVE common, not ground.** Band it red at its junction so green never reads as ground in this machine.

### III.3.5 — Motor-lead entry: grommet, sheath anchor, strain relief
The four motor leads leave the sealed motor head and drop down the chrome pillar into the casting, where they pass a **bare aluminum edge at the housing/base entry**. This is a hard-earned lesson, not an optional nicety:

> **FIELD-FAILURE LESSON (specimen 13505).** During routing, the protective sheath over the motor leads slipped back at the housing entry and left a short length of the **WHITE lead bare**. That bare conductor touched the grounded aluminum base and **arced** on power-up. The ground system did exactly its job — the fault went line-to-ground and cleared, never energizing the chassis — but the lead had to be rebuilt. Root cause was purely mechanical: an unanchored sheath and no strain relief let the insulation migrate.

**Do this at the motor-lead entry, every time:**
1. **Grommet the pass-through.** Fit a rubber grommet (or high-temp silicone) in the entry opening so no conductor ever bears on a bare cast edge.
2. **Anchor the sheath.** Fix the protective sleeve so it **cannot slide back** off the conductors — a cable clamp, tie anchor, or adhesive-lined heat-shrink at the entry. The sheath must stay put under the pillar's routing tension.
3. **Add strain relief.** Secure the loom just inside the entry so any pull is taken by the jacket, not by the solder/crimp joints or the insulation at the edge.
4. **Re-inspect before closing up.** With the leads dressed, confirm no copper is visible anywhere along the run and that flexing the loom does not expose any.

---

## III.4 — Commissioning (cold-check & first power-on)

Never apply mains until the machine passes an unpowered cold-check.

**Stage 0 — cold checks (cord unplugged, DMM). All must pass:**
1. Ground pin ↔ bare chassis: **≤ 0.2 Ω** (near-zero over lead resistance).
2. Hot ↔ chassis, Neutral ↔ chassis, Ground ↔ hot, Ground ↔ neutral: all **O.L. (open)**.
3. Branch continuity: all-off = O.L.; rheostat on = motor winding + rheostat (tens–hundreds Ω, dropping as the knob advances); toggle on = **≈ 220 Ω** (heater R1 in parallel with the pilot lamp).

*As performed, Stage 0 caught and fixed two real faults — a marginally-seated Wago (added ~60 Ω series resistance) and a dead pilot bulb — which is exactly its purpose.*

**Stage 1 — first power-on.** The safest first power-up is through a current-limiting **dim-bulb tester + GFCI**; with Stage 0 fully passed and the motor already proven on a low-voltage DC bench supply, a direct power-on is a reasonable low-risk alternative. **Always start with the rheostat at OFF** (it is the motor's only on/off), plug in, then sweep the speed up (a soft-start that spares the plug, brushes, and commutator); return to OFF before unplugging.

**Result (S/N 13505):** motor runs and reverses cleanly, rheostat controls speed, heater warms the drying chamber (~160–200 °F), pilot lamp lit. Full function confirmed.

> **OPERATING SAFETY.** (1) The commutator sparks (normal for a brushed motor) — an ignition source — so **use non-flammable / water-based cleaning solutions and good ventilation**, never volatile solvent near the running motor. (2) Because the machine handles **liquids next to a mains motor, keep it on a GFCI** for all use.

---
*Figures to be finalized from `photos/` and `drawings/`. Confidence labels per the Document Production Standards. Full as-performed detail (products, provenance, per-photo figure notes) in `restoration-log.md`.*

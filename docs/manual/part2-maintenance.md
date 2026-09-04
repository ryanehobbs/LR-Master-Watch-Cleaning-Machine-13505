# Part II — Maintenance & Service
### L&R Master Watch Cleaning Machine · Master · S/N 13505

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from specimen S/N 13505 by Hobbs R.E., 2026. For reference only.

*Title block: Date June 12, 2026 · L&R Precision Cleaning Machine · Master · S/N 13505 · L&R MFG. CO. · Engineer Hobbs R.E.*

> ⚠️ **Best-judgment procedures.** No original L&R service sheet was available; maintenance below is reconstructed from this machine's design and general practice. Intervals are guidance, not factory spec.

---

## II.0 — Safety before servicing

- **Unplug the machine before any service** — it is live whenever plugged in (the speed knob is the only on/off).
- Treat the neck loom's **green wire as LIVE** (it is a motor branch, not a ground).
- After electrical work, run the **Stage-0 cold-checks** (II.4) before powering up.

---

## II.1 — Lubrication (the oiling system)

This is the **early oiled-bearing generation** — the sleeve bearings (BRG-001/002) are fed by a wool-yarn/felt wick system from an oil reservoir, **not** sealed-for-life. They need periodic oil.

- **Upper bearing:** lift the silver **"OIL" cap (UH-011)** on top of the motor dome and put a few drops of light machine oil (**Bramec Zoom Spout** or equivalent) onto the felt pad beneath it. Oil wicks down the internal yarn to the shaft. Replace the cap.
- **Lower bearing:** oil is fed through the wick/felt reservoir at the lower housing; add a few drops at the oil-wick port.
- **Frequency:** a few drops before extended use, or periodically with regular use. **Do not over-oil** — excess migrates onto the commutator/brushes.
- **Oil type:** light machine/turbine oil only. **Never oil the rubber jar seal** — condition rubber with silicone (Part III, III.2.2), never petroleum.

> The felt/yarn wicks must stay oil-saturated for the capillary feed to work. If a bearing runs dry or noisy, re-service the wick pack (Part III, III.3).

---

## II.2 — Brushes & commutator

The motor is a **brushed universal motor** — the carbon brushes are a wear item.

- **Access:** the two brush caps (**UH-004**) on the sides of the upper housing unscrew to withdraw each brush.
- **Inspect** for length (replace when worn short), free movement in the holder, and good spring tension. Keep spare carbon brushes on hand.
- **Commutator:** should be smooth and light-brown. Normal operation shows a small spark at the brushes, especially on start-up. **Heavy, continuous sparking or a ring of fire at steady speed** means service is due: clean the commutator (fine abrasive / commutator stick, clear the mica grooves between segments) and check brush seating.
- **After a rebuild**, new brushes spark more until they bed in to the commutator's curve — this settles with run time.

> ⚠️ Brush sparking is an ignition source — another reason for non-flammable solutions + ventilation (Part I, I.4).

---

## II.3 — Cleaning & finish care

- **Wrinkle finish (body + housings):** wipe with a soft cloth; blow dust from the texture. A light coat of **micro-crystalline wax (e.g. Renaissance Wax)**, buffed, protects and deepens the black without gloss. **Do not use WD-40 or oily dressings** on the finish — they go blotchy and attract dust.
- **Chrome (post/hardware):** wipe clean; wax lightly to protect. No abrasive polish on the plating.
- **Jewel/glass:** microfiber + a little glass cleaner; do not wax the lens face.
- **Jars & seal:** rinse jars between fluid changes; keep the rubber seal (PLT-002) pliable (silicone).

---

## II.4 — Electrical service & cold-checks

The control unit was rewired to a modern grounded standard — see the **as-built schematic `drawings/electrical/LR-ELEC-003`** (and the as-found `LR-ELEC-002` for the original circuit).

- **Junctions are serviceable:** the distribution nodes use **Wago 221 lever connectors** — open a lever to probe or re-land a wire without cutting. The rheostat's two lugs are the only soldered joints.
- **Color code:** BLACK hot · WHITE neutral · **GREEN ground only** · RED motor forward · BLUE motor reverse · YELLOW motor speed/common · **RED-with-band** heater/lamp return. (The motor loom keeps legacy colors; its green lead is a **live common**, banded red at its junction — not a ground.)
- **Pilot bulb:** a 120 V / 6 W lamp in parallel with the heater; if it fails the heater still works (independent pilot, not a fuse). Replace like-for-like.

**Stage-0 cold-checks (cord UNPLUGGED, DMM) — run after any electrical service, before power-on:**
1. Ground pin ↔ bare chassis: **≤ 0.2 Ω**.
2. Hot ↔ chassis · Neutral ↔ chassis · Ground ↔ hot · Ground ↔ neutral: all **O.L. (open)**.
3. All-off: hot ↔ neutral **O.L.**; rheostat on = motor winding + rheostat (drops as knob advances); toggle on = **≈ 220 Ω** (heater ∥ pilot).

**First power-up after service:** rheostat at OFF, ideally through a dim-bulb tester + GFCI; sweep the speed up as a soft-start.

---

## II.5 — Troubleshooting

| Symptom | Likely cause | Action |
|---|---|---|
| Motor won't start | Speed knob at OFF; no power; GFCI tripped; dry/stiff bearing | Sweep knob up from OFF; check outlet/GFCI; oil bearings; check brushes |
| Motor hums but won't turn | Only one field lead energized / a broken motor-leg connection | Check the motor-leg Wago joins (a Wago open removes a leg); verify with the schematic |
| Runs one direction only | Reverse (plunger) leg open | Check the plunger switch + its Wago/loom junction |
| Heavy sparking / ring of fire at commutator | Worn brushes, dirty/rough commutator | Service brushes + commutator (II.2) |
| No heat / drying chamber cold | Toggle off; heater branch open; R1 or connection fault | Toggle on (jewel should light); cold-check the heater branch (~220 Ω); re-seat the return Wago |
| Pilot lamp dark but heater works | Bulb burned out (independent pilot) | Replace the 120 V/6 W bulb |
| Bearing noisy / shaft binds | Reservoir wick dry; contamination | Oil the wick (II.1); if persistent, re-service the wick pack (Part III) |
| Fluid splashing out of the jar | Jar seal (PLT-002) hardened or mis-seated | Recondition/reseat the rubber seal (silicone) |
| GFCI trips on power-up | Ground fault in the wiring | Stop; re-run Stage-0 cold-checks; find the fault before retrying |

---

## II.6 — Reference

- **Wiring:** `drawings/electrical/LR-ELEC-003` (as-built) · `LR-ELEC-002` (as-found).
- **Mechanical drawings:** `drawings/components/` + `drawings/exploded/` (full motor + base package).
- **Parts:** Parts Dictionary + dimension CSVs in `docs/dimensions/`.
- **Full restoration detail:** `restoration-log.md`, `teardown-log.md`, and Part III of this manual.

---
*Maintenance intervals are guidance; adjust to use. Confidence labels per the Document Production Standards.*

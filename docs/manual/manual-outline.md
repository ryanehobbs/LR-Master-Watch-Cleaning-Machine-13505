# Shop Manual — Proposed Outline & Style Template
### L&R Master Watch Cleaning Machine, S/N 13505

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered and restored by Hobbs R.E., 2026, from direct physical measurement and hands-on restoration of specimen S/N 13505. For restoration reference only.

Derived from the survey in [`reference-survey.md`](reference-survey.md). The structure follows the classic L&R two-part spine (Operate / Maintain) and **adds a third part — Restoration — which the factory manuals never had.** That restoration part is where your firsthand knowledge lives; it is the heart of this document.

## Style template (apply to every section)
- **Title block** on every page footer (per CLAUDE.md standard): Date *June 12, 2026* · L&R Precision Cleaning Machine · Master · S/N 13505 · L&R MFG. CO. · Engineer Hobbs R.E.
- **Reproduction footer** on every page (verbatim text above).
- **Section banding:** each part gets a header tab (Operate / Maintain / Restore), L&R-style.
- **Procedure format:** bold title → optional *Trouble / Cause / Remedy* triad → numbered steps → inline **CAUTION** (caps) → **Helpful Hints** bullets.
- **Every part callout uses its canonical Part ID** (UH-003, ARM-006, STR-002…) tied to the Parts Dictionary; figures are our own SVGs/photos only.
- **Dimension provenance labels** carry through: (CONFIRMED) / (EST.) / (SYN).

---

## Front Matter
- Cover — machine photo (restored), model badge, title.
- Reproduction & originality statement; how to use this manual.
- **Table of Contents.**
- **Specifications** — 110 V AC, universal series motor, 2-pole; original 2-wire (now upgraded to 3-wire grounded); overall dimensions; U.S. Patent 1872812. *(model: Tempo 400 spec habit)*
- **What's in the box / parts inventory** — original complement: basket, jars, inserts, center column, cap/gasket, cord. *(model: Console carton checklist)*

## Part I — Operating Instructions
1. Setup & leveling; jar layout (cleaning / rinse positions); fluids (period-correct vs modern safe solvents).
2. Loading the basket; basket types & inserts.
3. The controls — one at a time: **Plunger switch (S1)**, **Toggle switch (S2)**, **Rheostat speed control (RH1)**, **Pilot lamp**. Each: what it does + a CAUTION. *(model: Console "Machine Controls")*
4. Running a cycle — clean → rinse → dry/spin-off; recommendations for best results.
5. **Solvent safety** (caps warning) — modern note replacing the original gasoline/benzine/chlorinated-solvent guidance.
   - *Primary source to transcribe here: the original 4-page L&R Master operating sheet (Source 5) once a clean copy is obtained.*

## Part II — Maintenance & Service
1. **Lubrication schedule** (calendar cadence): bearings (BRG-001/002), oil-wick & feed tube (LH-006), shaft journals — lube points, intervals, **Zoom Spout oil**. *(model: Tempo 400 Periodic Maintenance)*
2. **Motor service** — brush inspection/replacement (UH-003 brush ports, UH-004 caps, UH-005 set screws), commutator (ARM-006) care.
3. **Bearing & wick overhaul** — *(promote from our completed restoration notes)*; spherical sleeve bearings, merino reservoir packing, felt washer stack, Century TA-2226CS spring.
4. **Speed-control adjustment** — rheostat. *(model: Vari-Matic "Adjusting Basket Motor Speed")*
5. **Troubleshooting table** — Problem / Solution rows: won't run (check cord, brushes, rheostat), runs slow/erratic, no spin-off, etc. *(model: Console + Tempo 400)*
6. **Diagram pages (back of section):**
   - Machine Diagram & exploded parts list → **EXP-001 / EXP-002** + Parts Dictionary.
   - **Wiring Diagram** → schematic + harness routing + **wire schedule table (W-1…W-6)**.

## Part III — Restoration (the firsthand contribution)
*Written as a restorer's narrative + reusable procedures — the part you most want to share. Model: the myretrowatches "U-seal / hydraulic" writeup, but for our subsystems.*
1. **Assessment / as-found condition** — photos, what was wrong, the green-neck-wire LIVE hazard discovery.
2. **Cosmetic refinishing** — Citristrip strip → prep/mask → IPA wipe → self-etching primer → VHT Wrinkle Plus (H/V/diagonal) → heat-cure. *(R-2 written)*
3. **Cleaning** — general mild-soap ultrasonic for small parts; Citranox on some mesh basket pieces. *(R-3 written)*
4. **Gasket conditioning** — Citranox clean + silicone-oil soak; why not WD-40.
5. **Sleeve bearing & oil-wick rebuild** — full procedure with dimensions and the felt/spring/wick stack.
6. **Electrical overhaul** *(upcoming — the next active work):*
   - As-found verified schematic (ring-out with DMM).
   - 3-wire grounded rewire: cordage, chassis ground bond, silicone wire spec.
   - **Wire harness BOM (W-1…W-6)** + pre-cut/tin bench prep.
   - **Cold-check diagnostic matrix** (ground continuity, hot/neutral-chassis shorts, circuit continuity) before first power-on.
7. **Reassembly** — motor housing reinstallation (the designated "first procedure to fully document"): tools, techniques, step sequence, torque/fit notes.

## Appendices
- **A. Parts Dictionary / BOM** — canonical Part IDs + names (+ any known original L&R part numbers cross-referenced from the 1995 list).
- **B. Confirmed dimensional dataset** — the 5 CSVs.
- **C. Drawing index** — the 9-sheet SVG package.
- **D. Materials & consumables** — paint, solvents, oil, wick/felt, spring, cordage, wire.
- **E. References & attribution** — the surveyed L&R manuals (Vari-Matic, Tempo 400, Console, U-seal sheet) and forum/archive links, cited as influences. No reproduced figures.

---

## Build order (suggested)
1. Lock this outline with the user.
2. Draft **Part III (Restoration)** first — it's mostly written already inside CLAUDE.md and it's the unique value. Convert each COMPLETE phase into a formatted procedure.
3. Slot in **Part II** (maintenance/troubleshooting/diagrams) — reuses existing drawings + harness BOM.
4. Draft **Part I** once the original Master operating sheet (Source 5) is obtained for accurate primary content.
5. Decide output format (Markdown source → PDF/`docx` for distribution) and the repo LICENSE before publishing.

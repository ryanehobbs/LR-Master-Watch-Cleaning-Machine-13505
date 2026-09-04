# Gemini Rev-Bump Prompts — ARM-013 callout (B2) + title-block rename (B3) — 2026-06-23

Purpose:
- **B2** — add **ARM-013** (upper-journal phenolic end-float washer stack, ×4) to **ARM-001**, **EXP-001**, **EXP-002**. Mirror of the lower-journal ARM-011/012 set added in the 2026-06-20 pass.
- **B3** — correct the title-block model nomenclature **"Mark 1 Master" → "Master"** ("Mark 1/2/3" is collector shorthand, NOT L&R factory nomenclature; only "L&R" / "MASTER" is cast on the machine).

**Feed each prompt to Gemini together with the current SVG named in the prompt.** After export:
strip any `.svg.svg` double extension; no `--` (double hyphen) inside SVG comments; keep the 1200x800
master template + standard title block; bump the Rev letter and add the revision note.

**Standard title-block fields:** Date June 12 2026 · Product L&R Precision Cleaning Machine ·
**Model Master** · Serial 13505 · Manufacturer L&R MFG. CO. · Engineer Hobbs R.E.
**Reproduction annotation** must remain on every sheet.

**⚠️ TWO TITLE-BLOCK FIXES already applied to the other 10 sheets — apply them on these re-renders too:**
1. **DATE must read exactly `June 12, 2026`** (earlier Gemini exports drifted to June 13/14 — do not restamp the current date).
2. **DRAWING TITLE value must NOT overflow into the PART NUMBER / ID cell.** On the header-style title block the "DRAWING TITLE" value (monospace 12px at x=765) was running past the x=965 cell divider over the "PART NUMBER / ID" value at x=975. Constrain it to its cell — keep the full title text but fit it (e.g. `font-size="10px" textLength="185" lengthAdjust="spacingAndGlyphs"`, or shrink the font so the longest title ends before x=955). (EXP-001/002 use a wide title row with no Part Number cell, so no overlap there — just keep the date fix.)

**ARM-013 spec (all CONFIRMED):** phenolic, non-conductive, oil/heat-resistant; **QTY 4, ALL IDENTICAL**
(no 3+1 split, unlike the lower ARM-012). **OD 0.4705"**, **bore 0.2500"** (slip-fit on the upper journal
SHF-002 Ø0.250"), **thickness 0.0175" each**, **4-stack = 0.070"**. Function: end-float / axial-spacing
shim stack on the UPPER journal, riding against the UPPER bearing (BRG-001) at the commutator end — sets
the rotor's top-end axial position (upper-end mirror of the lower ARM-011/012 stack).

---

## 1) ARM-001 Armature Assembly — Rev E -> Rev F   (B2 + B3)
Source file: `drawings/components/ARM-001_Armature_Assembly_Rev_E.svg`

Add the **upper-journal** phenolic end-float washer stack on **SHF-002** (the commutator / upper-bearing end):

- New part: **ARM-013 — Phenolic End-Float Washer (Upper), QTY 4 (all identical)**: OD **0.4705"**, bore
  **0.2500"**, thickness **0.0175"** each; 4-stack **0.070"**.
- Placement/order on the upper journal SHF-002: thin slip-on washer stack near the upper-bearing end,
  riding against **BRG-001** — between the upper brass collar (**ARM-008**) region and the top journal end
  / upper-bearing location. (This is the exact mirror of how ARM-011/012 sit on the lower journal against
  BRG-002.)
- Leader callout: `ARM-013 PHENOLIC WASHER x4 (ALL IDENTICAL) — OD 0.4705" / BORE 0.2500" / THK 0.0175" EA
  (CONFIRMED)`, plus a stack note `4-WASHER END-FLOAT STACK = 0.070"; SETS ROTOR TOP-END AXIAL POSITION
  AGAINST BRG-001`.
- Note to distinguish the three phenolic stacks: "ARM-013 = UPPER journal (against BRG-001); ARM-011 x3 +
  ARM-012 = LOWER journal (against BRG-002); all phenolic, non-conductive." Keep ARM-010/011/012 as drawn.
- **B3 title-block fix:** change the Model field from **"Mark 1 Master" to "Master"** (and any header text
  "MARK 1 MASTER..." to "MASTER...").
- Title block: **Rev F**. Revision note: "Rev F: added ARM-013 x4 phenolic upper-journal end-float washer
  stack on SHF-002 (against BRG-001); model nomenclature corrected to Master."

---

## 2) EXP-001 Motor Exploded (2D profile) — Rev E -> Rev F   (B2 + B3)
Source file: `drawings/exploded/EXP-001_Motor_Exploded_Rev_E.svg`

Insert the 4 upper-journal phenolic washers into the exploded UPPER-journal sequence:

- In the vertical exploded stack (UH-001 -> STR-001 -> BRG-001 -> ARM-001 ...), the upper journal of
  ARM-001 meets **BRG-001**. Insert **ARM-013 x4** on the upper journal **between BRG-001 and the armature
  upper journal** (commutator end) — the mirror of the ARM-011/012 stack already shown on the lower journal
  between ARM-001 and BRG-002.
- Draw as thin discs on the common centerline with a leader callout + Part ID (`ARM-013 PHENOLIC x4`);
  keep dims compact — full dims live on ARM-001.
- **B3 title-block fix:** Model "Mark 1 Master" -> "Master" (and any "MARK 1 MASTER..." header -> "MASTER...").
- Title block: **Rev F**. Revision note: "Rev F: inserted ARM-013 x4 phenolic washer stack between BRG-001
  and the ARM-001 upper journal; model nomenclature corrected to Master."

---

## 3) EXP-002 Motor 3D Exploded (axonometric showcase) — Rev E -> Rev F   (B2 + B3)
Source file: `drawings/exploded/EXP-002_Motor_3D_Exploded_Rev_E.svg`

Same insertion as EXP-001, in the 3D axonometric stack:

- Add the **4 ARM-013 washers** as scaled ellipse discs (depth-projected like the other parts) on the
  upper journal, **between BRG-001 and the armature upper journal** (commutator end): ARM-012/011 stack
  stays on the lower journal.
- Render in a phenolic-look finish (reddish-brown / amber, matte), distinct from brass (ARM-010) and steel
  (bearings); tether to the central alignment guideline like the other elements.
- Leader callout with Part ID (`ARM-013 PHENOLIC x4`). Keep ARM-010 as the external brass slinger and the
  lower ARM-011/012 stack as drawn.
- **B3 title-block fix:** Model "Mark 1 Master" -> "Master" (and any "MARK 1 MASTER..." header -> "MASTER...").
- Title block: **Rev F** (date stays June 12 2026 per standard). Revision note: "Rev F: added ARM-013 x4
  phenolic upper-journal end-float washer stack on the upper journal; model nomenclature corrected to Master."

---

## B3 — title-block rename on the remaining 9 sheets (nomenclature only)
These sheets need ONLY the "Mark 1 Master" -> "Master" correction (no geometry change). Either run them
through Gemini one rev each, OR (faster, deterministic) apply the text substitution directly in the SVG and
bump the rev. Sheets + rev bumps:

| Sheet | Rev bump |
|---|---|
| BRG-001 Upper Bearing | D -> E |
| BRG-002 Lower Bearing | C -> D |
| BSK-002 Mesh Basket | C -> D  *(see special note)* |
| HW-001 External Hardware | F -> G |
| LH-001 Lower Housing | F -> G |
| PLT-001 Platform Seal Deck | C -> D |
| SPN-002 Basket Drive Spindle | C -> D |
| STR-001 Stator Assembly | Q -> R |
| UH-001 Upper Housing | K -> L |

For each: change Model **"Mark 1 Master" -> "Master"**; change any header "MARK 1 MASTER CLEANING MACHINE"
-> "MASTER CLEANING MACHINE" and "MARK 1 MASTER" -> "MASTER". Revision note: "Rev X: model nomenclature
corrected to Master (Mark 1/2/3 is collector shorthand, not factory)."

**⚠️ BSK-002 SPECIAL NOTE — do NOT blind-replace.** BSK-002 carries a technical note:
`Nominal basket dia for this system (Mark 1 Master) = 2 3/4" (2.750");`
Reword to keep the size fact but drop the model-name implication, e.g.:
`Nominal basket dia for this (early/large-basket) generation = 2 3/4" (2.750"); later units used 2 1/4".
(Mark 1/2 = collector shorthand, not L&R factory nomenclature.)`

---

### After Gemini renders (housekeeping)
- Save into `drawings/components/` and `drawings/exploded/`; strip `.svg.svg`.
- Archive superseded files to `archive/old_svg/`.
- Refresh the `.svg.txt` source snapshots in `drawings/source/`.
- Update the CLAUDE.md drawing table + close ledger B2/B3.

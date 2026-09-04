# Gemini Rev-Bump Prompts — Phase 1 Drawing Callouts (2026-06-20)

Purpose: add three parts that are in the BOM/logs but not yet on the engineering sheets —
**BRG-011** (lower-housing retaining ring), **ARM-011 ×3 + ARM-012 ×1** (phenolic end-float washers).

**Feed each prompt to Gemini together with the current SVG named in the prompt.** After export:
strip any `.svg.svg` double extension; no `--` (double hyphen) inside SVG comments; keep the 1200x800
master template + standard title block; bump the Rev letter in the title block and add the revision note.

**Standard title-block fields (unchanged):** Date June 12 2026 · Product L&R Precision Cleaning Machine ·
Model Master · Serial 13505 · Manufacturer L&R MFG. CO. · Engineer Hobbs R.E.
**Reproduction annotation** must remain on every sheet.

---

## 1) BRG-002 Lower Bearing — Rev B → Rev C
Source file: `drawings/components/BRG-002_Lower_Bearing_Rev_B.svg`

Add the bottom-of-pocket retaining ring that seats below this bearing in the lower housing:

- New part: **BRG-011 — Metal Retaining Ring** (lower housing only).
- Dimensions (all CONFIRMED): **OD 0.500"**, **ID 0.295"**, **thickness 1/16" (0.0625")**.
- Function/placement: a friction-fit flat metal ring installed at the very bottom of the lower-housing
  bearing pocket, capturing the small felt washer (BRG-010) and retaining the bearing stack. It is
  tapped flush with a brass punch on install.
- Draw it as a small flat ring in section + plan, with a leader callout `BRG-011 METAL RETAINING RING —
  OD 0.500" / ID 0.295" / THK 1/16" (CONFIRMED)`, positioned at the bottom of the bearing-pocket stack.
- Add a note: "BRG-011 is LOWER housing only; the upper housing has no bottom retaining ring."
- Title block: Rev C. Revision note: "Rev C: added BRG-011 retaining ring callout (bottom of pocket)."

---

## 2) LH-001 Lower Housing — Rev E → Rev F  (optional if BRG-002 Rev C covers it)
Source file: `drawings/components/LH-001_Lower_Housing_Rev_E.svg`

In the bearing-pocket cross-section, show **BRG-011** seated at the base of the pocket:

- Same part/dims as above (OD 0.500" / ID 0.295" / THK 1/16", CONFIRMED).
- Place it at the bottom of the pocket below where BRG-002 + felt washers sit; thin flat ring in the
  section view, with a leader `BRG-011 RETAINING RING (FRICTION-FIT)`.
- Title block: Rev F. Revision note: "Rev F: show BRG-011 retaining ring seated at base of bearing pocket."

---

## 3) ARM-001 Armature Assembly — Rev D → Rev E
Source file: `drawings/components/ARM-001_Armature_Assembly_Rev_D.svg`

Add the lower-journal phenolic end-float washer stack on **SHF-003** (ARM-010 is already shown):

- New parts (all phenolic, non-conductive, oil/heat-resistant; bore slip-fits SHF-003 Ø0.280"):
  - **ARM-011 — Phenolic End-Float Washer (Large), QTY 3**: OD **0.630"**, bore **0.285"**, thickness **0.017"** each.
  - **ARM-012 — Phenolic End-Float Washer (Small), QTY 1**: OD **0.500"**, bore **0.285"**, thickness **0.016"**.
  - Combined 4-washer stack thickness **0.065"** (CONFIRMED).
- Placement/order on the lower journal SHF-003: these are INTERNAL washers that seat ON TOP of the
  lower bearing (BRG-002). Order, from the bearing toward the armature: **ARM-012 (small, closest to the
  bearing) → ARM-011 ×3**. Draw them as a thin slip-on washer stack on the lower journal, between the
  fan-end collar (ARM-009) region and the bearing/ARM-010 location.
- Leader callouts: `ARM-011 PHENOLIC WASHER x3 — OD 0.630" / BORE 0.285" / THK 0.017" EA (CONFIRMED)`
  and `ARM-012 PHENOLIC WASHER x1 — OD 0.500" / BORE 0.285" / THK 0.016" (CONFIRMED)`, plus a stack note
  `4-WASHER END-FLOAT STACK = 0.065"; SETS FAN (ARM-007) CLEARANCE ABOVE HOUSING FLOOR`.
- Note to distinguish from ARM-010: "ARM-011/012 are INTERNAL (on top of BRG-002); ARM-010 is the
  EXTERNAL brass slinger below the housing." Keep ARM-010 as already drawn.
- Title block: Rev E. Revision note: "Rev E: added ARM-011 x3 + ARM-012 phenolic end-float washer stack on SHF-003."

---

## 4) EXP-001 Motor Exploded (2D profile) — Rev D → Rev E
Source file: `drawings/exploded/EXP-001_Motor_Exploded_Rev_D.svg`

Insert the 4 phenolic washers into the exploded lower-journal sequence:

- Sequence on the lower journal (top=armature side, going down toward the basket):
  `ARM-001 lower journal → ARM-011 x3 → ARM-012 → BRG-002 (in LH-001) → [journal protrudes] → ARM-010 (external slinger) → SPN-002 spindle …`
- So the 4 washers go BETWEEN the armature lower journal and BRG-002, with **ARM-012 adjacent to BRG-002**
  and the **3x ARM-011 above it**. ARM-010 stays on the far (basket) side of BRG-002/LH-001.
- Draw them as thin discs on the common centerline with leader callouts and Part IDs (ARM-011, ARM-012);
  keep dims compact (`ARM-011 PHENOLIC x3`, `ARM-012 PHENOLIC x1`) — full dims live on ARM-001.
- Title block: Rev E. Revision note: "Rev E: inserted ARM-011 x3 + ARM-012 phenolic washer stack between ARM-001 lower journal and BRG-002."

---

## 5) EXP-002 Motor 3D Exploded (axonometric showcase) — Rev D → Rev E
Source file: `drawings/exploded/EXP-002_Motor_3D_Exploded_Rev_D.svg`

Same insertion as EXP-001, in the 3D axonometric stack:

- Add the 4 phenolic washers as scaled ellipse discs (depth-projected like the other parts) on the lower
  journal, between the armature and BRG-002: **ARM-012 nearest BRG-002, ARM-011 x3 above it.**
- Render them in a phenolic-look finish (reddish-brown/amber, matte) distinct from the brass ARM-010
  slinger and the steel bearing; tether to the central alignment guideline like the other elements.
- Leader callouts with Part IDs (ARM-011 x3, ARM-012 x1); keep ARM-010 as the external brass slinger.
- Title block: Rev E (date stays June 12 2026 per standard). Revision note: "Rev E: added ARM-011 x3 + ARM-012 phenolic end-float washer stack on lower journal."

---

### After Gemini renders (housekeeping)
- Save into `drawings/components/` (sheets 1-3) and `drawings/exploded/` (sheets 4-5); strip `.svg.svg`.
- Archive the superseded Rev D/E/B files to `archive/old_svg/`.
- Refresh the `.svg.txt` source snapshots in `drawings/source/`.
- Update the CLAUDE.md drawing table + REWORK QUEUE (mark BRG-011 / ARM-011/012 callouts DONE).

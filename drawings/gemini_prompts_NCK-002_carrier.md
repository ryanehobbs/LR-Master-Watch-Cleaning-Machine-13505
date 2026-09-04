# Gemini Prompt — NCK-002 Motor-Mount Carrier (new drawing, route A to B)

**Feed this prompt to Gemini together with the draft seed SVG:**
`drawings/components/NCK-002_MotorMount_Carrier_Rev_A_DRAFT.svg`

After export: strip any `.svg.svg` double extension; no `--` (double hyphen) inside SVG comments; save as
`drawings/components/NCK-002_MotorMount_Carrier_Rev_A.svg` (drop the DRAFT/SEED wording in the header + title block); keep the master template + standard title block.

**Standard title-block fields:** Date June 12 2026 · Product L&R Precision Cleaning Machine · Model Master ·
Serial 13505 · Manufacturer L&R MFG. CO. · Engineer Hobbs R.E. **Reproduction annotation stays on the sheet.**

---

## PROMPT

Render a clean, professional vintage-style mechanical engineering drawing of the part in the attached draft SVG: the **NCK-002 Motor-Mount Carrier** for an L&R Master watch-cleaning machine. The draft is a rough dimensioned seed — reproduce the SAME part and SAME dimensions, but render it properly (accurate proportions to the dims below, clean orthographic views, professional dimensioning, cast-part shading with soft radii and draft angles).

**What the part is (for correct form):**
A small cast bracket. A **square sleeve** (socket) slides onto the square top of the post (NCK-001). The BOTTOM of the sleeve is a **split clevis clamp**: a saw-cut slot through one side, closed by a cross screw (NCK-003) to grip the post. The TOP of the carrier is an **open concave saddle** that cradles the ROUND upper motor housing (UH-001). Two flat **mount ears** wing out to the sides, each with a **counterbored** hole; two screws pass through into the round housing's two mount holes to retain the motor. A small **alignment tab / key** protrudes from one edge of the sleeve. Sand-cast aluminium: soft radiused edges, draft angles, no crisp machined corners except the bored/tapped holes and the square bore.

**Views to draw (2 or 3 orthographic):**
- **TOP / PLAN** (looking down the post axis): square sleeve outline, the central square bore, the two mount ears with their counterbored holes, the alignment tab, and the saddle opening.
- **FRONT ELEVATION**: the sloped hump profile (low at the ends, high at the center saddle), the concave saddle notch at top, the square sleeve, and the split clevis clamp at the base with its tightener holes + slot.
- **(optional) SIDE ELEVATION or a section** through the sleeve/clevis if it helps clarity.

**Dimensions (all CONFIRMED by caliper unless noted) — label these on the views:**
- Square bore (post fit), inside across-flats: **1.26"** (fit-critical)
- Square sleeve body: outer width **2.232"**, body height **~1.67"**
- Overall length across the two ears: **3.04"**
- Mount holes (x2), stepped/counterbored: **0.300-0.305" thru / 0.565" counterbore** (seats screw head); spacing **2.30" center-to-center**
- Alignment tab: base width **0.300"**, tip width **0.1975"** (tapered), protrusion/height **0.3905"**
- Split clevis clamp: total opening width **0.622"**, internal slot gap **0.102"**; tightener holes **0.450" clearance** (one ear) / **0.305" threaded** (other ear) for NCK-003
- Overall envelope: length **3.04"** x depth **2.232"** x height **0.95" at the ends sloping to 1.50" max at the center**; mounting-ear plate thickness **0.25"**
- Saddle cradle: **open concave** (no bore dim); concave radius = the OD of the round upper housing UH-001 it seats (**~R1.60"**, from UH-001 outer dia 3.200") — label as `(SYN, = mating UH-001 OD)`.

**Confidence labels:** put `(CONFIRMED)` on the measured dims; the saddle radius is `(SYN)`.

**House standard:**
- Canvas **1200 x 800** engineering border; header strip top; title block bottom-right, notes box bottom-left.
- Header: "NCK-002  MOTOR-MOUNT CARRIER  —  L&R MASTER 13505" + "NCK-002 Rev A" at right.
- Notes: keep the function notes (1-3) and the reproduction annotation verbatim.
- Title-block fields as listed above; Drawing/Rev = NCK-002 / Rev A — FIRST ISSUE.
- All part callouts use canonical IDs (NCK-002 the carrier, NCK-001 post, NCK-003 clamp screw, UH-001 upper housing).
- Output valid SVG. No `--` inside SVG comments.

Return only the finished SVG.

---

### After Gemini renders (housekeeping)
- Save into `drawings/components/` as `NCK-002_MotorMount_Carrier_Rev_A.svg`; strip any `.svg.svg`; delete/keep the DRAFT seed as you prefer.
- Refresh the `.svg.txt` source snapshot in `drawings/source/`.
- Update the CLAUDE.md drawing table (add NCK-002 Rev A) + memory.
- Sanity-check: all dims above present + correct; Part IDs correct.

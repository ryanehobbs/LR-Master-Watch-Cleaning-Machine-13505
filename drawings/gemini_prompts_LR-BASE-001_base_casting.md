# Gemini Prompt — LR-BASE-001 Base Casting Rev B (route A to B)

**Feed this prompt to Gemini together with the draft seed:**
`drawings/source/LR-BASE-001_Base_Casting_Rev_B_DRAFT.svg.txt`

After export: strip any `.svg.svg` double extension; no `--` (double hyphen) inside SVG comments; save as
`drawings/components/LR-BASE-001_Base_Casting_Rev_B.svg` (drop the DRAFT/SEED wording); keep master template + title block.
Remove any `[cite: N]` citation artifacts Gemini may insert into text.

**Standard title-block fields:** Date June 12 2026 · Product L&R Precision Cleaning Machine · Model Master ·
Serial 13505 · Manufacturer L&R MFG. CO. · Engineer Hobbs R.E. **Reproduction annotation stays on the sheet.**

---

## PROMPT

Render a clean, professional vintage-style mechanical engineering drawing of the part in the attached draft SVG: the **LR-BASE-001 Base Casting** of an L&R Master watch-cleaning machine. The draft is a rough dimensioned seed — reproduce the SAME part and SAME dimensions, but render it properly: accurate proportions to the dims below, clean orthographic views, professional dimensioning, and cast-part shading (sand-cast: soft radiused edges, draft angles, NO crisp machined corners except the drilled/tapped holes and the square post socket).

**What the part is (for correct form):**
A large sand-cast aluminium body. Rounded-rectangle plan with a squared rear wall (rounded corners) and STRAIGHT left/right sides; the bottom transitions via a gentle S-curve into a forward, teardrop/paddle **control tongue**, then curves to a broad rounded bottom. It holds **4 wells in a 2x2 square grid** (4.500" pitch): the front-left is the **HEATER WELL** (a tall raised tube), the other three are equal **JAR BAYS**. A central **square post socket** (BAS-006) sits between the 4 wells. The forward **tongue** carries the controls: a rheostat knob on a FLAT face (no recess), a jewel lamp (upper-left), a plunger button (upper-right), and a toggle on the LEFT SIDE FACE; cast relief lettering "L&R MASTER" in a smile arc plus "OFF" and "ON" with a sweep arrow. The casting rests on **3 raised feet** (2 rear corners + 1 front under the tongue). An AC grommet hole is on the REAR wall.

**Views to draw:**
- **PLAN VIEW** (top-down, rear wall at top, forward tongue at bottom): body outline, the 4 wells (heater front-left, 3 jar bays), central square post socket, the tongue with its control holes + cast lettering, and the 3 feet.
- **FRONT ELEVATION**: the tall heater tube rising from the body, the body block, jar-well rims, the forward tongue ramp, the 3 feet, and the rear-wall grommet.
- (optional) a SIDE ELEVATION or partial SECTION through the heater well if it aids clarity.

**Dimensions (all CONFIRMED by caliper unless noted) — label on the views:**
- Body: width **8.875"** (L-R) x depth **9.375"** (rear to well-cluster front, excl. tongue) x height **2.875"**; overall depth with tongue **12.875"**; wall thickness **0.280"**; feet **0.350"** proud (3 pads).
- Wells (2x2 grid): **4.500"** pitch (X and Y, square); cluster diagonal **6.364"**.
- Jar bays (x3): bore **3.955"**, depth **1.925"**, floor **0.800"** above base bottom, wall **0.300"**; jar OD ref 3.830".
- Heater well (front-left): total height **7.375"**, tube above body **4.500"**, top lip ID **3.268"**, interior bore **3.800"** (NOTE: SMALLER than the jar bays, it is the taller well not wider), bore depth rim to cast-top ledge **4.9075"**, lower section (R1 gap) **2.550"**, wall **0.120"**, floor opening **3.80"** (full bore), R1 bracket screw hole **0.190"**.
- Post socket BAS-006: square inside across-flats **1.300"** (fit-critical), depth **2.9035"** (near full body height); NO oil/access bore; retained by **6 screws in 2 groups** (4 SET screws: one large 3/8 + three 1/2in #10; plus 2 POST-penetrating screws ~#5-6).
- Tongue BAS-004: widths **4.80"** (at body) / **3.80"** (middle) / **2.00"** (front tip); projection **3.500"**; face ramp **26.6 deg**; rheostat on a FLAT face (NO cast recess); rheostat shaft hole **0.395"**; jewel, plunger, and toggle holes **0.490"** each.
- Grommet BAS-007: on the REAR wall, centered (~4.5" lateral); hole center **1.000"** up from the foot plane; stepped bore **0.400"** inner / **0.595"** outer.
- Cast relief lettering BAS-005 (for repro): "L&R MASTER" smile arc chord **3.138"**, letter cap height **0.489"**, struck ~R**2.75"**; "OFF" width **0.63"**; "ON" sweep arrow ~**0.625"** long. Typeface: mid-century condensed sans (Franklin Gothic Condensed / News Gothic).

**Confidence labels:** `(CONFIRMED)` on measured dims. Note the corrections vs the old Rev A plan view: heater bore is SMALLER than jars (not larger); rheostat is on a FLAT face (no recess); NO oil bore in BAS-006; the body is ROUNDED sand-cast (not squared).

**House standard:**
- Canvas **1200 x 800** engineering border; header strip top; title block bottom-right; notes box bottom-left.
- Header: "LR-BASE-001  BASE CASTING  —  L&R MASTER 13505" + "LR-BASE-001 Rev B" at right.
- Reproduction annotation verbatim: "REPRODUCTION DOCUMENT — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from direct physical measurement of specimen S/N 13505. Curated by Hobbs R.E., 2026. Reference only."
- Title-block fields as listed; Drawing/Rev = LR-BASE-001 / Rev B — supersedes the old plan-view Rev A.
- Canonical Part IDs where labeled (BAS-002 heater well, BAS-003 jar bay, BAS-004 tongue, BAS-005 lettering, BAS-006 post socket, BAS-007 grommet).
- Output valid SVG. No `--` inside comments. No `[cite: N]` artifacts in text.

Return only the finished SVG.

---

### After Gemini renders (housekeeping)
- Save into `drawings/components/` as `LR-BASE-001_Base_Casting_Rev_B.svg`; strip `.svg.svg`; remove any `[cite: N]`.
- Refresh the `.svg.txt` source snapshot; archive this DRAFT seed to `archive/old_svg/` for 1:1 parity.
- The old root-folder plan-view `LR-BASE-001_Base_Casting.svg` (Rev A) is superseded; archive it too.
- Update the CLAUDE.md drawing table (add LR-BASE-001 Rev B) + memory.
- Sanity-check: all dims above present + correct; corrections reflected; Part IDs correct.

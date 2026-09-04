# Gemini Prompt — Polish/Render LR-ELEC-003 (Control Unit As-Built Rewire)

**Feed this prompt to Gemini together with the source SVG:**
`drawings/electrical/LR-ELEC-003_ControlUnit_AsBuilt_Rewire_Rev_A.svg`
(or the text snapshot `drawings/source/LR-ELEC-003_ControlUnit_AsBuilt_Rewire_Rev_A.svg.txt`)

After export: strip any `.svg.svg` double extension; no `--` (double hyphen) inside SVG comments; keep it Rev A (this is a cosmetic re-render of an unpublished first issue, not a content change).

---

## PROMPT

You are cleaning up and re-rendering an existing electrical schematic SVG (attached). This is a METER-VERIFIED as-built wiring schematic for a vintage watch-cleaning machine. Produce a polished, professional engineering-schematic version.

**ABSOLUTE RULES — do not change the electrical content:**
- Preserve EVERY connection, wire, and node EXACTLY as in the source. Do not add, remove, reroute, or "correct" any connection. The circuit is verified correct.
- Preserve all node labels exactly: **N1 (neutral), N2 (hot), N3 (heater/lamp return), N4 (motor forward), N5 (motor speed/common), N6 (motor reverse).**
- Preserve all component IDs and values exactly: **R1/CTL-007 (220 Ohm Ohmite P/N 33974, ~65W), DS1/CTL-005 (120V 6W pilot), S1/CTL-003 (plunger transfer switch, a=forward/OUT, c=reverse/IN, d+b=hot common), S2/CTL-004 (heater switch, SPST), RV1/CTL-001 (425 Ohm IRC rheostat, wiper + CCW, full CCW=OFF), M1 (universal series motor), P1/CTL-008 (3-wire NEMA 5-15P cord).**
- Preserve the WIRE COLORS exactly (they are meaningful): BLACK=hot(N2), WHITE/gray=neutral(N1), GREEN=ground only, RED=motor forward(N4), BLUE=motor reverse(N6), YELLOW/amber=motor speed-common(N5), RED-with-band(dashed)=heater/lamp return(N3).
- Preserve the ground system: 3-wire grounded inlet (L/N/G), the W-6 chassis bond (green ring lug to bare casting) drawn as a ground symbol.
- Preserve the Wago 221 junction callouts at N2 (5-port), N1 (3-port), N3 (3-port), and the "loom green = LIVE common, band red" caution at N5.
- Preserve ALL notes text (1 through 6) and the color key verbatim in meaning.

**WHAT TO IMPROVE (visual only):**
- Clean, evenly-spaced layout; eliminate any label overlaps or crowding; align components on a tidy grid.
- Use proper schematic symbols: resistor zigzag for R1 and the rheostat RV1 (with wiper arrow), an X-in-circle for the lamp DS1, a labeled box for the plunger transfer switch S1, a standard SPST symbol for S2, a circle for motor M1, a standard earth-ground symbol for the chassis bond.
- Make the two horizontal rails (N2 hot top, N1 neutral bottom) clean and clearly labeled; show the three Wago distribution nodes as neat labeled connectors.
- Keep it clean line-art on white; colored strokes only for the wire colors above. Legible monospaced or clean sans-serif labels.

**HOUSE STANDARD (keep):**
- Canvas 1200 x 820 engineering border with a header strip across the top reading: "L&R PRECISION CLEANING MACHINE  —  CONTROL UNIT  —  AS-BUILT 3-WIRE GROUNDED REWIRE (R-5)" and "LR-ELEC-003  Rev A" at the right.
- Keep the NOTES block and the TITLE BLOCK (bottom). Title-block fields: Product = L&R Precision Cleaning Machine; Model = Master; Serial = 13505; Manufacturer = L&R MFG. CO.; Engineer = Hobbs R.E.; Date = June 12, 2026; Drawing/Rev = LR-ELEC-003 / Rev A — FIRST ISSUE (as-built + commissioned).
- Keep the REPRODUCTION annotation verbatim: "REPRODUCTION DOCUMENT — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from direct physical measurement of specimen S/N 13505. Curated by Hobbs R.E., 2026. Reference only."
- Output valid SVG. No `--` inside SVG comments.

Return only the finished SVG.

---

### After Gemini renders (housekeeping)
- Save into `drawings/electrical/`; strip any `.svg.svg` double extension.
- If content unchanged (cosmetic only), keep the same filename/Rev A and archive the Claude-authored source to `archive/old_svg/` if you prefer the Gemini render as the master; OR keep both and note which is the published master.
- Refresh the `.svg.txt` source snapshot in `drawings/source/`.
- Sanity-check: every node (N1-N6), every value, every wire color, and all 6 notes must match the original. If Gemini altered any connection or label, reject and re-run.

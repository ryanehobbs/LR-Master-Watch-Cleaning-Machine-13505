# L&R Master Watch Cleaning Machine (Vintage) — Restoration Master Log

## Workspace Structure (refactored 2026-06-14 for GitHub publication)
This project was migrated from the old flat `Pictures\LR Watch Cleaner Restoration` layout into a clean repo structure. Canonical paths:

| Path | Contents |
|---|---|
| `docs/dimensions/` | The 5 dimensional CSVs (parts dictionary / BOM + per-assembly measurements) |
| `docs/manual/` | Workshop manual (future) |
| `drawings/components/` | 7 component blueprints (UH-001, LH-001, BRG-001/002, ARM-001, STR-001, HW-001) |
| `drawings/exploded/` | EXP-001 (2D profile) + EXP-002 (3D axonometric) |
| `drawings/source/` | `.svg.txt` plain-text snapshots of each sheet |
| `photos/` | Bench photos by subsystem: `housing/` `armature/` `bearings/` `stator-wiring/` `gasket/` `basket/` `hardware/` `control-stack/` `concept-renders/` |
| `reference/` | External manuals, archive PDFs, styling refs (incl. IMG_1646.PNG) |
| `archive/` | Superseded drafts / working backup — git-ignored, not published |
| `README.md` / `.gitignore` | Repo scaffolding |

**Photo-classification corrections applied during the refactor (per-image agent audit):**
- The old `Stater Assembly Breakdown` folder was misnamed — its 14 photos are the ARMATURE (rotor), now in `photos/armature/`.
- 3 hardware shots (carbon brush + 2 brush-cap/set-screw photos) moved out of wiring → `photos/hardware/`.
- 1 stator-coil shot (IMG_1581) moved from housing → `photos/stator-wiring/`.
- Cleanup candidates noted (not deleted): 3 duplicate armature pairs (`…_1.jpeg`), IMG_1669 blank caliper frame.

(Old path retained as untouched backup until verified.)

---

## ⭐ ACTION BOARD — master TODO index (updated 2026-06-16, evening stop)
Single place to see what's open. Detailed context lives in the REWORK QUEUE (under NEXT SESSION PICKUP) and the `docs/manual/` checklists; this board is the index of what to tackle.

### 📋 LIVE OPEN-ITEMS LEDGER (updated 2026-06-23 — THIS is the current TODO; supersedes older items below)
**▶▶ SESSION CLOSE 2026-06-23 — MOTOR / POWER HEAD 100% COMPLETE.** Mechanically assembled (Phase 2), electrically wired (R-11), bench-tested + reversing confirmed (R-10, photo+video), all 12 drawings at current revs, all photos curated. **No motor work remains.** Restoration log R-1…R-11 written (only R-5 electrical-rewire is future). **NEXT SESSION = MAIN UNIT / CONTROL UNIT** — start at E4 (meter rheostat + dropping resistor) → ring out the machine → verified schematic → R-5 3-wire grounded rewire; plus base/neck/controls measurement capture (BAS-/NCK-/CTL-). See the "NEXT SESSION PICKUP" section for the full handoff.
**Plan (motor phase, now closed):** electrical bench test (R-10) + final wiring (R-11) done; paper/data/drawing items batch-closed.

**① Capture DURING the electrical test (R-10) — resolved by doing the work:**
| # | Item | Notes |
|---|---|---|
| E1 | Stator (STR-001) field-coil **wire lengths** + **final connection** | ✅ **DONE (R-11, 2026-06-23):** final connection map confirmed — **GREEN → brass clip mounted on a brush** (armature/common side); **BLACK → black field lead from the stator (STR-001); WHITE → white field lead from the stator.** Lengths per R-10 prep (sheath ~5.5"; green ~4.5"; black/white ~3.25"). |
| E2 | **Motor wire map** | ✅ **DONE + REFINED (R-10, 2026-06-21 → cont. 2026-06-23):** **GREEN = common live** (armature/brush-series end, always +). **BLACK & WHITE = the two reversing leads** (field path ends). **Green(+)→Black(−) = one direction; Green(+)→White(−) = the other** (CW/CCW). WHITE is NOT a dead tap — it's the second-direction return. Never bridge black+white (field-only, no torque). **Field detail (R-11):** 2 field coils; the **inner end of each coil is tied together** (yellow/green band) → clip → **brush A**; **GREEN (line, red band) → brush B**; **BLACK + WHITE = the two coils' outer ends** (the reversing pair to the rheostat). |
| E3 | **Rigol DP932A bench test** result | ✅ **PASS (R-10):** motor **starts turning at ~12 V / 0.5 A** (Green+/Black−, White floating), spins free — windings/brushes/commutator good. **2026-06-23 cont.:** reversing verified — switching return Black↔White (green held +) reverses spin. **Photos filed:** `R10-01/02` + `R10-video.MOV` (bench setup, Rigol display @ 0.5 A limit). |
| E4 | Meter **rheostat** + **dropping resistor** | ✅ **CLOSED (2026-06-25):** **RV1** = 2-terminal rheostat, **~50 Ω (full CW) → ~394 Ω → OPEN/OFF (full CCW)** (not the ~750 Ω REF pot). **R1 = 220 Ω (CONFIRMED)** = the **heater** (DS1 is a 120 V pilot in parallel, NOT in series — so R1 is not a dropper). Across the line: 0.55 A / **~65 W** in the heater well (rated ~55 W REF; runs hot by design). |
| E5 | Confirm **plunger = reverse?** / **toggle = heater?** | ✅ **CONFIRMED by operator (2026-06-25, wiring dictation):** **PLUNGER (S1) = motor reverse** — out/default = FORWARD, pushed in = REVERSE; the motor BLACK + WHITE leads land on it (it swaps the field ends). **TOGGLE (S2) = heater switch.** **GREEN motor lead → rheostat.** Roles now match E-1690 intent. (Meter ring-out still nails exact terminal/segment netlist — see E8.) |
| E6 | **Green-wire exact color** callout | ✅ **CLOSED (2026-06-23):** **RED heat-shrink** applied to the neck GREEN conductor to flag it **LIVE — not ground**; terminal mapping per E1 (green → brush clip). Confirmed LIVE by E-1690. |
| E7 | **Neck cable replacement** (SJOOW 16/3 + braided sleeve) | ✅ **DONE (R-11, 2026-06-23):** green → brush clip (RED heat-shrink = LIVE), black/white → stator black/white field leads, nylon loom to control unit. Chassis ground stays a separate bond (W-6). |
| E9 | **Control-unit as-wired connection map → verified schematic** | ✅ **MAP COMPLETE + METERED (2026-06-25)** — all components, values, roles, makers, the 6-node netlist, and the plunger truth table confirmed. **NEXT: draw the verified as-found schematic** (then R-5 grounded-rewire target). Detail: **FULL CONTACT-POINT TRACE (2026-06-25):** operator labeled every component's contact points (A/B; motor A/B/C/D) and traced all 10 wires → assembled to **5 nodes** in `docs/dimensions/Control Unit Wiring Map - Sheet1.csv` (OBSERVED conf.). **Terminals now use industry RefDes-Terminal naming (locked 2026-06-25):** P1 cord (P1-L/P1-N) · RV1 rheostat (RV1-W wiper/RV1-CCW end) · S1 plunger (S1-COM/NO/NC) · S2 toggle (S2-COM/NO) · DS1 lamp (DS1-TIP/SHELL) · R1 heater resistor (R1-1/2) · M1 motor (M1-S1/S2 field, M1-A1/A2 armature, A2=internal field-tap brush). **Nodes (6, plunger resolved 2026-06-25):** N1 NEUTRAL (P1-N/RV1-CCW/S2-COM) · N2 HOT (P1-L/R1-1/DS1-SHELL/**S1-d+b jumpered**) · N3 heater+lamp return (R1-2/DS1-TIP/S2-NO) · N4 FORWARD leg (S1-a/M1-S1 white) · N5 armature/speed (RV1-W/M1-A1 grn) · N6 REVERSE leg (S1-c/M1-S2 black). **Plunger contacts a/b/c/d (operator sketch): d=top-left & b=bottom-left jumpered by red braid=hot common (bulb taps d); c=top-right=black, a=bottom-right=white. ✅ Truth table CONFIRMED 2026-06-25: OUT closes hot→a(white)=FORWARD; IN closes hot→c(black)=REVERSE. The black/white motor leads are SWITCHED B-outputs, NOT on the hot rail — this fixes the earlier N2-knot mislabel.** **Circuit:** rheostat in motor return leg = speed+ON/OFF; toggle switches heater return; **lamp reads PARALLEL with heater** (both N2↔N3 via toggle). **No master switch** — N2 hot whenever plugged. **LAMP RESOLVED (2026-06-25): DS1 = 120 V / 6 W** (0.05 A, ~2400 Ω; corrected from an earlier 12 V misread) ⇒ **DS1 is a line-voltage pilot in PARALLEL with R1 — the as-traced parallel is CORRECT, no mislabel.** R1 (220 Ω) is the **pure heater** (~65 W across the line); the lamp is an independent "heater-ON" pilot. *(This removes the earlier "R1/DS1 knot mislabel" concern — that was driven by the wrong 12 V reading.)* **Plunger RESOLVED (2026-06-25, operator sketch, contacts a/b/c/d):** A-side d(top-left)+b(bottom-left) **jumpered by red braid = hot common** (bulb taps d, on N2); B-side **a(bottom-right)=motor white=FORWARD (N4), c(top-right)=motor black=REVERSE (N6).** Transfer switch routes hot to one field lead. **This fixes the N2-knot mislabel** (black c / white a are switched outputs, not on the hot rail). ✅ **Truth table CONFIRMED 2026-06-25:** OUT closes hot→a(white)=forward; IN closes hot→c(black)=reverse (c<->hot: IN 1.3-3 Ω, OUT OL; a<->hot: OUT 2-3 Ω, IN OL). Closed-contact R is high/fluctuating (dirty contacts → clean at rebuild). *(Operator sketch → file `reference/LR-plunger-wiring-sketch.jpeg`.)* **⚠️ Solder joints throughout = "nasty solder blobs" from a bad prior solder job (more prior-rework evidence) → redo all joints properly (or clip terminals) at reassembly.** (Values DONE: RV1 ~50–394 Ω+OFF, R1 220 Ω.) **COMPONENTS NOW REMOVED (2026-06-25, CU-Step 5):** RV1/S1/DS1/R1 + red jewel (CTL-006) lifted off the casting **as one still-wired cluster** (operator approach: free mechanically, leave solder joints, verify+desolder on bench). Casting now bare for refinishing. Bench TODO on the cluster: knot mislabel + plunger truth table + wiper-lug ID → desolder/clean → verified schematic. **⚠️ Unknown loose piece** (not a CTL part; "toward the post") set aside — photograph + ID (likely NCK-). R1 detail: held in heater well by a **spring band + slotted (rusted) screw**, wrapped in an **adhesive-backed paper sleeve**. Then upgrade OBSERVED→CONFIRMED + draw verified schematic (supersedes LR-ELEC-001 series-path guess; anchor E-1690). |

**② Batch-CLOSE after the electrical test — paper / data / drawings:**
| # | Item | Type |
|---|---|---|
| B1 | **ARM-013** — VERIFY all-4-identical vs 3+1 size split; finalize dims | ✅ **CLOSED (2026-06-23):** dims recorded & CONFIRMED (OD 0.4705", bore 0.2500", thk 0.0175" ea, QTY 4). **All 4 identical** (single OD — no 3+1 split, unlike lower ARM-012). |
| B2 | Drawing rework: add **ARM-013** to ARM-001 + EXP-001/002 (annotate SHF-002 vs BRG-001) | ✅ **DONE (2026-06-23):** Gemini rendered **ARM-001 Rev F, EXP-001 Rev F, EXP-002 Rev F** — ARM-013 ×4 upper-journal stack added; validated (ARM-013 present, REV F, June 12 2026, no "Mark 1", XML parses, no comment-hyphen issues, title overflow constrained). Old Rev E archived; source snapshots resynced. |
| B3 | Drawing: title block **"Mark 1 Master" → "Master"** on all 12 sheets | ✅ **12/12 DONE (2026-06-23):** 9 sheets by direct in-place edit + rev bump (UH-001→L, LH-001→G, BRG-001→E, BRG-002→D, STR-001→R, HW-001→G, PLT-001→D, SPN-002→D, BSK-002→D; BSK note reworded); the final 3 (ARM-001/EXP-001/EXP-002→Rev F) via the B2 Gemini render. Also folded in: DATE→June 12 2026 + DRAWING TITLE overflow fix on the header-style sheets. |
| B4 | File brush-port photos (R9-09/10/11) + any new R-9/R-10 shots | ✅ **DONE (2026-06-23):** `photos/stator-wiring/` fully curated (0 raw IMG_ left) — 13 **R-11 wiring** (`R11-01…R11-13`), 11 **stator field-coil bench-doc** (`STR-001-01…11`) + topology pair (`STR-001-topology` / `-annotated`) + lead-ID (`STR-001-leadID-white`), 2 **wire-gauge** (`STR-fieldlead-gauge-01/02`); hand-drawn wiring diagram → `reference/LR-fieldcoil-wiring-diagram.jpeg`. **R-10 bench-test photos NOW filed** (`R10-01/02` + `R10-video.MOV`) and R-11 set extended to `R11-01…R11-17`. Old→new map in `photos/stator-wiring/figure-index.md`. (No R-9 brush-port R9-09/10/11 shots surfaced.) |
| E8 | **Heat-shrink color (SAFETY)** | ✅ **EXPLAINED/RESOLVED (2026-06-23, per restorer):** green LINE lead **IS marked RED** (correct, R11-14). The **yellow/green** band marks an **INTERNAL field-coil junction** — the inner end of each of the 2 field coils tied together → clip → one brush; it is NOT a mismarked ground and NOT a user-facing conductor (the chassis ground is a separate ring-lug bond, W-6). Green → the other brush; Black + White = the two coils' outer (reversing) ends. *(Repo caveat: yellow/green strictly = Protective-Earth by convention; a one-line doc note keeps it unambiguous for others, but the junction is internal to the motor.)* |
| B5 | Download factory diagram **E-1690** into `reference/` | repo |
| B6 | Check base **under the main cover for a hand-punched build date** | quick bench |

**③ Mechanical — Phase 2 (assembly) ✅ COMPLETE (2026-06-23):**
| # | Item |
|---|---|
| M1 | ✅ **DONE (2026-06-23):** ARM-013 ×4 installed on the upper journal (against BRG-001) at final join. |
| M2 | ✅ **DONE (2026-06-23):** housings joined + FLG-002 torqued → deck (PLT-001/002) → spindle **SPN-002** → basket **BSK-002** → mounted to body. |

**→ MOTOR / POWER HEAD is now CLOSED — mechanically assembled (Phase 2 done) and electrically wired (R-11 final connection done).** Remaining motor-package items are documentation-only (B2 drawing rework, B3 title-block rename, B4 photos). Everything else open (E4 meter rheostat/dropping resistor, E5 plunger/toggle role at ring-out, full verified schematic + 3-wire grounded rewire) belongs to the **CONTROL UNIT / main-unit phase**, not the motor housing.

**④ VERIFY / time-dependent (can't close now):**
| # | Item |
|---|---|
| V1 | R-8 super-glue effect on long-term oil wicking (runtime) |
| V2 | Slinger gap ~0.0255" (value from 2nd unit) — confirm in service |
| V3 | Motor patent number (~1933) — optional Google Patents lookup |

**⑤ Later phases:** full electrical = verified schematic (anchored by E-1690) → **3-wire grounded rewire (R-5)**; repo publish = LICENSE + `git init`; optional TechDraw sheets + STL exports of unobtainable parts.

---

**✅ SECOND REV-BUMP RENDERED & RECONCILED (2026-06-17).** Current revs: **PLT-001 Rev C, HW-001 Rev F, BSK-002 Rev C, SPN-002 Rev C, EXP-001 Rev D, EXP-002 Rev D** (others unchanged). 12 SVGs, 1:1 source snapshots, superseded revs archived, no double extensions. **The rotating-assembly / power-head package is now COMPLETE — fully measured AND fully drawn.** No bench work and no drawing work outstanding on the power head. Deferred streams remaining: control unit, workshop manual, publication.

### A. Power head — rotating-assembly capture  ✅ ESSENTIALLY COMPLETE
Full BOM + mechanism mapped and dimensioned; all drawings reconciled (rev-bumps done 2026-06-16). Detailed dims in `Shaft Train Parts Dictionary.csv` + `Shaft Train Dimensions - Sheet1.csv` and the "Shaft Train / Power Head" table below.
- [x] ARM-010 thrust washer — fully dimensioned (OD 0.8125/0.7825, bore 0.280, thickness 0.1075).
- [x] PLT-001 disk / PLT-002 gasket / PLT-004 tubes — dimensioned; FLG-002 through both on 2.300" BCD.
- [x] SPN-002 spindle + SPN-005/006/007 fasteners/spring — dimensioned (ring OD corrected to 2.703", length 3.05").
- [x] BSK-002 basket + BSK-003 lid — dimensioned; bayonet mechanism resolved.
- [x] Shaft Train Dimensions CSV created; re-audit done; 12-sheet drawing package reconciled to confirmed dims.
- **LOOSE ENDS remaining (small — see the LOOSE ENDS LEDGER below).**

### ⚠️ LOOSE ENDS LEDGER — original 10 CLOSED 2026-06-16
| # | Item | Resolution |
|---|---|---|
| 1 | SPN-005 TPI | **1/4-20** (CONFIRMED) |
| 2 | SPN-005 drive | **slotted**, RH turn (CONFIRMED) |
| 3 | SPN-007 thread/drive | **#6-32** (corrected from #6-24), slotted dome head (CONFIRMED) |
| 4 | PLT-002 taper direction | **wide 3.5015" on disk side → narrow 3.2015" into jar** (CONFIRMED) |
| 5 | PLT-001 bolt count | **2 holes = FLG-002 bolts; 4 holes = rivets (PLT-005) mounting gasket to disk** (CONFIRMED) |
| 6 | PLT-001 center collar | **integral** (hole formed in the plate; no separate bushing) (CONFIRMED) |
| 7 | BSK-002 bayonet slot | width **0.1855"**, axial entry **0.420"**, hook run **0.2700"** (CONFIRMED) |
| 8 | SPN-002 hub | impeller+hub **cast as one** — no discrete hub dia (CONFIRMED) |
| 9 | Accessory baskets | **2 shipped** with S/N 13505 = BSK-004/005; BSK-006/007 not present (CONFIRMED) |
| 10 | PLT-002 identity | **yes = the reconditioned patent-1872812 gasket** (CONFIRMED) |

**🆕 NEW small follow-ups that emerged (minor):**
- [x] **PLT-005 Gasket Deck Fastener** — RESOLVED: original = 4 rivets (drilled out, dims unrecoverable); restoration = **stainless M4-0.7×10mm flat-head Phillips screw + stainless M4-0.7 hex nut** ×4, **reusing the original washers (PLT-006, OD 0.4385")** (see restoration-log R-6). Flat head = flush (no trim). FULLY SPEC'D.
- [x] **PLT-006 Gasket Deck Washer ×4 (ORIGINAL)** — OD 0.4385", thickness 0.0415", **ID 0.1570"** (all CONFIRMED; ~M4 nominal so the M4 screw clears cleanly). FULLY SPEC'D.
- [x] **BSK-004 / BSK-005** — RESOLVED: L&R "Multimovement Holder Inserts", **Code #10118** (×2, 1 set); dia 2.5", height 0.620" (CONFIRMED). First original L&R part number captured.
- [ ] PLT-001 eyelet collar OD; SPN-002 ring-pin material; mesh wire material — cosmetic, low priority.

**🔁 SECOND REV-BUMP — ✅ DONE 2026-06-17.** Rendered, cleaned, archived, source-synced. The changes that were applied:
| Sheet | Rev | Change |
|---|---|---|
| PLT-001 Platform | B→C | Show **4 rivets (PLT-005, original design of record)** + 2 FLG-002 bolt holes (not 6 bolts); taper **narrow end into jar**; center hole integral. Add a note: restoration substitutes M4×12 screw+nut+washer (resto-log R-6) |
| HW-001 Hardware | E→F | SPN-005 → **1/4-20 slotted**; SPN-007 → **#6-32**; ADD **PLT-005** (orig rivet + restoration-alt stainless M4-0.7×10 flat-head Phillips screw + SS hex nut) and **PLT-006** original washer (OD 0.4385") |
| BSK-002 Basket | B→C | Bayonet slot: width 0.1855" / axial 0.420" / hook 0.2700" (replace the single 0.420"); add note: nominal basket dia 2 3/4" for this system (Mark 1), Mark 2+ used 2 1/4" |
| SPN-002 Spindle | B→C (minor) | SPN-005 callout → 1/4-20 slotted; note hub+impeller cast as one |
| EXP-001/002 | C→D (minor) | Reflect rivets + taper direction in callouts |

### B. Shop manual curation
Survey done (`docs/manual/reference-survey.md`); outline done (`docs/manual/manual-outline.md`).
- [ ] Obtain a clean copy of the original **L&R Master operating sheet** (Scribd) to transcribe primary operating content.
- [~] Draft **Part III (Restoration)** first — `teardown-log.md` now COMPLETE (7 steps from dictation); compile the digested chapter (teardown → restoration → reassembly) from `restoration-log.md` + `teardown-log.md`; backfill R-2…R-5 from the COMPLETE phases. Output: Markdown first, then PDF/DOCX.
- [x] **Gasket product name RESOLVED (2026-06-20)** — **SEKODAY Treadmill Belt Lubricant** = silicone oil (non-cracking type), 100% (confirmed by box photo). Gasket = PLT-002 (patent 1872812).
- [ ] Then **Part II (Maintenance)**, then **Part I (Operating)**.
- [ ] Decide output format (Markdown → PDF/docx) before publishing.
- [ ] **OPEN ITEM (not now): generate documentation-grade drawings for the manual** from the FreeCAD models (`cad/`) — TechDraw dimensioned sheets + ballooned exploded view + BOM table (canonical Part IDs), exported SVG/PDF. Pipeline validated 2026-06-17 (a style preview was rendered). This supersedes/augments the Gemini SVGs with geometry-driven dimensions.

### C. Control unit — SEPARATE work stream (later)
Base casting, neck/chrome pillar, rheostat, switches, pilot lamp, electrical harness (W-).
- [ ] Ring out the real machine with a DMM → verified as-is schematic.
- [ ] Draft corrected 3-wire grounded rewire target schematic.
- [x] **Base casting dims — CAPTURE COMPLETE (2026-07-10/11)** → `docs/dimensions/Base Casting Dimensions - Sheet1.csv` (authoritative). BAS-001/002/003/004/005/006/007 + BAS-008 (flat profile) + NCK-002 carrier all CONFIRMED. Corrections folded into CLAUDE.md + Parts Dictionary (heater bore smaller-not-larger; no rheostat recess; no BAS-006 oil bore; post socket 2.9035 ~= full height; 6 post screws in 2 groups; rounded sand-cast form). **Remaining:** BAS-008 installed tang height (needs mock assembly); BAS-002 octagon caliper-confirm (~3.0 EST); NCK-001 post + NCK-003 clamp screw (OUT FOR RECHROME — capture on return, ⚠️ measure post across-flats before plating).

### D. Repo / publication
- [ ] Choose **LICENSE** (suggested: MIT for code, CC-BY-4.0 for docs/drawings).
- [ ] `git init`; optional Git LFS for photos.
- [ ] Promote EXP-001/002 FIRST ISSUE → RELEASED after final review (after the power-head rework above).

### E. Housekeeping
- [ ] File the 5 ARM-010 bench photos into `photos/` with descriptive names; link from teardown-log Step 3.
- [ ] Save the S/N 13645 reference photo to `reference/` (not `photos/` — not our machine); it's the current source for PLT geometry pending bench measurement.

## How We Work

**Project Goal:** Open-source restoration project to be published on GitHub.

### AI Agent Roles
| Agent | Responsibilities |
|---|---|
| **Claude** | Electrical layouts, test plans, procedure documentation (teardown + restoration steps), project tracking and status |
| **Gemini** | Mechanical drawings (markup-based iteration), vintage workshop manual drafting (requires accurate measurements + procedure explanations: evaluation, removal, installation) |

### Procedure Documentation Standard
When documenting any teardown or reassembly procedure, capture:
- Tools used
- Techniques and tricks applied
- Step-by-step sequence
- Measurements required for workshop manual accuracy

Starting point: motor housing reinstallation is the first procedure to fully document.

## Reference Links
- https://www.lrultrasonics.com/history
- https://mb.nawcc.org/threads/l-r-master-watch-cleaning-machine.198512/
- https://www.reddit.com/r/Watches/comments/n5274p/identification_1900s_lr_watch_cleaning_machine/
- https://www.scribd.com/document/456605930/OPERATING-INSTRUCTIONS-L-R-Master-Watch-cleaning-Machine

---

## Project Goal
Complete vintage restoration:
- Mechanical breakdown and rebuild of all components
- Full electrical rewiring with modern safety grounding
- Refinishing all surfaces to near-original factory condition

---

## Restoration Status by Phase

### COMPLETE — Cosmetic Refinishing (Motor Housings)
- Stripped the baked-on factory enamel/varnish/grease with **Citristrip** paint/varnish stripper gel (citrus-based, safe on aluminum); wire-brush + picks for fins/chambers/notches; removed all stripper residue, dried immediately (flash-rust prevention)
- Scuffed for tooth (abrasive pad/wire wheel); precision-masked all running faces/bores/flanges with razor-trimmed high-temp tape; **final 99.9% IPA wipe of everything immediately before the etch primer**
- Applied Rust-Oleum 249322 Self-Etching Primer (zinc phosphate base) in ultra-thin continuous coats — matte olive-drab/grey appearance confirms proper anchor
- Applied VHT SP201 Wrinkle Plus in a heavy 3-coat crosshatch matrix:
  - Coat 1: Horizontal passes
  - Coat 2: Vertical passes (5-min flash)
  - Coat 3: Diagonal passes (5-min flash) — uniform multidirectional film build over rounded contours
- Heat gun (and/or oven) at ~350°F after the level window — tight, uniform heavy grain achieved
- Masking pulled while film still warm to preserve internal mechanical dimensions
- **Current status:** Cure complete. Tight uniform heavy grain achieved. Both housing halves fully refinished and ready for reassembly.

### COMPLETE — Small Components & Basket Assembly
- **General clean (during teardown):** all small parts that fit the tank (bearings, screws/fasteners, collars, washers, tube, brackets) ultrasonically degreased in **mild diluted soap**; oversized parts (housings, base, neck) cleaned by hand. (Restoration-log R-3.)
- **Heavy clean:** some of the badly fouled **mesh basket pieces** got a dedicated **Citranox** clean — baked-on chemical sludge and oxidation stripped; mesh open, bright, and pristine.

### COMPLETE — Gasket Conditioning
- Jar-seal gasket (PLT-002): single molded rubber piece carrying the molded mark **U.S. PATENT 1,872,812** — this is **L&R's 1930/1932 "Watch Cleaning Machine" patent (inventor Frank Regero), used as a maker's mark, NOT a patent on the seal itself** (see External Reference Intel). (Earlier records mislabeled this the "main motor cap seal"; it is the jar seal.)
- Cleaned with warm Citranox solution to remove orange-brown chemical film; patent text now crisp
- 16+ hour immersion soak in SEKODAY Treadmill Belt Lubricant (silicone oil, non-cracking type); microfiber buffed to full satin-black finish
- Rubber fully re-saturated — structural pliability restored
- **NOTE:** WD-40 ruled out for rubber contact — petroleum distillates swell and degrade vintage elastomers
- Hardware upgrade: replacing original fastening system with modern screw-and-nut for even compression on reassembly

### COMPLETE — Sleeve Bearing & Oil Wick Overhaul
- Bearing type confirmed: self-aligning spherical sleeve bearings (ball-and-socket style)
- Original factory config: continuous natural yarn threaded through central lube hole to contact shaft, remainder wrapped around bearing globe; flat wool felt washers at pocket edges for dust blocking and oil containment
- **New reservoir packing:** Estako Wool 98 — 100% Superwash Merino Worsted Yarn, Off-White (un-dyed, won't leach or mat when saturated)
- **New felt washer stock (as-installed, confirmed R-7):** SAE F3 wool felt washers — small (BRG-010) + large (BRG-009), trim-to-fit dust/retaining washers for the spherical bearing pockets. (Earlier records listed "Singer Potted Motor F-1" — that was an error; the felt actually used is SAE F3.)
- **Oil:** Zoom Spout precision oil

### Reassembly Sequence — ✅ PHASE 1 & 2 COMPLETE (2026-06-23); Phase 3 (electrical) = next session
Order: **lube/bearings → mechanical (motor + power head) → electrical last.** This is also the manual's lead procedure ("motor reinstallation"). Detail = teardown-log in reverse + restoration-log + the bearing/wick and rewire notes. Capture per the Procedure Documentation Standard (tools, technique, step sequence, measurements) as each phase is performed.

**▶ PHASE 1 — BEARINGS & LUBRICATION: ✅ COMPLETE (both housings, 2026-06-20).**
- ✅ **Lower-housing bearing DONE 2026-06-19** (restoration-log **R-7**) — wick/felt/spring built, BRG-011 retaining ring friction-fit, **armature test-fit good**. Photos `R7-01…R7-08` (+ `R7-09…R7-11` extra angles) in `photos/bearings/`.
- ✅ **Upper-housing bearing DONE 2026-06-20** (restoration-log **R-8**, from 4 voice memos) — **armature test-fit good, spins fine**. Photos `R8-01…R8-08`. Was the harder install (15+ failed attempts).
  - **Upper differs from lower:** (1) yarn rides **INSIDE** the bearing's internal top-to-bottom **slit** (lower rides outside the ball); (2) the upper "small felt" is a **solid felt TAB/PAD** (no center cutout, just a pin-hole) sitting at the very top **under the OIL cap (UH-011)** — oil added on top wets the pad → wicks down the slotted yarn → bottom washer/shaft; (3) **NO BRG-011 retaining ring**.
  - **Working method:** yarn knotted to a ~0.400" wood peg (clove-hitch) → knot slipped over the inner-end of the bearing → other end through the slit → wrapped tight at top → **Loctite Super Glue** dab to anchor (felt too pliable to hold otherwise). ⚠️ **(VERIFY)** super-glue's effect on long-term oil wicking — watch over time.
- ✅ **PHASE 2 — MECHANICAL: COMPLETE (2026-06-23, R-9 → R-11).** Stator installed; armature dropped in (ARM-013 ×4 upper-journal washers added at join); halves joined + FLG-002 torqued; deck (PLT-001/002) → spindle SPN-002 → basket BSK-002 → mounted to body. ARM-010 slinger to ~0.0255" gap. Motor wired (R-11) + bench-tested (R-10). **→ PHASE 3 (electrical, control-unit) is the next session's work.**
- **Materials (confirmed as-installed):** SAE F3 felt washers + GE 1/8" fan oil wick (~1¼" cut) + wool yarn reservoir (Estako Wool 98) + Bramec Zoom Spout oil. (Felt = SAE F3 confirmed; earlier "Singer F-1" was an error. Wool = Estako unchanged.)
- **New parts found 2026-06-19 — ARM-011 / ARM-012 lower-journal end-float washers** (4 total on SHF-003, on top of BRG-002; set fan clearance). ARM-011 ×3 (OD 0.630"), ARM-012 ×1 (OD 0.500"), bore 0.2850", 4-stack 0.0650". Material = non-metallic **phenolic** (thermoset resin), non-conductive, oil/heat-resistant (CONFIRMED non-metal + phenolic ID 2026-06-20). See Armature section + dictionary.
- **Drawing callouts (Phase-1 finds): ✅ DONE 2026-06-20** — BRG-011 added (BRG-002 **Rev C** + LH-001 **Rev F**); ARM-011/012 phenolic washer stack added (ARM-001 **Rev E**, EXP-001 **Rev E**, EXP-002 **Rev E**). Old revs archived; source snapshots resynced; package clean (12 SVGs, 1:1).

**Phase 1 — Bearings & lubrication (first):**
- Pack oil-wick reservoir yarn (BRG-008, Estako merino) into each housing pocket; thread through bearing bore to contact shaft.
- Stack felt washers per the bearing table: BRG-009 large (top of pocket), bearing + BRG-012 conical spring at the ball equator, BRG-010 small (below), BRG-011 metal retainer (lower housing bottom).
- Seat spherical bearings (BRG-001 upper / BRG-002 lower) in their sockets.
- Install oil feed tube (LH-006) + its wick in the lower housing; oil all wicks (Zoom Spout).

**Phase 2 — Mechanical (motor + power head):**
- Install stator (STR-001) in upper housing — 2× STR-008 screws on the 2.300" circle.
- Drop armature (ARM-001) in from the top (stepped shaft): upper journal SHF-002 → BRG-001 (with the **ARM-013 ×4 phenolic end-float washers** on the upper journal against BRG-001), lower journal SHF-003 → BRG-002.
- Join housing halves at the flange (FLG-001 register step); torque the 2× FLG-002 tie-bolts into the UH-009 bosses — these also clamp the platform deck (via PLT-004 standoff tubes).
- Platform deck sub-assembly: gasket (PLT-002) fastened to disk (PLT-001) by 4× PLT-005 (restoration: SS M4-0.7×10 flat-head Phillips + nut) reusing PLT-006 washers; mount to lower housing.
- Lower journal SHF-003 stack: ARM-011×3 + ARM-012 end-float washers (internal, on top of BRG-002) → ARM-010 slinger/thrust washer (external) → basket drive spindle (SPN-002), locked by SPN-005 set screw → retention spring (SPN-006) + brass screw (SPN-007).
- Basket (BSK-002) bayonets onto the SPN-002 ring pins; fit lid (BSK-003).
- Brushes (UH-004 caps + UH-005 set screws in UH-003 ports); oil access cap (UH-011).
- Mount the motor/power-head assembly to the L&R body (UH-010 foot, 2 mount screws).

**Phase 3 — Electrical (last):** see Electrical section below.
- Ring out the machine (DMM) → produce the VERIFIED schematic first.
- 3-wire grounded rewire per the harness BOM (W-1…W-6): silicone wire, NEMA 5-15P cord, chassis ground bond.
- Run the Post-Assembly Cold-Check Diagnostic Matrix (unpowered) BEFORE first power-on.

### UPCOMING — Electrical Rewiring & Safety Grounding
See Electrical section below.

---

## Electrical Wiring Layout

### System Overview
- 110V AC, legacy 2-wire non-grounded system (Hot + Neutral only)
- Original design relies entirely on component isolation for operator protection — no earth ground

### Component Matrix
| Component | Description |
|---|---|
| Rheostat | Ceramic-insulated toroidal power resistor; manages motor speed via sweeping wiper arm modifying voltage. **Maker: IRC (International Resistance Co.)** — stamped on the wiper (CONFIRMED, photo 2026-06-25). ✅ **VALUE CONFIRMED 2026-06-25: "425 OHMS" stamped on body** (metered ~394 Ω max, aged). 2-terminal **rheostat** (wiper + one coil end), **NOT** the ~750 Ω 3-terminal pot the forums quote. **Full CCW = OPEN/OL = motor OFF** (confirms the cast "OFF"); CW sweep **~394 Ω (slow) → ~50 Ω (fast)**. So RV1 = motor master ON/OFF + speed. Replacement (if ever) = a ~400–500 Ω wirewound rheostat rated for motor current, with an off detent. The **motor GREEN lead** (M1-A1) lands on the wiper side; **mains WHITE/neutral** on the end side. |
| Plunger Switch | Top-mounted momentary mechanical switch. ✅ **CONFIRMED (operator, 2026-06-25): = MOTOR REVERSE.** Out/default = FORWARD; pressed-in = REVERSE. The motor **BLACK + WHITE** leads land on it; it swaps the two field ends to reverse. **Construction:** **4 connection points (DPDT)** — corrected 2026-06-25 (was traced as 2; two were missed). Multi-plate stacked-contact (copper finned plate stack in a black bakelite shroud); a DPDT swaps both field leads = reversing. The missed 2 terminals are the likely source of the N2-knot/lamp-series mislabel → re-trace all 4 at bench. **Maker: ARROW H&H (Arrow Hart & Hegeman), MADE IN USA, UL insp'd; TYPE 3392, 1A 125VAC.** Red/yellow braided cloth lead; press-fit button (pulls off). Truth table (COM/NO/NC) at bench. |
| Power Resistor ("Heater") | Ceramic-bodied tubular power resistor — ✅ **CONFIRMED (operator, 2026-06-25): this IS the "heater unit"**, mounted **in the heater well (BAS-002) on a copper strap/clamp**, a wire soldered to each end cap. **Marked: OHMITE, P/N 33974, 220 Ω ±10%** (vitreous-enamel tubular power resistor) — stamp confirms the metered value. **The pilot lamp (DS1, 120 V) is in PARALLEL with it, not in series** — so R1 is purely the heater, not a lamp dropper. ✅ **Value = 220 Ω (CONFIRMED, metered + stamped 2026-06-25)** — the HEATER (the 120 V/6 W pilot DS1 is parallel, not series, so R1 is NOT a lamp dropper). Across the line: 0.55 A / **~65 W** in the heater well (rated ~55 W REF; runs hot by design). (The "40 Ω" floating in our notes is the motor field-coil resistance, not this.) Modern swap = a **PTC heater element (30–50 W)** on the same copper strap. Confirm by meter. |
| Status Bulb + Toggle Switch | Chassis-mounted incandescent lamp ("MADE IN U.S.A.", brass socket) behind faceted red jewel lens. ✅ **Installed bulb = 120 V / 6 W, China, date code "C 01/18" (~Jan 2018) — CONFIRMED under magnification 2026-06-25 off the actual in-unit bulb** → 0.05 A, ~2400 Ω — a **line-voltage pilot in PARALLEL with R1** (as-traced is correct; no dropper needed). R1 (220 Ω) is the **pure heater** (~65 W across the line). *(The earlier "12 V" was a misread off a SPARE, not the installed bulb.)* ⚠️ **Installed bulb is a recent (~2018) NON-ORIGINAL replacement.** **Spares that came with the unit = 12 V/6 W TAIWAN — do NOT fit this circuit** (a 12 V bulb in the parallel/line wiring blows instantly; don't install them). **Most likely (operator's read): the 12 V spares are simply the WRONG bulbs** — bought for a different/later L&R variant that uses 12 V pilots, by someone who didn't realize they don't fit this unit. So the spares are **not evidence** about this unit's original config (no rewire implied). This unit's original lamp-branch intent (series vs parallel) stays **UNKNOWN** — only E-1690 would settle it. ✅ **CONFIRMED (operator): toggle = HEATER+pilot switch.** **Toggle maker: Arrow-Hart & Hegeman (Arrow H&H), MADE IN USA, UL insp'd; rated 3 A / 250 V** — same maker as plunger S1 (heavier rating than S1's 1 A/125 V; heater branch ~0.6 A = ample margin). |

### CRITICAL HAZARD — Neck Wiring Illusion
The internal wire loom through the casting neck to the motor has three wires: **Green, Black, White**.

**The Green wire is NOT a safety ground.** It is a live, current-carrying branch link connecting the motor assembly down to a dedicated terminal block on the rheostat stack. During rewire it must remain isolated and treated as a hot circuit element.

**✅ CONFIRMED by the FACTORY WIRING DIAGRAM (2026-06-20):** L&R's own drawing **E-1690 "Wiring Diagram — Master W.C.M."** (L&R Mfg. Co., drawn P.H., dated 3-24-60, supersedes the 4-19-50 drawing, "used on A-4100"; found as a NAWCC attachment) shows the **GREEN wire running from the MOTOR to the RHEOSTAT** — a live branch, exactly as stated. The only earth **GND** on the diagram is at the **A.C. LINE** input, separate from the green motor wire. The diagram also confirms **HEATER + PILOT LIGHT in series** on the line (bulb acts as a fuse). NOTE: E-1690 is the **1960 revision** (ours is the earlier oiled generation), but the green=motor-to-rheostat topology matches our 3-wire loom. This is a genuine **primary source** — worth saving into `reference/` for the repo.

### Master Schematic (Current As-Found State)
```
                   +-------------------+
                   |                   |
                   |   UPPER MOTOR     |
                   |                   |
                   +---+---+-------+---+
                       |   |       |
               Green   |   | Black | White
               (Neck)  |   |(Neck) | (Neck)
                       |   |       |
+--------------------+ |   +-------------+
|                    |           |
|                    v           |
|           +---------------+   |
|           | SWITCH BUTTON |   |
|           |   (Plunger)   |   |
|           +-------+-------+   |
|                   ^           |
|                   | Black     |
|                   |           |
|   +------------+  |           |
|   | INDICATOR  |  |           |
|   |    BULB    +--+           |
|   +-----+------+             |
|         |                    |
|   Black |                    |
|         v                    |
|   +-----+----------+         |
+-->| POWER RESISTOR |         |
    |    (Heater)    |         |
    +-----+----------+         |
          ^                    |
    Black |                    |
          |                    v
          |        +-------+-------+
          |        | TOGGLE SWITCH |
          |        +-------+-------+
          |                |
          |                | White
          |                v
          |        +-------+-------+
          +<-------+   RHEOSTAT    +<-----------+
                   |  Speed Control|
                   +-------+-------+
                           ^
                           | White
                           |
Line (110V AC) Hot  (Black) -+
Line (110V AC) Neut (White) -----------------------+
```

### Rewiring Plan — Modern 3-Prong Safety Upgrade
1. **Cordage:** 3-conductor **16AWG** with molded NEMA 5-15P grounding plug
2. **Hot/Neutral:** Terminate Black (Hot) and White (Neutral) exactly per historical schematic above
3. **Chassis Ground Bond:** Green ground wire from new cord bonded permanently to aluminum base casting
   - Select structural screw location (e.g., internal cable strap retention bosses)
   - Strip localized contact area down to clean, bright bare aluminum
   - Apply **star washer directly beneath screw head** to bite into chassis metal
   - Secure with heavy-duty crimped brass ring terminal
   - Provides low-impedance fault path directly back to household breaker panel
4. **Wire spec:** Continuous, highly flexible **silicone-coated wire, 125°C minimum rating** throughout to replace original brittle wiring (avoid standard PVC wire near the resistor well)

### Wire Harness BOM (Pre-Cut Bench Specs)
Pre-measure, cut, and tin all wires before committing to the chassis to avoid touching a hot iron to fresh paint.

| ID | Color | Gauge/Type | Cut Length | From → To |
|---|---|---|---|---|
| W-1 | Black | 16 AWG Silicone | 5.5 in | AC Line Inlet → Plunger S1 |
| W-2 | Black | 16 AWG Silicone | 3.5 in | Plunger S1 → Resistor R1 |
| W-3 | White | 16 AWG Silicone | 6.0 in | AC Line Inlet → Rheostat base terminal |
| W-4 | White | 16 AWG Silicone | 4.0 in | Toggle S2 → Rheostat wiper arm |
| W-5 | Black | 16 AWG Silicone | 3.0 in | Resistor R1 → Toggle S2 |
| W-6 | Green | 16 AWG Stranded | 4.5 in | AC Plug Ground → Chassis casting boss (ring lug) |
| Neck cable (REPLACEMENT, 2026-06-21) | BLK/WHT/GRN | **SJOOW 16 AWG/3** portable power cable (300 V, −40/+90 °C); dressed with a **braided expandable sleeve + heat-shrink ends** for vintage cloth-cover aesthetics | — | Motor (upper column) → rheostat/control terminal board. Replaces the original brittle 3-wire neck loom. |

**⚠️ NECK-CABLE GREEN CONDUCTOR — CRITICAL (do not mistake for ground):** the new SJOOW cable has BLK/WHT/**GRN** conductors, but per the **Neck Wiring Illusion** + factory diagram **E-1690**, the neck **GREEN is a LIVE motor→rheostat branch — NOT a safety ground.** All three neck conductors carry motor-circuit current. **The chassis safety ground is a SEPARATE bond (harness W-6, plug ground → chassis boss), not through this cable.** **MARKING APPLIED (2026-06-21): a RED heat-shrink band on the neck green conductor = "LIVE — not ground."** Red was chosen deliberately: it reads as hot/line in AC and, unlike yellow, **avoids the green+yellow = Protective-Earth trap** (confirmed on the heat-shrink kit's own color chart: Yellow/Green = PE/ground). Pair the band with a "LIVE" tag at the terminal for the open-source build. (A non-green 3rd conductor would be the safer convention, but green replicates the original — so it's flagged red instead.) **Spec note:** SJOOW jacket is 90 °C; fine for the neck run (motor↔control), but keep the **125 °C silicone** for the internal leads near the resistor well (W-1…W-5).

### Post-Assembly Cold-Check Diagnostic Matrix
**Perform all checks UN-POWERED (cord unplugged) with a DMM before first power-on.**

| Step | Check | Probes | Target |
|---|---|---|---|
| 1 | Safety ground continuity | Round earth pin on plug ↔ bare metal screw on casing | ≤ 0.2 Ω |
| 2 | Hot–chassis short | Flat Hot blade on plug ↔ chrome upper column pillar | O.L. (open) |
| 3 | Neutral–chassis short | Flat Neutral blade on plug ↔ chrome upper column pillar | O.L. (open) |
| 4 | Circuit continuity (depress plunger) | Hot blade ↔ Neutral blade, plunger held in | ~28 Ω + rheostat coil gradient |

---

## Mechanical Layout

### Parts Dictionary
Canonical part names for the motor assembly are defined in `Motor Assembly Parts Dictionary.csv`. All documentation, drawings, and workshop manual content must use these names. Each part has a unique ID (e.g. UH-003 = Brush Port) — use the ID when referencing parts across documents.

**SCOPE EXPANDED 2026-06-15 — full shaft/spindle train.** The dataset now aims to cover the *entire rotating assembly*, not just the motor. New prefixes: **SPN-** (spindle/drive train above the motor — center column, impeller bracket, basket coupling) and **BSK-** (basket family). Provisional entries are in `docs/dimensions/Shaft Train Parts Dictionary.csv`; bench capture is driven by `docs/manual/shaft-train-capture-checklist.md`. Most SPN-/BSK- rows are PROVISIONAL pending measurement. Prefix registry: UH/LH/FLG/SHF/ARM/BRG/STR/MTR (motor) · SPN/PLT/BSK (power-head: spindle / platform-deck / basket) · W- (wire harness).

**PLATFORM DECK FOUND 2026-06-15 (was missing).** A stationary **Platform Disk (PLT-001)** carrying a **rubber jar seal (PLT-002)** sits beneath the motor; the basket hangs below it and the shaft passes through it. It is **secured by the two FLG-002 housing tie-bolts** (confirmed from reference machine S/N 13645) — so FLG-002 does more than clamp the housing halves, which is why it is 3.090" long. FLG-002 description corrected in the motor dictionary. PLT-002 may be the molded rubber seal already conditioned (U.S. PATENT 1872812) — to confirm. Capture driven by the checklist §A2.

**MACHINE SPLIT INTO TWO WORK UNITS (2026-06-15).** The user works the machine as two separate sub-units that together make the whole:
1. **Rotating assembly / power head** — motor (UH/LH/FLG/SHF/ARM/BRG/STR) + shaft train (SPN/BSK). CURRENT FOCUS.
2. **Control unit** — base casting, neck / chrome pillar, rheostat, switches, pilot lamp, and the electrical harness (W-). Treated as its own work stream with its own dataset/drawings. **TEARDOWN STARTED 2026-06-24.**

Documentation, BOM, and the shop manual should keep these two units distinct in organization even though the final assembly stitches them together.

**CONTROL-UNIT PART-ID SCHEME LOCKED 2026-06-24** — canonical names in `docs/dimensions/Control Unit Parts Dictionary.csv` (assembly ID **CU-001**). Prefixes:
- **BAS-** base/body — BAS-001 Main Base Casting · BAS-002 Heater Cylinder Well · BAS-003 Solution Jar Bay (×3) · BAS-004 Control Tongue · BAS-005 Cast Relief Lettering · BAS-006 Post Mount Boss · BAS-007 AC Line Grommet (DISINTEGRATED → replace)
- **NCK-** neck/post/carrier — NCK-001 Post/Mast (square, ROUNDED TOP; tap-out removed, corrosion-bound) · NCK-002 Motor-Mount Carrier (swivels on round top to index over each jar bay + heater) · NCK-003 Carrier Clamp Screw (tighten at an angle → carrier base catches a SQUARE CORNER of mast = holds motor raised) · NCK-004 VOID (no lift handle; top loop = power cable)
- **CTL-** controls/electrical — CTL-001 Rheostat (~750Ω PROPOSED) · CTL-002 Rheostat Knob · CTL-003 Plunger Switch (reverse flag, PROPOSED) · CTL-004 Toggle Switch (heater flag, PROPOSED) · CTL-005 Pilot Lamp (series/fuse) · CTL-006 Jewel Lens · CTL-007 Dropping Resistor (~200-220Ω/55W PROPOSED) · CTL-008 AC Line Cord (removed → 3-wire grounded replacement, R-5) · CTL-009 Neck Loom BLK/WHT/GRN (GREEN = live branch, not ground) · CTL-010 Terminal/Junction Points (ring-out before removal; anchor E-1690)

Dimensions sheet still to be built as parts come off; ring-out/connection map is the next bench step BEFORE removing any CTL component.

**CONTROL-UNIT RESTORATION ROADMAP (user outline, locked 2026-06-24).** Three phases mirroring the motor-head flow:

*Phase 1 — Strip & Prep*
1. **Map then remove** the electrical components (CTL-001..010). Ring-out/connection map (CTL-010) anchored to E-1690 comes FIRST — driven by `docs/manual/control-unit-ringout-checklist.md` (terminal-by-terminal node registry, directed wire-segment netlist, full continuity matrix, switch truth tables, component-value capture). Only then unbolt rheostat / switches / lamp / resistor and set aside. Dimension + photograph each as it comes off (build the CU dimensions sheet here). **GATE: nothing leaves the casting until its wires are logged + photographed with tags visible.**
2. **Reinstall intent (record now, execute Phase 3):** clean up all connections, switch to **clip/quick-connect terminals** for easier, more organized joints, and **add the safety ground** (this is the R-5 3-wire grounded rewire target).
3. **Citristrip** the old finish off the castings once components are out. **Strip batch (staged 2026-06-25):** BAS-001 main casting (flaking wrinkle paint + primer + an older repaint = prior rework), NCK-002 carrier, **PLT-001 platform disk** (the round 6-bolt+center-hole plate = already-cataloged power-head deck that carries the PLT-002 jar seal — needs refinish; ✅ PLT-002 rubber gasket REMOVED/detached 2026-06-25 — clear to strip), and **BAS-008 Heater-Well Motor Stop** (flat tang blade, 2-screw mount at the heater well — best-judgment = limits how far the carrier lowers the motor/basket over the heater so it dries above the element). **Process:** Citristrip is aluminum-safe; apply THICK + cover with cling film + keep OUT of direct sun (dries/quits); expect multiple coats; **protect the cast "L&R MASTER"/"ON" relief** (brass brush / plastic scraper in recesses, don't sand the lettering); neutralize + dry fully before primer.
4. **Clean, prep, smooth:** knock down rough as-cast areas; fill pits/level casting lines (keep filler clear of bores, threads, and the post boss BAS-006). **⚠️ Use J-B Weld HIGH HEAT, not Bondo** — polyester body filler can shrink/outgas/soften at the 350 °F wrinkle bake; J-B Weld High Heat (~450–550 °F) survives it. **Full base-casting refinish + cast-letter ("OFF"/BAS-005 "L&R MASTER") restoration workflow → `docs/manual/base-refinish-sequence.md`** (15-step operator sequence + Claude technical review). **⚠️ Key review flag:** the Vaseline letter-mask-under-wrinkle-cure step is high-risk (petroleum migrates at ~350 °F → fisheyes/adhesion failure) → PREFER doing letters LAST via paint-fill wipe-back (CTL-002 knob method) after the wrinkle cures. Keep the wrinkle coat/cure IDENTICAL to motor-housing R-2 so textures match.
   - **Trim sub-task (parallel, bench-side):** the **Bakelite/phenolic trim is POLISHED, not painted** — pull the **CTL-002 rheostat knob** (and CTL-003 plunger cap) while the casting is being stripped/painted. Confirm Bakelite (Simichrome rag turns yellow), then: **polish** (Simichrome/Brasso → Novus) → **degrease the arrow groove** → **re-fill the faded white arrow** by enamel paint-fill wipe-back (Testors gloss white #1145; wipe back ACROSS the groove) → **cure 24 h** → **seal** dome with Renaissance wax. Protect the knurl + molded arrow during polishing. (Separate from the broken **donor brush-cap** recast question.)

*Phase 2 — Finish*
5. **Prep for VHT** (degrease w/ IPA, self-etching primer per the motor-head process).
6. **Paint** — VHT wrinkle topcoat + heat cure (match the motor-housing procedure in R-2).

*Phase 3 — Reassemble & Commission*
7. **Reinstall components** into the refinished casting.
8. **Route wires** (new 3-conductor grounded harness; clip terminals; chassis ground bond).
9. **Bench test** (Rigol DP932A, low-V safe check) → cold-check continuity matrix.
10. **Final hookup** to mains.
11. **Test run.**

Cross-refs: safety ground + rewire = restoration-log **R-5** (was deferred); cosmetic process mirrors **R-2**; bench/cold-check method mirrors **R-10**. Source outline: `OneDrive\L&R.md`.

**↔ ORTHOGONAL — optional modernization ideas (NON-ORIGINAL, not committed):** parked in `docs/enhancement-ideas.md` — (1) auto forward/reverse module (SPDT relay + cycle timer on the white/black field leads; coast pause + snubbed); (2) master power switch in the hot leg (fixes "always live when plugged"); (3) fusing (3 A SLOW-BLOW reasonable for ~1.6 A est. load; measure first). Ideas 2+3 fold into a switched-fused grounded IEC inlet with R-5. Keep the as-found design (LR-ELEC-002) restorable; label any built as enhancements.

### Measurement Capture Goal
**COMPLETE.** All motor housing dimensions confirmed at bench. Checklist below is the authoritative record. Status: ✓ = confirmed | — = not yet measured.

Reference file: `Motor Housing Dimensions - Sheet1.csv`

#### Upper Housing Half
| Feature | Measurement | Status |
|---|---|---|
| Overall height | 2.650" | ✓ |
| Outer diameter | 3.200" | ✓ |
| Depth (interior cavity) | 1.850" | ✓ |
| Wire entry width (UH-002) | 0.950" | ✓ |
| Wire entry height (UH-002) | 0.700" | ✓ |
| Wire entry position — bottom edge above mating flange (UH-002) | 0.500" | ✓ |
| Motor brush port ID — one port each side (left & right) of upper housing | 0.435" | ✓ |
| Motor brush port OD — one port each side (left & right) of upper housing | 0.530" | ✓ |
| Upper set screw ID — 2 screws, retain brush caps | 0.150" | ✓ |
| Mount screw ID — 2 screws, mount motor housing to L&R body | 0.300" | ✓ |
| Interior depth — dome to bolt boss base (UH-009) | 1.100" | ✓ |
| Height — base to brush port center (UH-003) | 1.500" | ✓ |
| Depth — brush port (UH-003) | 0.500" | ✓ |
| Wall thickness | ~0.100" | ✓ |
| Shaft clearance opening top (UH-008) | 0.460" | ✓ |
| Vent openings — count (UH-007) | 4 | ✓ |
| Vent opening height (UH-007) | ~0.800" (EST.) | ✓ |
| Vent opening width — teardrop profile: bottom 0.330", top 0.120" | 0.330" / 0.120" | ✓ |

**Interior layout note — vertical feature positions (from base/flange):**
- Brush port center (UH-003): 1.500" from base — upper zone of housing
- Bolt boss base (UH-009): ~1.550" from base (SYN — derived: 2.650" total height minus 1.100" from dome interior)
- Brush ports confirmed above bolt bosses as expected

**Angular layout (top view):**
- Brush ports (UH-003): left and right — 180° apart, define the 0°/180° axis
- Wire entry (UH-002): 90° from brush port axis — sits on the front or rear face of the housing
- All three features are evenly distributed around the housing at 90° intervals

#### Lower Housing Half
| Feature | Measurement | Status |
|---|---|---|
| Overall height | 1.700" | ✓ |
| Outer diameter | 3.000" | ✓ |
| Depth (interior cavity) | 1.000" | ✓ |
| Oil wick port bore diameter (LH-002) | 0.290" | ✓ |
| Oil wick port bore depth (LH-002) | 0.600" | ✓ |
| Oil feed tube length (LH-006) | 1.296" | ✓ |
| Oil feed tube body OD (LH-006) | 0.293" | ✓ (press-fits LH-002 bore 0.290") |
| Oil feed tube ID/bore (LH-006) | 0.247" | ✓ (inside jaws; wall ~0.023") |
| Oil feed tube installed protrusion (LH-006) | 1.000" | ✓ (seats ~0.30" into port) |
| Lower screw ID | 0.200" | ✓ |
| Upper screw OD | 0.350" | ✓ |
| Wall thickness | ~0.100" | ✓ |
| Shaft clearance opening bottom (LH-004) | 0.500" | ✓ |

**Oil feed system note:** LH-002 is the *port bore* in the housing body. A separate brass **Oil Feed Tube (LH-006)** is pressed into that bore and carries an internal wick that draws oil up to the lower bearing (BRG-002). The two are distinct parts.

#### Mating Flange (where halves join)
Flange OD is captured by the Diameter row above — Upper = 3.200", Lower = 3.000".

**Fastening method:** 2 long bolts enter through the bottom face of the lower housing (clearance hole ID = 0.200") and thread into bosses cast into the inside of the upper housing (boss OD = 0.350"). No nuts — upper housing is self-threaded.

| Feature | Measurement | Status |
|---|---|---|
| Flange thickness — upper housing (FLG-001) | 0.095" | ✓ |
| Flange thickness — lower housing (FLG-001) | 0.080" | ✓ |
| Flange register step — lower housing (FLG-004) | 0.050" | ✓ |
| Bolt circle diameter — center-to-center (FLG-003) | 2.300" | ✓ |

#### Mounting / Neck Interface (base of lower housing)
**Mounting method:** 2 mount screws (ID 0.300") in the upper housing attach the motor housing assembly to the main L&R body.

| Feature | Measurement | Status |
|---|---|---|
| Lower housing foot OD (LH-005) | 0.750" | ✓ |
| Lower housing foot height (LH-005) | 0.500" | ✓ |
| Lower housing foot ID (LH-005) | 0.500" | ✓ |
| Upper housing foot OD — lower section (UH-010) | 0.900" | ✓ |
| Upper housing foot height — lower section (UH-010) | 0.300" | ✓ |
| Upper housing foot OD — register step (UH-010) | 0.805" | ✓ |
| Upper housing foot height — register step (UH-010) | 0.200" | ✓ |
| Upper housing foot total height (UH-010) | 0.500" | ✓ |
| Upper housing foot ID / bore — oil access channel (UH-010) | 0.460" | ✓ |
| Mount screw bolt circle diameter | 2.300" | ✓ |
| Oil access cap OD (UH-011) | 0.880" | ✓ |
| Oil access cap ID / bore (UH-011) | 0.805" | ✓ |
| Oil access cap height (UH-011) | 0.290" | ✓ |

---

### Armature Assembly (Rotor)
Reference file: `Armature Assembly Dimensions - Sheet1.csv` | Parts: ARM-001 through ARM-013, SHF-001 through SHF-003

**IMPORTANT — Terminology:** The rotating assembly is the ARMATURE (rotor). The stationary field coil assembly inside the upper housing is the STATOR (STR- prefix). Do not confuse the two.

| Feature | Part ID | Stack Length | Confidence | Diameter | Notes |
|---|---|---|---|---|---|
| Upper Journal | SHF-002 | 0.845" | SYN | Ø0.250" | Reduced 0.130" — ARM-008 was double-counted in raw measurement |
| Brass Shaft Collar Upper | ARM-008 | 0.130" | CONFIRMED | Ø0.970" | Commutator-side retaining collar |
| Commutator | ARM-006 | 0.405" | CONFIRMED | Ø0.970" | Copper segments; brush contact surface |
| Winding Overhang — Commutator End | ARM-004 | 0.480" | SYN | Ø0.970"→Ø1.300" | Reduced 0.085" — soft boundary with core |
| Armature Core (Lamination Stack) | ARM-002 | 0.775" | CONFIRMED | Ø1.505" | Iron lamination stack; widest point of rotor |
| Winding Overhang — Fan End | ARM-005 | 0.385" | SYN | Ø1.300"→Ø0.300" | Reduced 0.085" — soft boundary with core |
| Cooling Fan | ARM-007 | 0.325" | CONFIRMED | Ø1.300" | Draws air through UH-007 vent openings |
| Brass Shaft Collar Lower | ARM-009 | 0.100" | CONFIRMED | Ø0.560" | Fan-side retaining collar |
| Lower Journal | SHF-003 | 1.875" | SYN | Ø0.280" | Reduced 0.100" — ARM-009 was double-counted; lands on exact 1-7/8" |
| **Overall Assembly** | ARM-001 | **5.320"** | CONFIRMED | — | Stack verified ✓ |

**Motor Shaft**
- Stepped shaft design — upper journal smaller diameter than lower journal
- Upper journal: Ø0.250" (1/4") — matches BRG-001 bore; exits through UH-008 top shaft clearance
- Lower journal: Ø0.280" (9/32") — matches BRG-002 bore; larger diameter intentional, not wear
- Stepped design allows armature to be dropped in from top during assembly

**ARM-010 — Lower Journal Thrust Washer (added 2026-06-15):** stepped brass washer on SHF-003 outside the lower housing; not part of the 5.320" OAL stack (slip-on, external). Dims/function partly pending — see REWORK QUEUE under NEXT SESSION PICKUP.

**ARM-011 / ARM-012 — Lower-journal end-float washer stack (found 2026-06-19):** a stack of **4 flat washers** on the lower journal SHF-003, **inside** the housing, sitting **on top of the lower bearing (BRG-002)** at the very bottom of the armature. These shim the rotor's axial height so the **cooling fan (ARM-007) clears the lower housing floor and spins freely**. Internal — distinct from the external slinger ARM-010.
- **Material: phenolic** insulating washers (thermoset resin; reddish-brown/amber — classic phenolic), non-conductive, oil/heat-resistant. Non-metal CONFIRMED 2026-06-19; identified as phenolic 2026-06-20. Colors vary tan/deep-red/amber/dark. Armature-specific shims, not generic hardware washers.
- **ARM-011** ×3 — large fiber washers: OD **0.630"**, bore **0.2850"** (slip-fits SHF-003 Ø0.280"), thickness **0.0170"** each (CONFIRMED).
- **ARM-012** ×1 — small washer closest to the bearing: OD **0.500"**, bore **0.2850"**, thickness **0.0160"** (CONFIRMED).
- **Combined 4-washer stack thickness: 0.0650"** (CONFIRMED). *(Sum of individuals = 0.067"; stacked/seated = 0.065".)*
- **Drawing status:** ARM-011/012 already added to **ARM-001 (Rev E)** + **EXP-001/002 (Rev E)** on SHF-003.

**ARM-013 — Upper-journal end-float washer stack (found 2026-06-21):** the **upper-end MIRROR** of the lower set — **4 phenolic washers** on the **upper journal (SHF-002)**, riding against the **upper bearing (BRG-001)**, setting the rotor's top-end axial position. Same phenolic (non-conductive) material as ARM-011/012; were likewise missing from the original dataset.
- OD **0.4705"** (~0.470"); bore **0.2500"** (= upper journal Ø0.250", slip-fit); thickness **0.0175"** each (CONFIRMED). QTY **4**.
- ⚠️ **VERIFY:** whether all 4 are identical OD, or include a smaller bearing-side washer (like ARM-012 on the lower side).
- ⚠️ **Install on FINAL JOIN** — these go on the upper journal against BRG-001; they were NOT in the earlier test-fits, and the rotor's upper end-float depends on them.
- **Drawing rework (new):** add **ARM-013** to **ARM-001** + **EXP-001/002**, annotate on **SHF-002** against BRG-001.

### Stator (Field Coil Assembly)
Reference file: `Stator Assembly Dimensions - Sheet1.csv` | Parts: STR-001 through STR-008

The stationary field assembly (STR- prefix) lives inside the upper motor housing (UH-001). It does not rotate. 2-pole universal series motor configuration.

**TOPOLOGY (corrected, confirmed at bench):** The core has **two distinct pole sections (left + right) but is ONE continuous piece — not split into separate halves.** It is a single unified salient-pole core (STR-002): continuous top + bottom yoke arcs join the two inward-projecting salient poles with aggressively waisted sides. The two "half-moon" sections measured at the bench are these two pole regions of the one lamination — the measured arc/height/thickness values remain valid. (Earlier records treated it as a physically split STR-002 Left + STR-003 Right pair; that was the interpretation error — the sections are distinct but not separable. STR-003 is now VOID — geometry merged into STR-002.) All iron is laminated electrical steel stacked to the 0.736" axial height to minimize eddy-current loss on AC.

| Feature | Part ID | Arc (Outer) | Height | Radial Thickness | Confidence |
|---|---|---|---|---|---|
| Stator Pole Core (Unified, one piece) | STR-002 | 4.000" per pole region | 0.736" | 0.200" (yoke) | CONFIRMED |
| *(void — merged into STR-002)* | STR-003 | — | — | — | VOID |
| Field Coil Left | STR-004 | 2.25" | 1.65" | 0.482" (depth) | CONFIRMED |
| Field Coil Right | STR-005 | 2.25" | 1.65" | 0.482" (depth) | CONFIRMED |
| Pole Shoe Left (integral to STR-002) | STR-006 | 1.70" | 0.736" | 0.045" | CONFIRMED |
| Pole Shoe Right (integral to STR-002) | STR-007 | 1.70" | 0.736" | 0.045" | CONFIRMED |
| Stator Mount Screw | STR-008 | L 1.942" | #10-32 UNF | — | CONFIRMED |

**Pole shoes are INTEGRAL to the unified core (STR-002), confirmed at bench** — they extend inward from the outer yoke as the salient-pole tips; the field coil sits/houses in the neck between the yoke back-iron and the pole shoe. STR-006/007 are retained as named callout features of STR-002, not separable parts. Field coils are 2 (one per pole), confirmed.

**Key derived geometry (SYN):**
- Core outer radius: 1.500" (seats against housing inner bore 3.000" ÷ 2)
- Pole region angle span: 152.8° per pole arc → measured arc 4.000" / radius 1.500"
- Yoke inner face radius: 1.300" (= outer 1.500" − thickness 0.200")
- Chord hole-to-hole: 2.300" (CONFIRMED) — matches housing bolt circle; stator registration points
- **4 mounting holes total:** 2 pass-through for the housing tie-bolts (FLG-002) that clamp the two housing halves; 2 dedicated stator mount screws (STR-008). STR-001 drawing correctly shows all 4.
- Pole shoe inner face radius: ~0.773" | Air gap to armature: ~0.020"
- Field coil radial depth: 0.482" (CONFIRMED; consistent with yoke inner face 1.300" − pole shoe outer face 0.818")

### Sleeve Bearings — Confirmed Dimensions
Reference file: `Master Dimesion Upper & Lower Bearings - Sheet1.csv`

| Feature | Upper Bearing | Lower Bearing | Upper Housing | Lower Housing |
|---|---|---|---|---|
| ID (Center Bore) | 0.250" | 0.280" | na | na |
| OD (Spherical Ball) | 0.560" | 0.560" | 0.750" | 0.750" |
| Height | 0.670" | 0.700" | 0.845" | 0.845" |
| OD (Top Collar) | 0.410" | 0.440" | 0.640" | 0.640" |
| OD (Bottom Collar) | 0.410" | 0.405" | 0.465" | 0.500" |

**Key geometry notes:**
- Spherical ball (0.560") is larger than both housing bottom openings (0.465" / 0.500") — ball seats on housing socket and self-retains
- Height delta between bearing and housing (~0.145–0.175") provides pocket space for felt washers at each end
- Bottom collar protrudes through housing bottom opening; top collar retained by felt washer (OD ~0.640" to match housing bore)
- Housing OD (Spherical Ball): 0.750" (CONFIRMED) — matches spring large OD exactly; snug fit against socket wall

**Felt washer & retainer stack — per bearing:**

| Position | Upper Housing | Lower Housing |
|---|---|---|
| Top of pocket | BRG-009 Large Felt Washer (center cutout) | BRG-009 Large Felt Washer (center cutout) |
| Bearing | BRG-001 Upper Bearing; BRG-012 Spring encircles ball at equator | BRG-002 Lower Bearing; BRG-012 Spring encircles ball at equator |
| Below bearing | BRG-010 Small Felt Washer (solid disc — no cutout) | BRG-010 Small Felt Washer (center cutout) |
| Bottom of pocket | — | BRG-011 Metal Retaining Washer |

**As-built clarifications from R-8 (upper) / R-7 (lower) installs:**
- **Upper bearing (BRG-001) has an internal top-to-bottom SLIT** in the bore — the wool yarn (BRG-008) routes **through that slit** (rides inside), vs the lower housing where the yarn rides the **outside** of the ball.
- **Upper "small felt" (BRG-010) is really a solid felt TAB/PAD with only a pin-hole** (not a washer) and sits at the **very top, under the oil cap (UH-011)** — oil added at the top wets this pad and capillary-wicks down the slotted yarn to the shaft/bottom. (So in the upper housing the small felt is at the oil-cap end, not literally "below" the bearing.)
- **Upper housing has NO BRG-011** retaining ring (bottom-of-pocket is empty); the ball self-retains. BRG-011 is lower-housing only.

---

### Shaft Train / Power Head — non-motor rotating + deck parts (captured 2026-06-15)
Reference files: `Shaft Train Parts Dictionary.csv`, `Shaft Train Dimensions - Sheet1.csv`. These complete the *rotating assembly* beyond the motor. Confirmed dims:

| Part | Name | Key confirmed dims | Notes |
|---|---|---|---|
| ARM-010 | Lower Journal Thrust Washer (stepped) | outer step OD 0.8125", inner step OD 0.7825", bore 0.2800", thickness 0.1075" | On SHF-003 outside lower housing; carries rotor axial load |
| SPN-002 | Basket Drive Spindle (aluminum, 1-pc) | bore 0.2805", body OD 0.5065", **ring OD 2.703"** (CORRECTED — was wrongly 3.0505"), ring ID 2.425", ring H 0.277", **length hub-to-end 3.05"**; ring pins: dia 0.125", H 0.145", pin-circle 2.92" | Armature SHF-003 slides in, set-screwed; 3-vane impeller + hub CAST AS ONE (no discrete hub dia; 0.8500" was approx). 3 ring pins engage basket bayonet. (old 2.6960" VOID) |
| SPN-005 | Spindle Set Screw | thread **1/4-20** (RH), length 0.185", **slotted** | Locks SHF-003 in spindle bore — FULLY SPEC'D |
| SPN-006 | Basket Retention Spring (3-prong steel) | per leg 0.24"H × 0.95"L × 0.0265" thick; spread 1.91" | Compresses as basket seats |
| SPN-007 | Spring Retaining Screw (brass) | thread **#6-32** (corrected), length 0.465", head dia 0.265", slotted dome head | Holds SPN-006 to spindle hub — FULLY SPEC'D |
| PLT-001 | Platform Disk (flat metal) | OD 3.0085", thick 0.0550", center hole 0.370" (integral), 6× 0.310" holes @ 2.300" BCD | **Of 6 holes: 2 = FLG-002 bolts, 4 = PLT-005 rivets** (mount gasket to disk) |
| PLT-002 | Tapered Jar Seal Gasket | wide OD 3.5015", narrow 3.2015", bore 1.5505", H 0.8082", hole ID 0.310", seat thick 0.1805" | Molded rubber, **= reconditioned patent-1872812 seal**; **wide face on disk, narrow end into jar**; riveted to disk (PLT-005) |
| PLT-004 | Mount Standoff Tube ×2 | L 0.6990", OD 0.3765", bore 0.2020", wall ~0.087" | FLG-002 bolts pass through; set platform standoff (2 bolt holes) |
| PLT-005 | Gasket Deck Fastener ×4 | original rivet dims lost; resto = stainless M4-0.7×10 flat-head Phillips screw + SS hex nut | Fastens gasket to disk (4 of 6 holes). Original=rivet; restoration=screw+nut (reuses orig PLT-006 washers); flat head = flush |
| PLT-006 | Gasket Deck Washer ×4 (ORIGINAL) | OD 0.4385", thick 0.0415", ID 0.1570" | Original flat washer under each PLT-005 fastener; retained in restoration (ID ~M4, screw clears cleanly) |
| BSK-002 | Mesh Basket | OD 2.8025", height 2.25", 24 mesh / 0.0240" wire (opening ~0.0177"); bayonet slot: width 0.1855", axial entry 0.420", hook run 0.2700" | 3 bayonet lugs engage SPN-002 ring pins (pin-circle 2.92"); locked by SPN-006 |
| BSK-003 | Basket Lid / Cover | OD 2.70", thickness 0.086", center hole 0.1475" | Flip lid |
| BSK-004/005 | Multimovement Holder Inserts ×2 (L&R Code #10118) | dia 2.5", height 0.620" | Fine-mesh movement-holder inserts; sit inside the main basket. **First original L&R part number captured.** BSK-006/007 not present |

**Assembly chain (top→bottom):** motor (ARM/SHF) → ARM-011×3 + ARM-012 end-float washer stack on SHF-003 (internal, on top of lower bearing BRG-002) → ARM-010 slinger/thrust washer on SHF-003 (external, below housing) → SPN-002 spindle (set-screwed on; carries impeller + basket) → BSK-002 basket (bayonets onto SPN-002 ring pins, locked by SPN-006 spring) → BSK-003 lid. Stationary deck: PLT-001 disk + PLT-002 tapered gasket, mounted to lower housing by FLG-002 bolts through PLT-004 standoff tubes; gasket seals into the glass jar.

### Gemini Drawing Update Queue (2026-06-15) — feed sheet-by-sheet
Work to do with Gemini to bring the SVG package in line with the new power-head parts. Source data: the two Shaft Train CSVs + the table above.

| Sheet | Action | What to add / change |
|---|---|---|
| ✅ ARM-001 Armature | DONE — Rev C | `ARM-001_Armature_Assembly_Rev_C.svg`. Added ARM-010 stepped thrust washer on SHF-003 (OD 0.8125"/0.7825", bore 0.280", thickness EST.) |
| ✅ HW-001 Hardware schedule | DONE — Rev D | `HW-001_External_Hardware_Rev_D.svg`. Added PLT-004 standoff tube ×2, SPN-005 set screw, SPN-006 retention spring, SPN-007 brass screw (last three EST.); FLG-002 cross-ref note added |
| ✅ EXP-001 2D exploded | DONE — Rev B | `EXP-001_Motor_Exploded_Rev_B.svg`. Extended stack: ARM-010 → SPN-002 spindle → BSK-002 basket + lid; PLT deck (PLT-001/002/004) sealing into jar |
| ✅ EXP-002 3D exploded | DONE — Rev B | `EXP-002_Motor_3D_Exploded_Rev_B.svg`. Full power-head added in 3D axonometric (aluminum spindle, SS mesh basket, rubber gasket into jar, brass screw). |

**✅ GEMINI DRAWING UPDATE QUEUE — first pass COMPLETE (2026-06-15).** All sheets updated/created and the package reconciled: 12 SVGs in `drawings/`, each with a matching `.svg.txt` source snapshot; no double extensions; stale Rev snapshots retired to `archive/old_svg/Cleanup/`.

**✅ REV-BUMP QUEUE COMPLETE (2026-06-16).** All 7 sheets regenerated, double-extension/`(2)` artifacts cleaned, superseded revs archived to `archive/old_svg/` (+ snapshots to `Cleanup/`), and source snapshots resynced. Current package: SPN-002 **Rev B**, ARM-001 **Rev D**, HW-001 **Rev E**, PLT-001 **Rev B**, BSK-002 **Rev B**, EXP-001 **Rev C**, EXP-002 **Rev C** (others unchanged). 12 SVGs, 1:1 source snapshots, no orphans. What was changed:
| Sheet | Rev | Change |
|---|---|---|
| SPN-002 Spindle | A→B | **CORRECT** ring OD to **2.703"** (was 3.0505") + length to **3.05"** hub-to-end (drop 2.6960"); add ring ID 2.425"/H 0.277"; ring pins dia 0.125"/H 0.145"/circle 2.92"; flip SPN-005/006/007 to CONFIRMED dims |
| ARM-001 Armature | C→D | ARM-010 thickness **0.1075"** → CONFIRMED |
| HW-001 Hardware | D→E | SPN-005 (1/4×0.185"), SPN-006 (3-prong, legs 0.24×0.95×0.0265", spread 1.91"), SPN-007 (#6-24×0.465", head 0.265") → CONFIRMED |
| PLT-001 Platform | A→B | center hole 0.370", 6× 0.310" @ 2.300" BCD (eyelets); PLT-002 hole 0.310"/seat 0.1805"; FLG-002 through both → CONFIRMED |
| BSK-002 Basket | A→B | height 2.25", 24 mesh/0.0240" wire, bayonet slot 0.420", lid 2.70"/0.086"/hole 0.1475" → CONFIRMED |
| EXP-001 / EXP-002 | B→C | Fold in the SPN-002 corrections + all above; re-derive the stack |

Still a few small confirms before final RELEASED: SPN-002 hub label (0.8500"), SPN-005 TPI/drive, SPN-007 drive, PLT-002 taper direction, the 6-hole bolt count, which accessory baskets shipped. The rev-bump prompts are drafted (see session handoff).
| LH-001 Lower Housing | MINOR (optional) | Note FLG-002 also clamps the platform deck via PLT-004 standoffs |
| ✅ SPN-002 Spindle sheet | DONE — Rev A | `SPN-002_Basket_Drive_Spindle_Rev_A.svg` in `drawings/components/` (FIRST ISSUE). Aluminum basket spindle: bore 0.2805", OD 0.5065", ring OD 3.0505", L 2.6960"; 3 impeller vanes; 3 ring pins; set-screw cross-hole; SPN-005/006/007 shown (EST.) |
| ✅ PLT platform sheet | DONE — Rev A | `PLT-001_Platform_Seal_Deck_Rev_A.svg` in `drawings/components/` (FIRST ISSUE). Platform disk (PLT-001) + tapered jar seal (PLT-002) + standoff tubes (PLT-004) deck assembly |
| ✅ BSK basket sheet | DONE — Rev A | `BSK-002_Mesh_Basket_Rev_A.svg`. Mesh basket OD 2.8025" with 3 bayonet lugs + flip lid (BSK-003); height/mesh/lid-OD EST. |

All new/updated sheets follow the standards: 1200×800 master template, title block (June 12 2026 / Master / S/N 13505 / Hobbs R.E.), reproduction annotation, canonical Part-ID callouts, confidence labels, no `--` in SVG comments. Gemini-export gotchas: strip trailing `.svg` from `.svg.svg`; correct any auto-stamped date back to the standard.

## Document Production Standards

All technical documents produced for this project (SVG drawings, workshop manual, dimension sheets, schematics) must conform to the following standards.

### Title Block — Required Fields
| Field | Value |
|---|---|
| Date | June 12, 2026 |
| Product Name | L&R Precision Cleaning Machine |
| Product Model | Master |
| Product Serial | 13505 |
| Manufacturer | L&R MFG. CO. |
| Engineer | Hobbs R.E. |

**Model nomenclature note (changed 2026-06-20):** Use **"Master"** as the model — that is the actual cast/printed L&R model name. The earlier **"Mark 1 Master"** label was dropped: web research found that **"Mark 1/2/3" is collector shorthand (single-source hobbyist taxonomy), NOT an L&R factory designation** — nothing is stamped "Mark" on the machine. Where generational context matters, refer to the **"early oiled-bearing generation"** (which is our S/N 13505) vs. the later sealed-bearing / front-panel generations, and cite it as the collector scheme (REF), not factory fact. See External Reference Intel — Web research (2026-06-20).

### Reproduction Annotation
Every document must carry a prominent annotation making clear these are not original manufacturer documents. Use this text verbatim (adapt format to document type — notes block on SVG, header line on CSV, footer on manual pages):

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from direct physical measurement of specimen S/N 13505. Curated by Hobbs R.E., 2026. For restoration reference only.

### Part Reference Standard
All part callouts in any diagram, drawing, or document must use the canonical Part ID from `Motor Assembly Parts Dictionary.csv`. No freehand labels or aliases — every annotation that refers to a physical component must carry its Part ID (e.g. UH-003, ARM-006, STR-002) so it maps unambiguously back to the BOM.

---

## Technical Drawing Project (Engineering Blueprints — SVG)

**Goal:** Produce vintage-style mechanical engineering drawings of each machine component, then stitch into a full-assembly drawing. Working component-by-component (verify each before assembling).

**Workflow established:**
- Claude owns measurement capture, data accuracy, and handoff documentation (CLAUDE.md + CSVs)
- User feeds confirmed measurement data from Claude's CSVs into Gemini
- Gemini produces mechanical renderings and iterates on drawings via markup
- SVG files are exported from Gemini's renderings — not authored by Claude
- **SVG file storage:** `drawings/components/` (component sheets), `drawings/exploded/` (EXP sheets), `drawings/source/` (`.svg.txt` snapshots)
- SVG comments must NOT contain double-hyphens `--` (breaks XML parsing)

**Early SVG drawings (pre-workflow):** Armature, base casting plan view, and electrical schematic were authored by Claude directly in prior sessions before this workflow was established. These remain as reference but future drawings follow the Gemini pipeline above.

**Core strategy — 2D individual component profiles only:** Pipeline is strictly focused on front elevations and cross-sectional cuts of individual parts. Exploded views, multi-view nested sheets, and 3D projections are intentionally deferred until all individual parts are drawn — then tackled as a unified phase.

**Two-phase workflow going forward:**
1. **Redline Audit Loop (CURRENT):** Finalized 2D SVGs are printed and bench-audited next to the raw components. Deviations in lines, tolerances, clearances, or annotations are marked in red pen and fed back to update the master SVGs. Redline photos archived under `archive/old_svg/External Revisions/`.
2. **Exploded 3D Assembly (FUTURE):** Once every 2D dimension is locked as verified source of truth, build an axonometric 3D exploded view from the flat dataset (zone grid + title-block styling per reference IMG_1646.PNG).

**Drawing sequence:**
- ✅ Base casting plan view
- ✅ Upper motor housing (UH-001) — Rev K
- ✅ Lower motor housing (LH-001) — Rev E
- ✅ Upper sleeve bearing (BRG-001) — Rev D
- ✅ Lower sleeve bearing (BRG-002) — Rev B
- ✅ Armature assembly (ARM-001) — Rev B
- ✅ Stator / field coil assembly (STR-001) — Rev Q (unified one-piece core, confirmed)
- ✅ External hardware schedule (HW-001) — Rev C
- ✅ Motor exploded profile (2D) — `EXP-001_Motor_Exploded_Rev_A.svg` (FIRST ISSUE)
- ✅ 3D axonometric exploded showcase — `EXP-002_Motor_3D_Exploded_Rev_A.svg` (FIRST ISSUE) — gradients, depth ellipses, Rev E lower-housing detail
- ✅ **Control-unit verified as-found electrical schematic — `drawings/electrical/LR-ELEC-002_ControlUnit_AsFound_Rev_A.svg` (FIRST ISSUE, 2026-06-25)** — Claude-authored. Meter-verified 6-node circuit: P1 inlet, R1‖DS1 heater+pilot via S2, S1 4-contact transfer-switch reversing (a/b/c/d), M1 series motor, RV1 speed+OFF. Supersedes the inferred LR-ELEC-001. Next: corrected 3-wire grounded rewire schematic (R-5).
- ⬜ Neck / chrome pillar + motor bracket
- ⬜ Plunger cap, controls
- ⬜ Full assembly stitch

**7-sheet 2D motor blueprint package is 100% LOCKED — fully bench-audited via the Redline Audit Loop and ready for the open-source repo.** All sheets on the 1200x800 master template. Motor dimensional dataset complete (all parts + fasteners measured). Next drafting phase is the 3D exploded assembly. (Base/neck/control components remain out of current scope.)

### Master Template Standard (GitHub publication)
All finalized motor-package SVGs migrated to a common engineering template for the open-source repo:
- **Canvas:** 1200 x 800 engineering border
- **Layout:** balanced 2x2 orthographic grid for centering multiple views
- **Coordinates:** A–D / 1–3 margin coordinate tracking
- **Standardized:** title blocks, metadata control, technical-spec blocks across all sheets
- All hidden XML comments scrubbed for flawless rendering (no `--` in comments)

### Drawing files
SVG files live under `drawings/` (`components/`, `exploded/`, `source/`). The early Claude-authored root drawings (LR-BASE-001, LR-ELEC-001, etc.) are not in the active set; any superseded SVGs are under `archive/old_svg/`.

| File | Location | Component | Status |
|---|---|---|---|
| `UH-001_Upper_Housing_Rev_L.svg` | `drawings/components/` | Upper motor housing | DONE — Gemini Rev K. 4-view orthographic layout; 2.650" height. **Rev L: model nomenclature → Master.** |
| `LH-001_Lower_Housing_Rev_G.svg` | `drawings/components/` | Lower motor housing | DONE — Gemini **Rev F**. 4-view; 1.700" height. (Rev E rebuilt the oil wick port LH-002: true 0.600" tubular boss, wings removed, rotated to 6 o'clock.) **Rev F: added BRG-011 retaining ring seated at base of bearing pocket. Rev G: model nomenclature → Master.** |
| `BRG-001_Upper_Bearing_Rev_E.svg` | `drawings/components/` | Upper sleeve bearing | DONE — Gemini Rev D. Bronze cross-hatching, center-bore hidden layer, 1:1 true-scale cross-section; 0.560" ball OD / 0.670" height. Rev D added the Ø0.410" (CONFIRMED) bottom-collar (BRG-006) callout on the front elevation. **Rev E: model nomenclature → Master.** |
| `BRG-002_Lower_Bearing_Rev_D.svg` | `drawings/components/` | Lower sleeve bearing | DONE — Gemini **Rev C**. Asymmetries vs upper bearing: 0.700" height, Ø0.280" bore, 0.440" top collar, 0.405" bottom collar. **Rev C: added BRG-011 retaining ring callout (OD 0.500"/ID 0.295"/1/16", bottom of pocket). Rev D: model nomenclature → Master.** |
| `ARM-001_Armature_Assembly_Rev_F.svg` | `drawings/components/` | Motor armature (rotor) | DONE — Gemini **Rev F**. Landscape; 5.320" OAL, stepped shaft (Ø0.250"/Ø0.280"), commutator, winding cones, fan, brass collars (ARM-008/009). Rev E added ARM-011 ×3 + ARM-012 lower-journal phenolic stack; **Rev F added the ARM-013 ×4 phenolic end-float washer stack on the UPPER journal SHF-002 (against BRG-001); model → Master.** |
| `STR-001_Stator_Assembly_Rev_R.svg` | `drawings/components/` | Stator / field coil assembly | DONE — Gemini Rev Q. UNIFIED salient pole core (one piece): continuous top/bottom yoke arcs, two inward salient poles, waisted sides. Rev Q moved the 4 clearance holes off the cross-hatched core body out to the centers of the four 45° corner "ears", locking them onto the confirmed 2.300" bolt circle. STR-003 voided (merged into STR-002). **Rev R: model nomenclature → Master.** |
| `HW-001_External_Hardware_Rev_G.svg` | `drawings/components/` | External hardware schedule | DONE — Gemini Rev F (unified fastener sheet: FLG-002 tie-bolts, UH-004 brush caps, UH-005 set screws, LH-006 oil feed tube, SPN/PLT fasteners incl. PLT-005). **Rev G: model nomenclature → Master.** |
| `EXP-001_Motor_Exploded_Rev_F.svg` | `drawings/exploded/` | Motor assembly — exploded PROFILE (2D) | DONE — Gemini **Rev F**. Vertical exploded stack: UH-001 → STR-001 → BRG-001 → ARM-001 → BRG-002 → LH-001, extended through the power head (ARM-010 slinger, SPN-002 spindle, deck, basket). Rev E inserted the ARM-011 ×3 + ARM-012 stack (lower journal); **Rev F inserted the ARM-013 ×4 stack between BRG-001 and the upper journal; model → Master.** Reproduction disclaimer + master title block. |
| `EXP-002_Motor_3D_Exploded_Rev_F.svg` | `drawings/exploded/` | Motor assembly — 3D AXONOMETRIC exploded SHOWCASE | DONE — Gemini **Rev F**. Showcase master view: flat cross-sections projected into 3D axonometric space (scaled ellipses for depth), gradient material finishes (aluminum / steel / brass / copper / iron). Integrates power-head detail. Rev E added the lower-journal ARM-011/012 stack; **Rev F added the ARM-013 ×4 phenolic stack (phenolic finish) on the upper journal; model → Master.** Reproduction disclaimer + master title block. |
| `LR-13505-01_Armature_Assembly.svg` | (archived) | Motor armature (rotor) — OLD | SUPERSEDED by ARM-001 Rev B in `drawings/components/`. |
| `LR-BASE-001_Base_Casting.svg` | project root | Base casting — PLAN VIEW ONLY | DONE (Claude pre-workflow) — user approved. Elevations deferred. |
| `LR-Assembly-Full-Machine.svg` | project root | Full machine first-pass | SUPERSEDED — wrong base (2 wells); rebuild from verified components later |
| `LR-ELEC-001_Schematic.svg` | project root | Electrical schematic — AS-OBSERVED (motor) | SUPERSEDED for the control unit by LR-ELEC-002. Claude pre-workflow; junctions were `?`. |
| `LR-ELEC-002_ControlUnit_AsFound_Rev_A.svg` | `drawings/electrical/` | Control-unit verified as-found schematic | DONE — FIRST ISSUE 2026-06-25 (Claude). Meter-verified 6-node circuit; CTL- IDs; reproduction + title block. Supersedes LR-ELEC-001 `?` junctions. Next: R-5 grounded-rewire target. |
| `LR-MTR-EXPL-001_Motor_Housing_Exploded.svg` | project root | Motor housing — exploded parts view | REV A — 21 parts, canonical Part IDs. Rendered inline; needs export. Deferred — exploded views on hold until all individual parts drawn. |

### Base casting — geometry (LR-BASE-001, PLAN VIEW)
Source: prior session sketches + **FULL CALIPER CAPTURE 2026-07-10/11** → `docs/dimensions/Base Casting Dimensions - Sheet1.csv` (authoritative). Base-casting dimensional capture is **COMPLETE** (only BAS-008 installed tang height + BAS-002 octagon caliper-confirm + rechrome parts NCK-001/003 remain).

- **Cast-aluminum base.** FORWARD at bottom. ROUNDED / organic sand-cast form (soft radii, draft angles) — only drilled/tapped holes + the BAS-006 square socket are crisp/machined.
- **OUTLINE:** Squared top (rear wall, flat with rounded corners). **STRAIGHT left & right sides — NO waist indents, NO lobes.** At the bottom the sides transition into the forward control tongue via a subtle S-curve, then gradually curve around to a broad, rounded (not pointed) bottom.
- **4 wells** in a 2×2 grid (4.500 pitch): Heater Cyl. Well (front-left), Jar Bay 1 (front-right), Jar Bay 2 (rear-right), Jar Bay 3 (rear-left). Wells sit fully inside the body walls.
- **Chrome pillar** — square profile, centered between all 4 wells — neck/motor mount, NOT round.
- **Controls on tongue:** Rheostat knob (center, on a FLAT face — **NO cast recess** [CORRECTED]; "ON/OFF" arc + sweep arrow); Red jewel indicator (upper-left); Plunger switch button (upper-right); Toggle switch (protrudes from LEFT SIDE FACE).
- **Cast relief lettering:** "L&R MASTER" smile arc + "OFF" + "ON->" on the FLAT tongue face (no recess).
- **Side console slope:** forward-down ramp, **26.6deg** (rise 1.5 / run 3.0).

**Key CONFIRMED dims (see CSV for full set):** body 8.875 W x 9.375 D (excl. tongue) x 2.875 H; overall depth 12.875 (tongue incl.); wall 0.280; feet 0.350 proud (3 pads). Jar bays: bore 3.955, depth 1.925. Heater well: 7.375 tall, bore 3.800 (SMALLER than jar bays [CORRECTED, not larger]), cast-top ledge at 4.9075 down. BAS-006 square socket: 1.300 inside across-flats, depth 2.9035, retained by 6 screws in 2 groups (4 set + 2 post-penetrating [CORRECTED, not "3+1"]); NO oil bore. BAS-007 grommet: rear wall centered, center 1.000 up, bore 0.400 inner/0.595 outer. NCK-002 carrier: square bore 1.26, 2 mount screws 0.300/0.565 c'bore @ 2.30 c-c into UH-001. No motor interface on the base top (mounts via post+carrier).

### Drawing conventions in use
- Title block bottom-right, notes box bottom-left, header strip on top
- Arrowhead markers `arr-l`/`arr-r` defined in `<defs>`; centerlines dash-dot; hidden/depth features dashed

**Dimension confidence labels — required on every callout:**
| Label | Meaning |
|---|---|
| `(CONFIRMED)` | Direct bench measurement — caliper or tape |
| `(EST.)` | Estimated from photo proportion or best visual judgment |
| `(SYN)` | Synthesized — derived mathematically from confirmed measurements (e.g. wall thickness inferred from OD minus known interior dim) |

Any `(EST.)` or `(SYN)` callout is a candidate for upgrade to `(CONFIRMED)` when a direct measurement becomes available. Workshop manual must not publish a dim as authoritative unless it carries `(CONFIRMED)`.

### Electrical schematic (LR-ELEC-001) — AS-OBSERVED
Redrawn from the archive's ASCII "Master System Electrical Schematic" (vintage_motor_restoration_archive.pdf p.3) into proper engineering symbology for debugging. Components: M1 universal series motor, S1 plunger (momentary), LMP1 pilot lamp, R1 power resistor (lamp dropper), S2 toggle, RH1 rheostat (speed), P1 2-wire ungrounded cord. Documented series path: M1-BLK → S1 → LMP1 → R1 → S2 → RH1. Neck loom color-coded: BLK/WHT/GRN.
- **As-is only** — reflects prior non-original rework, NOT a corrected design.
- Hazards flagged: no earth ground; GREEN neck wire is a LIVE branch (not ground).
- `?` flags mark ambiguous junctions (rheostat terminals; Hot-ties-to-Green-rail) that the source couldn't resolve — verify with a meter.
- **✅ Cross-check vs FACTORY diagram E-1690 (2026-06-20):** the L&R factory wiring diagram (see CRITICAL HAZARD section + External Reference Intel) **confirms** the GREEN = motor→rheostat live branch and the in-series pilot-lamp/heater. It also suggests the plunger may be a motor-REVERSE control and the toggle the heater switch (re-check our S1/S2 roles at ring-out). Use E-1690 as the reference when drawing the verified schematic.
- **Future work (deferred):** (1) ring out the real machine and produce a verified schematic (now anchored by factory diagram E-1690); (2) draft a corrected + 3-wire grounded rewire target schematic for the upgrade phase.

### Dimensional accuracy — living refinement
Many dims are still "(EST.)" from photos/sketches. User will capture better caliper/tape measurements over time at the bench and we update the SVGs for accuracy as those come in. When the user gives a new measured value, find the matching "(EST.)" callout, replace the number, and re-label it "(CONFIRMED)". Geometry (proportions/positions) should be re-derived from confirmed dims where it matters.

### NEXT SESSION PICKUP

**▶▶ CURRENT STATE (read this first; supersedes older notes in this section).**

**🏁 THE MACHINE IS RESTORED + FUNCTIONAL — both the motor head (R-11) AND the control unit (R-5) are complete and bench-verified running on mains.** Motor runs both directions, rheostat controls speed, heater works, pilot lit; Stage-0 cold-checks all passed; first mains power-on successful (see restoration-log R-5). Wiring modernized for safety + serviceability (3-wire ground, silicone wire, Wago junctions).

**⭐ NEXT PHASE = DOCUMENTATION FINALIZATION + OPEN-SOURCE PUBLISH (the machine work is done; remaining is the repo/manual package):**
1. **Shop manual — ✅ ALL 3 PARTS DRAFTED (first draft cut).** `docs/manual/part1-operating.md` (operating cycle, controls, safety), `part2-maintenance.md` (lubrication/brushes/electrical service/troubleshooting table/cold-checks), `part3-restoration.md` (full restoration chapter: assessment, disassembly, component restoration, reassembly, R-5 rewire, commissioning). All curated from the logs; Part I+II carry a best-judgment caveat (no original L&R operating/service sheet obtained). **✅ COMPILED to DOCX:** `docs/manual/LR-Master-13505-Workshop-Manual.docx` — title page + Word TOC field + all 3 parts (page breaks between), built via a python-docx markdown converter (`scratchpad/build_manual.py`; no pandoc/LibreOffice on this machine, real Python at `AppData\Local\Programs\Python\Python312`). Structure verified (230 paras / 42 headings / 2 tables). **4 figures embedded** (base plan→Part I; wiring schematic→Part II+III; motor exploded EXP-001→Part III), rendered PNGs in `docs/manual/figures/`. **Figure render pipeline (no cairo/inkscape/LibreOffice on this box):** flatten the SVG's CSS `<style>` classes to inline `style=` attrs (else the class-based fills render black) → PyMuPDF (`convert_to_pdf` then pixmap @3x) → PIL auto-crop. EXP-002 (3D) skipped — its gradients flatten to dark silhouettes in MuPDF. Build script `scratchpad/build_manual.py` (markdown→docx converter + figure anchors). Operator to eyeball in Word + Update Field for the TOC. **Remaining:** operator review pass; optional BOM/parts appendix; optional PDF export.
2. **Drawings — ✅ PACKAGE COMPLETE (16 SVGs, source snapshots 1:1, parity verified).** All control-unit drawings now done: **LR-ELEC-003** (as-built grounded rewire, Claude-authored + Gemini-polished), **NCK-002** carrier (Rev A, Gemini via draft-seed A→B), **LR-BASE-001 Rev B** base casting (Gemini via draft-seed A→B; supersedes old plan-view Rev A, archived). Motor package (10 comp + 2 exploded) + LR-ELEC-002 (as-found) current. Gemini-render housekeeping applied (stripped [cite:N] artifacts, no double-hyphen comments, note corrections). **Remaining drawing polish (optional):** promote EXP-001/EXP-002 FIRST ISSUE → RELEASED after a final review; optional BAS-008 tang detail sheet.
3. **Repo publish** — choose LICENSE (MIT code / CC-BY-4.0 docs); `git init` (+ Git LFS for photos); organize `docs/` `drawings/` `photos/` `reference/`; write README; download factory diagram E-1690 into `reference/`.
4. **Follow-ups on the machine** (non-blocking): add a plug-in GFCI for liquid-handling use; optional verify motor run current <1 A; the donor 2nd unit is a separate future project.

*Machine-build detail below retained as history.*

**⭐ (HISTORY) MOTOR / POWER HEAD = 100% COMPLETE — assembled, wired, tested, drawn, photographed.**

**Motor close-out done this session (2026-06-23):**
- **Mechanical (Phase 2):** ARM-013 ×4 upper-journal phenolic washers installed; halves joined + FLG-002 torqued; deck (PLT-001/002) → spindle SPN-002 → basket BSK-002 → mounted to body. (M1/M2 done.)
- **Electrical:** final wiring R-11 — GREEN line lead (RED heat-shrink) → brush B; the two field coils' inner ends tie together (yellow/green band = INTERNAL coil junction, not a ground) → brush A; BLACK + WHITE = the coils' outer reversing ends → rheostat. Bench test R-10 PASS (Rigol DP932A, ~12 V/0.5 A, spins free); reversing CONFIRMED (green held +, swap Black↔White). E8 heat-shrink question RESOLVED (green=red; yellow/green=internal coil tie).
- **Drawings:** ARM-013 added (ARM-001 F, EXP-001 F, EXP-002 F); title-block "Mark 1 Master"→"Master" on all 12; date→June 12 2026; title-overflow fixed. 12 SVGs / 12 snapshots / 0 double-ext, parity verified.
- **Photos:** `photos/stator-wiring/` fully curated — R10-01/02 + R10-video (bench test), R11-01…R11-17 (final wiring), STR-001-01…11 + topology/leadID, STR-fieldlead-gauge-01/02; wiring diagram → `reference/`. Map in `photos/stator-wiring/figure-index.md`.
- **Restoration log:** R-1…R-11 written (R-5 electrical-rewire is the only future entry).

**✅ SESSION CLOSE 2026-06-25 — CONTROL-UNIT ELECTRICAL CAPTURE COMPLETE.** All components removed from the casting as a wired cluster (CU-Step 5); every component metered + maker-ID'd; full 6-node as-found netlist + plunger 4-contact transfer-switch truth table CONFIRMED; verified schematic **LR-ELEC-002 Rev A** issued. E4 + E5 + E9 closed. (Map detail in `docs/dimensions/Control Unit Wiring Map - Sheet1.csv`; raw dictations in `docs/manual/controlunit_*_raw.txt`.)
- **In-session photos are NOT on disk (chat attachments)** → land them per `photos/control-unit/figure-index.md`; file the plunger a/b/c/d sketch to `reference/LR-plunger-wiring-sketch.jpeg`. Photograph the unknown "post" piece.

**PROGRESS (2026-06-25 cont.):** ✅ All electrical components **desoldered + cleaned**. Plunger (S1) + heater toggle (S2) being **replaced** (parts awaited — see next-session item 1). ✅ **Base unit stripped down.** **NCK-001 Post + NCK-003 clamp bolt = chrome-plated BRASS (CONFIRMED — chrome flaking exposes brass); cleaned + sent OUT for professional RE-CHROME** (can't plate at home). ⚠️ Measure post OD + base bore (BAS-006) before plating (chrome adds thickness → carrier-slide/base-seat fit); mask/chase threads; light final fit after. Carrier NCK-002 (cast) = paint, not chrome.

**NEXT SESSION — CONTROL UNIT R-5 WIRING (⭐ START HERE — we are at the WIRE-CONNECTING stage; work in SMALL STEPS, confirm each before the next):**

*Status going in (all done): casting VHT-wrinkled + cured; base/neck/control + NCK-002 dims captured; **rechrome NCK-001 post + NCK-003 clamp RETURNED** (unblocked); **replacement soldering station acquired** (old Weller WESD51 died — retired); component tails prepped/color-coded/N3-banded + dry-fit into the casting; **Wago 221 junction plan set**; CTL-011 heat-shield restored; **motor head RE-VERIFIED healthy on resume** (Rigol: spins ~14 V/0.5 A, reverses both ways — restoration-log R-5 resume). Reference: the two wiring diagrams (high-level ladder color scheme + point-to-point) + verified schematic LR-ELEC-002 (6-node map). Wiring philosophy = MODERNIZE for safety + serviceability (see memory [[feedback-wiring-modernize-safety]]); document deviations honestly.*

**Colors:** BLACK=hot(N2) · WHITE=neutral(N1) · GREEN=ground only · RED=motor fwd(N4) · BLUE=motor rev(N6) · YELLOW=speed/common(N5) · RED+band=heater/lamp return(N3). Plunger: red=fwd(out), blue=rev(in), black=hot common(d/b).

Small-step order:
1. **Test-fit rechromed NCK-001 post** into BAS-006 socket (1.300" across-flats) — chrome adds ~0.001–0.003"; lap lightly if snug. Fit NCK-003 clamp (chase threads if chrome bound them).
2. **Solder RV1 rheostat tails** (new iron): **wiper → yellow (N5)**, **CCW end → white (N1)**. DeoxIt the wiper track first (track only, not the resistance wire).
3. **Make the 3 Wago distribution junctions:** **N2 hot = 5-port** (cord-L + R1-blk + DS1-blk + plunger-blk) · **N1 neutral = 3-port** (cord-N + S2-wht + RV1-wht) · **N3 = 3-port** (R1 + DS1 + S2, all red-banded).
4. **Motor legs (2-wire each):** **N4** red ↔ loom **white** · **N6** blue ↔ loom **black** · **N5** yellow ↔ loom **green** ⚠ BAND the loom green red (it's live common, NOT ground). Keep **N4/N6 serviceable** (2-port Wago) so forward/reverse can be swapped after first power-up if direction is backwards.
5. **Ground bond (W-6):** green ring lug → bare chassis under a star washer (scrape spot to bright aluminum).
6. **Stage-0 cold-checks** (cord UNPLUGGED, DMM) — safety gates: ground pin↔chassis **≤0.2 Ω**; hot↔chassis, neutral↔chassis, ground↔hot, ground↔neutral all **O.L.** Netlist: all-off hot↔neutral **O.L.**; rheostat-on+plunger both ways = motor winding+rheostat; toggle-on = **≈220 Ω** (R1 ∥ lamp). ALL must pass before power.
7. **Stage-1 bring-up:** dim-bulb tester → variac + isolation xfmr + GFCI → then mains. ⚠️ verify motor running current < 1 A vs the plunger's 1 A rating. Write up results into restoration-log **R-5**.
8. **Donor cross-validation** (when convenient) — confirm same variant + read its bulb/wiring to settle original lamp config.

**Parallel finishing streams (not blockers):**
- **Repo:** B5 download E-1690 into `reference/`; choose LICENSE (MIT code / CC-BY-4.0 docs); `git init` (+ optional Git LFS for photos); promote EXP-001/002 FIRST ISSUE → RELEASED after review; file S/N 13645 reference photo into `reference/`.
- **Shop manual:** compile Part III (Restoration) from teardown-log + restoration-log → Part II → Part I; decide output (Markdown→PDF/docx); optional TechDraw geometry-driven sheets from `cad/`.

**Runtime `(VERIFY)` — can't close at the bench:** V1 R-8 super-glue effect on long-term wicking; V2 slinger ~0.0255" running gap under power. **Optional:** V3 motor patent (~1933) Google-Patents lookup; low-priority cosmetic dims (PLT-001 eyelet collar OD, SPN-002 ring-pin material, mesh wire material).

---

**Historical detail (motor build — retained for reference):**

**DONE / status:**
- **Measurement + drawings:** full dataset captured; **12-sheet drawing package current, reconciled & fully buttoned up (2026-06-23).** Latest revs: **UH-001 L, LH-001 G, BRG-001 E, BRG-002 D, STR-001 R, HW-001 G, SPN-002 D, PLT-001 D, BSK-002 D, ARM-001 F, EXP-001 F, EXP-002 F.** 12 SVGs / 12 source snapshots / 0 double-ext (verified, parity OK). **Title-block model reads "Master" on ALL 12** (Mark 1 Master corrected); **ARM-013 ×4 upper-journal stack now on ARM-001 + EXP-001/002** (B2 done); DATE = June 12 2026 everywhere; DRAWING TITLE overflow fixed on the header-style sheets. Superseded revs archived to `archive/old_svg/`.
  - **Two title-block fixes folded into the current revs (2026-06-23, in-place — no extra rev bump):** (1) **DATE normalized to June 12, 2026** on BRG-001/BRG-002/LH-001/STR-001/UH-001 (Gemini had drifted to June 13/14); (2) **DRAWING TITLE overflow fixed** on the 7 header-style sheets (ARM-001, BRG-001/002, HW-001, LH-001, STR-001, UH-001) — the title value was running over the PART NUMBER / ID field; constrained with `font-size 10px + textLength 185 + lengthAdjust spacingAndGlyphs` (full text preserved). Source snapshots resynced. The B2 Gemini prompts now carry both fixes so the ARM-001/EXP re-renders keep them.
- **Reassembly Phase 1 (bearings & lube) COMPLETE** — lower (R-7) + upper (R-8) bearings installed, both armature test-fits good. Photos `R7-01…R7-11`, `R8-01…R8-08` in `photos/bearings/`.
- **Reassembly Phase 2 (mechanical) STARTED 2026-06-21 (R-9):** armature + 4 phenolic washers into lower housing; ARM-010 slinger pressed on (arbor-press method) to a ~0.0255" gap; two-halves test-fit good; brush caps UH-004 in (finger/rubber-mallet); stator STR-001 test-fit (its lead clip attaches to a brush port); full motor test-fit — **armature spins FREELY ✓**. Photos `R9-01…R9-08` filed in `photos/bearings/`.
- **Restoration log:** R-1, R-2, R-3, R-4, R-6, R-7, R-8, **R-9** all written. Only **R-5 (electrical)** remains, and it's future (post-rewire).
- **New parts this cycle:** ARM-011 ×3 + ARM-012 phenolic end-float washers (drawn + dimensioned). Material/data corrections all reconciled (Citristrip not Citranox; IPA pre-paint wipe; SAE F3 felt; original BRG-012 springs reused; SEKODAY = silicone oil).
- **Web research done (3 agents + Chrome read):** see "External Reference Intel — Web research (2026-06-20)". Wins: **factory wiring diagram E-1690 CONFIRMS green=live + series pilot/heater**; **patent 1872812 = L&R basket-mounting patent**; "Mark 1/2/3" = collector slang (title block → "Master"); our unit = early **oiled** generation (validates wick overhaul); rheostat ≈750 Ω, dropping resistor ≈55 W/~200–220 Ω; verbatim operating procedure captured.

**NEXT (in order) — ⚠️ SUPERSEDED: every item below is now DONE (see SESSION CLOSE 2026-06-23 above); kept for build history:**
1. ✅ **DONE 2026-06-21 (R-9):** armature + 4 phenolic washers into the **lower housing**; **ARM-010 slinger pressed on** (Dillon XL650 reloading press as an arbor press + Everbilt 3/8"×1‑1/4" fender-washer driver) — seated to a **~0.0255" running gap** (NOT bottomed). **Also done same session:** two-halves **test-fit good** (SHF-002 → BRG-001); **brush caps UH-004 hand-inserted** into the brush ports. *Phase 2 mechanical STARTED; lower housing COMPLETE.*
   **Restorer's stated next steps (acknowledged — not yet done):**
   - **Install the stator (STR-001)** into the upper housing — involves **measuring/cutting the field-coil wiring** to "just enough length for a solid connection without excess" (test-fit to get the wire lengths).
   - **Bench-test the motor on a Rigol DP932A programmable DC power supply** (standalone, NOT hooked to the main unit / NOT mains) to confirm the motor + wiring work before final assembly. The motor is a **universal (AC/DC) series motor**, so it will spin on **low-voltage DC** — ramp the voltage up slowly with a **current limit set** and watch for free rotation + reasonable draw (smoke-test). After that the upper motor-housing portion is "mostly done."
   - Then finish Phase 2: **fit the ARM-013 ×4 phenolic washers on the upper journal (against BRG-001)** → **join + torque the 2× FLG-002 tie-bolts** (UH-009 bosses; also clamp the deck via PLT-004) → platform deck (PLT-001 + PLT-002) → **spindle SPN-002** (SPN-005 set screw) → **basket BSK-002** + lid → mount to body. *(Dictate as you go → R-10+.)*
   - ⚠️ **NEW (2026-06-21): ARM-013** — 4 phenolic upper-journal end-float washers found (OD 0.4705"/bore 0.2500"/0.0175" ea; mirror of ARM-011/012). Were NOT in the earlier test-fits — **install on final join.** Drawing rework: add ARM-013 to ARM-001 + EXP-001/002 (VERIFY all-4-identical vs 3+1).
2. **Quick bench check:** look under the main cover on the **base casting for a hand-punched build date** (could date S/N 13505).
3. **Repo prep:** download **E-1690** into `reference/`; one-pass SVG title-block update to "Master"; then LICENSE + `git init`.
4. **Electrical (later):** ring out the real machine → verified schematic (anchored by E-1690) → 3-wire grounded rewire. Re-check plunger(=reverse?) / toggle(=heater?) roles; meter the rheostat (~750 Ω) + dropping resistor (~200–220 Ω).

**Open `(VERIFY)` items:** R-8 super-glue effect on long-term wicking (time-will-tell); exact green-wire color mapping (confirmed live by mechanism + E-1690, not yet by a verbatim color callout); motor patent number (~1933) not located.

---

**Measurement capture:** COMPLETE — all four sub-assemblies (housing, armature, bearings, stator) fully documented.
**Gemini drawing pipeline:** ⚠️ **STALE rev list — see SESSION CLOSE 2026-06-23 (top of this section) for current revs.** (Historical: the original 7-sheet 2D motor package was locked at UH-001 K, LH-001 E, BRG-001 D, BRG-002 B, ARM-001 B, STR-001 Q, HW-001 C — all since superseded; package is now 12 sheets at the revs listed above.) `.svg` in `drawings/components/` + `drawings/exploded/`; `.svg.txt` snapshots in `drawings/source/`; superseded revs + redline photos in `archive/`.

**✅ RESOLVED — STATOR TOPOLOGY:** The stator iron is a single UNIFIED salient-pole core (STR-002) with two distinct (non-split) pole sections. Gemini Rev Q topology is correct; bench-measured arcs (4.000" per pole region, 0.736" height, 0.200" yoke thickness) remain valid. STR-003 voided/merged into STR-002. Pole shoes (STR-006/007) CONFIRMED integral to the core (extend from yoke; coil sits in neck between yoke and shoe). Field coils = 2, CONFIRMED. Field coil + pole shoe arc/height/depth all upgraded to CONFIRMED by caliper. CSVs + Parts Dictionary updated.

**Motor dimensional dataset COMPLETE — all fasteners now measured.**
- STR-008 stator mount screw — #10-32, length 1.942", slotted headless end, plain shank + threaded tip. The SHORTER of the two yoke fastener types.
- FLG-002 housing tie-bolt — length 3.090", domed/ball slotted head 0.352" dia, thread #10-32 (major dia 0.189"). The LONGER bolt; clamps the housing halves into upper boss UH-009.
- LH-006 Oil Feed Tube — 1.296" L, 0.293" body OD, 0.247" ID/bore, ~0.023" wall, 1.000" installed protrusion.
- ✅ STR-008 ≠ FLG-002 (confirmed different): both #10-32 thread, but FLG-002 is longer (3.090" vs 1.942") with a domed head vs STR-008's slotted headless end. Both on the 2.300" bolt circle.

**Prior redline items (both resolved):**
- ✅ STR-001 4-hole count correct: 2 housing tie-bolt (FLG-002) pass-throughs + 2 dedicated stator mount screws (STR-008).
- ✅ LH-002 vs brass oil feed tube: distinct parts. LH-002 = port bore; LH-006 = the brass tube insert. HW-001 Rev C corrected the nomenclature to LH-006.

**✅ EXPLODED VIEWS COMPLETE** — both EXP-001 (2D profile) and EXP-002 (3D axonometric showcase) done at FIRST ISSUE with full reproduction annotation + master title blocks. EXP-002 date corrected to June 12 2026 to match the standard. The full drawing package is now 9 sheets (7 component + 2 exploded).

### ⚠️ REWORK QUEUE — open items that invalidate "locked" status

**🔄 STATUS UPDATE 2026-06-19 — read this first (supersedes the stale items below):**
- ✅ **ARM-010 RESOLVED** — fully dimensioned (thickness 0.1075") + function confirmed (liquid slinger); already incorporated into ARM-001 Rev D + EXP-001/002 Rev D. The ARM-010 checkboxes below are DONE/historical.
- ✅ **PLT-001/002 RESOLVED** — captured, drawn (PLT-001 Rev C), deck in the bolt stack. The PLT checkboxes below are DONE/historical.
- ✅ **DONE 2026-06-20 — Phase-1 drawing callouts:**
  - [x] **BRG-011** retaining ring → BRG-002 **Rev C** + LH-001 **Rev F**.
  - [x] **ARM-011 ×3 + ARM-012 ×1** phenolic washer stack → ARM-001 **Rev E**, EXP-001 **Rev E**, EXP-002 **Rev E** (annotated on SHF-003). Material confirmed phenolic.
  - Old revs archived to `archive/old_svg/`; source `.svg.txt` snapshots resynced; package clean (12 SVGs, 1:1).
- ✅ **DONE — procedure:** R-8 upper-housing bearing install (transcribed + logged 2026-06-20).

---

**ARM-010 — newly discovered part (logged 2026-06-15). [✅ RESOLVED 2026-06-19 — see status update above; retained for history.]** A stepped brass **Lower Journal Thrust Washer** was found on the lower journal (SHF-003, fan/basket end), riding outside the lower housing face — it had never been captured in the dataset or any drawing. Added to `Motor Assembly Parts Dictionary.csv`. Confirmed dims: outer step OD 0.8125" (13/16", housing side), inner step OD 0.7825" (~25/32", basket side), bore ID 0.2800" (9/32", slip-fits SHF-003). Likely function: thrust washer — carries vertical rotor weight against housing, sets end-float, caps downward travel (OD > LH-004 0.500" opening). Documented in `docs/manual/teardown-log.md` Step 3.
- [x] **Capture remaining dims** — DONE (ARM-010 thickness 0.1075", full dims in dictionary + CSV).
- [x] **Confirm function** — DONE (= liquid slinger, confirmed; canonical description finalized).
- [x] **Add ARM-010 to `Armature Assembly Dimensions - Sheet1.csv`** — DONE.
- [x] **Drawing rework** — DONE (ARM-010 on ARM-001 + EXP-001/002; later revs added ARM-011/012/013 too).
- [x] **File bench photos** — DONE (filed in `photos/`).
- [x] **Re-audit for other omitted slip-on parts** — DONE (found ARM-011/012/013 phenolic washer stacks; all captured + drawn).

**PLT-001/002 — platform deck + jar seal (logged 2026-06-15, was missing). ✅ ALL RESOLVED.**
- [x] **Capture dims** — DONE (PLT-001 disk + PLT-002 gasket fully dimensioned; FLG-002 stack order confirmed).
- [x] **Confirm** PLT-002 = the conditioned molded rubber seal (patent 1872812) — DONE.
- [x] **Drawing rework** — DONE (PLT-001 component sheet exists, Rev D; deck shown in HW-001 + EXP-001/002 bolt stack).

Open options for next session:
- (a) Electrical — ring out real machine → verified schematic; then 3-wire grounded rewire target schematic.
- (b) Package/repo prep — workspace already refactored into the repo structure (docs/ drawings/ photos/ reference/ archive/) with README + .gitignore. Remaining: choose a LICENSE (MIT for code + CC-BY-4.0 for docs/drawings suggested), `git init`, optional Git LFS for photos.
- (c) Any further drawing polish (e.g. promote EXP sheets from FIRST ISSUE to RELEASED after a final review).

Workflow: iterate SVG in small steps; user reviews in Chrome each time; no `--` inside SVG comments.

---

## 3D CAD Models (FreeCAD) — NEW capability, 2026-06-17
A parametric/scripted 3D model set now exists alongside the SVG drawings.
- **Tool:** FreeCAD 1.1.1. Headless runner: `C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe`.
- **Workflow:** Claude authors Python build scripts → runs them headless via `freecadcmd` → user reviews the `.FCStd` in the FreeCAD GUI (press `0` for iso, Fit all; Spacebar if a part opens hidden). Mirrors the Gemini review loop, but Claude writes the actual geometry.
- **Units:** confirmed dims are INCHES; models built in mm (×25.4).
- **Folder `cad/`:** `scripts/` (build scripts), `batch1..4/` (per-part `.FCStd` + STEP), `assembly/` (`L_and_R_Master_Exploded.FCStd` + combined STEP).
- **Modeled (~25 parts):** collars (ARM-008/009), thrust washer (ARM-010), tube (PLT-004), washer (PLT-006), platform disk (PLT-001), tapered gasket (PLT-002), lid (BSK-003), bearings (BRG-001/002, approx), spindle (SPN-002, impeller approx), basket (BSK-002, mesh shown as solid wall), housings (UH/LH, approx turned solids), rotor (ARM-001, true stacked silhouette, OAL 5.320"), stator (STR-001, approx ring), fasteners (FLG-002/STR-008/SPN-005/SPN-007). Exploded assembly = 20 objects.
- **Approximations:** organic/cast detail (impeller vane curvature, woven mesh, dome curvature, domed bolt heads, salient poles) simplified; all fully-dimensioned features are exact. STEP files are shareable/3D-printable.
- **Open follow-ons:** TechDraw drawings for the manual (see ACTION BOARD B); optional STL exports of unobtainable parts (gasket, #10118 inserts, washers); collapsed/as-built assembly; renders/animation (need GUI + external renderer).

## Voice Dictation / Transcription Pipeline — NEW capability, 2026-06-17
Offline speech-to-text for capturing bench procedures by voice (the "doctor dictation" workflow).
- **Stack:** real Python 3.12 at `C:\Users\ryane\AppData\Local\Programs\Python\Python312\python.exe` + `faster-whisper` (CPU, model `small.en`). Fully offline/local — no cloud, no phone-copy step.
- **Workflow:** user dictates on iPhone (Voice Memos) → drops the `.m4a` (e.g., into OneDrive) → Claude transcribes via a small script (`WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(path, vad_filter=True)`) → scribes the transcript into the structured logs.
- **First use:** teardown dictation (873 words) → full `docs/manual/teardown-log.md` (raw at `docs/manual/teardown_dictation_raw.txt`).
- **Note:** the restorer's dictation uses "stator"=ARMATURE/rotor and "field coil"=STATOR (opposite of canonical); logs reconcile to canonical IDs.

## Shop Manual — working files (in `docs/manual/`)
- `teardown-log.md` — **COMPLETE** 7-step disassembly (from dictation; canonical Part IDs; bearing-removal method flagged + candidate better-methods listed).
- `restoration-log.md` — R-1 gasket recondition, R-6 deck rivet→screw conversion; R-2…R-5 (refinish/clean/bearing-overhaul/electrical) to backfill.
- `manual-outline.md`, `reference-survey.md`, `shaft-train-capture-checklist.md` — structure, style survey, bench checklist.
- `part3-restoration.md` — **STARTED 2026-06-17.** III.1 Disassembly fully digested from the teardown (7 steps, prose, Fig. callouts); III.0/III.2/III.3/III.4 stubbed. R-2/R-3/R-4 still to backfill. Figures TBD from `photos/` + `drawings/` + line-art.
- **Manual styling:** target a VINTAGE L&R look (black section banners, justified serif body, margin figures with leader callouts, caps cautions, running header + page numbers) — a styled HTML/CSS preview of III.1.4 was approved; that CSS becomes the typeset template. Presentation layer is separate from the `.md` content; typeset to PDF/HTML once content locks.
- **NEXT for the manual:** backfill R-2/R-3/R-4 into Part III; map which `photos/` shots cover which Fig. callouts (line-art fills gaps); then typeset Part III to a vintage-style PDF.

## External Reference Intel — WatchRepairTalk (mined 2026-06-19, tag REF)
Sources: watchrepairtalk.com "L&R Cleaning Machines" + "How to open the motor on an L&R Master" threads (+ a partly AI-generated maintenance writeup). May include Mark-2 / inaccurate info — all tagged REF, verify against bench.
**Corroborates us (independent confirmation):**
- **ARM-010 = a "slinger"** — forum consensus: the grooved disk on the shaft just below the motor housing keeps cleaning-jar fluid from wicking up into the motor. Resolves our open ARM-010 function question (was thrust-washer-vs-slinger). Updated in motor dictionary + teardown-log Step 4.
- Our **teardown sequence** matches other owners' (bottom ring → slinger → lower case spins free → stuck bearing → bearing puller).
- **SPN-002 impeller/spindle** (friction-fit + set screw, holds baskets, "paint-stirrer" 3-blade) and its **fragility** confirmed; basket **≈ 2¾"** independently confirmed.
**Actionable:**
- **Step-7 bearing removal (answers the open call):** internal-jaw / blind-hole bearing puller (e.g. HF #95987) or DIY hex-bolt+pipe+washer+nut; penetrating-oil soak for dried fluid; heat the Al housing; never steel-hammer the casting. (Added to teardown-log Step 7.)
- **STL print candidates (prioritize from our CAD):** brush caps **UH-004** and impeller **SPN-002** — both commonly crack/break per the community; our open-source STL exports would be genuinely useful. (Others already use FreeCAD for these.)
- **Electrical:** the ceramic "heater" resistor current-limits the motor at full rheostat; community replacement = **Dale 40 Ω**. ⚠️ **CORRECTED 2026-06-20 (web research):** the **40 Ω is the motor FIELD-COIL resistance**, not the lamp dropping resistor — the **pilot-lamp dropping resistor is ~200–220 Ω / 50 W.** Ring out our actual resistor before ordering. (See External Reference Intel — Web research.)
- Reference video to pursue: "L&R Master Watch Cleaning Machine Restoration and Wiring" (YouTube).
**⚠️ Conflicts — DO NOT adopt without bench verify:**
- AI writeup claims a single conical spring in the UPPER housing as an axial preload over the shaft. **Our bench data:** BRG-012 conical springs at BOTH bearings, encircling the spherical ball at the equator (centering/retention) — CONFIRMED + matched replacement. Trust our measurement; verify spring role during reassembly.
- WD-40/penetrating oil OK on bare metal only — keep OFF rubber (we ruled it out for elastomers).

## External Reference Intel — Web research (2026-06-20, tag REF; Google Patents = primary/CONFIRMED, forums = REF)
Background research agents (web). Primary sources tagged where found; forum/dealer items are REF — verify against bench.

**★ Patent US 1,872,812 — CONFIRMED (primary, Google Patents https://patents.google.com/patent/US1872812A/en):**
- Title **"Watch Cleaning Machine"**, inventor **Frank Regero**, assignee **L & R Manufacturing Co.**, **filed 1930-07-11, granted 1932-08-23.**
- It is **NOT a gasket/seal patent.** It covers the **basket-mounting mechanism**: a depending rotatable shaft + a holder with **radial spring arms**, and a **wire-mesh basket with a rim + locking means** that snaps onto those arms (attach/detach) — plus nested mesh baskets and a cork-lined cover. **This directly matches our power head: SPN-002 spring-arm holder + BSK-002 bayonet basket.** Independent corroboration of our reverse-engineered basket design.
- ⇒ The "U.S. PATENT 1872812" molded into our rubber jar-seal (PLT-002) is **L&R's foundational machine patent used as a maker's mark — not a patent on the seal itself.** Pushes L&R's machine lineage back to **1930**.

**★ Control switches — Arrow-Hart & Hegeman (Arrow H&H) — maker ID + dating (2026-06-25, REF):** Both control-unit switches (plunger S1 + heater toggle S2) are stamped **"ARROW H&H ... MADE IN U.S.A. ... UND. LAB. INSP'D"** (one also **"TYPE 3392, 1A 125 VAC"** = the plunger). **Arrow-Hart & Hegeman Electric Co., Hartford CT** — formed by the **1927–28 merger** of Arrow Electric + Hart & Hegeman; major US maker of toggle/safety switches & motor starters (supplied DeWalt et al.); later Cooper Industries → **Eaton (2012)**, brand "Arrow Hart" still used. **Bakelite housing + braided cloth leads + UL stamp ⇒ ~1930s–60s.** Dating note: the **1928 merger is a terminus post quem** — these switches (and this wiring) are **≥1928**, consistent with our ~1936–47 machine estimate, though they could equally be **early-service-era replacements** (the unit shows prior rework). *(Source: user/Gemini analysis of the stamps; company history is general reference.)*

**"Mark 1/2/3" nomenclature — collector shorthand, NOT L&R (REF):** No "Mark"/model sub-designation appears cast or printed on the machines. The widely-repeated scheme (origin: watchuseek "Respect the elder — L&R Master redone" thread) is **Mk1 = oiled bearings 1936–46 · Mk2 = sealed bearings ~1947 · Mk3 = front-panel redesign 1948.** Our internal "sleeve = Mark1 / roller = Mark2" binary does **not** cleanly map to that documented oiled→sealed→roller progression — so **treat our "Mark 1 Master" label as internal shorthand, not factory nomenclature** (consider for the title-block standard). Bearing-type variation IS real (some Masters used cylindrical roller bearings; ball/sleeve substitution works if speed kept down).

**Serial dating (REF inference):** No public L&R serial→year table. Serials run into the 17,000s. Our **S/N 13505** most plausibly sits in the **1936–1947** window (earlier topology: no front panel, rheostat tongue, sleeve bearings) — inference, not documented.

**Operating spec (REF, from manual snippets):** variable rheostat; run at **moderate speed — "correct" speed makes fluid rise ≈1.5" up the jar wall**; **reverse the basket several times in each jar**; **~3 minutes per jar**; clean → rinse → dry; factory fluid = **L&R "Extra Fine" Watch Cleaning Solution #109**. (Full manual is NAWCC JPEG scans + Scribd 456605930 — both paywalled/403 to auto-fetch; a Chrome-driven read could capture the verbatim text.)

**Part numbers (REF, dealer/secondary — NOT confirmed L&R factory):** Dave's Watch Parts SKUs: **wt10149** (Master 2¼" basket top), **wt10152** (2¼" mid), **wt11318** (glass jar). eBay basket screen marked **#517J**. ⚠️ **Our "#10118 Multimovement Holder Inserts" could NOT be corroborated online — downgrade to UNVERIFIED** until a source/label confirms it.

**Electrical (REF — NAWCC snippets):**
- Motor = universal series AC/DC, brushed, **~60 W**. Rheostat = ceramic wirewound, clockwise = start/faster. (Corroborates us.)
- **Pilot lamp is wired in SERIES and acts as a FUSE** — "the power runs through the pilot light; if the bulb is dead, so is your heater." Signature L&R design; **corroborates our schematic's inline bulb→resistor path.**
- **⚠️ RESISTOR-VALUE CORRECTION:** the "**40 Ω**" figure in our earlier WatchRepairTalk note is the **resistance between the two motor FIELD COILS (~40 Ω)** — NOT the lamp dropping resistor. The **pilot-lamp dropping resistor is ~200–220 Ω / 50 W** (e.g. #41 2.5V ½A bulb in series w/ 220 Ω; or 6S6 12V ½A w/ 200–220 Ω). Bulb spec is **model-dependent** (#41 2.5V, or 6V, or 6S6 12V) — identify the socket before buying. **Ring out our actual resistor to settle it.**
- **Green neck wire = corroborated-by-mechanism (still bench-verify):** the 3-wire white/black/green neck loom appears **only on REVERSIBLE-motor models** (reverse = swap armature-vs-field polarity via a switch). So the neck green is an **internal live motor lead**, exactly as we state. The common forum "green = ground" advice refers to the **NEW 3-prong cord's** green, a *different* wire — not a contradiction. (Our machine HAS the 3-wire loom ⇒ it is a reversible model — see Controls flag below.)
- **Parts sources (REF):** eBay (motor resistor, bearing sets, brush-cap sets, "The Agitator" auto-reverse mod, jar adapters); **Dave's Watch Parts**; **L&R still stocks propellers + basket drive-spring parts** that screw onto the propeller.
- **Documented failure points:** seized motor bearings; **crumbling 18/3 motor-wire insulation → ground faults** (matches our replace-all-wiring plan); cracked propeller/impeller (SPN-002, friction-fit + set screw); the **two flat basket drive springs lose tension**; dead pilot bulb kills the heater (series-fuse).
- **3D-print candidates (community confirms none published yet — our STLs would be novel):** jar/basket adapter & positioning rings (best first), the **propeller/impeller (SPN-002)**, knob/lens bezel/red-jewel retainer, wire-retainer clips. AVOID printing heater-well, resistor mounts, bearing seats, drive-spring interfaces.

**History / manual (REF — single-source unless noted):**
- **Mk1/2/3 years (1936–46 / ~1947 / 1948) trace to ONE watchuseek post**, repeated downstream — treat as single-source hobbyist taxonomy, NOT factory fact. Only **"L & R" and "MASTER"** are cast on the machine; no "Mark" is stamped.
- **Bearing generations:** early Master = **OILED bearings** (oil access hole on top of the motor housing — matches our **UH-011 oil cap / UH-010 oil channel / wick system**); later (~1947) = **SEALED** bearings, which is the generation whose manual says the motor **"never requires oiling."** ⇒ **Our S/N 13505 is the EARLY OILED generation — it DOES require oiling, and our wick/oil overhaul (R-4/R-7/R-8) is correct for it.** Do NOT cite "never requires oiling" for our machine. Roller-bearing variant = **unconfirmed** (only oiled-sleeve vs sealed documented; our spherical sleeve fits the oiled gen).
- **Operating procedure (read first-hand from NAWCC 5004; manual quoted verbatim by R. Huegel + practice from D. Sinclair):**
  - Jars: cleaning jar = **L&R "Extra Fine"** solution to the middle of the "L&R" letters; two rinse jars = **L&R #3 Rinse**.
  - **Manual (verbatim):** "run each station for **three minutes with frequent reversals** at a speed that will keep the liquids from splashing out of the jars (**about a medium speed**)." Correct speed = fluid rises **~1.5" up the jar wall** with small bubbles; never fast enough to splash.
  - **Why reverse:** centrifugal spin makes air bubbles cling to the parts and block cleaning — **reversing breaks them up**; reversing also cleans **half-disassembled movements** (fully-disassembled parts don't need it).
  - **Practice (D. Sinclair):** brief **spin-off at ~25% speed** (or "not so fast the machine shudders") between stations; **~2 min in each rinse**; **~5 min in the heated drying chamber**, moderate speed throughout. (The basket runs slightly eccentric to the arbor — moderate speed protects the machine + movement.)
- **⚠️ CONTROLS FLAG (re-interpret during ring-out):** a manual snippet calls the **red plunger button a REVERSING control** and the **toggle the HEATER (drying) switch.** Our schematic currently reads the plunger as "Hot distribution to motor" and the toggle as a "legacy mode" switch. Since our machine is a reversible model (3-wire loom), the **plunger may actually be the motor-reverse control and the toggle the heater switch** — verify against the wiring during the electrical phase.
- **Baskets:** two factory sizes — **small** (clips on arms INSIDE the ring) and **large** (~deeper, clips on tabs OUTSIDE the ring, for 18-size); diameters **2¼" (small)** and **2¾" (large)**. Part **#517J** = a 4-compartment basket screen (a real part-number sighting). **#10118 remains UNVERIFIED.**
- **Serial dating:** no public chart; serials reach the 17,000s (17879 attested; its "=1947" is a search-engine guess). **13505 ≈ 1936–1947** by inference only.
- A separate **L&R motor patent (~1933, expired 1950)** is what collectors use for dating: patent text still on a casting ⇒ pre-1950 build. Our casting still bears patent text ⇒ pre-expiry. (Patent number not yet located — follow-up.)

**★ Chrome-driven direct NAWCC reads (2026-06-20) — first-hand, upgrade these from snippet-grade:**
- **★★ FACTORY WIRING DIAGRAM E-1690 — PRIMARY SOURCE (read directly):** L&R's own "Wiring Diagram — Master W.C.M.", drawn **P.H.**, dated **3-24-60** (supersedes the **4-19-50** drawing), "used on A-4100", L&R Mfg. Co. (NAWCC attachment, "manual needed" thread 41996). Topology: **A.C. LINE (with earth GND at the line) → motor (BLACK + WHITE leads); GREEN runs motor → RHEOSTAT (speed); HEATER + PILOT LIGHT in series on the line.** **CONFIRMS our "green = live motor-to-rheostat branch, not ground"** and the **series pilot-lamp/heater (bulb-as-fuse)**. Caveat: 1960 revision (ours is the earlier oiled gen) — topology still matches our 3-wire loom. **Action: download E-1690 into `reference/` for the repo.**
- **Rheostat = a ~750 Ω potentiometer** (NEW value we lacked). It's rare; people substitute a **500 Ω pot**, or a 500 Ω pot + a series power resistor. (NAWCC 198512.)
- **Dropping/"heater" resistor ≈ 55 W** factory; a **PTC heater element (30 W or 50 W, ~110 V)** is a clean modern replacement and mounts on the **same copper band/strap**. Original resistors are scarce (occasional eBay). Heater elements also via **Dave's Watch Parts** (Dave = the board admin). (NAWCC 198512.)
- **Motor patent: granted 1933, expired 1950** → dating bracket: if patent text is still on the casting, the machine predates ~1950. **Our casting still bears patent text ⇒ pre-1950.** (Separate from the 1932 basket patent 1872812; the motor patent number is still not located.) (NAWCC 198512.)
- **⭐ ACTIONABLE dating tip:** some L&R units (Vari-Matic noted) have the **manufacturing date hand-punched into the BASE, under the main cover.** → **Check our base casting under the cover for a hand-punched date** — could date S/N 13505 directly. (NAWCC 198512, WoodyR.)
- **Reversible-motor mechanism (corroborates our 3-wire loom = reversible):** reverse by a **DPDT switch that swaps the armature vs. the field windings** (brush leads brought out). Note an "unbalanced" universal motor runs with only one field winding; brush "connection angle"/phasing is optimized for one direction, so reversing can increase arcing. (NAWCC 150973.)
- **Bearing removal — independently corroborates our Step-7 method:** pry the end-bell cap with **two screwdrivers 180° apart**; **warm the bell** to soften hardened grease; tap the shaft with a **small drift**; never force. Sealed-bearing motors have **no end cap** (a quick oiled-vs-sealed tell). (NAWCC 36053.)
- **Rewiring technique (community):** solder new leads to the field coil, **tie them down with heavy dental floss**, shrink-tube the splice, and **seal the joint to the winding with RTV or epoxy.** (NAWCC 36053.)
- **Still NOT captured (locked in non-text media):** the **verbatim operating manual** (NAWCC JPEG scans / Scribd embed / watchuseek PDF — all images or paywalled) and the **exact green-wire color mapping** (lives in a wiring-diagram image, not forum text). Our "neck green = live" remains corroborated-by-mechanism, not yet by a verbatim diagram. **watchuseek is domain-blocked** even in-browser. To get the manual verbatim would need OCR of the JPEG scans or hand-transcription.

**Access note:** NAWCC (readable in a logged-in browser), watchuseek (domain-blocked), watchrepairtalk, learntimeonline, Scribd all block automated WebFetch (403/paywall) — agent-phase detail came from search snippets only; the Chrome-read items above are first-hand. The richest untapped primary sources (the **NAWCC manual JPEG scans**, the **watchuseek "Respect the elder" restored-manual PDF + rewiring photo-essay**, NAWCC threads 198512/150973/36053/5004) would need a **Chrome-driven, logged-in browser read** — that would likely settle the live-green-wire detail, the exact resistor/bulb values, and capture the full verbatim manual.

## Parts & Materials Reference
| Item | Product | Notes |
|---|---|---|
| Topcoat | VHT SP201 Wrinkle Plus | Black wrinkle finish |
| Primer | Rust-Oleum 249322 Self-Etching Primer | Zinc phosphate base |
| Finish stripper | Citristrip (citrus paint & varnish stripper gel) | Strips factory enamel/varnish off the aluminum castings (R-2); safe on aluminum |
| Basket cleaner | Citranox solution (some mesh basket pieces) | Phosphate cleaner; NOT used for paint stripping |
| Gasket lubricant | SEKODAY Treadmill Belt Lubricant (silicone oil, non-cracking type) | 16+ hr soak; silicone = for rubber/plastic, NOT metal (per mfg) |
| Bearing yarn | Estako Wool 98 — 100% Superwash Merino Worsted, Off-White | Reservoir packing |
| Bearing felt washers | SAE F3 wool felt washers — small (BRG-010) + large (BRG-009) | Dust/retaining washers; CONFIRMED as-installed R-7 (supersedes earlier "Singer F-1" note, which was an error) |
| Motor oil | Bramec Zoom Spout multi-purpose turbine oil | Pre-lube felts + wick (R-7) |
| Oil wick (as-installed R-7) | GE 1/8" oil wick (vintage-fan type), ~1¼" cut + wool yarn reservoir (BRG-008) | routed through oil-wick port; capillary feed |
| Brass punches | Grace USA brass flat punches | seat BRG-011 retaining ring / no-mar tapping |
| New power cord | 3-conductor 16AWG, NEMA 5-15P plug | Grounding upgrade |
| Ground terminal | Heavy-duty crimped brass ring terminal | Chassis bond |
| Star washer | Standard internal-tooth star washer | Under chassis ground screw head — bites bare aluminum |
| Internal harness wire | 16 AWG Silicone, 125°C min (or PTFE) | Replace all internal wiring; avoid PVC near resistor well |
| Neck cable (replacement) | SJOOW 16 AWG/3 portable power cable, 300 V, −40/+90 °C | Motor↔control neck run; replaces brittle original loom. ⚠️ neck GREEN = LIVE branch, NOT ground |
| Neck cable cosmetic sleeve | Braided expandable sleeve + heat-shrink ends | Vintage cloth-cover aesthetic over the SJOOW neck cable |
| Bearing spring (BRG-012) | ORIGINAL factory springs REUSED | 302/304 SS tapered conical; large OD 0.750", small OD 0.500", free length 0.440", wire 0.0625"; 2 per machine. **Originals reused in R-7/R-8** — not replaced. Century Spring **TA-2226CS** identified as the dimensional equivalent / source-if-needed, but NOT installed. |
| Platform gasket fastener (restoration) | Stainless M4-0.7 × 10mm flat-head Phillips screw + stainless M4-0.7 hex nut (×4) | Replaces the 4 original PLT-005 rivets (drilled out to service gasket); REUSES the original washers (PLT-006, OD 0.4385"); flat countersunk head sits flush |
| Bakelite polish (control trim) | Simichrome (or Brasso) metal polish → Novus 2/1 plastic polish | Cut oxidation off the CTL-002 rheostat knob + CTL-003 plunger cap + any phenolic trim; hand-polish only (no power buffer); brush the knurl, stay off molded lettering |
| Bakelite sealer | Renaissance Wax (or light mineral oil) | Seal polished phenolic for depth + slow re-oxidation; apply AFTER any paint-fill cures |
| Knob marking paint | Testors gloss white enamel #1145 (or enamel paint marker) | RE-FILL the faded white arrow line on CTL-002 by paint-fill wipe-back; degrease groove first; wipe back across the line; cure 24 h before sealing |

## Bench Test & Rework Equipment — Reassembly & Commissioning Phase (earmarked 2026-06-25)
**Recall at the reassembly/test phase.** Equipment TYPES + key specs + representative examples to source (Amazon/etc.) — **verify current listings/specs before buying; no prices recorded (they change).** Already on hand: **Fluke 112 DMM** (continuity/Ω/V) + **Rigol DP932A** DC supply (low-V motor test). The list below fills the AC-commissioning + rework gaps. Goal: bring the machine up SAFELY and accurately before mains (see Stage 0/1/2 commissioning plan).

**A. Safe powered bring-up (Stage 1, before mains):**
- **Dim-bulb tester** — series-incandescent current limiter; THE #1 first-power-on safety device. Buy ready-made ("dim bulb tester") or DIY (metal box + lamp socket + outlet + 60–100 W *incandescent* bulbs). A dead short makes the bulb glow bright & starves the fault.
- **Variac / variable autotransformer** — bring voltage 0→120 V gradually while watching current. ~500 VA (≥5 A) ample (e.g., TEMCo, VEVOR). ⚠️ Does NOT isolate — pair with isolation xfmr.
- **Isolation transformer** — 1:1, ~150–300 VA; breaks the hot–chassis tie for safe probing (e.g., Triad N-68X or generic).
- **GFCI outlet/adapter** — plug the machine in via GFCI for first runs; trips on ground fault.

**B. Measurement (AC commissioning):**
- **Plug-in power meter** — Kill A Watt (P3 P4400/P4460): V / A / W at the outlet. Confirms **motor running current vs the 1 A plunger rating** + heater wattage.
- **AC clamp meter** — in-line motor current, non-invasive: Fluke 323/325 or budget UNI-T UT210E (true-RMS, low range). Pair with an **AC line splitter (1×/10×)** to clamp a 2-wire cord.
- **IR / contact thermometer** — monitor the Ohmite heater resistor temp during bring-up (~65 W, runs hot); confirm not overheating.
- **(Optional, most accurate) Insulation tester / 500 V megohmmeter** — winding/wire-to-chassis insulation check before mains (gold-standard pre-power safety).

**C. Rework & assembly** (you found bad prior solder blobs + want clip terminals):
- **Temperature-controlled soldering station** + rosin-core solder, **flux**, **desoldering braid + solder sucker** — redo the nasty joints cleanly.
- **Insulated quick-connect/clip terminals (FASTON/spade)** + **ratcheting crimper** + **heat-shrink** — the organized, serviceable connections per the roadmap.
- **Helping-hands / PCB holder**, **fume extractor**.

**D. Contact cleaning:**
- **DeoxIt D5 (Caig)** — clean the dirty plunger contacts + rheostat wiper (closed-contact R was 1.3–3 Ω = oxidized).
- **Fiberglass scratch pen / contact burnisher** — for the oxidized switch contacts + rheostat track.

## Donor / parts unit (second machine)
A **second identical L&R Master** (much rougher, more used) was acquired as a **parts + reference donor.** Notes:
- Its **carbon brushes are shorter (more worn)** than our specimen's — grabbed as spares "just in case" during the R-10 debugging; our machine keeps the better (longer) pair.
- Its **bakelite brush-cap is broken** (only the brass insert remains) — the trigger for the brush-cap reproduction options below.
- The **slinger-to-housing gap reference (~0.0255", R-9 / ledger V2)** was measured off this donor unit (our as-found gap wasn't recorded before removal).
- Keep it for spares + dimensional cross-checks. *(It will itself be restored later — separate project.)*
- **★ CONTROL-UNIT ELECTRICAL CROSS-VALIDATION (planned 2026-06-25):** use the donor as a **second independent reference** for the open control-unit electrical items — esp. the **original lamp config (series vs parallel)** we can't pin on our (reworked) unit. Check on the donor: its **bulb voltage + lamp-branch wiring** (12 V-series ⇒ original was series; 120 V-parallel ⇒ parallel is original), the **plunger 4-terminal DPDT wiring**, **RV1 (~425 Ω) / R1 (~220 Ω) values**, **switch makers/types** (Arrow H&H? Type 3392?), and whether it has the **unknown "post" piece** in place. **Caveats:** (1) confirm the donor is the **same variant** (serial range, oiled-vs-sealed bearing, panel style) before treating it as like-for-like; (2) the donor may **also be reworked** — scan for non-original signs (modern wire, wire nuts, China/Taiwan bulbs) first. **Read:** both agree ⇒ high confidence it's original/typical; they differ ⇒ that difference flags a variant or a rework on one unit.
- **★ FIRST DONOR CHECK (2026-06-25):** donor **wiring looks the SAME as our unit — no additional/new parts visible** (donor appears *less* modified than ours). ⇒ **Moderate evidence the parallel lamp topology is ORIGINAL/typical, not a rework artifact** (downgrades the "our lamp branch was rewired" idea; our unit's rework may be limited to consumables like the 2018 bulb). **Still open:** (a) donor **serial is PAINTED OVER** → confirm variant by physical tells instead (bearing type oiled-vs-sealed, panel style); (b) donor **bulb voltage unread** (tight spot) — but if its wiring is parallel like ours, the bulb is almost certainly ~120 V (a 12 V bulb in parallel would blow). Net: "parallel/120 V = original/typical" now at **moderate confidence**, not fully closed.

## Parts — Repair / Replace / Reproduce (reference; best-judgment, no factory spec)
Captured as **options** for the open-source manual (most not yet performed on our specimen):
- **Sleeve bearings (BRG-001/002):** replace (eBay "L&R Master bearing set"), re-bush, or **make-your-own on a lathe/CNC** from **SAE 660 / C932 bearing bronze** (turn bore + spherical OD + collars; ream/hone the bore to ~0.001–0.002" clearance; match the ball OD to the housing socket). **3D printing NOT viable** (running surface). **JB Weld** only for a static crack in the bearing's outer body or to retain it — **never the running bore.**
- **Carbon brushes (UH-004 internals):** a **wear consumable — fully replaceable.** Cylindrical carbon on a copper pigtail. Buy **carbon brush stock to the measured diameter**, cut to length, **bed the face to the commutator radius**, attach/solder the pigtail. (Worn/short brushes are normal end-of-life, not a fault.)
- **Brush cap (UH-004 body — bakelite + brass insert):** ⚠️ **bakelite is a THERMOSET — it does NOT melt, so you CANNOT heat-set the brass into it** (heat-set inserts only work in thermoplastics). To reproduce a broken cap:
  - (a) **3D-print the cap in a heat-resistant THERMOPLASTIC** (PETG / ABS / ASA / nylon / PC, or high-temp SLA resin) and **heat-set the brass in** — the standoff/insert trick, just in a printable plastic (not bakelite). *(NOT PLA — too low-temp.)*
  - (b) **Machine a new cap from black phenolic / Garolite (G10) rod** (bakelite-like, oil/heat-resistant, machinable) and **press-fit or epoxy** the brass in (machined phenolic is thermoset → can't heat-set). Most authentic; fits the lathe-repro path.
  - (c) **Cast a resin replica** from a mold of a good cap, embedding the brass.
  - Material must be an **insulator** (the cap isolates the brush from the housing). Phenolic resin is still made industrially (rod/sheet readily machinable), but you **can't mold or 3D-print a thermoset at home.** *(Not yet done — option only; the broken cap is on the donor unit.)*
- **Parts sourcing (REF):** eBay (bearing set, brush-cap sets, jar/adapters, "Agitator" reverse mod); **Dave's Watch Parts**; **L&R** still stocks propellers + basket drive-spring parts. **#517J** = a basket-screen part number. (See External Reference Intel.)

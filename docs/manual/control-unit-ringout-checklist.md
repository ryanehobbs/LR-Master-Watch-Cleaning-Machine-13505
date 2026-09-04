# Control Unit Electrical Ring-Out & Connection-Map Checklist
### L&R Master Watch Cleaning Machine, S/N 13505 — Control Unit (CU-001)

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from hands-on restoration of specimen S/N 13505. Curated by Hobbs R.E., 2026. For restoration reference only.

**Goal:** Produce a *complete, terminal-by-terminal, as-wired connection map* of the control unit **before any component is removed**, so the machine can be (a) drawn as a **verified as-found schematic** (replacing the inferred LR-ELEC-001) and (b) correctly re-wired with a safety ground. This is the **gate** for Phase-1 component removal — once a wire is cut or a lug disturbed without being logged, the actual as-wired state of *this* unit is lost (E-1690 only gives the generic factory intent, and this unit already shows prior-restoration rework).

**Accuracy doctrine (user directive — "very very very detailed and accurate"):**
- **Nothing leaves the casting until its every wire is logged AND photographed with tags visible.**
- Every physical terminal gets a **printed/tape tag** with its node name (below) **before** ringing out.
- Record **both ends** of every wire as a directed segment. A wire is not "done" until both endpoints are named.
- Capture **wire color, gauge (AWG/visual), insulation type** (cloth / rubber / PVC / bare-tinned), **length**, and **routing** (which side, through which hole, over/under what).
- Note **every splice, twist-solder joint, solder blob, terminal strip, or ring-lug** as its own node (these are the CTL-010 junctions).
- Tag confidence on EVERY reading: **(CONFIRMED)** metered/seen · **(EST.)** visual · **(SYN)** derived · **(ASSUMED)** not yet verified.

---

## 0. SAFETY & BENCH SETUP — do first, every session
- [ ] **Cord unplugged from mains the entire time.** All ring-out is **un-powered, DMM only.** (Powered tests happen later on the Rigol DP932A per the cold-check matrix — NOT here.)
- [ ] Original AC cord (CTL-008) already removed — confirm **no other energy source** (no capacitors expected in this resistive/series design; if any cap is found, short its leads with an insulated screwdriver and log it).
- [ ] DMM checks: fresh battery; verify continuity-beep on shorted leads (~0 Ω) and OL on open leads before trusting readings. Note meter lead resistance (zero it / subtract it — matters for low-Ω windings & the lamp).
- [ ] Good light + magnification on the underside; phone camera ready for macro.
- [ ] Soft jaws / no scratching the casting (it gets refinished, but threads/bores must stay clean).

## 0b. PRE-REMOVAL GATE & DISASSEMBLY CAPTURE (added 2026-06-25)
**Why:** the as-found joints are dirty/corroded with shared solder blobs → in-situ resistance readings are unreliable (a crusty joint adds ohms and can read a real connection as a false OPEN). So **accurate values are taken in-hand after removal on cleaned terminals**, not in-circuit. The connection map already came from a **visual wire-trace** (meter was only a cross-check), so it stands.

**Point of no return = cutting/desoldering before tagging.** Before the iron touches anything:
- [ ] **Tag every terminal** with its industry label (P1-L, RV1-W, S1-COM, R1-1, DS1-TIP, M1-S2 …) — tape flags.
- [ ] **Photograph each joint with tags visible** (most done — confirm every lug legible).
- [ ] **DS1 bulb rating read** ✅ (12 V/6 W).
- [ ] Optional quick **node-to-chassis** glance *if probes still reach bright metal* (else do post-removal).

**Disassembly capture — resolves the last two unknowns physically:**
- [ ] **As you unsolder each blob, count + tag EVERY wire entering it before it separates.** A blob joining N wires *is* a node — separating it directly shows the true structure (fixes the R1/DS1/S2/S1 series-vs-parallel mislabel on the spot).
- [ ] **Plunger (S1):** tag its wires, remove, **bench-test in-hand** — DMM continuity across all lug pairs in OUT vs IN → assign COM/NO/NC. Count its lugs first (3 ⇒ SPDT reverse: COM=hot, NO/NC=M1-S1/M1-S2).
- [ ] **RV1 wiper lug:** note which lug rides the moving arm = RV1-W (visual).

**In-hand metering discipline (clean readings):**
- [ ] Meter on the component's **own terminals**, never through a harness joint.
- [ ] **Clean the lug to bright metal** (fiberglass pen / fine abrasive / DeoxIt) before probing.
- [ ] **Zero leads** (short probes ≈ 0.3 Ω) before each value.
- [ ] Expected clean values: **R1 ~216 Ω**, RV1 ~50–394 Ω (done), DS1 cold a few Ω, motor windings low single digits.

## 1. AS-FOUND DOCUMENTATION — before touching anything
- [ ] **Overall underside photo**, oriented (mark FORWARD/tongue edge). Note orientation in every later photo.
- [ ] **Photograph each component in place** with its wires attached and undisturbed: rheostat, plunger, toggle, lamp socket, dropping resistor, terminal strip(s), grommet hole, neck-loom stubs.
- [ ] Note the **as-found state of the neck loom (CTL-009)**: which colored stubs (BLK/WHT/GRN) are present at the control-unit end, and what each currently lands on. (Recall: at the motor head, GREEN→brush, BLACK/WHITE→field reversing leads — so down here BLK/WHT/GRN must terminate on the rheostat/switch network.)
- [ ] Flag anything that looks **non-original / prior-rework**: modern wire nuts, replacement wire colors, re-soldered joints, added jumpers, drilled holes. Photograph + describe. (This unit is known to have been worked on before.)

## 2. NODE / TERMINAL REGISTRY — name everything, then tag it
Define and **physically tag** every terminal. Use these names (extend the numbering to match the actual lug count you find — count lugs and record it):

| Node | Component | Notes — confirm lug count at bench |
|---|---|---|
| **P1-H / P1-N** | (removed) AC line cord | Hot / Neutral — already cut; log where the stubs *used to* land if visible from solder marks. |
| **RH1-1 / RH1-2 / RH1-3** | Rheostat (CTL-001) | Toroidal pot. Expect 2 coil-end lugs + 1 wiper lug. **Identify the wiper** (see §5). Tag CW/CCW ends. |
| **S1-1 / S1-2 / (S1-3)** | Plunger switch (CTL-003) | Momentary. Count lugs — 2 = simple SPST; 3+ = SPDT/DPDT (reversing). Tag common (C) vs throws. |
| **S2-1 / S2-2 / (S2-3)** | Toggle switch (CTL-004) | Count lugs; tag common vs throws. |
| **LMP1-A / LMP1-B** | Pilot lamp socket (CTL-005) | A = center/tip contact, B = shell. |
| **R1-1 / R1-2 / (R1-T)** | Dropping resistor (CTL-007) | Ceramic. 2 ends; log any sliding tap band (R1-T) and its position. |
| **NL-BLK / NL-WHT / NL-GRN** | Neck loom (CTL-009) | The 3 motor leads at the control-unit end. GRN = LIVE branch, NOT ground. |
| **TS-#** | Terminal strip / junctions (CTL-010) | Number each lug/post of any fiber/Bakelite strip; number each free splice/twist-solder joint TSx as its own node. |
| **CHS** | Chassis (BAS-001 casting) | Reference for insulation tests + future safety-ground bond point (BAS-006 area / a stripped boss). |

- [ ] Tag count complete; **every lug in every photo carries a readable tag.**

### §2b — Contact-Point Dictation Worksheet (spoken labels) — PREFERRED METHOD
The operator's chosen method (2026-06-25): tag a contact point on **every** component, then dictate **per contact point** what lands there. This is double-entry (each wire named from both ends) and self-checking.

**Industry terminal labels** (RefDes-Terminal; tag physically + say these exact words). Locked 2026-06-25:

| Component | RefDes | Terminals (say these) | Notes |
|---|---|---|---|
| Line cord | **P1** | **P1-L** (hot/black), **P1-N** (neutral/white) | [+ P1-PE ground at rewire] |
| Rheostat (IRC) | **RV1** | **RV1-W** (wiper), **RV1-CCW** (track end) | which is wiper = meter |
| Plunger (reverse, momentary) | **S1** | **S1-COM**, **S1-NO**, **S1-NC** | count lugs; COM/NO/NC via truth table |
| Toggle (heater) | **S2** | **S2-COM** (line), **S2-NO** (load) | count lugs |
| Indicator lamp | **DS1** | **DS1-TIP** (center), **DS1-SHELL** | which wire = tip vs shell, verify |
| Heater resistor | **R1** | **R1-1 / R1-2** | non-polar end caps |
| Motor loom | **M1** | **M1-S1 / M1-S2** (field ends), **M1-A1** (green brush), **M1-A2** (internal field-tap brush) | S=series field, A=armature (NEMA) |
| Splices / posts | **TB1** | **TB1-1, TB1-2 …** | any terminal block / free splice |

**Dictation template (one per contact point, walk the whole machine):**
> "**[POINT]**: [N] wire(s) — a **[color]** [marking] to **[POINT]**; a **[color]** to **[POINT]**; … [or: one empty/unused lug]."

Rules: name **color + printed marking** for each wire; list **all** wires on a multi-wire point (catches junctions); call out **empty lugs**; saying each wire twice (both ends) is expected and good. Photograph each component **after tagging**, tags visible.

> **SUPERSEDED 2026-06-25 (same day):** the loose verbal map below was replaced by a **full contact-point trace** (operator tagged every component A/B + motor A/B/C/D and traced all 10 wires). The resolved 5-node netlist now lives in **`docs/dimensions/Control Unit Wiring Map - Sheet1.csv`** (OBSERVED conf.). Two meter items remain: **lamp voltage rating** (lamp traced PARALLEL w/ heater) and **plunger truth table**. Use the CSV as the working map; §3a kept only as the first-pass record.

## 3a. PRELIMINARY AS-DICTATED MAP (2026-06-25) — **ASSUMED, not yet metered**
First-pass connection map from the operator's verbal walk-through (`controlunit_wiring_dictation_raw.txt`) + photos. **Every row here is (ASSUMED)** until the DMM ring-out (§3/§4) confirms it. The operator flagged a **cross-connection at the resistor/lamp/plunger** he could not fully resolve by eye — treat that region as unverified.

**Confirmed functional roles (by operation):** PLUNGER **S1 = motor reverse** (out = forward, in = reverse); TOGGLE **S2 = heater switch**; GREEN motor lead → rheostat; rheostat **= IRC** brand (speed). Ceramic power resistor **R1 = the "heater unit"** — mounted in the heater well (BAS-002) on a copper strap; in series feeding the pilot lamp.

| # | From | To | Wire | Notes (ASSUMED) |
|---|---|---|---|---|
| a1 | NL-GRN (motor) | RH1 (rheostat) | green | exact lug TBD — likely wiper/speed out to motor |
| a2 | NL-BLK (motor) | S1 plunger | black | field reversing end |
| a3 | NL-WHT (motor) | S1 plunger | white | field reversing end (S1 swaps a2/a3 = reverse) |
| a4 | P1-H mains (hot) | R1 end-1 | black | mains hot into the heater resistor |
| a5 | P1-N mains (neutral) | RH1-a | white | mains neutral to rheostat terminal "a" |
| a6 | RH1-a (same lead as a5) | S2 toggle | black | branch off the neutral/rheostat node to heater switch |
| a7 | S2 toggle | R1 end-2 | black | switched leg into other end of heater resistor |
| a8 | R1 ("heater unit") | LMP1 lamp | black | resistor feeds the pilot lamp (series dropper) |
| a9 | LMP1 lamp | R1 (other side) | black | **CROSS** — operator-flagged, unresolved |
| a10 | (cross node) | S1 plunger | black | **CROSS** — operator-flagged, unresolved |

> ⚠️ The a8–a10 loop (resistor ↔ lamp ↔ plunger) is the part to ring out most carefully — verbal description was ambiguous. The DMM continuity matrix (§4) is what resolves it.

## 3. WIRE SEGMENT LIST — the directed connection map (core deliverable)
For **every physical wire/jumper**, dictate one row. This table IS the verified netlist.

**Dictation template (read aloud, one per wire):**
> "Segment S-__: from node ____ to node ____, color ____, gauge ____, insulation ____, length ____ inches, routing ____, joint type at each end (solder lug / screw / wire-nut / twist-solder) ____, confidence ____."

| Seg | From node | To node | Color | Gauge | Insul. | Length | Routing / notes | Conf. |
|---|---|---|---|---|---|---|---|---|
| S-01 | | | | | | | | |
| S-02 | | | | | | | | |
| (add rows as needed — expect ~8–14 segments) | | | | | | | | |

- [ ] Every node from §2 appears as an endpoint on **at least one** segment (orphan node = something missed — re-inspect).

## 4. CONTINUITY MATRIX — buzz every pair (catches hidden/internal links)
With DMM on continuity/ohms, **unplugged**, probe **every node against every other node** and record ~0 Ω (connected), a resistance value (connected through a component), or OL (open). This is what catches a jumper you couldn't see or a switch internally bridging two lugs.

- [ ] Fill the upper triangle of the N×N node matrix (only need each pair once). For switches/rheostat, record the reading **and the actuator position** it was taken in (see §5).
- [ ] **Insulation / isolation checks** (each should read **OL** with cord removed and switches open):
  - [ ] Every node ↔ **CHS** (chassis): expect **OL** everywhere (original design relies on isolation; any node reading short-to-chassis is a fault/hazard — flag it). (CONFIRMED/EST.)
  - [ ] NL-GRN ↔ CHS specifically: **must be OL** — proves GREEN is a live branch, **not** a chassis ground. Record the number.

## 5. COMPONENT CHARACTERIZATION — values + switch truth tables
**Rheostat (CTL-001) — RH1:**
- [ ] Identify the wiper: the lug-pair whose resistance **changes as you turn the knob** is wiper↔end; the pair that stays **fixed** is end↔end (= full coil).
- [ ] End-to-end (full coil) resistance: ______ Ω. **Target ~750 Ω (REF/NAWCC).** (CONFIRMED by meter ⇒ closes ledger **E4**.)
- [ ] Wiper sweep: full CCW ______ Ω → full CW ______ Ω; note knob direction vs ON/OFF arc; note if there's an end "click"/off detent that opens the circuit. (smooth? dead spots? open spots?)

**Dropping resistor (CTL-007) — R1:**
- [ ] End-to-end resistance: ______ Ω. **Target ~200–220 Ω, ~55 W (REF).** (CONFIRMED ⇒ closes **E4**.)
- [ ] If a tap band exists: R1-1↔R1-T ____ Ω, R1-T↔R1-2 ____ Ω, and the tap's physical position.

**Pilot lamp (CTL-005) — LMP1:**
- [ ] Cold filament resistance LMP1-A↔LMP1-B: ______ Ω (low, a few–tens of Ω = good filament; OL = burned out). Note bulb base type/markings if any.

**Plunger switch (CTL-003) — S1 truth table:** record which lug-pairs are **closed (~0 Ω)** vs **open (OL)** in each actuator state.
| State | Closed pairs | Open pairs |
|---|---|---|
| Released (rest) | | |
| Pressed (plunger in) | | |
- [ ] Determine pole/throw (SPST? SPDT? DPDT?) and whether it **swaps two lines** (= reversing) vs simply makes/breaks one (= on/off). This is the physical evidence for **E5 (plunger = reverse?)**.

**Toggle switch (CTL-004) — S2 truth table:**
| State | Closed pairs | Open pairs |
|---|---|---|
| Up / pos 1 | | |
| Down / pos 2 | | |
- [ ] Pole/throw + what it makes/breaks → evidence for **E5 (toggle = heater?)**.

## 6. NECK-LOOM (CTL-009) MAPPING — tie the two units together
- [ ] **NL-BLK** lands on node ______ (CONFIRMED). 
- [ ] **NL-WHT** lands on node ______ (CONFIRMED).
- [ ] **NL-GRN** lands on node ______ (CONFIRMED) — and **NL-GRN↔CHS = OL** re-verified.
- [ ] Cross-check against the **motor-head** map (R-11): GREEN→brush (common), BLACK/WHITE→field outer reversing ends. The control-unit terminations must be consistent with reversing via Black↔White swap (proven on the Rigol, R-10). Note any inconsistency.

## 7. BUILD THE VERIFIED SCHEMATIC — reconcile & resolve the `?` flags
- [ ] From §3 + §4, write the **verified node list / netlist** (each node → everything electrically common to it).
- [ ] Trace and confirm (or correct) the inferred **series path**: `M1(neck) → S1 → LMP1 → R1 → S2 → RH1`. Mark each hop CONFIRMED or CORRECTED with the actual segment evidence.
- [ ] Resolve the two old `?` junctions from LR-ELEC-001: **(a)** the rheostat terminal usage (which lug is line, which is wiper-out to motor); **(b)** the "Hot-ties-to-Green-rail" question. Replace `?` with metered fact.
- [ ] Reconcile against **factory diagram E-1690** (anchor): note where S/N 13505 **matches** the factory intent and where the **prior rework deviates**. Both get documented (factory intent vs as-found-this-unit).

## 8. OUTPUTS THIS FEEDS
- [ ] **`docs/dimensions/Control Unit Wiring Map - Sheet1.csv`** — the §3 segment table + §2 node registry, machine-readable. (Create from this checklist's data.)
- [ ] **Verified as-found schematic** — new SVG (supersedes the inferred LR-ELEC-001 `?` flags); CTL- part IDs on every symbol.
- [ ] **Corrected 3-wire grounded rewire target schematic** — the R-5 design: same logic, + chassis-ground bond (CHS), clip/quick-connect terminals, new 16 AWG silicone harness, modern dropping-resistor/PTC option.
- [ ] Component values (rheostat, dropping resistor, lamp) → close ledger **E4**; switch roles → close **E5**.
- [ ] Manual Part III (Restoration) electrical section + the post-rewire **cold-check continuity matrix** (already drafted in CLAUDE.md) for first power-on.

## Open questions to settle at the bench
- [ ] Lug count on RH1 / S1 / S2 (drives pole-throw interpretation).
- [ ] Is there a **terminal strip** (fiber/Bakelite) or are joints free twist-solder? (Defines how many CTL-010 nodes.)
- [ ] Does the dropping resistor mount on the **copper band/strap** (per NAWCC) — relevant to the PTC-heater replacement option?
- [ ] Any **second gasket/insulator** behind the lamp jewel or under the rheostat that should get a CTL/BAS ID?

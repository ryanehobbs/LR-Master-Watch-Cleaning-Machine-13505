# Motor Teardown Log — L&R Master Watch Cleaning Machine, S/N 13505

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from hands-on restoration of specimen S/N 13505. Curated by Hobbs R.E., 2026. For restoration reference only.

**What this is:** the as-performed disassembly sequence, reconstructed by the restorer. It is the source for the Part III *Restoration* reassembly procedures (read in reverse for reassembly). See [`manual-outline.md`](manual-outline.md).

**Source:** voice-memo dictation 2026-06-17, transcribed locally (faster-whisper). Raw transcript: [`teardown_dictation_raw.txt`](teardown_dictation_raw.txt).

**⚠️ Terminology reconciliation (important):** in the dictation the restorer said **"stator" / "stator shaft"** for what the project canonically calls the **ARMATURE / rotor** (the rotating shaft, ARM-001 / SHF-003), and said **"field coil"** for what the project calls the **STATOR** (the stationary field assembly, STR-001). This log uses the **canonical** Part IDs (ARMATURE = rotor, STATOR = field coil).

**Provenance tags:** **(DICTATION)** from the voice memo (recall-grade) · **(PHOTO)** corroborated by a bench photo · **(VERIFY)** needs a check before publishing.

**Step schema:** Action · Part IDs · Tools · Technique/trick · Cautions · Provenance.

---

### Step 1 — Remove the basket + drive spindle from the armature shaft
- **Action:** Back out the spindle set screw and pull the basket/spindle "outer column" off the armature's lower journal as a unit.
- **Part IDs:** Set screw **SPN-005** (1/4-20, slotted) retains the basket drive spindle **SPN-002** on the armature lower journal **SHF-003**; basket **BSK-002** rides on SPN-002. (SPN-005 = the screw that couples spindle→shaft so the motor drives the basket.)
- **Tools:** flat-head/slotted screwdriver; small rubber mallet.
- **Technique:** back the set screw out; the assembly was stuck (long-seated), so freed it with **very light, subtle rubber-mallet taps** — not hard at all. Removed the assembly, set aside.
- **Caution:** tap *gently*; excess force risks the shaft/spindle.
- **Provenance:** (DICTATION)

### Step 2 — Identify the platform deck (context; removed with the housing bolts)
- **Action:** Note the deck stack before pulling the housing bolts.
- **Part IDs:** Platform disk **PLT-001** carries the tapered rubber jar seal **PLT-002** (wedges into the jar to stop solution splashing); gasket is fastened to the disk by **PLT-005** rivets. Two long housing bolts **FLG-002** pass up through the deck (via **PLT-004** standoff tubes), on either side, and clamp the two motor-housing halves together.
- **Provenance:** (DICTATION)

### Step 3 — Remove the two long housing bolts; separate the housings
- **Action:** Unscrew the two long bolts; the lower housing drops away from the upper, and the armature comes down with the lower housing (seated in the lower bearing).
- **Part IDs:** **FLG-002** ×2 (housing tie-bolts). Lower housing **LH-001** + armature **ARM-001** drop as a unit; they stay together via the lower bearing **BRG-002**.
- **Tools:** screwdriver to fit FLG-002.
- **Caution:** support the dropping assembly so the armature/commutator isn't damaged.
- **Provenance:** (DICTATION) — *dictation called the rotor "the stator"; it is the ARMATURE.*

### Step 4 — Remove the stepped brass thrust ring (ARM-010) to free the armature
- **Action:** Drive the stepped brass ring down and off the lower journal with a bearing puller so the armature can come out.
- **Part IDs:** **ARM-010** stepped brass ring on lower journal **SHF-003**; freeing it releases armature **ARM-001**. *(REF: WatchRepairTalk forum identifies this grooved disk as a **"slinger"** — keeps cleaning-jar fluid from wicking up the shaft into the motor; consistent with its lower/basket-end location. Independent posts describe the same removal sequence we used.)*
- **Tools:** elevated vise; rubber mallet; **bearing/gear puller**.
- **Technique:** the ring sits very close to the bottom of the lower housing — **do not pry** (it would bend the brass ring). Instead: clamp the housing+shaft in an **elevated vise** so there's clearance beneath the shaft; **tap the very top of the shaft with the rubber mallet (a bit more force)** to walk the ring slightly down the shaft; once there's room, fit a **bearing puller** (center on the shaft end, the two teeth gripping the ring) and **gently back the ring all the way off.** With the ring off, the whole armature lifts out; set aside.
- **Caution:** never pry the ring directly (bends it); use the puller for even pressure.
- **Provenance:** (DICTATION) — supersedes the earlier rough "tap the rubber shaft end" note; the real method was tap-from-top + bearing puller.

### Step 5 — Disconnect the electrical (snip the field-coil leads)
- **Action:** Cut the wires feeding the field coil where the neck loom enters the motor.
- **Part IDs:** 3-wire cord/loom (BLK/WHT/GRN) from the main control unit into the motor; leads land on the **STATOR** field coil (STR-001).
- **Tools:** flush cutters / snips.
- **Caution:** ⚠️ the **GREEN neck wire is NOT a ground — it is a live current-carrying branch** (see Electrical section). Treat all three as hot during any future work. On reassembly these are replaced per the rewire plan (silicone wire, 3-wire grounded), not re-spliced.
- **Provenance:** (DICTATION)

### Step 6 — Remove the field coil (stator)
- **Action:** Remove the two stator mount bolts and lift the field coil out of the upper housing.
- **Part IDs:** **STR-008** stator mount screws ×2 → frees the stator **STR-001**. (Note: the yoke also had the 2× FLG-002 pass-throughs, already out from Step 3.)
- **Tools:** screwdriver/driver to fit STR-008.
- **Result:** both housings now bare except the two bearings.
- **Provenance:** (DICTATION)

### Step 7 — Remove the sleeve bearings + springs from both housings
- **Action:** Tap each spherical bearing and its conical spring out of its housing pocket.
- **Part IDs:** **BRG-001** (upper) / **BRG-002** (lower) spherical sleeve bearings; **BRG-012** conical springs (one per housing).
- **Tools:** rubber or wood block; mallet.
- **Technique:** with the housing **face-down (outside toward you)**, used a rubber/wood block and **light tapping to drive the bearing out of the spring**, then removed the spring from the housing. Same approach on both lower and upper housings — it worked.
- **RECOMMENDED method (best-judgment, ⚠️ NOT factory-verified):** **release the conical spring (BRG-012) first** with a pick/hook — the spring is what captures the ball in the socket, so with it removed the bearing should free with almost no force. This is the most likely *intended* service method because the bearing is **spring-retained, not press-fit**. ⚠️ **No original L&R shop manual exists for this machine** — this recommendation is reverse-engineered from how the parts go together, not a documented factory procedure. Treat as best practice, not gospel; confirm gently and stop if it resists.
- **As-performed on this specimen (what actually happened):** with the housing **face-down**, used a rubber/wood block + **light mallet tapping to drive the bearing out of the spring**, then removed the spring. It worked on both housings, but is cruder than the spring-first method above.
- **Other candidate methods (UNTESTED here — alternatives if the spring-first release won't free it):**
  1. **Warm the aluminum housing** (~80-120 °C: heat gun / low oven / boiling water) — aluminum expands faster than the bearing, loosening the fit; tap/push out easily while warm. Do before refinishing or mask the wrinkle paint.
  2. **Press, don't hammer** — arbor press / vise with a drift or socket seated squarely on the ball/collar, housing on an open-bore fixture so it exits straight (even pressure vs impact).
  3. **Soft drift / blind-hole puller** — brass or Delrin drift from the opposite side, or an internal collet + slide-hammer puller. Keep all force axial; never pry against the spherical socket.
- **Provenance:** (DICTATION) as-performed; RECOMMENDED + candidate methods = engineering best-judgment, **untested here and not from any factory manual** (none exists for this machine).
- **REF — community-corroborated methods (WatchRepairTalk, multiple posters):** use an **internal-jaw / blind-hole bearing puller** sized to the bearing bore (e.g. Harbor Freight #95987), or a **DIY puller** — a hex bolt trimmed to pass the casing hole and engage the bearing race, with a pipe spacer + washer + nut on the far side to draw it out axially. **Soak with penetrating oil** (overnight) to dissolve the hard brown dried-cleaning-fluid residue first; **gently heat the aluminum housing** (heat gun) since it expands faster than the steel shaft; **never strike the cast-aluminum housing with a steel hammer** (cracks it) — rubber/rawhide/leather mallet only. (Keep penetrating oil OFF any rubber.)

---

## End state
Motor housing **completely disassembled** — both housings bare, all internals out — ready for cleaning/refinishing and eventual reassembly (see the Reassembly Sequence in CLAUDE.md, which is this log in reverse).

## Open items to reconcile
- [x] **Terminology confirmed** (user 2026-06-17): dictation "field coil" = STR-001 stator; "stator/stator shaft" = armature/rotor. Log is in canonical IDs.
- [x] **Step 1 confirmed:** SPN-005 set screw couples spindle SPN-002 to armature shaft SHF-003 — basket + spindle come off together.
- [x] **Step 4 confirmed:** the brass ring pulled (elevated vise + tap-from-top + bearing puller) is ARM-010, the stepped thrust washer.
- [ ] Confirm the **proper bearing-removal method** (Step 7) vs the tap-out approach used (still flagged VERIFY).

---

# PART II — CONTROL UNIT / MAIN UNIT TEARDOWN
*Started 2026-06-24 (voice dictation → `teardown_controlunit_dictation_raw.txt`). Motor head is complete; this is the base/body + post + controls. Provisional Part IDs: **BAS-** base/body · **NCK-** neck/post/carrier · **CTL-** controls/electrical (confirm names).*

### CU-Step 1 — Extract the neck (motor-head) cable
- Flipped the unit **upside down.** **Snipped the wires** that run up to the motor head, **leaving the component-side connections intact** (so the internal wiring can be mapped later). Pulled the old neck cable out through the **square metal post (the conduit)**. → old neck cable **discarded.**

### CU-Step 2 — Remove the motor-mount carrier from the post top
- The **Post / Mast (NCK-001)** is a **square chrome bar with a ROUNDED TOP.** The **motor-mount carrier (NCK-002)** clamps the motor housing and rides on the post, held by a **tighten/loosen clamp screw (NCK-003).** Loosened the screw and **removed the carrier.**
- **⭐ Mechanism (how it works — confirmed by restorer):** on the **rounded top**, the carrier can **swivel/rotate** to index the motor over **each jar bay and the heater station.** To **hold the motor raised**, you **tighten the clamp at an angle** so part of the carrier base **rests/catches on a SQUARE CORNER of the mast** (the square shaft below the round top acts as the height detent/rest). So: round top = free swivel; square corners = positional rest + raised hold.
- **Naming correction:** there is **NO lift handle** (dropped the earlier "NCK-003 handle"); the black loop at the top is the **power-cable loop**, not a grip. NCK-003 is now the **carrier clamp/lock screw.**

### CU-Step 3 — Free the post from the base
- At the **base of the post: 4 fasteners** — **3 long screws** through the casting into the post, + **1 set screw with a metal spacer tab** pressing against the post (**tension/locating**). Removed all four.
- The post **would not pull out** — heavily **embedded by corrosion.** Applied **Kroil penetrating oil**, let it soak; hand-pulling still failed; **tapped it out from the bottom.**
- ⚠️ **Finding:** heavy **internal corrosion**; the unit **appears to have been worked on / restored once before** — the corrosion was the cause of the post binding (it should slide out easily).

### CU-Step 4 — Remove the main AC power cord
- **Snipped** the wall cord the same way (**kept the internal component connections** for mapping); old cord **discarded.**
- The **rubber grommet** the AC line passes through had **gone hard/brittle and disintegrated** → **needs replacement** (new part — provisional **BAS-grommet / CTL- AC-inlet grommet**).

### CU-Step 5 — Remove the electrical components (as a wired cluster)
*Approach (operator choice): free each component from its **mechanical mount only**, leaving all solder joints intact, and lift the harness out as **one wired cluster** — verify the knot + plunger truth table on the bench, then desolder/clean. Frees the casting for refinishing in parallel.* (DICTATION 2026-06-25, `controlunit_disassembly_dictation_raw.txt`)
- **Plunger (S1):** the **button is press-fit** — tug it straight up to pop it off, then remove the switch body.
- **Heater resistor (R1):** held centered in the heater well by a **spring wire band**; a **slotted screw (badly rusted)** releases the band's tension. Backed the screw out, worked the resistor free. R1 had a **paper film sleeve** wrapping it (looks **adhesive-backed**, now loose) — set aside (reproduce/refit on reassembly).
- **Pilot lamp (DS1):** mounted on a **metal bracket bolted to the housing**; pulled the bulb, then loosened the bracket bolt (too tight for a crescent wrench → small pliers). **Removing RV1 first opened up access to the bulb.**
- **Jewel (CTL-006):** the **red lens housing** that makes the bulb read red on the panel — removed.
- **Rheostat (RV1):** removed (done before the bulb, which eased access).
- **State:** all four CTL components (RV1, S1, DS1, R1) + jewel now **off the casting but still wired together** as the cluster, per plan. Casting now free for strip/Bondo/paint.
- **⚠️ UNKNOWN PIECE:** a part came loose that the operator couldn't place — **not part of any CTL component**; "looks like it might have gone toward the **post**." Set aside for ID. **TODO: photograph it** → likely a **NCK-** (post/carrier) detail (spacer/tension tab from the post base? cf. CU-Step 3's set-screw + spacer tab) — confirm before it's lost.

### CU — current state & next
- **Post removed; all electrical components removed (wired cluster); casting bare and ready for refinishing.**
- **NEXT (bench, on the cluster):** resolve the **R1/DS1/S2/S1 knot** mislabel (separate tagged wires off each blob), **plunger truth table** in-hand, **RV1 wiper-lug ID**, then **desolder + clean** each joint and re-meter values clean. Then **verified schematic** → R-5 grounded rewire. Also: **chassis-isolation** check was the one in-situ reading (do/recall if captured pre-lift).
- **Capture as parts are cleaned:** dims + photos per component for the CTL- dimension sheet; bag/label mounting hardware (R1 spring band + slotted screw, lamp bracket + bolt, switch nuts, jewel) — reused/refinished.
- **New parts to source:** AC-line **grommet** (rubber, disintegrated); 3-wire grounded cord + silicone internal wire (R-5); possibly a new R1 band screw (rusted).
- **Provenance:** (DICTATION) 2026-06-24 / 2026-06-25.
- [ ] Upgrade (DICTATION) steps to (PHOTO) where bench shots corroborate them.

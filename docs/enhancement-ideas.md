# Enhancement Ideas — Optional Modernizations (NON-ORIGINAL)

> **Parking lot, orthogonal to the main restoration.** These are *optional* electrical enhancements discussed as hypotheticals — **not** part of the faithful as-found restoration. None are committed. Guiding rule: **anything done here must keep the as-found design intact/restorable** (the verified `LR-ELEC-002` schematic is the reference), and everything must fold into the grounded, fused **R-5 rewire** — never the original 2-wire ungrounded scheme. Document any that get built as *enhancements*, clearly labeled non-original, in the shop manual.

Status legend: 💡 idea only · 🔬 evaluating · ✅ adopted into R-5 · ❌ declined

---

## 1. 💡 Automatic forward/reverse module
**Goal:** machine cycles motor forward ↔ reverse on its own, no operator input (manual plunger reversing still available).

**Why it's easy here:** reversing = which field lead is hot (white/a = forward, black/c = reverse), sharing one hot common. Anything that alternates hot between those two leads on a timer = auto-reverse. Rheostat (speed/OFF) and the armature/green return are untouched.

**Core:** one **SPDT relay** replicates the plunger (COM = hot, throws = white / black) + a **repeat-cycle timer** driving the coil.
- Timer options: (a) off-the-shelf adjustable **repeat-cycle timer relay** (cheapest); (b) **microcontroller (Arduino/ESP) + relay board** (most flexible); (c) **vintage cam/drum timer** (synchronous motor + cam — period-correct, more work).

**Engineering cautions (make it last):**
- **Coast pause between directions** — do NOT slam a spinning universal motor into reverse (big current spike + brush arcing). Sequence: forward → OFF (coast) → reverse → OFF → repeat.
- **Size relay contacts for INRUSH** (several× running), not just running current (<1 A bench). Suggest 8–10 A / 250 V contacts.
- **Snubber** across the contacts (RC) or an MOV — tames the inductive motor arc, big contact-life win.
- Mains-powered → on the grounded/fused R-5 system, enclosed.
- Optional: keep the manual plunger as a **manual/auto selector** or override.

---

## 2. 💡 Master power switch (fixes "always live when plugged in")
**Problem (documented):** no master switch — the hot rail (N2) is energized the moment the cord is plugged in; only the rheostat (motor) and toggle (heater) gate their branches.

**Fix:** a switch in the **HOT (line) conductor at the inlet, upstream of N2.** Open = whole machine dead.
- **Switch the HOT** specifically (not neutral). SPST in the hot leg = standard. **DPST** (hot + neutral) = full isolation, "belt and suspenders."
- Rheostat + heater toggle remain as downstream sub-controls (Master ON → then run motor / heater).
- **Sizing:** carries the TOTAL machine current — size for the sum with margin (~6–10 A / 250 V; measure total draw first).

**Recommended single-part solution:** a **switched + fused IEC inlet module** (C14 power-entry w/ integral rocker switch + fuse holder) — gives the **grounded inlet + master switch + fuse** in one, pairs perfectly with the R-5 grounded cord. Vintage-look alternative: a bat-handle toggle (matches the Arrow H&H aesthetic) + separate inline fuse.

**Nice touch:** a **power-ON indicator** (the existing red jewel DS1 is the HEATER indicator, not a mains-on light) — an illuminated master switch or a small neon shows the machine is live.

---

## 3. 💡 Fusing — would a 3 A fuse work?
**Estimated steady-state total ≈ 1.6 A:** heater R1 0.55 A + lamp DS1 0.05 A + motor **≤ ~1 A** (inferred: the original plunger that carries the motor is rated **1 A**/125 V, so motor running ≤ ~1 A; the 3 A/250 V toggle on the ~0.6 A heater branch agrees).

**→ A 3 A fuse is reasonable** (~1.9× headroom on steady-state; 360 W capacity vs ~190 W load). **BUT:**
- **Use a SLOW-BLOW (time-delay / "T") fuse**, NOT fast-blow — the universal motor's startup **inrush** (several× running, brief) will nuisance-trip a fast 3 A. Slow-blow rides through inrush and still protects against real overload/short.
- **Measure first** (Kill-A-Watt): if steady-state ~1.5–2 A → **3 A slow-blow**; if it runs hotter (>~2.4 A) → step to **4–5 A slow-blow** (still well under 16 AWG ampacity ~10 A+).
- The fuse protects **the machine/its wiring** from a fault; the **house breaker** protects the building wiring (complementary). A fuse close to the load protects far better than the 15–20 A house breaker alone.

---

## Synergy note
Ideas 2 + 3 + the R-5 grounded rewire combine cleanly into **one switched-fused grounded IEC inlet** (ground + master switch + slow-blow fuse + new cord). Idea 1 (auto-reverse) is independent and bolts onto the white/black field leads downstream. If any are adopted, capture them as labeled non-original enhancements and update R-5 + the manual.

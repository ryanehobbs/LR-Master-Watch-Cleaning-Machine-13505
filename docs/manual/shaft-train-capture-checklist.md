# Shaft Train Capture Checklist — top to bottom
### L&R Master Watch Cleaning Machine, S/N 13505

> **REPRODUCTION DOCUMENT** — Not an original L&R Mfg. Co. technical publication. Reverse-engineered from hands-on restoration of specimen S/N 13505. Curated by Hobbs R.E., 2026. For restoration reference only.

**Goal:** make the *entire rotating assembly* a complete, dimensioned BOM — not just the motor. Walk the shaft **top (basket) → bottom (lower journal)** and capture every part that mounts on or is driven by it. Prompted by the ARM-010 discovery: if one internal washer was missed, shaft-mounted parts are likely uncatalogued.

**Provenance tags** (same system as the dimension dataset): **(CONFIRMED)** caliper/tape · **(EST.)** from photo · **(SYN)** derived · **(PROVISIONAL)** existence assumed, not yet verified.

**Per-part capture fields:** Part ID · canonical name · exists? (Y/N) · mounts to / driven by · key dims (OD, height/length, bore ID, thread, mesh size) · how retained (nut/pin/press/slip) · provenance · photo ref.

---

## A. Spindle / Drive train (SPN-) — links shaft to basket
- [ ] **SPN-002 Center Column** — confirmed exists. Capture: OD, length, bore, how it couples to the upper journal (SHF-002, Ø0.250").
- [ ] **SPN-003 Top Impeller Bracket** — confirmed exists. Capture: what it does (basket seat? spinner? air impeller?), dims, how it mounts.
- [ ] **SPN-004 Basket-to-Shaft Coupling** — does the basket thread on, drop on a pin, or seat on a fanwheel/fork? Identify and measure. (Comparable L&R machines use a fanwheel + fork.)
- [ ] Any **collar / scribe ring / spinner** on the spindle (watch for another ARM-010-style washer here).

## A2. Platform / deck + jar seal (PLT-)
- [ ] **PLT-001 Platform Disk** — newly found (was missing). Capture: OD, thickness, center bore (shaft pass-through), the 2 bolt-hole positions, and **the exact FLG-002 stack order** (bolt head → platform → lower housing → upper-housing boss?).
- [ ] **PLT-002 Platform Gasket** — confirm whether this is the **same molded rubber seal already conditioned** (U.S. PATENT 1872812) or a second gasket; measure.
- [ ] Confirm the platform is **stationary** (shaft rotates through it) vs rotating.

## B. Basket family (BSK-)
- [ ] **BSK-002 Mesh Basket** — confirmed exists. Capture: OD, overall height, mesh size, how it seats.
- [ ] **BSK-003 Basket Cover / Tray** — confirm + measure (depressed-side tray?).
- [ ] **BSK-004 Divider Partition Basket** — confirm whether this machine has one; measure if present.
- [ ] **BSK-005 Clock Basket** (large) — confirm/measure if supplied.
- [ ] **BSK-006 Multiple Insert Set** — confirm/measure if supplied.
- [ ] **BSK-007 Small Parts Unit** — confirm/measure if supplied.
- [ ] Note which accessories actually came with S/N 13505 vs generic catalog items (for the manual's "what's in the box").

## C. Reconcile against the motor (already done)
- [ ] Confirm the spindle train's bottom interface = the motor's upper journal (SHF-002), and that nothing between basket and motor is missing.
- [ ] Close out **ARM-010** (lower journal thrust washer) thickness + function while at the bench.

---

## Outputs this feeds
- `Shaft Train Parts Dictionary.csv` — upgrade PROVISIONAL rows to confirmed as captured.
- A `Shaft Train Dimensions - Sheet1.csv` (create once measurements exist), mirroring the motor dimension sheets.
- Drawing pipeline: new SPN-/BSK- component sheets, then fold into a **full-machine** exploded view (currently EXP-001/002 are motor-only).
- Manual Part I (Operating) basket/loading section + Part III (Restoration) basket cleaning writeup.

## Open question for the bench
- Is there a separate **fanwheel/impeller** on the spindle (distinct from the motor's cooling fan ARM-007), as on the Vari-Matic? Resolve so we don't double-count or miss it.

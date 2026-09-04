# L&R Master S/N 13505 - FreeCAD pilot: PLT-006 washer + PLT-004 standoff tube
# Confirmed dims are in INCHES; modeled in mm (CAD standard). 1 in = 25.4 mm.
import os, FreeCAD as App, Part

MM = 25.4
def inch(v): return v * MM

OUT = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad\pilot"
os.makedirs(OUT, exist_ok=True)

doc = App.newDocument("PLT_pilot")

# --- PLT-006 Gasket Deck Washer (ORIGINAL): OD 0.4385, ID 0.1570, thick 0.0415 ---
w_od, w_id, w_th = inch(0.4385), inch(0.1570), inch(0.0415)
washer = Part.makeCylinder(w_od/2.0, w_th).cut(Part.makeCylinder(w_id/2.0, w_th))
o1 = doc.addObject("Part::Feature", "PLT_006_Gasket_Deck_Washer")
o1.Shape = washer

# --- PLT-004 Mount Standoff Tube: OD 0.3765, bore 0.2020, length 0.6990 ---
t_od, t_bore, t_len = inch(0.3765), inch(0.2020), inch(0.6990)
tube = Part.makeCylinder(t_od/2.0, t_len).cut(Part.makeCylinder(t_bore/2.0, t_len))
tube.translate(App.Vector(20, 0, 0))  # offset so they don't overlap
o2 = doc.addObject("Part::Feature", "PLT_004_Mount_Standoff_Tube")
o2.Shape = tube

doc.recompute()
fcstd = os.path.join(OUT, "PLT_pilot.FCStd")
doc.saveAs(fcstd)

# STEP exports (open-format, reusable)
Part.export([o1], os.path.join(OUT, "PLT-006_Gasket_Deck_Washer.step"))
Part.export([o2], os.path.join(OUT, "PLT-004_Mount_Standoff_Tube.step"))

# verify against expected
for o in (o1, o2):
    bb = o.Shape.BoundBox
    print("%-28s bbox(in): %.4f x %.4f x %.4f  solid=%s  vol_mm3=%.2f" % (
        o.Name, bb.XLength/MM, bb.YLength/MM, bb.ZLength/MM,
        o.Shape.isValid() and o.Shape.Solids and "yes" or "no", o.Shape.Volume))
print("SAVED:", fcstd)
print("STEP files in:", OUT)

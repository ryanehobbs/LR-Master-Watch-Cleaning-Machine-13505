# L&R Master S/N 13505 - FreeCAD Batch 3: motor housings (APPROX cast solids)
# Confirmed dims in INCHES -> mm. Modeled as turned bodies (cyl + cone); cast detail omitted.
import os, FreeCAD as App, Part

MM = 25.4
def IN(v): return v * MM
def cyl(r, h, z=0.0): return Part.makeCylinder(r, h, App.Vector(0, 0, z))
def cone(r1, r2, h, z=0.0): return Part.makeCone(r1, r2, h, App.Vector(0, 0, z))

OUT = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad\batch3"
os.makedirs(OUT, exist_ok=True)
parts = []

# ===== UH-001 Upper Housing: OD 3.200, height 2.650, cavity depth 1.850, wall ~0.100,
#       top shaft hole 0.460. Dome approximated as a cone taper above a cylinder body. =====
uh_R = IN(3.200)/2
body_h = IN(2.000)
dome_h = IN(2.650) - body_h
outer = cyl(uh_R, body_h).fuse(cone(uh_R, IN(0.30), dome_h, body_h))
cavity = cyl(IN(3.000)/2, IN(1.850))                 # wall = (3.200-3.000)/2 = 0.100
shaft_top = cyl(IN(0.460)/2, IN(2.650))              # top shaft clearance UH-008
uh = outer.cut(cavity).cut(shaft_top)
parts.append(("UH_001_Upper_Housing_APPROX", uh))

# ===== LH-001 Lower Housing: OD 3.000, height 1.700, cavity depth 1.000, wall ~0.100,
#       bottom shaft hole 0.500. Bowl: cone foot (bottom) widening to a cylinder body (top). =====
lh_R = IN(3.000)/2
foot_h = IN(0.700)
body_h2 = IN(1.700) - foot_h
outer2 = cone(IN(0.40), lh_R, foot_h).fuse(cyl(lh_R, body_h2, foot_h))
cavity2 = cyl(IN(2.800)/2, IN(1.000), IN(1.700) - IN(1.000))  # opens at top, wall ~0.100
shaft_bot = cyl(IN(0.500)/2, IN(1.700))              # bottom shaft clearance LH-004
lh = outer2.cut(cavity2).cut(shaft_bot)
parts.append(("LH_001_Lower_Housing_APPROX", lh))

# ===== build doc, lay out, export =====
doc = App.newDocument("Batch3_Housings")
xc = 0.0
for name, shp in parts:
    bb = shp.BoundBox
    shp = shp.copy(); shp.translate(App.Vector(xc - bb.Center.x, 0, 0))
    o = doc.addObject("Part::Feature", name); o.Shape = shp
    try: o.Visibility = True
    except Exception: pass
    Part.export([o], os.path.join(OUT, name + ".step"))
    xc += bb.XLength + 15.0
doc.recompute()
fcstd = os.path.join(OUT, "Batch3_Housings.FCStd")
doc.saveAs(fcstd)
print("PARTS:", len(parts))
for o in doc.Objects:
    bb = o.Shape.BoundBox
    print("  %-32s in: %.3f x %.3f x %.3f  solid=%s" % (o.Name, bb.XLength/MM, bb.YLength/MM, bb.ZLength/MM,
        ("yes" if (o.Shape.isValid() and o.Shape.Solids) else "NO")))
print("SAVED:", fcstd)

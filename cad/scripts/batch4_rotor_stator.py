# L&R Master S/N 13505 - FreeCAD Batch 4: ARM-001 rotor + STR-001 stator (APPROX)
import os, math, FreeCAD as App, Part
MM = 25.4
def IN(v): return v * MM
def cyl(r, h, z): return Part.makeCylinder(r, h, App.Vector(0, 0, z))
def cone(r1, r2, h, z): return Part.makeCone(r1, r2, h, App.Vector(0, 0, z))

OUT = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad\batch4"
os.makedirs(OUT, exist_ok=True)
parts = []

# ===== ARM-001 Armature (rotor) - stacked silhouette, bottom (lower journal) -> top =====
# (segment, dia1, dia2, length)  cone if dia1!=dia2
segs = [
    ("SHF-003 lower journal", 0.280, 0.280, 1.875),
    ("ARM-009 collar",        0.560, 0.560, 0.100),
    ("ARM-007 fan",           1.300, 1.300, 0.325),
    ("ARM-005 winding cone",  0.300, 1.300, 0.385),
    ("ARM-002 core",          1.505, 1.505, 0.775),
    ("ARM-004 winding cone",  1.300, 0.970, 0.480),
    ("ARM-006 commutator",    0.970, 0.970, 0.405),
    ("ARM-008 collar",        0.970, 0.970, 0.130),
    ("SHF-002 upper journal", 0.250, 0.250, 0.845),
]
rotor = None; z = 0.0
for nm, d1, d2, L in segs:
    seg = cyl(IN(d1)/2, IN(L), z) if d1 == d2 else cone(IN(d1)/2, IN(d2)/2, IN(L), z)
    rotor = seg if rotor is None else rotor.fuse(seg)
    z += IN(L)
parts.append(("ARM_001_Armature_Rotor_APPROX", rotor))   # OAL should = 5.320"

# ===== STR-001 Stator (unified pole core) - APPROX ring seating in upper housing =====
# outer R 1.500 (seats housing bore 3.000), bore ~1.546 (pole-shoe inner face), height 0.736,
# 4 mounting holes (0.20) on 2.300 BCD
stator = cyl(IN(3.000)/2, IN(0.736), 0).cut(cyl(IN(0.773), IN(0.736), 0))
r = IN(2.300)/2
for i in range(4):
    a = math.radians(45 + 90*i)
    stator = stator.cut(cyl(IN(0.20)/2, IN(0.736)*3, -IN(0.736)).translated(App.Vector(r*math.cos(a), r*math.sin(a), 0)) if hasattr(Part.Shape,'translated') else Part.makeCylinder(IN(0.20)/2, IN(0.736)*3, App.Vector(r*math.cos(a), r*math.sin(a), -IN(0.736))))
parts.append(("STR_001_Stator_Ring_APPROX", stator))

doc = App.newDocument("Batch4_Rotor_Stator")
xc = 0.0
for name, shp in parts:
    bb = shp.BoundBox
    shp = shp.copy(); shp.translate(App.Vector(xc - bb.Center.x, 0, 0))
    o = doc.addObject("Part::Feature", name); o.Shape = shp
    try: o.Visibility = True
    except Exception: pass
    Part.export([o], os.path.join(OUT, name + ".step"))
    xc += bb.XLength + 18.0
doc.recompute()
fcstd = os.path.join(OUT, "Batch4_Rotor_Stator.FCStd")
doc.saveAs(fcstd)
print("PARTS:", len(parts))
for o in doc.Objects:
    bb = o.Shape.BoundBox
    print("  %-34s in: %.3f x %.3f x %.3f  solid=%s" % (o.Name, bb.XLength/MM, bb.YLength/MM, bb.ZLength/MM,
        ("yes" if (o.Shape.isValid() and o.Shape.Solids) else "NO")))
print("SAVED:", fcstd)

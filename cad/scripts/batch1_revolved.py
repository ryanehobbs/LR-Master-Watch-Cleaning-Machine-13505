# L&R Master S/N 13505 - FreeCAD Batch 1: simple revolved/prismatic parts
# Confirmed dims in INCHES, modeled in mm (1 in = 25.4 mm). Parts laid in a row along +X.
import os, math, FreeCAD as App, Part

MM = 25.4
def IN(v): return v * MM

OUT = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad\batch1"
os.makedirs(OUT, exist_ok=True)

def cyl(r, h, z=0.0):
    return Part.makeCylinder(r, h, App.Vector(0, 0, z))

def disc(od, thick, holes):
    """flat disc with through-holes: holes = list of (dia, x, y)"""
    s = cyl(od/2.0, thick)
    for d, x, y in holes:
        s = s.cut(Part.makeCylinder(d/2.0, thick*3, App.Vector(x, y, -thick)))
    return s

def bolt_holes(dia, bcd, n=6):
    r = bcd/2.0
    return [(dia, r*math.cos(math.radians(60*i)), r*math.sin(math.radians(60*i))) for i in range(n)]

parts = []  # (name, shape)

# ARM-008 Brass Shaft Collar Upper: OD 0.970, len 0.130, bore 0.250
parts.append(("ARM_008_Brass_Collar_Upper", cyl(IN(0.970)/2, IN(0.130)).cut(cyl(IN(0.250)/2, IN(0.130)))))

# ARM-009 Brass Shaft Collar Lower: OD 0.560, len 0.100, bore 0.280
parts.append(("ARM_009_Brass_Collar_Lower", cyl(IN(0.560)/2, IN(0.100)).cut(cyl(IN(0.280)/2, IN(0.100)))))

# ARM-010 Lower Journal Thrust Washer (stepped): outer step OD 0.8125, inner step OD 0.7825,
# bore 0.280, total thickness 0.1075 (per-step split assumed 50/50)
t = IN(0.1075); t1 = t/2.0
arm010 = cyl(IN(0.8125)/2, t1, 0).fuse(cyl(IN(0.7825)/2, t1, t1)).cut(cyl(IN(0.280)/2, t))
parts.append(("ARM_010_Thrust_Washer_stepped", arm010))

# PLT-001 Platform Disk: OD 3.0085, thick 0.055, center hole 0.370, 6x 0.310 @ 2.300 BCD
plt001 = disc(IN(3.0085), IN(0.055),
              [(IN(0.370), 0, 0)] + bolt_holes(IN(0.310), IN(2.300), 6))
parts.append(("PLT_001_Platform_Disk", plt001))

# PLT-002 Tapered Jar Seal Gasket: wide OD 3.5015 (base) -> narrow 3.2015 (top), height 0.8082,
# center bore 1.5505, 6x 0.310 @ 2.300 BCD
h = IN(0.8082)
gasket = Part.makeCone(IN(3.5015)/2, IN(3.2015)/2, h)
gasket = gasket.cut(cyl(IN(1.5505)/2, h*1.2, -h*0.1))
for d, x, y in bolt_holes(IN(0.310), IN(2.300), 6):
    gasket = gasket.cut(Part.makeCylinder(d/2, h*1.4, App.Vector(x, y, -h*0.2)))
parts.append(("PLT_002_Tapered_Jar_Seal_Gasket", gasket))

# PLT-004 Mount Standoff Tube: OD 0.3765, bore 0.2020, length 0.6990
parts.append(("PLT_004_Mount_Standoff_Tube", cyl(IN(0.3765)/2, IN(0.6990)).cut(cyl(IN(0.2020)/2, IN(0.6990)))))

# PLT-006 Gasket Deck Washer: OD 0.4385, ID 0.1570, thick 0.0415
parts.append(("PLT_006_Gasket_Deck_Washer", cyl(IN(0.4385)/2, IN(0.0415)).cut(cyl(IN(0.1570)/2, IN(0.0415)))))

# BSK-003 Basket Lid: OD 2.70, thick 0.086, center hole 0.1475
parts.append(("BSK_003_Basket_Lid", disc(IN(2.70), IN(0.086), [(IN(0.1475), 0, 0)])))

# BRG-001 Upper Bearing (spherical-sleeve approx): ball OD 0.560, bore 0.250, height 0.670,
#   top collar OD 0.410, bottom collar OD 0.410
def bearing(ball_od, bore, height, top_col, bot_col):
    rb = ball_od/2.0; zc = height/2.0
    s = Part.makeSphere(rb, App.Vector(0, 0, zc))
    s = s.fuse(cyl(bot_col/2.0, zc, 0))           # bottom collar
    s = s.fuse(cyl(top_col/2.0, height-zc, zc))    # top collar
    s = s.cut(cyl(bore/2.0, height*1.2, -height*0.1))
    return s
parts.append(("BRG_001_Upper_Bearing", bearing(IN(0.560), IN(0.250), IN(0.670), IN(0.410), IN(0.410))))

# BRG-002 Lower Bearing: ball OD 0.560, bore 0.280, height 0.700, top collar 0.440, bottom collar 0.405
parts.append(("BRG_002_Lower_Bearing", bearing(IN(0.560), IN(0.280), IN(0.700), IN(0.440), IN(0.405))))

# --- build document, lay out in a row, bake visibility, export ---
doc = App.newDocument("Batch1_Revolved")
xc = 0.0
for name, shp in parts:
    bb = shp.BoundBox
    shp = shp.copy(); shp.translate(App.Vector(xc - bb.Center.x, 0, 0))
    o = doc.addObject("Part::Feature", name)
    o.Shape = shp
    try: o.Visibility = True
    except Exception: pass
    Part.export([o], os.path.join(OUT, name + ".step"))
    xc += bb.XLength + 12.0  # gap
doc.recompute()
fcstd = os.path.join(OUT, "Batch1_Revolved.FCStd")
doc.saveAs(fcstd)

print("PARTS BUILT:", len(parts))
for o in doc.Objects:
    bb = o.Shape.BoundBox
    print("  %-34s in: %.4f x %.4f x %.4f  solid=%s" % (
        o.Name, bb.XLength/MM, bb.YLength/MM, bb.ZLength/MM,
        ("yes" if (o.Shape.isValid() and o.Shape.Solids) else "NO")))
print("SAVED:", fcstd)

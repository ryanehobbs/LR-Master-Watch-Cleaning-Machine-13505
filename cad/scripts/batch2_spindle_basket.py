# L&R Master S/N 13505 - FreeCAD Batch 2: spindle, basket, fasteners
# Confirmed dims in INCHES -> mm. Heavier parts are APPROXIMATED (noted).
import os, math, FreeCAD as App, Part

MM = 25.4
def IN(v): return v * MM
def cyl(r, h, z=0.0): return Part.makeCylinder(r, h, App.Vector(0, 0, z))
ROT = lambda shp, ang: (lambda s: (s.rotate(App.Vector(0,0,0), App.Vector(0,0,1), ang) or s))(shp.copy())

OUT = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad\batch2"
os.makedirs(OUT, exist_ok=True)
parts = []

# ============ SPN-002 Basket Drive Spindle (APPROX impeller) ============
ring_od, ring_id, ring_h = IN(2.703), IN(2.425), IN(0.277)
shaft_od, shaft_len, bore = IN(0.5065), IN(3.05), IN(0.2805)
hub_od = IN(0.85)
pin_d, pin_len, pin_r = IN(0.125), IN(0.145), IN(1.46)

ring = cyl(ring_od/2, ring_h).cut(cyl(ring_id/2, ring_h))
hub  = cyl(hub_od/2, IN(0.45))
shaft = cyl(shaft_od/2, shaft_len)
spindle = ring.fuse(hub).fuse(shaft)
# 3 spokes (approx vanes): radial bars hub->ring
sp_len = ring_id/2 - hub_od/2 + 1.0
for a in (0, 120, 240):
    bar = Part.makeBox(sp_len, IN(0.10), IN(0.20), App.Vector(hub_od/2 - 0.5, -IN(0.05), 0))
    bar.rotate(App.Vector(0,0,0), App.Vector(0,0,1), a)
    spindle = spindle.fuse(bar)
# 3 radial retention pins on ring OD
for a in (0, 120, 240):
    pin = cyl(pin_d/2, pin_len)                      # along +Z
    pin.rotate(App.Vector(0,0,0), App.Vector(0,1,0), 90)   # -> along +X
    pin.translate(App.Vector(ring_od/2 - 1.0, 0, ring_h/2))
    pin.rotate(App.Vector(0,0,0), App.Vector(0,0,1), a)
    spindle = spindle.fuse(pin)
# bore from top down (does not pierce impeller)
spindle = spindle.cut(cyl(bore/2, shaft_len, shaft_len*0.30))
parts.append(("SPN_002_Basket_Drive_Spindle_APPROX", spindle))

# ============ BSK-002 Mesh Basket (cup; mesh shown as thin wall) ============
b_od, b_h, wall = IN(2.8025), IN(2.25), IN(0.03)
mesh_h = b_h - IN(0.25); collar_h = IN(0.25)
body = cyl(b_od/2, mesh_h).cut(cyl(b_od/2 - wall, mesh_h, wall))   # cup w/ bottom
collar = cyl(b_od/2, collar_h, mesh_h).cut(cyl(b_od/2 - IN(0.08), collar_h, mesh_h))
basket = body.fuse(collar)
# 3 bayonet slots (approx vertical notches), width 0.1855
for a in (0, 120, 240):
    slot = Part.makeBox(IN(0.20), IN(0.1855), IN(0.18), App.Vector(b_od/2 - IN(0.20), -IN(0.1855)/2, mesh_h))
    slot.rotate(App.Vector(0,0,0), App.Vector(0,0,1), a)
    basket = basket.cut(slot)
parts.append(("BSK_002_Mesh_Basket_cup", basket))

# ============ Fasteners ============
def bolt(shank_d, length, head_d=None, head_h=None):
    s = cyl(shank_d/2, length)
    if head_d: s = s.fuse(cyl(head_d/2, head_h, length))
    return s

parts.append(("FLG_002_Housing_Bolt",  bolt(IN(0.189), IN(3.090), IN(0.352), IN(0.14))))  # domed head approx (cyl)
parts.append(("STR_008_Stator_Screw",  bolt(IN(0.188), IN(1.942))))                        # slotted headless
parts.append(("SPN_005_Set_Screw",     bolt(IN(0.250), IN(0.185))))                        # 1/4-20 headless
parts.append(("SPN_007_Brass_Screw",   bolt(IN(0.138), IN(0.465), IN(0.265), IN(0.10))))   # #6-32 dome head approx

# ============ build doc, lay out, export ============
doc = App.newDocument("Batch2_Spindle_Basket")
xc = 0.0
for name, shp in parts:
    bb = shp.BoundBox
    shp = shp.copy(); shp.translate(App.Vector(xc - bb.Center.x, 0, 0))
    o = doc.addObject("Part::Feature", name); o.Shape = shp
    try: o.Visibility = True
    except Exception: pass
    Part.export([o], os.path.join(OUT, name + ".step"))
    xc += bb.XLength + 14.0
doc.recompute()
fcstd = os.path.join(OUT, "Batch2_Spindle_Basket.FCStd")
doc.saveAs(fcstd)
print("PARTS:", len(parts))
for o in doc.Objects:
    bb = o.Shape.BoundBox
    print("  %-38s in: %.3f x %.3f x %.3f  solid=%s" % (o.Name, bb.XLength/MM, bb.YLength/MM, bb.ZLength/MM,
        ("yes" if (o.Shape.isValid() and o.Shape.Solids) else "NO")))
print("SAVED:", fcstd)

# L&R Master S/N 13505 - FreeCAD Batch 5: exploded assembly (imports Batch 1-4 STEPs)
import os, FreeCAD as App, Part
MM = 25.4
CAD = r"C:\Users\ryane\OneDrive\Documents\Hobbies\Watch Repair\L&R Master Watch Cleaning Machine 13505\cad"
OUT = os.path.join(CAD, "assembly"); os.makedirs(OUT, exist_ok=True)

def load(folder, name):
    s = Part.Shape(); s.read(os.path.join(CAD, folder, name + ".step")); return s

# main central column, TOP -> BOTTOM (true assembly order)
COLUMN = [
    ("batch3","UH_001_Upper_Housing_APPROX"),
    ("batch4","STR_001_Stator_Ring_APPROX"),
    ("batch1","BRG_001_Upper_Bearing"),
    ("batch4","ARM_001_Armature_Rotor_APPROX"),
    ("batch1","BRG_002_Lower_Bearing"),
    ("batch3","LH_001_Lower_Housing_APPROX"),
    ("batch1","ARM_010_Thrust_Washer_stepped"),
    ("batch1","PLT_001_Platform_Disk"),
    ("batch1","PLT_002_Tapered_Jar_Seal_Gasket"),
    ("batch2","SPN_002_Basket_Drive_Spindle_APPROX"),
    ("batch2","BSK_002_Mesh_Basket_cup"),
    ("batch1","BSK_003_Basket_Lid"),
]
# hardware side column
HARDWARE = [
    ("batch2","FLG_002_Housing_Bolt"),
    ("batch2","STR_008_Stator_Screw"),
    ("batch1","PLT_004_Mount_Standoff_Tube"),
    ("batch1","PLT_006_Gasket_Deck_Washer"),
    ("batch2","SPN_005_Set_Screw"),
    ("batch2","SPN_007_Brass_Screw"),
    ("batch1","ARM_008_Brass_Collar_Upper"),
    ("batch1","ARM_009_Brass_Collar_Lower"),
]

doc = App.newDocument("L_and_R_Master_Exploded")

def place_column(items, target_x, gap):
    top = 0.0
    for folder, name in items:
        shp = load(folder, name).copy()
        bb = shp.BoundBox
        shp.translate(App.Vector(target_x - bb.Center.x, 0 - bb.Center.y, top - bb.ZMax))
        o = doc.addObject("Part::Feature", name); o.Shape = shp
        try: o.Visibility = True
        except Exception: pass
        top -= (bb.ZLength + gap)

place_column(COLUMN, 0.0, 14.0)
place_column(HARDWARE, 150.0, 10.0)

doc.recompute()
fcstd = os.path.join(OUT, "L_and_R_Master_Exploded.FCStd")
doc.saveAs(fcstd)
# combined STEP of everything
Part.export(doc.Objects, os.path.join(OUT, "L_and_R_Master_Exploded.step"))
print("OBJECTS:", len(doc.Objects))
print("SAVED:", fcstd)

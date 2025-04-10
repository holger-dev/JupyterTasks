#!/usr/bin/env python3
import os, sys, json, shutil, getpass, unicodedata, grp

def normalize_name(name):
    return unicodedata.normalize("NFKD", name.lower().replace(" ", "").replace("-", "")).encode("ascii", "ignore").decode()

def finde_schuelerpfad(vorname, nachname):
    vn, nn = normalize_name(vorname), normalize_name(nachname)
    for ordner in os.listdir("/mnt/vol1_jupyter/"):
        if ordner.startswith("jupyter-") and vn in normalize_name(ordner) and nn in normalize_name(ordner):
            return os.path.join("/mnt/vol1_jupyter/", ordner)
    return None

if len(sys.argv) != 3:
    print("Aufruf: lehrer_collect.py <KURSNAME> <DATEINAME_OHNE_ENDUNG>")
    sys.exit(1)

kurs, basisname = sys.argv[1:]
nutzer = getpass.getuser()
gruppen = [g.gr_name for g in grp.getgrall() if nutzer in g.gr_mem]
if "lehrer" not in gruppen:
    print("🚫 Zugriff verweigert: Nur für Mitglieder der Gruppe 'lehrer'")
    sys.exit(1)

kurse = json.load(open("/mnt/vol1_jupyter/jsondata/kurse.json"))
if kurs not in kurse:
    print(f"🚫 Kurs '{kurs}' nicht gefunden.")
    sys.exit(1)

zielordner = f"/mnt/vol1_jupyter/{nutzer}/Abgabe_{basisname}"
os.makedirs(zielordner, exist_ok=True)

print(f"📥 Sammle '{basisname}.ipynb' aus Kurs '{kurs}':\n")

for s in kurse[kurs]["schueler"]:
    pfad = finde_schuelerpfad(s["vorname"], s["nachname"])
    if pfad:
        quell = os.path.join(pfad, f"{basisname}_{normalize_name(s['vorname'])}.{normalize_name(s['nachname'])}.ipynb")
        if os.path.exists(quell):
            shutil.copy2(quell, zielordner)
            print(f"✅ {s['vorname']} {s['nachname']} → eingesammelt")
        else:
            print(f"⚠️ {s['vorname']} {s['nachname']} → Datei fehlt")
    else:
        print(f"❌ {s['vorname']} {s['nachname']} → Verzeichnis nicht gefunden.")

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

if len(sys.argv) != 4:
    print("Aufruf: lehrer_copy.py <KURSNAME> <QUELLDATEI> <DATEINAME_OHNE_ENDUNG>")
    sys.exit(1)

kurs, quelldatei, basisname = sys.argv[1:]
nutzer = getpass.getuser()
gruppen = [g.gr_name for g in grp.getgrall() if nutzer in g.gr_mem]
if "lehrer" not in gruppen:
    print("🚫 Zugriff verweigert: Nur für Mitglieder der Gruppe 'lehrer'")
    sys.exit(1)

kurse = json.load(open("/mnt/vol1_jupyter/jsondata/kurse.json"))
if kurs not in kurse:
    print(f"🚫 Kurs '{kurs}' nicht gefunden.")
    sys.exit(1)

print(f"📤 Verteile '{quelldatei}' an Kurs '{kurs}':\n")

for s in kurse[kurs]["schueler"]:
    pfad = finde_schuelerpfad(s["vorname"], s["nachname"])
    if pfad:
        zieldatei = f"{basisname}_{normalize_name(s['vorname'])}.{normalize_name(s['nachname'])}.ipynb"
        ziel = os.path.join(pfad, zieldatei)
        shutil.copy2(quelldatei, ziel)
        print(f"✅ {s['vorname']} {s['nachname']} → {ziel}")
    else:
        print(f"❌ {s['vorname']} {s['nachname']} → Verzeichnis nicht gefunden.")

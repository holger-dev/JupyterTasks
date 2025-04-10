#!/usr/bin/env python3
import subprocess, json, os, grp, getpass
from datetime import datetime

JSON_PFAD = "/mnt/vol1_jupyter/jsondata/kurse.json"
TASK_PFAD = "/mnt/vol1_jupyter/tasks"

def farbe(text, code):
    return f"\033[{code}m{text}\033[0m"

def zeige_menue():
    print("\n" + farbe("=== 📚 Lehrer-Menü ===", "1;36"))
    print(f"{farbe('1)', '1;32')} 📤 Aufgabe an Kurs verteilen")
    print(f"{farbe('2)', '1;33')} 📥 Aufgabe von Kurs einsammeln")
    print(f"{farbe('3)', '1;34')} 💬 Feedback an Kurs verteilen")
    print(f"{farbe('4)', '1;35')} 👤 Einzelaufgabe an Schüler verteilen")
    print(f"{farbe('5)', '1;31')} ❌ Abbrechen")

def kurs_auswahl():
    with open(JSON_PFAD) as f:
        kurse = json.load(f)
    kursliste = list(kurse.keys())

    print("\nVerfügbare Kurse:")
    for idx, kurs in enumerate(kursliste):
        print(f"{farbe(str(idx + 1), '1;36')}) {kurs}")

    auswahl = input("\nKursnummer eingeben: ")
    if not auswahl.isdigit() or int(auswahl) < 1 or int(auswahl) > len(kursliste):
        print(farbe("❌ Ungültige Eingabe.", "1;31"))
        return None

    return kursliste[int(auswahl) - 1]

def hauptmenue():
    nutzer = getpass.getuser()
    gruppen = [g.gr_name for g in grp.getgrall() if nutzer in g.gr_mem]
    if "lehrer" not in gruppen:
        print(farbe("🚫 Zugriff verweigert: Nur für Mitglieder der Gruppe 'lehrer'", "1;31"))
        return

    while True:
        zeige_menue()
        wahl = input(farbe("\n🔧 Aktion auswählen (1–5): ", "1;36")).strip()

        if wahl == "1":
            kurs = kurs_auswahl()
            if kurs:
                dateiname = input("📄 Dateiname (ohne .ipynb): ").strip()
                quelldatei = f"{dateiname}.ipynb"
                subprocess.run([f"{TASK_PFAD}/lehrer_copy.py", kurs, quelldatei, dateiname])
        elif wahl == "2":
            kurs = kurs_auswahl()
            if kurs:
                dateiname = input("📄 Dateiname (ohne .ipynb): ").strip()
                print(f"📦 Einsammeln gestartet ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
                subprocess.run([f"{TASK_PFAD}/lehrer_collect.py", kurs, dateiname])
        elif wahl == "3":
            kurs = kurs_auswahl()
            if kurs:
                dateiname = input("📄 Dateiname (ohne .ipynb): ").strip()
                print(f"📤 Feedback startet ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
                subprocess.run([f"{TASK_PFAD}/lehrer_feedback.py", kurs, dateiname])
        elif wahl == "4":
            vorname = input("👤 Vorname des Schülers: ").strip()
            nachname = input("👤 Nachname des Schülers: ").strip()
            dateiname = input("📄 Dateiname (ohne .ipynb): ").strip()
            subprocess.run([f"{TASK_PFAD}/lehrer_copy_one.py", vorname, nachname, dateiname])
        elif wahl == "5":
            print(farbe("\n🚪 Vorgang abgebrochen. Auf Wiedersehen!", "1;31"))
            break
        else:
            print(farbe("❌ Ungültige Auswahl. Bitte 1–5 eingeben.", "1;31"))

if __name__ == "__main__":
    hauptmenue()

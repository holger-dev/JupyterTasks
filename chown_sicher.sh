#!/bin/bash
# Dieses Skript sollte mit einem Cronjob alle 30 Sekunden verbunden werden, damit die Zugriffsrechte der User:innen korrekt gesetzt werden. Sonst können die SuS nicht in die Notebooks coden!

# Die Base gibt an, wo die Verzeichnisse von Jupyter gespeichert werden!
BASE="${1:-/mnt/vol1_jupyter}"

# Nur Schülerordner durchgehen (nicht versteckte Ordner!)
find "$BASE" -maxdepth 2 -mindepth 2 -type f -name "*.ipynb" ! -path "*/.*/*" |>
  dir=$(dirname "$file")
  file_owner=$(stat -c %U "$file" 2>/dev/null)
  dir_owner=$(stat -c %U "$dir" 2>/dev/null)

  if [ "$file_owner" != "$dir_owner" ] && [ -n "$dir_owner" ]; then
    chown "$dir_owner:$dir_owner" "$file"
    echo "🔁 Setze Besitzer von $file → $dir_owner"
  fi
done

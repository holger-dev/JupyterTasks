# Vorbereitung

Damit du eine Aufgabe an einen Kurs verteilen kannst, muss der gesamte Kurs einmal in der JSON angelegt werden. Die Datei DATEIPFAD/jsondata/kurse.json enthält die Kurse. Hier nach dem Schema in der Datei einen Kurs inkl. aller Schüler anlegen (bitte Kursex.json beachten)! Hier könnte man auch am Anfang des Schuljahres mit einem Script anhand der Kurslisten die Kursdateien erstellen. 

Jeder Schüler erhält einen User auf dem Jupyter-Server, unabhängig des Kurses. Das bedeutet, dass jeder Schüler die Daten aus z.B. Klasse 8 automatisch auch in Klasse 9 mitnimmt, da nur die Kurszuweisung in der JSON geändert wird, nicht aber der User selbst.

Jeder Lehrer muss in der Gruppe lehrer auf dem Server sein! So fügt man Lehrer hinzu (vorher als root auf dem Server anmelden!)

´´´
sudo usermod -aG lehrer BENUTZERNAME
´´´

Die Gruppenzuweisung ist wichtig, da nur Lehrer das Recht haben, Daten in die Schülerverzeichnisse zu kopieren! Dies muss mit dem root-User auf dem Server bei jedem neuen Lehrer aktualisiert werden, damit dieser auch verteilen kann.

Wir verteilen immer eine Datei, die wir in unserem individuellen Jupyter haben. Das bedeutet, diese Datei muss auch im eigenen Verzeichnis vorhanden sein.

Sobald ../tasks/start.py ausgeführt wird und ein Dateiname eingegeben, sucht das Script aus dem aktuellen Ort nach dieser Datei! Willst du also die Datei im Verzeichnis Aufgaben/WPU8/Python/AB_01.py verteilen, musst du entweder den ganzen Pfad angeben oder in das Verzeichnis navigieren (mit cd VERZEICHNIS oder cd ../ wieder hoch usw.) und von hier die Datei verteilen.

# Verteilen
Gehe als Lehrer normal in dein Jupyter rein.
Erstelle ein Aufgaben-Notebook, z.B. Aufgabe1.

Öffne dann ein Terminal in Jupyter (neuer Tab und dann Terminal) und gebe ein ../tasks/start.py
Wähle im Menü 1 aus zum Verteilen.
Wähle deinen Kurs aus.
Gebe den Dateinamen (ohne Endung) ein von der Datei, die verteilt werden soll (beachte den Hinweis zum Dateinamen).
Enter!
Der Output zeigt dir, welche Schüler alles die Datei bekommen haben.

Nun musst du 30 Sekunden warten! Danach sind erst alle Schreibrechte gesetzt und die Schüler können die Datei in ihrem individuellen Jupyter bearbeiten.

Dateien werden einfach in den Schülerordnern kopiert und ggf. auch überschrieben! Achte also gut auf die Dateinamen, dass diese einzigartig sind! Z.B. PF8_T1_Test.py o.ä.!

# Einsammeln

Beim Einsammeln werden aus dem gesamten Kurs die Datei eingesammelt. Wichtig ist, dass der Dateiname der gleiche ist wie bei der Datei, die verteilt worden ist. Die Schüler dürfen NICHT den Dateinamen ändern! Anschließend wie folgt vorgehen:

Gehe als Lehrer normal in dein Jupyter rein.
Öffne dann ein Terminal in Jupyter (neuer Tab und dann Terminal) und gebe ein ../tasks/start.py
Wähle im Menü 2 aus zum Einsammeln.
Wähle deinen Kurs aus.
Gebe den Dateinamen (ohne Endung) ein von der Datei, die eingesammelt werden soll.
Enter!
Der Output zeigt dir, welche Dateien eingesammelt worden sind.
Feedback verteilen

Nachdem alle Dateien im Ordner kontrolliert und bewertet worden sind, kann die Feedback-Datei verteilt werden. Dazu wie folgt vorgehen:

Gehe als Lehrer normal in dein Jupyter rein.
Öffne dann ein Terminal in Jupyter (neuer Tab und dann Terminal) und gebe ein ../tasks/start.py
Wähle im Menü 3 aus zum Feedback verteilen.
Wähle deinen Kurs aus.
Gebe den Dateinamen (ohne Endung) ein von der Datei, die eingesammelt werden soll.
Enter!
Der Output zeigt dir, welche Feedbackdateien verteilt worden sind.
Einzelkopie

Sollte ein Schüler nachträglich in den Kurs kommen oder es andere Probleme geben, kann die Aufgabe auch an einen Schüler verteilt werden. Voraussetzung ist, dass der Schüler einmal bei Jupyter eingeloggt war!
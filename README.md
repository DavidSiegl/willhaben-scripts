# Automate willhaben

Für passionierte Gebrauchtwarenhändler und Schnäppchenjäger werden hier pythonbasierte Skripts zur Verfügung gestellt, um repetitive Inputs bzw. Prozesse auf der Seite willhaben.at zu automatisieren. 
Das Projekt ist noch nicht abgeschlossen und wird laufend um weitere Skripts ergänzt.

Bereits verfügbare Skripts:
 - willhaben_neu_einstellen.py überprüft die Anzeigen eines Useraccounts, und falls abgelaufene Anzeigen existieren, werden diese automatisch wiedereingestellt.
 - willhaben_preise ermöglicht das Aktualisieren der Preise der ältesten fünf Artikeln eines Useraccounts mittels der Eingabe individueller Discount-Variablen, um so die Chance auf einen Verkauf von weniger beliebten Artikel zu erhöhen.

Um die Interaktion von Skript und Browser zu ermöglichen, wird die Erweiterung Selenium [https://www.selenium.dev/] benötigt.

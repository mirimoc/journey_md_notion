---
title: Nächste Schritte
date: 2023-03-17
---

---
title: Nächste Schritte
date: 2023-07-17
---

## To Dos

* Test der zwei Pakete
* Analysieren des Codes
* Was kann ich alles verwenden
* Was muss ich adden

## Plan

Habe gerade ein anderes Paket gefunden [md2notion](https://github.com/Cobertos/md2notion).
Leider ist das auch nicht so toll, aber ich kann mein md-File rendern lassen, und dann uploaden.
So müsste ich nur den Upload nachbauen.

### Ablauf

1. Erstellen bzw. 'öffnen' einer Notion Page
2. Vergleich notion page mit git repo .md-files aus dem Journal Ordner
3. Aufzeigen der Unterschiede
4. Merge der beiden Versionen
5. Aktualisieren von notion page mit den Änderungen aus dem git repo und umgekehrt

## Komplikationen

* Pakete dürfen keinen "-" im Namen haben. Hatte Probleme das Paket zu importieren.
* Werden damit fette Probleme mit dem Subtree haben. Werde ich mir aber später anschauen.
* git-notion baut auf ein Paket auf, welches eine inoffizielle API nutzt und statt des offiziellen API-Tokens wird ein
  Token-v2 genutzt, welcher mit den Cookies verwendet wird. Das will ich nicht, was heißt, dass ich doch ein eigenes
  Paket schreiben muss.
* Leider kann ich auch nicht [md2notion](https://github.com/Cobertos/md2notion)  nutzen, da das Rendern mit einem
  anderen Paket erstellt worde. Ich müsste alles umschreiben.

## Ideen

Was auch geil wäre, wenn ich alles als Hugo printen könnte.


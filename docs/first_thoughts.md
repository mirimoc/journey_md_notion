---
title: "Brainstorming"
date: 2023-07-12
---

## Wie würde der perfekte Ablauf des Programms aussehen?

1. Schreiben von Notizen in docs in einem .md-File
2. Schreiben von Notizen in Notion
3. Initialisieren eines Notion Projekt per API
    1. Übergeben einer Notion API-Keys in einem config-file
    2. Name des Projektes und weitere Parameter definieren
    3. Erstellen eines Projektes in einer Datenbank
1. Push/Pull -> Daten werden synchronisiert
2. Ad Hoc -> Daten werden per Befehl(CLI, Script, Executable, etc.) synchronisiert

## Wie sieht ein MVP aus?


* Mithilfe von Python oder Go einfaches Script/Executable manuell Sync erstellen

## Welche Funktionen sind essenziell für das MVP?

* Markdown to Notion
* Notion to Markdown

## Was für Tools gibt es bereits oder welche Tools können benutzt werden?

* https://github.com/tryfabric/martian -> markdown to notion parser | Typescript
* https://github.com/kjk/notionapi/blob/master/tomarkdown/markdown.go -> notion to markdown | Go
* https://github.com/Cobertos/md2notion/ -> markdown to notion | Python
* https://github.com/echo724/notion2md -> notion to markdown | Python

## Welchen Ansatz nutze ich?

Tyescript fällt für mich raus, weil ich überhaupt keine Ahnung habe Typescript zu installieren, geschweige wie ich es
nutze. Bei Go habe ich ein Paket gefunden, dass 'nur' in eine Richtung geht. Für Python hingehen in beide Richtungen und
beide Pakete können auch als CLI genutzt werden, weshalb ich für den ersten Lauf auf die zwei Python Pakete
zurückgreifen werde. Gerne würde ich Golang testen und eine CLI damit aufbauen, aber es ist zu einfach zwei Python
Pakete zu nutzen, die auch noch CLI anbieten.

Vielleicht schreibe ich später eine Golang CLI für diesen Anwendungsfall, gerade ist mir schnelles Entwickeln wichtiger
als langes Experimentieren.

## Was sind die nächsten Schritte?

1. Testen der zwei Pakete
2. Verbinden der Pakete
4. Überlegen, wie ich die CLI in meinen Workflow nutzen kann.
3. Fork der Pakete, wenn viele Änderungen gemacht werden müssen.


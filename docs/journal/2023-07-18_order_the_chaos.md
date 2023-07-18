---
title: Order the chaos
date: 2023-07-18
kind: "todo"
---

## Aufbau

Drei wesentliche Aufgaben gibt es, die ich realisieren will:

* Umwandeln von Markdown to Notion -> md2notion
* Umwandeln von Notion to Markdown -> notion2md
* Synchronisieren von Notion und Markdown 

## Umwandeln von Markdown to Notion
* Schreiben einer markdown Datei
* Einlesen der Eigenschaften der Markdown-Datei
* Einlesen der Blöcke der Markdown-Datei
* Erstellen einer Notion-Seite
* Importieren der Eigenschaften aus der Markdown-Datei in die Notion-Seite
* Importieren der Blöcke aus der Markdown-Datei in die Notion-Seite
* Speichern der Notion-Seite

## Herausforderungen
* Wie erstelle ich eine Notion-Seite an der richtigen Stelle?
* Wie importiere ich die Eigenschaften in die Notion-Seite?
* Wie importiere ich die Blöcke in die Notion-Seite?
* Wie überführe ich die Blöcke aus dem Markdown in die Notion-Seite?
* Wie erstelle ich eine Notion-Seite nur dann, wenn sie noch nicht nicht existiert?

## Tests
* [ ] Manuelles Erstellen einer Seite auf Notion und überschreiben dieser mit der API 
* [ ] Konvertieren mit `convert` aus md2notion und upload mit der offiziellen API
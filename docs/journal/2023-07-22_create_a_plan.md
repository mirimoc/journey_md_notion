---
title: Create a plan
date: 2023-07-22
---

## Was habe ich vor?

Ich will mir einen Überblick schaffen, wie `md2notion` funktioniert und wie ich es für meine Zwecke nutzen kann.
Wenn ich es programmiere auf meine Weise, habe ich die Befürchtung, dass es zu umständlich wird.
Deshalb möchte ich mich von anderen Instanzen inspirieren lassen.
Außerdem ist das auch eine gute Übung, um mich im 'Code-Reading' vertraut zu machen.

## Was ist mein Ziel und wie will ich vorangehen?

* Ziel ist es, dass ich es mir so einfach mache, wie nötig, um einen Code zu schreiben, den ich nutzen kann, um md-Files
  in Notion zu importieren.
* Ich suche eine Möglichkeit, wie ich am besten meine md-Files in Notion importieren kann.
* Für das erste reicht mir straight-forward, dass es hochgeladen wird, sprich Datei wird erstellt und hochgeladen.
* Ich möchte es vermeiden, dass ich für jedes Element eine eigene Funktion schreiben muss.
* Deshalb will ich schauen, wie es in `md2notion` gelöst ist.

## Ablauf von `md2notion`

* `upload` wird aufgerufen, um eine Klasse, die extra für diesen Upload erstellt wurde, initialisiert.
* Es auch möglich, dass man einzelne Elemente hochladen kann. Dafür wird die Datei zuerst gerendert.
* In diesem Rendern wird diese Arbeit gemacht.
* Es wurde ein `Converter` erstellt, der die Markdown-Datei rendert. Diese Render-Klasse ist erbt von einer
  BaseRender-Klasse, die aus Mistletoe stammt. Mistletoe parsen die Markdown-Datei und gibt einen Baum zurück.
* mistloe nutzt Renderer, die Markdowns rendern.
* md2notion nutzt dafür einen eigens konzipierteen Renderer (NotionPyRenderer), der die Markdown-Elemente in
  Notion-Elemente umwandelt.
* OK. In NotionPy `notion.block` sind alle möglichen Blöcke definiert, die es in Notion gibt ... also genau das, was ich
  verhindern wollte zu machen.
* Es wird dort sehr viel mit Vererbung gemacht. Finde ich ganz nice, weil man dann nicht ewig viel schreiben muss, aber
  was die Lesbarkeit angeht, ist es nicht so schön.
* Für meinen Anwendungsfall brauche ich ja nicht alle. Auch bei md2notion werden nur die Blöcke importiert, die wirklich
  genutzt werden. Dies wird nur problematisch, wenn ich Blöcke in Notion nutzen will, die es in Markdown nicht gibt bzw.
  gesondert behandelt werden müssen. Damit kann ich die meisten Blöcke in notion-py ignorieren.

## Was habe ich gelernt?

* Wirklich wahnsinnig eleganten Code zu schreiben, ist gar nicht so einfach. Die meisten schreiben denselben Mist hin
* Meine Anfangsidee war also gar nicht so schlecht.
* Es hat Spaß gemacht, den Code von anderen zu lesen und zu verstehen. Hilfreich ist es am Anfang zu schauen, welche
  Pakete anfangs importiert werden.
* Ich brauche bald mal eine CLI, um die Markdown-Dateien zu erstellen. Dafür brauche ich aber wieder Templates für meine
  Markdown bzw. wäre das nice to have.

## Was sind die nächsten Schritte?

* Erstmal die CLI bauen. Scheint wirklich sehr entspannt zu sein, ob mit Go oder Python. Beides ist schnell und
  unkompliziert umzusetzen.
* Schwieriger wird es, dass ich mir eine Struktur baue, die immer gleich ist. Also, dass ich immer die gleichen Blöcke
  nutze. Das ist aber auch nicht so schwer. Ich muss mir nur überlegen, wie ich das am besten mache.
* Kann ich ja auch mit der Zeit anpassen.
* Alle Blöcke, die ich brauche. Vielleicht brauche ich mich nicht so sehr mit `notion-py` auseinandersetzen, da die
  Struktur schon anders ist. Am Ende sind es .json-Files, die ich hochladen muss. Jedoch das mit den Renderer
  interessiert mich, und ich würde mir das gerne anschauen.

Also:
* [ ] CLI bauen 
* [ ] Renderer anschauen und verstehen
* [ ] Ersten Block bauen und schauen, ob es funktioniert.
---
title: "Erste Schritte"
date: 2023-07-13
---

## To Dos

* Test der zwei Pakete
* Analysieren des Codes
* Auslesen eines Markdowns
* Forken

## Journal

### Git Notion

Sehr einfaches Packages, welches eine CLI beinhaltet und auch bereits einen Workflow anbietet.
Es werden alle .md-Files wie sie im Repo strukturiert sind in Notion hochgeladen.
Gerne würde ich jedoch nur .md-Files synchronisieren, die auch als "hochladen" markiert sind.

    def sync_to_notion(repo_root: str = "."):
        os.chdir(repo_root)
        config = ConfigParser()
        config.read(os.path.join(repo_root, "setup.cfg"))
        repo_name = os.path.basename(os.getcwd())

        root_page_url = os.getenv("NOTION_ROOT_PAGE") or config.get('git-notion', 'notion_root_page')
        ignore_regex = os.getenv("NOTION_IGNORE_REGEX") or config.get('git-notion', 'ignore_regex', fallback=None)
        root_page = get_client().get_block(root_page_url)
        repo_page = get_or_create_page(root_page, repo_name)

        # TODO: Add if statement for read-able markdowns.
        for file in glob.glob("**/*.md", recursive=True):
            if ignore_regex is None or not re.match(ignore_regex, file):
                print(file)
                upload_file(repo_page, file)

Wenn ich die Schleife anpasse, kann ich dies ändern, dass nur die Artikel geändert werden, die ich ändern möchte.

Das Auslesen wird in der Funktion `upload_file` gemacht. Mithilfe von hash-Funktionen werden Änderungen ermittelt.

    def upload_file(base_page, filename: str, page_title=None):
        page_title = page_title or filename
        page = get_or_create_page(base_page, page_title)
        
        # md5 -> cryptographic hash function
        hasher = hashlib.md5()
        with open(filename, "rb") as mdFile:
            buf = mdFile.read()
            hasher.update(buf)
        if page.children and hasher.hexdigest() in str(page.children[0]):
            return page

        for child in page.children:
            child.remove()
        page.children.add_new(TextBlock, title=f"MD5: {hasher.hexdigest()}")

        with open(filename, "r", encoding="utf-8") as mdFile:
            upload(mdFile, page)
        return page    

Ich bin mir nicht sicher, ob es mit Hash möglich ist, genaue Größen herauszufiltern und diese gesondert zu speichern.
Ich hätte json genutzt.

In diesem Paket wird nur von der 'Github-Seite' das ganze betrachtet.(Was tun, wenn es nicht Github ist?)
Es fehlt das Modul, dass abgecheckt wird, ob Notion etwas Neues hat. Da muss eh definiert werden, was dann geupdatet
wird und was dann die obere Instanz ist. Ob wir über das Datum gehen? Markdowns haben kein Änderungsdatum oder ob Github
immer das neuste ist?! Kann gut sein, dass schnell mal alles vernichtet wird. Müsste daher ein Merge geben.

Jedenfalls muss das noch hinzugefügt werden.

Heute ist mir die Idee gekommen, dass ich ein LLM Modell nutzen könnte und auf Basis dessen meine Fragen stellen könnte.
Ich könnte es mit meinen Daten finetunen und auch alle Kundenprojekte könnte ich damit finetunen und Kundenreports
könnten dann erstellt werden.
Ich könnte auch eine Summary über die ganzen .md-Files erstellen und dann diese immer in ein großes .md-File einfügen.

## Ideen

* Ich könnte schauen, wie [notion2md](https://github.com/echo724/notion2md) funktioniert und wie ich das in mein Projekt
  einbinden kann.
* Vielleicht wäre es auch eine Idee, dass ich beides erstmal erzeuge und dann miteinander vergleiche?! Finde ich ganz
  gut, jedoch muss ich mal schauen, ob der Output der zwei Pakete gleich ist, wenn ja, dann könnte ich
  wieder mit der Hash-Funktion arbeiten.
  Wenn nicht, müsste ich schauen, was man dann macht. Sehr geil wäre es, wenn es dann in einem Merge Konflikt endet.
* Um das ganze zu deployen, wäre es nice, es ins Docker zu packen. Ich könnte auch schauen, ob ich das ganze in ein
  Python-Package packen kann. Dafür müsste ich dann ein dockerfile erstellen.
* Dann kann es lokal sowie auf einem Server deployed werden.
* Ich könnte auch schauen, wie ich das mit dem LLM Modell machen kann, aber das wird wohl erst später eingesetzt.

## Was sind die nächsten Schritte - Umsetzung?

Da ich wohl [notion2md](https://github.com/echo724/notion2md) und [git-notion](https://github.com/NarekA/git-notion)
beides nutzen will, wie ich diese zwei Repos in mein Repo einbinde. Nutze ich ein Submodule oder Subtree?
Ich glaube ich gehe mit Subtree, weil ich nicht so hart auf Trennung gehen muss. Da am Ende alles eins sein wird, ist
mir es michtiger, dass die Historie erhalten bleibt.

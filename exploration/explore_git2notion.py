import mistletoe

from md2notion.upload import convert, uploadBlock

import configparser
from notion_client import Client
from notion_client.helpers import collect_paginated_api
from notion_client.helpers import iterate_paginated_api

config = configparser.ConfigParser()
try:
    from Renderer import NotionPyRenderer
    config.read('../config.ini')
    with open('../docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)
except:
    from exploration.Renderer import NotionPyRenderer
    config.read('config.ini')
    with open('docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)

notion_token = config.get('NOTION', 'TOKEN')
database_id = config.get('NOTION', 'DB_ID')

notion = Client(auth=notion_token)

page_id = 'dcdd3971a8f24047929a931a912cb9d5'

page_ids = list()
for pages in iterate_paginated_api(notion.databases.query, database_id=database_id):
    print(pages)

import yaml

def parse_markdown_with_header(markdown_content):
    # Split the Markdown content into lines
    lines = markdown_content.strip().split("\n")

    # Find the start and end of the YAML front matter (between the first two '---' lines)
    start_index = None
    end_index = None
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start_index is None:
                start_index = i
            elif end_index is None:
                end_index = i
                break

    if start_index is not None and end_index is not None:
        # Extract the YAML front matter content
        yaml_content = "\n".join(lines[start_index + 1 : end_index]).strip()

        # Parse the YAML content
        yaml_data = yaml.safe_load(yaml_content)

        # Extract the title and date from the YAML data
        title = yaml_data.get("title", "")
        date = yaml_data.get("data", "")
        rest_of_content = "\n".join(lines[end_index + 1 :]).strip()

    #     # Render the rest of the Markdown content using Mistletoe
    #     rendered_content = mistletoe.markdown(rest_of_content)
    #     return title, date, rendered_content
    # else:
    #     # If no YAML front matter found, render the entire content
    #     rendered_content = mistletoe.markdown(markdown_content)
    #     return "", "", rendered_content








for block in rendered:
    print(block)
    notion.blocks.children.append(block_id=page_id, children=[block])












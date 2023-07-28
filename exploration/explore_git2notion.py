import mistletoe
from Renderer import NotionPyRenderer
from md2notion.upload import convert, uploadBlock

import configparser
from notion_client import Client
from notion_client.helpers import collect_paginated_api
from notion_client.helpers import iterate_paginated_api
rendered = convert("../docs/journal/brainstorming.md")

# # Follow the instructions at https://github.com/jamalex/notion-py#quickstart to setup Notion.py
# client = NotionClient(token_v2="<token_v2>")
# page = client.get_block("https://www.notion.so/myorg/Test-c0d20a71c0944985ae96e661ccc99821")
#
# with open("TestMarkdown.md", "r", encoding="utf-8") as mdFile:
#     newPage = page.children.add_new(PageBlock, title="TestMarkdown Upload")
#     upload(mdFile, newPage) #Appends the converted contents of TestMarkdown.md to newPage
#
# # Process the rendered array of `notion-py` block descriptors here
# # (just dicts with some properties to pass to `notion-py`)
#
# # Upload all the blocks
# for blockDescriptor in rendered:
#     uploadBlock(blockDescriptor, page, mdFile.name)

config = configparser.ConfigParser()
config.read('../config.ini')

notion_token = config.get('NOTION', 'TOKEN')
database_id = config.get('NOTION_DB', 'DB_ID')

notion = Client(auth=notion_token)

try:
    with open('../docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)
except:
    with open('docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)




page_ids = list()
for pages in iterate_paginated_api(notion.databases.query, database_id=database_id):
    print(pages)














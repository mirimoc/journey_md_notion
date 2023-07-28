import mistletoe
from Renderer import NotionPyRenderer

try:
    with open('../docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)
except:
    with open('docs/journal/2023-07-27_23:16:27_planning.md', 'r') as fin:
        rendered = mistletoe.markdown(fin, NotionPyRenderer)
print(rendered)

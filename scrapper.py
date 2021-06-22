import requests
import re
import ast
from bs4 import BeautifulSoup

LINK = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSW5uZLrFwbB16BFBvn7XaIwlsgudMwMmHlqSOs8I5etYAYuek6jgYEQM4cDvhRCDWp5a1ZGLwHLkkn/pubchart?oid=291919261&format=interactive"

r = requests.get(LINK)
soup = BeautifulSoup(r.content, 'html.parser') 
info = soup.find("script").find_next_sibling()

trimmed = re.search("'chartJson': '(.*?)', 'serializedChartProperties'", str(info)).group(1)
converted = "\"" + trimmed.replace("\\/", "/").encode().decode('unicode_escape').replace('\"','\'') + "\""
# x = ast.literal_eval(y)
# print(x)
# print(type(x))

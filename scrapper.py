import requests
import re
import ast
from bs4 import BeautifulSoup

LINK = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSW5uZLrFwbB16BFBvn7XaIwlsgudMwMmHlqSOs8I5etYAYuek6jgYEQM4cDvhRCDWp5a1ZGLwHLkkn/pubchart?oid=291919261&format=interactive"

def get_info():
    r = requests.get(LINK)
    soup = BeautifulSoup(r.content, 'html.parser') 
    info = soup.find("script").find_next_sibling()

    trimmed = re.search("'chartJson': '(.*?)', 'serializedChartProperties'", str(info)).group(1)
    converted =  trimmed.replace("\\/", "/").encode().decode('unicode_escape').replace('\"','\'').replace("true", "True")

    dictionary = ast.literal_eval(converted)

    location = dictionary['options']['title']
    time = dictionary['subtitle']
    percentage = dictionary['dataTable']['rows'][0]['c'][0]['f']
    waiting = dictionary['dataTable']['rows'][0]['c'][1]['f'] 

    return location, time, percentage, waiting
import requests
import re
import ast
from bs4 import BeautifulSoup

LINK_ELIAS = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSW5uZLrFwbB16BFBvn7XaIwlsgudMwMmHlqSOs8I5etYAYuek6jgYEQM4cDvhRCDWp5a1ZGLwHLkkn/pubchart?oid=291919261&format=interactive"
LINK_EHUB = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKl9d-Qyig483T0HB8Y8C3yKngbXny3uXzjr6YhAPQmtHTGqAHo727SEOHbnOsKNj9c330vaCL3VOU/pubchart?oid=291919261&format=interactive"
LINK = ""

def get_info(choice):
    if choice == 1:
        LINK = LINK_ELIAS
    else:
        LINK = LINK_EHUB

    r = requests.get(LINK)
    soup = BeautifulSoup(r.content, 'html.parser') 
    info = soup.find("script").find_next_sibling()

    trimmed = re.search("'chartJson': '(.*?)', 'serializedChartProperties'", str(info)).group(1)
    converted =  trimmed.replace("\\/", "/").encode().decode('unicode_escape').replace('\"','\'').replace("true", "True")

    dictionary = ast.literal_eval(converted)

    location = dictionary['options']['title'][20:]
    time = dictionary['options']['subtitle'][-7:]
    percentage = dictionary['dataTable']['rows'][0]['c'][0]['f']
    waiting = dictionary['dataTable']['rows'][0]['c'][1]['f'] 

    return location, time, percentage, waiting


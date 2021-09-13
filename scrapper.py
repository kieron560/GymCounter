import requests
import re
import ast
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

LINK_ELIAS =    "https://docs.google.com/spreadsheets/d/e/2PACX-1vSW5uZLrFwbB16BFBvn7XaIwlsgudMwMmHlqSOs8I5etYAYuek6jgYEQM4cDvhRCDWp5a1ZGLwHLkkn/pubchart?oid=291919261&format=interactive"
LINK_EHUB =     "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKl9d-Qyig483T0HB8Y8C3yKngbXny3uXzjr6YhAPQmtHTGqAHo727SEOHbnOsKNj9c330vaCL3VOU/pubchart?oid=291919261&format=interactive"
LINK_SENGKANG = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRWYdoCbymn2XQahgAIQw5sSGODoWwSaS-c91M-Wdifrmqw1_HvdBC9YryTWRA_Tph2pLkYHt8fDkcV/pubchart?oid=291919261&format=interactive"
LINK_PUNGGOL =  "https://docs.google.com/spreadsheets/d/e/2PACX-1vTi7jd0wZVGfyuQ7Gy5vIM3OBeiv4vpJTVD-1QJfrFUsFkF1BLxV1uQw4zzFOgwDhlvRqnVazIZjxav/pubchart?oid=664793316&format=interactive"
LINK_SKH =      "https://docs.google.com/spreadsheets/d/e/2PACX-1vQeB_x1R71bnIRNJuGFfcHdY4neWPwGhBQsg8yVkI6vADaybcCheMwds3gLRA0JGBRL-MOCr90qqc-_/pubchart?oid=291919261&format=interactive"
LINK = ""

def get_info(choice):
    if choice == 1:
        LINK = LINK_ELIAS
    elif choice == 2:
        LINK = LINK_EHUB
    elif choice == 3:
        LINK = LINK_SKH
    elif choice == 4:
        LINK = LINK_PUNGGOL
    else:
        LINK = LINK_SENGKANG

    r = requests.get(LINK)
    soup = BeautifulSoup(r.content, 'lxml') 
    info = soup.find("script").find_next_sibling()

    # Trim the long script tag to the relevant portions
    trimmed = re.search("'chartJson': '(.*?)', 'serializedChartProperties'", str(info)).group(1)

    # Decoding the script tag, and changing the various words so that Python's ast.literal_eval() function can parse it
    converted =  trimmed.replace("\\/", "/").encode().decode('unicode_escape').replace('\"','\'').replace("true", "True").replace("false", "False").replace("null","None")

    dictionary = ast.literal_eval(converted)

    location = dictionary['options']['title'][20:]
    time = dictionary['options']['subtitle'].replace(" ","")[-7:]

    # Changes 2300HRS to 2300hrs for consistency
    if LINK == LINK_PUNGGOL:
        time = time.lower()

    # Sengkang's script tag code is different for some reason
    if LINK == LINK_SENGKANG:
        percentage = dictionary['dataTable']['rows'][0]['c'][1]['f']
        waiting = dictionary['dataTable']['rows'][1]['c'][1]['f'] 
    else:
        percentage = dictionary['dataTable']['rows'][0]['c'][0]['f']
        waiting = dictionary['dataTable']['rows'][0]['c'][1]['f']

    return location, time, percentage, waiting


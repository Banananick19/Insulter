from parsers.MainParser import Parser
from config import *
import re
import os

def create_cache(lines):
    with open(CACHE, 'a') as file:
        file.write('\n'.join(lines))

def get_cache():
    if os.path.exists(CACHE):
        lines = open(CACHE, 'r').readlines()
        return lines
    else:
        return []

def get_lines():
    prs = Parser(URL)
    try:
        d = prs.get_data(SELECTOR)
    except:
        d = get_cache()

    for index, s in enumerate(d):
        d[index] = re.sub(r'(\<(/?[^>]+)>)', '', str(s))
    create_cache(d)
    return d

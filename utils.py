from parsers.MainParser import Parser
from config import *
import re

def get_lines():
    prs = Parser(URL)
    d = prs.get_data(SELECTOR)
    for index, s in enumerate(d):
        d[index] = re.sub(r'(\<(/?[^>]+)>)', '', str(s))
    return d

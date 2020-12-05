from parsers.MainParser import Parser
from config import *
from utils import *
import re

def get_selector_last(selector):
    point = selector.rfind(' ')
    return selector[point+1:]


def get_lines():
    prs = Parser(URL)
    d = prs.get_data(SELECTOR)
    for index, s in enumerate(d):
        d[index] = re.sub('<\s*(/?)\s*{}>'.format(get_selector_last(SELECTOR)), '', str(s))
    return d

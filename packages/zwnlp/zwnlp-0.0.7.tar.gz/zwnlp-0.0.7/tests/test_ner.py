import pytest
import os
import sys
TEST_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.join(TEST_DIR, '..')
sys.path.insert(0, PARENT_DIR)

from zwutils.config import Config
from zwutils.fileutils import readfile, writefile
from zwnlp.ner import NER
from zwnlp.utils import langcode

def test_zh_ner():
    cfg = Config('conf/zwnlp.json', default={
        'corenlp': {
            'memsize': '4G',
            'timeout': 30000
        }
    })
    with NER(cfg=cfg, lang='zh') as ner:
        s = readfile('data/上海证券报.html')
        r = ner.htmloutput(s)
    writefile('test_zh_ner.html', r)

def test_en_ner():
    cfg = Config('conf/zwnlp.json')
    with NER(cfg=cfg, lang='en') as ner:
        s = readfile('data/FoxNews.html')
        r = ner.htmloutput(s)
    writefile('test_en_ner.html', r)    

if __name__=='__main__':
    test_en_ner()
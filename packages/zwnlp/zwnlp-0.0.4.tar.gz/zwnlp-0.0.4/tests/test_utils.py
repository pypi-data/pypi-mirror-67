import pytest
from zwutils.fileutils import readfile
from zwnlp import utils

def test_temp_html_clean():
    s = readfile('data/上海证券报.html')
    s = utils.temp_html_clean(s)
    assert 1

def test_langid():
    zh = utils.langcode('这是中文')
    en = utils.langcode('this is english')
    assert zh == 'zh' and en == 'en'

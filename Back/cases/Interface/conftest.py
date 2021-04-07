# -*- coding: utf-8 -*-

from . import *


@pytest.fixture(scope='module', autouse=True)
def train():
    ret = root_path
    print("++++++++++++++++++++++++++++++++++++")
    print(f'In {__file__}, {ret}')
    print("++++++++++++++++++++++++++++++++++++")

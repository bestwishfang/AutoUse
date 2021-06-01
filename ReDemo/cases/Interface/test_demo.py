# -*- coding: utf-8 -*-

from . import *


@pytest.fixture()
def myfixture():
    print("执行myfixture")


class TestDemo:

    def test_one(self):
        print("执行test_one")
        assert 1 + 1 == 3

    def test_two(self, myfixture):
        print("执行test_two")
        assert 1 == 1

    def test_three(self):
        print("执行test_three")
        assert 1 + 1 == 2

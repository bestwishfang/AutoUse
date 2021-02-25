from . import *


@pytest.fixture
def setup_teardown():
    print(f"=================Test Begin=================")
    print(f'{__file__}')
    yield
    print(f"=================Test End=================")


def test_one():
    print('test_one')
    print(base.BASE_DIR)
    # assert 1 is None


def test_again(setup_teardown):
    print('test_again')
    print(base.BASE_DIR)
    # assert 1 is None

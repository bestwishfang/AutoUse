from . import *


@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print(f"=================Test Begin=================")

    yield
    print(f"=================Test End=================")


def test_begin():
    print('test_next')
    print(base.BASE_DIR)
    # assert 1 is None

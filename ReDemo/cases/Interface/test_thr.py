from . import *


@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print(f"=================Test Begin=================")
    print(f'{__file__}')
    yield
    print(f"=================Test End=================")


def test_thr():
    print('test_thr')
    print(base.BASE_DIR)


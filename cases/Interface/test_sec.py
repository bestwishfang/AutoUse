from . import *


@pytest.fixture(scope='function', autouse=True)
def setup_teardown():
    print(f"=================Test Begin=================")

    yield
    print(f"=================Test End=================")


def test_sec():
    print('test_sec')
    print(base.BASE_DIR)


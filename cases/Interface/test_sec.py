from . import *


@pytest.fixture
def setup_teardown():
    print(f"=================Test Begin=================")
    print(f'{__file__}')
    yield
    print(f"=================Test End=================")


def test_sec(setup_teardown):
    print('test_sec')
    print(base.BASE_DIR)


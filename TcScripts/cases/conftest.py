# -*- coding: utf-8 -*-


from . import *


def pytest_addoption(parser):
    parser.addoption(
        "--testbed", action="store", default="../config/exp.yaml", help="my option: test exp yaml"
    )


@pytest.fixture(scope='session', autouse=True)
def tear_set_up_down(request):
    print('========================= test set up =========================')
    testbed = request.config.getoption("--testbed")
    print(f'test bed: {testbed}')
    exp_args = parse_yaml.ExpArgs()
    exp_args.parse_yaml_args(yaml_path=testbed)
    print(f'server_ip: {exp_args.system.server_ip}')

    data = {
        'exp_args': exp_args,
    }
    yield data
    print('OK')
    print('======================== test set down =========================')

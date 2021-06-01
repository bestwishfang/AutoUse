# -*- coding: utf-8 -*-
import os
from .conftest import tear_set_up_down


def test_xyz_timing(tear_set_up_down):
    print('In test xyz timing')
    data = tear_set_up_down
    exp_args = data.get('exp_args')
    print(f'server_ip: {exp_args.system.server_ip}')

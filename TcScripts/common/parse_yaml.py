# -*- coding: utf-8 -*-

"""
__date:         2021/04/16
__author:       ssfang
__corporation:  OriginQuantum
__usage:

"""

import os

import yaml
import numpy as np

from .base import qarange

config_path = os.path.dirname(os.path.dirname(__file__)) + '/config'


class Bunch(object):
    def __init__(self, data: dict = None):
        if data:
            self.__dict__.update(data)


class ExpArgs(object):
    """
    Parse yaml file, like `config/exp.yaml`.
    """

    def __init__(self):
        self.system = None
        self.flows = None
        self.experiments = None
        self.parameter = None

    def parse_yaml_args(self, yaml_path=None):
        """
        Parse yaml config info.
        Args:
            yaml_path: yaml file path, default `config/exp.yaml`

        Returns:
            exp_args: ExpArgs object
        """
        if not yaml_path:
            yaml_path = '{}/exp.yaml'.format(config_path)
        with open(yaml_path, mode='r', encoding='utf-8') as fp:
            data = yaml.safe_load(fp)

        self.__dict__.update(data)
        self._change_key_to_attr(self)

    def _change_key_to_attr(self, obj):
        """
        If obj.attr value is dict, change the value key to an attribute.
        Recursion operate.
        Args:
            obj: an object

        """
        except_list = [
            'flows',
            'scan_flux',
            'repeat_loops',
        ]
        for attr in dir(obj):
            if not attr.startswith('_'):
                value = getattr(obj, attr)
                if isinstance(value, dict):
                    setattr(obj, attr, Bunch(value))
                    new_obj = getattr(obj, attr)
                    self._change_key_to_attr(new_obj)
                elif isinstance(value, list) and attr not in except_list:

                    if len(value) == 3:
                        start, end, step = value
                        if isinstance(start, str):
                            start, end, step = eval(start), eval(end), eval(step)
                        if end - start > step:
                            new_value = qarange(start, end, step)
                            setattr(obj, attr, new_value)
                    elif len(value) == 2:
                        a, b = value
                        if isinstance(a, str):
                            new_value = [eval(a), eval(b)]
                            setattr(obj, attr, new_value)

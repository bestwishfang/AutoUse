# -*- coding: utf-8 -*-
from decimal import Decimal

import numpy as np


def qarange(start, end, step):
    """
    Convert the cyclic measurement and control data into the required array
    :param start:
    :param end:
    :param step:
    :return: np.array
    """
    if Decimal(str(end)) - Decimal(str(start)) < Decimal(str(step)) or step == 0:
        return [start]
    start_decimal = str(start)[::-1].find('.')
    step_decimal = str(step)[::-1].find('.')
    data_decimal = max([step_decimal, start_decimal])
    if data_decimal == -1:
        data_decimal = 0
    data_number = int((Decimal(str(end)) - Decimal(str(start))) / Decimal(str(step)))
    end_data = round(start + data_number * step, data_decimal)
    data_np = np.linspace(start, end_data, data_number + 1)
    data_list = [round(data, data_decimal) for data in data_np]
    return data_list

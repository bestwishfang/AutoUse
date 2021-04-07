import sys
import os
import pytest

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if root_path not in sys.path:
    sys.path.append(root_path)

from common import base


# common_path = os.path.join(os.getcwd(), r'../../common')
#
# print(common_path)
# if common_path not in sys.path:
#     sys.path.append(common_path)
#
# import base

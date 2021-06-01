# -*- coding: utf-8 -*-


import os
import sys
import warnings

warnings.filterwarnings("ignore")
base_dir = os.path.dirname(os.path.dirname(os.getcwd()))

if base_dir not in sys.path:
    sys.path.append(base_dir)

import pytest
from TCScripts.common import parse_yaml

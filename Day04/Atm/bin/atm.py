__author__ = "Alex Li"

import os
import sys
from conf import settings
from core import main

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

main.login()

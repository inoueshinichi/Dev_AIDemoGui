"""共通ライブラリ
"""

import os
import sys
import time
import datetime as dt
import re
import math
import glob
import pathlib
import shutil
import ctypes
import platform
import abc
import functools
import inspect
import threading
import copy
import json
import csv
import pprint

from collections import (
    deque,
    Counter,
    defaultdict,
    OrderedDict,
    ChainMap,
)

import numpy as np
np.set_printoptions(suppress=True) # 指数表記を禁止

import scipy as sp
import cv2
import PIL
import pandas as pd
import tqdm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import qimage2ndarray as qn;
import openpyxl
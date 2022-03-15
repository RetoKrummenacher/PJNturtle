# This is to import methods from the package

from pjnturtle.turtle import *

import os, sys
fpath = os.path.join(os.path.dirname(__file__), 'common')
sys.path.append(fpath)

from point import *
from utils import *
from penstate import *
from color import *
from colordict import *

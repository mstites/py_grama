from .base import *
from .count import *
from .group import *
from .join import *
from .mask_helpers import *

for verb in dir():
    if "ize" in verb:
        exec(verb.replace("ize", "ise") + "=" + verb)

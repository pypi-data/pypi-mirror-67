import sys
import typing
from . import ops
from . import types
from . import props
from . import utils
from . import context
from . import app
from . import path

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''

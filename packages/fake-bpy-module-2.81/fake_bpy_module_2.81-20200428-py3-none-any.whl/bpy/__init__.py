import sys
import typing
from . import types
from . import app
from . import ops
from . import utils
from . import path
from . import context
from . import props

context: 'types.Context' = None

data: 'types.BlendData' = None
'''Access to Blenders internal data '''

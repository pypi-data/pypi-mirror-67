"""Write me."""

__version__ = "1.0.post1"

from . import core
from . import ode
from . import utils

try:
    import modelbase_pde as pde
except ImportError:
    pass

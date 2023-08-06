from .__about__ import *

from . import lib
from .geo import GeoSet, getGeoSet
from .config import *
from . import core
from .core import is_w7x_instance, get_server, get_ws_class, run_service
from . import transcodings
from . import flt, vmec, extender, batch
from .flt import MagneticConfig, Machine, Points3D
from . import evaluation
from .plotting.poincare import plot_poincare_surfaces, plot_poincare_geometries
from .plotting.tile_loads import plot_tile_loads
from .plotting.vmec import plot_fourier

def switch_offline():
    """Allows loading old results without calling the web-service."""
    core.get_ws_class = lambda x, y: type(None)

import pkg_resources

from rockart.canvas import Canvas
from rockart.exceptions import RockartException


__all__ = [Canvas.__name__, RockartException.__name__]

try:
    __version__ = pkg_resources.get_distribution("rockart").version
except pkg_resources.DistributionNotFound:
    pass

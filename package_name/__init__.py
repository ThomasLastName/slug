__version__ = "1.1.0"

from pkg_resources import get_distribution, DistributionNotFound
__version__ = get_distribution('package_name').version

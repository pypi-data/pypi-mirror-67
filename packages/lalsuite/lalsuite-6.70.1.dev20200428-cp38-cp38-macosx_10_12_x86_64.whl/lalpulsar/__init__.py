# Import SWIG wrappings, if available
from .lalpulsar import *

__version__ = "1.18.2.1"

## \addtogroup lalpulsar_python
"""This package provides Python wrappings and extensions to LALPulsar"""



#
# This section was added automatically to support using LALSuite as a wheel.
#
import os
import pkg_resources
new_path = pkg_resources.resource_filename('lalapps', 'data')
path = os.environ.get('LAL_DATA_PATH')
path = path.split(':') if path else []
if new_path not in path:
    path.append(new_path)
os.environ['LAL_DATA_PATH'] = ':'.join(path)

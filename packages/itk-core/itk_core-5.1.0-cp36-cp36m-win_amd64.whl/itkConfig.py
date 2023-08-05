#==========================================================================
#
#   Copyright NumFOCUS
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0.txt
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#==========================================================================*/

"""Insight Toolkit (itk) configuration module.

This module contains user options and paths to libraries and language support
files used internally.

User options can be set by importing itkConfig and changing the option values.

Currently-supported options are:
  DebugLevel: must be one of SILENT, WARN, or ERROR (these values are defined
    in itkConfig). Default is WARN.
  ImportCallback: importing itk libraries can take a while. ImportCallback will
    be called when each new library is imported in the import process.
    ImportCallback must be a function that takes two parameters: the name of
    the library being imported, and a float (between 0 and 1) reflecting the
    fraction of the import that is completed.
  LazyLoading: Only load an itk library when needed. Before the library is
    loaded, the namespace will be inhabited with dummy objects."""


# User options
SILENT = 0; WARN = 1; ERROR = 2
DebugLevel = WARN
ImportCallback = None
ProgressCallback = None
LazyLoading = True
NotInPlace = False



# Internal settings

import warnings
def itkFormatWarning(msg, *a, **kwa):
    """"Format the warnings issued by itk to display only the message.

    This will ignore the filename and the linenumber where the warning was
    triggered. The message is returned to the warnings module.
    """

    return str(msg) + '\n'

# Redefine the format of the warnings
warnings.formatwarning = itkFormatWarning


import os
def normalized_path(relative_posix_path):
    if relative_posix_path != 'None':
        file_dir = os.path.split(__file__)[0]
        relative_path = relative_posix_path.replace('/', os.sep)
        return os.path.normpath(os.path.join(file_dir, relative_path))

# swig_lib: location of the swig-generated shared libraries
swig_lib = normalized_path('../lib')

# swig_py: location of the xxxPython.py swig-generated python interfaces
swig_py = normalized_path('../lib')

# config_py: location of xxxConfix.py CMake-generated library descriptions
config_py = normalized_path('itk/Configuration')

# put the itkConfig.py path in the path list
path = [os.path.join(config_py, '..')]
# also populate path with the WRAPITK_PYTHON_PATH var
if 'WRAPITK_PYTHON_PATH' in os.environ:
  path.extend(os.environ['WRAPITK_PYTHON_PATH'].split(':'))

doxygen_root = normalized_path('../Doc')

del normalized_path
del os

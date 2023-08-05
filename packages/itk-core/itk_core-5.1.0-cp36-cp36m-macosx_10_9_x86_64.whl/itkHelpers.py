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

import re
import functools

_HAVE_XARRAY = False
try:
    import xarray as xr
    _HAVE_XARRAY = True
except ImportError:
    pass

def camel_to_snake_case(name):
    snake = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    snake = re.sub('([a-z0-9])([A-Z])', r'\1_\2', snake)
    return snake.replace('__', '_').lower()

def is_arraylike(arr):
    return hasattr(arr, 'shape') and \
    hasattr(arr, 'dtype') and \
    hasattr(arr, '__array__') and \
    hasattr(arr, 'ndim')

def accept_numpy_array_like_xarray(image_filter):
    """Decorator that allows itk.ProcessObject snake_case functions to accept
    NumPy array-like or xarray DataArray inputs for itk.Image inputs. If a NumPy array-like is
    passed as an input, output itk.Image's are converted to numpy.ndarray's. If a xarray DataArray is
    passed as an input, output itk.Image's are converted to xarray.DataArray's."""
    import numpy as np
    import itk

    @functools.wraps(image_filter)
    def image_filter_wrapper(*args, **kwargs):
        have_array_input = False
        have_xarray_input = False

        args_list = list(args)
        for index, arg in enumerate(args):
            if _HAVE_XARRAY and isinstance(arg, xr.DataArray):
                    have_xarray_input = True
                    image = itk.image_from_xarray(arg)
                    args_list[index] = image
            elif not isinstance(arg, itk.Object) and is_arraylike(arg):
                have_array_input = True
                array = np.asarray(arg)
                image = itk.image_view_from_array(array)
                args_list[index] = image

        potential_image_input_kwargs = ('input', 'input1', 'input2', 'input3')
        for key, value in kwargs.items():
            if (key.lower() in potential_image_input_kwargs or "image" in key.lower()):
                if _HAVE_XARRAY and isinstance(value, xr.DataArray):
                    have_xarray_input = True
                    image = itk.image_from_xarray(value)
                    kwargs[key] = image
                elif not isinstance(value, itk.Object) and is_arraylike(value):
                    have_array_input = True
                    array = np.asarray(value)
                    image = itk.image_view_from_array(array)
                    kwargs[key] = image

        if have_xarray_input or have_array_input:
            # Convert output itk.Image's to numpy.ndarray's
            output = image_filter(*tuple(args_list), **kwargs)
            if isinstance(output, tuple):
                output_list = list(output)
                for index, value in output_list:
                    if isinstance(value, itk.Image):
                        if have_xarray_input:
                            data_array = itk.xarray_from_image(value)
                            output_list[index] = data_array
                        else:
                            array = itk.array_view_from_image(value)
                            output_list[index] = array
                return tuple(output_list)
            else:
                if isinstance(output, itk.Image):
                    if have_xarray_input:
                        output = itk.xarray_from_image(output)
                    else:
                        output = itk.array_view_from_image(output)
                return output
        else:
            return image_filter(*args, **kwargs)
    return image_filter_wrapper

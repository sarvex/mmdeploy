# Copyright (c) OpenMMLab. All rights reserved.
import importlib

from mmdeploy.utils import Codebase


def get_library_version(lib):
    """Try to get the version of a library if it has been installed.

    Args:
        lib (str): The name of library.

    Returns:
        None | str: If the library has been installed, return version.
    """
    try:
        lib = importlib.import_module(lib)
        version = lib.__version__ if hasattr(lib, '__version__') else None
    except Exception:
        version = None

    return version


def get_codebase_version():
    """Get the version dictionary of all supported codebases.

    Returns:
        Dict: The name and the version of supported codebases.
    """
    version_dict = {}
    for enum in Codebase:
        codebase = enum.value
        version_dict[codebase] = get_library_version(codebase)
    return version_dict


def get_backend_version():
    """Get the version dictionary of some supported backend.

    Returns:
        Dict: The name and the version of some supported backend.
    """
    backend_library_list = ['tensorrt', 'onnxruntime', 'ncnn', 'tvm']
    return {
        backend: get_library_version(backend)
        for backend in backend_library_list
    }

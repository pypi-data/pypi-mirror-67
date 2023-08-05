import poetry_version

from .auth import NNDAuth

__version__ = poetry_version.extract(source_file=__file__)

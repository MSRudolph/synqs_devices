"""Check python version"""
import sys

if sys.version_info < (3, 6):
    raise RuntimeError("MakoCamera strongly prefers Python 3.6+")

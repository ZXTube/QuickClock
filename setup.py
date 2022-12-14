# This script is only used to turn the main.py script into a windows executable, by running `python setup.py build`

from cx_Freeze import setup, Executable
import pkgutil

files = []
includes = ["encodings", "collections", "importlib", "pygame", "time"]
excludes = [i.name for i in list(pkgutil.iter_modules()) if i.ispkg and i.name not in includes]

target = Executable(
    target_name="QuickClock.exe",
    script="main.py",
    base="Win32GUI"
)
setup(
    name="QuickClock",
    version="1.0",
    author="ZiyadCodes, https://ziyadcodes.000webhostapp.com",
    executables=[target],
    options={"build_exe": {"include_files": files, "excludes": excludes, "optimize": 2}},  # Try optimize 2 first
    description="QuickClock"
)

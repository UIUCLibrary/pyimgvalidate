import os
# import sys
from setuptools.config import read_configuration
import cx_Freeze
import pytest

def get_project_metadata():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), "setup.cfg"))
    return read_configuration(path)["metadata"]
# import imgvalidator
import platform
metadata = get_project_metadata()

def create_msi_tablename(python_name, fullname):
    shortname = python_name[:6].replace("_", "").upper()
    longname = fullname
    return "{}|{}".format(shortname, longname)


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
MSVC = os.path.join(PYTHON_INSTALL_DIR, 'vcruntime140.dll')


def get_tests():
    root = "tests"
    test_files = []
    for x in filter(lambda x: x.is_file and os.path.splitext(x.name)[1] == ".py", os.scandir(root)):
        test_files.append(os.path.join(root, x.name))
    print("Found files {}".format(", ".join(test_files)))
    return test_files


INCLUDE_FILES = [
    "documentation.url",
] + get_tests()

directory_table = [
    (
        "ProgramMenuFolder",  # Directory
        "TARGETDIR",  # Directory_parent
        "PMenu|Programs",  # DefaultDir
    ),
    (
        "PMenu",  # Directory
        "ProgramMenuFolder",  # Directory_parent
        create_msi_tablename(metadata["name"], metadata["name"])
    ),
]
shortcut_table = [
    (
        "startmenuShortcutDoc",  # Shortcut
        "PMenu",  # Directory_
        "{} Documentation".format(create_msi_tablename(metadata["name"], metadata["name"])),
        "TARGETDIR",  # Component_
        "[TARGETDIR]documentation.url",  # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        'TARGETDIR'  # WkDir
    ),
]

if os.path.exists(MSVC):
    INCLUDE_FILES.append(MSVC)

build_exe_options = {
    "includes":        pytest.freeze_includes(),
    "include_msvcr": True,
    "packages": [
        "os",
        'pytest',
        "packaging",
        "six",
        "appdirs",
        # # "tests",
        "imgvalidator"
    ],
    "excludes": ["tkinter"],
    "include_files": INCLUDE_FILES,

}

target_name = 'imgvalidator.exe' if platform.system() == "Windows" else 'imgvalidator'
cx_Freeze.setup(
    name=metadata["name"],
    description=metadata["description"],
    license="University of Illinois/NCSA Open Source License",
    version=metadata["version"],
    author=metadata["author"],
    author_email=metadata["author_email"],
    options={
        "build_exe": build_exe_options,
        "bdist_msi": {
            "upgrade_code": "39B7662E-8A18-447C-8FA3-E4FE377BAB2F",
            "data": {
                "Shortcut": shortcut_table,
                "Directory": directory_table
            },

        }
    },
    executables=[cx_Freeze.Executable("imgvalidator/__main__.py",
                            targetName=target_name, base="Console")],

)

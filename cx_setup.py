import os
import sys
import cx_Freeze
import pytest
import imgvalidator
import platform

metadata_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'imgvalidator', '__version__.py')
metadata = dict()
with open(metadata_file, 'r', encoding='utf-8') as f:
    exec(f.read(), metadata)

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
        create_msi_tablename(metadata["__title__"], metadata["FULL_TITLE"])
    ),
]
shortcut_table = [
    (
        "startmenuShortcutDoc",  # Shortcut
        "PMenu",  # Directory_
        "{} Documentation".format(create_msi_tablename(metadata["__title__"], metadata["FULL_TITLE"])),
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
    name=metadata["FULL_TITLE"],
    description=metadata["__description__"],
    license="University of Illinois/NCSA Open Source License",
    version=metadata["__version__"],
    author=metadata["__author__"],
    author_email=metadata["__author_email__"],
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

# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5

from py2exe import freeze
import os
import shutil

if os.path.exists("dist"):
    shutil.rmtree("dist")

build_exe_option = {
    "excludes" : [],
    "compressed" : 1,
    "optimize" : 1,
    "bundle_files" : 3,
}

freeze(
    options = build_exe_option,
    console= [
        {"script" : "SerialCommandTool.py"}
    ],
    zipfile=None,
    version_info={
        "version" : "0.0.0",
        "product_name" : "SerialCommandTool",
        "copyright" : "(C) 2024 yumekasa5"
    }
)

# shutil.copytree("Settings", "dist/Settings")
# shutil.copytree("LICENSES", "dist/LICENSES")
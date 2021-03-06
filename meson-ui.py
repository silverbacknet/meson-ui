#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.mesonuimain import mesonui_main
from pathlib import Path
import sys


# If we run uninstalled, add the script directory to sys.path to ensure that
# we always import the correct mesonui modules even if PYTHON_PATH is mangled
mesonui_exe = Path(sys.argv[0]).resolve()
if (mesonui_exe.parent / 'mesonui').is_dir():
    sys.path.insert(0, str(mesonui_exe.parent))


if __name__ == "__main__":
    sys.exit(mesonui_main())

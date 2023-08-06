
#!/bin/bash
cd $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PYTHON=/usr/local/Cellar/python/3.7.5/Frameworks/Python.framework/Versions/3.7/bin/python3.7
export PYTHONPATH=$(${PYTHON} -c "import sys;print(sys.path)"):${PYTHONPATH}
export DYLD_LIBRARY_PATH=$(${PYTHON} -c "import os,sysconfig;print(os.path.realpath(sysconfig.get_config_var('LIBDIR')))"):${DYLD_LIBRARY_PATH}
Qt5_DIR=$(pwd)/bin/qt QT_PLUGIN_PATH=${Qt5_DIR}/plugins bin/visusviewer.app/Contents/MacOS/visusviewer "$@"

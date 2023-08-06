
#!/bin/bash
cd $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PYTHON=/usr/local/opt/python@3.8/bin/python3.8
export PYTHONPATH=$(${PYTHON} -c "import sys;print(sys.path)"):${PYTHONPATH}
export DYLD_LIBRARY_PATH=$(${PYTHON} -c "import os,sysconfig;print(os.path.realpath(sysconfig.get_config_var('LIBDIR')))"):${DYLD_LIBRARY_PATH}
Qt5_DIR=$(pwd)/bin/qt QT_PLUGIN_PATH=${Qt5_DIR}/plugins bin/visusviewer.app/Contents/MacOS/visusviewer "$@"

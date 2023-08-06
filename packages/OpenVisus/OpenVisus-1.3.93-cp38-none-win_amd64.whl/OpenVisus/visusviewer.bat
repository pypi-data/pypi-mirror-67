
cd %~dp0
set PYTHON=C:\Python38-x64\python.exe
set PATH=%PYTHON%\..;%PATH%;.\bin 
set Qt5_DIR=bin\Qt
set PATH=%Qt5_DIR%\bin;%PATH%
set QT_PLUGIN_PATH=%Qt5_DIR%\plugins
"bin\visusviewer.exe" %*

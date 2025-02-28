@echo off
if "%~1"=="-minimized" goto :start
start /min cmd /c "%~f0" -minimized
exit
:start

python main.py

powershell.exe -command ^ "& {set-executionpolicy Remotesigned -Scope Process; .'.\wifi.ps1' }"
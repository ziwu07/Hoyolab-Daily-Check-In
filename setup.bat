PowerShell.exe -ExecutionPolicy Bypass -File script.ps1
set "currentDir=%CD%"
"%currentDir%\venv\Script\python.exe" "%currentDir%\scheduler.py"
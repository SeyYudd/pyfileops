@echo off
REM Upgrade pip and install requirements from this folder
python -m pip install --upgrade pip
python -m pip install -r "%~dp0requirements.txt"
echo.
echo Requirements installation complete.
exit /b 0

@echo off
REM Simple runner for Windows
python --version >NUL 2>&1
IF ERRORLEVEL 1 (
  echo Python is not installed or not on PATH.
  echo Please install Python 3.10+ from https://www.python.org/downloads/
  pause
  exit /b 1
)
python src\near_miss.py
pause

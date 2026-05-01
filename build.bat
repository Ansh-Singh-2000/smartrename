@echo off
echo ========================================
echo Building Smart Rename Executable
echo ========================================
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
    echo.
)

echo Building executable...
pyinstaller --onefile --name SmartRename --icon=icon.ico --clean smart_rename.py

if errorlevel 1 (
    echo.
    echo ❌ Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✓ Build successful!
echo ========================================
echo.
echo Executable location: dist\SmartRename.exe
echo.
echo You can now:
echo 1. Copy SmartRename.exe to any folder
echo 2. Run SmartRename.exe in that folder
echo 3. Enter your GROQ_API_KEY on first run
echo.
pause

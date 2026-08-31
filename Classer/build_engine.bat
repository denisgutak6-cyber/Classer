@echo off
setlocal enabledelayedexpansion

cd /d "%~dp0"

echo [0/4] Updating ENGINE_BUILD...

set "FILE=Engine\INFO\INFVal.py"

if not exist "%FILE%" (
    echo ERROR: File not found: %FILE%
    echo Current directory: %CD%
    pause
    exit /b 1
)

for /f "tokens=1,2 delims==" %%A in ('findstr /b "ENGINE_BUILD" "%FILE%"') do (
    set /a NEW_BUILD=%%B+1
)

if not defined NEW_BUILD (
    echo ERROR: ENGINE_BUILD not found in %FILE%
    pause
    exit /b 1
)

powershell -NoProfile -Command "(Get-Content '%FILE%') -replace '^ENGINE_BUILD\s*=.*$', 'ENGINE_BUILD = %NEW_BUILD%' | Set-Content '%FILE%'"

echo ENGINE_BUILD updated to !NEW_BUILD!

echo [1/4] Compiling Engine via Nuitka...
python -m nuitka --module Engine --include-package=Engine --unstripped

if errorlevel 1 (
    echo ERROR: Nuitka compilation failed!
    pause
    exit /b 1
)

echo [2/4] Preparing Dist folder...
if not exist Dist mkdir Dist

echo [3/4] Renaming and moving .pyd and .pdb files...
if exist Dist\Engine.pyd del /q Dist\Engine.pyd
if exist Dist\Engine.pdb del /q Dist\Engine.pdb

for %%f in (Engine.*.pyd) do (
    move "%%f" "Dist\Engine.pyd" >nul
)

if exist Engine.pdb (
    move "Engine.pdb" "Dist\Engine.pdb" >nul
) else if exist Engine.build (
    for /r Engine.build %%g in (Engine.pdb) do (
        if exist "%%g" move "%%g" "Dist\Engine.pdb" >nul
    )
)

echo [4/4] Cleaning up build artifacts...
if exist Engine.build (
    del /s /q Engine.build\*.obj >nul 2>&1
)
if exist *.pyi del /s /q *.pyi >nul 2>&1

echo ==========================================
echo  ConsoleSTDIO (Engine.pyd + Engine.pdb) successfully built!
echo  ENGINE_BUILD = !NEW_BUILD!
echo ==========================================
pause

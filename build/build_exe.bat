@echo off
REM FastCut - Windows exe derleme script'i
REM Bu dosya Windows uzerinde, Python ve pip kurulu bir makinede calistirilmalidir.

setlocal
cd /d "%~dp0\.."

echo [1/3] Bagimliliklar kuruluyor...
pip install -r requirements.txt
if errorlevel 1 goto :error

echo [2/3] Eski build/dist klasorleri temizleniyor...
if exist "build\pyinstaller" rmdir /s /q "build\pyinstaller"
if exist "build\FastCut.spec" del /q "build\FastCut.spec"
if exist "dist" rmdir /s /q "dist"

echo [3/3] PyInstaller ile FastCut.exe derleniyor...
pyinstaller --noconfirm --onefile --windowed ^
    --icon "%~dp0..\icon.ico" ^
    --name "FastCut" ^
    --distpath "dist" ^
    --workpath "build\pyinstaller" ^
    --specpath "build" ^
    "main.pyw"
if errorlevel 1 goto :error

echo.
echo Basarili! Cikti dosyasi: dist\FastCut.exe
goto :eof

:error
echo.
echo HATA: Derleme basarisiz oldu. Yukaridaki mesaji kontrol edin.
exit /b 1

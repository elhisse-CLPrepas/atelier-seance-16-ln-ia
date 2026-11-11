@echo off
setlocal
chcp 65001 >nul
pushd "%~dp0guide\ressources"
if errorlevel 1 exit /b 1
py -3 -X utf8 demonstration-s16.py
set "demo_status=%errorlevel%"
if not "%demo_status%"=="0" echo Execution interrompue. Lire le message ci-dessus.
if "%demo_status%"=="0" echo Demonstration terminee. Resultat dans dossier-demo-s16\04-communication.
pause
popd
exit /b %demo_status%

@ECHO OFF
SET var=%cd%
set DIR=%var%
pyinstaller .\utils\screencapturer\main.py --noconfirm --onefile 
pause
exit


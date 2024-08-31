@echo off
setlocal

set NODE_URL=https://nodejs.org/dist/v18.18.1/node-v18.18.1-x64.msi

set INSTALLER=nodejs_installer.msi

echo Downloading Node.js installer...
powershell -Command "Invoke-WebRequest -Uri %NODE_URL% -OutFile %INSTALLER%"

if not exist %INSTALLER% (
    echo Failed to download Node.js installer.
    exit /b 1
)

echo Installing Node.js...
msiexec /i %INSTALLER% /quiet /norestart

del %INSTALLER%

echo Node.js installation completed.
endlocal
pause
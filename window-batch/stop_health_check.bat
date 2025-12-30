@echo off
chcp 65001 > nul
REM ===================================================
REM 서버 헬스체크 프로그램 종료 스크립트
REM ===================================================

echo.
echo ===================================================
echo 서버 헬스체크 프로그램 종료
echo ===================================================
echo.
echo 실행 중인 health-check.py 프로세스를 찾는 중...
echo.

REM health-check.py를 실행 중인 python 프로세스 종료
for /f "tokens=2" %%a in ('tasklist /FI "IMAGENAME eq python.exe" /FO LIST ^| find "PID:"') do (
    wmic process where "ProcessId=%%a" get CommandLine 2>nul | find "health-check.py" >nul
    if not errorlevel 1 (
        echo 프로세스 %%a 종료 중...
        taskkill /PID %%a /F
    )
)

REM pythonw.exe도 확인
for /f "tokens=2" %%a in ('tasklist /FI "IMAGENAME eq pythonw.exe" /FO LIST ^| find "PID:"') do (
    wmic process where "ProcessId=%%a" get CommandLine 2>nul | find "health-check.py" >nul
    if not errorlevel 1 (
        echo 프로세스 %%a 종료 중...
        taskkill /PID %%a /F
    )
)

echo.
echo 종료 완료!
echo.
pause


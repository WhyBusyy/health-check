@echo off
chcp 65001 > nul
REM ===================================================
REM 서버 헬스체크 프로그램 백그라운드 실행 스크립트
REM 콘솔 창 없이 백그라운드에서 실행됩니다
REM ===================================================

REM ========== 설정 영역 (여기를 수정하세요) ==========
SET API_URL=http://localhost:3000/api/health
SET CHECK_INTERVAL=10
SET TIMEOUT=5
SET ALERT_MESSAGE=A서버가 다운되었습니다
REM ==================================================

echo.
echo ===================================================
echo 서버 헬스체크 프로그램을 백그라운드에서 시작합니다
echo ===================================================
echo API URL: %API_URL%
echo 체크 간격: %CHECK_INTERVAL%초
echo 알림 메시지: %ALERT_MESSAGE%
echo ===================================================
echo.
echo 프로그램이 백그라운드에서 실행됩니다.
echo 종료하려면 작업 관리자에서 python.exe 프로세스를 종료하세요.
echo.
echo 3초 후 이 창은 자동으로 닫힙니다...
timeout /t 3 > nul

REM 백그라운드에서 Python 실행 (로그 파일 생성)
start /B pythonw health-check.py --url %API_URL% --interval %CHECK_INTERVAL% --timeout %TIMEOUT% --alert "%ALERT_MESSAGE%"

exit


@echo off
chcp 65001 > nul
REM ===================================================
REM 서버 헬스체크 프로그램 자동 실행 스크립트
REM ===================================================

REM 스크립트 디렉토리로 이동
cd /d "%~dp0.."

REM ========== 설정 영역 (여기를 수정하세요) ==========
SET API_URL=http://localhost:3000/api/health
SET CHECK_INTERVAL=10
SET TIMEOUT=5
SET ALERT_MESSAGE=A서버가 다운되었습니다
SET VERBOSE=
REM VERBOSE 모드를 사용하려면: SET VERBOSE=--verbose
REM ==================================================

echo.
echo ===================================================
echo 서버 헬스체크 프로그램 시작
echo ===================================================
echo API URL: %API_URL%
echo 체크 간격: %CHECK_INTERVAL%초
echo 알림 메시지: %ALERT_MESSAGE%
echo ===================================================
echo.
echo 프로그램이 실행 중입니다...
echo 종료하려면 이 창을 닫거나 Ctrl+C를 누르세요.
echo.

REM Python 실행
python health-check.py --url %API_URL% --interval %CHECK_INTERVAL% --timeout %TIMEOUT% --alert "%ALERT_MESSAGE%" %VERBOSE%

pause


#!/usr/bin/env python3
"""
서버 헬스체크 프로그램
10초마다 API에 헬스체크 요청을 보내고, 응답이 없으면 소리 알림
"""

import requests
import time
import winsound  # Windows 전용 소리 모듈
from datetime import datetime
import sys

# 설정
API_URL = "http://localhost:3000/api/health"  # 헬스체크 API URL 변경 필요
CHECK_INTERVAL = 10  # 10초
TIMEOUT = 5  # 타임아웃 5초
BEEP_FREQUENCY = 1000  # 비프음 주파수 (Hz)
BEEP_DURATION = 500  # 비프음 지속 시간 (ms)

def beep_alert():
    """소리 알림"""
    try:
        # Windows 비프음 (주파수, 지속시간)
        winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
        print("🔔 알림 소리 재생")
    except Exception as e:
        print(f"⚠️ 소리 재생 실패: {e}")

def check_health():
    """헬스체크 실행"""
    try:
        response = requests.get(API_URL, timeout=TIMEOUT)
        if response.status_code == 200:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.Timeout:
        return False, "TIMEOUT"
    except requests.exceptions.ConnectionError:
        return False, "CONNECTION_ERROR"
    except Exception as e:
        return False, str(e)

def main():
    """메인 함수"""
    print("=" * 50)
    print("서버 헬스체크 프로그램 시작")
    print(f"API URL: {API_URL}")
    print(f"체크 간격: {CHECK_INTERVAL}초")
    print("=" * 50)
    print()

    consecutive_failures = 0

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            is_healthy, status = check_health()

            if is_healthy:
                consecutive_failures = 0
                print(f"[{timestamp}] ✅ 정상 - Status: {status}")
            else:
                consecutive_failures += 1
                print(f"[{timestamp}] ❌ 실패 - Status: {status} (연속 실패: {consecutive_failures}회)")
                
                # 응답이 없으면 소리 알림
                beep_alert()
                print(f"⚠️ 서버 응답 없음! 연속 {consecutive_failures}회 실패")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n\n프로그램 종료")
        sys.exit(0)

if __name__ == "__main__":
    main()


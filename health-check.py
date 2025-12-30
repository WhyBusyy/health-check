#!/usr/bin/env python3
"""
서버 헬스체크 프로그램
10초마다 API에 헬스체크 요청을 보내고, 응답이 없으면 소리 알림
"""

import requests
import time
import platform
import os
from datetime import datetime
import sys
import argparse

# 기본 설정
DEFAULT_API_URL = "http://localhost:3000/api/health"
DEFAULT_CHECK_INTERVAL = 10  # 10초
DEFAULT_TIMEOUT = 5  # 타임아웃 5초
BEEP_FREQUENCY = 1000  # 비프음 주파수 (Hz)
BEEP_DURATION = 500  # 비프음 지속 시간 (ms)

def beep_alert():
    """소리 알림 - 크로스 플랫폼 지원"""
    try:
        system = platform.system()
        
        if system == "Windows":
            # Windows: winsound 사용
            import winsound
            winsound.Beep(BEEP_FREQUENCY, BEEP_DURATION)
            print("🔔 알림 소리 재생 (Windows)")
            
        elif system == "Darwin":  # macOS
            # macOS: 시스템 사운드 재생
            os.system('afplay /System/Library/Sounds/Glass.aiff &')
            print("🔔 알림 소리 재생 (macOS)")
            
        elif system == "Linux":
            # Linux: 시스템 벨 사용
            # beep 명령어가 있으면 사용, 없으면 시스템 벨
            result = os.system('beep -f {} -l {} 2>/dev/null'.format(BEEP_FREQUENCY, BEEP_DURATION))
            if result != 0:
                # beep 명령어가 없으면 시스템 벨
                print('\a')
            print("🔔 알림 소리 재생 (Linux)")
            
        else:
            # 기타 운영체제: 시스템 벨
            print('\a')
            print("🔔 알림 소리 재생 (System Bell)")
            
    except Exception as e:
        # 실패 시 시스템 벨로 폴백
        try:
            print('\a')
            print(f"🔔 알림 소리 재생 (Fallback) - {e}")
        except:
            print(f"⚠️ 소리 재생 실패: {e}")

def check_health(api_url, timeout):
    """헬스체크 실행"""
    try:
        response = requests.get(api_url, timeout=timeout)
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
    # 명령줄 인자 파싱
    parser = argparse.ArgumentParser(
        description='서버 헬스체크 프로그램 - API에 주기적으로 헬스체크 요청을 보내고 응답이 없으면 알림',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
  python health-check.py --url http://localhost:3000/api/health
  python health-check.py --url https://api.example.com/health --interval 5 --timeout 3
  python health-check.py -u http://localhost:8080/health -i 15
        """
    )
    
    parser.add_argument(
        '--url', '-u',
        type=str,
        default=DEFAULT_API_URL,
        help=f'헬스체크 API URL (기본값: {DEFAULT_API_URL})'
    )
    
    parser.add_argument(
        '--interval', '-i',
        type=int,
        default=DEFAULT_CHECK_INTERVAL,
        help=f'체크 간격(초) (기본값: {DEFAULT_CHECK_INTERVAL})'
    )
    
    parser.add_argument(
        '--timeout', '-t',
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f'요청 타임아웃(초) (기본값: {DEFAULT_TIMEOUT})'
    )
    
    args = parser.parse_args()
    
    # 설정 출력
    print("=" * 50)
    print("서버 헬스체크 프로그램 시작")
    print(f"API URL: {args.url}")
    print(f"체크 간격: {args.interval}초")
    print(f"타임아웃: {args.timeout}초")
    print("=" * 50)
    print()

    consecutive_failures = 0

    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            is_healthy, status = check_health(args.url, args.timeout)

            if is_healthy:
                consecutive_failures = 0
                print(f"[{timestamp}] ✅ 정상 - Status: {status}")
            else:
                consecutive_failures += 1
                print(f"[{timestamp}] ❌ 실패 - Status: {status} (연속 실패: {consecutive_failures}회)")
                
                # 응답이 없으면 소리 알림
                beep_alert()
                print(f"⚠️ 서버 응답 없음! 연속 {consecutive_failures}회 실패")

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\n\n프로그램 종료")
        sys.exit(0)

if __name__ == "__main__":
    main()


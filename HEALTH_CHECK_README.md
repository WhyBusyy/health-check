# 서버 헬스체크 프로그램

10초마다 API에 헬스체크를 보내고, 응답이 없으면 소리 알림을 울리는 크로스 플랫폼 프로그램입니다.

## 지원 운영체제

- ✅ Windows
- ✅ macOS
- ✅ Linux

## 설치 방법

1. Python 설치 확인
```bash
python --version
# 또는
python3 --version
```

2. 필요한 패키지 설치
```bash
pip install -r requirements-health-check.txt
```

## 사용 방법

1. `health-check.py` 파일을 열어서 API URL을 수정하세요
```python
API_URL = "http://localhost:3000/api/health"  # 여기를 실제 API URL로 변경
```

2. 프로그램 실행
```bash
python health-check.py
```

## 설정 변경

`health-check.py` 파일에서 다음 설정을 변경할 수 있습니다:

- `API_URL`: 헬스체크할 API 주소
- `CHECK_INTERVAL`: 체크 간격 (초 단위, 기본값: 10초)
- `TIMEOUT`: 요청 타임아웃 (초 단위, 기본값: 5초)
- `BEEP_FREQUENCY`: 비프음 주파수 (Hz, 기본값: 1000)
- `BEEP_DURATION`: 비프음 지속 시간 (ms, 기본값: 500)

## 기능

- ✅ 10초마다 자동 헬스체크
- 🔔 응답 없을 때 소리 알림 (크로스 플랫폼 지원)
  - Windows: winsound 비프음
  - macOS: 시스템 사운드 (Glass.aiff)
  - Linux: beep 명령어 또는 시스템 벨
- 📊 연속 실패 횟수 표시
- ⏰ 타임스탬프 표시
- ⌨️ Ctrl+C로 안전하게 종료
- 🌍 Windows, macOS, Linux 모두 지원

## 예시 출력

```
==================================================
서버 헬스체크 프로그램 시작
API URL: http://localhost:3000/api/health
체크 간격: 10초
==================================================

[2024-01-15 14:30:00] ✅ 정상 - Status: 200
[2024-01-15 14:30:10] ✅ 정상 - Status: 200
[2024-01-15 14:30:20] ❌ 실패 - Status: TIMEOUT (연속 실패: 1회)
🔔 알림 소리 재생
⚠️ 서버 응답 없음! 연속 1회 실패
```


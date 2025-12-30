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

### 기본 실행 (기본 URL 사용)

```bash
python health-check.py
```

### API URL 지정하여 실행

```bash
python health-check.py --url http://your-api.com/health
```

### 옵션 전체 사용

```bash
python health-check.py --url http://your-api.com/health --interval 5 --timeout 3
```

### 짧은 옵션 사용

```bash
python health-check.py -u http://your-api.com/health -i 15 -t 10
```

### TTS 음성 알림 사용

```bash
python health-check.py --url http://your-api.com/health --alert "A서버가 다운되었습니다"
```

```bash
python health-check.py -u http://localhost:3000/health -a "주의! 서버 응답 없음"
```

### 도움말 보기

```bash
python health-check.py --help
```

## 명령줄 옵션

| 옵션         | 짧은 옵션 | 설명                                      | 기본값                             |
| ------------ | --------- | ----------------------------------------- | ---------------------------------- |
| `--url`      | `-u`      | 헬스체크할 API URL                        | `http://localhost:3000/api/health` |
| `--interval` | `-i`      | 체크 간격(초)                             | 10                                 |
| `--timeout`  | `-t`      | 요청 타임아웃(초)                         | 5                                  |
| `--alert`    | `-a`      | 실패 시 TTS로 읽을 알림 메시지 (선택사항) | 없음 (비프음 사용)                 |

### 고급 설정 (코드 수정 필요)

`health-check.py` 파일에서 다음 설정을 변경할 수 있습니다:

- `BEEP_FREQUENCY`: 비프음 주파수 (Hz, 기본값: 1000)
- `BEEP_DURATION`: 비프음 지속 시간 (ms, 기본값: 500)

## 기능

- ✅ 10초마다 자동 헬스체크
- 🔔 응답 없을 때 소리 알림 (크로스 플랫폼 지원)
  - Windows: winsound 비프음
  - macOS: 시스템 사운드 (Glass.aiff)
  - Linux: beep 명령어 또는 시스템 벨
- 🔊 **TTS 음성 알림** - 커스텀 메시지를 음성으로 재생
  - Windows: PowerShell SAPI 사용
  - macOS: `say` 명령어 사용
  - Linux: `espeak` 또는 `spd-say` 사용
- 📊 연속 실패 횟수 표시
- ⏰ 타임스탬프 표시
- ⌨️ Ctrl+C로 안전하게 종료
- 🌍 Windows, macOS, Linux 모두 지원

## 예시 출력

### 비프음 알림 (기본)

```
$ python health-check.py --url http://localhost:3000/api/health --interval 10

==================================================
서버 헬스체크 프로그램 시작
API URL: http://localhost:3000/api/health
체크 간격: 10초
타임아웃: 5초
==================================================

[2024-01-15 14:30:00] ✅ 정상 - Status: 200
[2024-01-15 14:30:10] ✅ 정상 - Status: 200
[2024-01-15 14:30:20] ❌ 실패 - Status: TIMEOUT (연속 실패: 1회)
🔔 알림 소리 재생 (macOS)
⚠️ 서버 응답 없음! 연속 1회 실패
```

### TTS 음성 알림

```
$ python health-check.py --url http://localhost:3000/api/health --alert "A서버가 다운되었습니다"

==================================================
서버 헬스체크 프로그램 시작
API URL: http://localhost:3000/api/health
체크 간격: 10초
타임아웃: 5초
알림 메시지: A서버가 다운되었습니다
==================================================

[2024-01-15 14:30:00] ✅ 정상 - Status: 200
[2024-01-15 14:30:10] ✅ 정상 - Status: 200
[2024-01-15 14:30:20] ❌ 실패 - Status: TIMEOUT (연속 실패: 1회)
🔊 TTS 재생 (macOS): A서버가 다운되었습니다
⚠️ 서버 응답 없음! 연속 1회 실패
```

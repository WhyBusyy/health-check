# 서버 헬스체크 프로그램

10초마다 API에 헬스체크를 보내고, 응답이 없으면 소리 알림을 울리는 크로스 플랫폼 프로그램입니다.

## 지원 운영체제

- ✅ Windows
- ✅ macOS
- ✅ Linux

## 파일 구조

```
health-check/
├── health-check.py                      # 메인 프로그램
├── requirements-health-check.txt        # Python 패키지 의존성
├── README.md                            # 사용 설명서
├── start_health_check.bat              # Windows 일반 실행 (콘솔 창 표시)
├── start_health_check_background.bat   # Windows 백그라운드 실행
└── stop_health_check.bat               # Windows 프로그램 종료
```

## 🚀 빠른 시작 (Windows)

노트북을 닫고 계속 모니터링하고 싶다면:

1. **패키지 설치**

   ```cmd
   pip install -r requirements-health-check.txt
   ```

2. **`start_health_check_background.bat` 편집**
   - 메모장으로 열어서 API URL과 알림 메시지 수정
3. **실행**
   - 파일 더블클릭
4. **전원 설정 변경**

   - 제어판 > 전원 옵션 > 덮개 닫기 동작 > "아무 작업도 안 함"

5. **노트북 닫기** 🎉
   - 이제 노트북을 닫아도 계속 모니터링됩니다!

---

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

## Windows 노트북 덮개를 닫아도 계속 실행하기

Windows 노트북에서 덮개를 닫아도 프로그램이 계속 실행되도록 하는 방법입니다.

### 방법 1: Windows 전원 설정 변경 (가장 간단)

1. **제어판 > 전원 옵션** 열기
2. 현재 사용 중인 전원 계획 옆의 **"계획 설정 변경"** 클릭
3. **"고급 전원 설정 변경"** 클릭
4. **"덮개 닫기 동작"** 찾기
   - **배터리 사용**: "아무 작업도 안 함"
   - **전원에 연결**: "아무 작업도 안 함"
5. 적용 및 확인

> ⚠️ **주의**: 이 설정은 노트북을 닫아도 화면만 꺼지고 시스템은 계속 실행됩니다. 배터리가 소모될 수 있으니 전원 연결 권장합니다.

### 방법 2: 백그라운드 실행 (pythonw 사용)

프로그램을 콘솔 창 없이 백그라운드에서 실행합니다.

```cmd
pythonw health-check.py --url http://your-api.com/health --alert "서버 다운됨"
```

> **참고**: `pythonw`는 콘솔 창을 표시하지 않지만, 로그를 볼 수 없습니다. 디버깅 시에는 `python` 명령어를 사용하세요.

### 방법 3: 로그 파일과 함께 백그라운드 실행

로그를 파일로 저장하면서 백그라운드 실행:

```cmd
python health-check.py --url http://your-api.com/health --alert "서버 다운됨" > health-check.log 2>&1
```

### 방법 4: 간편 실행 배치 파일 사용 (추천!)

Windows용 배치 파일이 제공되어 더블클릭만으로 실행할 수 있습니다.

#### 📁 제공되는 배치 파일

1. **`start_health_check.bat`** - 일반 실행 (콘솔 창 표시)
   - 로그를 실시간으로 볼 수 있음
   - 디버깅에 유용
2. **`start_health_check_background.bat`** - 백그라운드 실행
   - 콘솔 창 없이 백그라운드 실행
   - 알림만 받고 싶을 때 사용
3. **`stop_health_check.bat`** - 프로그램 종료
   - 백그라운드로 실행 중인 프로그램 종료

#### 사용법

1. 배치 파일을 메모장으로 열기
2. 설정 영역 수정:

```batch
SET API_URL=http://localhost:3000/api/health
SET CHECK_INTERVAL=10
SET TIMEOUT=5
SET ALERT_MESSAGE=A서버가 다운되었습니다
```

3. 저장 후 더블클릭으로 실행

#### 프로그램 종료하기

- **일반 실행**: 콘솔 창을 닫거나 Ctrl+C
- **백그라운드 실행**: `stop_health_check.bat` 실행

### 방법 5: Windows 시작 프로그램으로 등록 (자동 실행)

컴퓨터가 부팅될 때 자동으로 실행되도록 설정:

1. `start_health_check_background.bat` 파일 우클릭
2. "바로 가기 만들기" 선택
3. `Win + R` 키 누르고 `shell:startup` 입력 후 Enter
4. 열린 폴더에 방금 만든 바로가기 복사
5. 이제 Windows 부팅 시 자동으로 백그라운드에서 헬스체크 시작

> 💡 **Tip**: 백그라운드 버전을 사용하면 콘솔 창 없이 조용히 실행됩니다.

### 💡 추천 조합

**노트북을 닫고 계속 모니터링하려면**:

1. ✅ **방법 1**로 전원 설정 변경
2. ✅ **방법 4**로 배치 파일 실행
3. ✅ 노트북 전원 연결 유지

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

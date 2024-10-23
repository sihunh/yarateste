실시간으로 웹 페이지를 스캔하여 타이포스쿼팅 공격이나 악성 리다이렉션을 탐지합니다.
주요 기능

실시간 URL 스캔: Chrome Driver를 활용한 웹페이지 소스 분석
YARA 기반 패턴 탐지: 악성 코드 및 의심스러운 패턴 검사
VirusTotal 연동: 2차 검증을 통한 정확도 향상
자동 파일 다운로드 모니터링: Drive-by Download 공격 탐지
스테가노그래피 탐지: 숨겨진 악성코드 패턴 분석
Firebase Cloud 연동: 실시간 데이터 동기화 및 모니터링

설치 방법

필수 요구사항:

Python 3.8 이상
Chrome Browser
Chrome Driver


패키지 설치:

bashCopypip install -r requirements.txt

Chrome Driver 설정:

Chrome Driver 다운로드
다운로드한 드라이버를 시스템 경로에 추가



사용 방법

UI.py 실행:

bashCopypython UI.py

기본 설정:

다운로드 경로: C:\test_download
프로필 경로: C:\test_profile
로그 저장 경로: logs 폴더



구조
Copy├── UI.py                  # 메인 UI 
├── rules/                 # YARA 룰 정의
│   └── malicious.yar     # 악성코드 패턴
├── logs/                  # 로그 파일
└── modules/              # 핵심 모듈
    ├── scanner.py        # URL 스캐너
    ├── validator.py      # 2차 검증
    └── monitor.py        # 파일 모니터링
개발 배경
20대 시절 타이포스쿼팅 공격으로 인한 이더리움 피해 경험을 바탕으로 개발되었습니다. 유사한 피싱 공격을 예방하고 사용자들의 자산을 보호하기 위해 만들어졌습니다.
향후 계획

네트워크 내 악성 DNS 트래픽 분석 탐지 기능 추가
UI/UX 개선
실시간 알림 시스템 강화

참고 자료

Chrome Driver Capabilities
VirusTotal API Documentation

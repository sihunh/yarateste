#이더리움 피싱 사이트 및 악성 URL을 탐지하기 위한 보안 도구입니다. 실시간으로 웹 페이지를 스캔하여 타이포스쿼팅 공격이나 악성 리다이렉션을 탐지합니다.

개발 배경
20살때 타이퍼쿼스팅 공격을 당하여 이더월렛에 돈을 날려버린적이 있습니다. 해당 이더월렛 도메인과 비슷한 악성사이트로 리다이렉트가 일어나 거기에 암호화파일을 올리고 암호문을 적었던걸로 기억합니다. 그런일을 막기위해 해당 프로그램을 만들어 보았습니다.
기능

실시간 URL 스캔 (Chrome Driver 활용)
YARA 기반 패턴 탐지
VirusTotal API 연동 2차 검증
Drive-by Download 공격 탐지
스테가노그래피 탐지
Firebase Cloud 연동

실행 방법

UI.py 실행

주요 설정

다운로드 경로: C:\test_download
프로필 경로: C:\test_profile
로그 저장: logs 폴더

구현 내용
1차 검증

chromedriver에서 검색하는 내용 전체 websrc_번호로 파일소스 저장
YARA 룰에 의한 패턴 검사
탐지시 wintoast 알림
검사 로그는 logs 파일에 저장

2차 검증

VirusTotal API 활용 악성 URL 확인
API 제한: 일일 500개, 분당 4개
검사 시간 약 1분 소요 (데몬 스레드로 실행)

파일 다운로드 모니터링

Drive by download 공격 대응
다운로드된 파일 해시값 검증
스테가노그래피 기술 탐지

참고

Chrome Driver: https://chromedriver.chromium.org/capabilities
VirusTotal API: https://developers.virustotal.com/reference/url-object

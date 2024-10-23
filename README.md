# 악성 URL 탐지 도구

## 개요

이 프로젝트는 이더리움 관련 피싱 사이트 및 악성 URL을 탐지하는 보안 도구입니다. 웹 페이지를 실시간으로 스캔하여 타이포스쿼팅 공격, 악성 리다이렉션 등을 탐지하며, 사용자의 자산을 보호하기 위해 제작되었습니다.

## 개발 배경

20살 때 타이포스쿼팅 공격을 받아 이더리움을 도난당한 경험이 있습니다. 이더월렛과 유사한 악성 사이트로 리다이렉트되어 암호화된 파일을 업로드하고, 암호를 입력해버린 적이 있습니다. 이와 같은 일을 방지하기 위해 본 도구를 개발했습니다.

## 주요 기능

- **실시간 URL 스캔**: Chrome Driver를 사용하여 웹 페이지를 실시간으로 스캔합니다.
- **YARA 기반 패턴 탐지**: YARA 룰을 사용해 악성 패턴을 탐지합니다.
- **VirusTotal API 연동**: VirusTotal API를 통해 2차 검증을 수행합니다.
- **Drive-by Download 공격 탐지**: 다운로드된 파일의 해시값을 검증하여 악성 다운로드를 탐지합니다.
- **스테가노그래피 탐지**: 스테가노그래피 기법으로 숨겨진 악성 데이터를 탐지합니다.
- **Firebase Cloud 연동**: 실시간 알림 및 클라우드 연동 기능을 제공합니다.

## 실행 방법

1. Python 환경에서 `UI.py` 파일을 실행합니다.
2. 아래의 설정 경로를 참고하여 다운로드와 로그를 관리합니다.

## 주요 설정

- **다운로드 경로**: `C:\test_download`
- **프로필 경로**: `C:\test_profile`
- **로그 저장 경로**: `logs` 폴더

## 구현 내용

### 1차 검증

- ChromeDriver에서 웹 페이지 소스를 저장하고 YARA 룰을 적용하여 패턴 검사를 수행합니다.
- 악성 패턴이 탐지되면 wintoast 알림을 제공합니다.
- 검사 로그는 `logs` 폴더에 저장됩니다.

### 2차 검증

- VirusTotal API를 사용하여 추가 악성 URL 검증을 수행합니다.
  - **API 제한**: 일일 500개, 분당 4개
  - **검사 시간**: 약 1분 소요 (데몬 스레드로 비동기 실행)

### 파일 다운로드 모니터링

- Drive-by Download 공격을 대응합니다.
- 다운로드된 파일의 해시값을 실시간으로 검증하여 악성 다운로드를 차단합니다.
- 스테가노그래피 기법 탐지를 통해 이미지 등 숨겨진 악성 데이터를 탐지합니다.

## 참고 자료

- **Chrome Driver**: [Chrome Driver 공식 페이지](https://chromedriver.chromium.org/capabilities)
- **VirusTotal API**: [VirusTotal API 문서](https://developers.virustotal.com/reference/url-object)

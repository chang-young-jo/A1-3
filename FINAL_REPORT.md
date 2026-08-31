# A1-3 AI 웹개발 미션 최종 보고서

# Machine Doctor AI

## 1. 프로젝트 개요

### 프로젝트명

**Machine Doctor AI**

### 프로젝트 주제

AI 기반 공작기계 품질문제 분석 웹서비스

### 프로젝트 목적

Machine Doctor AI는 공작기계에서 발생하는 이상 현상과 발생 조건을 사용자가 입력하면 AI가 입력 내용을 분석하여 예상 원인, 점검 항목 및 권장 조치를 제안하는 웹서비스입니다.

공작기계 품질, 생산, 서비스 및 유지보수 업무에서 이상 현상이 발생했을 때 초기 문제 분석과 점검 방향 설정을 지원하는 것을 목적으로 개발했습니다.

AI가 제공하는 결과는 참고용이며, 실제 장비의 최종 진단은 측정 데이터와 전문가의 판단을 통해 이루어져야 합니다.

---

## 2. 주요 사용자

Machine Doctor AI의 주요 사용자는 다음과 같습니다.

- 공작기계 품질 엔지니어
- 공작기계 생산 엔지니어
- 공작기계 서비스 엔지니어
- 설비 유지보수 담당자
- 생산 현장 설비 관리 담당자

---

## 3. 웹서비스 구성

Machine Doctor AI는 다음 4개의 주요 섹션으로 구성했습니다.

### HOME

서비스명과 주요 기능을 소개하고 AI 분석 화면으로 이동할 수 있도록 구성했습니다.

### 서비스 소개

Machine Doctor AI의 개발 목적과 주요 기능을 설명합니다.

### AI 품질분석

사용자가 공작기계의 이상 현상과 발생 조건을 입력하고 AI 분석 결과를 확인하는 핵심 기능입니다.

### 사용방법

서비스 사용 순서와 AI 분석 결과 이용 시 주의사항을 안내합니다.

---

## 4. 핵심 AI 기능

사용자는 다음 두 가지 정보를 입력합니다.

### 입력 1 - 이상 현상

예:

```text
주축 회전 시 고주파 소음과 진동이 발생합니다.
```

### 입력 2 - 발생 조건

예:

```text
8000rpm 이상에서 소음이 증가하고
주축 온도도 함께 상승합니다.
```

사용자가 **AI 분석하기** 버튼을 누르면 OpenAI API를 이용하여 입력 내용을 분석합니다.

AI는 다음 세 가지 정보를 중심으로 결과를 제공합니다.

1. 예상 원인
2. 점검 항목
3. 권장 조치

---

## 5. AI 동작 구조

전체 데이터 흐름은 다음과 같습니다.

```text
사용자
   ↓
이상 현상 / 발생 조건 입력
   ↓
HTML
   ↓
JavaScript
   ↓
fetch('/api/analyze')
   ↓
Python Backend
   ↓
OpenAI API
   ↓
AI 분석 결과
   ↓
Python Backend
   ↓
JavaScript
   ↓
웹페이지에 결과 표시
```

이를 통해 Frontend와 Backend가 API 방식으로 데이터를 주고받도록 구현했습니다.

---

## 6. 기술 스택

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Vercel Serverless Functions

### AI

- OpenAI API

### 개발환경

- Visual Studio Code

### 형상관리

- Git
- GitHub

### 배포

- Vercel

---

## 7. 프로젝트 구조

```text
A1-3
├── api
│   └── analyze.py
├── css
│   └── style.css
├── images
├── js
│   └── app.js
├── .gitignore
├── index.html
├── README.md
├── requirements.txt
├── SERVICE_PLAN.md
└── FINAL_REPORT.md
```

---

## 8. 오류 처리

### 빈 입력

사용자가 이상 현상을 입력하지 않은 경우:

```text
분석할 이상 현상을 입력해주세요.
```

라는 메시지를 표시하도록 구현했습니다.

### AI 분석 중

OpenAI API 응답을 기다리는 동안:

```text
AI가 분석 중입니다. 잠시만 기다려주세요...
```

라는 메시지를 표시합니다.

### API 오류

AI API 또는 Backend 통신 과정에서 오류가 발생하면 사용자에게 오류 안내 메시지를 표시하도록 구현했습니다.

---

## 9. 반응형 웹 구현

Machine Doctor AI는 데스크톱뿐만 아니라 모바일 환경에서도 사용할 수 있도록 CSS Media Query를 적용했습니다.

다음 환경에서 화면을 확인했습니다.

- Desktop
- Mobile

화면 크기에 따라 메뉴, 입력창, 버튼 및 콘텐츠가 자동으로 조정되도록 구성했습니다.

---

## 10. API Key 보안

OpenAI API Key는 소스코드에 직접 작성하지 않고 환경 변수로 관리했습니다.

로컬 개발 환경에서는:

```text
.env
```

파일을 사용했습니다.

`.gitignore`에 `.env`를 등록하여 실제 API Key가 GitHub에 업로드되지 않도록 설정했습니다.

Vercel에서는 Environment Variables 기능을 이용하여 다음 환경 변수를 별도로 등록했습니다.

```text
OPENAI_API_KEY
```

이를 통해 실제 API Key가 소스코드와 GitHub Repository에 공개되지 않도록 관리했습니다.

---

## 11. Git / GitHub 활용

프로젝트 개발 과정에서 Git을 이용하여 변경 이력을 관리했습니다.

주요 과정은 다음과 같습니다.

```text
프로젝트 생성
    ↓
git init
    ↓
git add
    ↓
git commit
    ↓
GitHub Repository 연결
    ↓
git push
```

기능 구현 및 문서 작성 과정에서도 추가 Commit을 생성하여 개발 이력을 관리했습니다.

---

## 12. Vercel 배포

GitHub의 A1-3 Repository를 Vercel과 연결하여 웹서비스를 배포했습니다.

Vercel 환경 변수에 `OPENAI_API_KEY`를 등록하여 배포 환경에서도 OpenAI API가 동작하도록 구성했습니다.

배포 후 실제 Vercel URL에서 다음 기능을 확인했습니다.

- 웹페이지 정상 접속
- 상단 메뉴 이동
- 사용자 입력
- AI 분석 요청
- 실제 AI 분석 결과 출력
- 빈 입력 오류 처리
- 모바일 반응형 화면

---

## 13. 최종 테스트 결과

| 테스트 항목 | 결과 |
|---|---|
| 웹사이트 접속 | PASS |
| HOME 화면 | PASS |
| 서비스 소개 | PASS |
| AI 품질분석 화면 | PASS |
| 사용방법 화면 | PASS |
| 이상 현상 입력 | PASS |
| 발생 조건 입력 | PASS |
| OpenAI API 호출 | PASS |
| AI 분석 결과 출력 | PASS |
| 빈 입력 오류 처리 | PASS |
| 데스크톱 화면 | PASS |
| 모바일 반응형 화면 | PASS |
| GitHub Repository | PASS |
| Vercel 배포 | PASS |
| API Key 비공개 | PASS |

---

## 14. 배포 URL

### Vercel

```text
https://a1-3-silk.vercel.app/
```

---

## 15. GitHub Repository

```text
https://github.com/chang-young-jo/A1-3.git
```

---

## 16. 제출 증빙자료

프로젝트 수행 결과를 확인할 수 있도록 다음 증빙자료를 준비했습니다.

### 01. 웹서비스 데스크톱 화면

Machine Doctor AI가 데스크톱 환경에서 정상적으로 표시되는 화면

### 02. AI 기능 정상 동작

사용자가 이상 현상과 발생 조건을 입력하고 실제 AI 분석 결과가 표시되는 화면

### 03. 빈 입력 오류 처리

필수 입력값이 없는 상태에서 사용자 안내 메시지가 표시되는 화면

### 04. 모바일 반응형 화면

스마트폰 화면 크기에서도 웹서비스가 정상적으로 표시되는 화면

### 05. AI 코딩 도구 사용 과정

AI 코딩 도구를 이용하여 코드를 작성하고 개발 과정을 진행한 화면

### 06. GitHub Repository

프로젝트 파일과 개발 이력이 등록된 GitHub Repository 화면

### 07. Vercel 배포 완료

Machine Doctor AI가 Vercel에 정상적으로 배포된 화면

---

## 17. 프로젝트 수행 과정

전체 프로젝트는 다음 순서로 진행했습니다.

```text
서비스 아이디어 선정
        ↓
서비스 기획
        ↓
프로젝트 구조 생성
        ↓
HTML 웹페이지 구현
        ↓
CSS 디자인 및 반응형 구현
        ↓
JavaScript 기능 구현
        ↓
Python Backend 구현
        ↓
OpenAI API 연동
        ↓
Frontend ↔ Backend 연결
        ↓
오류 처리
        ↓
Git / GitHub 소스 관리
        ↓
Vercel 배포
        ↓
실제 AI 기능 테스트
        ↓
README 작성
        ↓
서비스 기획서 작성
        ↓
증빙자료 작성
```

---

## 18. 프로젝트를 통해 학습한 내용

이번 프로젝트를 통해 단순한 코드 작성뿐만 아니라 실제 AI 웹서비스를 개발하고 배포하는 전체 과정을 경험했습니다.

특히 다음 내용을 학습했습니다.

- HTML, CSS, JavaScript의 역할
- Frontend와 Backend의 차이
- JavaScript `fetch()`를 이용한 API 통신
- Python Backend 구현
- OpenAI API 활용
- 환경 변수를 이용한 API Key 관리
- `.gitignore`를 이용한 보안 관리
- Git을 이용한 개발 이력 관리
- GitHub Repository 관리
- Vercel을 이용한 웹서비스 배포
- 로컬 환경과 실제 배포 환경의 차이
- 모바일 반응형 웹 구현
- AI 코딩 도구를 활용한 개발 과정

---

## 19. 최종 결과

**Machine Doctor AI**를 통해 아이디어 기획부터 Frontend, Backend, OpenAI API 연동, GitHub 소스 관리 및 Vercel 배포까지 실제 AI 웹서비스 개발 과정을 완료했습니다.

최종적으로 사용자가 공작기계 이상 현상과 발생 조건을 입력하면 AI가 내용을 분석하여 **예상 원인, 점검 항목 및 권장 조치**를 제공하는 웹서비스를 구현했습니다.
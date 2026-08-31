# Machine Doctor AI

AI를 활용하여 공작기계에서 발생하는 이상 현상을 분석하고,  
예상 원인과 점검 항목, 권장 조치를 제안하는 AI 웹서비스입니다.

---

## 1. 서비스 소개

**Machine Doctor AI**는 공작기계에서 발생하는 품질 문제와 이상 현상을 보다 빠르게 분석할 수 있도록 지원하는 AI 기반 웹서비스입니다.

사용자가 공작기계의 **이상 현상**과 **발생 조건**을 입력하면 OpenAI API를 활용하여 입력 내용을 분석하고 다음 정보를 제공합니다.

- 예상 원인
- 점검 항목
- 권장 조치

공작기계 품질, 생산, 서비스 엔지니어 및 현장 작업자가 문제 발생 시 초기 점검 방향을 설정하는 데 도움을 주는 것을 목적으로 합니다.

> **주의:** Machine Doctor AI의 분석 결과는 참고용이며, 실제 장비의 최종 진단은 측정 결과와 전문가의 판단을 통해 이루어져야 합니다.

---

## 2. 주요 기능

Machine Doctor AI는 다음 기능을 제공합니다.

- 공작기계 이상 현상 입력
- 이상 발생 조건 입력
- OpenAI API 기반 AI 분석
- 예상 원인 제공
- 점검 항목 제공
- 권장 조치 제공
- 빈 입력에 대한 오류 안내
- AI 분석 중 사용자 안내 메시지 표시
- API 오류 발생 시 오류 메시지 표시
- 모바일 / 태블릿 / 데스크톱 반응형 화면 제공
- 상단 메뉴를 이용한 페이지 섹션 이동

---

## 3. 페이지 구성

웹서비스는 다음과 같은 주요 섹션으로 구성되어 있습니다.

### 3.1 HOME

Machine Doctor AI의 서비스명과 주요 목적을 보여주는 메인 화면입니다.

사용자는 **AI 분석 시작하기** 버튼을 이용하여 AI 품질분석 영역으로 이동할 수 있습니다.

### 3.2 서비스 소개

Machine Doctor AI가 어떤 목적으로 개발되었으며 어떤 기능을 제공하는지 설명합니다.

### 3.3 AI 품질분석

사용자가 공작기계의 이상 현상과 발생 조건을 입력하는 핵심 기능입니다.

사용자가 **AI 분석하기** 버튼을 누르면 입력 내용이 AI로 전달되고 분석 결과가 화면에 표시됩니다.

### 3.4 사용방법

서비스 사용 순서와 AI 분석 결과 이용 시 주의사항을 안내합니다.

---

## 4. 기술 스택

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Vercel Serverless Functions

### AI

- OpenAI API

### 개발 및 형상관리

- Visual Studio Code
- Git
- GitHub

### 배포

- Vercel

---

## 5. 프로젝트 구조

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
└── requirements.txt
```

각 파일의 주요 역할은 다음과 같습니다.

- `index.html` : 웹페이지의 기본 구조
- `css/style.css` : 웹페이지 디자인 및 반응형 화면 구성
- `js/app.js` : 사용자 입력 처리 및 Backend API 호출
- `api/analyze.py` : OpenAI API를 호출하는 Python Backend
- `requirements.txt` : Python 패키지 정보
- `.gitignore` : GitHub에 업로드하지 않을 파일 설정
- `README.md` : 프로젝트 설명 및 실행/배포 방법

---

## 6. AI 동작 구조

Machine Doctor AI의 전체 데이터 흐름은 다음과 같습니다.

```text
사용자 입력
    ↓
index.html
    ↓
JavaScript (app.js)
    ↓
fetch('/api/analyze')
    ↓
Python Backend (api/analyze.py)
    ↓
OpenAI API
    ↓
AI 분석 결과 반환
    ↓
JavaScript
    ↓
웹페이지에 분석 결과 표시
```

사용자가 입력한 공작기계 이상 현상과 발생 조건은 JavaScript에서 처리됩니다.

JavaScript의 `fetch()`를 이용하여 `/api/analyze` Backend로 데이터를 전달하고, Python Backend에서 OpenAI API를 호출합니다.

OpenAI가 생성한 분석 결과는 다시 JavaScript로 전달되어 웹페이지에 표시됩니다.

---

## 7. 로컬 실행 방법

### 7.1 프로젝트 준비

GitHub 저장소를 Clone하거나 프로젝트 파일을 다운로드합니다.

### 7.2 Python 패키지 설치

VS Code에서 터미널을 열고 다음 명령어를 실행합니다.

```bash
pip install -r requirements.txt
```

### 7.3 환경 변수 설정

프로젝트 최상위 폴더에 `.env` 파일을 생성합니다.

`.env` 파일에 다음과 같이 OpenAI API Key를 입력합니다.

```text
OPENAI_API_KEY=본인의_OpenAI_API_Key
```

실제 API Key는 보안을 위해 코드 또는 GitHub에 공개하지 않습니다.

### 7.4 Python Backend 실행

터미널에서 다음 명령어를 실행합니다.

```bash
python api/analyze.py
```

서버가 정상적으로 실행되면 웹페이지에서 AI 분석 기능을 테스트합니다.

### 7.5 AI 기능 테스트

예를 들어 다음과 같이 입력합니다.

```text
이상 현상:
주축 회전 시 고주파 소음과 진동이 발생합니다.

발생 조건:
8000rpm 이상에서 소음이 증가하고
주축 온도도 함께 상승합니다.
```

**AI 분석하기** 버튼을 누르면 OpenAI API를 통해 분석한 결과가 화면에 표시됩니다.

---

## 8. Vercel 배포 방법

Machine Doctor AI는 GitHub와 Vercel을 연동하여 배포합니다.

### 배포 순서

1. 프로젝트 코드를 GitHub 저장소에 Push합니다.
2. Vercel에 GitHub 계정으로 로그인합니다.
3. GitHub의 `A1-3` Repository를 Import합니다.
4. Framework Preset은 `Other`를 사용합니다.
5. Root Directory는 프로젝트 최상위 폴더로 설정합니다.
6. Vercel의 Environment Variables에 `OPENAI_API_KEY`를 추가합니다.
7. Value에 실제 OpenAI API Key를 입력합니다.
8. Deploy를 실행합니다.
9. 배포가 완료되면 생성된 Vercel URL로 접속합니다.
10. 실제 배포 환경에서 AI 분석 기능이 정상적으로 작동하는지 확인합니다.

---

## 9. 환경 변수 및 API Key 보안

OpenAI API Key는 외부에 공개되면 안 되기 때문에 코드에 직접 작성하지 않습니다.

로컬 개발 환경에서는 `.env` 파일을 이용하여 API Key를 관리합니다.

```text
OPENAI_API_KEY=본인의_OpenAI_API_Key
```

`.gitignore`에는 다음 항목을 등록합니다.

```text
.env
__pycache__/
*.pyc
.vscode/
```

따라서 `.env` 파일과 실제 API Key는 GitHub Repository에 업로드되지 않습니다.

Vercel 배포 환경에서는 `.env` 파일을 업로드하지 않고 Vercel의 **Environment Variables** 기능을 이용하여 `OPENAI_API_KEY`를 별도로 등록합니다.

---

## 10. 오류 처리

Machine Doctor AI는 사용자 편의를 위해 오류 상황에 대한 안내 기능을 제공합니다.

### 10.1 빈 입력

사용자가 이상 현상을 입력하지 않고 **AI 분석하기** 버튼을 누르면 다음과 같은 안내 메시지를 표시합니다.

```text
분석할 이상 현상을 입력해주세요.
```

### 10.2 AI 분석 중

OpenAI API의 응답을 기다리는 동안 사용자에게 분석이 진행되고 있음을 안내합니다.

```text
AI가 분석 중입니다. 잠시만 기다려주세요...
```

### 10.3 API 오류

AI API 호출 과정에서 문제가 발생한 경우 사용자에게 오류 안내 메시지를 표시하도록 구성했습니다.

이를 통해 API 오류가 발생하더라도 사용자가 현재 상황을 알 수 있도록 했습니다.

---

## 11. 배포 URL

Machine Doctor AI는 Vercel을 이용하여 실제 웹서비스로 배포했습니다.

### Vercel URL

```text
https://a1-3-silk.vercel.app/
```

배포된 URL을 통해 PC 및 모바일 환경에서 웹서비스에 접속할 수 있습니다.

---

## 12. GitHub Repository

프로젝트 전체 소스코드는 GitHub에서 관리합니다.

### GitHub Repository URL

```text
https://github.com/chang-young-jo/A1-3.git
```

GitHub Repository에는 다음 내용이 포함되어 있습니다.

- Frontend 코드
- Python Backend 코드
- requirements.txt
- README.md
- .gitignore

보안을 위해 `.env` 파일과 실제 OpenAI API Key는 포함하지 않습니다.

---

## 13. 개발 목적 및 학습 내용

이번 프로젝트의 목적은 AI 코딩 도구를 활용하여 아이디어를 실제 웹서비스로 구현하고 인터넷에 배포하는 전체 개발 과정을 경험하는 것입니다.

Machine Doctor AI 프로젝트를 진행하면서 다음 내용을 학습했습니다.

### HTML / CSS / JavaScript

- HTML을 이용한 웹페이지 구조 작성
- CSS를 이용한 웹페이지 디자인
- 반응형 웹페이지 구현
- JavaScript를 이용한 사용자 입력 처리
- 버튼 클릭 이벤트 처리

### Frontend와 Backend 연결

- JavaScript `fetch()` 사용
- Frontend에서 Backend API 호출
- Backend 응답을 웹페이지에 표시하는 과정 이해

### Python Backend

- Python을 이용한 Backend API 구현
- 사용자 입력 데이터 처리
- AI API 호출 결과 반환

### OpenAI API

- OpenAI API 연동
- 사용자 입력을 AI에 전달
- AI 분석 결과를 웹서비스에 표시

### API Key 보안

- `.env`를 이용한 환경 변수 관리
- `.gitignore`를 이용한 API Key 유출 방지
- Vercel Environment Variables 설정

### Git / GitHub

- Git Repository 초기화
- 변경 파일 관리
- Commit을 통한 개발 이력 관리
- GitHub Repository와 로컬 프로젝트 연결
- Push를 통한 소스코드 관리

### Vercel 배포

- GitHub와 Vercel 연동
- Python Serverless Function 배포
- 환경 변수 설정
- 실제 인터넷 URL 생성
- 배포 환경에서 AI 기능 테스트

---

## 프로젝트 결과

Machine Doctor AI를 통해 다음과 같은 전체 웹서비스 개발 흐름을 구현했습니다.

```text
아이디어 기획
    ↓
HTML / CSS / JavaScript Frontend 개발
    ↓
Python Backend 개발
    ↓
OpenAI API 연동
    ↓
Git / GitHub 소스 관리
    ↓
Vercel 배포
    ↓
실제 URL에서 AI 웹서비스 실행
```

이번 프로젝트를 통해 단순히 AI에게 코드를 생성하도록 요청하는 것에서 나아가, 웹서비스의 Frontend와 Backend 구조, API 통신, 환경 변수, GitHub 소스 관리 및 실제 배포까지의 전체 흐름을 학습했습니다.
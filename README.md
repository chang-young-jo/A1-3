# Machine Doctor AI

AI를 활용하여 공작기계에서 발생하는 이상 현상을 분석하고,
예상 원인과 점검 항목, 권장 조치를 제안하는 웹서비스입니다.

---

## 1. 서비스 소개

Machine Doctor AI는 공작기계 품질 및 고장 문제를 보다 빠르게 분석할 수 있도록
사용자의 입력 내용을 기반으로 AI가 점검 방향을 제안하는 서비스입니다.

사용자가 공작기계의 이상 현상과 발생 조건을 입력하면,
OpenAI API를 통해 다음 내용을 제공합니다.

- 예상 원인
- 점검 항목
- 권장 조치

본 서비스의 분석 결과는 참고용이며,
실제 장비 점검 및 전문가의 판단이 필요합니다.

---

## 2. 주요 기능

- 공작기계 이상 현상 입력
- 발생 조건 입력
- OpenAI API 기반 AI 분석
- 예상 원인 제공
- 점검 항목 제공
- 권장 조치 제공
- 빈 입력 오류 처리
- AI 분석 중 안내 메시지
- 모바일/태블릿/데스크톱 반응형 화면 제공

---

## 3. 페이지 구성

### HOME

서비스의 주요 목적과 기능을 소개합니다.

### 서비스 소개

Machine Doctor AI가 어떤 목적으로 만들어졌는지 설명합니다.

### AI 품질분석

사용자가 공작기계 이상 현상과 발생 조건을 입력하고
AI 분석 결과를 확인할 수 있습니다.

### 사용방법

서비스 사용 순서와 주의사항을 안내합니다.

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

### 배포 및 형상관리

- Git
- GitHub
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
└── req'''uirements.txt
```

## 6. AI 동작구조

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
웹페이지 결과 표시
# 🌟 숫자 순서대로!

**5~7세 아이를 위한 숫자 순서 규칙 발견 게임**

> 아이가 스스로 **"규칙을 발견"**하는 경험을 하도록 설계된 교육용 웹게임입니다.

**[🚀 바로 플레이하기](https://noivan0.github.io/kids-number-sequence/)**

---

## ✨ 특징

- **Guided Discovery 방식**: "다음 숫자를 찾아보세요"가 아니라, 아이가 직접 패턴(1씩, 5씩, 10씩)을 발견하게 유도
- **Phase + Track 구조**: 총 4개 Phase, 9개 Track으로 단위 개념을 단계적으로 확장
- **단위 시각화**: 5, 10 단위로 숫자를 그룹핑해서 보여줌 (10의 자리 직관 강화)
- **완전 모바일 최적화**: 5~7세 아이가 큰 손가락으로도 쉽게 터치 가능
- **PWA 지원**: 홈 화면에 설치 가능 (실제 앱처럼 사용)

---

## 📱 지금 바로 사용하기

### 웹에서 플레이
https://noivan0.github.io/kids-number-sequence/

### 앱처럼 설치하기 (추천)
1. 위 링크를 크롬/사파리/엣지로 열기
2. 주소창 오른쪽에 **설치 아이콘**이 나타나면 클릭
3. 설치 후 홈 화면에서 바로 실행 가능 (오프라인 지원)

---

## 🎮 게임 구성 (Phase + Track)

| Phase | 이름             | 주요 학습 내용                     | 트랙 수 |
|-------|------------------|------------------------------------|---------|
| 1     | 순서 감각        | 1의 단위로 숫자가 이어지는 규칙     | 3       |
| 2     | 10의 자리 직관   | 10이 특별한 단위라는 것을 인지       | 4       |
| 3     | 패턴 발견        | 2~10씩 다양한 간격으로 규칙 발견     | 9       |
| 4     | 큰 수 감각       | 100~10000 단위의 크기와 규칙 이해   | 6       |

총 22개 트랙

---

## 🧠 교육 철학

이 게임은 다음 교육 이론을 바탕으로 설계되었습니다:

- **Variation Theory**: 한 번에 하나의 변수만 변화시켜 규칙을 명확히 드러냄
- **Guided Discovery**: 정답을 알려주지 않고 아이가 스스로 발견하게 함
- **Scaffolding**: 진행률 표시 + "규칙 발견!" 배지로 성취감 제공
- **Multiple Representations**: 숫자, 위치, 색상, 그룹핑으로 다중 표현

---

## 🛠️ 로컬에서 실행하기 (개발자용)

```bash
cd kids-number-sequence
python3 -m http.server 5500
```

그 후 `http://localhost:5500` 접속

---

## 📁 프로젝트 구조

```
kids-number-sequence/
├── index.html          # 게임 전체 (단일 파일 PWA)
├── manifest.json       # PWA 설정
├── README.md
├── DESIGN.md           # UI 디자인 가이드
└── GAME_DESIGN.md      # 교육 설계 문서 (상세)
```

---

## 🙏 만든 사람

- **noivan0** (AI Engineer)
- 유아 수 개념 교육에 관심이 많아 직접 설계·개발

---

**아이와 함께 즐겁게 숫자 규칙을 발견해보세요!** 🌟

라이브 데모: https://noivan0.github.io/kids-number-sequence/

---

## 🚀 GitHub Pages + PWA 배포 가이드 (완전 호환)

### 1. GitHub Pages 배포 방법
1. 이 저장소를 Fork 또는 직접 사용
2. `Settings > Pages`에서 다음 설정:
   - Source: **Deploy from a branch**
   - Branch: `main` (또는 `master`)
   - Folder: `/ (root)`
3. 저장 후 `https://<username>.github.io/kids-number-sequence/` 에서 접근 가능

### 2. iOS PWA 완벽 호환을 위한 준비 (이미 적용됨)
- `manifest.json` 에 `scope`, `start_url`, `display: standalone` 설정 완료
- HTML에 iOS 전용 meta 태그 모두 포함:
  - `apple-mobile-web-app-capable`
  - `apple-mobile-web-app-status-bar-style`
  - `viewport-fit=cover`
- 큰 터치 타겟 (82px 이상) 적용
- Standalone 모드에서 안전 영역 대응

### 3. 홈 화면에 추가 후 동작
- iOS Safari에서 "홈 화면에 추가" → 완전한 웹앱처럼 동작 (상단 브라우저 바 사라짐)
- 오프라인에서도 기본 플레이 가능 (Tailwind CDN는 최초 로드 후 캐시됨)

> **주의**: 순수 오프라인 완벽 지원을 원하시면 Service Worker를 추가할 수 있습니다. 현재는 교육용 PWA로서 실사용에 충분한 수준입니다.

---

## 내부 자료

상세 기획 문서, 마케팅 채널 리스트, B2B 제안서, 워크시트 샘플 등은 로컬 전용으로 관리하고 있습니다. (공개 저장소에는 포함되지 않습니다.)
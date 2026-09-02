# thinkbox — 방(세션) 공유 지식 아카이브

네오지오 포켓 한글 프로젝트를 여러 방(Claude 세션)이 나눠 일한다.
같은 함정을 방마다 따로 배우는 낭비를 끊는 것이 이 저장소의 존재 이유다.
**일을 시작하기 전에 [knowledge/traps.md](knowledge/traps.md) 를 한 번 읽어라 —
전부 실제로 두 번 이상 재발한 사고들이다.**

## 색인

| 문서 | 내용 |
|---|---|
| [knowledge/traps.md](knowledge/traps.md) | 재발 함정 모음 — 인코딩·WSL·PowerShell·빌드·안드로이드 |
| [knowledge/methodology.md](knowledge/methodology.md) | 실측 방법론 — 판정 사다리, 투사체 원거리 규명, 검수법 |
| [knowledge/input-mech.md](knowledge/input-mech.md) | 격투게임 입력 메커니즘 해부 — 게임 무관 공통 절차 (주소 찾기→잣대 반증→시험대→입력 규격) |
| [knowledge/ram-map-svc.md](knowledge/ram-map-svc.md) | SVC 램 지도 — 엔진이 실사용 중인 오프셋 전표 + 게임 규칙 실측값 |
| [knowledge/ram-map-ss2.md](knowledge/ram-map-ss2.md) | SS2 전투 램 — 액션 ID·체력·재는 법 (효과음/해설용) |
| [knowledge/ecosystem.md](knowledge/ecosystem.md) | 레포 지도 — 무엇이 어디 살고 배포가 어떻게 도는지 |
| [handover/sp-room.md](handover/sp-room.md) | SP 방 스냅샷 — 산출물 지도 + 한 줄 요청 목록 |

릴리즈 규칙(태그·자산 이름·판올림)은 원본이 KrPatch 에 있다:
[RELEASE_RULES.md](https://github.com/rmdkdkr-png/KrPatch/blob/main/RELEASE_RULES.md)

## 쓰는 법

- 한 주제 = 한 파일. 마크다운. 파일명은 ASCII 케밥.
- 문서 머리에 **어느 방·언제** 적었는지 한 줄.
- **실측과 추측을 구분해 적어라.** 실측이면 근거(주소·프레임·해시)를 같이.
- 새 함정에 당했으면 traps.md 에 한 절 추가 — 그게 이 저장소의 세금이다.
- **토큰·PAT·개인정보 절대 금지.** 커밋 전에 눈으로 확인.
- 각 방의 상세 인수인계(HANDOVER)는 각자 레포에 두고, 여기 handover/ 에는
  요약 스냅샷과 링크만.

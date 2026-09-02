# SP 방 스냅샷 (원버튼 엔진 · PocketCore 앱)

> 2026-09-02 기준. 상세는 각 링크의 원본이 진실이다.

## 지금 상태

- **SVC 원버튼 엔진**: 완성·배포 중 (v3.49). 콤보(착지 엣지사이클)·파생 게이트·모으기
  (문턱 30f/유예 8f)·강약 주입·링 주입까지. 회귀 22/23 (밀착 1건 기지 실패).
- **PocketCore 앱**: 8게임 인지(한패 자동 적용), 코어·음성팩·한패 자동 다운로드,
  오토세이브, 게임별 패드 3프로필, 소식창. 배포 3레포 체제(ecosystem.md 참조).
- 미해결 (엔진): 레오나 무발동 원인 미상 · 강펀캔슬 피해 0 · 밀착 무발동 ·
  하오마루 반전 스테이트 전면 무발동 · 가일 차지 내부 상태 미발견(40f 모으기로 우회).

## 산출물 지도 (전부 ss2-sp-core / ss2-main 레포)

| 것 | 자리 |
|---|---|
| 인수인계 상세 | ss2-sp-core `tools/svc/HANDOVER.md` (v3.33~49 사가 전부) |
| 이식 안내서 (KOF R2·FFC·SS1·SS2) | ss2-sp-core `tools/svc/SP_PORTING.md` |
| 실측 메모 72KB | ss2-sp-core `tools/svc/SVC_MEMO.md` |
| 기술표 + 생성기 | ss2-sp-core `tools/svc/{moves.json, gen_svc_moves.py}` |
| 공통 해부 절차 | `knowledge/input-mech.md` (원본 tools/mech/MECH.md) |
| SVC 램 지도 | `knowledge/ram-map-svc.md` |
| 회귀 러너·시나리오 | **ss2-main** `tools/svc/{sprun.py, scenarios.tsv, svcrun.c}` ← 이쪽이 최신 |
| 세이브 274개 | `~/ss2/saves/svc/` (`svc_c<캐릭>_<변형>.st`) |
| 패치 재생성기 | ss2-sp-core `tools/core/regen_patch.sh` — build/libretro.c 수정 후 필수 |
| 웹 커맨드 조회표 | `~/ss2/ref/motm/커맨드_대조표.md` (+StrategyWiki 33건, 나무위키 사본) |

## 다른 방이 SP 방에 시킬 수 있는 것 (한 줄 요청)

- "patches.json 재배포" — 새 IPS 릴리즈를 앱 색인에 반영
- "코어 재배포" — 코어 수정 후 core-svc/core-ss2 릴리즈 갱신
- 새 게임 추가 — 롬 헤더 0x24 표식 12바이트 실측값과 함께
- 음성팩 판올림 — 파일 + 판번호

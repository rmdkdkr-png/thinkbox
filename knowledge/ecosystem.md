# 레포 지도 — 무엇이 어디 살고, 배포가 어떻게 도는가

(첫 작성: SP 방, 2026-09-02 — 레포 정리 직후 기준)

## 살아 있는 레포

| 레포 | 역할 | 릴리즈 |
|---|---|---|
| **PocketCore** | 앱 소스 + 앱 대문 README | 고정 태그 `app`: APK + version.json + **색인 3종**(patches/cores/news .json) + 스샷 |
| **ss2-sp-core** | SP 코어 소스(빌드트리 포함) + 도구·HANDOVER | `core-svc` `core-ss2` `ss2-voice` (ABI별 .so 3벌, 음성팩) |
| **KrPatch** | 한글패치 IPS + 한패 대문 README + RELEASE_RULES.md | 게임별 `<id>-v<판>` |
| **thinkbox** | (이 저장소) 방 공유 지식 | — |

레거시: SS1-KPatch·ss2-sp-runner·ss1-sp-runner·CustumApKS·emu-ex-plus-alpha 는 휴면.
SS1 한패도 지금은 KrPatch(ss1-v0.19)가 원본이다.
KrPatch 의 옛 `pocketcore` 태그는 구버전 앱(v3.48 이하)이 새 APK 로 갈아타는 다리 — 지우지 말 것.

## 앱 업데이트 흐름 (버튼 하나)

```
앱 「업데이트 확인」
 → PocketCore app 태그 version.json   (새 APK 있으면 설치 흐름으로 — 여기서 끝)
 → cores.json  → ss2-sp-core 릴리즈에서 기기 ABI 코어·음성팩 다운로드
                 (코어는 앱 내부 files/cores/ — sdcard 는 noexec)
 → patches.json → KrPatch 릴리즈에서 게임별 최신 IPS → PocketCore/patch/
 → news.json   → 소식 창
```

색인 3종은 SP 방 스크립트가 만든다:
- `pub_content.py` — 코어·팩 릴리즈 갱신 + cores.json 생성 + 소식 축적
- `pub_pocketcore.py` — patches.json 생성(KrPatch 실태를 정규식으로 훑음) + 앱 업로드
  + 다리 갱신 + README 대문 2곳 + news.json 업로드

**IPS 만 올리면 앱 반영은 색인 재배포 때** — SP 방에 「patches.json 재배포」 한 줄.
자산 이름 규칙은 [RELEASE_RULES.md](https://github.com/rmdkdkr-png/KrPatch/blob/main/RELEASE_RULES.md).

## 대문 원칙

- README(대문)는 **처음 보는 사람에게 지금의 전체 기능**을 설명한다. 판 이력 금지.
- 이력은 앱 소식창(news.json)과 릴리즈 본문에.
- KrPatch README 는 맨 위 마커(`<!-- GATE:BEGIN/END -->`) 구역만 자동 갱신 —
  아래 수제 문서(사무쇼2 상세)는 보존된다. PocketCore README 는 전체 자동.

## 게임 표식 (롬 헤더 0x24, 12바이트 — 전부 실측)

| id | 표식 | | id | 표식 |
|---|---|---|---|---|
| ss2 | `SAMURAI2` | | kofr2 | `KOF R2` |
| svc | `SNKvsCAPCOM1` | | ffc | `RB_F_CONTACT` |
| ss1 | `SAMURAI` | | ms1 | `METALSLUG1ST` |
| lb | `LASTBLADE` | | ms2 | `METALSLUG2ND` |

(SAMURAI2 가 SAMURAI 보다 먼저 걸려야 한다 — 앞부분 일치 판정이라 순서가 중요.)

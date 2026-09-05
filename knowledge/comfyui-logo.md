# ComfyUI (WSL) — 로고 아트 생성 엔진 · 경로와 실행법

본부 승인(2026-09-05)으로 claude-eb 가 깔았다. 전부 `/home/dudu/comfy` 아래, 되돌릴 수 있다(폴더째 지우면 끝).
GPU: RTX 5070 12GB (Blackwell → torch cu128 필요). 1-f7 도 이걸 같이 쓴다.

## 자리
| 것 | 경로 |
|---|---|
| 가상환경 | `/home/dudu/comfy/venv` (uv · python 3.12 · torch 2.11.0+cu128 · cuda OK) |
| ComfyUI | `/home/dudu/comfy/ComfyUI` (git, `--depth 1`) |
| 커스텀 노드 | `custom_nodes/comfyui_controlnet_aux` (전처리) · `custom_nodes/ComfyUI_IPAdapter_plus` (cubiq) |
| 모델 | `ComfyUI/models/checkpoints/sd_xl_base_1.0.safetensors` · `models/controlnet/xinsir_controlnet_canny_sdxl_1.0.safetensors` · `models/ipadapter/ip-adapter-plus_sdxl_vit-h.safetensors` · `models/clip_vision/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` |
| 설치 기록 | `/home/dudu/comfy/install.log` (스크립트 `/home/dudu/comfy_install.sh`) |
| 작업 | `/home/dudu/comfy/work/<게임>/` — 월화 시험은 `work/lb/` |

## 띄우기 / 끄기
```bash
cd /home/dudu/comfy && source venv/bin/activate && nohup python ComfyUI/main.py --listen 127.0.0.1 --port 8188 > comfy.out 2>&1 &
curl -s 127.0.0.1:8188/system_stats | head -c 300     # 살아 있나
pkill -f 'ComfyUI/main.py'                            # 끄기
```
브라우저 UI 는 `http://127.0.0.1:8188` (WSL 안 포트 — Windows 에서도 localhost 로 열린다).

## API 로 돌리기 (스크립트)
`/home/dudu/comfy/work/comfy_lb_run.py [seed] [denoise] [cn_strength] [ip_weight]`
- 그래프: SDXL → IP-Adapter Plus(원본 로고 PNG 참조) → ControlNet canny(획 힌트) → img2img(원본을 잠재로, denoise 0.6 안팎) → 4장.
- 입력은 `ComfyUI/input/` 에 복사해 두고 `LoadImage` 로 읽는다. 출력은 `ComfyUI/output/` → `work/<게임>/out/` 로 복사.
- 노드 이름(클래스): `CheckpointLoaderSimple` `CLIPTextEncode` `LoadImage` `ImageScale` `VAEEncode` `ControlNetLoader` `ControlNetApplyAdvanced` `IPAdapterUnifiedLoader`(preset `PLUS (high strength)`) `IPAdapter` `KSampler` `VAEDecode` `SaveImage`.

## 획 힌트 만들기
`/home/dudu/comfy/work/lb_hint.py <크기> <기울기> <굵기>` — 명조(batang.ttc)로 한글을 찍고 팽창·기울임·장체(높이 맞추고 가로 누름)로 «붓글씨 형태»만 만든다 → `hint_mask.png`(흰 글자) · `hint_canny.png`(윤곽) · `hint_layout.png`(원본 위 확인).
힌트는 형태다 — 최종 그림은 모델이 입힌 질감이어야 한다(글꼴 티가 나면 실패). 원본 참조는 하니스 캡처(`lb_title_4x.png`, 160×120 을 4배).

## 그 다음 (1-f7 몫)
생성 PNG → 팔레트·칸 규칙·타일 예산으로 양자화 → 그림 아이템에 넣기 → 원본/한글 나란히 캡처 → 왕복 증명.

## 함정
- WSL 파이썬 3.14 로는 torch 휠이 없다 — venv 는 3.12.
- 첫 실행 때 `IPAdapterUnifiedLoader` 가 clip_vision 파일 이름을 못 찾으면 `models/clip_vision/` 이름을 `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` 로 맞춘다(그 이름으로 받아 두었다).
- 12GB 라 SDXL 1024×768 + ControlNet + IP-Adapter 는 넉넉하지만, FLUX 는 fp8 경계.

## 2026-09-05 17:35 첫 검증 (월화 4장) — claude-eb
- 모델 넷 다 내려옴(17:28). 공통 실행기 , 힌트 .
- 시간: 첫 장 37s(모델 적재 포함), 그 뒤 **장당 16s** — 4장 65~85s. 생성은 병목이 아니다. 병목은 양자화·삽입·캡처(게임당 도구 손질).
- 결과: denoise 0.62(img2img)는 원본 라틴 글자가 남아 실패. **denoise 1.0 · ControlNet 1.0 · IP-Adapter 0.7** 이 정답 — 「월화의 검사」가 SNK 로고 질감(주황 그라데이션·감색 테·흰 하이라이트)으로 나온다. 0.85/0.5 도 됨. 시트 .
- 부제 띠(「Beyond the Destiny」)는 모델이 가짜 라틴을 채운다 → 양자화 때 마스크로 원본 띠를 보존(quantize_logo --mask).
- 다음: SS2 (참조 jp_logo 4×를 640×480 으로 레터박스, 힌트 「사무라이/쇼다운!」 두 줄, 「2」·칼·리본은 마스크 보존).

## 2026-09-05 17:35 첫 검증 (월화 4장) — claude-eb
- 모델 넷 다 내려옴(17:28). 공통 실행기 `/home/dudu/comfy/work/comfy_run.py <작업폴더> <참조.png> <획힌트.png> <접두사> [seed denoise cn ip 장수 프롬프트파일]`, 힌트 `work/hint_text.py <폴더> <참조4x> x0 y0 x1 y1 기울기 굵기 줄…`.
- 시간: 첫 장 37s(모델 적재 포함), 그 뒤 **장당 16s** — 4장 65~85s. 생성은 병목이 아니다. 병목은 양자화·삽입·캡처(게임당 도구 손질).
- 결과: denoise 0.62(img2img)는 원본 라틴 글자가 남아 실패. **denoise 1.0 · ControlNet 1.0 · IP-Adapter 0.7** 이 정답 — 「월화의 검사」가 SNK 로고 질감(주황 그라데이션·감색 테·흰 하이라이트)으로 나온다. 0.85/0.5 도 됨. 시트 `~/ss2/work_lang/v10/logo/eb/gen/`.
- 부제 띠(「Beyond the Destiny」)는 모델이 가짜 라틴을 채운다 → 양자화 때 마스크로 원본 띠를 보존(quantize_logo --mask).
- 참조가 4:3 이 아니면(SS2 160×88) 640×480 으로 레터박스해서 넣는다(그래프가 1024×768 로 맞추므로 비율이 일그러진다).
- 그림 넣기 순서(본부 2026-09-05): SS2 로고 → SS2 붓글씨 배너(평면1 지도 + 문자RAM 타일, 자산 카드 knowledge/gfx-ss2/ASSET_CARDS.md) → 월화·메탈·카드·아랑·R-2·SvC.

## 2026-09-05 18:10 SS2 배너 「승부」 첫 성공 — claude-eb
- 그림 글자(붓글씨)는 **img2img 로 간다**: ControlNet canny 만으로는 SDXL 이 도형·바탕을 뒤집어 칸을 통째로 빨갛게 칠한다(시도 4번 다 실패).
  되는 설정 = 참조·잠재 둘 다 «빨간 글자 / 검은 바탕» 초기 그림(힌트 마스크를 색칠한 것) · **denoise 0.75** · ControlNet 0.35 · IP-Adapter 0.25.
  힌트는 형태만 주고 획은 모델이 다시 그린다(붓 들어감·빠짐, 굵기 변화가 생긴다 — 글꼴 티 없음).
- 파이프라인: (프롬프트 파일에  줄로 부정 프롬프트) → 상자 잘라 1배 축소·2값화 → 팔레트 색칠 → 이식소 (--merge) → 화면 캡처.
- 도구:  (plan/quant/build/show) — 자산 JSON 의 «그릴 수 있는 칸»을 그림으로 보여 준다. 삽입은 이식소 도구를 쓴다.
- **한패 자산의 벽**:  는 지금 한글 글자가 잉크를 놓은 칸에만 타일이 있다(그릴 수 있는 칸 40/108, 모양도 들쭉날쭉). 순정  는 66칸 직사각형이라 새 글자가 그대로 들어간다.
  → 새 붓글씨를 한패에 넣으려면 **한패 쪽 타일 배정을 순정처럼 넓혀야** 한다(지도 손질 = 이식소 몫). 이번 시범은 순정 롬에 넣어 화면으로 확인했다: .

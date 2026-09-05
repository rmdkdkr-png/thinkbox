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

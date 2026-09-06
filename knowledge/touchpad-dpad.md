# 화면 십자키 — 다른 에뮬과 견주고 고칠 자리 (이식소, 2026-09-06)

유저: **「Dpad 터치 매핑이 다른 에뮬보다 별로다. MAME 나 NGP.emu 좀 보고 와라.」**

## 남들은 이렇게 한다

### NGP.emu (emu-ex-plus-alpha, `EmuFramework/src/vcontrols/VControllerDPad.cc`)
- 각도 섹터가 **아니다**. **축 기준 문턱**: `c.x > xDeadzone` 이면 →, `c.y < -yDeadzone` 이면 ↑.
- **★ 교차 데드존** — 한 축을 많이 밀수록 «다른 축의 문턱이 올라간다»:
  `if (abs(c.x) > deadzonePixels) yDeadzone += (abs(c.x) - deadzonePixels) * diagonalSensitivity;`
  곧 **대각의 어려움을 연속적으로 조절**한다. `diagonalSensitivity` 는 0.01~1.0 설정값.
- 데드존이 **실치수**(1.00~3.00 mm). 패드 크기 비율이 아니다 — 패드를 키워도 느낌이 안 변한다.
- 입력 영역 `padArea` 가 그린 것(`padBaseArea`)의 **1.5배**.

### MAME4droid (`.../input/TouchController.java`)
- **3×3 사각 격자**. 데드존 **없음** — 칸 안이면 무조건 그 방향.
- 대각이 **제 칸**을 갖는다(코너 셀). 2/4/8방향 모드를 고를 수 있다.
- 좌표가 레이아웃 파일에 있어 **그림과 판정을 따로** 둔다(`fixControllerCoords`).

## 우리 것의 흠 — **그림과 판정이 다르다**

`PadView.java`
- 그리기(`:388~398`): **팔 넷짜리 십자**. 팔 반폭 `R*0.42`, **네 귀퉁이는 빈칸**.
- 판정(`dpadDir`, `:526~548`): **8방향 각도 섹터**. 정방향 48° · 대각 42°.

→ **대각이 화면에 없다.** 유저는 십자를 보는데 빈 귀퉁이를 누르면 대각이 나간다.
  「안 눌리는 데를 눌렀는데 딴 게 나온다」로 겪는다.

둘째: **정방향과 대각이 거의 같은 넓이**(48/42). 남들은 정방향을 우대한다 —
MAME 은 격자 구조로, NGP.emu 는 교차 데드존으로. 격투에서 ←홀드 가드가 ↙로 샌다.

셋째: **조절 항목이 없다.**

(입력 캡처 반경은 `1.35 * R`(`:650`)로 이미 넓다. 데드존도 유저가 「아닌 듯」이라 했다. 이 둘은 흠이 아니다.)

## ★ 격자냐 여덟 갈래냐 — **여덟 갈래를 권한다**

MAME 이 격자인 것은 **패드가 네모 이미지**라서다. 우리는 사정이 다르다:

1. 우리 판정은 **이미 각도**이고 **붙잡기(히스테리시스)**가 있다. 격자로 바꾸면 둘 다 버린다.
2. 우리 캡처 영역은 **원**(1.35R)이다. 네모 격자를 얹으면 «또» 그림과 판정이 어긋난다.
3. 여덟 갈래는 **정방향/대각 넓이를 연속으로 조절**할 수 있다 — 격자는 못 한다.
4. 우리와 사정이 같은 쪽(벡터·원형)은 NGP.emu 이고, 그쪽이 각도 계열이다.

**곧 「판정을 그림에 맞추는」 게 아니라 「그림을 판정에 맞춘다」.** 고칠 곳이 그리기 쪽이라
위험이 작다 — 입력 규칙은 넓이 표만 바뀐다.

## 붙일 조각

### ① 표 하나에서 판정각과 그리는 각이 같이 나온다

```java
/* 0:R 1:UR 2:U 3:UL 4:L 5:DL 6:D 7:DR — 중심각은 d*45도 */
private static final int[] DIR_BIT = {
    1 << Emu.RIGHT,
    (1 << Emu.RIGHT) | (1 << Emu.UP),
    1 << Emu.UP,
    (1 << Emu.UP) | (1 << Emu.LEFT),
    1 << Emu.LEFT,
    (1 << Emu.LEFT) | (1 << Emu.DOWN),
    1 << Emu.DOWN,
    (1 << Emu.DOWN) | (1 << Emu.RIGHT),
};
/* 대각 민감도 — {정방향 반폭, 대각 반폭}. 4*(2a) + 4*(2b) = 360 이어야 빈틈이 없다. */
private static final float[][] DPAD_SPAN = {
    { 30f, 15f },   /* 좁게   정방향 60 · 대각 30 — 가드가 안 샌다 */
    { 27f, 18f },   /* 보통   54 / 36  (기본) */
    { 24f, 21f },   /* 넓게   48 / 42  — 지금 값 */
};
private int diagPref = 1;                 /* 설정 「대각 민감도」 */
private int dpadLastDir = -1;             /* 붙잡기용 — 옛 dpadLast(비트) 대신 방향 번호 */

private float dpadHalf(int d)   { return DPAD_SPAN[diagPref][(d & 1) == 0 ? 0 : 1]; }
private float dpadCenter(int d) { return d * 45f; }
```

### ② 판정

```java
private int dpadDir(float x, float y) {
    int di = dpadIndex();
    if (di < 0) return 0;
    float dx = x - cx(di), dy = y - cy(di), R = radOf(di);
    /* 데드존 — 잡혀 있으면 더 작게(놓기 어렵게). 지금 값 그대로 둔다. */
    float dead = R * (dpadLastDir >= 0 ? 0.07f : 0.12f);
    if (dx * dx + dy * dy < dead * dead) { dpadLastDir = -1; return 0; }
    float ang = (float) Math.toDegrees(Math.atan2(-dy, dx));
    if (ang < 0) ang += 360f;
    /* 붙잡기 — 지금 방향의 섹터를 «+6도» 넘어야 놓는다 */
    if (dpadLastDir >= 0
            && angDist(ang, dpadCenter(dpadLastDir)) <= dpadHalf(dpadLastDir) + 6f)
        return DIR_BIT[dpadLastDir];
    for (int d = 0; d < 8; d++)
        if (angDist(ang, dpadCenter(d)) <= dpadHalf(d)) {
            dpadLastDir = d; return DIR_BIT[d];
        }
    /* 경계에서 부동소수로 새면 가장 가까운 중심으로 */
    int d = Math.round(ang / 45f) & 7;
    dpadLastDir = d; return DIR_BIT[d];
}
```

### ③ 그리기 — **판정과 같은 각으로** 여덟 갈래

```java
/* ⚠ 각 규약이 둘이다. 우리 수학각은 «반시계»(0=오른쪽, atan2(-dy,dx)),
   Canvas.drawArc/Path.arcTo 는 «시계»다. 그래서 화면각 = −수학각.
   섹터 [c−h, c+h] → arcTo(oval, −(c+h), 2h). 여기서 부호를 놓치면 상하가 뒤집힌다. */
private final RectF dpadOval = new RectF();
private final Path  dpadPath = new Path();

// ... 그리기 루프의 b == -1 가지를 통째로 갈아 끼운다
float dcx = cx(i), dcy = cy(i), R = radOf(i);
dpadOval.set(dcx - R, dcy - R, dcx + R, dcy + R);
for (int d = 0; d < 8; d++) {
    float h = dpadHalf(d), c0 = dpadCenter(d);
    boolean on = dpadMask != 0 && (dpadMask & DIR_BIT[d]) == DIR_BIT[d]
                 && Integer.bitCount(dpadMask) == Integer.bitCount(DIR_BIT[d]);
    fill.setColor(on ? 0x77ffffff
                     : ((d & 1) == 0 ? 0x33ffffff : 0x1fffffff));  /* 대각은 살짝 어둡게 */
    dpadPath.reset();
    dpadPath.moveTo(dcx, dcy);
    dpadPath.arcTo(dpadOval, -(c0 + h) + 1.2f, 2f * h - 2.4f);     /* 갈래 사이 틈 */
    dpadPath.close();
    c.drawPath(dpadPath, fill);
}
fill.setColor(0x22ffffff);
c.drawCircle(dcx, dcy, R * 0.12f, fill);      /* 가운데 중립 — 데드존과 같은 크기 */
```

**대각을 살짝 어둡게** 칠하면 「여기는 대각이다」가 눈에 들어오면서도 정방향이 먼저 읽힌다.
가운데 원은 **데드존과 같은 크기**로 그린다 — 안 그리면 또 그림과 판정이 어긋난다.

### ④ 설정 항목

`대각 민감도` — 좁게 / 보통 / 넓게 (기본 **보통**). 값은 `diagPref` 로 바로 간다.
NGP.emu 가 같은 것을 설정으로 뺐다. 「가드가 샌다」와 「대각이 안 나온다」는 사람마다 갈린다.

## 곁들여 — 짧은 탭이 새는 것 (실측)

`EmuActivity.onDrawFrame` 이 프레임당 한 번 `padMask` 를 읽는다. 그래서 짧은 탭이 샌다.
**코어 쪽 실측** (SvC, 캐릭 6 × 위상 6 = 36회):

| 누른 프레임 | 점프 성공 |
|---|---|
| **1** | **18/36 — 딱 50%** |
| 2 | 36/36 |
| 3 | 36/36 |
| 4 | 36/36 |

**1프레임은 동전 던지기**다(캐릭터를 안 가리고 위상이 반반). **2프레임부터 확실**하다.
→ 앱의 「방향 비트가 새로 서면 최소 3프레임 살린다」 걸쇠는 **여유 있게 맞는 처방**이다.
⚠ **버튼(A·B)에는 걸지 마라** — 「탭=약 / 꾹=강」 문턱이 6~8프레임이라 길이를 늘리면 약이 강이 된다.

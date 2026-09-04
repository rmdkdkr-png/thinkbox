# 카드 파이터즈 클래시 1 — 한글 번역 텍본 (고증 검수용)

원문과 번역을 나란히 둔 것입니다. **틀린 곳을 짚어 주시면**
그대로 고칩니다. 롬을 안 열어도 읽을 수 있게 만들었습니다.

- `자리` 는 롬 안 포인터 주소입니다. 고칠 때 이걸로 짚어 주세요.
- `n → m바이트` 는 원문 자리와 번역 길이입니다.
  넘치면 빈 곳으로 옮겨 담으므로 길이는 제약이 아닙니다.
- `{XX}` 는 게임이 채우는 자리입니다. **그대로 있어야** 합니다.
  `{08}` 플레이어 이름 · `{09}` 상대 이름 · `{0A}` 카드 이름
  `{0E}` 숫자 · `{17}` 능력 이름 · `{0C}{0D}` 예/아뇨 선택줄

대상: SNK판 `crc32 94B63A97` · 캡콤판 `crc32 80CE137B`
(두 판이 같은 표를 쓰므로 번역도 공통입니다)

## 차림표·안내·용어집 (35개)

게임을 켜고 바로 보이는 글과 용어 설명입니다.

### `070004`  22 → 20바이트

```
원문 | BEGIN GAME FROM START.
```

```
번역 | 처음부터 시작합니다.
```

### `070008`  18 → 23바이트  (빈 곳으로 옮겨 담음)

```
원문 | EXPLAIN GAME PLAY.
```

```
번역 | 게임 방법을 알려줍니다.
```

### `07000C`  31 → 33바이트  (빈 곳으로 옮겨 담음)

```
원문 | REVIEW TITLES
원문 | DISPLAYED SO FAR.
```

```
번역 | 지금까지 나온 제목을
번역 | 다시 봅니다.
```

### `070010`  33 → 28바이트

```
원문 | SEE NEOGEO POCKET
원문 | FIGHTING INTRO.
```

```
번역 | 네오지오 포켓
번역 | 격투 소개 보기
```

### `070014`  32 → 42바이트  (빈 곳으로 옮겨 담음)

```
원문 | ERROR OCCURRED.
원문 | SAVED DATA LOST.
```

```
번역 | 오류가 났습니다.
번역 | 저장 자료가 지워졌습니다.
```

### `070018`  19 → 19바이트

```
원문 | PLAY INFO
원문 | TERM INFO
```

```
번역 | 게임 안내
번역 | 용어 설명
```

### `07001C`  26 → 28바이트  (빈 곳으로 옮겨 담음)

```
원문 | EXPLAIN CARD BATTLE RULES.
```

```
번역 | 카드 대전 규칙을 알려줍니다.
```

### `070020`  14 → 19바이트  (빈 곳으로 옮겨 담음)

```
원문 | SEE TERM INFO.
```

```
번역 | 용어 설명을 봅니다.
```

### `070024`  17 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE CHARACTER.
```

```
번역 | 캐릭터를 고르세요.
```

### `070028`  48 → 47바이트

```
원문 | CARD GAME BEGINNERS
원문 | PREFER TO COLLECT SNK CARDS.
```

```
번역 | 카드 게임이 처음이면
번역 | SNK 카드를 모으는 게 좋다.
```

### `07002C`  50 → 36바이트

```
원문 | GIRLS FROM WEST JAPAN
원문 | PREFER TO COLLECT SNK CARDS.
```

```
번역 | 서일본 여자아이는
번역 | SNK 카드를 모은다.
```

### `070030`  62 → 48바이트

```
원문 | PREVIOUS SC CARD CLASH WINNERS
원문 | PREFER TO COLLECT CAPCOM CARDS.
```

```
번역 | 지난 SC 카드 클래시 우승자는
번역 | 캡콤 카드를 모은다.
```

### `070034`  49 → 33바이트

```
원문 | CAP'S KID SISTER PREFERS TO
원문 | COLLECT CAPCOM CARDS.
```

```
번역 | 캡의 여동생은 캡콤
번역 | 카드를 모은다.
```

### `070038`  5 → 11바이트  (빈 곳으로 옮겨 담음)

```
원문 | OK?
원문 | {0C}
```

```
번역 | 맞습니까?
번역 | {0C}
```

### `07003C`  39 → 35바이트

```
원문 | ENTER NAME.
원문 | (PUSH OPTION BUTTON TO END)
```

```
번역 | 이름을 넣으세요.
번역 | (OPTION 으로 끝냄)
```

### `070040`  5 → 11바이트  (빈 곳으로 옮겨 담음)

```
원문 | OK?
원문 | {0C}
```

```
번역 | 맞습니까?
번역 | {0C}
```

### `070044`  35 → 28바이트

```
원문 | PREVIOUS DATA TO BE DELETED.
원문 | 
원문 | OK?
원문 | {0D}
```

```
번역 | 전 자료가 지워집니다.
번역 | 
번역 | OK?
번역 | {0D}
```

### `070048`  12 → 16바이트  (빈 곳으로 옮겨 담음)

```
원문 | END ENTRY?
원문 | {0D}
```

```
번역 | 그만 넣을까요?
번역 | {0D}
```

### `07004C`  3 → 2바이트

```
원문 | END
```

```
번역 | 끝
```

### `070058`  24 → 19바이트

```
원문 | START GAME
원문 | EXPLAIN RULES
```

```
번역 | 게임 시작
번역 | 규칙 설명
```

### `07005C`  33 → 28바이트

```
원문 | CONTINUE
원문 | START GAME
원문 | EXPLAIN RULES
```

```
번역 | 이어하기
번역 | 게임 시작
번역 | 규칙 설명
```

### `07006C`  9 → 7바이트

```
원문 | PLAY TIME
```

```
번역 | 논 시간
```

### `070070`  5 → 4바이트

```
원문 | ALBUM
```

```
번역 | 앨범
```

### `070078`  18 → 19바이트  (빈 곳으로 옮겨 담음)

```
원문 | OK TO SAVE DATA?
원문 | {0D}
```

```
번역 | 자료를 저장할까요?{0D}
```

### `07007C`  11 → 13바이트  (빈 곳으로 옮겨 담음)

```
원문 | DATA SAVED.
```

```
번역 | 저장했습니다.
```

### `070084`  33 → 34바이트  (빈 곳으로 옮겨 담음)

```
원문 | SAVING DATA.
원문 | DON'T TURN UNIT OFF.
```

```
번역 | 저장 중입니다.
번역 | 전원을 끄지 마세요.
```

### `070090`  11 → 9바이트

```
원문 | ACTION CARD
```

```
번역 | 액션 카드
```

### `070094`  10 → 9바이트

```
원문 | NO ABILITY
```

```
번역 | 능력 없음
```

### `0700A0`  9 → 9바이트

```
원문 | 1
원문 | 2
원문 | 3
원문 | 4
원문 | 5
```

```
번역 | 1/2/3/4/5
```

### `0700A8`  11 → 12바이트  (빈 곳으로 옮겨 담음)

```
원문 | REMAKE DECK
```

```
번역 | 덱 다시 짜기
```

### `0700B4`  46 → 42바이트

```
원문 | DECK CAN'T BE FORMED
원문 | WITHOUT 50 OR MORE CARDS.
```

```
번역 | 카드가 50장이 안 되면
번역 | 덱을 짤 수 없습니다.
```

### `0700BC`  38 → 35바이트

```
원문 | NO DECK AVAILABLE.
원문 | MAKE DECK FOR GAME.
```

```
번역 | 쓸 덱이 없습니다.
번역 | 덱을 먼저 짜세요.
```

### `0700C0`  10 → 9바이트

```
원문 | CARD ALBUM
```

```
번역 | 카드 앨범
```

### `070104`  11 → 16바이트  (빈 곳으로 옮겨 담음)

```
원문 | SELECT CARD
```

```
번역 | 카드를 고르세요.
```

### `070108`  6 → 4바이트

```
원문 | DECIDE
```

```
번역 | 결정
```


## 카드 효과 설명 (613개)

대전 중 카드를 고를 때마다 나옵니다. 규칙 용어가 많아
**용어를 통일하는 것이 중요**합니다 — 링·손패·더미·버린 패·
얼음·백업·합체 공격·되받기·캐릭터 카드·액션 카드.

### `070640`  94 → 68바이트

```
원문 | Shuffles Pile after all Hand cards
원문 | are returned. During this turn,
원문 | Discards become hand cards.
```

```
번역 | 손패를 모두 더미로 돌린 뒤
번역 | 섞는다. 이 턴 동안
번역 | 버린 패가 손패가 된다.
```

### `070644`  67 → 33바이트

```
원문 | Keeps character out of Freeze
원문 | Phase even if this character
원문 | attacks.
```

```
번역 | 공격해도 이 캐릭터는
번역 | 얼지 않는다.
```

### `070648`  46 → 32바이트

```
원문 | Randomly selects 1 enemy card
원문 | and discards it.
```

```
번역 | 상대 카드 1장을
번역 | 무작위로 버린다.
```

### `07064C`  69 → 49바이트

```
원문 | Draw up to 2 cards from enemy's
원문 | pile and put in enemy's discard
원문 | pile.
```

```
번역 | 상대 더미에서 2장까지
번역 | 뽑아 상대 버린 패로
번역 | 보낸다.
```

### `070650`  76 → 50바이트

```
원문 | Discards hand and lets you pick
원문 | the same number of new cards
원문 | + 1 extra card.
```

```
번역 | 손패를 다 버리고
번역 | 같은 수보다 1장 많게
번역 | 새로 뽑는다.
```

### `070654`  76 → 60바이트

```
원문 | See enemy's cards. If there're
원문 | AC Cards,may place 1 on enemy's
원문 | discard deck.
```

```
번역 | 상대 손패를 본다.
번역 | 액션 카드가 있으면
번역 | 1장을 버린 패로 보낸다.
```

### `07065C`  34 → 29바이트

```
원문 | Raise 1 character's
원문 | BP 300 points.
```

```
번역 | 캐릭터 1명의
번역 | BP를 300 올린다.
```

### `070660`  71 → 58바이트

```
원문 | Keeps 1 enemy character
원문 | (in Freeze Phase) frozen
원문 | for next Action Phase.
```

```
번역 | 얼어 있는 상대 캐릭터를
번역 | 다음 행동 단계까지
번역 | 계속 얼려 둔다.
```

### `07066C`  42 → 36바이트

```
원문 | Freezes any other character than
원문 | this one.
```

```
번역 | 이 캐릭터 말고
번역 | 다른 캐릭터를 얼린다.
```

### `070670`  78 → 56바이트

```
원문 | KOs 1 other character in your
원문 | ring. BP rises according to KOed
원문 | character's BP.
```

```
번역 | 내 링의 다른 캐릭터를
번역 | 쓰러뜨린다. 그 BP만큼
번역 | BP가 오른다.
```

### `070680`  40 → 35바이트

```
원문 | Lets this character attack in
원문 | this turn.
```

```
번역 | 이 턴에 이 캐릭터가
번역 | 공격할 수 있다.
```

### `070690`  79 → 56바이트

```
원문 | Selects AC Card from your hand
원문 | and discards it. Get 1 SP for each
원문 | card in hand.
```

```
번역 | 손패의 액션 카드를
번역 | 골라 버린다. 손패 수만큼
번역 | SP를 얻는다.
```

### `070698`  24 → 19바이트

```
원문 | Lowers enemy's SP 3 pts.
```

```
번역 | 상대 SP를 3 내린다.
```

### `0706A0`  54 → 39바이트

```
원문 | Shuffles deck after this
원문 | character's returned to deck.
```

```
번역 | 이 캐릭터를 덱으로
번역 | 돌린 뒤 덱을 섞는다.
```

### `0706A4`  88 → 60바이트

```
원문 | Discards entire hand. Shuffles
원문 | deck after 1 card's selected from
원문 | deck and added to hand.
```

```
번역 | 손패를 다 버린다.
번역 | 덱에서 1장을 골라 손패에
번역 | 넣고 덱을 섞는다.
```

### `0706B4`  65 → 46바이트

```
원문 | After seeing the deck's top
원문 | 3 cards, rearrange them in any
원문 | order.
```

```
번역 | 덱 맨 위 3장을 보고
번역 | 원하는 차례로 다시
번역 | 놓는다.
```

### `0706B8`  71 → 56바이트

```
원문 | Draws 1 AC card from hand and
원문 | discards it. Gives enemy 300 pts.
원문 | damage.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다. 상대에게
번역 | 300 피해를 준다.
```

### `0706BC`  49 → 40바이트

```
원문 | Give enemy damage when this
원문 | character's attacked.
```

```
번역 | 이 캐릭터가 맞으면
번역 | 상대에게 피해를 준다.
```

### `0706C0`  75 → 54바이트

```
원문 | KOs this character at the end of
원문 | the turn if he attacks or counter
원문 | attacks.
```

```
번역 | 공격하거나 되받으면
번역 | 턴이 끝날 때 이 캐릭터가
번역 | 쓰러진다.
```

### `0706C4`  36 → 26바이트

```
원문 | Returns this character to your
원문 | hand.
```

```
번역 | 이 캐릭터를 손패로
번역 | 돌린다.
```

### `0706C8`  12 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | Draw 1 card.
```

```
번역 | 카드를 1장 뽑는다.
```

### `0706D0`  84 → 62바이트

```
원문 | After your turn ends, gives all
원문 | "frozen" characters in enemy's
원문 | Ring 200 pts. damage.
```

```
번역 | 내 턴이 끝나면 상대 링의
번역 | 얼어 있는 캐릭터에게
번역 | 200 피해를 준다.
```

### `0706D4`  12 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | Draw 1 card.
```

```
번역 | 카드를 1장 뽑는다.
```

### `0706DC`  26 → 25바이트

```
원문 | Freezes 1 enemy character.
```

```
번역 | 상대 캐릭터 1명을 얼린다.
```

### `0706E8`  80 → 55바이트

```
원문 | Raises the BP of all characters
원문 | in your ring (including this
원문 | character) 100 pts.
```

```
번역 | 이 캐릭터를 포함해
번역 | 내 링의 모든 캐릭터
번역 | BP를 100 올린다.
```

### `0706EC`  17 → 17바이트

```
원문 | See enemy's hand.
```

```
번역 | 상대 손패를 본다.
```

### `0706F8`  40 → 27바이트

```
원문 | Disables this character's
원문 | counterattack.
```

```
번역 | 이 캐릭터는
번역 | 되받을 수 없다.
```

### `0706FC`  40 → 29바이트

```
원문 | Disables [ Abilities for all
원문 | characters.
```

```
번역 | 모든 캐릭터의
번역 | [능력을 막는다.
```

### `070700`  48 → 43바이트

```
원문 | KOs this character. Discards all
원문 | players' hands.
```

```
번역 | 이 캐릭터가 쓰러지고
번역 | 서로 손패를 다 버린다.
```

### `070704`  34 → 26바이트

```
원문 | Ends all characters' Freeze Phase.
```

```
번역 | 모든 캐릭터의 얼음을 푼다.
```

### `07070C`  77 → 60바이트

```
원문 | KOs this character. Decreases 1
원문 | character's (selected randomly)
원문 | Life 500 pts.
```

```
번역 | 이 캐릭터가 쓰러지고
번역 | 무작위로 고른 캐릭터
번역 | 체력을 500 줄인다.
```

### `070710`  30 → 33바이트  (빈 곳으로 옮겨 담음)

```
원문 | Skips enemy's next Draw Phase.
```

```
번역 | 상대의 다음 뽑기
번역 | 단계를 건너뛴다.
```

### `070714`  37 → 41바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs 1 of your characters.
원문 | Get 200 HP.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | HP를 200 얻는다.
```

### `070718`  40 → 31바이트

```
원문 | Raises each player's AC Card
원문 | Cost 3 pts.
```

```
번역 | 서로 액션 카드 비용이
번역 | 3 오른다.
```

### `07071C`  60 → 35바이트

```
원문 | Draw 1 discarded card,
원문 | return to deck, and deck is
원문 | shuffled.
```

```
번역 | 버린 패 1장을
번역 | 덱으로 돌리고 섞는다.
```

### `070724`  79 → 67바이트

```
원문 | KOs all other characters in your
원문 | Ring. Raises SP 3 pts for each
원문 | KOed character.
```

```
번역 | 내 링의 다른 캐릭터가
번역 | 모두 쓰러진다. 쓰러진
번역 | 수만큼 SP가 3씩 오른다.
```

### `07072C`  50 → 36바이트

```
원문 | Disables this character's attacks,
원문 | counterattacks.
```

```
번역 | 이 캐릭터는 공격도
번역 | 되받기도 못 한다.
```

### `070730`  31 → 23바이트

```
원문 | Decreases enemy's Life 500 pts.
```

```
번역 | 상대 체력을 500 줄인다.
```

### `070734`  50 → 37바이트

```
원문 | Lowers enemy's or an enemy
원문 | character's HP 300 pts.
```

```
번역 | 상대나 상대 캐릭터의
번역 | HP를 300 내린다.
```

### `070738`  59 → 46바이트

```
원문 | Lowers this character's and 1
원문 | enemy character's HP 500 pts.
```

```
번역 | 이 캐릭터와 상대 캐릭터
번역 | 1명의 HP를 500 내린다.
```

### `070740`  63 → 47바이트

```
원문 | Steal up to 3 SPs from enemy when
원문 | this character damages enemy.
```

```
번역 | 이 캐릭터가 피해를 주면
번역 | 상대 SP를 3까지 뺏는다.
```

### `070744`  43 → 36바이트

```
원문 | Decreases 1 other character's
원문 | Life 200 pts.
```

```
번역 | 다른 캐릭터 1명의
번역 | 체력을 200 줄인다.
```

### `070750`  16 → 14바이트

```
원문 | Raises SP 3 pts.
```

```
번역 | SP를 3 올린다.
```

### `070760`  31 → 27바이트

```
원문 | Shuffles yours or enemy's deck.
```

```
번역 | 내 덱이나 상대 덱을
번역 | 섞는다.
```

### `070764`  31 → 23바이트

```
원문 | Decreases enemy's Life 200 pts.
```

```
번역 | 상대 체력을 200 줄인다.
```

### `070768`  64 → 48바이트

```
원문 | Decreases this character's and 1
원문 | enemy character's Life 300 pts.
```

```
번역 | 이 캐릭터와 상대 캐릭터
번역 | 1명의 체력을 300 줄인다.
```

### `07076C`  96 → 72바이트

```
원문 | Selects 1 AC card from hand and
원문 | discards it. 1 character loses
원문 | Abilities and its BP becomes 100.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다. 캐릭터 1명이
번역 | 능력을 잃고 BP가 100이 된다.
```

### `070770`  40 → 27바이트

```
원문 | Disables this character's
원문 | counterattack.
```

```
번역 | 이 캐릭터는
번역 | 되받을 수 없다.
```

### `070774`  48 → 39바이트

```
원문 | Returns 1 other character to its
원문 | original owner.
```

```
번역 | 다른 캐릭터 1명을
번역 | 원래 주인에게 돌린다.
```

### `070778`  53 → 44바이트

```
원문 | Disables enemy character's
원문 | attack in next enemy turn.
```

```
번역 | 다음 상대 턴에
번역 | 상대 캐릭터가 공격을
번역 | 못 한다.
```

### `070784`  30 → 19바이트

```
원문 | Reduces each player's SP to 0.
```

```
번역 | 서로 SP가 0이 된다.
```

### `070790`  85 → 65바이트

```
원문 | KOs 1 character whose BP is
원문 | 800 or more (or this character if
원문 | another's unavailable).
```

```
번역 | BP가 800 이상인 캐릭터를
번역 | 쓰러뜨린다. 없으면
번역 | 이 캐릭터가 쓰러진다.
```

### `070794`  82 → 58바이트

```
원문 | Gives 400 pts. damage to 1
원문 | character (or this character if
원문 | another's unavailable).
```

```
번역 | 캐릭터 1명에게
번역 | 400 피해를 준다. 없으면
번역 | 이 캐릭터가 받는다.
```

### `070798`  45 → 37바이트

```
원문 | Decreases all other character's
원문 | Life 300 pts.
```

```
번역 | 다른 모든 캐릭터의
번역 | 체력을 300 줄인다.
```

### `0707A4`  40 → 30바이트

```
원문 | Uses up 2 SPs at beginning of
원문 | your turn.
```

```
번역 | 내 턴이 시작될 때
번역 | SP를 2 쓴다.
```

### `0707AC`  40 → 42바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs all characters (including
원문 | this one).
```

```
번역 | 이 캐릭터를 포함해
번역 | 모든 캐릭터가 쓰러진다.
```

### `0707B0`  87 → 58바이트

```
원문 | Draws 1 Ability (]) CHA Card and
원문 | discards it. Mimics same effect
원문 | of drawn Ability card.
```

```
번역 | ]능력이 있는 캐릭터
번역 | 카드를 1장 버리고
번역 | 그 능력을 흉내 낸다.
```

### `0707D0`  68 → 41바이트

```
원문 | Nullifies damage when this
원문 | character counterattacks a
원문 | United Attack.
```

```
번역 | 합체 공격을 되받을 때
번역 | 피해를 받지 않는다.
```

### `0707D4`  54 → 51바이트

```
원문 | KOs this character. Get 100 HPs
원문 | for each card in hand.
```

```
번역 | 이 캐릭터가 쓰러지고
번역 | 손패 장수마다 HP를
번역 | 100 얻는다.
```

### `0707DC`  91 → 61바이트

```
원문 | Draws 1 CHA Card from hand and
원문 | discards it (KOs this character if
원문 | no CHA Card's available).
```

```
번역 | 손패의 캐릭터 카드를
번역 | 1장 버린다. 없으면
번역 | 이 캐릭터가 쓰러진다.
```

### `0707E0`  83 → 56바이트

```
원문 | BP becomes same as 1 enemy
원문 | character's. Valid only when
원문 | character is in enemy ring.
```

```
번역 | BP가 상대 캐릭터와
번역 | 같아진다. 상대 링에
번역 | 있을 때만 통한다.
```

### `0707E4`  65 → 57바이트

```
원문 | Selects 1 CHA Card from hand.
원문 | BP becomes same as selected
원문 | card's.
```

```
번역 | 손패의 캐릭터 카드를
번역 | 1장 고른다. BP가 그
번역 | 카드와 같아진다.
```

### `0707FC`  52 → 30바이트

```
원문 | BP rises 200 pts. when this
원문 | character attacks alone.
```

```
번역 | 혼자 공격하면
번역 | BP가 200 오른다.
```

### `070810`  87 → 65바이트

```
원문 | Discards hand. All characters but
원문 | this one get 100 pts. damage for
원문 | each discarded card.
```

```
번역 | 손패를 다 버린다.
번역 | 버린 장수마다 이 캐릭터를
번역 | 뺀 모두에게 100 피해.
```

### `070820`  62 → 49바이트

```
원문 | This character damages the
원문 | enemy, enemy takes 600 pts.
원문 | damage.
```

```
번역 | 이 캐릭터가 피해를 주면
번역 | 상대가 600 피해를
번역 | 받는다.
```

### `070824`  77 → 62바이트

```
원문 | Draw 1 AC Card from hand and
원문 | discard it. Decrease 1 character's
원문 | Life 500 pts.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다. 캐릭터 1명의
번역 | 체력을 500 줄인다.
```

### `070828`  67 → 33바이트

```
원문 | Keeps character out of Freeze
원문 | Phase even if this character
원문 | attacks.
```

```
번역 | 공격해도 이 캐릭터는
번역 | 얼지 않는다.
```

### `07082C`  67 → 59바이트

```
원문 | Uses up all SP. All character's
원문 | (except this one's) BP becomes
원문 | 100.
```

```
번역 | SP를 다 쓴다. 이 캐릭터를
번역 | 뺀 모든 캐릭터의 BP가
번역 | 100이 된다.
```

### `070830`  28 → 20바이트

```
원문 | Neutralizes all ] Abilities.
```

```
번역 | 모든 ]능력을 없앤다.
```

### `07083C`  55 → 45바이트

```
원문 | See deck's top card. Card can be
원문 | put at bottom of deck.
```

```
번역 | 덱 맨 위 카드를 본다.
번역 | 맨 아래로 보낼 수 있다.
```

### `070848`  54 → 44바이트

```
원문 | BP rises 100 pts. when enemy
원문 | discards character cards.
```

```
번역 | 상대가 캐릭터 카드를
번역 | 버리면 BP가 100 오른다.
```

### `07084C`  70 → 51바이트

```
원문 | Each player discards all AC cards
원문 | in hand after showing hand to
원문 | enemy.
```

```
번역 | 서로 손패를 보인 뒤
번역 | 손패의 액션 카드를
번역 | 모두 버린다.
```

### `070850`  63 → 43바이트

```
원문 | Shuffles deck after adding one
원문 | JUNI and JULI card to your hand.
```

```
번역 | 유니와 율리 카드를
번역 | 손패에 넣고 덱을 섞는다.
```

### `070864`  67 → 50바이트

```
원문 | See top card of enemy's deck.
원문 | Can be put on bottom of
원문 | enemy's deck.
```

```
번역 | 상대 덱 맨 위 카드를
번역 | 본다. 맨 아래로 보낼 수
번역 | 있다.
```

### `070868`  22 → 29바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs 1 other character.
```

```
번역 | 다른 캐릭터 1명을
번역 | 쓰러뜨린다.
```

### `07086C`  77 → 62바이트

```
원문 | Draw 1 AC Card from hand and
원문 | discard it. Decrease 1 character's
원문 | Life 200 pts.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다. 캐릭터 1명의
번역 | 체력을 200 줄인다.
```

### `070870`  97 → 61바이트

```
원문 | See up to 3 top cards on the
원문 | enemy's deck. Chooses 2 cards and
원문 | puts them on enemy's discard deck.
```

```
번역 | 상대 덱 맨 위 3장까지
번역 | 본다. 2장을 골라 상대
번역 | 버린 패로 보낸다.
```

### `070874`  56 → 39바이트

```
원문 | Disable counter-attack when
원문 | enemy has 1 or no character.
```

```
번역 | 상대 캐릭터가 1명
번역 | 이하면 되받지 못한다.
```

### `070878`  43 → 36바이트

```
원문 | After drawing 4 cards, discard 3
원문 | from hand.
```

```
번역 | 4장을 뽑은 뒤
번역 | 손패에서 3장을 버린다.
```

### `07088C`  27 → 19바이트

```
원문 | Decreases enemy's SP 6 pts.
```

```
번역 | 상대 SP를 6 내린다.
```

### `070890`  46 → 40바이트

```
원문 | BP doubled if your Life
원문 | is 1,000 pts. or less.
```

```
번역 | 내 체력이 1000 이하면
번역 | BP가 두 배가 된다.
```

### `070894`  65 → 43바이트

```
원문 | Shuffles deck after returning all
원문 | discarded AC Cards to the deck.
```

```
번역 | 버린 액션 카드를 모두
번역 | 덱으로 돌리고 섞는다.
```

### `07089C`  71 → 44바이트

```
원문 | Decreases enemy's Life 200 pts
원문 | when this character is
원문 | counter-attacked.
```

```
번역 | 이 캐릭터가 되받히면
번역 | 상대 체력을 200 줄인다.
```

### `0708AC`  87 → 59바이트

```
원문 | When this character damages the
원문 | enemy, AC Cards can't be used in
원문 | the enemy's next turn.
```

```
번역 | 이 캐릭터가 피해를 주면
번역 | 다음 상대 턴에 액션 카드를
번역 | 못 쓴다.
```

### `0708B0`  61 → 41바이트

```
원문 | Allows characters appearing in
원문 | the ring to use Abilities ([).
```

```
번역 | 링에 막 나온 캐릭터도
번역 | [능력을 쓸 수 있다.
```

### `0708B4`  58 → 42바이트

```
원문 | Allows back-up for characters
원문 | appearing in ring this turn.
```

```
번역 | 이 턴에 링에 나온
번역 | 캐릭터도 백업할 수 있다.
```

### `0708B8`  69 → 52바이트

```
원문 | Pick 1 card if your hand's cards
원문 | are less than enemy's at turn's
원문 | end.
```

```
번역 | 턴이 끝날 때 내 손패가
번역 | 상대보다 적으면
번역 | 1장을 뽑는다.
```

### `0708BC`  60 → 49바이트

```
원문 | Raises BPs 100 pts. each time
원문 | enemy adds a card to his hand.
```

```
번역 | 상대가 손패에 카드를
번역 | 더할 때마다 BP가
번역 | 100 오른다.
```

### `0708C0`  66 → 47바이트

```
원문 | Draws 1 AC Card from your hand
원문 | and discards it. Raises HP
원문 | 300 pts.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다.
번역 | HP가 300 오른다.
```

### `0708CC`  68 → 41바이트

```
원문 | Nullifies damage when this
원문 | character counterattacks a
원문 | United Attack.
```

```
번역 | 합체 공격을 되받을 때
번역 | 피해를 받지 않는다.
```

### `0708D4`  65 → 50바이트

```
원문 | When this character counter
원문 | attacks, BP equals enemy
원문 | character's.
```

```
번역 | 이 캐릭터가 되받을 때
번역 | BP가 상대 캐릭터와
번역 | 같아진다.
```

### `0708D8`  75 → 53바이트

```
원문 | Every player lose 1 SP for each
원문 | card in hand at the beginning of
원문 | your turn.
```

```
번역 | 내 턴이 시작될 때
번역 | 서로 손패 장수만큼
번역 | SP를 1씩 잃는다.
```

### `0708E4`  32 → 34바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs 1 character in Freeze Phase.
```

```
번역 | 얼어 있는 캐릭터 1명을
번역 | 쓰러뜨린다.
```

### `0708E8`  40 → 43바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs one of your characters.
원문 | Draw 1 card.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | 카드를 1장 뽑는다.
```

### `0708EC`  58 → 38바이트

```
원문 | This character gets life points
원문 | when it damages the enemy.
```

```
번역 | 이 캐릭터가 피해를 주면
번역 | 체력을 얻는다.
```

### `0708F0`  42 → 39바이트

```
원문 | KOs 1 of your characters. Raises
원문 | SP 8 pts.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | SP가 8 오른다.
```

### `0708F4`  51 → 34바이트

```
원문 | Raises or decreases BP 300 pts.
원문 | (Decided randomly.)
```

```
번역 | BP가 300 오르거나
번역 | 내린다. (무작위)
```

### `070900`  39 → 39바이트

```
원문 | Randomly draws 1 AC Card from
원문 | the deck.
```

```
번역 | 덱에서 액션 카드를
번역 | 무작위로 1장 뽑는다.
```

### `070908`  81 → 69바이트

```
원문 | KOs all other characters in your
원문 | ring. BP rises 300 pts. for each
원문 | KOed character.
```

```
번역 | 내 링의 다른 캐릭터가
번역 | 모두 쓰러진다. 쓰러진
번역 | 수만큼 BP가 300씩 오른다.
```

### `07090C`  56 → 47바이트

```
원문 | All characters lose Abilities
원문 | (this character included).
```

```
번역 | 이 캐릭터를 포함해
번역 | 모든 캐릭터가 능력을
번역 | 잃는다.
```

### `070918`  69 → 51바이트

```
원문 | SP rises 3 pts. at end of your turn
원문 | if your SP is lower than enemy's.
```

```
번역 | 턴이 끝날 때 내 SP가
번역 | 상대보다 적으면
번역 | SP가 3 오른다.
```

### `070920`  52 → 39바이트

```
원문 | Draw 1 card from hand and
원문 | discard. BP rises 300 pts.
```

```
번역 | 손패에서 1장을 버린다.
번역 | BP가 300 오른다.
```

### `070924`  46 → 42바이트

```
원문 | Draw 1 card when this character
원문 | damages enemy.
```

```
번역 | 이 캐릭터가 피해를 주면
번역 | 카드를 1장 뽑는다.
```

### `070928`  86 → 67바이트

```
원문 | KOs everyone but this character.
원문 | Shuffles deck when this
원문 | character's returned to deck.
```

```
번역 | 이 캐릭터만 남고 모두
번역 | 쓰러진다. 이 캐릭터가
번역 | 덱으로 돌아가면 섞는다.
```

### `07092C`  50 → 33바이트

```
원문 | Shuffles the deck when you hold
원문 | all "Q-BEE" cards.
```

```
번역 | Q비 카드를 다 모으면
번역 | 덱을 섞는다.
```

### `070930`  75 → 45바이트

```
원문 | Shuffles deck after all discarded
원문 | character cards are returned to
원문 | the deck.
```

```
번역 | 버린 캐릭터 카드를 모두
번역 | 덱으로 돌리고 섞는다.
```

### `070934`  71 → 62바이트

```
원문 | Discards all AC Cards in your
원문 | hand. Get 200 BP for each
원문 | discarded card.
```

```
번역 | 손패의 액션 카드를
번역 | 모두 버린다. 버린 장수마다
번역 | BP를 200 얻는다.
```

### `070940`  82 → 59바이트

```
원문 | Returns 1 of your characters to
원문 | hand (or this character if
원문 | another's unavailable).
```

```
번역 | 내 캐릭터 1명을 손패로
번역 | 돌린다. 없으면
번역 | 이 캐릭터가 돌아간다.
```

### `070944`  41 → 39바이트

```
원문 | KOs this character and 1 enemy
원문 | character.
```

```
번역 | 이 캐릭터와 상대 캐릭터
번역 | 1명이 쓰러진다.
```

### `070948`  68 → 54바이트

```
원문 | Uses up 10 SPs. (If SP is less than
원문 | 10 pts., this character's KOed.)
```

```
번역 | SP를 10 쓴다. SP가
번역 | 10보다 적으면 이 캐릭터가
번역 | 쓰러진다.
```

### `070958`  91 → 60바이트

```
원문 | SP is not used up when using 1 AC
원문 | Card right after using this
원문 | Ability (for this turn only).
```

```
번역 | 이 능력을 쓴 바로 뒤
번역 | 액션 카드 1장은 SP를
번역 | 안 쓴다. (이 턴만)
```

### `070964`  56 → 46바이트

```
원문 | All characters in ring can use
원문 | [ Abilities in this turn.
```

```
번역 | 이 턴에 링의 모든
번역 | 캐릭터가 [능력을
번역 | 쓸 수 있다.
```

### `070968`  43 → 31바이트

```
원문 | Decreases each player's
원문 | AC Card Cost 2 pts.
```

```
번역 | 서로 액션 카드 비용이
번역 | 2 내린다.
```

### `07096C`  32 → 29바이트

```
원문 | Raises 1 character's BP 200 pts.
```

```
번역 | 캐릭터 1명의
번역 | BP를 200 올린다.
```

### `070970`  86 → 60바이트

```
원문 | Shuffles through Pile for first AC
원문 | card, adds it to Hand, and
원문 | discards shuffled cards.
```

```
번역 | 더미에서 첫 액션 카드를
번역 | 찾아 손패에 넣고
번역 | 뒤진 카드는 버린다.
```

### `070978`  49 → 45바이트

```
원문 | BP doubled when 3 characters
원문 | are in enemy's ring.
```

```
번역 | 상대 링에 캐릭터가
번역 | 3명이면 BP가 두 배가 된다.
```

### `07097C`  51 → 34바이트

```
원문 | Stops Freeze Phase for all
원문 | characters in your ring.
```

```
번역 | 내 링의 모든 캐릭터가
번역 | 얼지 않는다.
```

### `070984`  71 → 64바이트

```
원문 | Randomly discards 1 card from
원문 | hand. Gives 1 of your characters
원문 | 300 BPs.
```

```
번역 | 손패에서 1장을 무작위로
번역 | 버린다. 내 캐릭터 1명의
번역 | BP가 300 오른다.
```

### `070988`  93 → 58바이트

```
원문 | At the beginning of your turn,
원문 | shuffles the deck after this
원문 | character's returned to the deck.
```

```
번역 | 내 턴이 시작될 때
번역 | 이 캐릭터가 덱으로 돌아가고
번역 | 덱을 섞는다.
```

### `070998`  34 → 33바이트

```
원문 | KOs 1 character receiving
원문 | back-up.
```

```
번역 | 백업받은 캐릭터 1명을
번역 | 쓰러뜨린다.
```

### `07099C`  68 → 50바이트

```
원문 | Provides back-up attacks to all
원문 | characters in the ring in
원문 | this turn.
```

```
번역 | 이 턴에 링의 모든
번역 | 캐릭터가 백업 공격을
번역 | 할 수 있다.
```

### `0709A4`  80 → 59바이트

```
원문 | Shuffles decks after returning all
원문 | characters (including this one)
원문 | to each deck.
```

```
번역 | 이 캐릭터를 포함해 모든
번역 | 캐릭터를 각자 덱으로
번역 | 돌리고 섞는다.
```

### `0709A8`  62 → 53바이트

```
원문 | Draws 1 character card randomly
원문 | from deck and adds it to hand.
```

```
번역 | 덱에서 캐릭터 카드를
번역 | 무작위로 1장 뽑아
번역 | 손패에 넣는다.
```

### `0709AC`  77 → 61바이트

```
원문 | Gives 400 pts. damage to all
원문 | characters in Freeze Phase
원문 | (including this one).
```

```
번역 | 이 캐릭터를 포함해
번역 | 얼어 있는 모든 캐릭터에게
번역 | 400 피해를 준다.
```

### `0709BC`  48 → 35바이트

```
원문 | Stops use of AC card during the
원문 | next enemy turn.
```

```
번역 | 다음 상대 턴에
번역 | 액션 카드를 못 쓴다.
```

### `0709C0`  56 → 62바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs this character. Draws 1 CHA
원문 | Card randomly from deck.
```

```
번역 | 이 캐릭터가 쓰러지고
번역 | 덱에서 캐릭터 카드를
번역 | 무작위로 1장 뽑는다.
```

### `0709C4`  52 → 46바이트

```
원문 | KOs this character. Changes 1
원문 | character to "Zombie."
```

```
번역 | 이 캐릭터가 쓰러지고
번역 | 캐릭터 1명이 좀비가 된다.
```

### `0709C8`  49 → 39바이트

```
원문 | Gives 1 enemy character or enemy
원문 | 100 pts. damage.
```

```
번역 | 상대나 상대 캐릭터에게
번역 | 100 피해를 준다.
```

### `0709CC`  69 → 43바이트

```
원문 | Selects 1 character with Ability.
원문 | Steals Ability from that
원문 | character.
```

```
번역 | 능력이 있는 캐릭터를
번역 | 골라 그 능력을 뺏는다.
```

### `0709D0`  61 → 51바이트

```
원문 | Decreases all characters's life
원문 | (including this one) 200 pts.
```

```
번역 | 이 캐릭터를 포함해
번역 | 모든 캐릭터의 체력을
번역 | 200 줄인다.
```

### `0709DC`  55 → 49바이트

```
원문 | Draw 1 AC Card from hand and
원문 | discards it. Draw 2 cards.
```

```
번역 | 손패의 액션 카드를
번역 | 1장 버린다.
번역 | 카드를 2장 뽑는다.
```

### `0709EC`  88 → 62바이트

```
원문 | KOs 1 character in your Ring.
원문 | Gives that character's BP damage
원문 | to 1 different character.
```

```
번역 | 내 링의 캐릭터 1명이
번역 | 쓰러진다. 그 BP만큼
번역 | 다른 캐릭터에게 피해.
```

### `0709F0`  45 → 37바이트

```
원문 | Decreases all enemy characters'
원문 | Life 100 pts.
```

```
번역 | 상대 캐릭터 모두의
번역 | 체력을 100 줄인다.
```

### `0709F4`  48 → 33바이트

```
원문 | Disable counter-attack when
원문 | you're out of cards.
```

```
번역 | 카드가 다 떨어지면
번역 | 되받지 못한다.
```

### `0709FC`  84 → 71바이트

```
원문 | Select 1 CHA Card from deck.
원문 | After deck's shuffled, places that
원문 | card on top of deck.
```

```
번역 | 덱에서 캐릭터 카드를
번역 | 1장 고른다. 덱을 섞은 뒤
번역 | 그 카드를 맨 위에 놓는다.
```

### `070A04`  51 → 34바이트

```
원문 | Stops Freeze Phase for all
원문 | characters in your ring.
```

```
번역 | 내 링의 모든 캐릭터가
번역 | 얼지 않는다.
```

### `070A08`  84 → 55바이트

```
원문 | Spares all characters in your Ring
원문 | from Freeze Phase, even after
원문 | Attacks(or Unions).
```

```
번역 | 공격이나 합체 공격을
번역 | 해도 내 링의 캐릭터가
번역 | 얼지 않는다.
```

### `070A0C`  71 → 58바이트

```
원문 | Keeps 1 enemy character
원문 | (in Freeze Phase) frozen
원문 | for next Action Phase.
```

```
번역 | 얼어 있는 상대 캐릭터를
번역 | 다음 행동 단계까지
번역 | 계속 얼려 둔다.
```

### `070A10`  71 → 46바이트

```
원문 | Frees 1 character in Freeze Phase.
원문 | Or puts 1 character in Freeze
원문 | Phase.
```

```
번역 | 얼어 있는 캐릭터를 풀거나
번역 | 캐릭터 1명을 얼린다.
```

### `070A14`  37 → 30바이트

```
원문 | Returns 1 of your characters to
원문 | hand.
```

```
번역 | 내 캐릭터 1명을
번역 | 손패로 돌린다.
```

### `070A18`  61 → 51바이트

```
원문 | Returns 1 of yours and 1 enemy
원문 | character to each side's hand.
```

```
번역 | 내 캐릭터와 상대 캐릭터를
번역 | 1명씩 각자 손패로 돌린다.
```

### `070A1C`  28 → 27바이트

```
원문 | Returns 1 character to hand.
```

```
번역 | 캐릭터 1명을 손패로
번역 | 돌린다.
```

### `070A20`  36 → 33바이트

```
원문 | Returns all characters to each
원문 | hand.
```

```
번역 | 모든 캐릭터를 각자
번역 | 손패로 돌린다.
```

### `070A24`  37 → 31바이트

```
원문 | Decreases 1 character's Life 300
원문 | pts.
```

```
번역 | 캐릭터 1명의
번역 | 체력을 300 줄인다.
```

### `070A28`  66 → 63바이트

```
원문 | KOs 1 of your characters. BP
원문 | damage is given to another
원문 | character.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | 그 BP만큼 다른 캐릭터에게
번역 | 피해를 준다.
```

### `070A2C`  65 → 57바이트

```
원문 | KOs 1 of your characters.
원문 | Decreases all characters'
원문 | Life 300 pts.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | 모든 캐릭터의 체력을
번역 | 300 줄인다.
```

### `070A30`  31 → 23바이트

```
원문 | Decreases enemy's Life 300 pts.
```

```
번역 | 상대 체력을 300 줄인다.
```

### `070A34`  39 → 32바이트

```
원문 | Decreases all characters'
원문 | Life 500 pts.
```

```
번역 | 모든 캐릭터의
번역 | 체력을 500 줄인다.
```

### `070A38`  31 → 23바이트

```
원문 | Decreases enemy's Life 500 pts.
```

```
번역 | 상대 체력을 500 줄인다.
```

### `070A3C`  37 → 32바이트

```
원문 | KOs all characters receiving
원문 | back-up.
```

```
번역 | 백업받은 캐릭터가
번역 | 모두 쓰러진다.
```

### `070A40`  39 → 39바이트

```
원문 | KOs all characters with 400 BP or
원문 | less.
```

```
번역 | BP가 400 이하인
번역 | 캐릭터가 모두 쓰러진다.
```

### `070A44`  48 → 41바이트

```
원문 | KOs 1 of your characters and an
원문 | enemy character.
```

```
번역 | 내 캐릭터와 상대 캐릭터가
번역 | 1명씩 쓰러진다.
```

### `070A48`  39 → 39바이트

```
원문 | KOs all characters with 500 BP or
원문 | more.
```

```
번역 | BP가 500 이상인
번역 | 캐릭터가 모두 쓰러진다.
```

### `070A4C`  80 → 63바이트

```
원문 | Select 1 of your characters and
원문 | an enemy character, and KO
원문 | remaining characters.
```

```
번역 | 내 캐릭터와 상대 캐릭터를
번역 | 1명씩 고른다. 나머지는
번역 | 모두 쓰러진다.
```

### `070A50`  19 → 23바이트  (빈 곳으로 옮겨 담음)

```
원문 | KOs all characters.
```

```
번역 | 모든 캐릭터가 쓰러진다.
```

### `070A54`  57 → 49바이트

```
원문 | KOs 1 of your characters. The BP
원문 | amount is added to Life.
```

```
번역 | 내 캐릭터 1명이 쓰러지고
번역 | 그 BP만큼 체력이 오른다.
```

### `070A5C`  75 → 66바이트

```
원문 | KO any number of your characters.
원문 | Add 2 pts. to SP for each KOed
원문 | character.
```

```
번역 | 내 캐릭터를 원하는 만큼
번역 | 쓰러뜨린다. 쓰러진 수만큼
번역 | SP가 2씩 오른다.
```

### `070A60`  16 → 14바이트

```
원문 | Raises SP 5 pts.
```

```
번역 | SP를 5 올린다.
```

### `070A64`  30 → 19바이트

```
원문 | Reduces each player's SP to 0.
```

```
번역 | 서로 SP가 0이 된다.
```

### `070A68`  71 → 64바이트

```
원문 | KOs any number of your
원문 | characters. Draw 1 card for each
원문 | KOed character.
```

```
번역 | 내 캐릭터를 원하는 만큼
번역 | 쓰러뜨린다. 쓰러진 수만큼
번역 | 카드를 뽑는다.
```

### `070A6C`  77 → 57바이트

```
원문 | See up to 3 of the deck's top cards.
원문 | Add 1 to your hand and discard the
원문 | rest.
```

```
번역 | 덱 맨 위 3장까지 본다.
번역 | 1장을 손패에 넣고
번역 | 나머지는 버린다.
```

### `070A70`  13 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | Draw 2 cards.
```

```
번역 | 카드를 2장 뽑는다.
```

### `070A74`  41 → 36바이트

```
원문 | After discarding your hand, draw
원문 | 5 cards.
```

```
번역 | 손패를 다 버린 뒤
번역 | 카드를 5장 뽑는다.
```

### `070A78`  32 → 29바이트

```
원문 | Raises 1 character's BP 300 pts.
```

```
번역 | 캐릭터 1명의
번역 | BP를 300 올린다.
```

### `070A7C`  94 → 66바이트

```
원문 | Changes a character's BP to the
원문 | top card of enemy's Pile. (KOs
원문 | character if AC Card's on top.)
```

```
번역 | 캐릭터 BP가 상대 더미
번역 | 맨 위 카드와 같아진다.
번역 | 액션 카드면 쓰러진다.
```

### `070A80`  47 → 36바이트

```
원문 | Raises all character's BP in your
원문 | ring 200 pts.
```

```
번역 | 내 링의 모든 캐릭터
번역 | BP를 200 올린다.
```

### `070A84`  75 → 63바이트

```
원문 | Choose 1 character with a
원문 | [Ability. 1 of your characters
원문 | gets that ability.
```

```
번역 | [능력이 있는 캐릭터를
번역 | 고른다. 내 캐릭터 1명이
번역 | 그 능력을 얻는다.
```

### `070A88`  58 → 45바이트

```
원문 | Select characters with Ability
원문 | and switch their Abilities.
```

```
번역 | 능력이 있는 캐릭터를
번역 | 골라 서로 능력을 바꾼다.
```

### `070A8C`  47 → 43바이트

```
원문 | All characters get 1 Ability
원문 | found in the game.
```

```
번역 | 모든 캐릭터가 이 게임의
번역 | 능력 하나를 얻는다.
```

### `070A90`  67 → 51바이트

```
원문 | See enemy's hand. Select 1 card
원문 | and put it in enemy's discard
원문 | pile.
```

```
번역 | 상대 손패를 본다.
번역 | 1장을 골라 상대 버린 패로
번역 | 보낸다.
```

### `070A94`  71 → 53바이트

```
원문 | Each player discards all CHA cards
원문 | in hand after showing hand to
원문 | enemy.
```

```
번역 | 서로 손패를 보인 뒤
번역 | 손패의 캐릭터 카드를
번역 | 모두 버린다.
```

### `070A98`  90 → 60바이트

```
원문 | After player with most cards in
원문 | Hand discards all cards, picks
원문 | same cards as other player.
```

```
번역 | 손패가 많은 쪽이 다 버리고
번역 | 상대와 같은 장수만큼
번역 | 다시 뽑는다.
```

### `070A9C`  89 → 65바이트

```
원문 | After seeing up to 3 cards from
원문 | top of your or enemy's Pile,
원문 | rearrange them in any order.
```

```
번역 | 내 더미나 상대 더미 맨 위
번역 | 3장까지 보고 원하는 차례로
번역 | 다시 놓는다.
```

### `070AA0`  59 → 41바이트

```
원문 | Discards all AC Cards in deck.
원문 | Shuffles deck after discard.
```

```
번역 | 덱의 액션 카드를 모두
번역 | 버리고 덱을 섞는다.
```

### `070AA4`  102 → 70바이트

```
원문 | Returns all Hand cards to Pile.
원문 | After Pile's shuffled, pick number
원문 | of cards returned to Pile + 1 more.
```

```
번역 | 손패를 모두 더미로 돌린다.
번역 | 더미를 섞은 뒤 돌린 수보다
번역 | 1장 많게 뽑는다.
```

### `070AA8`  68 → 49바이트

```
원문 | Take up to 3 cards from enemy
원문 | Pile and place them in enemy
원문 | Discards.
```

```
번역 | 상대 더미에서 3장까지
번역 | 뽑아 상대 버린 패로
번역 | 보낸다.
```

### `070AAC`  74 → 73바이트

```
원문 | Selects 1 AC Card from Pile. After
원문 | shuffled, puts that card on Pile's
원문 | top.
```

```
번역 | 더미에서 액션 카드를
번역 | 1장 고른다. 더미를 섞은 뒤
번역 | 그 카드를 맨 위에 놓는다.
```

### `070AB0`  87 → 64바이트

```
원문 | Draw 5 cards from deck and
원문 | arrange as desired. Discard other
원문 | deck cards and hand cards.
```

```
번역 | 덱에서 5장을 뽑아
번역 | 원하는 대로 놓는다. 나머지
번역 | 덱과 손패는 버린다.
```

### `070AB4`  65 → 50바이트

```
원문 | Changes the top card on your or
원문 | enemy's deck to a different card.
```

```
번역 | 내 덱이나 상대 덱
번역 | 맨 위 카드를 다른 카드로
번역 | 바꾼다.
```

### `070AB8`  94 → 66바이트

```
원문 | Draw up to 3 discard cards and
원문 | return them to the deck. After
원문 | deck is shuffled, draw one card.
```

```
번역 | 버린 패에서 3장까지
번역 | 덱으로 돌린다. 덱을 섞은 뒤
번역 | 카드를 1장 뽑는다.
```

### `070ABC`  63 → 41바이트

```
원문 | After returning all discards to
원문 | the deck, the deck is shuffled.
```

```
번역 | 버린 패를 모두 덱으로
번역 | 돌리고 덱을 섞는다.
```

### `070AC0`  49 → 42바이트

```
원문 | Draw 1 AC Card from discard pile
원문 | and add to hand.
```

```
번역 | 버린 패에서 액션 카드를
번역 | 1장 손패에 넣는다.
```

### `070AC4`  56 → 44바이트

```
원문 | Draw 1 character card from discard
원문 | pile and add to hand.
```

```
번역 | 버린 패에서 캐릭터 카드를
번역 | 1장 손패에 넣는다.
```

### `070AC8`  98 → 74바이트

```
원문 | Select one AC card but another
원문 | EMULATE card from enemy's discard
원문 | pile. Has same affect of AC Card.
```

```
번역 | 상대 버린 패에서 "흉내"가
번역 | 아닌 액션 카드를 1장 골라
번역 | 그 효과를 그대로 쓴다.
```

### `070ACC`  64 → 56바이트

```
원문 | During this turn, a character
원문 | getting Back-Up gets it
원문 | endlessly.
```

```
번역 | 이 턴 동안 백업받은
번역 | 캐릭터는 몇 번이든
번역 | 백업받을 수 있다.
```

### `070AD0`  66 → 49바이트

```
원문 | During this turn, Union 1 attacks
원문 | require 0 SP; Union 2 take 5 SP.
```

```
번역 | 이 턴 동안 둘 합체는
번역 | SP 0, 셋 합체는 SP 5가
번역 | 든다.
```

### `070AD4`  85 → 51바이트

```
원문 | Characters can be brought back
원문 | into the ring after previously
원문 | appearing in this turn.
```

```
번역 | 이 턴에 한 번 나왔던
번역 | 캐릭터도 링에 다시
번역 | 낼 수 있다.
```

### `070AD8`  89 → 69바이트

```
원문 | Each player chooses 1 card from
원문 | the other's Pile. Players keep
원문 | this card until game ends.
```

```
번역 | 서로 상대 더미에서 1장씩
번역 | 고른다. 그 카드는 대전이
번역 | 끝날 때까지 갖는다.
```

### `070ADC`  31 → 30바이트

```
원문 | All characters' BP becomes 200.
```

```
번역 | 모든 캐릭터의 BP가
번역 | 200이 된다.
```

### `070AE0`  91 → 53바이트

```
원문 | Disables your and enemy's
원문 | characters from attacking during
원문 | this turn and enemy's next turn.
```

```
번역 | 이 턴과 다음 상대 턴에
번역 | 서로 캐릭터가 공격하지
번역 | 못한다.
```

### `070AE4`  78 → 68바이트

```
원문 | Change 1 character to another in
원문 | this game (Back-up characters are
원문 | discarded).
```

```
번역 | 캐릭터 1명을 이 게임의
번역 | 다른 캐릭터로 바꾼다.
번역 | 백업 캐릭터는 버려진다.
```

### `070AE8`  82 → 62바이트

```
원문 | Choose "GRENADE," "PRAYER," or
원문 | "SHOWTIME." Card gets same
원문 | effect of selected item.
```

```
번역 | "수류탄" "기도" "쇼타임"
번역 | 중 하나를 골라
번역 | 그 효과를 그대로 쓴다.
```

### `070AEC`  68 → 59바이트

```
원문 | KOs all of your characters. After
원문 | this turn ends, a new turn begins.
```

```
번역 | 내 캐릭터가 모두 쓰러진다.
번역 | 이 턴이 끝나면
번역 | 새 턴이 시작된다.
```

### `070FA0`  95 → 73바이트

```
원문 | CAP
원문 | "What can I do for you?
원문 | ...Lookin' for a game?
원문 | Very well, you got it.
원문 | But can you beat me?"
```

```
번역 | 캡
번역 | "무슨 일이야?
번역 | …한판 하자고?
번역 | 좋아, 받아 주지.
번역 | 근데 날 이길 수 있겠어?"
```

### `070FA4`  54 → 25바이트

```
원문 | CAP
원문 | "You're quite a player.
원문 | Here's a present for you."
```

```
번역 | 캡
번역 | "제법인데.
번역 | 이거 받아."
```

### `070FA8`  26 → 19바이트

```
원문 | CAP
원문 | "See you around, kid."
```

```
번역 | 캡
번역 | "또 보자, 꼬마."
```

### `070FAC`  69 → 52바이트

```
원문 | CAP
원문 | "Whew! That was a blast!
원문 | ...This should make you
원문 | stronger. Here!"
```

```
번역 | 캡
번역 | "휴! 재밌었어!
번역 | …이거 쓰면 더 강해질
번역 | 거야. 받아!"
```

### `070FB4`  73 → 58바이트

```
원문 | KID
원문 | "Oh, you've come.
원문 | I was wanted to play you,
원문 | but I'm busy now. Later!"
```

```
번역 | 키드
번역 | "어, 왔구나.
번역 | 한판 하고 싶었는데
번역 | 지금은 바빠. 나중에!"
```

### `070FB8`  87 → 69바이트

```
원문 | KID
원문 | "Yo! {08}!
원문 | Show me just how strong
원문 | you've become. Get ready!"
원문 | FIGHT AGAINST THE KID?
원문 | {0D}
```

```
번역 | 키드
번역 | "야! {08}!
번역 | 얼마나 강해졌는지
번역 | 보여 줘. 준비됐어?"
번역 | 키드와 겨룰까요?
번역 | {0D}
```

### `070FBC`  31 → 30바이트

```
원문 | KID
원문 | "All right. That's my boy!"
```

```
번역 | 키드
번역 | "좋아. 그래야 내 친구지!"
```

### `070FC0`  46 → 32바이트

```
원문 | KID
원문 | "It's OK if you don't want to
원문 | play, wimp!"
```

```
번역 | 키드
번역 | "하기 싫으면 관둬,
번역 | 겁쟁이!"
```

### `070FC4`  61 → 49바이트

```
원문 | KID
원문 | "Okay! You've gotten good!
원문 | I'm impressed!
원문 | Here's a coin!"
```

```
번역 | 키드
번역 | "오! 많이 늘었네!
번역 | 대단한데!
번역 | 코인 하나 줄게!"
```

### `070FC8`  30 → 19바이트

```
원문 | KID
원문 | "You can play me anytime!"
```

```
번역 | 키드
번역 | "언제든 덤벼!"
```

### `070FCC`  71 → 63바이트

```
원문 | KID
원문 | "Over already?
원문 | Your need better deck balance?
원문 | Study! Study! Study!"
```

```
번역 | 키드
번역 | "벌써 끝이야?
번역 | 덱 짜임새를 손봐야겠는데?
번역 | 공부! 공부! 공부!"
```

### `070FD0`  85 → 59바이트

```
원문 | KID
원문 | "Hey, {08}!
원문 | Been workin' on your deck?
원문 | Care to try it out?"
원문 | FIGHT AGAINST THE KID?
원문 | {0D}
```

```
번역 | 키드
번역 | "어이, {08}!
번역 | 덱 손봤어?
번역 | 한번 써 볼래?"
번역 | 키드와 겨룰까요?
번역 | {0D}
```

### `070FD8`  27 → 22바이트

```
원문 | KID
원문 | "You've been studying!"
```

```
번역 | 키드
번역 | "공부 좀 했구나!"
```

### `070FDC`  22 → 20바이트

```
원문 | KID
원문 | "Keep it up, kid!"
```

```
번역 | 키드
번역 | "그 기세로 가!"
```

### `070FE0`  80 → 54바이트

```
원문 | KID
원문 | "Hmm, last time was a fluke.
원문 | Don't get cocky just because
원문 | you won one game!"
```

```
번역 | 키드
번역 | "흠, 저번엔 운이었어.
번역 | 한판 이겼다고
번역 | 으스대지 마!"
```

### `070FE4`  66 → 54바이트

```
원문 | KID
원문 | "Oh, how's it going?
원문 | I'm a little busy now!
원문 | Try me later, OK?"
```

```
번역 | 키드
번역 | "어, 잘 지내?
번역 | 지금 좀 바빠!
번역 | 나중에 오면 안 될까?"
```

### `070FE8`  95 → 76바이트

```
원문 | KID
원문 | "Back again, {08}?!
원문 | Great! Let's play!
원문 | If you win, this coin's yours!"
원문 | PLAY AGAINST THE KID?
원문 | {0D}
```

```
번역 | 키드
번역 | "또 왔어, {08}?!
번역 | 좋아! 한판 하자!
번역 | 이기면 이 코인 줄게!"
번역 | 키드와 겨룰까요?
번역 | {0D}
```

### `070FEC`  24 → 22바이트

```
원문 | KID
원문 | "Okay, let's begin!"
```

```
번역 | 키드
번역 | "좋아, 시작하자!"
```

### `070FF0`  50 → 34바이트

```
원문 | KID
원문 | "If you change your mind,
원문 | come back any time!"
```

```
번역 | 키드
번역 | "마음 바뀌면
번역 | 언제든 다시 와!"
```

### `070FF4`  63 → 48바이트

```
원문 | KID
원문 | "A splendid fight!
원문 | Here's your coin!
원문 | Take good care of it!"
```

```
번역 | 키드
번역 | "멋진 승부였어!
번역 | 코인 여기 있어!
번역 | 잘 간직해!"
```

### `070FF8`  59 → 47바이트

```
원문 | KID
원문 | "Oh, so close.
원문 | I'll play you anytime!
원문 | Come again soon!"
```

```
번역 | 키드
번역 | "아깝다, 아까워.
번역 | 언제든 붙어 줄게!
번역 | 또 와!"
```

### `070FFC`  58 → 49바이트

```
원문 | TAKA
원문 | "Whoo-hya!
원문 | It's {08}!
원문 | Let's play!"
원문 | FIGHT AGAINST TAKA?
원문 | {0D}
```

```
번역 | 타카
번역 | "우후!
번역 | {08}잖아!
번역 | 한판 하자!"
번역 | 타카와 겨룰까요?
번역 | {0D}
```

### `071000`  24 → 14바이트

```
원문 | TAKA
원문 | "Expect the worst!"
```

```
번역 | 타카
번역 | "각오해!"
```

### `071004`  21 → 19바이트

```
원문 | TAKA
원문 | "{08}, you baby!!!"
```

```
번역 | 타카
번역 | "{08}, 애송이!!!"
```

### `071008`  52 → 48바이트

```
원문 | TAKA
원문 | "Argh! Beaten by you?!
원문 | Oh, the humanity! Here!"
```

```
번역 | 타카
번역 | "윽! 너한테 지다니?!
번역 | 말도 안 돼! 자, 받아!"
```

### `07100C`  30 → 20바이트

```
원문 | TAKA
원문 | "Come again! Whoo-hyah!!"
```

```
번역 | 타카
번역 | "또 와! 우후!!"
```

### `071010`  54 → 48바이트

```
원문 | TAKA
원문 | "Whoo-hyah!!
원문 | I won! I won!
원문 | Try again, Loooo-ser!"
```

```
번역 | 타카
번역 | "우후!!
번역 | 이겼다! 이겼어!
번역 | 다시 덤벼, 패배자!"
```

### `071014`  64 → 48바이트

```
원문 | TAKA
원문 | "Whoo-hyah!
원문 | Why it's {08}!
원문 | Another game?"
원문 | PLAY AGAINST TAKA?
원문 | {0D}
```

```
번역 | 타카
번역 | "우후!
번역 | {08} 아냐!
번역 | 한판 더?"
번역 | 타카와 겨룰까요?
번역 | {0D}
```

### `071018`  26 → 21바이트

```
원문 | TAKA
원문 | "Gyah! I lost again?"
```

```
번역 | 타카
번역 | "으악! 또 졌어?"
```

### `071020`  128 → 90바이트

```
원문 | "Nice timing, punk.
원문 | The Kid told me
원문 | if I can beat you,
원문 | I'm the mightiest!
원문 | So, how 'bout a game?
원문 | It's an offer you can't refuse."
```

```
번역 | "때맞춰 왔군, 꼬마.
번역 | 키드가 그러던데
번역 | 너만 이기면
번역 | 내가 최강이라고!
번역 | 한판 어때?
번역 | 거절 못 할걸."
```

### `071024`  59 → 52바이트

```
원문 | SHIN
원문 | "Zounds! I lost!
원문 | ...Here, take this.
원문 | And don't gloat!"
```

```
번역 | 신
번역 | "이런! 졌잖아!
번역 | …자, 이거 받아.
번역 | 으스대지는 말고!"
```

### `071028`  47 → 36바이트

```
원문 | SHIN
원문 | "I'll win next time! So don't
원문 | leave town!"
```

```
번역 | 신
번역 | "다음엔 내가 이겨!
번역 | 동네 뜨지 마!"
```

### `07102C`  82 → 74바이트

```
원문 | SHIN
원문 | "All right! I won!
원문 | You let me win, didn't you?
원문 | Keep this until or next game."
```

```
번역 | 신
번역 | "좋았어! 내가 이겼다!
번역 | 일부러 져 준 거 아니지?
번역 | 다음까지 이거 갖고 있어."
```

### `071030`  44 → 32바이트

```
원문 | SHIN
원문 | Next time show me what you
원문 | really got!"
```

```
번역 | 신
번역 | "다음엔 진짜 실력을
번역 | 보여 줘!"
```

### `071034`  59 → 54바이트

```
원문 | FO
원문 | "Weelcome!
원문 | Ahm a busy a now!
원문 | You check me in later, OK?"
```

```
번역 | 포
번역 | "어서 오세요!
번역 | 지금은 바빠요!
번역 | 나중에 다시 와요, 네?"
```

### `071038`  93 → 98바이트  (빈 곳으로 옮겨 담음)

```
원문 | FO
원문 | "Weelcome!
원문 | I am Fo Gott En.
원문 | My kids never call! Anyway,
원문 | you play me!"
원문 | 
원문 | FIGHT AGAINST FO?
원문 | {0D}
```

```
번역 | 포
번역 | "어서 오세요!
번역 | 나는 포 갓 튼이오.
번역 | 애들이 통 연락을 안 해!
번역 | 어쨌든 한판 합시다!"
번역 | 
번역 | 포와 겨룰까요?
번역 | {0D}
```

### `07103C`  25 → 25바이트

```
원문 | FO
원문 | "OK! I show no mercy!"
```

```
번역 | 포
번역 | "좋아! 봐주지 않겠소!"
```

### `071040`  28 → 26바이트

```
원문 | FO
원문 | "OK. We play later, huh?"
```

```
번역 | 포
번역 | "그럼 나중에 하지, 응?"
```

### `071044`  70 → 60바이트

```
원문 | FO
원문 | "Holy Toad! I lost!
원문 | But I had a good time!
원문 | You take this coin, OK?"
```

```
번역 | 포
번역 | "이런 세상에! 졌군!
번역 | 그래도 즐거웠소!
번역 | 이 코인 받아요, 네?"
```

### `071048`  25 → 18바이트

```
원문 | FO
원문 | "You come again, OK?!"
```

```
번역 | 포
번역 | "또 와요, 네?!"
```

### `07104C`  75 → 65바이트

```
원문 | FO
원문 | "Oh baby, I win big!
원문 | This's real unusial!
원문 | I had the fun. See you later."
```

```
번역 | 포
번역 | "오호, 크게 이겼구먼!
번역 | 이런 일도 다 있네!
번역 | 즐거웠소. 또 봅시다."
```

### `071050`  92 → 80바이트

```
원문 | FO
원문 | "Howdy Doddy!
원문 | You got a high learning curve.
원문 | Let's play 'CARD CLASH.'"
원문 | PLAY AGAINST FO?
원문 | {0D}
```

```
번역 | 포
번역 | "안녕하시오!
번역 | 배우는 게 빠르구먼.
번역 | "카드 클래시" 한판 합시다."
번역 | 포와 겨룰까요?
번역 | {0D}
```

### `07105C`  26 → 19바이트

```
원문 | FO
원문 | "Melons! I lost again!"
```

```
번역 | 포
번역 | "이런! 또 졌군!"
```

### `071060`  34 → 39바이트  (빈 곳으로 옮겨 담음)

```
원문 | FO
원문 | "I win big next time! You see!"
```

```
번역 | 포
번역 | "다음엔 크게 이기겠소!
번역 | 두고 보시오!"
```

### `071064`  79 → 84바이트  (빈 곳으로 옮겨 담음)

```
원문 | FO
원문 | "Come to uncle, baby! I won!
원문 | No try, no win, huh?
원문 | I had fun. See you among!"
```

```
번역 | 포
번역 | "이리 오시오, 내가 이겼소!
번역 | 안 해 보면 못 이기지, 안 그렇소?
번역 | 즐거웠소. 또 봅시다!"
```

### `071068`  49 → 54바이트  (빈 곳으로 옮겨 담음)

```
원문 | FO
원문 | "Weelcome!
원문 | Hey, {08}!
원문 | I'm busy. Come back later."
```

```
번역 | 포
번역 | "어서 오세요!
번역 | 어이, {08}!
번역 | 지금 바쁘오. 나중에 오시오."
```

### `07106C`  82 → 68바이트

```
원문 | FO
원문 | "Weelcome!
원문 | I wanted to play you!
원문 | Okay, you get ready, you."
원문 | FIGHT AGAINST FO?
원문 | {0D}
```

```
번역 | 포
번역 | "어서 오세요!
번역 | 한판 하고 싶었소!
번역 | 자, 준비하시오."
번역 | 포와 겨룰까요?
번역 | {0D}
```

### `071070`  100 → 84바이트

```
원문 | NORI
원문 | "Hey, care for a game?
원문 | I feel lucky today...
원문 | How 'bout it. Give it a shot?
원문 | PLAY AGAINST NORI?
원문 | {0D}
```

```
번역 | 노리
번역 | "어이, 한판 어때?
번역 | 오늘 운이 좋은 것 같은데…
번역 | 어때, 해 볼래?"
번역 | 노리와 겨룰까요?
번역 | {0D}
```

### `071074`  23 → 22바이트

```
원문 | NORI
원문 | "Okay, let's play.
```

```
번역 | 노리
번역 | "좋아, 시작하자."
```

### `071078`  34 → 33바이트

```
원문 | NORI
원문 | "No? I'll try somebody else."
```

```
번역 | 노리
번역 | "싫다고? 다른 사람 찾지 뭐."
```

### `07107C`  78 → 58바이트

```
원문 | NORI
원문 | "You're pretty good...
원문 | Quite an instructive game.
원문 | Here's a card for you."
```

```
번역 | 노리
번역 | "제법이잖아…
번역 | 배울 게 많은 승부였어.
번역 | 카드 하나 줄게."
```

### `071080`  30 → 20바이트

```
원문 | NORI
원문 | "Play me again sometime."
```

```
번역 | 노리
번역 | "언제 또 붙자."
```

### `071084`  75 → 58바이트

```
원문 | NORI
원문 | "Oh, you were so close.
원문 | You'll win next time. NOT !
원문 | Sayonara, sucker."
```

```
번역 | 노리
번역 | "아, 아까웠어.
번역 | 다음엔 이길 거야. 뻥{19}!
번역 | 잘 가라, 호구."
```

### `071088`  90 → 74바이트

```
원문 | NORI
원문 | "Fancy meeting you here.
원문 | Hope you've improved.
원문 | Care for a game?"
원문 | PLAY AGAINST NORI?
원문 | {0D}
```

```
번역 | 노리
번역 | "여기서 다 만나네.
번역 | 좀 늘었길 바라는데.
번역 | 한판 할까?"
번역 | 노리와 겨룰까요?
번역 | {0D}
```

### `07108C`  26 → 23바이트

```
원문 | NORI
원문 | "Hmph. You won, huh?"
```

```
번역 | 노리
번역 | "흥. 네가 이겼네?"
```

### `071090`  31 → 23바이트

```
원문 | NORI
원문 | "Happy trials, tomodachi!"
```

```
번역 | 노리
번역 | "잘해 봐라, 친구!"
```

### `071094`  58 → 49바이트

```
원문 | NORI
원문 | "Hmm. My win, I guess.
원문 | Let's play again if you wish."
```

```
번역 | 노리
번역 | "음. 내가 이겼나 보네.
번역 | 하고 싶으면 또 붙자."
```

### `071098`  107 → 93바이트

```
원문 | HARUMI
원문 | "Hmm. What to do?
원문 | 'NAKORURU,' 'CHARLOTTE,'
원문 | 'MARIE'...
원문 | I just can't decide.
원문 | Wait till I'm ready, OK?"
```

```
번역 | 하루미
번역 | "음. 어쩌지?
번역 | "나코루루" "샬롯"
번역 | "마리"…
번역 | 도무지 못 고르겠네.
번역 | 준비될 때까지 기다려, 응?"
```

### `07109C`  144 → 128바이트

```
원문 | HARUMI
원문 | "Okay! Now I'm ready!
원문 | Meet the 'Ikoma Special.'
원문 | Not me, my deck, stupid!
원문 | Pretty cooool, huh!
원문 | This deck will kill!"
원문 | PLAY AGAINST HARUMI?
원문 | {0D}
```

```
번역 | 하루미
번역 | "좋아! 준비 끝!
번역 | "이코마 스페셜"이야.
번역 | 내가 아니라 덱 말이야, 바보!
번역 | 멋지지 않아?
번역 | 이 덱은 다 쓸어버려!"
번역 | 하루미와 겨룰까요?
번역 | {0D}
```

### `0710A0`  44 → 32바이트

```
원문 | HARUMI
원문 | "OK! Cut the cards!
원문 | And bring it on!"
```

```
번역 | 하루미
번역 | "자! 카드 섞어!
번역 | 덤벼 봐!"
```

### `0710A4`  85 → 67바이트

```
원문 | HARUMI
원문 | "What...is...this?
원문 | I made the perfect deck!
원문 | Is this the end of little Harumi?"
```

```
번역 | 하루미
번역 | "이게… 뭐야…?
번역 | 완벽한 덱을 짰는데!
번역 | 하루미는 여기서 끝인가?"
```

### `0710A8`  132 → 100바이트

```
원문 | HARUMI
원문 | "You weenie!
원문 | Ikoma, Goddess of Destruction,
원문 | lost!
원문 | I'll be gunning for you.
원문 | Here's a coin, flukester.
원문 | Treat it nice, or else!"
```

```
번역 | 하루미
번역 | "이 얄미운!
번역 | 파괴의 여신 이코마가
번역 | 지다니!
번역 | 두고 보자.
번역 | 코인 여기, 운빨아.
번역 | 잘 간직해, 안 그러면!"
```

### `0710AC`  258 → 193바이트

```
원문 | HARUMI
원문 | "You can't win and run!!
원문 | After this, what about
원문 | my legend as the best?"
원문 | KEIKO
원문 | "Whaddya talkin' about?
원문 | Always yelling 'Do over!'
원문 | and 'Those aren't the rules!'
원문 | Then you tear up the cards.
원문 | That's why your called
원문 | 'Goddess of Destruction.'
원문 | 
원문 | HARUMI
원문 | "Gulp!!"
```

```
번역 | 하루미
번역 | "이기고 도망칠 순 없어!!
번역 | 이러면 최강이라는
번역 | 내 전설은 어떡해?"
번역 | 케이코
번역 | "무슨 소리야?
번역 | 맨날 "다시 해!"
번역 | "그건 규칙이 아냐!" 하고
번역 | 카드를 찢어 놓고선.
번역 | 그래서 "파괴의 여신"이잖아.
번역 | 
번역 | 하루미
번역 | "윽!!"
```

### `0710B0`  62 → 54바이트

```
원문 | HARUMI
원문 | "Wah hah! I won!
원문 | Drop by again.
원문 | I'll play you anytime."
```

```
번역 | 하루미
번역 | "하하! 내가 이겼다!
번역 | 또 들러.
번역 | 언제든 붙어 줄게."
```

### `0710B4`  93 → 72바이트

```
원문 | HARUMI
원문 | "You're the only one to beat me.
원문 | You won't be so lucky again!"
원문 | 
원문 | PLAY AGAINST HARUMI?
원문 | {0D}
```

```
번역 | 하루미
번역 | "날 이긴 건 너뿐이야.
번역 | 다음엔 그런 운 없어!"
번역 | 
번역 | 하루미와 겨룰까요?
번역 | {0D}
```

### `0710B8`  66 → 57바이트

```
원문 | HARUMI
원문 | "What...is...that?
원문 | Are you pouting?
원문 | I won fair and square."
```

```
번역 | 하루미
번역 | "그게… 뭐야…?
번역 | 삐친 거야?
번역 | 정정당당하게 이겼는데."
```

### `0710BC`  88 → 62바이트

```
원문 | HARUMI
원문 | "Curses, curses. Lost again.
원문 | This's too bee-zarre!
원문 | Phooey! Take it, you hustler!"
```

```
번역 | 하루미
번역 | "아 진짜, 또 졌어.
번역 | 너무 이상해!
번역 | 칫! 가져가, 이 사기꾼!"
```

### `0710C0`  66 → 52바이트

```
원문 | HARUMI
원문 | "I won't lose next time!"
원문 | KEIKO
원문 | "Talk about sour grapes..."
```

```
번역 | 하루미
번역 | "다음엔 안 져!"
번역 | 케이코
번역 | "괜히 억지 부리기는…"
```

### `0710C4`  63 → 57바이트

```
원문 | HARUMI
원문 | "Wah hah! I won!
원문 | What great cards!
원문 | I owe it to my fans."
```

```
번역 | 하루미
번역 | "하하! 이겼다!
번역 | 카드가 끝내주네!
번역 | 다 팬들 덕분이야."
```

### `0710C8`  104 → 85바이트

```
원문 | KEIKO
원문 | "Welcome to my place.
원문 | Welcome to
원문 | NEO Choopy Fighters.
원문 | Care to play a game?"
원문 | 
원문 | PLAY AGAINST KEIKO?
원문 | {0D}
```

```
번역 | 케이코
번역 | "어서 와.
번역 | 네오 츄피 파이터즈에
번역 | 온 걸 환영해.
번역 | 한판 할래?"
번역 | 
번역 | 케이코와 겨룰까요?
번역 | {0D}
```

### `0710CC`  70 → 51바이트

```
원문 | KEIKO
원문 | "All right. Let's get playing.
원문 | My 'Rimnerel' deck's invincible!"
```

```
번역 | 케이코
번역 | "좋아. 시작하자.
번역 | 내 "림네렐" 덱은 무적이야!"
```

### `0710D0`  60 → 42바이트

```
원문 | KEIKO
원문 | "Yeah. Too bad, huh. ...Heck!
원문 | Drop by again sometime!"
```

```
번역 | 케이코
번역 | "그래, 아쉽네. …칫!
번역 | 언제 또 들러!"
```

### `0710D4`  63 → 53바이트

```
원문 | KEIKO
원문 | "Yikes! I lost.
원문 | Whachya gonna do?
원문 | Here's a little bonus."
```

```
번역 | 케이코
번역 | "헉! 졌네.
번역 | 어쩔 수 없지 뭐.
번역 | 덤으로 이거 줄게."
```

### `0710D8`  51 → 35바이트

```
원문 | KEIKO
원문 | "Yeah, I'll win next time.
원문 | Let's play again."
```

```
번역 | 케이코
번역 | "다음엔 내가 이겨.
번역 | 또 붙자."
```

### `0710DC`  82 → 57바이트

```
원문 | KEIKO
원문 | "Whooee, that was fun!
원문 | I'll play you any day.
원문 | You come back here, you hear?"
```

```
번역 | 케이코
번역 | "우와, 재밌었어!
번역 | 언제든 붙어 줄게.
번역 | 또 와, 알았지?"
```

### `0710E0`  75 → 60바이트

```
원문 | KEIKO
원문 | "I lost last time, but
원문 | I won't mess up again!"
원문 | 
원문 | PLAY AGAINST KEIKO?
원문 | {0D}
```

```
번역 | 케이코
번역 | "저번엔 졌지만
번역 | 이번엔 안 그래!"
번역 | 
번역 | 케이코와 겨룰까요?
번역 | {0D}
```

### `0710E4`  19 → 19바이트

```
원문 | KEIKO
원문 | "Let's play!"
```

```
번역 | 케이코
번역 | "한판 하자!"
```

### `0710E8`  81 → 62바이트

```
원문 | KEIKO
원문 | "The curse of Ikoma, Goddess of
원문 | Destruction!"
원문 | 
원문 | HARUMI
원문 | "What? I heard that!"
```

```
번역 | 케이코
번역 | "파괴의 여신 이코마의
번역 | 저주다!"
번역 | 
번역 | 하루미
번역 | "뭐? 다 들렸어!"
```

### `0710EC`  51 → 41바이트

```
원문 | KEIKO
원문 | "The curse of..."
원문 | HARUMI
원문 | "All right already!"
```

```
번역 | 케이코
번역 | "저주가…"
번역 | 하루미
번역 | "알았어 알았어!"
```

### `0710F0`  83 → 55바이트

```
원문 | KEIKO
원문 | "Now that was delightful!
원문 | Let's play again, huh?
원문 | Huh, how 'bout it? Huh? OK?"
```

```
번역 | 케이코
번역 | "이야, 신났다!
번역 | 또 하자, 응?
번역 | 응? 어때? 응? 좋지?"
```

### `0710F4`  152 → 129바이트

```
원문 | NONAKA
원문 | "Hey, call me Nonaka.
원문 | NEO Choopy Fighters invited me.
원문 | Quite a place, isn't it?
원문 | I owe it all to Kyo.
원문 | How about playing me?"
원문 | PLAY AGAINST NONAKA?
원문 | {0D}
```

```
번역 | 노나카
번역 | "어이, 노나카라고 불러.
번역 | 네오 츄피 파이터즈가 불러 줬어.
번역 | 괜찮은 데지?
번역 | 다 쿄 덕분이야.
번역 | 나랑 한판 어때?"
번역 | 노나카와 겨룰까요?
번역 | {0D}
```

### `0710F8`  86 → 64바이트

```
원문 | NONAKA
원문 | "Let's get playing!
원문 | What's my deck's name?
원문 | I call it 'Burning Luck.' Cool, huh?
```

```
번역 | 노나카
번역 | "시작하자!
번역 | 내 덱 이름이 뭐냐고?
번역 | "불타는 운"이야. 멋지지?"
```

### `0710FC`  97 → 73바이트

```
원문 | NONAKA
원문 | "Oh my. That's a shame...
원문 | Let's play again if you're game!
원문 | Well, see you in the big time!"
```

```
번역 | 노나카
번역 | "이런. 아쉽게 됐네…
번역 | 생각 있으면 또 붙자!
번역 | 그럼, 큰 무대에서 보자!"
```

### `071100`  97 → 65바이트

```
원문 | NONAKA
원문 | "Oh, shoot! I'm beaten!
원문 | Heck! Oh, the shame of it!
원문 | ...Fudge. Guess I gotta give you
원문 | this."
```

```
번역 | 노나카
번역 | "아 젠장! 졌어!
번역 | 칫! 창피해 죽겠네!
번역 | …에잇. 이거 줘야겠지."
```

### `071104`  61 → 51바이트

```
원문 | NONAKA
원문 | "The fun starts here!
원문 | I won't lose so easy next time!"
```

```
번역 | 노나카
번역 | "재미는 지금부터야!
번역 | 다음엔 그리 쉽게 안 져!"
```

### `071108`  80 → 61바이트

```
원문 | NONAKA
원문 | "Heh, heh. Having fun yet?
원문 | This CARD CLASH is...
원문 | it's awesome, isn't it?"
```

```
번역 | 노나카
번역 | "헤헤. 재밌지?
번역 | 이 카드 클래시라는 게…
번역 | 끝내주지 않아?"
```

### `07110C`  122 → 107바이트

```
원문 | NONAKA
원문 | "Hey, let's go again.
원문 | How about it?
원문 | 
원문 | Feel lucky? In the pocket?
원문 | This game'll be a good one."
원문 | PLAY AGAINST NONAKA?
원문 | {0D}
```

```
번역 | 노나카
번역 | "어이, 한판 더 하자.
번역 | 어때?
번역 | 
번역 | 운 좋은 것 같아? 자신 있어?
번역 | 이번 판은 재밌을 거야."
번역 | 노나카와 겨룰까요?
번역 | {0D}
```

### `071110`  24 → 24바이트

```
원문 | NONAKA
원문 | "OK! Let's play!"
```

```
번역 | 노나카
번역 | "좋아! 시작하자!"
```

### `071114`  88 → 76바이트

```
원문 | NONAKA
원문 | "So that's where it goes.
원문 | You got the touch, kid.
원문 | Here, take this card, hustler!"
```

```
번역 | 노나카
번역 | "아, 그렇게 되는구나.
번역 | 감이 좋은데, 꼬마.
번역 | 자, 이 카드 가져가, 사기꾼!"
```

### `071118`  67 → 43바이트

```
원문 | NONAKA
원문 | "I'm waiting for our next game.
원문 | Keep your fingertips moist!"
```

```
번역 | 노나카
번역 | "다음 판 기다릴게.
번역 | 손끝 잘 풀어 놔!"
```

### `07111C`  140 → 97바이트

```
원문 | TAKE
원문 | "Huh?
원문 | Do you play cards, too?
원문 | Wow, I'm in luck!
원문 | I'm sick of playing with Mika.
원문 | 
원문 | How about playing
원문 | a game with me?"
원문 | PLAY AGAINST TAKE?
원문 | {0D}
```

```
번역 | 타케
번역 | "어?
번역 | 너도 카드 해?
번역 | 와, 운 좋다!
번역 | 미카랑만 하다 질렸거든.
번역 | 
번역 | 나랑 한판
번역 | 어때?"
번역 | 타케와 겨룰까요?
번역 | {0D}
```

### `071120`  46 → 34바이트

```
원문 | TAKE
원문 | "OK, let's get started!
원문 | Prepare to lose!"
```

```
번역 | 타케
번역 | "자, 시작하자!
번역 | 질 각오 하고!"
```

### `071124`  85 → 71바이트

```
원문 | TAKE
원문 | "What was that?
원문 | I thought I could teach Mika
원문 | and finally get out of here. Darn!"
```

```
번역 | 타케
번역 | "뭐야 방금?
번역 | 미카한테 한 수 가르치고
번역 | 여기서 벗어나려 했는데. 젠장!"
```

### `071128`  114 → 105바이트

```
원문 | TAKE
원문 | "What? I lost? No way!"
원문 | MIKA
원문 | "I thought you knew how to play,
원문 | Take."
원문 | 
원문 | TAKE
원문 | "Be quiet. I do know how to play!"
```

```
번역 | 타케
번역 | "뭐? 내가 졌다고? 말도 안 돼!"
번역 | 미카
번역 | "할 줄 아는 줄 알았는데,
번역 | 타케."
번역 | 
번역 | 타케
번역 | "조용히 해. 할 줄 알거든!"
```

### `07112C`  110 → 79바이트

```
원문 | TAKE
원문 | "This isn't happening.
원문 | I've lost my touch because
원문 | I'm always playing with you."
원문 | MIKA
원문 | "Oh, Take! Boo hoo!"
```

```
번역 | 타케
번역 | "이럴 리가 없어.
번역 | 너랑만 하다 보니
번역 | 감이 죽었잖아."
번역 | 미카
번역 | "어머, 타케! 흑흑!"
```

### `071130`  107 → 93바이트

```
원문 | TAKE
원문 | "Just as I thought.
원문 | I'm so awesome!
원문 | King of the World, putz!"
원문 | MIKA
원문 | "Aren't you overdoing it a
원문 | little?"
```

```
번역 | 타케
번역 | "역시 내 생각대로야.
번역 | 난 정말 대단해!
번역 | 세상의 왕이라고, 임마!"
번역 | 미카
번역 | "좀 오버하는 거 아냐?"
```

### `071134`  111 → 87바이트

```
원문 | TAKE
원문 | "I was in a slump last time.
원문 | But Ikoma gave me some tips,
원문 | so I can't lose this time."
원문 | PLAY AGAINST TAKE?
원문 | {0D}
```

```
번역 | 타케
번역 | "저번엔 부진했어.
번역 | 근데 이코마가 요령을 알려 줘서
번역 | 이번엔 안 져."
번역 | 타케와 겨룰까요?
번역 | {0D}
```

### `071138`  25 → 20바이트

```
원문 | TAKE
원문 | "And away we goooo!"
```

```
번역 | 타케
번역 | "자, 간다아아!"
```

### `07113C`  40 → 35바이트

```
원문 | TAKE
원문 | "What the...?
원문 | Nuts! You're no fun!"
```

```
번역 | 타케
번역 | "뭐야 이거…?
번역 | 에잇! 재미없게!"
```

### `071140`  63 → 62바이트

```
원문 | TAKE
원문 | "I lost this fast?"
원문 | MIKA
원문 | "Take?..."
원문 | TAKE
원문 | "No, you see...."
```

```
번역 | 타케
번역 | "이렇게 빨리 졌다고?"
번역 | 미카
번역 | "타케…?"
번역 | 타케
번역 | "아니, 그게…."
```

### `071144`  65 → 59바이트

```
원문 | TAKE
원문 | "I'll win for sure next time!"
원문 | MIKA
원문 | "I'm dating a loser...."
```

```
번역 | 타케
번역 | "다음엔 꼭 이긴다!"
번역 | 미카
번역 | "내 남자친구가 패배자라니…."
```

### `071148`  64 → 49바이트

```
원문 | TAKE
원문 | "I am Master of the Universe!"
원문 | MIKA
원문 | "Cool your jets, Take!"
```

```
번역 | 타케
번역 | "내가 우주의 지배자다!"
번역 | 미카
번역 | "진정해, 타케!"
```

### `07114C`  132 → 106바이트

```
원문 | MIKA
원문 | "Oh, hi there!
원문 | Um, Take just taught me
원문 | how to arrange the deck.
원문 | Care for a game with me?
원문 | It's really fun!"
원문 | PLAY AGAINST MIKA?
원문 | {0D}
```

```
번역 | 미카
번역 | "어, 안녕!
번역 | 음, 타케가 방금
번역 | 덱 짜는 법을 가르쳐 줬어.
번역 | 나랑 한판 할래?
번역 | 진짜 재밌어!"
번역 | 미카와 겨룰까요?
번역 | {0D}
```

### `071150`  69 → 62바이트

```
원문 | MIKA
원문 | "Hmm. Let's see...
원문 | I'll call this deck...
원문 | 'Choopy.' Let's play!"
```

```
번역 | 미카
번역 | "음. 어디 보자…
번역 | 이 덱 이름은…
번역 | "츄피"로 할래. 시작하자!"
```

### `071154`  180 → 139바이트

```
원문 | MIKA
원문 | "Worried about me and Take?
원문 | Don't worry a bit.
원문 | Take and I are
원문 | cuddly-wuddlies.
원문 | So don't give it a second thought.
원문 | Isn't that right,
원문 | Take-shmeshy?
원문 | TAKE
원문 | "You said a mouth full!"
```

```
번역 | 미카
번역 | "나랑 타케 사이가 궁금해?
번역 | 걱정 안 해도 돼.
번역 | 타케랑 나는
번역 | 알콩달콩하거든.
번역 | 그러니까 신경 쓰지 마.
번역 | 그렇지,
번역 | 타케 자기야?"
번역 | 타케
번역 | "말 다 했냐!"
```

### `071158`  88 → 69바이트

```
원문 | MIKA
원문 | "Yikes! I lost....
원문 | Take, don't scold
원문 | your wittle Mika-pika!
원문 | TAKE
원문 | "You're hopeless!"
```

```
번역 | 미카
번역 | "헉! 졌다….
번역 | 타케, 우리 미카 혼내지 마!"
번역 | 타케
번역 | "너 정말 못 말려!"
```

### `07115C`  34 → 29바이트

```
원문 | MIKA
원문 | "Wow, that was fun! See you!"
```

```
번역 | 미카
번역 | "우와, 재밌었어! 또 봐!"
```

### `071160`  178 → 133바이트

```
원문 | MIKA
원문 | "Oh, really?
원문 | I won the game?
원문 | What do I do now?"
원문 | TAKE
원문 | "What are you blabbing about?
원문 | You won, didn't you?
원문 | Gloat about it!"
원문 | MIKA
원문 | "But that's rude, isn't it?"
원문 | TAKE
원문 | "Oh brother!"
```

```
번역 | 미카
번역 | "어, 정말?
번역 | 내가 이긴 거야?
번역 | 이제 어쩌지?"
번역 | 타케
번역 | "무슨 헛소리야?
번역 | 이겼잖아?
번역 | 좀 자랑하라고!"
번역 | 미카
번역 | "그건 실례 아냐?"
번역 | 타케
번역 | "아이고 참!"
```

### `071164`  93 → 74바이트

```
원문 | MIKA
원문 | "So, we meet again!
원문 | I had a ball last time.
원문 | Hey, let's play again."
원문 | PLAY AGAINST MIKA?
원문 | {0D}
```

```
번역 | 미카
번역 | "또 만났네!
번역 | 지난번엔 정말 재밌었어.
번역 | 또 한판 하자."
번역 | 미카와 겨룰까요?
번역 | {0D}
```

### `071168`  99 → 63바이트

```
원문 | MIKA
원문 | "I've improved since last time...
원문 | You're up against my new deck,
원문 | 'The Great Choopies!' Ready?"
```

```
번역 | 미카
번역 | "지난번보다 늘었어…
번역 | 새 덱 "위대한 츄피들"이야.
번역 | 준비됐어?"
```

### `07116C`  66 → 46바이트

```
원문 | MIKA
원문 | "Oh, shoot...What a shame!...
원문 | Well, see you again some time."
```

```
번역 | 미카
번역 | "아, 저런… 아쉽다!…
번역 | 그럼 언제 또 보자."
```

### `071170`  101 → 80바이트

```
원문 | MIKA
원문 | "Ah! Uh? I lost again.
원문 | Guess a new name
원문 | doesn't make it stronger...."
원문 | TAKE
원문 | "You got that right."
```

```
번역 | 미카
번역 | "아! 어? 또 졌네.
번역 | 이름 바꾼다고
번역 | 세지진 않나 봐…."
번역 | 타케
번역 | "그건 맞는 말이다."
```

### `071174`  55 → 42바이트

```
원문 | MIKA
원문 | "I'm upset. But I had fun!
원문 | Let's play again, huh?"
```

```
번역 | 미카
번역 | "분해. 그래도 재밌었어!
번역 | 또 하자, 응?"
```

### `071178`  66 → 44바이트

```
원문 | MIKA
원문 | "Huh? Really? I won?
원문 | You could knock
원문 | me over with a feather!"
```

```
번역 | 미카
번역 | "어? 정말? 내가 이겼어?
번역 | 깜짝 놀랐잖아!"
```

### `07117C`  94 → 63바이트

```
원문 | KANA
원문 | "If you want to play me,
원문 | You got to beat those 3 people.
원문 | Then I'll consider playing you."
```

```
번역 | 카나
번역 | "나랑 붙고 싶으면
번역 | 저 세 사람을 이겨 봐.
번역 | 그럼 생각해 보지."
```

### `071180`  104 → 86바이트

```
원문 | KANA
원문 | "Hey, you're no pushover.
원문 | Let's deal a few.
원문 | If you win, I'll give you a coin."
원문 | PLAY AGAINST KANA?
원문 | {0D}
```

```
번역 | 카나
번역 | "어이, 만만치 않은데.
번역 | 몇 판 붙어 보자.
번역 | 이기면 코인 하나 줄게."
번역 | 카나와 겨룰까요?
번역 | {0D}
```

### `071184`  35 → 29바이트

```
원문 | KANA
원문 | "Don't even think you'll win!"
```

```
번역 | 카나
번역 | "이길 생각은 하지도 마!"
```

### `071188`  58 → 37바이트

```
원문 | KANA
원문 | "Lost your nerve?
원문 | Come back when you find your
원문 | guts!"
```

```
번역 | 카나
번역 | "겁먹었어?
번역 | 배짱 생기면 다시 와!"
```

### `07118C`  62 → 51바이트

```
원문 | KANA
원문 | "You know your cards...
원문 | As I promised, here's your coin."
```

```
번역 | 카나
번역 | "카드를 좀 아는군….
번역 | 약속대로 코인 여기 있어."
```

### `071190`  81 → 55바이트

```
원문 | KANA
원문 | "I await our next meeting.
원문 | You got talent, kid.
원문 | Good luck and good dealing."
```

```
번역 | 카나
번역 | "다음을 기다리지.
번역 | 재능이 있어, 꼬마.
번역 | 행운을 빈다."
```

### `071194`  87 → 67바이트

```
원문 | KANA
원문 | "Oh, so close...But that's 
원문 | the difference between us.
원문 | I'm a pro, and you're not."
```

```
번역 | 카나
번역 | "아깝네…. 하지만 그게
번역 | 너와 나의 차이야.
번역 | 난 프로고 넌 아니지."
```

### `071198`  85 → 65바이트

```
원문 | KANA
원문 | "Back again?
원문 | Glad to see you.
원문 | Of course you want to play?!"
원문 | PLAY AGAINST KANA?
원문 | {0D}
```

```
번역 | 카나
번역 | "또 왔어?
번역 | 반갑네.
번역 | 물론 한판 하고 싶겠지?"
번역 | 카나와 겨룰까요?
번역 | {0D}
```

### `0711A4`  54 → 43바이트

```
원문 | KANA
원문 | "You're one tough player...Here,
원문 | take this card!"
```

```
번역 | 카나
번역 | "만만찮은 상대군…. 자,
번역 | 이 카드 받아!"
```

### `0711A8`  79 → 69바이트

```
원문 | KANA
원문 | "Oh, that was joy!
원문 | I never thought work
원문 | could be this fun! I feel guilty."
```

```
번역 | 카나
번역 | "아, 즐거웠어!
번역 | 일이 이렇게 재밌을 줄은
번역 | 몰랐네! 미안할 지경이야."
```

### `0711AC`  56 → 45바이트

```
원문 | KANA
원문 | "It's my win! Oh ho ho!
원문 | ...I'm such a stinker!...."
```

```
번역 | 카나
번역 | "내가 이겼네! 호호!
번역 | …나도 참 짓궂지…."
```

### `0711B0`  93 → 91바이트

```
원문 | AKI
원문 | "Hi, I'm Aki.
원문 | I just learned the
원문 | CARD CLASH rules.
원문 | Care to play me?"
원문 | 
원문 | PLAY AGAINST AKI?
원문 | {0D}
```

```
번역 | 아키
번역 | "안녕, 나는 아키야.
번역 | 카드 클래시 규칙을
번역 | 막 배웠어.
번역 | 나랑 한판 할래?"
번역 | 
번역 | 아키와 겨룰까요?
번역 | {0D}
```

### `0711B4`  32 → 21바이트

```
원문 | AKI
원문 | "Well, let's cut the cards!"
```

```
번역 | 아키
번역 | "자, 카드 섞자!"
```

### `0711B8`  57 → 40바이트

```
원문 | AKI
원문 | "Well, that's that....
원문 | Guess you're not in the mood."
```

```
번역 | 아키
번역 | "음, 그렇구나….
번역 | 생각이 없나 보네."
```

### `0711BC`  36 → 32바이트

```
원문 | AKI
원문 | "Ah. I lost...
원문 | Here, take this!"
```

```
번역 | 아키
번역 | "아. 졌다…
번역 | 자, 이거 받아!"
```

### `0711C0`  56 → 37바이트

```
원문 | AKI
원문 | "I need to study more.
원문 | Play with me again sometime."
```

```
번역 | 아키
번역 | "더 공부해야겠어.
번역 | 언제 또 붙자."
```

### `0711C4`  76 → 57바이트

```
원문 | AKI
원문 | "Whoo. Looks like I won.
원문 | I had such a fun time!
원문 | Play me again sometime!"
```

```
번역 | 아키
번역 | "우와. 내가 이겼나 봐.
번역 | 정말 재밌었어!
번역 | 언제 또 하자!"
```

### `0711C8`  88 → 77바이트

```
원문 | AKI
원문 | "Oh, hi!
원문 | I won't roll over this time!
원문 | If your game, let's play!"
원문 | PLAY AGAINST AKI?
원문 | {0D}
```

```
번역 | 아키
번역 | "어, 안녕!
번역 | 이번엔 그냥 안 져!
번역 | 생각 있으면 한판 하자!"
번역 | 아키와 겨룰까요?
번역 | {0D}
```

### `0711CC`  49 → 36바이트

```
원문 | AKI
원문 | "Ah. I lost again....
원문 | Here, this is for you!"
```

```
번역 | 아키
번역 | "아. 또 졌네….
번역 | 자, 이거 받아!"
```

### `0711D0`  116 → 87바이트

```
원문 | SAKI
원문 | "What? CARD CLASH?
원문 | I'm just a beginner.
원문 | Take it easy on me, huh?...
원문 | Hee, hee. All right?"
원문 | 
원문 | PLAY AGAINST SAKI?
원문 | {0D}
```

```
번역 | 사키
번역 | "뭐? 카드 클래시?
번역 | 난 초보인데.
번역 | 살살해 줘, 응?…
번역 | 헤헤. 괜찮지?"
번역 | 
번역 | 사키와 겨룰까요?
번역 | {0D}
```

### `0711D4`  49 → 26바이트

```
원문 | SAKI
원문 | "Let's give it a whirl.
원문 | Let the game begin!"
```

```
번역 | 사키
번역 | "한번 해 보자.
번역 | 시작!"
```

### `0711D8`  72 → 62바이트

```
원문 | SAKI
원문 | "Huh? What a bore!
원문 | Come on, let's play.
원문 | Don't make Saki pout, huh?"
```

```
번역 | 사키
번역 | "어? 시시하게!
번역 | 에이, 한판 하자.
번역 | 사키 삐치게 하지 마, 응?"
```

### `0711DC`  45 → 37바이트

```
원문 | SAKI
원문 | "Oh, I lost! ...Shoot!
원문 | Here, take this!"
```

```
번역 | 사키
번역 | "아, 졌다! …칫!
번역 | 자, 이거 받아!"
```

### `0711E0`  69 → 60바이트

```
원문 | SAKI
원문 | "How come I lost?....
원문 | I just don't get it.
원문 | Play Saki again, OK?"
```

```
번역 | 사키
번역 | "내가 왜 졌지?….
번역 | 도무지 모르겠네.
번역 | 사키랑 또 하자, 응?"
```

### `0711E4`  82 → 74바이트

```
원문 | SAKI
원문 | "Yeah! Saki wins!
원문 | I did it! I'll be a card queen!
원문 | Ha! Just kidding! Hee hee."
```

```
번역 | 사키
번역 | "좋았어! 사키 승리!
번역 | 해냈다! 카드 여왕이 될 거야!
번역 | 하! 농담이야. 헤헤."
```

### `0711E8`  129 → 124바이트

```
원문 | SAKI
원문 | "Hi, I'm Saki.
원문 | Yuki calls me "Airhead."
원문 | Isn't she terrible?
원문 | She'll regret that!
원문 | Hey, let's play cards."
원문 | PLAY AGAINST SAKI?
원문 | {0D}
```

```
번역 | 사키
번역 | "안녕, 나는 사키야.
번역 | 유키는 날 "맹꽁이"라고 불러.
번역 | 너무하지 않아?
번역 | 후회하게 해 줄 거야!
번역 | 자, 카드 하자."
번역 | 사키와 겨룰까요?
번역 | {0D}
```

### `0711EC`  54 → 37바이트

```
원문 | SAKI
원문 | "Ha-ah! I lost again...
원문 | Here's your card! Shoot!"
```

```
번역 | 사키
번역 | "아아! 또 졌어…
번역 | 카드 여기! 칫!"
```

### `0711F0`  128 → 126바이트

```
원문 | YUKI
원문 | "Bongiorno! I'm Yuki.
원문 | I love CARD CLASH.
원문 | I can't get enough of the game!
원문 | How about a game -- or 100?"
원문 | 
원문 | PLAY AGAINST YUKI?
원문 | {0D}
```

```
번역 | 유키
번역 | "본조르노! 나는 유키야.
번역 | 카드 클래시를 정말 좋아해.
번역 | 아무리 해도 질리지가 않아!
번역 | 한판… 아니 백판 어때?"
번역 | 
번역 | 유키와 겨룰까요?
번역 | {0D}
```

### `0711F4`  37 → 29바이트

```
원문 | YUKI
원문 | "That's the spirit. Let's play!"
```

```
번역 | 유키
번역 | "바로 그거지. 시작하자!"
```

### `0711F8`  69 → 51바이트

```
원문 | YUKI
원문 | "Oh, I'm crushed!
원문 | Play me again, okay?
원문 | I'll be waiting for you."
```

```
번역 | 유키
번역 | "아, 속상해!
번역 | 또 붙어 줘, 응?
번역 | 기다리고 있을게."
```

### `0711FC`  88 → 62바이트

```
원문 | YUKI
원문 | "Oh, that was a close game.
원문 | I have two of these cards.
원문 | It's yours. Can you use it?"
```

```
번역 | 유키
번역 | "아, 아슬아슬했네.
번역 | 이 카드 두 장 있어.
번역 | 너 가져. 쓸 만해?"
```

### `071200`  61 → 47바이트

```
원문 | YUKI
원문 | "I'll win next time for sure!
원문 | Just sit back...and lose!"
```

```
번역 | 유키
번역 | "다음엔 꼭 이긴다!
번역 | 가만히 앉아서… 져 봐!"
```

### `071204`  62 → 56바이트

```
원문 | YUKI
원문 | "Come to mama, I win!
원문 | At this pace,
원문 | I'll be unstoppable!"
```

```
번역 | 유키
번역 | "이리 오렴, 내가 이겼다!
번역 | 이 기세면
번역 | 아무도 못 막아!"
```

### `071208`  102 → 86바이트

```
원문 | YUKI
원문 | "Bongiorno! You're back!
원문 | Let's play CARD CLASH!
원문 | You can't just win and run!"
원문 | PLAY AGAINST YUKI?
원문 | {0D}
```

```
번역 | 유키
번역 | "본조르노! 또 왔네!
번역 | 카드 클래시 하자!
번역 | 이기고 그냥 갈 순 없지!"
번역 | 유키와 겨룰까요?
번역 | {0D}
```

### `07120C`  88 → 67바이트

```
원문 | YUKI
원문 | "Aw, I should of put that there!!
원문 | I got two of these cards.
원문 | Here. Can you use one?"
```

```
번역 | 유키
번역 | "아, 저기 놨어야 했는데!!
번역 | 이 카드 두 장 있어.
번역 | 자. 한 장 쓸래?"
```

### `071214`  65 → 48바이트

```
원문 | (IT'S A ZOMBIE COMING TO GET
원문 | YOU!!)
원문 | What will you do?!
원문 | 
원문 | ESCAPE?
원문 | {0D}
```

```
번역 | (좀비가 다가온다!!)
번역 | 어떻게 할까?!
번역 | 
번역 | 도망칠까요?
번역 | {0D}
```

### `071218`  40 → 36바이트

```
원문 | ZOMBIE
원문 | "Ooooh Whoaaaa...
원문 | (IT LOOKS SAD.)
```

```
번역 | 좀비
번역 | "우우우 와아아…
번역 | (슬퍼 보인다.)
```

### `07121C`  150 → 104바이트

```
원문 | ZOMBIE
원문 | "Pwaah!
원문 | How was I?! Scary, huh!
원문 | Glad to meet you.
원문 | Name's Yosiki.
원문 | Quite a good job...
원문 | this make-up!
원문 | Oh, almost forgot.
원문 | Got to give this to you."
```

```
번역 | 좀비
번역 | "푸하!
번역 | 어땠어?! 무서웠지!
번역 | 반가워.
번역 | 난 요시키야.
번역 | 제법이지…
번역 | 이 분장!
번역 | 아, 깜빡할 뻔했다.
번역 | 이거 줘야지."
```

### `071220`  63 → 48바이트

```
원문 | YOSIKI
원문 | "Well, I'll be on my way!
원문 | We'll meet again soon. Maybe."
```

```
번역 | 요시키
번역 | "자, 난 이만 간다!
번역 | 곧 또 보자고. 아마도."
```

### `071224`  49 → 48바이트

```
원문 | ZOMBIE
원문 | "Oooooooh!
원문 | (...???
원문 | A VICTORY CALL, MAYBE?)
```

```
번역 | 좀비
번역 | "우우우우우!
번역 | (…???
번역 | 이긴 걸 알리는 소린가?)
```

### `071228`  86 → 70바이트

```
원문 | ZOMBIE
원문 | "Ooowhoa...Uh?
원문 | (???LOOKS LIKE THE
원문 | ZOMBIE WANTS TO PLAY.)
원문 | PLAY AGAINST ZOMBIE?
원문 | {0D}
```

```
번역 | 좀비
번역 | "우우와… 어?
번역 | (???좀비가
번역 | 한판 하자는 것 같다.)
번역 | 좀비와 겨룰까요?
번역 | {0D}
```

### `071230`  46 → 36바이트

```
원문 | ZOMBIE
원문 | "Wh, Whoooo ooooh....
원문 | (...WHO IS THIS?)
```

```
번역 | 좀비
번역 | "우, 우우우 우우….
번역 | (…누구지?)
```

### `071234`  40 → 35바이트

```
원문 | ZOMBIE
원문 | "Whooooooooaaa!
원문 | (...WHO IS THIS?)
```

```
번역 | 좀비
번역 | "우우우우우우아아!
번역 | (…누구지?)
```

### `071238`  99 → 97바이트

```
원문 | MIKAMI
원문 | "Welcome to "Evil Manor!"
원문 | If you want this coin,
원문 | you must defeat us."
원문 | PLAY AGAINST MIKAMI?
원문 | {0D}
```

```
번역 | 미카미
번역 | "악의 저택에 온 걸 환영한다!
번역 | 이 코인이 갖고 싶다면
번역 | 우리를 꺾어야 해."
번역 | 미카미와 겨룰까요?
번역 | {0D}
```

### `07123C`  80 → 69바이트

```
원문 | MIKAMI
원문 | "OK. You've got guts!
원문 | We'll see how tough you are
원문 | against my 'Evil' deck!
```

```
번역 | 미카미
번역 | "좋아. 배짱 있군!
번역 | 내 "이블" 덱을 상대로
번역 | 얼마나 버티는지 보자!"
```

### `071240`  70 → 61바이트

```
원문 | MIKAMI
원문 | "No way! No way!
원문 | That's not enough to
원문 | experience true horror!!"
```

```
번역 | 미카미
번역 | "안 돼! 안 돼!
번역 | 그 정도로는 진짜 공포를
번역 | 맛볼 수 없어!!"
```

### `071244`  112 → 104바이트

```
원문 | MIKAMI
원문 | "That's it. That is it!!!
원문 | That deck can make
원문 | real horror!!!
원문 | Find out what real horror
원문 | is with this card."
```

```
번역 | 미카미
번역 | "그거야. 바로 그거!!!
번역 | 그 덱이라면
번역 | 진짜 공포를 만들 수 있어!!!
번역 | 이 카드로
번역 | 진짜 공포가 뭔지 알아봐."
```

### `071248`  63 → 59바이트

```
원문 | MIKAMI
원문 | "Yeah. I lost. But real horror...
원문 | That's where it's at!"
```

```
번역 | 미카미
번역 | "그래, 내가 졌다.
번역 | 하지만 진짜 공포…
번역 | 그게 핵심이지!"
```

### `07124C`  67 → 56바이트

```
원문 | MIKAMI
원문 | "My 'Evil' deck's unbeatable!
원문 | I'll play you again, anytime!"
```

```
번역 | 미카미
번역 | "내 "이블" 덱은 무적이야!
번역 | 언제든 다시 붙어 주지!"
```

### `071250`  98 → 76바이트

```
원문 | MIKAMI
원문 | "So, you've returned.
원문 | Once you know real horror,
원문 | you can't go back!"
원문 | PLAY AGAINST MIKAMI?
원문 | {0D}
```

```
번역 | 미카미
번역 | "또 왔군.
번역 | 진짜 공포를 한번 알면
번역 | 돌아갈 수 없지!"
번역 | 미카미와 겨룰까요?
번역 | {0D}
```

### `071254`  83 → 70바이트

```
원문 | MIKAMI
원문 | "Good. That's the spirit!
원문 | Let's enjoy real horror.
원문 | Let's savor it together."
```

```
번역 | 미카미
번역 | "좋아. 그 기백이야!
번역 | 진짜 공포를 즐겨 보자.
번역 | 함께 음미해 보자고."
```

### `071258`  148 → 126바이트

```
원문 | MIKAMI
원문 | "That's it! That's the stuff!
원문 | I knew you understood.
원문 | This is what horror's about.
원문 | Experience even great horror.
원문 | Take this card, if you dare!"
```

```
번역 | 미카미
번역 | "그거야! 바로 그거!
번역 | 네가 이해했을 줄 알았어.
번역 | 이게 바로 공포라는 거다.
번역 | 더 큰 공포를 맛봐라.
번역 | 용기 있으면 이 카드를 받아!"
```

### `07125C`  74 → 62바이트

```
원문 | MIKAMI
원문 | "What do you mean, Be quiet?
원문 | It ruins the horror?
원문 | Well, excuse me!"
```

```
번역 | 미카미
번역 | "조용히 하라니?
번역 | 공포가 깨진다고?
번역 | 허 참, 미안하게 됐군!"
```

### `071260`  120 → 97바이트

```
원문 | YURI
원문 | "'RESIDENT EVIL' sure is scary,
원문 | huh?
원문 | 
원문 | ...But enough of that story.
원문 | How about some CARD CLASH?"
원문 | PLAY AGAINST YURI?
원문 | {0D}
```

```
번역 | 유리
번역 | ""바이오하자드" 진짜 무섭지?
번역 | 
번역 | …그 얘긴 그만하고.
번역 | 카드 클래시 한판 어때?"
번역 | 유리와 겨룰까요?
번역 | {0D}
```

### `071264`  33 → 40바이트  (빈 곳으로 옮겨 담음)

```
원문 | YURI
원문 | "Let's begin.
원문 | I feel lucky!"
```

```
번역 | 유리
번역 | "시작하자.
번역 | 오늘 운이 좋은 것 같아!"
```

### `071268`  62 → 36바이트

```
원문 | YURI
원문 | "That's that... Well, let's
원문 | get together again sometime."
```

```
번역 | 유리
번역 | "그렇구나… 그럼
번역 | 언제 또 보자."
```

### `07126C`  59 → 43바이트

```
원문 | YURI
원문 | "Geez! I lost, didn't I?
원문 | Well, here's a card for you."
```

```
번역 | 유리
번역 | "어휴! 내가 졌네?
번역 | 자, 카드 하나 줄게."
```

### `071270`  95 → 94바이트

```
원문 | YURI
원문 | "What if a zombie came now?
원문 | ...That is, care to discuss the
원문 | scariness of 'RESIDENT EVIL'?"
```

```
번역 | 유리
번역 | "지금 좀비가 나타나면 어쩌지?
번역 | …아니 그게,
번역 | "바이오하자드"가 얼마나 무서운지 얘기해 볼래?"
```

### `071274`  58 → 55바이트

```
원문 | YURI
원문 | "Rest in peace!
원문 | ...Hey, I sound like
원문 | Ibuki, don't I?"
```

```
번역 | 유리
번역 | "편히 잠들거라!
번역 | …어라, 나 이부키 같은
번역 | 말투 아냐?"
```

### `071278`  103 → 88바이트

```
원문 | YURI
원문 | "Kenzan Ibuki! ...Ah...
원문 | That's Ibuki's line, huh?
원문 | How about some CARD CLASH?"
원문 | PLAY AGAINST YURI?
원문 | {0D}
```

```
번역 | 유리
번역 | "참견 무용! …아…
번역 | 그거 이부키 대사잖아?
번역 | 카드 클래시 한판 어때?"
번역 | 유리와 겨룰까요?
번역 | {0D}
```

### `07127C`  75 → 53바이트

```
원문 | YURI
원문 | "Well, let's get started.
원문 | I've gotten better.
원문 | I won't lose so easily!"
```

```
번역 | 유리
번역 | "자, 시작하자.
번역 | 나 많이 늘었어.
번역 | 그리 쉽게 안 져!"
```

### `071280`  49 → 38바이트

```
원문 | YURI
원문 | "Huh? I lost again...
원문 | Here, take this card."
```

```
번역 | 유리
번역 | "어? 또 졌네…
번역 | 자, 이 카드 받아."
```

### `071284`  66 → 41바이트

```
원문 | YURI
원문 | "That was fun.
원문 | How about challenging me
원문 | to a quiz next time?"
```

```
번역 | 유리
번역 | "재밌었어.
번역 | 다음엔 퀴즈로 겨뤄 볼래?"
```

### `071288`  73 → 59바이트

```
원문 | YURI
원문 | "You're still a tyro!
원문 | ...Uh oh. That's...
원문 | That's Ibuki's line, huh."
```

```
번역 | 유리
번역 | "아직 애송이로구나!
번역 | …어이쿠. 그것도
번역 | 이부키 대사잖아."
```

### `07128C`  108 → 91바이트

```
원문 | SHIN
원문 | "All right! At last!
원문 | I'm going to win for sure!
원문 | 
원문 | And you must do one thing:
원문 | That's lose, and lose big!"
```

```
번역 | 신
번역 | "좋았어! 드디어!
번역 | 이번엔 반드시 이긴다!
번역 | 
번역 | 너는 딱 하나만 하면 돼.
번역 | 지는 거야, 그것도 크게!"
```

### `071290`  75 → 73바이트

```
원문 | SHIN
원문 | "Argh! You won!
원문 | No excuses.
원문 | 
원문 | Oh, here. Take this!
원문 | It might be useful!"
```

```
번역 | 신
번역 | "윽! 네가 이겼구나!
번역 | 변명은 없다.
번역 | 
번역 | 자, 여기. 받아!
번역 | 쓸모 있을지도 몰라!"
```

### `071294`  26 → 21바이트

```
원문 | SHIN
원문 | "Good luck, big guy!"
```

```
번역 | 신
번역 | "잘해 봐라, 친구!"
```

### `071298`  57 → 51바이트

```
원문 | SHIN
원문 | "All right! I won!
원문 | So guts are what
원문 | it's all about!"
```

```
번역 | 신
번역 | "좋았어! 내가 이겼다!
번역 | 역시 근성이
번역 | 제일이라니까!"
```

### `07129C`  60 → 44바이트

```
원문 | SHIN
원문 | "What? Hey! {08}!
원문 | How about a game?"
원문 | 
원문 | PLAY AGAINST SHIN?
원문 | {0D}
```

```
번역 | 신
번역 | "어? 야! {08}!
번역 | 한판 어때?"
번역 | 
번역 | 신과 겨룰까요?
번역 | {0D}
```

### `0712A0`  51 → 38바이트

```
원문 | SHIN
원문 | "OK! Let's play!
원문 | I'll win for sure this time!"
```

```
번역 | 신
번역 | "좋아! 시작하자!
번역 | 이번엔 꼭 이긴다!"
```

### `0712A4`  65 → 47바이트

```
원문 | SHIN
원문 | "What? You busy?
원문 | I'm always here.
원문 | Drop by when you're free."
```

```
번역 | 신
번역 | "뭐? 바빠?
번역 | 난 늘 여기 있어.
번역 | 한가할 때 들러."
```

### `0712A8`  50 → 36바이트

```
원문 | SHIN
원문 | "Oh rats! I lost...
원문 | Here's your stupid card."
```

```
번역 | 신
번역 | "에잇! 졌잖아…
번역 | 자, 카드 가져가."
```

### `0712AC`  76 → 60바이트

```
원문 | SHIN
원문 | "Ooh hoo hoo!
원문 | I can read you like a book.
원문 | When we meet next, I'll win!"
```

```
번역 | 신
번역 | "오 호 호!
번역 | 네 속은 훤히 보여.
번역 | 다음에 만나면 내가 이긴다!"
```

### `0712B0`  68 → 63바이트

```
원문 | CAP
원문 | "Whew!
원문 | Sorry, but...
원문 | I just can't lose...
원문 | No mercy!
원문 | Let's play!"
```

```
번역 | 캡
번역 | "휴!
번역 | 미안하지만…
번역 | 난 질 수 없어…
번역 | 봐주지 않는다!
번역 | 한판 하자!"
```

### `0712B4`  68 → 53바이트

```
원문 | CAP
원문 | "It's your victory.
원문 | Whether this card helps
원문 | is all up to you..."
```

```
번역 | 캡
번역 | "네 승리다.
번역 | 이 카드가 도움이 될지는
번역 | 네게 달렸어…"
```

### `0712B8`  22 → 25바이트  (빈 곳으로 옮겨 담음)

```
원문 | CAP
원문 | "I must be going."
```

```
번역 | 캡
번역 | "난 이만 가 봐야겠다."
```

### `0712BC`  52 → 38바이트

```
원문 | CAP
원문 | "Whew!
원문 | Good game...
원문 | Let's do it again sometime."
```

```
번역 | 캡
번역 | "휴!
번역 | 좋은 승부였어…
번역 | 언제 또 하자."
```

### `0712C0`  61 → 47바이트

```
원문 | CAP
원문 | "Greetings.
원문 | Care to try your stuff?"
원문 | 
원문 | PLAY AGAINST CAP?
원문 | {0D}
```

```
번역 | 캡
번역 | "안녕.
번역 | 실력 좀 보여 줄래?"
번역 | 
번역 | 캡과 겨룰까요?
번역 | {0D}
```

### `0712C4`  30 → 18바이트

```
원문 | CAP
원문 | "Well, let's get started."
```

```
번역 | 캡
번역 | "자, 시작하자."
```

### `0712C8`  38 → 30바이트

```
원문 | CAP
원문 | "Game over...
원문 | Until next we meet."
```

```
번역 | 캡
번역 | "승부 끝…
번역 | 다음에 또 보자."
```

### `0712CC`  129 → 104바이트

```
원문 | KEI
원문 | "You're one tough cookie!"
원문 | But since I've come this far,
원문 | I won't lose to you.
원문 | Resign yourself to reality.
원문 | Let's get dealing!"
```

```
번역 | 케이
번역 | "만만찮은 상대군!
번역 | 하지만 여기까지 온 이상
번역 | 너에게 질 수 없어.
번역 | 현실을 받아들여라.
번역 | 자, 카드를 돌리자!"
```

### `0712D0`  115 → 99바이트

```
원문 | KEI
원문 | "Guess I lost...
원문 | I shouldn't have held back.
원문 | Well, no complaints.
원문 | With this card, 
원문 | your deck'll be unbeatable!"
```

```
번역 | 케이
번역 | "내가 졌구나…
번역 | 봐주지 말았어야 했는데.
번역 | 뭐, 불만은 없다.
번역 | 이 카드가 있으면
번역 | 네 덱은 무적일 거야!"
```

### `0712D4`  29 → 23바이트

```
원문 | KEI
원문 | "Well, good luck to you!"
```

```
번역 | 케이
번역 | "자, 행운을 빈다!"
```

### `0712D8`  54 → 68바이트  (빈 곳으로 옮겨 담음)

```
원문 | KEI
원문 | "Yes! I won!
원문 | Don't feel bad.
원문 | Cards are no picnic!"
```

```
번역 | 케이
번역 | "좋았어! 내가 이겼다!
번역 | 너무 상심 마.
번역 | 카드가 만만한 게 아니거든!"
```

### `0712DC`  88 → 78바이트

```
원문 | KEI
원문 | "Hey! {08}!
원문 | You're looking bored.
원문 | If you're bored, it's card time!"
원문 | PLAY AGAINST KEI?
원문 | {0D}
```

```
번역 | 케이
번역 | "어이! {08}!
번역 | 심심해 보이는데.
번역 | 심심하면 카드 할 시간이지!"
번역 | 케이와 겨룰까요?
번역 | {0D}
```

### `0712E0`  43 → 33바이트

```
원문 | KEI
원문 | "That's the spirit!
원문 | Let's get playing!"
```

```
번역 | 케이
번역 | "그 기백이야!
번역 | 자, 시작하자!"
```

### `0712E4`  43 → 36바이트

```
원문 | KEI
원문 | "Wow, how boring!
원문 | Well, see you later."
```

```
번역 | 케이
번역 | "와, 재미없기는!
번역 | 그럼 또 보자."
```

### `0712E8`  68 → 57바이트

```
원문 | KEI
원문 | "Oh no! I lost!
원문 | Oh well, that's life.
원문 | Here, take this with you."
```

```
번역 | 케이
번역 | "이런! 졌잖아!
번역 | 뭐, 사는 게 그렇지.
번역 | 자, 이거 가져가."
```

### `0712EC`  98 → 79바이트

```
원문 | KEI
원문 | "Well, that's enough for today.
원문 | But I'll win the next time we
원문 | meet.
원문 | Count on it, card battler!
```

```
번역 | 케이
번역 | "오늘은 이만하자.
번역 | 하지만 다음에 만나면
번역 | 내가 이긴다.
번역 | 두고 봐, 카드 파이터!"
```

### `0712F0`  96 → 78바이트

```
원문 | KEI
원문 | "That's more like it! I win!
원문 | This is what victory's about!
원문 | I'm just too good. Later, loser!"
```

```
번역 | 케이
번역 | "그래야지! 내가 이겼다!
번역 | 승리란 이런 거야!
번역 | 난 너무 잘해. 잘 가라, 패배자!"
```

### `0712F4`  129 → 91바이트

```
원문 | COMET
원문 | "Hello there.
원문 | Time for the big game.
원문 | I can't say I'll win for sure...
원문 | but I don't intend to lose.
원문 | So, let's start playing!"
```

```
번역 | 코멧
번역 | "안녕.
번역 | 큰 승부를 할 시간이야.
번역 | 꼭 이긴다고는 못 하지만…
번역 | 질 생각도 없어.
번역 | 자, 시작하자!"
```

### `0712F8`  120 → 89바이트

```
원문 | COMET
원문 | "That was impressive.
원문 | With that talent,
원문 | you may just win it all.
원문 | If this card can help out,
원문 | I'll be tickled pink!"
```

```
번역 | 코멧
번역 | "대단했어.
번역 | 그 재능이면
번역 | 다 이길 수도 있겠어.
번역 | 이 카드가 도움이 된다면
번역 | 나도 기쁠 거야!"
```

### `0712FC`  34 → 25바이트

```
원문 | COMET
원문 | "Let's play again some day."
```

```
번역 | 코멧
번역 | "언제 또 한판 하자."
```

### `071300`  80 → 54바이트

```
원문 | COMET
원문 | "Well, that's the game.
원문 | I sure had a fun time.
원문 | Let's face off again soon."
```

```
번역 | 코멧
번역 | "자, 승부는 끝났네.
번역 | 정말 즐거웠어.
번역 | 곧 또 겨루자."
```

### `071304`  84 → 67바이트

```
원문 | COMET
원문 | "Hello, {08}.
원문 | I'll show you my hand,
원문 | if you show me yours."
원문 | PLAY AGAINST COMET?
원문 | {0D}
```

```
번역 | 코멧
번역 | "안녕, {08}.
번역 | 네가 패를 보이면
번역 | 나도 보여 줄게."
번역 | 코멧과 겨룰까요?
번역 | {0D}
```

### `071308`  83 → 55바이트

```
원문 | COMET
원문 | "Well, let's get started.
원문 | I let you win last time,
원문 | but this time, forget it!"
```

```
번역 | 코멧
번역 | "자, 시작하자.
번역 | 지난번엔 봐줬지만
번역 | 이번엔 어림없어!"
```

### `07130C`  60 → 41바이트

```
원문 | COMET
원문 | "That's that. Well, if you
원문 | change your mind, call me."
```

```
번역 | 코멧
번역 | "그렇구나. 뭐,
번역 | 마음 바뀌면 불러 줘."
```

### `071310`  41 → 39바이트

```
원문 | COMET
원문 | "Tough as ever...
원문 | Here, take this."
```

```
번역 | 코멧
번역 | "여전히 만만찮네…
번역 | 자, 이거 받아."
```

### `071314`  59 → 53바이트

```
원문 | COMET
원문 | "'Pride goes before a fall.'
원문 | Don't get cocky, kiddo!"
```

```
번역 | 코멧
번역 | ""교만은 패망의 선봉이라."
번역 | 으스대지 마라, 꼬마!"
```

### `071318`  74 → 59바이트

```
원문 | COMET
원문 | "Oh, over so soon.
원문 | Let's play again!.
원문 | I can't wait to see who wins."
```

```
번역 | 코멧
번역 | "아, 벌써 끝났네.
번역 | 또 하자!
번역 | 누가 이길지 궁금해 죽겠어."
```

### `07131C`  129 → 104바이트

```
원문 | KID
원문 | "Hey, {08}!
원문 | I don't know what's going on,
원문 | but I got this invitation.
원문 | Anyway, think you can beat me?
원문 | Come on, let's play a game."
```

```
번역 | 키드
번역 | "어이, {08}!
번역 | 무슨 일인지는 모르겠는데
번역 | 이런 초대장을 받았어.
번역 | 어쨌든, 날 이길 수 있겠어?
번역 | 자, 한판 하자."
```

### `071320`  147 → 117바이트

```
원문 | KID
원문 | "Ugh. I really stunk.
원문 | I was so sure of this deck.
원문 | Just what happened here?
원문 | Oh well, here's a card for you.
원문 | ...I don't know what it is,
원문 | though."
```

```
번역 | 키드
번역 | "윽. 형편없었어.
번역 | 이 덱이면 될 줄 알았는데.
번역 | 대체 뭐가 잘못된 거지?
번역 | 에이, 카드 하나 줄게.
번역 | …뭔지는 나도 모르지만."
```

### `071324`  33 → 31바이트

```
원문 | KID
원문 | "When did you get so strong?"
```

```
번역 | 키드
번역 | "언제 이렇게 강해진 거야?"
```

### `071328`  90 → 76바이트

```
원문 | FO
원문 | "Ai yah!...
원문 | What's going in here?
원문 | I got invitation to here.
원문 | Anyway, you go easy on me!"
```

```
번역 | 포
번역 | "아이고!…
번역 | 여긴 무슨 일이오?
번역 | 나도 초대장을 받았소.
번역 | 어쨌든 살살해 주시오!"
```

### `07132C`  106 → 93바이트

```
원문 | FO
원문 | "Ai yah!... I lost...
원문 | I tried so hard.
원문 | But no regrets!
원문 | Here, you takey this!
원문 | Go on, takey it with you!"
```

```
번역 | 포
번역 | "아이고!… 졌구먼…
번역 | 열심히 했는데.
번역 | 그래도 후회는 없소!
번역 | 자, 이거 받아요!
번역 | 어서, 가져가시오!"
```

### `071330`  18 → 20바이트  (빈 곳으로 옮겨 담음)

```
원문 | FO
원문 | "Good luck, {08}!"
```

```
번역 | 포
번역 | "행운을 비오, {08}!"
```

### `071334`  110 → 98바이트

```
원문 | NISHI
원문 | "Hey! Is CARD CLASH that fun?
원문 | I remembered the rules.
원문 | Can I oblige you to a game?"
원문 | PLAY AGAINST NISHI?
원문 | {0D}
```

```
번역 | 니시
번역 | "어이! 카드 클래시가 그리 재밌소?
번역 | 나도 규칙을 익혔소.
번역 | 한판 청해도 되겠소?"
번역 | 니시와 겨룰까요?
번역 | {0D}
```

### `071338`  27 → 21바이트

```
원문 | NISHI
원문 | "Take it easy on me."
```

```
번역 | 니시
번역 | "살살해 주시오."
```

### `07133C`  27 → 24바이트

```
원문 | NISHI
원문 | "No? That's too bad."
```

```
번역 | 니시
번역 | "싫다고? 아쉽구먼."
```

### `071340`  117 → 90바이트

```
원문 | NISHI
원문 | "Hey, you can do that?
원문 | That is fascinating.
원문 | ...Oh, by the way,
원문 | Here's a 'GEESE' card.
원문 | It may be useful to you."
```

```
번역 | 니시
번역 | "어이, 그렇게도 되는구먼?
번역 | 참 흥미롭소.
번역 | …아 참,
번역 | "기스" 카드가 있소.
번역 | 쓸모가 있을지도."
```

### `071344`  28 → 26바이트

```
원문 | NISHI
원문 | "I'm busy. Excuse me."
```

```
번역 | 니시
번역 | "바쁘오. 실례하겠소."
```

### `071348`  78 → 66바이트

```
원문 | NISHI
원문 | "I won, didn't I? Hmm...
원문 | Whoops, look at the time.
원문 | I got a meeting. Ta!"
```

```
번역 | 니시
번역 | "내가 이겼구먼? 흠…
번역 | 어이쿠, 벌써 시간이.
번역 | 회의가 있소. 이만!"
```

### `07134C`  66 → 57바이트

```
원문 | NISHI
원문 | "So, we meet again.
원문 | Some CARD CLASH?"
원문 | 
원문 | PLAY AGAINST NISHI?
원문 | {0D}
```

```
번역 | 니시
번역 | "또 만났구먼.
번역 | 카드 클래시 한판?"
번역 | 
번역 | 니시와 겨룰까요?
번역 | {0D}
```

### `071350`  93 → 60바이트

```
원문 | NISHI
원문 | "Hey, that's one way to do it.
원문 | That is fascinating....
원문 | Here's a token of my gratitude."
```

```
번역 | 니시
번역 | "어이, 그런 수도 있구먼.
번역 | 참 흥미롭소….
번역 | 감사의 표시요."
```

### `071354`  50 → 41바이트

```
원문 | NISHI
원문 | "Whoops. Look at the time...
원문 | Must be going!"
```

```
번역 | 니시
번역 | "어이쿠. 벌써 시간이…
번역 | 가 봐야겠소!"
```

### `071358`  92 → 80바이트

```
원문 | NISHI
원문 | "Ha, ha, ha. I won!
원문 | Golly, is it that time already?
원문 | I'm so busy, I can't stand it...."
```

```
번역 | 니시
번역 | "하하하. 내가 이겼소!
번역 | 어이쿠, 벌써 이 시간인가?
번역 | 바빠서 견딜 수가 없구먼…."
```

### `07135C`  80 → 61바이트

```
원문 | SHIN
원문 | "{08}! It's been ages!
원문 | I've been workin' out.
원문 | How about you?
원문 | Let's mix it up!"
```

```
번역 | 신
번역 | "{08}! 오랜만이야!
번역 | 나 열심히 단련했어.
번역 | 너는 어때?
번역 | 한판 붙자!"
```

### `071360`  95 → 67바이트

```
원문 | SHIN
원문 | "Ugh. I lost...
원문 | ...I can't bear it, but I lost.
원문 | 
원문 | Your an awesome force,
원문 | {08}! You won again!"
```

```
번역 | 신
번역 | "윽. 졌어…
번역 | …분하지만 졌다.
번역 | 
번역 | 너 정말 대단하구나,
번역 | {08}! 또 이겼어!"
```

### `071364`  61 → 49바이트

```
원문 | SHIN
원문 | "I am victorious!
원문 | Whew! That was close!
원문 | Let's go again!"
```

```
번역 | 신
번역 | "내가 이겼다!
번역 | 휴! 아슬아슬했어!
번역 | 한판 더 가자!"
```

### `071368`  120 → 100바이트

```
원문 | CAP
원문 | "Hmp...You kept me waiting.
원문 | I can't believe you got so
원문 | good in this short time. Bizarre!
원문 | Let's play like champions!"
```

```
번역 | 캡
번역 | "흠… 기다리게 하는군.
번역 | 이 짧은 사이에 이렇게 늘다니
번역 | 믿기지가 않아. 놀랍군!
번역 | 챔피언답게 겨뤄 보자!"
```

### `07136C`  98 → 71바이트

```
원문 | CAP
원문 | "Hmph...
원문 | For you to get this tough...
원문 | It boggles the mind.
원문 | Congratulations!
원문 | You have won big!"
```

```
번역 | 캡
번역 | "흠…
번역 | 이만큼 강해지다니…
번역 | 놀라울 따름이야.
번역 | 축하한다!
번역 | 크게 이겼구나!"
```

### `071370`  65 → 48바이트

```
원문 | CAP
원문 | "Phew....
원문 | I can't afford to lose...
원문 | Don't think badly of me."
```

```
번역 | 캡
번역 | "휴….
번역 | 난 질 수 없어…
번역 | 나쁘게 생각하지 마라."
```

### `071374`  182 → 137바이트

```
원문 | SHIN
원문 | "Hey, {08}!
원문 | Let's try some special rules,
원문 | huh?
원문 | It could be thrilling, I think.
원문 | Let's mix our decks together.
원문 | And 3 or more of the same
원문 | cards can be in a deck."
원문 | PLAY AGAINST SHIN?
원문 | {0D}
```

```
번역 | 신
번역 | "어이, {08}!
번역 | 특별 규칙으로 해 볼까?
번역 | 
번역 | 꽤 짜릿할 것 같은데.
번역 | 서로 덱을 섞자.
번역 | 그리고 같은 카드를
번역 | 3장 넘게 넣어도 되는 걸로."
번역 | 신과 겨룰까요?
번역 | {0D}
```

### `071378`  29 → 21바이트

```
원문 | SHIN
원문 | "Okay. Let's mix decks!"
```

```
번역 | 신
번역 | "좋아. 덱을 섞자!"
```

### `07137C`  87 → 73바이트

```
원문 | SHIN
원문 | "No? Could've been fun.
원문 | Well, then.
원문 | How about a normal game?"
원문 | PLAY AGAINST SHIN?
원문 | {0D}
```

```
번역 | 신
번역 | "싫다고? 재밌었을 텐데.
번역 | 그럼 뭐.
번역 | 보통 규칙으로 할까?"
번역 | 신과 겨룰까요?
번역 | {0D}
```

### `071380`  38 → 20바이트

```
원문 | SHIN
원문 | "All right! Let's start playing!"
```

```
번역 | 신
번역 | "좋아! 시작하자!"
```

### `071384`  85 → 59바이트

```
원문 | SHIN
원문 | "What? Don't feel like playing?
원문 | After all your wins,
원문 | have you lost your hunger?"
```

```
번역 | 신
번역 | "뭐? 할 생각 없어?
번역 | 그렇게 이겨 놓고
번역 | 의욕이 사라진 거야?"
```

### `071388`  20 → 18바이트

```
원문 | SHIN
원문 | "Crud! I lost!"
```

```
번역 | 신
번역 | "제기랄! 졌어!"
```

### `07138C`  33 → 27바이트

```
원문 | SHIN
원문 | "Well, I had a ball. Later!"
```

```
번역 | 신
번역 | "뭐, 즐거웠어. 또 보자!"
```

### `071394`  27 → 23바이트

```
원문 | SHIN
원문 | "Let's jumble rumble!"
```

```
번역 | 신
번역 | "자, 뒤죽박죽 가자!"
```

### `071398`  67 → 50바이트

```
원문 | SHIN
원문 | "Heh, heh, heh.
원문 | With these new rules,
원문 | I may be the strongest!"
```

```
번역 | 신
번역 | "헤헤헤.
번역 | 이 새 규칙이면
번역 | 내가 제일 셀지도 몰라!"
```

### `07139C`  59 → 50바이트

```
원문 | SHIN
원문 | "Yes! I won!
원문 | That game was smokin'!
원문 | Let's play again!"
```

```
번역 | 신
번역 | "좋았어! 이겼다!
번역 | 방금 그 판 끝내줬어!
번역 | 또 하자!"
```

### `0713A0`  206 → 158바이트

```
원문 | CAP
원문 | "Hey!...
원문 | How about a change of pace?
원문 | 
원문 | Let's mix our decks together.
원문 | We might get something out of it.
원문 | These special rules allow you
원문 | to put
원문 | more than 3 of the same card in
원문 | a deck...."
원문 | PLAY AGAINST CAP?
원문 | {0D}
```

```
번역 | 캡
번역 | "어이…
번역 | 기분 전환 좀 할까?
번역 | 
번역 | 서로 덱을 섞어 보자.
번역 | 뭔가 얻는 게 있을지도 몰라.
번역 | 이 특별 규칙에서는
번역 | 같은 카드를 3장 넘게
번역 | 덱에 넣을 수 있다…."
번역 | 캡과 겨룰까요?
번역 | {0D}
```

### `0713A4`  26 → 20바이트

```
원문 | CAP
원문 | "Well, let's play...."
```

```
번역 | 캡
번역 | "자, 시작하지…."
```

### `0713A8`  77 → 59바이트

```
원문 | CAP
원문 | "You don't want to try it?
원문 | How about a normal game?"
원문 | 
원문 | PLAY AGAINST CAP?
원문 | {0D}
```

```
번역 | 캡
번역 | "해 볼 생각 없나?
번역 | 보통 규칙으로 할까?"
번역 | 
번역 | 캡과 겨룰까요?
번역 | {0D}
```

### `0713AC`  21 → 20바이트

```
원문 | CAP
원문 | "So, let's play."
```

```
번역 | 캡
번역 | "그럼, 시작하자."
```

### `0713B0`  38 → 34바이트

```
원문 | CAP
원문 | "I see...Well, I won't push you.."
```

```
번역 | 캡
번역 | "그렇군…. 뭐, 강요는 안 하지."
```

### `0713B4`  11 → 8바이트

```
원문 | CAP
원문 | "Hmph."
```

```
번역 | 캡
번역 | "흠."
```

### `0713B8`  35 → 23바이트

```
원문 | CAP
원문 | "That was an interesting game."
```

```
번역 | 캡
번역 | "흥미로운 승부였다."
```

### `0713BC`  20 → 21바이트  (빈 곳으로 옮겨 담음)

```
원문 | CAP
원문 | "Hmph. You won."
```

```
번역 | 캡
번역 | "흠. 네가 이겼군."
```

### `0713C0`  23 → 14바이트

```
원문 | CAP
원문 | "See you around..."
```

```
번역 | 캡
번역 | "또 보자…"
```

### `0713C4`  32 → 27바이트

```
원문 | CAP
원문 | "These new rules are fun..."
```

```
번역 | 캡
번역 | "이 새 규칙, 재미있군…"
```

### `0713C8`  48 → 41바이트

```
원문 | CAP
원문 | "Whew!
원문 | Good match...
원문 | I await our next game."
```

```
번역 | 캡
번역 | "휴!
번역 | 좋은 승부였다…
번역 | 다음을 기다리지."
```

### `0713CC`  94 → 73바이트

```
원문 | YOSIKI
원문 | "Whoa! We meet again!
원문 | Are you busy?
원문 | Let's play some CARD CLASH!"
원문 | PLAY AGAINST YOSIKI?
원문 | {0D}
```

```
번역 | 요시키
번역 | "오! 또 만났네!
번역 | 바빠?
번역 | 카드 클래시 한판 하자!"
번역 | 요시키와 겨룰까요?
번역 | {0D}
```

### `0713D0`  30 → 32바이트  (빈 곳으로 옮겨 담음)

```
원문 | YOSIKI
원문 | "OK. I'm free anytime."
```

```
번역 | 요시키
번역 | "좋아. 난 언제든 한가해."
```

### `0713D4`  64 → 45바이트

```
원문 | YOSIKI
원문 | "Oh, really?
원문 | Well, then, how about
원문 | a bike ride together?"
```

```
번역 | 요시키
번역 | "어, 그래?
번역 | 그럼 같이
번역 | 오토바이나 탈까?"
```

### `0713D8`  82 → 69바이트

```
원문 | YOSIKI
원문 | "Whoa! You trounced me!
원문 | Here's a "MECH-ZANGIEF" card.
원문 | It's super powerful!"
```

```
번역 | 요시키
번역 | "우와! 완전히 발렸네!
번역 | "메카 장기에프" 카드 줄게.
번역 | 엄청 세다고!"
```

### `0713DC`  66 → 57바이트

```
원문 | YOSIKI
원문 | "Quite rare, this is!"
원문 | Next time, though,
원문 | I intend to win!"
```

```
번역 | 요시키
번역 | "이거 꽤 귀한 거야!
번역 | 하지만 다음엔
번역 | 내가 이길 거야!"
```

### `0713E0`  93 → 86바이트

```
원문 | YOSIKI
원문 | "Ha ha ha! It's my win!
원문 | Well, I'll show you my rare...
원문 | Not! This is my little secret!"
```

```
번역 | 요시키
번역 | "하하하! 내가 이겼다!
번역 | 그럼 내 희귀 카드를 보여 주…
번역 | 지 말까! 이건 내 비밀이야!"
```

### `0713E4`  105 → 80바이트

```
원문 | YOSIKI
원문 | "We meet yet again!
원문 | How's the card I gave you?
원문 | Care to try it out with me?"
원문 | PLAY AGAINST YOSIKI?
원문 | {0D}
```

```
번역 | 요시키
번역 | "또 만났네!
번역 | 내가 준 카드는 어때?
번역 | 나랑 한번 써 볼래?"
번역 | 요시키와 겨룰까요?
번역 | {0D}
```

### `0713EC`  68 → 60바이트

```
원문 | YOSIKI
원문 | "Whew! I give! I give!
원문 | Well, then...
원문 | Take one of my doubles!"
```

```
번역 | 요시키
번역 | "휴! 항복! 항복!
번역 | 그럼 뭐…
번역 | 내 여분 카드 하나 가져가!"
```

### `0713F0`  88 → 74바이트

```
원문 | YOSIKI
원문 | "You calling me stingy?
원문 | Ha ha! Sticks and stones!
원문 | But don't knock my weak cards!"
```

```
번역 | 요시키
번역 | "나보고 짜다고?
번역 | 하하! 말은 말일 뿐!
번역 | 그래도 내 약한 카드 흉보지 마!"
```

### `0713F4`  61 → 50바이트

```
원문 | YOSIKI
원문 | "Whoo hoo! I won!
원문 | Oh, that was fun!
원문 | Let's play again!"
```

```
번역 | 요시키
번역 | "우후! 내가 이겼다!
번역 | 야, 재밌었어!
번역 | 또 하자!"
```

### `0713F8`  111 → 103바이트

```
원문 | MASK
원문 | "Whoo hah hah hah!
원문 | I'm Mask.
원문 | Mask, the Game Crusader!
원문 | Well, {08}!
원문 | Show me what you got!"
원문 | PLAY AGAINST MASK?
원문 | {0D}
```

```
번역 | 마스크
번역 | "우하하하하!
번역 | 나는 마스크.
번역 | 게임의 성전사 마스크다!
번역 | 자, {08}!
번역 | 네 실력을 보여라!"
번역 | 마스크와 겨룰까요?
번역 | {0D}
```

### `0713FC`  60 → 53바이트

```
원문 | MASK
원문 | "Hoo hoo hoo! It's a game!
원문 | Can you match my technique?"
```

```
번역 | 마스크
번역 | "후후후! 승부다!
번역 | 내 기술을 당해 낼 수 있겠나?"
```

### `071400`  78 → 61바이트

```
원문 | MASK
원문 | "You won't play?
원문 | Well, see you in the funny papers.
원문 | Whoo hah hah hah hah!
```

```
번역 | 마스크
번역 | "안 하겠다고?
번역 | 그럼 만화에서나 보자꾸나.
번역 | 우하하하하하!"
```

### `071404`  47 → 43바이트

```
원문 | MASK
원문 | "You passed the test!
원문 | Here's a cool card."
```

```
번역 | 마스크
번역 | "시험을 통과했군!
번역 | 멋진 카드를 주마."
```

### `071408`  146 → 108바이트

```
원문 | MASK
원문 | "It's too early to smile.
원문 | You need to work before you
원문 | can get the rare cards.
원문 | Hear the calling, the card calling!
원문 | Whooo hah hah hah hah hah!"
```

```
번역 | 마스크
번역 | "웃기엔 아직 이르다.
번역 | 희귀 카드를 얻으려면
번역 | 더 갈고닦아야 해.
번역 | 들리는가, 카드의 부름이!
번역 | 우하하하하하하!"
```

### `07140C`  71 → 58바이트

```
원문 | MASK
원문 | "Still green as a sprout.
원문 | Later, wimp!
원문 | Whooo hah hah hah hah hah!"
```

```
번역 | 마스크
번역 | "아직 새파랗구나.
번역 | 또 보자, 애송이!
번역 | 우하하하하하하!"
```

### `071410`  73 → 66바이트

```
원문 | MASK
원문 | "You've come quite far!
원문 | It's time to give you this.
원문 | Go on, take it."
```

```
번역 | 마스크
번역 | "제법 멀리까지 왔군!
번역 | 이제 이걸 줄 때가 됐다.
번역 | 어서, 받아라."
```

### `071414`  95 → 77바이트

```
원문 | MASK
원문 | "Uh oh. I must be off!
원문 | I may not look it, but I'm so busy.
원문 | Toodles! Whoo hah hah hah hah!"
```

```
번역 | 마스크
번역 | "어이쿠. 가 봐야겠군!
번역 | 이래 봬도 무척 바쁘다네.
번역 | 잘 있게! 우하하하하하!"
```

### `071418`  87 → 65바이트

```
원문 | MASK
원문 | "You haven't lost your stuff!
원문 | Impressive! Quite impressive!
원문 | I give you this card."
```

```
번역 | 마스크
번역 | "실력이 죽지 않았군!
번역 | 훌륭해! 아주 훌륭해!
번역 | 이 카드를 주마."
```

### `07141C`  83 → 70바이트

```
원문 | MASK
원문 | "Good gaming to you here on!
원문 | Later, you card demon!
원문 | Whoo hah hah hah hah hah!"
```

```
번역 | 마스크
번역 | "앞으로도 좋은 승부를!
번역 | 또 보자, 카드의 악마여!
번역 | 우하하하하하하!"
```

### `071434`  92 → 64바이트

```
원문 | SHIN
원문 | "You're going in my place!
원문 | So I won't forgive you if you
원문 | come back a loser. Good luck!"
```

```
번역 | 신
번역 | "내 몫까지 가는 거야!
번역 | 그러니 지고 돌아오면
번역 | 용서 안 해. 잘해!"
```

### `071438`  34 → 31바이트

```
원문 | CAP
원문 | "Hmph.
원문 | I'm...rooting for you."
```

```
번역 | 캡
번역 | "흠.
번역 | 난… 널 응원하고 있다."
```

### `07143C`  88 → 70바이트

```
원문 | KEI
원문 | "Because you beat me...
원문 | I won't forgive you if you lose.
원문 | Give 'em heck, you maniac!"
```

```
번역 | 케이
번역 | "날 이겼으니까…
번역 | 지면 용서 안 한다.
번역 | 실컷 해 줘라, 이 미치광이야!"
```

### `071440`  62 → 52바이트

```
원문 | COMET
원문 | "Well, off you go!
원문 | I'll be behind you...
원문 | like a shadow!"
```

```
번역 | 코멧
번역 | "자, 어서 가!
번역 | 난 뒤에서 지켜볼게…
번역 | 그림자처럼!"
```

### `071444`  92 → 85바이트

```
원문 | KID
원문 | "You can win. You got the stuff!
원문 | That is, your my disciple.
원문 | OK! Now go kick some booty!"
```

```
번역 | 키드
번역 | "넌 이길 수 있어. 실력이 있잖아!
번역 | 그러니까, 내 제자니까.
번역 | 좋아! 가서 다 쓸어버려!"
```

### `071448`  71 → 63바이트

```
원문 | FO
원문 | "If you win, I bake you a cake!
원문 | You come back a winner,
원문 | you listen?"
```

```
번역 | 포
번역 | "이기면 케이크를 구워 주겠소!
번역 | 꼭 이겨서 돌아오시오,
번역 | 알겠소?"
```

### `07144C`  29 → 24바이트

```
원문 | CAP
원문 | "Hmph. You're good, kid."
```

```
번역 | 캡
번역 | "흠. 제법이군, 꼬마."
```

### `071450`  58 → 48바이트

```
원문 | CAP
원문 | "Hmph.
원문 | You know what to do
원문 | with that card I gave you."
```

```
번역 | 캡
번역 | "흠.
번역 | 내가 준 그 카드를
번역 | 어떻게 쓸지는 알겠지."
```

### `071454`  102 → 81바이트

```
원문 | NISHI
원문 | "You can do things like that?
원문 | That's simply fascinating?
원문 | Here, take this card for your
원문 | trouble."
```

```
번역 | 니시
번역 | "그런 것도 되는구먼?
번역 | 참으로 흥미롭소.
번역 | 자, 수고한 값으로
번역 | 이 카드를 받으시오."
```

### `071458`  68 → 62바이트

```
원문 | YOSIKI
원문 | "Whoa! I give!
원문 | Strong as ever.
원문 | Here, take these extra cards!"
```

```
번역 | 요시키
번역 | "우와! 항복!
번역 | 여전히 세구나.
번역 | 자, 이 남는 카드들 가져가!"
```

### `07145C`  109 → 85바이트

```
원문 | YOSIKI
원문 | "Hey, we meet still again!
원문 | Care for some CARD CLASH?
원문 | Let's play a little game."
원문 | PLAY AGAINST YOSIKI?
원문 | {0D}
```

```
번역 | 요시키
번역 | "어, 또 만났네!
번역 | 카드 클래시 한판 어때?
번역 | 가볍게 한판 하자."
번역 | 요시키와 겨룰까요?
번역 | {0D}
```

### `071460`  162 → 137바이트

```
원문 | YOSIKI
원문 | "Whoa! We meet again!
원문 | I want to get into Peep Gem,
원문 | but I can't get in like this.
원문 | How about some CARD CLASH?
원문 | Come on, let's go nuts!"
원문 | PLAY AGAINST YOSIKI?
원문 | {0D}
```

```
번역 | 요시키
번역 | "오! 또 만났네!
번역 | 핍 젬에 들어가고 싶은데
번역 | 이래서는 못 들어가겠어.
번역 | 카드 클래시 한판 어때?
번역 | 자, 신나게 놀아 보자!"
번역 | 요시키와 겨룰까요?
번역 | {0D}
```

### `071464`  57 → 54바이트

```
원문 | YOSIKI
원문 | "You won't play? Rats!
원문 | Gee. I hope I get in soon."
```

```
번역 | 요시키
번역 | "안 한다고? 이런!
번역 | 에휴. 빨리 들어가야 할 텐데."
```

### `071468`  39 → 37바이트

```
원문 | SHIN
원문 | "Ouch! Geez!
원문 | Hey, watch it, huh?!"
```

```
번역 | 신
번역 | "아야! 이런!
번역 | 야, 조심 좀 해, 응?!"
```

### `07146C`  82 → 69바이트

```
원문 | AHM
원문 | "Hidey-ho, {08}
원문 | You should drop by
원문 | my place, sometime!
원문 | I may have some hot info!"
```

```
번역 | 아무
번역 | "안녕, {08}
번역 | 언제 우리 가게에
번역 | 한번 들러!
번역 | 좋은 정보가 있을지도 몰라!"
```

### `071470`  111 → 90바이트

```
원문 | WILD YOSHIDA
원문 | "Keep this under your hat...
원문 | There are cards you can
원문 | only get in VS MODE.
원문 | Taka gave me the scoop."
```

```
번역 | 와일드 요시다
번역 | "이건 비밀인데…
번역 | 대전 모드에서만 얻을 수
번역 | 있는 카드가 있어.
번역 | 타카한테 들었지."
```

### `07147C`  122 → 105바이트

```
원문 | BYTE
원문 | "Welcome, stranger.
원문 | This is Plaza Capcom.
원문 | Did you know Plaza...
원문 | means "town square" in Latin?
원문 | Make yourself at home."
```

```
번역 | 바이트
번역 | "어서 오시오, 낯선 이여.
번역 | 여기는 플라자 캡콤.
번역 | 플라자가 라틴어로
번역 | "광장"이란 걸 알았소?
번역 | 편히 계시오."
```

### `071480`  192 → 149바이트

```
원문 | TAKETA
원문 | "You can only use RARITY D
원문 | cards in the slot machine
원문 | next door, you know....
원문 | Get 30 cards with a '777.'
원문 | Hey, you look lucky...
원문 | If all goes well, you can go
원문 | nuts with the Trade Machine!"
```

```
번역 | 타케타
번역 | "옆집 슬롯머신에는
번역 | D등급 카드만 넣을 수 있어….
번역 | "777"이 나오면 30장 받아.
번역 | 어이, 운이 좋아 보이는데…
번역 | 잘하면 교환기에서
번역 | 한몫 챙길 수도 있겠어!"
```

### `071484`  115 → 92바이트

```
원문 | BUNNY
원문 | "NEOGEO World's
원문 | Pao Pao Cafe just opened.
원문 | It's true, you know.
원문 | Richard is just swamped
원문 | getting ready for it."
```

```
번역 | 버니
번역 | "네오지오 월드의
번역 | 파오파오 카페가 막 열렸어.
번역 | 정말이야.
번역 | 리처드가 준비하느라
번역 | 정신이 없대."
```

### `071488`  145 → 113바이트

```
원문 | BUNNY
원문 | "In back of Evil Manor...
원문 | Some people have cards
원문 | that no one's seen before.
원문 | They'd make a really powerful
원문 | deck!
원문 | Go there and check it out!"
```

```
번역 | 버니
번역 | "악의 저택 뒤쪽에…
번역 | 아무도 못 본 카드를
번역 | 가진 사람들이 있대.
번역 | 엄청 센 덱을 만들 수 있을 거야!
번역 | 가서 확인해 봐!"
```

### `07148C`  35 → 34바이트

```
원문 | BUNNY
원문 | "Come in, {08}.
원문 | Enjoy yourself."
```

```
번역 | 버니
번역 | "어서 와, {08}.
번역 | 즐겁게 놀다 가."
```

### `071490`  88 → 54바이트

```
원문 | BUNNY
원문 | "Come to join the tournament?
원문 | If you can win, you'll
원문 | get some rare cards, I hear."
```

```
번역 | 버니
번역 | "대회에 나가려고?
번역 | 이기면 희귀 카드를
번역 | 받는다던데."
```

### `071494`  137 → 122바이트

```
원문 | BUNNY
원문 | "I just saw Mask!
원문 | Right here in the lobby!
원문 | I almost fainted!
원문 | But when I called to him,
원문 | he just took off?...
원문 | Do you think he's shy?"
```

```
번역 | 버니
번역 | "방금 마스크를 봤어!
번역 | 바로 여기 로비에서!
번역 | 기절할 뻔했지 뭐야!
번역 | 근데 불렀더니
번역 | 그냥 가 버리더라고?…
번역 | 수줍음이 많은 걸까?"
```

### `071498`  114 → 93바이트

```
원문 | BUNNY
원문 | "That was a great game!
원문 | You were good, {08}.
원문 | But Cap was awesome!
원문 | That nihilistic manner!
원문 | He's just so dreamy!"
```

```
번역 | 버니
번역 | "멋진 승부였어!
번역 | 너도 잘했어, {08}.
번역 | 근데 캡이 정말 대단했어!
번역 | 그 냉소적인 태도!
번역 | 너무 멋있어!"
```

### `07149C`  114 → 93바이트

```
원문 | BUNNY
원문 | "That was a great game!
원문 | You were good, {08}.
원문 | But Cap was awesome!
원문 | That nihilistic manner!
원문 | He's just so dreamy!"
```

```
번역 | 버니
번역 | "멋진 승부였어!
번역 | 너도 잘했어, {08}.
번역 | 근데 캡이 정말 대단했어!
번역 | 그 냉소적인 태도!
번역 | 너무 멋있어!"
```

### `0714BC`  113 → 86바이트

```
원문 | BUNNY
원문 | "That was a great game.
원문 | You were good, {08}.
원문 | But Shin was awesome.
원문 | Such burning passion!
원문 | He's just so dreamy!"
```

```
번역 | 버니
번역 | "멋진 승부였어.
번역 | 너도 잘했어, {08}.
번역 | 근데 신이 대단했어.
번역 | 그 불타는 열정!
번역 | 너무 멋있어!"
```

### `0714C0`  113 → 86바이트

```
원문 | BUNNY
원문 | "That was a great game.
원문 | You were good, {08}.
원문 | But Shin was awesome.
원문 | Such burning passion!
원문 | He's just so dreamy!"
```

```
번역 | 버니
번역 | "멋진 승부였어.
번역 | 너도 잘했어, {08}.
번역 | 근데 신이 대단했어.
번역 | 그 불타는 열정!
번역 | 너무 멋있어!"
```

### `0714D4`  85 → 66바이트

```
원문 | AHM
원문 | "Hi, {08}.
원문 | You should drop by
원문 | my place once in a while.
원문 | I might have some new info!"
```

```
번역 | 아무
번역 | "안녕, {08}.
번역 | 가끔 우리 가게에
번역 | 들러 줘.
번역 | 새 정보가 있을지도 몰라!"
```

### `0714D8`  98 → 103바이트  (빈 곳으로 옮겨 담음)

```
원문 | GIRL
원문 | "Oh, bummer...
원문 | I thought they were testing
원문 | a new game here. Oh well.
원문 | I'll try the NEO Print."
```

```
번역 | 여자아이
번역 | "아, 아쉽다…
번역 | 여기서 새 게임을 시험하는 줄
번역 | 알았는데. 뭐 어쩔 수 없지.
번역 | 네오 프린트나 해야겠다."
```

### `0714DC`  52 → 42바이트

```
원문 | "Huh?
원문 | You already have it?...
원문 | Just like a champion!"
```

```
번역 | "어?
번역 | 벌써 갖고 있다고?…
번역 | 역시 챔피언답네!"
```

### `0714E0`  143 → 123바이트

```
원문 | NISHI
원문 | "Why its {08}.
원문 | How's it going?"
원문 | 
원문 | YOSIKI
원문 | "Are you joining the tournament?
원문 | If you beat 4 players,
원문 | you can win a rare card!"
원문 | JOIN TOURNAMENT?
원문 | {0D}
```

```
번역 | 니시
번역 | "어이, {08} 아니오.
번역 | 잘 지내시오?"
번역 | 
번역 | 요시키
번역 | "대회에 나갈 거야?
번역 | 네 명을 이기면
번역 | 희귀 카드를 받을 수 있어!"
번역 | 대회에 나갈까요?
번역 | {0D}
```

### `0714E4`  119 → 95바이트

```
원문 | BUNNY
원문 | "You did it, huh?!
원문 | You beat 20 players!
원문 | You're great!
원문 | If you can beat
원문 | Mask like that,
원문 | you might get a rare card!"
```

```
번역 | 버니
번역 | "해냈구나?!
번역 | 스무 명을 이겼어!
번역 | 대단해!
번역 | 그렇게 마스크까지 이기면
번역 | 희귀 카드를 받을지도 몰라!"
```

### `0714E8`  49 → 38바이트

```
원문 | BUNNY
원문 | "You're joining the tournament?
원문 | Good luck!"
```

```
번역 | 버니
번역 | "대회에 나가는구나?
번역 | 행운을 빌게!"
```

### `0714EC`  60 → 60바이트

```
원문 | DOORMAN
원문 | "Welcome to SC Hotel, sir.
원문 | Have a comfortable stay."
```

```
번역 | 도어맨
번역 | "SC 호텔에 오신 것을 환영합니다.
번역 | 편히 쉬다 가십시오."
```

### `0715E0`  188 → 143바이트

```
원문 | KID
원문 | "...Here are the rules...
원문 | Hey! {08}!
원문 | Are you listening?
원문 | I'm trying to teach you,
원문 | and you're spacing out! What gall!
원문 | Do you want to hear the
원문 | rules for CARD CLASH again?"
원문 | SEE RULES AGAIN?
원문 | {0D}
```

```
번역 | 키드
번역 | "…규칙은 이런 거야…
번역 | 야! {08}!
번역 | 듣고 있어?
번역 | 가르쳐 주는데
번역 | 딴생각이나 하고! 어이가 없네!
번역 | 카드 클래시 규칙을
번역 | 다시 들을래?"
번역 | 규칙을 다시 볼까요?
번역 | {0D}
```

### `0715E4`  279 → 215바이트

```
원문 | KID
원문 | "That's my disciple.
원문 | You got talent!
원문 | You should enter the SC CARD
원문 | CLASH!
원문 | I'm sure you'll go to the top!
원문 | Strike while the iron's hot!
원문 | Take on other players and gather
원문 | SC coins!
원문 | Win 5 coins and you can
원문 | enter the Tokyo Championship!
원문 | If you forget the rules,
원문 | look at NOTES below.
```

```
번역 | 키드
번역 | "역시 내 제자야.
번역 | 재능이 있어!
번역 | SC 카드 클래시에 나가 봐!
번역 | 분명 정상까지 갈 거야!
번역 | 쇠뿔도 단김에 빼랬다!
번역 | 다른 사람들과 겨뤄
번역 | SC 코인을 모아!
번역 | 코인 5개를 모으면
번역 | 도쿄 대회에 나갈 수 있어!
번역 | 규칙을 잊으면
번역 | 아래 안내를 봐."
```

### `0715E8`  106 → 67바이트

```
원문 | AHM
원문 | "Oh, hey there!
원문 | I was just looking at all 
원문 | 
원문 | the stuff on this bulletin board.
원문 | It's really interesting!
```

```
번역 | 아무
번역 | "어, 안녕!
번역 | 이 게시판에 붙은 걸
번역 | 
번역 | 구경하고 있었어.
번역 | 꽤 재미있네!"
```

### `0715EC`  124 → 77바이트

```
원문 | AHM
원문 | "Congratulations on your win!
원문 | I've been hearing a lot
원문 | about, {08}.
원문 | Let me in on your CARD CLASH
원문 | secrets sometime soon, huh?
```

```
번역 | 아무
번역 | "우승 축하해!
번역 | {08} 얘기 많이 들었어.
번역 | 언제 카드 클래시 비법 좀
번역 | 알려 줘, 응?"
```

### `0715F0`  84 → 69바이트

```
원문 | GIRL
원문 | "This dog's cute, but...
원문 | I'm afraid to touch it...
원문 | It might bark, you know...."
```

```
번역 | 여자아이
번역 | "이 개 귀엽긴 한데…
번역 | 만지기가 무서워…
번역 | 짖을지도 모르잖아…."
```

### `0715F4`  102 → 101바이트

```
원문 | GIRL
원문 | "I can pet this dog now!
원문 | I wish I could take it home...
원문 | I'll call it 'Poppy,' or maybe
원문 | 'Rush'..."
```

```
번역 | 여자아이
번역 | "이제 이 개를 쓰다듬을 수 있어!
번역 | 집에 데려가고 싶다…
번역 | "포피"라고 부를까,
번역 | 아니면 "러시"라고…"
```

### `0715F8`  16 → 10바이트

```
원문 | DOG
원문 | "Woof woof!"
```

```
번역 | 개
번역 | "멍멍!"
```

### `0715FC`  20 → 14바이트

```
원문 | DOG
원문 | "Yelp...yelp..."
```

```
번역 | 개
번역 | "낑… 낑…"
```

### `071600`  162 → 128바이트

```
원문 | WILD YOSHIDA
원문 | "Hey, you play CARD CLASH, too?
원문 | Watch it when you
원문 | go up against Taka.
원문 | If he starts to lose,
원문 | he'll flip the table over!
원문 | TAKA
원문 | "You pinhead! You stink!"
```

```
번역 | 와일드 요시다
번역 | "어이, 너도 카드 클래시 해?
번역 | 타카랑 붙을 땐 조심해.
번역 | 지기 시작하면
번역 | 판을 엎어 버리거든!"
번역 | 타카
번역 | "이 멍청아! 재수 없어!"
```

### `071604`  92 → 92바이트

```
원문 | WILD YOSHIDA
원문 | "You beat Taka! Whoa!
원문 | It's not his card ability,
원문 | I can't stand his attitude..."
```

```
번역 | 와일드 요시다
번역 | "타카를 이겼구나! 우와!
번역 | 카드 실력이 문제가 아니라,
번역 | 그 태도를 참을 수가 없어…"
```

### `071608`  226 → 131바이트

```
원문 | SHIGGY
원문 | "Have you heard?
원문 | There's an ability that can
원문 | change cards to different ones...
원문 | If your card is changed, it stays
원문 | changed until the match is over.
원문 | Even if you put it back in your
원문 | hand,
원문 | it stays the same. Watch
원문 | yourself!"
```

```
번역 | 시기
번역 | "들었어?
번역 | 카드를 다른 카드로
번역 | 바꾸는 능력이 있대…
번역 | 한번 바뀌면 승부가 끝날 때까지
번역 | 그대로래.
번역 | 손패로 돌려도
번역 | 그대로라니까. 조심해!"
```

### `07160C`  82 → 53바이트

```
원문 | SHIGGY
원문 | "Have you heard?
원문 | There are cards you can only
원문 | find in the Trading Machines.
```

```
번역 | 시기
번역 | "들었어?
번역 | 교환기에서만 얻을 수 있는
번역 | 카드가 있대."
```

### `071674`  172 → 149바이트

```
원문 | KID
원문 | "Ooh. Good play!
원문 | Just like you, {08}
원문 | That's my disciple.
원문 | I've taught you all I know.
원문 | But just in case,
원문 | do you want me to explain
원문 | CARD CLASH rules again?
원문 | SEE RULES AGAIN?
원문 | {0D}
```

```
번역 | 키드
번역 | "오. 잘하는데!
번역 | 역시 너답다, {08}
번역 | 내 제자야.
번역 | 아는 건 다 가르쳐 줬어.
번역 | 그래도 혹시 모르니,
번역 | 카드 클래시 규칙을
번역 | 다시 설명해 줄까?"
번역 | 규칙을 다시 볼까요?
번역 | {0D}
```

### `071678`  260 → 198바이트

```
원문 | KID
원문 | "Oh, so close...
원문 | But it's no time to mope!
원문 | You must enter the CARD CLASH!
원문 | Strike while the iron's hot and 
원문 | take on other players to get SC
원문 | coins.
원문 | When you've gathered 5 coins,
원문 | hurry on to the Tokyo Tournament!
원문 | If you forget the rules,
원문 | look at NOTES below."
```

```
번역 | 키드
번역 | "아, 아까웠어…
번역 | 하지만 낙담할 때가 아냐!
번역 | 카드 클래시에 나가야지!
번역 | 쇠뿔도 단김에 빼랬다고,
번역 | 다른 사람들과 겨뤄 SC 코인을
번역 | 모아.
번역 | 코인 5개를 모으면
번역 | 어서 도쿄 대회로 가!
번역 | 규칙을 잊으면
번역 | 아래 안내를 봐."
```

### `071680`  169 → 135바이트

```
원문 | FO
원문 | "Oh! {08}!
원문 | You listen good to 
원문 | my CARD CLASH rules.
원문 | I made this notebook,
원문 | and memorized them all!
원문 | If you forget the rules,
원문 | I can take a look at this."
원문 | SEE RULES AGAIN?
원문 | {0D}
```

```
번역 | 포
번역 | "오! {08}!
번역 | 내 카드 클래시 규칙 설명을
번역 | 잘 들었구먼.
번역 | 이 공책을 만들어서
번역 | 다 외웠다오!
번역 | 규칙을 잊으면
번역 | 이걸 보면 되오."
번역 | 규칙을 다시 볼까요?
번역 | {0D}
```

### `071684`  339 → 253바이트

```
원문 | FO
원문 | "That kid's interesting, huh?
원문 | But that's another story...
원문 | Sorry you get me off track...
원문 | That's just like you, {08}
원문 | If you play like that...
원문 | I'll win this year's
원문 | CARD CLASH Tournament for sure!
원문 | Let's get playing,
원문 | and find some coins!
원문 | If we can get 5 SC Coins,
원문 | We go to the Tokyo Tournament!
원문 | ...Did you know that?
원문 | Ah ha ha! Someone's upset!"
```

```
번역 | 포
번역 | "그 꼬마 재미있지 않소?
번역 | 그건 그렇고…
번역 | 미안하오, 얘기가 샜구먼…
번역 | 역시 자네답소, {08}
번역 | 그렇게만 하면…
번역 | 올해 카드 클래시 대회는
번역 | 내가 꼭 이기겠소!
번역 | 어서 겨뤄서
번역 | 코인을 모읍시다!
번역 | SC 코인 5개를 모으면
번역 | 도쿄 대회로 가는 거요!
번역 | …알고 있었소?
번역 | 하하하! 누가 삐쳤구먼!"
```

### `071688`  110 → 100바이트

```
원문 | BYTE
원문 | "Welcome to my abode!
원문 | The toy shop, "Lost World"!
원문 | Just in time. It's sale time!
원문 | First come, first serve!"
```

```
번역 | 바이트
번역 | "내 가게에 온 걸 환영하오!
번역 | 장난감 가게 "로스트 월드"!
번역 | 마침 잘 왔소. 세일 중이오!
번역 | 선착순이오!"
```

### `07168C`  259 → 194바이트

```
원문 | AKIMAN
원문 | "I'll teach you some battle hints!
원문 | Once in a while, you should give
원문 | up some HP by not
원문 | counterattacking.
원문 | Saving your strong characters
원문 | for counterattacks! It's awesome!
원문 | But be careful! Do it too often,
원문 | and you might get KO'ed.
원문 | Shoot for the stars, kid!"
```

```
번역 | 아키만
번역 | "승부 요령을 알려 주지!
번역 | 가끔은 되받지 않고
번역 | HP를 좀 내주는 것도 좋아.
번역 | 센 캐릭터를 되받기용으로
번역 | 아껴 두는 거지! 끝내주지!
번역 | 하지만 조심해! 너무 자주 하면
번역 | 쓰러질 수도 있어.
번역 | 크게 노려라, 꼬마!"
```

### `071690`  199 → 141바이트

```
원문 | AKIMAN
원문 | "Nice win!
원문 | Huh? You reached your
원문 | goal and lost your hunger?
원문 | Whatcha talkin' about?
원문 | You gotta keep fighting...
원문 | You still have the fun from
원문 | collecting all these cards!
원문 | Shoot for the stars, kid!"
```

```
번역 | 아키만
번역 | "잘 이겼다!
번역 | 어? 목표를 이뤄서
번역 | 의욕이 사라졌다고?
번역 | 무슨 소리야?
번역 | 계속 싸워야지…
번역 | 카드를 다 모으는
번역 | 재미가 남아 있잖아!
번역 | 크게 노려라, 꼬마!"
```

### `071694`  344 → 281바이트

```
원문 | FO
원문 | "Ah hya! That kid's a scream!
원문 | But that's another story...
원문 | I should drive on the track...
원문 | I can't believe you lost,
원문 | {08}. Unthinkable!
원문 | But you cheer sideways!
원문 | There's always the CARD CLASH!
원문 | Get back and take on players
원문 | to find some SC coins!
원문 | Win 5 coins, and you're
원문 | off to the Tokyo Tournament!
원문 | ...What? You knew that?
원문 | Ah hah! Someone's peeved!"
```

```
번역 | 포
번역 | "아하! 그 꼬마 웃기지 않소!
번역 | 그건 그렇고…
번역 | 나도 제 갈 길을 가야 하는데…
번역 | 자네가 지다니, {08}.
번역 | 믿을 수가 없구먼!
번역 | 하지만 기운 내시오!
번역 | 카드 클래시는 계속되오!
번역 | 돌아가서 사람들과 겨뤄
번역 | SC 코인을 모으시오!
번역 | 코인 5개를 모으면
번역 | 도쿄 대회로 가는 거요!
번역 | …뭐요? 알고 있었소?
번역 | 하하! 누가 삐쳤구먼!"
```

### `071698`  86 → 79바이트

```
원문 | BOY
원문 | "Whoa! Huge isn't it!
원문 | This thing is it...
원문 | the Dust Dragon!
원문 | Just push this switch!"
```

```
번역 | 남자아이
번역 | "우와! 엄청 크지!
번역 | 이게 바로…
번역 | 더스트 드래곤이야!
번역 | 이 스위치를 눌러 봐!"
```

### `07169C`  88 → 74바이트

```
원문 | BOY
원문 | "Wah ha! Scared you, huh?
원문 | Scared me at first, too!
원문 | Everyone leaks a little at this!"
```

```
번역 | 남자아이
번역 | "와하! 놀랐지?
번역 | 나도 처음엔 놀랐어!
번역 | 다들 이거 보면 좀 지린다니까!"
```

### `0716A0`  125 → 119바이트

```
원문 | MAN
원문 | "Oh yeah. What a bargain!
원문 | I got a RARITY A card!
원문 | This is my lucky day!
원문 | Trade Machines are great!
원문 | Give it a whirl, kiddo!"
```

```
번역 | 아저씨
번역 | "오 좋았어. 완전 횡재네!
번역 | A등급 카드가 나왔어!
번역 | 오늘 운이 좋은 날이야!
번역 | 교환기 정말 좋아!
번역 | 너도 한번 돌려 봐, 꼬마!"
```

### `0716A4`  75 → 71바이트

```
원문 | MAN
원문 | "Hmmm...
원문 | This is the same card
원문 | I put in there...
원문 | Oh well, that's life."
```

```
번역 | 아저씨
번역 | "흠…
번역 | 내가 넣은 거랑
번역 | 똑같은 카드가 나왔네…
번역 | 뭐, 사는 게 그렇지."
```

### `0716A8`  172 → 151바이트

```
원문 | BOY
원문 | "Hey, know about SP?
원문 | Play a CHA card,
원문 | and SP will increase.
원문 | But sometimes it goes
원문 | to zero with certain CHA cards.
원문 | SP decreases when you use
원문 | AC cards and Unite Attacks!"
```

```
번역 | 남자아이
번역 | "어이, SP 알아?
번역 | 캐릭터 카드를 내면
번역 | SP가 올라가.
번역 | 근데 어떤 캐릭터 카드는
번역 | 0으로 만들어 버리기도 해.
번역 | 액션 카드나 합체 공격을 쓰면
번역 | SP가 줄어들어!"
```

### `0716AC`  167 → 131바이트

```
원문 | TEEN
원문 | "Remember the rules?
원문 | If you have any questions,
원문 | check the 'JOY JOY BOARD.'
원문 | If you know a few of its secrets,
원문 | it may help you in games...
원문 | And I mean, it may help."
```

```
번역 | 청소년
번역 | "규칙 기억나?
번역 | 궁금한 게 있으면
번역 | "조이조이 게시판"을 봐.
번역 | 거기 비밀을 몇 개 알면
번역 | 승부에 도움이 될지도…
번역 | 어디까지나 "될지도"야."
```

### `0716B0`  50 → 54바이트  (빈 곳으로 옮겨 담음)

```
원문 | BYTE
원문 | "You can't come in here!
원문 | This is staff only!"
```

```
번역 | 바이트
번역 | "여긴 들어오면 안 되오!
번역 | 관계자 외 출입 금지요!"
```

### `0716B4`  109 → 93바이트

```
원문 | GIRL
원문 | "This figure's cool!
원문 | Oh yeah, have you heard?
원문 | 
원문 | You can only put 3 of the
원문 | same card in a deck.
원문 | Watch it!"
```

```
번역 | 여자아이
번역 | "이 피규어 멋지다!
번역 | 아 참, 들었어?
번역 | 
번역 | 같은 카드는 덱에 3장까지만
번역 | 넣을 수 있대.
번역 | 조심해!"
```

### `0716B8`  54 → 38바이트

```
원문 | AN-CHAN
원문 | "Sylphy is such a babe!
원문 | Don't you think so?"
원문 | {0D}
```

```
번역 | 형
번역 | "실피 정말 예쁘지 않냐?
번역 | 안 그래?"
번역 | {0D}
```

### `0716BC`  37 → 32바이트

```
원문 | AN-CHAN
원문 | "Yeah, yeah. Isn't she? Huh?"
```

```
번역 | 형
번역 | "그렇지, 그렇지. 예쁘지? 응?"
```

### `0716C0`  30 → 21바이트

```
원문 | AN-CHAN
원문 | "Hmph. Still a child!"
```

```
번역 | 형
번역 | "흥. 아직 애구먼!"
```

### `0716C4`  83 → 71바이트

```
원문 | GEEZER
원문 | "Whew!...
원문 | Watching this warehouse is rough.
원문 | It's getting tight here, too..."
```

```
번역 | 영감
번역 | "휴우…
번역 | 이 창고 지키는 것도 고된 일이야.
번역 | 여기도 점점 비좁아지고…"
```

### `0716C8`  76 → 57바이트

```
원문 | GEEZER
원문 | "This is shot!
원문 | This can be recycled.
원문 | When will they pick this up?..."
```

```
번역 | 영감
번역 | "이건 못 쓰겠군!
번역 | 재활용은 되겠어.
번역 | 언제 가져가려나…"
```

### `0716CC`  154 → 121바이트

```
원문 | MR. EDA
원문 | "I lost to Akiman!...
원문 | And now I gotta clean
원문 | this stuff up!
원문 | Geez, this Trading Machine's
원문 | busted and can't be used.
원문 | Glad I didn't put a card in it!"
```

```
번역 | 에다 씨
번역 | "아키만한테 졌어!…
번역 | 그래서 지금 이걸
번역 | 치우고 있는 거라고!
번역 | 어휴, 이 교환기는
번역 | 고장 나서 못 써.
번역 | 카드 안 넣길 잘했지!"
```

### `0716D0`  131 → 98바이트

```
원문 | MR. EDA
원문 | "Hey hey hey!
원문 | How 'bout that a card out of
원문 | the broken Trading Machine.
원문 | Ah, I want to finish this
원문 | and go back to playing..."
```

```
번역 | 에다 씨
번역 | "어이 어이 어이!
번역 | 고장 난 교환기에서
번역 | 카드가 나왔잖아.
번역 | 아, 얼른 끝내고
번역 | 게임하러 가고 싶다…"
```

### `0716D8`  22 → 25바이트  (빈 곳으로 옮겨 담음)

```
원문 | DUST DRAGON
원문 | "Ugyaaah!"
```

```
번역 | 더스트 드래곤
번역 | "우갸아아!"
```

### `0716EC`  101 → 81바이트

```
원문 | BOY
원문 | "Ouch....
원문 | What the heck was that?
원문 | Huh? {08}. Oh wow!
원문 | Are you going to be in
원문 | this year's CARD CLASH?"
```

```
번역 | 남자아이
번역 | "아야….
번역 | 방금 그거 뭐였지?
번역 | 어? {08}. 우와!
번역 | 올해 카드 클래시에
번역 | 나가는 거야?"
```

### `0716F0`  140 → 115바이트

```
원문 | MAN
원문 | "Hey, there's a Trading Machine!
원문 | I can trade in cards I don't need!
원문 | 
원문 | But I don't know what'll come out
원문 | until I put some cards in there."
```

```
번역 | 아저씨
번역 | "어이, 교환기가 있네!
번역 | 필요 없는 카드를 바꿀 수 있어!
번역 | 
번역 | 근데 카드를 넣어 보기 전엔
번역 | 뭐가 나올지 모른단 말이지."
```

### `0716F4`  82 → 54바이트

```
원문 | SHIGGY
원문 | "Did you hear?
원문 | The cards in crane games are
원문 | changed quite often, you know."
```

```
번역 | 시기
번역 | "들었어?
번역 | 크레인 게임에 든 카드는
번역 | 꽤 자주 바뀐대."
```

### `0716F8`  93 → 92바이트

```
원문 | BYTE
원문 | "Hey, welcome.
원문 | We're holding the
원문 | 'NEO Choopy Fighters
원문 | Tournament' now
원문 | Just go upstairs!"
```

```
번역 | 바이트
번역 | "어이, 어서 오시오.
번역 | 지금 "네오 츄피 파이터즈
번역 | 대회"를 열고 있소.
번역 | 위층으로 올라가시오!"
```

### `0716FC`  76 → 71바이트

```
원문 | BARTENDER
원문 | "H, hey. Welcome!
원문 | ...Sorry. I'm new here.
원문 | I'm kind of nervous...."
```

```
번역 | 바텐더
번역 | "어, 어서 오세요!
번역 | …죄송합니다. 여기 처음이라.
번역 | 좀 긴장돼서요…."
```

### `071700`  216 → 183바이트

```
원문 | MIRAGE
원문 | "Hello there.
원문 | Know how to make
원문 | a really kick-butt deck?
원문 | You gotta balance your
원문 | CHA and AC cards.
원문 | And you gotta time 'BACK-UP'
원문 | and 'UNITE ATTACK' just right
원문 | And after that...you should
원문 | use characters you like."
```

```
번역 | 미라주
번역 | "안녕하세요.
번역 | 제대로 센 덱을 짜는 법
번역 | 아세요?
번역 | 캐릭터 카드와 액션 카드의
번역 | 균형을 맞춰야 해요.
번역 | 그리고 "백업"과
번역 | "합체 공격" 때를 잘 잡아야죠.
번역 | 그다음엔… 좋아하는
번역 | 캐릭터를 쓰면 돼요."
```

### `071704`  80 → 69바이트

```
원문 | MIRAGE
원문 | "Congratulations! Nice win!
원문 | How about trying a different
원문 | deck next game?"
```

```
번역 | 미라주
번역 | "축하해요! 잘 이겼어요!
번역 | 다음엔 다른 덱으로
번역 | 해 보는 건 어때요?"
```

### `071708`  260 → 229바이트

```
원문 | SHIROI
원문 | "Greetings. I'm Eiji Shiroi.
원문 | I'm working on a
원문 | new design here....
원문 | Boy, my shoulder's are stiff...
원문 | Hey, did you know this?
원문 | There are Trading Machines
원문 | in Lost World and SC Park.
원문 | The cards you can get
원문 | each have different rarities!
원문 | You should check it out!"
```

```
번역 | 시로이
번역 | "안녕하세요. 시로이 에이지입니다.
번역 | 여기서 새 디자인을
번역 | 작업하고 있어요….
번역 | 아이고, 어깨가 뻐근하네…
번역 | 어, 이건 알고 계셨나요?
번역 | 로스트 월드와 SC 파크에
번역 | 교환기가 있어요.
번역 | 거기서 얻는 카드는
번역 | 등급이 다 다릅니다!
번역 | 한번 확인해 보세요!"
```

### `07170C`  129 → 109바이트

```
원문 | GIRL
원문 | "Oh, shucks!
원문 | I thought they were testing
원문 | a new video game here!
원문 | I guess I'll just watch the
원문 | Neo Choopy Fighters
원문 | Tournament."
```

```
번역 | 여자아이
번역 | "아, 아쉽다!
번역 | 여기서 새 비디오 게임을
번역 | 시험하는 줄 알았는데!
번역 | 그냥 네오 츄피 파이터즈
번역 | 대회나 봐야겠다."
```

### `071710`  114 → 89바이트

```
원문 | CHOOPY LULU
원문 | "Congratulations on getting a
원문 | coin.
원문 | Look at the NOTES on the right.
원문 | You might find some awesome
원문 | info!"
```

```
번역 | 츄피 룰루
번역 | "코인을 얻은 걸 축하해요.
번역 | 오른쪽 안내를 보세요.
번역 | 멋진 정보를 찾을지도
번역 | 모릅니다!"
```

### `071714`  35 → 29바이트

```
원문 | NAKA
원문 | "Hey!
원문 | Care for a KOF match?"
원문 | {0D}
```

```
번역 | 나카
번역 | "어이!
번역 | KOF 한판 어때?"
번역 | {0D}
```

### `071718`  71 → 54바이트

```
원문 | NAKA
원문 | "I'm on the Psycho Soldier team!
원문 | Hoo hoo hoo. Bring it on,
원문 | woman!"
```

```
번역 | 나카
번역 | "난 사이코 솔저 팀이야!
번역 | 후후후. 덤벼 봐,
번역 | 아가씨!"
```

### `07171C`  362 → 239바이트

```
원문 | @
원문 | 
원문 | @@
원문 | 
원문 | @@@
원문 | 
원문 | NAKA
원문 | "Geez! I lost!
원문 | Guess I haven't had
원문 | enough training.
원문 | ...C'est la guerre.
원문 | I'll let you in on something.
원문 | There's a '?' in the character
원문 | column of the 'Back-Up List',
원문 | right?
원문 | If it's an SNK character,
원문 | a CAPCOM character will do
원문 | Back-Up.
원문 | If it's a CAPCOM character,
원문 | an SNK character does Back-Up.
원문 | I bet there are some real
원문 | strange combinations there!"
```

```
번역 | @
번역 | 
번역 | @@
번역 | 
번역 | @@@
번역 | 
번역 | 나카
번역 | "이런! 졌잖아!
번역 | 아직 수련이 부족했나 봐.
번역 | …어쩔 수 없지.
번역 | 하나 알려 줄게.
번역 | "백업 목록"의 캐릭터 칸에
번역 | "?"가 있지?
번역 | SNK 캐릭터라면
번역 | 캡콤 캐릭터가 백업을 해.
번역 | 캡콤 캐릭터라면
번역 | SNK 캐릭터가 백업을 하지.
번역 | 분명 희한한 조합도
번역 | 있을 거야!"
```

### `071720`  82 → 71바이트

```
원문 | @
원문 | 
원문 | @@
원문 | 
원문 | @@@
원문 | 
원문 | NAKA
원문 | "Wah ha ha! I won!
원문 | Don't be a pouty-pants!
원문 | Butch up, little boy!"
```

```
번역 | @
번역 | 
번역 | @@
번역 | 
번역 | @@@
번역 | 
번역 | 나카
번역 | "와하하! 내가 이겼다!
번역 | 삐치지 마!
번역 | 사내답게 굴어, 꼬마!"
```

### `071724`  52 → 39바이트

```
원문 | NAKA
원문 | "What? Well, tough beans
원문 | if you don't like it!"
```

```
번역 | 나카
번역 | "뭐? 마음에 안 들면
번역 | 어쩔 수 없지!"
```

### `071728`  207 → 162바이트

```
원문 | MASQUERADER
원문 | "I'm a fan of Ikoma!
원문 | I'm trying to collect
원문 | all of her cards I can...
원문 | But if I get a 'KING' card,
원문 | I'll have a complete set.
원문 | Do you have a 'KING' card?
원문 | If you do, let's trade."
원문 | TRADE "KING" CARD?
원문 | {0D}
```

```
번역 | 가면 쓴 사람
번역 | "난 이코마 팬이야!
번역 | 그녀의 카드를 되는 대로
번역 | 모으고 있는데…
번역 | "킹" 카드만 있으면
번역 | 한 벌이 완성돼.
번역 | "킹" 카드 있어?
번역 | 있으면 바꾸자."
번역 | "킹" 카드를 바꿀까요?
번역 | {0D}
```

### `07172C`  96 → 71바이트

```
원문 | MASQUERADER
원문 | "All right! Thank you!
원문 | Here...Take this 'ROULETTE' card!
원문 | Take good care of it, huh?"
```

```
번역 | 가면 쓴 사람
번역 | "좋았어! 고마워!
번역 | 자… 이 "룰렛" 카드 받아!
번역 | 잘 간직해, 응?"
```

### `071730`  94 → 77바이트

```
원문 | MASQUERADER
원문 | "All right...Hey!?
원문 | You don't have a 'KING' card!
원문 | You big liar! You shouldn't lie!"
```

```
번역 | 가면 쓴 사람
번역 | "좋아… 어라!?
번역 | "킹" 카드가 없잖아!
번역 | 거짓말쟁이! 거짓말하면 못써!"
```

### `071734`  83 → 55바이트

```
원문 | MASQUERADER
원문 | "Oh, that's too bad...
원문 | Well, if you feel like trading,
원문 | give me a call."
```

```
번역 | 가면 쓴 사람
번역 | "아, 아쉽네…
번역 | 바꿀 마음이 생기면
번역 | 불러 줘."
```

### `071738`  100 → 84바이트

```
원문 | MASQUERADER
원문 | "Thanks for trading with me.
원문 | You really helped me out!
원문 | If you get other cards, call me."
```

```
번역 | 가면 쓴 사람
번역 | "바꿔 줘서 고마워.
번역 | 정말 큰 도움이 됐어!
번역 | 다른 카드가 생기면 또 불러 줘."
```

### `07175C`  66 → 46바이트

```
원문 | CHOOPY GROUPIE
원문 | "C'mon, let's play!"
원문 | PLAY AGAINST CHOOPY GROUPIE?
원문 | {0D}
```

```
번역 | 츄피 팬
번역 | "자, 한판 하자!"
번역 | 츄피 팬과 겨룰까요?
번역 | {0D}
```

### `071760`  81 → 69바이트

```
원문 | CHOOPY GROUPIE
원문 | "OK. Question 1.
원문 | ...Huh? This isn't a quiz?
원문 | Huh? Hey, where am I?"
```

```
번역 | 츄피 팬
번역 | "좋아. 1번 문제.
번역 | …어? 퀴즈가 아니었어?
번역 | 어라? 여기가 어디지?"
```

### `071764`  72 → 47바이트

```
원문 | CHOOPY GROUPIE
원문 | "Afraid of losing?
원문 | I can dig that.
원문 | I'm one tough player!"
```

```
번역 | 츄피 팬
번역 | "질까 봐 겁나?
번역 | 이해해.
번역 | 내가 좀 세거든!"
```

### `071768`  140 → 98바이트

```
원문 | CHOOPY GROUPIE
원문 | "Have you heard? Have you?
원문 | The next KOF game...
원문 | It's full polygon and has 60
원문 | characters!
원문 | ...Do you think...the rumor's
원문 | true?"
```

```
번역 | 츄피 팬
번역 | "들었어? 들었어?
번역 | 다음 KOF 말이야…
번역 | 완전 폴리곤에 캐릭터가
번역 | 60명이래!
번역 | …그 소문… 진짜일까?"
```

### `07176C`  147 → 109바이트

```
원문 | CHOOPY GROUPIE
원문 | "I'm a big fan of Terry.
원문 | As a matter of fact, I just
원문 | got a 'TERRY' card recently.
원문 | Boy, RARITY B cards...
원문 | they sure don't come easy!"
```

```
번역 | 츄피 팬
번역 | "난 테리 완전 팬이야.
번역 | 실은 얼마 전에
번역 | "테리" 카드를 얻었어.
번역 | 야, B등급 카드는…
번역 | 정말 쉽게 안 나오더라!"
```

### `071770`  111 → 84바이트

```
원문 | CHOOPY GROUPIE
원문 | "Oh my God! It's Nonaka!
원문 | Yah! Yah!
원문 | Your the voice of Kyo
원문 | in KOF, aren't you?
원문 | Oh no! Whoo! Whoo!"
```

```
번역 | 츄피 팬
번역 | "세상에! 노나카다!
번역 | 꺄! 꺄!
번역 | KOF에서 쿄 목소리
번역 | 맡으신 분이죠?
번역 | 어떡해! 꺄! 꺄!"
```

### `071774`  89 → 57바이트

```
원문 | CHOOPY GROUPIE
원문 | "My 'Zangy' is really strong!
원문 | He can twirl around
원문 | anybody that I take on!"
```

```
번역 | 츄피 팬
번역 | "내 "장기"는 정말 세!
번역 | 누구든 빙빙 돌려 버린다고!"
```

### `071778`  80 → 70바이트

```
원문 | CHOOPY GROUPIE
원문 | "Whoo hoo! I-KO-MA!
원문 | I'll follow you anywhere,
원문 | Ikoma. I am yours!"
```

```
번역 | 츄피 팬
번역 | "우후! 이-코-마!
번역 | 어디든 따라갈게요,
번역 | 이코마. 저는 당신 거예요!"
```

### `07177C`  217 → 176바이트

```
원문 | CHOOPY GROUPIE
원문 | "Keiko! Whoo hoo!
원문 | I'm over here!
원문 | 
원문 | Have you come to enter the
원문 | Neo Choopy Fighters Tournament?
원문 | Keiko, you say your own lines,
원문 | right?
원문 | And you have 'RIMNEREL' in your
원문 | deck.
원문 | Ikoma uses 'NAKORURU'
원문 | of course!"
```

```
번역 | 츄피 팬
번역 | "케이코! 우후!
번역 | 저 여기 있어요!
번역 | 
번역 | 네오 츄피 파이터즈 대회에
번역 | 나오신 거예요?
번역 | 케이코, 대사 직접 하시죠?
번역 | 그리고 덱에 "림네렐"이
번역 | 들어 있고요.
번역 | 이코마는 물론
번역 | "나코루루"를 쓰죠!"
```

### `071780`  77 → 70바이트

```
원문 | CHOOPY GROUPIE
원문 | "Hey, Keiko!
원문 | Aw man, too many people!
원문 | I can't see her at all!"
```

```
번역 | 츄피 팬
번역 | "어이, 케이코!
번역 | 아 진짜, 사람이 너무 많아!
번역 | 하나도 안 보이잖아!"
```

### `071784`  274 → 181바이트

```
원문 | CHOOPY GROUPIE
원문 | "I heard CARD CLASH has
원문 | both an SNK version...
원문 | and a CAPCOM version, right?
원문 | Cards you can't find in one
원문 | version,
원문 | I hear you can find in the other.
원문 | Cool, huh?!
원문 | Because I got the SNK version...
원문 | 
원문 | I'm going to get my friend to
원문 | buy the CAPCOM version.
원문 | Smart, huh?"
```

```
번역 | 츄피 팬
번역 | "카드 클래시에 SNK판이랑…
번역 | 캡콤판이 따로 있다며?
번역 | 한쪽에 없는 카드를
번역 | 다른 쪽에서 찾을 수 있대.
번역 | 멋지지 않아?!
번역 | 난 SNK판을 샀으니까…
번역 | 
번역 | 친구한테 캡콤판을
번역 | 사게 할 거야.
번역 | 똑똑하지?"
```

### `071788`  151 → 114바이트

```
원문 | CHOOPY GROUPIE
원문 | "Hey, heard about the NEO Laser?
원문 | You can burn your face
원문 | onto a key holder, and stuff.
원문 | I want to do it with Nonaka.
원문 | He's just so dreamy!"
```

```
번역 | 츄피 팬
번역 | "어이, 네오 레이저 들어 봤어?
번역 | 열쇠고리 같은 데
번역 | 얼굴을 새길 수 있대.
번역 | 노나카랑 같이 하고 싶다.
번역 | 너무 멋있어!"
```

### `07178C`  88 → 62바이트

```
원문 | CHOOPY GROUPIE
원문 | "My 'Chanko' is so tough!
원문 | He can blast away anyone.
원문 | Bada-boom boom boom!"
```

```
번역 | 츄피 팬
번역 | "내 "챤코"는 정말 세!
번역 | 누구든 날려 버린다고.
번역 | 펑 펑 펑!"
```

### `071790`  113 → 97바이트

```
원문 | CHOOPY GROUPIE
원문 | "Oooowhooooaaaa!
원문 | You hear this NEO CHOOPY
원문 | 
원문 | Two minutes of Take and Mika.
원문 | It is just unbelievable!"
```

```
번역 | 츄피 팬
번역 | "우우우와아아!
번역 | 이 네오 츄피 들어 봤어?
번역 | 
번역 | 타케랑 미카가 2분 동안 나와.
번역 | 진짜 믿기지가 않아!"
```

### `07179C`  130 → 97바이트

```
원문 | CHOOPY GROUPIE
원문 | "Whoo hoo hoo. You're reckless!
원문 | Card fighters like Ikoma
원문 | are just so tough.
원문 | Amateurs like you
원문 | wouldn't understand!"
```

```
번역 | 츄피 팬
번역 | "우후후. 무모하기는!
번역 | 이코마 같은 카드 파이터는
번역 | 정말 세다고.
번역 | 너 같은 초보는
번역 | 이해 못 할걸!"
```

### `0717A0`  78 → 61바이트

```
원문 | CHOOPY GROUPIE
원문 | "Oooh no!
원문 | Amateur power! Frightful!
원문 | You're no ordinary player."
```

```
번역 | 츄피 팬
번역 | "이럴 수가!
번역 | 초보의 힘! 무섭다!
번역 | 보통 실력이 아니잖아."
```

### `0717A4`  43 → 32바이트

```
원문 | CHOOPY GROUPIE
원문 | "Good luck!
원문 | I'm behind you!"
```

```
번역 | 츄피 팬
번역 | "행운을 빌어!
번역 | 응원할게!"
```

### `0717A8`  53 → 43바이트

```
원문 | CHOOPY GROUPIE
원문 | "NEO Choopy Fighters...
원문 | Join the fun!"
```

```
번역 | 츄피 팬
번역 | "네오 츄피 파이터즈…
번역 | 같이 즐겨요!"
```

### `0717AC`  55 → 46바이트

```
원문 | CHOOPY GROUPIE
원문 | "Ah! The champion!
원문 | Please play with me!"
```

```
번역 | 츄피 팬
번역 | "앗! 챔피언이다!
번역 | 저랑 한판 해 주세요!"
```

### `0717B0`  148 → 143바이트

```
원문 | HARUMI & KEIKO
원문 | "NEO CHOOPY------
원문 | NEO CHOOPY FIGHTERS begins!
원문 | All those who beat us...
원문 | get SC coins!
원문 | Raise your hand to play!"
원문 | JOIN THE TOURNAMENT?
원문 | {0C}
```

```
번역 | 하루미 & 케이코
번역 | "네오 츄피------
번역 | 네오 츄피 파이터즈 시작!
번역 | 우리를 이긴 사람에게…
번역 | SC 코인을 드립니다!
번역 | 하고 싶으면 손 드세요!"
번역 | 대회에 나갈까요?
번역 | {0C}
```

### `0717B4`  158 → 152바이트

```
원문 | HARUMI& KEIKO
원문 | "NEO CHOOPY------
원문 | NEO CHOOPY FIGHTERS begins!
원문 | We're out of coins...
원문 | but all winners get a card!
원문 | Raise your hand to play!"
원문 | JOIN THE TOURNAMENT?
원문 | {0C}
```

```
번역 | 하루미 & 케이코
번역 | "네오 츄피------
번역 | 네오 츄피 파이터즈 시작!
번역 | 코인은 다 떨어졌지만…
번역 | 이긴 사람에게 카드를 드려요!
번역 | 하고 싶으면 손 드세요!"
번역 | 대회에 나갈까요?
번역 | {0C}
```

### `0717B8`  53 → 47바이트

```
원문 | KEIKO
원문 | "Hey, you there!
원문 | HARUMI
원문 | "Good. Come over here."
```

```
번역 | 케이코
번역 | "어이, 거기 너!"
번역 | 하루미
번역 | "좋아. 이리 와."
```

### `0717C0`  157 → 156바이트

```
원문 | BYTE
원문 | "Welcome!
원문 | 'Dark Stalkers '99?'
원문 | No, that's not it...
원문 | 'Zero Fatal Fury'...
원문 | Nah, that's not it...
원문 | ...Anyway, we put a new
원문 | game in here!
원문 | Try it out! Enjoy!"
```

```
번역 | 바이트
번역 | "어서 오시오!
번역 | "다크 스토커즈 99"?
번역 | 아니, 그게 아니고…
번역 | "제로 아랑전설"…
번역 | 아니, 그것도 아니고…
번역 | …아무튼 새 게임을
번역 | 들여놨소!
번역 | 한번 해 보시오! 즐기시오!"
```

### `0717C4`  124 → 117바이트

```
원문 | BARTENDER
원문 | "Welcome back.
원문 | The SC CARD CLASH prelims
원문 | are going on here now.
원문 | It's going on next door.
원문 | You should join the fun!"
```

```
번역 | 바텐더
번역 | "다시 오셨군요.
번역 | SC 카드 클래시 예선이
번역 | 지금 여기서 열리고 있어요.
번역 | 바로 옆에서 하고 있습니다.
번역 | 한번 나가 보세요!"
```

### `0717C8`  106 → 83바이트

```
원문 | KEENU
원문 | "Eh? Got a 'TERRY' card on you?
원문 | If you do, I'll hope you'll
원문 | trade it for a 'CHUN-LI.'"
원문 | TRADE CARD?
원문 | {0D}
```

```
번역 | 키누
번역 | "어? "테리" 카드 있어?
번역 | 있으면 "춘리"랑
번역 | 바꿔 줬으면 하는데."
번역 | 카드를 바꿀까요?
번역 | {0D}
```

### `0717CC`  79 → 74바이트

```
원문 | KEENU
원문 | "What? You'll trade?
원문 | Lucky! Thanks a lot!
원문 | Ask and ye shall receive, huh?"
```

```
번역 | 키누
번역 | "뭐? 바꿔 준다고?
번역 | 운 좋다! 정말 고마워!
번역 | 구하는 자에게 길이 있다더니!"
```

### `0717D0`  59 → 51바이트

```
원문 | KEENU
원문 | "Huh?
원문 | You don't got 'TERRY?'
원문 | Check before you trade!"
```

```
번역 | 키누
번역 | "어?
번역 | "테리"가 없잖아?
번역 | 바꾸기 전에 확인 좀 해!"
```

### `0717D4`  70 → 51바이트

```
원문 | KEENU
원문 | "Sorry to hear that....
원문 | Well, I'll keep looking.
원문 | See you later."
```

```
번역 | 키누
번역 | "아쉽게 됐네….
번역 | 뭐, 계속 찾아봐야지.
번역 | 또 보자."
```

### `0717DC`  199 → 152바이트

```
원문 | KEENU
원문 | "A challenger! Let's play.
원문 | WHAP!
원문 | 
원문 | WHAP! POW!
원문 | 
원문 | WHAP! POW POW!
원문 | 
원문 | WHAP! POW POW POW!
원문 | 
원문 | "Yeeeeek!"
원문 | 
원문 | ({08} WINS)
원문 | 
원문 | KEENU
원문 | "Oooph. I lost...
원문 | Didn't think you'd jump there...
원문 | That was fun. Let's play again!"
```

```
번역 | 키누
번역 | "도전자다! 한판 하자.
번역 | 퍽!
번역 | 
번역 | 퍽! 펑!
번역 | 
번역 | 퍽! 펑 펑!
번역 | 
번역 | 퍽! 펑 펑 펑!
번역 | 
번역 | "으아악!"
번역 | 
번역 | ({08} 승리)
번역 | 
번역 | 키누
번역 | "으윽. 졌네…
번역 | 거기서 뛸 줄은 몰랐어….
번역 | 재밌었어. 또 하자!"
```

### `0717E0`  165 → 140바이트

```
원문 | KEENU
원문 | "A challenger! Let's go!"
원문 | CRASH!
원문 | 
원문 | CRASH! POW!
원문 | 
원문 | CRASH! POW POW!
원문 | 
원문 | CRASH! POW POW POW!
원문 | 
원문 | "Yeah! I won!"
원문 | 
원문 | ({08} LOST...)
원문 | 
원문 | KEENU
원문 | "Ha ha ha! I won!
원문 | Care for a rematch?!"
```

```
번역 | 키누
번역 | "도전자다! 가자!"
번역 | 쾅!
번역 | 
번역 | 쾅! 펑!
번역 | 
번역 | 쾅! 펑 펑!
번역 | 
번역 | 쾅! 펑 펑 펑!
번역 | 
번역 | "좋아! 내가 이겼다!"
번역 | 
번역 | ({08} 패배…)
번역 | 
번역 | 키누
번역 | "하하하! 내가 이겼다!
번역 | 한판 더 어때?!"
```

### `0717E4`  65 → 52바이트

```
원문 | (I'LL PASS...)
원문 | 
원문 | KEENU
원문 | "What? You won't fight?
원문 | What a letdown!..."
```

```
번역 | (그만둘래…)
번역 | 
번역 | 키누
번역 | "뭐? 안 싸운다고?
번역 | 김새게 하네!…"
```

### `0717E8`  43 → 32바이트

```
원문 | KEENU
원문 | "Oh, back again?
원문 | Jump on in anytime."
```

```
번역 | 키누
번역 | "어, 또 왔어?
번역 | 언제든 덤벼."
```

### `0717EC`  69 → 58바이트

```
원문 | BOY
원문 | "Yes! I cleared stage 41!
원문 | I've almost got this
원문 | puzzle game beat!"
```

```
번역 | 남자아이
번역 | "좋았어! 41단계 깼다!
번역 | 이 퍼즐 게임 거의
번역 | 다 깼어!"
```

### `0717F0`  75 → 60바이트

```
원문 | SENSEI
원문 | "What? That's weird?...
원문 | Was Goyoke really
원문 | that strong after all?..."
```

```
번역 | 선생님
번역 | "뭐? 이상하군?…
번역 | 고요케가 정말 그렇게
번역 | 강했던 건가?…"
```

### `0717F4`  31 → 33바이트  (빈 곳으로 옮겨 담음)

```
원문 | BOY
원문 | "Eat this, Reflecto Force!"
```

```
번역 | 남자아이
번역 | "받아라, 리플렉토 포스!"
```

### `0717FC`  57 → 49바이트

```
원문 | TONKO
원문 | "Don't talk to me, bub.
원문 | I'm about to finish URIEN."
```

```
번역 | 톤코
번역 | "말 걸지 마, 임마.
번역 | 이제 곧 유리엔을 끝낸다."
```

### `071800`  88 → 79바이트

```
원문 | TONKO
원문 | "Whew. A tough opponent...
원문 | I'm a great URIEN player, huh?
원문 | I've never lost a game!"
```

```
번역 | 톤코
번역 | "휴. 만만찮은 상대였어…
번역 | 내가 유리엔은 잘 다루지?
번역 | 한 번도 진 적이 없다고!"
```

### `071804`  77 → 67바이트

```
원문 | BOY
원문 | "I wanna play that game, but...
원문 | That guy's so good,
원문 | he plays forever...."
```

```
번역 | 남자아이
번역 | "저 게임 하고 싶은데…
번역 | 저 형이 너무 잘해서
번역 | 끝나질 않아…."
```

### `071808`  80 → 74바이트

```
원문 | SCHOOL KID
원문 | "Yes. All right! Huh?
원문 | Whoops! Got so involved,
원문 | I forget where I was!"
```

```
번역 | 학생
번역 | "좋았어! 됐다! 어?
번역 | 어이쿠! 너무 몰입해서
번역 | 어디까지 했는지 잊어버렸네!"
```

### `07180C`  57 → 49바이트

```
원문 | SCHOOL KID
원문 | "Power dunk!
원문 | Rats! Blocked!
원문 | Aaah! Cut it out!"
```

```
번역 | 학생
번역 | "파워 덩크!
번역 | 젠장! 막혔다!
번역 | 아아! 그만 좀 해!"
```

### `071810`  62 → 53바이트

```
원문 | STUDENT
원문 | "Soul Fist!
원문 | Yes! All right!
원문 | Next a combo from a jump!"
```

```
번역 | 학생
번역 | "소울 피스트!
번역 | 좋았어! 됐다!
번역 | 다음은 점프 콤보다!"
```

### `071814`  57 → 45바이트

```
원문 | SCHOOL KID
원문 | "Tornado Kick!
원문 | Uh! He ducked!
원문 | Ha ha! A block!"
```

```
번역 | 학생
번역 | "토네이도 킥!
번역 | 어! 숙였네!
번역 | 하하! 막았다!"
```

### `071828`  89 → 60바이트

```
원문 | KEENU
원문 | "Hmm. You're quite a player.
원문 | How about a game with me?
원문 | I'll be waiting over there."
```

```
번역 | 키누
번역 | "흠. 제법인데.
번역 | 나랑 한판 어때?
번역 | 저기서 기다리고 있을게."
```

### `07182C`  129 → 93바이트

```
원문 | BARTENDER
원문 | "Hey, good to see you again.
원문 | I got the recent edition
원문 | of 'CAPCOM Secret File.'
원문 | It's chock full of
원문 | all kind of secrets!"
```

```
번역 | 바텐더
번역 | "어, 또 뵙네요.
번역 | "캡콤 시크릿 파일" 최신호를
번역 | 구했어요.
번역 | 온갖 비밀이
번역 | 가득 들어 있습니다!"
```

### `071860`  133 → 119바이트

```
원문 | BARTENDER
원문 | "Welcome!
원문 | I'm a pro at this
원문 | job now!
원문 | Ask me anything.
원문 | This is just a rumor...
원문 | But I hear Nishi
원문 | has some really cool cards."
```

```
번역 | 바텐더
번역 | "어서 오세요!
번역 | 이제 이 일도
번역 | 프로가 됐죠!
번역 | 뭐든 물어보세요.
번역 | 이건 소문인데요…
번역 | 니시가 정말 좋은 카드를
번역 | 갖고 있대요."
```

### `071864`  142 → 132바이트

```
원문 | BARTENDER
원문 | "Welcome!
원문 | I'm a pro at this
원문 | job now!
원문 | Ask me anything.
원문 | This is just a rumor...
원문 | But that Yosiki guy...
원문 | he's packing some sweet cards."
```

```
번역 | 바텐더
번역 | "어서 오세요!
번역 | 이제 이 일도
번역 | 프로가 됐죠!
번역 | 뭐든 물어보세요.
번역 | 이건 소문인데요…
번역 | 그 요시키라는 사람…
번역 | 끝내주는 카드를 갖고 있대요."
```

### `071868`  58 → 51바이트

```
원문 | KEIKO
원문 | "Oh, it's {08}."
원문 | HARUMI
원문 | "All right. It's rematch time!"
```

```
번역 | 케이코
번역 | "어, {08}잖아."
번역 | 하루미
번역 | "좋아. 재대결 시간이야!"
```

### `07186C`  58 → 51바이트

```
원문 | KEIKO
원문 | "Oh, it's {08}."
원문 | HARUMI
원문 | "All right. It's rematch time!"
```

```
번역 | 케이코
번역 | "어, {08}잖아."
번역 | 하루미
번역 | "좋아. 재대결 시간이야!"
```

### `071870`  57 → 59바이트  (빈 곳으로 옮겨 담음)

```
원문 | HARUMI
원문 | "Hey! No one's here."
원문 | KEIKO
원문 | "Oh bummer! ...Later!"
```

```
번역 | 하루미
번역 | "어이! 아무도 없잖아."
번역 | 케이코
번역 | "아 아쉽네! …나중에!"
```

### `07187C`  23 → 25바이트  (빈 곳으로 옮겨 담음)

```
원문 | KID
원문 | "OK, I'll explain."
```

```
번역 | 키드
번역 | "좋아, 설명해 줄게."
```

### `071880`  177 → 128바이트

```
원문 | KID
원문 | "You got it? ...That's right!
원문 | Cap, last year's champion,
원문 | has come here to play.
원문 | How about taking him on?
원문 | If you lose, nothing changes.
원문 | Win, and you're laughing!
원문 | Go get him!"
```

```
번역 | 키드
번역 | "알겠어? …그래 맞아!
번역 | 작년 챔피언 캡이
번역 | 여기 왔대.
번역 | 한번 붙어 보는 게 어때?
번역 | 지면 달라질 게 없고,
번역 | 이기면 대박이지!
번역 | 가서 이겨!"
```

### `071884`  179 → 139바이트

```
원문 | KID
원문 | "You following me? By the way..
원문 | Cap, last year's champion,
원문 | has come here to play.
원문 | How about taking him on?
원문 | If you lose, nothing changes.
원문 | Win, and it's your break!
원문 | Go get him!"
```

```
번역 | 키드
번역 | "따라오고 있어? 그건 그렇고…
번역 | 작년 챔피언 캡이
번역 | 여기 왔대.
번역 | 한번 붙어 보는 게 어때?
번역 | 지면 달라질 게 없고,
번역 | 이기면 기회가 열려!
번역 | 가서 이겨!"
```

### `071888`  154 → 116바이트

```
원문 | KID
원문 | "Understand? Oh, by the way...
원문 | Cap, last year's champion,
원문 | has come here to play.
원문 | How about taking him on?
원문 | You could learn something.
원문 | Now, go get him!"
```

```
번역 | 키드
번역 | "알겠어? 아 참, 그런데…
번역 | 작년 챔피언 캡이
번역 | 여기 왔대.
번역 | 한번 붙어 보는 게 어때?
번역 | 배울 게 있을 거야.
번역 | 자, 가서 이겨!"
```


## 카드·능력 이름 (434개)

사람 이름은 한국 격투게임판에서 굳어진 표기를 따랐습니다.
기술 이름은 뜻이 있으면 옮기고 고유하면 소리대로 적었습니다.
**16바이트(한글 8자) 고정**이라 길게 못 씁니다.

### `050514`  16 → 4바이트

```
원문 | TERRY
```

```
번역 | 테리
```

### `050524`  16 → 9바이트

```
원문 | TERRY RUSH
```

```
번역 | 테리 러시
```

### `050554`  16 → 4바이트

```
원문 | ANDY
```

```
번역 | 앤디
```

### `050564`  16 → 11바이트

```
원문 | SHADOW SLICER
```

```
번역 | 그림자 베기
```

### `050594`  16 → 2바이트

```
원문 | JOE
```

```
번역 | 죠
```

### `0505A4`  16 → 5바이트

```
원문 | S-UPPER
```

```
번역 | S어퍼
```

### `0505D4`  16 → 4바이트

```
원문 | MAI
```

```
번역 | 마이
```

### `0505E4`  16 → 4바이트

```
원문 | MORPH
```

```
번역 | 변신
```

### `050614`  16 → 4바이트

```
원문 | BILLY
```

```
번역 | 빌리
```

### `050624`  16 → 13바이트

```
원문 | SHRIKE DROP
```

```
번역 | 슈라이크 드롭
```

### `050654`  16 → 2바이트

```
원문 | KIM
```

```
번역 | 김
```

### `050694`  16 → 5바이트

```
원문 | DUCK KING
```

```
번역 | 덕 킹
```

### `0506A4`  16 → 7바이트

```
원문 | DUCK DANCE
```

```
번역 | 덕 댄스
```

### `0506D4`  16 → 9바이트

```
원문 | BLUE MARY
```

```
번역 | 블루 메리
```

### `0506E4`  16 → 10바이트

```
원문 | MARACHNID
```

```
번역 | 마라크니드
```

### `050714`  16 → 5바이트

```
원문 | HON FU
```

```
번역 | 혼 후
```

### `050754`  16 → 2바이트

```
원문 | BOB
```

```
번역 | 밥
```

### `050794`  16 → 8바이트

```
원문 | YAMAZAKI
```

```
번역 | 야마자키
```

### `0507A4`  16 → 6바이트

```
원문 | FACE OFF
```

```
번역 | 맞대결
```

### `0507D4`  16 → 5바이트

```
원문 | CHONG SHU
```

```
번역 | 총 슈
```

### `0507E4`  16 → 4바이트

```
원문 | FOGEY FISTS
```

```
번역 | 노권
```

### `050814`  16 → 7바이트

```
원문 | CHONG LEI
```

```
번역 | 총 레이
```

### `050854`  16 → 2바이트

```
원문 | RICK
```

```
번역 | 릭
```

### `050894`  16 → 7바이트

```
원문 | XIANG FEI
```

```
번역 | 샹 페이
```

### `0508D4`  16 → 8바이트

```
원문 | ALFRED
```

```
번역 | 알프레드
```

### `0508E4`  16 → 7바이트

```
원문 | W-RIDER
```

```
번역 | W라이더
```

### `050914`  16 → 6바이트

```
원문 | TSUGUMI
```

```
번역 | 츠구미
```

### `050954`  16 → 8바이트

```
원문 | KRAUSER
```

```
번역 | 크라우저
```

### `050994`  16 → 4바이트

```
원문 | GEESE
```

```
번역 | 기스
```

### `0509D4`  16 → 2바이트

```
원문 | RYO
```

```
번역 | 료
```

### `0509E4`  16 → 7바이트

```
원문 | SPIRIT SURGE
```

```
번역 | 기 폭발
```

### `050A14`  16 → 6바이트

```
원문 | ROBERT
```

```
번역 | 로버트
```

### `050A54`  16 → 4바이트

```
원문 | YURI
```

```
번역 | 유리
```

### `050A64`  16 → 5바이트

```
원문 | BRING IT ON!
```

```
번역 | 덤벼!
```

### `050A94`  16 → 6바이트

```
원문 | TAKUMA
```

```
번역 | 타쿠마
```

### `050AD4`  16 → 13바이트

```
원문 | MR. KARATE
```

```
번역 | 미스터 가라테
```

### `050AE4`  16 → 4바이트

```
원문 | M.I.A.
```

```
번역 | 실종
```

### `050B14`  16 → 2바이트

```
원문 | KING
```

```
번역 | 킹
```

### `050B24`  16 → 4바이트

```
원문 | DEALER
```

```
번역 | 딜러
```

### `050B54`  16 → 2바이트

```
원문 | JOHN
```

```
번역 | 존
```

### `050B94`  16 → 9바이트

```
원문 | LEE PYLON
```

```
번역 | 리 파이론
```

### `050BD4`  16 → 9바이트

```
원문 | MR. BIG
```

```
번역 | 미스터 빅
```

### `050C14`  16 → 6바이트

```
원문 | EIJI
```

```
번역 | 에이지
```

### `050C24`  16 → 4바이트

```
원문 | PROPHECY
```

```
번역 | 예언
```

### `050C54`  16 → 6바이트

```
원문 | KASUMI
```

```
번역 | 카스미
```

### `050C64`  16 → 11바이트

```
원문 | OVERLAP CRUNCH
```

```
번역 | 겹쳐 부수기
```

### `050C94`  16 → 8바이트

```
원문 | HAOHMARU
```

```
번역 | 하오마루
```

### `050CA4`  16 → 4바이트

```
원문 | IRON SLICE
```

```
번역 | 철참
```

### `050CD4`  16 → 4바이트

```
원문 | UKYO
```

```
번역 | 우쿄
```

### `050CE4`  16 → 11바이트

```
원문 | DWINDLING LIFE
```

```
번역 | 시드는 목숨
```

### `050D14`  16 → 4바이트

```
원문 | HANZO
```

```
번역 | 한조
```

### `050D24`  16 → 6바이트

```
원문 | DUST CLOUD
```

```
번역 | 흙먼지
```

### `050D54`  16 → 6바이트

```
원문 | GALFORD
```

```
번역 | 갈포드
```

### `050D64`  16 → 11바이트

```
원문 | HEY, POPPY!
```

```
번역 | 이봐, 포피!
```

### `050D94`  16 → 11바이트

```
원문 | NAKORURU(C)
```

```
번역 | 나코루루(C)
```

### `050DA4`  16 → 11바이트

```
원문 | BALM OF NATURE
```

```
번역 | 자연의 은혜
```

### `050DD4`  16 → 11바이트

```
원문 | NAKORURU(T)
```

```
번역 | 나코루루(T)
```

### `050DE4`  16 → 13바이트

```
원문 | SHIKUROO'S FANG
```

```
번역 | 시쿠루 송곳니
```

### `050E14`  16 → 8바이트

```
원문 | NAKORURU
```

```
번역 | 나코루루
```

### `050E24`  16 → 13바이트

```
원문 | MAMAHAHA CALL
```

```
번역 | 마마하하 부름
```

### `050E54`  16 → 9바이트

```
원문 | RIMNEREL(C)
```

```
번역 | 림네렐(C)
```

### `050E64`  16 → 11바이트

```
원문 | WIND WHISPER
```

```
번역 | 바람 속삭임
```

### `050E94`  16 → 9바이트

```
원문 | RIMNEREL(T)
```

```
번역 | 림네렐(T)
```

### `050EA4`  16 → 4바이트

```
원문 | KONRIL
```

```
번역 | 콘릴
```

### `050ED4`  16 → 6바이트

```
원문 | JUBEI
```

```
번역 | 주베이
```

### `050F14`  16 → 4바이트

```
원문 | CHARLOTTE
```

```
번역 | 샬롯
```

### `050F54`  16 → 6바이트

```
원문 | KYOSHIRO
```

```
번역 | 쿄시로
```

### `050F64`  16 → 9바이트

```
원문 | WARRIOR DANCE
```

```
번역 | 무사의 춤
```

### `050F94`  16 → 4바이트

```
원문 | GENAN
```

```
번역 | 겐안
```

### `050FA4`  16 → 9바이트

```
원문 | PEEPING KAY!
```

```
번역 | 훔쳐보기!
```

### `050FD4`  16 → 5바이트

```
원문 | TAM TAM
```

```
번역 | 탐 탐
```

### `051014`  16 → 5바이트

```
원문 | CHAM CHAM
```

```
번역 | 챰 챰
```

### `051054`  16 → 6바이트

```
원문 | GENJURO
```

```
번역 | 겐주로
```

### `051064`  16 → 8바이트

```
원문 | I KNEW IT!
```

```
번역 | 그럴 줄!
```

### `051094`  16 → 6바이트

```
원문 | NICOTINE
```

```
번역 | 니코틴
```

### `0510A4`  16 → 9바이트

```
원문 | EXORCISM CARD
```

```
번역 | 퇴마 카드
```

### `0510D4`  16 → 8바이트

```
원문 | SHIZUMARU
```

```
번역 | 시즈마루
```

### `0510E4`  16 → 9바이트

```
원문 | MIDSUMMER RAIN
```

```
번역 | 한여름 비
```

### `051114`  16 → 6바이트

```
원문 | GAIRA
```

```
번역 | 가이라
```

### `051124`  16 → 5바이트

```
원문 | SHOUT!
```

```
번역 | 외침!
```

### `051154`  16 → 6바이트

```
원문 | BASARA
```

```
번역 | 바사라
```

### `051194`  16 → 6바이트

```
원문 | KAZUKI
```

```
번역 | 카즈키
```

### `0511A4`  16 → 6바이트

```
원문 | IMBROGLIO
```

```
번역 | 뒤엉킴
```

### `0511D4`  16 → 6바이트

```
원문 | SOUGETSU
```

```
번역 | 소게츠
```

### `0511E4`  16 → 11바이트

```
원문 | FRIGID SMIRK
```

```
번역 | 서늘한 웃음
```

### `051214`  16 → 7바이트

```
원문 | SHIKI(C)
```

```
번역 | 시키(C)
```

### `051224`  16 → 7바이트

```
원문 | NRG SYPHON
```

```
번역 | 기 흡수
```

### `051254`  16 → 7바이트

```
원문 | SHIKI(T)
```

```
번역 | 시키(T)
```

### `051264`  16 → 11바이트

```
원문 | YUGA'S SPELL
```

```
번역 | 유가의 주문
```

### `051294`  16 → 6바이트

```
원문 | ASRA
```

```
번역 | 아스라
```

### `0512A4`  16 → 11바이트

```
원문 | RISING EVIL
```

```
번역 | 깨어나는 악
```

### `0512D4`  16 → 6바이트

```
원문 | TAIZAN
```

```
번역 | 타이잔
```

### `051314`  16 → 8바이트

```
원문 | AMAKUSA
```

```
번역 | 아마쿠사
```

### `051324`  16 → 11바이트

```
원문 | GIVE YOURSELF
```

```
번역 | 몸을 바쳐라
```

### `051354`  16 → 6바이트

```
원문 | ZANKURO
```

```
번역 | 잔쿠로
```

### `051394`  16 → 4바이트

```
원문 | THE UMP
```

```
번역 | 심판
```

### `0513A4`  16 → 4바이트

```
원문 | MYSTIC
```

```
번역 | 신비
```

### `0513D4`  16 → 2바이트

```
원문 | KYO
```

```
번역 | 쿄
```

### `0513E4`  16 → 11바이트

```
원문 | OROCHI WAVE
```

```
번역 | 오로치 파동
```

### `051414`  16 → 5바이트

```
원문 | KYO(P)
```

```
번역 | 쿄(P)
```

### `051424`  16 → 5바이트

```
원문 | 182WAYS
```

```
번역 | 182식
```

### `051454`  16 → 8바이트

```
원문 | BENIMARU
```

```
번역 | 베니마루
```

### `051464`  16 → 6바이트

```
원문 | THUNDERGOD FIST
```

```
번역 | 뇌신권
```

### `051494`  16 → 6바이트

```
원문 | DAIMON
```

```
번역 | 다이몬
```

### `0514D4`  16 → 8바이트

```
원문 | HEIDERN
```

```
번역 | 하이데른
```

### `0514E4`  16 → 7바이트

```
원문 | S-BRINGER
```

```
번역 | S브링어
```

### `051514`  16 → 6바이트

```
원문 | LEONA
```

```
번역 | 레오나
```

### `051524`  16 → 10바이트

```
원문 | X-CALIBRE
```

```
번역 | 엑스칼리버
```

### `051554`  16 → 4바이트

```
원문 | RALF
```

```
번역 | 랄프
```

### `051594`  16 → 4바이트

```
원문 | CLARK
```

```
번역 | 클락
```

### `0515D4`  16 → 8바이트

```
원문 | A.ASAMIYA
```

```
번역 | 아사미야
```

### `0515E4`  16 → 11바이트

```
원문 | PSYCHO CHARGE
```

```
번역 | 사이코 충전
```

### `051614`  16 → 4바이트

```
원문 | KENSU
```

```
번역 | 켄수
```

### `051624`  16 → 10바이트

```
원문 | MEAT MUFFIN!
```

```
번역 | 고기 머핀!
```

### `051654`  16 → 9바이트

```
원문 | CHIN GENSAI
```

```
번역 | 친 겐사이
```

### `051694`  16 → 2바이트

```
원문 | CHAN
```

```
번역 | 창
```

### `0516D4`  16 → 2바이트

```
원문 | CHOI
```

```
번역 | 최
```

### `0516E4`  16 → 6바이트

```
원문 | ENABLER
```

```
번역 | 조력자
```

### `051714`  16 → 6바이트

```
원문 | SAISHU
```

```
번역 | 사이슈
```

### `051724`  16 → 4바이트

```
원문 | EXORCISM
```

```
번역 | 퇴마
```

### `051754`  16 → 4바이트

```
원문 | SHINGO
```

```
번역 | 신고
```

### `051764`  16 → 12바이트

```
원문 | BURNING SHINGO!
```

```
번역 | 불타는 신고!
```

### `051794`  16 → 6바이트

```
원문 | CHIZURU
```

```
번역 | 치즈루
```

### `0517A4`  16 → 5바이트

```
원문 | CONTAIN!
```

```
번역 | 봉인!
```

### `0517D4`  16 → 6바이트

```
원문 | IORI
```

```
번역 | 이오리
```

### `0517E4`  16 → 9바이트

```
원문 | BLOOD CONTRACT
```

```
번역 | 피의 계약
```

### `051814`  16 → 6바이트

```
원문 | YASHIRO
```

```
번역 | 야시로
```

### `051824`  16 → 4바이트

```
원문 | COUNTERBLOW
```

```
번역 | 반격
```

### `051854`  16 → 6바이트

```
원문 | SHERMIE
```

```
번역 | 셰르미
```

### `051864`  16 → 10바이트

```
원문 | BE GENTLE TO ME
```

```
번역 | 잘 대해 줘
```

### `051894`  16 → 6바이트

```
원문 | CHRIS
```

```
번역 | 크리스
```

### `0518D4`  16 → 6바이트

```
원문 | GOENITZ
```

```
번역 | 괴니츠
```

### `051914`  16 → 6바이트

```
원문 | OROCHI
```

```
번역 | 오로치
```

### `051924`  16 → 4바이트

```
원문 | SANITY
```

```
번역 | 이성
```

### `051954`  16 → 6바이트

```
원문 | MATURE
```

```
번역 | 마츄어
```

### `051994`  16 → 6바이트

```
원문 | VICE
```

```
번역 | 바이스
```

### `0519D4`  16 → 11바이트

```
원문 | WILD IORI
```

```
번역 | 폭주 이오리
```

### `0519E4`  16 → 4바이트

```
원문 | KURF
```

```
번역 | 커프
```

### `051A14`  16 → 11바이트

```
원문 | WILD LEONA
```

```
번역 | 폭주 레오나
```

### `051A24`  16 → 4바이트

```
원문 | AWAKENING
```

```
번역 | 각성
```

### `051A54`  16 → 2바이트

```
원문 | K'
```

```
번역 | K'
```

### `051A64`  16 → 12바이트

```
원문 | UNSTOPPABLE
```

```
번역 | 막을 수 없음
```

### `051A94`  16 → 6바이트

```
원문 | MAXIMA
```

```
번역 | 맥시마
```

### `051AD4`  16 → 6바이트

```
원문 | kaede
```

```
번역 | 카에데
```

### `051B14`  16 → 6바이트

```
원문 | KAEDE
```

```
번역 | 카에데
```

### `051B24`  16 → 9바이트

```
원문 | POWER MATCH
```

```
번역 | 힘 겨루기
```

### `051B54`  16 → 6바이트

```
원문 | MORIYA
```

```
번역 | 모리야
```

### `051B94`  16 → 9바이트

```
원문 | AKARI(P)
```

```
번역 | 아카리(P)
```

### `051BA4`  16 → 8바이트

```
원문 | 100 DEMON NIGHT
```

```
번역 | 백귀야행
```

### `051BD4`  16 → 9바이트

```
원문 | AKARI(S)
```

```
번역 | 아카리(S)
```

### `051BE4`  16 → 9바이트

```
원문 | ONE-WAY MORPH
```

```
번역 | 일방 변신
```

### `051C14`  16 → 4바이트

```
원문 | JUZO
```

```
번역 | 주조
```

### `051C54`  16 → 8바이트

```
원문 | WASHIZUKA
```

```
번역 | 와시즈카
```

### `051C94`  16 → 6바이트

```
원문 | KOJIRO
```

```
번역 | 코지로
```

### `051CD4`  16 → 6바이트

```
원문 | AMANO
```

```
번역 | 아마노
```

### `051D14`  16 → 6바이트

```
원문 | MUKURO
```

```
번역 | 무쿠로
```

### `051D54`  16 → 7바이트

```
원문 | LEE REKKA
```

```
번역 | 리 렛카
```

### `051D94`  16 → 4바이트

```
원문 | ZANTETSU
```

```
번역 | 참철
```

### `051DD4`  16 → 4바이트

```
원문 | SHIGEN
```

```
번역 | 시겐
```

### `051DE4`  16 → 9바이트

```
원문 | STEEL BULB
```

```
번역 | 강철 구근
```

### `051E14`  16 → 6바이트

```
원문 | KAGAMI
```

```
번역 | 카가미
```

### `051E24`  16 → 6바이트

```
원문 | PHOENIX
```

```
번역 | 불사조
```

### `051E54`  16 → 6바이트

```
원문 | HIBIKI
```

```
번역 | 히비키
```

### `051E94`  16 → 6바이트

```
원문 | SETSUNA
```

```
번역 | 세츠나
```

### `051EA4`  16 → 11바이트

```
원문 | LIFE SIGN
```

```
번역 | 생명의 징표
```

### `051ED4`  16 → 6바이트

```
원문 | THE WANDERER
```

```
번역 | 방랑자
```

### `051EE4`  16 → 5바이트

```
원문 | CHANGE!
```

```
번역 | 교체!
```

### `051F14`  16 → 6바이트

```
원문 | AKARI
```

```
번역 | 아카리
```

### `051F24`  16 → 7바이트

```
원문 | PONTA LEAF
```

```
번역 | 폰타 잎
```

### `051F54`  16 → 6바이트

```
원문 | HAYATE
```

```
번역 | 하야테
```

### `051F94`  16 → 4바이트

```
원문 | CAROL
```

```
번역 | 캐롤
```

### `051FD4`  16 → 4바이트

```
원문 | ROSA
```

```
번역 | 로사
```

### `052014`  16 → 6바이트

```
원문 | KIM SUE IL
```

```
번역 | 김수일
```

### `052054`  16 → 6바이트

```
원문 | SHISHIOU
```

```
번역 | 시시오
```

### `052094`  16 → 4바이트

```
원문 | guy
```

```
번역 | 가이
```

### `0520A4`  16 → 9바이트

```
원문 | LONELY RING
```

```
번역 | 외로운 링
```

### `0520D4`  16 → 6바이트

```
원문 | TAKATO
```

```
번역 | 타카토
```

### `052114`  16 → 9바이트

```
원문 | ROB PYTHON
```

```
번역 | 롭 파이톤
```

### `052154`  16 → 4바이트

```
원문 | ERI
```

```
번역 | 에리
```

### `052194`  16 → 6바이트

```
원문 | TARMA
```

```
번역 | 타르마
```

### `0521D4`  16 → 6바이트

```
원문 | MARCO
```

```
번역 | 마르코
```

### `0521E4`  16 → 7바이트

```
원문 | ENEMY CHASER
```

```
번역 | 적 추격
```

### `052214`  16 → 4바이트

```
원문 | FIO
```

```
번역 | 피오
```

### `052254`  16 → 4바이트

```
원문 | RODDY
```

```
번역 | 로디
```

### `052294`  16 → 4바이트

```
원문 | CATHY
```

```
번역 | 캐시
```

### `0522D4`  16 → 6바이트

```
원문 | ATHENA
```

```
번역 | 아테나
```

### `0522E4`  16 → 6바이트

```
원문 | FIRE SWORD
```

```
번역 | 화염검
```

### `052314`  16 → 2바이트

```
원문 | RYU
```

```
번역 | 류
```

### `052324`  16 → 9바이트

```
원문 | S.HADO-KEN
```

```
번역 | 초 파동권
```

### `052354`  16 → 2바이트

```
원문 | KEN
```

```
번역 | 켄
```

### `052364`  16 → 11바이트

```
원문 | RAGE WAVE
```

```
번역 | 분노의 파동
```

### `052394`  16 → 4바이트

```
원문 | CHUN-LI
```

```
번역 | 춘리
```

### `0523A4`  16 → 6바이트

```
원문 | S.B.KICK
```

```
번역 | 초 B킥
```

### `0523D4`  16 → 4바이트

```
원문 | GUILE
```

```
번역 | 가일
```

### `0523E4`  16 → 5바이트

```
원문 | S.KICK
```

```
번역 | 초 킥
```

### `052414`  16 → 4바이트

```
원문 | E.HONDA
```

```
번역 | 혼다
```

### `052454`  16 → 6바이트

```
원문 | BLANKA
```

```
번역 | 블랑카
```

### `052494`  16 → 4바이트

```
원문 | DHALSIM
```

```
번역 | 달심
```

### `0524A4`  16 → 6바이트

```
원문 | ENLIGHTENMENT
```

```
번역 | 깨달음
```

### `0524D4`  16 → 8바이트

```
원문 | ZANGIEF
```

```
번역 | 장기에프
```

### `052514`  16 → 6바이트

```
원문 | BALROG
```

```
번역 | 발로그
```

### `052554`  16 → 4바이트

```
원문 | VEGA
```

```
번역 | 베가
```

### `052594`  16 → 6바이트

```
원문 | SAGAT
```

```
번역 | 사가트
```

### `0525A4`  16 → 9바이트

```
원문 | TRUE POWER
```

```
번역 | 진정한 힘
```

### `0525D4`  16 → 8바이트

```
원문 | M. BISON
```

```
번역 | M.바이슨
```

### `0525E4`  16 → 13바이트

```
원문 | EVIL CHARISMA
```

```
번역 | 악의 카리스마
```

### `052614`  16 → 6바이트

```
원문 | DEE JAY
```

```
번역 | 디제이
```

### `052654`  16 → 6바이트

```
원문 | T. HAWK
```

```
번역 | T.호크
```

### `052694`  16 → 7바이트

```
원문 | FEI-LING
```

```
번역 | 페이 링
```

### `0526D4`  16 → 4바이트

```
원문 | CAMMY
```

```
번역 | 캐미
```

### `052714`  16 → 7바이트

```
원문 | CAMMY(A)
```

```
번역 | 캐미(A)
```

### `052724`  16 → 4바이트

```
원문 | SPY
```

```
번역 | 첩자
```

### `052754`  16 → 6바이트

```
원문 | AKUMA
```

```
번역 | 아쿠마
```

### `052764`  16 → 6바이트

```
원문 | SHUN-GOKU-SATSU
```

```
번역 | 순옥살
```

### `052794`  16 → 5바이트

```
원문 | RYU(A)
```

```
번역 | 류(A)
```

### `0527A4`  16 → 6바이트

```
원문 | HADO-KEN
```

```
번역 | 파동권
```

### `0527D4`  16 → 7바이트

```
원문 | CHUN-LI(A)
```

```
번역 | 춘리(A)
```

### `0527E4`  16 → 5바이트

```
원문 | SORRY!
```

```
번역 | 미안!
```

### `052814`  16 → 4바이트

```
원문 | GUY
```

```
번역 | 가이
```

### `052824`  16 → 8바이트

```
원문 | HAYA-GAKE
```

```
번역 | 하야가케
```

### `052854`  16 → 4바이트

```
원문 | ROSE
```

```
번역 | 로즈
```

### `052864`  16 → 9바이트

```
원문 | TAROT CARD
```

```
번역 | 타로 카드
```

### `052894`  16 → 4바이트

```
원문 | CHARLIE
```

```
번역 | 찰리
```

### `0528D4`  16 → 4바이트

```
원문 | SODOM
```

```
번역 | 소돔
```

### `052914`  16 → 4바이트

```
원문 | BIRDIE
```

```
번역 | 버디
```

### `052954`  16 → 4바이트

```
원문 | ADON
```

```
번역 | 아돈
```

### `052994`  16 → 2바이트

```
원문 | DAN
```

```
번역 | 단
```

### `0529A4`  16 → 5바이트

```
원문 | WHAT GIVES?
```

```
번역 | 뭐야?
```

### `0529D4`  16 → 6바이트

```
원문 | SAKURA
```

```
번역 | 사쿠라
```

### `0529E4`  16 → 13바이트

```
원문 | SAKURA FIGHT
```

```
번역 | 사쿠라 파이트
```

### `052A14`  16 → 2바이트

```
원문 | GEN
```

```
번역 | 겐
```

### `052A24`  16 → 4바이트

```
원문 | CHANGING SCHOOL
```

```
번역 | 전학
```

### `052A54`  16 → 6바이트

```
원문 | ROLENTO
```

```
번역 | 로렌토
```

### `052A94`  16 → 4바이트

```
원문 | KARIN
```

```
번역 | 카린
```

### `052AA4`  16 → 6바이트

```
원문 | HOU-SHOU
```

```
번역 | 호우쇼
```

### `052AD4`  16 → 6바이트

```
원문 | R. MIKA
```

```
번역 | R.미카
```

### `052B14`  16 → 4바이트

```
원문 | JUNI
```

```
번역 | 유니
```

### `052B54`  16 → 4바이트

```
원문 | JULI
```

```
번역 | 율리
```

### `052B94`  16 → 6바이트

```
원문 | ALEX
```

```
번역 | 알렉스
```

### `052BA4`  16 → 9바이트

```
원문 | S.HEADBUTT
```

```
번역 | 초 박치기
```

### `052BD4`  16 → 2바이트

```
원문 | YUN
```

```
번역 | 윤
```

### `052C14`  16 → 2바이트

```
원문 | YANG
```

```
번역 | 양
```

### `052C54`  16 → 2바이트

```
원문 | SEAN
```

```
번역 | 션
```

### `052C64`  16 → 11바이트

```
원문 | SORE LOSER
```

```
번역 | 억울한 패자
```

### `052C94`  16 → 4바이트

```
원문 | ORO
```

```
번역 | 오로
```

### `052CA4`  16 → 7바이트

```
원문 | TENGU STONE
```

```
번역 | 텐구 돌
```

### `052CD4`  16 → 6바이트

```
원문 | ELENA
```

```
번역 | 엘레나
```

### `052CE4`  16 → 4바이트

```
원문 | HEALING
```

```
번역 | 치유
```

### `052D14`  16 → 6바이트

```
원문 | IBUKI
```

```
번역 | 이부키
```

### `052D54`  16 → 6바이트

```
원문 | NECRO
```

```
번역 | 네크로
```

### `052D94`  16 → 6바이트

```
원문 | MAKOTO
```

```
번역 | 마코토
```

### `052DA4`  16 → 5바이트

```
원문 | YELL!
```

```
번역 | 기합!
```

### `052DD4`  16 → 1바이트

```
원문 | Q
```

```
번역 | Q
```

### `052E14`  16 → 6바이트

```
원문 | TWELVE
```

```
번역 | 트웰브
```

### `052E24`  16 → 5바이트

```
원문 | X.C.O.P.Y.
```

```
번역 | X카피
```

### `052E54`  16 → 4바이트

```
원문 | REMY
```

```
번역 | 레미
```

### `052E64`  16 → 4바이트

```
원문 | REVENGE
```

```
번역 | 복수
```

### `052E94`  16 → 4바이트

```
원문 | RETSU
```

```
번역 | 렛츠
```

### `052ED4`  16 → 2바이트

```
원문 | LEE
```

```
번역 | 리
```

### `052F14`  16 → 4바이트

```
원문 | EVIL RYU
```

```
번역 | 사류
```

### `052F24`  16 → 9바이트

```
원문 | EVIL ENERGY
```

```
번역 | 악의 기운
```

### `052F54`  16 → 8바이트

```
원문 | DEMITRI
```

```
번역 | 데미트리
```

### `052F64`  16 → 15바이트

```
원문 | MIDNIGHT BLISS
```

```
번역 | 미드나잇 블리스
```

### `052F94`  16 → 6바이트

```
원문 | MORRIGAN
```

```
번역 | 모리건
```

### `052FA4`  16 → 9바이트

```
원문 | LIFE SUCKER
```

```
번역 | 생명 흡수
```

### `052FD4`  16 → 9바이트

```
원문 | MORRIGAN(P)
```

```
번역 | 모리건(P)
```

### `052FE4`  16 → 11바이트

```
원문 | GOODNIGHT KISS
```

```
번역 | 굿나잇 키스
```

### `053014`  16 → 8바이트

```
원문 | J. TALBAIN
```

```
번역 | J.탈바인
```

### `053024`  16 → 7바이트

```
원문 | SEETHING BLOOD
```

```
번역 | 끓는 피
```

### `053054`  16 → 6바이트

```
원문 | L. RAPTOR
```

```
번역 | L.랩터
```

### `053094`  16 → 4바이트

```
원문 | VICTOR
```

```
번역 | 빅터
```

### `0530D4`  16 → 8바이트

```
원문 | FELICIA
```

```
번역 | 펠리시아
```

### `0530E4`  16 → 11바이트

```
원문 | SIDEKICK ART
```

```
번역 | 조수의 기술
```

### `053114`  16 → 8바이트

```
원문 | SASQUATCH
```

```
번역 | 사스콰치
```

### `053154`  16 → 6바이트

```
원문 | BISHAMON
```

```
번역 | 비샤몬
```

### `053164`  16 → 11바이트

```
원문 | REGRETFUL LOP
```

```
번역 | 아쉬운 베기
```

### `053194`  16 → 10바이트

```
원문 | ANAKARIS
```

```
번역 | 아나카리스
```

### `0531A4`  16 → 8바이트

```
원문 | J.O.T.P.
```

```
번역 | J.O.T.P.
```

### `0531D4`  16 → 6바이트

```
원문 | RIKUO
```

```
번역 | 리쿠오
```

### `053214`  16 → 4바이트

```
원문 | HUITZIL
```

```
번역 | 위칠
```

### `053254`  16 → 6바이트

```
원문 | PYRON
```

```
번역 | 파이론
```

### `053264`  16 → 11바이트

```
원문 | COSMO POWER
```

```
번역 | 코스모 파워
```

### `053294`  16 → 6바이트

```
원문 | HSIEN-KO
```

```
번역 | 시엔코
```

### `0532D4`  16 → 6바이트

```
원문 | DONOVAN
```

```
번역 | 도노반
```

### `0532E4`  16 → 9바이트

```
원문 | CHANGE IMMORTAL
```

```
번역 | 불사 변신
```

### `053314`  16 → 4바이트

```
원문 | JEDAH
```

```
번역 | 제다
```

### `053324`  16 → 6바이트

```
원문 | P.D.C.
```

```
번역 | P.D.C.
```

### `053354`  16 → 8바이트

```
원문 | B.B. HOOD
```

```
번역 | B.B.후드
```

### `053364`  16 → 9바이트

```
원문 | APPLE FOR YOU
```

```
번역 | 사과 하나
```

### `053394`  16 → 3바이트

```
원문 | Q-BEE
```

```
번역 | Q비
```

### `0533A4`  16 → 8바이트

```
원문 | PLUS B
```

```
번역 | 플러스 B
```

### `0533D4`  16 → 6바이트

```
원문 | LILITH
```

```
번역 | 릴리스
```

### `0533E4`  16 → 9바이트

```
원문 | BECOMING ONE
```

```
번역 | 하나 되기
```

### `053414`  16 → 6바이트

```
원문 | HAYATO
```

```
번역 | 하야토
```

### `053424`  16 → 6바이트

```
원문 | ASHURA
```

```
번역 | 아수라
```

### `053454`  16 → 8바이트

```
원문 | B.HAYATO
```

```
번역 | B.하야토
```

### `053494`  16 → 2바이트

```
원문 | JUNE
```

```
번역 | 준
```

### `0534D4`  16 → 2바이트

```
원문 | RAIN
```

```
번역 | 비
```

### `0534E4`  16 → 7바이트

```
원문 | BACK OFF!
```

```
번역 | 물러서!
```

### `053514`  16 → 11바이트

```
원문 | JIN SAOTOME
```

```
번역 | 진 사오토메
```

### `053524`  16 → 13바이트

```
원문 | S.DYNAMITE
```

```
번역 | S다이너마이트
```

### `053554`  16 → 8바이트

```
원문 | BLODIA
```

```
번역 | 블로디아
```

### `053564`  16 → 9바이트

```
원문 | ENERGY COST
```

```
번역 | 기력 소모
```

### `053594`  16 → 11바이트

```
원문 | ZERO AKUMA
```

```
번역 | 제로 아쿠마
```

### `0535D4`  16 → 4바이트

```
원문 | LEO
```

```
번역 | 레오
```

### `053614`  16 → 4바이트

```
원문 | KENJI
```

```
번역 | 켄지
```

### `053654`  16 → 4바이트

```
원문 | TESSA
```

```
번역 | 테사
```

### `053664`  16 → 11바이트

```
원문 | SOLAR CANE
```

```
번역 | 태양 지팡이
```

### `053694`  16 → 9바이트

```
원문 | AL & IVEN
```

```
번역 | 알 & 이븐
```

### `0536D4`  16 → 7바이트

```
원문 | MAI LING
```

```
번역 | 마이 링
```

### `053714`  16 → 4바이트

```
원문 | BATSU
```

```
번역 | 바츠
```

### `053724`  16 → 7바이트

```
원문 | BOILING BLOOD
```

```
번역 | 끓는 피
```

### `053754`  16 → 6바이트

```
원문 | KYOSUKE
```

```
번역 | 쿄스케
```

### `053764`  16 → 2바이트

```
원문 | COOL
```

```
번역 | 쿨
```

### `053794`  16 → 6바이트

```
원문 | HINATA
```

```
번역 | 히나타
```

### `0537A4`  16 → 5바이트

```
원문 | GO FOR IT!
```

```
번역 | 힘내!
```

### `0537D4`  16 → 6바이트

```
원문 | akira
```

```
번역 | 아키라
```

### `0537E4`  16 → 7바이트

```
원문 | BROTHER SEARCH
```

```
번역 | 형 찾기
```

### `053814`  16 → 6바이트

```
원문 | AKIRA
```

```
번역 | 아키라
```

### `053854`  16 → 6바이트

```
원문 | DAIGO
```

```
번역 | 다이고
```

### `053864`  16 → 5바이트

```
원문 | FINISH IT!
```

```
번역 | 끝내!
```

### `053894`  16 → 4바이트

```
원문 | KYOKO
```

```
번역 | 쿄코
```

### `0538A4`  16 → 4바이트

```
원문 | MASSAGE
```

```
번역 | 안마
```

### `0538D4`  16 → 6바이트

```
원문 | HIDEO
```

```
번역 | 히데오
```

### `053914`  16 → 4바이트

```
원문 | FALCON
```

```
번역 | 팰컨
```

### `053924`  16 → 9바이트

```
원문 | POWER STONE
```

```
번역 | 파워 스톤
```

### `053954`  16 → 6바이트

```
원문 | AYAME
```

```
번역 | 아야메
```

### `053964`  16 → 10바이트

```
원문 | OHKA-GAKURE
```

```
번역 | 오카가쿠레
```

### `053994`  16 → 5바이트

```
원문 | WANG TANG
```

```
번역 | 왕 탕
```

### `0539D4`  16 → 4바이트

```
원문 | RYOMA
```

```
번역 | 료마
```

### `053A14`  16 → 4바이트

```
원문 | ROUGE
```

```
번역 | 루즈
```

### `053A54`  16 → 4바이트

```
원문 | HIRYU
```

```
번역 | 히류
```

### `053A64`  16 → 6바이트

```
원문 | CYPHER
```

```
번역 | 사이퍼
```

### `053A94`  16 → 4바이트

```
원문 | OPTION
```

```
번역 | 옵션
```

### `053AA4`  16 → 4바이트

```
원문 | SUPPORT
```

```
번역 | 지원
```

### `053AD4`  16 → 4바이트

```
원문 | CODY
```

```
번역 | 코디
```

### `053B14`  16 → 4바이트

```
원문 | HAGGAR
```

```
번역 | 해거
```

### `053B24`  16 → 8바이트

```
원문 | SPINNING LARIAT
```

```
번역 | 라리아트
```

### `053B54`  16 → 4바이트

```
원문 | DAMND
```

```
번역 | 댐드
```

### `053B64`  16 → 8바이트

```
원문 | WHISTLE
```

```
번역 | 호루라기
```

### `053B94`  16 → 8바이트

```
원문 | C.COMMANDO
```

```
번역 | C.코만도
```

### `053BA4`  16 → 6바이트

```
원문 | C.CORRIDOR
```

```
번역 | C.복도
```

### `053BD4`  16 → 6바이트

```
원문 | G.THE NINJA
```

```
번역 | G.닌자
```

### `053C14`  16 → 8바이트

```
원문 | M.THE KNIFE
```

```
번역 | M.나이프
```

### `053C54`  16 → 11바이트

```
원문 | BABY HEAD
```

```
번역 | 베이비 헤드
```

### `053C94`  16 → 4바이트

```
원문 | LEON
```

```
번역 | 레온
```

### `053CA4`  16 → 4바이트

```
원문 | CONFINEMENT
```

```
번역 | 감금
```

### `053CD4`  16 → 6바이트

```
원문 | CLAIRE
```

```
번역 | 클레어
```

### `053CE4`  16 → 4바이트

```
원문 | DECOY
```

```
번역 | 미끼
```

### `053D14`  16 → 4바이트

```
원문 | ZOMBIE
```

```
번역 | 좀비
```

### `053D24`  16 → 12바이트

```
원문 | RESIDENT EVIL
```

```
번역 | 바이오하자드
```

### `053D54`  16 → 2바이트

```
원문 | JILL
```

```
번역 | 질
```

### `053D64`  16 → 6바이트

```
원문 | BERETTA
```

```
번역 | 베레타
```

### `053D94`  16 → 4바이트

```
원문 | MEGA MAN
```

```
번역 | 록맨
```

### `053DA4`  16 → 9바이트

```
원문 | ENEMY ABILITY
```

```
번역 | 적의 능력
```

### `053DD4`  16 → 2바이트

```
원문 | ROLL
```

```
번역 | 롤
```

### `053DE4`  16 → 9바이트

```
원문 | ROLL BUSTER
```

```
번역 | 롤 버스터
```

### `053E14`  16 → 4바이트

```
원문 | RUSH
```

```
번역 | 러시
```

### `053E54`  16 → 6바이트

```
원문 | PROTO MAN
```

```
번역 | 블루스
```

### `053E94`  16 → 4바이트

```
원문 | MEGA MAN X
```

```
번역 | 엑스
```

### `053EA4`  16 → 9바이트

```
원문 | PARTS CHANGE
```

```
번역 | 파츠 교체
```

### `053ED4`  16 → 4바이트

```
원문 | ZERO
```

```
번역 | 제로
```

### `053F14`  16 → 4바이트

```
원문 | ARTHUR
```

```
번역 | 아서
```

### `053F54`  16 → 11바이트

```
원문 | RED ARREMER
```

```
번역 | 레드 아리마
```

### `053F94`  16 → 6바이트

```
원문 | LUCIFER
```

```
번역 | 루시퍼
```

### `053FA4`  16 → 4바이트

```
원문 | SACRIFICE
```

```
번역 | 희생
```

### `053FD4`  16 → 5바이트

```
원문 | RYU (B)
```

```
번역 | 류(B)
```

### `053FE4`  16 → 4바이트

```
원문 | TRANSFORM
```

```
번역 | 변형
```

### `054014`  16 → 4바이트

```
원문 | NINA
```

```
번역 | 니나
```

### `054024`  16 → 4바이트

```
원문 | WINGS
```

```
번역 | 날개
```

### `054054`  16 → 4바이트

```
원문 | MICHELLE
```

```
번역 | 미셸
```

### `054094`  16 → 4바이트

```
원문 | SAKI
```

```
번역 | 사키
```

### `0540A4`  16 → 4바이트

```
원문 | STAND-BY
```

```
번역 | 대기
```

### `0540D4`  16 → 13바이트

```
원문 | MECH ZANGIEF
```

```
번역 | 메카 장기에프
```

### `054114`  16 → 5바이트

```
원문 | FIGHT!
```

```
번역 | 싸워!
```

### `054154`  16 → 4바이트

```
원문 | LIGHTNING
```

```
번역 | 번개
```

### `054194`  16 → 4바이트

```
원문 | DOUBLE
```

```
번역 | 더블
```

### `0541D4`  16 → 8바이트

```
원문 | PUPPET
```

```
번역 | 꼭두각시
```

### `054214`  16 → 4바이트

```
원문 | ESCAPE
```

```
번역 | 도망
```

### `054254`  16 → 6바이트

```
원문 | PEACEMAKER
```

```
번역 | 중재자
```

### `054294`  16 → 4바이트

```
원문 | REPARATION
```

```
번역 | 배상
```

### `0542D4`  16 → 4바이트

```
원문 | SCHOOL'S OUT
```

```
번역 | 하교
```

### `054314`  16 → 9바이트

```
원문 | COVER FIRE
```

```
번역 | 엄호 사격
```

### `054354`  16 → 4바이트

```
원문 | BOPPER
```

```
번역 | 보퍼
```

### `054394`  16 → 4바이트

```
원문 | CHAOS
```

```
번역 | 혼돈
```

### `0543D4`  16 → 6바이트

```
원문 | GRENADE
```

```
번역 | 수류탄
```

### `054414`  16 → 11바이트

```
원문 | MEGA CRUSH
```

```
번역 | 메가 크러시
```

### `054454`  16 → 9바이트

```
원문 | EARTH'S PIKE
```

```
번역 | 대지의 창
```

### `054494`  16 → 4바이트

```
원문 | BREAK UP
```

```
번역 | 결별
```

### `0544D4`  16 → 2바이트

```
원문 | NOTHINGNESS
```

```
번역 | 무
```

### `054514`  16 → 7바이트

```
원문 | DOUBLE KO
```

```
번역 | 더블 KO
```

### `054554`  16 → 8바이트

```
원문 | SERAPHIC W
```

```
번역 | 천사의 W
```

### `054594`  16 → 11바이트

```
원문 | FATE DUEL
```

```
번역 | 운명의 결투
```

### `0545D4`  16 → 4바이트

```
원문 | SLAUGHTER
```

```
번역 | 학살
```

### `054614`  16 → 9바이트

```
원문 | RAW SHIELD
```

```
번역 | 맨몸 방패
```

### `054654`  16 → 4바이트

```
원문 | GRACE
```

```
번역 | 은총
```

### `054694`  16 → 4바이트

```
원문 | ABDUCTION
```

```
번역 | 납치
```

### `0546D4`  16 → 10바이트

```
원문 | PSYCHE UP!
```

```
번역 | 정신 집중!
```

### `054714`  16 → 11바이트

```
원문 | HEY! HEY!
```

```
번역 | 어이! 어이!
```

### `054754`  16 → 4바이트

```
원문 | HERITAGE
```

```
번역 | 유산
```

### `054794`  16 → 12바이트

```
원문 | BEST SHOT
```

```
번역 | 최고의 한 방
```

### `0547D4`  16 → 13바이트

```
원문 | LUCKY KITTY
```

```
번역 | 행운의 고양이
```

### `054814`  16 → 7바이트

```
원문 | ROUND 2
```

```
번역 | 2라운드
```

### `054854`  16 → 4바이트

```
원문 | AWAKENING
```

```
번역 | 각성
```

### `054894`  16 → 4바이트

```
원문 | MORPH
```

```
번역 | 변신
```

### `0548D4`  16 → 7바이트

```
원문 | SHOWTIME!
```

```
번역 | 쇼타임!
```

### `054914`  16 → 6바이트

```
원문 | ESP
```

```
번역 | 초능력
```

### `054954`  16 → 4바이트

```
원문 | SUBSTITUTE
```

```
번역 | 대체
```

### `054994`  16 → 4바이트

```
원문 | CURSE
```

```
번역 | 저주
```

### `0549D4`  16 → 4바이트

```
원문 | STIFLER
```

```
번역 | 방해
```

### `054A14`  16 → 9바이트

```
원문 | STORM RUSH
```

```
번역 | 폭풍 돌격
```

### `054A54`  16 → 6바이트

```
원문 | PRIDE
```

```
번역 | 자존심
```

### `054A94`  16 → 4바이트

```
원문 | MISCHIEF
```

```
번역 | 장난
```

### `054AD4`  16 → 11바이트

```
원문 | NO TRICKS
```

```
번역 | 속임수 금지
```

### `054B14`  16 → 4바이트

```
원문 | MAKEOVER
```

```
번역 | 단장
```

### `054B54`  16 → 6바이트

```
원문 | PESTER
```

```
번역 | 성가심
```

### `054B94`  16 → 4바이트

```
원문 | MANAGEMENT
```

```
번역 | 경영
```

### `054BD4`  16 → 11바이트

```
원문 | LAST RESORT
```

```
번역 | 최후의 수단
```

### `054C14`  16 → 4바이트

```
원문 | ROULETTE
```

```
번역 | 룰렛
```

### `054C54`  16 → 4바이트

```
원문 | SHOPPING
```

```
번역 | 쇼핑
```

### `054C94`  16 → 4바이트

```
원문 | LAUNDRY
```

```
번역 | 빨래
```

### `054CD4`  16 → 4바이트

```
원문 | STUDY
```

```
번역 | 공부
```

### `054D14`  16 → 4바이트

```
원문 | REVIVE
```

```
번역 | 부활
```

### `054D54`  16 → 4바이트

```
원문 | EMULATE
```

```
번역 | 흉내
```

### `054D94`  16 → 5바이트

```
원문 | ACTIVATE!
```

```
번역 | 발동!
```

### `054DD4`  16 → 6바이트

```
원문 | TOOPTADON
```

```
번역 | 툽타돈
```

### `054E14`  16 → 5바이트

```
원문 | SP PARTNER
```

```
번역 | SP 짝
```

### `054E54`  16 → 6바이트

```
원문 | SYNCHRO
```

```
번역 | 싱크로
```

### `054E94`  16 → 4바이트

```
원문 | INDULGE
```

```
번역 | 탐닉
```

### `054ED4`  16 → 8바이트

```
원문 | GLARE OFF
```

```
번역 | 노려보기
```

### `054F14`  16 → 6바이트

```
원문 | SHADOW
```

```
번역 | 그림자
```

### `054F54`  16 → 9바이트

```
원문 | TRI-QUIZ
```

```
번역 | 삼중 퀴즈
```

### `054F94`  16 → 9바이트

```
원문 | RESET BUTTON
```

```
번역 | 리셋 단추
```

### `054FD4`  16 → 6바이트

```
원문 | DREGS
```

```
번역 | 찌꺼기
```


## NPC 대사 (163개)

인물마다 말투를 달리했습니다.
캡·마스크는 무겁게, 키드·타카는 가볍게, 포·니시·야규는
나이 든 말투, 츄피 팬은 들뜬 말투로 잡았습니다.

### `07014C`  16 → 19바이트  (빈 곳으로 옮겨 담음)

```
원문 | YOU GOT
원문 | NO CARD.
```

```
번역 | 카드를 받지 못했다.
```

### `070170`  16 → 12바이트

```
원문 | ARE YOU READY?
원문 | {0C}
```

```
번역 | 준비됐나요?{0C}
```

### `070174`  18 → 18바이트

```
원문 | TURNED DOWN MATCH.
```

```
번역 | 대전을 물렀습니다.
```

### `070178`  18 → 20바이트  (빈 곳으로 옮겨 담음)

```
원문 | MATCH TURNED DOWN.
```

```
번역 | 대전이 물러졌습니다.
```

### `070188`  17 → 16바이트

```
원문 | CHOOSING VS MODE.
```

```
번역 | 대전 방식 고르기
```

### `070194`  12 → 9바이트

```
원문 | CARD YOU GOT
```

```
번역 | 받은 카드
```

### `0701C8`  17 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | REARRANGING DECK.
```

```
번역 | 덱을 다시 짜는 중.
```

### `0701D8`  15 → 9바이트

```
원문 | ALBUM COMPLETED
```

```
번역 | 앨범 완성
```

### `0701E4`  19 → 16바이트

```
원문 | PROCEED TO
원문 | AIRPORT.
```

```
번역 | 공항으로 갑니다.
```

### `070320`  39 → 30바이트

```
원문 |   COUNTER   RING CHARACTER
원문 |   NO COUNTER
```

```
번역 | {20}되받기{20}{20}{20}링 캐릭터
번역 | {20}안 되받기
```

### `070324`  22 → 17바이트

```
원문 |    SINGLE      UNITE 2
```

```
번역 | {20}{20}혼자{20}{20}{20}{20}{20}합체 2
```

### `070328`  42 → 31바이트

```
원문 |    SINGLE      UNITE 2
원문 |             UNITE 3
```

```
번역 | {20}{20}혼자{20}{20}{20}{20}{20}합체 2
번역 | {20}{20}{20}{20}{20}{20}{20}합체 3
```

### `07032C`  12 → 11바이트

```
원문 |   USE
원문 |   DATA
```

```
번역 | {20}사용
번역 | {20}자료
```

### `070330`  48 → 45바이트

```
원문 |   HAND    SEARCH    INFO
원문 |   ATTACK  ABILITY   END
```

```
번역 | {20}손패{20}{20}{20}{20}찾기{20}{20}{20}{20}{20}정보
번역 | {20}공격{20}{20}{20}{20}능력{20}{20}{20}{20}{20}종료
```

### `070334`  53 → 47바이트

```
원문 |    RING CHA  YOUR DISCARDS
원문 |    STATUS   ENEMY DISCARDS
```

```
번역 | {20}{20}링 캐릭터{20}{20}내 버린 패
번역 | {20}{20}상태{20}{20}{20}{20}{20}상대 버린 패
```

### `070338`  9 → 6바이트

```
원문 | BACK-UP {0A}
```

```
번역 | 백업 {0A}
```

### `07033C`  8 → 8바이트

```
원문 | {0A}'S "{17}"!
```

```
번역 | {0A}의 "{17}"!
```

### `070340`  12 → 9바이트

```
원문 | {0A}'S BACK-UP!
```

```
번역 | {0A}의 백업!
```

### `070344`  8 → 6바이트

```
원문 |  ATTACK!
```

```
번역 |  공격!
```

### `070348`  13 → 13바이트

```
원문 | {0A} POWERED UP!
```

```
번역 | {0A}가 강해졌다!
```

### `07034C`  9 → 7바이트

```
원문 | {0A} ENTERS!
```

```
번역 | {0A} 등장!
```

### `070350`  33 → 29바이트

```
원문 | {08} CHARACTER'S
원문 | FREEZE PHASE ENDED.
```

```
번역 | {08}의 캐릭터가
번역 | 얼음에서 풀렸다.
```

### `070354`  33 → 29바이트

```
원문 | {09} CHARACTER'S
원문 | FREEZE PHASE ENDED.
```

```
번역 | {09}의 캐릭터가
번역 | 얼음에서 풀렸다.
```

### `070358`  8 → 6바이트

```
원문 | {08}'S TURN
```

```
번역 | {08}의 턴
```

### `07035C`  8 → 6바이트

```
원문 | {09}'S TURN
```

```
번역 | {09}의 턴
```

### `070360`  10 → 10바이트

```
원문 | {08} USES
원문 | "{0A}"
```

```
번역 | {08} 사용
번역 | "{0A}"
```

### `070364`  10 → 10바이트

```
원문 | {09} USES
원문 | "{0A}"
```

```
번역 | {09} 사용
번역 | "{0A}"
```

### `070368`  12 → 17바이트  (빈 곳으로 옮겨 담음)

```
원문 | {08} DRAWS CARD
```

```
번역 | {08}가 카드를 뽑았다
```

### `07036C`  12 → 17바이트  (빈 곳으로 옮겨 담음)

```
원문 | {09} DRAWS CARD
```

```
번역 | {09}가 카드를 뽑았다
```

### `070370`  26 → 26바이트

```
원문 | NO CHARACTER WITH [ABILITY
```

```
번역 | [능력을 가진 캐릭터가 없다
```

### `070374`  32 → 28바이트

```
원문 | CHOOSE CHARACTER TO USE
원문 | [ABILITY
```

```
번역 | [능력을 쓸 캐릭터를
번역 | 고르세요
```

### `070378`  17 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE 2ND PLAYER
```

```
번역 | 두 번째 사람을 고르세요.
```

### `07037C`  24 → 19바이트

```
원문 | NOT ENOUGH"SP"
원문 | (COST: {0E})
```

```
번역 | SP 모자람
번역 | (비용: {0E})
```

### `070380`  14 → 9바이트

```
원문 | SP USES {0E} PTS.
```

```
번역 | SP {0E} 소모
```

### `070384`  20 → 25바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE 5 CARDS EACH.
```

```
번역 | 각자 카드를 5장 고르세요.
```

### `070388`  12 → 11바이트

```
원문 | CHOOSE CARD.
```

```
번역 | 카드 고르기
```

### `07038C`  40 → 30바이트

```
원문 | CHOOSE CARD.
원문 | (SORT CARDS WITH "OPTION".)
```

```
번역 | 카드 고르기
번역 | (OPTION 으로 정렬)
```

### `070390`  17 → 13바이트

```
원문 | CHOOSE CHARACTER.
```

```
번역 | 캐릭터 고르기
```

### `070394`  26 → 24바이트

```
원문 | CHARACTER CAN'T "BACK-UP".
```

```
번역 | 백업할 수 없는 캐릭터다.
```

### `070398`  26 → 22바이트

```
원문 | CHARACTER HAS NO [ABILITY.
```

```
번역 | [능력이 없는 캐릭터다.
```

### `07039C`  24 → 24바이트

```
원문 | CHARACTER CAN'T COUNTER.
```

```
번역 | 되받을 수 없는 캐릭터다.
```

### `0703A0`  17 → 11바이트

```
원문 | FIRST CHARACTER'S
```

```
번역 | 첫 캐릭터의
```

### `0703A4`  22 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHARACTER CAN'T ATTACK
```

```
번역 | 공격할 수 없는 캐릭터다.
```

### `0703A8`  42 → 33바이트

```
원문 | JUST ENTERED RING.
원문 | CAN'T USE FOR BACK-UPS.
```

```
번역 | 방금 링에 나왔다.
번역 | 백업에 못 쓴다.
```

### `0703AC`  39 → 34바이트

```
원문 | JUST ENTERED RING.
원문 | CAN'T USE [ABILITIES
```

```
번역 | 방금 링에 나왔다.
번역 | [능력을 못 쓴다.
```

### `0703B0`  32 → 31바이트

```
원문 | JUST ENTERED RING.
원문 | CAN'T ATTACK.
```

```
번역 | 방금 링에 나왔다.
번역 | 공격 못 한다.
```

### `0703B4`  20 → 19바이트

```
원문 | NO ENEMY TO COUNTER.
```

```
번역 | 되받을 상대가 없다.
```

### `0703B8`  8 → 7바이트

```
원문 | END TURN
```

```
번역 | 턴 종료
```

### `0703BC`  28 → 25바이트

```
원문 | CHOOSE CHARACTER TO COUNTER?
```

```
번역 | 되받을 캐릭터를 고르세요.
```

### `0703C0`  25 → 25바이트

```
원문 | CHOOSE BACK-UP CHARACTER.
```

```
번역 | 백업할 캐릭터를 고르세요.
```

### `0703C4`  25 → 17바이트

```
원문 | DISCARD RETURNED TO PILE!
```

```
번역 | 버린 패가 더미로!
```

### `0703C8`  24 → 29바이트  (빈 곳으로 옮겨 담음)

```
원문 | ONLY 1 BACK-UP PER TURN.
```

```
번역 | 백업은 턴마다 한 번만 됩니다.
```

### `0703CC`  24 → 20바이트

```
원문 | CHOOSE COUNTER CHARACTER
```

```
번역 | 되받을 캐릭터 고르기
```

### `0703D0`  29 → 29바이트

```
원문 | DO COUNTER?
원문 |     YES        NO
```

```
번역 | 되받을까요?
번역 | {20}{20}{20}{19}예{20}{20}{20}{20}{20}{20}{1A}아뇨
```

### `0703D4`  9 → 9바이트

```
원문 | NO EFFECT
```

```
번역 | 효과 없음
```

### `0703D8`  15 → 25바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE ATTACKER
```

```
번역 | 공격할 캐릭터를 고르세요.
```

### `0703DC`  16 → 20바이트  (빈 곳으로 옮겨 담음)

```
원문 | NO ATTACKER LEFT
```

```
번역 | 공격할 캐릭터가 없다
```

### `0703E0`  30 → 29바이트

```
원문 | MAKE ATTACK?
원문 |     YES        NO
```

```
번역 | 공격할까요?
번역 | {20}{20}{20}{19}예{20}{20}{20}{20}{20}{20}{1A}아뇨
```

### `0703E4`  23 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | CAN'T BACK-UP IN FREEZE
```

```
번역 | 얼어 있어 백업할 수 없다
```

### `0703E8`  30 → 25바이트

```
원문 | CAN'T USE [ABILITIES IN FREEZE
```

```
번역 | 얼어 있어 [능력을 못 쓴다
```

### `0703EC`  23 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | CAN'T COUNTER IN FREEZE
```

```
번역 | 얼어 있어 되받을 수 없다
```

### `0703F0`  22 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | CAN'T ATTACK IN FREEZE
```

```
번역 | 얼어 있어 공격할 수 없다
```

### `0703F4`  21 → 24바이트  (빈 곳으로 옮겨 담음)

```
원문 | NO CARD TO PUT ON TOP
```

```
번역 | 맨 위에 놓을 카드가 없다
```

### `0703F8`  16 → 19바이트  (빈 곳으로 옮겨 담음)

```
원문 | NO CARD IN PILE!
```

```
번역 | 더미에 카드가 없다!
```

### `0703FC`  12 → 9바이트

```
원문 | SHUFFLE PILE
```

```
번역 | 더미 섞기
```

### `070400`  21 → 21바이트

```
원문 | CHOOSE YOUR CHARACTER
```

```
번역 | 내 캐릭터를 고르세요.
```

### `070404`  16 → 17바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE YOUR RING
```

```
번역 | 내 링을 고르세요.
```

### `070408`  16 → 14바이트

```
원문 | NO DISCARDS LEFT
```

```
번역 | 버린 패가 없다
```

### `07040C`  15 → 18바이트  (빈 곳으로 옮겨 담음)

```
원문 | NO CARD IN HAND
```

```
번역 | 손패에 카드가 없다
```

### `070410`  25 → 23바이트

```
원문 | CHOOSE CHARACTER POSITION
```

```
번역 | 캐릭터 자리를 고르세요.
```

### `070414`  20 → 18바이트

```
원문 | NO CHARACTER IN RING
```

```
번역 | 링에 캐릭터가 없다
```

### `070418`  10 → 7바이트

```
원문 | {08}'S FIRST!
```

```
번역 | {08} 선공!
```

### `07041C`  10 → 7바이트

```
원문 | {09}'S FIRST!
```

```
번역 | {09} 선공!
```

### `070420`  19 → 16바이트

```
원문 | CHOOSE FIRST PLAYER
```

```
번역 | 선공을 고르세요.
```

### `070424`  22 → 23바이트  (빈 곳으로 옮겨 담음)

```
원문 | CHOOSE ENEMY CHARACTER
```

```
번역 | 상대 캐릭터를 고르세요.
```

### `070428`  10 → 8바이트

```
원문 | TIME'S UP!
```

```
번역 | 시간 끝!
```

### `07042C`  8 → 4바이트

```
원문 | STAND-BY
```

```
번역 | 대기
```

### `070430`  30 → 25바이트

```
원문 | NO CHARACTER CARD
원문 | IN {08}'S PILE!
```

```
번역 | {08} 더미에
번역 | 캐릭터 카드 없음
```

### `070434`  30 → 25바이트

```
원문 | NO CHARACTER CARD
원문 | IN {09}'S PILE!
```

```
번역 | {09} 더미에
번역 | 캐릭터 카드 없음
```

### `070438`  23 → 21바이트

```
원문 | NO AC CARD
원문 | IN {08}'S PILE!
```

```
번역 | {08} 더미에
번역 | AC 카드 없음
```

### `07043C`  23 → 21바이트

```
원문 | NO AC CARD
원문 | IN {09}'S PILE!
```

```
번역 | {09} 더미에
번역 | AC 카드 없음
```

### `070440`  30 → 24바이트

```
원문 | CHOOSE AC CARD
원문 | TO PLACE ON TOP
```

```
번역 | 위에 놓을
번역 | AC 카드 고르기
```

### `070444`  31 → 28바이트

```
원문 | CHOOSE CHA CARD
원문 | TO PLACE ON TOP
```

```
번역 | 위에 놓을
번역 | 캐릭터 카드 고르기
```

### `070448`  22 → 15바이트

```
원문 | {0E} SP USED
원문 | FOR \ABILITY
```

```
번역 | SP {0E} 씀
번역 | \능력에
```

### `07044C`  22 → 21바이트

```
원문 | CHOOSE FIRST CHARACTER
```

```
번역 | 첫 캐릭터를 고르세요.
```

### `070450`  21 → 17바이트

```
원문 | CAN'T CHOOSE THIS ONE
```

```
번역 | 이건 고를 수 없다
```

### `070454`  30 → 23바이트

```
원문 | CHOOSE TARGET
원문 | (YOUR CHARACTER)
```

```
번역 | 대상 고르기
번역 | (내 캐릭터)
```

### `070458`  31 → 25바이트

```
원문 | CHOOSE TARGET
원문 | (ENEMY CHARACTER)
```

```
번역 | 대상 고르기
번역 | (상대 캐릭터)
```

### `07045C`  40 → 32바이트

```
원문 | CHOOSE TARGET
원문 |   YOUR PILE   ENEMY'S PILE
```

```
번역 | 대상 고르기
번역 | {20}내 더미{20}{20}{20}상대 더미
```

### `07188C`  157 → 121바이트

```
원문 | KID
원문 | "Ha ha. Probably..Oh, by the way.
원문 | Cap, last year's champion,
원문 | has come here to play.
원문 | How about taking him on?
원문 | You could learn something.
원문 | Now, go get him!"
```

```
번역 | 키드
번역 | "하하. 아마도. 아 참, 그런데.
번역 | 작년 챔피언 캡이
번역 | 여기 왔대.
번역 | 한번 붙어 보는 게 어때?
번역 | 배울 게 있을 거야.
번역 | 자, 가서 이겨!"
```

### `071898`  25 → 23바이트

```
원문 | FO
원문 | "OK. You listen well!"
```

```
번역 | 포
번역 | "좋소. 잘 들었구먼!"
```

### `07189C`  62 → 60바이트

```
원문 | FO
원문 | "Do you understand?
원문 | Good. Now I must go
원문 | teach some others."
```

```
번역 | 포
번역 | "이해했소?
번역 | 좋소. 이제 다른 사람들도
번역 | 가르치러 가야겠구먼."
```

### `0718A0`  75 → 67바이트

```
원문 | FO
원문 | "Oh, really? That's big bummer.
원문 | Well, all right.
원문 | I go teach some others"
```

```
번역 | 포
번역 | "오, 그렇소? 아쉽구먼.
번역 | 뭐, 알겠소.
번역 | 다른 사람들 가르치러 가겠소."
```

### `0718A8`  92 → 76바이트

```
원문 | KEENU
원문 | "Hey, got a 'CHUN-LI' card?
원문 | If you have one,
원문 | I'll trade it for 'TERRY.'
원문 | TRADE CARDS?
원문 | {0D}
```

```
번역 | 키누
번역 | "어이, "춘리" 카드 있어?
번역 | 있으면
번역 | "테리"랑 바꿔 줄게."
번역 | 카드를 바꿀까요?
번역 | {0D}
```

### `0718AC`  66 → 52바이트

```
원문 | KEENU
원문 | "Huh?
원문 | You don't have a 'CHUN-LI'?
원문 | Why you wasting my time?!"
```

```
번역 | 키누
번역 | "어?
번역 | "춘리"가 없잖아?
번역 | 왜 내 시간을 뺏는 거야?!"
```

### `0718B0`  69 → 63바이트

```
원문 | TAM
원문 | "Nice timing.
원문 | There playing 'RESIDENT EVIL'
원문 | in back.
원문 | Go and see."
```

```
번역 | 탐
번역 | "때맞춰 왔네.
번역 | 뒤쪽에서 "바이오하자드"를
번역 | 하고 있어.
번역 | 가서 봐."
```

### `0718B4`  58 → 53바이트

```
원문 | YOUNG LADY
원문 | "Hey, where's my food?"
원문 | CHEF
원문 | "Coming right up!"
```

```
번역 | 아가씨
번역 | "저기요, 제 음식은요?"
번역 | 요리사
번역 | "금방 나갑니다!"
```

### `0718B8`  29 → 31바이트  (빈 곳으로 옮겨 담음)

```
원문 | GIRL
원문 | "Aw! I broke my cookie!"
```

```
번역 | 여자아이
번역 | "앗! 과자가 부서졌어!"
```

### `0718BC`  81 → 77바이트

```
원문 | GIRL
원문 | "Aw! I can't catch one!"
원문 | CARNY GUY
원문 | "Here, it's on the house!"
원문 | GIRL
원문 | "Yippee!"
```

```
번역 | 여자아이
번역 | "앗! 하나도 못 잡겠어!"
번역 | 노점상
번역 | "자, 이건 서비스야!"
번역 | 여자아이
번역 | "우와!"
```

### `0718C0`  127 → 95바이트

```
원문 | BOY
원문 | "Hmmm...
원문 | With all these shops,
원문 | I just can't decide.
원문 | I think I'll try the Trading
원문 | Machine
원문 | at the fortune teller's first...."
```

```
번역 | 남자아이
번역 | "음…
번역 | 가게가 이렇게 많으니
번역 | 도무지 못 고르겠네.
번역 | 일단 점집에 있는
번역 | 교환기부터 해 볼까…."
```

### `0718C4`  133 → 127바이트

```
원문 | BOY
원문 | "Did you enter the RESIDENT EVIL
원문 | MANSION?
원문 | It was just so real!
원문 | It scared me silly!
원문 | My sweety was so scared,
원문 | she had conniptions!"
```

```
번역 | 남자아이
번역 | "바이오하자드 저택에
번역 | 들어가 봤어?
번역 | 진짜 실감 났어!
번역 | 무서워 죽는 줄 알았다니까!
번역 | 내 여자친구는 너무 놀라서
번역 | 기절할 뻔했어!"
```

### `0718C8`  72 → 71바이트

```
원문 | GIRL
원문 | "You liar!...
원문 | He yelled when you saw
원문 | the zombie make-up. Pathetic!"
```

```
번역 | 여자아이
번역 | "거짓말쟁이!…
번역 | 좀비 분장 보고 네가 소리 질렀잖아.
번역 | 한심하기는!"
```

### `0718CC`  66 → 61바이트

```
원문 | SASUGA
원문 | "Step right up!
원문 | These are delicious!
원문 | Have some octo-balls!"
```

```
번역 | 사스가
번역 | "자자, 어서 오세요!
번역 | 맛있습니다!
번역 | 타코야키 드셔 보세요!"
```

### `0718D0`  138 → 114바이트

```
원문 | SASUGA
원문 | "Oh, you have the 'UMP' card!
원문 | It may not seem like much,
원문 | but pair it with an AC card,
원문 | and...Whoops! You can try
원문 | the rest yourself!"
```

```
번역 | 사스가
번역 | "오, "심판" 카드를 갖고 있네!
번역 | 별것 아닌 것 같아도
번역 | 액션 카드랑 같이 쓰면…
번역 | 어이쿠! 나머지는
번역 | 직접 해 보시오!"
```

### `0718D4`  115 → 117바이트  (빈 곳으로 옮겨 담음)

```
원문 | OCTO-BALL GUY
원문 | "Step right up...
원문 | My octopus balls
원문 | just can't be beat...
원문 | No one's tastier than me!
원문 | Sasuga's says so!"
```

```
번역 | 타코야키 아저씨
번역 | "자, 어서 오시오…
번역 | 내 타코야키는
번역 | 어디에도 안 지지…
번역 | 나보다 맛있는 데는 없소!
번역 | 사스가도 그리 말했다오!"
```

### `0718D8`  108 → 82바이트

```
원문 | FORTUNE TELLER
원문 | "Step right up!
원문 | My Trading Machine's payoff
원문 | is pretty inconsistent...
원문 | Play at your own risk!"
```

```
번역 | 점쟁이
번역 | "자, 어서 오시오!
번역 | 내 교환기는 나오는 게
번역 | 들쭉날쭉하다오….
번역 | 각오하고 하시오!"
```

### `0718DC`  155 → 107바이트

```
원문 | PIZZA PLACE
원문 | "Come and eat!
원문 | It seems that the Game Crusader
원문 | has some really rare cards on him.
원문 | But that's neither here or there,
원문 | how about some of my pizza?
```

```
번역 | 피자집
번역 | "와서 드시오!
번역 | 게임의 성전사가
번역 | 엄청 귀한 카드를 갖고 있다더군.
번역 | 뭐, 그건 그렇고,
번역 | 피자 한 조각 어떻소?"
```

### `0718E0`  76 → 67바이트

```
원문 | YAGYU
원문 | "Call me Yagyu...
원문 | Used to be a company man...
원문 | But now I'm my own man!"
```

```
번역 | 야규
번역 | "야규라고 부르시오…
번역 | 예전엔 회사원이었지…
번역 | 지금은 자유인이오!"
```

### `0718E4`  108 → 86바이트

```
원문 | YAGYU
원문 | "My name's Yagyu...
원문 | Ah ah ah ah...
원문 | Hey, you fool!
원문 | You won't get away with that!
원문 | What did I do to you?"
```

```
번역 | 야규
번역 | "내 이름은 야규…
번역 | 아 아 아 아…
번역 | 야, 이 녀석!
번역 | 그냥 못 넘어가!
번역 | 내가 뭘 잘못했다고?"
```

### `0718E8`  92 → 85바이트

```
원문 | YAGYU
원문 | "My name's Yagyu...
원문 | Don't tell my wife I lost my job.
원문 | She'd slice me like a blowfish!"
```

```
번역 | 야규
번역 | "내 이름은 야규…
번역 | 아내한테 실직한 거 말하지 마시오.
번역 | 복어처럼 회를 떠 버릴 거요!"
```

### `0718EC`  106 → 75바이트

```
원문 | YAGYU
원문 | "My name's Yagyu...
원문 | Thanks to the economy,
원문 | I'm hanging around here...
원문 | Know where I'm coming from?"
원문 | {0D}
```

```
번역 | 야규
번역 | "내 이름은 야규…
번역 | 경기가 이래서
번역 | 여기 죽치고 있소….
번역 | 내 심정 알겠소?"
번역 | {0D}
```

### `0718F0`  78 → 64바이트

```
원문 | YAGYU
원문 | "What do you know about me?
원문 | Huh?
원문 | You don't know jack!
원문 | Aaah, boo hoo...."
```

```
번역 | 야규
번역 | "나에 대해 뭘 안다고?
번역 | 어?
번역 | 아무것도 모르면서!
번역 | 으아, 흑흑…."
```

### `0718F4`  60 → 47바이트

```
원문 | YAGYU
원문 | "Yeah, you can't understand...
원문 | Those were the days..."
```

```
번역 | 야규
번역 | "그래, 이해 못 하겠지…
번역 | 그때가 좋았는데…"
```

### `0718F8`  306 → 254바이트

```
원문 | YAGYU
원문 | "My name's Yagyu...
원문 | Thanks to the economy,
원문 | I'm hanging around here...
원문 | By the way, I got this card
원문 | from my friend Tam, but...
원문 | getting it for free ticks me off.
원문 | 
원문 | Do you have a 'JUBEI' card?
원문 | He's really cool, isn't he?
원문 | If you do, I'll trade you for this
원문 | 'CURSE' card? How about it?
원문 | TRADE "JUBEI" CARD?
원문 | {0D}
```

```
번역 | 야규
번역 | "내 이름은 야규…
번역 | 경기가 이래서
번역 | 여기 죽치고 있소….
번역 | 그건 그렇고, 친구 탐한테서
번역 | 이 카드를 받았는데…
번역 | 공짜로 받으니 영 찜찜하구먼.
번역 | 
번역 | "주베이" 카드 있소?
번역 | 그 친구 정말 멋지지 않소?
번역 | 있으면 이 "저주" 카드랑
번역 | 바꿔 주겠소. 어떻소?"
번역 | "주베이" 카드를 바꿀까요?
번역 | {0D}
```

### `0718FC`  33 → 25바이트

```
원문 | YAGYU
원문 | "Hey, thanks for the card."
```

```
번역 | 야규
번역 | "어이, 카드 고맙소."
```

### `071900`  66 → 57바이트

```
원문 | YAGYU
원문 | "Now this is a real man!
원문 | Sigh...
원문 | I got to get a new job...."
```

```
번역 | 야규
번역 | "이래야 사내지!
번역 | 하아…
번역 | 새 일자리를 구해야 하는데…."
```

### `071904`  112 → 98바이트

```
원문 | YAGYU
원문 | "Why, you pip-squeak!
원문 | You don't even have
원문 | a 'JUBEI' card on you!
원문 | Liar...Liar...
원문 | I hope YOU get downsized!"
```

```
번역 | 야규
번역 | "이런 애송이 같으니!
번역 | "주베이" 카드도 없으면서!
번역 | 거짓말쟁이… 거짓말쟁이…
번역 | 너도 잘리길 바란다!"
```

### `071908`  78 → 71바이트

```
원문 | YAGYU
원문 | "Oh, really?...
원문 | Whoa! I'm out of time!
원문 | I have an interview!
원문 | Later, kid!"
```

```
번역 | 야규
번역 | "오, 그렇소?…
번역 | 어이쿠! 시간이 없구먼!
번역 | 면접이 있소!
번역 | 또 보세, 꼬마!"
```

### `07190C`  52 → 41바이트

```
원문 | YAGYU
원문 | "You again?...
원문 | What's life all about, huh?..."
```

```
번역 | 야규
번역 | "또 왔소?…
번역 | 인생이란 게 뭘까, 응?…"
```

### `071910`  148 → 123바이트

```
원문 | GIRL
원문 | "Howdy!
원문 | I came here with
원문 | Grandpa, you know...
원문 | But he got lost, it seems.
원문 | He's such a putz!
원문 | I'll look for him myself.
원문 | Don't knock yourself out!"
```

```
번역 | 여자아이
번역 | "안녕하세요!
번역 | 할아버지랑 같이 왔는데요…
번역 | 길을 잃으신 것 같아요.
번역 | 참 딱하죠!
번역 | 제가 직접 찾아볼게요.
번역 | 신경 쓰지 마세요!"
```

### `071918`  30 → 24바이트

```
원문 | ZOMBIE
원문 | "Hid...den...Roooooom!"
```

```
번역 | 좀비
번역 | "숨… 겨진… 바앙!"
```

### `07191C`  23 → 19바이트

```
원문 | ZOMBIE
원문 | "Oooh whooooaa!"
```

```
번역 | 좀비
번역 | "우우 와아아!"
```

### `071920`  43 → 36바이트

```
원문 | ZOMBIE
원문 | "Oooh whoooooaa!...Cough!
원문 | ...Cough!"
```

```
번역 | 좀비
번역 | "우우 와아아아!…콜록!
번역 | …콜록!"
```

### `071924`  61 → 50바이트

```
원문 | ZOMBIE
원문 | "Oooh whooooaaa!
원문 | ...Upstairs...
원문 | ...Card...Trading...."
```

```
번역 | 좀비
번역 | "우우 와아아아아!
번역 | …위층….
번역 | …카드… 교환…."
```

### `071928`  23 → 21바이트

```
원문 | ZOMBIE
원문 | "Oooh whoooaaa!"
```

```
번역 | 좀비
번역 | "우우 와아아아!"
```

### `07192C`  33 → 25바이트

```
원문 | ZOMBIE
원문 | "That...doesn't...hurt..."
```

```
번역 | 좀비
번역 | "그건… 안… 아파…"
```

### `071930`  28 → 24바이트

```
원문 | ZOMBIE
원문 | "It itches...Nice..."
```

```
번역 | 좀비
번역 | "간지러워… 좋아…"
```

### `071934`  60 → 56바이트

```
원문 | ZOMBIE
원문 | "Oooh whoooaa!
원문 | D...Dust Dragon....
원문 | Push...button...."
```

```
번역 | 좀비
번역 | "우우 와아아!
번역 | 더… 더스트 드래곤….
번역 | 버튼… 눌러…."
```

### `071938`  53 → 42바이트

```
원문 | ZOMBIE
원문 | "Ooooh..."
원문 | (THERE'S A BIG HOLE IN HIS
원문 | STOMACH)
```

```
번역 | 좀비
번역 | "우우우…"
번역 | (배에 큰 구멍이 뚫려 있다)
```

### `07193C`  18 → 17바이트

```
원문 | ZOMBIE
원문 | "Whoooo..."
```

```
번역 | 좀비
번역 | "우우우우…"
```

### `071940`  36 → 33바이트

```
원문 | ZOMBIE
원문 | "Ooh...
원문 | ...Oooh whoooaaa!---"
```

```
번역 | 좀비
번역 | "우우…
번역 | …우우 와아아아!---"
```

### `071944`  27 → 26바이트

```
원문 | ZOMBIE
원문 | "H...Hungreeeeee..."
```

```
번역 | 좀비
번역 | "배… 배고파아아아…"
```

### `07194C`  49 → 47바이트

```
원문 | ZOMBIE
원문 | "Gooo Ooooooh!---
원문 | (WAH! IT'S STILL ALIVE!)
```

```
번역 | 좀비
번역 | "구우 우우우우!---
번역 | (으악! 아직 살아 있다!)
```

### `071950`  53 → 47바이트

```
원문 | ZOMBIE
원문 | "Goo Whooooaaaa!!---
원문 | ...Yagyu...
원문 | ...Curse...."
```

```
번역 | 좀비
번역 | "구우 와아아아아!!---
번역 | …야규….
번역 | …저주…."
```

### `07195C`  119 → 107바이트

```
원문 | GIRL
원문 | "What a sweet and delicious
원문 | apple!
원문 | But collecting cards
원문 | is no sweet endeavor. Oh yeah!"
원문 | 
원문 | SEE IF CARD HAS RARITY?
원문 | {0D}
```

```
번역 | 여자아이
번역 | "정말 달고 맛있는
번역 | 사과다!
번역 | 하지만 카드 모으기는
번역 | 그리 달콤하지 않지. 그렇지!"
번역 | 
번역 | 카드 등급을 볼까요?
번역 | {0D}
```

### `071964`  58 → 56바이트

```
원문 | GIRL
원문 | "Sure you understand?
원문 | Don't come crying to me later."
```

```
번역 | 여자아이
번역 | "정말 알아들었어요?
번역 | 나중에 울면서 오지 마세요."
```

### `071968`  75 → 75바이트

```
원문 | GIRL
원문 | "Just like you.
원문 | You've mastered the rules
원문 | like a real CARD CLASH pro!"
```

```
번역 | 여자아이
번역 | "역시 당신답네요.
번역 | 진짜 카드 클래시 고수처럼
번역 | 규칙을 다 익히셨군요!"
```

### `071974`  103 → 109바이트  (빈 곳으로 옮겨 담음)

```
원문 | GIRL
원문 | "Hey there!
원문 | I finally found my grandpa.
원문 | But then he got lost again.
원문 | He's just a hopeless grandpa."
```

```
번역 | 여자아이
번역 | "안녕하세요!
번역 | 드디어 할아버지를 찾았어요.
번역 | 근데 또 길을 잃으셨지 뭐예요.
번역 | 정말 못 말리는 할아버지예요."
```

### `071F40`  176 → 130바이트

```
원문 |   DECK
원문 | 
원문 | The 50 cards used by each player
원문 | in battles are called the "DECK" .
원문 | 
원문 | You can add desired cards to a
원문 | deck, but you can include only 3 of
원문 | a kind of the same card in a it.
```

```
번역 | {20}{20}덱
번역 | 
번역 | 카드 대전에서 쓰는
번역 | 50장의 카드 묶음을
번역 | "덱"이라 한다.
번역 | 
번역 | 원하는 카드를 덱에
번역 | 넣을 수 있지만, 같은
번역 | 카드는 3장까지만 넣을
번역 | 수 있다.
```

### `071F44`  218 → 130바이트

```
원문 |   CHA CARD
원문 | 
원문 | The "CHA CARD" is the card most
원문 | needed for your battle power and
원문 | is  imperative  when  creating
원문 | decks.
원문 | 
원문 | By using a character (CHA card
원문 | put in the Ring) to attack, each
원문 | player can damage the opposing
원문 | player.
```

```
번역 | {20}{20}캐릭터 카드
번역 | 
번역 | 대전에서 가장 중요한
번역 | 카드이며 덱을 짤 때
번역 | 반드시 있어야 한다.
번역 | 
번역 | 링에 낸 캐릭터로
번역 | 공격하면 상대에게
번역 | 피해를 줄 수 있다.
```

### `071F48`  270 → 150바이트

```
원문 |   HAND
원문 | 
원문 | Cards held by each player are
원문 | called the "HAND".
원문 | 
원문 | When starting battles, 5 cards are
원문 | in your hand, and 1 can be
원문 | added later per turn.
원문 | There's no limit for cards in your
원문 | hand so you can keep as many as
원문 | you want.
원문 | 
원문 | Cards labelled "HAND" refer to
원문 | those in your hand.
```

```
번역 | {20}{20}손패
번역 | 
번역 | 각자 손에 든 카드를
번역 | "손패"라 한다.
번역 | 
번역 | 대전을 시작할 때 5장을
번역 | 들고, 턴마다 1장씩
번역 | 더 뽑을 수 있다.
번역 | 
번역 | 손패 장수에는 제한이
번역 | 없어 얼마든지 들 수
번역 | 있다.
```

### `071F4C`  237 → 150바이트

```
원문 |   AC CARD (ACTION CARD)
원문 | 
원문 | The "AC CARD" offers a variety
원문 | of useful assistance.
원문 | 
원문 | Listed on each AC card is the SP
원문 | (called "COST") needed to use
원문 | the card.The card can't be used
원문 | without this SP.
원문 | 
원문 | Any number of AC cards can be
원문 | used in a turn.
```

```
번역 | {20}{20}액션 카드
번역 | 
번역 | 여러 가지로 도움을
번역 | 주는 카드다.
번역 | 
번역 | 카드마다 쓰는 데 드는
번역 | SP("비용")가 적혀
번역 | 있고, 그만큼 SP가
번역 | 없으면 못 쓴다.
번역 | 
번역 | 한 턴에 몇 장이든
번역 | 쓸 수 있다.
```

### `071F50`  257 → 140바이트

```
원문 |   PILE
원문 | 
원문 | Each  shuffled  deck  at  the
원문 | beginning of battles is called the
원문 | "PILE".
원문 | 
원문 | When drawing a card, you must
원문 | always draw from the top of the
원문 | pile.
원문 | You can't look at cards in your
원문 | pile whenever you like.
원문 | 
원문 | Cards labelled "PILE" refer to
원문 | those in your pile.
```

```
번역 | {20}{20}더미
번역 | 
번역 | 대전을 시작할 때 섞어
번역 | 둔 덱을 "더미"라 한다.
번역 | 
번역 | 카드를 뽑을 때는 반드시
번역 | 더미 맨 위에서 뽑는다.
번역 | 
번역 | 더미 안을 마음대로
번역 | 들여다볼 수는 없다.
```

### `071F54`  193 → 128바이트

```
원문 |   ATTACK
원문 | 
원문 | An "ATTACK" is when you use
원문 | your characters to assault and
원문 | damage the enemy.
원문 | 
원문 | Any  number  of  characters can
원문 | attack, but frozen characters or
원문 | those just put in the Ring can't
원문 | attack.
```

```
번역 | {20}{20}공격
번역 | 
번역 | 캐릭터로 상대를 쳐서
번역 | 피해를 주는 것이다.
번역 | 
번역 | 몇 명이든 공격할 수
번역 | 있지만, 얼어 있거나
번역 | 방금 링에 낸 캐릭터는
번역 | 공격하지 못한다.
```

### `071F58`  242 → 142바이트

```
원문 |   DISCARDS
원문 | 
원문 | "DISCARDS" are cards put in the
원문 | used card pile.
원문 | 
원문 | Used AC Cards and KO'ed CHA
원문 | cards are all put here.
원문 | During battles, you can see each
원문 | player's discards using "SEARCH."
원문 | 
원문 | Cards labelled "DISCARD" refer
원문 | to those in your discard pile.
```

```
번역 | {20}{20}버린 패
번역 | 
번역 | 다 쓴 카드를 모아 두는
번역 | 곳이다.
번역 | 
번역 | 쓴 액션 카드와 쓰러진
번역 | 캐릭터가 모두 여기로
번역 | 간다.
번역 | 
번역 | 대전 중에는 "찾기"로
번역 | 서로의 버린 패를 볼 수
번역 | 있다.
```

### `071F5C`  221 → 110바이트

```
원문 |   UNITE ATTACK 1
원문 | 
원문 | The  "UNITE  ATTACK"  is when
원문 | numerous   characters   attack
원문 | together  at  once  and  not
원문 | separately.
원문 | 
원문 | To do UNITE ATTACKS, 5 SPs are
원문 | needed in a DOUBLE UNITE ATTACK
원문 | and 10 SPs for a TRIPLE UNITE
원문 | ATTACK.
```

```
번역 | {20}{20}합체 공격 1
번역 | 
번역 | 여러 캐릭터가 따로
번역 | 치지 않고 한꺼번에
번역 | 치는 것이다.
번역 | 
번역 | 둘이 합치면 SP 5,
번역 | 셋이 합치면 SP 10이
번역 | 든다.
```

### `071F60`  211 → 160바이트

```
원문 |   BP
원문 | 
원문 | "BP" means "Battle Points" and
원문 | show a character's attack power
원문 | and strength.
원문 | 
원문 | If the "BP" falls to zero, that
원문 | character is KO'ed and discarded.
원문 | 
원문 | The maximum "BP" level is 3300
원문 | (9900 during a UNITE ATTACK).
```

```
번역 | {20}{20}BP
번역 | 
번역 | "배틀 포인트"의 줄임말로
번역 | 캐릭터의 공격력과
번역 | 튼튼함을 나타낸다.
번역 | 
번역 | BP가 0이 되면 그
번역 | 캐릭터는 쓰러져 버린
번역 | 패로 간다.
번역 | 
번역 | BP는 최대 3300이다
번역 | (합체 공격 때는 9900).
```

### `071F64`  299 → 153바이트

```
원문 |   UNITE ATTACK 2
원문 | 
원문 | "UNITE  ATTACKS"  offer  the
원문 | benefit  of  "PIERCE  DAMAGE."
원문 | 
원문 | Unlike  single  attacks,  if  the
원문 | total  BP  of  the  attacking
원문 | character  is  higher  than  the
원문 | counterattack character because
원문 | even in a counterattack, only
원문 | this BP difference can be taken
원문 | given as damage to the enemy.
```

```
번역 | {20}{20}합체 공격 2
번역 | 
번역 | 합체 공격에는 "관통
번역 | 피해"가 붙는다.
번역 | 
번역 | 혼자 칠 때와 달리,
번역 | 치는 쪽 BP 합이 막는
번역 | 쪽보다 높으면 그 차이
번역 | 만큼이 상대에게 그대로
번역 | 피해로 들어간다.
```

### `071F68`  197 → 128바이트

```
원문 |   SP
원문 | 
원문 | "SP" means "Soul Points" and
원문 | shows needed enery for using AC
원문 | Cards and Unite Attacks.
원문 | 
원문 | "SP" shows the amount of "SP"
원문 | increase as characters are put in
원문 | the Ring.
원문 | 
원문 | The maximum "SP" value is 99.
```

```
번역 | {20}{20}SP
번역 | 
번역 | "소울 포인트"의 줄임말로
번역 | 액션 카드와 합체 공격에
번역 | 드는 힘을 나타낸다.
번역 | 
번역 | 링에 캐릭터를 낼수록
번역 | SP가 올라간다.
번역 | 
번역 | SP는 최대 99다.
```

### `071F6C`  272 → 177바이트

```
원문 |   COUNTERATTACK
원문 | 
원문 | A "COUNTERATTACK" is when your
원문 | character  counters  an  enemy
원문 | attack.
원문 | 
원문 | But  1  character  can't
원문 | counterattack numerous attackers
원문 | or  numerous  characters  can't
원문 | counterattack repeatedly against
원문 | 1  attacker.
원문 | 
원문 | Also,  frozen  characters  can't
원문 | counterattack.
```

```
번역 | {20}{20}되받아치기
번역 | 
번역 | 상대 공격을 내 캐릭터로
번역 | 맞받는 것이다.
번역 | 
번역 | 다만 한 캐릭터가 여럿을
번역 | 한꺼번에 맞받을 수는
번역 | 없고, 여럿이 한 명을
번역 | 거듭 맞받을 수도 없다.
번역 | 
번역 | 얼어 있는 캐릭터는
번역 | 맞받지 못한다.
```

### `071F70`  195 → 124바이트

```
원문 |   HP
원문 | 
원문 | "HP"  means  "Hit  Points"  and
원문 | shows players' life energy levels.
원문 | 
원문 | "HP" drops when attacked by an
원문 | enemy  character,  and  your
원문 | character loses when it drops to
원문 | zero.
원문 | 
원문 | Maximum "HP" is 9900.
```

```
번역 | {20}{20}HP
번역 | 
번역 | "히트 포인트"의 줄임말로
번역 | 플레이어의 생명력이다.
번역 | 
번역 | 상대 캐릭터에게 맞으면
번역 | HP가 줄고, 0이 되면
번역 | 진다.
번역 | 
번역 | HP는 최대 9900이다.
```

### `071F74`  107 → 76바이트

```
원문 |   RING
원문 | 
원문 | The  field  wherein  characters
원문 | fight is the "RING"
원문 | 
원문 | Each player can put up to 3 cards
원문 | in the Ring.
```

```
번역 | {20}{20}링
번역 | 
번역 | 캐릭터가 싸우는 자리를
번역 | "링"이라 한다.
번역 | 
번역 | 링에는 각자 3장까지
번역 | 낼 수 있다.
```

### `071F78`  156 → 112바이트

```
원문 |   TURN
원문 | 
원문 | A  "TURN"  is  when  a  player
원문 | follows procedures etc to move
원문 | the game along.
원문 | 
원문 | A "BATTLE" is when you and your
원문 | enemy  repeat  turns  until one
원문 | wins.
```

```
번역 | {20}{20}턴
번역 | 
번역 | 한 사람이 차례를 따라
번역 | 게임을 진행하는 것이
번역 | "턴"이다.
번역 | 
번역 | 서로 턴을 주고받아
번역 | 승부가 날 때까지가
번역 | 한 "대전"이다.
```

### `071F7C`  232 → 123바이트

```
원문 |   FREEZE
원문 | 
원문 | "FREEZE" is a condition in which
원문 | characters fall when attacking or
원문 | using a [Ability, leaving them
원문 | unable to act.
원문 | 
원문 | Characters  can  also  slip into
원문 | "FREEZE" Phase with an AC card or
원문 | the power of another character's
원문 | Ability.
```

```
번역 | {20}{20}얼음
번역 | 
번역 | 공격하거나 능력을 쓰면
번역 | 캐릭터가 얼어 아무것도
번역 | 못 하게 된다.
번역 | 
번역 | 액션 카드나 다른
번역 | 캐릭터의 능력으로도
번역 | 얼어붙을 수 있다.
```

### `071F80`  192 → 122바이트

```
원문 |   PHASES
원문 | 
원문 | A "PHASE" refers to each "STEP"
원문 | a battle takes.
원문 | 1  turn  consists  of  4  phases.
원문 | 
원문 | 1. Activate Phase
원문 | 2. Draw Phase
원문 | 3. Main Phase
원문 | 4. Counterattack Phase
원문 | 
원문 | See Phases 1 - 4 for details.
```

```
번역 | {20}{20}단계
번역 | 
번역 | 대전이 밟아 가는 각
번역 | 차례를 "단계"라 한다.
번역 | 
번역 | 한 턴은 네 단계다.
번역 | 
번역 | 1. 풀림 단계
번역 | 2. 뽑기 단계
번역 | 3. 주 단계
번역 | 4. 되받기 단계
```

### `071F84`  269 → 165바이트

```
원문 |   BACK-UP 1
원문 | 
원문 | "BACK-UP"  is  linking  your
원문 | character in the Ring with one in
원문 | your Hand.
원문 | 
원문 | The  character  receiving
원문 | "BACK-UP"  gets  300 extra BP
원문 | regardless  of  the  BACK-UP
원문 | character's BP.
원문 | 
원문 | Note that character combinations
원문 | for  successful  "BACK-UP"  are
원문 | predetermined.
```

```
번역 | {20}{20}백업 1
번역 | 
번역 | 링에 있는 캐릭터에
번역 | 손패의 캐릭터를 덧대는
번역 | 것이다.
번역 | 
번역 | 백업을 받은 캐릭터는
번역 | 덧댄 쪽 BP와 상관없이
번역 | BP가 300 오른다.
번역 | 
번역 | 어떤 짝이 백업이 되는지는
번역 | 미리 정해져 있다.
```

### `071F88`  249 → 159바이트

```
원문 |   PHASE 1
원문 | 
원문 | "ACTIVATE PHASE"
원문 | All characters in your Ring are
원문 | released from Freeze Phase.
원문 | 
원문 | As this phase progresses,
원문 | characters  can attack  and use
원문 | [Abilities again.
원문 | 
원문 | Certain characters may stay in
원문 | Freeze Phase, based on AC cards
원문 | and Ability effects.
```

```
번역 | {20}{20}1단계
번역 | 
번역 | "풀림 단계"
번역 | 
번역 | 링에 있는 내 캐릭터가
번역 | 모두 얼음에서 풀린다.
번역 | 
번역 | 이 단계를 지나면 다시
번역 | 공격하고 능력을 쓸 수
번역 | 있다.
번역 | 
번역 | 액션 카드나 능력에 따라
번역 | 안 풀리기도 한다.
```

### `071F8C`  329 → 229바이트

```
원문 |   BACK-UP 2
원문 | 
원문 | Back-up  can't  be  given  for
원문 | characters  who  just enter the
원문 | Ring and Frozen characters, and
원문 | can't be made more than 2 times
원문 | per turn.
원문 | Characters used for "BACK-UP"
원문 | are not considered to be in the
원문 | Ring.
원문 | If characters getting "BACK-UP"
원문 | are KO'ed or returned to the hand
원문 | or pile,the "BACK-UP" character
원문 | is discarded.
```

```
번역 | {20}{20}백업 2
번역 | 
번역 | 방금 링에 낸 캐릭터와
번역 | 얼어 있는 캐릭터에는
번역 | 백업을 못 하고, 한 턴에
번역 | 두 번까지만 할 수 있다.
번역 | 
번역 | 백업으로 쓴 캐릭터는
번역 | 링에 있는 것으로 치지
번역 | 않는다.
번역 | 
번역 | 백업받은 캐릭터가 쓰러지거나
번역 | 손패나 더미로 돌아가면
번역 | 백업 캐릭터도 버려진다.
```

### `071F90`  214 → 140바이트

```
원문 |   PHASE 2
원문 | 
원문 | "DRAW PHASE"
원문 | A  phase  for  drawing  1  card.
원문 | 
원문 | If there's no card in the pile
원문 | during  this  phase,  you  lose.
원문 | 
원문 | Also, this phase can be skipped
원문 | based on  character's  Abilities
원문 | and card's can't be drawn.
```

```
번역 | {20}{20}2단계
번역 | 
번역 | "뽑기 단계"
번역 | 
번역 | 카드를 1장 뽑는 단계다.
번역 | 
번역 | 이때 더미에 카드가
번역 | 없으면 진다.
번역 | 
번역 | 캐릭터 능력에 따라 이
번역 | 단계를 건너뛰어 카드를
번역 | 못 뽑기도 한다.
```

### `071F94`  193 → 100바이트

```
원문 |   ]ABILITY
원문 | 
원문 | The "]ABILITY" is one that has
원문 | an effect when a character is in
원문 | the Ring (always as is permitted).
원문 | 
원문 | Once the character is put in the
원문 | Ring,  the ]ABILITY's  effect
원문 | cannot be stopped.
```

```
번역 | {20}{20}]능력
번역 | 
번역 | 캐릭터가 링에 있는 동안
번역 | 늘 듣는 능력이다.
번역 | 
번역 | 한번 링에 내고 나면
번역 | ]능력의 효과는 멈출 수
번역 | 없다.
```

### `071F98`  271 → 207바이트

```
원문 |   PHASE 3
원문 | 
원문 | "MAIN PHASE"
원문 | You can do any of the following
원문 | in any order during this phase.
원문 | 
원문 | {FB} Put CHA Card in Ring.(1 only)
원문 | {FB} Use BACK-UP Attack(Once only)
원문 | {FB} Use [Ability
원문 | {FB} Use AC Card
원문 | {FB} Make Attack
원문 | Once the Attack begins, this
원문 | phase ends and the Counterattack
원문 | Phase begins.
```

```
번역 | {20}{20}3단계
번역 | 
번역 | "주 단계"
번역 | 
번역 | 이 단계에서는 아래를
번역 | 아무 차례로나 할 수 있다.
번역 | 
번역 | {FB} 캐릭터 카드 내기(1장)
번역 | {FB} 백업 하기(한 번만)
번역 | {FB} [능력 쓰기
번역 | {FB} 액션 카드 쓰기
번역 | {FB} 공격하기
번역 | 
번역 | 공격을 시작하면 이 단계가
번역 | 끝나고 되받기 단계로 간다.
```

### `071F9C`  213 → 140바이트

```
원문 |   [ABILITY
원문 | 
원문 | A"[ABILITY"is one accompanied
원문 | by  a  Freeze  Phase  when  its
원문 | activated.
원문 | 
원문 | Using  this  ability  disables
원문 | attacks and counterattacks.
원문 | 
원문 | Characters just put in the Ring
원문 | cannot use a [ABILITY in that
원문 | turn.
```

```
번역 | {20}{20}[능력
번역 | 
번역 | 쓰면 캐릭터가 얼어붙는
번역 | 능력이다.
번역 | 
번역 | 이 능력을 쓰면 그 턴에는
번역 | 공격도 되받기도 못 한다.
번역 | 
번역 | 방금 링에 낸 캐릭터는
번역 | 그 턴에 [능력을 못 쓴다.
```

### `071FA0`  172 → 107바이트

```
원문 |   PHASE 4
원문 | 
원문 | "COUNTERATTACK PHASE"
원문 | A  phase  for  deciding  how to
원문 | counterattack  against  the
원문 | attacking  player  (player  in
원문 | stand-by).
원문 | 
원문 | When this phase ends, the turn
원문 | ends.
```

```
번역 | {20}{20}4단계
번역 | 
번역 | "되받기 단계"
번역 | 
번역 | 치고 들어온 쪽에 맞서
번역 | 어떻게 되받을지 정하는
번역 | 단계다.
번역 | 
번역 | 이 단계가 끝나면 턴도
번역 | 끝난다.
```


## 영문으로 둔 것

- **이름 넣기 글자판** — A~Z 격자가 코드에 박혀 있어
  한글 자모가 안 맞습니다. 반만 옮기면 더 어색합니다.
- 게임 로고·`BP`/`SP`/`HP` 같은 그림 글자

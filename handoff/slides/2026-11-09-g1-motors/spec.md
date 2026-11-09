# Slide spec: handoff/slides/2026-11-09-g1-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-09-g1-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana (racer names must be exact: 大峯豊, 深谷知博, 上條暢嵩, 井上忠政, 豊田健士郎, 松井繁, 河合佑樹, 山口剛, 上野真之介, 湯川浩司). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols (CHANGED from the first version, please follow exactly): "G1" is the letter G followed by the half-width digit 1 (NOT a Roman numeral, NOT the letter I). Parentheses "(" ")" are HALF-width ASCII parentheses everywhere (headlines on s2/s3, s4 T12, footnotes). "?" in s4 T3 is a HALF-width ASCII question mark, followed by exactly one half-width space. Every "|" is a half-width ASCII bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot (in s5 T4-T6 it is the first character of the line; do not replace it with a round bullet "•"). "%", "/", ".", "R" and digits are half-width. Half-width spaces appear exactly: between "R" and the boat number in every "10R 1号艇"-style item (e.g. "11R 6号艇"), in s4 T3 after "?" and between "11R" and "6号艇", and inside "BOAT RACE" in the footnotes. No other spaces. "、" and "。" are Japanese punctuation. "※" in s5 T8 is the full-width reference mark.
- Wrapping: headlines on s2/s3/s4, s5 T4-T7 and footnotes may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the rank column in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote (last item) at the bottom in small #9fb3c8.
- Sizes at 1122x1402: s1 title T2/T3 about 90px (each on ONE line, never wrap), s1 T4 about 46px; headline T3 on s2-s5 about 60px (may wrap to two lines on s2/s3/s4); table header about 32px; table race column about 36px; table name and motor columns about 50px; table rank column about 70px digits; s4 T6 about 120px digits, s4 T9 about 160px digits; body text about 42px (s2 T32, s3 T24 also 42px); footnotes about 24px.
- In big numbers, "%" and "位" are about 45% of the digit height, on the same line.

## s1 (cover)
- Base image: handoff/images/2026-11-09-g1/cover.png (night race under floodlights, boat turning around a buoy, dark top area). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium (about 46px), on a dark translucent pill so it reads clearly. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 住之江G1|5日目
- T2: 10〜12Rの18機を
- T3: 機歴で格付け
- T4: 65機中2位・3位が10R・12Rの1号艇
- T5: データで読むボートレース

## s2 (top motors)
- Headline T3 white, large.
- A clean table card with 4 columns. Header row, all small #9fb3c8: T4 (race column), T5 (racer), T6 (motor), T7 (rank, right-aligned).
- 6 data rows with thin divider lines. Each row: race item in #9fb3c8 (small), racer name in white (medium), motor number in white (medium), rank in big yellow (right-aligned).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
- Rows 1 and 2 (ranks 2位 and 3位) get a slightly brighter, warm-tinted row background.
- Under the table: T32 in yellow, medium (about 42px). Footnote T33 at the bottom.
- T1: モーター格付け|住之江G1
- T2: 2/5
- T3: 機歴の上位(65機中16位以内)
- T4: レース
- T5: 選手
- T6: 号機
- T7: 順位
- T8: 10R 1号艇
- T9: 大峯豊
- T10: 80号機
- T11: 2位
- T12: 12R 1号艇
- T13: 深谷知博
- T14: 35号機
- T15: 3位
- T16: 11R 2号艇
- T17: 上條暢嵩
- T18: 11号機
- T19: 5位
- T20: 11R 3号艇
- T21: 井上忠政
- T22: 61号機
- T23: 11位
- T24: 11R 6号艇
- T25: 豊田健士郎
- T26: 52号機
- T27: 14位
- T28: 11R 5号艇
- T29: 松井繁
- T30: 24号機
- T31: 16位
- T32: 11Rに上位機が4機集まった
- T33: BOAT RACE公式の競走成績・番組表(住之江の2026/4/3〜11/8の開催分)を独自に集計。順位は、乗り手のクセを除いた展示タイムの速さで65機を並べたもの

## s3 (lower motors)
- Same table layout and sizes as s2, but 4 data rows, and the rank column numbers in warning red #ff8a8a instead of yellow.
  - Header: T4, T5, T6, T7
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Under the table: T24 white, medium (about 42px). Footnote T25 at the bottom.
- T1: モーター格付け|住之江G1
- T2: 3/5
- T3: 機歴の下位寄り(65機中50位以下)
- T4: レース
- T5: 選手
- T6: 号機
- T7: 順位
- T8: 12R 6号艇
- T9: 河合佑樹
- T10: 28号機
- T11: 51位
- T12: 11R 4号艇
- T13: 山口剛
- T14: 81号機
- T15: 52位
- T16: 10R 4号艇
- T17: 上野真之介
- T18: 14号機
- T19: 53位
- T20: 12R 2号艇
- T21: 湯川浩司
- T22: 77号機
- T23: 55位
- T24: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T25: BOAT RACE公式の競走成績・番組表(住之江の2026/4/3〜11/8の開催分)を独自に集計。順位は、乗り手のクセを除いた展示タイムの速さで65機を並べたもの

## s4 (one motor in focus)
- Headline T3 white, large (may wrap to two lines). Below it T4 in yellow, medium-large (about 52px).
- Two cards side by side, same size.
  - Left card: label T5 white small-medium, then T6 big (about 120px digits, must fit inside the card) in #9fb3c8, then T7 small #9fb3c8 (may wrap).
  - Right card (highlighted, border #FFC400, slightly warm-tinted background): label T8 white small-medium, then T9 huge (about 160px digits) in yellow #FFC400, then T10 small #9fb3c8.
- Under the cards: T11 in yellow, large (about 56px). Then T12 white, small-medium (about 34px). Then T13 small (about 30px) in warning red #ff8a8a. Footnote T14 at the bottom.
- T1: モーター格付け|住之江G1
- T2: 4/5
- T3: 数字以上に出ている? 11R 6号艇
- T4: 豊田健士郎・52号機
- T5: 公式の2連対率
- T6: 32.85%
- T7: 65機の中央値33.58%を下回る
- T8: 展示ベースの機歴
- T9: 14位
- T10: 65機中
- T11: 今節の展示は18人中最速
- T12: レース内中央値より平均0.046秒速い(5走)
- T13: 5走だけなので、数字は大きく振れる
- T14: BOAT RACE公式の競走成績・番組表を独自に集計。公式2連対率は11/9の番組表、機歴は2026/4/3〜11/8、今節の展示は11/5〜11/8の開催分

## s5 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium (about 42px), each may wrap. Each line already starts with "・"; do NOT add any other bullet symbol. Only "2位・3位" in T4, "4機" in T5 and "14位" in T6 are yellow.
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: モーター格付け|住之江G1
- T2: 5/5
- T3: まとめ
- T4: ・65機中2位・3位が10R・12Rの1号艇
- T5: ・11Rは16位以内が4機と、上位機が集まった
- T6: ・豊田健士郎は2連対率は平凡でも、機歴は14位
- T7: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-09-g1-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

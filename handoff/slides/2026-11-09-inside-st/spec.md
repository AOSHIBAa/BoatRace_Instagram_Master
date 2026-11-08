# Slide spec: handoff/slides/2026-11-09-inside-st

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-09-inside-st/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, commas, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: every "|" is a half-width ASCII bar with NO spaces around it. Parentheses "（" "）" in the footnotes are FULL-width Japanese parentheses. "〜" is a Japanese wave dash. "・" is a Japanese middle dot. "ST" is half-width capital letters. "%", "/" (2/5, 4/3, 11/7), "." and digits are half-width. Commas in numbers (5,462 / 1,232 etc.) are half-width. In s1 T4 there is exactly one half-width space after "近畿4場". "、" and "。" are Japanese punctuation.
- Wrapping: long sentences may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote at the bottom in small #9fb3c8.
- Sizes at 1122x1402: headline T3 about 72px; s2 T4 digits about 220px; table numbers (1着率 column) about 80px; レース数 column about 44px; body text about 44px; footnotes about 26px.
- In the big numbers, the "%" sign is about 45% of the digit height, on the same line. Inline "%" inside sentences (s5) is normal text size.

## s1 (cover)
- Base image: handoff/images/2026-11-09/cover.png (night race, three boats exiting a turn, dark sky on top). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: スタート分析|近畿4場
- T2: 1コースの1着率
- T3: STでこう変わる
- T4: 近畿4場 5,462レースを集計
- T5: 近畿4場をデータで読む

## s2 (overall + by venue)
- Headline T3 white, large. Directly under it, one huge yellow number T4 (the largest element on the slide). Then T5 white, medium.
- Below: one card with 4 rows, thin divider lines between rows. Each row: venue name on the left in white (T6, T8, T10, T12), its number on the right, big (about 80px digits), right-aligned, white (T7, T9, T11, T13).
- Footnote T14 at the bottom.
- T1: スタート分析|近畿4場
- T2: 2/5
- T3: 1コースの1着率
- T4: 56.3%
- T5: 場別では尼崎がいちばん高く、三国がいちばん低い
- T6: 尼崎
- T7: 60.2%
- T8: 住之江
- T9: 56.8%
- T10: びわこ
- T11: 55.7%
- T12: 三国
- T13: 52.3%
- T14: BOAT RACE公式の競走成績（2026/4/3〜11/7、場ごとに集計期間が異なる）を独自に集計。6艇の着順とSTがすべて記録された5,462レースが対象

## s3 (by the 1-course boat's own start timing)
- Headline T3 white, large.
- A clean table card with 3 columns. Header row, all small: T4 (left column, white), T5 (middle column, yellow), T6 (right column, #9fb3c8).
- 4 data rows, thin divider lines between rows. Each row: ST label left in white (medium), middle number big and yellow, right number small in #9fb3c8. Numbers right-aligned in their columns.
  - Row 1: T7, T8, T9
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15
  - Row 4: T16, T17, T18
- Under the table: T19 small #9fb3c8. Footnote T20 at the bottom.
- T1: スタート分析|近畿4場
- T2: 3/5
- T3: 1コースのSTごとの1着率
- T4: 1コースのST
- T5: 1着率
- T6: レース数
- T7: 0.10以下
- T8: 70.3%
- T9: 1,232
- T10: 0.11〜0.15
- T11: 63.5%
- T12: 1,741
- T13: 0.16〜0.20
- T14: 52.1%
- T15: 1,398
- T16: 0.21以上
- T17: 34.6%
- T18: 1,091
- T19: STは数字が小さいほど早いスタート
- T20: BOAT RACE公式の競走成績（2026/4/3〜11/7、場ごとに集計期間が異なる）を独自に集計。6艇の着順とSTがすべて記録された5,462レースが対象

## s4 (vs the 2-course boat — the key slide)
- Same table layout as s3 (headline T3, header T4/T5/T6, 4 rows, T19 under the table, footnote T20).
  - Row 1: T7, T8, T9
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15
  - Row 4: T16, T17, T18 — highlight this whole row: its card background slightly red-tinted, label T16 and number T17 in warning red #ff8a8a (T17 big), T18 in #9fb3c8.
- Rows 1-3 middle numbers are yellow as in s3.
- Unlike s3, T19 under the table is white and medium size (about 44px), not small grey.
- T1: スタート分析|近畿4場
- T2: 4/5
- T3: 2コースより遅れると
- T4: 2コースと比べたST
- T5: 1着率
- T6: レース数
- T7: 0.05秒以上速い
- T8: 64.6%
- T9: 1,139
- T10: 0.01〜0.04秒速い
- T11: 62.4%
- T12: 1,818
- T13: 同じ〜0.04秒遅い
- T14: 55.5%
- T15: 1,844
- T16: 0.05秒以上遅い
- T17: 27.8%
- T18: 661
- T19: 0.05秒以上遅れると、1着率は3割を切る
- T20: BOAT RACE公式の競走成績（2026/4/3〜11/7、場ごとに集計期間が異なる）を独自に集計。6艇の着順とSTがすべて記録された5,462レースが対象

## s5 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium-large; only the numbers "56.3%", "70.3%" and "27.8%" in yellow ("34.6%" stays white).
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: スタート分析|近畿4場
- T2: 5/5
- T3: まとめ
- T4: ・1コースの1着率は56.3%
- T5: ・ST0.10以下なら70.3%、0.21以上は34.6%
- T6: ・2コースより0.05秒以上遅いと27.8%
- T7: STはレース後に分かる記録です。予想では、選手の平均STや展示のスタートと合わせて見てください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-09-inside-st/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

# Slide spec: handoff/slides/2026-11-08-exhibition-top

Slides: s1.png ... s4.png (4 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-08-exhibition-top/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 4 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, commas, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: every "|" is a half-width ASCII bar with NO spaces around it. Parentheses "（" "）" in the footnotes are FULL-width Japanese parentheses. "〜" is a Japanese wave dash. "・" is a Japanese middle dot. "？" in s1 T3 is a FULL-width question mark. "%" , "/" (2/4, 4/3, 11/7) and digits are half-width. Commas in numbers (5,462 / 4,795) are half-width. In s1 T4 there is exactly one half-width space after "近畿4場". "、" and "。" are Japanese punctuation.
- Wrapping: long sentences may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s4): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote at the bottom in small #9fb3c8.
- Sizes at 1122x1402: headline T3 about 72px; s2 T4 digits about 220px; table/venue numbers (s2 T7,T9,T11,T13 and s3 middle column) about 80px, s3 right column about 56px; body text about 44px; footnotes about 26px.
- In the big numbers listed above, the "%" sign is about 45% of the digit height, on the same line. Inline "%" inside sentences (s2 T5, s4 T5, T6) is normal text size.

## s1 (cover)
- Base image: handoff/images/2026-11-08/cover.png (night race, boat turning around an orange buoy). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 展示タイム分析|近畿4場
- T2: 展示1位は
- T3: 何%勝つ？
- T4: 近畿4場 5,462レースを集計
- T5: 近畿4場をデータで読む

## s2 (overall rate + by venue)
- Headline T3 white, large. Directly under it, one huge yellow number T4 (the largest element on the slide). Then T5 white, medium.
- Below: one card with 4 rows, thin divider lines between rows. Each row: venue name on the left in white (T6, T8, T10, T12), its number on the right, big, right-aligned, white (T7, T9, T11, T13).
- Footnote T14 at the bottom.
- T1: 展示タイム分析|近畿4場
- T2: 2/4
- T3: 展示1位の1着率
- T4: 27.3%
- T5: 4回に1回ほど。3着以内まで広げると62.6%
- T6: 住之江
- T7: 29.7%
- T8: 尼崎
- T9: 27.9%
- T10: びわこ
- T11: 27.2%
- T12: 三国
- T13: 24.8%
- T14: BOAT RACE公式の競走成績（2026/4/3〜11/7、場ごとに集計期間が異なる）を独自に集計。全艇の着順が確定し、展示1位が1艇だけの4,795レースが対象

## s3 (by course — the key slide)
- Headline T3 white, large.
- A clean table card with 3 columns. Header row: T4 (left column), T5 (middle column, yellow), T6 (right column, #9fb3c8), all small.
- 6 data rows, thin divider lines between rows. Each row: course label left in white, middle number big and yellow, right number medium in #9fb3c8. Numbers right-aligned in their columns.
  - Row 1: left T7, middle T8, right T9
  - Row 2: left T10, middle T11, right T12
  - Row 3: left T13, middle T14, right T15
  - Row 4: left T16, middle T17, right T18
  - Row 5: left T19, middle T20, right T21
  - Row 6: left T22, middle T23, right T24
- Under the table: T25 small #9fb3c8. Footnote T26 at the bottom.
- T1: 展示タイム分析|近畿4場
- T2: 3/4
- T3: コースで大きく変わる
- T4: 進入コース
- T5: 展示1位
- T6: コース全体
- T7: 1コース
- T8: 63.7%
- T9: 56.3%
- T10: 2コース
- T11: 22.3%
- T12: 13.6%
- T13: 3コース
- T14: 20.6%
- T15: 13.4%
- T16: 4コース
- T17: 15.5%
- T18: 9.9%
- T19: 5コース
- T20: 7.8%
- T21: 5.4%
- T22: 6コース
- T23: 3.3%
- T24: 1.4%
- T25: 数字は1着率。コース全体は、同じ期間にそのコースに入った全艇の1着率
- T26: BOAT RACE公式の競走成績（2026/4/3〜11/7、場ごとに集計期間が異なる）を独自に集計。近畿4場の合計

## s4 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium-large; only the numbers "63.7%" and "3.3%" in yellow.
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: 展示タイム分析|近畿4場
- T2: 4/4
- T3: まとめ
- T4: ・展示1位でも、1着は4回に1回ほど
- T5: ・1コースの展示1位は63.7%が1着
- T6: ・6コースは展示1位でも3.3%
- T7: 展示タイムは直線の足が中心の指標で、出足・まわり足は反映されにくいです。展示はコースとセットで見てください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s4.png and report.json in handoff/slides/2026-11-08-exhibition-top/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

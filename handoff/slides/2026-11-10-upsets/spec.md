# Slide spec: handoff/slides/2026-11-10-upsets

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-10-upsets/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, commas, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: every "|" is a half-width ASCII bar with NO spaces around it. "？" in s1 T3 is a FULL-width Japanese question mark. Parentheses "（" "）" (footnotes, s4 T6 and T9) are FULL-width Japanese parentheses. "〜" is a Japanese wave dash. "・" is a Japanese middle dot. "＝" in s2 T8 is a FULL-width equals sign. "%", "/" (2/5, 7/7, 11/7, 11/1), "." and digits are half-width. Commas in numbers (3,392 / 2,440 / 10,000 etc.) are half-width. Exactly one half-width space: after "近畿4場" in s1 T4, after "中央値" in s4 T6 and T9, and the one space inside "BOAT RACE" in the footnotes. "・" also appears in every footnote (払戻金・競走成績). "、" and "。" are Japanese punctuation.
- Wrapping: long sentences may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except table numbers in s3, right-aligned in their columns). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote (last item) at the bottom in small #9fb3c8.
- Sizes at 1122x1402: s1 title T2/T3 about 110px, s1 T4 about 46px; headline T3 about 72px; s5 T4-T6 about 52px; s2 T4 about 220px digits; s3 row 1 T8 about 110px; big hero numbers about 220px digits; table numbers about 80px; body text about 44px; footnotes about 26px.
- In big numbers, "%" and "円" are about 45% of the digit height, on the same line. Inline "%" inside sentences (s5) is normal text size.

## s1 (cover)
- Base image: handoff/images/2026-11-10/cover.png (late-afternoon race, one boat turning around a buoy, dark top area). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 配当分析|近畿4場
- T2: いちばん荒れたのは
- T3: どの場？
- T4: 近畿4場 3,392レースの3連単を集計
- T5: データで読むボートレース

## s2 (overall)
- Headline T3 white, large. Directly under it, one huge yellow number T4 (the largest element on the slide). Then T5 white, medium.
- Below: one card. Inside the card: T6 small #9fb3c8 on top, then T7 big white (about 100px digits).
- Under the card: T8 small white. Footnote T9 at the bottom.
- T1: 配当分析|近畿4場
- T2: 2/5
- T3: 3連単が万舟になった割合
- T4: 16.4%
- T5: 約6レースに1回
- T6: 3連単配当の中央値
- T7: 2,440円
- T8: 万舟＝3連単の払戻が100円につき10,000円以上
- T9: BOAT RACE公式の払戻金・競走成績（2026/7/7〜11/7、尼崎は11/1まで）を独自に集計。3連単の払戻が1通りだけの3,392レースが対象

## s3 (by venue)
- Headline T3 white, large.
- A clean table card with 3 columns. Header row, all small: T4 (left column, white), T5 (middle column, yellow), T6 (right column, #9fb3c8).
- 4 data rows, thin divider lines between rows. Each row: venue name left in white (medium), middle number big and yellow, right number medium in #9fb3c8. Numbers right-aligned in their columns.
  - Row 1: T7, T8, T9 — highlight this row: card background slightly warm-tinted, T8 extra big.
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15
  - Row 4: T16, T17, T18
- Under the table: T19 white, medium (about 44px). Footnote T20 at the bottom.
- T1: 配当分析|近畿4場
- T2: 3/5
- T3: 場別の万舟率
- T4: 場
- T5: 万舟率
- T6: 中央値
- T7: 三国
- T8: 18.8%
- T9: 2,980円
- T10: 住之江
- T11: 16.1%
- T12: 2,340円
- T13: びわこ
- T14: 15.9%
- T15: 2,400円
- T16: 尼崎
- T17: 14.9%
- T18: 2,190円
- T19: いちばん荒れたのは三国、いちばん堅いのは尼崎
- T20: BOAT RACE公式の払戻金・競走成績（2026/7/7〜11/7、尼崎は11/1まで）を独自に集計。3連単の払戻が1通りだけの3,392レースが対象

## s4 (by winning course — the key slide)
- Headline T3 white, large.
- Two cards stacked vertically, same size.
  - Card A: label T4 white medium on top, then T5 huge (about 180px digits) in #9fb3c8, then T6 small #9fb3c8.
  - Card B (highlighted, background slightly red-tinted, border #ff8a8a): label T7 white medium, then T8 huge (about 180px digits) in warning red #ff8a8a, then T9 small #9fb3c8.
- Under the cards: T10 white, medium (about 44px). Footnote T11 at the bottom.
- T1: 配当分析|近畿4場
- T2: 4/5
- T3: 1コースが勝つかどうかで万舟率は大きく変わる
- T4: 1コースが1着のとき
- T5: 3.8%
- T6: 中央値 1,470円（1,881レース）
- T7: 2〜6コースが1着のとき
- T8: 32.1%
- T9: 中央値 5,750円（1,511レース）
- T10: 1コースが負けたレースでは、約3レースに1回が万舟
- T11: BOAT RACE公式の払戻金・競走成績（2026/7/7〜11/7、尼崎は11/1まで）を独自に集計。1着の進入コースで分類

## s5 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium-large; only the numbers "16.4%", "18.8%" and "32.1%" in yellow ("14.9%" stays white).
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: 配当分析|近畿4場
- T2: 5/5
- T3: まとめ
- T4: ・万舟率は近畿4場全体で16.4%
- T5: ・三国18.8%がいちばん高く、尼崎14.9%がいちばん低い
- T6: ・1コースが負けたレースは万舟率32.1%
- T7: 荒れるかどうかは、1コースが勝つかどうかで大きく変わりました。1コースの信頼度とセットで見てください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-10-upsets/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

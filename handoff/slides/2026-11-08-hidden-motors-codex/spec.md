# Slide spec: handoff/slides/2026-11-08-hidden-motors-codex

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 5 seconds on a phone).
Report: write handoff/slides/2026-11-08-hidden-motors-codex/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, commas, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: every "|" is a half-width ASCII bar with NO spaces around it. Parentheses "( )" are half-width. "〜" is a Japanese wave dash. "①②③④" are circled digits. "・" is a Japanese middle dot. Commas in numbers (3,300 / 299,400 / 4,490 / 2,450) are half-width. "%" and "/" (2/5, 7/7, 10/20, 11/4) are half-width. Keep the half-width spaces exactly as written (e.g. s4 T11 "10/20 5R 3連単 299,400円", s3 T7 "びわこ 25号機").
- Wrapping: long sentences may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own line/element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote at the bottom in small #9fb3c8.

## s1 (cover)
- Base image: handoff/images/2026-11-08/cover.png (night race, boat turning around an orange buoy). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge white title on two lines: T2 (white) then T3 (yellow). Below it a short yellow horizontal bar, then subtitle T4 in white, medium. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 機歴分析|近畿4場
- T2: 2連対率に
- T3: だまされるな
- T4: 誰が乗っても展示が速い「隠れ上位モーター」
- T5: 近畿4場をデータで読む

## s2 (method)
- Headline two lines: T3 white; T4 with only "乗った人の腕" in yellow and "も混ざる" in white; large. Then T5 in #9fb3c8, medium. Then one card containing T6, T7, T8, T9 as four lines (circled digits in yellow, text white). Footnote T10.
- T1: 機歴分析|隠れ上位モーター
- T2: 2/5
- T3: 公式の2連対率は
- T4: 乗った人の腕も混ざる
- T5: 強い選手が乗れば上がり、弱い選手が続けば下がる。だから「誰が乗っても展示が速いか」でモーターだけの力を測りました。
- T6: ① 約3,300レースの展示タイムをモーターごとに集計
- T7: ② 毎レース、6艇の真ん中のタイムと比べて何秒速いかを計算
- T8: ③ 選手のクセを補正(その選手が他のモーターで出した展示と比べる)
- T9: ④ 偶然では説明できない差だけを残す
- T10: BOAT RACE公式の競走成績・番組表(2026/7/7〜11/4)を独自に集計。展示タイムはレース内の中央値との差

## s3 (comparison table, the key slide)
- Headline T3 white, large. Then a clean table card with 4 columns: [motor] [T4] [T5] [T6]. Header row T4, T5, T6 in #9fb3c8 small (first header cell empty).
- Row 1: T7 (venue white, "25号機" yellow) | T8 white | T9 yellow, large | T10 white
- Row 2: T11 (venue white, "51号機" yellow) | T12 | T13 yellow, large | T14
- Row 3: T15 (venue white, "55号機" yellow) | T16 | T17 yellow, large | T18
- Thin divider lines between rows. Numbers must be big and right-aligned in their columns.
- Under the table: T19 in #ff8a8a small. Footnote T21.
- T1: 機歴分析|隠れ上位モーター
- T2: 3/5
- T3: 公式は平凡、展示は上位
- T4: 公式2連対率
- T5: 展示(真ん中より)
- T6: 普段より速かった選手
- T7: びわこ 25号機
- T8: 27.6%
- T9: 0.049秒速い
- T10: 8人中8人
- T11: 尼崎 51号機
- T12: 29.1%
- T13: 0.024秒速い
- T14: 13人中10人
- T15: 三国 55号機
- T16: 33.1%
- T17: 0.024秒速い
- T18: 11人中9人
- T19: 公式2連対率の場の中央値 びわこ32.4% 尼崎32.5% 三国33.6%
- T21: BOAT RACE公式の競走成績・番組表(2026/7/7〜11/4)を独自に集計。展示タイムはレース内の中央値との差

## s4 (payouts)
- Headline two lines: T3 white, T4 yellow. Then T5 in #9fb3c8.
- Card A: label T6 (#9fb3c8, no space between venue and number). Two columns: left label T7 with big yellow T8; right label T9 with big white T10. Bottom line T11 small #9fb3c8.
- Card B: label T12. Left T13 with big yellow T14; right T15 with big white T16. Bottom line T17 small #9fb3c8.
- Footnote T18.
- T1: 機歴分析|隠れ上位モーター
- T2: 4/5
- T3: 配当でも
- T4: 穴をあけていた
- T5: 2連対率が低いので人気になりにくく、その分よくつく。
- T6: 住之江84号機(67走)
- T7: 単勝回収率
- T8: 116%
- T9: 場の平均
- T10: 63%
- T11: 10/20 5R 3連単 299,400円の2着に絡む
- T12: びわこ25号機(73走)
- T13: 単勝回収率
- T14: 96%
- T15: 場の平均
- T16: 68%
- T17: 3着内のときの3連単中央値 4,490円(場2,450円)
- T18: BOAT RACE公式の競走成績(2026/7/7〜11/4)を独自に集計。単勝回収率は毎回100円買った場合。1着回数が少ないため、数字は大きく振れます

## s5 (summary)
- Headline T3 white, large. Then list T4-T7, one per line, white; ONLY the motor numbers ("25号機","51号機","47号機","55号機","84号機") in yellow; venue names, "(公式...)" and "・" stay white.
- Card with T8 in white, medium. Bottom T9 small #9fb3c8.
- T1: 機歴分析|隠れ上位モーター
- T2: 5/5
- T3: まとめ
- T4: ・びわこ 25号機(公式27.6%)
- T5: ・尼崎 51号機(公式29.1%)・47号機(公式29.5%)
- T6: ・三国 55号機(公式33.1%)
- T7: ・住之江 84号機(公式32.0%、乗った8人全員が普段より速い)
- T8: 展示タイムは直線の足が中心の指標です。出足・まわり足は別に見てください。出走表でこの番号を見たら、展示をチェック。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-08-hidden-motors-codex/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

# Slide spec: handoff/slides/2026-11-18-biwako-hidden-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-18-biwako-hidden-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in handoff/slides/2026-11-18-biwako-hidden-motors/expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Racer names must be exact: 中亮太 (three characters only: 中 + 亮 + 太; NO space), 柳生泰二 (柳 is the willow kanji, 泰 NOT 秦), 山田哲也. Do not add spaces inside names.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses, NO commas inside numbers (write "26260円", never "26,260円") and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot and appears only inside the footnotes s2 T21, s4 T21 and s5 T25 exactly as written; there are NO bullets anywhere. "%", "/", ".", "R" and all digits are half-width. Cells like "2/5" and "9/16" are digit(s), half-width slash, digit(s) with no spaces. Half-width spaces appear ONLY inside "BOAT RACE" in the footnotes and in s5 T7, T10, T13, T16, T19 between the race and boat (e.g. "1R 1号艇": exactly one half-width space after "R"). No other spaces anywhere (e.g. "16走", "37.5%", "25号機", "4位", "11/15の3R" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T26 is the full-width reference mark.
- Wrapping: Any item not listed in this rule as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. These may wrap automatically: s2 T21, s3 T29, s4 T21, s5 T23, s5 T24, s5 T25, s5 T26. s1 T2/T3/T4, all headlines T3 on s2-s5, and all table cells must NOT wrap. Wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8.
- Margins ~7% each side, left-aligned (except the right-aligned columns stated below). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote at the bottom in small #9fb3c8 (about 22px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px (shrink slightly if needed to keep it on one line).

## s1 (cover)
- Base image: handoff/images/2026-11-18/cover.png (one white kyotei boat with a racer in a white suit and white helmet turning next to an orange-and-white buoy, lake and mountains behind, dark overcast sky in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (each on ONE line, never wrap): T2 in white about 66px (shrink if needed to stay on one line), then T3 in yellow about 120px, the biggest text in the series (shrink if needed to stay on one line). Below it a short yellow horizontal bar, then subtitle T4 in white, about 40px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: びわこ5日目|11/18
- T2: 2連対率は平凡でも機歴上位の3機
- T3: 4日間で1着3回
- T4: うち11/15の3Rは3連単26260円の万舟
- T5: データで読むボートレース

## s2 (the three motors)
- Headline T3 (one line).
- A clean table card with 4 columns: rank, motor number, racer, official 2-place rate. Header row (about 28px, #9fb3c8): T4, T5, T6, T7.
- 3 data rows with thin divider lines, evenly spaced and generous height. Rank in yellow #FFC400 about 52px ("位" same size as the digits); motor number white about 46px ("号機" same size as the digits); racer white bold about 50px; 2-place rate white about 52px, right-aligned in its column.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
- Under the table: T20 in yellow #FFC400, about 40px (one line). Footnote T21 at the bottom (may wrap).
- T1: 機歴上位の3機|びわこ
- T2: 2/5
- T3: 展示は速いのに2連対率は中央値以下
- T4: 機歴
- T5: 号機
- T6: 選手
- T7: 公式2連対率
- T8: 4位
- T9: 25号機
- T10: 中亮太
- T11: 28.28%
- T12: 6位
- T13: 17号機
- T14: 柳生泰二
- T15: 31.72%
- T16: 11位
- T17: 58号機
- T18: 山田哲也
- T19: 30.37%
- T20: 62機の中央値は32.645%
- T21: BOAT RACE公式の競走成績・番組表を独自に集計。機歴はびわこの2026/4/8〜11/17の開催分で、乗り手のクセを除いた展示タイムの速さで62機を並べた順位。2連対率は11/18の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算。同じ条件の51号機は今節の出走なし

## s3 (4 days, 16 starts)
- Headline T3 (one line).
- A clean table card with 5 columns: rank, racer, exhibition top-2 count, top-2 finishes, wins. Header row (about 28px, #9fb3c8): T4, T5, T6, T7, T8.
- 3 data rows with thin divider lines, evenly spaced. Rank in yellow #FFC400 about 44px; racer white bold about 44px; the three count columns white about 48px, right-aligned in their columns.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
- A 4th total row separated by a thicker divider and a slightly brighter warm-tinted background: T24 (white, about 40px) spanning the rank and racer columns, then T25, T26, T27 in yellow #FFC400 about 52px in the three count columns.
- Under the table: T28 in white, about 38px (one line). Footnote T29 at the bottom (may wrap).
- T1: 答え合わせ|びわこ
- T2: 3/5
- T3: 3機の11/14〜11/17の16走
- T4: 機歴
- T5: 選手
- T6: 展示1〜2位
- T7: 2連対
- T8: 1着
- T9: 4位
- T10: 中亮太
- T11: 2/5
- T12: 1/5
- T13: 0/5
- T14: 6位
- T15: 柳生泰二
- T16: 4/6
- T17: 3/6
- T18: 1/6
- T19: 11位
- T20: 山田哲也
- T21: 3/5
- T22: 2/5
- T23: 2/5
- T24: 3機の合計
- T25: 9/16
- T26: 6/16
- T27: 3/16
- T28: 展示1〜2位は16走中9回、2連対率は37.5%
- T29: BOAT RACE公式の競走成績を独自に集計。びわこの11/14〜11/17。数字は回数/走数。展示1〜2位は各レース内の展示タイム順で、同タイムは上位扱い。進入はすべて枠どおり

## s4 (the three wins)
- Headline T3 (one line).
- A table card with 4 columns: race, racer, boat, trifecta payout. Header row (about 28px, #9fb3c8): T4, T5, T6, T7.
- 3 data rows with thin divider lines, evenly spaced and generous height. Race white about 40px; racer white bold about 46px; boat white about 40px; payout about 54px, right-aligned in its column.
  - Row 1: T8, T9, T10, T11 — this row gets a warm-tinted row background and T11 is yellow #FFC400.
  - Row 2: T12, T13, T14, T15 — T15 white.
  - Row 3: T16, T17, T18, T19 — T19 white.
- Under the table: T20 in yellow #FFC400, about 38px (one line). Footnote T21 at the bottom (may wrap).
- T1: 1着の3走|びわこ
- T2: 4/5
- T3: 1着3回のうち1回は万舟
- T4: レース
- T5: 選手
- T6: 枠
- T7: 3連単
- T8: 11/15の3R
- T9: 山田哲也
- T10: 5号艇
- T11: 26260円
- T12: 11/16の12R
- T13: 山田哲也
- T14: 2号艇
- T15: 8750円
- T16: 11/17の3R
- T17: 柳生泰二
- T18: 1号艇
- T19: 1480円
- T20: 11/15の3Rは展示4位から1着、単勝1580円
- T21: BOAT RACE公式の競走成績・払戻金を独自に集計。びわこの11/14〜11/17。払戻金は100円あたり。万舟は3連単1万円以上。1着3回だけの結果は大きく振れます

## s5 (today's races and summary)
- Headline T3 (one line).
- A table card with 3 columns: race and boat, racer, rank. Header row (about 28px, #9fb3c8): T4, T5, T6.
- 5 data rows with thin divider lines, evenly spaced. Race-and-boat white about 40px; racer white bold about 44px; rank yellow #FFC400 about 44px, right-aligned ("位" same size as the digits). Rows 1 and 2 (both 1R) get a slightly brighter warm-tinted row background.
  - Row 1: T7, T8, T9
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15
  - Row 4: T16, T17, T18
  - Row 5: T19, T20, T21
- Below the table, a card with a thin yellow border: small yellow title T22 (about 30px), then T23 in white about 34px (may wrap).
- Below the card: T24 in white, about 26px (may wrap). Then T25 in small #9fb3c8 (about 22px, may wrap). At the very bottom T26 in small #9fb3c8 (about 22px, may wrap).
- T1: 今日の出番|びわこ
- T2: 5/5
- T3: 今日11/18の出番
- T4: レースと枠
- T5: 選手
- T6: 機歴
- T7: 1R 1号艇
- T8: 山田哲也
- T9: 11位
- T10: 1R 6号艇
- T11: 中亮太
- T12: 4位
- T13: 5R 4号艇
- T14: 山田哲也
- T15: 11位
- T16: 7R 2号艇
- T17: 中亮太
- T18: 4位
- T19: 10R 3号艇
- T20: 柳生泰二
- T21: 6位
- T22: まとめ
- T23: 3機は4日間16走で2連対6回。今日の1Rには2機が出走します。
- T24: 展示タイムは直線寄りの指標で、まわり足は反映されにくく、着順は乗り手や枠にも左右されます。4日間だけの結果は大きく振れます。
- T25: BOAT RACE公式の競走成績・番組表を独自に集計。11/18のびわこ。機歴はびわこの2026/4/8〜11/17の開催分・62機中の順位
- T26: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-18-biwako-hidden-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

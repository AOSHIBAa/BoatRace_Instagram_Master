# Slide spec: handoff/slides/2026-11-13-mikuni-hidden-motors

Slides: s1.png ... s5.png (5 slides). Format: POST (carousel; tables are read at the viewer's own pace, but keep them clean and very legible on a phone).
Report: write handoff/slides/2026-11-13-mikuni-hidden-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 宮嵜隆太郎 (嵜 not 崎), 梶山涼斗, 外崎悟, 板倉敦史, 枝尾賢, 樋口喜彦. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot (in s5 T4-T7 it is the first character of the line; do not replace it with a round bullet "•"). "%", "/", ".", "R" and digits are half-width. The only half-width space is inside "BOAT RACE" in footnotes. No other spaces anywhere. "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: s3 T16-T18, s4 T48, s5 T4-T9 and all footnotes may wrap automatically; wrapping must never add, remove or change characters. Headlines (T3), s1 T2/T3/T4 and all table cells must NOT wrap. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 is about 24px).
- Headline T3 on s2-s5: white, about 56px, ONE line.
- In the big numbers of s3 (T9-T15), "%" is about 45% of the digit height, on the same line. In s2 rate cells, "%" is normal size.

## s1 (cover)
- Base image: handoff/images/2026-11-13/cover.png (one white kyotei boat with a racer in a yellow suit and white helmet, running on calm water at sunset with city buildings behind, dark sky in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 92px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 44px, on a dark translucent pill so it reads clearly. Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 三国|4日目
- T2: 2連対率は平凡でも
- T3: 展示が速い7機
- T4: 今節29走で2連対12回
- T5: データで読むボートレース

## s2 (the 7 motors)
- Headline T3.
- A table card with 4 columns: motor, rank, official 2-place rate, this series. Header row small #9fb3c8 (about 28px): T4, T5, T6, T7.
- 7 data rows with thin divider lines, evenly spaced. Motor cell white bold about 40px. Rank cell yellow #FFC400 about 40px. Rate cell white about 36px. Series cell white about 32px. In the 66号機 row (T28-T31) the series cell T31 is #9fb3c8.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
  - Row 7: T32, T33, T34, T35
- Under the table: T36 in yellow, about 36px, one line if possible. Footnote T37 at the bottom.
- T1: 隠れ上位モーター|三国
- T2: 2/5
- T3: 節前の機歴で選んだ7機
- T4: 号機
- T5: 機歴
- T6: 2連対率
- T7: 今節3日間
- T8: 55号機
- T9: 3位
- T10: 32.50%
- T11: 4走・2連対1回
- T12: 48号機
- T13: 7位
- T14: 32.14%
- T15: 5走・2連対3回
- T16: 53号機
- T17: 13位
- T18: 33.94%
- T19: 5走・2連対3回
- T20: 15号機
- T21: 15位
- T22: 28.07%
- T23: 4走・2連対1回
- T24: 63号機
- T25: 21位
- T26: 32.69%
- T27: 6走・2連対2回
- T28: 66号機
- T29: 22位
- T30: 30.32%
- T31: 今節は出走なし
- T32: 69号機
- T33: 23位
- T34: 30.77%
- T35: 5走・2連対2回
- T36: 2連対率はどれも60機の中央値33.945%以下
- T37: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は三国の2026/4/5〜11/7の開催分で、乗り手のクセを除いた展示タイムの速さで60機を並べた順位。公式2連対率は番組表の値で、66号機は11/7、ほかの6機は11/10時点。今節は11/10〜11/12

## s3 (comparison)
- Headline T3.
- A clean table card with 4 columns: label column (wide), then three number columns. Header row small #9fb3c8 (about 28px): T4, T5, T6, T7.
- Row 1 (highlighted: warm-tinted row background, numbers in yellow #FFC400): T8 (white, about 38px), T9, T10, T11 (about 72px digits).
- Row 2 (normal): T12 (#9fb3c8, about 34px), T13, T14, T15 (white, about 60px digits).
- Under the table: T16 in yellow, about 42px. Then T17 white, about 34px. Then T18 in warning red #ff8a8a, about 32px. Footnote T19 at the bottom.
- T1: 隠れ上位モーター|三国
- T2: 3/5
- T3: 今節3日間をほかの機と比べる
- T4: 区分
- T5: 1着率
- T6: 2連対率
- T7: 3着以内率
- T8: 7機・29走
- T9: 17.2%
- T10: 41.4%
- T11: 58.6%
- T12: ほかの機・187走
- T13: 16.6%
- T14: 32.1%
- T15: 48.7%
- T16: 2連対率は9.3ポイント上、1着率はほぼ同じ
- T17: 1コースからの出走は29走中6走
- T18: 3日間・29走だけの結果で、数字は大きく振れる
- T19: BOAT RACE公式の競走成績を独自に集計。三国11/10〜11/12の全36レース。ほかの機の187走には完走しなかった1走を含み、2連対・3着以内に数えない

## s4 (today's entries)
- Headline T3.
- A table card with 4 columns: race, boat, racer, motor. Header row small #9fb3c8 (about 26px): T4, T5, T6, T7.
- 10 data rows with thin divider lines, evenly spaced, compact. Race cell yellow #FFC400 about 34px. Boat cell white about 32px. Racer cell white bold about 36px. Motor cell #9fb3c8 about 32px. Put a slightly thicker divider between different races (between rows 2/3, 4/5, 5/6, 6/7, 8/9).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
  - Row 7: T32, T33, T34, T35
  - Row 8: T36, T37, T38, T39
  - Row 9: T40, T41, T42, T43
  - Row 10: T44, T45, T46, T47
- Under the table: T48 in yellow, about 36px. Footnote T49 at the bottom.
- T1: 隠れ上位モーター|三国
- T2: 4/5
- T3: 今日は6レースに延べ10走
- T4: レース
- T5: 艇
- T6: 選手
- T7: 号機
- T8: 1R
- T9: 2号艇
- T10: 宮嵜隆太郎
- T11: 55号機
- T12: 1R
- T13: 5号艇
- T14: 梶山涼斗
- T15: 15号機
- T16: 2R
- T17: 2号艇
- T18: 外崎悟
- T19: 63号機
- T20: 2R
- T21: 3号艇
- T22: 板倉敦史
- T23: 69号機
- T24: 6R
- T25: 5号艇
- T26: 枝尾賢
- T27: 48号機
- T28: 8R
- T29: 2号艇
- T30: 梶山涼斗
- T31: 15号機
- T32: 9R
- T33: 2号艇
- T34: 樋口喜彦
- T35: 53号機
- T36: 9R
- T37: 5号艇
- T38: 宮嵜隆太郎
- T39: 55号機
- T40: 11R
- T41: 2号艇
- T42: 枝尾賢
- T43: 48号機
- T44: 11R
- T45: 4号艇
- T46: 外崎悟
- T47: 63号機
- T48: 1R・2R・9R・11Rは2機が同じレースに出走
- T49: BOAT RACE公式の番組表を独自に集計。三国11/13の出走表。号機は2/5の7機

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four bullet lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written.
- Below the card: T8 in #9fb3c8, about 30px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: 隠れ上位モーター|三国
- T2: 5/5
- T3: まとめ
- T4: ・節前の機歴で選んだ7機は、今節29走で2連対12回
- T5: ・今節の2連対率41.4%で、ほかの機の32.1%より高い
- T6: ・1着率は17.2%と16.6%でほぼ同じ
- T7: ・今日は1R・2R・9R・11Rに2機ずつ
- T8: 展示タイムは直線寄りの指標で、まわり足は反映されにくい点にご注意ください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only the slide PNGs and report.json, then `git pull --rebase origin main` and `git push origin HEAD:main`.

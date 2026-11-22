# Slide spec: handoff/slides/2026-11-22-mikuni-3r-top10

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-22-mikuni-3r-top10/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 真庭明志, 後藤盛也, 柳沢一 (沢 not 澤; three characters only), 川崎誠志, 藤原孝斗, 松田祐季 (祐 not 佑). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "・" is the small Japanese middle dot: it appears inside s1 T4, s2 T32, s5 T4 and s5 T7 (between numbers), inside the footnotes s2 T34 (once), s3 T25 (twice) and s4 T38 (once), and is ALSO the first character of each line s5 T4-T7 (draw it as "・", never as a round bullet "•", and do not add any other bullet). "%", "/", ".", "R" and digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes and inside the s4 race cells such as "1R 1号艇" (exactly one half-width space between "R" and the boat number). No other spaces anywhere (e.g. "48号機", "34.51%", "23990円", "1号艇" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T34, s3 T25, s4 T38; s2 T33; s4 T37; s5 T4-T9. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the rank / result column in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px. Table header row about 30px in #9fb3c8. Table cells: racer name white bold about 46px, motor white about 42px, lane / race column about 38px, rank / result column about 60px digits. In ranks and results, "位" and "着" are about 45% of the digit height, on the same line (also in the s4 exhibition column). Per-slide sizes below override these defaults.

## s1 (cover)
- Base image: handoff/images/2026-11-22/cover.png (three white open-cockpit kyotei boats with racers in yellow, red and blue suits exiting a turn in choppy grey water, big white spray, an orange-and-white turn buoy on the right, a breakwater, and a dark stormy sky filling the top half). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 90px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 38px, on a dark translucent pill so it reads clearly (one line; shrink slightly if needed). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 三国2日目|11/22
- T2: 今日の3Rは
- T3: 機歴トップ10が4機
- T4: 60機中2位・3位・7位・10位が同じレースに
- T5: データで読むボートレース

## s2 (3R lineup)
- Headline T3 (one line, keep it big).
- Table card with 4 columns: lane (white, about 38px), racer, motor, rank (right-aligned). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 6 data rows with thin divider lines, evenly spaced and generous height. Rank color: 7位, 2位, 3位 and 10位 in yellow #FFC400; 41位 and 17位 in white. Rows 1, 2, 3 and 6 get a slightly brighter, warm-tinted row background.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
- Under the table: T32 in yellow, about 42px (one line). Then T33 in warning red #ff8a8a, about 30px (may wrap). Footnote T34 at the bottom (may wrap).
- T1: モーター格付け|三国
- T2: 2/5
- T3: 3Rは機歴10位以内が4機
- T4: 枠
- T5: 選手
- T6: 号機
- T7: 機歴
- T8: 1号艇
- T9: 真庭明志
- T10: 48号機
- T11: 7位
- T12: 2号艇
- T13: 後藤盛也
- T14: 45号機
- T15: 2位
- T16: 3号艇
- T17: 柳沢一
- T18: 55号機
- T19: 3位
- T20: 4号艇
- T21: 川崎誠志
- T22: 65号機
- T23: 41位
- T24: 5号艇
- T25: 藤原孝斗
- T26: 63号機
- T27: 17位
- T28: 6号艇
- T29: 松田祐季
- T30: 43号機
- T31: 10位
- T32: 10位以内の4機は1・2・3・6号艇
- T33: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T34: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は三国の2026/4/5〜11/21の開催分で、乗り手のクセを除いた展示タイムの速さで60機を並べた順位。出走は11/22の番組表

## s3 (rank vs official 2-ren rate)
- Headline T3 (one line).
- Table card with 4 columns: rank (yellow, about 60px digits, LEFT-aligned as the first column), motor (white), racer (white bold), official 2-ren rate (the ONLY right-aligned column on this slide, about 52px digits; "%" about 45% of digit height). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 4 data rows with thin divider lines, evenly spaced and generous height. The rate cells T15 and T19 (32.74% and 33.33%) are in warning red #ff8a8a; T11 and T23 are white. Rows 2 and 3 get a slightly brighter, warm-tinted row background.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Under the table: T24 in white, about 40px (one line), with only "34.51%" in yellow. Footnote T25 at the bottom (may wrap).
- T1: モーター格付け|三国
- T2: 3/5
- T3: 4機のうち2機は2連対率が中央値未満
- T4: 機歴
- T5: 号機
- T6: 選手
- T7: 公式2連対率
- T8: 2位
- T9: 45号機
- T10: 後藤盛也
- T11: 35.26%
- T12: 3位
- T13: 55号機
- T14: 柳沢一
- T15: 32.74%
- T16: 7位
- T17: 48号機
- T18: 真庭明志
- T19: 33.33%
- T20: 10位
- T21: 43号機
- T22: 松田祐季
- T23: 44.19%
- T24: 60機の中央値は34.51%
- T25: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は三国の2026/4/5〜11/21の開催分・60機中の順位。2連対率は11/22の番組表の値で、中央値は60機それぞれの最新の番組表の値から計算

## s4 (day 1 results of the 4 motors)
- Headline T3 (one line).
- Table card with 4 columns: race and lane (about 38px, white), racer (white bold), exhibition rank in race (about 40px), result (right-aligned, about 56px digits). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 7 data rows with thin divider lines, evenly spaced. Result color: the two "1着" cells (T11 and T19) in yellow #FFC400; all other results white, and "記録なし" (T31) in #9fb3c8 at about 32px. Row 3 (2R) gets a slightly brighter, warm-tinted row background.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
  - Row 7: T32, T33, T34, T35
- Under the table: T36 in yellow, about 38px (one line). Then T37 in warning red #ff8a8a, about 28px (may wrap). Footnote T38 at the bottom (may wrap).
- T1: 初日の答え合わせ|三国
- T2: 4/5
- T3: 4機の初日11/21は7走で1着2回
- T4: レース
- T5: 選手
- T6: 展示順位
- T7: 着順
- T8: 1R 1号艇
- T9: 松田祐季
- T10: 2位
- T11: 1着
- T12: 1R 4号艇
- T13: 真庭明志
- T14: 1位
- T15: 5着
- T16: 2R 5号艇
- T17: 後藤盛也
- T18: 2位
- T19: 1着
- T20: 6R 6号艇
- T21: 柳沢一
- T22: 4位
- T23: 2着
- T24: 8R 5号艇
- T25: 真庭明志
- T26: 6位
- T27: 6着
- T28: 10R 1号艇
- T29: 後藤盛也
- T30: 2位
- T31: 記録なし
- T32: 12R 4号艇
- T33: 松田祐季
- T34: 2位
- T35: 5着
- T36: 2Rは5号艇から1着、3連単23990円
- T37: 1日7走だけの結果で、数字は大きく振れる
- T38: BOAT RACE公式の競走成績・払戻金を独自に集計。三国11/21。展示は各レース内の展示タイムの順位で、同タイムは上位扱い。払戻金は100円あたり。記録なしは競走成績に着順が載っていないもの

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "4機" in T4, "中央値未満" in T5, "1着2回" in T6, "9R・10R・11R" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 34px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: モーター格付け|三国
- T2: 5/5
- T3: まとめ
- T4: ・今日の3Rは機歴10位以内の4機が1・2・3・6号艇
- T5: ・3位の55号機と7位の48号機は2連対率が中央値未満
- T6: ・4機は初日7走で1着2回、2Rは3連単23990円
- T7: ・9R・10R・11Rにも4機のうち1機ずつ出走
- T8: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-22-mikuni-3r-top10/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

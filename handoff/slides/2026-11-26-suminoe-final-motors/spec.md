# Slide spec: handoff/slides/2026-11-26-suminoe-final-motors

Slides: s1.png ... s4.png (4 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-26-suminoe-final-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 4 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 竹井貴史, 坂口周 (three characters only), 清水敦揮 (敦 not 惇; 揮 not 輝), 澁川夏 (澁 is the old form, NOT 渋; three characters only), 島田賢人, 原田篤志. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses, NO question marks and NO bullet symbols (no "・", no "•") anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it (T1 of every slide). "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "/" (in dates and in the s3 table cells such as "9/9"), "%", ".", "R", the letters of "BOAT RACE" and all digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "35号機", "1号艇", "9走で1着7回", "34.29%" have no spaces). "、" and "。" are Japanese punctuation. "※" in s4 T9 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T40 and s3 T41; s2 T39; s4 T4-T9. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone. Use the SAME bold gothic weight on all 4 slides.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the numeric columns in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s4): small yellow label T1 top-left (about 30px) on a slim yellow-outlined pill, page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s4 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s4 white, about 56px. Table header row about 30px in #9fb3c8. Table cells: lane column about 36px white, racer name white bold about 42px, motor white about 38px, rank and count columns about 46px. In "位" cells the unit "位" is about 45% of the digit height, on the same line; in "%" cells the "%" is about 60% of the digit height. Per-slide sizes below override these defaults.

## s1 (cover)
- Base image: handoff/images/2026-11-26/cover.png (one white open-cockpit kyotei boat with a racer in a white suit and white helmet, banking around an orange-and-white cylindrical turn buoy on the right, big white spray on the left, a grey lake with dark mountains, and a heavy overcast dark-grey sky filling the top half). Use it as the photo background; keep the same boat, buoy and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 92px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 38px, on a dark translucent pill so it reads clearly (one line; shrink slightly if needed). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 住之江最終日|11/26
- T2: 優勝戦の6機を
- T3: 機歴で格付け
- T4: 1号艇の35号機は今節9走で1着7回
- T5: データで読むボートレース

## s2 (the 6 final motors)
- Headline T3 (one line, keep it big).
- Table card with 5 columns: lane, racer (white bold), motor (white), rank (right-aligned), win-rate (white, right-aligned). Header row T4, T5, T6, T7, T8 is all in #9fb3c8.
- 6 data rows with thin divider lines, evenly spaced and generous height. Rank colors: "3位" (T12) and "11位" (T27) in yellow #FFC400; "50位" (T32) and "49位" (T37) in warning red #ff8a8a; "15位" and "21位" white. The win-rate "19.08%" (T28) is in warning red #ff8a8a; the other rates white. Row 4 (T24-T28) gets a slightly brighter, warm-tinted row background.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
  - Row 6: T34, T35, T36, T37, T38
- Under the table: T39 in yellow #FFC400, about 36px (may wrap to two lines). Footnote T40 at the bottom (may wrap).
- T1: 優勝戦|住之江
- T2: 2/4
- T3: 6機の機歴は3位〜50位
- T4: 枠
- T5: 選手
- T6: 号機
- T7: 機歴
- T8: 2連対率
- T9: 1号艇
- T10: 竹井貴史
- T11: 35号機
- T12: 3位
- T13: 34.29%
- T14: 2号艇
- T15: 坂口周
- T16: 74号機
- T17: 15位
- T18: 36.92%
- T19: 3号艇
- T20: 清水敦揮
- T21: 62号機
- T22: 21位
- T23: 31.82%
- T24: 4号艇
- T25: 澁川夏
- T26: 36号機
- T27: 11位
- T28: 19.08%
- T29: 5号艇
- T30: 島田賢人
- T31: 75号機
- T32: 50位
- T33: 34.35%
- T34: 6号艇
- T35: 原田篤志
- T36: 63号機
- T37: 49位
- T38: 24.44%
- T39: 36号機は2連対率が65機中63位でも機歴11位
- T40: BOAT RACE公式の競走成績と番組表を独自に集計。機歴は住之江の2026/4/3〜11/25の開催分で、乗り手のクセを除いた展示タイムの速さで65機を並べた順位。2連対率は11/26の番組表の値で、順位は65機それぞれの最新の番組表の値で比較

## s3 (this series, 11/21-11/25)
- Headline T3 (one line, keep it big).
- Table card with 5 columns: racer (white bold), rank (white, right-aligned), exhibition 1st-2nd count (yellow #FFC400, right-aligned), wins (white, right-aligned), top-2 finishes (white, right-aligned). Header row T4, T5, T6, T7, T8 is all in #9fb3c8.
- Count cells are written as "count/starts" (e.g. "9/9"): draw the whole cell in ONE size, about 48px, all half-width, no spaces. In the rank column (T5 column) the unit "位" is about 45% of the digit height, as on s2.
- 6 data rows with thin divider lines, evenly spaced. Row 1 (T9-T13) gets a slightly brighter, warm-tinted row background.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
  - Row 6: T34, T35, T36, T37, T38
- Under the table: T39 in yellow, about 38px (one line). Then T40 in warning red #ff8a8a, about 30px (one line). Footnote T41 at the bottom (may wrap).
- T1: 今節の成績|住之江
- T2: 3/4
- T3: 6人の今節5日間の成績
- T4: 選手
- T5: 機歴
- T6: 展示1〜2位
- T7: 1着
- T8: 2連対
- T9: 竹井貴史
- T10: 3位
- T11: 9/9
- T12: 7/9
- T13: 8/9
- T14: 坂口周
- T15: 15位
- T16: 1/9
- T17: 3/9
- T18: 8/9
- T19: 清水敦揮
- T20: 21位
- T21: 1/8
- T22: 2/8
- T23: 6/8
- T24: 澁川夏
- T25: 11位
- T26: 5/9
- T27: 2/9
- T28: 6/9
- T29: 島田賢人
- T30: 50位
- T31: 2/9
- T32: 1/9
- T33: 5/9
- T34: 原田篤志
- T35: 49位
- T36: 5/9
- T37: 1/9
- T38: 7/9
- T39: 35号機は9走すべて展示2位以内
- T40: 5日間だけの結果で、数字は大きく振れる
- T41: BOAT RACE公式の競走成績を独自に集計。住之江11/21〜11/25。数字は回数/走数。展示1〜2位は各レース内の展示タイムの順で、同タイムは上位扱い。展示タイムは直線寄りの指標で、まわり足は反映されにくい

## s4 (summary)
- Headline T3 (まとめ).
- One card containing the four lines T4-T7, each in its own row separated by thin divider lines, white, about 40px, generous spacing (each may wrap inside the card). NO bullet symbols before the lines. Only these parts are yellow #FFC400: "3位〜50位" in T4, "1着7回" in T5, "19.08%" and "機歴11位" in T6, "2機" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 32px (may wrap).
- At the bottom, T9 in small #9fb3c8 (about 24px, may wrap).
- T1: まとめ|住之江
- T2: 4/4
- T3: まとめ
- T4: 優勝戦の6機は機歴3位〜50位
- T5: 1号艇の35号機は機歴3位、今節9走で1着7回
- T6: 4号艇の36号機は2連対率19.08%でも機歴11位
- T7: 11/21時点の機歴トップ10のうち2機が優勝戦に
- T8: 着順は乗り手や枠にも左右されます。機歴は材料のひとつとして見てください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s4.png and report.json in handoff/slides/2026-11-26-suminoe-final-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

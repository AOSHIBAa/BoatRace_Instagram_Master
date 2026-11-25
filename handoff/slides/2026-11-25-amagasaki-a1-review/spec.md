# Slide spec: handoff/slides/2026-11-25-amagasaki-a1-review

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-25-amagasaki-a1-review/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 石田章央, 深井利寿, 河村了 (three characters only), 鈴木孝明, 大場恒季, 西野翔太, 宮田龍馬, 板橋侑我 (侑 not 佑), 浜本裕己 (浜 not 濱; 己 not 巳 or 已), 末永祐輝 (祐 not 佑). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it (s1 T1 and T1 of s2-s5). "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "・" is the small Japanese middle dot: it appears inside s2 T5 (once), s2 T9 (three times) and the footnote s4 T40 (once), and is ALSO the first character of each line s5 T4-T7 (draw it as "・", never as a round bullet "•", and do not add any other bullet). "/", "A", "R", the letters of "BOAT RACE" and all digits are half-width. "A1" (in s1 T2 and s2 T12) is a half-width capital letter A followed by the digit one; never render it as "AI", "Al" or "A I". The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "56号機", "1号艇", "36走で1着14回", "12R" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T13, s3 T31, s4 T40; s2 T12; s3 T30; s5 T4-T9. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone. Use the SAME bold gothic weight on all 5 slides.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the numeric columns in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px) on a slim yellow-outlined pill, page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 56px. Table header row about 30px in #9fb3c8. Table cells: racer name white bold about 44px, motor white about 40px, lane column about 38px, rank and count columns about 52px digits. In "位" and "回" cells the unit is about 45% of the digit height, on the same line. Per-slide sizes below override these defaults.

## s1 (cover)
- Base image: handoff/images/2026-11-25/cover.png (kyotei boats on an urban riverside course in late-afternoon sunlight). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 88px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 38px, on a dark translucent pill so it reads clearly (one line; shrink slightly if needed). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 尼崎6日目|11/25
- T2: A1級6人のモーター
- T3: 5日間の答え合わせ
- T4: 機歴50位以下の4機が36走で1着14回
- T5: データで読むボートレース

## s2 (top 2 vs bottom 4, two big cards)
- Headline T3 (one line).
- Two stacked cards of equal size, full width, generous padding.
  - Card A (thin #9fb3c8 border): T4 in #9fb3c8 about 34px; T5 white about 36px; then on one line T6 in white about 64px and, to its right, T7 in white about 44px.
  - Card B (thin yellow border and a slightly warm-tinted background): T8 in yellow about 34px; T9 white about 32px (one line; shrink slightly if needed); then on one line T10 in yellow #FFC400 about 64px and, to its right, T11 in yellow about 44px.
  - In T6 and T10 the digits are big and "走で", "着", "回" are about 50% of the digit height. In T7 and T11 ("2連対10回", "2連対23回") the leading "2" is the same small size as "連対"; only "10" and "23" are big digits.
- Under the cards: T12 in warning red #ff8a8a, about 30px (may wrap). Footnote T13 at the bottom (may wrap).
- T1: 答え合わせ|尼崎
- T2: 2/5
- T3: 機歴の上位と下位、11/20〜11/24
- T4: 機歴10位以内の2機
- T5: 石田章央・深井利寿
- T6: 18走で1着5回
- T7: 2連対10回
- T8: 機歴50位以下の4機
- T9: 河村了・鈴木孝明・大場恒季・西野翔太
- T10: 36走で1着14回
- T11: 2連対23回
- T12: 乗り手は6人ともA1級。5日間だけの結果で、数字は大きく振れる
- T13: BOAT RACE公式の競走成績を独自に集計。尼崎11/20〜11/24。機歴は11/20の投稿時点の順位で、尼崎で2026/4/17〜11/17に開催された分の展示タイムを乗り手のクセを除いて比べ、63機を並べたもの

## s3 (bottom 4 table)
- Headline T3 (one line; it is long, so shrink to fit, about 50px).
- Table card with 5 columns: racer (white bold), motor (white), rank (warning red #ff8a8a, right-aligned), exhibition-1st count (yellow #FFC400, right-aligned), wins (white, right-aligned). Header row T4, T5, T6, T7, T8 is all in #9fb3c8.
- 4 data rows with thin divider lines, evenly spaced and generous height. Rows 2 and 3 (T14-T23) get a slightly brighter, warm-tinted row background.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
- Under the table: T29 in white, about 38px (one line). Then T30 in warning red #ff8a8a, about 28px (may wrap). Footnote T31 at the bottom (may wrap).
- T1: 答え合わせ|尼崎
- T2: 3/5
- T3: 50位以下でも展示1位は36走で13回
- T4: 選手
- T5: 号機
- T6: 機歴
- T7: 展示1位
- T8: 1着
- T9: 河村了
- T10: 6号機
- T11: 50位
- T12: 0回
- T13: 4回
- T14: 鈴木孝明
- T15: 20号機
- T16: 51位
- T17: 5回
- T18: 4回
- T19: 大場恒季
- T20: 60号機
- T21: 55位
- T22: 7回
- T23: 3回
- T24: 西野翔太
- T25: 49号機
- T26: 56位
- T27: 1回
- T28: 3回
- T29: 10位以内の2機は18走で展示1位4回
- T30: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T31: BOAT RACE公式の競走成績を独自に集計。尼崎11/20〜11/24、各9走。展示1位は各レース内で展示タイムが最も速かった回数で、同タイムは上位扱い。機歴は11/20の投稿時点の63機中の順位

## s4 (today's 12R)
- Headline T3 (one line, keep it big).
- Table card with 5 columns: lane (white, about 36px), racer (white bold), motor (white), rank (right-aligned), this-series wins (white, right-aligned). Header row T4, T5, T6, T7, T8 is all in #9fb3c8.
- 6 data rows with thin divider lines, evenly spaced. Rank color: "1位" (T22) and "5位" (T37) in yellow #FFC400; "50位" (T27) in warning red #ff8a8a; the other ranks white. Row 3 (T19-T23) gets a slightly brighter, warm-tinted row background.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
  - Row 6: T34, T35, T36, T37, T38
- Under the table: T39 in yellow, about 38px (one line). Footnote T40 at the bottom (may wrap).
- T1: 今日の12R|尼崎
- T2: 4/5
- T3: 機歴1位の56号機は3号艇
- T4: 枠
- T5: 選手
- T6: 号機
- T7: 機歴
- T8: 今節1着
- T9: 1号艇
- T10: 宮田龍馬
- T11: 16号機
- T12: 18位
- T13: 4回
- T14: 2号艇
- T15: 板橋侑我
- T16: 55号機
- T17: 12位
- T18: 5回
- T19: 3号艇
- T20: 浜本裕己
- T21: 56号機
- T22: 1位
- T23: 2回
- T24: 4号艇
- T25: 河村了
- T26: 6号機
- T27: 50位
- T28: 4回
- T29: 5号艇
- T30: 末永祐輝
- T31: 21号機
- T32: 25位
- T33: 3回
- T34: 6号艇
- T35: 石田章央
- T36: 54号機
- T37: 5位
- T38: 3回
- T39: 1位の56号機は今節8走で2連対2回
- T40: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は尼崎の2026/4/17〜11/24の開催分で、乗り手のクセを除いた展示タイムの速さで63機を並べた順位。今節1着は11/20〜11/24の回数。出走は11/25の番組表

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "1着14回" in T4, "1着5回" in T5, "乗り手や枠" in T6, "56号機" in T7 (T7 is "・今日の12Rは最新の機歴1位、56号機が3号艇"); everything else in those lines is white.
- Below the card: T8 in white, about 34px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: 答え合わせ|尼崎
- T2: 5/5
- T3: まとめ
- T4: ・機歴50位以下の4機は36走で1着14回、2連対23回
- T5: ・機歴10位以内の2機は18走で1着5回、2連対10回
- T6: ・機歴は展示の速さの順位で、着順は乗り手や枠にも左右される
- T7: ・今日の12Rは最新の機歴1位、56号機が3号艇
- T8: 機歴は材料のひとつとして見てください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-25-amagasaki-a1-review/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

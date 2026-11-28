# Slide spec: handoff/slides/2026-11-28-amagasaki-top10-day1

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-28-amagasaki-top10-day1/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 藤岡俊介, 上原健次郎 (five characters, ends with 郎), 吉川元浩, 山下昂大 (昂 not 昴), 秦英悟 (three characters), 夏山亮平, 川島拓郎, 吉田和仁, 川口貴久. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses, NO question marks and NO bullet symbols (no "・", no "•") anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it (T1 of every slide). "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "/" (in dates such as "11/28" and "2026/4/17", in page numbers such as "2/5" and in the s4 table cells such as "10/16"), "%", "R", the letters of "BOAT RACE" and all digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "56号機", "1号艇12号機", "2着、2着", "16走で", "10R" have no spaces). "、" and "。" are Japanese full-width punctuation. "※" in s5 T17 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T27, s3 T28, s4 T19, s5 T16, s5 T17; and s5 T14. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone. Use the SAME bold gothic weight on all 5 slides.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the count columns in the s4 table, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px) on a slim yellow-outlined pill, page number T2 top-right in #9fb3c8 (about 28px), footnote at the bottom in small #9fb3c8 (about 22px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 56px. Table header rows about 30px in #9fb3c8. Per-slide sizes below override these defaults.

## s1 (cover)
- Base image: handoff/images/2026-11-28/cover.png (one white open-cockpit kyotei boat running to the right on golden late-afternoon water, racer in a yellow suit and white full-face helmet, big white spray behind the motor, the whole top half almost black). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo (the boat and the spray) clearly visible and do not put any text over the boat. If that file does not exist, use a plain navy background with no photo.
- Blend the dark top half into navy. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 96px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 40px, on a dark translucent pill (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the water with a subtle shadow.
- T1: 尼崎2日目|11/28
- T2: 機歴トップ10の
- T3: 初日の成績
- T4: 16走で2連対10回、1着5回
- T5: データで読むボートレース

## s2 (rank 1-5)
- Headline T3 (one line).
- Table card with 4 columns: rank (yellow #FFC400, about 50px), motor (white, about 44px), racer (white bold, about 42px), finishes (white, about 42px). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 5 data rows with thin divider lines, evenly spaced (each row about 120px tall).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22 — this row is dimmed: all three items in #9fb3c8, T22 in the racer column; the finishes cell of this row is EMPTY (draw nothing there, no dash).
  - Row 5: T23, T24, T25, T26
- In finishes cells the "着" is about 60% of the digit height; the digits are big.
- Footnote T27 at the bottom (may wrap).
- T1: 機歴トップ10|尼崎
- T2: 2/5
- T3: 機歴1〜5位と初日の着順
- T4: 機歴
- T5: 号機
- T6: 初日の選手
- T7: 初日の着順
- T8: 1位
- T9: 56号機
- T10: 藤岡俊介
- T11: 2着、2着
- T12: 2位
- T13: 23号機
- T14: 上原健次郎
- T15: 1着
- T16: 3位
- T17: 61号機
- T18: 吉川元浩
- T19: 1着、2着
- T20: 4位
- T21: 63号機
- T22: 今節の出走なし
- T23: 5位
- T24: 54号機
- T25: 山下昂大
- T26: 2着、4着
- T27: BOAT RACE公式の競走成績と番組表を独自に集計。機歴は尼崎の2026/4/17〜11/27の開催分で、乗り手のクセを除いた展示タイムの速さを、走数とばらつきも加味して63機で並べた順位。初日は11/27

## s3 (rank 6-10)
- Same layout as s2: headline T3, table card with the same 4 columns and header T4-T7, 5 data rows (each row about 120px tall), all rows normal (none dimmed).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Footnote T28 at the bottom (may wrap).
- T1: 機歴トップ10|尼崎
- T2: 3/5
- T3: 機歴6〜10位と初日の着順
- T4: 機歴
- T5: 号機
- T6: 初日の選手
- T7: 初日の着順
- T8: 6位
- T9: 37号機
- T10: 秦英悟
- T11: 2着、1着
- T12: 7位
- T13: 12号機
- T14: 夏山亮平
- T15: 5着、3着
- T16: 8位
- T17: 4号機
- T18: 川島拓郎
- T19: 3着、6着
- T20: 9位
- T21: 36号機
- T22: 吉田和仁
- T23: 1着
- T24: 10位
- T25: 31号機
- T26: 川口貴久
- T27: 1着、6着
- T28: BOAT RACE公式の競走成績を独自に集計。尼崎11/27。着順はレース番号の順

## s4 (day 1, top 10 vs the rest)
- Headline T3 (one line, keep it big).
- Table card with 4 columns: group label (left), exhibition 1st-2nd, top-2 finishes, wins (the three count columns right-aligned). Header row T4, T5, T6, T7 in #9fb3c8.
- 2 data rows, each about 160px tall, with a thin divider: Row 1 T8, T9, T10, T11 — T8 in yellow #FFC400 bold about 40px, count cells white about 58px, and this row has a slightly brighter warm-tinted background. Row 2 T12, T13, T14, T15 — T12 in white about 40px, count cells white about 58px.
- Count cells are written as "count/starts" (e.g. "10/16"): draw the whole cell in ONE size, all half-width, no spaces.
- Under the table: T16 in yellow about 38px (one line; shrink slightly if needed). Then T17 in white about 32px (one line). Then T18 in warning red #ff8a8a about 30px (one line). Footnote T19 at the bottom (may wrap).
- T1: 初日の71走|尼崎
- T2: 4/5
- T3: 機歴トップ10とそれ以外
- T4: 区分
- T5: 展示1〜2位
- T6: 2連対
- T7: 1着
- T8: トップ10の9機
- T9: 5/16
- T10: 10/16
- T11: 5/16
- T12: それ以外
- T13: 20/55
- T14: 14/55
- T15: 7/55
- T16: 2連対は16走中10回、それ以外は55走中14回
- T17: 初日の展示1〜2位は16走中5回
- T18: 1日だけの結果で、数字は大きく振れる
- T19: BOAT RACE公式の競走成績を独自に集計。尼崎11/27の12R、71走。数字は回数/走数。展示1〜2位は各レース内の展示タイムの順で、同タイムは上位扱い。展示タイムは直線寄りの指標で、まわり足は反映されにくい

## s5 (today's races + summary)
- Headline T3 (one line).
- Three stacked cards, one per race, each about 150px tall. In each card: race label big yellow #FFC400 on the left (about 56px), and to its right two lines: first line white bold about 36px, second line #9fb3c8 about 30px (one line; shrink slightly if needed).
  - Card 1: T4 (race), T5 (first line), T6 (second line)
  - Card 2: T7 (race), T8 (first line), T9 (second line)
  - Card 3: T10 (race), T11 (first line), T12 (second line)
- Below the cards: small yellow heading T13 (about 32px), then T14 in white about 32px (may wrap), then T15 in #9fb3c8 about 26px (one line).
- Footnote T16 in small #9fb3c8 (about 22px, may wrap), and at the very bottom T17 in small #9fb3c8 (about 22px, may wrap).
- T1: 今日の出番|尼崎
- T2: 5/5
- T3: 今日11/28の注目レース
- T4: 4R
- T5: 機歴トップ10が3機
- T6: 1号艇12号機、4号艇36号機、5号艇61号機
- T7: 10R
- T8: 機歴1位と2位
- T9: 3号艇23号機、6号艇56号機
- T10: 3R
- T11: 機歴2位と8位
- T12: 4号艇23号機、5号艇4号機
- T13: まとめ
- T14: 機歴トップ10の9機は初日16走で2連対10回、1着5回。今日は10レースで14回の出番。
- T15: 着順は乗り手や枠、進入にも左右されます。
- T16: BOAT RACE公式の競走成績と番組表を独自に集計。今日の出番は11/28の番組表。全14回の出番はキャプションに掲載
- T17: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-28-amagasaki-top10-day1/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

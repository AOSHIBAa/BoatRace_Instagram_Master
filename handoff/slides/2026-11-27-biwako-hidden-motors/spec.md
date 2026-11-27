# Slide spec: handoff/slides/2026-11-27-biwako-hidden-motors

Slides: s1.png ... s4.png (4 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-27-biwako-hidden-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 4 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 尾形栄治 (栄 not 榮; 治 not 冶), 栗原一馬 (four characters), 服部幸男 (four characters). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses, NO question marks and NO bullet symbols (no "・", no "•") anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it (T1 of every slide). "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "/" (in dates, in "2/4" page numbers and in the s3 table cells such as "5/6"), "%", ".", "R", the letters of "BOAT RACE" and all digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "58号機", "3号艇", "6走で", "32.21%", "1R" have no spaces). "、" and "。" are Japanese punctuation. "※" in s4 T32 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T21, s3 T30, s4 T31; s4 T29, T30, T32. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone. Use the SAME bold gothic weight on all 4 slides.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the numeric columns in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s4): small yellow label T1 top-left (about 30px) on a slim yellow-outlined pill, page number T2 top-right in #9fb3c8 (about 28px), footnote at the bottom in small #9fb3c8 (about 22px).
- Sizes at 1122x1402: headline T3 on s2-s4 white, about 56px. Table header row about 30px in #9fb3c8. In "位" cells the unit "位" is about 45% of the digit height, on the same line; in "%" cells the "%" is about 60% of the digit height. Per-slide sizes below override these defaults.

## s1 (cover)
- Base image: handoff/images/2026-11-27/cover.png (three white open-cockpit kyotei boats in a diagonal line from upper-left to lower-right, racers in blue, black and white suits with full-face helmets, big white spray behind them, a grey lake with dark green mountains, and a heavy dark overcast sky filling the top half). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 92px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 38px, on a dark translucent pill so it reads clearly (one line; shrink slightly if needed). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: びわこ5日目|11/27
- T2: 2連対率は平凡でも
- T3: 機歴上位の3機
- T4: 58号機は今節6走で展示1〜2位5回
- T5: データで読むボートレース

## s2 (the 3 motors)
- Headline T3 (one line; shrink slightly if needed, keep it big).
- Table card with 4 columns: rank (yellow #FFC400, about 52px, right-aligned), motor (white, about 44px), racer (white bold, about 44px), win-rate (white, about 46px, right-aligned). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 3 data rows with thin divider lines, evenly spaced, generous height (each row about 130px tall).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
- Under the table: T20 in #9fb3c8 about 34px, one line, inside a slim outlined box. Footnote T21 at the bottom (may wrap).
- T1: 機歴上位の3機|びわこ
- T2: 2/4
- T3: 展示は速いのに2連対率は中央値以下
- T4: 機歴
- T5: 号機
- T6: 今節の選手
- T7: 2連対率
- T8: 6位
- T9: 25号機
- T10: 尾形栄治
- T11: 27.45%
- T12: 9位
- T13: 58号機
- T14: 栗原一馬
- T15: 30.56%
- T16: 11位
- T17: 51号機
- T18: 服部幸男
- T19: 29.66%
- T20: 62機の中央値は32.21%
- T21: BOAT RACE公式の競走成績と番組表を独自に集計。機歴はびわこの2026/4/8〜11/26の開催分で、乗り手のクセを除いた展示タイムの速さを、走数とばらつきも加味して62機で並べた順位。2連対率は11/27の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算。同じ条件で機歴4位の17号機は今節の出走なし

## s3 (this series, 11/23-11/26)
- Headline T3 (one line, keep it big).
- Table card with 5 columns: motor (white, about 38px), racer (white bold, about 40px), exhibition 1st-2nd count (yellow #FFC400, right-aligned), top-2 finishes (white, right-aligned), wins (white, right-aligned). Header row T4, T5, T6, T7, T8 is all in #9fb3c8.
- Count cells are written as "count/starts" (e.g. "5/6", "10/18"): draw the whole cell in ONE size, about 48px, all half-width, no spaces.
- 3 data rows plus a total row, with thin divider lines, evenly spaced. Row 2 (T14-T18, 58号機) gets a slightly brighter, warm-tinted row background. The total row (T24-T27) is separated by a thicker line; its label T24 is in #9fb3c8 and its count cells are bold.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Total row: T24 (spans the motor and racer columns), T25, T26, T27
- Under the table: T28 in yellow, about 38px (one line; shrink slightly if needed). Then T29 in warning red #ff8a8a, about 30px (one line). Footnote T30 at the bottom (may wrap).
- T1: 今節の成績|びわこ
- T2: 3/4
- T3: 3機の今節18走
- T4: 号機
- T5: 選手
- T6: 展示1〜2位
- T7: 2連対
- T8: 1着
- T9: 25号機
- T10: 尾形栄治
- T11: 3/6
- T12: 0/6
- T13: 0/6
- T14: 58号機
- T15: 栗原一馬
- T16: 5/6
- T17: 3/6
- T18: 1/6
- T19: 51号機
- T20: 服部幸男
- T21: 2/6
- T22: 3/6
- T23: 1/6
- T24: 3機の合計
- T25: 10/18
- T26: 6/18
- T27: 2/18
- T28: 展示1〜2位は18走中10回、2連対は6回
- T29: 4日間だけの結果で、数字は大きく振れる
- T30: BOAT RACE公式の競走成績を独自に集計。びわこ11/23〜11/26。数字は回数/走数。展示1〜2位は各レース内の展示タイムの順で、同タイムは上位扱い。展示タイムは直線寄りの指標で、まわり足は反映されにくい

## s4 (today's races + summary)
- Headline T3 (one line).
- Compact table card with 4 columns: race (white, about 40px), lane (white, about 38px), racer (white bold, about 40px), motor (yellow #FFC400, about 40px). Header row T4, T5, T6, T7 in #9fb3c8 (about 28px). 5 data rows with thin divider lines (each row about 72px tall).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Below the table: small yellow heading T28 (about 32px), then T29 in white about 32px (may wrap; only "11450円" in yellow), then T30 in #9fb3c8 about 26px (may wrap).
- Footnote T31 in small #9fb3c8 (about 22px, may wrap), and at the very bottom T32 in small #9fb3c8 (about 22px, may wrap).
- T1: 今日の出番|びわこ
- T2: 4/4
- T3: 今日11/27の出番
- T4: レース
- T5: 枠
- T6: 選手
- T7: 号機
- T8: 1R
- T9: 3号艇
- T10: 栗原一馬
- T11: 58号機
- T12: 3R
- T13: 2号艇
- T14: 服部幸男
- T15: 51号機
- T16: 5R
- T17: 2号艇
- T18: 尾形栄治
- T19: 25号機
- T20: 6R
- T21: 4号艇
- T22: 栗原一馬
- T23: 58号機
- T24: 9R
- T25: 5号艇
- T26: 服部幸男
- T27: 51号機
- T28: まとめ
- T29: 3機は今節18走で展示1〜2位10回、2連対6回。58号機は11/25の4Rで1着、3連単11450円。
- T30: 展示タイムは直線寄りの指標で、まわり足は反映されにくく、着順は乗り手や枠にも左右されます。
- T31: BOAT RACE公式の競走成績、番組表、払戻金を独自に集計。今日の出番は11/27の番組表。払戻金は100円あたり
- T32: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s4.png and report.json in handoff/slides/2026-11-27-biwako-hidden-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

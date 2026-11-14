# Slide spec: handoff/slides/2026-11-14-biwako-a1-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-14-biwako-a1-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 菊地孝平 (地 not 池), 馬場貴也, 中亮太 (three characters only), 松井繁, 長田頼宗, 権藤俊光, 柳生泰二, 山田哲也, 西村拓也, 佐々木完太, 池永太 (three characters only), 守屋美穂. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. "A1" in s1 T2 is the half-width capital letter A followed by the half-width digit 1. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot: inside s2 T30, s3 T21 and in the middle of s5 T6/T7 it separates race numbers; in s5 T4-T7 it is ALSO the first character of each line (draw it as the small Japanese middle dot "・", never as a round bullet "•", and do not add any other bullet). "%", "/", ".", "R" and digits are half-width. Half-width spaces appear ONLY in these places: between "8R" and "1号艇" in s1 T4 and s5 T4 ("8R 1号艇"), and inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "40号機", "12R", "28.28%" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed in this rule as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. s3 T23, s4 T26, s4 T27, s2 T33, s5 T4-T9 and the s4 headline T3 (wrap only between 上でも and 機歴) may wrap automatically; wrapping must never add, remove or change characters. s1 T2/T3/T4, s2/s3 headlines T3 and all table cells must NOT wrap. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the rank column in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px. Table header row about 30px in #9fb3c8. Table cells: racer name white bold about 48px, motor white about 44px, third column about 40px, rank column about 66px digits. In ranks, "位" is about 45% of the digit height, on the same line. In rates, "%" is normal size.

## s1 (cover)
- Base image: handoff/images/2026-11-14/cover.png (one white kyotei boat with a racer in a white suit and white helmet, turning left beside an orange-and-white buoy on choppy water, mountains behind, dark stormy sky in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 90px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 44px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: びわこ|初日
- T2: A1級52人のモーターを
- T3: 機歴で格付け
- T4: 62機中1位は8R 1号艇の40号機
- T5: データで読むボートレース

## s2 (top 6 motors)
- Headline T3 (one line).
- A clean table card with 4 columns: racer, motor, today's race(s), rank (right-aligned). Header row: T4, T5, T6, T7.
- 6 data rows with thin divider lines, evenly spaced. Racer white bold, motor white, race column #9fb3c8, rank big yellow #FFC400 right-aligned.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
- Rows 1 and 2 (ranks 1位 and 2位) get a slightly brighter, warm-tinted row background.
- Under the table: T32 in yellow, about 42px. Footnote T33 at the bottom (may wrap).
- T1: モーター格付け|びわこ
- T2: 2/5
- T3: 機歴の上位6機
- T4: 選手
- T5: 号機
- T6: 今日
- T7: 順位
- T8: 菊地孝平
- T9: 40号機
- T10: 8R
- T11: 1位
- T12: 馬場貴也
- T13: 18号機
- T14: 12R
- T15: 2位
- T16: 中亮太
- T17: 25号機
- T18: 6R
- T19: 3位
- T20: 松井繁
- T21: 11号機
- T22: 12R
- T23: 4位
- T24: 長田頼宗
- T25: 57号機
- T26: 7R
- T27: 5位
- T28: 権藤俊光
- T29: 13号機
- T30: 3R・8R
- T31: 6位
- T32: 8Rと12Rには上位6機が2機ずつ
- T33: BOAT RACE公式の競走成績・番組表を独自に集計。機歴はびわこの2026/4/8〜11/10の開催分で、乗り手のクセを除いた展示タイムの速さで62機を並べた順位。出走は11/14の番組表

## s3 (rate is ordinary, rank is high)
- Headline T3 (one line).
- Same table layout and sizes as s2, 4 columns: racer, motor, official 2-place rate (white), rank (big yellow #FFC400, right-aligned). Header row: T4, T5, T6, T7.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
- Under the table: T20 in yellow, about 40px (one line if possible). Then T21 white, about 38px. Then T22 white, about 38px. Footnote T23 at the bottom (may wrap).
- T1: モーター格付け|びわこ
- T2: 3/5
- T3: 2連対率は平凡でも機歴は上位
- T4: 選手
- T5: 号機
- T6: 2連対率
- T7: 順位
- T8: 中亮太
- T9: 25号機
- T10: 28.28%
- T11: 3位
- T12: 柳生泰二
- T13: 17号機
- T14: 31.72%
- T15: 7位
- T16: 山田哲也
- T17: 58号機
- T18: 30.37%
- T19: 12位
- T20: 3機とも2連対率は62機の中央値32.645%以下
- T21: 今日は2R・6R・11Rに出走
- T22: 6Rは1号艇58号機と6号艇25号機
- T23: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は2026/4/8〜11/10の開催分。2連対率は11/14の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算

## s4 (rate above the median, rank is low)
- Headline T3 (may wrap to two lines).
- Same table layout and sizes as s3 (third column = official 2-place rate in white, about 40px, "%" half-width at the same size), but the rank column numbers are in warning red #ff8a8a instead of yellow. Header row: T4, T5, T6, T7.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Under the table: T24 in white, about 38px. Then T25 white, about 38px. Then T26 in warning red #ff8a8a, about 32px (may wrap). Footnote T27 at the bottom (may wrap).
- T1: モーター格付け|びわこ
- T2: 4/5
- T3: 2連対率は中央値より上でも機歴は下位
- T4: 選手
- T5: 号機
- T6: 2連対率
- T7: 順位
- T8: 佐々木完太
- T9: 39号機
- T10: 37.86%
- T11: 56位
- T12: 西村拓也
- T13: 49号機
- T14: 38.06%
- T15: 59位
- T16: 守屋美穂
- T17: 64号機
- T18: 34.03%
- T19: 60位
- T20: 池永太
- T21: 67号機
- T22: 34.59%
- T23: 61位
- T24: 4機とも2連対率は62機の中央値32.645%より上
- T25: 5Rは1号艇49号機と2号艇67号機
- T26: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T27: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は2026/4/8〜11/10の開催分。2連対率は11/14の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: the two characters "1位" in T4 ("62機中" stays white), "2機ずつ" in T5, "機歴上位の3機" in T6, "機歴下位の4機" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 34px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: モーター格付け|びわこ
- T2: 5/5
- T3: まとめ
- T4: ・62機中1位の40号機は8R 1号艇の菊地孝平
- T5: ・8Rと12Rには上位6機が2機ずつ
- T6: ・2連対率は平凡でも機歴上位の3機は2R・6R・11R
- T7: ・2連対率は中央値より上でも機歴下位の4機は1R・5R・7R・10R
- T8: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-14-biwako-a1-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

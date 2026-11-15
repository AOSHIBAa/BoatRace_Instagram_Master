# Slide spec: handoff/slides/2026-11-15-biwako-day1-review

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-15-biwako-day1-review/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in handoff/slides/2026-11-15-biwako-day1-review/expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 菊地孝平 (地 not 池), 馬場貴也, 中亮太 (three characters only), 松井繁, 長田頼宗, 権藤俊光, 佐々木完太, 西村拓也, 守屋美穂, 池永太 (three characters only). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot: in s5 T4-T7 it is the first character of each line (draw it as the small Japanese middle dot "・", never as a round bullet "•", and do not add any other bullet); in s5 T7 it ALSO separates the three race entries. "%", "/", ".", "R" and digits are half-width. Half-width spaces appear ONLY inside "BOAT RACE" in the footnotes. No other spaces anywhere (e.g. "1号艇", "83.3%", "9420円", "3R中亮太" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed in this rule as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. These may wrap automatically: s2 T20, s2 T21, s3 T38, s4 T28, s4 T30, s5 T4-T9. s1 T2/T3/T4, all headlines T3 on s2-s5, and all table/bar cells must NOT wrap. Wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a (not used in this series except where stated).
- Margins ~7% each side, left-aligned (except the right-aligned columns stated below). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px.

## s1 (cover)
- Base image: handoff/images/2026-11-15/cover.png (three white kyotei boats with racers in red, blue and yellow suits and white helmets, on a lake with mountains behind and a grey overcast sky in the top half). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (each on ONE line, never wrap): T2 in white about 84px, then T3 in yellow about 120px (the biggest text in the series). Below it a short yellow horizontal bar, then subtitle T4 in white, about 40px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: びわこ|初日の答え合わせ
- T2: 初日は1号艇が
- T3: 12戦10勝
- T4: 格付け上位6機の1号艇は3走すべて1着
- T5: データで読むボートレース

## s2 (wins by boat number)
- Headline T3 (one line).
- A card with a simple horizontal bar chart of 6 rows, one per boat number, evenly spaced. Each row: label on the left in white about 40px, then a horizontal bar, then the count on the right of the bar about 44px.
  - Row 1: label T4, count T5. The bar is long (full available width) and yellow #FFC400; the count T5 is yellow and bigger, about 60px.
  - Row 2: T6, T7 (NO bar at all; count in #9fb3c8 placed where the bar would start)
  - Row 3: T8, T9 (short white bar exactly 1/5 the length of row 1's bar; count white)
  - Row 4: T10, T11 / Row 5: T12, T13 / Row 6: T14, T15 (same style as row 2)
- Below the chart, two side-by-side small cards: left card has label T16 (#9fb3c8, about 28px) above big yellow T17 (about 80px); right card has label T18 (#9fb3c8, about 28px) above big white T19 (about 80px). In T17 and T19 the "%" is the same size as the digits, same line.
- Then T20 in white, about 34px (may wrap). Footnote T21 at the bottom (may wrap).
- T1: 初日の結果|びわこ
- T2: 2/5
- T3: 12レースの1着の枠
- T4: 1号艇
- T5: 10勝
- T6: 2号艇
- T7: 0勝
- T8: 3号艇
- T9: 2勝
- T10: 4号艇
- T11: 0勝
- T12: 5号艇
- T13: 0勝
- T14: 6号艇
- T15: 0勝
- T16: 初日の1号艇1着率
- T17: 83.3%
- T18: 4/8〜11/10の1号艇1着率
- T19: 55.6%
- T20: 3連単の最高は6Rの9420円、万舟はなし
- T21: BOAT RACE公式の競走成績・払戻金を独自に集計。初日はびわこの11/14の12レース。比較はびわこの2026/4/8〜11/10の1435レースで、1号艇が1着になった割合

## s3 (top 6 motors: how they did on day 1)
- Headline T3 (one line).
- A clean table card with 4 columns: racer, rank, boat number, finish. Header row (about 30px, #9fb3c8): T4, T5, T6, T7.
- 7 data rows with thin divider lines, evenly spaced. Racer white bold about 46px (left); rank in yellow #FFC400 about 46px; boat number white about 42px; finish white bold about 50px, right-aligned. In ranks and finishes the "位"/"着" is the same size as the digits.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
  - Row 7: T32, T33, T34, T35
- Rows 1, 2 and 6 (the "1号艇 / 1着" rows) get a slightly brighter, warm-tinted row background and their finish "1着" is yellow #FFC400.
- Under the table: T36 in yellow, about 40px. Then T37 white, about 38px. Footnote T38 at the bottom (may wrap).
- T1: 答え合わせ|びわこ
- T2: 3/5
- T3: 機歴の上位6機の初日
- T4: 選手
- T5: 順位
- T6: 枠
- T7: 着
- T8: 菊地孝平
- T9: 1位
- T10: 1号艇
- T11: 1着
- T12: 馬場貴也
- T13: 2位
- T14: 1号艇
- T15: 1着
- T16: 中亮太
- T17: 3位
- T18: 6号艇
- T19: 5着
- T20: 松井繁
- T21: 4位
- T22: 2号艇
- T23: 4着
- T24: 長田頼宗
- T25: 5位
- T26: 5号艇
- T27: 2着
- T28: 権藤俊光
- T29: 6位
- T30: 1号艇
- T31: 1着
- T32: 権藤俊光
- T33: 6位
- T34: 5号艇
- T35: 3着
- T36: 1号艇の3走は3回とも1着
- T37: 2〜6号艇の4走は1着なし
- T38: BOAT RACE公式の競走成績を独自に集計。順位は11/14の出走前の機歴で、びわこの2026/4/8〜11/10の開催分から乗り手のクセを除いた展示タイムの速さで62機を並べたもの。結果は11/14のびわこ

## s4 (bottom 4 motors: how they did on day 1)
- Headline T3 (one line).
- Same table layout, row height and sizes as s3 (4 columns: racer, rank, boat number, finish; 5 rows with the same row height as s3, the card is simply shorter), but the rank column is in warning red #ff8a8a instead of yellow. Header row: T4, T5, T6, T7.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Rows 3 and 4 (the "1号艇 / 1着" rows) get a slightly brighter, warm-tinted row background and their finish "1着" is yellow #FFC400.
- Under the table: T28 in yellow, about 38px (may wrap). Then T29 white, about 38px. Footnote T30 at the bottom (may wrap).
- T1: 答え合わせ|びわこ
- T2: 4/5
- T3: 前日紹介の機歴下位4機の初日
- T4: 選手
- T5: 順位
- T6: 枠
- T7: 着
- T8: 佐々木完太
- T9: 56位
- T10: 3号艇
- T11: 3着
- T12: 佐々木完太
- T13: 56位
- T14: 5号艇
- T15: 6着
- T16: 西村拓也
- T17: 59位
- T18: 1号艇
- T19: 1着
- T20: 守屋美穂
- T21: 60位
- T22: 1号艇
- T23: 1着
- T24: 池永太
- T25: 61位
- T26: 2号艇
- T27: 3着
- T28: 機歴は下位でも1号艇の2走は2回とも1着
- T29: 1号艇以外の3走は最高で3着
- T30: BOAT RACE公式の競走成績を独自に集計。順位は11/14の出走前の機歴で、びわこの2026/4/8〜11/10の開催分から乗り手のクセを除いた展示タイムの速さで62機を並べたもの。結果は11/14のびわこ。下位4機は、11/14の投稿で紹介した、2連対率が中央値より上でも機歴は下位の4機

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 38px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "12戦10勝" in T4, "55.6%" in T5, "すべて1着" in T6, "3R中亮太・7R長田頼宗・11R松井繁" in T7; everything else in those lines is white. If T7 wraps, break it only right after "乗るのは" (never inside a racer name); a slightly smaller size (about 34px) is fine.
- Below the card: T8 in white, about 34px (may wrap).
- At the bottom, T9 in small #9fb3c8 (about 24px, may wrap).
- T1: 答え合わせ|びわこ
- T2: 5/5
- T3: まとめ
- T4: ・初日は1号艇が12戦10勝、1着率83.3%
- T5: ・びわこの4/8〜11/10の55.6%を大きく上回った
- T6: ・上位6機と前日紹介の下位4機、1号艇の5走はすべて1着
- T7: ・上位6機で今日1号艇に乗るのは3R中亮太・7R長田頼宗・11R松井繁
- T8: 1日12レースだけの結果は大きく振れます。枠や進入とあわせて参考にしてください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-15-biwako-day1-review/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

# Slide spec: handoff/slides/2026-11-16-amagasaki-series-review

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-16-amagasaki-series-review/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in handoff/slides/2026-11-16-amagasaki-series-review/expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 薗頭心 (薗 with the grass radical on top, NOT 園; three characters only), 村上彰一, 武藤綾子, 中澤和志 (澤 is the old form, NOT 沢), 平尾崇典 (崇 NOT 祟). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot: in s5 T4-T7 it is the first character of each line (draw it as the small Japanese middle dot "・", never as a round bullet "•", and do not add any other bullet); it also appears inside s3 T36, s4 T23, s4 T27, s4 T29, and s5 T5 exactly as written. "%", "/", ".", "R", "A1", "B1", "B2", the "B" in "B級" and all digits are half-width. In s3 the cells like "6/6" are digit, half-width slash, digit with no spaces. Half-width spaces appear ONLY inside "BOAT RACE" in the footnotes and between the race and boat in s4 (e.g. "2R 4号艇": one half-width space after "R"). No other spaces anywhere (e.g. "32走", "28.1%", "23号機", "1位" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed in this rule as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. These may wrap automatically: s2 T16, s2 T17, s3 T36, s4 T28, s4 T29, s5 T4-T9. s1 T2/T3/T4, all headlines T3 on s2-s5, and all table/card cells must NOT wrap. Wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a (only where stated).
- Margins ~7% each side, left-aligned (except the right-aligned columns stated below). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px (shrink slightly if needed to keep it on one line).

## s1 (cover)
- Base image: handoff/images/2026-11-16/cover.png (one white kyotei boat with a racer in a white suit and white helmet turning at an orange-and-white buoy, lake and mountains behind, dark overcast sky in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (each on ONE line, never wrap): T2 in white about 80px, then T3 in yellow about 120px (the biggest text in the series). Below it a short yellow horizontal bar, then subtitle T4 in white, about 40px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 尼崎|11/12〜11/15の答え合わせ
- T2: 機歴上位5機の32走
- T3: 2連対は9回
- T4: A1級選手の2機で9回、B級選手の3機は0回
- T5: データで読むボートレース

## s2 (two groups side by side)
- Headline T3 (one line).
- Two equal cards side by side, same height.
  - Left card (thin yellow border): title T4 in yellow about 34px (one line). Then T5 white about 44px. Then a row: label T6 (#9fb3c8, about 28px) above value T7 (white, about 96px; "回" same size as the digits). Then label T8 (#9fb3c8, about 28px) above value T9 (yellow #FFC400, about 96px; "回" same size as the digits).
  - Right card (thin #9fb3c8 border): title T10 in white about 34px (one line). Then T11 white about 44px. Then label T12 above value T13 (white, about 96px), then label T14 above value T15 (yellow #FFC400, about 96px). Same sizes and positions as the left card.
- Below the cards: T16 in white, about 36px (may wrap). Footnote T17 at the bottom (may wrap).
- T1: 答え合わせ|尼崎
- T2: 2/5
- T3: 展示は速くても2連対は同じ9回
- T4: 機歴1〜5位の5機
- T5: 32走
- T6: 展示1〜2位
- T7: 21回
- T8: 2連対
- T9: 9回
- T10: 機歴40位以下の4機
- T11: 27走
- T12: 展示1〜2位
- T13: 4回
- T14: 2連対
- T15: 9回
- T16: 2連対率は5機が28.1%、4機が33.3%
- T17: BOAT RACE公式の競走成績を独自に集計。尼崎の11/12〜11/15の4日間。どちらも11/12の投稿で紹介した機で、順位は尼崎の2026/4/17〜11/1の開催分から乗り手のクセを除いた展示タイムの速さで63機を並べたもの。4機は公式2連対率が中央値より上でも機歴40位以下

## s3 (top 5 motors: 4 days)
- Headline T3 (one line).
- A clean table card with 5 columns: rank, racer, class, exhibition top-2 count, top-2 finishes. Header row (about 28px, #9fb3c8): T4, T5, T6, T7, T8.
- 5 data rows with thin divider lines, evenly spaced. Rank in yellow #FFC400 about 44px; racer white bold about 46px; class white about 40px; exhibition column white about 46px; top-2 finish column bold about 50px, right-aligned. In ranks the "位" is the same size as the digits.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
- Rows 4 and 5 (the A1 rows) get a slightly brighter, warm-tinted row background and their last-column values (T28, T33) are yellow #FFC400. In rows 1-3 the last-column values (T13, T18, T23) are #9fb3c8.
- Under the table: T34 in yellow, about 38px. Then T35 white, about 38px. Footnote T36 at the bottom (may wrap).
- T1: 答え合わせ|尼崎
- T2: 3/5
- T3: 機歴1〜5位の5機の4日間
- T4: 機歴
- T5: 選手
- T6: 級別
- T7: 展示1〜2位
- T8: 2連対
- T9: 1位
- T10: 薗頭心
- T11: B2
- T12: 6/6
- T13: 0/6
- T14: 2位
- T15: 村上彰一
- T16: B1
- T17: 4/6
- T18: 0/6
- T19: 3位
- T20: 武藤綾子
- T21: B1
- T22: 3/6
- T23: 0/6
- T24: 4位
- T25: 中澤和志
- T26: A1
- T27: 1/7
- T28: 5/7
- T29: 5位
- T30: 平尾崇典
- T31: A1
- T32: 7/7
- T33: 4/7
- T34: A1級選手の2機は14走で1着7回、うち万舟2回
- T35: B級選手の3機は18走で2連対なし
- T36: BOAT RACE公式の競走成績・払戻金・番組表を独自に集計。尼崎の11/12〜11/15。数字は回数/走数。展示1〜2位は各レース内の展示タイム順で、同タイムは上位扱い。村上彰一の6走には着順の記録がない1走を含む。万舟は3連単1万円以上

## s4 (today's races)
- Headline T3 (one line).
- A table card with 4 columns: rank, motor number, racer, race and boat. Header row (about 28px, #9fb3c8): T4, T5, T6, T7.
- 5 data rows with thin divider lines, evenly spaced. Rank yellow #FFC400 about 42px; motor number white about 40px; racer white bold about 44px; race-and-boat white about 38px, left-aligned in its column. In ranks the "位" and in motor numbers the "号機" are the same size as the digits (T23 and T27 are long: shrink them slightly so they stay on ONE line).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Under the table: T28 in yellow, about 36px (may wrap). Footnote T29 at the bottom (may wrap).
- T1: 今日の出番|尼崎
- T2: 4/5
- T3: 上位5機の11/16の出番
- T4: 機歴
- T5: 号機
- T6: 選手
- T7: レースと枠
- T8: 1位
- T9: 23号機
- T10: 薗頭心
- T11: 2R 4号艇
- T12: 2位
- T13: 56号機
- T14: 村上彰一
- T15: 9R 5号艇
- T16: 3位
- T17: 63号機
- T18: 武藤綾子
- T19: 4R 2号艇
- T20: 4位
- T21: 61号機
- T22: 中澤和志
- T23: 8R 6号艇・12R 1号艇
- T24: 5位
- T25: 54号機
- T26: 平尾崇典
- T27: 1R 3号艇・10R 4号艇
- T28: 12Rは1号艇に4位機、3号艇と6号艇に40位以下の2機
- T29: BOAT RACE公式の番組表を独自に集計。11/16の尼崎。順位は尼崎の2026/4/17〜11/1の開催分・63機中の機歴

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 38px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "21回" in T4, "中澤和志・平尾崇典" in T5, "2連対9回" in T6, "8Rと12R" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 32px (may wrap).
- At the bottom, T9 in small #9fb3c8 (about 24px, may wrap).
- T1: まとめ|尼崎
- T2: 5/5
- T3: まとめ
- T4: ・機歴上位5機は4日間32走で展示1〜2位が21回
- T5: ・2連対9回はすべてA1級の中澤和志・平尾崇典
- T6: ・40位以下の4機は展示1〜2位が4回でも2連対9回
- T7: ・今日は8Rと12Rで上位機と40位以下の機が同じレースに
- T8: 展示タイムは直線寄りの指標で、まわり足は反映されにくく、着順は乗り手や枠にも左右されます。4日間だけの結果は大きく振れます。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-16-amagasaki-series-review/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

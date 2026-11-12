# Slide spec: handoff/slides/2026-11-12-amagasaki-motor-gap

Slides: s1.png ... s4.png (4 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-12-amagasaki-motor-gap/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 4 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana (racer names must be exact: 薗頭心, 村上彰一, 武藤綾子, 中澤和志, 平尾崇典, 谷口丞, 山田竜一, 笠原亮, 上田健太. Note 薗 not 園, 澤 not 沢, 崇 not 祟, 丞 not 承, 竜 not 龍). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot (in s4 T4-T6 it is the first character of the line; do not replace it with a round bullet "•"). "%", "/", ".", "R" and digits are half-width. Half-width spaces appear ONLY: between "R" and the boat number in every race item (e.g. "3R 3号艇・8R 6号艇"), and inside "BOAT RACE" in the footnotes. No other spaces. "、" and "。" are Japanese punctuation. "※" in s4 T8 is the full-width reference mark.
- Wrapping: s3 T3, s4 T4-T8 and footnotes may wrap automatically; wrapping must never add, remove or change characters. Table cells must NOT wrap (make the race column wide enough; shrink its font slightly if needed). Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark navy translucent rounded boxes (NOT white) with thin semi-transparent borders.
- Data slides (s2-s4): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote (last item) at the bottom in small #9fb3c8.
- Sizes at 1122x1402: s1 title T2/T3 about 90px (each on ONE line, never wrap), s1 T4 about 44px; headline T3 on s2-s4 about 60px; table header about 30px; s2 rank column about 60px digits (yellow); motor column about 44px white; racer column about 44px white; s2 race column about 32px #9fb3c8; s3 percentage column about 44px white; s3 machine-rank column about 52px in warning red #ff8a8a; body text about 42px; footnotes about 24px; s1 T1 and the T1 label on data slides about 30px; page number T2 about 28px; s1 T5 about 28px; s4 T7 about 40px; s4 T8 about 26px.

## s1 (cover)
- Base image: handoff/images/2026-11-12/cover.png (kyotei boats in a close pack on a wide course, dark top area). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium, on a dark translucent pill so it reads clearly. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 尼崎|新節初日
- T2: 2連対率と展示の
- T3: ズレを読む
- T4: 機歴の1〜5位機がそろって出走
- T5: データで読むボートレース

## s2 (machine rank 1-5)
- Headline T3 white, large.
- A clean table card with 4 columns, in this order from left: rank, motor, racer, today's races. Header row, all small #9fb3c8: T4, T5, T6, T7.
- 5 data rows with thin divider lines, in this order:
  - Row 1: T8 (rank), T9 (motor), T10 (racer), T11 (race)
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- No highlighted rows. Under the table: T28 in yellow, medium (about 44px). Footnote T29 at the bottom.
- T1: モーター格付け|尼崎
- T2: 2/4
- T3: 機歴の1〜5位・63機中
- T4: 順位
- T5: 号機
- T6: 選手
- T7: 今日のレース
- T8: 1位
- T9: 23号機
- T10: 薗頭心
- T11: 1R 4号艇
- T12: 2位
- T13: 56号機
- T14: 村上彰一
- T15: 3R 3号艇・8R 6号艇
- T16: 3位
- T17: 63号機
- T18: 武藤綾子
- T19: 6R 2号艇
- T20: 4位
- T21: 61号機
- T22: 中澤和志
- T23: 6R 1号艇・12R 5号艇
- T24: 5位
- T25: 54号機
- T26: 平尾崇典
- T27: 3R 6号艇・12R 3号艇
- T28: 6Rは1号艇に4位機、2号艇に3位機
- T29: BOAT RACE公式の競走成績・番組表を独自に集計。尼崎の2026/4/17〜11/1の開催分。順位は、乗り手のクセを除いた展示タイムの速さで63機を並べたもの

## s3 (high 2-rate, low machine rank)
- Headline T3 white, large (may wrap to two lines).
- A clean table card with 4 columns, in this order from left: motor, racer, official 2-rate, machine rank. Header row, all small #9fb3c8: T4, T5, T6, T7.
- 4 data rows with thin divider lines, in this order:
  - Row 1: T8 (motor), T9 (racer), T10 (2-rate, white), T11 (machine rank, red #ff8a8a)
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Under the table: T24 white, small-medium (about 32px). Then a card with yellow border containing T25 in yellow, medium (about 40px). Footnote T26 at the bottom.
- T1: モーター格付け|尼崎
- T2: 3/4
- T3: 2連対率は高めでも機歴40位以下の4機
- T4: 号機
- T5: 選手
- T6: 2連対率
- T7: 機歴
- T8: 32号機
- T9: 谷口丞
- T10: 39.87%
- T11: 42位
- T12: 62号機
- T13: 山田竜一
- T14: 37.91%
- T15: 48位
- T16: 8号機
- T17: 笠原亮
- T18: 37.82%
- T19: 50位
- T20: 13号機
- T21: 上田健太
- T22: 36.99%
- T23: 55位
- T24: 63機の2連対率の中央値は33.12%
- T25: 24号機は2連対率が中央値並みの33.12%でも機歴14位
- T26: BOAT RACE公式の競走成績・番組表を独自に集計。今日の出走機のうち、2連対率が中央値より上で機歴40位以下の機。公式2連対率は11/12の番組表、機歴は尼崎の2026/4/17〜11/1の開催分・63機中の順位

## s4 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium (about 42px), each may wrap. Each line already starts with "・"; do NOT add any other bullet symbol. Only "1〜5位機" in T4, "4位・5位・8位・10位機" in T5 and "機歴40位以下" in T6 are yellow.
- Card (dark navy, not white) with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: モーター格付け|尼崎
- T2: 4/4
- T3: まとめ
- T4: ・機歴の1〜5位機がそろって初日に出走
- T5: ・12Rは4位・5位・8位・10位機が同じレースに
- T6: ・32・62・8・13号機は2連対率は高めでも、機歴40位以下
- T7: 展示タイムは直線寄りの指標で、まわり足は反映されにくい点にご注意ください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s4.png and report.json in handoff/slides/2026-11-12-amagasaki-motor-gap/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

# Slide spec: handoff/slides/2026-11-10-mikuni-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-10-mikuni-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana (racer names must be exact: 冨成謙児, 増田進, 宮嵜隆太郎, 古結宏, 枝尾賢, 夏山亮平, 中島昂章. Note 冨 not 富, 嵜 not 崎, 昂 not 昴). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot (in s5 T4-T6 it is the first character of the line; do not replace it with a round bullet "•"). "%", "/", ".", "R" and digits are half-width. Half-width spaces appear ONLY: between "R" and the boat number in every race item (e.g. "7R 4号艇", "1R 4号艇・7R 1号艇"), and inside "BOAT RACE" in the footnotes. No other spaces. "、" and "。" are Japanese punctuation. "※" in s5 T8 is the full-width reference mark.
- Wrapping: headlines, s4 T4/T7/T12/T13, s5 T4-T8 and footnotes may wrap automatically; wrapping must never add, remove or change characters. Table cells must NOT wrap (make the race column wide enough; shrink its font slightly if needed). Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote (last item) at the bottom in small #9fb3c8.
- Sizes at 1122x1402: s1 title T2/T3 about 90px (each on ONE line, never wrap), s1 T4 about 44px; headline T3 on s2-s5 about 60px; table header about 30px; table rank column about 60px digits (yellow); motor column about 44px white; racer column about 44px white; race column about 32px #9fb3c8; s4 T6 about 120px digits, s4 T9 about 160px digits; body text about 42px; footnotes about 24px; s1 T1 and the T1 label on data slides about 30px; page number T2 about 28px; s1 T5 about 28px; s4 T5/T8 about 34px; s4 T7/T10 about 28px; s5 T7 about 40px; s5 T8 about 26px.
- In big numbers, "%" and "位" are about 45% of the digit height, on the same line.

## s1 (cover)
- Base image: handoff/images/2026-11-10/cover.png (late-afternoon kyotei race, boat turning around a buoy, dark top area). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium, on a dark translucent pill so it reads clearly. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 三国|新節初日
- T2: 機歴の上位10機を
- T3: 引いたのは誰か
- T4: 7Rに1位・2位・5位機がそろう
- T5: データで読むボートレース

## s2 (rank 1-5)
- Headline T3 white, large.
- A clean table card with 4 columns, in this order from left: rank, motor, racer, today's races. Header row, all small #9fb3c8: T4, T5, T6, T7.
- 5 data rows with thin divider lines, in this order:
  - Row 1: T8 (rank), T9 (motor), T10 (racer), T11 (race)
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20 (rank), T21 (motor), then T22 spans the racer and race columns, in #9fb3c8 (not white), same size as the race column. Row 4 has NO racer name.
  - Row 5: T23, T24, T25, T26
- Rows 1, 2 and 5 (the three motors in 7R) get a slightly brighter, warm-tinted row background.
- Under the table: T27 in yellow, medium (about 44px). Footnote T28 at the bottom.
- T1: モーター格付け|三国
- T2: 2/5
- T3: 機歴の1〜5位・60機中
- T4: 順位
- T5: 号機
- T6: 選手
- T7: 今日のレース
- T8: 1位
- T9: 40号機
- T10: 冨成謙児
- T11: 7R 4号艇
- T12: 2位
- T13: 45号機
- T14: 増田進
- T15: 1R 4号艇・7R 1号艇
- T16: 3位
- T17: 55号機
- T18: 宮嵜隆太郎
- T19: 1R 3号艇・9R 1号艇
- T20: 4位
- T21: 42号機
- T22: 今日は出走なし
- T23: 5位
- T24: 35号機
- T25: 古結宏
- T26: 7R 5号艇・12R 1号艇
- T27: 7Rに1位・2位・5位機がそろう
- T28: BOAT RACE公式の競走成績・番組表を独自に集計。三国の2026/4/5〜11/7の開催分。順位は、乗り手のクセを除いた展示タイムの速さで60機を並べたもの

## s3 (rank 6-10)
- Same table layout and sizes as s2 (rank numbers also yellow).
  - Header: T4, T5, T6, T7
  - Row 1: T8 (rank), T9 (motor), then T10 spans the racer and race columns in #9fb3c8. No racer name.
  - Row 2: T11, T12, T13, T14
  - Row 3: T15, T16, T17, T18
  - Row 4: T19 (rank), T20 (motor), then T21 spans the racer and race columns in #9fb3c8. No racer name.
  - Row 5: T22, T23, T24, T25
- No highlighted rows. Under the table: T26 in yellow, medium (about 44px). Footnote T27 at the bottom.
- T1: モーター格付け|三国
- T2: 3/5
- T3: 機歴の6〜10位・60機中
- T4: 順位
- T5: 号機
- T6: 選手
- T7: 今日のレース
- T8: 6位
- T9: 51号機
- T10: 今日は出走なし
- T11: 7位
- T12: 48号機
- T13: 枝尾賢
- T14: 8R 5号艇
- T15: 8位
- T16: 52号機
- T17: 夏山亮平
- T18: 8R 2号艇
- T19: 9位
- T20: 46号機
- T21: 今日は出走なし
- T22: 10位
- T23: 43号機
- T24: 中島昂章
- T25: 6R 1号艇・11R 5号艇
- T26: 上位10機のうち7機が初日に出走
- T27: BOAT RACE公式の競走成績・番組表を独自に集計。三国の2026/4/5〜11/7の開催分。順位は、乗り手のクセを除いた展示タイムの速さで60機を並べたもの

## s4 (one motor in focus)
- Headline T3 white, large. Below it T4 in yellow, medium (about 44px, may wrap).
- Two cards side by side, same size.
  - Left card: label T5 white small-medium, then T6 big (about 120px digits, must fit inside the card) in #9fb3c8, then T7 small #9fb3c8.
  - Right card (highlighted, border #FFC400, slightly warm-tinted background): label T8 white small-medium, then T9 huge (about 160px digits) in yellow #FFC400, then T10 small #9fb3c8.
- Under the cards: T11 in yellow, large (about 56px). Then T12 white, small-medium (about 32px, may wrap). Then T13 small (about 30px) in warning red #ff8a8a. Footnote T14 at the bottom.
- T1: モーター格付け|三国
- T2: 4/5
- T3: 2連対率は平凡な55号機
- T4: 宮嵜隆太郎・1R 3号艇と9R 1号艇
- T5: 公式の2連対率
- T6: 32.50%
- T7: 60機の真ん中より下
- T8: 展示ベースの機歴
- T9: 3位
- T10: 60機中
- T11: 展示は平均0.033秒速い
- T12: 乗り手のクセを除いた、レース内中央値との差・146走の平均
- T13: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T14: BOAT RACE公式の競走成績・番組表を独自に集計。公式2連対率は11/10の番組表、機歴は三国の2026/4/5〜11/7の開催分

## s5 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium (about 42px), each may wrap. Each line already starts with "・"; do NOT add any other bullet symbol. Only "1位・2位・5位機" in T4, "7機" in T5 and "機歴は上位" in T6 are yellow.
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: モーター格付け|三国
- T2: 5/5
- T3: まとめ
- T4: ・機歴1位・2位・5位機が7Rにそろう
- T5: ・上位10機のうち7機が初日に出走
- T6: ・55号機と48号機は2連対率は平凡でも、機歴は上位
- T7: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-10-mikuni-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

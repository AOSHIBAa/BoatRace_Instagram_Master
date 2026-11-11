# Slide spec: handoff/slides/2026-11-11-mikuni-day1-review

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-11-mikuni-day1-review/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 冨成謙児 (冨 not 富), 古結宏, 増田進, 枝尾賢. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot (in s5 T4-T6 it is the first character of the line; do not replace it with a round bullet "•"). In "4-5-1" and "5-4-1" each "-" is a half-width ASCII hyphen-minus (not a long dash, not "ー"). "%", "/", ".", ",", "R" and digits are half-width; "7,820円" and "25,440円" use a half-width comma. Half-width spaces appear ONLY: between "3連単" and the combination in s3 T20 and s4 T11 (e.g. "3連単 4-5-1"), and inside "BOAT RACE" in the footnotes. No other spaces. "、" and "。" are Japanese punctuation. "※" in s5 T8 is the full-width reference mark.
- Wrapping: s2 T14/T15, s3 T22, s4 T12, s5 T4-T8 and footnotes may wrap automatically; wrapping must never add, remove or change characters. Headlines (T3), s1 T2/T3/T4 and table cells must NOT wrap. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 24px).
- Headline T3 on s2-s5: white, about 60px, ONE line.
- In big numbers, "%", "円" and "位" are about 45% of the digit height, on the same line.

## s1 (cover)
- Base image: handoff/images/2026-11-11/cover.png (one kyotei boat running fast on choppy water under a dark stormy sky). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 96px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 44px, on a dark translucent pill so it reads clearly. Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 三国|初日の答え合わせ
- T2: 機歴の上位10機
- T3: 11走で1着4回
- T4: 7Rは1位・2位・5位機で1〜3着
- T5: データで読むボートレース

## s2 (comparison)
- Headline T3.
- A clean table card with 3 columns: label column (wide), then two number columns. Header row, small #9fb3c8 (about 30px): T4, T5, T6.
- Row 1 (highlighted: warm-tinted row background, numbers in yellow #FFC400): T7 (white, about 40px), T8 (about 88px digits), T9 (about 88px digits).
- Row 2 (normal): T10 (#9fb3c8, about 40px), T11 (white, about 72px digits), T12 (white, about 72px digits).
- Under the table: T13 in yellow, about 46px. Then T14 white, about 34px. Then T15 in warning red #ff8a8a, about 32px. Footnote T16 at the bottom.
- T1: 答え合わせ|三国
- T2: 2/5
- T3: 上位10機の初日11走
- T4: 区分
- T5: 1着率
- T6: 3着以内率
- T7: 上位10機・11走
- T8: 36.4%
- T9: 81.8%
- T10: ほかの機・61走
- T11: 13.1%
- T12: 44.3%
- T13: 11走で1着4回・3着以内9回
- T14: 展示タイムがレース内2位以内だったのも11走中8走
- T15: 1日だけの結果で、数字は大きく振れる
- T16: BOAT RACE公式の競走成績・払戻金を独自に集計。三国11/10の全12レース。機歴は三国の2026/4/5〜11/7の開催分で、乗り手のクセを除いた展示タイムの速さで60機を並べた順位。展示の順位は同タイムを同順位

## s3 (race 7)
- Headline T3.
- A table card with 4 columns: finish, racer, motor and rank, course. Header row small #9fb3c8 (about 30px): T4, T5, T6, T7.
- 3 data rows with thin divider lines. Finish cell (T8/T12/T16) yellow, about 54px. Racer cell white, about 46px. Motor cell white, about 38px. Course cell #9fb3c8, about 34px.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
- Under the table, a highlighted card (border #FFC400, slightly warm background): label T20 white about 40px on the left, and T21 huge yellow on the right (about 120px digits).
- Then T22 white, about 36px. Footnote T23 at the bottom.
- T1: 答え合わせ|三国
- T2: 3/5
- T3: 7Rは上位機で1〜3着
- T4: 着
- T5: 選手
- T6: 号機・機歴
- T7: 進入
- T8: 1着
- T9: 冨成謙児
- T10: 40号機・1位
- T11: 4コース
- T12: 2着
- T13: 古結宏
- T14: 35号機・5位
- T15: 5コース
- T16: 3着
- T17: 増田進
- T18: 45号機・2位
- T19: 1コース
- T20: 3連単 4-5-1
- T21: 7,820円
- T22: 展示タイムもこの3人が6艇中の上位3つ
- T23: BOAT RACE公式の競走成績・払戻金を独自に集計。三国11/10の全12レース。機歴は三国の2026/4/5〜11/7の開催分で、乗り手のクセを除いた展示タイムの速さで60機を並べた順位

## s4 (race 8)
- Headline T3. Below it T4 in yellow, about 46px.
- Two cards side by side, same size.
  - Left card: label T5 white about 34px, then T6 big (about 110px digits, must fit inside the card) in #9fb3c8, then T7 small #9fb3c8 (about 28px).
  - Right card (highlighted, border #FFC400, slightly warm-tinted background): label T8 white about 34px, then T9 huge (about 160px digits) in yellow #FFC400, then T10 small #9fb3c8 (about 28px).
- Under the cards: T11 in yellow, large (about 58px, one line). Then T12 in warning red #ff8a8a, about 32px. Footnote T13 at the bottom.
- T1: 答え合わせ|三国
- T2: 4/5
- T3: 8Rは7位の48号機が1着
- T4: 枝尾賢・5コースから
- T5: 公式の2連対率
- T6: 32.14%
- T7: 60機の真ん中より下
- T8: 展示ベースの機歴
- T9: 7位
- T10: 60機中
- T11: 3連単 5-4-1は25,440円
- T12: 1レースだけの結果で、次も勝つとは限らない
- T13: BOAT RACE公式の競走成績・番組表・払戻金を独自に集計。公式2連対率は11/10の番組表、機歴は三国の2026/4/5〜11/7の開催分

## s5 (summary)
- Headline T3 white, about 60px like the other headlines. Then T4, T5, T6 as three lines in white, about 42px, each may wrap. Each line already starts with "・"; do NOT add any other bullet symbol. Only "1着4回・3着以内9回" in T4, "1コース" in T5 and "大きく振れる" in T6 are yellow. A yellow phrase may break across lines, but its color must stay continuous.
- Card with T7 in white, about 40px. Bottom T8 small #9fb3c8 (about 26px).
- T1: 答え合わせ|三国
- T2: 5/5
- T3: まとめ
- T4: ・上位10機は11走で1着4回・3着以内9回
- T5: ・4勝のうち2勝は1コースで、枠の有利も含む数字
- T6: ・1日・11走だけの結果なので、数字は大きく振れる
- T7: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-11-mikuni-day1-review/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

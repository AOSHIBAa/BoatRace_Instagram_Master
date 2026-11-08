# Slide spec: handoff/slides/2026-11-11-wind

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-11-wind/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, commas, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: every "|" is a half-width ASCII bar with NO spaces around it. "？" in s1 T3 and s3 T3 is a FULL-width Japanese question mark. Parentheses "（" "）" (footnotes and s5 T4) are FULL-width Japanese parentheses. "〜" is a Japanese wave dash. "・" is a Japanese middle dot. "%", "/" (2/5, 4/3, 11/7, 11/1), "." , "m" and digits are half-width. Commas in numbers (5,459 / 4,577) are half-width. Exactly one half-width space: after "近畿4場" in s1 T4, after "風速別" in s2 T3, after "場別" in s4 T3, and the one space inside "BOAT RACE" in the footnotes. "、" and "。" are Japanese punctuation. "※" in s5 T8 is the full-width Japanese reference mark.
- Wrapping: long sentences may wrap automatically; wrapping must never add, remove or change characters. Each listed item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except table numbers in s3 and s4, right-aligned in their columns). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left, page number T2 top-right in #9fb3c8, footnote (last item) at the bottom in small #9fb3c8.
- Sizes at 1122x1402: s1 title T2/T3 about 110px (T3 must stay on ONE line: shrink it to about 90px if needed, never wrap it), s1 T4 about 46px; headline T3 about 72px; s2 hero numbers T5/T8 about 180px digits; table numbers about 80px; table venue/course names about 52px; table header about 36px; s5 T4-T6 about 48px; body text about 44px; footnotes about 26px.
- Color meaning: warning red #ff8a8a marks only the values where the inside course clearly weakened (s2 T8, s4 T15 and T18); other highlighted numbers are yellow.
- In big numbers, "%" is about 45% of the digit height, on the same line. Inline "%" inside sentences (s5) is normal text size.

## s1 (cover)
- Base image: handoff/images/2026-11-11/cover.png (coastal course, strong wind, one boat running straight, dark top area). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible.
- Darken the top half with a navy gradient. Top-left small yellow label T1. Huge title on two lines: T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, medium. Footer T5 small, white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 風の分析|近畿4場
- T2: 風速5m以上で
- T3: 1コースはどうなる？
- T4: 近畿4場 5,459レースを集計
- T5: データで読むボートレース

## s2 (overall — wind 4m or less vs 5m or more)
- Headline T3 white, large.
- Two cards stacked vertically, same size.
  - Card A: label T4 white medium on top, then T5 huge (about 180px digits) in white, then T6 small #9fb3c8.
  - Card B (highlighted, background slightly red-tinted, border #ff8a8a): label T7 white medium, then T8 huge (about 180px digits) in warning red #ff8a8a, then T9 small #9fb3c8.
- Under the cards: T10 in yellow, medium-large (about 56px). Footnote T11 at the bottom.
- T1: 風の分析|近畿4場
- T2: 2/5
- T3: 風速別 1コースの1着率
- T4: 風速4m以下
- T5: 57.0%
- T6: 4,577レース
- T7: 風速5m以上
- T8: 52.9%
- T9: 882レース
- T10: 5m以上では約4ポイント低い
- T11: BOAT RACE公式の競走成績（2026/4/3〜11/7の開催分、尼崎は4/17〜11/1）を独自に集計。風速はレース時の記録で、風向は区別していない。6艇の着順・進入がそろう5,459レースが対象

## s3 (which course won instead)
- Headline T3 white, large.
- A clean table card with 3 columns. Header row, all small: T4 (left column, white), T5 (middle column, #9fb3c8), T6 (right column, yellow).
- 3 data rows, thin divider lines between rows. Each row: course name left in white (medium), middle number medium in #9fb3c8, right number big in yellow. Numbers right-aligned in their columns.
  - Row 1: T7, T8, T9
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15 — highlight this row: card background slightly warm-tinted, T15 extra big (about 100px digits).
- Under the table: T16 white, medium (about 44px). Footnote T17 at the bottom.
- T1: 風の分析|近畿4場
- T2: 3/5
- T3: 1着はどのコースに回った？
- T4: 1着の進入
- T5: 4m以下
- T6: 5m以上
- T7: 1コース
- T8: 57.0%
- T9: 52.9%
- T10: 2コース
- T11: 13.5%
- T12: 14.2%
- T13: 3〜6コース
- T14: 29.5%
- T15: 32.9%
- T16: 風が強い日は、3〜6コースの1着が増えた
- T17: BOAT RACE公式の競走成績（2026/4/3〜11/7の開催分、尼崎は4/17〜11/1）を独自に集計。1着の進入コースで分類

## s4 (by venue)
- Headline T3 white, large.
- A clean table card with 3 columns. Header row, all small: T4 (left column, white), T5 (middle column, #9fb3c8), T6 (right column, yellow).
- 4 data rows, thin divider lines between rows. Each row: venue name left in white (medium), middle number medium in #9fb3c8, right number big in yellow. Numbers right-aligned in their columns.
  - Row 1: T7, T8, T9
  - Row 2: T10, T11, T12
  - Row 3: T13, T14, T15 — right number T15 in warning red #ff8a8a instead of yellow
  - Row 4: T16, T17, T18 — right number T18 in warning red #ff8a8a instead of yellow
- Under the table: T19 white, medium (about 44px), then T20 small #9fb3c8 (about 30px). Footnote T21 at the bottom.
- T1: 風の分析|近畿4場
- T2: 4/5
- T3: 場別 1コースの1着率
- T4: 場
- T5: 4m以下
- T6: 5m以上
- T7: 尼崎
- T8: 60.3%
- T9: 59.8%
- T10: 住之江
- T11: 56.9%
- T12: 54.5%
- T13: びわこ
- T14: 56.8%
- T15: 49.5%
- T16: 三国
- T17: 53.8%
- T18: 47.0%
- T19: 尼崎はほぼ変わらず、びわこと三国は約7ポイント低い
- T20: 住之江の5m以上は66レースと少なく、数字は振れやすい
- T21: BOAT RACE公式の競走成績（2026/4/3〜11/7の開催分、尼崎は4/17〜11/1）を独自に集計。5m以上は尼崎331・びわこ198・三国287レース

## s5 (summary)
- Headline T3 white, large. Then T4, T5, T6 as three lines in white, medium-large; only the number "52.9%" in T4 is yellow ("57.0%" stays white).
- Card with T7 in white, medium. Bottom T8 small #9fb3c8.
- T1: 風の分析|近畿4場
- T2: 5/5
- T3: まとめ
- T4: ・風速5m以上で1コースの1着率は52.9%（4m以下は57.0%）
- T5: ・減った分の多くは3〜6コースの1着に回った
- T6: ・びわこと三国は差が大きく、尼崎はほぼ変わらない
- T7: 風の強い日は、場ごとの傾向とあわせて1コースの信頼度を考える参考にしてください。
- T8: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-11-wind/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

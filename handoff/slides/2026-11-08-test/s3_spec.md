# Slide spec: 2026-11-08-test / s3

Output file: `handoff/slides/2026-11-08-test/s3.png`
Also write: `handoff/slides/2026-11-08-test/s3_report.json`
  {"file":"s3.png","size_px":"WxH","attempts":N,"text_check":[{"id":"T1","expected":"...","rendered_ok":true}, ...],"notes":""}

## Absolute rules
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (closest available, e.g. 1024x1280). Instagram infographic slide.
- Render EVERY text item below EXACTLY as written: same characters, same digits, same decimal points, same punctuation. Japanese text must be correct kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- The words "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成" must NOT appear anywhere.
- Symbols: in T1 the bar "|" is a half-width ASCII bar with NO spaces around it. In T8, T12, T15 the parentheses "( )" are half-width. In T15 "〜" is a Japanese wave dash. In T7 there is exactly one half-width space before "32.4%".
- Line breaks: T4 and T15 may wrap automatically, but wrapping must never add, remove or change characters, and no bullet or symbol at line starts.
- "BOAT RACE" in T15 is plain text in the same font as the footnote. Never draw it as a logo or mark.
- No people, no faces, no photos. Flat graphic design only.
- After generating, read every text item in the image yourself and compare character by character with the list. If ANY item differs, regenerate (max 3 attempts total). Record results in s3_report.json honestly.

## Design
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow in the top-right corner and a faint blue glow in the bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), high contrast, very legible on a phone.
- Accent color: yellow #FFC400. Main text: white. Secondary text (T2, T4, T5, T8, T10, T12, T13, T15): light grey-blue #9fb3c8. Warning-ish label: soft red #ff8a8a.
- Layout top to bottom, left-aligned with generous margins (~7% each side):

1. Top-left small yellow label (T1). Top-right small grey page number (T2).
2. Big headline (T3) in white, with the part "25号機" in yellow. Generous empty space below it.
3. Lead sentence (T4) in light grey-blue, medium size, 2 lines.
4. Card A (dark translucent rounded-corner box, thin semi-transparent #ff8a8a border):
   - small grey-blue label (T5)
   - huge white number (T6); the "%" is about 45% of the digit height, same line. Then on the same line small #ff8a8a text (T7). Do not mix up the T6 and T7 numbers.
5. Card B (dark translucent rounded-corner box, thin semi-transparent #FFC400 border):
   - small grey-blue label (T8)
   - huge yellow "0.049" with "秒速い" at about 45% of the digit height on the same line, no line break (T9)
   - small grey-blue label (T10)
   - big white "62" with smaller "%" (T11), then small #9fb3c8 text (T12) on the same line
   - small grey-blue label (T13)
   - big white text (T14)
6. Bottom footnote in small grey text, 2 lines (T15).

## Text items (render exactly)
- T1: 機歴分析|隠れ上位モーター
- T2: 3/7
- T3: びわこ 25号機
- T4: 数字は平凡。でも乗った選手のほとんどが、普段より速い展示を出しています。
- T5: 公式のモーター2連対率
- T6: 27.6%
- T7: 場の中央値 32.4%
- T8: 展示タイム(レースの真ん中より)
- T9: 0.049秒速い
- T10: 展示がレース内2位以内
- T11: 62%
- T12: (73走)
- T13: 普段より展示が速かった選手
- T14: 8人中8人
- T15: BOAT RACE公式の競走成績・番組表(2026/7/7〜11/4)を独自に集計。展示タイムはレース内の中央値との差

## Commit
Commit only `s3.png` and `s3_report.json`, then `git pull --rebase origin main` and `git push origin HEAD:main`.

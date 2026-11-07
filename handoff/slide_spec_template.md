# Slide spec: <FOLDER>

Slides: s1.png ... s<N>.png  (N = 3 to 5)
Format: <REEL or POST>
Report: write <FOLDER>/report.json
  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}], "notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1024x1280 or 1122x1402). All slides must share the same design system so they look like one series.
- Render EVERY text item EXACTLY as written in expected.json: same characters, digits, decimal points, punctuation, half/full width. Japanese text must be correct kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures or flags.
- The words "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成" must NOT appear anywhere.
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Line wrapping is allowed only where noted; wrapping must never add, remove or change characters, and no bullet/symbol at line starts unless written in the text.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), high contrast, very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned. Cards: dark translucent rounded boxes with thin semi-transparent colored borders.
- Big numbers: digits very large; units such as "%" or "秒速い" about 45% of digit height, on the same line.
- Every data slide: small yellow label top-left, page number "n/N" top-right in #9fb3c8, footnote at the bottom in #9fb3c8.

## s1 (cover)
- Background photo: <handoff/images/DATE/cover.png — use it as the base image, keep the boat and scene, do not redraw a different boat>  (or: "no photo, navy background")
- Darken the top half with a gradient so the title is readable. Title (T1) huge white with the key word in yellow, yellow short bar, subtitle (T2), small footer (T3).
- Text: see expected.json "s1".

## s2 ... s<N>
<For each slide: layout from top to bottom, which text ID goes where, colors and relative sizes, symbol notes (e.g. "| is half-width, no spaces").>

## Commit
Commit only the slide PNGs and report.json, then `git pull --rebase origin main` and `git push origin HEAD:main`.

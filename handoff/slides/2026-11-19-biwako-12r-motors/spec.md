# Slide spec: handoff/slides/2026-11-19-biwako-12r-motors

Slides: s1.png ... s4.png (4 slides). Format: POST (carousel; readers swipe at their own pace, so the 6-row tables may be dense but must stay very legible).
Report: write handoff/slides/2026-11-19-biwako-12r-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 4 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in handoff/slides/2026-11-19-biwako-12r-motors/expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Racer names must be exact, with NO spaces inside: 長田頼宗 (頼 is the "rely" kanji, NOT 瀬; 宗 NOT 宋), 遠藤エミ (エミ in katakana), 宮地元輝 (four characters: 宮 地 元 輝), 丸野一樹, 磯部誠 (three characters), 山崎郡 (three characters; 郡 is the "county" kanji, NOT 群).
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses, NO commas inside numbers and NO question marks anywhere in this series. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is a Japanese wave dash. "・" is a Japanese middle dot and appears only inside the footnotes s2 T40, s4 T10 exactly as written; there are NO bullets anywhere. "%", "/", ".", "R" and all digits are half-width. Cells like "4/6" and "27/41" are digit(s), half-width slash, digit(s) with no spaces. Half-width spaces appear ONLY inside "BOAT RACE" in the footnotes; no other spaces anywhere (e.g. "57号機", "5号艇", "40.69%", "41走" have no spaces). "、" and "。" are Japanese punctuation. "※" in s4 T11 is the full-width reference mark.
- Wrapping: Any item not listed in this rule as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. These may wrap automatically: s2 T40, s3 T44, s4 T8, s4 T9, s4 T10, s4 T11. Each listed item is its own element; do not merge or split items. Wrapping must never add, remove or change characters.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8.
- Margins ~7% each side, left-aligned (except the right-aligned columns stated below). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s4): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote at the bottom in small #9fb3c8 (about 22px).
- Sizes at 1122x1402: headline T3 on s2-s4 white, about 56px (shrink slightly if needed to keep it on one line).

## s1 (cover)
- Base image: handoff/images/2026-11-19/cover.png (photorealistic kyotei boats on a lake course, mountains on the horizon, dark overcast sky in the top part). Use it as the photo background; keep the same boats and scene, do not redraw different boats. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (each on ONE line, never wrap): T2 in white about 60px (shrink if needed to stay on one line), then T3 in yellow about 130px, the biggest text in the series. Below it a short yellow horizontal bar, then subtitle T4 in white, about 40px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: びわこ6日目|11/19
- T2: 今日の12Rの6機を機歴で並べると
- T3: 5位〜39位
- T4: 6機で2連対率トップの12号機は機歴27位
- T5: データで読むボートレース

## s2 (the six motors, ordered by rank)
- Headline T3 (one line).
- A clean table card with 5 columns: rank, motor number, racer, boat (lane), official 2-place rate. Header row (about 26px, #9fb3c8): T4, T5, T6, T7, T8.
- 6 data rows with thin divider lines, evenly spaced. Rank in yellow #FFC400 about 44px ("位" same size as the digits); motor number white about 38px; racer white bold about 42px; boat white about 34px; 2-place rate white about 44px, right-aligned in its column. Row 5 (T29-T33, 磯部誠) gets a slightly brighter warm-tinted row background and its rate T33 is yellow #FFC400.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
  - Row 6: T34, T35, T36, T37, T38
- Under the table: T39 in yellow #FFC400, about 38px (one line). Footnote T40 at the bottom (may wrap).
- T1: 12Rの6機|びわこ
- T2: 2/4
- T3: 機歴の順と2連対率の順は別
- T4: 機歴
- T5: 号機
- T6: 選手
- T7: 枠
- T8: 2連対率
- T9: 5位
- T10: 57号機
- T11: 長田頼宗
- T12: 3号艇
- T13: 40.69%
- T14: 8位
- T15: 21号機
- T16: 遠藤エミ
- T17: 5号艇
- T18: 37.04%
- T19: 12位
- T20: 20号機
- T21: 宮地元輝
- T22: 1号艇
- T23: 37.50%
- T24: 14位
- T25: 66号機
- T26: 丸野一樹
- T27: 2号艇
- T28: 33.57%
- T29: 27位
- T30: 12号機
- T31: 磯部誠
- T32: 6号艇
- T33: 44.06%
- T34: 39位
- T35: 14号機
- T36: 山崎郡
- T37: 4号艇
- T38: 35.71%
- T39: 6機とも中央値32.645%を上回る
- T40: BOAT RACE公式の競走成績・番組表を独自に集計。機歴はびわこの2026/4/8〜11/18の開催分で、乗り手のクセを除いた展示タイムの速さで62機を並べた順位。2連対率は11/19の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算

## s3 (this series, 41 starts)
- Headline T3 (one line).
- A clean table card with 5 columns: rank, racer, exhibition top-2 count, top-2 finishes, wins. Header row (about 26px, #9fb3c8): T4, T5, T6, T7, T8.
- 6 data rows with thin divider lines, evenly spaced. Rank in yellow #FFC400 about 44px; racer white bold about 42px; the three count columns white about 44px, right-aligned in their columns. Row 3 (T19-T23, 宮地元輝) gets a slightly brighter warm-tinted row background.
  - Row 1: T9, T10, T11, T12, T13
  - Row 2: T14, T15, T16, T17, T18
  - Row 3: T19, T20, T21, T22, T23
  - Row 4: T24, T25, T26, T27, T28
  - Row 5: T29, T30, T31, T32, T33
  - Row 6: T34, T35, T36, T37, T38
- A 7th total row separated by a thicker divider and a warm-tinted background: T39 (white, about 36px) spanning the rank and racer columns, then T40, T41, T42 in yellow #FFC400 about 46px in the three count columns.
- Under the table: T43 in white, about 36px (one line). Footnote T44 at the bottom (may wrap).
- T1: 今節の成績|びわこ
- T2: 3/4
- T3: 6人の11/14〜11/18の41走
- T4: 機歴
- T5: 選手
- T6: 展示1〜2位
- T7: 2連対
- T8: 1着
- T9: 5位
- T10: 長田頼宗
- T11: 1/6
- T12: 4/6
- T13: 2/6
- T14: 8位
- T15: 遠藤エミ
- T16: 0/7
- T17: 4/7
- T18: 3/7
- T19: 12位
- T20: 宮地元輝
- T21: 4/7
- T22: 6/7
- T23: 2/7
- T24: 14位
- T25: 丸野一樹
- T26: 3/7
- T27: 5/7
- T28: 2/7
- T29: 27位
- T30: 磯部誠
- T31: 2/7
- T32: 4/7
- T33: 3/7
- T34: 39位
- T35: 山崎郡
- T36: 1/7
- T37: 4/7
- T38: 2/7
- T39: 6人の合計
- T40: 11/41
- T41: 27/41
- T42: 14/41
- T43: 宮地元輝は7走で2連対6回、展示1〜2位も4回
- T44: BOAT RACE公式の競走成績を独自に集計。びわこの11/14〜11/18。数字は回数/走数。展示1〜2位は各レース内の展示タイム順で、同タイムは上位扱い。進入はすべて枠どおり

## s4 (three points and summary)
- Headline T3 (one line).
- Three stacked point cards, each a dark translucent rounded box with a thin yellow left accent bar; inside each, one line of white text about 36px (shrink slightly to stay on one line): T4, T5, T6 (top to bottom).
- Below them, a card with a thin yellow border: small yellow title T7 (about 30px), then T8 in white about 32px (may wrap).
- Below the card: T9 in white, about 26px (may wrap). Then T10 in small #9fb3c8 (about 22px, may wrap). At the very bottom T11 in small #9fb3c8 (about 22px, may wrap).
- T1: まとめ|びわこ
- T2: 4/4
- T3: 数字で見る12Rの6機
- T4: 機歴の最上位は長田頼宗の57号機で5位
- T5: 2連対率が最も高い磯部誠の12号機は機歴27位
- T6: 遠藤エミは展示1〜2位0回でも1着3回
- T7: まとめ
- T8: 6機の機歴は5位から39位まで開きがあり、2連対率の順とは一致しません。今節は6人の41走で1着14回。
- T9: 展示タイムは直線寄りの指標で、まわり足は反映されにくく、着順は乗り手や枠にも左右されます。1人6〜7走の結果は大きく振れます。
- T10: BOAT RACE公式の競走成績・番組表を独自に集計。11/19のびわこ12R。機歴はびわこの2026/4/8〜11/18の開催分・62機中の順位
- T11: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only the slide PNGs (s1.png-s4.png) and report.json, then `git pull --rebase origin main` and `git push origin HEAD:main`.

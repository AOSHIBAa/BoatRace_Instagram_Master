# Slide spec: handoff/slides/2026-11-20-amagasaki-a1-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-20-amagasaki-a1-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 石田章央, 深井利寿 (寿 not 壽), 宮田龍馬 (龍 not 竜), 末永祐輝, 河村了 (three characters only), 鈴木孝明, 大場恒季, 西野翔太, 土屋蘭 (three characters only). Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. "A1" and "B1" are a half-width capital letter followed by the half-width digit 1. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "・" is the small Japanese middle dot: it separates race numbers in s2 T10/T14/T18/T22 and s3 T25, separates names in s5 T5, and is ALSO the first character of each line s5 T4-T7 (draw it as "・", never as a round bullet "•", and do not add any other bullet). "%", "/", ".", "R" and digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes; no other spaces anywhere (e.g. "54号機", "4R・12R", "20.14%", "1号艇" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T25, s3 T27, s4 T33; s3 T26; s5 T4-T9. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the rank column in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px. Table header row about 30px in #9fb3c8. Table cells: racer name white bold about 48px, motor white about 44px, race / rate column about 40px, rank column about 66px digits. In ranks, "位" is about 45% of the digit height, on the same line. In rates, "%" is normal size.

## s1 (cover)
- Base image: handoff/images/2026-11-20/cover.png (one white kyotei boat with a racer in a blue suit and white helmet running straight at night, stadium floodlights and blurred city lights behind, spray on the left, dark empty sky in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 90px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 44px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 尼崎|新節初日
- T2: A1級8人のモーターを
- T3: 機歴で格付け
- T4: 63機中50位以下に4人
- T5: データで読むボートレース

## s2 (first half of the 8 A1 racers, by motor rank)
- Headline T3 (one line).
- A clean table card with 4 columns: racer, motor, today's races (#9fb3c8), rank (big, right-aligned; 5位 and 7位 in yellow #FFC400, 19位 and 32位 in white). Header row: T4, T5, T6, T7.
- 4 data rows with thin divider lines, evenly spaced and generous height.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Rows 1 and 2 (5位 and 7位) get a slightly brighter, warm-tinted row background.
- Under the table: T24 in yellow, about 42px (one line). Footnote T25 at the bottom (may wrap).
- T1: モーター格付け|尼崎
- T2: 2/5
- T3: A1級8人を機歴順に、前半の4人
- T4: 選手
- T5: 号機
- T6: 今日
- T7: 順位
- T8: 石田章央
- T9: 54号機
- T10: 4R・12R
- T11: 5位
- T12: 深井利寿
- T13: 36号機
- T14: 6R・12R
- T15: 7位
- T16: 宮田龍馬
- T17: 16号機
- T18: 8R・12R
- T19: 19位
- T20: 末永祐輝
- T21: 21号機
- T22: 7R・11R
- T23: 32位
- T24: 機歴10位以内は石田章央と深井利寿の2人
- T25: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は尼崎の2026/4/17〜11/17の開催分で、乗り手のクセを除いた展示タイムの速さで63機を並べた順位。出走は11/20の番組表

## s3 (second half: ranks 50 and below)
- Headline T3 (one line).
- Same table layout and sizes as s2, 4 columns: racer, motor, official 2-place rate (white, about 40px), rank. The rank column numbers are in warning red #ff8a8a instead of yellow. Header row: T4, T5, T6, T7.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
- Under the table: T24 in yellow, about 40px (one line). Then T25 white, about 38px (one line). Then T26 in warning red #ff8a8a, about 32px (may wrap). Footnote T27 at the bottom (may wrap).
- T1: モーター格付け|尼崎
- T2: 3/5
- T3: 後半の4人は機歴50位以下
- T4: 選手
- T5: 号機
- T6: 2連対率
- T7: 順位
- T8: 河村了
- T9: 6号機
- T10: 20.14%
- T11: 50位
- T12: 鈴木孝明
- T13: 20号機
- T14: 27.50%
- T15: 51位
- T16: 大場恒季
- T17: 60号機
- T18: 30.67%
- T19: 55位
- T20: 西野翔太
- T21: 49号機
- T22: 28.48%
- T23: 56位
- T24: 4機とも2連対率は63機の中央値33.13%未満
- T25: 4人の出走は1R・3R・5R・7R・10R・12R
- T26: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T27: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は尼崎の2026/4/17〜11/17の開催分・63機中の順位。2連対率は11/20の番組表の値で、中央値は63機それぞれの最新の番組表の値から計算

## s4 (12R: all six are A1)
- Headline T3 (one line, keep it big).
- Table card with 4 columns: lane (white, about 40px), racer, motor, rank (right-aligned). Header row: T4, T5, T6, T7.
- 6 data rows with thin divider lines, evenly spaced. Rank color: 5位 and 7位 in yellow #FFC400; 19位 in white; 50位, 51位, 56位 in warning red #ff8a8a.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
- Under the table: T32 in yellow, about 42px (one line). Footnote T33 at the bottom (may wrap).
- T1: モーター格付け|尼崎
- T2: 4/5
- T3: 12Rは6人全員A1級
- T4: 枠
- T5: 選手
- T6: 号機
- T7: 順位
- T8: 1号艇
- T9: 宮田龍馬
- T10: 16号機
- T11: 19位
- T12: 2号艇
- T13: 石田章央
- T14: 54号機
- T15: 5位
- T16: 3号艇
- T17: 河村了
- T18: 6号機
- T19: 50位
- T20: 4号艇
- T21: 深井利寿
- T22: 36号機
- T23: 7位
- T24: 5号艇
- T25: 西野翔太
- T26: 49号機
- T27: 56位
- T28: 6号艇
- T29: 鈴木孝明
- T30: 20号機
- T31: 51位
- T32: 機歴の上位2機は2号艇と4号艇
- T33: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は尼崎の2026/4/17〜11/17の開催分で、乗り手のクセを除いた展示タイムの速さで63機を並べた順位。出走は11/20の番組表

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "石田章央と深井利寿の2人" in T4, "50位以下" in T5, "5位から56位まで" in T6, "23号機" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 34px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: モーター格付け|尼崎
- T2: 5/5
- T3: まとめ
- T4: ・A1級8人のうち機歴10位以内は石田章央と深井利寿の2人
- T5: ・河村了・鈴木孝明・大場恒季・西野翔太の4人は50位以下
- T6: ・12Rは6人全員A1級で、機歴は5位から56位まで
- T7: ・63機中1位の23号機はB1級の土屋蘭、3Rと9Rに出走
- T8: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-20-amagasaki-a1-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

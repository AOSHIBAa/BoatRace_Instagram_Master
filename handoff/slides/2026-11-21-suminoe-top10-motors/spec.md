# Slide spec: handoff/slides/2026-11-21-suminoe-top10-motors

Slides: s1.png ... s5.png (5 slides). Format: REEL (each slide shown about 4 seconds on a phone, so keep layouts simple and numbers very big).
Report: write handoff/slides/2026-11-21-suminoe-top10-motors/report.json  {"slides":[{"file":"s1.png","size_px":"WxH","attempts":N}],"notes":""}

## Absolute rules (all slides)
- Use the built-in image generation tool. Do NOT draw with code, HTML, SVG, PIL or any font rendering library.
- Portrait 4:5 (e.g. 1122x1402). All 5 slides share ONE design system so they look like one series.
- Render EVERY text item EXACTLY as written below (also in expected.json): same characters, digits, decimal points, punctuation, half/full width. Correct Japanese kanji/kana. Racer names must be exact: 鈴木勝博, 冨田秀幸 (冨 with no dot on top, not 富), 竹井貴史, 山田佑樹 (佑 not 祐), 渡邉俊介 (邉 not 辺 or 邊), 山下拓巳 (巳 not 己 or 已), 福岡泉水, 石井孝之, 上田洋平, 澁川夏 (澁 not 渋; three characters only), 齋藤和政 (齋 not 斎 or 斉), 平田健之佑 (five characters), 阿久根芳仁. Do not translate, paraphrase, round, or add any other text, numbers, logos, watermarks, signatures, arrows-with-text or flags.
- Forbidden words anywhere: "AI", "Claude", "ChatGPT", "Codex", "OpenAI", "Gemini", "生成".
- No human faces. No official BOAT RACE logos or marks; "BOAT RACE" in footnotes is plain text in the footnote font.
- Symbols: There are NO parentheses and NO question marks anywhere in this series. "A1" is a half-width capital letter A followed by the half-width digit 1. Every "|" is a half-width ASCII vertical bar with NO spaces around it. "〜" is the Japanese wave dash U+301C (not the full-width tilde "～"). "・" is the small Japanese middle dot: it separates race numbers in s2 T10/T14/T18 and s3 T14/T18/T26, separates numbers in s4 T32 and s5 T7, appears inside the footnotes s2 T29 (once), s3 T30 (twice) and s4 T34 (once), and is ALSO the first character of each line s5 T4-T7 (draw it as "・", never as a round bullet "•", and do not add any other bullet). "%", "/", ".", "R" and digits are half-width. The ONLY half-width spaces in the whole series are inside "BOAT RACE" in the footnotes; no other spaces anywhere (e.g. "80号機", "4R・11R", "47.10%", "1号艇" have no spaces). "、" and "。" are Japanese punctuation. "※" in s5 T9 is the full-width reference mark.
- Wrapping: Any item not listed here as may-wrap must stay on ONE line; if it is too long, shrink its font slightly rather than wrap. May wrap: footnotes s2 T29, s3 T30, s4 T34; s4 T33; s5 T4-T9. Wrapping must never add, remove or change characters. Each item is its own element; do not merge or split items.
- After generating, read every text item yourself and compare character by character. If ANY item differs, regenerate that slide (max 3 attempts per slide).

## Design system
- Background: deep navy gradient (#071a33 to #0b2a4a), subtle warm glow top-right, faint blue glow bottom-left.
- Font look: bold modern Japanese gothic (sans-serif), very legible on a phone.
- Colors: accent yellow #FFC400, main text white, secondary text #9fb3c8, warning red #ff8a8a.
- Margins ~7% each side, left-aligned (except the rank column in tables, right-aligned). Cards: dark translucent rounded boxes with thin semi-transparent borders.
- Data slides (s2-s5): small yellow label T1 top-left (about 30px), page number T2 top-right in #9fb3c8 (about 28px), footnote (last item) at the bottom in small #9fb3c8 (about 22px; s5 T9 about 24px).
- Sizes at 1122x1402: headline T3 on s2-s5 white, about 58px. Table header row about 30px in #9fb3c8. Table cells: racer name white bold about 48px, motor white about 44px, race / lane column about 40px, rank column about 66px digits. In ranks, "位" is about 45% of the digit height, on the same line.

## s1 (cover)
- Base image: handoff/images/2026-11-21/cover.png (one white kyotei boat with a racer in a yellow suit and white helmet turning left around an orange-and-white turn buoy in warm low sunlight, big white spray behind, dark trees in the top half). Use it as the photo background; keep the same boat and scene, do not redraw a different boat. Keep the bottom ~45% of the photo clearly visible. If that file does not exist, use a plain navy background with no photo.
- Darken the top half with a navy gradient. Top-left small yellow label T1 (about 30px). Huge title on two lines (about 90px, each on ONE line, never wrap): T2 in white, then T3 in yellow. Below it a short yellow horizontal bar, then subtitle T4 in white, about 44px, on a dark translucent pill so it reads clearly (one line). Footer T5 small (about 28px), white at 80% opacity, bottom-left over the photo with a subtle shadow.
- T1: 住之江|新節初日
- T2: 機歴トップ10の
- T3: モーターは誰の手に
- T4: 65機中1〜10位が全機出走
- T5: データで読むボートレース

## s2 (motor ranks 1-5)
- Headline T3 (one line).
- A clean table card with 4 columns: racer, motor, today's races (#9fb3c8), rank (big, right-aligned; all five data ranks in yellow #FFC400). Header row T4, T5, T6, T7 is all in #9fb3c8 (including 順位).
- 5 data rows with thin divider lines, evenly spaced and generous height.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Row 1 (1位) gets a slightly brighter, warm-tinted row background.
- Under the table: T28 in yellow, about 34px (one line; it is long, so keep it small enough to fit). Footnote T29 at the bottom (may wrap).
- T1: モーター格付け|住之江
- T2: 2/5
- T3: 機歴1〜5位の5機と今日の出番
- T4: 選手
- T5: 号機
- T6: 今日
- T7: 順位
- T8: 鈴木勝博
- T9: 80号機
- T10: 4R・11R
- T11: 1位
- T12: 冨田秀幸
- T13: 38号機
- T14: 1R・6R
- T15: 2位
- T16: 竹井貴史
- T17: 35号機
- T18: 3R・12R
- T19: 3位
- T20: 山田佑樹
- T21: 20号機
- T22: 6R
- T23: 4位
- T24: 渡邉俊介
- T25: 79号機
- T26: 10R
- T27: 5位
- T28: 1位の80号機は2連対率も65機中1位の47.10%
- T29: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は住之江の2026/4/3〜11/10の開催分で、乗り手のクセを除いた展示タイムの速さで65機を並べた順位。出走と2連対率は11/21の番組表。2連対率の順位は65機それぞれの最新の番組表の値で比較

## s3 (motor ranks 6-10)
- Headline T3 (one line).
- Same table layout and sizes as s2, 4 columns: racer, motor, today's races (#9fb3c8), rank (all five data ranks in yellow #FFC400). Header row T4, T5, T6, T7 is all in #9fb3c8 (including 順位).
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
- Rows 3 and 5 (8位 and 10位) get a slightly brighter, warm-tinted row background.
- Under the table: T28 in yellow, about 34px (one line; it is long, so keep it small enough to fit). Then T29 in white, about 36px (one line). Footnote T30 at the bottom (may wrap).
- T1: モーター格付け|住之江
- T2: 3/5
- T3: 機歴6〜10位の5機と今日の出番
- T4: 選手
- T5: 号機
- T6: 今日
- T7: 順位
- T8: 山下拓巳
- T9: 11号機
- T10: 5R
- T11: 6位
- T12: 福岡泉水
- T13: 51号機
- T14: 3R・9R
- T15: 7位
- T16: 石井孝之
- T17: 30号機
- T18: 5R・10R
- T19: 8位
- T20: 上田洋平
- T21: 64号機
- T22: 2R
- T23: 9位
- T24: 澁川夏
- T25: 36号機
- T26: 3R・8R
- T27: 10位
- T28: 30号機は2連対率25.37%、36号機は19.08%
- T29: どちらも65機の中央値33.58%未満
- T30: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は住之江の2026/4/3〜11/10の開催分・65機中の順位。2連対率は11/21の番組表の値で、中央値は65機それぞれの最新の番組表の値から計算

## s4 (3R: three top-10 motors)
- Headline T3 (one line, keep it big).
- Table card with 4 columns: lane (white, about 40px), racer, motor, rank (right-aligned). Header row T4, T5, T6, T7 is all in #9fb3c8.
- 6 data rows with thin divider lines, evenly spaced. Rank color: 7位, 3位 and 10位 in yellow #FFC400; 32位, 39位 and 15位 in white. Rows 1, 2 and 5 get a slightly brighter, warm-tinted row background.
  - Row 1: T8, T9, T10, T11
  - Row 2: T12, T13, T14, T15
  - Row 3: T16, T17, T18, T19
  - Row 4: T20, T21, T22, T23
  - Row 5: T24, T25, T26, T27
  - Row 6: T28, T29, T30, T31
- Under the table: T32 in yellow, about 42px (one line). Then T33 in warning red #ff8a8a, about 30px (may wrap). Footnote T34 at the bottom (may wrap).
- T1: モーター格付け|住之江
- T2: 4/5
- T3: 3Rは機歴10位以内が3機
- T4: 枠
- T5: 選手
- T6: 号機
- T7: 順位
- T8: 1号艇
- T9: 福岡泉水
- T10: 51号機
- T11: 7位
- T12: 2号艇
- T13: 竹井貴史
- T14: 35号機
- T15: 3位
- T16: 3号艇
- T17: 齋藤和政
- T18: 73号機
- T19: 32位
- T20: 4号艇
- T21: 平田健之佑
- T22: 69号機
- T23: 39位
- T24: 5号艇
- T25: 澁川夏
- T26: 36号機
- T27: 10位
- T28: 6号艇
- T29: 阿久根芳仁
- T30: 55号機
- T31: 15位
- T32: 10位以内の3機は1・2・5号艇
- T33: 展示タイムは直線寄りの指標で、まわり足は反映されにくい
- T34: BOAT RACE公式の競走成績・番組表を独自に集計。機歴は住之江の2026/4/3〜11/10の開催分で、乗り手のクセを除いた展示タイムの速さで65機を並べた順位。出走は11/21の番組表

## s5 (summary)
- Headline T3 (まとめ).
- A card containing the four lines T4-T7, white, about 40px, generous line spacing; each line starts with "・" exactly as written (may wrap inside the card). Only these parts are yellow #FFC400: "10機がすべて" in T4, "竹井貴史と渡邉俊介の2人" in T5, "中央値未満" in T6, "3機" in T7; everything else in those lines is white.
- Below the card: T8 in white, about 34px.
- At the bottom, T9 in small #9fb3c8 (about 24px).
- T1: モーター格付け|住之江
- T2: 5/5
- T3: まとめ
- T4: ・65機中、機歴1〜10位の10機がすべて今日出走
- T5: ・10機に乗る10人のうちA1級は竹井貴史と渡邉俊介の2人
- T6: ・8位の30号機と10位の36号機は2連対率が中央値未満
- T7: ・3Rは機歴10位以内の3機が1・2・5号艇に入る
- T8: 進入や枠とあわせて、モーターの見方の参考にしてください。
- T9: ※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。

## Commit
Commit only s1.png-s5.png and report.json in handoff/slides/2026-11-21-suminoe-top10-motors/, then `git pull --rebase origin main` and `git push origin HEAD:main`.

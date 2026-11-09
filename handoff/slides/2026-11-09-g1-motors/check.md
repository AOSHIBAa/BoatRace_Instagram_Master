# 照合の記録(2026-11-09 g1-motors)
- 1回目(Codex): check_slide_text.py で11件NG。GⅠ(U+2160)が「GI」、全角かっこ・全角？が半角として書き起こされた(文字の中身は一致)。
- 指示書を「G1」・半角かっこ・半角?に変更し、Codexに全5枚を1回作り直し依頼。
- 2回目(Codex): s1・s5 は一致。s2・s3・s4 はかっこ・?が全角として書き起こされ6件NG(transcript_v2.json)。
- 手順書どおり、s2〜s4 は scripts/slides.py の部品で expected.json の文字をそのまま使って作り直し(scripts/fallback_2026-11-09-g1-motors.py)。Codex版は codex_s2〜s4.png として保存(投稿には使わない)。
- 目視: 全5枚の文字・数字を expected.json と照合。人物の顔・ロゴ・「AI」の文字なし。表紙の艇は競艇の艇に見える。
- s5 の行頭「・」は丸い記号ぎみに描かれている(Codex報告どおり。書き起こしでは一致)。

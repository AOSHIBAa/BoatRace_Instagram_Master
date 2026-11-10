# 照合の記録(2026-11-10 mikuni-motors)
- 1回目(Codex書き起こし transcript_v1.json): check_slide_text.py で1件NG(s4 T12に「の」が1文字多い)。目視で、s2 T18・s4 T4 の「宮嵜」が「宮寄」に近い字形になっているのも確認(書き起こしでは一致扱い)。
- Codex に s2・s4 を1回作り直し依頼。s4 T12 は直ったが、Codex自身が「嵜」を3回とも描けなかったと報告。
- 2回目(transcript_v2.json): s2 T18・s4 T4 が「宮寄隆太郎」で2件NG。
- 手順書どおり、s2・s4 は scripts/slides.py の部品で expected.json の文字をそのまま使って作り直し(scripts/fallback_2026-11-10-mikuni-motors.py)。Codex版は codex_s2.png・codex_s4.png として保存(投稿には使わない)。
- 目視: 全5枚の文字・数字を expected.json と照合。人物の顔・ロゴ・「AI」の文字なし。表紙の艇は競艇の艇に見える。
- s5 の行頭「・」は丸い記号ぎみ(Codex報告どおり。書き起こしでは一致)。

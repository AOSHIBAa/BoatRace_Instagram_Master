"""data.json から expected.json を作る(数字は assert で data.json と突き合わせる)。"""
import json
from pathlib import Path
F = Path("handoff/slides/2026-11-27-biwako-hidden-motors")
d = json.load(open(F / "data.json", encoding="utf-8"))
H = {h["motor"]: h for h in d["hidden"]}; S = d["summary"]
assert d["n_motors"] == 62 and d["period_start"] == "2026-04-08" and abs(d["motor_2r_median"] - 32.21) < 1e-9
assert [h["motor"] for h in d["hidden"]] == ["17", "25", "58", "51"] and [h["rank"] for h in d["hidden"]] == [4, 6, 9, 11]
assert S["17"]["rides"] == 0
name = {k: S[k]["names"][0] for k in ("25", "58", "51")}
assert name == {"25": "尾形栄治", "58": "栗原一馬", "51": "服部幸男"}
def frac(k, f): return f"{S[k][f]}/{S[k]['rides']}"
a = S["all"]; assert (a["rides"], a["ex_top2"], a["top2"], a["wins"]) == (18, 10, 6, 2)
win58 = [r for r in d["rides"] if r["motor"] == "58" and r["pos"] == "1"]
assert len(win58) == 1 and win58[0]["date"] == "2026-11-25" and win58[0]["race"] == 4 and win58[0]["sanrentan"] == ["1-2-6", 11450]
assert S["58"]["ex_top2"] == 5 and S["58"]["rides"] == 6 and S["58"]["top2"] == 3
today = [(t["race"], t["boat"], t["name"], t["motor"]) for t in d["today"]]
assert today == [(1, 3, "栗原一馬", "58"), (3, 2, "服部幸男", "51"), (5, 2, "尾形栄治", "25"), (6, 4, "栗原一馬", "58"), (9, 5, "服部幸男", "51")]
DIS = "※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。"
e = {
 "s1": {"T1": "びわこ5日目|11/27", "T2": "2連対率は平凡でも", "T3": "機歴上位の3機",
        "T4": f"58号機は今節{S['58']['rides']}走で展示1〜2位{S['58']['ex_top2']}回", "T5": "データで読むボートレース"},
 "s2": {"T1": "機歴上位の3機|びわこ", "T2": "2/4", "T3": "展示は速いのに2連対率は中央値以下",
        "T4": "機歴", "T5": "号機", "T6": "今節の選手", "T7": "2連対率"},
 "s3": {"T1": "今節の成績|びわこ", "T2": "3/4", "T3": "3機の今節18走",
        "T4": "号機", "T5": "選手", "T6": "展示1〜2位", "T7": "2連対", "T8": "1着"},
 "s4": {"T1": "今日の出番|びわこ", "T2": "4/4", "T3": "今日11/27の出番",
        "T4": "レース", "T5": "枠", "T6": "選手", "T7": "号機"},
}
i = 8
for k in ("25", "58", "51"):
    h = H[k]
    e["s2"].update({f"T{i}": f"{h['rank']}位", f"T{i+1}": f"{k}号機", f"T{i+2}": name[k], f"T{i+3}": f"{h['motor_2r']:.2f}%"}); i += 4
e["s2"]["T20"] = f"62機の中央値は{d['motor_2r_median']:.2f}%"
e["s2"]["T21"] = ("BOAT RACE公式の競走成績と番組表を独自に集計。機歴はびわこの2026/4/8〜11/26の開催分で、乗り手のクセを除いた展示タイムの速さを、走数とばらつきも加味して62機で並べた順位。"
                  "2連対率は11/27の番組表の値で、中央値は62機それぞれの最新の番組表の値から計算。同じ条件で機歴4位の17号機は今節の出走なし")
i = 9
for k in ("25", "58", "51"):
    e["s3"].update({f"T{i}": f"{k}号機", f"T{i+1}": name[k], f"T{i+2}": frac(k, "ex_top2"), f"T{i+3}": frac(k, "top2"), f"T{i+4}": frac(k, "wins")}); i += 5
e["s3"].update({"T24": "3機の合計", "T25": f"{a['ex_top2']}/{a['rides']}", "T26": f"{a['top2']}/{a['rides']}", "T27": f"{a['wins']}/{a['rides']}",
                "T28": f"展示1〜2位は{a['rides']}走中{a['ex_top2']}回、2連対は{a['top2']}回",
                "T29": "4日間だけの結果で、数字は大きく振れる",
                "T30": "BOAT RACE公式の競走成績を独自に集計。びわこ11/23〜11/26。数字は回数/走数。展示1〜2位は各レース内の展示タイムの順で、同タイムは上位扱い。展示タイムは直線寄りの指標で、まわり足は反映されにくい"})
i = 8
for rc, bt, nm, mo in today:
    e["s4"].update({f"T{i}": f"{rc}R", f"T{i+1}": f"{bt}号艇", f"T{i+2}": nm, f"T{i+3}": f"{mo}号機"}); i += 4
e["s4"].update({"T28": "まとめ",
                "T29": f"3機は今節{a['rides']}走で展示1〜2位{a['ex_top2']}回、2連対{a['top2']}回。58号機は11/25の4Rで1着、3連単11450円。",
                "T30": "展示タイムは直線寄りの指標で、まわり足は反映されにくく、着順は乗り手や枠にも左右されます。",
                "T31": "BOAT RACE公式の競走成績、番組表、払戻金を独自に集計。今日の出番は11/27の番組表。払戻金は100円あたり",
                "T32": DIS})
(F / "expected.json").write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(e, ensure_ascii=False, indent=1))

"""2026-11-27 びわこ5日目: 2連対率は中央値以下でも機歴上位の「隠れ上位」モーターの今節(11/23〜11/26)と今日の出番。
機歴の順位は motors.json(びわこ)の並び順(乗り手補正後の展示偏差の t 値の昇順)。展示順位はレース内昇順、同タイムは上位扱い。
"""
import csv, json, collections
from pathlib import Path
V = "びわこ"; DAYS = ["2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26"]; TODAY = "2026-11-27"
F = Path("handoff/slides/2026-11-27-biwako-hidden-motors")
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[V]
ms = m["motors"]
rank = {str(x["motor"]): (i + 1, x) for i, x in enumerate(ms)}
hidden = [str(x["motor"]) for x in ms if x["hidden"]]
out = {"venue": V, "period_start": m["start"], "n_motors": len(ms), "motor_2r_median": m["motor_2r_median"],
       "hidden": [{"motor": k, "rank": rank[k][0], "motor_2r": rank[k][1]["motor_2r"], "t": rank[k][1]["t"],
                   "starts": rank[k][1]["starts"], "ex_top2_all": rank[k][1]["ex_top2"]} for k in hidden],
       "rides": [], "today": [], "summary": {}}
pay = {}
for d in DAYS:
    for r in csv.DictReader(open(f"data/payouts/{d}.csv", encoding="utf-8")):
        if r["venue"] == V and r["ticket_type"] in ("tansho", "sanrensho"):
            pay[(d, r["race_number"], r["ticket_type"])] = (r["winning_combination"], int(r["payout"]))
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(f"data/results/{d}.csv", encoding="utf-8")):
        if r["venue"] == V:
            by[r["race"]].append(r)
    for rn, es in sorted(by.items(), key=lambda x: int(x[0])):
        ex = [float(e["exhibition"]) for e in es if e["exhibition"] and float(e["exhibition"]) > 0]
        for e in es:
            if e["motor"] in hidden:
                t = float(e["exhibition"])
                out["rides"].append({"date": d, "race": int(rn), "boat": int(e["boat"]), "entrance": e["entrance"],
                    "name": e["racer_name"], "motor": e["motor"], "ex": t, "ex_rank": 1 + sum(1 for x in ex if x < t),
                    "n_ex": len(ex), "pos": e["position"],
                    "tansho": pay.get((d, rn, "tansho")), "sanrentan": pay.get((d, rn, "sanrensho"))})
for k in hidden:
    rs = [r for r in out["rides"] if r["motor"] == k]
    out["summary"][k] = {"rides": len(rs), "ex_top2": sum(r["ex_rank"] <= 2 for r in rs),
                         "top2": sum(r["pos"] in ("1", "2") for r in rs), "wins": sum(r["pos"] == "1" for r in rs),
                         "names": sorted({r["name"] for r in rs})}
rs = out["rides"]
out["summary"]["all"] = {"rides": len(rs), "ex_top2": sum(r["ex_rank"] <= 2 for r in rs),
                         "top2": sum(r["pos"] in ("1", "2") for r in rs), "wins": sum(r["pos"] == "1" for r in rs)}
for r in csv.DictReader(open(f"data/program/{TODAY}.csv", encoding="utf-8")):
    if r["venue"] == V and r["motor"] in hidden:
        out["today"].append({"race": int(r["race"]), "boat": int(r["boat"]), "name": r["racer_name"],
                             "class": r["racer_class"], "motor": r["motor"], "motor_2r": r["motor_2r"]})
(F / "data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out["hidden"], ensure_ascii=False)); print(json.dumps(out["summary"], ensure_ascii=False))
for r in out["today"]: print(r)

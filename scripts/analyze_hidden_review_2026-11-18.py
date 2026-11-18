"""2026-11-18 びわこ5日目: 2連対率は平凡でも機歴上位の3機(25・17・58号機)の11/14〜11/17の成績と、今日の出番。
順位は motors.json(びわこ 2026/4/8〜11/17)の ex_adj 昇順。展示順位はレース内昇順、同タイムは上位扱い。
"""
import csv, json, collections
from pathlib import Path
V = "びわこ"; DAYS = ["2026-11-14", "2026-11-15", "2026-11-16", "2026-11-17"]; TODAY = "2026-11-18"
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[V]
ms = sorted(m["motors"], key=lambda x: x["ex_adj"])
rank = {str(x["motor"]): (i + 1, x) for i, x in enumerate(ms)}
hidden = [str(x["motor"]) for x in ms if x["hidden"]]
out = {"venue": V, "period_start": m["start"], "n_motors": len(ms), "motor_2r_median": m["motor_2r_median"],
       "hidden": [{"motor": k, "rank": rank[k][0], "motor_2r": rank[k][1]["motor_2r"], "t": rank[k][1]["t"]} for k in hidden],
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
                ties = sum(1 for x in ex if x == t) - 1
                out["rides"].append({"date": d, "race": int(rn), "boat": int(e["boat"]), "entrance": e["entrance"],
                    "name": e["racer_name"], "motor": e["motor"], "ex": t, "ex_rank": 1 + sum(1 for x in ex if x < t),
                    "ex_ties": ties, "pos": e["position"],
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
Path("handoff/slides/2026-11-18-biwako-hidden-motors/data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out["hidden"], ensure_ascii=False)); print(json.dumps(out["summary"], ensure_ascii=False))
for r in rs: print(r)
for r in out["today"]: print(r)

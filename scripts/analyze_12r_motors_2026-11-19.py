"""2026-11-19 びわこ6日目: 12R(A1級6人)のモーター6機を機歴で格付けし、11/14〜11/18の今節成績を集計。
順位は motors.json(びわこ 2026/4/8〜11/18)の ex_adj 昇順。展示順位はレース内昇順、同タイムは上位扱い。
"""
import csv, json, collections
from pathlib import Path
V = "びわこ"; DAYS = ["2026-11-14", "2026-11-15", "2026-11-16", "2026-11-17", "2026-11-18"]; TODAY = "2026-11-19"; RACE = "12"
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[V]
ms = sorted(m["motors"], key=lambda x: x["ex_adj"])
rank = {str(x["motor"]): (i + 1, x) for i, x in enumerate(ms)}
entry = [r for r in csv.DictReader(open(f"data/program/{TODAY}.csv", encoding="utf-8")) if r["venue"] == V and r["race"] == RACE]
motors = [e["motor"] for e in entry]
out = {"venue": V, "period_start": m["start"], "n_motors": len(ms), "motor_2r_median": m["motor_2r_median"], "entry": [], "rides": [], "summary": {}}
for e in entry:
    rk, x = rank[e["motor"]]
    out["entry"].append({"boat": int(e["boat"]), "name": e["racer_name"], "class": e["racer_class"], "motor": e["motor"],
                         "motor_2r": e["motor_2r"], "rank": rk, "t": x["t"], "ex_adj": x["ex_adj"], "hidden": x["hidden"], "starts": x["starts"]})
pay = {}
for d in DAYS:
    for r in csv.DictReader(open(f"data/payouts/{d}.csv", encoding="utf-8")):
        if r["venue"] == V and r["ticket_type"] in ("tansho", "sanrensho"):
            pay[(d, r["race_number"], r["ticket_type"])] = (r["winning_combination"], int(r["payout"]))
    by = collections.defaultdict(list)
    for r in csv.DictReader(open(f"data/results/{d}.csv", encoding="utf-8")):
        if r["venue"] == V: by[r["race"]].append(r)
    for rn, es in sorted(by.items(), key=lambda x: int(x[0])):
        ex = [float(e["exhibition"]) for e in es if e["exhibition"] and float(e["exhibition"]) > 0]
        for e in es:
            if e["motor"] in motors:
                t = float(e["exhibition"]) if e["exhibition"] else 0
                out["rides"].append({"date": d, "race": int(rn), "boat": int(e["boat"]), "entrance": e["entrance"], "name": e["racer_name"],
                    "motor": e["motor"], "ex": t, "ex_rank": 1 + sum(1 for x in ex if x < t) if t > 0 else None,
                    "pos": e["position"], "tansho": pay.get((d, rn, "tansho")), "sanrentan": pay.get((d, rn, "sanrensho"))})
for k in motors:
    rs = [r for r in out["rides"] if r["motor"] == k]
    out["summary"][k] = {"rides": len(rs), "ex_top2": sum((r["ex_rank"] or 9) <= 2 for r in rs), "top2": sum(r["pos"] in ("1", "2") for r in rs),
                         "wins": sum(r["pos"] == "1" for r in rs), "names": sorted({r["name"] for r in rs}), "pos": [r["pos"] for r in rs]}
rs = out["rides"]
out["summary"]["all"] = {"rides": len(rs), "ex_top2": sum((r["ex_rank"] or 9) <= 2 for r in rs), "top2": sum(r["pos"] in ("1", "2") for r in rs), "wins": sum(r["pos"] == "1" for r in rs)}
Path("handoff/slides/2026-11-19-biwako-12r-motors/data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for e in out["entry"]: print(e)
for k, v in out["summary"].items(): print(k, v)
for r in rs: print(r)

"""2026-11-22 三国2日目: 3Rに機歴10位以内のモーターが4機(2・3・7・10位)。
順位は motors.json(三国 2026/4/5〜11/21)の ex_adj 昇順。4機の初日11/21の成績(展示順位はレース内昇順、同タイムは上位扱い)と払戻金。
"""
import csv, json, collections
from pathlib import Path
V = "三国"; Y = "2026-11-21"; TODAY = "2026-11-22"; OUT = "handoff/slides/2026-11-22-mikuni-3r-top10"
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[V]
ms = sorted(m["motors"], key=lambda x: x["ex_adj"])
rank = {str(x["motor"]): (i + 1, x) for i, x in enumerate(ms)}
prog = [r for r in csv.DictReader(open(f"data/program/{TODAY}.csv", encoding="utf-8")) if r["venue"] == V]
out = {"venue": V, "period_start": m["start"], "n_motors": len(ms), "motor_2r_median": m["motor_2r_median"],
       "race3": [], "top10_by_race": {}, "day1": [], "today_top4": []}
for r in prog:
    rk = rank[r["motor"]][0]
    if r["race"] == "3":
        out["race3"].append({"boat": int(r["boat"]), "name": r["racer_name"], "class": r["racer_class"], "motor": r["motor"],
                             "rank": rk, "motor_2r": float(r["motor_2r"]), "hidden": rank[r["motor"]][1]["hidden"],
                             "t": rank[r["motor"]][1]["t"], "starts": rank[r["motor"]][1]["starts"]})
    if rk <= 10:
        out["top10_by_race"].setdefault(r["race"], []).append(rk)
top4 = [e["motor"] for e in out["race3"] if e["rank"] <= 10]
for r in prog:
    if r["motor"] in top4:
        out["today_top4"].append({"race": int(r["race"]), "boat": int(r["boat"]), "name": r["racer_name"], "motor": r["motor"]})
pay = {}
for r in csv.DictReader(open(f"data/payouts/{Y}.csv", encoding="utf-8")):
    if r["venue"] == V and r["ticket_type"] in ("tansho", "sanrensho"):
        pay[(r["race_number"], r["ticket_type"])] = (r["winning_combination"], int(r["payout"]))
by = collections.defaultdict(list)
for r in csv.DictReader(open(f"data/results/{Y}.csv", encoding="utf-8")):
    if r["venue"] == V:
        by[r["race"]].append(r)
for rn, es in sorted(by.items(), key=lambda x: int(x[0])):
    ex = [float(e["exhibition"]) for e in es if e["exhibition"] and float(e["exhibition"]) > 0]
    for e in es:
        if e["motor"] in top4:
            t = float(e["exhibition"])
            out["day1"].append({"race": int(rn), "boat": int(e["boat"]), "entrance": e["entrance"], "name": e["racer_name"],
                                "motor": e["motor"], "rank": rank[e["motor"]][0], "ex": t,
                                "ex_rank": 1 + sum(1 for x in ex if x < t), "pos": e["position"] or None,
                                "tansho": pay.get((rn, "tansho")), "sanrentan": pay.get((rn, "sanrensho"))})
Path(OUT).mkdir(parents=True, exist_ok=True)
Path(f"{OUT}/data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=1))

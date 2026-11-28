"""2026-11-28 尼崎2日目: 機歴トップ10(motors.json の並び順)のモーターの初日11/27の成績と、今日11/28の出番。
展示順位はレース内昇順、同タイムは上位扱い。比較対象は同じ日の尼崎のそれ以外の出走。
"""
import csv, json, collections
from pathlib import Path
V = "尼崎"; DAY = "2026-11-27"; TODAY = "2026-11-28"
F = Path("handoff/slides/2026-11-28-amagasaki-top10-day1")
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[V]
ms = m["motors"]
top = [str(x["motor"]) for x in ms[:10]]
rank = {str(x["motor"]): i + 1 for i, x in enumerate(ms)}
p27 = {r["motor"]: r for r in csv.DictReader(open(f"data/program/{DAY}.csv", encoding="utf-8")) if r["venue"] == V}
prog = [r for r in csv.DictReader(open(f"data/program/{TODAY}.csv", encoding="utf-8")) if r["venue"] == V]
p28 = {r["motor"]: r for r in prog}
pay = {}
for r in csv.DictReader(open(f"data/payouts/{DAY}.csv", encoding="utf-8")):
    if r["venue"] == V and r["ticket_type"] in ("tansho", "sanrensho"):
        pay[(r["race_number"], r["ticket_type"])] = (r["winning_combination"], int(r["payout"]))
by = collections.defaultdict(list)
for r in csv.DictReader(open(f"data/results/{DAY}.csv", encoding="utf-8")):
    if r["venue"] == V:
        by[r["race"]].append(r)
rides = []
for rn, es in sorted(by.items(), key=lambda x: int(x[0])):
    ex = [float(e["exhibition"]) for e in es if e["exhibition"] and float(e["exhibition"]) > 0]
    for e in es:
        t = float(e["exhibition"]) if e["exhibition"] else 0
        rides.append({"race": int(rn), "boat": int(e["boat"]), "entrance": e["entrance"], "name": e["racer_name"],
                      "motor": e["motor"], "ex": t, "ex_rank": 1 + sum(1 for x in ex if x < t) if t > 0 else None,
                      "pos": e["position"], "top10": e["motor"] in top,
                      "tansho": pay.get((rn, "tansho")), "sanrentan": pay.get((rn, "sanrensho"))})
def summ(rs):
    return {"rides": len(rs), "ex_top2": sum(1 for r in rs if r["ex_rank"] and r["ex_rank"] <= 2),
            "top2": sum(r["pos"] in ("1", "2") for r in rs), "wins": sum(r["pos"] == "1" for r in rs)}
out = {"venue": V, "period_start": m["start"], "n_motors": len(ms), "motor_2r_median": m["motor_2r_median"],
       "races_day1": len(by), "top10": [], "today": [], "summary": {}}
for k in top:
    x = ms[rank[k] - 1]
    rs = [r for r in rides if r["motor"] == k]
    out["top10"].append({"rank": rank[k], "motor": k, "motor_2r_prog28": p28.get(k, {}).get("motor_2r"),
        "motor_2r_prog27": p27.get(k, {}).get("motor_2r"), "motor_2r_json": x["motor_2r"],
        "name": (p27.get(k) or p28.get(k) or {}).get("racer_name"), "class": (p27.get(k) or p28.get(k) or {}).get("racer_class"),
        "ride_list": [{kk: r[kk] for kk in ("race", "boat", "entrance", "ex", "ex_rank", "pos", "sanrentan")} for r in rs],
        **summ(rs)})
out["summary"]["top10"] = summ([r for r in rides if r["top10"]])
out["summary"]["others"] = summ([r for r in rides if not r["top10"]])
out["summary"]["all"] = summ(rides)
for r in prog:
    if r["motor"] in top:
        out["today"].append({"race": int(r["race"]), "boat": int(r["boat"]), "name": r["racer_name"], "class": r["racer_class"],
                             "motor": r["motor"], "rank": rank[r["motor"]], "motor_2r": r["motor_2r"]})
out["today"].sort(key=lambda r: (r["race"], r["boat"]))
(F / "data.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for t in out["top10"]:
    print(t["rank"], t["motor"], t["name"], t["class"], t["motor_2r_prog27"], t["motor_2r_prog28"], [(r["race"], r["ex_rank"], r["pos"], r["sanrentan"]) for r in t["ride_list"]])
print(out["summary"]); print(out["races_day1"])
for r in out["today"]: print(r)

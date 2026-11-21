"""2026-11-21 住之江 新節初日:機歴1〜10位のモーターの今日の出番と、2連対率とのズレ。

使い方: python3 scripts/analyze_top10_2026-11-21.py > handoff/slides/2026-11-21-suminoe-top10-motors/data.json
"""
import csv
import json
import statistics as st
import subprocess
from collections import defaultdict
from pathlib import Path

DAY, VENUE = "2026-11-21", "住之江"
lineup = json.loads(subprocess.check_output(
    ["python3", "scripts/analyze_lineup_motors.py", DAY, VENUE] + [str(i) for i in range(1, 13)]))
m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[VENUE]
mx = {x["motor"]: x for x in m["motors"]}
prog = {(r["race"], r["boat"]): r for r in csv.DictReader(open(f"data/program/{DAY}.csv", encoding="utf-8"))
        if r["venue"] == VENUE}
last = max(p.stem for p in Path("data/results").glob("*.csv")
           if any(r["venue"] == VENUE for r in csv.DictReader(p.open(encoding="utf-8"))))
for e in lineup["entries"]:
    p = prog[(str(e["race"]), str(e["boat"]))]
    e["class"] = p["racer_class"]
    e["ex_top2"] = mx[e["motor"]]["ex_top2"]
    e["result_2r"] = mx[e["motor"]]["result_2r"]

top = defaultdict(lambda: {"races": []})
for e in lineup["entries"]:
    if e["rank"] <= 10:
        t = top[e["rank"]]
        t.update({k: e[k] for k in ("rank", "motor", "name", "class", "motor_2r_program", "hidden", "ex_top2", "starts")})
        t["races"].append(f'{e["race"]}R')
per_race = defaultdict(list)
for e in lineup["entries"]:
    per_race[e["race"]].append({"boat": e["boat"], "name": e["name"], "motor": e["motor"], "rank": e["rank"]})
by2r = sorted(m["motors"], key=lambda x: -x["motor_2r"])
out = {
    "venue": VENUE, "day": DAY, "period": f'{m["start"]}〜{last}', "n_motors": len(m["motors"]),
    "motor_2r_median": m["motor_2r_median"],
    "motor_2r_top3": [(x["motor"], x["motor_2r"]) for x in by2r[:3]],
    "top10": [top[k] for k in sorted(top)],
    "top10_count_in_race": {r: sum(1 for x in v if x["rank"] <= 10) for r, v in sorted(per_race.items())},
    "race3": per_race[3],
    "entries": lineup["entries"],
}
print(json.dumps(out, ensure_ascii=False, indent=1))

"""指定日・指定場・指定レースの出走メンバーのモーターを、motors.json の機歴(乗り手補正後の展示偏差 ex_adj)で格付けする。

使い方: python3 scripts/analyze_lineup_motors.py 2026-11-09 住之江 10 11 12 [--series 2026-11-05]
--series を付けると、その日から前日までの同じ場での、各選手の展示偏差(レース内中央値との差)の平均も出す。
"""
import csv
import json
import statistics as st
import sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path


def main():
    args = sys.argv[1:]
    series = None
    if "--series" in args:
        i = args.index("--series")
        series = args[i + 1]
        args = args[:i] + args[i + 2:]
    day, venue, races = args[0], args[1], [str(int(x)) for x in args[2:]]
    m = json.load(open("data/analysis/motors.json", encoding="utf-8"))[venue]
    motors = sorted(m["motors"], key=lambda x: x["ex_adj"])
    rank = {x["motor"]: (i + 1, x) for i, x in enumerate(motors)}
    prog = [r for r in csv.DictReader(open(f"data/program/{day}.csv", encoding="utf-8"))
            if r["venue"] == venue and r["race"] in races]

    ser = defaultdict(list)
    if series:
        d = date.fromisoformat(series)
        end = date.fromisoformat(day)
        while d < end:
            p = Path(f"data/results/{d.isoformat()}.csv")
            if p.exists():
                rows = [r for r in csv.DictReader(p.open(encoding="utf-8")) if r["venue"] == venue]
                by = defaultdict(list)
                for r in rows:
                    by[r["race"]].append(r)
                for es in by.values():
                    ex = []
                    for e in es:
                        try:
                            t = float(e["exhibition"])
                        except ValueError:
                            t = 0
                        if t > 0:
                            ex.append((e, t))
                    if len(ex) < 6:
                        continue
                    md = st.median([t for _, t in ex])
                    for e, t in ex:
                        ser[e["racer_number"]].append(t - md)
            d += timedelta(days=1)

    out = {"venue": venue, "day": day, "period_start": m["start"], "n_motors": len(motors),
           "motor_2r_median": m["motor_2r_median"], "entries": []}
    for r in sorted(prog, key=lambda r: (int(r["race"]), int(r["boat"]))):
        rk, x = rank[int(r["motor"])]
        s = ser.get(r["racer_number"], [])
        out["entries"].append({
            "race": int(r["race"]), "boat": int(r["boat"]), "name": r["racer_name"],
            "motor": int(r["motor"]), "rank": rk, "ex_adj": x["ex_adj"], "t": x["t"],
            "starts": x["starts"], "hidden": x["hidden"], "motor_2r_program": float(r["motor_2r"]),
            "series_ex_mean": round(st.mean(s), 4) if s else None, "series_n": len(s),
        })
    print(json.dumps(out, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

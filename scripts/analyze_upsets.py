#!/usr/bin/env python3
"""3連単の配当から「荒れやすさ」を集計する(場別・風速別・1着コース別)。
対象: 3連単の払戻が1つだけ記録され、競走成績(風速・進入・着順)と結び付くレース。
万舟 = 3連単の払戻が10,000円以上。
出力: data/analysis/upsets.json
"""
import glob, json
import pandas as pd

p = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("data/payouts/*.csv"))])
s = p[p.ticket_type == "sanrensho"].copy()
s["payout"] = pd.to_numeric(s.payout, errors="coerce")
cnt = s.groupby(["date", "venue", "race_number"]).payout.transform("count")
s = s[(cnt == 1) & s.payout.notna()].rename(columns={"race_number": "race"})
r = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("data/results/*.csv"))])
r["pos"] = pd.to_numeric(r.position, errors="coerce")
w = r[r.pos == 1][["date", "venue", "race", "entrance", "wind_speed"]].drop_duplicates(["date", "venue", "race"])
d = s.merge(w, on=["date", "venue", "race"], how="inner")
d["man"] = d.payout >= 10000
def st(x):
    return {"n": int(len(x)), "man_rate": round(x.man.mean() * 100, 1), "median": int(x.payout.median()),
            "max": int(x.payout.max())}
out = {"races": int(len(d)), "all": st(d),
       "period": {v: [x.date.min(), x.date.max()] for v, x in d.groupby("venue")},
       "by_venue": {v: st(x) for v, x in d.groupby("venue")}}
d["wb"] = pd.cut(d.wind_speed, [-1, 2, 4, 99], labels=["0〜2m", "3〜4m", "5m以上"])
out["by_wind"] = {k: st(x) for k, x in d.groupby("wb", observed=True)}
d["win_c"] = d.entrance.apply(lambda c: "1コース" if c == 1 else "2〜6コース")
out["by_winner_course"] = {k: st(x) for k, x in d.groupby("win_c")}
out["share_course1_win"] = round((d.entrance == 1).mean() * 100, 1)
out["max_race"] = d.loc[d.payout.idxmax(), ["date", "venue", "race", "payout"]].astype(str).to_dict()
json.dump(out, open("data/analysis/upsets.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

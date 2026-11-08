#!/usr/bin/env python3
"""風速・波高ごとに、1着の進入コースの割合を集計する。
対象: 6艇すべての着順・進入が記録され、風速が記録されたレース(フライング・欠場・失格などを含むレースは除外)。
風向は場ごとにコースの向きが違うため使わない。
出力: data/analysis/wind.json
"""
import glob, json
import pandas as pd

r = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("data/results/*.csv"))])
r["pos"] = pd.to_numeric(r.position, errors="coerce")
r["ent"] = pd.to_numeric(r.entrance, errors="coerce")
r["ws"] = pd.to_numeric(r.wind_speed, errors="coerce")
r["wv"] = pd.to_numeric(r.wave, errors="coerce")
key = ["date", "venue", "race"]
g = r.groupby(key)
ok = (g.pos.transform(lambda s: s.notna().all() and len(s) == 6 and set(s) == {1, 2, 3, 4, 5, 6})
      & g.ent.transform(lambda s: s.notna().all() and set(s) == {1, 2, 3, 4, 5, 6})
      & g.ws.transform(lambda s: s.notna().all()))
d = r[ok]
w = d[d.pos == 1].copy()
lab = ["0〜2m", "3〜4m", "5m以上"]
w["wb"] = pd.cut(w.ws, [-1, 2.5, 4.5, 99], labels=lab)


def stat(x):
    return {"n": int(len(x)), "c1": round((x.ent == 1).mean() * 100, 1),
            "c2": round((x.ent == 2).mean() * 100, 1),
            "c3_6": round((x.ent >= 3).mean() * 100, 1)}


out = {"races": int(len(w)), "all": stat(w),
       "period": {v: [x.date.min(), x.date.max()] for v, x in d.groupby("venue")},
       "by_wind": {k: stat(x) for k, x in w.groupby("wb", observed=True)},
       "by_venue_wind": {v: {k: stat(y) for k, y in x.groupby("wb", observed=True)} for v, x in w.groupby("venue")},
       "le4": stat(w[w.ws <= 4]),
       "by_venue_le4_ge5": {v: {"4m以下": stat(x[x.ws <= 4]), "5m以上": stat(x[x.ws >= 5])} for v, x in w.groupby("venue")},
       "share_5m": {v: round((x.ws >= 5).mean() * 100, 1) for v, x in w.groupby("venue")}}
wl = ["0〜2cm", "3〜4cm", "5cm以上"]
w["vb"] = pd.cut(w.wv, [-1, 2.5, 4.5, 999], labels=wl)
out["by_wave"] = {k: stat(x) for k, x in w.groupby("vb", observed=True)}
json.dump(out, open("data/analysis/wind.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

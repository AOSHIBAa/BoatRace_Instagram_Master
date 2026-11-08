#!/usr/bin/env python3
"""1コース(進入1)の1着率を、1コース自身のSTと、2コースとのST差で集計する。
対象: 6艇すべての着順とSTが記録されたレース(フライング・欠場・失格などを含むレースは除外)。
出力: data/analysis/inside_st.json
"""
import glob, json
import pandas as pd

r = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("data/results/*.csv"))])
r["pos"] = pd.to_numeric(r.position, errors="coerce")
r["st"] = pd.to_numeric(r.st, errors="coerce")
key = ["date", "venue", "race"]
g = r.groupby(key)
ok = g.pos.transform(lambda s: s.notna().all() and len(s) == 6) & g.st.transform(lambda s: s.notna().all())
d = r[ok].copy()
c1 = d[d.entrance == 1].copy()
c1["win"] = c1.pos == 1
out = {"races": int(len(c1)), "win_rate": round(c1.win.mean() * 100, 1),
       "period": {v: [x.date.min(), x.date.max()] for v, x in d.groupby("venue")},
       "by_venue": {v: {"n": int(len(x)), "win": round(x.win.mean() * 100, 1)} for v, x in c1.groupby("venue")}}
# 取り込みデータでは 0.10/0.20/0.30 の一部が 0.09/0.19/0.29 になっている(0.01の誤差)ため、
# x.x9 と x.x0 が同じ区分に入るように区切る
lab = ["0.10以下", "0.11〜0.15", "0.16〜0.20", "0.21以上"]
c1["b"] = pd.cut(c1.st.round(2), [-1, 0.105, 0.155, 0.205, 9], labels=lab)
out["by_own_st"] = {k: {"n": int(len(x)), "win": round(x.win.mean() * 100, 1)} for k, x in c1.groupby("b", observed=True)}
e = d.pivot_table(index=key, columns="entrance", values="st")
diff = (e[1] - e[2]).round(2)
df = pd.DataFrame({"diff": diff, "win": c1.set_index(key).win}).dropna()
lab2 = ["0.05秒以上速い", "0.01〜0.04秒速い", "同じ〜0.04秒遅い", "0.05秒以上遅い"]
df["b"] = pd.cut(df["diff"], [-9, -0.045, -0.005, 0.045, 9], labels=lab2)
out["vs_course2"] = {k: {"n": int(len(x)), "win": round(x.win.astype(bool).mean() * 100, 1)} for k, x in df.groupby("b", observed=True)}
json.dump(out, open("data/analysis/inside_st.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

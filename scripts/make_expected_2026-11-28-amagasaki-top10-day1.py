"""2026-11-28 尼崎2日目 機歴トップ10の初日の成績: data.json から expected.json と spec.md を作る。"""
import json
from pathlib import Path
F = Path("handoff/slides/2026-11-28-amagasaki-top10-day1")
d = json.load(open(F / "data.json", encoding="utf-8"))
NAME_FIX = {"上原健次": "上原健次郎"}  # 番組表は4文字で切れるため競走成績の表記を使う
S = d["summary"]; t10 = S["top10"]; ot = S["others"]
def pos_cell(m): return "、".join(f'{r["pos"]}着' for r in m["ride_list"])
rows = []
for m in d["top10"]:
    rows.append((f'{m["rank"]}位', f'{m["motor"]}号機', NAME_FIX.get(m["name"], m["name"]) if m["name"] else None, pos_cell(m) if m["ride_list"] else None))
n_top = sum(1 for m in d["top10"] if m["ride_list"])
today = d["today"]; races = sorted({r["race"] for r in today})
def lanes(rn): return "、".join(f'{r["boat"]}号艇{r["motor"]}号機' for r in today if r["race"] == rn)
def ranks(rn): return sorted(r["rank"] for r in today if r["race"] == rn)
assert ranks(4) == [3, 7, 9] and ranks(10) == [1, 2] and ranks(3) == [2, 8]
DIS = "※舟券の購入は20歳から。余裕資金で楽しみましょう。データは過去の傾向で、結果を保証するものではありません。"
E = {}
E["s1"] = {"T1": "尼崎2日目|11/28", "T2": "機歴トップ10の", "T3": "初日の成績",
           "T4": f'{t10["rides"]}走で2連対{t10["top2"]}回、1着{t10["wins"]}回', "T5": "データで読むボートレース"}
def table_slide(page, head, rs):
    s = {"T1": "機歴トップ10|尼崎", "T2": f"{page}/5", "T3": head, "T4": "機歴", "T5": "号機", "T6": "初日の選手", "T7": "初日の着順"}
    i = 8
    for r in rs:
        for v in r:
            if v is not None:
                s[f"T{i}"] = v; i += 1
    return s, i
E["s2"], i = table_slide(2, "機歴1〜5位と初日の着順", [r if r[2] else (r[0], r[1], "今節の出走なし", None) for r in rows[:5]])
E["s2"][f"T{i}"] = f'BOAT RACE公式の競走成績と番組表を独自に集計。機歴は尼崎の{d["period_start"].replace("-0", "/").replace("-", "/")}〜11/27の開催分で、乗り手のクセを除いた展示タイムの速さを、走数とばらつきも加味して{d["n_motors"]}機で並べた順位。初日は11/27'
E["s3"], i = table_slide(3, "機歴6〜10位と初日の着順", rows[5:10])
E["s3"][f"T{i}"] = "BOAT RACE公式の競走成績を独自に集計。尼崎11/27。着順はレース番号の順"
E["s4"] = {"T1": f'初日の{S["all"]["rides"]}走|尼崎', "T2": "4/5", "T3": "機歴トップ10とそれ以外",
    "T4": "区分", "T5": "展示1〜2位", "T6": "2連対", "T7": "1着",
    "T8": f"トップ10の{n_top}機", "T9": f'{t10["ex_top2"]}/{t10["rides"]}', "T10": f'{t10["top2"]}/{t10["rides"]}', "T11": f'{t10["wins"]}/{t10["rides"]}',
    "T12": "それ以外", "T13": f'{ot["ex_top2"]}/{ot["rides"]}', "T14": f'{ot["top2"]}/{ot["rides"]}', "T15": f'{ot["wins"]}/{ot["rides"]}',
    "T16": f'2連対は{t10["rides"]}走中{t10["top2"]}回、それ以外は{ot["rides"]}走中{ot["top2"]}回',
    "T17": f'初日の展示1〜2位は{t10["rides"]}走中{t10["ex_top2"]}回',
    "T18": "1日だけの結果で、数字は大きく振れる",
    "T19": f'BOAT RACE公式の競走成績を独自に集計。尼崎11/27の{d["races_day1"]}R、{S["all"]["rides"]}走。数字は回数/走数。展示1〜2位は各レース内の展示タイムの順で、同タイムは上位扱い。展示タイムは直線寄りの指標で、まわり足は反映されにくい'}
E["s5"] = {"T1": "今日の出番|尼崎", "T2": "5/5", "T3": "今日11/28の注目レース",
    "T4": "4R", "T5": "機歴トップ10が3機", "T6": lanes(4),
    "T7": "10R", "T8": "機歴1位と2位", "T9": lanes(10),
    "T10": "3R", "T11": "機歴2位と8位", "T12": lanes(3),
    "T13": "まとめ",
    "T14": f'機歴トップ10の{n_top}機は初日{t10["rides"]}走で2連対{t10["top2"]}回、1着{t10["wins"]}回。今日は{len(races)}レースで{len(today)}回の出番。',
    "T15": "着順は乗り手や枠、進入にも左右されます。",
    "T16": f"BOAT RACE公式の競走成績と番組表を独自に集計。今日の出番は11/28の番組表。全{len(today)}回の出番はキャプションに掲載",
    "T17": DIS}
(F / "expected.json").write_text(json.dumps(E, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(E, ensure_ascii=False, indent=1))

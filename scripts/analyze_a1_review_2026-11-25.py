"""11/25 尼崎:11/20に紹介したA1級8人のモーター(機歴10位以内2人・50位以下4人ほか)の今節11/20〜11/24の答え合わせと、今日の12R。
出力: handoff/slides/2026-11-25-amagasaki-a1-review/data.json
"""
import csv, json, os

V = '尼崎'
DAYS = ['2026-11-20', '2026-11-21', '2026-11-22', '2026-11-23', '2026-11-24']
OUT = 'handoff/slides/2026-11-25-amagasaki-a1-review/data.json'
# 11/20の投稿(機歴は 4/17〜11/17)の分類
GROUPS = {'top': [54, 36], 'mid': [16, 21], 'low': [6, 20, 60, 49]}

rows = []
for d in DAYS:
    rows += [r for r in csv.DictReader(open(f'data/results/{d}.csv')) if r['venue'] == V]
races = {}
for r in rows:
    races.setdefault((r['date'], r['race']), []).append(r)
pay = {}
for d in DAYS:
    f = f'data/payouts/{d}.csv'
    if not os.path.exists(f):
        continue
    for p in csv.DictReader(open(f)):
        if p['venue'] == V and p['ticket_type'] == 'sanrensho':
            pay[(p['date'], p['race_number'])] = (p['winning_combination'], int(p['payout']))


def exr(r):
    ex = sorted(float(x['exhibition']) for x in races[(r['date'], r['race'])] if x['exhibition'])
    if not r['exhibition']:
        return None
    return ex.index(float(r['exhibition'])) + 1  # 同タイムは上位扱い


m = json.load(open('data/analysis/motors.json'))[V]
rank_now = {x['motor']: i + 1 for i, x in enumerate(m['motors'])}
prog = [p for p in csv.DictReader(open('data/program/2026-11-25.csv')) if p['venue'] == V]

out = dict(venue=V, days=DAYS, period_now=f"{m['start']}〜{DAYS[-1]}", n_motors=len(m['motors']),
           motor_2r_median=m['motor_2r_median'], groups={}, r12=[])
for g, ms in GROUPS.items():
    G = dict(n=0, ex1=0, ex12=0, w=0, r2=0, r3=0, nopos=0)
    per = []
    for mo in ms:
        rs = sorted([r for r in rows if int(r['motor']) == mo], key=lambda r: (r['date'], int(r['race'])))
        P = dict(motor=mo, name=rs[0]['racer_name'], rank_now=rank_now.get(mo), n=len(rs), ex1=0, ex12=0,
                 w=0, r2=0, r3=0, nopos=0, runs=[])
        for r in rs:
            e = exr(r)
            P['ex1'] += e == 1
            P['ex12'] += e is not None and e <= 2
            pos = r['position']
            P['runs'].append(dict(date=r['date'], race=int(r['race']), boat=int(r['boat']), entrance=r['entrance'],
                                  ex=r['exhibition'], ex_rank=e, pos=pos, payout=pay.get((r['date'], r['race']))))
            if not pos.isdigit():
                P['nopos'] += 1
                continue
            p = int(pos)
            P['w'] += p == 1
            P['r2'] += p <= 2
            P['r3'] += p <= 3
        P['today'] = [(int(p['race']), int(p['boat'])) for p in prog if int(p['motor']) == mo]
        per.append(P)
        for k in G:
            G[k] += P[k]
    out['groups'][g] = dict(total=G, motors=per)
for p in sorted([p for p in prog if p['race'] == '12'], key=lambda p: int(p['boat'])):
    mo = int(p['motor'])
    rs = [r for r in rows if int(r['motor']) == mo]
    pos = [int(r['position']) for r in rs if r['position'].isdigit()]
    out['r12'].append(dict(boat=int(p['boat']), name=p['racer_name'], cls=p['racer_class'], motor=mo,
                           rank_now=rank_now[mo], motor_2r=float(p['motor_2r']), series_n=len(rs),
                           series_w=sum(x == 1 for x in pos), series_r2=sum(x <= 2 for x in pos),
                           series_names=sorted(set(r['racer_name'] for r in rs))))
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
for g, v in out['groups'].items():
    t = v['total']
    print(g, t)
    for P in v['motors']:
        print('  ', P['motor'], P['name'], 'now', P['rank_now'], 'n', P['n'], 'ex1', P['ex1'], 'ex12', P['ex12'],
              'w', P['w'], 'r2', P['r2'], 'r3', P['r3'], 'nopos', P['nopos'], 'today', P['today'])
        for r in P['runs']:
            print('      ', r)
print('12R')
for x in out['r12']:
    print('  ', x)

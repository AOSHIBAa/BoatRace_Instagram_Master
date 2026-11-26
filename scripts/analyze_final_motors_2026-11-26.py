"""11/26 住之江 最終日:優勝戦(12R)の6機を機歴で格付けし、今節11/21〜11/25の成績を集計する。
12Rが優勝戦であることは、11/25の9R・10R・11Rの1・2着の6人と一致することで確認。
出力: handoff/slides/2026-11-26-suminoe-final-motors/data.json
"""
import csv, json, os, statistics

V = '住之江'
DAYS = ['2026-11-21', '2026-11-22', '2026-11-23', '2026-11-24', '2026-11-25']
TODAY = '2026-11-26'
OUT = 'handoff/slides/2026-11-26-suminoe-final-motors/data.json'

rows = []
for d in DAYS:
    rows += [r for r in csv.DictReader(open(f'data/results/{d}.csv')) if r['venue'] == V]
races = {}
for r in rows:
    races.setdefault((r['date'], r['race']), []).append(r)
pay = {}
for d in DAYS:
    for p in csv.DictReader(open(f'data/payouts/{d}.csv')):
        if p['venue'] == V and p['ticket_type'] == 'sanrensho':
            pay[(p['date'], p['race_number'])] = int(p['payout'])


def exr(r):
    if not r['exhibition']:
        return None
    ex = sorted(float(x['exhibition']) for x in races[(r['date'], r['race'])] if x['exhibition'])
    return ex.index(float(r['exhibition'])) + 1  # 同タイムは上位扱い


m = json.load(open('data/analysis/motors.json'))[V]
rank_now = {x['motor']: i + 1 for i, x in enumerate(m['motors'])}
mt = {x['motor']: x for x in m['motors']}
prog_all = [p for p in csv.DictReader(open(f'data/program/{TODAY}.csv')) if p['venue'] == V]
fin = sorted([p for p in prog_all if p['race'] == '12'], key=lambda p: int(p['boat']))

# 優勝戦の確認:11/25 9〜11Rの1・2着
semi = sorted(r['racer_name'] for r in rows if r['date'] == DAYS[-1] and r['race'] in ('9', '10', '11') and r['position'] in ('1', '2'))
assert semi == sorted(p['racer_name'] for p in fin), (semi, [p['racer_name'] for p in fin])

out = dict(venue=V, days=DAYS, period=f"{m['start']}〜{DAYS[-1]}", n_motors=len(m['motors']),
           motor_2r_median=m['motor_2r_median'], final=[])
for p in fin:
    mo = int(p['motor'])
    rs = sorted([r for r in rows if int(r['motor']) == mo], key=lambda r: (r['date'], int(r['race'])))
    assert all(r['racer_number'] == p['racer_number'] for r in rs), (mo, set(r['racer_name'] for r in rs))
    P = dict(boat=int(p['boat']), name=p['racer_name'], cls=p['racer_class'], motor=mo, rank=rank_now[mo],
             motor_2r=p['motor_2r'], hidden=mt[mo]['hidden'], t=mt[mo]['t'], n=len(rs), ex1=0, ex12=0, w=0, r2=0,
             nopos=0, runs=[])
    for r in rs:
        e = exr(r)
        P['ex1'] += e == 1
        P['ex12'] += e is not None and e <= 2
        P['runs'].append((r['date'][5:], int(r['race']), int(r['boat']), r['entrance'], r['exhibition'], e, r['position'], pay.get((r['date'], r['race']))))
        if r['position'].isdigit():
            P['w'] += r['position'] == '1'
            P['r2'] += int(r['position']) <= 2
        else:
            P['nopos'] += 1
    out['final'].append(P)
# 2連対率の順位(65機それぞれの最新の番組表の値)
latest = {}
for d in sorted(os.listdir('data/program')):
    if d[:10] < m['start'] or d[:10] > TODAY:
        continue
    for p in csv.DictReader(open(f'data/program/{d}')):
        if p['venue'] == V and p['motor_2r']:
            latest[int(p['motor'])] = float(p['motor_2r'])
vals = sorted(latest.values(), reverse=True)
out['n_2r'] = len(vals)
out['median_2r_calc'] = statistics.median(vals)
for P in out['final']:
    v = float(P['motor_2r'])
    P['rank_2r'] = sum(x > v for x in vals) + 1
json.dump(out, open(OUT, 'w'), ensure_ascii=False, indent=1)
print(out['period'], out['n_motors'], out['motor_2r_median'], out['n_2r'], out['median_2r_calc'])
for P in out['final']:
    print({k: v for k, v in P.items() if k != 'runs'})
    for r in P['runs']:
        print('    ', r)

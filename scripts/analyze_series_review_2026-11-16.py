import csv,json
rows=[]
for d in ['12','13','14','15']:
  rows+= [r for r in csv.DictReader(open(f'data/results/2026-11-{d}.csv')) if r['venue']=='尼崎']
races={}
for r in rows: races.setdefault((r['date'],r['race']),[]).append(r)
pay={}
for d in ['12','13','14','15']:
  for p in csv.DictReader(open(f'data/payouts/2026-11-{d}.csv')):
    if p['venue_code']=='13' and p['ticket_type']=='sanrensho': pay[(p['date'],p['race_number'])]=(p['winning_combination'],int(p['payout']))
def exr(r):
  ex=sorted(float(x['exhibition']) for x in races[(r['date'],r['race'])] if x['exhibition'])
  return ex.index(float(r['exhibition']))+1
out={}
prog=[p for p in csv.DictReader(open('data/program/2026-11-16.csv')) if p['venue']=='尼崎']
groups={'top':[23,56,63,61,54],'low':[32,62,8,13],'h':[24]}
for g,ms in groups.items():
  G=dict(n=0,ex12=0,ex1=0,w=0,r2=0,r3=0,nopos=0)
  per=[]
  for m in ms:
    rs=sorted([r for r in rows if r['motor']==str(m)],key=lambda r:(r['date'],int(r['race'])))
    P=dict(motor=m,name=rs[0]['racer_name'],n=len(rs),ex1=0,ex12=0,w=0,r2=0,r3=0,nopos=0,courses=[],pos=[],wins=[])
    for r in rs:
      e=exr(r);P['ex1']+=e==1;P['ex12']+=e<=2
      pos=r['position'];P['pos'].append(pos);P['courses'].append(r['entrance'])
      if pos=='':P['nopos']+=1;continue
      p=int(pos);P['w']+=p==1;P['r2']+=p<=2;P['r3']+=p<=3
      if p==1:P['wins'].append((r['date'],r['race'],pay.get((r['date'],r['race']))))
    P['today']=[(p['race'],p['boat'],p['racer_name'],p['racer_class']) for p in prog if p['motor']==str(m)]
    per.append(P)
    for k in ['n','ex1','ex12','w','r2','r3','nopos']:G[k]+=P[k]
  out[g]=dict(total=G,motors=per)
json.dump(out,open('/tmp/claude-0/-home-claude/d8bdd964-710c-51de-b7e4-9a30744a275b/scratchpad/agg.json','w'),ensure_ascii=False,indent=1)
for g in out:
  t=out[g]['total'];print(g,t, 'r2%',round(100*t['r2']/t['n'],1),'ex12%',round(100*t['ex12']/t['n'],1))
  for P in out[g]['motors']:print(' ',P)

import csv,glob,collections as C
rows=[]
for p in sorted(glob.glob('data/results/*.csv')): rows+=list(csv.DictReader(open(p,encoding='utf-8')))
races=C.defaultdict(list)
for r in rows: races[(r['date'],r['venue'],r['race'])].append(r)
print(min(k[0] for k in races),max(k[0] for k in races))
st=C.defaultdict(lambda:[0,0,0,0]); bycourse=C.defaultdict(lambda:[0,0]); base=C.defaultdict(lambda:[0,0])
solo=C.defaultdict(lambda:[0,0])
for k,b in races.items():
  b=[x for x in b if x['exhibition'] not in ('','0','0.0') and x['position'] in {'1','2','3','4','5','6'} and x['position']!='' and x['entrance']]
  if len(b)<6: continue
  ex=[float(x['exhibition']) for x in b]; m=min(ex)
  tops=[x for x in b if float(x['exhibition'])==m]
  v=k[1]; s=st[v]; s[0]+=1
  if len(tops)==1:
    t=tops[0]; s[1]+=1; s[2]+= t['position']=='1'; s[3]+= t['position'] in('1','2','3')
    c=t['entrance']; bycourse[(v,c)][0]+=1; bycourse[(v,c)][1]+= t['position']=='1'
  for x in b: base[(v,x['entrance'])][0]+=1; base[(v,x['entrance'])][1]+= x['position']=='1'
for v,s in st.items(): print(v,'races',s[0],'uniqueTop',s[1],'win%',round(100*s[2]/s[1],1),'top3%',round(100*s[3]/s[1],1))
for v in st:
  print(v,[(c,bycourse[(v,c)][0],round(100*bycourse[(v,c)][1]/max(1,bycourse[(v,c)][0]),1),round(100*base[(v,c)][1]/base[(v,c)][0],1)) for c in '123456'])
print('---combined')
T=[sum(s[i] for s in st.values()) for i in range(4)]; print(T, round(100*T[2]/T[1],1), round(100*T[3]/T[1],1))
for c in '123456':
  n=sum(bycourse[(v,c)][0] for v in st); w=sum(bycourse[(v,c)][1] for v in st)
  bn=sum(base[(v,c)][0] for v in st); bw=sum(base[(v,c)][1] for v in st)
  print(c,n,w,round(100*w/n,1),bn,bw,round(100*bw/bn,1))
for v in st: print(v, min(k[0] for k in races if k[1]==v))
ties=sum(s[0]-s[1] for s in st.values()); print('ties',ties)

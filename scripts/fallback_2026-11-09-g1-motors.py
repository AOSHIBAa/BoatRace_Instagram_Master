import json,sys,shutil
from pathlib import Path
sys.path.insert(0,'scripts')
from slides import page, render
from PIL import Image
F='handoff/slides/2026-11-09-g1-motors'
e=json.load(open(f'{F}/expected.json'))
def table(s, ids_rows, hdr, col, top=330, rowh=112):
    h=e[s]
    out=f'<div class="card" style="top:{top}px;height:{90+rowh*len(ids_rows)}px"></div>'
    xs=[110,340,610,960]
    for x,i,al in zip(xs,hdr,['l','l','l','r']):
        st=f'right:{1080-x}px' if al=='r' else f'left:{x}px'
        out+=f'<div style="position:absolute;top:{top+26}px;{st};font-size:32px;color:#9fb3c8;font-weight:700">{h[i]}</div>'
    for n,row in enumerate(ids_rows):
        y=top+90+n*rowh
        out+=f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:2px;background:rgba(255,255,255,.12)"></div>'
        if s=='s2' and n<2: out+=f'<div style="position:absolute;top:{y+2}px;left:82px;right:82px;height:{rowh-2}px;background:rgba(255,196,0,.10)"></div>'
        a,b,c,d=[h[i] for i in row]
        out+=f'<div style="position:absolute;top:{y+36}px;left:110px;font-size:36px;color:#9fb3c8;font-weight:700">{a}</div>'
        out+=f'<div style="position:absolute;top:{y+28}px;left:340px;font-size:46px;font-weight:900">{b}</div>'
        out+=f'<div style="position:absolute;top:{y+28}px;left:610px;font-size:46px;font-weight:900">{c}</div>'
        out+=f'<div style="position:absolute;top:{y+12}px;right:120px;font-size:66px;font-weight:900;color:{col}">{d}</div>'
    return out, top+90+rowh*len(ids_rows)
def T(s,i): return e[s][i]
hs=[]
# s2
rows=[[f'T{8+4*k}',f'T{9+4*k}',f'T{10+4*k}',f'T{11+4*k}'] for k in range(6)]
b,y=table('s2',rows,['T4','T5','T6','T7'],'#FFC400')
b+=f'<div style="position:absolute;top:{y+40}px;left:80px;right:80px;font-size:48px;font-weight:900;color:#FFC400">{T("s2","T32")}</div>'
hs.append(page(2,5,T('s2','T1'),T('s2','T3'),'',b,T('s2','T33')).replace('<div class="page">2/5</div>',f'<div class="page">{T("s2","T2")}</div>'))
# s3
rows=[[f'T{8+4*k}',f'T{9+4*k}',f'T{10+4*k}',f'T{11+4*k}'] for k in range(4)]
b,y=table('s3',rows,['T4','T5','T6','T7'],'#ff8a8a')
b+=f'<div style="position:absolute;top:{y+50}px;left:80px;right:80px;font-size:46px;font-weight:900;line-height:1.4">{T("s3","T24")}</div>'
hs.append(page(3,5,T('s3','T1'),T('s3','T3'),'',b,T('s3','T25')))
# s4
h=e['s4']
b=f'<div style="position:absolute;top:262px;left:80px;font-size:56px;font-weight:900;color:#FFC400">{h["T4"]}</div>'
def card(x,lab,big,sub,bigcol,border,px):
    return (f'<div class="card" style="top:380px;height:380px;left:{x}px;right:auto;width:445px;border-color:{border}"></div>'
            f'<div style="position:absolute;top:410px;left:{x}px;width:445px;text-align:center;font-size:38px;font-weight:700">{lab}</div>'
            f'<div style="position:absolute;top:{560-px*0.62}px;left:{x}px;width:445px;text-align:center;font-size:{px}px;font-weight:900;color:{bigcol};line-height:1.2">{big}</div>'
            f'<div style="position:absolute;top:690px;left:{x}px;width:445px;text-align:center;font-size:30px;color:#9fb3c8;font-weight:700">{sub}</div>')
b+=card(80,h['T5'],h['T6'],h['T7'],'#cfd8e3','rgba(255,255,255,.25)',104)
b+=card(555,h['T8'],h['T9'],h['T10'],'#FFC400','#FFC400',150)
b+=f'<div style="position:absolute;top:800px;left:80px;right:80px;font-size:62px;font-weight:900;color:#FFC400">{h["T11"]}</div>'
b+=f'<div style="position:absolute;top:910px;left:80px;right:80px;font-size:40px;font-weight:700">{h["T12"]}</div>'
b+=f'<div style="position:absolute;top:985px;left:80px;right:80px;font-size:36px;font-weight:700;color:#ff8a8a">{h["T13"]}</div>'
hs.append(page(4,5,h['T1'],h['T3'],'',b,h['T14']))
fixed=[]
for x in hs:
    x=x.replace('<div class="page">2/5</div>','<div class="page">2/5</div>')
    fixed.append(x.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px','h2{position:absolute;top:150px;left:80px;right:60px;white-space:nowrap;font-size:56px').replace('.tag{position:absolute;top:70px;left:80px;font-size:30px','.tag{position:absolute;top:70px;left:80px;font-size:34px'))
paths=render(fixed,'/tmp/fb_slides',contact=False)
for n,p in zip([2,3,4],paths):
    Image.open(p).resize((1122,1402),Image.LANCZOS).save(f'{F}/s{n}_fallback.png')
print('done')

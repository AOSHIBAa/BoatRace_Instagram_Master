"""2026-11-21 住之江 機歴トップ10: Codex版の s3(「山下拓巳」の巳が己と読める)と s5(行頭の中黒が丸い箇条書き記号+空白と読める)が
作り直し後も照合NGのため、slides.py の部品で expected.json の文字そのままに s3・s5 を作る。"""
import json
import sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-21-suminoe-top10-motors'
E = json.load(open(f'{F}/expected.json', encoding='utf-8'))
NW = 'white-space:nowrap;'


def fix(html, n):
    html = html.replace('.src{position:absolute;bottom:52px;left:80px;right:80px;font-size:23px;color:#6f8bb0',
                        '.src{position:absolute;bottom:52px;left:80px;right:80px;font-size:23px;color:#9fb3c8')
    html = html.replace(f'<div class="page">{n}/5</div>', f'<div class="page" style="color:#9fb3c8">{n}/5</div>')
    return html.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px',
                        'h2{position:absolute;top:140px;left:80px;right:60px;white-space:nowrap;font-size:60px')


# s3
h = E['s3']
TOP, HDR, RH = 280, 80, 120
XS = [110, 400, 610, 0]
b = f'<div class="card" style="top:{TOP}px;height:{HDR+RH*5+10}px"></div>'
for x, k in zip(XS[:3], ['T4', 'T5', 'T6']):
    b += f'<div style="position:absolute;top:{TOP+24}px;left:{x}px;font-size:30px;color:#9fb3c8;font-weight:700">{h[k]}</div>'
b += f'<div style="position:absolute;top:{TOP+24}px;right:115px;font-size:30px;color:#9fb3c8;font-weight:700">{h["T7"]}</div>'
for n in range(5):
    k = [f'T{8+4*n+i}' for i in range(4)]
    y = TOP + HDR + n * RH
    if n in (2, 4):
        b += f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:{RH}px;background:rgba(255,196,0,.10)"></div>'
    b += f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:1px;background:rgba(255,255,255,.15)"></div>'
    b += f'<div style="position:absolute;top:{y+30}px;left:{XS[0]}px;font-size:48px;font-weight:900;{NW}">{h[k[0]]}</div>'
    b += f'<div style="position:absolute;top:{y+34}px;left:{XS[1]}px;font-size:42px;font-weight:700;{NW}">{h[k[1]]}</div>'
    b += f'<div style="position:absolute;top:{y+36}px;left:{XS[2]}px;font-size:40px;font-weight:700;color:#9fb3c8;{NW}">{h[k[2]]}</div>'
    num = h[k[3]][:-1]
    b += (f'<div style="position:absolute;top:{y+14}px;right:115px;font-weight:900;color:#FFC400;{NW}">'
          f'<span style="font-size:72px">{num}</span><span style="font-size:34px">位</span></div>')
yb = TOP + HDR + RH * 5 + 40
b += f'<div style="position:absolute;top:{yb}px;left:80px;right:60px;font-size:36px;font-weight:900;color:#FFC400;{NW}">{h["T28"]}</div>'
b += f'<div style="position:absolute;top:{yb+62}px;left:80px;right:60px;font-size:36px;font-weight:900;{NW}">{h["T29"]}</div>'
s3 = fix(page(3, 5, h['T1'], h['T3'], '', b, h['T30']), 3)

# s5
h = E['s5']
hl = {'T4': '10機がすべて', 'T5': '竹井貴史と渡邉俊介の2人', 'T6': '中央値未満', 'T7': '3機'}
brk = {'T4': '10機がすべて', 'T5': '竹井貴史', 'T6': '2連対率', 'T7': '1・2・5'}  # 2行目の始まり(文字は変えず改行位置だけ指定)
inner = ''
for k in ['T4', 'T5', 'T6', 'T7']:
    t = h[k]
    i = t.index(brk[k])
    a, c = t[:i], t[i:]
    a = a.replace(hl[k], f'<span class="hl">{hl[k]}</span>', 1)
    c = c.replace(hl[k], f'<span class="hl">{hl[k]}</span>', 1)
    assert (a + c).count('class="hl"') == 1, k
    inner += f'<div style="margin-bottom:30px;padding-left:1em;text-indent:-1em;{NW}">{a}<br>{c}</div>'
t8 = h['T8']
j = t8.index('参考')
b = (f'<div class="card" style="top:290px;height:660px"></div>'
     f'<div style="position:absolute;top:330px;left:120px;right:100px;font-size:40px;font-weight:700;line-height:1.5">{inner}</div>'
     f'<div style="position:absolute;top:1000px;left:80px;right:80px;font-size:36px;font-weight:700;line-height:1.5">{t8[:j]}<br>{t8[j:]}</div>')
s5 = fix(page(5, 5, h['T1'], h['T3'], '', b, h['T9']), 5)
s5 = s5.replace('font-size:23px;color:#9fb3c8', 'font-size:24px;color:#9fb3c8')

paths = render([s3, s5], '/tmp/fb_suminoe', contact=False)
for p, name in zip(paths, ['s3', 's5']):
    Image.open(p).resize((1122, 1402), Image.LANCZOS).save(f'/tmp/fb_suminoe/{name}_fallback.png')
print('done')

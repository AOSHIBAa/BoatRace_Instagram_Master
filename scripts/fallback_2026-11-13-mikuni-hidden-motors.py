"""2026-11-13 三国 隠れ上位モーター: Codex版 s4 で選手名「嵜」が2回とも「寄」と読める字形になったため、slides.py の部品で expected.json の文字そのままに s4 を作り直す。"""
import json
import sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-13-mikuni-hidden-motors'
e = json.load(open(f'{F}/expected.json', encoding='utf-8'))
h = e['s4']
NW = 'white-space:nowrap;'
TOP, HDR, RH = 280, 66, 78
XS = [115, 290, 480, 800]
rows = [[f'T{8+4*i}', f'T{9+4*i}', f'T{10+4*i}', f'T{11+4*i}'] for i in range(10)]
race_break = {2, 4, 5, 6, 8}  # この行の上に太い区切り線(レースが変わる所)

b = f'<div class="card" style="top:{TOP}px;height:{HDR+RH*len(rows)+10}px"></div>'
for x, k in zip(XS, ['T4', 'T5', 'T6', 'T7']):
    b += f'<div style="position:absolute;top:{TOP+18}px;left:{x}px;font-size:28px;color:#9fb3c8;font-weight:700">{h[k]}</div>'
for n, r in enumerate(rows):
    y = TOP + HDR + n * RH
    thick = n in race_break
    b += (f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:{3 if thick else 1}px;'
          f'background:rgba(255,255,255,{.35 if thick else .12})"></div>')
    b += f'<div style="position:absolute;top:{y+14}px;left:{XS[0]}px;font-size:38px;font-weight:900;color:#FFC400;{NW}">{h[r[0]]}</div>'
    b += f'<div style="position:absolute;top:{y+16}px;left:{XS[1]}px;font-size:34px;font-weight:700;{NW}">{h[r[1]]}</div>'
    b += f'<div style="position:absolute;top:{y+14}px;left:{XS[2]}px;font-size:38px;font-weight:900;{NW}">{h[r[2]]}</div>'
    b += f'<div style="position:absolute;top:{y+16}px;left:{XS[3]}px;font-size:34px;font-weight:700;color:#9fb3c8;{NW}">{h[r[3]]}</div>'
yb = TOP + HDR + RH * len(rows) + 34
b += f'<div style="position:absolute;top:{yb}px;left:80px;right:80px;font-size:40px;font-weight:900;color:#FFC400;{NW}">{h["T48"]}</div>'

html = page(4, 5, h['T1'], h['T3'], '', b, h['T49'])
html = html.replace('<div class="page">4/5</div>', '<div class="page" style="color:#9fb3c8">4/5</div>')
html = html.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px',
                    'h2{position:absolute;top:140px;left:80px;right:60px;white-space:nowrap;font-size:62px')
paths = render([html], '/tmp/fb_mikuni', contact=False)
Image.open(paths[0]).resize((1122, 1402), Image.LANCZOS).save(f'{F}/s4_fallback.png')
print('done')

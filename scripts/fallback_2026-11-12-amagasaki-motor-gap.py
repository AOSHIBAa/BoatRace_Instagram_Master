"""2026-11-12 尼崎モーター格付け: Codex版 s2 で選手名「薗」が正しく描けなかった(2回とも「園」に近い崩れた字形)ため、slides.py の部品で expected.json の文字そのままに s2 を作り直す。"""
import json
import sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-12-amagasaki-motor-gap'
e = json.load(open(f'{F}/expected.json', encoding='utf-8'))
NW = 'white-space:nowrap;'


def table(h, hdr, rows, top=310, rowh=118):
    xs = [105, 260, 450, 660]
    out = f'<div class="card" style="top:{top}px;height:{84+rowh*len(rows)}px"></div>'
    for x, i in zip(xs, hdr):
        out += f'<div style="position:absolute;top:{top+24}px;left:{x}px;font-size:30px;color:#9fb3c8;font-weight:700">{h[i]}</div>'
    for n, row in enumerate(rows):
        y = top + 84 + n * rowh
        out += f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:2px;background:rgba(255,255,255,.12)"></div>'
        out += f'<div style="position:absolute;top:{y+20}px;left:105px;font-size:58px;font-weight:900;color:#FFC400;line-height:1.2">{h[row[0]]}</div>'
        out += f'<div style="position:absolute;top:{y+34}px;left:260px;font-size:42px;font-weight:900;{NW}">{h[row[1]]}</div>'
        out += f'<div style="position:absolute;top:{y+34}px;left:450px;font-size:40px;font-weight:900;{NW}">{h[row[2]]}</div>'
        out += f'<div style="position:absolute;top:{y+42}px;left:660px;font-size:28px;font-weight:700;color:#9fb3c8;{NW}">{h[row[3]]}</div>'
    return out, top + 84 + rowh * len(rows)


def fix(x, n):
    x = x.replace(f'<div class="page">{n}/4</div>', f'<div class="page" style="color:#9fb3c8">{n}/4</div>')
    return x.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px',
                     'h2{position:absolute;top:150px;left:80px;right:60px;white-space:nowrap;font-size:60px')


h = e['s2']
rows = [['T8', 'T9', 'T10', 'T11'], ['T12', 'T13', 'T14', 'T15'], ['T16', 'T17', 'T18', 'T19'],
        ['T20', 'T21', 'T22', 'T23'], ['T24', 'T25', 'T26', 'T27']]
b, y = table(h, ['T4', 'T5', 'T6', 'T7'], rows)
b += f'<div style="position:absolute;top:{y+40}px;left:80px;right:80px;font-size:46px;font-weight:900;color:#FFC400">{h["T28"]}</div>'
paths = render([fix(page(2, 4, h['T1'], h['T3'], '', b, h['T29']), 2)], '/tmp/fb_amagasaki', contact=False)
Image.open(paths[0]).resize((1122, 1402), Image.LANCZOS).save(f'{F}/s2_fallback.png')
print('done')

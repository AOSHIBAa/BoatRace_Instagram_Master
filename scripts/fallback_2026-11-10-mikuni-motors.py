"""2026-11-10 三国モーター格付け: Codex版で選手名「宮嵜」が正しく描けなかった s2・s4 を、slides.py の部品で expected.json の文字そのままに作り直す。"""
import json
import sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-10-mikuni-motors'
e = json.load(open(f'{F}/expected.json', encoding='utf-8'))
NW = 'white-space:nowrap;'


def table(h, hdr, rows, warm, top=310, rowh=118):
    xs = [105, 260, 420, 650]
    out = f'<div class="card" style="top:{top}px;height:{84+rowh*len(rows)}px"></div>'
    for x, i in zip(xs, hdr):
        out += f'<div style="position:absolute;top:{top+24}px;left:{x}px;font-size:30px;color:#9fb3c8;font-weight:700">{h[i]}</div>'
    for n, row in enumerate(rows):
        y = top + 84 + n * rowh
        out += f'<div style="position:absolute;top:{y}px;left:82px;right:82px;height:2px;background:rgba(255,255,255,.12)"></div>'
        if n in warm:
            out += f'<div style="position:absolute;top:{y+2}px;left:82px;right:82px;height:{rowh-2}px;background:rgba(255,196,0,.10)"></div>'
        out += f'<div style="position:absolute;top:{y+20}px;left:105px;font-size:58px;font-weight:900;color:#FFC400;line-height:1.2">{h[row[0]]}</div>'
        out += f'<div style="position:absolute;top:{y+34}px;left:260px;font-size:42px;font-weight:900;{NW}">{h[row[1]]}</div>'
        if len(row) == 3:
            out += f'<div style="position:absolute;top:{y+42}px;left:420px;font-size:32px;font-weight:700;color:#9fb3c8;{NW}">{h[row[2]]}</div>'
        else:
            out += f'<div style="position:absolute;top:{y+34}px;left:420px;font-size:40px;font-weight:900;{NW}">{h[row[2]]}</div>'
            out += f'<div style="position:absolute;top:{y+42}px;left:650px;font-size:28px;font-weight:700;color:#9fb3c8;{NW}">{h[row[3]]}</div>'
    return out, top + 84 + rowh * len(rows)


def fix(x, n):
    x = x.replace(f'<div class="page">{n}/5</div>', f'<div class="page" style="color:#9fb3c8">{n}/5</div>')
    return x.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px',
                     'h2{position:absolute;top:150px;left:80px;right:60px;white-space:nowrap;font-size:60px')


hs = []
# s2
h = e['s2']
rows = [['T8', 'T9', 'T10', 'T11'], ['T12', 'T13', 'T14', 'T15'], ['T16', 'T17', 'T18', 'T19'],
        ['T20', 'T21', 'T22'], ['T23', 'T24', 'T25', 'T26']]
b, y = table(h, ['T4', 'T5', 'T6', 'T7'], rows, warm={0, 1, 4})
b += f'<div style="position:absolute;top:{y+40}px;left:80px;right:80px;font-size:46px;font-weight:900;color:#FFC400">{h["T27"]}</div>'
hs.append(fix(page(2, 5, h['T1'], h['T3'], '', b, h['T28']), 2))
# s4
h = e['s4']
b = f'<div style="position:absolute;top:250px;left:80px;font-size:44px;font-weight:900;color:#FFC400">{h["T4"]}</div>'


def card(x, lab, big, sub, bigcol, border, px):
    return (f'<div class="card" style="top:350px;height:380px;left:{x}px;right:auto;width:445px;border-color:{border}"></div>'
            f'<div style="position:absolute;top:380px;left:{x}px;width:445px;text-align:center;font-size:34px;font-weight:700">{lab}</div>'
            f'<div style="position:absolute;top:{540-px*0.62}px;left:{x}px;width:445px;text-align:center;font-size:{px}px;font-weight:900;color:{bigcol};line-height:1.2">{big}</div>'
            f'<div style="position:absolute;top:660px;left:{x}px;width:445px;text-align:center;font-size:28px;color:#9fb3c8;font-weight:700">{sub}</div>')


b += card(80, h['T5'], h['T6'], h['T7'], '#9fb3c8', 'rgba(255,255,255,.25)', 104)
b += card(555, h['T8'], h['T9'], h['T10'], '#FFC400', '#FFC400', 150)
b += f'<div style="position:absolute;top:770px;left:80px;right:80px;font-size:60px;font-weight:900;color:#FFC400">{h["T11"]}</div>'
b += f'<div style="position:absolute;top:875px;left:80px;right:80px;font-size:31px;font-weight:700;line-height:1.5">{h["T12"]}</div>'
b += f'<div style="position:absolute;top:950px;left:80px;right:80px;font-size:30px;font-weight:700;color:#ff8a8a">{h["T13"]}</div>'
hs.append(fix(page(4, 5, h['T1'], h['T3'], '', b, h['T14']), 4))

paths = render(hs, '/tmp/fb_mikuni', contact=False)
for n, p in zip([2, 4], paths):
    Image.open(p).resize((1122, 1402), Image.LANCZOS).save(f'{F}/s{n}_fallback.png')
print('done')

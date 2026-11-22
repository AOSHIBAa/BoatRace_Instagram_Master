"""2026-11-22 三国 3R 機歴トップ10: Codex版 s5 の行頭の中黒が丸い箇条書き記号+空白と読め、作り直し後も照合NGのため、
slides.py の部品で expected.json の文字そのままに s5 を作る(Codex版に合わせて黄色帯ラベル・黄色の「まとめ」)。"""
import json, sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-22-mikuni-3r-top10'
h = json.load(open(f'{F}/expected.json', encoding='utf-8'))['s5']
NW = 'white-space:nowrap;'
hl = {'T4': '4機', 'T5': '中央値未満', 'T6': '1着2回', 'T7': '9R・10R・11R'}
inner = ''
for k in ['T4', 'T5', 'T6', 'T7']:
    t = h[k]
    assert t.count(hl[k]) == 1, k
    inner += f'<div style="margin-bottom:40px;{NW}">{t.replace(hl[k], f"<span class=hl>{hl[k]}</span>")}</div>'
t8 = h['T8']; j = t8.index('参考')
b = (f'<div class="card" style="top:330px;height:470px;border-color:rgba(120,170,255,.45)"></div>'
     f'<div style="position:absolute;top:385px;left:105px;right:90px;font-size:35px;font-weight:700;line-height:1.5">{inner}</div>'
     f'<div style="position:absolute;top:900px;left:80px;right:80px;font-size:40px;font-weight:700;line-height:1.5">{t8[:j]}<br>{t8[j:]}</div>')
html = page(5, 5, h['T1'], h['T3'], '', b, h['T9'])
html = html.replace('.tag{position:absolute;top:70px;left:80px;font-size:30px;letter-spacing:.12em;color:#ffc400;font-weight:700}',
                    '.tag{position:absolute;top:60px;left:70px;font-size:34px;color:#111;background:#ffc400;padding:6px 18px;border-radius:10px;font-weight:900}')
html = html.replace('.page{position:absolute;top:70px;right:80px;font-size:30px;color:#6f8bb0', '.page{position:absolute;top:62px;right:80px;font-size:40px;color:#9fb3c8')
html = html.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px', 'h2{position:absolute;top:160px;left:80px;right:80px;color:#ffc400;font-size:110px')
html = html.replace('.src{position:absolute;bottom:52px;left:80px;right:80px;font-size:23px;color:#6f8bb0', '.src{position:absolute;bottom:60px;left:80px;right:80px;font-size:25px;color:#9fb3c8')
p = render([html], '/tmp/fb_mikuni', contact=False)[0]
Image.open(p).resize((1122, 1402), Image.LANCZOS).save('/tmp/fb_mikuni/s5_fallback.png')
open('/tmp/fb_mikuni/s5.html', 'w').write(html)
print('done')

"""2026-11-25 尼崎 A1級6人のモーター答え合わせ: Codex版 s5 の行頭の中黒が丸い箇条書き記号+空白と読め、作り直し後も照合NGの場合に、
slides.py の部品で expected.json の文字そのままに s5 を作る(Codex版に合わせて黄色枠ラベル・白の「まとめ」)。"""
import json, sys
sys.path.insert(0, 'scripts')
from slides import page, render
from PIL import Image

F = 'handoff/slides/2026-11-25-amagasaki-a1-review'
OUT = '/tmp/claude-0/-home-claude/c5ca85e1-8f66-593f-bc41-3b5aadd55269/scratchpad/fb'
h = json.load(open(f'{F}/expected.json', encoding='utf-8'))['s5']
hl = {'T4': '1着14回', 'T5': '1着5回', 'T6': '乗り手や枠', 'T7': '56号機'}
inner = ''
for k in ['T4', 'T5', 'T6', 'T7']:
    t = h[k]
    assert t.count(hl[k]) == 1, k
    shown = t.replace(hl[k], f"<span class=hl>{hl[k]}</span>")
    if k in ('T4', 'T5'):
        shown = shown.replace('、', '、<br>')  # 改行位置だけ指定(文字は変えない)
    inner += f'<div style="margin-bottom:34px;padding-left:1em;text-indent:-1em">{shown}</div>'
b = (f'<div class="card" style="top:330px;height:640px;border-color:rgba(120,170,255,.35)"></div>'
     f'<div style="position:absolute;top:370px;left:110px;right:100px;font-size:38px;font-weight:700;line-height:1.5">{inner}</div>'
     f'<div style="position:absolute;top:1020px;left:80px;right:60px;font-size:38px;font-weight:900;white-space:nowrap">{h["T8"]}</div>')
html = page(5, 5, h['T1'], h['T3'], '', b, h['T9'])
html = html.replace('.tag{position:absolute;top:70px;left:80px;font-size:30px;letter-spacing:.12em;color:#ffc400;font-weight:700}',
                    '.tag{position:absolute;top:50px;left:60px;font-size:40px;color:#ffc400;border:4px solid #ffc400;padding:6px 26px;border-radius:40px;font-weight:900}')
html = html.replace('.page{position:absolute;top:70px;right:80px;font-size:30px;color:#6f8bb0', '.page{position:absolute;top:58px;right:80px;font-size:46px;color:#9fb3c8')
html = html.replace('h2{position:absolute;top:150px;left:80px;right:80px;font-size:66px', 'h2{position:absolute;top:150px;left:70px;right:80px;font-size:130px')
html = html.replace('.src{position:absolute;bottom:52px;left:80px;right:80px;font-size:23px;color:#6f8bb0', '.src{position:absolute;bottom:80px;left:80px;right:80px;font-size:27px;color:#9fb3c8')
p = render([html], OUT, contact=False)[0]
Image.open(p).resize((1122, 1402), Image.LANCZOS).save(f'{OUT}/s5_fallback.png')
open(f'{OUT}/s5.html', 'w').write(html)
print('done', p)

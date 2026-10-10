"""Draw the 128px mark and render four English store assets with Chromium."""
from pathlib import Path
import base64
import json
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
COLORS = json.loads((ROOT / 'manifest.json').read_text('utf-8'))['theme']['colors']
def color(key):
    return '#%02X%02X%02X' % tuple(COLORS[key])

def draw_logo():
    scale = 4
    canvas = Image.new('RGBA', (128 * scale, 128 * scale))
    d = ImageDraw.Draw(canvas)
    def ellipse(box, fill):
        d.ellipse(tuple(round(v * scale) for v in box), fill=fill)
    def polygon(points, fill):
        d.polygon([(round(x * scale), round(y * scale)) for x, y in points], fill=fill)
    def roundbox(box, radius, fill):
        d.rounded_rectangle(tuple(round(v * scale) for v in box), radius=radius * scale, fill=fill)
    # Sun behind a scalloped cloud; the pale rim separates the two silhouettes.
    ellipse((48, 15, 108, 75), '#957DAD')
    ellipse((52, 19, 104, 71), '#FFDFD3')
    ellipse((12, 52, 54, 94), '#957DAD')
    ellipse((30, 33, 83, 86), '#957DAD')
    ellipse((66, 50, 112, 96), '#957DAD')
    roundbox((12, 64, 112, 102), 19, '#957DAD')
    ellipse((16, 56, 54, 94), '#E0BBE4')
    ellipse((34, 37, 79, 82), '#E0BBE4')
    ellipse((66, 54, 108, 96), '#E0BBE4')
    roundbox((16, 66, 108, 98), 16, '#E0BBE4')
    roundbox((28, 86, 96, 96), 5, '#D291BC')
    # Single four-point sparkle, balanced against the sun.
    polygon([(22, 16), (25, 25), (34, 28), (25, 31), (22, 40), (19, 31), (10, 28), (19, 25)], '#957DAD')
    canvas = canvas.resize((128, 128), Image.Resampling.LANCZOS)
    dest = ROOT / 'logo' / 'logo128.png'
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest)
    assert canvas.getbbox() is not None and canvas.mode == 'RGBA'

draw_logo()
LOGO = 'data:image/png;base64,' + base64.b64encode((ROOT/'logo/logo128.png').read_bytes()).decode()
css = '''
*{box-sizing:border-box}body{margin:0;font-family:Arial,sans-serif;color:var(--ink)}
:root{--paper:#F1F3F5;--lavender:#E0BBE4;--rose:#D291BC;--pink:#FEC8D8}
.browser{width:1280px;height:800px;background:var(--ntp);position:relative;overflow:hidden}
.tabs{height:44px;background:var(--frame);color:var(--inactive);display:flex;align-items:end;gap:8px;padding:7px 12px 0}
.tab{width:228px;height:37px;border-radius:12px 12px 0 0;padding:11px 16px;font-size:13px}
.tab.active{background:var(--toolbar);color:var(--ink)}.close{float:right}.newtab{padding:9px 12px;font-size:22px}
.window-controls{margin-left:auto;display:flex;gap:30px;padding:11px 12px;font-size:16px}
.tools{height:52px;background:var(--toolbar);display:flex;align-items:center;padding:0 18px;gap:23px;font-size:22px}
.omni{height:36px;flex:1;background:var(--omni);border-radius:24px;display:flex;align-items:center;gap:13px;font-size:13px;padding:0 16px}
.omni .star{margin-left:auto;font-size:21px}.tune{font-size:18px}.profile{width:27px;height:27px;background:var(--frame);color:white;border-radius:50%;font-size:13px;display:grid;place-items:center}
.bookmarks{height:33px;background:var(--toolbar);border-bottom:1px solid #49385018;padding:9px 22px;display:flex;gap:30px;font-size:12px}
.content{text-align:center;padding-top:128px}.google{font-size:82px;line-height:1.15;letter-spacing:-4px;color:var(--accent);font-weight:500;margin-bottom:34px}
.search{width:590px;height:52px;border-radius:30px;background:var(--omni);margin:auto;display:flex;align-items:center;gap:18px;padding:0 22px;box-shadow:0 2px 9px #49385018;color:#6D626F;font-size:15px}
.search svg{width:20px;height:20px;stroke:var(--ink);fill:none;stroke-width:2}.search .mic{margin-left:auto}
.shortcuts{display:flex;justify-content:center;gap:35px;margin-top:31px}.shortcut{width:84px;font-size:12px}.circle{margin:0 auto 11px;width:47px;height:47px;border-radius:50%;display:grid;place-items:center;background:var(--toolbar);font-size:21px;color:var(--accent)}
.customize{position:absolute;right:22px;bottom:20px;border-radius:20px;background:var(--toolbar);padding:10px 16px;font-size:12px}
.intro{width:1280px;height:800px;background:var(--paper);padding:55px 65px;position:relative}
.eyebrow{font-size:12px;letter-spacing:3px;color:var(--accent)}h1{font-family:Georgia,serif;font-weight:normal}
.intro h1{font-size:53px;margin:18px 0 12px}.intro .subtitle{font-size:21px;margin:0}.intro .logo{position:absolute;right:69px;top:44px;width:100px;height:100px}
.cards{display:grid;grid-template-columns:repeat(6,1fr);gap:18px;margin-top:40px}.card{grid-column:span 2;height:205px;padding:25px;border:1px solid #49385022;border-radius:18px;display:flex;flex-direction:column;justify-content:end}
.card:nth-child(n+4){grid-column:span 3}.card strong{font-size:23px}.card .hex{font-size:15px;margin-top:10px}.card .role{font-size:14px;margin-top:8px}.intro .foot{font-size:15px;margin-top:29px}
.promo{background:var(--paper);position:relative;overflow:hidden}.small{width:440px;height:280px;display:flex;align-items:center;justify-content:center;text-align:center}
.small .copy{display:flex;align-items:center;flex-direction:column;transform:translateY(-4px)}.small img{width:78px;height:78px;margin-top:-9px;margin-bottom:2px}.small h1{font-size:31px;margin:5px 0 12px}.small p{font-size:13px;margin:0 0 19px}.small .eyebrow{font-size:10px;letter-spacing:3px}
.wide{width:1400px;height:560px}.wide .copy{position:absolute;left:61px;top:72px;width:390px}.wide img{width:94px;height:94px;margin:-15px 0 -3px -6px}.wide h1{font-size:60px;line-height:1.04;margin:8px 0 21px}.wide p{font-size:20px;line-height:1.55;margin:0 0 26px}.wide .preview{position:absolute;left:510px;top:77px;transform:scale(.66);transform-origin:top left;border:1px solid #957DAD70;border-radius:15px;overflow:hidden;box-shadow:0 18px 45px #49385022}.wide .browser{height:614px}.wide .content{padding-top:68px}.wide .cloud{position:absolute;width:620px;height:240px;border-radius:55% 45% 0 0;background:var(--lavender);right:-60px;bottom:-98px}.wide .cloud:before{content:'';position:absolute;width:320px;height:170px;border-radius:50%;background:var(--pink);left:-160px;bottom:-20px}
'''
css += ':root{' + ';'.join('--'+a+':'+color(b) for a,b in [
    ('frame','frame'),('toolbar','toolbar'),('omni','omnibox_background'),
    ('ntp','ntp_background'),('ink','ntp_text'),('accent','ntp_link'),
    ('inactive','tab_background_text')]) + '}'

def browser():
    return '''<div class="browser"><div class="tabs"><div class="tab active">New Tab <span class="close">×</span></div><div class="tab">Reading list <span class="close">×</span></div><div class="newtab">+</div><div class="window-controls"><span>−</span><span>□</span><span>×</span></div></div>
    <div class="tools"><span>←</span><span>→</span><span>↻</span><div class="omni"><span class="tune">☷</span>Search or type a URL<span class="star">☆</span></div><div class="profile">P</div><span>⋮</span></div>
    <div class="bookmarks"><span>▱ Bookmarks</span><span>▱ Reading</span><span>▱ Design</span><span>▱ Inspiration</span></div>
    <div class="content"><div class="google">Google</div><div class="search"><svg viewBox="0 0 24 24"><circle cx="10" cy="10" r="6"/><path d="m15 15 5 5"/></svg>Search Google or type a URL<svg class="mic" viewBox="0 0 24 24"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 10v2a7 7 0 0 0 14 0v-2M12 19v4"/></svg></div>
    <div class="shortcuts"><div class="shortcut"><div class="circle">▱</div>Reading</div><div class="shortcut"><div class="circle">✦</div>Inspiration</div><div class="shortcut"><div class="circle">+</div>Add shortcut</div></div></div><div class="customize">✎ &nbsp; Customize Chrome</div></div>'''

palette = [
    ('Muted Lavender', '#957DAD', 'Window frame', '#241B2D'),
    ('Pale Plum', '#E0BBE4', 'Logo & artwork', '#493850'),
    ('Dusty Rose', '#D291BC', 'Logo & artwork', '#493850'),
    ('Blush Pink', '#FEC8D8', 'Artwork · inspires pale blush page', '#493850'),
    ('Creamy Peach', '#FFDFD3', 'Toolbar & active tab', '#493850'),
]
cards=''.join(f'<div class="card" style="background:{c};color:{fg}"><strong>{n}</strong><span class="hex">{c}</span><span class="role">{role}</span></div>' for n,c,role,fg in palette)
intro=f'<div class="intro"><img class="logo" src="{LOGO}" alt="Cloud and sunset mark"><div class="eyebrow">A SOFTER SHADE OF EVENING</div><h1>Pastel Afterglow Theme</h1><p class="subtitle">A little afterglow for your everyday browser.</p><div class="cards">{cards}</div><p class="foot">Solid colors · Soft pastel palette · Minimal design · No permissions required</p></div>'
small=f'<div class="promo small"><div class="copy"><img src="{LOGO}"><h1>Pastel Afterglow</h1><p>A little afterglow for your everyday browser.</p><div class="eyebrow">CHROME THEME</div></div></div>'
wide=f'<div class="promo wide"><div class="cloud"></div><div class="copy"><img src="{LOGO}"><h1>Pastel<br>Afterglow</h1><p>Soft lavender. Warm peach.<br>A gentle glow for every tab.</p><div class="eyebrow">CHROME THEME</div></div><div class="preview">{browser()}</div></div>'
jobs=[('screenshot-1-browser',1280,800,browser(),'screenshots/en/screenshot-1-browser.png'),('screenshot-2-introduction',1280,800,intro,'screenshots/en/screenshot-2-introduction.png'),('promo-440x280',440,280,small,'promo/440x280.png'),('promo-1400x560',1400,560,wide,'promo/1400x560.png')]
with sync_playwright() as p:
    engine=p.chromium.launch(headless=True)
    page=engine.new_page(device_scale_factor=1)
    for name,w,h,body,destination in jobs:
        html='<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Pastel Afterglow Theme</title><style>'+css+'</style></head><body>'+body+'</body></html>'
        reference=ROOT/'store-assets/references'/f'{name}.html'
        reference.parent.mkdir(parents=True,exist_ok=True)
        reference.write_text(html,'utf-8')
        page.set_viewport_size({'width':w,'height':h})
        page.set_content(html)
        page.evaluate('document.fonts.ready')
        png=reference.with_suffix('.png')
        page.screenshot(path=str(png))
        target=ROOT/'store-assets'/destination
        target.parent.mkdir(parents=True,exist_ok=True)
        with Image.open(png) as img:
            assert img.size == (w,h)
            img.convert('RGB').save(target)
        print(f'Rendered {destination}: {w}x{h}')
    engine.close()
print('Logo validated: logo/logo128.png, 128x128 RGBA')

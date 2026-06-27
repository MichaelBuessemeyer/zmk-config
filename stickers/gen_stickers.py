#!/usr/bin/env python3
# Composite keycap-legend stickers for the Corne Choc Pro German-macOS layout.
# ONE 14x14mm sticker per key, all layers at once:
#   TL=BASE(0)  TR=NUM(1)  BL=SYM(2)  BR=FUN(4)  center=NAV(3)
# Plus separate orange mini-stickers for the home-row modifiers (front edge).
import os
OUT_DIR = "/Users/micha/Projects/zmk-config/stickers"
os.makedirs(OUT_DIR, exist_ok=True)

COL = {'base':'#1A1A1A','mod':'#E8590C','num':'#1971C2','sym':'#E03131','nav':'#2F9E44','fun':'#7048E8'}

ICONS = {
 'vol-': '<path d="M3 9h3.5L11 5v14L6.5 15H3z"/><path d="M14 9a4.5 4.5 0 0 1 0 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>',
 'vol+': '<path d="M3 9h3.5L11 5v14L6.5 15H3z"/><path d="M14 9a4.5 4.5 0 0 1 0 6" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/><path d="M16.7 6.3a9 9 0 0 1 0 11.4" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>',
 'mute': '<path d="M3 9h3.5L11 5v14L6.5 15H3z"/><path d="M15 9l5 6M20 9l-5 6" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/>',
 'playpause': '<path d="M3.5 5l8 7-8 7z"/><rect x="14.6" y="5" width="2.6" height="14" rx="0.6"/><rect x="19" y="5" width="2.6" height="14" rx="0.6"/>',
 'prev': '<rect x="3.4" y="5" width="2.4" height="14" rx="0.6"/><path d="M21 5l-7 7 7 7z"/><path d="M13.4 5l-6 7 6 7z"/>',
 'next': '<rect x="18.2" y="5" width="2.4" height="14" rx="0.6"/><path d="M3 5l7 7-7 7z"/><path d="M10.6 5l6 7-6 7z"/>',
 'bright-': '<circle cx="12" cy="12" r="3"/><g stroke="currentColor" stroke-width="1.7" stroke-linecap="round"><path d="M12 4.5v2"/><path d="M12 17.5v2"/><path d="M4.5 12h2"/><path d="M17.5 12h2"/></g>',
 'bright+': '<circle cx="12" cy="12" r="4.1"/><g stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M12 2.4v3"/><path d="M12 18.6v3"/><path d="M2.4 12h3"/><path d="M18.6 12h3"/><path d="M5.1 5.1l2.1 2.1"/><path d="M16.8 16.8l2.1 2.1"/><path d="M18.9 5.1l-2.1 2.1"/><path d="M7.2 16.8l-2.1 2.1"/></g>',
}

def cell_pos(p):
    if p <= 6:   return (0,0,p+1)
    if p <= 13:  return (1,0,p-6)
    if p <= 20:  return (0,1,p-13)
    if p <= 27:  return (1,1,p-20)
    if p <= 33:  return (0,2,p-27)
    if p <= 39:  return (1,2,p-33+1)
    if p <= 42:  return (0,3,p-40+5)
    return (1,3,p-43+1)

# legends per layer (46). '' empty, 'm:X' modifier, 'ic:name' icon.
base = ['⎋','Q','W','E','R','T','⌦','⌫','Y','U','I','O','P','Ü',
        '⇥','A','S','D','F','G','m:⌘','m:⌥','H','J','K','L',';','Ö',
        '⇪','Z','X','C','V','B','N','M',',','.','/','Ä',
        'm:⇧','FN','␣','⏎','⌫','⌦']
num  = ['','[','7','8','9',']','','','','','','','','',
        '',';','4','5','6','=','','','','m:⇧','m:⌃','m:⌥','m:⌘','',
        '','`','1','2','3','\\','','','','','','',
        '0','.','','','','']
sym  = ['','!','@','{','}','|','','','`','+','*','/','%','ß',
        '','#','$','(',')','=','','','&','-',':',';','"','€',
        '','^','~','[',']','\\','_','<','>','?',"'",'§',
        '','','','','','']
nav  = ['','⌘Z','⌘X','⌘C','⌘V','⌘A','','','⇞','↖','↑','↘','⇟','⌃↑',
        '','m:⌘','m:⌥','m:⌃','m:⇧','','','','','←','↓','→','','⌘⇥',
        '','','','','','','','⌫','⌦','','Ins','⌃↓',
        '','','','','','']
fun  = ['','F1','F2','F3','F4','F5','','','F6','F7','F8','F9','F10','',
        '','m:⌘','m:⌥','m:⌃','m:⇧','F11','','','ic:vol-','ic:vol+','ic:mute','ic:playpause','F12','',
        '','BT✗','BT1','BT2','BT3','BT4','ic:prev','ic:next','ic:bright-','ic:bright+','RST','BOOT',
        '','','STUD','RGB','','']

THUMBS = {40:('⇧',COL['mod'],None,None), 41:('FN',COL['fun'],None,None),
          42:('␣',COL['base'],'NAV',COL['nav']), 43:('⏎',COL['base'],'SYM',COL['sym']),
          44:('⌫',COL['base'],'NUM',COL['num']), 45:('⌦',COL['base'],None,None)}

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def parse(entry, layerkey):
    if entry == '' or entry is None: return None
    if entry.startswith('ic:'): return ('icon', entry[3:], COL[layerkey])
    if entry.startswith('m:'):  return ('text', entry[2:], COL['mod'])
    return ('text', entry, COL[layerkey])

def glyph_html(item, big=False):
    kind, val, color = item
    if kind == 'icon':
        sz = '5.2mm' if big else '4.6mm'
        return f'<svg viewBox="0 0 24 24" width="{sz}" height="{sz}" fill="currentColor" style="color:{color}">{ICONS[val]}</svg>'
    n = len(val)
    if big:  size = '3.7mm' if n<=2 else '2.8mm'
    else:    size = '4.3mm' if n<=1 else ('2.9mm' if n==2 else ('2.2mm' if n==3 else '1.9mm'))
    return f'<span style="font-size:{size};color:{color};font-weight:500;line-height:1">{esc(val)}</span>'

def composite(p):
    tl = parse(base[p],'base'); tr = parse(num[p],'num')
    bl = parse(sym[p],'sym');  br = parse(fun[p],'fun'); ce = parse(nav[p],'nav')
    out = ['<div class="ckey">']
    corners = [(tl,'top:0.7mm;left:1.1mm;text-align:left'),
               (tr,'top:0.7mm;right:1.1mm;text-align:right'),
               (bl,'bottom:0.7mm;left:1.1mm;text-align:left'),
               (br,'bottom:0.7mm;right:1.1mm;text-align:right')]
    for item, pos in corners:
        if item: out.append(f'<div style="position:absolute;{pos};line-height:1">{glyph_html(item)}</div>')
    if ce:
        cv = ce[1]                              # center = NAV layer: always green, no ring
        if cv in ('←', '↓', '↑', '→'):
            csz, cw = '4mm', '700'              # arrows: smaller base, but bold + present
        else:
            csz, cw = ('3.1mm' if len(cv) <= 2 else '2.3mm'), '500'
        out.append(f'<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);line-height:1">'
                   f'<span style="font-size:{csz};color:{COL["nav"]};font-weight:{cw}">{esc(cv)}</span></div>')
    out.append('</div>')
    return ''.join(out)

def thumb(p):
    g, gc, tag, tc = THUMBS[p]
    inner = f'<span style="font-size:5.6mm;color:{gc};font-weight:500;line-height:1">{esc(g)}</span>'
    if tag:
        inner += f'<span style="font-size:2.4mm;color:{tc};font-weight:500;margin-top:0.6mm">{tag}</span>'
    return f'<div class="ckey" style="display:flex;flex-direction:column;align-items:center;justify-content:center">{inner}</div>'

def render_half(half):
    main = ['<div class="half">']
    slot = {}
    for p in range(46):
        h,r,c = cell_pos(p)
        if h==half and r<3: slot[(r,c)] = p
    for r in range(3):
        for c in range(1,8):
            p = slot.get((r,c))
            inner = composite(p) if p is not None else '<div class="empty"></div>'
            main.append(f'<div style="grid-column:{c};grid-row:{r+1}">{inner}</div>')
    main.append('</div>')
    th = ['<div class="half thumbs">']
    tslot = {}
    for p in range(46):
        h,r,c = cell_pos(p)
        if h==half and r==3: tslot[c]=p
    for c in range(1,8):
        p = tslot.get(c)
        inner = thumb(p) if p is not None else '<div class="empty"></div>'
        th.append(f'<div style="grid-column:{c}">{inner}</div>')
    th.append('</div>')
    return f'<div class="halfwrap">{"".join(main)}{"".join(th)}</div>'

# sample "how to read" keycap (zoomed ~30mm), using the Q/A-style example
def sample():
    spots = [('BASE','base','Q','top:2mm;left:2.4mm'),
             ('NUM','num','7','top:2mm;right:2.4mm'),
             ('SYM','sym','@','bottom:2mm;left:2.4mm'),
             ('FUN','fun','F1','bottom:2mm;right:2.4mm')]
    h = ['<div style="position:relative;width:30mm;height:30mm;border:0.3mm dashed #999;border-radius:2.5mm;background:#fff;flex:none">']
    for name,k,g,pos in spots:
        h.append(f'<div style="position:absolute;{pos};text-align:left"><div style="font-size:6mm;color:{COL[k]};font-weight:500;line-height:1">{esc(g)}</div></div>')
    h.append(f'<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)"><span style="font-size:7mm;color:{COL["nav"]};font-weight:700">←</span></div>')
    h.append('</div>')
    return ''.join(h)

key_items = [('base','↖ top-left'),('num','↗ top-right'),('sym','↙ bottom-left'),('fun','↘ bottom-right'),('nav','● center')]
KEY = ''
for k,lbl in key_items:
    layernum = {'base':'0','num':'1','sym':'2','nav':'3','fun':'4'}[k]
    KEY += (f'<div style="display:flex;align-items:center;gap:2mm;margin-bottom:1.8mm">'
            f'<span style="width:4mm;height:4mm;border-radius:1mm;background:{COL[k]};display:inline-block"></span>'
            f'<span style="font-size:3.2mm"><b style="font-weight:500">{lbl}</b> &nbsp; layer {layernum} · {k.upper()}</span></div>')
KEY += (f'<div style="display:flex;align-items:center;gap:2mm;margin-top:2mm">'
        f'<span style="width:4mm;height:4mm;border-radius:1mm;background:{COL["mod"]};display:inline-block"></span>'
        f'<span style="font-size:3.2mm">orange = modifiers ⌘⌥⌃⇧ (home-row mods are separate front-edge stickers below)</span></div>')

mods = ['⌘','⌥','⌃','⇧','⇧','⌃','⌥','⌘']; labels = ['A','S','D','F','J','K','L',';']
STRIP = ''.join(
    f'<div style="display:flex;flex-direction:column;align-items:center">'
    f'<div class="modcell"><span style="font-size:2.6mm;color:{COL["mod"]};font-weight:500;line-height:1">{m}</span></div>'
    f'<span style="font-size:1.8mm;color:#999;margin-top:0.5mm">{l}</span></div>'
    for m,l in zip(mods,labels))

HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4 landscape; margin: 8mm; }}
* {{ box-sizing: border-box; }}
html,body {{ margin:0;padding:0;font-family:-apple-system,"SF Pro Text","Helvetica Neue",Arial,sans-serif;
  color:#1A1A1A;-webkit-print-color-adjust:exact;print-color-adjust:exact; }}
h1 {{ font-size:5.5mm;margin:0 0 1.5mm;font-weight:600; }}
.sub {{ font-size:3mm;color:#555;margin:0 0 3mm;line-height:1.5;max-width:250mm; }}
.top {{ display:flex;gap:10mm;align-items:flex-start;margin-bottom:4mm; }}
.calib {{ display:flex;align-items:center;gap:2.5mm;margin-top:3mm;font-size:2.8mm;color:#333; }}
.cbox {{ width:10mm;height:10mm;border:0.3mm solid #1A1A1A;flex:none; }}
.board {{ display:flex;gap:12mm;margin-top:2mm; }}
.halfwrap {{ display:flex;flex-direction:column; }}
.half {{ display:grid;grid-template-columns:repeat(7,13mm);gap:3.5mm; }}
.thumbs {{ margin-top:3.5mm; }}
.ckey {{ width:13mm;height:13mm;border:0.2mm dashed #c4c4c4;border-radius:1.2mm;position:relative;background:#fff; }}
.empty {{ width:13mm;height:13mm; }}
.modnote {{ font-size:3mm;color:#444;margin:5mm 0 2.2mm; }}
.modstrip {{ display:flex;gap:3.5mm; }}
.modcell {{ width:4mm;height:3mm;border:0.15mm dashed #c4c4c4;border-radius:0.6mm;display:flex;align-items:center;justify-content:center; }}
</style></head><body>
  <h1>Corne Choc Pro — all-layer keycap stickers (German · macOS)</h1>
  <div class="sub">One sticker per key shows every layer at once, color-coded by layer. Print on sticker foil at
    <b>100% / actual size</b> (turn OFF "fit to page"). Each cell is 13&nbsp;mm; cut on the
    dashed line and keep it centered (caps are negatively curved). Home-row modifiers are separate mini-stickers
    (bottom) for the front edge of the cap.</div>
  <div class="top">
    <div>{sample()}<div style="font-size:2.8mm;color:#777;margin-top:1.5mm;text-align:center;width:30mm">how to read each sticker</div></div>
    <div>{KEY}<div class="calib"><div class="cbox"></div><span>⟵ must measure exactly <b>10&nbsp;mm</b> when printed</span></div></div>
  </div>
  <div class="board">{render_half(0)}{render_half(1)}</div>
  <div class="modnote">Home-row modifiers — print <b>smaller</b>, stick on the <b>front edge</b> of A&nbsp;S&nbsp;D&nbsp;F / J&nbsp;K&nbsp;L&nbsp;; :</div>
  <div class="modstrip">{STRIP}</div>
</body></html>'''

path = os.path.join(OUT_DIR, "corne_keycap_stickers.html")
open(path,"w").write(HTML)
print("wrote", path, len(HTML), "bytes")

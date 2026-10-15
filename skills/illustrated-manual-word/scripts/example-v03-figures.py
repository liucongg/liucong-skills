#!/usr/bin/env python3
"""Original instructional plates: one watch geometry, one pump geometry, explicit states."""
from pathlib import Path
from xml.sax.saxutils import escape
import argparse, json
INK='#283239'; MID='#7A858D'; BLUE='#2368B5'; PAPER='#FAFAF8'
DEFS='''<defs>
<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#FBFCFD"/><stop offset=".4" stop-color="#DCE1E5"/><stop offset=".68" stop-color="#F5F7F8"/><stop offset="1" stop-color="#AEB8C0"/></linearGradient>
<linearGradient id="rim" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#9BA7B1"/><stop offset=".3" stop-color="#F5F7F8"/><stop offset="1" stop-color="#B2BCC4"/></linearGradient>
<linearGradient id="dark" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#48535B"/><stop offset=".5" stop-color="#17232C"/><stop offset="1" stop-color="#313E48"/></linearGradient>
<linearGradient id="rubber" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#909A9F"/><stop offset=".35" stop-color="#C8CED1"/><stop offset="1" stop-color="#ADB6BB"/></linearGradient>
<pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><path d="M0 0V10" stroke="#A6B0B7" stroke-width="1.2"/></pattern>
<marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto" markerUnits="strokeWidth"><path d="M0 0L8 4.5L0 9" fill="#2368B5"/></marker>
<marker id="grey" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto" markerUnits="strokeWidth"><path d="M0 0L7 4L0 8" fill="#283239"/></marker>
</defs>'''
def txt(x,y,s,size=26,color=INK,anchor='start',weight=400):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(s)}</text>'
def line(x1,y1,x2,y2,color=BLUE,width=4,arrow=True):
    marker='grey' if color==INK else 'arrow'
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"'+(f' marker-end="url(#{marker})"' if arrow else '')+'/>'
def leader(points,label,x,y):
    a=points[0]; path=' '.join(('M' if i==0 else 'L')+f'{p[0]} {p[1]}' for i,p in enumerate(points))
    return f'<path d="{path}" fill="none" stroke="{MID}" stroke-width="1.6"/><circle cx="{a[0]}" cy="{a[1]}" r="4" fill="{INK}"/>'+txt(x,y,label,31)
def screw(x,y,r=7):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#DDE3E7" stroke="{MID}" stroke-width="1.3"/><path d="M{x-r*.5} {y-r*.5}L{x+r*.5} {y+r*.5}M{x-r*.5} {y+r*.5}L{x+r*.5} {y-r*.5}" stroke="{MID}" stroke-width="1.1"/>'
def svg(body,w,h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>text{{font-family:PingFang SC,Noto Sans CJK SC,sans-serif}}</style>{DEFS}<rect width="{w}" height="{h}" fill="{PAPER}"/>{body}</svg>'

def watch(x,y,scale=1,shift=0,pressed=False,show_arrow=False,insert=False,upper=True):
    # Both state plates use this exact case, release-button and band definition.
    out=[]
    if upper:
        out += ['<path d="M-104 -176L-90 -275Q0 -291 90 -275L104 -176Z" fill="url(#rubber)" stroke="#74818B" stroke-width="2"/>',
                '<path d="M-94 -183L-82 -264Q0 -275 82 -264L94 -183" fill="none" stroke="#DDE1E3" stroke-width="2"/>']
    out += [f'<g transform="translate({shift},0)"><path d="M-104 176L-88 288Q0 310 88 288L104 176Z" fill="url(#rubber)" stroke="#74818B" stroke-width="2"/>',
            '<path d="M-90 185L-78 278Q0 292 78 278L90 185" fill="none" stroke="#DDE1E3" stroke-width="2"/>',
            '<rect x="-119" y="168" width="238" height="26" rx="10" fill="url(#rim)" stroke="#74818B" stroke-width="1.8"/>',
            '<path d="M-105 178H105" stroke="#EFF2F4" stroke-width="2"/>',
            '<circle cx="0" cy="252" r="10" fill="#BDC5C9" stroke="#929FA6" stroke-width="1.3"/></g>',
            '<rect x="-148" y="-152" width="310" height="338" rx="62" fill="#AAB5BD" stroke="#586773" stroke-width="2.2"/>',
            '<rect x="-157" y="-167" width="310" height="338" rx="62" fill="url(#metal)" stroke="#667681" stroke-width="2.2"/>',
            '<rect x="-145" y="-155" width="286" height="314" rx="54" fill="none" stroke="#EFF3F5" stroke-width="2"/>',
            '<rect x="-177" y="-105" width="22" height="56" rx="11" fill="url(#rim)" stroke="#63717A" stroke-width="2"/>',
            '<path d="M-173 -100V-54M-166 -100V-54M-159 -99V-56" stroke="#88949D" stroke-width="1"/>',
            '<rect x="-170" y="-7" width="13" height="72" rx="6" fill="url(#rim)" stroke="#63717A" stroke-width="1.6"/>',
            '<circle cx="-2" cy="0" r="113" fill="url(#rim)" stroke="#727F88" stroke-width="2"/>',
            '<circle cx="-2" cy="0" r="102" fill="url(#dark)" stroke="#23333D" stroke-width="2"/>',
            '<circle cx="-2" cy="0" r="91" fill="none" stroke="#647078" stroke-width="1"/>']
    for dx,dy in [(-34,-34),(34,-34),(-34,34),(34,34)]:
        out += [f'<circle cx="{dx-2}" cy="{dy}" r="24" fill="#101C24" stroke="#64747D" stroke-width="2"/>',
                f'<ellipse cx="{dx-8}" cy="{dy-8}" rx="9" ry="6" fill="#455862" opacity=".6"/>']
    for dx,dy in [(0,-76),(0,76),(-76,0),(76,0)]:
        out += [f'<circle cx="{dx-2}" cy="{dy}" r="6" fill="#CBD3D7" stroke="#657580" stroke-width="1"/>']
    out += ['<rect x="-46" y="-143" width="88" height="17" rx="8" fill="#A4AFB7" stroke="#63747F" stroke-width="1.6"/>',
            f'<rect x="-46" y="128" width="88" height="17" rx="8" fill="{BLUE if pressed else "#A4AFB7"}" stroke="{BLUE if pressed else "#63747F"}" stroke-width="1.6"/>']
    if pressed:
        out += ['<path d="M-25 134H21" stroke="#92C7F0" stroke-width="2"/>']
    if show_arrow:
        out += [line(-125 if not insert else -240,201,-245 if not insert else -127,201,width=6)]
    return f'<g transform="translate({x},{y}) scale({scale})">'+''.join(out)+'</g>'

def pump(x,y,scale=1,state='suction',labels=False):
    # Working chamber is LEFT of piston; valves allow bottom-to-top flow.
    piston=745 if state=='suction' else 545
    intake=state=='suction'; outlet=not intake
    out=[]
    out += ['<ellipse cx="602" cy="615" rx="416" ry="23" fill="#D7DCDF" opacity=".45"/>',
            '<path d="M265 513H915L965 552H215Z" fill="url(#metal)" stroke="#6D7A84" stroke-width="2"/>',
            '<path d="M215 552H965V577H215Z" fill="#B2BEC5" stroke="#6D7A84" stroke-width="2"/>']
    for q in [(260,550),(914,550),(312,521),(860,521)]: out.append(screw(*q))
    # supports mechanically meet the cylinder and the base.
    out += ['<path d="M355 440H406V516H332Z M815 440H865L891 516H815Z" fill="url(#metal)" stroke="#6D7A84" stroke-width="2"/>',
            '<path d="M280 250H888Q910 250 910 275V445Q910 465 888 465H280Z" fill="url(#metal)" stroke="#677783" stroke-width="2.3"/>',
            '<path d="M285 258H890V284H310V430H890V457H285Z" fill="url(#hatch)" stroke="#73828B" stroke-width="1.5"/>',
            '<rect x="310" y="284" width="580" height="146" fill="#F3F6F7" stroke="#73828B" stroke-width="1.6"/>',
            f'<rect x="310" y="284" width="{piston-310}" height="146" fill="#D6E9F5"/>',
            f'<path d="M312 306H{piston-8} M312 409H{piston-8}" stroke="#B6D5E9" stroke-width="1"/>',
            '<rect x="267" y="237" width="27" height="242" rx="5" fill="url(#rim)" stroke="#687883" stroke-width="2"/>',
            '<rect x="878" y="237" width="28" height="242" rx="5" fill="url(#rim)" stroke="#687883" stroke-width="2"/>']
    for xx in [280,892]:
        for yy in [268,450]: out.append(screw(xx,yy,5))
    # Cylinder head and manifold. The two open ducts connect to the SAME chamber.
    out += ['<path d="M329 285V96 M329 430V591" stroke="#687883" stroke-width="59" fill="none"/>',
            '<path d="M329 285V96 M329 430V591" stroke="#C4CDD3" stroke-width="54" fill="none"/>',
            '<path d="M329 285V96 M329 430V591" stroke="#D6E9F5" stroke-width="26" fill="none"/>']
    for yy in [111,215,485,575]:
        out += [f'<rect x="293" y="{yy}" width="72" height="13" rx="3" fill="url(#rim)" stroke="#647580" stroke-width="1.5"/>']
    # Each non-return valve has a seat, ball and chamber. Ball lifts UP when open.
    for yy,is_open in [(165,outlet),(525,intake)]:
        out += [f'<rect x="287" y="{yy-43}" width="84" height="80" rx="8" fill="url(#metal)" stroke="#687883" stroke-width="2"/>',
                f'<path d="M311 {yy+25}V{yy-36}H347V{yy+25}" fill="#D6E9F5" stroke="#9AACB7" stroke-width="1"/>',
                f'<path d="M298 {yy+24}H315L321 {yy+13} M337 {yy+13}L343 {yy+24}H360" fill="none" stroke="#526873" stroke-width="3"/>',
                f'<circle cx="329" cy="{yy-11 if is_open else yy+5}" r="15" fill="url(#rim)" stroke="#5D717D" stroke-width="2"/>',
                f'<path d="M299 {yy-24}H311 M347 {yy-24}H359" stroke="#526873" stroke-width="2"/>']
    # Steel rod, piston head, two seals and right gland.
    out += [f'<rect x="{piston}" y="347" width="{1050-piston}" height="23" fill="url(#rim)" stroke="#687883" stroke-width="1.7"/>',
            f'<rect x="{piston-14}" y="292" width="34" height="130" rx="4" fill="url(#metal)" stroke="#5E727F" stroke-width="2.2"/>',
            f'<rect x="{piston-10}" y="287" width="9" height="140" rx="2" fill="#425763"/>',
            f'<rect x="{piston+9}" y="287" width="7" height="140" rx="2" fill="#425763"/>',
            '<rect x="908" y="325" width="37" height="67" rx="5" fill="url(#metal)" stroke="#687883" stroke-width="2"/>',
            '<path d="M912 331V386M938 331V386" stroke="#96A5AE" stroke-width="2"/>',
            '<rect x="1044" y="324" width="18" height="69" rx="7" fill="url(#dark)" stroke="#374C58" stroke-width="1.7"/>']
    out += [line(965,290,1040,290,color=INK,width=5) if intake else line(1040,290,965,290,color=INK,width=5)]
    if intake:
        out += [line(329,609,329,573,width=4),line(329,477,329,444,width=4),line(397,356,502,356,width=4)]
        out += [txt(400,530,'入口阀 · 开',32,BLUE),txt(400,171,'出口阀 · 关',32)]
    else:
        out += [line(490,356,390,356,width=4),line(329,266,329,225,width=4),line(329,113,329,69,width=4)]
        out += [txt(400,530,'入口阀 · 关',32),txt(400,171,'出口阀 · 开',32,BLUE)]
    if labels:
        out += [leader([(590,272),(660,210),(730,210)],'剖开的缸壁',740,217),
                leader([(piston+4,393),(770,482),(952,482)],'活塞与密封圈',965,490),
                txt(210,48,'送往出口',22,BLUE),txt(205,643,'来自水源',22,BLUE)]
    return f'<g transform="translate({x},{y}) scale({scale})">'+''.join(out)+'</g>'

def make(out):
    out=Path(out); out.mkdir(parents=True,exist_ok=True)
    plates={}
    b=watch(510,360,.94,pressed=True)
    b+=leader([(506,488),(710,488),(780,434)],'表带释放按钮',795,436)
    b+=leader([(410,530),(243,613),(145,613)],'表带连接端',55,620)
    b+=txt(780,480,'不是侧面的数码表冠',22,MID)
    b+=txt(46,50,'01 / 找到表背的释放按钮',24,BLUE,weight=600)
    b+=txt(45,700,'看表背，而不是看屏幕；靠近表带连接处的短条按钮才是操作位置。',23)
    plates['watch-locate']=(b,1300,745)
    b=txt(45,46,'02 / 持续按住，沿槽滑出',24,BLUE,weight=600)
    b+=watch(350,318,.73,pressed=True,show_arrow=True,upper=False)
    b+=watch(995,318,.73,shift=-185,pressed=True,show_arrow=True,upper=False)
    b+=txt(350,580,'先按住释放按钮',26,anchor='middle',weight=500)
    b+=txt(995,580,'保持按住，同时横向滑出',26,anchor='middle',weight=500)
    b+=txt(670,334,'→',45,MID,anchor='middle')
    plates['watch-remove']=(b,1350,625)
    b=txt(45,46,'03 / 沿同一条槽装回',24,BLUE,weight=600)
    b+=watch(390,310,.80,shift=-205,show_arrow=True,insert=True,upper=False)
    b+=watch(1040,310,.80,upper=False)
    b+=txt(390,592,'文字朝向你，连接端对齐槽口',24,anchor='middle')
    b+=txt(1040,592,'滑入，直到感到并听到咔嗒声',24,anchor='middle')
    plates['watch-insert']=(b,1400,650)
    b=txt(45,50,'04 / 装好后再检查',24,BLUE,weight=600)
    for i,(title,sub) in enumerate([('锁定',['不按释放按钮时，','不应自由滑动']),('卡住',['重新按住释放按钮，','再沿槽滑动']),('未锁住',['不要佩戴；','按官方指南重新装配'])]):
        x=45+i*440
        b+=f'<rect x="{x}" y="104" width="410" height="178" rx="14" fill="#F0F3F5" stroke="#D8DFE4"/>'
        b+=txt(x+25,155,title,30,INK,weight=600)
        b+=txt(x+25,208,sub[0],28)
        b+=txt(x+25,246,sub[1],28)
    plates['watch-check']=(b,1380,322)
    b=txt(45,52,'同一个腔体，两只单向阀',28,BLUE,weight=600)
    b+=pump(50,62,1.03,'suction',True)
    b+=txt(1090,423,'拉',28,BLUE)
    plates['pump-overview']=(b,1450,770)
    b=txt(45,46,'A / 吸入：活塞向右，左侧容积增大',34,BLUE,weight=600)
    b+=pump(20,70,1.04,'suction')
    b+=txt(1220,370,'吸入',30,BLUE,weight=500)
    b+=txt(45,782,'B / 排出：活塞向左，左侧容积减小',34,BLUE,weight=600)
    b+=pump(20,806,1.04,'delivery')
    b+=txt(1220,1110,'排出',30,BLUE,weight=500)
    plates['pump-strokes']=(b,1420,1480)
    for name,(body,w,h) in plates.items():(out/(name+'.svg')).write_text(svg(body,w,h),encoding='utf-8')
    model={'watch':{'case_reused':True,'button':'back-lower','remove_slide':'left','insert_slide':'right'},
           'pump':{'working_chamber':'left-of-piston','flow':'bottom-in/top-out',
                   'states':[{'name':'suction','piston_x':745,'inlet_open':True,'outlet_open':False},
                             {'name':'delivery','piston_x':545,'inlet_open':False,'outlet_open':True}],
                   'notice':'Textbook single-acting piston model; not a named product or pressure-rated design.'}}
    for s in model['pump']['states']:
        assert s['inlet_open'] != s['outlet_open']
        assert 310 < s['piston_x'] < 878
    (out/'model.json').write_text(json.dumps(model,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'ok':True,'plates':list(plates),'state_assertions':4},ensure_ascii=False))
if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('out'); make(p.parse_args().out)

#!/usr/bin/env python3
"""Build a source-bound sample manuscript; reuses a reviewed local AI context image."""
from pathlib import Path
import argparse, json, hashlib

def main(project):
    root=Path(project).resolve(); figs=root/'figures'
    if not (figs/'water-context.png').is_file() or not (root/'generation.json').is_file():
        raise SystemExit('Supply a real generated context image and its actual generation.json; no placeholder is allowed.')
    sources=[
      {'id':'S1','title':'Apple Support · Change your Apple Watch band','url':'https://support.apple.com/en-us/108908','kind':'official','verified':True,'retrieved_on':'2026-10-12','excerpt':'Hold down the band release button, then slide the band across to remove it. Make sure that the text on the band is facing you, then slide the new band in until you feel and hear a click. Never force the band into the slot. Do not wear your Apple Watch if the band is sliding.'},
      {'id':'S2','title':'Virtual Labs · Single Acting Reciprocating Pump','url':'https://fm-iitk.vlabs.ac.in/exp/reciprocating-pump/theory.html','kind':'institutional','verified':True,'retrieved_on':'2026-10-12','excerpt':'When the piston moves towards right, the suction valve opens and liquid is forced into the left side of the piston. When the piston moves to the left, high pressure builds up, the delivery valve opens and liquid is forced into the delivery pipe.'},
      {'id':'S3','title':'Engineers Edge · Positive Displacement Pump Operation','url':'https://www.engineersedge.com/pumps/positive_disp_pump_operation.htm','kind':'reference','verified':True,'retrieved_on':'2026-10-12','excerpt':'Check valves in the suction and discharge ports allow flow in only one direction. The volume of liquid moved in one cycle equals the change in cylinder liquid volume during the piston travel.'}]
    claims=[{'id':'C1','text':'表带释放按钮需持续按住；沿槽滑出而非向外拔或扭。','source_ids':['S1'],'status':'verified'},
            {'id':'C2','text':'表带文字朝向操作者，滑入直到感到并听到咔嗒声；未锁住不能佩戴。','source_ids':['S1'],'status':'verified'},
            {'id':'C3','text':'本单作用教学模型右移活塞增加左侧工作腔，吸入时入口开出口关；排出时相反。','source_ids':['S2','S3'],'status':'verified'}]
    parts=[{'id':'W1','name':'表壳背面'},{'id':'W2','name':'表带释放按钮'},{'id':'W3','name':'表带连接端'},
           {'id':'P1','name':'缸体/左侧工作腔'},{'id':'P2','name':'活塞/活塞杆/密封圈'},
           {'id':'P3','name':'入口止回阀'},{'id':'P4','name':'出口止回阀'}]
    definitions=[
      ('F01','watch-locate','overview','先在哪里按？','下方短条按钮是操作位置；传感器只帮助辨认表背，未复刻某个机型的配置。','表背、表带连接端与被强调的下方释放按钮。',['C1'],['S1'],['W1','W2','W3'],150),
      ('F02','watch-remove','sequence','按住之后向哪里滑？','同一表壳、同一条槽；蓝色表示持续按压与横向滑动，不表示朝屏幕外拔出。','两幅共享结构的手表背面图，按钮保持按下，表带向左滑出。',['C1'],['S1'],['W1','W2','W3'],164),
      ('F03','watch-insert','sequence','新表带如何装回？','与滑出方向相反，沿槽装入。文字朝向操作者；勿强塞。','新表带从左向右滑入同一条连接槽。',['C2'],['S1'],['W1','W2','W3'],164),
      ('F04','watch-check','detail','装好后怎样判断？','三种检查与处理；具体表带的额外步骤以官方型号说明为准。','锁定、卡住和未锁住三种情况的短检查提示。',['C1','C2'],['S1'],['W2','W3'],164),
      ('F05','water-context','context','先观察一个熟悉的水流情境','AI情境插图，不是实拍，也不作为活塞泵内部结构的证据。','清水从玻璃壶连续流入杯中，无机构或数据标注。',[],[],[],148),
      ('F06','pump-overview','section','容积和单向阀各负责什么？','教学剖面：活塞改变左侧腔体容积；两只止回阀限定从下方入口到上方出口的方向。','活塞泵剖面展示缸壁、密封活塞、杆与导向、两只阀、支架及基座。',['C3'],['S2','S3'],['P1','P2','P3','P4'],156),
      ('F07','pump-strokes','state-pair','为什么往返运动没有把水原路推回？','上下两图共用同一缸体和阀座；只改变活塞位置、阀球位置与当前流向。蓝箭头为水流。','吸入时入口阀开出口关；排出时入口关出口开。',['C3'],['S2','S3'],['P1','P2','P3','P4'],146)]
    figures=[]; assets=[]
    for fid,name,kind,question,caption,alt,cids,sids,pids,width in definitions:
        method='generated' if name=='water-context' else 'svg'; role='context' if method=='generated' else 'technical'
        fig={'id':fid,'asset_id':'A'+fid[1:],'method':method,'role':role,'kind':kind,'question':question,'caption':caption,'alt_text':alt,'png':f'figures/{name}.png','provenance':'original','claim_ids':cids,'source_ids':sids,'part_ids':pids,'width_mm':width}
        asset={'id':fig['asset_id'],'path':fig['png'],'method':method,'role':role,'purpose':question,'alt_text':alt,'source_ids':sids,'width_mm':width,'sha256':hashlib.sha256((root/fig['png']).read_bytes()).hexdigest(),
               'rights':'原创技术重绘，基于公开说明作个人评估，非官方且无品牌授权；不含官方原页。' if method=='svg' else 'AI生成情境插图；对外使用须遵守当前生成服务条款。',
               'decision_reason':'结构/方向/状态需确定且同源，选择SVG，不用独立生图猜机构。' if method=='svg' else '情境与玻璃/水材质不含产品结构或参数，采用生成图片并明确限制。'}
        if method=='svg': fig['svg']=f'figures/{name}.svg'; asset['svg']=fig['svg']
        else: asset['generation']=json.loads((root/'generation.json').read_text(encoding='utf-8'))
        figures.append(fig); assets.append(asset)
    def p(text): return {'type':'paragraph','text':text}
    def f(i): return {'type':'figure','id':f'F{i:02d}'}
    def c(label,text): return {'type':'callout','label':label,'text':text}
    pages=[
      {'kicker':'样章 01 / 真实对象的操作图','title':'换表带：先松开，再滑出','lead':'动作只有两步，难点是按对位置，并在滑动时保持按住。',
       'blocks':[p('把手表屏幕朝下，放在干净的无绒软布或软垫上。先确认新表带与表壳尺寸兼容；链式表带另有拆分步骤，不直接套用本页。[S1]'),f(1),f(2),c('滑不动时','不要增加拉力或扭转表带。重新按住释放按钮，确认没有松手，再沿连接槽滑出。')]},
      {'kicker':'样章 01 / 装回与检查','title':'“滑进去了”还不等于锁好了','lead':'装回要沿原来的槽，最后确认它不会自行滑动。',
       'blocks':[p('让表带上的文字朝向你，保持连接端与槽口对齐，滑入直到感到并听到咔嗒声。不要为了追求“卡牢”把不兼容的表带硬塞进去。[S1]'),f(3),f(4),
                 {'type':'table','headers':['你看到的情况','下一步'], 'rows':[['不按释放按钮，表带仍自由滑动','不要佩戴；按官方指南重新安装。'],['听不到咔嗒声或无法锁住','勿强塞，核对尺寸与连接端方向。'],['使用链式表带、海洋/回环等款式','查对应款式的额外步骤，不把通用双图当全套指南。']]},
                 c('图版范围','这里忠实重建操作位置与滑动关系，不声称毫米级复刻某一型号。传感器和表壳细节作识别性简化；真实产品以官方指南为准。')]},
      {'kicker':'样章 02 / 从情境进入原理','title':'活塞来回，水却向前','lead':'往返运动只改变容积；真正决定水往哪走的，是两只单向阀。',
       'blocks':[f(5),p('倒水时，水顺着高度差流走。泵则由外部机械功驱动，改变腔体压力，再通过阀门把流动组织起来；不能把“吸水”理解成活塞隔空抓住了水。[S2][S3]'),f(6),c('先认结构','蓝色为水与当前流向，灰色为固体。活塞右侧不是本模型的工作腔；剖开只是为了看内部，并非真的缺了一面缸壁。')]},
      {'kicker':'样章 02 / 同一机构的两个状态','title':'两扇门，轮流打开','lead':'跟着活塞看腔体大小，再看哪个阀离开阀座。',
       'blocks':[f(7),{'type':'table','headers':['当前状态','左侧工作腔','入口阀 / 出口阀'],'rows':[['吸入：活塞向右','容积增大，水从入口进入','开 / 关'],['排出：活塞向左','容积减小，水从出口排出','关 / 开']]},
                 p('止回阀响应压差，不需要人按顺序去开关。若取消它们，单凭活塞往返就不能保证本图的单向输送。这里省略驱动曲柄、真实密封设计、瞬态损失和气蚀等问题。[S2][S3]'),
                 c('安全与适用范围','这是单作用泵的教学模型，不对应任何产品的压力等级、尺寸或可制造设计。不要按图制作密闭加压装置或把它用于维修。')]}
    ]
    book={'schema_version':'0.3','media_manifest':'media.json','delivery_kind':'sample-chapter',
      'sample_objectives':['正确表达真实对象的按压/滑动','同源剖面与两个阀状态','正确区分生成情境图与原理证据'],
      'sample_limits':'两个可阅读样章，不是整本百科、厂家手册或毫米级1:1认证；不宣称用户已经认可审美。',
      'title':'表带更换与活塞泵 · 图解样章','reader':'无专业背景的成年人','mode':'real-structure','scope':'表带更换操作与单作用活塞泵原理的非官方教学说明。',
      'series':'图解样章','font':'PingFang SC','page_layout':'fixed',
      'design':{'accent':'263338','ink':'263338','body_pt':10.3,'heading_pt':23,'line_spacing':1.19},
      'sources_on_new_page':True,'include_sources':True,
      'figure_notice':'图版说明：表带操作图与泵剖面为原创SVG绘制，参数和比例不作制造依据。水流情境图由Grok Imagine生成并编辑，明确不作证据。正文、图注、表格及来源可编辑；图内标签/零件随PNG嵌入，SVG与状态定义另存。官方原图只在本地研究目录作参照，不包含在本Word或再发行Skill包中。',
      'sources':sources,'claims':claims,'parts':parts,'figures':figures,'pages':pages}
    (root/'book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2),encoding='utf-8')
    (root/'media.json').write_text(json.dumps({'assets':assets},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'ok':True,'figures':len(figures),'svg':6,'generated':1,'editorial_units':4,'source_sheet':True}))
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('project');main(ap.parse_args().project)

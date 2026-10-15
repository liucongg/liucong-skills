#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the complete, sourced visual-baseline manuscript. Does not fake external retrieval."""
import json, datetime, pathlib, sys
root=pathlib.Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
day='2026-10-11'  # Frozen example retrieval date; never pretend a rerun did fresh research.
def source(i,title,url,excerpt,use):
    return dict(id=i,title=title,url=url,excerpt=excerpt,use=use,kind='official',verified=True,retrieved_on=day,license='reference-only; no external figures reproduced')
sources=[
 source('S01','HARIO smart G：组装顺序','https://global.hario.com/faq/grinder_6_en.pdf','Insert the washer and shaft into the hopper from the top. Next, place the hopper shaft cover over the shaft from below and insert it into the grooves at the end of the body. After this, push the spring.','核对真实部件名称和轴向关系；不用于复刻厂家外观'),
 source('S02','HARIO：磨豆机拆解','https://global.hario.com/faq/grinder_7_en.pdf','Remove the spring and the hopper shaft cover from bottom of the hopper. Finally, remove the shaft and washer to finish disassem-bly.','说明清理拆解中存在的小件和顺序；具体机型必须对照其手册'),
 source('S03','HARIO：豆子从哪里进入、咖啡粉从哪里落下','https://global.hario.com/faq/grinder_2_en.pdf','Open the lid and put the coffee beans in the hopper (top part). The ground coffee come out from the hopper and drop into the bottle (lower part).','支撑使用流程和粉末路径'),
 source('S04','HARIO FAQ：Grinder 保养与材料限制','https://global.hario.com/faq/','All parts of the coffee grinders can be disassembled and washed, apart from wooden products and those made with iron burr. Be careful when washing because there are many small parts that could be easily lost.','支撑清理提醒；不把陶瓷款水洗规则套给木件或铁磨芯'),
 source('S05','Baratza：Stepped vs. Stepless','https://www.baratza.com/en-us/blog/product-guides/stepped-vs-stepless','Each grind adjustment moves the burrs a set distance closer or apart from each other, and that distance determines the size of your grind.','只解释磨芯间隙的一般机制；不引用该品牌电动款的档位或操作到手摇机'),
 source('S06','HARIO：研磨粗细的通用说明','https://global.hario.com/faq/grinder_1_en.pdf','Generally the coarseness of ground can be adjusted by turning the grind adjustment knob or nut depends on the type of mill. Check which type of mill you have.','支撑各机型调整装置不同；明确不能跨型号通用点击数')]
parts=[('01','摇柄','将手的动作传给主轴'),('02','上盖','盖住储豆仓'),('03','垫圈','轴向小件，拆卸时注意保管'),('04','主轴','连接摇柄与内磨芯'),('05','弹簧','磨芯组件中的轴向小件'),('06','储豆机身','容纳咖啡豆并承接磨芯'),('07','外磨芯','与内磨芯组成研磨区'),('08','内磨芯','随轴转动，与外磨芯配合'),('09','定位销','定位小件，不要遗漏'),('10','调节旋钮','改变磨芯的相对位置'),('11','接粉杯','收集落下的咖啡粉')]
claims=[('C01','机身上部装豆，粉末落入下部接粉杯。',['S03']),('C02','参考结构含主轴、垫圈、弹簧、内外磨芯及调节旋钮等部件。',['S01','S02']),('C03','调整磨芯的相对距离可以改变研磨粗细。',['S05','S06']),('C04','拆卸过程中存在容易遗失的小件；木件和铁磨芯不应套用水洗方法。',['S04']),('C05','调整装置、方向与档位必须按具体机型确认。',['S06']),('C06','拆卸和重装时需要核对磨芯、弹簧、垫圈和旋钮等组件。',['S01','S02'])]
names=['F01-hero','F02-overview','F03-exploded','F04-section','F05-adjust','F06-operation','F07-care','F08-check']
figspec=[
 ('overview','整机在读物里怎样出现？','整机教学模型。以真实锥刀研磨机制为依据，外观、配色与比例为原创设计，不对应某一款产品。',['C01','C02'],['S01','S03'],['P01','P02','P06','P11']),
 ('overview','拿在手里时先认识哪些部件？','外部件号沿用全书：01摇柄、02上盖、06储豆机身、11接粉杯。里面的组件在下一张爆炸图展开。',['C01','C02'],['S01','S03'],['P01','P02','P06','P11']),
 ('exploded','被外壳挡住的组件如何对应？','教学爆炸图。机身向侧面移开，内部件沿轴线分离；这是读结构的图，不是照此拆机的工序或实测装配尺寸。',['C02','C06'],['S01','S02'],['P'+p[0] for p in parts]),
 ('section','咖啡豆在哪一段变成咖啡粉？','剖面保留储豆仓、主轴、内外磨芯和接粉杯的相对关系。青绿箭头表示豆/粉的阅读路径；磨纹、空隙为教学放大。',['C01','C02','C03'],['S01','S03','S05'],['P04','P05','P06','P07','P08','P10','P11']),
 ('comparison','细和粗的差别发生在哪里？','两图使用同一结构和比例，只放大研磨区的相对间隙。左侧较窄、右侧较宽；不是粒径刻度、点击数或产品参数。',['C03','C05'],['S05','S06'],['P07','P08','P10']),
 ('sequence','一次使用的基本顺序是什么？','操作关系示意：加豆、转摇柄、取出咖啡粉。第一格剖开机身供观察，剖开并不是实际操作动作；具体开盖和转向依本机说明书。',['C01','C05'],['S03','S06'],['P01','P02','P06','P11']),
 ('care','清理时最容易忽略什么？','磨芯、主轴与垫圈分组放置，右侧画出清理刷。示意不代表所有部件都能水洗；材料限制见正文。',['C02','C04','C06'],['S01','S02','S04'],['P03','P04','P07','P08']),
 ('inspection','重新使用前核对什么？','教学模型局部剖开，让检查部位可见：上部装配、下部研磨组件和干燥状态。不是故障修理或维修合格证明。',['C04','C06'],['S01','S02','S04'],['P01','P02','P06','P08','P10'])]
figures=[]
for i,(kind,q,caption,cids,sids,pids) in enumerate(figspec):
    figures.append(dict(id=f'F{i+1:02}',kind=kind,question=q,caption=caption,alt_text=q+'；'+caption,svg='figures/'+names[i]+'.svg',png='figures/'+names[i]+'.png',width_mm=164,claim_ids=cids,source_ids=sids,part_ids=pids,provenance='original'))
figures[0]['width_mm']=150
figures[2]['width_mm']=150
def p(text):return dict(type='paragraph',text=text)
def f(i):return dict(type='figure',id=f'F{i:02}')
def box(label,text):return dict(type='callout',label=label,text=text)
def table(headers,rows):return dict(type='table',headers=headers,rows=rows)
pages=[
 dict(title='手摇磨豆机\n图解说明书',kicker='图解器物 / VISUAL MANUAL 01',lead='看清结构，理解研磨，再把一次使用做好。',blocks=[f(1),p('一颗咖啡豆不会因为摇柄转得漂亮就自动变成合适的咖啡粉。真正工作的地方藏在机身下部：内磨芯与外磨芯之间的狭窄通道。这本小册从一件完整器物走到内部，再回到加豆、调整和清理，让图和动作一一对应。'),table(['先解决的问题','从这里读'],[['我该看哪几个部件？','认识整机 → 零件与编号'],['豆子究竟在哪里变成粉？','剖面原理 → 粗细对照'],['怎样开始、清理、排查？','操作顺序 → 保养 → 使用前核对']]),box('这本书的边界','这是原创通用锥刀教学模型，不是HARIO或其他品牌的官方说明书。真实部件关系参考公开资料；外观、间距、颜色和移开量经过简化。不提供点击数、粒径、公差或维修认证。')]),
 dict(title='01 / 先认识手里这件器物',lead='先记住四个外部件，再去理解里面的磨芯。',blocks=[f(2),p('01摇柄是动作入口，06机身是你握持和装豆的位置，11接粉杯是结果出口。整豆从上部储豆仓进入，粉末从下方落到杯中。[S03] 沿这条路径阅读，比背一串零件名称更有用。'),p('外观相似不代表操作相同。有些产品的粗细控制在顶部，有些在底部；接粉杯也可能采用不同连接方式。这本书用底部旋钮的通用结构解释原理，不把某个型号的方向、刻度或拆装方式当成通用规则。[S06]'),table(['部件','你在一次使用中做什么'],[['01 摇柄','把手的转动传给主轴，不靠速度设定粒度。'],['02 上盖 / 06 机身','确认开盖方法，向储豆仓装豆。'],['11 接粉杯','研磨结束后取出咖啡粉，留意是否仍有残留。']]),box('读图方式','圆圈数字是稳定件号，不是操作步骤。灰色表现外壳和金属，米色表现磨芯，青绿帮助寻找握持/调整部位；色彩不是材料认证。')]),
 dict(title='02 / 拆开看：零件不是一堆名字',lead='机身移到侧面，才看得见轴线上的工作组件。',blocks=[f(3),table(['件号','名称','在这本书中的作用'],[['P'+i,n,r] for i,n,r in parts]),p('垫圈、弹簧和定位件很小，但不是可有可无的装饰。参考组装资料和拆解说明时，应该核对它们与主轴、磨芯的关系。[S01][S02] 图中省略部分轴套和外壳细节；机身横移仅为观察，不表示实际产品应从侧面抽出。')]),
 dict(title='03 / 剖面原理：豆子在哪里变成粉',lead='摇柄提供运动；内外磨芯之间的研磨区完成破碎。',blocks=[f(4),p('顺着箭头从上往下看：储豆仓把豆子送向研磨区域，主轴把摇柄的运动传到内磨芯，内外磨芯之间的通道让豆子在通过时逐步变小。最后，粉末落入下方接粉杯。[S01][S03] 图中用几颗整豆和少量粉点代表流动，不描述真实堆积和颗粒分布。'),p('理解这张图，要把两件事分开：转动让研磨持续发生；磨芯的相对位置影响粉的粗细。[S05] 因而“转得更快”与“设得更细”并不是同一个控制。前者是动作，后者是几何关系。'),box('剖面不是实物照片','为了看清因果，这里去掉半边外壳，放大磨纹和间隙，并省略不影响阅读的支撑细节。箭头表示豆/粉路径，不表示水路、电流或机械轴线。'),table(['图中观察到什么','它解释什么'],[['主轴连接内磨芯','为什么转摇柄能带动研磨'],['两磨芯之间存在通道','为什么不是单纯把豆子放进一个空盒子'],['研磨区在接粉杯上方','为什么粉末可以向下收集']])]),
 dict(title='04 / 粗与细：差别在两磨芯之间',lead='先理解间隙，再回到自己机器的具体档位。',blocks=[f(5),p('厂家对调整机制的解释是：调整使磨芯彼此靠近或远离，相对距离影响研磨粗细。[S05] 这张图把差别放大，左侧保留较窄的研磨通道，右侧更宽。它表达趋势，不是一把可以从图上量粒径的尺子。'),p('实际使用时，先确认本机的调节装置和说明。不要直接抄另一台机器的“几格”“几圈”，也不要把这张局部图当成校准标准。HARIO的通用说明也先要求判断自己是哪一种调节机构。[S06]'),table(['你准备改什么','一次只确认这一件事'],[['控制方式','找到本机旋钮或调节螺母，而不是加快摇柄。'],['前后变化','保留上一设置，做小幅调整，再观察这一批粉。'],['档位记录','记本机的位置与方向，别把别人的点击数当通用答案。']]),box('先停下来再辨认','本书不要求把磨芯强行拧到接触来找“零点”。图中没有真实公差或最小间隙；初始化和校准只依对应机型原说明书。')]),
 dict(title='05 / 一次使用，把顺序做对',lead='装豆、研磨、取粉；每一步知道自己在做什么。',blocks=[f(6),dict(type='steps',items=['确认上盖和接粉杯的安装方式，再向上部储豆仓装豆。不要把豆子倒进下部接粉杯。[S03]','按本机说明握持机身并转动摇柄。磨芯会把豆子带入研磨区；明显卡住时先停下，不用蛮力硬拧。','研磨结束后，按本机连接方式取下接粉杯，取出咖啡粉，再检查仓内是否仍有明显残留。']),p('第一格为了说明加豆位置而局部剖开，真实使用不需要拆掉机身。图里没有手部姿势，也不提供所有型号通用的旋转方向。这里解释的是一条基本工作链，具体动作要回到手中产品的说明书。[S03]'),box('让一次尝试可比较','需要调整粗细时，先保留当前设置的记录。不要同时改豆量、磨度和冲煮方式，又把差异全部归因于磨豆机。此处只讲可观察的使用顺序，不给适用于所有咖啡豆的配方。')]),
 dict(title='06 / 清理与保养：先看材料，再看顺序',lead='小件不要遗失；能不能水洗，不能凭外观猜。',blocks=[f(7),p('制造商提醒，清理磨豆机时有许多容易遗失的小件。[S04] 拆下一个就分组放好，而不是把弹簧、垫圈和磨芯一起倒进水槽。可以先拍下自己的实际结构；本书的教学爆炸图不能替代本机的装配顺序。'),p('HARIO的说明明确把木件和铁磨芯排除在通用水洗方式之外，这些部件可以按其说明用干布或刷子清理。[S04] 因此，看到别人的陶瓷磨芯能洗，不代表自己的金属磨芯也应该浸泡。是否可以洗、用什么清洁剂以及如何干燥，以对应产品说明为准。'),table(['清理前','清理后'],[['先确认材料与本机拆解说明。','检查小件是否齐全，按本机顺序装回。'],['准备小件托盘，不把它们放在排水口边。','应干燥的部件充分干燥后再使用。'],['不为照着教学图而强拆固定结构。','重新确认磨芯与旋钮的位置，不沿用未经核对的设置。']]),box('这一页不承诺什么','不提供润滑、除锈、磨芯修复或强制拆卸方案；不把所有金属统称为可水洗材料。若原手册与这里的通用提醒有差异，按本机手册处理。')]),
 dict(title='07 / 使用前核对与安全排查',lead='先检查能安全确认的地方，不把排查变成修机器。',blocks=[f(8),table(['你看到的现象','先核对','下一步'],[['摇柄明显卡住','装配、是否有豆、是否有可见异物','先停下；回读本机说明，不强行用力。'],['粗细与上次差很多','调节位置，以及清理后小件是否装回','按本机顺序核对，记录当前设置再做小幅比较。'],['清理后发现多出小件','垫圈、弹簧、定位件的归属','不要先凑合使用；对照原装配图，不按本图猜。'],['材料能否水洗不确定','本机磨芯和外壳的材料','先读护理说明；不确定时不要套用其他型号的水洗做法。']]),p('上述表格是保守的核对路径，不是故障诊断结论。原始资料直接支撑零件名称、组装顺序、装豆/出粉位置和护理限制；外观、示意间隙与图版构成经过教学简化。[S01][S02][S03][S04]'),box('读完应该留下的三个判断','你能指出豆子走过哪里；能解释为什么磨芯间隙影响粗细；能在清理前区分原手册、通用提醒与教学示意。这比记住一个不通用的档位数字更重要。')])]
pages[2]['blocks'][1]=table(['上部与支承组件','研磨与收集组件'],[
 ['P01 摇柄：将动作传给主轴','P07 外磨芯：组成研磨通道'],
 ['P02 上盖：盖住储豆仓','P08 内磨芯：随主轴转动'],
 ['P03 垫圈：轴向小件，注意保管','P09 定位销：定位小件，不要遗漏'],
 ['P04 主轴：连接摇柄与内磨芯','P10 调节旋钮：改变磨芯相对位置'],
 ['P05 弹簧：磨芯组件的轴向小件','P11 接粉杯：收集咖啡粉'],
 ['P06 储豆机身：储豆并承接组件','件号与爆炸图一致；不是操作序号']])
book=dict(title='手摇磨豆机 · 图解说明书',series='图解器物',reader='无专业背景、希望理解和正确使用手摇锥刀磨豆机的成年人',mode='real-structure',scope='真实锥刀机制的通用教学说明，不是特定品牌机型的外观复刻、维修图或制造图',delivery_kind='production',page_layout='fixed',sources_on_new_page=True,font='PingFang SC',include_sources=True,include_toc=False,sources=sources,claims=[dict(id=i,text=t,source_ids=s,status='verified',critical=True) for i,t,s in claims],parts=[dict(id='P'+i,name=n,function=r) for i,n,r in parts],figures=figures,pages=pages,figure_notice='图版均为原创SVG教学示意，由Anatomy几何库辅助生成；未复制厂商图。参考结构以HARIO公开资料为线索，一般间隙原理参考Baratza；外观与尺寸不是特定产品。正文、表格和图注可编辑，Word插图为2200px宽PNG，SVG原稿保留。')
(root/'book.json').write_text(json.dumps(book,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(ok=True,manifest=str(root/'book.json'),editorial_units=len(pages),plates=len(figures)),ensure_ascii=False))

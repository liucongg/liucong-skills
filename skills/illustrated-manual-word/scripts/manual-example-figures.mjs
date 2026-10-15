import fs from 'node:fs';
import path from 'node:path';
import * as K from '../assets/vendor/anatomy/kit/iso-kit.mjs';
import * as G from '../assets/vendor/anatomy/kit/lathe.mjs';
const out=process.argv[2];if(!out)throw Error('Usage: node manual-example-figures.mjs output-dir');fs.mkdirSync(out,{recursive:true});
const ink='#263338',paper='#f7f4ed',teal='#39766f';
const CSS=`.iso-line{fill:none;stroke:${ink};stroke-width:1.1;stroke-linecap:round;stroke-linejoin:round}.iso-line[data-tone=faint]{stroke:#a3aaa0;stroke-width:.65}.iso-line[data-tone=mid]{stroke:#718079;stroke-width:.85}.iso-fill{fill:#e8e9df}.iso-top{fill:#fbfaf3}.iso-shade[data-shade="0"]{fill:#a9b4ac}.iso-shade[data-shade="1"]{fill:#bdc6bc}.iso-shade[data-shade="2"]{fill:#d1d7cb}.iso-shade[data-shade="3"]{fill:#e0e3d7}.dark .iso-fill,.dark .iso-top{fill:#46524f}.dark .iso-shade{fill:#2d4139}.dark .iso-line{stroke:#1c302b}.teal .iso-fill{fill:#61958c}.teal .iso-top{fill:#81aba0}.teal .iso-shade[data-shade="0"]{fill:#2b5b51}.teal .iso-shade[data-shade="1"]{fill:#366e60}.teal .iso-shade[data-shade="2"]{fill:#4a8877}.teal .iso-shade[data-shade="3"]{fill:#6a9c8b}.teal .iso-line{stroke:#284f44}.ceramic .iso-fill{fill:#eadcc0}.ceramic .iso-top{fill:#f8edda}.ceramic .iso-shade{fill:#cebc9a}text{font-family:'PingFang SC','Noto Sans CJK SC',sans-serif;fill:${ink}}`;
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
const t=(x,y,s,n=25,c=ink,a='start')=>`<text x="${x}" y="${y}" font-size="${n}" style="fill:${c}" text-anchor="${a}">${esc(s)}</text>`;
const arr=d=>`<path d="${d}" fill="none" stroke="${teal}" stroke-width="3" marker-end="url(#a)"/>`;
const num=(x,y,n)=>`<circle cx="${x}" cy="${y}" r="21" fill="${paper}" stroke="${teal}" stroke-width="2"/>${t(x,y+8,n,23,teal,'middle')}`;
function save(n,w,h,b){fs.writeFileSync(path.join(out,n+'.svg'),`<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="原创通用锥刀磨豆机教学模型，非厂家机型外观或尺寸图"><style>${CSS}</style><defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="${teal}"/></marker><pattern id="h" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M-2 12L12-2" stroke="#a7a695" stroke-width="1"/></pattern></defs><rect width="${w}" height="${h}" fill="${paper}"/>${b}</svg>`);}
const F=z=>G.frameAlong([0,0,z],[0,0,1]);
function machine(w=1050,h=710,{explode=false,labels=false,open=false}={}){
 const zmax=explode?385:234;
 const P=K.fitProjection([[-50,-50,0],[50,50,0],[98,8,zmax],[0,0,zmax]],w,h,{pad:70,elevation:24,azimuth:42});
 const list=[];
 const put=(id,p,s,mat='',inner='')=>list.push({p,svg:`<g data-part="${id}">${K.solidSvg(s,{tone:'hi',crease:'faint',className:mat,inner})}</g>`});
 const cyl=(id,x,y,r,z,hh,mat='',inner='')=>put(id,[x,y,z+hh/2],K.cylinder(x,y,r,z,hh,P,64,.65),mat,inner);
 cyl('P11',0,0,34,0,explode?49:65,'',K.lineSvg(K.sideArc(0,0,34,12,P),{tone:'faint'})+K.lineSvg(K.sideArc(0,0,34,54,P),{tone:'faint'}));
 put('P07',[0,0,explode?133:89],G.ringBand(explode?123:78,explode?143:98,16,27,F(0),P,{steps:64}),'ceramic');
 put('P08',[0,0,explode?101:94],G.solidOf([[0,16],[18,8],[23,4]],F(explode?90:83),P,{steps:64}),'ceramic',K.lineSvg(G.ribsOf(F(explode?90:83),0,18,16,20,P,{r1:8,twist:.3}),{tone:'mid'}));
 let az=explode?66:71;cyl('P10',0,0,15,az,9,'teal',K.lineSvg(K.knurl(0,0,15,az,az+9,24,P),{tone:'faint'}));
 cyl('P04',0,0,3.3,explode?223:92,explode?92:118);
 const bx=explode?-63:0,by=explode?63:0,bz=explode?156:70;
 if(!open)cyl('P06',bx,by,32,bz,explode?96:110,'',K.lineSvg(K.sideArc(bx,by,32,bz+4,P),{tone:'mid'})+K.lineSvg(K.sideArc(bx,by,32,bz+(explode?91:105),P),{tone:'mid'}));
 else put('P06',[-25,-25,134],K.slabOf({x:-32,y:-32,w:13,d:64,r:4},70,110,P,6,.5));
 if(!explode&&!open)cyl('P06',0,0,33.1,124,28,'teal',K.lineSvg(K.knurl(0,0,33.2,126,150,44,P),{tone:'faint'}));
 const sz=explode?176:112,sp=[];for(let i=0;i<=170;i++){let a=i/170*Math.PI*12;sp.push(K.iso([6*Math.cos(a),6*Math.sin(a),sz+i/170*18],P));}list.push({p:[0,0,sz+9],svg:`<g data-part="P05"><path d="${K.pathOf(sp)}" fill="none" stroke="#52675d" stroke-width="2.1"/></g>`});
 put('P03',[0,0,explode?321:184],G.ringBand(explode?319:181,explode?323:185,3.5,10,F(0),P,{steps:56}));
 cyl('P02',0,0,33,explode?333:184,7,'dark');
 const hz=explode?357:208;put('P01',[40,0,hz],K.slabOf({x:-7,y:-5,w:101,d:10,r:3},hz,5,P,6,.6));cyl('P01',83,0,10,hz+5,19,'dark');
 put('P09',[0,0,explode?85:87],K.slabOf({x:-9,y:-2,w:18,d:4,r:.5},explode?83:85,4,P,4));
 list.sort((a,b)=>K.depthOf(a.p,P)-K.depthOf(b.p,P));
 let b=`<ellipse cx="${w*.49}" cy="${h-57}" rx="115" ry="14" fill="#d4d4c5" opacity=".45"/>`+list.map(x=>x.svg).join('');
 if(explode){const a=K.iso([0,0,0],P),c=K.iso([0,0,385],P);b=`<path d="M${a}L${c}" fill="none" stroke="#b1b9ac" stroke-dasharray="5 9" stroke-width="1.2"/>`+b;}
 if(labels){const ls=explode?[[[83,0,364],825,95,'01','摇柄'],[[0,0,337],800,177,'02','上盖'],[[0,0,321],820,230,'03','垫圈'],[[0,0,277],798,296,'04','主轴'],[[0,0,185],800,374,'05','弹簧'],[[bx,by,210],84,286,'06','储豆机身'],[[0,0,133],800,448,'07','外磨芯'],[[0,0,101],800,500,'08','内磨芯'],[[0,0,85],800,552,'09','定位销'],[[0,0,69],800,604,'10','调节旋钮'],[[0,0,28],85,598,'11','接粉杯']]:[[[83,0,219],760,118,'01','摇柄'],[[0,0,188],735,227,'02','上盖'],[[28,12,140],715,370,'06','储豆机身'],[[25,9,29],705,550,'11','接粉杯']];for(const [p,x,y,n,s] of ls){let [a,c]=K.iso(p,P),ex=x>w/2?x-27:x+160;b+=`<path d="M${a} ${c}L${ex} ${c}L${ex} ${y-7}" fill="none" stroke="#728279" stroke-width="1.4"/><circle cx="${a}" cy="${c}" r="3" fill="${teal}"/>`+num(x,y-7,n)+t(x+30,y,s,24);}}
 return b;
}
const bean=(x,y,r=0)=>`<g transform="translate(${x} ${y}) rotate(${r})"><ellipse rx="13" ry="8" fill="#927057" stroke="#644e3e" stroke-width="1.2"/><path d="M-10 0Q0-5 10 1" fill="none" stroke="#d9b991" stroke-width="1.4"/></g>`;
save('F01-hero',1050,710,machine()+t(70,82,'HAND MILL / 01',22,teal)+t(70,124,'从整颗豆子，到一杯的起点',27));
save('F02-overview',1050,710,machine(1050,710,{labels:true}));
save('F03-exploded',1050,750,machine(1050,750,{explode:true,labels:true}));
function section(x=425,y=40,s=1){return `<g transform="translate(${x} ${y}) scale(${s})"><g data-part="P06"><path d="M-120 42Q-128 23-108 15H108Q128 23 120 42L100 434H73L83 46H-83L-73 434H-100Z" fill="url(#h)" stroke="${ink}" stroke-width="2"/></g><path d="M-88 45L-72 260H72L88 45" fill="#eee8dc" stroke="#7d887e" stroke-width="1.5"/><g data-part="P04"><rect x="-7" y="4" width="14" height="401" rx="4" fill="#cdd4cb" stroke="${ink}" stroke-width="1.8"/></g><g data-part="P05"><path d="M-20 230C40 235-40 243 20 249C-40 256 40 262-20 269C40 276-40 283 20 289" fill="none" stroke="#596b62" stroke-width="3"/></g><g data-part="P07"><path d="M-78 291L-39 325L-62 372H-100Z M78 291L39 325L62 372H100Z" fill="#d4c4a6" stroke="${ink}" stroke-width="2"/></g><g data-part="P08"><path d="M0 289L48 369H-48Z" fill="#eee0bc" stroke="${ink}" stroke-width="2"/><path d="M-8 315L23 360M-24 338L-8 361M11 314L-14 355" stroke="#927f5e" fill="none" stroke-width="2"/></g><g data-part="P10"><rect x="-28" y="390" width="56" height="21" rx="5" fill="${teal}" stroke="${ink}" stroke-width="1.5"/></g><g data-part="P11"><path d="M-103 432L-94 540Q0 563 94 540L103 432H86L78 520Q0 537-78 520L-86 432Z" fill="#e0e3d8" stroke="${ink}" stroke-width="2"/></g>${bean(-49,118,-26)}${bean(45,158,20)}${bean(-38,185,-10)}${bean(32,228,14)}${arr('M-52 203L-58 282')}${arr('M56 258L56 307')}${arr('M-55 375L-66 469')}${arr('M55 375L66 469')}<g fill="#967254">${Array.from({length:12},(_,i)=>`<circle cx="${-55+i*10}" cy="${495+(i%3)*6}" r="2.5"/>`).join('')}</g></g>`;}
save('F04-section',1050,660,section()+t(660,145,'① 整豆进入储豆仓')+t(660,302,'② 主轴带动内磨芯')+t(660,370,'③ 两磨芯间逐步破碎')+t(660,533,'④ 粉末落入接粉杯')+t(58,80,'剖面揭示内部关系',22,teal)+t(58,614,'开口、间距与磨纹为教学放大，不是实测尺寸。',23,'#798380'));
function gap(x,d,label){return `<g transform="translate(${x} 65)"><path d="M-112 25L-40 101L-66 178H-130Z M112 25L40 101L66 178H130Z" fill="#d4c4a7" stroke="${ink}" stroke-width="2"/><path d="M0 ${39+d}L${45-d*.35} 170H${-45+d*.35}Z" fill="#eee1bc" stroke="${ink}" stroke-width="2"/>${arr(`M-62 117L${-47+d*.35} 125`)}<path d="M-10 171V224H10V171" fill="#cdd3ca" stroke="${ink}" stroke-width="1.5"/><rect x="-46" y="224" width="92" height="25" rx="8" fill="${teal}" stroke="${ink}" stroke-width="2"/>${t(0,315,label,28,ink,'middle')}${t(0,353,d<10?'较窄的研磨间隙':'较宽的研磨间隙',24,'#798380','middle')}</g>`;}
save('F05-adjust',1050,590,gap(280,4,'更细')+gap(770,25,'更粗')+`<path d="M525 45V455" stroke="#b1b9ac" stroke-dasharray="6 8"/>`+t(65,540,'改变的是两磨芯的相对间隙，不是摇柄转得多快。',27,teal));
let b='';for(let i=0;i<3;i++){b+=`<g transform="translate(${i*340+10} 28) scale(.78)">${machine(420,475,{open:i===0})}</g>`+num(i*340+65,438,String(i+1).padStart(2,'0'))+t(i*340+95,445,['打开上盖加豆','握住机身转摇柄','取下接粉杯'][i],23);if(i<2)b+=arr(`M${i*340+307} 250h26`);}save('F06-operation',1050,540,b+t(58,504,'旋转方向和拆杯方式以手中机型的原说明书为准。',22,'#798380'));
const Q=K.fitProjection([[-25,-25,0],[25,25,0],[0,0,65]],270,270,{pad:30});
b=`<rect x="92" y="100" width="866" height="345" rx="35" fill="#e5e5d7" stroke="#b5bbb0" stroke-width="2"/>`+`<g transform="translate(118 135)">${K.solidSvg(G.ringBand(0,15,16,29,F(0),Q,{steps:64}),{className:'ceramic',tone:'hi'})}${K.solidSvg(G.solidOf([[0,15],[22,4]],F(25),Q,{steps:64}),{className:'ceramic',tone:'hi'})}</g>`+`<g transform="translate(405 136)">${K.solidSvg(K.cylinder(0,0,3,0,65,Q,40),{tone:'hi'})}${K.solidSvg(G.ringBand(30,34,4,14,G.frameAlong([21,6,0],[0,0,1]),Q,{steps:44}),{tone:'hi'})}</g>`+`<g transform="translate(754 260)"><path d="M0 22Q55-1 91 25L54 71L-38 74Z" fill="#e9dec1" stroke="${ink}" stroke-width="2"/>${Array.from({length:13},(_,i)=>`<path d="M${i*4-20} 59l-8 32" stroke="#957659" stroke-width="2"/>`).join('')}</g>`+t(155,493,'磨芯 / 不混放',26)+t(463,493,'小件 / 不遗失',26)+t(755,493,'清理 / 干燥',26)+t(58,69,'拆下来，是为了清理；装回去，顺序同样重要。',26,teal);save('F07-care',1050,550,b);
save('F08-check',1050,600,`<g transform="translate(0 30)">${machine(560,500,{open:true})}</g>`+t(610,120,'重新使用前，核对三处',29)+num(645,210,'01')+t(685,219,'上盖、摇柄已就位',26)+num(645,306,'02')+t(685,315,'磨芯与旋钮已装回',26)+num(645,402,'03')+t(685,411,'部件完全干燥',26)+t(78,559,'若明显卡住，先停下排查；不要用蛮力硬拧。',25,teal));
console.log(JSON.stringify({ok:true,plates:8,out:path.resolve(out),real_product_replica:false}));

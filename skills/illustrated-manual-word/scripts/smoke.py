#!/usr/bin/env python3
"""Exercise the real toolchain. This is a technical check, NOT a user sample book."""
import argparse
import datetime
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def run(*args):
    subprocess.run([str(x) for x in args], check=True)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True)
    args = parser.parse_args()
    project = Path(args.project).resolve()
    project.mkdir(parents=True, exist_ok=True)
    day = datetime.datetime.now().astimezone().date().isoformat()
    run("node", HERE / "figure-smoke.mjs", project / "figures/kit-smoke.svg")
    run(sys.executable, HERE / "manual.py", "raster", project / "figures/kit-smoke.svg", "--out", project / "figures/kit-smoke.png")
    sources = [
      {"id":"S01","title":"Microsoft: Edit SVG images in Microsoft 365","url":"https://support.microsoft.com/en-us/office/edit-svg-images-in-microsoft-365-69f29d39-194a-4072-8c35-dbe5e7ea528c","kind":"official","verified":True,"retrieved_on":day,"excerpt":"Microsoft Word, PowerPoint, Outlook, and Excel for Microsoft 365 on Windows, Mac, Android, and Windows Mobile support inserting and editing scalable vector graphics (.SVG) files in your documents, presentations, email messages, and workbooks.","license":"reference-only"},
      {"id":"S02","title":"Anatomy: source and kit API","url":"https://github.com/wheresryan22/anatomy","kind":"official","verified":True,"retrieved_on":day,"excerpt":"It makes SVG with optional WebGL shaders and 3D, for docs, articles and landing pages.","license":"MIT"},
      {"id":"S03","title":"DK: The Way Things Work","url":"https://dk.com/products/9780241569764-the-way-things-work","kind":"official","verified":True,"retrieved_on":day,"excerpt":"David Macaulay's beautiful illustrations show the inner workings of each machine, from clocks and watches to jet engines and the Internet.","license":"reference-only"}
    ]
    book = {"delivery_kind":"technical-smoke","title":"绘图到Word：技术链路验收","subtitle":"不是正式样书，不代表科学或审美验收已经完成","reader":"工具链测试人员","mode":"concept-analogy","scope":"检验代码真实生成SVG、兼容PNG、可编辑DOCX与LibreOffice页面，不冒充主题样书", "font":"PingFang SC" if sys.platform=="darwin" else "Noto Sans CJK SC",
      "sources":sources,
      "claims":[
        {"id":"C01","text":"Word支持SVG，具体工具链仍需要自己的嵌图策略。","source_ids":["S01"],"status":"verified","critical":True},
        {"id":"C02","text":"Anatomy有SVG几何绘图库，可用于技术插画。","source_ids":["S02"],"status":"verified","critical":True},
        {"id":"C03","text":"图解读物可以用插画解释机器内部工作方式。","source_ids":["S03"],"status":"verified","critical":True}
      ],
      "parts":[{"id":"P01","name":"底座"},{"id":"P02","name":"支架"},{"id":"P03","name":"滑块"}],
      "figures":[{"id":"F01","kind":"overview","question":"几何库产生的实体与中文纸面标注是否能进入文档？","svg":"figures/kit-smoke.svg","png":"figures/kit-smoke.png","width_mm":164,"caption":"技术测试夹具：三组实体使用同一轴测投影，另加件号和中文引出标签。这不是咖啡机、传动机构或缓存的正式解释图。","alt_text":"底座承托两根立柱和上方横梁，中间有带件号的滑块；标签分别指向底座、支架和滑块。","claim_ids":["C02"],"source_ids":["S02"],"part_ids":["P01","P02","P03"],"provenance":"original"}],
      "pages":[
        {"title":"一张图怎样进入Word","kicker":"技术检查 · 01","lead":"图来自实际执行的Anatomy几何库，文字来自Word原生段落。","blocks":[
          {"type":"paragraph","text":"Anatomy可以用代码构建SVG图形。[S02] 下面的夹具只用来验证绘图库、中文标签和兼容图层能一起工作，不作为正式样书的艺术质量证明。"},
          {"type":"figure","id":"F01"},
          {"type":"paragraph","text":"本版本保留SVG原稿，再导出高分辨率PNG嵌进DOCX。正文和图注仍可选择编辑，但插图不是Word独立零件，也不宣称它在文档内部仍是原生矢量。"}
        ]},
        {"title":"文件能打开，还不等于书做好了","kicker":"技术检查 · 02","lead":"这次测试把生成、结构检查和真实页面渲染分开。","blocks":[
          {"type":"paragraph","text":"Microsoft 365的Word支持插入与编辑SVG。[S01] 这不自动证明当前Python脚本的嵌图与跨软件布局正确，因此本Skill明确采用兼容PNG，并要求实际渲染。"},
          {"type":"table","headers":["检查层","本次能证明什么","不能证明什么"],"rows":[["代码执行","SVG、PNG与DOCX真实生成","主题原理准确"],["文件结构","正文可编辑、图片关系完整","中文排版与阅读质量"],["LibreOffice渲染","真实Word文件能转换并生成页图","每页都已经被视觉审阅"]]},
          {"type":"paragraph","text":"《The Way Things Work》以插画说明机器内部工作方式。[S03] 我们借鉴的是这种解释任务，不复制其受版权保护的内页。正式样书还要证明图确实帮助读者理解，并对每个主题重新搜证据。"},
          {"type":"callout","label":"未完成项","text":"技术链路通过不能替代三本样书。样书执行者仍需研究具体主题、设计真正的图、逐页查看和修正；review.json默认未审阅，不能自动改为通过。"}
        ]}
      ],"include_sources":True,"include_toc":False}
    manifest = project / "book.json"
    manifest.write_text(json.dumps(book, ensure_ascii=False, indent=2),encoding="utf-8")
    docx = project / "out/technical-smoke.docx"
    run(sys.executable, HERE / "manual.py", "validate", manifest)
    run(sys.executable, HERE / "manual.py", "build", manifest, "--out", docx)
    run(sys.executable, HERE / "manual.py", "inspect", docx, "--out", project / "qa/package.json")
    run(sys.executable, HERE / "manual.py", "render", docx, "--out-dir", project / "qa")
    print(json.dumps({"ok":True,"purpose":"technical toolchain smoke, not a finished sample book","docx":str(docx),"visual_review_completed":False},ensure_ascii=False))

if __name__ == "__main__":
    main()

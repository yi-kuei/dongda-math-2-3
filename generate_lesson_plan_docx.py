# -*- coding: utf-8 -*-
"""
generate_lesson_plan_docx.py
將《2-3_對數及其運算的意義_四節課教學計畫與教案》
編譯為 100% 符合微軟原生 OMML 數學方程式編輯規格之 JIS B4 直式單欄 Word 教案文件 (.docx)
版面：JIS B4 直式單欄 (257mm x 364mm)
字體大小：升級為大字體清晰舒適閱讀版 (內文 11~11.5pt，標題 14~22pt)
密碼授權：首頁下載驗證密碼統一為 88888888
"""

import os
import re
import docx
from docx.shared import Mm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn
from lxml import etree
import latex2mathml.converter

# 尋找微軟 MML2OMML.XSL
XSL_PATHS = [
    r"C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL",
    r"C:\Program Files (x86)\Microsoft Office\root\Office16\MML2OMML.XSL",
    r"C:\Program Files\Microsoft Office\Office16\MML2OMML.XSL",
    r"C:\Program Files (x86)\Microsoft Office\Office16\MML2OMML.XSL",
]
XSL_FILE = next((p for p in XSL_PATHS if os.path.exists(p)), None)
TRANSFORM = etree.XSLT(etree.parse(XSL_FILE)) if XSL_FILE else None

total_omml_converted = 0

def latex_to_omml(latex_str):
    global total_omml_converted
    if not TRANSFORM:
        return None
    try:
        clean = (latex_str
                 .replace(r'\dfrac', r'\frac')
                 .replace(r'\,', ' ')
                 .replace(r'\approx', '~')
                 .replace(r'\cdot', r'\times')
                 .replace(r'\iff', r'\Leftrightarrow')
                 .replace(r'\implies', r'\Rightarrow')
                 .replace(r'\le', r'\le')
                 .replace(r'\ge', r'\ge')
                 .replace(r'\neq', r'\neq')
                 )
        mml = latex2mathml.converter.convert(clean)
        omml = TRANSFORM(etree.fromstring(mml.encode('utf-8')))
        xml = re.sub(r'<\?xml[^>]+\?>', '', etree.tostring(omml, encoding='utf-8').decode('utf-8')).strip()
        node = parse_xml(xml)
        total_omml_converted += 1
        return node
    except Exception as e:
        print(f"[警告] OMML 轉換失敗: [{latex_str}] -> {e}")
        return None

def add_math_runs(paragraph, text, default_color=None, bold=False, font_size=Pt(11)):
    """切分字串並將所有 $...$ 或 $$...$$ 轉換為微軟原生 OMML 數學方程式 (<m:oMath>)"""
    parts = re.split(r'(\$\$[\s\S]+?\$\$|\$[^\$]+?\$)', text)
    for part in parts:
        if not part:
            continue
        if (part.startswith('$$') and part.endswith('$$') and len(part) > 4) or \
           (part.startswith('$') and part.endswith('$') and len(part) > 2):
            expr = part[2:-2].strip() if part.startswith('$$') else part[1:-1].strip()
            node = latex_to_omml(expr)
            if node is not None:
                paragraph._p.append(node)
            else:
                r = paragraph.add_run(expr)
                r.font.name = "Cambria Math"
                r.font.size = font_size
                r.bold = bold
                if default_color:
                    r.font.color.rgb = RGBColor(*default_color)
        else:
            r = paragraph.add_run(part)
            r.font.name = "微軟正黑體"
            r.font.size = font_size
            r.bold = bold
            if default_color:
                r.font.color.rgb = RGBColor(*default_color)

def fill_cell_multiline(cell, full_text, default_color=None, bold=False, font_size=Pt(11), alignment=WD_ALIGN_PARAGRAPH.LEFT):
    """處理表格儲存格中包含多行換行符號之文字，並逐行渲染 OMML 數學方程式"""
    lines = full_text.split('\n')
    for idx, line in enumerate(lines):
        if idx == 0:
            p = cell.paragraphs[0]
        else:
            p = cell.add_paragraph()
        p.alignment = alignment
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.35
        add_math_runs(p, line, default_color=default_color, bold=bold, font_size=font_size)

def set_cell_margins(cell, top=140, bottom=140, left=130, right=130):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table, color_hex="CBD5E1"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:left w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:bottom w:val="single" w:sz="8" w:space="0" w:color="{color_hex}"/>'
            f'<w:right w:val="single" w:sz="6" w:space="0" w:color="{color_hex}"/>'
            f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
            f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def make_lesson_plan_doc():
    global total_omml_converted
    total_omml_converted = 0
    doc = docx.Document()
    
    # 版面設定：JIS B4 直向 (257mm x 364mm)，單欄排版
    section = doc.sections[0]
    section.page_width = Mm(257)
    section.page_height = Mm(364)
    section.top_margin = Mm(20)
    section.bottom_margin = Mm(20)
    section.left_margin = Mm(20)
    section.right_margin = Mm(20)
    
    # 確保為單欄排版
    sectPr = section._sectPr
    cols = sectPr.xpath('w:cols')
    if cols:
        cols[0].set(qn('w:num'), '1')
    else:
        new_cols = OxmlElement('w:cols')
        new_cols.set(qn('w:num'), '1')
        sectPr.append(new_cols)
    
    # 頁首
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("東大版 技術高中數學（第三冊）2-3 對數及其運算的意義 ‧ 四節課課程計畫與教學教案 (JIS B4 直式單欄 OMML 標準版)")
    hrun.font.name = "微軟正黑體"
    hrun.font.size = Pt(9.5)
    hrun.font.color.rgb = RGBColor(140, 140, 140)
    
    # 頁尾
    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    frun = fp.add_run("PLVS 數學科教學研究會 ‧ 名偵探柯南數理探案特訓 旗艦全功能標準版 ｜ 驗證授權密碼 88888888")
    frun.font.name = "微軟正黑體"
    frun.font.size = Pt(9.5)
    frun.font.color.rgb = RGBColor(140, 140, 140)

    # 1. 主標題 (22pt)
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(8)
    p_title.paragraph_format.space_after = Pt(4)
    r1 = p_title.add_run("東大版 技術高中數學（第三冊）單元 2-3\n對數及其運算的意義 課程計畫與教學教案")
    r1.font.name = "微軟正黑體"
    r1.font.size = Pt(22)
    r1.bold = True
    r1.font.color.rgb = RGBColor(120, 53, 15) # 琥珀深棕

    # 副標題 (13pt)
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(16)
    r2 = p_sub.add_run("【名偵探柯南數理探案特訓 ‧ 旗艦全功能教學標準版】（4 節課 × 50 分鐘，共 200 分鐘）\n微軟原生 OMML 數學方程式高規格編印版 ｜ JIS B4 直式單欄教學手冊")
    r2.font.name = "微軟正黑體"
    r2.font.size = Pt(13)
    r2.bold = True
    r2.font.color.rgb = RGBColor(180, 83, 9)

    # 2. 基本資料表
    info_tbl = doc.add_table(rows=4, cols=4)
    info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(info_tbl, "D97706")
    
    info_data = [
        [("設計單位", True), ("PLVS 數學科教學研究會", False), ("實施年級", True), ("技術型高級中等學校二年級", False)],
        [("教材版本", True), ("東大版 數學（第三冊）2-3 (課本 P.74~84)", False), ("教學總時數", True), ("4 節課（每節 50 分鐘，共 200 分鐘）", False)],
        [("教學資源", True), ("單檔 HTML 互動探案平台、Word 原生 OMML 雙欄學習單、65張圖解卡 PDF", False), ("授權密碼", True), ("88888888 (首頁教案與解答卷宗下載驗證)", False)],
        [("核心素養", True), ("數-U-A1 系統思考與符號運算、數-U-B1 科技資訊與動態模擬、數-U-C2 芮氏地震生活素養", False), ("評量工具", True), ("65道自檢題、60秒速算PK、JIS B4 雙欄學習單", False)],
    ]
    
    col_widths = [Mm(32), Mm(76), Mm(32), Mm(77)]
    for r_idx, row in enumerate(info_data):
        for c_idx, (text, is_hdr) in enumerate(row):
            cell = info_tbl.cell(r_idx, c_idx)
            cell.width = col_widths[c_idx]
            set_cell_margins(cell, top=90, bottom=90, left=120, right=120)
            if is_hdr:
                set_cell_shading(cell, "FEF3C7")
                fill_cell_multiline(cell, text, default_color=(120, 53, 15), bold=True, font_size=Pt(11))
            else:
                set_cell_shading(cell, "FFFFFF")
                fill_cell_multiline(cell, text, default_color=(51, 65, 85), bold=False, font_size=Pt(11))
                
    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # 3. 壹、總體課程計畫架構與時數分配總表
    h1 = doc.add_paragraph()
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    hr1 = h1.add_run("壹、總體課程計畫架構與時數分配總表")
    hr1.font.name = "微軟正黑體"
    hr1.font.size = Pt(16)
    hr1.bold = True
    hr1.font.color.rgb = RGBColor(30, 58, 138)

    plan_tbl = doc.add_table(rows=5, cols=5)
    plan_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(plan_tbl, "CBD5E1")
    
    plan_headers = ["節次", "核心主題", "課本範圍", "搭配圖解卡與工具", "核心學習目標與教學任務 (含 OMML 數學式)"]
    plan_widths = [Mm(24), Mm(40), Mm(34), Mm(42), Mm(77)]
    
    for c_idx, h_text in enumerate(plan_headers):
        cell = plan_tbl.cell(0, c_idx)
        cell.width = plan_widths[c_idx]
        set_cell_margins(cell, top=110, bottom=110, left=110, right=110)
        set_cell_shading(cell, "1E3A8A")
        fill_cell_multiline(cell, h_text, default_color=(255, 255, 255), bold=True, font_size=Pt(12), alignment=WD_ALIGN_PARAGRAPH.CENTER)
        
    plan_rows = [
        (
            "第一節\n(50 min)",
            "對數的由來、定義與\n底真數雙重防偽條件",
            "課本 P.74~76\n例題 1~2\n隨堂 1~2",
            "CASE 01~08\n🔬 動態消長儀實驗室\n📝 學習單模組一&二",
            "1. 透過納皮爾歷史引導「化乘除為加減」與求指數次方之對數本質。\n2. 熟練指數對數互化：$a^x = b \\iff x = \\log_a b$（繞一圈口訣）。\n3. 掌握底數條件 $a > 0, a \\neq 1$ 與真數條件 $b > 0$。\n4. 解聯立不等式求參數合法範圍，數線交集破案。"
        ),
        (
            "第二節\n(50 min)",
            "對數基礎求值、五大基本\n運算性質與加減實戰",
            "課本 P.76~79\n例題 3~5\n隨堂 3~5",
            "CASE 09~26\n⚡ 60秒對數速算挑戰\n📝 學習單範例3~5",
            "1. 整數、分數、小數、方根底數對數求值心法。\n2. 熟記三大性質：$\\log_a 1=0, \\log_a a=1, a^{\\log_a b}=b$。\n3. 熟練同底相加（真數乘）、同底相減（真數除）與次方飛翔法則。\n4. 掌握「正放分子、負放分母」一步統整約分神技，展開班級 60 秒速算 PK。"
        ),
        (
            "第三節\n(50 min)",
            "換底公式推導、連鎖骨牌律\n與基準對數代數表示",
            "課本 P.79~82\n例題 6~8\n隨堂 6~8",
            "CASE 27~42\n🔬 運算律密碼盤實驗室\n📝 學習單重點3&範例6~8",
            "1. 熟記換底口訣：「原底住樓下分母，真數住樓上分子」。\n2. 掌握倒數性質與連鎖骨牌消滅法（$\\log_a b \\times \\log_b c = \\log_a c$）。\n3. 指數換底穿透化簡（如 $5^{\\frac{\\log_2 7}{\\log_2 5}} = 7$）。\n4. 質因數分解拆解基準對數代數表示（$\\log_{10} 2=x, \\log_{10} 3=y$）。"
        ),
        (
            "第四節\n(50 min)",
            "是非題迷思深度診斷、\n芮氏地震素養與密室考核",
            "課本 P.83~84\n自我評量是非題、\n基礎進階與素養題",
            "CASE 43~65\n🔬 芮氏地震能量模擬器\n🏆 少年偵探團考核 STAGE 01~06",
            "1. 深度診斷 5 大是非題思維迷思（加除不能拆、負數真數陷阱、正負區間）。\n2. 攻克係數還原次方、巢狀對數由內而外化簡與多項式展開。\n3. 融入生活素養：運用 $\\log_{10} E = 11.8 + 1.5M$ 算 921 能量並理解 31.6 倍與 1000 倍之對數意義。\n4. 少年偵探團 6 階段闖關考核，完成 65 案授階名偵探！"
        )
    ]
    
    for r_idx, r_data in enumerate(plan_rows, start=1):
        bg_col = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(r_data):
            cell = plan_tbl.cell(r_idx, c_idx)
            cell.width = plan_widths[c_idx]
            set_cell_margins(cell, top=90, bottom=90, left=110, right=110)
            set_cell_shading(cell, bg_col)
            if c_idx == 0:
                fill_cell_multiline(cell, text, default_color=(120, 53, 15), bold=True, font_size=Pt(11.5), alignment=WD_ALIGN_PARAGRAPH.CENTER)
            elif c_idx in (1, 2, 3):
                fill_cell_multiline(cell, text, default_color=(30, 41, 59), bold=(c_idx==1), font_size=Pt(11))
            else:
                fill_cell_multiline(cell, text, default_color=(15, 23, 42), bold=False, font_size=Pt(11))

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 4. 貳、分節詳細教學教案 (四節課詳細表)
    h2 = doc.add_paragraph()
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(6)
    hr2 = h2.add_run("貳、分節詳細教學教案 (Detailed Lesson Plans)")
    hr2.font.name = "微軟正黑體"
    hr2.font.size = Pt(16)
    hr2.bold = True
    hr2.font.color.rgb = RGBColor(30, 58, 138)

    periods_data = [
        (
            "第一節課教案：對數的由來、定義與底真數雙重防偽條件 (50 分鐘)",
            [
                ("00~10 分\n(10 min)", "引起動機\n概念奠基",
                 "1. 投影首頁，開啟 CASE 01 探案情境：提問「$2^x = 32$，則 $x=5$；但若 $2^x = 30$，$x$ 是多少？」。\n2. 介紹 17 世紀納皮爾歷經 20 年苦心發明對數簡化繁重天文乘除之歷史。\n3. 揭示新符號：$x = \\log_2 30$。",
                 "1. 思考 $2^4 = 16 < 30 < 32 = 2^5$，體會對數符號之必要性。\n2. 理解對數就是「求指數次方」！",
                 "平台首頁\nCASE 01 圖解卡\n納皮爾歷史插圖"),
                ("10~22 分\n(12 min)", "核心概念\n定義與互化",
                 "1. 投影 CASE 02，講解定義：若 $a>0, a\\neq 1, b>0$，則 $a^x = b \\iff x = \\log_a b$。\n2. 傳授柯南破案神技口訣：「底數還是底數，指數變對數，對數變指數！」（繞一圈法則）。\n3. 啟動【🔬 動態消長儀實驗室】，展示底數與指數滑動之連動。\n4. 指導填寫學習單【模組一：重點 1】。",
                 "1. 練習繞一圈互化箭頭，朗誦記憶口訣。\n2. 於學習單【重點 1】完成指數對數互化填空。",
                 "CASE 02 圖解卡\n動態消長儀實驗室\nWord 學習單（模組一）"),
                ("22~35 分\n(13 min)", "範例精講\n定義辨析排雷",
                 "1. 投影 CASE 05 & 06（例題 1 與隨堂 1）：\n   - 檢視 $\\log_1 5$：底為 1 違規！無意義。\n   - 檢視 $\\log_{-2} 3$：底為負違規！無意義。\n   - 檢視 $\\log_3 (-4)$ 與 $\\log_2 0$：真數小於等於 0 違規！無意義。\n   - 檢視 $\\log_2 \\frac{1}{5}$：完全合法！\n2. 展示「👓 名偵探推理筆記」雙重防偽安全鎖。",
                 "1. 學習「快速掃描法」：一眼看底數、一眼看真數。\n2. 完成學習單【模組二：CASE 05 & 06】實戰練習。",
                 "CASE 05、06 圖解卡\n白板紅筆標記違規處\nWord 學習單（模組二）"),
                ("35~46 分\n(11 min)", "進階演練\n存在條件求範圍",
                 "1. 投影 CASE 07（例題 2：求 $\\log_{x-1}(x+5)$ 有意義之範圍）：\n   - 列聯立不等式：$\\begin{cases} x-1 > 0 \\\\ x-1 \\neq 1 \\\\ x+5 > 0 \\end{cases} \\implies \\begin{cases} x > 1 \\\\ x \\neq 2 \\\\ x > -5 \\end{cases}$。\n   - 數線求交集得 $x > 1$ 且 $x \\neq 2$。\n2. 學生自主演練 CASE 08（隨堂 2：$-2 < x < 3$ 且 $x \\neq -1$）。",
                 "1. 牢記解題 SOP：底數 2 條件、真數 1 條件，缺一不可！\n2. 於學習單【CASE 07 & 08】畫數線求嚴謹區間解。",
                 "CASE 07、08 圖解卡\n白板數線繪圖\nWord 學習單（範例 2）"),
                ("46~50 分\n(4 min)", "課堂總結\n自我檢核",
                 "1. 隨機點擊 CASE 07 正面自我檢核抽屜，抽點學生作答。\n2. 預告下節課進行「60 秒對數速算破案挑戰」，指派作業。",
                 "1. 點擊卡片正面自我檢核按鈕，即時檢驗理解度。\n2. 記錄今日作業：完成學習單前 2 題。",
                 "互動檢核抽屜\n學習單作業指派")
            ]
        ),
        (
            "第二節課教案：對數基礎求值、五大基本運算性質與加減實戰 (50 分鐘)",
            [
                ("00~12 分\n(12 min)", "各類求值精講\n指數對照心法",
                 "1. 投影 CASE 09～12（例題 3 各小題）：\n   - 整數型：$\\log_2 64 = \\log_2(2^6) = 6$。\n   - 分數型：$\\log_3 \\frac{1}{81} = \\log_3(3^{-4}) = -4$。\n   - 小數型：$\\log_{0.1} 0.001 = \\log_{10^{-1}}(10^{-3}) = 3$。\n   - 方根型：$\\log_{25} 5 = \\log_{5^2}(5^1) = \\frac{1}{2}$。\n2. 總結求值心法：化為同底次方，次方直接相比！\n3. 學生演練隨堂 3（CASE 13～16）。",
                 "1. 熟練質因數分解與負數、分數次方概念。\n2. 於學習單【模組二：CASE 09~16】完成求值計算。",
                 "CASE 09~16 圖解卡\nWord 學習單（範例 3）"),
                ("12~24 分\n(12 min)", "五大運算律\n乘除變加減解密",
                 "1. 投影 CASE 03，演示三大核心口訣：\n   - 三大送分題：$\\log_a 1=0, \\log_a a=1, a^{\\log_a b}=b$。\n   - 乘法變加法：$\\log_a(MN) = \\log_a M + \\log_a N$（同底相加大結合！）。\n   - 除法變減法：$\\log_a\\frac{M}{N} = \\log_a M - \\log_a N$（同底相減大分離！）。\n   - 次方飛翔法：$\\log_{a^k}(b^m) = \\frac{m}{k}\\log_a b$（真數次方飛分子，底數次方飛分母！）。\n2. 投影 CASE 17～20 精講例題 4 與隨堂 4。",
                 "1. 朗誦記憶口訣，掌握次方往前飛規則。\n2. 完成學習單【重點 2】公式填空與範例 4 演練。",
                 "CASE 03、17~20 圖解卡\nWord 學習單（重點 2）"),
                ("24~35 分\n(11 min)", "連續加減化簡\n質因數重組破案",
                 "1. 投影 CASE 21～23（例題 5 系列）：\n   - 加法：$\\log_6 9 + \\log_6 4 = \\log_6 36 = 2$。\n   - 減法：$\\log_5 45 - \\log_5 9 = \\log_5 5 = 1$。\n   - 連續加減：$\\log_3 36 - \\log_3 8 + \\log_3 54 = \\log_3\\frac{36 \\times 54}{8} = \\log_3 243 = 5$！\n2. 傳授破案絕招：「正的在分子，負的在分母，一次統整約分破案！」\n3. 學生練習隨堂 5（CASE 24～26）。",
                 "1. 學習「正放分子、負放分母」的一步統整技巧。\n2. 完成學習單【模組二：CASE 21~26】題目。",
                 "CASE 21~26 圖解卡\n白板多色約分展示\nWord 學習單（範例 5）"),
                ("35~47 分\n(12 min)", "課堂高潮\n60秒對數速算挑戰",
                 "1. 投影平台頂部【阿笠博士實驗室 ‧ 60秒對數速算挑戰】。\n2. 教師先示範一局：螢幕出現 $\\log_2 16 = ?$，快速點選 4，展示 Combo 與音效。\n3. 全班分組 PK 賽：上台挑戰與手機/平板掃碼連線同步進行。\n4. 結算最高分，展示「少年名偵探徽章」。",
                 "1. 全神貫注投入 60 秒限時作答。\n2. 在九宮格常見答案按鈕中迅速反應，消除運算生疏感。\n3. 班級氣氛熱烈，強化反射速度！",
                 "60秒速算挑戰模組\n手機掃碼連線伺服器\n即時排行榜結算"),
                ("47~50 分\n(3 min)", "總結與交代作業",
                 "1. 總結口訣：「同底加乘減除，正放分子負放分母」。\n2. 指派作業：課本 P.78 隨堂 4、5 與學習單範例 3～5。",
                 "1. 齊聲複誦口訣，整理筆記。\n2. 課後自主練習速算挑戰。",
                 "學習單指派")
            ]
        ),
        (
            "第三節課教案：換底公式推導、連鎖骨牌律與基準對數代數表示 (50 分鐘)",
            [
                ("00~15 分\n(15 min)", "換底公式推導\n三大超強推論",
                 "1. 投影 CASE 04，講解換底原理：引入新底數 $c$：$$\\log_a b = \\frac{\\log_c b}{\\log_c a}$$\n2. 傳授口訣：「大家一起分，原底住樓下（分母），真數住樓上（分子）！」\n3. 延伸兩大黃金推論：\n   - 倒數關係：$\\log_a b = \\frac{1}{\\log_b a}$（底真互換，對數翻轉！）。\n   - 連鎖骨牌律：$\\log_a b \\cdot \\log_b c = \\log_a c$（對角相同骨牌倒，首尾相連一線通！）。\n4. 指導填寫學習單【重點 3】。",
                 "1. 理解換底公式的幾何與代數推導。\n2. 於學習單【重點 3】寫下換底公式與兩大推論口訣。",
                 "CASE 04 圖解卡\nWord 學習單（重點 3）"),
                ("15~26 分\n(11 min)", "換底與指數型\n穿透化簡精講",
                 "1. 投影 CASE 27～29（例題 6 系列）：\n   - 換底反用：$\\frac{\\log_5 32}{\\log_5 2} = \\log_2 32 = 5$。\n   - 指數換底：$5^{\\frac{\\log_2 7}{\\log_2 5}} = 5^{\\log_5 7} = 7$（穿透破案！）。\n   - 次方互換：$9^{\\log_3 5} = (3^{\\log_3 5})^2 = 5^2 = 25$。\n2. 學生演練隨堂 6（CASE 30～32）。",
                 "1. 掌握「底數與對數底同，真數直接跳出來」的穿透神技。\n2. 完成學習單【模組二：CASE 27~32】題目。",
                 "CASE 27~32 圖解卡\nWord 學習單（範例 6）"),
                ("26~37 分\n(11 min)", "連鎖骨牌律\n多重相乘破案",
                 "1. 投影 CASE 33 & 34（例題 7 系列）：\n   - 倒數相消：$\\log_2 5 \\times \\log_5 2 = 1$。\n   - 多重連鎖：$\\log_2 3 \\times \\log_3 5 \\times \\log_5 8 = \\log_2 8 = 3$！\n   - 在大螢幕用領結紅筆將斜對角 3 與 3、5 與 5 劃線消滅，直觀展示骨牌效應！\n2. 學生演練隨堂 7（CASE 35 & 36）。",
                 "1. 體驗斜對角相消的快感，觀察首項底數與末項真數之連動。\n2. 完成學習單【模組二：CASE 33~36】題目。",
                 "CASE 33~36 圖解卡\n白板紅筆骨牌連線\nWord 學習單（範例 7）"),
                ("37~47 分\n(10 min)", "基準對數拆解\n代數表示進階題",
                 "1. 投影 CASE 37～39（例題 8 系列：設 $\\log_{10} 2=x, \\log_{10} 3=y$）：\n   - 拆解真數 12：$\\log_{10}(2^2 \\times 3) = 2x + y$。\n   - 拆解真數 $\\frac{8}{9}$：$\\log_{10}\\frac{2^3}{3^2} = 3x - 2y$。\n   - 異底換底：$\\log_3 40 = \\frac{\\log_{10} 40}{\\log_{10} 3} = \\frac{3x + 1}{y}$！\n2. 強調神技暗號：$\\log_{10} 10 = 1$，常數項往往藏在因數 10 中！\n3. 學生練習隨堂 8（CASE 40～42）。",
                 "1. 學習「質因數分解 ➔ 拆為加減 ➔ 代換代數符號」三步解題流程。\n2. 於學習單【模組二：CASE 37~42】完成代數代換計算。",
                 "CASE 37~42 圖解卡\nWord 學習單（範例 8）"),
                ("47~50 分\n(3 min)", "總結與提煉",
                 "1. 提煉破案口訣：「異底相乘用連鎖，異底除法想換底，代數表示找質因數！」。\n2. 交代作業：學習單範例 6～8。",
                 "1. 複誦口訣，整理筆記。\n2. 預告下節課進行全單元是非題大診斷與地震素養應用。",
                 "學習單指派")
            ]
        ),
        (
            "第四節課教案：是非題迷思深度診斷、芮氏地震素養與密室考核 (50 分鐘)",
            [
                ("00~15 分\n(15 min)", "是非題大排雷\n五大思維迷思診斷",
                 "1. 投影 CASE 43～47（課後觀念是非題五大案）：\n   - 案 1 (○)：$a>0, a\\neq 1 \\implies \\log_a 1 = 0$ 恆成立（真數為 1 必為 0！）。\n   - 案 2 (✕)：$\\log_a(M+N) = \\log_a M + \\log_a N$（致命錯誤！反例：$\\log_{10}(1+9)=1 \\neq \\log_{10} 1 + \\log_{10} 9$）。\n   - 案 3 (✕)：$\\frac{\\log_a M}{\\log_a N} = \\log_a(M-N)$（致命錯誤！除法不能拆為相減！）。\n   - 案 4 (✕)：$\\log_3(-3)^2 = 2\\log_3(-3)$（負數真數陷阱！左式真數為 9 合法，右式真數為 $-3$ 違規！）。\n   - 案 5 (✕)：$b>0 \\implies \\log_{10} b > 0$（正負區間迷思！若 $0<b<1$ 則對數為負！）。\n2. 引導填寫學習單【模組三：是非題專題】。",
                 "1. 學生於座位上以手勢比出「○」或「✕」。\n2. 抽點學生起立說出「錯誤原因與具體反例」，徹底掃除觀念死角。",
                 "CASE 43~47 是非圖解卡\n正誤診斷印章\nWord 學習單（模組三）"),
                ("15~27 分\n(12 min)", "進階題型精講\n係數還原與巢狀",
                 "1. 投影 CASE 53（習題 3(3)：係數還原次方）：\n   - $2\\log_5 10 - 4\\log_5 2 + \\log_5 20 = \\log_5\\frac{100 \\times 20}{16} = \\log_5 125 = 3$！\n2. 投影 CASE 56（習題 4(3)：巢狀對數）：\n   - 求 $\\log_9(\\log_2 8)$：由內向外，$\\log_2 8 = 3 \\implies \\log_9 3 = \\frac{1}{2}$。\n3. 投影 CASE 63（習題 9：多項式雙括號乘法展開）。",
                 "1. 掌握「運算前係數必須全部丟回次方」的黃金原則。\n2. 演練由內而外剝洋蔥般的巢狀解法。\n3. 完成學習單【模組三：進階習題】。",
                 "CASE 53、56、63 圖解卡\nWord 學習單（模組三）"),
                ("27~38 分\n(11 min)", "生活素養應用\n芮氏地震能量模擬",
                 "1. 投影 CASE 64 & 65（習題 10(1)(2) 地震能量探案）：\n   - 公式：$\\log_{10} E = 11.8 + 1.5M$。\n   - 題 (1)：若 $E = 10^{19.3} \\implies 19.3 = 11.8 + 1.5M \\implies M = 5.0$。\n   - 題 (2)：921 大地震規模 $7.3 \\implies \\log_{10} E = 11.8 + 1.5(7.3) = 22.75 \\implies E = 10^{22.75}$ 爾格！\n2. 啟動【🔬 芮氏地震能量波形模擬器】，拖曳拉桿比較：\n   - 規模每增加 1 階，能量暴增 $10^{1.5} \\approx 31.6$ 倍；增加 2 階，能量暴增 $10^3 = 1000$ 倍！",
                 "1. 深刻體會對數在自然災害評估中的宏觀壓縮能力。\n2. 於學習單【模組三：生活素養專區】精確完成計算。",
                 "CASE 64、65 圖解卡\n地震能量模擬器\nWord 學習單（素養題）"),
                ("38~47 分\n(9 min)", "全單元總結\n少年偵探團考核",
                 "1. 投影 CASE 65 結案總覽：回顧四大支柱。\n2. 開啟【🎯 少年偵探團 6 階段特訓考核】，引導學生進行密室逃脫終極闖關：\n   - 涵蓋 STAGE 01~06，配置 3 顆手錶麻醉針指針生命值（❤️）。\n3. 全班結算成績，頒發「技術高中特等數理名偵探」榮譽勳章。",
                 "1. 於手機或大螢幕完成闖關總測驗，檢視個人總積分與授階評級。\n2. 享受 65 案全數破解的沉浸式破案成就感！",
                 "少年偵探團闖關模組\n榮譽結業證書頒發"),
                ("47~50 分\n(3 min)", "收卷與反思筆記",
                 "1. 收回完成之 JIS B4 雙欄學習單。\n2. 提醒學生：首頁提供教案與解答卷宗下載，驗證密碼為 88888888。可離線儲存隨時複習。",
                 "1. 填寫學習單最後一欄【偵探搜查實作反思與心得筆記】。\n2. 繳交學習單。",
                 "學習單收件與評量")
            ]
        )
    ]

    for sec_title, p_rows in periods_data:
        sh = doc.add_paragraph()
        sh.paragraph_format.space_before = Pt(12)
        sh.paragraph_format.space_after = Pt(4)
        shr = sh.add_run(f"📋 {sec_title}")
        shr.font.name = "微軟正黑體"
        shr.font.size = Pt(13)
        shr.bold = True
        shr.font.color.rgb = RGBColor(180, 83, 9)

        cur_tbl = doc.add_table(rows=len(p_rows)+1, cols=5)
        cur_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_table_borders(cur_tbl, "CBD5E1")
        
        headers = ["時間", "教學環節", "教師教學活動 (Teacher's Activities)", "學生學習活動 (Students' Activities)", "教學資源與數位工具"]
        t_widths = [Mm(22), Mm(26), Mm(80), Mm(54), Mm(35)]
        
        for c_idx, h_text in enumerate(headers):
            c = cur_tbl.cell(0, c_idx)
            c.width = t_widths[c_idx]
            set_cell_margins(c, top=90, bottom=90, left=90, right=90)
            set_cell_shading(c, "0F766E") # 藍綠
            fill_cell_multiline(c, h_text, default_color=(255, 255, 255), bold=True, font_size=Pt(11), alignment=WD_ALIGN_PARAGRAPH.CENTER)
            
        for r_idx, (t_time, t_step, t_act, s_act, t_res) in enumerate(p_rows, start=1):
            bg = "F0FDFA" if r_idx % 2 == 1 else "FFFFFF"
            row_items = [t_time, t_step, t_act, s_act, t_res]
            for c_idx, text in enumerate(row_items):
                c = cur_tbl.cell(r_idx, c_idx)
                c.width = t_widths[c_idx]
                set_cell_margins(c, top=80, bottom=80, left=90, right=90)
                set_cell_shading(c, bg)
                if c_idx == 0:
                    fill_cell_multiline(c, text, default_color=(120, 53, 15), bold=True, font_size=Pt(10.5), alignment=WD_ALIGN_PARAGRAPH.CENTER)
                elif c_idx == 1:
                    fill_cell_multiline(c, text, default_color=(15, 118, 110), bold=True, font_size=Pt(10.5), alignment=WD_ALIGN_PARAGRAPH.CENTER)
                else:
                    fill_cell_multiline(c, text, default_color=(15, 23, 42), bold=False, font_size=Pt(10.5))
                    
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # 5. 參、多元評量策略與成績評定規準
    h3 = doc.add_paragraph()
    h3.paragraph_format.space_before = Pt(14)
    h3.paragraph_format.space_after = Pt(6)
    hr3 = h3.add_run("參、多元評量策略與成績評定規準 (Rubrics)")
    hr3.font.name = "微軟正黑體"
    hr3.font.size = Pt(16)
    hr3.bold = True
    hr3.font.color.rgb = RGBColor(30, 58, 138)

    p_rub = doc.add_paragraph()
    p_rub.paragraph_format.space_after = Pt(6)
    p_rub.paragraph_format.line_spacing = 1.35
    add_math_runs(p_rub, "本單元落實「歷程評量」與「表現任務評量」，結合紙本與數位工具：\n1. 課堂互動與數位速算表現（30%）：【60秒對數速算挑戰】達成 10 題以上且正確率 80% 以上者得滿分；阿笠博士實驗室主動發表度。\n2. JIS B4 雙欄學習單書寫（40%）：模組一觀念填空（10%）、模組二成對例題與隨堂演算（15%）、模組三是非題與地震素養（10%）、模組四反思筆記（5%）。\n3. 少年偵探團 STAGE 闖關總評量（30%）：全套 65 題正面自檢題與 6 大關卡之總答對率。", font_size=Pt(11))

    rub_tbl = doc.add_table(rows=6, cols=5)
    rub_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(rub_tbl, "CBD5E1")
    
    rub_headers = ["評分維度", "A 優異 (90-100)", "B 良好 (80-89)", "C 基礎 (70-79)", "D 待加強 (<70)"]
    rub_widths = [Mm(30), Mm(47), Mm(47), Mm(47), Mm(46)]
    
    for c_idx, h_text in enumerate(rub_headers):
        c = rub_tbl.cell(0, c_idx)
        c.width = rub_widths[c_idx]
        set_cell_margins(c, top=90, bottom=90, left=90, right=90)
        set_cell_shading(c, "4338CA") # 靛藍
        fill_cell_multiline(c, h_text, default_color=(255, 255, 255), bold=True, font_size=Pt(11.5), alignment=WD_ALIGN_PARAGRAPH.CENTER)
        
    rub_rows = [
        (
            "定義掌握",
            "指數對數雙向互化流暢，底數真數 3 道防線列式嚴謹，能精確解聯立不等式。",
            "能正確互化指數與對數，解不等式偶有邊界漏掉等號但能更正。",
            "能認出對數符號，但常常忘記檢查底數不為 1 或真數大於 0。",
            "無法正確互化指數與對數，概念混亂。"
        ),
        (
            "運算律熟練度",
            "加乘減除轉化自如，次方飛翔法則與正分子負分母運算精確無誤。",
            "能掌握基本運算性質，多項連續加減通分過程偶有小計算失誤。",
            "需仰賴公式表方能計算，常誤將加法拆為相加。",
            "對數運算公式嚴重混淆，無法進行代數化簡。"
        ),
        (
            "換底與代數拆解",
            "能熟練默寫換底公式與連鎖律，質因數分解拆解基準對數流暢神速。",
            "能使用基本換底公式，基準代數代換經提示後能順利完成。",
            "僅能做同底計算，遇到異底或代數符號轉換感到無從下手。",
            "完全無法掌握換底技巧。"
        ),
        (
            "是非題診斷力",
            "5 題是非題全對，且能以嚴謹數學反例具體說明錯誤原因。",
            "是非題答對 4 題，能說出主要錯誤概念。",
            "是非題答對 3 題，僅知對錯但說不出具體原因。",
            "缺乏概念辨析能力，猜題成分居多。"
        ),
        (
            "素養應用力",
            "熟練運用地震公式進行指數對數運算，清楚解釋 31.6 倍與 1000 倍之對數意義。",
            "能代入地震公式算出答案，科學記號運算偶有小筆誤。",
            "能代入公式，但計算指數次方時出現障礙。",
            "無法理解公式意義與題意。"
        )
    ]
    
    for r_idx, r_data in enumerate(rub_rows, start=1):
        bg = "EEF2FF" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, text in enumerate(r_data):
            c = rub_tbl.cell(r_idx, c_idx)
            c.width = rub_widths[c_idx]
            set_cell_margins(c, top=80, bottom=80, left=90, right=90)
            set_cell_shading(c, bg)
            if c_idx == 0:
                fill_cell_multiline(c, text, default_color=(67, 56, 202), bold=True, font_size=Pt(11), alignment=WD_ALIGN_PARAGRAPH.CENTER)
            else:
                fill_cell_multiline(c, text, default_color=(15, 23, 42), bold=False, font_size=Pt(10.5))

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # 6. 肆、差異化教學與班級經營指引
    h4 = doc.add_paragraph()
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(6)
    hr4 = h4.add_run("肆、差異化教學與班級經營指引")
    hr4.font.name = "微軟正黑體"
    hr4.font.size = Pt(16)
    hr4.bold = True
    hr4.font.color.rgb = RGBColor(30, 58, 138)

    diff_text = (
        "1. 教師課前準備：影印 JIS B4 雙欄學習單（每人一張，雙面印刷）；準備教師解答版（紅字 OMML 詳解，密碼 88888888）；筆電連線教室大螢幕開啟 index.html。\n"
        "2. 差異化教學策略：\n"
        "   - 拔尖（學習優異組）：引導攻克 CASE 58（$\\log_{12} 5$ 換底代數表示）、CASE 62（$100^x + 10^{-x}$ 對數求值）與 CASE 63（多項式乘法展開）；邀請擔任名偵探小隊長。\n"
        "   - 扶弱（學習緩步組）：專注掌握 CASE 01~04（定義與運算律）與 CASE 09~16（基礎求值）；透過「動態消長儀」與「60秒速算挑戰」降低數學焦慮；是非題重點輔導「加法不能拆」與「負數無對數」。\n"
        "3. 班級經營與情境融入：稱呼學生為「特派搜查員」，答對例題全班齊聲喊：「CASE CLOSED！真相永遠只有一個！」；劇院模式電子白板用領結紅筆標記分子、西裝藍筆標記分母、眼鏡金筆標記約分相消。"
    )
    p_diff = doc.add_paragraph()
    p_diff.paragraph_format.line_spacing = 1.35
    add_math_runs(p_diff, diff_text, font_size=Pt(11))

    # 儲存檔案
    out_docx = "2-3_對數及其運算的意義_四節課教學計畫與教案.docx"
    doc.save(out_docx)
    print(f"[OK] 教案 Word 檔建置成功: {out_docx}")
    print(f"[OMML] 本次微軟原生 OMML 數學方程式轉換總數: {total_omml_converted} 處")

if __name__ == "__main__":
    make_lesson_plan_doc()

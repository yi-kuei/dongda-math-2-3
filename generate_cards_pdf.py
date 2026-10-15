# -*- coding: utf-8 -*-
"""
generate_cards_pdf.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
A4 橫向滿版圖解學習卡產生器 (HTML + Edge Headless 高解析向量 PDF)
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦完備版標準：
- A4 橫向 (297mm x 210mm) 一頁一張雙欄卡片，共 65 案
- 左側正面案情卷宗題幹與柯南破案導引，右側背面線索推理鏈與向量幾何圖解
- 全欄位 100% KaTeX 標準數學式渲染，公式上下行距優化 line-height: 2.35
- 產出 2-3_對數及其運算的意義_全套65張圖解學習卡.pdf，並同步歸檔至 download/
"""

import os
import subprocess
import time
import shutil
import cards_part1
import cards_part2

EDGE_PATHS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]
EDGE_EXE = next((p for p in EDGE_PATHS if os.path.exists(p)), None)

def generate_printable_html(cards):
    html = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <title>2-3 對數及其運算的意義 ‧ 全套 {len(cards)} 張圖解學習卡</title>
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @page {{
      size: 297mm 210mm landscape;
      margin: 0;
    }}
    body {{
      margin: 0;
      padding: 0;
      background-color: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    .page-container {{
      width: 297mm;
      height: 210mm;
      padding: 10mm 14mm 8mm 14mm;
      box-sizing: border-box;
      page-break-after: always;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #ffffff;
      position: relative;
    }}
    .katex, .katex-html, .katex-display {{
      white-space: nowrap !important;
    }}
    .katex-display {{
      margin: 0.2em 0 !important;
      display: inline-block !important;
    }}
    .katex svg {{
      display: block !important;
      position: absolute !important;
      width: 100% !important;
      height: inherit !important;
      fill: currentColor !important;
      stroke: currentColor !important;
      max-height: none !important;
      margin: 0 !important;
    }}
    .card-front-content, .leading-relaxed {{
      line-height: 2.35 !important;
    }}
    .card-front-content br, .leading-relaxed br {{
      display: block !important;
      content: "" !important;
      margin-top: 0.7rem !important;
    }}
  </style>
</head>
<body>
"""

    for idx, card in enumerate(cards):
        steps_html = "".join([f"""
          <div class="mb-2 p-2.5 rounded-lg bg-amber-50/60 border border-amber-200/80 text-xs">
            <span class="font-bold text-amber-800 mr-1">{s['title']}</span>
            <span class="text-slate-800">{s['content']}</span>
          </div>
        """ for s in card['steps']])

        html += f"""
  <div class="page-container">
    <!-- 頂部頁首 -->
    <div class="flex items-center justify-between pb-2 border-b border-amber-200">
      <div class="flex items-center gap-2">
        <span class="px-2.5 py-0.5 rounded text-xs font-black bg-blue-900 text-white font-mono">CASE #{card['id']:02d}</span>
        <span class="px-2.5 py-0.5 rounded text-xs font-black bg-amber-600 text-white">{card['tag']}</span>
        <span class="text-sm font-bold text-slate-800">東大版 技術高中數學（第三冊）2-3 對數及其運算的意義</span>
        <span class="px-2 py-0.5 rounded text-xs font-semibold bg-amber-100 text-amber-800">{card['category']} ‧ {card['page']}</span>
      </div>
      <div class="text-xs font-bold text-amber-700">
        名偵探柯南數理探案特訓 ‧ 數位教學學習包
      </div>
    </div>

    <!-- 主體內容：左右雙欄自適應卡片 -->
    <div class="grid grid-cols-2 gap-4 flex-1 my-3 items-stretch">
      <!-- 左欄：正面案情題幹與審題導引 -->
      <div class="flex flex-col justify-between p-4 rounded-xl bg-[#fbf9f4] border-2 border-amber-300/80 shadow-xs">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-red-100 text-red-700">
              案情卷宗題幹
            </span>
            <span class="text-xs text-slate-400 font-mono">CASE #{card['id']:02d} / {len(cards)}</span>
          </div>
          <h2 class="text-lg font-bold text-slate-900 mb-3">{card['title']}</h2>
          <div class="card-front-content text-sm text-slate-800 leading-relaxed font-normal">
            {card['front_content']}
          </div>
        </div>
        
        <div class="mt-4 pt-3 border-t border-amber-200/80">
          <div class="text-xs text-amber-800 bg-amber-100/70 p-2.5 rounded-lg border border-amber-200 font-medium">
            {card['front_tip']}
          </div>
        </div>
      </div>

      <!-- 右欄：背面線索推理鏈與 SVG 幾何圖解 -->
      <div class="flex flex-col justify-between p-4 rounded-xl bg-white border-2 border-slate-200 shadow-xs">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-700">
              👓 名偵探推理筆記 ‧ 線索推理鏈
            </span>
          </div>

          <!-- 線索鏈條 -->
          <div class="space-y-1 mb-2">
            {steps_html}
          </div>

          <!-- 結論框 -->
          <div class="p-2.5 rounded-lg bg-emerald-50 border border-emerald-300 text-xs text-emerald-900 font-bold mb-2">
            {card['conclusion']}
          </div>
        </div>

        <!-- SVG 幾何圖形區 -->
        <div class="w-full h-36 flex items-center justify-center bg-slate-50 rounded-lg border border-slate-200 p-1 overflow-hidden">
          {card['svg']}
        </div>
      </div>
    </div>

    <!-- 頁尾署名與版權資訊 -->
    <div class="flex items-center justify-between pt-2 border-t border-slate-200 text-[11px] text-slate-400">
      <div>PLVS 數學科 ‧ 教育學習用 ｜ 名偵探柯南數理探案特訓 旗艦完備版</div>
      <div class="font-mono">第 {idx + 1} 頁 / 共 {len(cards)} 頁</div>
    </div>
  </div>
"""

    html += """
  <script>
    document.addEventListener("DOMContentLoaded", function() {
      renderMathInElement(document.body, {
        delimiters: [
          {left: "$$", right: "$$", display: true},
          {left: "$", right: "$", display: false}
        ],
        throwOnError: false
      });
      // 標記就緒狀態
      window.isReadyForPdf = true;
    });
  </script>
</body>
</html>
"""
    return html

def main():
    print("[START] 正在載入圖解學習卡資料庫...")
    all_cards = cards_part1.CARDS_PART1 + cards_part2.CARDS_PART2
    print(f"[OK] 成功載入 {len(all_cards)} 張圖解卡片資料！")

    html_file = "cards_printable.html"
    pdf_file = "2-3_對數及其運算的意義_全套65張圖解學習卡.pdf"

    print("[START] 正在生成高解析滿版列印 HTML...")
    html_content = generate_printable_html(all_cards)
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[OK] 成功產生 {html_file}")

    if not EDGE_EXE:
        print("[WARN] 找不到 Microsoft Edge，請以瀏覽器手動開啟 cards_printable.html 並列印成 PDF！")
        return

    print(f"[START] 呼叫 Edge Headless 引擎編譯高解析向量 PDF: {pdf_file}...")
    abs_html = os.path.abspath(html_file)
    abs_pdf = os.path.abspath(pdf_file)

    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--run-all-compositor-stages-before-draw",
        f"--print-to-pdf={abs_pdf}",
        abs_html
    ]

    try:
        proc = subprocess.Popen(cmd)
        proc.wait(timeout=60)
        time.sleep(2)
        if os.path.exists(abs_pdf):
            size_mb = os.path.getsize(abs_pdf) / (1024 * 1024)
            print(f"[OK] 恭喜！高解析圖解學習卡 PDF 編譯完成: {pdf_file} (檔案大小: {size_mb:.2f} MB)")
            # 複製到 download 目錄
            os.makedirs("download", exist_ok=True)
            dl_pdf = os.path.join("download", pdf_file)
            shutil.copy(abs_pdf, dl_pdf)
            print(f"[OK] 已同步複製至: {dl_pdf}")
        else:
            print("[WARN] PDF 檔案未產出，請手動列印。")
    except Exception as e:
        print(f"[ERROR] Edge Headless 編譯過程發生例外: {e}")

if __name__ == "__main__":
    main()

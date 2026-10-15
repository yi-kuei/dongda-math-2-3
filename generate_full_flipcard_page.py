# -*- coding: utf-8 -*-
"""
generate_full_flipcard_page.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
數位翻牌圖解互動平台主頁 index.html 生成器
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦完備版標準：
- 卡片網格強制雙欄 (grid-cols-1 md:grid-cols-2)
- 全欄位 100% KaTeX 標準數學式，正面無水平捲軸適度折行
- 頁尾第一列三色膠囊訪客計數器 (人氣/到訪/互動由 0 起算)
- 雙向同步逐步導引 showStep，課堂聚焦與半透明模糊遮蔽
- 劇院全螢幕滿版 (max-w-[94vw]) 內嵌多功能電子白板
- 內嵌 Base64 學生學習單、教師解答版 (密碼 88888888) 與 16:9 PPTX 簡報
"""

import json
import cards_part1
import cards_part2
import interactive_cards_data
import interactive_js_module
import docx_b64

def generate_index_html():
    cards = cards_part1.CARDS_PART1 + cards_part2.CARDS_PART2
    cards_json = json.dumps(cards, ensure_ascii=False)
    quiz_json = json.dumps(interactive_cards_data.QUIZ_DATA, ensure_ascii=False)
    stages_json = json.dumps(interactive_cards_data.CHALLENGE_STAGES, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="zh-TW" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>東大版 技術高中數學（第三冊）2-3 對數及其運算的意義 ‧ 數位翻牌互動課程平台</title>
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  
  <!-- FontAwesome 6 Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <!-- KaTeX CSS & JS -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- QRCode.js -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>

  <style>
    .perspective {{
      perspective: 1200px;
    }}
    .transform-style-3d {{
      transform-style: preserve-3d;
    }}
    .backface-hidden {{
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
    }}
    .rotate-y-180 {{
      transform: rotateY(180deg);
    }}

    .katex, .katex-html, .katex-display {{
      white-space: nowrap !important;
    }}
    .katex-display {{
      margin: 0.2em 0 !important;
      display: inline-block !important;
      max-width: 100% !important;
    }}
    .katex svg,
    #fullscreen-modal .katex svg {{
      display: block !important;
      position: absolute !important;
      width: 100% !important;
      height: inherit !important;
      fill: currentColor !important;
      stroke: currentColor !important;
      max-height: none !important;
      margin: 0 !important;
    }}

    #fullscreen-modal:fullscreen,
    #fullscreen-modal:-webkit-full-screen {{
      width: 100vw !important;
      height: 100vh !important;
      max-width: 100vw !important;
      max-height: 100vh !important;
      padding: 0 !important;
      margin: 0 !important;
      border-radius: 0 !important;
    }}

    #mindmap-modal-dialog:fullscreen,
    #mindmap-modal-dialog:-webkit-full-screen {{
      max-width: 100vw !important;
      width: 100vw !important;
      height: 100vh !important;
      max-height: 100vh !important;
      border-radius: 0 !important;
      margin: 0 !important;
    }}

    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #f1f5f9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
  </style>
</head>
<body class="bg-slate-100 text-slate-800 font-sans antialiased min-h-screen flex flex-col selection:bg-red-600 selection:text-white">

  <!-- 頂部導覽列 (柯南深藍風格 + 偵探徽章) -->
  <header class="sticky top-0 z-40 bg-slate-900/95 backdrop-blur-md border-b-2 border-red-600 shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <div class="flex items-center gap-3">
        <a href="#top" class="flex items-center gap-2.5 group">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-900 via-blue-800 to-red-600 flex items-center justify-center text-white shadow-md shadow-blue-950 group-hover:scale-105 transition-all border border-amber-400/30">
            <i class="fa-solid fa-glasses text-lg text-amber-300"></i>
          </div>
          <div>
            <h1 class="text-base sm:text-lg font-black text-white tracking-tight whitespace-nowrap flex items-center gap-1.5">
              <span>名偵探柯南 ‧ 數理偵查檔案</span>
              <span class="text-xs px-2 py-0.5 rounded bg-red-600 text-white font-mono font-bold">2-3</span>
            </h1>
            <p class="text-[11px] font-bold text-amber-300 whitespace-nowrap">
              東大版 技術高中數學（第三冊）‧ 第二章 指數與對數解密篇
            </p>
          </div>
        </a>
      </div>

      <div class="flex items-center gap-2 sm:gap-3">
        <button onclick="openCheatSheetModal()" class="px-3 py-1.5 rounded-xl bg-amber-400 text-slate-950 hover:bg-amber-300 text-xs font-black transition-all flex items-center gap-1.5 shadow-md shadow-amber-400/20">
          <i class="fa-solid fa-scroll text-red-600"></i> <span class="hidden sm:inline">解密口訣錦囊</span>
        </button>
        <button onclick="openMindmapModal()" class="px-3 py-1.5 rounded-xl bg-blue-950/80 text-blue-200 hover:bg-blue-800 hover:text-white text-xs font-bold transition-all flex items-center gap-1.5 border border-blue-700/60 shadow-xs">
          <i class="fa-solid fa-sitemap text-amber-400"></i> <span class="hidden sm:inline">破案知識網絡</span>
        </button>
        <button onclick="openLabModal()" class="px-3 py-1.5 rounded-xl bg-slate-800 text-amber-300 hover:bg-amber-500 hover:text-slate-950 text-xs font-bold transition-all flex items-center gap-1.5 border border-amber-400/40 shadow-xs">
          <i class="fa-solid fa-flask text-amber-400"></i> <span class="hidden sm:inline">阿笠博士實驗室</span>
        </button>
        <button onclick="openChallengeModal(0)" class="px-3 py-1.5 rounded-xl bg-red-600 text-white hover:bg-red-500 text-xs font-bold transition-all flex items-center gap-1.5 shadow-md shadow-red-900/50">
          <i class="fa-solid fa-bullseye text-white"></i> <span class="hidden sm:inline">少年偵探團考核</span>
        </button>
        <button onclick="openQrModal()" class="p-2 rounded-xl bg-slate-800 text-slate-300 hover:bg-slate-700 text-xs font-bold transition-all border border-slate-700" title="手機掃碼搜查連線">
          <i class="fa-solid fa-qrcode text-amber-400"></i>
        </button>
      </div>
    </div>
  </header>

  <!-- 主橫幅區 (Hero Section：柯南深藍海軍西裝 + 領結紅 + 偵探儀表板) -->
  <section class="bg-gradient-to-b from-slate-950 via-blue-950 to-slate-900 text-white pt-10 pb-12 px-4 sm:px-6 lg:px-8 border-b-4 border-amber-500">
    <div class="max-w-7xl mx-auto">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
        <div class="lg:col-span-8">
          <div class="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-blue-900/60 text-amber-300 border border-amber-400/40 text-xs font-bold mb-4 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
            <span>【名偵探柯南 ‧ 數理搜查任務】真相永遠只有一個！</span>
          </div>
          <h2 class="text-3xl sm:text-4xl lg:text-5xl font-black tracking-tight mb-4 leading-tight text-white">
            對數及其運算的意義 ‧ 密碼破解特訓
          </h2>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed mb-6 max-w-2xl">
            收錄全單元 {len(cards)} 件案件線索圖解學習卡（堅持一題一案、一小題獨立成卡，例題隨堂與課後習題 100% 忠實課本原文）。
            配備名偵探破案導引、線索推理鏈、多功能電子搜查白板、阿笠博士動態實驗室與滿版探案簡報。
          </p>

          <!-- 資源下載快捷列 (SOP v4.0 純化旗艦四大標竿按鈕) -->
          <div class="flex flex-wrap items-center gap-3">
            <button onclick="downloadStudentDocx()" class="px-4 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-bold text-xs sm:text-sm shadow-md shadow-amber-950 transition-all flex items-center gap-2 border border-amber-400">
              <i class="fa-solid fa-file-lines text-slate-950"></i> 偵探搜查實作單 (B4 Word)
            </button>
            <button onclick="openTeacherPwdModal('lesson_plan')" class="px-4 py-2.5 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs sm:text-sm border border-emerald-500 shadow-md shadow-emerald-950 transition-all flex items-center gap-2">
              <i class="fa-solid fa-chalkboard-user text-amber-300"></i> 四節課教學計畫與教案 (B4 Word)
            </button>
            <button onclick="openTeacherPwdModal('teacher')" class="px-4 py-2.5 rounded-xl bg-red-700 hover:bg-red-600 text-white font-bold text-xs sm:text-sm border border-red-500 shadow-md shadow-red-950 transition-all flex items-center gap-2">
              <i class="fa-solid fa-user-secret text-amber-300"></i> 警視廳機密解答卷宗 (密碼保護)
            </button>
            <a href="download/2-3_對數及其運算的意義_全套65張圖解學習卡.pdf" target="_blank" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs sm:text-sm border border-amber-400/50 hover:border-amber-400 transition-all flex items-center gap-2">
              <i class="fa-solid fa-file-pdf text-amber-400"></i> 全套 65 案圖解卡 (A4 PDF)
            </a>
          </div>
        </div>

        <!-- 橫幅右側：即時偵查情報儀表板 -->
        <div class="lg:col-span-4 bg-slate-900/80 backdrop-blur-md rounded-2xl p-5 border-2 border-blue-800/80 shadow-2xl">
          <div class="text-xs font-bold text-amber-300 mb-3 flex items-center justify-between">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-shield-halved text-red-500"></i> 即時偵查情報儀表板</span>
            <span class="text-[10px] text-slate-400 font-mono">CASE 01~{len(cards)}</span>
          </div>
          <div class="grid grid-cols-3 gap-2 text-center mb-4">
            <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
              <div class="text-[10px] text-slate-400 mb-0.5">總搜查人次</div>
              <div id="stat-pageviews" class="text-lg font-black text-red-400 font-mono">0</div>
            </div>
            <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
              <div class="text-[10px] text-slate-400 mb-0.5">到訪特派員</div>
              <div id="stat-visitors" class="text-lg font-black text-amber-400 font-mono">0</div>
            </div>
            <div class="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
              <div class="text-[10px] text-slate-400 mb-0.5">破案互動數</div>
              <div id="stat-interactions" class="text-lg font-black text-emerald-400 font-mono">0</div>
            </div>
          </div>
          <div>
            <div class="flex items-center justify-between text-xs text-slate-300 font-semibold mb-1.5">
              <span class="flex items-center gap-1"><i class="fa-solid fa-stamp text-red-500"></i> 案件破案結案進度</span>
              <span id="progress-text" class="text-[11px] text-amber-300">已結案 0 / {len(cards)} 件</span>
            </div>
            <div class="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden border border-slate-700">
              <div id="progress-bar-fill" class="h-full bg-gradient-to-r from-red-600 via-amber-500 to-emerald-400 transition-all duration-500" style="width: 0%"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- 篩選列與卡片操作列 -->
  <section class="sticky top-16 z-30 bg-white/95 backdrop-blur-md border-b border-slate-200 py-3 px-4 sm:px-6 lg:px-8 shadow-xs">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
      <div class="flex flex-wrap items-center gap-1.5 sm:gap-2">
        <button onclick="filterByCategory('all')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-bold transition-all bg-blue-900 text-white shadow-xs">
          全部案件 ({len(cards)})
        </button>
        <button onclick="filterByCategory('對數定義')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          對數定義
        </button>
        <button onclick="filterByCategory('存在條件')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          存在條件
        </button>
        <button onclick="filterByCategory('基本性質')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          基本性質
        </button>
        <button onclick="filterByCategory('對數求值')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          對數求值
        </button>
        <button onclick="filterByCategory('加減運算')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          加減運算
        </button>
        <button onclick="filterByCategory('換底公式')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-700 hover:bg-blue-50 hover:text-blue-900">
          換底公式
        </button>
        <button onclick="filterByCategory('連鎖律')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-700">
          連鎖律
        </button>
        <button onclick="filterByCategory('綜合應用')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-700">
          綜合應用
        </button>
        <button onclick="filterByCategory('課後習作')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-700">
          課後習作
        </button>
        <button onclick="filterByCategory('進階思考')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-700">
          進階思考
        </button>
        <button onclick="filterByCategory('素養應用')" class="category-btn px-3 py-1.5 rounded-xl text-xs font-semibold transition-all bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-700">
          素養應用
        </button>
      </div>

      <div class="flex items-center gap-2">
        <button onclick="filterByStatus('all')" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-100 text-slate-600 hover:bg-slate-200">
          全部
        </button>
        <button onclick="filterByStatus('mastered')" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-50 text-emerald-700 hover:bg-emerald-100">
          <i class="fa-solid fa-check text-emerald-600"></i> 已熟練
        </button>
        <button onclick="filterByStatus('review')" class="px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-50 text-amber-700 hover:bg-amber-100">
          <i class="fa-solid fa-star text-amber-500"></i> 待複習
        </button>
        <div class="w-px h-4 bg-slate-300 mx-1"></div>
        <button onclick="flipAllCards(true)" class="p-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 text-xs font-bold" title="全部翻到背面詳解">
          <i class="fa-solid fa-rotate-right"></i> 全翻背面
        </button>
        <button onclick="flipAllCards(false)" class="p-1.5 rounded-lg bg-slate-100 text-slate-600 hover:bg-indigo-50 hover:text-indigo-600 text-xs font-bold" title="全部翻回正面題目">
          <i class="fa-solid fa-rotate-left"></i> 全翻正面
        </button>
      </div>
    </div>
  </section>

  <!-- 卡片網格主容器 (強制雙欄) -->
  <main class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8">
    <div id="cards-grid" class="grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8">
      <!-- 由 JS 動態生成 65 張圖卡 -->
    </div>
  </main>

  <!-- 頁尾 (第一列三色膠囊訪客計數器) -->
  <footer class="bg-white border-t border-slate-200 py-8 px-4 sm:px-6 lg:px-8 mt-12 text-center">
    <div class="max-w-4xl mx-auto space-y-4">
      
      <!-- 第一列：三色圖示膠囊徽章 (Core Rule 5 鐵律) -->
      <div class="flex items-center justify-center">
        <div class="inline-flex flex-wrap items-center justify-center gap-3 sm:gap-5 bg-slate-50 border border-slate-200 rounded-full px-5 py-2 shadow-xs text-xs font-bold text-slate-600">
          <div class="flex items-center gap-1.5">
            <i class="fa-solid fa-eye text-rose-500"></i>
            <span>人氣計數</span>
            <span id="footer-pageviews" class="font-mono font-extrabold text-slate-800">0</span>
            <span>次瀏覽</span>
          </div>
          <div class="w-px h-4 bg-slate-300"></div>
          <div class="flex items-center gap-1.5">
            <i class="fa-solid fa-users text-blue-600"></i>
            <span>到訪學生</span>
            <span id="footer-visitors" class="font-mono font-extrabold text-blue-700">0</span>
            <span>人</span>
          </div>
          <div class="w-px h-4 bg-slate-300"></div>
          <div class="flex items-center gap-1.5">
            <i class="fa-solid fa-bolt text-amber-500"></i>
            <span>學習互動</span>
            <span id="footer-interactions" class="font-mono font-extrabold text-emerald-700">0</span>
            <span>次操作</span>
          </div>
        </div>
      </div>

      <!-- 第二列：課程名稱與署名 (Core Rule 9) -->
      <div class="text-xs text-slate-400 space-y-1">
        <p class="font-semibold text-slate-600">
          東大版 技術高中數學（第三冊）2-3 對數及其運算的意義 ‧ 數位互動課程教學包
        </p>
        <p>
          <span class="font-bold text-slate-500">PLVS 數學科  教育學習用</span> ｜ 嚴格遵守 2026 最新正式版標準規範製作
        </p>
      </div>

    </div>
  </footer>

  <!-- 彈窗模組 1：劇院全螢幕模式 (柯南名偵探搜查劇院 + 搜查電子白板) -->
  <div id="fullscreen-modal" class="hidden fixed inset-0 z-50 bg-slate-950 flex flex-col w-screen h-screen m-0 p-0 overflow-hidden">
    <!-- 頂部高對比導航與白板工具列 -->
    <header class="h-14 px-3 sm:px-4 bg-slate-900 border-b-2 border-red-600 flex items-center justify-between text-white shrink-0 select-none z-30">
      <!-- 左側：顯著返回鍵群與案件資訊 -->
      <div class="flex items-center gap-2 sm:gap-3 min-w-0">
        <!-- 核心返回鍵：返回案件總覽 -->
        <button onclick="closeModal()" class="px-3 py-1.5 rounded-lg bg-blue-800 hover:bg-blue-700 text-white font-bold text-xs sm:text-sm flex items-center gap-1.5 shadow-md transition-all border border-blue-500/40" title="返回案卷總覽 (按 ESC 鍵)">
          <i class="fa-solid fa-arrow-left"></i>
          <span>返回案卷總覽 (ESC)</span>
        </button>

        <!-- 知識網絡返回鍵 (從心智圖跳轉時顯現) -->
        <button id="modal-back-to-mindmap-btn" onclick="returnToMindmap()" class="hidden px-2.5 py-1.5 rounded-lg bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs flex items-center gap-1.5 shadow-sm transition-all border border-amber-400/30" title="返回破案知識網絡">
          <i class="fa-solid fa-sitemap"></i>
          <span class="hidden sm:inline">返回破案網絡</span>
        </button>

        <span id="modal-front-badge" class="px-2.5 py-1 rounded-md bg-slate-800 text-amber-300 border border-slate-700 text-xs font-black shrink-0 font-mono"></span>
        <h2 id="modal-front-title" class="text-sm sm:text-base font-bold text-slate-100 truncate max-w-xs sm:max-w-md md:max-w-lg"></h2>
      </div>

      <!-- 中間：名偵探電子白板工具列 -->
      <div class="hidden md:flex items-center gap-1.5 bg-slate-800/95 px-3 py-1 rounded-xl border border-slate-700 shadow-inner">
        <!-- 模式切換：滑鼠操作 (V) vs 偵探筆記 (B) vs 螢光標註 (H) vs 消除證物 (E) -->
        <div class="flex items-center bg-slate-900/80 p-0.5 rounded-lg border border-slate-700">
          <button id="wb-tool-mouse" onclick="setWhiteboardMode('mouse')" class="px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-emerald-600 text-white shadow-md ring-2 ring-emerald-400" title="現場調查模式 (按 V 鍵)：穿透白板，點選操作下方卡片步驟、滑動內容或選取文字">
            <i class="fa-solid fa-arrow-pointer"></i>
            <span>調查 (V)</span>
          </button>
          <button id="wb-tool-pen" onclick="setWhiteboardMode('pen')" class="px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700" title="偵探筆記模式 (按 B 鍵)：手寫紀錄筆跡">
            <i class="fa-solid fa-pen"></i>
            <span>筆記 (B)</span>
          </button>
          <button id="wb-tool-highlighter" onclick="setWhiteboardMode('highlighter')" class="px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700" title="重點螢光標註 (按 H 鍵)：半透明粗筆刷，畫線標記關鍵證物不遮擋文字">
            <i class="fa-solid fa-highlighter text-amber-400"></i>
            <span>螢光 (H)</span>
          </button>
          <button id="wb-tool-eraser" onclick="setWhiteboardMode('eraser')" class="px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700" title="證物擦除模式 (按 E 鍵)">
            <i class="fa-solid fa-eraser"></i>
            <span>擦除 (E)</span>
          </button>
        </div>

        <div class="w-px h-4 bg-slate-600 mx-0.5"></div>

        <!-- 畫筆/螢光筆粗細選擇器 -->
        <div id="wb-pen-size-group" class="flex items-center gap-1">
          <select id="wb-pen-size-select" onchange="setPenSize(this.value)" class="bg-slate-700 text-white text-xs rounded px-1.5 py-1 border-0 focus:ring-1 focus:ring-amber-400 cursor-pointer" title="筆刷粗細">
            <option value="2">細筆 2px</option>
            <option value="4" selected>標準 4px</option>
            <option value="7">重點 7px</option>
            <option value="14">螢光 14px</option>
            <option value="22">螢光粗 22px</option>
            <option value="32">特粗標註 32px</option>
          </select>
        </div>

        <!-- 螢光筆專屬透明度選擇器 -->
        <div id="wb-alpha-group" class="hidden flex items-center gap-1 bg-slate-900/60 px-2 py-0.5 rounded-lg border border-amber-500/30">
          <span class="text-[11px] text-amber-300 font-bold flex items-center gap-1">
            <i class="fa-solid fa-circle-half-stroke"></i>
            <span class="hidden lg:inline">透明度:</span>
          </span>
          <select id="wb-highlighter-alpha" onchange="setHighlighterAlpha(this.value)" class="bg-slate-700 text-amber-300 font-bold text-xs rounded px-1.5 py-0.5 border-0 focus:ring-1 focus:ring-amber-400 cursor-pointer" title="調整螢光筆透明度">
            <option value="0.2">20% 輕透</option>
            <option value="0.4" selected>40% 標準</option>
            <option value="0.6">60% 鮮明</option>
            <option value="0.8">80% 深邃</option>
          </select>
        </div>

        <!-- 橡皮擦專屬大小選擇器 -->
        <div id="wb-eraser-size-group" class="hidden flex items-center gap-1 bg-slate-900/60 px-2 py-0.5 rounded-lg border border-amber-400/30">
          <span class="text-[11px] text-amber-400 font-bold flex items-center gap-1">
            <i class="fa-solid fa-eraser"></i>
            <span class="hidden lg:inline">擦除大小:</span>
          </span>
          <select id="wb-eraser-size-select" onchange="setEraserSize(this.value)" class="bg-slate-700 text-white font-bold text-xs rounded px-1.5 py-0.5 border-0 focus:ring-1 focus:ring-amber-400 cursor-pointer" title="調整橡皮擦擦除大小">
            <option value="12">細擦 12px</option>
            <option value="26" selected>中擦 26px</option>
            <option value="50">粗擦 50px</option>
            <option value="90">大板擦 90px</option>
          </select>
        </div>

        <!-- 調色盤群組 -->
        <div id="wb-colors-group" class="flex items-center gap-1 ml-0.5">
          <button onclick="setPenColor('#dc2626')" class="w-4 h-4 rounded-full bg-red-600 border border-white/50 hover:scale-110 transition-transform" title="領結紅"></button>
          <button onclick="setPenColor('#1e40af')" class="w-4 h-4 rounded-full bg-blue-800 border border-white/50 hover:scale-110 transition-transform" title="西裝藍"></button>
          <button onclick="setPenColor('#facc15')" class="w-4 h-4 rounded-full bg-yellow-400 border border-white/50 hover:scale-110 transition-transform" title="眼鏡金黃"></button>
          <button onclick="setPenColor('#16a34a')" class="w-4 h-4 rounded-full bg-green-600 border border-white/50 hover:scale-110 transition-transform" title="綠"></button>
          <button onclick="setPenColor('#d97706')" class="w-4 h-4 rounded-full bg-amber-600 border border-white/50 hover:scale-110 transition-transform" title="橘"></button>
          <button onclick="setPenColor('#9333ea')" class="w-4 h-4 rounded-full bg-purple-600 border border-white/50 hover:scale-110 transition-transform" title="紫"></button>
          <button onclick="setPenColor('#0f172a')" class="w-4 h-4 rounded-full bg-slate-900 border border-white/50 hover:scale-110 transition-transform" title="墨黑"></button>
          <input type="color" onchange="setPenColor(this.value)" class="w-5 h-5 rounded cursor-pointer bg-transparent border-0" title="自訂色彩">
        </div>

        <div class="w-px h-4 bg-slate-600 mx-0.5"></div>
        <button onclick="undoStroke()" class="p-1.5 rounded-lg bg-slate-700 text-slate-300 hover:text-white text-xs transition-all" title="復原上一筆">
          <i class="fa-solid fa-rotate-left"></i>
        </button>
        <button onclick="clearWhiteboard()" class="p-1.5 rounded-lg bg-slate-700 text-slate-300 hover:text-red-400 text-xs transition-all" title="清空白板">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>

      <!-- 右側：翻頁導航 + 全螢幕滿版切換 + 快捷返回鍵 -->
      <div class="flex items-center gap-2 shrink-0">
        <span id="modal-card-indicator" class="text-xs font-mono text-slate-400 hidden sm:inline">1 / {len(cards)}</span>
        <button onclick="prevModalCard()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition-all border border-slate-700" title="上一案件 (← 鍵)">
          <i class="fa-solid fa-chevron-left"></i>
        </button>
        <button onclick="nextModalCard()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white text-xs font-bold transition-all border border-slate-700" title="下一案件 (→ 鍵)">
          <i class="fa-solid fa-chevron-right"></i>
        </button>
        <button id="modal-fs-toggle-btn" onclick="toggleCardModalFullscreen()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-amber-300 hover:text-amber-200 text-xs font-bold transition-all border border-slate-700 flex items-center gap-1.5" title="全螢幕滿版投影 (按 F 鍵)">
          <i class="fa-solid fa-maximize"></i>
          <span class="hidden lg:inline">滿版劇院 (F)</span>
        </button>
        <button onclick="closeModal()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white text-xs font-bold flex items-center gap-1 shadow-sm transition-all" title="關閉返回總覽 (ESC)">
          <i class="fa-solid fa-xmark text-sm"></i>
          <span>返回</span>
        </button>
      </div>
    </header>

    <!-- 劇院全螢幕主體內容 (100% 滿版無黑邊寬螢幕佈局) -->
    <div id="modal-content-wrapper" class="relative flex-1 w-full h-[calc(100vh-3.5rem)] grid grid-cols-1 lg:grid-cols-2 gap-3 p-3 overflow-hidden bg-slate-950">
      <canvas id="whiteboard-canvas" class="absolute inset-0 z-20 pointer-events-none cursor-default w-full h-full"></canvas>

      <!-- 左欄：案件題幹與柯南破案導引 (滿版自適應) -->
      <div class="bg-white rounded-xl p-5 sm:p-6 flex flex-col justify-between shadow-xl border-t-4 border-blue-900 border-x border-b border-slate-200 z-10 overflow-y-auto">
        <div>
          <div class="text-xs font-black text-blue-900 mb-2.5 flex items-center gap-1.5">
            <i class="fa-solid fa-folder-closed text-red-600"></i>
            <span>案件題幹與核心概念</span>
          </div>
          <div id="modal-front-math" class="text-base sm:text-xl text-slate-800 leading-relaxed break-words py-2"></div>
        </div>
        <div id="modal-front-tip" class="mt-4 p-4 rounded-xl bg-amber-50/90 border border-amber-300 text-sm text-amber-950 leading-relaxed shadow-2xs"></div>
      </div>

      <!-- 右欄：線索推理鏈、結論印章與證物圖解 (滿版自適應) -->
      <div class="bg-white rounded-xl p-5 sm:p-6 flex flex-col justify-between shadow-xl border-t-4 border-red-600 border-x border-b border-slate-200 z-10 overflow-y-auto">
        <div class="space-y-3">
          <div class="flex items-center justify-between pb-2 border-b border-slate-100">
            <div class="text-xs font-black text-blue-950 flex items-center gap-1.5">
              <i class="fa-solid fa-glasses text-red-600"></i>
              <span>名偵探推理筆記與線索</span>
            </div>
            <div id="modal-step-buttons" class="flex items-center gap-1.5"></div>
          </div>
          <div id="modal-steps-container" class="space-y-2.5"></div>
          <div id="modal-conclusion" class="p-3 rounded-xl bg-red-50/80 border-2 border-red-500 text-sm font-bold text-red-950 shadow-2xs"></div>
        </div>
        <div id="modal-svg-container" class="mt-3 p-3 bg-slate-50 rounded-xl border border-slate-200 flex items-center justify-center min-h-[160px] max-h-[320px] overflow-hidden shadow-inner"></div>
      </div>

      <!-- 右下角懸浮模式切換膠囊 (現場調查 | 偵探筆記 | 螢光重點 | 證物擦除) -->
      <div id="wb-floating-switch" class="absolute bottom-4 right-5 z-30 flex items-center bg-slate-900/90 backdrop-blur-md px-2 py-1.5 rounded-full border border-slate-700/80 shadow-2xl text-xs font-bold gap-1 select-none">
        <button id="wb-float-mouse" onclick="setWhiteboardMode('mouse')" class="px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all bg-emerald-600 text-white shadow-lg ring-2 ring-emerald-400 font-black" title="切換為調查模式：點選操作下方卡片步驟">
          <i class="fa-solid fa-arrow-pointer"></i>
          <span>現場調查</span>
        </button>
        <button id="wb-float-pen" onclick="setWhiteboardMode('pen')" class="px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800" title="切換為筆記：手寫紀錄字跡">
          <i class="fa-solid fa-pen"></i>
          <span>偵探筆記</span>
        </button>
        <button id="wb-float-highlighter" onclick="setWhiteboardMode('highlighter')" class="px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800" title="切換為螢光標註：半透明畫重點">
          <i class="fa-solid fa-highlighter text-amber-400"></i>
          <span>螢光標註</span>
        </button>
        <button id="wb-float-eraser" onclick="setWhiteboardMode('eraser')" class="px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800" title="切換為擦除：擦除證物筆跡">
          <i class="fa-solid fa-eraser"></i>
          <span>消除證物</span>
        </button>
      </div>

    </div>
  </div>

  <!-- 彈窗模組 2：心智圖視窗 -->
  <div id="mindmap-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div id="mindmap-modal-dialog" class="bg-white rounded-2xl w-full max-w-5xl h-[88vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-slate-50">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-sitemap text-indigo-600 text-lg"></i>
          <h3 class="font-black text-slate-800 text-base">單元知識架構全覽心智圖</h3>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="toggleMindmapFullscreen()" class="px-3 py-1.5 rounded-xl bg-slate-200 hover:bg-slate-300 text-slate-700 text-xs font-bold transition-all" title="全螢幕投影 (按 F 鍵)">
            <i class="fa-solid fa-maximize"></i> 全螢幕投影 (F)
          </button>
          <button onclick="closeMindmapModal()" class="px-3 py-1.5 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold transition-all">
            <i class="fa-solid fa-arrow-left"></i> 返回學習卡總覽 (ESC)
          </button>
        </div>
      </div>
      <div id="mindmap-tree-content" class="flex-1 p-6 overflow-y-auto"></div>
      <div class="px-6 py-3 border-t border-slate-200 flex items-center justify-between bg-slate-50 text-xs text-slate-400">
        <span>點擊節點卡號可直接跳轉全螢幕投影，並支援一鍵返回心智圖</span>
        <button onclick="closeMindmapModal()" class="font-bold text-slate-600 hover:text-indigo-600">
          返回總覽 (ESC)
        </button>
      </div>
    </div>
  </div>

  <!-- 彈窗模組 3：動態幾何圖形實驗室 -->
  <div id="lab-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl w-full max-w-4xl max-h-[85vh] flex flex-col shadow-2xl border border-slate-200 overflow-hidden">
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-emerald-50">
        <div class="flex items-center gap-2">
          <i class="fa-solid fa-flask text-emerald-600 text-lg"></i>
          <h3 class="font-black text-slate-800 text-base">單元專屬動態幾何實驗室：對數曲線與芮氏地震能量尺</h3>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="closeLabModal()" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-all" title="返回學習卡總覽 (ESC)">
            <i class="fa-solid fa-arrow-left"></i>
            <span>返回總覽 (ESC)</span>
          </button>
        </div>
      </div>

      <div class="p-6 overflow-y-auto space-y-6">
        <!-- 實驗 1：對數曲線與底數互動實驗室 -->
        <div class="bg-slate-50 rounded-xl p-5 border border-slate-200">
          <h4 class="font-bold text-slate-800 text-sm mb-3">實驗一：對數函數 $y = \\log_a(x)$ 底數動態形變實驗</h4>
          <div class="mb-4">
            <label class="text-xs font-bold text-slate-600">
              底數 a 值：<span id="lab-base-val" class="text-indigo-600 font-mono font-black text-sm">2.0</span>
              <span class="text-slate-400 font-normal ml-2">(拖曳滑桿觀察 a &gt; 1 遞增 與 0 &lt; a &lt; 1 遞減曲線形變)</span>
            </label>
            <input type="range" id="lab-base-slider" min="0.2" max="5.0" step="0.1" value="2.0" class="w-full mt-1 accent-indigo-600">
          </div>
          <div id="lab-curve-svg-container" class="p-3 bg-white rounded-lg border border-slate-200 flex items-center justify-center min-h-[240px]"></div>
        </div>

        <!-- 實驗 2：地震規模與能量對數尺模擬器 -->
        <div class="bg-slate-50 rounded-xl p-5 border border-slate-200">
          <h4 class="font-bold text-slate-800 text-sm mb-3">實驗二：芮氏地震規模與能量對數尺（$\\log_{{10}} E = 11.8 + 1.5M$）</h4>
          <div class="mb-4">
            <label class="text-xs font-bold text-slate-600">
              芮氏地震規模 M：<span id="lab-eq-val" class="text-rose-600 font-mono font-black text-sm">5.0</span>
              <span class="text-slate-400 font-normal ml-2">(拖曳觀察地震釋放能量呈指數級幾何暴增)</span>
            </label>
            <input type="range" id="lab-eq-slider" min="3.0" max="9.0" step="0.1" value="5.0" class="w-full mt-1 accent-rose-600">
          </div>
          <div id="lab-eq-result" class="p-4 bg-white rounded-lg border border-slate-200 text-center"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- 彈窗模組 3.5：名偵探解密口訣錦囊 (速記圖形與心法) -->
  <div id="cheatsheet-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl w-full max-w-4xl max-h-[88vh] flex flex-col shadow-2xl border-4 border-amber-500 overflow-hidden">
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-gradient-to-r from-blue-950 via-slate-900 to-red-950 text-white">
        <div class="flex items-center gap-2.5">
          <div class="w-9 h-9 rounded-xl bg-amber-400 text-slate-950 flex items-center justify-center text-lg font-black shadow-md">
            <i class="fa-solid fa-scroll text-red-600"></i>
          </div>
          <div>
            <h3 class="font-black text-amber-300 text-base">名偵探破案密碼 ‧ 對數解密口訣錦囊</h3>
            <p class="text-[11px] text-slate-300">秒殺對數定義互換、運算化簡、換底連鎖與高頻避雷心法</p>
          </div>
        </div>
        <button onclick="closeCheatSheetModal()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-all" title="返回總覽 (ESC)">
          <i class="fa-solid fa-arrow-left"></i>
          <span>返回 (ESC)</span>
        </button>
      </div>

      <div class="p-6 overflow-y-auto space-y-5 bg-slate-50">
        <!-- 錦囊 1：旋轉蝸牛法 -->
        <div class="bg-white p-5 rounded-2xl border-2 border-blue-900 shadow-xs">
          <div class="flex items-center gap-2 mb-2">
            <span class="px-2 py-0.5 rounded bg-blue-900 text-white text-xs font-black font-mono">SECRET 1</span>
            <h4 class="font-black text-blue-950 text-sm sm:text-base">指對數互換【旋轉蝸牛法】（逆時針畫圈神技）</h4>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
            <div class="md:col-span-7 space-y-2 text-xs sm:text-sm text-slate-700 leading-relaxed">
              <div class="p-2.5 bg-blue-50/60 rounded-xl border border-blue-200 font-bold text-blue-950">
                口訣：<span class="text-red-600">「從底數出發，繞過等號扛次方，最後撞向真數！」</span>
              </div>
              <ul class="list-disc pl-5 space-y-1">
                <li>看到 $\\log_a b = x$，筆尖點在底數 $a$。</li>
                <li>逆時針畫弧線繞過等號，把 $x$ 頂上去變成次方 $\\implies a^x$。</li>
                <li>弧線繼續繞回左邊撞向真數 $b$ $\\implies = b$。</li>
                <li><strong>心法底氣：</strong>「底數永遠在底部，對數本質就是求次方！」</li>
              </ul>
            </div>
            <div class="md:col-span-5 bg-gradient-to-tr from-slate-900 to-blue-950 text-white p-4 rounded-xl text-center shadow-inner">
              <div class="text-xs text-amber-300 font-bold mb-1">【蝸牛旋轉軌跡圖解】</div>
              <div class="text-lg font-mono font-black py-2 tracking-wide text-amber-400">
                $\\log_{{a}} b = x \\iff a^x = b$
              </div>
              <div class="text-[11px] text-slate-300 font-medium">例：$\\log_2 8 = 3 \\iff 2^3 = 8$</div>
            </div>
          </div>
        </div>

        <!-- 錦囊 2：四字破案訣 -->
        <div class="bg-white p-5 rounded-2xl border-2 border-amber-500 shadow-xs">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-2 py-0.5 rounded bg-amber-500 text-slate-950 text-xs font-black font-mono">SECRET 2</span>
            <h4 class="font-black text-amber-950 text-sm sm:text-base">對數四律【四字破案神訣】（押韻速記）</h4>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
              <div class="font-black text-amber-900 mb-1 flex items-center gap-1">
                <i class="fa-solid fa-plus-minus text-amber-600"></i> ①「真數相乘，對數相加」
              </div>
              <div class="font-mono text-slate-800 py-1">$\\log_a(MN) = \\log_a M + \\log_a N$</div>
              <div class="text-[11px] text-slate-600">合體相乘兩案卷，拆開分開用加法記！</div>
            </div>
            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
              <div class="font-black text-amber-900 mb-1 flex items-center gap-1">
                <i class="fa-solid fa-divide text-amber-600"></i> ②「真數相除，對數相減」
              </div>
              <div class="font-mono text-slate-800 py-1">$\\log_a(\\frac{{M}}{{N}}) = \\log_a M - \\log_a N$</div>
              <div class="text-[11px] text-slate-600">分子除以分母，拆開運算變成減法！</div>
            </div>
            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
              <div class="font-black text-amber-900 mb-1 flex items-center gap-1">
                <i class="fa-solid fa-arrow-up-from-bracket text-amber-600"></i> ③「真上次頂，底下方沉」
              </div>
              <div class="font-mono text-slate-800 py-1">$\\log_{{a^r}} M^s = \\frac{{s}}{{r}} \\log_a M$</div>
              <div class="text-[11px] text-slate-600">真數次方提到分子，底數次方掉到分母！</div>
            </div>
            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200">
              <div class="font-black text-amber-900 mb-1 flex items-center gap-1">
                <i class="fa-solid fa-wand-magic-sparkles text-amber-600"></i> ④「上下同底，穿透還原」
              </div>
              <div class="font-mono text-slate-800 py-1">$a^{{\\log_a M}} = M$</div>
              <div class="text-[11px] text-slate-600">底數與對數底相同，瞬間抵消真數落地！</div>
            </div>
          </div>
        </div>

        <!-- 錦囊 3：換底高鐵與連鎖骨牌 -->
        <div class="bg-white p-5 rounded-2xl border-2 border-emerald-600 shadow-xs">
          <div class="flex items-center gap-2 mb-3">
            <span class="px-2 py-0.5 rounded bg-emerald-600 text-white text-xs font-black font-mono">SECRET 3</span>
            <h4 class="font-black text-emerald-950 text-sm sm:text-base">換底公式【高鐵換軌法】與【骨牌連鎖律】</h4>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs sm:text-sm">
            <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200">
              <div class="font-black text-emerald-900 mb-1">🚄 換底公式：樓上留樓上，樓下掉樓下！</div>
              <div class="font-mono text-slate-800 py-1.5 text-center text-sm">$\\log_a b = \\frac{{\\log_c b}}{{\\log_c a}}$</div>
              <div class="text-xs text-slate-600 leading-relaxed">
                原本上面的真數 $b$ 留在分子（樓上），原本下面的底數 $a$ 掉到分母（樓下）！<br>
                <strong>倒數特例：</strong>$\\log_a b = \\frac{{1}}{{\\log_b a}}$（底真互換直接倒數！）
              </div>
            </div>
            <div class="p-3.5 rounded-xl bg-emerald-50 border border-emerald-200">
              <div class="font-black text-emerald-900 mb-1">🀄 骨牌連鎖律：對角連連看，中間全倒光！</div>
              <div class="font-mono text-slate-800 py-1.5 text-center text-sm">$\\log_a b \\cdot \\log_b c \\cdot \\log_c d = \\log_a d$</div>
              <div class="text-xs text-slate-600 leading-relaxed">
                化為分式後，右上與左下真底互相約分，整排骨牌中間全部消去，只留下起點與終點！
              </div>
            </div>
          </div>
        </div>

        <!-- 錦囊 4：防錯避雷針 -->
        <div class="bg-red-50 p-5 rounded-2xl border-2 border-red-500 shadow-xs">
          <div class="flex items-center gap-2 mb-2">
            <span class="px-2 py-0.5 rounded bg-red-600 text-white text-xs font-black font-mono">WARNING</span>
            <h4 class="font-black text-red-950 text-sm sm:text-base">柯南嚴選 ‧ 考場高頻【防錯避雷針】（絕不能犯）</h4>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-2.5 text-xs text-red-950 font-bold">
            <div class="p-2.5 bg-white rounded-xl border border-red-300">
              <div class="text-red-600">❌ 禁忌一：內加外不加！</div>
              <div class="font-mono mt-1 text-slate-700">$\\log(M+N) \\ne \\log M + \\log N$</div>
              <div class="text-[11px] text-slate-500 font-normal">括號內相加絕不能拆成對數相加！</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-red-300">
              <div class="text-red-600">❌ 禁忌二：內減外不減！</div>
              <div class="font-mono mt-1 text-slate-700">$\\log(M-N) \\ne \\log M - \\log N$</div>
              <div class="text-[11px] text-slate-500 font-normal">括號內相減絕不能拆成對數相減！</div>
            </div>
            <div class="p-2.5 bg-white rounded-xl border border-red-300">
              <div class="text-red-600">❌ 禁忌三：對數相乘不能加！</div>
              <div class="font-mono mt-1 text-slate-700">$(\\log M)(\\log N) \\ne \\log(M+N)$</div>
              <div class="text-[11px] text-slate-500 font-normal">兩個對數相乘沒有任何加法合併公式！</div>
            </div>
          </div>
        </div>
      </div>

      <div class="px-6 py-3 border-t border-slate-200 flex items-center justify-between bg-white text-xs text-slate-500">
        <span class="font-bold text-blue-900"><i class="fa-solid fa-stamp text-red-600 mr-1"></i> 掌握破案錦囊，對數化簡一招制敵！</span>
        <button onclick="closeCheatSheetModal()" class="px-3 py-1 bg-slate-800 text-white font-bold rounded-lg hover:bg-slate-700">
          關閉錦囊 (ESC)
        </button>
      </div>
    </div>
  </div>

  <!-- 彈窗模組 4：闖關檢核系統 (CASE 01~06 少年偵探團升級考核) -->
  <div id="challenge-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl w-full max-w-2xl max-h-[88vh] flex flex-col shadow-2xl border-2 border-blue-900 overflow-hidden">
      <div class="px-6 py-4 border-b border-slate-200 flex items-center justify-between bg-blue-950 text-white">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-lg bg-red-600 flex items-center justify-center text-white text-base">
            <i class="fa-solid fa-bullseye"></i>
          </div>
          <div>
            <h3 class="font-black text-amber-300 text-base" id="stage-title">少年偵探團升級特訓考核</h3>
            <p class="text-[11px] text-slate-300" id="stage-desc">包含 CASE 05 警視廳特訓與 CASE 06 劇場版終極魔王關</p>
          </div>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="closeChallengeModal()" class="px-3 py-1.5 rounded-lg bg-red-600 hover:bg-red-500 text-white text-xs font-bold flex items-center gap-1.5 shadow-sm transition-all" title="返回案件總覽 (ESC)">
            <i class="fa-solid fa-arrow-left"></i>
            <span>返回 (ESC)</span>
          </button>
        </div>
      </div>

      <div class="p-6 overflow-y-auto space-y-4">
        <!-- 案件關卡快捷選單 -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-2">
          <button onclick="openChallengeModal(0)" class="p-2 rounded-lg bg-slate-100 hover:bg-blue-100 text-left transition-all border border-slate-200">
            <div class="text-[11px] font-black text-blue-900 font-mono">CASE 01</div>
            <div class="text-xs font-bold text-slate-700">初步勘驗 ‧ 存在條件</div>
          </button>
          <button onclick="openChallengeModal(1)" class="p-2 rounded-lg bg-slate-100 hover:bg-blue-100 text-left transition-all border border-slate-200">
            <div class="text-[11px] font-black text-blue-900 font-mono">CASE 02</div>
            <div class="text-xs font-bold text-slate-700">暗號破譯 ‧ 對數求值</div>
          </button>
          <button onclick="openChallengeModal(2)" class="p-2 rounded-lg bg-slate-100 hover:bg-blue-100 text-left transition-all border border-slate-200">
            <div class="text-[11px] font-black text-blue-900 font-mono">CASE 03</div>
            <div class="text-xs font-bold text-slate-700">證物化驗 ‧ 運算整合</div>
          </button>
          <button onclick="openChallengeModal(3)" class="p-2 rounded-lg bg-slate-100 hover:bg-blue-100 text-left transition-all border border-slate-200">
            <div class="text-[11px] font-black text-blue-900 font-mono">CASE 04</div>
            <div class="text-xs font-bold text-slate-700">連環暗鎖 ‧ 換底連鎖</div>
          </button>
          <button onclick="openChallengeModal(4)" class="p-2 rounded-lg bg-amber-100 hover:bg-amber-200 text-left transition-all border-2 border-amber-400">
            <div class="text-[11px] font-black text-amber-800 font-mono">CASE 05 ★</div>
            <div class="text-xs font-bold text-amber-950">警視廳特訓 ‧ 習作實戰</div>
          </button>
          <button onclick="openChallengeModal(5)" class="p-2 rounded-lg bg-red-100 hover:bg-red-200 text-left transition-all border-2 border-red-500">
            <div class="text-[11px] font-black text-red-700 font-mono">CASE 06 👑</div>
            <div class="text-xs font-bold text-red-950">劇場版 ‧ 終極魔王破案</div>
          </button>
        </div>

        <!-- 偵查面板 (麻醉槍針數與破案得分) -->
        <div class="bg-slate-900 text-white p-3 rounded-xl flex items-center justify-between text-xs font-bold border border-slate-700">
          <div class="flex items-center gap-1.5">
            <span class="text-amber-300">麻醉槍指針：</span>
            <span id="stage-lives" class="text-base tracking-widest">🎯🎯🎯</span>
          </div>
          <div class="flex items-center gap-3">
            <span id="stage-combo" class="text-amber-400 font-black animate-pulse"></span>
            <span>破案積分：<span id="stage-score" class="text-emerald-400 font-mono text-sm">0</span></span>
          </div>
        </div>

        <div id="stage-question-container" class="bg-slate-50 p-5 rounded-2xl border border-slate-200"></div>
      </div>
    </div>
  </div>

  <!-- 彈窗模組 5：教師密碼驗證 (警視廳機密解鎖：88888888) -->
  <div id="teacher-pwd-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl w-full max-w-md p-6 shadow-2xl border-2 border-red-600 text-center">
      <div class="w-12 h-12 rounded-full bg-red-100 text-red-600 flex items-center justify-center mx-auto mb-3 text-xl">
        <i class="fa-solid fa-user-secret"></i>
      </div>
      <h3 class="font-black text-slate-900 text-base mb-1">警視廳機密解答卷宗 ‧ 存取驗證</h3>
      <p class="text-xs text-slate-500 mb-4">請輸入專業偵查授權密碼以取得紅字步驟解答卷宗</p>
      
      <input type="password" id="teacher-pwd-input" placeholder="請輸入 8 位數授權密碼" class="w-full text-center px-4 py-2.5 rounded-xl border border-slate-300 focus:outline-none focus:ring-2 focus:ring-red-500 text-sm font-mono mb-2">
      <div id="teacher-pwd-err" class="text-xs font-bold text-red-600 hidden mb-3"></div>

      <div class="flex items-center gap-2">
        <button onclick="closeTeacherPwdModal()" class="flex-1 py-2.5 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs font-bold">
          取消
        </button>
        <button onclick="verifyTeacherPwd()" class="flex-1 py-2.5 rounded-xl bg-red-600 hover:bg-red-700 text-white text-xs font-bold shadow-md shadow-red-200">
          驗證並解鎖
        </button>
      </div>
    </div>
  </div>

  <!-- 彈窗模組 6：手機掃碼上線 QR Code -->
  <div id="qrcode-modal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
    <div class="bg-white rounded-2xl w-full max-w-sm p-6 shadow-2xl border border-slate-200 text-center">
      <div class="flex items-center justify-between mb-4">
        <h3 class="font-black text-slate-800 text-sm flex items-center gap-1.5">
          <i class="fa-solid fa-mobile-screen-button text-indigo-600"></i> 手機掃碼立即上線
        </h3>
        <button onclick="closeQrModal()" class="text-slate-400 hover:text-slate-600 p-1">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
      <div id="qrcode-display" class="flex justify-center p-4 bg-slate-50 rounded-xl border border-slate-200 mb-4"></div>
      <p class="text-xs text-slate-500 mb-2">學生使用手機或平板相機掃描，免裝 App 即可連線</p>
      <input type="text" id="qr-url-input" class="w-full text-xs text-slate-600 bg-slate-100 rounded-lg p-2 border border-slate-200 mb-3" value="" readonly>
      <button onclick="copyQrUrl()" class="w-full py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold">
        複製網址
      </button>
    </div>
  </div>

  <!-- 嵌入資料與全域邏輯 -->
  <script>
    window.CARDS_DATA = {cards_json};
    window.QUIZ_DATA = {quiz_json};
    window.CHALLENGE_STAGES = {stages_json};
    window.B64_STUDENT_DOCX = "{docx_b64.DOCX_STUDENT_B64}";
    window.B64_TEACHER_DOCX = "{docx_b64.DOCX_TEACHER_B64}";
    window.B64_LESSON_PLAN_DOCX = "{docx_b64.DOCX_LESSON_PLAN_B64}";
  </script>

  <script>
    {interactive_js_module.INTERACTIVE_JS_CODE}
  </script>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("成功產生 index.html 旗艦版數位互動平台！")

if __name__ == "__main__":
    generate_index_html()

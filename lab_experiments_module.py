# -*- coding: utf-8 -*-
"""
lab_experiments_module.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
阿笠博士 7 大動態數理探案實驗室（Dr. Agasa Dynamic Science & Math Labs）
包含：
1. 底數動態形變實驗室 (y = log_a x 底數 a > 1 與 0 < a < 1)
2. 芮氏地震規模與能量對數尺 (log E = 4.8 + 1.5M 指數級暴增)
3. 指對數鏡射對稱實驗室 (y = a^x 與 y = log_a x 關於 y = x 對稱鏡像)
4. 納皮爾對數計算尺模擬器 (Napier Slide Rule：化乘除為加減的歷史神器)
5. 聲音分貝 (dB) 感官與能量倍率儀 (dB = 10 log(I/I0) 聽覺對數響度)
6. 化學酸鹼度 (pH 值) 光譜色階實驗室 (pH = -log[H+] 負對數變色試管)
7. 大數首數尾數顯微鏡 (大數位數與最高位數字定位儀)
分頁式無卷軸滿版設計，整合 KaTeX 與 Web Audio API。
"""

LAB_MODAL_HTML = r"""
  <!-- 彈窗模組 3：阿笠博士 7 大動態數理探案實驗室 (無卷軸分頁滿版設計) -->
  <style>
    #lab-modal * {
      scrollbar-width: none !important;
      -ms-overflow-style: none !important;
    }
    #lab-modal *::-webkit-scrollbar {
      display: none !important;
      width: 0 !important;
      height: 0 !important;
    }
  </style>
  <div id="lab-modal" class="hidden fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-1 sm:p-3">
    <div class="bg-white rounded-2xl w-full max-w-5xl h-[96vh] sm:h-[92vh] max-h-[840px] flex flex-col shadow-2xl border-2 border-emerald-500 overflow-hidden text-slate-800 select-none">
      
      <!-- 實驗室頂部標題與返回列 -->
      <header class="h-12 sm:h-14 px-3 sm:px-5 bg-gradient-to-r from-slate-900 via-emerald-950 to-slate-900 border-b border-emerald-500/70 flex items-center justify-between shrink-0 text-white">
        <div class="flex items-center gap-2.5">
          <div class="w-8 h-8 rounded-xl bg-gradient-to-tr from-emerald-400 to-teal-600 flex items-center justify-center text-slate-950 font-black text-base shadow-md">
            <i class="fa-solid fa-flask text-white"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h2 class="text-sm sm:text-base font-black text-emerald-300 tracking-tight flex items-center gap-1.5">
                阿笠博士 ‧ 7 大對數動態數理實驗室
              </h2>
              <span class="px-1.5 py-0.2 rounded-full bg-emerald-600 text-white text-[9px] font-extrabold uppercase animate-pulse">Dynamic Labs</span>
            </div>
          </div>
        </div>

        <div class="flex items-center gap-2">
          <button onclick="closeLabModal()" class="px-3 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs flex items-center gap-1 shadow-sm transition-all" title="返回學習卡總覽 (ESC)">
            <i class="fa-solid fa-arrow-left"></i>
            <span>返回總覽 (ESC)</span>
          </button>
        </div>
      </header>

      <!-- 7 大實驗分頁切換導航列 (橫向滑動/超薄) -->
      <nav class="bg-slate-100 px-2 sm:px-4 py-1.5 border-b border-slate-200 flex items-center gap-1 sm:gap-1.5 overflow-x-auto shrink-0 scrollbar-none">
        <button onclick="switchLabTab(1)" id="lab-tab-1" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-emerald-700 text-white shadow-xs">
          <span>① 底數形變</span>
        </button>
        <button onclick="switchLabTab(2)" id="lab-tab-2" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>② 芮氏地震</span>
        </button>
        <button onclick="switchLabTab(3)" id="lab-tab-3" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>③ 鏡射對稱</span>
        </button>
        <button onclick="switchLabTab(4)" id="lab-tab-4" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>④ 對數計算尺</span>
        </button>
        <button onclick="switchLabTab(5)" id="lab-tab-5" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>⑤ 聲音分貝</span>
        </button>
        <button onclick="switchLabTab(6)" id="lab-tab-6" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>⑥ pH 酸鹼度</span>
        </button>
        <button onclick="switchLabTab(7)" id="lab-tab-7" class="lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200">
          <span>⑦ 首尾顯微鏡</span>
        </button>
      </nav>

      <!-- 實驗內容容器 (七合一，高度自適應，無卷軸) -->
      <main class="flex-1 p-2 sm:p-4 overflow-hidden relative flex flex-col items-center justify-center bg-slate-50">

        <!-- ========================================== -->
        <!-- 實驗 1：對數曲線底數動態形變實驗室 -->
        <!-- ========================================== -->
        <div id="lab-panel-1" class="w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs">
            <span class="text-xs font-bold text-slate-700">
              底數 a 值：<span id="lab-base-val" class="text-indigo-600 font-mono font-black text-sm">2.0</span>
              <span class="text-slate-400 font-normal ml-2 text-[11px]">(拖曳滑桿觀察 a &gt; 1 遞增 與 0 &lt; a &lt; 1 遞減曲線形變)</span>
            </span>
            <span class="text-[11px] font-bold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
              恆過定點 (1, 0) ‧ 漸近線 x = 0
            </span>
          </div>
          <input type="range" id="lab-base-slider" min="0.2" max="5.0" step="0.1" value="2.0" class="w-full accent-indigo-600 cursor-pointer">
          <div id="lab-curve-svg-container" class="flex-1 p-2 bg-white rounded-xl border border-slate-200 flex items-center justify-center min-h-0 shadow-inner"></div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 2：芮氏地震規模與能量對數尺 -->
        <!-- ========================================== -->
        <div id="lab-panel-2" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs">
            <span class="text-xs font-bold text-slate-700">
              芮氏地震規模 M：<span id="lab-eq-val" class="text-rose-600 font-mono font-black text-sm">5.0</span>
              <span class="text-slate-400 font-normal ml-2 text-[11px]">($\log_{10} E = 4.8 + 1.5M$，觀察能量幾何級暴增)</span>
            </span>
            <span class="text-[11px] font-bold text-rose-700 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200">
              每差 1 級差約 31.6 倍 ‧ 差 2 級差 1000 倍
            </span>
          </div>
          <input type="range" id="lab-eq-slider" min="3.0" max="9.0" step="0.1" value="5.0" class="w-full accent-rose-600 cursor-pointer">
          <div class="flex-1 bg-white rounded-xl border border-slate-200 p-3 flex flex-col items-center justify-center min-h-0 shadow-inner space-y-2">
            <canvas id="lab-eq-canvas" width="600" height="150" class="max-w-full h-auto block"></canvas>
            <div id="lab-eq-result" class="text-center"></div>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 3：指對數鏡射對稱實驗室 (反函數對稱 y = x) -->
        <!-- ========================================== -->
        <div id="lab-panel-3" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex flex-wrap items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs text-xs">
            <div class="flex items-center gap-3">
              <span class="font-bold text-slate-700">底數 a：<span id="lab-sym-base-val" class="text-indigo-600 font-mono font-black">2.0</span></span>
              <input type="range" id="lab-sym-base-slider" min="1.2" max="3.5" step="0.1" value="2.0" class="w-28 accent-indigo-600">
              <span class="font-bold text-slate-700 ml-2">點 P 橫坐標 x：<span id="lab-sym-x-val" class="text-blue-600 font-mono font-black">1.0</span></span>
              <input type="range" id="lab-sym-x-slider" min="-1.5" max="2.2" step="0.1" value="1.0" class="w-28 accent-blue-600">
            </div>
            <span class="text-[11px] font-bold text-blue-800 bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200">
              $y = a^x$ 與 $y = \log_a x$ 對稱於直線 $y = x$
            </span>
          </div>
          <div class="flex-1 bg-white rounded-xl border border-slate-200 p-2 flex items-center justify-center min-h-0 shadow-inner">
            <canvas id="lab-sym-canvas" width="580" height="260" class="max-w-full h-auto block"></canvas>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 4：納皮爾對數計算尺模擬器 (化乘除為加減) -->
        <!-- ========================================== -->
        <div id="lab-panel-4" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs text-xs">
            <div class="flex items-center gap-3">
              <span class="font-bold text-slate-700">被乘數 A：<span id="lab-slide-a-val" class="text-blue-600 font-mono font-black">2.0</span></span>
              <input type="range" id="lab-slide-a" min="1.0" max="4.5" step="0.1" value="2.0" class="w-28 accent-blue-600">
              <span class="font-bold text-slate-700 ml-2">乘數 B：<span id="lab-slide-b-val" class="text-amber-600 font-mono font-black">3.0</span></span>
              <input type="range" id="lab-slide-b" min="1.0" max="4.5" step="0.1" value="3.0" class="w-28 accent-amber-600">
            </div>
            <span class="text-[11px] font-bold text-amber-800 bg-amber-50 px-2 py-0.5 rounded-md border border-amber-200">
              長度相加：$\log A + \log B = \log(A \times B)$
            </span>
          </div>
          <div class="flex-1 bg-amber-950/10 rounded-xl border border-amber-700/30 p-2 flex flex-col items-center justify-center min-h-0 shadow-inner space-y-2">
            <canvas id="lab-slide-canvas" width="620" height="180" class="max-w-full h-auto block"></canvas>
            <div id="lab-slide-formula" class="text-xs font-mono font-bold text-slate-800 bg-white px-4 py-1 rounded-lg border border-slate-200"></div>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 5：聲音分貝感官與能量倍率儀 -->
        <!-- ========================================== -->
        <div id="lab-panel-5" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs text-xs">
            <span class="font-bold text-slate-700">
              分貝值 (dB)：<span id="lab-db-val" class="text-purple-600 font-mono font-black text-sm">60</span> dB
              <span class="text-slate-400 font-normal ml-2 text-[11px]">($dB = 10 \log_{10}(I/I_0)$，人耳聽覺對數響度)</span>
            </span>
            <button onclick="playDbDemoTone()" class="px-2.5 py-0.5 rounded bg-purple-600 hover:bg-purple-500 text-white font-bold text-[11px] flex items-center gap-1 shadow-xs">
              <i class="fa-solid fa-volume-high"></i> 試聽此響度
            </button>
          </div>
          <input type="range" id="lab-db-slider" min="0" max="130" step="5" value="60" class="w-full accent-purple-600 cursor-pointer">
          <div class="flex-1 bg-white rounded-xl border border-slate-200 p-3 flex flex-col items-center justify-center min-h-0 shadow-inner space-y-2">
            <canvas id="lab-db-canvas" width="600" height="150" class="max-w-full h-auto block"></canvas>
            <div id="lab-db-desc" class="text-xs font-bold text-slate-700 text-center"></div>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 6：化學酸鹼度 (pH 值) 光譜色階實驗室 -->
        <!-- ========================================== -->
        <div id="lab-panel-6" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs text-xs">
            <span class="font-bold text-slate-700">
              氫離子濃度 $[H^+] = 10^{-x}$：<span id="lab-ph-val" class="text-rose-600 font-mono font-black text-sm">pH 7.0</span>
              <span class="text-slate-400 font-normal ml-2 text-[11px]">($pH = -\log_{10}[H^+]$，負對數色階漸變)</span>
            </span>
            <span id="lab-ph-nature" class="text-[11px] font-bold text-emerald-800 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200">
              中性水溶液
            </span>
          </div>
          <input type="range" id="lab-ph-slider" min="0" max="14" step="0.2" value="7.0" class="w-full accent-emerald-600 cursor-pointer">
          <div class="flex-1 bg-white rounded-xl border border-slate-200 p-3 flex flex-col sm:flex-row items-center justify-around min-h-0 shadow-inner gap-4">
            <!-- 試管動態液體 SVG -->
            <div id="lab-tube-container" class="w-36 flex items-center justify-center"></div>
            <!-- 化學資訊卡 -->
            <div id="lab-ph-info" class="flex-1 max-w-md space-y-1.5 text-xs"></div>
          </div>
        </div>

        <!-- ========================================== -->
        <!-- 實驗 7：大數首數尾數顯微鏡 -->
        <!-- ========================================== -->
        <div id="lab-panel-7" class="hidden w-full max-w-4xl flex flex-col h-full justify-between space-y-2">
          <div class="flex flex-wrap items-center justify-between bg-white px-3 py-1.5 rounded-xl border border-slate-200 shadow-xs text-xs">
            <div class="flex items-center gap-2">
              <span class="font-bold text-slate-700">底數：</span>
              <select id="lab-mag-base" onchange="updateMagnitudeLab()" class="bg-slate-100 border border-slate-300 rounded px-2 py-0.5 font-bold">
                <option value="2" selected>2</option>
                <option value="3">3</option>
                <option value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
              </select>
              <span class="font-bold text-slate-700 ml-2">次方：</span>
              <input type="range" id="lab-mag-exp" min="5" max="80" step="1" value="30" oninput="updateMagnitudeLab()" class="w-28 accent-indigo-600">
              <span id="lab-mag-exp-val" class="font-mono font-bold text-indigo-700">30</span>
            </div>
            <span class="text-[11px] font-bold text-indigo-800 bg-indigo-50 px-2 py-0.5 rounded-md border border-indigo-200">
              首數決定整數位數 ‧ 尾數決定首位數字
            </span>
          </div>
          <div class="flex-1 bg-white rounded-xl border border-slate-200 p-3 flex flex-col items-center justify-between min-h-0 shadow-inner space-y-2">
            <canvas id="lab-mag-canvas" width="600" height="120" class="max-w-full h-auto block"></canvas>
            <div id="lab-mag-result" class="w-full bg-slate-50 p-2.5 rounded-xl border border-slate-200 text-xs"></div>
          </div>
        </div>

      </main>

      <!-- 實驗室超薄頁尾 -->
      <footer class="h-7 sm:h-8 px-4 bg-slate-100 border-t border-slate-200 flex items-center justify-between text-[10px] text-slate-500 shrink-0">
        <span class="flex items-center gap-1.5">
          <i class="fa-solid fa-atom text-emerald-600 text-xs"></i>
          <span>阿笠博士動態科學實驗室 ‧ 7 大對數核心概念直觀探索</span>
        </span>
        <span class="font-mono text-slate-400 hidden sm:inline">
          INTERACTIVE SIMULATOR READY ‧ 100% NO SCROLLBAR
        </span>
      </footer>

    </div>
  </div>
"""

LAB_JS_CODE = r"""
// =========================================================================
// 阿笠博士 7 大動態數理實驗室核心 JavaScript 引擎
// =========================================================================

let currentLabTab = 1;

function openLabModal(tab = 1) {
    recordInteraction();
    const modal = document.getElementById('lab-modal');
    if (modal) {
        modal.classList.remove('hidden');
    }
    switchLabTab(tab);
}

function closeLabModal() {
    const modal = document.getElementById('lab-modal');
    if (modal) modal.classList.add('hidden');
}

function switchLabTab(tabIdx) {
    currentLabTab = tabIdx;
    for (let i = 1; i <= 7; i++) {
        const tab = document.getElementById(`lab-tab-${i}`);
        const panel = document.getElementById(`lab-panel-${i}`);
        if (tab && panel) {
            if (i === tabIdx) {
                tab.className = 'lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-emerald-700 text-white shadow-xs';
                panel.classList.remove('hidden');
            } else {
                tab.className = 'lab-nav-btn px-2.5 py-1 rounded-lg text-xs font-black transition-all flex items-center gap-1 whitespace-nowrap bg-white text-slate-600 hover:bg-slate-200';
                panel.classList.add('hidden');
            }
        }
    }

    if (tabIdx === 1) renderLogCurveLab();
    if (tabIdx === 2) renderEarthquakeLab();
    if (tabIdx === 3) renderSymmetryLab();
    if (tabIdx === 4) renderSlideRuleLab();
    if (tabIdx === 5) renderDecibelLab();
    if (tabIdx === 6) renderPhLab();
    if (tabIdx === 7) updateMagnitudeLab();
}

// -------------------------------------------------------------
// 實驗 1：底數形變
// -------------------------------------------------------------
function renderLogCurveLab() {
    const container = document.getElementById('lab-curve-svg-container');
    const valText = document.getElementById('lab-base-val');
    if (valText) valText.innerText = currentLabBase.toFixed(1);
    if (!container) return;

    const a = currentLabBase;
    const isIncreasing = (a > 1);
    const points = [];
    const originX = 50;
    const originY = 120;
    const scaleX = 35;
    const scaleY = 35;

    for (let x = 0.15; x <= 8.5; x += 0.15) {
        const y = Math.log(x) / Math.log(a);
        const svgX = originX + x * scaleX;
        const svgY = originY - y * scaleY;
        if (svgY >= 10 && svgY <= 230) {
            points.push(`${svgX.toFixed(1)},${svgY.toFixed(1)}`);
        }
    }
    const pathD = points.length > 0 ? `M ${points.join(' L ')}` : '';

    container.innerHTML = `
        <svg viewBox="0 0 380 240" class="w-full h-full overflow-visible">
            <line x1="20" y1="120" x2="360" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="50" y1="230" x2="50" y2="20" stroke="#94a3b8" stroke-width="1.5"/>
            <text x="350" y="115" class="text-xs fill-slate-500 font-serif">x</text>
            <text x="56" y="25" class="text-xs fill-slate-500 font-serif">y</text>
            <text x="36" y="135" class="text-xs fill-slate-500 font-serif">O</text>
            <line x1="50" y1="20" x2="50" y2="230" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="${originX + 1 * scaleX}" cy="${originY}" r="4" fill="#2563eb"/>
            <text x="${originX + 1 * scaleX}" y="${originY - 8}" text-anchor="middle" class="text-[11px] font-bold fill-blue-600">(1, 0)</text>
            <path d="${pathD}" fill="none" stroke="${isIncreasing ? '#2563eb' : '#dc2626'}" stroke-width="3"/>
            <foreignObject x="175" y="15" width="195" height="95">
                <div xmlns="http://www.w3.org/1999/xhtml" class="bg-white/95 p-2 rounded-xl border ${isIncreasing ? 'border-blue-200' : 'border-rose-200'} shadow-md">
                    <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                        <div class="text-sm font-bold ${isIncreasing ? 'text-blue-800' : 'text-rose-800'}">
                            $y = \\log_{${a.toFixed(1)}} x$
                        </div>
                        <span class="text-[10px] font-black px-1.5 py-0.2 rounded ${isIncreasing ? 'bg-blue-100 text-blue-700' : 'bg-rose-100 text-rose-700'}">
                            ${isIncreasing ? '嚴格遞增' : '嚴格遞減'}
                        </span>
                    </div>
                    <div class="text-[11px] text-slate-600 mt-1">漸近線：$x = 0$（y軸）</div>
                    <div class="text-[11px] text-slate-500">恆過定點：$(1, 0)$</div>
                </div>
            </foreignObject>
        </svg>
    `;
    if (window.renderMathInElement) renderMathInElement(container, { delimiters: [{left: '$', right: '$', display: false}] });
}

// -------------------------------------------------------------
// 實驗 2：芮氏地震
// -------------------------------------------------------------
function renderEarthquakeLab() {
    const M = currentEarthquakeM;
    const logE = 4.8 + 1.5 * M;
    const valText = document.getElementById('lab-eq-val');
    const resText = document.getElementById('lab-eq-result');
    if (valText) valText.innerText = M.toFixed(1);

    const canvas = document.getElementById('lab-eq-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // 繪製地震能量條
        const maxLog = 4.8 + 1.5 * 9.0;
        const minLog = 4.8 + 1.5 * 3.0;
        const pct = (logE - minLog) / (maxLog - minLog);

        ctx.fillStyle = '#f1f5f9';
        ctx.fillRect(40, 50, canvas.width - 80, 24);
        
        const grad = ctx.createLinearGradient(40, 0, canvas.width - 40, 0);
        grad.addColorStop(0, '#3b82f6');
        grad.addColorStop(0.5, '#f59e0b');
        grad.addColorStop(1, '#ef4444');
        ctx.fillStyle = grad;
        ctx.fillRect(40, 50, (canvas.width - 80) * pct, 24);

        // 刻度
        ctx.fillStyle = '#64748b';
        ctx.font = 'bold 10px monospace';
        for (let m = 3; m <= 9; m++) {
            const p = (m - 3) / 6;
            const x = 40 + (canvas.width - 80) * p;
            ctx.beginPath();
            ctx.moveTo(x, 74);
            ctx.lineTo(x, 82);
            ctx.stroke();
            ctx.fillText(`M${m}`, x - 8, 95);
        }
    }

    if (resText) {
        const energyTimes = Math.pow(10, 1.5 * (M - 5.0));
        resText.innerHTML = `
            <div class="text-xs font-bold text-slate-800">
                規模 ${M.toFixed(1)} 釋放能量約為規模 5.0 的 <span class="text-rose-600 font-mono text-sm">${energyTimes >= 1 ? Math.round(energyTimes).toLocaleString() : energyTimes.toFixed(3)}</span> 倍！
            </div>
            <div class="text-[11px] text-slate-500 mt-0.5">
                公式：$\\log_{10} E = 4.8 + 1.5M$，規模每多 1 級，能量差 $10^{1.5} \\approx 31.6$ 倍；每多 2 級，能量差 $10^3 = 1000$ 倍！
            </div>
        `;
        if (window.renderMathInElement) renderMathInElement(resText, { delimiters: [{left: '$', right: '$', display: false}] });
    }
}

// -------------------------------------------------------------
// 實驗 3：指對數鏡射對稱
// -------------------------------------------------------------
let symBase = 2.0;
let symX = 1.0;

function renderSymmetryLab() {
    const canvas = document.getElementById('lab-sym-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const cx = canvas.width / 2;
    const cy = canvas.height / 2;
    const scale = 36;

    // 網格與軸
    ctx.strokeStyle = '#e2e8f0';
    ctx.lineWidth = 1;
    for (let x = -7; x <= 7; x++) {
        ctx.beginPath();
        ctx.moveTo(cx + x * scale, 0);
        ctx.lineTo(cx + x * scale, canvas.height);
        ctx.stroke();
    }
    for (let y = -4; y <= 4; y++) {
        ctx.beginPath();
        ctx.moveTo(0, cy - y * scale);
        ctx.lineTo(canvas.width, cy - y * scale);
        ctx.stroke();
    }

    // 坐標軸
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(20, cy); ctx.lineTo(canvas.width - 20, cy);
    ctx.moveTo(cx, canvas.height - 15); ctx.lineTo(cx, 15);
    ctx.stroke();

    // 對稱軸 y = x (虛線)
    ctx.strokeStyle = '#94a3b8';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(cx - 130, cy + 130);
    ctx.lineTo(cx + 130, cy - 130);
    ctx.stroke();
    ctx.setLineDash([]);

    // 1. 繪製指數曲線 y = a^x (藍色)
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    for (let x = -4; x <= 3; x += 0.1) {
        const y = Math.pow(symBase, x);
        const px = cx + x * scale;
        const py = cy - y * scale;
        if (x === -4) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 2. 繪製對數曲線 y = log_a x (紅色)
    ctx.strokeStyle = '#ef4444';
    ctx.beginPath();
    for (let x = 0.05; x <= 7; x += 0.1) {
        const y = Math.log(x) / Math.log(symBase);
        const px = cx + x * scale;
        const py = cy - y * scale;
        if (x === 0.05) ctx.moveTo(px, py); else ctx.lineTo(px, py);
    }
    ctx.stroke();

    // 3. 點 P(x, a^x) 與 鏡射點 P'(a^x, x)
    const py1 = Math.pow(symBase, symX);
    const px1 = symX;

    const px2 = py1;
    const py2 = px1;

    const cpx1 = cx + px1 * scale;
    const cpy1 = cy - py1 * scale;
    const cpx2 = cx + px2 * scale;
    const cpy2 = cy - py2 * scale;

    // 垂直平分連線
    ctx.strokeStyle = '#f59e0b';
    ctx.lineWidth = 1.5;
    ctx.setLineDash([2, 2]);
    ctx.beginPath();
    ctx.moveTo(cpx1, cpy1);
    ctx.lineTo(cpx2, cpy2);
    ctx.stroke();
    ctx.setLineDash([]);

    // 點 P
    ctx.fillStyle = '#2563eb';
    ctx.beginPath(); ctx.arc(cpx1, cpy1, 5, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#1e3a8a';
    ctx.font = 'bold 11px sans-serif';
    ctx.fillText(`P(${px1.toFixed(1)}, ${py1.toFixed(1)})`, cpx1 + 8, cpy1 - 5);

    // 點 P'
    ctx.fillStyle = '#ef4444';
    ctx.beginPath(); ctx.arc(cpx2, cpy2, 5, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#991b1b';
    ctx.fillText(`P'(${px2.toFixed(1)}, ${py2.toFixed(1)})`, cpx2 + 8, cpy2 + 15);
}

// -------------------------------------------------------------
// 實驗 4：納皮爾對數計算尺
// -------------------------------------------------------------
let slideA = 2.0;
let slideB = 3.0;

function renderSlideRuleLab() {
    const canvas = document.getElementById('lab-slide-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const startX = 40;
    const totalW = canvas.width - 80;

    // 下尺 (固定 D 尺)
    ctx.fillStyle = '#fde68a';
    ctx.fillRect(startX, 90, totalW, 45);
    ctx.strokeStyle = '#d97706';
    ctx.lineWidth = 2;
    ctx.strokeRect(startX, 90, totalW, 45);

    // 上尺 (滑動 C 尺，偏移量為 log(slideA))
    const offsetPx = (Math.log10(slideA) / Math.log10(10)) * (totalW * 0.7);
    ctx.fillStyle = '#fed7aa';
    ctx.fillRect(startX + offsetPx, 40, totalW, 45);
    ctx.strokeStyle = '#ea580c';
    ctx.strokeRect(startX + offsetPx, 40, totalW, 45);

    // 繪製下尺刻度 (1 到 10)
    ctx.fillStyle = '#78350f';
    ctx.font = 'bold 11px monospace';
    ctx.textAlign = 'center';
    for (let v = 1; v <= 10; v++) {
        const x = startX + (Math.log10(v) / 1.0) * (totalW * 0.7);
        ctx.beginPath();
        ctx.moveTo(x, 90); ctx.lineTo(x, 105);
        ctx.stroke();
        ctx.fillText(v, x, 122);
    }

    // 繪製上尺刻度 (1 到 10)
    for (let v = 1; v <= 10; v++) {
        const x = startX + offsetPx + (Math.log10(v) / 1.0) * (totalW * 0.7);
        if (x <= startX + offsetPx + totalW) {
            ctx.beginPath();
            ctx.moveTo(x, 70); ctx.lineTo(x, 85);
            ctx.stroke();
            ctx.fillText(v, x, 62);
        }
    }

    // 游標對齊線
    const alignX = startX + offsetPx + (Math.log10(slideB) / 1.0) * (totalW * 0.7);
    ctx.strokeStyle = '#dc2626';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(alignX, 30);
    ctx.lineTo(alignX, 145);
    ctx.stroke();

    const product = slideA * slideB;
    const formulaDiv = document.getElementById('lab-slide-formula');
    if (formulaDiv) {
        formulaDiv.innerHTML = `對數長度相加：$\\log(${slideA.toFixed(1)}) + \\log(${slideB.toFixed(1)}) = \\log(${product.toFixed(1)}) \\implies ${slideA.toFixed(1)} \\times ${slideB.toFixed(1)} = ${product.toFixed(1)}$`;
        if (window.renderMathInElement) renderMathInElement(formulaDiv, { delimiters: [{left: '$', right: '$', display: false}] });
    }
}

// -------------------------------------------------------------
// 實驗 5：聲音分貝感官儀
// -------------------------------------------------------------
let currentDb = 60;

function renderDecibelLab() {
    const valText = document.getElementById('lab-db-val');
    const descText = document.getElementById('lab-db-desc');
    if (valText) valText.innerText = currentDb;

    const canvas = document.getElementById('lab-db-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // 儀表刻度
        const startX = 40;
        const totalW = canvas.width - 80;
        const pct = currentDb / 140;

        ctx.fillStyle = '#f1f5f9';
        ctx.fillRect(startX, 50, totalW, 20);

        const grad = ctx.createLinearGradient(startX, 0, startX + totalW, 0);
        grad.addColorStop(0, '#10b981');
        grad.addColorStop(0.5, '#f59e0b');
        grad.addColorStop(0.85, '#ef4444');
        grad.addColorStop(1, '#7f1d1d');
        ctx.fillStyle = grad;
        ctx.fillRect(startX, 50, totalW * pct, 20);

        // 指針
        ctx.fillStyle = '#0f172a';
        ctx.beginPath();
        ctx.moveTo(startX + totalW * pct, 42);
        ctx.lineTo(startX + totalW * pct - 6, 30);
        ctx.lineTo(startX + totalW * pct + 6, 30);
        ctx.closePath();
        ctx.fill();
    }

    if (descText) {
        const powerRatio = Math.pow(10, currentDb / 10);
        let scene = '正常交談';
        if (currentDb <= 20) scene = '落葉微風聲 / 呼吸聲';
        else if (currentDb <= 40) scene = '圖書館閱覽室 / 輕聲耳語';
        else if (currentDb <= 60) scene = '安靜辦公室 / 正常談話';
        else if (currentDb <= 85) scene = '鬧區街道 / 汽車行駛聲';
        else if (currentDb <= 100) scene = '柴油火車 / 割草機（長時間傷害聽力）';
        else if (currentDb <= 120) scene = '搖滾演唱會前排 / 飛機起飛痛閾！';
        else scene = '噴射引擎極限爆破（耳膜破裂危險）！';

        descText.innerHTML = `
            場景代表：<span class="text-purple-700 font-bold">${scene}</span> ‧ 
            聲波能量強度為基準聽閾之 <span class="font-mono text-rose-600">${powerRatio >= 1e6 ? powerRatio.toExponential(1) : Math.round(powerRatio).toLocaleString()}</span> 倍！
        `;
    }
}

function playDbDemoTone() {
    try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioContext();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        // 將分貝數映射為感知音量 (安全限制在 0.01 到 0.4 之間)
        const vol = Math.min(0.35, Math.max(0.01, (currentDb / 130) * 0.35));
        gain.gain.setValueAtTime(vol, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4);

        osc.frequency.setValueAtTime(440, ctx.currentTime);
        osc.start();
        osc.stop(ctx.currentTime + 0.4);
    } catch (e) {
        console.warn(e);
    }
}

// -------------------------------------------------------------
// 實驗 6：化學 pH 值色階尺
// -------------------------------------------------------------
let currentPh = 7.0;

function renderPhLab() {
    const valText = document.getElementById('lab-ph-val');
    const natureText = document.getElementById('lab-ph-nature');
    const tubeContainer = document.getElementById('lab-tube-container');
    const infoDiv = document.getElementById('lab-ph-info');

    if (valText) valText.innerText = `pH ${currentPh.toFixed(1)}`;

    // 計算廣用試紙顏色
    // pH 1: red(#ef4444), 3: orange(#f97316), 6: yellow(#eab308), 7: green(#22c55e), 9: cyan(#06b6d4), 11: blue(#3b82f6), 14: purple(#9333ea)
    let color = '#22c55e';
    let nature = '中性純水水溶液';
    if (currentPh < 6.8) {
        nature = currentPh <= 2.5 ? '強酸性溶液（胃酸/檸檬汁）' : '弱酸性溶液（咖啡/雨水）';
        const t = currentPh / 7.0;
        color = currentPh < 3 ? '#dc2626' : '#f97316';
    } else if (currentPh > 7.2) {
        nature = currentPh >= 11 ? '強鹼性溶液（漂白水/肥皂水）' : '弱鹼性溶液（小蘇打/海水）';
        color = currentPh > 11 ? '#7e22ce' : '#2563eb';
    }

    if (natureText) {
        natureText.innerText = nature;
        natureText.className = currentPh < 7 ? 'text-[11px] font-bold text-rose-800 bg-rose-50 px-2 py-0.5 rounded-md border border-rose-200' : 'text-[11px] font-bold text-blue-800 bg-blue-50 px-2 py-0.5 rounded-md border border-blue-200';
    }

    if (tubeContainer) {
        tubeContainer.innerHTML = `
            <svg viewBox="0 0 80 140" class="h-32">
                <!-- 試管外框 -->
                <path d="M 20 10 L 20 110 A 20 20 0 0 0 60 110 L 60 10 Z" fill="none" stroke="#94a3b8" stroke-width="3"/>
                <!-- 試管液體 -->
                <path d="M 22 45 L 22 110 A 18 18 0 0 0 58 110 L 58 45 Z" fill="${color}" opacity="0.85"/>
                <!-- 刻度線 -->
                <line x1="20" y1="40" x2="30" y2="40" stroke="#cbd5e1" stroke-width="2"/>
                <line x1="20" y1="65" x2="30" y2="65" stroke="#cbd5e1" stroke-width="2"/>
                <line x1="20" y1="90" x2="30" y2="90" stroke="#cbd5e1" stroke-width="2"/>
            </svg>
        `;
    }

    if (infoDiv) {
        const hConc = Math.pow(10, -currentPh);
        const ohConc = Math.pow(10, -(14 - currentPh));
        infoDiv.innerHTML = `
            <div class="p-2.5 rounded-xl bg-slate-100 border border-slate-200">
                <div class="font-bold text-slate-800 flex justify-between">
                    <span>$[H^+] = 10^{-${currentPh.toFixed(1)}}\\text{ M}$</span>
                    <span class="text-rose-600 font-mono">${hConc.toExponential(2)} M</span>
                </div>
                <div class="font-bold text-slate-600 flex justify-between mt-1">
                    <span>$[OH^-] = 10^{-${(14 - currentPh).toFixed(1)}}\\text{ M}$</span>
                    <span class="text-blue-600 font-mono">${ohConc.toExponential(2)} M</span>
                </div>
            </div>
            <div class="text-[11px] text-slate-500 leading-tight">
                <strong>定義：</strong>$pH = -\\log_{10}[H^+]$。當氫離子濃度越大（如 $10^{-1}$），前面負號使 $pH = 1$（強酸）；負號是為了將極小濃度化為正數指標！
            </div>
        `;
        if (window.renderMathInElement) renderMathInElement(infoDiv, { delimiters: [{left: '$', right: '$', display: false}] });
    }
}

// -------------------------------------------------------------
// 實驗 7：大數首數尾數顯微鏡
// -------------------------------------------------------------
function updateMagnitudeLab() {
    const baseEl = document.getElementById('lab-mag-base');
    const expEl = document.getElementById('lab-mag-exp');
    const expVal = document.getElementById('lab-mag-exp-val');
    const canvas = document.getElementById('lab-mag-canvas');
    const resultDiv = document.getElementById('lab-mag-result');

    if (!baseEl || !expEl) return;
    const b = parseInt(baseEl.value, 10);
    const p = parseInt(expEl.value, 10);
    if (expVal) expVal.innerText = p;

    // 計算常用對數 log10(b^p) = p * log10(b)
    const logVal = p * Math.log10(b);
    const characteristic = Math.floor(logVal); // 首數
    const mantissa = logVal - characteristic; // 尾數 (0 <= alpha < 1)
    const digits = characteristic + 1; // 整數位數

    // 計算最高位數字 (比對 mantissa 與 log10(1..9))
    let leadingDigit = 1;
    for (let d = 1; d <= 9; d++) {
        if (mantissa >= Math.log10(d)) {
            leadingDigit = d;
        }
    }

    if (canvas) {
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const startX = 40;
        const totalW = canvas.width - 80;

        // 尺規底色
        ctx.fillStyle = '#f8fafc';
        ctx.fillRect(startX, 40, totalW, 30);
        ctx.strokeStyle = '#cbd5e1';
        ctx.strokeRect(startX, 40, totalW, 30);

        // 標記 log 1~9 刻度
        ctx.fillStyle = '#475569';
        ctx.font = 'bold 10px monospace';
        ctx.textAlign = 'center';
        for (let d = 1; d <= 9; d++) {
            const lVal = Math.log10(d);
            const x = startX + lVal * totalW;
            ctx.beginPath();
            ctx.moveTo(x, 40); ctx.lineTo(x, 50);
            ctx.stroke();
            ctx.fillText(d, x, 62);
        }

        // 標記尾數指針 (alpha)
        const ptrX = startX + mantissa * totalW;
        ctx.fillStyle = '#dc2626';
        ctx.beginPath();
        ctx.moveTo(ptrX, 35);
        ctx.lineTo(ptrX - 5, 22);
        ctx.lineTo(ptrX + 5, 22);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle = '#dc2626';
        ctx.font = 'bold 11px monospace';
        ctx.fillText(`尾數 α = ${mantissa.toFixed(4)}`, ptrX, 16);
    }

    if (resultDiv) {
        resultDiv.innerHTML = `
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-2">
                <div class="p-2 rounded bg-indigo-50 border border-indigo-200">
                    <span class="text-indigo-900 font-black">① 首數 $n = ${characteristic}$：</span>
                    <span class="text-slate-700">決定整數位數，故 $${b}^{${p}}$ 在十進位制中為 <strong class="text-indigo-700">${digits} 位數</strong>！</span>
                </div>
                <div class="p-2 rounded bg-amber-50 border border-amber-200">
                    <span class="text-amber-900 font-black">② 尾數 $\\alpha \\approx ${mantissa.toFixed(4)}$：</span>
                    <span class="text-slate-700">落於 $\\log ${leadingDigit} \\le \\alpha < \\log ${leadingDigit + 1}$，故最高位數字為 <strong class="text-red-600">${leadingDigit}</strong>！</span>
                </div>
            </div>
            <div class="mt-1.5 text-[11px] text-slate-500 font-mono">
                科學記號精確估算：$${b}^{${p}} = 10^{${logVal.toFixed(4)}} = 10^{${mantissa.toFixed(4)}} \\times 10^{${characteristic}} \\approx ${(Math.pow(10, mantissa)).toFixed(3)} \\times 10^{${characteristic}}$
            </div>
        `;
        if (window.renderMathInElement) renderMathInElement(resultDiv, { delimiters: [{left: '$', right: '$', display: false}] });
    }
}

// -------------------------------------------------------------
// 初始化所有實驗監聽器
// -------------------------------------------------------------
function initLab() {
    const baseSlider = document.getElementById('lab-base-slider');
    if (baseSlider) {
        baseSlider.addEventListener('input', (e) => {
            currentLabBase = parseFloat(e.target.value);
            renderLogCurveLab();
        });
    }

    const eqSlider = document.getElementById('lab-eq-slider');
    if (eqSlider) {
        eqSlider.addEventListener('input', (e) => {
            currentEarthquakeM = parseFloat(e.target.value);
            renderEarthquakeLab();
        });
    }

    const symBaseEl = document.getElementById('lab-sym-base-slider');
    const symXEl = document.getElementById('lab-sym-x-slider');
    if (symBaseEl) {
        symBaseEl.addEventListener('input', (e) => {
            symBase = parseFloat(e.target.value);
            const val = document.getElementById('lab-sym-base-val');
            if (val) val.innerText = symBase.toFixed(1);
            renderSymmetryLab();
        });
    }
    if (symXEl) {
        symXEl.addEventListener('input', (e) => {
            symX = parseFloat(e.target.value);
            const val = document.getElementById('lab-sym-x-val');
            if (val) val.innerText = symX.toFixed(1);
            renderSymmetryLab();
        });
    }

    const slideAEl = document.getElementById('lab-slide-a');
    const slideBEl = document.getElementById('lab-slide-b');
    if (slideAEl) {
        slideAEl.addEventListener('input', (e) => {
            slideA = parseFloat(e.target.value);
            const val = document.getElementById('lab-slide-a-val');
            if (val) val.innerText = slideA.toFixed(1);
            renderSlideRuleLab();
        });
    }
    if (slideBEl) {
        slideBEl.addEventListener('input', (e) => {
            slideB = parseFloat(e.target.value);
            const val = document.getElementById('lab-slide-b-val');
            if (val) val.innerText = slideB.toFixed(1);
            renderSlideRuleLab();
        });
    }

    const dbSlider = document.getElementById('lab-db-slider');
    if (dbSlider) {
        dbSlider.addEventListener('input', (e) => {
            currentDb = parseInt(e.target.value, 10);
            renderDecibelLab();
        });
    }

    const phSlider = document.getElementById('lab-ph-slider');
    if (phSlider) {
        phSlider.addEventListener('input', (e) => {
            currentPh = parseFloat(e.target.value);
            renderPhLab();
        });
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLab);
} else {
    initLab();
}
"""


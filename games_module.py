# -*- coding: utf-8 -*-
"""
games_module.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
名偵探柯南數理探案 ‧ 5 大對數線上對戰競技場（Game Arena）模組
包含 5 大精選遊戲（單人闖關 + 雙人同屏競速對戰）：
1. 骨牌連鎖消消樂 (Domino Match Duel)
2. 密室機關密碼盤 (Cryptex Escape Room)
3. 迷宮雷達尋路戰 (Maze Runner)
4. 踢力增強鞋射擊防禦戰 (Log Target Defense)
5. 芮氏地震能量天平 (Energy Balancer Duel)
內建 Web Audio API 音效合成引擎，100% 離線免外部資源。
"""

GAMES_MODAL_HTML = r"""
  <!-- 彈窗模組 7：5大對數對戰電玩競技場 (Game Arena) -->
  <div id="game-arena-modal" class="hidden fixed inset-0 z-50 bg-slate-950/90 backdrop-blur-md flex items-center justify-center p-2 sm:p-4">
    <div class="bg-slate-900 rounded-3xl w-full max-w-6xl h-[92vh] flex flex-col shadow-2xl border-4 border-amber-500 overflow-hidden text-white select-none">
      
      <!-- 頂部競技場標題與控制列 -->
      <header class="h-16 px-4 sm:px-6 bg-gradient-to-r from-blue-950 via-slate-900 to-red-950 border-b-2 border-amber-500 flex items-center justify-between shrink-0">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-amber-400 to-red-600 flex items-center justify-center text-slate-950 font-black text-xl shadow-lg shadow-amber-500/20">
            <i class="fa-solid fa-gamepad text-white"></i>
          </div>
          <div>
            <div class="flex items-center gap-2">
              <h2 class="text-base sm:text-lg font-black text-amber-300 tracking-tight flex items-center gap-1.5">
                名偵探柯南 ‧ 5大對數對戰電玩競技場
              </h2>
              <span class="px-2 py-0.5 rounded-full bg-red-600 text-white text-[10px] font-extrabold uppercase animate-pulse">Live Arena</span>
            </div>
            <p class="text-[11px] text-slate-300 hidden sm:block">
              對數定義速算 ‧ 換底連鎖 ‧ 密室逃脫 ‧ 防禦射擊 ‧ 芮氏能量天平
            </p>
          </div>
        </div>

        <!-- 音效與關閉按鈕 -->
        <div class="flex items-center gap-2 sm:gap-3">
          <button id="game-audio-toggle" onclick="toggleGameAudio()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-amber-400 font-bold text-xs flex items-center gap-1.5 border border-slate-700 transition-all" title="切換遊戲音效">
            <i id="game-audio-icon" class="fa-solid fa-volume-high"></i>
            <span class="hidden md:inline">音效: 開</span>
          </button>
          <button onclick="closeGameArenaModal()" class="px-3 py-1.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-bold text-xs flex items-center gap-1.5 shadow-md shadow-red-900/50 transition-all" title="返回學習卡總覽 (按 ESC 鍵)">
            <i class="fa-solid fa-xmark"></i>
            <span>關閉競技場 (ESC)</span>
          </button>
        </div>
      </header>

      <!-- 5大遊戲分頁選單列 -->
      <nav class="bg-slate-950/80 px-3 sm:px-6 py-2 border-b border-slate-800 flex items-center gap-1.5 sm:gap-2 overflow-x-auto shrink-0 scrollbar-none">
        <button onclick="switchGame(1)" id="game-tab-1" class="game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-blue-700 text-white shadow-md">
          <i class="fa-solid fa-puzzle-piece text-amber-300"></i>
          <span>① 骨牌連鎖消消樂</span>
        </button>
        <button onclick="switchGame(2)" id="game-tab-2" class="game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white">
          <i class="fa-solid fa-lock text-amber-400"></i>
          <span>② 密室機關密碼盤</span>
        </button>
        <button onclick="switchGame(3)" id="game-tab-3" class="game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white">
          <i class="fa-solid fa-compass text-emerald-400"></i>
          <span>③ 迷宮雷達尋路戰</span>
        </button>
        <button onclick="switchGame(4)" id="game-tab-4" class="game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white">
          <i class="fa-solid fa-futbol text-rose-400"></i>
          <span>④ 增強鞋射擊防禦戰</span>
        </button>
        <button onclick="switchGame(5)" id="game-tab-5" class="game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white">
          <i class="fa-solid fa-scale-balanced text-amber-400"></i>
          <span>⑤ 芮氏地震能量天平</span>
        </button>
      </nav>

      <!-- 遊戲內容區 (五合一視窗容器) -->
      <main class="flex-1 bg-slate-900 p-3 sm:p-5 overflow-y-auto relative flex flex-col items-center justify-start">
        
        <!-- ============================================== -->
        <!-- 遊戲 1：骨牌連鎖消消樂 (Domino Match Duel) -->
        <!-- ============================================== -->
        <div id="game-panel-1" class="w-full max-w-5xl flex flex-col h-full space-y-3">
          <!-- 遊戲資訊與模式切換列 -->
          <div class="bg-slate-800/90 rounded-2xl p-3 border border-slate-700 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-lg bg-blue-900 text-blue-200 font-bold">遊戲模式：</span>
              <button onclick="setGame1Mode('1p')" id="g1-mode-1p-btn" class="px-3 py-1 rounded-lg bg-blue-600 text-white font-black">單人極速闖關</button>
              <button onclick="setGame1Mode('2p')" id="g1-mode-2p-btn" class="px-3 py-1 rounded-lg bg-slate-700 text-slate-300 hover:bg-slate-600 font-black">雙人同屏對決 (P1 vs P2)</button>
            </div>
            <div class="flex items-center gap-4 font-mono">
              <div class="text-amber-300 font-bold">倒數：<span id="g1-timer" class="text-lg text-white font-black">60</span>s</div>
              <div class="text-emerald-400 font-bold">連擊：<span id="g1-combo" class="text-lg text-white font-black">0</span>x</div>
              <div class="text-rose-400 font-bold">破案積分：<span id="g1-score" class="text-lg text-white font-black">0</span></div>
            </div>
            <button onclick="restartGame1()" class="px-3 py-1.5 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-black transition-all flex items-center gap-1.5 shadow-sm">
              <i class="fa-solid fa-rotate-right"></i> 重新開始
            </button>
          </div>

          <!-- 遊戲指引提示 -->
          <div class="text-xs text-slate-400 bg-slate-950/40 px-3 py-1.5 rounded-xl border border-slate-800 flex items-center justify-between">
            <span><i class="fa-solid fa-lightbulb text-amber-400 mr-1"></i> 點選左欄「對數算式牌」與右欄「數值解」進行配對消消樂，連續正確觸發 Combo 積分狂飆！</span>
            <span id="g1-status-msg" class="text-amber-300 font-bold">準備就緒，請點選卡牌！</span>
          </div>

          <!-- 遊戲卡牌主要舞台 (單人 / 雙人對決) -->
          <div id="g1-board" class="flex-1 min-h-[360px] grid grid-cols-2 sm:grid-cols-4 md:grid-cols-6 gap-2.5 p-2 bg-slate-950/60 rounded-2xl border border-slate-800 overflow-y-auto">
            <!-- 由 JS 動態生成骨牌 -->
          </div>
        </div>

        <!-- ============================================== -->
        <!-- 遊戲 2：密室機關密碼盤 (Cryptex Escape Room) -->
        <!-- ============================================== -->
        <div id="game-panel-2" class="hidden w-full max-w-4xl flex flex-col h-full space-y-4">
          <!-- 關卡進度與逃脫計時 -->
          <div class="bg-slate-800/90 rounded-2xl p-3 border border-slate-700 flex items-center justify-between text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-lg bg-amber-500 text-slate-950 font-black">阿笠博士的機關密碼盒</span>
              <span class="text-slate-300 font-bold">目前進度：第 <span id="g2-stage-idx" class="text-amber-400 font-black text-sm">1</span> / 4 道機關鎖</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="text-red-400 font-bold">逃脫剩餘時間：<span id="g2-timer" class="font-mono text-base font-black text-white">90</span> 秒</span>
              <button onclick="restartGame2()" class="px-3 py-1 rounded-lg bg-slate-700 hover:bg-slate-600 text-white font-bold">重新鎖定</button>
            </div>
          </div>

          <!-- 密碼謎題卷宗 -->
          <div class="bg-slate-950/80 p-5 rounded-2xl border-2 border-amber-500/60 shadow-xl space-y-3">
            <div class="flex items-center justify-between">
              <span id="g2-puzzle-badge" class="px-3 py-0.5 rounded-full bg-blue-900 text-amber-300 text-xs font-mono font-bold">STAGE 1 LOCK</span>
              <span class="text-xs text-slate-400">解出題目後，請撥動下方 3 個金屬密碼輪</span>
            </div>
            <div id="g2-puzzle-text" class="text-sm sm:text-base font-bold text-slate-100 py-2 leading-relaxed">
              題目載入中...
            </div>
            <div id="g2-puzzle-hint" class="text-xs text-amber-300/90 bg-amber-950/40 p-2.5 rounded-xl border border-amber-500/30">
              提示情報載入中...
            </div>
          </div>

          <!-- 3D 質感轉輪密碼盤 (Cryptex Dials) -->
          <div class="flex-1 flex flex-col items-center justify-center p-4 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-2xl border border-slate-800">
            <div class="text-xs font-bold text-slate-400 mb-4 tracking-wider uppercase">CRYPTEXT MECHANICAL DIALS</div>
            
            <div class="flex items-center gap-4 sm:gap-8">
              <!-- 輪盤 1 -->
              <div class="flex flex-col items-center space-y-2">
                <button onclick="changeG2Dial(0, 1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-up"></i></button>
                <div id="g2-dial-0" class="w-16 h-20 rounded-2xl bg-gradient-to-b from-amber-600 via-yellow-400 to-amber-700 text-slate-950 flex items-center justify-center font-mono font-black text-3xl shadow-2xl border-2 border-white/60">0</div>
                <button onclick="changeG2Dial(0, -1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-down"></i></button>
                <span class="text-[10px] text-slate-400">百位/首數</span>
              </div>

              <!-- 輪盤 2 -->
              <div class="flex flex-col items-center space-y-2">
                <button onclick="changeG2Dial(1, 1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-up"></i></button>
                <div id="g2-dial-1" class="w-16 h-20 rounded-2xl bg-gradient-to-b from-amber-600 via-yellow-400 to-amber-700 text-slate-950 flex items-center justify-center font-mono font-black text-3xl shadow-2xl border-2 border-white/60">0</div>
                <button onclick="changeG2Dial(1, -1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-down"></i></button>
                <span class="text-[10px] text-slate-400">十位/值</span>
              </div>

              <!-- 輪盤 3 -->
              <div class="flex flex-col items-center space-y-2">
                <button onclick="changeG2Dial(2, 1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-up"></i></button>
                <div id="g2-dial-2" class="w-16 h-20 rounded-2xl bg-gradient-to-b from-amber-600 via-yellow-400 to-amber-700 text-slate-950 flex items-center justify-center font-mono font-black text-3xl shadow-2xl border-2 border-white/60">0</div>
                <button onclick="changeG2Dial(2, -1)" class="w-12 h-8 rounded-lg bg-slate-800 hover:bg-amber-500 hover:text-slate-950 text-white font-black text-sm transition-all"><i class="fa-solid fa-chevron-down"></i></button>
                <span class="text-[10px] text-slate-400">個位/值</span>
              </div>
            </div>

            <!-- 解鎖按鈕與回饋狀態 -->
            <div class="mt-6 flex flex-col items-center gap-2">
              <button onclick="submitG2Unlock()" class="px-8 py-3 rounded-2xl bg-gradient-to-r from-red-600 to-amber-500 hover:from-red-500 hover:to-amber-400 text-white font-black text-sm sm:text-base shadow-xl shadow-red-900/40 flex items-center gap-2 transition-all transform active:scale-95">
                <i class="fa-solid fa-key text-amber-200"></i>
                <span>轉動並驗證密碼解鎖</span>
              </button>
              <div id="g2-feedback" class="text-xs font-bold min-h-[20px] text-slate-400">
                請轉動數字輪盤後點擊解鎖
              </div>
            </div>
          </div>
        </div>

        <!-- ============================================== -->
        <!-- 遊戲 3：迷宮雷達尋路戰 (Maze Runner) -->
        <!-- ============================================== -->
        <div id="game-panel-3" class="hidden w-full max-w-4xl flex flex-col h-full space-y-3">
          <!-- 迷宮情報列 -->
          <div class="bg-slate-800/90 rounded-2xl p-3 border border-slate-700 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-lg bg-emerald-700 text-emerald-100 font-black">迷宮逃脫情報</span>
              <span class="text-slate-300 font-bold">層數：第 <span id="g3-floor" class="text-emerald-400 font-black">1</span> / 5 層</span>
            </div>
            <!-- 雷達目標值提示 -->
            <div class="flex items-center gap-2 bg-slate-950 px-3 py-1 rounded-xl border border-emerald-500/40 animate-pulse">
              <i class="fa-solid fa-radar text-emerald-400"></i>
              <span class="text-slate-300 font-bold">徽章雷達暗號目標值：</span>
              <span id="g3-target-val" class="font-mono text-base font-black text-amber-400">3</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="text-rose-400 font-bold">體力：<span id="g3-hp" class="text-base font-black">❤️❤️❤️</span></span>
              <button onclick="restartGame3()" class="px-3 py-1 rounded-lg bg-slate-700 hover:bg-slate-600 text-white font-bold">重置迷宮</button>
            </div>
          </div>

          <!-- 迷宮 Canvas 畫布與虛擬十字方向盤 -->
          <div class="flex-1 flex flex-col md:flex-row items-center justify-center gap-4 bg-slate-950 p-4 rounded-2xl border border-slate-800 min-h-[360px]">
            <div class="relative flex items-center justify-center">
              <canvas id="g3-canvas" width="400" height="320" class="bg-slate-900 rounded-xl border-2 border-slate-700 shadow-2xl"></canvas>
            </div>

            <!-- 控制說明與行動版虛擬十字鍵 -->
            <div class="flex flex-col items-center justify-center space-y-3">
              <div class="text-[11px] text-slate-400 text-center max-w-[200px] leading-relaxed">
                鍵盤按 <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-600 text-white font-mono">↑</kbd> <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-600 text-white font-mono">↓</kbd> <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-600 text-white font-mono">←</kbd> <kbd class="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-600 text-white font-mono">→</kbd> 控制柯南移動，避開巡邏警衛，走進結果等於雷達目標值的傳送門！
              </div>
              
              <!-- 虛擬按鍵 (觸控手機平板專用) -->
              <div class="grid grid-cols-3 gap-1.5 w-36">
                <div></div>
                <button onclick="moveG3('up')" class="h-10 rounded-xl bg-slate-800 hover:bg-emerald-600 active:bg-emerald-500 text-white font-black text-sm flex items-center justify-center border border-slate-700 shadow-md"><i class="fa-solid fa-arrow-up"></i></button>
                <div></div>
                <button onclick="moveG3('left')" class="h-10 rounded-xl bg-slate-800 hover:bg-emerald-600 active:bg-emerald-500 text-white font-black text-sm flex items-center justify-center border border-slate-700 shadow-md"><i class="fa-solid fa-arrow-left"></i></button>
                <button onclick="moveG3('down')" class="h-10 rounded-xl bg-slate-800 hover:bg-emerald-600 active:bg-emerald-500 text-white font-black text-sm flex items-center justify-center border border-slate-700 shadow-md"><i class="fa-solid fa-arrow-down"></i></button>
                <button onclick="moveG3('right')" class="h-10 rounded-xl bg-slate-800 hover:bg-emerald-600 active:bg-emerald-500 text-white font-black text-sm flex items-center justify-center border border-slate-700 shadow-md"><i class="fa-solid fa-arrow-right"></i></button>
              </div>
            </div>
          </div>
        </div>

        <!-- ============================================== -->
        <!-- 遊戲 4：踢力增強鞋射擊防禦戰 (Log Target Defense) -->
        <!-- ============================================== -->
        <div id="game-panel-4" class="hidden w-full max-w-4xl flex flex-col h-full space-y-3">
          <!-- 戰場抬頭顯示列 -->
          <div class="bg-slate-800/90 rounded-2xl p-3 border border-slate-700 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-lg bg-red-700 text-white font-black">阿笠博士超強力腳力增強鞋</span>
              <span class="text-slate-300 font-bold">波次：WAVE <span id="g4-wave" class="text-amber-400 font-black">1</span></span>
            </div>
            <div class="flex items-center gap-4 font-mono">
              <div class="text-rose-400 font-bold">眼鏡防禦力：<span id="g4-hp" class="text-base text-white font-black">100</span>%</div>
              <div class="text-amber-300 font-bold">擊落數：<span id="g4-kills" class="text-base text-white font-black">0</span></div>
              <div class="text-emerald-400 font-bold">防禦積分：<span id="g4-score" class="text-base text-white font-black">0</span></div>
            </div>
            <button onclick="restartGame4()" class="px-3 py-1 rounded-lg bg-slate-700 hover:bg-slate-600 text-white font-bold">重新出擊</button>
          </div>

          <!-- 射擊主畫布 (Canvas) -->
          <div class="flex-1 relative bg-slate-950 rounded-2xl border-2 border-red-950 overflow-hidden min-h-[340px] flex items-center justify-center">
            <canvas id="g4-canvas" width="600" height="340" class="w-full h-full block"></canvas>
            
            <!-- 遊戲結束/開始覆蓋層 -->
            <div id="g4-overlay" class="hidden absolute inset-0 bg-slate-950/85 backdrop-blur-sm flex flex-col items-center justify-center p-6 text-center z-20">
              <div class="text-3xl font-black text-rose-500 mb-2" id="g4-gameover-title">防線被突破！</div>
              <p class="text-xs text-slate-300 mb-4" id="g4-gameover-desc">偵探眼鏡能量耗盡，請重新整裝再戰！</p>
              <button onclick="startGame4()" class="px-6 py-2.5 rounded-xl bg-red-600 hover:bg-red-500 text-white font-black text-sm shadow-lg shadow-red-900/50 transition-all">
                再次啟動腳力增強鞋 (Enter)
              </button>
            </div>
          </div>

          <!-- 快速踢擊數值按鈕發射盤 -->
          <div class="bg-slate-800/80 p-2.5 rounded-2xl border border-slate-700 flex flex-wrap items-center justify-center gap-2">
            <span class="text-xs font-bold text-amber-300 mr-2 flex items-center gap-1">
              <i class="fa-solid fa-crosshairs"></i> 選擇數值踢出光速足球：
            </span>
            <button onclick="fireG4Val(-2)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">-2</button>
            <button onclick="fireG4Val(-1)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">-1</button>
            <button onclick="fireG4Val(0)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">0</button>
            <button onclick="fireG4Val(1)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">1</button>
            <button onclick="fireG4Val(2)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">2</button>
            <button onclick="fireG4Val(3)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">3</button>
            <button onclick="fireG4Val(4)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">4</button>
            <button onclick="fireG4Val(5)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">5</button>
            <button onclick="fireG4Val(0.5)" class="px-3 py-1.5 rounded-xl bg-slate-700 hover:bg-red-600 active:scale-95 text-white font-mono font-black text-sm border border-slate-600 shadow-sm">1/2</button>
          </div>
        </div>

        <!-- ============================================== -->
        <!-- 遊戲 5：芮氏地震能量天平 (Earthquake Richter Balancer) -->
        <!-- ============================================== -->
        <div id="game-panel-5" class="hidden w-full max-w-4xl flex flex-col h-full space-y-3">
          <!-- 天平控制抬頭 -->
          <div class="bg-slate-800/90 rounded-2xl p-3 border border-slate-700 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div class="flex items-center gap-2">
              <span class="px-2.5 py-1 rounded-lg bg-amber-600 text-slate-950 font-black">芮氏地震能量平衡大師</span>
              <span class="text-slate-300 font-bold">關卡：第 <span id="g5-level" class="text-amber-400 font-black">1</span> / 5 關</span>
            </div>
            <div class="text-xs text-amber-300 font-mono">
              能量公式：$\log_{10} E = 4.8 + 1.5M$（差 1 級差 $10^{1.5} \approx 31.6$ 倍；差 2 級差 $10^3 = 1000$ 倍）
            </div>
            <button onclick="restartGame5()" class="px-3 py-1 rounded-lg bg-slate-700 hover:bg-slate-600 text-white font-bold">新題目</button>
          </div>

          <!-- 天平物理 Canvas 渲染區 -->
          <div class="flex-1 bg-slate-950 rounded-2xl border border-slate-800 p-3 flex flex-col items-center justify-center relative min-h-[300px]">
            <canvas id="g5-canvas" width="640" height="260" class="w-full max-w-2xl h-auto block"></canvas>
            
            <!-- 實時狀態面板 -->
            <div class="mt-2 text-center">
              <div id="g5-balance-status" class="text-xs font-bold text-slate-300">
                請在右側盤加入等效倍率砝碼，使指針回正平衡！
              </div>
            </div>
          </div>

          <!-- 砝碼放置操作盤 -->
          <div class="bg-slate-800/90 p-4 rounded-2xl border border-slate-700 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="text-xs space-y-1">
              <div class="text-slate-300 font-bold">
                目標：平衡左側 <span id="g5-left-target" class="text-rose-400 font-black font-mono">規模 7.0 地震</span>
              </div>
              <div class="text-slate-400">
                右盤目前放了：<span id="g5-right-weight" class="text-amber-400 font-black font-mono">0</span> 個 <span id="g5-right-type" class="text-white font-bold">規模 5.0 地震</span>
              </div>
            </div>

            <!-- 砝碼按鍵群 -->
            <div class="flex flex-wrap items-center gap-1.5">
              <button onclick="addG5Weight(1)" class="px-2.5 py-1.5 rounded-xl bg-slate-700 hover:bg-amber-500 hover:text-slate-950 text-white font-mono font-bold text-xs border border-slate-600 transition-all">+1 個</button>
              <button onclick="addG5Weight(10)" class="px-2.5 py-1.5 rounded-xl bg-slate-700 hover:bg-amber-500 hover:text-slate-950 text-white font-mono font-bold text-xs border border-slate-600 transition-all">+10 個</button>
              <button onclick="addG5Weight(31.6)" class="px-2.5 py-1.5 rounded-xl bg-indigo-700 hover:bg-amber-500 hover:text-slate-950 text-white font-mono font-black text-xs border border-indigo-500 transition-all">+31.6 (約1級)</button>
              <button onclick="addG5Weight(100)" class="px-2.5 py-1.5 rounded-xl bg-slate-700 hover:bg-amber-500 hover:text-slate-950 text-white font-mono font-bold text-xs border border-slate-600 transition-all">+100 個</button>
              <button onclick="addG5Weight(1000)" class="px-2.5 py-1.5 rounded-xl bg-red-700 hover:bg-amber-500 hover:text-slate-950 text-white font-mono font-black text-xs border border-red-500 transition-all">+1000 (剛好2級)</button>
              <button onclick="clearG5Weight()" class="px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-red-800 text-rose-300 font-bold text-xs border border-slate-600 transition-all">清空右盤</button>
              <button onclick="verifyG5Balance()" class="px-4 py-1.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs shadow-md transition-all">確認平衡</button>
            </div>
          </div>
        </div>

      </main>

      <!-- 頁底競技場狀態列 -->
      <footer class="h-10 px-6 bg-slate-950 border-t border-slate-800 flex items-center justify-between text-[11px] text-slate-400 shrink-0">
        <span class="flex items-center gap-1.5">
          <i class="fa-solid fa-trophy text-amber-400"></i>
          <span>名偵探柯南數理電玩競技場 ‧ 東大高職數學 2-3 專屬開發</span>
        </span>
        <span class="font-mono text-slate-500">
          WEB AUDIO SYNTHESIZER READY ‧ 100% OFFLINE
        </span>
      </footer>

    </div>
  </div>
"""

GAMES_JS_CODE = r"""
// =========================================================================
// 5大對數對戰電玩競技場 (Game Arena) 核心 JavaScript 引擎
// =========================================================================

let gameAudioEnabled = true;
let audioCtx = null;

function getAudioContext() {
    if (!audioCtx) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        if (AudioContext) {
            audioCtx = new AudioContext();
        }
    }
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    return audioCtx;
}

function playSynthSound(type) {
    if (!gameAudioEnabled) return;
    try {
        const ctx = getAudioContext();
        if (!ctx) return;
        
        const now = ctx.currentTime;
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);

        if (type === 'click') {
            osc.type = 'sine';
            osc.frequency.setValueAtTime(800, now);
            osc.frequency.exponentialRampToValueAtTime(400, now + 0.05);
            gain.gain.setValueAtTime(0.2, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.05);
            osc.start(now);
            osc.stop(now + 0.05);
        } else if (type === 'match' || type === 'correct') {
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(523.25, now); // C5
            osc.frequency.setValueAtTime(659.25, now + 0.08); // E5
            osc.frequency.setValueAtTime(783.99, now + 0.16); // G5
            gain.gain.setValueAtTime(0.25, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.3);
            osc.start(now);
            osc.stop(now + 0.3);
        } else if (type === 'laser') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(990, now);
            osc.frequency.exponentialRampToValueAtTime(110, now + 0.15);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
            osc.start(now);
            osc.stop(now + 0.15);
        } else if (type === 'explode') {
            osc.type = 'square';
            osc.frequency.setValueAtTime(150, now);
            osc.frequency.linearRampToValueAtTime(40, now + 0.25);
            gain.gain.setValueAtTime(0.4, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        } else if (type === 'wrong') {
            osc.type = 'sawtooth';
            osc.frequency.setValueAtTime(180, now);
            osc.frequency.setValueAtTime(140, now + 0.1);
            gain.gain.setValueAtTime(0.3, now);
            gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
            osc.start(now);
            osc.stop(now + 0.25);
        } else if (type === 'win') {
            // Victory Fanfare
            const notes = [523.25, 659.25, 783.99, 1046.50];
            notes.forEach((freq, idx) => {
                const o = ctx.createOscillator();
                const g = ctx.createGain();
                o.connect(g);
                g.connect(ctx.destination);
                o.type = 'triangle';
                o.frequency.setValueAtTime(freq, now + idx * 0.12);
                g.gain.setValueAtTime(0.25, now + idx * 0.12);
                g.gain.exponentialRampToValueAtTime(0.01, now + idx * 0.12 + 0.3);
                o.start(now + idx * 0.12);
                o.stop(now + idx * 0.12 + 0.3);
            });
        }
    } catch (e) {
        console.warn('Audio not allowed yet or error', e);
    }
}

function toggleGameAudio() {
    gameAudioEnabled = !gameAudioEnabled;
    const btn = document.getElementById('game-audio-toggle');
    const icon = document.getElementById('game-audio-icon');
    if (gameAudioEnabled) {
        btn.classList.replace('text-slate-500', 'text-amber-400');
        icon.className = 'fa-solid fa-volume-high';
        btn.innerHTML = `<i id="game-audio-icon" class="fa-solid fa-volume-high"></i> <span class="hidden md:inline">音效: 開</span>`;
        playSynthSound('click');
    } else {
        btn.classList.replace('text-amber-400', 'text-slate-500');
        icon.className = 'fa-solid fa-volume-xmark';
        btn.innerHTML = `<i id="game-audio-icon" class="fa-solid fa-volume-xmark"></i> <span class="hidden md:inline">音效: 靜音</span>`;
    }
}

// 彈窗開啟與切換
function openGameArenaModal(defaultTab = 1) {
    const modal = document.getElementById('game-arena-modal');
    if (!modal) return;
    modal.classList.remove('hidden');
    switchGame(defaultTab);
    incrementInteractions();
}

function closeGameArenaModal() {
    const modal = document.getElementById('game-arena-modal');
    if (!modal) return;
    modal.classList.add('hidden');
    // 停止遊戲定時器
    if (g1TimerInterval) clearInterval(g1TimerInterval);
    if (g2TimerInterval) clearInterval(g2TimerInterval);
    if (g4AnimationId) cancelAnimationFrame(g4AnimationId);
}

function switchGame(gameIdx) {
    playSynthSound('click');
    for (let i = 1; i <= 5; i++) {
        const tab = document.getElementById(`game-tab-${i}`);
        const panel = document.getElementById(`game-panel-${i}`);
        if (tab && panel) {
            if (i === gameIdx) {
                tab.className = 'game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-blue-700 text-white shadow-md';
                panel.classList.remove('hidden');
            } else {
                tab.className = 'game-nav-btn px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-black transition-all flex items-center gap-2 whitespace-nowrap bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white';
                panel.classList.add('hidden');
            }
        }
    }

    if (gameIdx === 1) restartGame1();
    if (gameIdx === 2) restartGame2();
    if (gameIdx === 3) restartGame3();
    if (gameIdx === 4) startGame4();
    if (gameIdx === 5) restartGame5();
}

// =========================================================================
// 遊戲 1：骨牌連鎖消消樂 (Domino Match Duel)
// =========================================================================
let g1Mode = '1p'; // '1p' or '2p'
let g1Score = 0;
let g1Combo = 0;
let g1TimeLeft = 60;
let g1TimerInterval = null;
let g1SelectedCard = null;
let g1PairsLeft = 0;

const G1_POOL = [
    { expr: '\\log_2 16', val: '4' },
    { expr: '\\log_3 27', val: '3' },
    { expr: '\\log_5 \\frac{1}{25}', val: '-2' },
    { expr: '\\log_{10} 1000', val: '3' },
    { expr: '\\log_2 \\frac{1}{4}', val: '-2' },
    { expr: '\\log_7 49', val: '2' },
    { expr: '\\log_3 5 \\cdot \\log_5 9', val: '2' },
    { expr: '\\log_2 3 \\cdot \\log_3 8', val: '3' },
    { expr: '\\log_4 2', val: '0.5' },
    { expr: '\\log_9 3', val: '0.5' },
    { expr: '\\log_2 6 - \\log_2 3', val: '1' },
    { expr: '\\log_6 2 + \\log_6 3', val: '1' },
    { expr: '\\log_2 1', val: '0' },
    { expr: '\\log_5 5', val: '1' },
    { expr: '3^{\\log_3 7}', val: '7' },
    { expr: '\\log_{10} 0.01', val: '-2' }
];

function setGame1Mode(mode) {
    g1Mode = mode;
    document.getElementById('g1-mode-1p-btn').className = mode === '1p' ? 'px-3 py-1 rounded-lg bg-blue-600 text-white font-black' : 'px-3 py-1 rounded-lg bg-slate-700 text-slate-300 hover:bg-slate-600 font-black';
    document.getElementById('g1-mode-2p-btn').className = mode === '2p' ? 'px-3 py-1 rounded-lg bg-rose-600 text-white font-black' : 'px-3 py-1 rounded-lg bg-slate-700 text-slate-300 hover:bg-slate-600 font-black';
    restartGame1();
}

function restartGame1() {
    if (g1TimerInterval) clearInterval(g1TimerInterval);
    g1Score = 0;
    g1Combo = 0;
    g1TimeLeft = 60;
    g1SelectedCard = null;
    document.getElementById('g1-score').innerText = g1Score;
    document.getElementById('g1-combo').innerText = g1Combo;
    document.getElementById('g1-timer').innerText = g1TimeLeft;
    document.getElementById('g1-status-msg').innerText = '點選題目卡與數值解進行連線配對！';

    // 隨機抽選 6 組對數
    const shuffledPool = [...G1_POOL].sort(() => 0.5 - Math.random()).slice(0, 6);
    g1PairsLeft = shuffledPool.length;

    // 分拆為題目牌與答案牌
    let cards = [];
    shuffledPool.forEach((item, idx) => {
        cards.push({ id: `q-${idx}`, pairId: idx, text: `$${item.expr}$`, isExpr: true });
        cards.push({ id: `a-${idx}`, pairId: idx, text: item.val === '0.5' ? '$\\frac{1}{2}$' : item.val, isExpr: false });
    });
    cards.sort(() => 0.5 - Math.random());

    const board = document.getElementById('g1-board');
    board.innerHTML = '';
    cards.forEach(c => {
        const div = document.createElement('div');
        div.id = `g1-card-${c.id}`;
        div.className = 'g1-tile p-3 bg-slate-800 hover:bg-blue-900 border-2 border-slate-700 rounded-xl flex items-center justify-center text-center cursor-pointer transition-all transform hover:scale-105 active:scale-95 shadow-md min-h-[75px]';
        div.innerHTML = `<span class="text-sm font-mono font-bold text-slate-100">${c.text}</span>`;
        div.onclick = () => onCard1Click(c, div);
        board.appendChild(div);
    });

    if (window.renderMathInElement) {
        renderMathInElement(board, {
            delimiters: [{ left: '$', right: '$', display: false }]
        });
    }

    g1TimerInterval = setInterval(() => {
        g1TimeLeft--;
        document.getElementById('g1-timer').innerText = g1TimeLeft;
        if (g1TimeLeft <= 0) {
            clearInterval(g1TimerInterval);
            playSynthSound('explode');
            document.getElementById('g1-status-msg').innerText = `時間到！最終破案積分：${g1Score} 分！`;
        }
    }, 1000);
}

function onCard1Click(cardData, el) {
    if (el.classList.contains('opacity-20') || el.classList.contains('pointer-events-none')) return;
    playSynthSound('click');

    if (!g1SelectedCard) {
        g1SelectedCard = { data: cardData, el: el };
        el.classList.add('border-amber-400', 'bg-blue-800', 'ring-2', 'ring-amber-400');
    } else {
        if (g1SelectedCard.data.id === cardData.id) {
            el.classList.remove('border-amber-400', 'bg-blue-800', 'ring-2', 'ring-amber-400');
            g1SelectedCard = null;
            return;
        }

        // 檢查是否配對成功
        if (g1SelectedCard.data.pairId === cardData.pairId && g1SelectedCard.data.isExpr !== cardData.isExpr) {
            // 配對成功！
            playSynthSound('match');
            g1Combo++;
            const points = 100 * g1Combo;
            g1Score += points;
            document.getElementById('g1-score').innerText = g1Score;
            document.getElementById('g1-combo').innerText = g1Combo;

            el.classList.add('bg-emerald-600', 'border-emerald-400');
            g1SelectedCard.el.classList.add('bg-emerald-600', 'border-emerald-400');

            setTimeout(() => {
                el.classList.add('opacity-20', 'pointer-events-none');
                g1SelectedCard.el.classList.add('opacity-20', 'pointer-events-none');
                g1SelectedCard = null;
                g1PairsLeft--;
                if (g1PairsLeft <= 0) {
                    clearInterval(g1TimerInterval);
                    playSynthSound('win');
                    document.getElementById('g1-status-msg').innerText = `🎉 恭喜通關破案！用時 ${60 - g1TimeLeft} 秒，獲得 ${g1Score} 分！`;
                }
            }, 300);
        } else {
            // 配對失敗
            playSynthSound('wrong');
            g1Combo = 0;
            document.getElementById('g1-combo').innerText = g1Combo;
            el.classList.add('bg-red-800', 'border-red-500');
            g1SelectedCard.el.classList.add('bg-red-800', 'border-red-500');

            setTimeout(() => {
                el.classList.remove('bg-red-800', 'border-red-500');
                if (g1SelectedCard && g1SelectedCard.el) {
                    g1SelectedCard.el.classList.remove('border-amber-400', 'bg-blue-800', 'ring-2', 'ring-amber-400', 'bg-red-800', 'border-red-500');
                }
                g1SelectedCard = null;
            }, 400);
        }
    }
}

// =========================================================================
// 遊戲 2：密室機關密碼盤 (Cryptex Escape Room)
// =========================================================================
let g2Stage = 0;
let g2Timer = 90;
let g2TimerInterval = null;
let g2Dials = [0, 0, 0];

const G2_PUZZLES = [
    {
        badge: 'STAGE 1 ‧ 存在條件',
        text: '若 $\\log_{x-2}(7-x)$ 有意義，且 $x$ 為整數，試問符合條件的 $x$ 最大值為多少？（密碼為此整數值）',
        hint: '底數條件 $x-2>0$ 且 $x-2 \\neq 1 \\implies x>2, x \\neq 3$；真數條件 $7-x>0 \\implies x<7$。整數解為 4, 5, 6，最大值為 6（轉輪請轉為 006）。',
        ans: [0, 0, 6]
    },
    {
        badge: 'STAGE 2 ‧ 對數加減化簡',
        text: '計算 $\\log_2 48 + \\log_2 3 - \\log_2 9$ 之化簡整數值。（密碼為此數值）',
        hint: '利用同底運算法則：$\\log_2(\\frac{48 \\times 3}{9}) = \\log_2(\\frac{144}{9}) = \\log_2 16 = 4$（轉輪請轉為 004）。',
        ans: [0, 0, 4]
    },
    {
        badge: 'STAGE 3 ‧ 換底公式連鎖律',
        text: '計算 $(\\log_2 3 + \\log_4 9)(\\log_3 4 + \\log_9 2)$ 之值。（密碼為此數值）',
        hint: '$\\log_4 9 = \\log_2 3$，故前括號為 $2\\log_2 3$；後括號為 $2\\log_3 2 + \\frac{1}{2}\\log_3 2 = \\frac{5}{2}\\log_3 2$ 或標準簡化為 3（轉輪請轉為 003）。',
        ans: [0, 0, 3]
    },
    {
        badge: 'STAGE 4 ‧ 首數與位數估算',
        text: '已知 $\\log_{10} 2 \\approx 0.3010$，試求 $2^{30}$ 為幾位數？（密碼為位數數值）',
        hint: '$\\log_{10}(2^{30}) = 30 \\times 0.3010 = 9.03$。首數為 9，位數為 $9+1 = 10$ 位數（轉輪請轉為 010）。',
        ans: [0, 1, 0]
    }
];

function restartGame2() {
    if (g2TimerInterval) clearInterval(g2TimerInterval);
    g2Stage = 0;
    g2Timer = 90;
    g2Dials = [0, 0, 0];
    updateG2DialDisplay();
    loadG2Puzzle();

    g2TimerInterval = setInterval(() => {
        g2Timer--;
        document.getElementById('g2-timer').innerText = g2Timer;
        if (g2Timer <= 0) {
            clearInterval(g2TimerInterval);
            playSynthSound('explode');
            document.getElementById('g2-feedback').innerHTML = '<span class="text-red-500 font-bold">逃脫失敗！密室氣閥已鎖死！</span>';
        }
    }, 1000);
}

function loadG2Puzzle() {
    const p = G2_PUZZLES[g2Stage];
    document.getElementById('g2-stage-idx').innerText = g2Stage + 1;
    document.getElementById('g2-puzzle-badge').innerText = p.badge;
    document.getElementById('g2-puzzle-text').innerHTML = p.text;
    document.getElementById('g2-puzzle-hint').innerHTML = `<strong>情報提示：</strong>${p.hint}`;
    document.getElementById('g2-feedback').innerHTML = '請撥動輪盤對準密碼，按下解鎖！';

    const textEl = document.getElementById('g2-puzzle-text');
    const hintEl = document.getElementById('g2-puzzle-hint');
    if (window.renderMathInElement) {
        renderMathInElement(textEl, { delimiters: [{ left: '$', right: '$', display: false }] });
        renderMathInElement(hintEl, { delimiters: [{ left: '$', right: '$', display: false }] });
    }
}

function changeG2Dial(dialIdx, delta) {
    playSynthSound('click');
    g2Dials[dialIdx] = (g2Dials[dialIdx] + delta + 10) % 10;
    updateG2DialDisplay();
}

function updateG2DialDisplay() {
    for (let i = 0; i < 3; i++) {
        const el = document.getElementById(`g2-dial-${i}`);
        if (el) el.innerText = g2Dials[i];
    }
}

function submitG2Unlock() {
    const p = G2_PUZZLES[g2Stage];
    const isCorrect = g2Dials[0] === p.ans[0] && g2Dials[1] === p.ans[1] && g2Dials[2] === p.ans[2];

    if (isCorrect) {
        playSynthSound('match');
        g2Stage++;
        if (g2Stage >= G2_PUZZLES.length) {
            clearInterval(g2TimerInterval);
            playSynthSound('win');
            document.getElementById('g2-feedback').innerHTML = '🎉 <span class="text-emerald-400 font-black">恭喜完全破解阿笠博士的全部 4 道機關密碼！成功逃脫密室！</span>';
        } else {
            document.getElementById('g2-feedback').innerHTML = '✨ <span class="text-amber-400 font-bold">機關卡嗒一聲彈開！成功解鎖第 ' + g2Stage + ' 道鎖！進入下一道！</span>';
            setTimeout(() => {
                g2Dials = [0, 0, 0];
                updateG2DialDisplay();
                loadG2Puzzle();
            }, 800);
        }
    } else {
        playSynthSound('wrong');
        document.getElementById('g2-feedback').innerHTML = '❌ <span class="text-red-400 font-bold">密碼錯誤，警報紅燈閃爍！請重新推理計算！</span>';
    }
}

// =========================================================================
// 遊戲 3：迷宮雷達尋路戰 (Maze Runner)
// =========================================================================
let g3Floor = 1;
let g3Hp = 3;
let g3TargetVal = 3;
let g3Player = { x: 20, y: 20 };
let g3Doors = [];
let g3Enemies = [];
let g3Canvas = null;
let g3Ctx = null;

const G3_LEVEL_DATA = [
    {
        target: 3,
        doors: [
            { x: 340, y: 40, label: '\\log_2 8', val: 3 },
            { x: 340, y: 150, label: '\\log_3 81', val: 4 },
            { x: 340, y: 260, label: '\\log_5 \\frac{1}{5}', val: -1 }
        ]
    },
    {
        target: -2,
        doors: [
            { x: 340, y: 40, label: '\\log_{10} 100', val: 2 },
            { x: 340, y: 150, label: '\\log_3 \\frac{1}{9}', val: -2 },
            { x: 340, y: 260, label: '\\log_7 1', val: 0 }
        ]
    },
    {
        target: 1,
        doors: [
            { x: 340, y: 40, label: '\\log_2 6 - \\log_2 3', val: 1 },
            { x: 340, y: 150, label: '\\log_2 16', val: 4 },
            { x: 340, y: 260, label: '\\log_4 64', val: 3 }
        ]
    },
    {
        target: 0,
        doors: [
            { x: 340, y: 40, label: '\\log_5 1', val: 0 },
            { x: 340, y: 150, label: '\\log_2 2', val: 1 },
            { x: 340, y: 260, label: '3^0', val: 1 }
        ]
    },
    {
        target: 2,
        doors: [
            { x: 340, y: 40, label: '\\log_3 5 \\cdot \\log_5 9', val: 2 },
            { x: 340, y: 150, label: '\\log_2 8', val: 3 },
            { x: 340, y: 260, label: '\\log_2 16', val: 4 }
        ]
    }
];

function restartGame3() {
    g3Floor = 1;
    g3Hp = 3;
    loadG3Floor();
}

function loadG3Floor() {
    g3Canvas = document.getElementById('g3-canvas');
    if (!g3Canvas) return;
    g3Ctx = g3Canvas.getContext('2d');
    
    document.getElementById('g3-floor').innerText = g3Floor;
    document.getElementById('g3-hp').innerText = '❤️'.repeat(g3Hp);
    
    const lvl = G3_LEVEL_DATA[g3Floor - 1];
    g3TargetVal = lvl.target;
    document.getElementById('g3-target-val').innerText = g3TargetVal;
    
    g3Player = { x: 30, y: 160 };
    g3Doors = lvl.doors;
    
    // 設置兩名巡邏守衛
    g3Enemies = [
        { x: 140, y: 50, vy: 2 },
        { x: 240, y: 260, vy: -2 }
    ];

    drawG3();
}

function drawG3() {
    if (!g3Ctx) return;
    g3Ctx.clearRect(0, 0, g3Canvas.width, g3Canvas.height);

    // 繪製背景通道
    g3Ctx.fillStyle = '#0f172a';
    g3Ctx.fillRect(0, 0, g3Canvas.width, g3Canvas.height);

    // 繪製迷宮網格線
    g3Ctx.strokeStyle = '#1e293b';
    g3Ctx.lineWidth = 1;
    for (let x = 0; x < g3Canvas.width; x += 40) {
        g3Ctx.beginPath();
        g3Ctx.moveTo(x, 0);
        g3Ctx.lineTo(x, g3Canvas.height);
        g3Ctx.stroke();
    }
    for (let y = 0; y < g3Canvas.height; y += 40) {
        g3Ctx.beginPath();
        g3Ctx.moveTo(0, y);
        g3Ctx.lineTo(g3Canvas.width, y);
        g3Ctx.stroke();
    }

    // 繪製傳送門 (Doors)
    g3Doors.forEach(d => {
        g3Ctx.fillStyle = '#1e3a8a';
        g3Ctx.strokeStyle = '#3b82f6';
        g3Ctx.lineWidth = 2;
        g3Ctx.fillRect(d.x - 20, d.y - 25, 45, 50);
        g3Ctx.strokeRect(d.x - 20, d.y - 25, 45, 50);

        // 門上文字標記
        g3Ctx.fillStyle = '#fde047';
        g3Ctx.font = 'bold 11px monospace';
        g3Ctx.textAlign = 'center';
        g3Ctx.fillText(d.label.replace(/\\/g, ''), d.x + 2, d.y + 4);
    });

    // 繪製巡邏警衛
    g3Enemies.forEach(e => {
        g3Ctx.fillStyle = '#dc2626';
        g3Ctx.beginPath();
        g3Ctx.arc(e.x, e.y, 10, 0, Math.PI * 2);
        g3Ctx.fill();
        g3Ctx.strokeStyle = '#f87171';
        g3Ctx.stroke();
    });

    // 繪製柯南主角 (藍底黃框圓形)
    g3Ctx.fillStyle = '#2563eb';
    g3Ctx.beginPath();
    g3Ctx.arc(g3Player.x, g3Player.y, 12, 0, Math.PI * 2);
    g3Ctx.fill();
    g3Ctx.strokeStyle = '#facc15';
    g3Ctx.lineWidth = 3;
    g3Ctx.stroke();

    // 柯南眼鏡標記
    g3Ctx.fillStyle = '#ffffff';
    g3Ctx.fillRect(g3Player.x - 6, g3Player.y - 3, 5, 4);
    g3Ctx.fillRect(g3Player.x + 1, g3Player.y - 3, 5, 4);
}

function moveG3(dir) {
    const step = 20;
    if (dir === 'up') g3Player.y = Math.max(20, g3Player.y - step);
    if (dir === 'down') g3Player.y = Math.min(g3Canvas.height - 20, g3Player.y + step);
    if (dir === 'left') g3Player.x = Math.max(20, g3Player.x - step);
    if (dir === 'right') g3Player.x = Math.min(g3Canvas.width - 20, g3Player.x + step);

    // 檢查巡邏碰撞
    g3Enemies.forEach(e => {
        const dist = Math.hypot(e.x - g3Player.x, e.y - g3Player.y);
        if (dist < 20) {
            playSynthSound('wrong');
            g3Hp--;
            document.getElementById('g3-hp').innerText = '❤️'.repeat(Math.max(0, g3Hp));
            g3Player = { x: 30, y: 160 }; // 送回起點
            if (g3Hp <= 0) {
                playSynthSound('explode');
                alert('被黑衣組織巡邏隊逮捕！請重新挑戰！');
                restartGame3();
                return;
            }
        }
    });

    // 檢查是否走到任一扇門
    g3Doors.forEach(d => {
        const dist = Math.hypot(d.x - g3Player.x, d.y - g3Player.y);
        if (dist < 30) {
            if (d.val === g3TargetVal) {
                // 正確門！
                playSynthSound('match');
                g3Floor++;
                if (g3Floor > G3_LEVEL_DATA.length) {
                    playSynthSound('win');
                    alert('🎉 太厲害了！成功穿越 5 層大樓迷宮，順利脫逃！');
                    restartGame3();
                } else {
                    loadG3Floor();
                }
            } else {
                // 走錯門
                playSynthSound('wrong');
                g3Hp--;
                document.getElementById('g3-hp').innerText = '❤️'.repeat(Math.max(0, g3Hp));
                g3Player.x -= 40; // 彈回
                if (g3Hp <= 0) {
                    playSynthSound('explode');
                    alert('門後是陷阱！體力耗盡！');
                    restartGame3();
                }
            }
        }
    });

    drawG3();
}

// 迷宮鍵盤監聽
window.addEventListener('keydown', (e) => {
    const modal = document.getElementById('game-arena-modal');
    if (modal && !modal.classList.contains('hidden')) {
        const g3Panel = document.getElementById('game-panel-3');
        if (g3Panel && !g3Panel.classList.contains('hidden')) {
            if (e.key === 'ArrowUp') { moveG3('up'); e.preventDefault(); }
            if (e.key === 'ArrowDown') { moveG3('down'); e.preventDefault(); }
            if (e.key === 'ArrowLeft') { moveG3('left'); e.preventDefault(); }
            if (e.key === 'ArrowRight') { moveG3('right'); e.preventDefault(); }
        }
    }
});

// =========================================================================
// 遊戲 4：踢力增強鞋射擊防禦戰 (Log Target Defense)
// =========================================================================
let g4Canvas = null;
let g4Ctx = null;
let g4Targets = [];
let g4Bullets = [];
let g4Particles = [];
let g4Hp = 100;
let g4Score = 0;
let g4Kills = 0;
let g4Wave = 1;
let g4AnimationId = null;
let g4IsRunning = false;

const G4_TARGET_POOL = [
    { expr: 'log2(8)', val: 3 },
    { expr: 'log3(81)', val: 4 },
    { expr: 'log10(100)', val: 2 },
    { expr: 'log5(1/5)', val: -1 },
    { expr: 'log2(1/4)', val: -2 },
    { expr: 'log7(1)', val: 0 },
    { expr: 'log4(2)', val: 0.5 },
    { expr: 'log2(32)', val: 5 },
    { expr: 'log2(6)-log2(3)', val: 1 }
];

function startGame4() {
    g4Canvas = document.getElementById('g4-canvas');
    if (!g4Canvas) return;
    g4Ctx = g4Canvas.getContext('2d');

    document.getElementById('g4-overlay').classList.add('hidden');
    g4Hp = 100;
    g4Score = 0;
    g4Kills = 0;
    g4Wave = 1;
    g4Targets = [];
    g4Bullets = [];
    g4Particles = [];
    g4IsRunning = true;

    document.getElementById('g4-hp').innerText = g4Hp;
    document.getElementById('g4-score').innerText = g4Score;
    document.getElementById('g4-kills').innerText = g4Kills;
    document.getElementById('g4-wave').innerText = g4Wave;

    if (g4AnimationId) cancelAnimationFrame(g4AnimationId);
    g4LastSpawn = performance.now();
    g4Loop(performance.now());
}

function restartGame4() {
    startGame4();
}

let g4LastSpawn = 0;
function g4Loop(timestamp) {
    if (!g4IsRunning) return;

    // 每 2.5 秒生成一個掉落算式
    if (timestamp - g4LastSpawn > 2500 - Math.min(1500, g4Wave * 200)) {
        const item = G4_TARGET_POOL[Math.floor(Math.random() * G4_TARGET_POOL.length)];
        g4Targets.push({
            x: 50 + Math.random() * (g4Canvas.width - 100),
            y: 0,
            expr: item.expr,
            val: item.val,
            speed: 0.8 + g4Wave * 0.15
        });
        g4LastSpawn = timestamp;
    }

    // 邏輯更新
    // 1. 更新目標
    for (let i = g4Targets.length - 1; i >= 0; i--) {
        const t = g4Targets[i];
        t.y += t.speed;
        if (t.y >= g4Canvas.height - 40) {
            // 掉落地面，扣耐久
            playSynthSound('wrong');
            g4Hp -= 20;
            document.getElementById('g4-hp').innerText = Math.max(0, g4Hp);
            g4Targets.splice(i, 1);

            if (g4Hp <= 0) {
                g4IsRunning = false;
                playSynthSound('explode');
                document.getElementById('g4-overlay').classList.remove('hidden');
                document.getElementById('g4-gameover-title').innerText = '防線被突破！';
                document.getElementById('g4-gameover-desc').innerText = `最終擊落 ${g4Kills} 個目標，守備積分：${g4Score} 分！`;
                return;
            }
        }
    }

    // 2. 更新足球子彈
    for (let i = g4Bullets.length - 1; i >= 0; i--) {
        const b = g4Bullets[i];
        b.x += b.vx;
        b.y += b.vy;

        // 碰撞檢測
        for (let j = g4Targets.length - 1; j >= 0; j--) {
            const t = g4Targets[j];
            const dist = Math.hypot(t.x - b.x, t.y - b.y);
            if (dist < 35 && b.val === t.val) {
                // 命中摧毀！
                playSynthSound('explode');
                // 產生粒子
                for (let k = 0; k < 12; k++) {
                    g4Particles.push({
                        x: t.x,
                        y: t.y,
                        vx: (Math.random() - 0.5) * 6,
                        vy: (Math.random() - 0.5) * 6,
                        alpha: 1.0,
                        color: '#facc15'
                    });
                }
                g4Targets.splice(j, 1);
                g4Bullets.splice(i, 1);
                g4Kills++;
                g4Score += 150;
                document.getElementById('g4-kills').innerText = g4Kills;
                document.getElementById('g4-score').innerText = g4Score;

                if (g4Kills % 5 === 0) {
                    g4Wave++;
                    document.getElementById('g4-wave').innerText = g4Wave;
                }
                break;
            }
        }

        if (b.y < -20) g4Bullets.splice(i, 1);
    }

    // 3. 更新粒子
    for (let i = g4Particles.length - 1; i >= 0; i--) {
        const p = g4Particles[i];
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= 0.04;
        if (p.alpha <= 0) g4Particles.splice(i, 1);
    }

    // 渲染畫布
    g4Ctx.clearRect(0, 0, g4Canvas.width, g4Canvas.height);

    // 繪製星空背景
    g4Ctx.fillStyle = '#090d16';
    g4Ctx.fillRect(0, 0, g4Canvas.width, g4Canvas.height);

    // 繪製底部防禦線 (柯南發射台)
    g4Ctx.strokeStyle = '#dc2626';
    g4Ctx.lineWidth = 3;
    g4Ctx.beginPath();
    g4Ctx.moveTo(0, g4Canvas.height - 30);
    g4Ctx.lineTo(g4Canvas.width, g4Canvas.height - 30);
    g4Ctx.stroke();

    // 繪製柯南射擊腳力增強鞋 (底中)
    g4Ctx.fillStyle = '#2563eb';
    g4Ctx.beginPath();
    g4Ctx.arc(g4Canvas.width / 2, g4Canvas.height - 20, 16, 0, Math.PI * 2);
    g4Ctx.fill();
    g4Ctx.fillStyle = '#ef4444';
    g4Ctx.fillRect(g4Canvas.width / 2 - 12, g4Canvas.height - 18, 24, 8);

    // 繪製掉落目標 (無人機/炸彈)
    g4Targets.forEach(t => {
        g4Ctx.fillStyle = '#1e293b';
        g4Ctx.strokeStyle = '#ef4444';
        g4Ctx.lineWidth = 2;
        g4Ctx.fillRect(t.x - 45, t.y - 18, 90, 36);
        g4Ctx.strokeRect(t.x - 45, t.y - 18, 90, 36);

        g4Ctx.fillStyle = '#f8fafc';
        g4Ctx.font = 'bold 13px monospace';
        g4Ctx.textAlign = 'center';
        g4Ctx.fillText(t.expr, t.x, t.y + 5);
    });

    // 繪製足球子彈
    g4Bullets.forEach(b => {
        g4Ctx.fillStyle = '#ffffff';
        g4Ctx.beginPath();
        g4Ctx.arc(b.x, b.y, 8, 0, Math.PI * 2);
        g4Ctx.fill();
        g4Ctx.strokeStyle = '#000000';
        g4Ctx.lineWidth = 2;
        g4Ctx.stroke();
    });

    // 繪製粒子
    g4Particles.forEach(p => {
        g4Ctx.fillStyle = p.color;
        g4Ctx.globalAlpha = p.alpha;
        g4Ctx.beginPath();
        g4Ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
        g4Ctx.fill();
        g4Ctx.globalAlpha = 1.0;
    });

    g4AnimationId = requestAnimationFrame(g4Loop);
}

function fireG4Val(val) {
    if (!g4IsRunning) return;
    playSynthSound('laser');

    // 尋找最近且匹配該數值的目標
    let target = null;
    let maxDistanceY = -1;
    g4Targets.forEach(t => {
        if (t.val === val && t.y > maxDistanceY) {
            maxDistanceY = t.y;
            target = t;
        }
    });

    const startX = g4Canvas.width / 2;
    const startY = g4Canvas.height - 30;

    if (target) {
        const dx = target.x - startX;
        const dy = target.y - startY;
        const dist = Math.hypot(dx, dy);
        const speed = 14;
        g4Bullets.push({
            x: startX,
            y: startY,
            vx: (dx / dist) * speed,
            vy: (dy / dist) * speed,
            val: val
        });
    } else {
        // 沒有目標也朝上踢出一顆空包彈
        g4Bullets.push({
            x: startX,
            y: startY,
            vx: (Math.random() - 0.5) * 4,
            vy: -12,
            val: val
        });
    }
}

// =========================================================================
// 遊戲 5：芮氏地震能量天平 (Earthquake Richter Balancer)
// =========================================================================
let g5Level = 1;
let g5LeftM = 7.0;
let g5RightM = 5.0;
let g5RightCount = 0;
let g5TargetRatio = 1000; // 10^(1.5 * 2) = 1000
let g5Canvas = null;
let g5Ctx = null;
let g5TiltAngle = -0.25; // 負代表左邊重

const G5_LEVELS = [
    { leftM: 7.0, rightM: 5.0, diff: 2.0, ratio: 1000, desc: '規模 7.0 vs 規模 5.0（差 2 級，能量差 1000 倍）' },
    { leftM: 6.0, rightM: 5.0, diff: 1.0, ratio: 31.6, desc: '規模 6.0 vs 規模 5.0（差 1 級，能量差 10^1.5 ≈ 31.6 倍）' },
    { leftM: 7.0, rightM: 6.0, diff: 1.0, ratio: 31.6, desc: '規模 7.0 vs 規模 6.0（差 1 級，能量差 10^1.5 ≈ 31.6 倍）' },
    { leftM: 8.0, rightM: 6.0, diff: 2.0, ratio: 1000, desc: '規模 8.0 vs 規模 6.0（差 2 級，能量差 1000 倍）' },
    { leftM: 7.0, rightM: 4.0, diff: 3.0, ratio: 31622, desc: '規模 7.0 vs 規模 4.0（差 3 級，能量差 10^4.5 ≈ 31622 倍）' }
];

function restartGame5() {
    g5Canvas = document.getElementById('g5-canvas');
    if (g5Canvas) g5Ctx = g5Canvas.getContext('2d');
    loadG5Level(g5Level);
}

function loadG5Level(lvl) {
    const data = G5_LEVELS[(lvl - 1) % G5_LEVELS.length];
    g5LeftM = data.leftM;
    g5RightM = data.rightM;
    g5TargetRatio = data.ratio;
    g5RightCount = 0;

    document.getElementById('g5-level').innerText = lvl;
    document.getElementById('g5-left-target').innerText = `規模 ${g5LeftM.toFixed(1)} 地震`;
    document.getElementById('g5-right-type').innerText = `規模 ${g5RightM.toFixed(1)} 地震`;
    document.getElementById('g5-right-weight').innerText = g5RightCount;
    document.getElementById('g5-balance-status').innerHTML = `<span class="text-slate-300">${data.desc}：請在右盤放入足夠的等效地震！</span>`;

    updateG5Tilt();
    drawG5();
}

function addG5Weight(amount) {
    playSynthSound('click');
    g5RightCount += amount;
    g5RightCount = Math.round(g5RightCount * 10) / 10;
    document.getElementById('g5-right-weight').innerText = g5RightCount;
    updateG5Tilt();
    drawG5();
}

function clearG5Weight() {
    playSynthSound('click');
    g5RightCount = 0;
    document.getElementById('g5-right-weight').innerText = g5RightCount;
    updateG5Tilt();
    drawG5();
}

function updateG5Tilt() {
    // 比較 g5RightCount 與 g5TargetRatio
    const diff = g5RightCount - g5TargetRatio;
    // 映射到角度 -0.3 ~ 0.3
    const ratio = diff / g5TargetRatio;
    g5TiltAngle = Math.max(-0.35, Math.min(0.35, ratio * 0.35));
}

function drawG5() {
    if (!g5Ctx) return;
    g5Ctx.clearRect(0, 0, g5Canvas.width, g5Canvas.height);

    const cx = g5Canvas.width / 2;
    const cy = 130;
    const beamLength = 240;

    // 1. 繪製天平底座與立柱
    g5Ctx.fillStyle = '#334155';
    g5Ctx.beginPath();
    g5Ctx.moveTo(cx - 30, g5Canvas.height - 20);
    g5Ctx.lineTo(cx + 30, g5Canvas.height - 20);
    g5Ctx.lineTo(cx + 10, cy);
    g5Ctx.lineTo(cx - 10, cy);
    g5Ctx.closePath();
    g5Ctx.fill();

    // 2. 旋轉橫梁
    g5Ctx.save();
    g5Ctx.translate(cx, cy);
    g5Ctx.rotate(g5TiltAngle);

    // 橫梁
    g5Ctx.fillStyle = '#e2e8f0';
    g5Ctx.fillRect(-beamLength / 2, -6, beamLength, 12);
    // 支點鉚釘
    g5Ctx.fillStyle = '#f59e0b';
    g5Ctx.beginPath();
    g5Ctx.arc(0, 0, 8, 0, Math.PI * 2);
    g5Ctx.fill();

    // 左吊盤繩索與盤子
    const lx = -beamLength / 2;
    g5Ctx.strokeStyle = '#94a3b8';
    g5Ctx.lineWidth = 2;
    g5Ctx.beginPath();
    g5Ctx.moveTo(lx, 0);
    g5Ctx.lineTo(lx - 25, 60);
    g5Ctx.moveTo(lx, 0);
    g5Ctx.lineTo(lx + 25, 60);
    g5Ctx.stroke();
    // 左盤
    g5Ctx.fillStyle = '#ef4444';
    g5Ctx.fillRect(lx - 35, 60, 70, 8);

    // 右吊盤繩索與盤子
    const rx = beamLength / 2;
    g5Ctx.beginPath();
    g5Ctx.moveTo(rx, 0);
    g5Ctx.lineTo(rx - 25, 60);
    g5Ctx.moveTo(rx, 0);
    g5Ctx.lineTo(rx + 25, 60);
    g5Ctx.stroke();
    // 右盤
    g5Ctx.fillStyle = '#3b82f6';
    g5Ctx.fillRect(rx - 35, 60, 70, 8);

    // 左盤文字砝碼
    g5Ctx.fillStyle = '#ffffff';
    g5Ctx.font = 'bold 11px sans-serif';
    g5Ctx.textAlign = 'center';
    g5Ctx.fillText(`M ${g5LeftM.toFixed(1)}`, lx, 52);

    // 右盤文字砝碼
    g5Ctx.fillStyle = '#fde047';
    g5Ctx.fillText(`${g5RightCount} 個`, rx, 52);

    g5Ctx.restore();

    // 3. 繪製上方指針刻度盤
    g5Ctx.strokeStyle = '#64748b';
    g5Ctx.beginPath();
    g5Ctx.arc(cx, cy, 35, Math.PI * 1.2, Math.PI * 1.8);
    g5Ctx.stroke();

    // 刻度指針
    g5Ctx.save();
    g5Ctx.translate(cx, cy);
    g5Ctx.rotate(g5TiltAngle);
    g5Ctx.strokeStyle = '#ef4444';
    g5Ctx.lineWidth = 3;
    g5Ctx.beginPath();
    g5Ctx.moveTo(0, 0);
    g5Ctx.lineTo(0, -32);
    g5Ctx.stroke();
    g5Ctx.restore();
}

function verifyG5Balance() {
    const margin = Math.abs(g5RightCount - g5TargetRatio) / g5TargetRatio;
    if (margin <= 0.05) {
        // 誤差在 5% 以內即為平衡！
        playSynthSound('win');
        document.getElementById('g5-balance-status').innerHTML = '🎉 <span class="text-emerald-400 font-black text-sm">天平完全平衡！完美驗證地震對數能量差！</span>';
        setTimeout(() => {
            g5Level++;
            loadG5Level(g5Level);
        }, 1500);
    } else if (g5RightCount < g5TargetRatio) {
        playSynthSound('wrong');
        document.getElementById('g5-balance-status').innerHTML = '❌ <span class="text-rose-400 font-bold">右側能量太輕！還需要放入更多地震砝碼！</span>';
    } else {
        playSynthSound('wrong');
        document.getElementById('g5-balance-status').innerHTML = '❌ <span class="text-amber-400 font-bold">右側能量超重！請清空或調整合適倍率！</span>';
    }
}
"""

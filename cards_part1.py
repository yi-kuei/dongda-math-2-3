# -*- coding: utf-8 -*-
"""
cards_part1.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
圖解學習卡資料集 Part 1 (CASE 01 ~ CASE 42)
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦完備版標準：
- 堅持「一題一卡、一小題獨立成卡」
- 課本例題與隨堂 100% 忠實原文
- 全欄位 100% KaTeX 標準數學式
- 正面無水平捲軸，適度 <br> 換行
- 2~4 步結構化思維導引（名偵探推理筆記 ‧ 線索推理鏈）
- 高解析 SVG 向量圖解
"""

CARDS_PART1 = [
    {
        "id": 1,
        "tag": "CASE 01",
        "page": "課本 p.74",
        "category": "對數定義",
        "title": "對數的由來與符號意義",
        "front_content": "「對數」在 17 世紀由蘇格蘭數學家納皮爾所發明。<br>為解決繁複的天文數字運算，他將乘除轉化為加減。<br>例如：$2^x = 32 \\implies x = 5$；<br>但若 $2^x = 30$，無法以有限小數精確寫出，<br>故定義全新符號：$x = \\log_2 30$ 表示其精確解。",
        "front_tip": "🕵️ 柯南破案導引：對數就是「求指數次方」！$\\log_a b$ 是問：底數 $a$ 要自乘幾次方才會等於真數 $b$？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：歷史背景與運算簡化",
                "content": "17 世紀天文航海需要龐大乘除計算，納皮爾發明對數，將繁雜的「乘除運算」透過指數對應轉化為簡易的「加減運算」。"
            },
            {
                "num": 2,
                "title": "線索 2：超越整數指數的符號誕生",
                "content": "當 $2^x = 32 = 2^5$ 時 $x = 5$。若 $2^x = 30$，因 $2^4 = 16 < 30 < 32 = 2^5$，解必在 4 到 5 之間，記作 $x = \\log_2 30$。"
            },
            {
                "num": 3,
                "title": "線索 3：雙向互換本質",
                "content": "指數式與對數式本質互通：底數在下方保持不變，指數與結果位置互換：$a^x = b \\iff x = \\log_a b$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$a^x = b \\iff x = \\log_a b$（底數在下不動，指數是求得的對數值）",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <defs>\n    <marker id=\"arr-red\" markerWidth=\"6\" markerHeight=\"6\" refX=\"5\" refY=\"3\" orient=\"auto\">\n      <path d=\"M0,0 L6,3 L0,6 Z\" fill=\"#dc2626\"/>\n    </marker>\n    <marker id=\"arr-grn\" markerWidth=\"6\" markerHeight=\"6\" refX=\"5\" refY=\"3\" orient=\"auto\">\n      <path d=\"M0,0 L6,3 L0,6 Z\" fill=\"#16a34a\"/>\n    </marker>\n  </defs>\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"2\"/>\n  <text x=\"190\" y=\"30\" text-anchor=\"middle\" font-size=\"14\" font-weight=\"bold\" fill=\"#1e40af\">指數與對數的雙向轉化</text>\n  \n  <path d=\"M 160 76 Q 190 60 220 76\" fill=\"none\" stroke=\"#dc2626\" stroke-width=\"2.5\" marker-end=\"url(#arr-red)\"/>\n  <text x=\"190\" y=\"58\" text-anchor=\"middle\" font-size=\"11\" font-weight=\"bold\" fill=\"#dc2626\">轉化</text>\n  \n  <path d=\"M 220 98 Q 190 114 160 98\" fill=\"none\" stroke=\"#16a34a\" stroke-width=\"2.5\" marker-end=\"url(#arr-grn)\"/>\n  <text x=\"190\" y=\"126\" text-anchor=\"middle\" font-size=\"11\" font-weight=\"bold\" fill=\"#16a34a\">還原</text>\n  \n  <foreignObject x=\"18\" y=\"45\" width=\"344\" height=\"132\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between\">\n      <div class=\"flex justify-between items-center w-full\">\n        <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-2 shadow-xs text-center w-[130px]\">\n          <div class=\"text-[11px] text-slate-500 font-medium\">指數式</div>\n          <div class=\"text-lg font-bold text-blue-600 mt-0.5\">$a^x = b$</div>\n        </div>\n        \n        <div class=\"w-[60px]\"></div>\n        \n        <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-2 shadow-xs text-center w-[130px]\">\n          <div class=\"text-[11px] text-slate-500 font-medium\">對數式</div>\n          <div class=\"text-lg font-bold text-blue-600 mt-0.5\">$x = \\log_a b$</div>\n        </div>\n      </div>\n      \n      <div class=\"text-[11px] text-slate-700 bg-white/95 px-3 py-1.5 rounded-lg border border-blue-200 shadow-2xs text-center\">\n        例：$2^5 = 32 \\iff 5 = \\log_2 32$ ； $2^x = 30 \\iff x = \\log_2 30$\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 2,
        "tag": "CASE 02",
        "page": "課本 p.74-75",
        "category": "存在條件",
        "title": "對數的定義與存在條件",
        "front_content": "設 $a > 0$、$a \\ne 1$ 且 $b > 0$。<br>若 $a^x = b$，以符號 $\\log_a b$ 表示 $x$：<br>$a^x = b \\iff x = \\log_a b$<br>符號 $\\log_a b$ 念作「以 $a$ 為底數時，$b$ 的對數」。<br>其中稱 $a$ 為<b>底數</b>，稱 $b$ 為<b>真數</b>。",
        "front_tip": "🕵️ 柯南破案導引：1. 底數大於 0；2. 底數不能等於 1；3. 真數必須嚴格大於 0！缺少任一項對數即無意義。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：底數條件的來源 ($a > 0, a \\ne 1$)",
                "content": "指數函數 $y = a^x$ 定義規定底數 $a > 0$ 且 $a \\ne 1$。若 $a \\le 0$，實數次方會出現虛數；若 $a = 1$，$1^x = 1$ 為常數函數，無法求出唯一的 $x$。"
            },
            {
                "num": 2,
                "title": "線索 2：真數條件的來源 ($b > 0$)",
                "content": "因為正數的任意次方恆為正數（$a^x > 0$），其圖形全在 $x$ 軸上方，故真數 $b = a^x$ 必須嚴格滿足 $b > 0$。"
            },
            {
                "num": 3,
                "title": "線索 3：存在條件整合檢核",
                "content": "任何對數式 $\\log_a b$ 有意義，必須三條件同時成立：$a > 0$、 $a \\ne 1$、 $b > 0$。缺一不可！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_a b$ 有意義 $\\iff a > 0$ 且 $a \\ne 1$（底數兩條件），且 $b > 0$（真數一條件）",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"170\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-1\">\n      <div class=\"text-xs font-bold text-slate-800 tracking-wide\">對數存在的「黃金三條件」</div>\n      <div class=\"flex justify-between items-center w-full gap-3 px-1 my-1\">\n        <div class=\"bg-rose-50/80 border-2 border-rose-300 rounded-xl p-2.5 text-center flex-1 shadow-xs\">\n          <div class=\"text-xs font-bold text-rose-700\">底數 $a$（兩大限制）</div>\n          <div class=\"text-base font-bold text-rose-800 my-1\">$a > 0 \\text{ 且 } a \\ne 1$</div>\n          <div class=\"text-[10px] text-rose-600\">基底必須為非 1 正數</div>\n        </div>\n        <div class=\"bg-emerald-50/80 border-2 border-emerald-300 rounded-xl p-2.5 text-center flex-1 shadow-xs\">\n          <div class=\"text-xs font-bold text-emerald-700\">真數 $b$（一大限制）</div>\n          <div class=\"text-base font-bold text-emerald-800 my-1\">$b > 0$</div>\n          <div class=\"text-[10px] text-emerald-600\">真數必須嚴格大於 0</div>\n        </div>\n      </div>\n      <div class=\"text-[11px] font-semibold text-slate-700 bg-white px-3 py-1 rounded-lg border border-slate-200 shadow-2xs text-center w-full\">\n        $\\log_a b$ 有意義 $\\iff a > 0, a \\ne 1 \\text{ 且 } b > 0$\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 3,
        "tag": "CASE 03",
        "page": "課本 p.77-78",
        "category": "基本性質",
        "title": "對數的五大基本運算性質",
        "front_content": "設 $a, M, N$ 為正實數且 $a \\ne 1$，$r, s$ 為實數且 $r \\ne 0$：<br>1. $\\log_a 1 = 0$、$\\log_a a = 1$<br>2. $\\log_{a^r} M^s = \\frac{s}{r}\\log_a M$<br>3. $\\log_a M + \\log_a N = \\log_a (MN)$<br>4. $\\log_a M - \\log_a N = \\log_a \\frac{M}{N}$<br>5. $a^{\\log_a M} = M$",
        "front_tip": "🕵️ 柯南破案導引：對數相加等於真數相乘；對數相減等於真數相除；次方提出時「分子是真數次方，分母是底數次方」！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：基礎值與次方提出律",
                "content": "因 $a^0 = 1, a^1 = a$，得 $\\log_a 1 = 0, \\log_a a = 1$。真數次方 $s$ 提至前方分子，底數次方 $r$ 提至前方分母：$\\log_{a^r} M^s = \\frac{s}{r}\\log_a M$。"
            },
            {
                "num": 2,
                "title": "線索 2：和差化積商律證明",
                "content": "令 $M = a^r, N = a^s$，則 $MN = a^{r+s}$，故 $\\log_a(MN) = r + s = \\log_a M + \\log_a N$。同理 $\\frac{M}{N} = a^{r-s}$ 導出減法公式。"
            },
            {
                "num": 3,
                "title": "線索 3：還原恆等式",
                "content": "若令 $\\log_a M = k$，則依定義 $a^k = M$。將 $k = \\log_a M$ 代回即得 $a^{\\log_a M} = M$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】同底對數加減化為真數乘除，次方提前化簡：$\\log_a (MN) = \\log_a M + \\log_a N, \\log_{a^r} M^s = \\frac{s}{r}\\log_a M$",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#38bdf8\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"12\" y=\"10\" width=\"356\" height=\"170\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-0.5\">\n      <div class=\"text-xs font-bold text-sky-900 tracking-wide\">五大基本對數運算性質速覽</div>\n      <div class=\"grid grid-cols-2 gap-2 w-full px-1 my-1\">\n        <div class=\"bg-sky-50 border border-sky-300 rounded-lg p-1.5 text-center shadow-2xs\">\n          <div class=\"text-[10px] font-bold text-sky-700\">1. 特殊值</div>\n          <div class=\"text-xs font-bold text-sky-900 mt-0.5\">$\\log_a 1 = 0 \\ , \\ \\log_a a = 1$</div>\n        </div>\n        <div class=\"bg-amber-50 border border-amber-300 rounded-lg p-1.5 text-center shadow-2xs\">\n          <div class=\"text-[10px] font-bold text-amber-700\">2. 次方提出律</div>\n          <div class=\"text-xs font-bold text-amber-900 mt-0.5\">$\\log_{a^r} M^s = \\frac{s}{r}\\log_a M$</div>\n        </div>\n        <div class=\"bg-emerald-50 border border-emerald-300 rounded-lg p-1.5 text-center shadow-2xs\">\n          <div class=\"text-[10px] font-bold text-emerald-700\">3. 和化積 / 差化商</div>\n          <div class=\"text-[11px] font-bold text-emerald-900 mt-0.5\">$\\log_a M \\pm \\log_a N = \\log_a(M \\cdot N^{\\pm 1})$</div>\n        </div>\n        <div class=\"bg-purple-50 border border-purple-300 rounded-lg p-1.5 text-center shadow-2xs\">\n          <div class=\"text-[10px] font-bold text-purple-700\">4. 互消恆等式</div>\n          <div class=\"text-xs font-bold text-purple-900 mt-0.5\">$a^{\\log_a M} = M$</div>\n        </div>\n      </div>\n      <div class=\"text-[10px] text-slate-600 bg-white px-2 py-0.5 rounded border border-slate-200 text-center w-full\">\n        口訣：同底相加真數相乘、同底相減真數相除、次方提出前做係數\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 4,
        "tag": "CASE 04",
        "page": "課本 p.78-79",
        "category": "換底連鎖",
        "title": "換底公式、連鎖律與倒數性質",
        "front_content": "設 $a, b, c, d$ 均為非 1 正實數，$M > 0$：<br>6. 換底公式：$\\log_a M = \\frac{\\log_c M}{\\log_c a}$<br>7. 連鎖律：$\\log_a b \\times \\log_b c \\times \\log_c d = \\log_a d$<br>8. 倒數性質：$\\log_a b = \\frac{1}{\\log_b a}$",
        "front_tip": "🕵️ 柯南破案導引：遇到異底對數時，統一換成常用底數 10，即可如多項式分數般進行上下交叉約分！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換底公式之推導",
                "content": "令 $\\log_a M = r \\implies M = a^r$。兩邊取以 $c$ 為底的對數：$\\log_c M = \\log_c a^r = r\\log_c a$。移項得 $r = \\frac{\\log_c M}{\\log_c a}$。"
            },
            {
                "num": 2,
                "title": "線索 2：連鎖律之約分效應",
                "content": "利用換底公式將各項換為以 10 為底：$\\frac{\\log b}{\\log a} \\times \\frac{\\log c}{\\log b} \\times \\frac{\\log d}{\\log c} = \\frac{\\log d}{\\log a} = \\log_a d$。中間項分子分母完全約去。"
            },
            {
                "num": 3,
                "title": "線索 3：底真數對調之倒數關係",
                "content": "令 $d = a$ 代入連鎖律：$\\log_a b \\times \\log_b a = \\log_a a = 1$，故 $\\log_a b = \\frac{1}{\\log_b a}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】換底公式：$\\log_a M = \\frac{\\log_c M}{\\log_c a}$；連鎖約分：$\\log_a b \\times \\log_b c = \\log_a c$；倒數：$\\log_a b \\times \\log_b a = 1$",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#fdf4ff\" stroke=\"#e879f9\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"12\" y=\"10\" width=\"356\" height=\"170\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-1\">\n      <div class=\"text-xs font-bold text-fuchsia-950 tracking-wide\">換底公式與骨牌式連鎖律</div>\n      <div class=\"flex justify-between items-center w-full gap-3 px-1 my-1\">\n        <div class=\"bg-white border-2 border-fuchsia-300 rounded-xl p-2.5 text-center flex-1 shadow-xs\">\n          <div class=\"text-xs font-bold text-fuchsia-700 mb-1\">換底公式</div>\n          <div class=\"text-sm font-bold text-fuchsia-900\">$\\log_a M = \\frac{\\log_c M}{\\log_c a}$</div>\n          <div class=\"text-[10px] text-slate-500 mt-1\">可引進任意新底數 $c$</div>\n        </div>\n        <div class=\"bg-white border-2 border-fuchsia-300 rounded-xl p-2.5 text-center flex-1 shadow-xs\">\n          <div class=\"text-xs font-bold text-fuchsia-700 mb-1\">連鎖律 (骨牌約分)</div>\n          <div class=\"text-sm font-bold text-fuchsia-900\">$\\log_a b \\cdot \\log_b c = \\log_a c$</div>\n          <div class=\"text-[10px] text-slate-500 mt-1\">倒數：$\\log_a b = \\frac{1}{\\log_b a}$</div>\n        </div>\n      </div>\n      <div class=\"text-[11px] font-semibold text-slate-700 bg-white px-3 py-1 rounded-lg border border-fuchsia-200 shadow-2xs text-center w-full\">\n        核心應用：面對異底對數乘積時，統一換成常用底數 10 進行上下約分\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 5,
        "tag": "CASE 05",
        "page": "課本 p.75",
        "category": "存在條件",
        "title": "對數的定義辨析",
        "front_content": "下列各式哪幾個是有意義的對數？<br>(A) $\\log_1 5$<br>(B) $\\log_5 1$<br>(C) $\\log_{-2} 3$<br>(D) $\\log_2 \\frac{1}{5}$<br>(E) $\\log_3 (-4)$",
        "front_tip": "🕵️ 柯南破案導引：審題重點：檢核底數是否滿足「$a > 0, a \\ne 1$」，並檢核真數是否滿足「$b > 0$」。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：檢驗 (A)、(B)",
                "content": "(A) $\\log_1 5$ 底數為 1，不合規定（底數不可為 1）。<br>(B) $\\log_5 1$ 底數 $5 > 0, 5 \\ne 1$，真數 $1 > 0$，符合定義（值為 0）。"
            },
            {
                "num": 2,
                "title": "線索 2：檢驗 (C)、(D)",
                "content": "(C) $\\log_{-2} 3$ 底數為 $-2 < 0$，不合規定。<br>(D) $\\log_2 \\frac{1}{5}$ 底數 $2 > 0, 2 \\ne 1$，真數 $\\frac{1}{5} > 0$，符合定義。"
            },
            {
                "num": 3,
                "title": "線索 3：檢驗 (E) 並結論",
                "content": "(E) $\\log_3 (-4)$ 真數為 $-4 < 0$，不合規定（真數必須大於 0）。故僅 (B)、(D) 有意義。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確選項為 (B)、(D)",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"170\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between text-xs py-1\">\n      <div class=\"font-bold text-slate-800 text-center pb-1 border-b border-slate-200\">例題 1 各選項定義檢核</div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(A) $\\log_1 5$</span> <span class=\"text-rose-700\">✕ 底數為 1 不合</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-emerald-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(B) $\\log_5 1 = 0$</span> <span class=\"text-emerald-700\">✓ 底數 $5 > 0, \\ne 1$；真數 $1 > 0$</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(C) $\\log_{-2} 3$</span> <span class=\"text-rose-700\">✕ 底數 $-2 < 0$</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-emerald-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(D) $\\log_2 \\frac{1}{5}$</span> <span class=\"text-emerald-700\">✓ 底數 $2 > 0, \\ne 1$；真數 $\\frac{1}{5} > 0$</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(E) $\\log_3 (-4)$</span> <span class=\"text-rose-700\">✕ 真數 $-4 < 0$</span>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 6,
        "tag": "CASE 06",
        "page": "課本 p.75",
        "category": "存在條件",
        "title": "對數的定義辨析",
        "front_content": "下列各式哪幾個是有意義的對數？<br>(A) $\\log_2 0$<br>(B) $\\log_0 2$<br>(C) $\\log_{\\frac{1}{2}} 5$<br>(D) $\\log_{\\frac{1}{2}} \\frac{5}{3}$<br>(E) $\\log_{-3} (-2)$",
        "front_tip": "🕵️ 柯南破案導引：嚴格把握「底數 $>0$ 且 $\\ne 1$；真數 $>0$」。負數或 0 均不合法！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：檢驗 (A)、(B)",
                "content": "(A) $\\log_2 0$ 真數為 0，不合（真數必須嚴格大於 0）。<br>(B) $\\log_0 2$ 底數為 0，不合（底數必須嚴格大於 0）。"
            },
            {
                "num": 2,
                "title": "線索 2：檢驗 (C)、(D)",
                "content": "(C) $\\log_{\\frac{1}{2}} 5$ 底數 $\\frac{1}{2} > 0, \\ne 1$，真數 $5 > 0$，符合定義。<br>(D) $\\log_{\\frac{1}{2}} \\frac{5}{3}$ 底數 $\\frac{1}{2} > 0, \\ne 1$，真數 $\\frac{5}{3} > 0$，符合定義。"
            },
            {
                "num": 3,
                "title": "線索 3：檢驗 (E) 並結論",
                "content": "(E) $\\log_{-3} (-2)$ 底數 $-3 < 0$ 且真數 $-2 < 0$，兩者均不合。故只有 (C)、(D) 有意義。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確選項為 (C)、(D)",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"170\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between text-xs py-1\">\n      <div class=\"font-bold text-slate-800 text-center pb-1 border-b border-slate-200\">隨堂練習 1 定義檢核結果</div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(A) $\\log_2 0$</span> <span class=\"text-rose-700\">✕ 真數不可為 0</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(B) $\\log_0 2$</span> <span class=\"text-rose-700\">✕ 底數不可為 0</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-emerald-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(C) $\\log_{\\frac{1}{2}} 5$</span> <span class=\"text-emerald-700\">✓ 底數 $\\frac{1}{2} > 0, \\ne 1$；真數 $5 > 0$</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-emerald-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(D) $\\log_{\\frac{1}{2}} \\frac{5}{3}$</span> <span class=\"text-emerald-700\">✓ 底數與真數均為正數</span>\n      </div>\n      <div class=\"flex items-center justify-between px-2 text-rose-600 font-semibold bg-white py-1 rounded border border-slate-100\">\n        <span>(E) $\\log_{-3} (-2)$</span> <span class=\"text-rose-700\">✕ 底數與真數均為負數</span>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 7,
        "tag": "CASE 07",
        "page": "課本 p.76",
        "category": "存在條件",
        "title": "對數存在的必要條件",
        "front_content": "若 $\\log_{x-1}(x + 5)$ 有意義，<br>則 $x$ 的範圍為何？",
        "front_tip": "🕵️ 柯南破案導引：列出不等式組：真數 $> 0$、底數 $> 0$ 且底數 $\\ne 1$，最後在數線上取三者交集！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：列出真數條件",
                "content": "真數必須大於 0：$x + 5 > 0 \\implies x > -5$。"
            },
            {
                "num": 2,
                "title": "線索 2：列出底數條件",
                "content": "底數必須大於 0 且不為 1：$x - 1 > 0 \\implies x > 1$；且 $x - 1 \\ne 1 \\implies x \\ne 2$。"
            },
            {
                "num": 3,
                "title": "線索 3：數線交集得出範圍",
                "content": "綜合以上：$x > -5$ 與 $x > 1$ 取交集為 $x > 1$，且排除 $x = 2$。故 $x > 1$ 且 $x \\ne 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$x > 1$ 且 $x \\ne 2$",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <line x1=\"30\" y1=\"110\" x2=\"350\" y2=\"110\" stroke=\"#64748b\" stroke-width=\"2\"/>\n  <circle cx=\"100\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"100\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">0</text>\n  <circle cx=\"170\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"170\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">1</text>\n  <circle cx=\"230\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"230\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">2</text>\n  <path d=\"M 170 110 L 170 75 L 340 75\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.5\"/>\n  <circle cx=\"170\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#2563eb\" stroke-width=\"2\"/>\n  <circle cx=\"230\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#dc2626\" stroke-width=\"2\"/>\n  <foreignObject x=\"12\" y=\"8\" width=\"356\" height=\"174\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-1\">\n      <div class=\"text-xs font-bold text-slate-800\">數線交集圖解：$x > 1$ 且 $x \\ne 2$</div>\n      <div class=\"flex justify-between w-full px-6 text-xs font-bold\">\n        <div class=\"text-blue-600\">真數條件：$x - 1 > 0 \\implies x > 1$</div>\n        <div class=\"text-rose-600\">挖空：$x \\ne 2$</div>\n      </div>\n      <div class=\"h-10\"></div>\n      <div class=\"text-xs font-bold text-slate-800 bg-white px-3 py-1 rounded-lg border border-slate-200 shadow-2xs\">\n        解集合：$x > 1 \\text{ 且 } x \\ne 2$\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 8,
        "tag": "CASE 08",
        "page": "課本 p.76",
        "category": "存在條件",
        "title": "對數存在的必要條件",
        "front_content": "若 $\\log_{x+2}(3 - x)$ 有意義，<br>則 $x$ 的範圍為何？",
        "front_tip": "🕵️ 柯南破案導引：真數 $3-x > 0$，底數 $x+2 > 0$ 且 $x+2 \\ne 1$。注意負號移項變號！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：列出真數條件",
                "content": "真數必須大於 0：$3 - x > 0 \\implies x < 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：列出底數條件",
                "content": "底數必須大於 0 且不為 1：$x + 2 > 0 \\implies x > -2$；且 $x + 2 \\ne 1 \\implies x \\ne -1$。"
            },
            {
                "num": 3,
                "title": "線索 3：求交集得出區間",
                "content": "取 $x < 3$ 與 $x > -2$ 的交集得 $-2 < x < 3$；再扣除 $x = -1$，得 $-2 < x < 3$ 且 $x \\ne -1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$-2 < x < 3$ 且 $x \\ne -1$",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <line x1=\"30\" y1=\"110\" x2=\"350\" y2=\"110\" stroke=\"#64748b\" stroke-width=\"2\"/>\n  <circle cx=\"80\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"80\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">-2</text>\n  <circle cx=\"140\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"140\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">-1</text>\n  <circle cx=\"280\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"280\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">3</text>\n  <path d=\"M 80 110 L 80 75 L 280 75 L 280 110\" fill=\"none\" stroke=\"#16a34a\" stroke-width=\"2.5\"/>\n  <circle cx=\"80\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#16a34a\" stroke-width=\"2\"/>\n  <circle cx=\"280\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#16a34a\" stroke-width=\"2\"/>\n  <circle cx=\"140\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#dc2626\" stroke-width=\"2\"/>\n  <foreignObject x=\"12\" y=\"8\" width=\"356\" height=\"174\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-1\">\n      <div class=\"text-xs font-bold text-slate-800\">數線交集圖解：$-2 < x < 3$ 且 $x \\ne -1$</div>\n      <div class=\"flex justify-between w-full px-6 text-xs font-bold\">\n        <div class=\"text-emerald-600\">真數與底數交集：$-2 < x < 3$</div>\n        <div class=\"text-rose-600\">挖空：$x \\ne -1$</div>\n      </div>\n      <div class=\"h-10\"></div>\n      <div class=\"text-xs font-bold text-slate-800 bg-white px-3 py-1 rounded-lg border border-slate-200 shadow-2xs\">\n        解集合：$-2 < x < 3 \\text{ 且 } x \\ne -1$\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 9,
        "tag": "CASE 09",
        "page": "課本 p.76",
        "category": "對數求值",
        "title": "對數求值：以 2 為底",
        "front_content": "試求下列對數之值：<br>$\\log_2 64$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：將真數 64 化為以底數 2 為基底的指數次方形式：$64 = 2^k$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：質因數分解真數",
                "content": "$64 = 2 \\times 32 = 2 \\times 2^5 = 2^6$。"
            },
            {
                "num": 2,
                "title": "線索 2：套用對數定義求值",
                "content": "由定義 $2^6 = 64 \\iff \\log_2 64 = 6$（或使用 $\\log_2 2^6 = 6\\log_2 2 = 6 \\times 1 = 6$）。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_2 64 = 6$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">指數轉換還原法</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$64 = 2^6$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 64 = 6$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 10,
        "tag": "CASE 10",
        "page": "課本 p.76",
        "category": "對數求值",
        "title": "對數求值：負指數型",
        "front_content": "試求下列對數之值：<br>$\\log_3 \\frac{1}{81}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：真數是分數，利用負指數關係：$\\frac{1}{a^n} = a^{-n}$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：將真數化為底數 3 的次方",
                "content": "$81 = 3^4$，因此分數 $\\frac{1}{81} = \\frac{1}{3^4} = 3^{-4}$。"
            },
            {
                "num": 2,
                "title": "線索 2：由定義求得對數值",
                "content": "因為 $3^{-4} = \\frac{1}{81}$，所以 $\\log_3 \\frac{1}{81} = -4$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 \\frac{1}{81} = -4$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">負指數轉化求值</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\frac{1}{81} = \\frac{1}{3^4} = 3^{-4}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_3 \\frac{1}{81} = -4$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 11,
        "tag": "CASE 11",
        "page": "課本 p.76",
        "category": "對數求值",
        "title": "對數求值：小數底數型",
        "front_content": "試求下列對數之值：<br>$\\log_{0.1} 0.001$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：觀察 $0.1$ 的幾次方會等於 $0.001$？注意小數位數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：觀察小數自乘次數",
                "content": "$0.1 = 10^{-1}$，$0.001 = 10^{-3} = (0.1)^3$。"
            },
            {
                "num": 2,
                "title": "線索 2：套用定義得解",
                "content": "因為 $(0.1)^3 = 0.001$，故 $\\log_{0.1} 0.001 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{0.1} 0.001 = 3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">小數連乘轉化</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$0.001 = (0.1)^3$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{0.1} 0.001 = 3$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 12,
        "tag": "CASE 12",
        "page": "課本 p.76",
        "category": "對數求值",
        "title": "對數求值：底數大於真數",
        "front_content": "試求下列對數之值：<br>$\\log_{25} 5$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：真數比底數小，開根號即為 $\\frac{1}{2}$ 次方：$25^k = 5$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：列出指數對應式",
                "content": "設 $25^k = 5$。由於 $\\sqrt{25} = 5$，亦即 $25^{\\frac{1}{2}} = 5$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出對數值",
                "content": "因為 $25^{\\frac{1}{2}} = 5$，所以 $\\log_{25} 5 = \\frac{1}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{25} 5 = \\frac{1}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">方根指數化轉化</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\sqrt[3]{25} = (5^2)^{\\frac{1}{3}} = 5^{\\frac{2}{3}}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_5 \\sqrt[3]{25} = \\frac{2}{3}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 13,
        "tag": "CASE 13",
        "page": "課本 p.77",
        "category": "對數求值",
        "title": "對數求值：以 3 為底",
        "front_content": "試求下列對數之值：<br>$\\log_3 27$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：思考 3 的幾次方等於 27？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：真數指數化",
                "content": "$27 = 3 \\times 3 \\times 3 = 3^3$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出對數值",
                "content": "因為 $3^3 = 27$，故 $\\log_3 27 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 27 = 3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">指數還原法</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$81 = 3^4$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_3 81 = 4$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 14,
        "tag": "CASE 14",
        "page": "課本 p.77",
        "category": "對數求值",
        "title": "對數求值：分數真數",
        "front_content": "試求下列對數之值：<br>$\\log_2 \\frac{1}{32}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：$32 = 2^5$，分數取倒數為負指數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分數轉負指數",
                "content": "$32 = 2^5 \\implies \\frac{1}{32} = 2^{-5}$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出對數值",
                "content": "因為 $2^{-5} = \\frac{1}{32}$，所以 $\\log_2 \\frac{1}{32} = -5$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_2 \\frac{1}{32} = -5$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">負指數轉化求值</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\frac{1}{32} = 2^{-5}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 \\frac{1}{32} = -5$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 15,
        "tag": "CASE 15",
        "page": "課本 p.77",
        "category": "對數求值",
        "title": "對數求值：分數底數與真數",
        "front_content": "試求下列對數之值：<br>$\\log_{\\frac{1}{5}} \\frac{1}{625}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：檢視底數 $\\frac{1}{5}$ 要自乘幾次會得到 $\\frac{1}{625}$？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：觀察分子分母次方",
                "content": "$625 = 5^4$，因此 $\\frac{1}{625} = (\\frac{1}{5})^4$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出對數值",
                "content": "因為 $(\\frac{1}{5})^4 = \\frac{1}{625}$，所以 $\\log_{\\frac{1}{5}} \\frac{1}{625} = 4$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{\\frac{1}{5}} \\frac{1}{625} = 4$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fefce8\" stroke=\"#eab308\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-amber-900 tracking-wide\">小數自乘轉化</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-amber-700\">$0.25 = (0.5)^2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{0.5} 0.25 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 16,
        "tag": "CASE 16",
        "page": "課本 p.77",
        "category": "對數求值",
        "title": "對數求值：分數底與整數真數",
        "front_content": "試求下列對數之值：<br>$\\log_{\\frac{1}{4}} 64$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：底數是 $\\frac{1}{4} = 4^{-1}$，真數是 $64 = 4^3$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：統一化為基底 4",
                "content": "底數為 $\\frac{1}{4} = 4^{-1}$，真數為 $64 = 4^3$。"
            },
            {
                "num": 2,
                "title": "線索 2：列出指數式求解",
                "content": "$(\\frac{1}{4})^{-3} = (4^{-1})^{-3} = 4^3 = 64$。故 $\\log_{\\frac{1}{4}} 64 = -3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{\\frac{1}{4}} 64 = -3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">方根指數化轉化</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\sqrt[4]{8} = (2^3)^{\\frac{1}{4}} = 2^{\\frac{3}{4}}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 \\sqrt[4]{8} = \\frac{3}{4}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 17,
        "tag": "CASE 17",
        "page": "課本 p.79",
        "category": "基本性質",
        "title": "對數基本性質：真數為 1 與底真相同",
        "front_content": "試求下列各式的值：<br>$\\log_5 1 + \\log_3 3$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：$\\log_a 1 = 0$ 且 $\\log_a a = 1$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分別計算兩項",
                "content": "第一項：因為 $5^0 = 1$，所以 $\\log_5 1 = 0$。<br>第二項：因為 $3^1 = 3$，所以 $\\log_3 3 = 1$。"
            },
            {
                "num": 2,
                "title": "線索 2：兩項相加",
                "content": "$0 + 1 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_5 1 + \\log_3 3 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">基本性質：特殊值相加</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_5 1 = 0 \\ , \\ \\log_3 3 = 1$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$0 + 1 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 18,
        "tag": "CASE 18",
        "page": "課本 p.79",
        "category": "基本性質",
        "title": "對數基本性質：方根真數提出",
        "front_content": "試求下列各式的值：<br>$\\log_3 \\sqrt{3}$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：根號轉為指數：$\\sqrt{3} = 3^{\\frac{1}{2}}$，利用 $\\log_a M^s = s\\log_a M$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：真數轉分數指數",
                "content": "$\\sqrt{3} = 3^{\\frac{1}{2}}$。"
            },
            {
                "num": 2,
                "title": "線索 2：次方提前化簡",
                "content": "$\\log_3 3^{\\frac{1}{2}} = \\frac{1}{2}\\log_3 3 = \\frac{1}{2} \\times 1 = \\frac{1}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 \\sqrt{3} = \\frac{1}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">次方提出律</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{2^2} 2^3 = \\frac{3}{2}\\log_2 2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\frac{3}{2} \\times 1 = \\frac{3}{2}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 19,
        "tag": "CASE 19",
        "page": "課本 p.79",
        "category": "基本性質",
        "title": "對數基本性質：特徵值求和",
        "front_content": "試求下列各式的值：<br>$\\log_{0.25} 1 + \\log_{100} 100$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：不論底數為何，只要真數為 1 則值為 0；底數真數相同則值為 1。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分項計算",
                "content": "$\\log_{0.25} 1 = 0$（真數為 1）；$\\log_{100} 100 = 1$（底真相同）。"
            },
            {
                "num": 2,
                "title": "線索 2：兩數相加",
                "content": "$0 + 1 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{0.25} 1 + \\log_{100} 100 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">基本性質：特殊值相減</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_7 7 = 1 \\ , \\ \\log_4 1 = 0$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1 - 0 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 20,
        "tag": "CASE 20",
        "page": "課本 p.79",
        "category": "基本性質",
        "title": "對數基本性質：底數與真數次方提出",
        "front_content": "試求下列各式的值：<br>$\\log_{25} 125$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：底數 $25 = 5^2$，真數 $125 = 5^3$，利用 $\\log_{a^r} M^s = \\frac{s}{r}\\log_a M$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：底數與真數質因數分解",
                "content": "$25 = 5^2$，$125 = 5^3$。原式寫為 $\\log_{5^2} 5^3$。"
            },
            {
                "num": 2,
                "title": "線索 2：提出次方計算",
                "content": "$\\log_{5^2} 5^3 = \\frac{3}{2}\\log_5 5 = \\frac{3}{2} \\times 1 = \\frac{3}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{25} 125 = \\frac{3}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">底真數化為質因數次方</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log_{2^3} 2^4 = \\frac{4}{3}\\log_2 2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\frac{4}{3} \\times 1 = \\frac{4}{3}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 21,
        "tag": "CASE 21",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數加法性質：同底對數相加",
        "front_content": "試求下列各式的值：<br>$\\log_6 9 + \\log_6 4$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：同底對數相加，真數相乘：$\\log_a M + \\log_a N = \\log_a (MN)$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合併真數相乘",
                "content": "$\\log_6 9 + \\log_6 4 = \\log_6(9 \\times 4) = \\log_6 36$。"
            },
            {
                "num": 2,
                "title": "線索 2：化簡對數值",
                "content": "$\\log_6 36 = \\log_6 6^2 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_6 9 + \\log_6 4 = 2$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">同底對數加法化為真數乘積</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_6 4 + \\log_6 9 = \\log_6(4 \\times 9)$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_6 36 = \\log_6 6^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 22,
        "tag": "CASE 22",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數減法性質：同底對數相減",
        "front_content": "試求下列各式的值：<br>$\\log_5 45 - \\log_5 9$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：同底對數相減，真數相除：$\\log_a M - \\log_a N = \\log_a \\frac{M}{N}$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合併真數相除",
                "content": "$\\log_5 45 - \\log_5 9 = \\log_5\\left(\\frac{45}{9}\\right) = \\log_5 5$。"
            },
            {
                "num": 2,
                "title": "線索 2：得出結果",
                "content": "$\\log_5 5 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_5 45 - \\log_5 9 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">同底對數減法化為真數相除</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_2 24 - \\log_2 3 = \\log_2 \\frac{24}{3}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 8 = \\log_2 2^3 = 3$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 23,
        "tag": "CASE 23",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數連加連減綜合運算",
        "front_content": "試求下列各式的值：<br>$\\log_3 36 - \\log_3 8 + \\log_3 54$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：同底對數加減，正項真數放分子相乘，負項真數放分母相除！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：綜合成單一真數乘除",
                "content": "$\\log_3 36 - \\log_3 8 + \\log_3 54 = \\log_3\\left(\\frac{36 \\times 54}{8}\\right)$。"
            },
            {
                "num": 2,
                "title": "線索 2：約分化簡分子分母",
                "content": "$\\frac{36 \\times 54}{8} = \\frac{9 \\times 54}{2} = 9 \\times 27 = 243$。"
            },
            {
                "num": 3,
                "title": "線索 3：以 3 為底求值",
                "content": "$243 = 3^5$，故 $\\log_3 243 = 5$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 36 - \\log_3 8 + \\log_3 54 = 5$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">同底連續加減連乘連除</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log_4 \\frac{12 \\times 24}{18} = \\log_4 16$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_4 4^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 24,
        "tag": "CASE 24",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數加法性質求值",
        "front_content": "試求下列各式的值：<br>$\\log_8 16 + \\log_8 32$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：同底相加合為真數相乘，再將底數 8 與真數統一化為 2 的次方！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合為真數乘積",
                "content": "$\\log_8 16 + \\log_8 32 = \\log_8(16 \\times 32) = \\log_8(2^4 \\times 2^5) = \\log_8 2^9$。"
            },
            {
                "num": 2,
                "title": "線索 2：底數 8 化為 2 的次方提係數",
                "content": "$8 = 2^3$，故 $\\log_{2^3} 2^9 = \\frac{9}{3}\\log_2 2 = 3 \\times 1 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_8 16 + \\log_8 32 = 3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">同底相加真數相乘</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_2\\left(12 \\times \\frac{4}{3}\\right) = \\log_2 16$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 2^4 = 4$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 25,
        "tag": "CASE 25",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數減法性質求值",
        "front_content": "試求下列各式的值：<br>$\\log_3 18 - \\log_3 2$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：同底相減化為真數相除，計算 $18 \\div 2$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合為真數相除",
                "content": "$\\log_3 18 - \\log_3 2 = \\log_3\\left(\\frac{18}{2}\\right) = \\log_3 9$。"
            },
            {
                "num": 2,
                "title": "線索 2：化簡對數值",
                "content": "$9 = 3^2$，故 $\\log_3 9 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 18 - \\log_3 2 = 2$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">同底相減真數相除</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_{10} \\frac{20}{2} = \\log_{10} 10$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{10} 10 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 26,
        "tag": "CASE 26",
        "page": "課本 p.80",
        "category": "加減運算",
        "title": "對數綜合加減求值",
        "front_content": "試求下列各式的值：<br>$\\log_2 12 + \\log_2 40 - \\log_2 15$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：正項真數 12 與 40 放分子相乘，負項真數 15 放分母！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合併真數乘除",
                "content": "$\\log_2 12 + \\log_2 40 - \\log_2 15 = \\log_2\\left(\\frac{12 \\times 40}{15}\\right)$。"
            },
            {
                "num": 2,
                "title": "線索 2：約分計算",
                "content": "$\\frac{12 \\times 40}{15} = \\frac{4 \\times 40}{5} = 4 \\times 8 = 32$。"
            },
            {
                "num": 3,
                "title": "線索 3：得出對數值",
                "content": "$32 = 2^5$，故 $\\log_2 32 = 5$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_2 12 + \\log_2 40 - \\log_2 15 = 5$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">真數連續運算化簡</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log_3 \\frac{54 \\times 18}{12} = \\log_3 81$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_3 3^4 = 4$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 27,
        "tag": "CASE 27",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "換底公式之逆運算",
        "front_content": "試求下列各式的值：<br>$\\frac{\\log_5 32}{\\log_5 2}$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：換底公式逆向使用：$\\frac{\\log_c M}{\\log_c a} = \\log_a M$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：套用換底公式逆運算",
                "content": "分子分母底數同為 5，逆用換底公式：$\\frac{\\log_5 32}{\\log_5 2} = \\log_2 32$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算對數值",
                "content": "因為 $32 = 2^5$，所以 $\\log_2 32 = 5$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\frac{\\log_5 32}{\\log_5 2} = 5$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">係數移回真數次方化簡</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_3 6^2 - \\log_3 4 = \\log_3 \\frac{36}{4}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_3 9 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 28,
        "tag": "CASE 28",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "指數上的換底化簡",
        "front_content": "試求下列各式的值：<br>$5^{\\frac{\\log_2 7}{\\log_2 5}}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：先將次方的分式化簡為單一對數，再利用 $a^{\\log_a M} = M$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：化簡指數部分的對數分式",
                "content": "次方為 $\\frac{\\log_2 7}{\\log_2 5}$。由換底公式逆用，得 $\\frac{\\log_2 7}{\\log_2 5} = \\log_5 7$。"
            },
            {
                "num": 2,
                "title": "線索 2：代回原指數式消去",
                "content": "原式變為 $5^{\\log_5 7}$。利用底數相同抵消性質 $a^{\\log_a M} = M$，得結果為 $7$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$5^{\\frac{\\log_2 7}{\\log_2 5}} = 7$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">方根次方提出與商數化簡</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_5 \\sqrt{10} - \\log_5 \\sqrt{2} = \\log_5 \\sqrt{5}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_5 5^{\\frac{1}{2}} = \\frac{1}{2}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 29,
        "tag": "CASE 29",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "複合底數指數運算",
        "front_content": "試求下列各式的值：<br>$9^{\\log_3 5}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：底數 $9 = 3^2$，將次方 2 乘進對數或將 2 移入真數當次方！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：改寫底數 9 為 3 的平方",
                "content": "$9^{\\log_3 5} = (3^2)^{\\log_3 5} = 3^{2\\log_3 5}$。"
            },
            {
                "num": 2,
                "title": "線索 2：將係數 2 移回真數次方",
                "content": "$2\\log_3 5 = \\log_3 (5^2) = \\log_3 25$。"
            },
            {
                "num": 3,
                "title": "線索 3：互消得出結果",
                "content": "$3^{\\log_3 25} = 25$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$9^{\\log_3 5} = 25$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">常用對數係數還原化簡</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log 5^2 + \\log 4 = \\log(25 \\times 4)$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log 100 = \\log 10^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 30,
        "tag": "CASE 30",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "換底公式逆用求值",
        "front_content": "試求下列各式的值：<br>$\\frac{\\log_2 243}{\\log_2 9}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：分子分母同底，合為 $\\log_9 243$，再化為 3 的次方！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換底公式逆運算",
                "content": "$\\frac{\\log_2 243}{\\log_2 9} = \\log_9 243$。"
            },
            {
                "num": 2,
                "title": "線索 2：提出 3 的次方求值",
                "content": "$9 = 3^2, 243 = 3^5$。故 $\\log_{3^2} 3^5 = \\frac{5}{2}\\log_3 3 = \\frac{5}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\frac{\\log_2 243}{\\log_2 9} = \\frac{5}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">係數還原與同項相減</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_2 2^3 - \\log_2 8 = \\log_2 8 - \\log_2 8$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$0$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 31,
        "tag": "CASE 31",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "指數含零對數運算",
        "front_content": "試求下列各式的值：<br>$4^{\\frac{\\log_7 1}{\\log_7 3}}$",
        "front_tip": "🕵️ 柯南破案導引：關鍵突破：注意到分子 $\\log_7 1$ 是多少？任何以合規底數的 1 之對數值均為 0！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：計算分子的對數值",
                "content": "因為 $7^0 = 1$，所以 $\\log_7 1 = 0$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算次方分式與總值",
                "content": "次方為 $\\frac{0}{\\log_7 3} = 0$。因此 $4^0 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$4^{\\frac{\\log_7 1}{\\log_7 3}} = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">方根乘積整合化簡</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_6 \\sqrt{12} + \\log_6 \\sqrt{3} = \\log_6 \\sqrt{36}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_6 6 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 32,
        "tag": "CASE 32",
        "page": "課本 p.81",
        "category": "換底公式",
        "title": "指數對數次方消去求值",
        "front_content": "試求下列各式的值：<br>$3^{\\log_9 16}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：將 $\\log_9 16$ 化為以 3 為底數的對數：$\\log_{3^2} 4^2 = \\log_3 4$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：化簡對數項",
                "content": "$\\log_9 16 = \\log_{3^2} 4^2 = \\frac{2}{2}\\log_3 4 = \\log_3 4$。"
            },
            {
                "num": 2,
                "title": "線索 2：代回原指數式互消",
                "content": "$3^{\\log_9 16} = 3^{\\log_3 4} = 4$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$3^{\\log_9 16} = 4$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">三項係數還原連除運算</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log \\frac{2^2 \\times 75}{3} = \\log 100$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log 10^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 33,
        "tag": "CASE 33",
        "page": "課本 p.81",
        "category": "連鎖律",
        "title": "對數倒數性質乘積",
        "front_content": "試求下列各式的值：<br>$\\log_2 5 \\times \\log_5 2$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：底數真數顛倒互為倒數：$\\log_a b \\times \\log_b a = 1$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換為常用對數檢驗",
                "content": "$\\log_2 5 \\times \\log_5 2 = \\frac{\\log_{10} 5}{\\log_{10} 2} \\times \\frac{\\log_{10} 2}{\\log_{10} 5}$。"
            },
            {
                "num": 2,
                "title": "線索 2：交叉約分得出結論",
                "content": "分子與分母完全抵消，結果為 1。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_2 5 \\times \\log_5 2 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">對數倒數性質乘積</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\frac{\\log 5}{\\log 2} \\times \\frac{\\log 2}{\\log 5}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1$</div>\n      </div>\n      <div class=\"text-[10px] text-slate-500 text-center mt-0.5\">倒數相乘恆為 1</div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 34,
        "tag": "CASE 34",
        "page": "課本 p.81",
        "category": "連鎖律",
        "title": "三項對數連鎖律",
        "front_content": "試求下列各式的值：<br>$\\log_2 3 \\times \\log_3 5 \\times \\log_5 8$",
        "front_tip": "🕵️ 柯南破案導引：公式要點：連鎖律骨牌約分：$\\log_a b \\times \\log_b c \\times \\log_c d = \\log_a d$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：骨牌式首尾相接",
                "content": "前項真數 3 與中項底數 3 相約；中項真數 5 與後項底數 5 相約，首尾相接得 $\\log_2 8$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算結果",
                "content": "$8 = 2^3$，故 $\\log_2 8 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_2 3 \\times \\log_3 5 \\times \\log_5 8 = 3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">三項對數骨牌連鎖律</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_2 3 \\cdot \\log_3 5 \\cdot \\log_5 8 = \\log_2 8$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_2 2^3 = 3$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 35,
        "tag": "CASE 35",
        "page": "課本 p.82",
        "category": "連鎖律",
        "title": "對數倒數相乘求值",
        "front_content": "試求下列各式的值：<br>$\\log_4 6 \\times \\log_6 4$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：兩對數底真顛倒，相乘恆等於 1。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：檢驗底真關係",
                "content": "前項底數 4、真數 6；後項底數 6、真數 4，兩者互為倒數。"
            },
            {
                "num": 2,
                "title": "線索 2：連鎖約分得出結果",
                "content": "$\\log_4 6 \\times \\log_6 4 = \\log_4 4 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_4 6 \\times \\log_6 4 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">對數倒數相乘求值</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_4 6 \\times \\log_6 4 = \\log_4 4$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 36,
        "tag": "CASE 36",
        "page": "課本 p.82",
        "category": "連鎖律",
        "title": "三項連鎖律求值",
        "front_content": "試求下列各式的值：<br>$\\log_9 8 \\times \\log_8 7 \\times \\log_7 3$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：連鎖律串聯約分得首尾 $\\log_9 3$，再化為 3 的次方！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：連鎖首尾串聯",
                "content": "中間項真數 8 與底數 8 約去、真數 7 與底數 7 約去，得首尾 $\\log_9 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：化簡對數值",
                "content": "$9 = 3^2$，故 $\\log_9 3 = \\log_{3^2} 3^1 = \\frac{1}{2}\\log_3 3 = \\frac{1}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_9 8 \\times \\log_8 7 \\times \\log_7 3 = \\frac{1}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">三項連鎖律首尾相接</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log_9 8 \\cdot \\log_8 7 \\cdot \\log_7 3 = \\log_9 3$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{3^2} 3^1 = \\frac{1}{2}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 37,
        "tag": "CASE 37",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：質因數分解拆解真數",
        "front_content": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，<br>試以 $x, y$ 表示：<br>$\\log_{10} 12$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：將 12 做質因數分解：$12 = 2^2 \\times 3$，再拆成對數相加！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：真數質因數分解",
                "content": "$12 = 4 \\times 3 = 2^2 \\times 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：對數性質展開",
                "content": "$\\log_{10} 12 = \\log_{10}(2^2 \\times 3) = \\log_{10} 2^2 + \\log_{10} 3 = 2\\log_{10} 2 + \\log_{10} 3$。"
            },
            {
                "num": 3,
                "title": "線索 3：以 x, y 代換",
                "content": "代入 $\\log_{10} 2 = x, \\log_{10} 3 = y$，得 $2x + y$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} 12 = 2x + y$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">質因數分解拆解真數</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$12 = 2^2 \\times 3 \\implies \\log 12 = 2\\log 2 + \\log 3$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$2a + b$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 38,
        "tag": "CASE 38",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：分數真數拆解",
        "front_content": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，<br>試以 $x, y$ 表示：<br>$\\log_{10} \\frac{8}{9}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：分數拆成真數相減：$\\log_{10} 8 - \\log_{10} 9$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：商化為對數相減",
                "content": "$\\log_{10} \\frac{8}{9} = \\log_{10} 8 - \\log_{10} 9$。"
            },
            {
                "num": 2,
                "title": "線索 2：質因數次方提出",
                "content": "$8 = 2^3, 9 = 3^2$，故 $\\log_{10} 2^3 - \\log_{10} 3^2 = 3\\log_{10} 2 - 2\\log_{10} 3$。"
            },
            {
                "num": 3,
                "title": "線索 3：以 x, y 代換",
                "content": "$3x - 2y$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} \\frac{8}{9} = 3x - 2y$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">真數分數拆為對數差</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log \\frac{8}{9} = \\log 2^3 - \\log 3^2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$3a - 2b$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 39,
        "tag": "CASE 39",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：換底公式與基準代換",
        "front_content": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，<br>試以 $x, y$ 表示：<br>$\\log_3 40$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：底數為 3，已知條件為常用對數底數 10，先換底為 $\\frac{\\log_{10} 40}{\\log_{10} 3}$！注意 $40 = 4 \\times 10$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換為常用底數 10",
                "content": "$\\log_3 40 = \\frac{\\log_{10} 40}{\\log_{10} 3}$。"
            },
            {
                "num": 2,
                "title": "線索 2：拆解分子真數 40",
                "content": "$40 = 4 \\times 10 = 2^2 \\times 10$。分子為 $\\log_{10}(2^2 \\times 10) = 2\\log_{10} 2 + \\log_{10} 10 = 2x + 1$。"
            },
            {
                "num": 3,
                "title": "線索 3：結合分母得解",
                "content": "分母 $\\log_{10} 3 = y$。故整體為 $\\frac{2x + 1}{y}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_3 40 = \\frac{2x + 1}{y}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">換底公式代數表示</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\log_3 40 = \\frac{\\log 40}{\\log 3} = \\frac{2\\log 2 + 1}{\\log 3}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\frac{2a + 1}{b}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 40,
        "tag": "CASE 40",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：拆解乘積質因數",
        "front_content": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，<br>試以 $x, y$ 表示：<br>$\\log_{10} 45$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：將 45 做質因數分解：$45 = 9 \\times 5 = 3^2 \\times 5$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：真數質因數分解",
                "content": "$45 = 3^2 \\times 5$。"
            },
            {
                "num": 2,
                "title": "線索 2：展開並代入代數符號",
                "content": "$\\log_{10}(3^2 \\times 5) = 2\\log_{10} 3 + \\log_{10} 5 = 2x + y$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} 45 = 2x + y$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">乘積質因數拆解</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$45 = 3^2 \\times 5 \\implies 2\\log 3 + \\log 5$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$2a + b$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 41,
        "tag": "CASE 41",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：商拆為對數差",
        "front_content": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，<br>試以 $x, y$ 表示：<br>$\\log_{10} \\frac{25}{27}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：分子 $25 = 5^2$，分母 $27 = 3^3$，商化為差！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：展開為對數相減",
                "content": "$\\log_{10} \\frac{25}{27} = \\log_{10} 25 - \\log_{10} 27$。"
            },
            {
                "num": 2,
                "title": "線索 2：提出次方代換",
                "content": "$\\log_{10} 5^2 - \\log_{10} 3^3 = 2\\log_{10} 5 - 3\\log_{10} 3 = 2y - 3x$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} \\frac{25}{27} = 2y - 3x$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-emerald-900 tracking-wide\">商拆為對數差</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-emerald-700\">$\\log \\frac{25}{27} = 2\\log 5 - 3\\log 3$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-emerald-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$2b - 3a$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 42,
        "tag": "CASE 42",
        "page": "課本 p.82",
        "category": "綜合應用",
        "title": "代數表示：換底公式綜合應用",
        "front_content": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，<br>試以 $x, y$ 表示：<br>$\\log_{30} 15$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：換底為 10：$\\frac{\\log_{10} 15}{\\log_{10} 30}$，其中 $15 = 3 \\times 5$，$30 = 3 \\times 10$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換為常用對數",
                "content": "$\\log_{30} 15 = \\frac{\\log_{10} 15}{\\log_{10} 30}$。"
            },
            {
                "num": 2,
                "title": "線索 2：拆解分子與分母",
                "content": "分子：$\\log_{10}(3 \\times 5) = \\log_{10} 3 + \\log_{10} 5 = x + y$。<br>分母：$\\log_{10}(3 \\times 10) = \\log_{10} 3 + \\log_{10} 10 = x + 1$。"
            },
            {
                "num": 3,
                "title": "線索 3：得出代數式",
                "content": "$\\frac{x + y}{x + 1}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{30} 15 = \\frac{x + y}{x + 1}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#faf5ff\" stroke=\"#a855f7\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-purple-900 tracking-wide\">換底公式綜合代換</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-purple-700\">$\\frac{\\log 15}{\\log 30} = \\frac{\\log 3 + \\log 5}{\\log 3 + 1}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-purple-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\frac{a + b}{a + 1}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
]

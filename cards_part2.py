# -*- coding: utf-8 -*-
"""
cards_part2.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
圖解學習卡資料集 Part 2 (CASE 43 ~ CASE 65)
章末課後自我評量全套題卡（是非題、基礎題、進階題、生活素養題）
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦完備版標準：
- 堅持「一題一卡、一小題獨立成卡」
- 課本習題 100% 忠實原文
- 是非題獨立成卡且正面提供反例解析
- 全欄位 100% KaTeX 標準數學式
- 正面無水平捲軸，適度 <br> 換行
- 2~4 步結構化思維導引（名偵探推理筆記 ‧ 線索推理鏈）
- 高解析 SVG 向量圖解
"""

CARDS_PART2 = [
    {
        "id": 43,
        "tag": "是非 1",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "觀念辨析：$\\log_a 1$ 的值",
        "front_content": "【觀念是非題】<br>若 $a > 0$ 且 $a \\ne 1$，則 $\\log_a 1 = 0$ 恆成立。<br><br>請判斷本敘述為 <b>○ 正確</b> 或 <b>✕ 錯誤</b>？",
        "front_tip": "🕵️ 柯南破案導引：由指數定義：任何非零實數的 0 次方為何值？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：回顧指數式",
                "content": "若底數 $a > 0$ 且 $a \\ne 1$，因為 $a^0 = 1$ 恆成立。"
            },
            {
                "num": 2,
                "title": "線索 2：轉化為對數定義",
                "content": "由對數定義 $a^x = b \\iff x = \\log_a b$，當 $x = 0, b = 1$ 時，必有 $\\log_a 1 = 0$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確答案為 ○（真數為 1 時對數值恆為 0）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#f0fdf4\" stroke=\"#22c55e\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex items-center justify-between px-3\">\n      <div class=\"flex flex-col items-center justify-center\">\n        <div class=\"w-14 h-14 rounded-full bg-emerald-600 text-white flex items-center justify-center text-3xl font-black shadow-md\">○</div>\n        <div class=\"text-xs font-bold text-emerald-800 mt-1\">恆真命題</div>\n      </div>\n      <div class=\"flex flex-col gap-2 flex-1 ml-4 bg-white p-3 rounded-xl border border-emerald-200 shadow-2xs\">\n        <div class=\"text-sm font-bold text-emerald-900\">$a^0 = 1$ 恆成立（$a > 0, a \\ne 1$）</div>\n        <div class=\"text-xs font-semibold text-emerald-700\">故 $\\log_a 1 = 0$ 恆為真！</div>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 44,
        "tag": "是非 2",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "觀念辨析：真數相加與對數相加",
        "front_content": "【觀念是非題】<br>$\\log_a (M + N) = \\log_a M + \\log_a N$ 恆成立。<br><br>請判斷本敘述為 <b>○ 正確</b> 或 <b>✕ 錯誤</b>？",
        "front_tip": "🕵️ 柯南破案導引：反例引導：代入簡單數值檢驗，例如 $M = 2, N = 2$ 或 $M = 1, N = 1$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：正確公式辨析",
                "content": "正確的對數加法性質為「同底相加化為真數相乘」：$\\log_a M + \\log_a N = \\log_a (MN)$，而非真數相加！"
            },
            {
                "num": 2,
                "title": "線索 2：舉出具體反例",
                "content": "設 $a = 2, M = 2, N = 2$：左式為 $\\log_2 (2 + 2) = \\log_2 4 = 2$；右式為 $\\log_2 2 + \\log_2 2 = 1 + 1 = 2$（恰巧相等）。再取 $M = 1, N = 1$：左式為 $\\log_2 (1 + 1) = \\log_2 2 = 1$；右式為 $\\log_2 1 + \\log_2 1 = 0 + 0 = 0 \\ne 1$。故不恆成立！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確答案為 ✕（真數相加不可拆開；對數相加為真數相乘）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fef2f2\" stroke=\"#ef4444\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex items-center justify-between px-3\">\n      <div class=\"flex flex-col items-center justify-center\">\n        <div class=\"w-14 h-14 rounded-full bg-rose-600 text-white flex items-center justify-center text-3xl font-black shadow-md\">✕</div>\n        <div class=\"text-xs font-bold text-rose-800 mt-1\">概念錯誤</div>\n      </div>\n      <div class=\"flex flex-col gap-1.5 flex-1 ml-4 bg-white p-2.5 rounded-xl border border-rose-200 shadow-2xs\">\n        <div class=\"text-xs font-bold text-rose-700\">✕ 錯誤：$\\log_a(M + N) \\ne \\log_a M + \\log_a N$</div>\n        <div class=\"text-xs font-bold text-emerald-700\">✓ 正確：$\\log_a(MN) = \\log_a M + \\log_a N$</div>\n        <div class=\"text-[10px] text-slate-500\">反例：$\\log(1+1) \\ne \\log 1 + \\log 1 = 0$</div>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 45,
        "tag": "是非 3",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "觀念辨析：對數相除與對數相減",
        "front_content": "【觀念是非題】<br>$\\frac{\\log_a M}{\\log_a N} = \\log_a (M - N)$ 恆成立。<br><br>請判斷本敘述為 <b>○ 正確</b> 或 <b>✕ 錯誤</b>？",
        "front_tip": "🕵️ 柯南破案導引：公式辨析：對數相除 $\\frac{\\log_a M}{\\log_a N}$ 是什麼公式？對數相減 $\\log_a M - \\log_a N$ 又是什麼？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：辨析兩側性質",
                "content": "左式 $\\frac{\\log_a M}{\\log_a N}$ 為換底公式逆用，等於 $\\log_N M$；而右式 $\\log_a (M - N)$ 真數相減不可拆解。"
            },
            {
                "num": 2,
                "title": "線索 2：正確減法公式",
                "content": "正確的減法公式為 $\\log_a M - \\log_a N = \\log_a \\frac{M}{N}$（是真數相除，不是對數相除）。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確答案為 ✕（$\\frac{\\log_a M}{\\log_a N} = \\log_N M$ 為換底公式，不等於 $\\log_a (M - N)$）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fef2f2\" stroke=\"#ef4444\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex items-center justify-between px-3\">\n      <div class=\"flex flex-col items-center justify-center\">\n        <div class=\"w-14 h-14 rounded-full bg-rose-600 text-white flex items-center justify-center text-3xl font-black shadow-md\">✕</div>\n        <div class=\"text-xs font-bold text-rose-800 mt-1\">概念錯誤</div>\n      </div>\n      <div class=\"flex flex-col gap-1.5 flex-1 ml-4 bg-white p-2.5 rounded-xl border border-rose-200 shadow-2xs\">\n        <div class=\"text-xs font-bold text-rose-700\">✕ 錯誤：$\\frac{\\log_a M}{\\log_a N} = \\log_N M$（換底結果）</div>\n        <div class=\"text-xs font-bold text-emerald-700\">✓ 正確減法：$\\log_a M - \\log_a N = \\log_a\\frac{M}{N}$</div>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 46,
        "tag": "是非 4",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "觀念辨析：真數為負數之次方提出",
        "front_content": "【觀念是非題】<br>$\\log_3 (-3)^2 = 2\\log_3 (-3)$ 恆成立。<br><br>請判斷本敘述為 <b>○ 正確</b> 或 <b>✕ 錯誤</b>？",
        "front_tip": "🕵️ 柯南破案導引：陷阱提醒：請務必檢查右式對數的真數是否符合存在定義！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：計算左式之值",
                "content": "左式真數為 $(-3)^2 = 9 > 0$，所以左式為 $\\log_3 9 = \\log_3 3^2 = 2$，數值完全合法且有意義。"
            },
            {
                "num": 2,
                "title": "線索 2：檢驗右式之合法性",
                "content": "右式出現 $\\log_3 (-3)$，但其真數為 $-3 < 0$！由對數定義，真數必須嚴格大於 0，因此右式根本無意義！等式不成立。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確答案為 ✕（右式真數 $-3 < 0$ 無意義，次方提出前提為底真數均合法）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fef2f2\" stroke=\"#ef4444\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex items-center justify-between px-3\">\n      <div class=\"flex flex-col items-center justify-center\">\n        <div class=\"w-14 h-14 rounded-full bg-rose-600 text-white flex items-center justify-center text-3xl font-black shadow-md\">✕</div>\n        <div class=\"text-xs font-bold text-rose-800 mt-1\">忽略定義域</div>\n      </div>\n      <div class=\"flex flex-col gap-1.5 flex-1 ml-4 bg-white p-2.5 rounded-xl border border-rose-200 shadow-2xs\">\n        <div class=\"text-xs font-bold text-emerald-700\">✓ 左式：$\\log_3(-3)^2 = \\log_3 9 = 2$（合法）</div>\n        <div class=\"text-xs font-bold text-rose-700\">✕ 右式：$2\\log_3(-3)$ 無意義！（真數 $< 0$）</div>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 47,
        "tag": "是非 5",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "觀念辨析：真數為正時對數值的正負",
        "front_content": "【觀念是非題】<br>若 $b > 0$，則 $\\log_{10} b > 0$ 恆成立。<br><br>請判斷本敘述為 <b>○ 正確</b> 或 <b>✕ 錯誤</b>？",
        "front_tip": "🕵️ 柯南破案導引：反例引導：當真數介於 0 與 1 之間（如 $b = 0.1$）時，對數值是多少？",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分析對數值與真數的關係",
                "content": "以常用對數 $\\log_{10} b$ 為例：當 $b > 1$ 時，$\\log_{10} b > 0$；當 $b = 1$ 時，$\\log_{10} 1 = 0$；當 $0 < b < 1$ 時，$\\log_{10} b < 0$。"
            },
            {
                "num": 2,
                "title": "線索 2：舉出反例",
                "content": "取 $b = 0.1 > 0$：$\\log_{10} 0.1 = \\log_{10} 10^{-1} = -1 < 0$。此時真數大於 0，但對數值為負數！"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】正確答案為 ✕（當 $0 < b < 1$ 時，$\\log_{10} b < 0$）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fef2f2\" stroke=\"#ef4444\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex items-center justify-between px-3\">\n      <div class=\"flex flex-col items-center justify-center\">\n        <div class=\"w-14 h-14 rounded-full bg-rose-600 text-white flex items-center justify-center text-3xl font-black shadow-md\">✕</div>\n        <div class=\"text-xs font-bold text-rose-800 mt-1\">對數值可負</div>\n      </div>\n      <div class=\"flex flex-col gap-1.5 flex-1 ml-4 bg-white p-2.5 rounded-xl border border-rose-200 shadow-2xs\">\n        <div class=\"text-xs font-bold text-rose-700\">✕ 迷思：真數為正不代表對數值為正！</div>\n        <div class=\"text-xs font-bold text-emerald-700\">反例：$\\log_{10} 0.1 = \\log_{10} 10^{-1} = -1 < 0$</div>\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 48,
        "tag": "習題 1",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "對數存在的必要條件求範圍",
        "front_content": "若 $\\log_{x-2}(7 - x)$ 有意義，<br>則 $x$ 的範圍為何？",
        "front_tip": "🕵️ 柯南破案導引：底數 $x-2 > 0$ 且 $x-2 \\ne 1$；真數 $7-x > 0$。三者取交集！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：列出真數條件",
                "content": "真數大於 0：$7 - x > 0 \\implies x < 7$。"
            },
            {
                "num": 2,
                "title": "線索 2：列出底數條件",
                "content": "底數大於 0 且不為 1：$x - 2 > 0 \\implies x > 2$；且 $x - 2 \\ne 1 \\implies x \\ne 3$。"
            },
            {
                "num": 3,
                "title": "線索 3：取交集得出範圍",
                "content": "$2 < x < 7$ 且 $x \\ne 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$2 < x < 7$ 且 $x \\ne 3$",
        "svg": "<svg viewBox=\"0 0 380 190\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"178\" rx=\"14\" fill=\"#f8fafc\" stroke=\"#cbd5e1\" stroke-width=\"1.8\"/>\n  <line x1=\"30\" y1=\"110\" x2=\"350\" y2=\"110\" stroke=\"#64748b\" stroke-width=\"2\"/>\n  <circle cx=\"80\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"80\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">2</text>\n  <circle cx=\"150\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"150\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">3</text>\n  <circle cx=\"290\" cy=\"110\" r=\"3\" fill=\"#64748b\"/><text x=\"290\" y=\"128\" text-anchor=\"middle\" font-size=\"11\" fill=\"#64748b\">7</text>\n  <path d=\"M 80 110 L 80 75 L 290 75 L 290 110\" fill=\"none\" stroke=\"#2563eb\" stroke-width=\"2.5\"/>\n  <circle cx=\"80\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#2563eb\" stroke-width=\"2\"/>\n  <circle cx=\"290\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#2563eb\" stroke-width=\"2\"/>\n  <circle cx=\"150\" cy=\"75\" r=\"4.5\" fill=\"#ffffff\" stroke=\"#dc2626\" stroke-width=\"2\"/>\n  <foreignObject x=\"12\" y=\"8\" width=\"356\" height=\"174\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col justify-between items-center py-1\">\n      <div class=\"text-xs font-bold text-slate-800\">數線交集圖解：$2 < x < 7$ 且 $x \\ne 3$</div>\n      <div class=\"flex justify-between w-full px-6 text-xs font-bold\">\n        <div class=\"text-blue-600\">真數與底數：$2 < x < 7$</div>\n        <div class=\"text-rose-600\">挖空：$x \\ne 3$</div>\n      </div>\n      <div class=\"h-10\"></div>\n      <div class=\"text-xs font-bold text-slate-800 bg-white px-3 py-1 rounded-lg border border-slate-200 shadow-2xs\">\n        解集合：$2 < x < 7 \\text{ 且 } x \\ne 3$\n      </div>\n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 49,
        "tag": "習題 2(1)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "基礎對數特徵值求和",
        "front_content": "試求下列各式的值：<br>$\\log_{10} 10 + \\log_{10} 1$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：直接套用基本性質：$\\log_a a = 1$ 與 $\\log_a 1 = 0$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：分別求得各項對數值",
                "content": "第一項：$\\log_{10} 10 = 1$；第二項：$\\log_{10} 1 = 0$。"
            },
            {
                "num": 2,
                "title": "線索 2：兩數相加",
                "content": "$1 + 0 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} 10 + \\log_{10} 1 = 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">特徵值直接計算</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{10} 10 = 1 \\ , \\ \\log_{10} 1 = 0$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1 + 0 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 50,
        "tag": "習題 2(2)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "方根底數與小數對數混合求值",
        "front_content": "試求下列各式的值：<br>$\\log_{\\sqrt{2}} 2 + \\log_9 \\sqrt{3} - \\log_{0.5} 0.125$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：各項分別化為指數次方提係數：$\\sqrt{2} = 2^{\\frac{1}{2}}, 9 = 3^2, \\sqrt{3} = 3^{\\frac{1}{2}}, 0.125 = (0.5)^3$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：計算第一項",
                "content": "$\\log_{2^{\\frac{1}{2}}} 2^1 = \\frac{1}{\\frac{1}{2}} = 2$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算第二項",
                "content": "$\\log_{3^2} 3^{\\frac{1}{2}} = \\frac{\\frac{1}{2}}{2} = \\frac{1}{4}$。"
            },
            {
                "num": 3,
                "title": "線索 3：計算第三項並加減",
                "content": "$0.125 = (0.5)^3 \\implies \\log_{0.5} (0.5)^3 = 3$。<br>全部加減：$2 + \\frac{1}{4} - 3 = -1 + \\frac{1}{4} = -\\frac{3}{4}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= -\\frac{3}{4}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">三項化簡求和</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_2 4 + \\log_{16} 2 - \\log_{\\frac{1}{3}} 27 = 2 + \\frac{1}{4} - (-3)$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$2 + \\frac{1}{4} + 3 = \\frac{21}{4}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 51,
        "tag": "習題 3(1)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "同底對數加法求值",
        "front_content": "試求下列各式的值：<br>$\\log_{12} 4 + \\log_{12} 36$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：同底對數相加等於真數相乘：$4 \\times 36$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合併真數相乘",
                "content": "$\\log_{12} 4 + \\log_{12} 36 = \\log_{12}(4 \\times 36) = \\log_{12} 144$。"
            },
            {
                "num": 2,
                "title": "線索 2：化簡對數值",
                "content": "$144 = 12^2$，故 $\\log_{12} 12^2 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{12} 4 + \\log_{12} 36 = 2$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">同底對數加法真數相乘</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{12}(4 \\times 36) = \\log_{12} 144$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{12} 12^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 52,
        "tag": "習題 3(2)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "常用對數加減運算",
        "front_content": "試求下列各式的值：<br>$\\log_{10} 25 + \\log_{10} 12 - \\log_{10} 3$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：加項放分子，減項放分母：$\\frac{25 \\times 12}{3}$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：合併真數乘除",
                "content": "$\\log_{10} 25 + \\log_{10} 12 - \\log_{10} 3 = \\log_{10}\\left(\\frac{25 \\times 12}{3}\\right)$。"
            },
            {
                "num": 2,
                "title": "線索 2：約分計算真數",
                "content": "$\\frac{25 \\times 12}{3} = 25 \\times 4 = 100$。"
            },
            {
                "num": 3,
                "title": "線索 3：求出對數值",
                "content": "$100 = 10^2$，故 $\\log_{10} 100 = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 2$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">常用對數約分化簡</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{10} \\frac{25 \\times 12}{3} = \\log_{10} 100$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{10} 10^2 = 2$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 53,
        "tag": "習題 3(3)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "係數還原次方後對數加減",
        "front_content": "試求下列各式的值：<br>$2\\log_5 10 - 4\\log_5 2 + \\log_5 20$",
        "front_tip": "🕵️ 柯南破案導引：關鍵步驟：先將前方的係數移回真數當次方：$2\\log_5 10 = \\log_5 10^2$、$4\\log_5 2 = \\log_5 2^4$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：係數移入真數次方",
                "content": "原式 $= \\log_5 10^2 - \\log_5 2^4 + \\log_5 20 = \\log_5 100 - \\log_5 16 + \\log_5 20$。"
            },
            {
                "num": 2,
                "title": "線索 2：合併真數乘除約分",
                "content": "$\\log_5\\left(\\frac{100 \\times 20}{16}\\right) = \\log_5\\left(\\frac{2000}{16}\\right) = \\log_5 125$。"
            },
            {
                "num": 3,
                "title": "線索 3：求出對數值",
                "content": "$125 = 5^3$，故 $\\log_5 125 = 3$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 3$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">係數還原次方後對數加減</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_5 \\frac{100 \\times 20}{16} = \\log_5 125$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_5 5^3 = 3$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 54,
        "tag": "習題 4(1)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "指數分式換底化簡",
        "front_content": "試求下列各式的值：<br>$4^{\\frac{\\log_7 16}{\\log_7 4}}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：換底公式逆用：$\\frac{\\log_7 16}{\\log_7 4} = \\log_4 16$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：化簡次方部分",
                "content": "由換底公式逆用：$\\frac{\\log_7 16}{\\log_7 4} = \\log_4 16$。而 $\\log_4 16 = \\log_4 4^2 = 2$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算指數次方",
                "content": "原式變為 $4^2 = 16$（或直接利用 $4^{\\log_4 16} = 16$ 互消）。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 16$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">次方倒數換底逆用</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">\\text{次方 } \\frac{1}{\\log_{16} 4} = \\log_4 16 = 2</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$4^2 = 16$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 55,
        "tag": "習題 4(2)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "指數對數相減與換底",
        "front_content": "試求下列各式的值：<br>$3^{\\log_9 20 - \\log_9 5}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：先算次方減法：$\\log_9 20 - \\log_9 5 = \\log_9 4$，再換為以 3 為底！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：化簡次方對數減法",
                "content": "$\\log_9 20 - \\log_9 5 = \\log_9\\left(\\frac{20}{5}\\right) = \\log_9 4$。"
            },
            {
                "num": 2,
                "title": "線索 2：底數與次方對齊",
                "content": "$\\log_9 4 = \\log_{3^2} 2^2 = \\frac{2}{2}\\log_3 2 = \\log_3 2$。"
            },
            {
                "num": 3,
                "title": "線索 3：指數對數互消",
                "content": "$3^{\\log_3 2} = 2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 2$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">減法商數與指數互消</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">\\text{次方 } \\log_3 6 - \\log_3 2 = \\log_3 3 = 1</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$3^1 = 3$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 56,
        "tag": "習題 4(3)",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "巢狀對數由內而外求值",
        "front_content": "試求下列各式的值：<br>$\\log_9(\\log_2 8)$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：括號優先！先由內層算出 $\\log_2 8$，再將結果作為外層真數！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：計算內層對數",
                "content": "內層真數：因為 $8 = 2^3$，所以 $\\log_2 8 = 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算外層對數",
                "content": "代入外層得 $\\log_9 3 = \\log_{3^2} 3^1 = \\frac{1}{2}\\log_3 3 = \\frac{1}{2}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_9(\\log_2 8) = \\frac{1}{2}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">巢狀對數分層剝繭</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">\\text{內層 } \\log_2 8 = 3 \\implies \\text{外層 } \\log_9 3</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\log_{3^2} 3 = \\frac{1}{2}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 57,
        "tag": "習題 5",
        "page": "課本 p.83",
        "category": "課後習作",
        "title": "三項對數連鎖律乘積",
        "front_content": "試求下列各式的值：<br>$\\log_9 7 \\times \\log_7 100 \\times \\log_{10} 3$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：先將各項次方提前（$9 = 3^2, 100 = 10^2$），再使用連鎖律約分！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：底數與真數次方提出",
                "content": "$\\log_9 7 = \\log_{3^2} 7 = \\frac{1}{2}\\log_3 7$；<br>$\\log_7 100 = \\log_7 10^2 = 2\\log_7 10$。"
            },
            {
                "num": 2,
                "title": "線索 2：係數相乘與連鎖律約分",
                "content": "係數相乘：$\\frac{1}{2} \\times 2 = 1$。<br>對數連鎖相乘：$\\log_3 7 \\times \\log_7 10 \\times \\log_{10} 3 = \\log_3 3 = 1$。"
            },
            {
                "num": 3,
                "title": "線索 3：得出總乘積",
                "content": "$1 \\times 1 = 1$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 1$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">連鎖律閉環約分</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">\\left(\\frac{1}{2} \\times 2\\right) \\cdot (\\log_3 7 \\cdot \\log_7 10 \\cdot \\log_{10} 3)</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1 \\times \\log_3 3 = 1$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 58,
        "tag": "習題 6",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "進階代數換底表達",
        "front_content": "設 $a = \\log_{10} 2$、$b = \\log_{10} 3$，<br>若以 $a, b$ 表示，則：<br>$\\log_{12} 5 = \\text{？}$",
        "front_tip": "🕵️ 柯南破案導引：關鍵技巧：以 10 為底換底！注意 $5 = \\frac{10}{2}$，故 $\\log_{10} 5 = 1 - \\log_{10} 2 = 1 - a$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：換為常用對數",
                "content": "$\\log_{12} 5 = \\frac{\\log_{10} 5}{\\log_{10} 12}$。"
            },
            {
                "num": 2,
                "title": "線索 2：轉化分子 log 5",
                "content": "$\\log_{10} 5 = \\log_{10}\\left(\\frac{10}{2}\\right) = \\log_{10} 10 - \\log_{10} 2 = 1 - a$。"
            },
            {
                "num": 3,
                "title": "線索 3：轉化分母 log 12 並代入",
                "content": "$\\log_{10} 12 = \\log_{10}(2^2 \\times 3) = 2\\log_{10} 2 + \\log_{10} 3 = 2a + b$。<br>故原式 $= \\frac{1 - a}{2a + b}$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{12} 5 = \\frac{1 - a}{2a + b}$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">核心代換 $\\log 5 = 1 - \\log 2$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{12} 5 = \\frac{\\log 5}{\\log 12} = \\frac{1 - a}{\\log(2^2 \\times 3)}$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$\\frac{1 - a}{2a + b}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 59,
        "tag": "習題 7(1)",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "常用對數近似值：$\\log_{10} 6$",
        "front_content": "已知 $\\log_{10} 2 \\approx 0.3010$、$\\log_{10} 3 \\approx 0.4771$，<br>試求下列各式之值：<br>$\\log_{10} 6 \\approx \\text{？}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：將 6 質因數分解：$6 = 2 \\times 3$，拆為兩對數相加！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：真數分解為 2 與 3 之積",
                "content": "$\\log_{10} 6 = \\log_{10}(2 \\times 3) = \\log_{10} 2 + \\log_{10} 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入近似值相加",
                "content": "$0.3010 + 0.4771 = 0.7781$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} 6 \\approx 0.7781$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">常用對數近似值相加</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log 6 = \\log 2 + \\log 3$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$0.3010 + 0.4771 = 0.7781$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 60,
        "tag": "習題 7(2)",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "常用對數近似值：$\\log_{10} 5$",
        "front_content": "已知 $\\log_{10} 2 \\approx 0.3010$、$\\log_{10} 3 \\approx 0.4771$，<br>試求下列各式之值：<br>$\\log_{10} 5 \\approx \\text{？}$",
        "front_tip": "🕵️ 柯南破案導引：關鍵技巧：$\\log_{10} 5 = \\log_{10} \\frac{10}{2} = 1 - \\log_{10} 2$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：轉為 10 與 2 之商",
                "content": "$\\log_{10} 5 = \\log_{10}\\left(\\frac{10}{2}\\right) = \\log_{10} 10 - \\log_{10} 2 = 1 - \\log_{10} 2$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入計算小數減法",
                "content": "$1 - 0.3010 = 0.6990$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} 5 \\approx 0.6990$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">常用對數互補關係</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log 5 = 1 - \\log 2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$1 - 0.3010 = 0.6990$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 61,
        "tag": "習題 7(3)",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "常用對數近似值：$\\log_{10} \\frac{3}{2}$",
        "front_content": "已知 $\\log_{10} 2 \\approx 0.3010$、$\\log_{10} 3 \\approx 0.4771$，<br>試求下列各式之值：<br>$\\log_{10} \\frac{3}{2} \\approx \\text{？}$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：真數相除拆為對數相減：$\\log_{10} 3 - \\log_{10} 2$。",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：商拆為對數差",
                "content": "$\\log_{10} \\frac{3}{2} = \\log_{10} 3 - \\log_{10} 2$。"
            },
            {
                "num": 2,
                "title": "線索 2：代入數值相減",
                "content": "$0.4771 - 0.3010 = 0.1761$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$\\log_{10} \\frac{3}{2} \\approx 0.1761$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">商對數近似值相減</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log \\frac{3}{2} = \\log 3 - \\log 2$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$0.4771 - 0.3010 = 0.1761$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 62,
        "tag": "習題 8",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "對數定義與指數次方求值",
        "front_content": "設 $x = \\log_{10} 5$，<br>試求：<br>$100^x + 10^{-x} = \\text{？}$",
        "front_tip": "🕵️ 柯南破案導引：關鍵還原：由 $x = \\log_{10} 5$ 得 $10^x = 5$！再求 $100^x = (10^x)^2$ 與 $10^{-x} = \\frac{1}{10^x}$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：還原指數式",
                "content": "$x = \\log_{10} 5 \\iff 10^x = 5$。"
            },
            {
                "num": 2,
                "title": "線索 2：計算各項指數值",
                "content": "$100^x = (10^2)^x = (10^x)^2 = 5^2 = 25$；<br>$10^{-x} = \\frac{1}{10^x} = \\frac{1}{5} = 0.2$。"
            },
            {
                "num": 3,
                "title": "線索 3：兩數相加求和",
                "content": "$25 + \\frac{1}{5} = \\frac{126}{5} = 25.2$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】$100^x + 10^{-x} = \\frac{126}{5}$（或 $25.2$）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">對數定義轉指數求值</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$\\log_{10} 5 = x \\implies 10^x = 5$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$100^x + 10^{-x} = 5^2 + \\frac{1}{5} = \\frac{126}{5}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 63,
        "tag": "習題 9",
        "page": "課本 p.84",
        "category": "進階思考",
        "title": "對數多項式乘法展開",
        "front_content": "試求下列各式的值：<br>$(\\log_2 3 + \\log_4 9)(\\log_3 4 + \\log_9 2)$",
        "front_tip": "🕵️ 柯南破案導引：解題思維：先化簡各括號內的項：$\\log_4 9 = \\log_{2^2} 3^2 = \\log_2 3$；同理化簡第二個括號！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：化簡第一括號",
                "content": "$\\log_4 9 = \\log_{2^2} 3^2 = \\log_2 3$。<br>第一括號為 $\\log_2 3 + \\log_2 3 = 2\\log_2 3$。"
            },
            {
                "num": 2,
                "title": "線索 2：化簡第二括號",
                "content": "$\\log_3 4 = \\log_3 2^2 = 2\\log_3 2$；$\\log_9 2 = \\log_{3^2} 2 = \\frac{1}{2}\\log_3 2$。<br>第二括號為 $2\\log_3 2 + \\frac{1}{2}\\log_3 2 = \\frac{5}{2}\\log_3 2$。"
            },
            {
                "num": 3,
                "title": "線索 3：相乘並利用倒數性質",
                "content": "$(2\\log_2 3) \\times (\\frac{5}{2}\\log_3 2) = (2 \\times \\frac{5}{2}) \\times (\\log_2 3 \\times \\log_3 2) = 5 \\times 1 = 5$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】原式 $= 5$",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#eff6ff\" stroke=\"#3b82f6\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-blue-900 tracking-wide\">同底化簡再相乘</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-blue-700\">$(2\\log_2 3) \\times \\left(\\frac{5}{2}\\log_3 2\\right)$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-blue-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$5 \\times (\\log_2 3 \\cdot \\log_3 2) = 5 \\times 1 = 5$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 64,
        "tag": "習題 10(1)",
        "page": "課本 p.84",
        "category": "素養應用",
        "title": "芮氏地震規模公式：求規模 $M$",
        "front_content": "【生活素養應用題】<br>芮氏地震規模 $M$ 和地震波所釋放的能量 $E$（單位：爾格）之關係式為：<br>$\\log_{10} E = 11.8 + 1.5M$<br>若有一地震波釋放了 $10^{19.3}$ 爾格的能量，<br>則此地震波的芮氏規模為何？",
        "front_tip": "🕵️ 柯南破案導引：將能量 $E = 10^{19.3}$ 代入關係式左邊，注意 $\\log_{10} 10^{19.3} = 19.3$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：將能量代入關係式左式",
                "content": "$\\log_{10} E = \\log_{10}(10^{19.3}) = 19.3$。"
            },
            {
                "num": 2,
                "title": "線索 2：列出一元一次方程式",
                "content": "$19.3 = 11.8 + 1.5M$。"
            },
            {
                "num": 3,
                "title": "線索 3：移項解出 M",
                "content": "$1.5M = 19.3 - 11.8 = 7.5 \\implies M = \\frac{7.5}{1.5} = 5.0$。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】芮氏規模為 $5.0$（或 $5$）",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fefce8\" stroke=\"#eab308\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-amber-900 tracking-wide\">芮氏地震規模公式求 $M$</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-amber-700\">$19.3 = 11.8 + 1.5M \\implies 1.5M = 7.5$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$M = 5.0$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
    {
        "id": 65,
        "tag": "習題 10(2)",
        "page": "課本 p.84",
        "category": "素養應用",
        "title": "921 集集大地震能量換算",
        "front_content": "【生活素養應用題】<br>芮氏地震規模 $M$ 和釋放能量 $E$ 關係式為：<br>$\\log_{10} E = 11.8 + 1.5M$<br>921 集集大地震的芮氏規模為 $7.3$，<br>則其震央所釋放的能量為多少爾格？",
        "front_tip": "🕵️ 柯南破案導引：將規模 $M = 7.3$ 代入右式，算出 $\\log_{10} E$，再轉為指數式 $E = 10^{\\text{次方}}$！",
        "steps": [
            {
                "num": 1,
                "title": "線索 1：將 M = 7.3 代入右式計算",
                "content": "$\\log_{10} E = 11.8 + 1.5 \\times 7.3$。<br>先算 $1.5 \\times 7.3 = 10.95$。"
            },
            {
                "num": 2,
                "title": "線索 2：相加求得對數值",
                "content": "$\\log_{10} E = 11.8 + 10.95 = 22.75$。"
            },
            {
                "num": 3,
                "title": "線索 3：還原為能量數值",
                "content": "由對數定義 $E = 10^{22.75}$ 爾格。"
            }
        ],
        "conclusion": "【CASE CLOSED 真相永遠只有一個！】釋放能量為 $10^{22.75}$ 爾格",
        "svg": "<svg viewBox=\"0 0 380 180\" class=\"w-full h-full\">\n  <rect x=\"8\" y=\"6\" width=\"364\" height=\"168\" rx=\"14\" fill=\"#fefce8\" stroke=\"#eab308\" stroke-width=\"1.8\"/>\n  <foreignObject x=\"14\" y=\"10\" width=\"352\" height=\"160\">\n    <div xmlns=\"http://www.w3.org/1999/xhtml\" class=\"w-full h-full flex flex-col items-center justify-between py-1 box-border\">\n      <div class=\"text-xs font-bold text-amber-900 tracking-wide\">921 集集大地震能量換算</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-amber-700\">$\\log_{10} E = 11.8 + 1.5(7.3) = 22.75$</div>\n      </div>\n      <div class=\"text-xs font-bold text-rose-500 leading-none\">$\\Downarrow$</div>\n      <div class=\"bg-white border-2 border-amber-300 rounded-xl px-3 py-1.5 shadow-xs text-center w-full max-w-[325px]\">\n        <div class=\"text-sm font-bold text-rose-600\">$E = 10^{22.75} \\text{ 爾格}$</div>\n      </div>\n      \n    </div>\n  </foreignObject>\n</svg>"
    },
]

# -*- coding: utf-8 -*-
"""
interactive_cards_data.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
互動測驗題庫 (QUIZ_DATA)、動態幾何參數切換 (MODEL_DATA) 與六大闖關關卡 (CHALLENGE_STAGES)
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦版標準：
- 每張圖卡配置正面自我檢核抽屜題
- 全欄位 100% KaTeX 標準數學式
- 包含 STAGE 01~06 闖關系統（STAGE 05 專門檢核習作實戰，STAGE 06 終極魔王）
"""

# 全套 65 張圖卡之正面自我檢核測驗 (單選 4 選 1 / 是非 2 選 1)
QUIZ_DATA = {
    # 觀念卡 (1 ~ 4)
    1: {
        "question": "若 $2^x = 30$，則依納皮爾所發明的對數符號，其解 $x$ 表示為下列何者？",
        "options": ["$\\log_{30} 2$", "$\\log_2 30$", "$30^2$", "$\\sqrt{30}$"],
        "answer": 1,
        "explanation": "由 $a^x = b \\iff x = \\log_a b$，以 2 為底數，故解為 $\\log_2 30$。"
    },
    2: {
        "question": "關於對數 $\\log_a b$ 有意義的條件，下列何者正確？",
        "options": ["$a > 0$ 且 $b > 0$", "$a > 0, a \\ne 1$ 且 $b > 0$", "$a > 0$ 且 $b \\ne 0$", "$a$ 與 $b$ 均為任意實數"],
        "answer": 1,
        "explanation": "底數必須 $a > 0$ 且 $a \\ne 1$；真數必須 $b > 0$。"
    },
    3: {
        "question": "若 $a > 0, a \\ne 1$，且 $M > 0, N > 0$，則 $\\log_a M + \\log_a N$ 等於下列何者？",
        "options": ["$\\log_a (M + N)$", "$\\log_a (MN)$", "$\\log_a (M^N)$", "$(\\log_a M)(\\log_a N)$"],
        "answer": 1,
        "explanation": "同底對數相加，等於真數相乘：$\\log_a (MN)$。"
    },
    4: {
        "question": "換底公式中，若將 $\\log_a b$ 換為以 $c$ 為底的對數，則其形式為何？",
        "options": ["$\\frac{\\log_c a}{\\log_c b}$", "$\\frac{\\log_c b}{\\log_c a}$", "$\\log_c (b - a)$", "$\\log_c (ab)$"],
        "answer": 1,
        "explanation": "換底公式為 $\\log_a b = \\frac{\\log_c b}{\\log_c a}$（真數在分子，原底數在分母）。"
    },

    # 例題 1 與 隨堂 1 (5 ~ 6)
    5: {
        "question": "下列哪一個是對數式且「有意義」？",
        "options": ["$\\log_1 5$", "$\\log_{-2} 3$", "$\\log_2 \\frac{1}{5}$", "$\\log_3 (-4)$"],
        "answer": 2,
        "explanation": "$\\log_2 \\frac{1}{5}$ 之底數 $2 > 0, \\ne 1$ 且真數 $\\frac{1}{5} > 0$，故有意義。"
    },
    6: {
        "question": "下列各式哪一個是有意義的對數？",
        "options": ["$\\log_2 0$", "$\\log_0 2$", "$\\log_{\\frac{1}{2}} 5$", "$\\log_{-3} (-2)$"],
        "answer": 2,
        "explanation": "$\\log_{\\frac{1}{2}} 5$ 底數為正數非 1，真數為正數，完全合乎定義。"
    },

    # 例題 2 與 隨堂 2 (7 ~ 8)
    7: {
        "question": "若 $\\log_{x-1}(x + 5)$ 有意義，則 $x$ 必須滿足下列何條件？",
        "options": ["$x > -5$", "$x > 1$", "$x > 1$ 且 $x \\ne 2$", "$x > 2$"],
        "answer": 2,
        "explanation": "真數 $x + 5 > 0 \\implies x > -5$；底數 $x - 1 > 0 \\implies x > 1$ 且 $x - 1 \\ne 1 \\implies x \\ne 2$。交集得 $x > 1$ 且 $x \\ne 2$。"
    },
    8: {
        "question": "若 $\\log_{x+2}(3 - x)$ 有意義，則 $x$ 的範圍為何？",
        "options": ["$x < 3$", "$-2 < x < 3$", "$-2 < x < 3$ 且 $x \\ne -1$", "$x > -2$ 且 $x \\ne -1$"],
        "answer": 2,
        "explanation": "真數 $3 - x > 0 \\implies x < 3$；底數 $x + 2 > 0 \\implies x > -2$ 且 $x \\ne -1$。交集為 $-2 < x < 3$ 且 $x \\ne -1$。"
    },

    # 例題 3(1~4) (9 ~ 12)
    9: {
        "question": "試求 $\\log_2 64$ 之值為多少？",
        "options": ["$4$", "$5$", "$6$", "$8$"],
        "answer": 2,
        "explanation": "因為 $2^6 = 64$，所以 $\\log_2 64 = 6$。"
    },
    10: {
        "question": "試求 $\\log_3 \\frac{1}{81}$ 之值為多少？",
        "options": ["$4$", "$-4$", "$-3$", "$\\frac{1}{4}$"],
        "answer": 1,
        "explanation": "因為 $3^{-4} = \\frac{1}{81}$，所以 $\\log_3 \\frac{1}{81} = -4$。"
    },
    11: {
        "question": "試求 $\\log_{0.1} 0.001$ 之值為多少？",
        "options": ["$2$", "$3$", "$-3$", "$0.3$"],
        "answer": 1,
        "explanation": "因為 $(0.1)^3 = 0.001$，故 $\\log_{0.1} 0.001 = 3$。"
    },
    12: {
        "question": "試求 $\\log_{25} 5$ 之值為多少？",
        "options": ["$2$", "$\\frac{1}{2}$", "$\\frac{1}{5}$", "$5$"],
        "answer": 1,
        "explanation": "因為 $25^{\\frac{1}{2}} = \\sqrt{25} = 5$，故 $\\log_{25} 5 = \\frac{1}{2}$。"
    },

    # 隨堂 3(1~4) (13 ~ 16)
    13: {
        "question": "試求 $\\log_3 27$ 之值為多少？",
        "options": ["$2$", "$3$", "$9$", "$27$"],
        "answer": 1,
        "explanation": "因為 $3^3 = 27$，故 $\\log_3 27 = 3$。"
    },
    14: {
        "question": "試求 $\\log_2 \\frac{1}{32}$ 之值為多少？",
        "options": ["$5$", "$-5$", "$-4$", "$-6$"],
        "answer": 1,
        "explanation": "因為 $2^{-5} = \\frac{1}{32}$，故值為 $-5$。"
    },
    15: {
        "question": "試求 $\\log_{\\frac{1}{5}} \\frac{1}{625}$ 之值為多少？",
        "options": ["$3$", "$4$", "$-4$", "$5$"],
        "answer": 1,
        "explanation": "因為 $(\\frac{1}{5})^4 = \\frac{1}{625}$，故對數值為 4。"
    },
    16: {
        "question": "試求 $\\log_{\\frac{1}{4}} 64$ 之值為多少？",
        "options": ["$3$", "$-3$", "$-4$", "$16$"],
        "answer": 1,
        "explanation": "因為 $(\\frac{1}{4})^{-3} = 4^3 = 64$，故對數值為 $-3$。"
    },

    # 例題 4(1~2) (17 ~ 18)
    17: {
        "question": "試求 $\\log_5 1 + \\log_3 3$ 之值為多少？",
        "options": ["$0$", "$1$", "$2$", "$4$"],
        "answer": 1,
        "explanation": "$\\log_5 1 = 0$，$\\log_3 3 = 1$，相加為 $0 + 1 = 1$。"
    },
    18: {
        "question": "試求 $\\log_3 \\sqrt{3}$ 之值為多少？",
        "options": ["$1$", "$\\frac{1}{2}$", "$2$", "$\\frac{1}{3}$"],
        "answer": 1,
        "explanation": "$\\sqrt{3} = 3^{\\frac{1}{2}}$，故 $\\log_3 3^{\\frac{1}{2}} = \\frac{1}{2}$。"
    },

    # 隨堂 4(1~2) (19 ~ 20)
    19: {
        "question": "試求 $\\log_{0.25} 1 + \\log_{100} 100$ 之值為多少？",
        "options": ["$0$", "$1$", "$2$", "$100$"],
        "answer": 1,
        "explanation": "$0 + 1 = 1$。"
    },
    20: {
        "question": "試求 $\\log_{25} 125$ 之值為多少？",
        "options": ["$\\frac{2}{3}$", "$\\frac{3}{2}$", "$5$", "$\\frac{5}{2}$"],
        "answer": 1,
        "explanation": "$\\log_{5^2} 5^3 = \\frac{3}{2}\\log_5 5 = \\frac{3}{2}$。"
    },

    # 例題 5(1~3) (21 ~ 23)
    21: {
        "question": "試求 $\\log_6 9 + \\log_6 4$ 之值為多少？",
        "options": ["$\\log_6 13$", "$2$", "$3$", "$6$"],
        "answer": 1,
        "explanation": "$\\log_6(9 \\times 4) = \\log_6 36 = \\log_6 6^2 = 2$。"
    },
    22: {
        "question": "試求 $\\log_5 45 - \\log_5 9$ 之值為多少？",
        "options": ["$1$", "$2$", "$5$", "$\\log_5 36$"],
        "answer": 0,
        "explanation": "$\\log_5\\frac{45}{9} = \\log_5 5 = 1$。"
    },
    23: {
        "question": "試求 $\\log_3 36 - \\log_3 8 + \\log_3 54$ 之值為多少？",
        "options": ["$3$", "$4$", "$5$", "$6$"],
        "answer": 2,
        "explanation": "$\\log_3(\\frac{36 \\times 54}{8}) = \\log_3 243 = \\log_3 3^5 = 5$。"
    },

    # 隨堂 5(1~3) (24 ~ 26)
    24: {
        "question": "試求 $\\log_8 16 + \\log_8 32$ 之值為多少？",
        "options": ["$2$", "$3$", "$4$", "$\\frac{8}{3}$"],
        "answer": 1,
        "explanation": "$\\log_8(16 \\times 32) = \\log_{2^3} 2^9 = \\frac{9}{3} = 3$。"
    },
    25: {
        "question": "試求 $\\log_3 18 - \\log_3 2$ 之值為多少？",
        "options": ["$1$", "$2$", "$3$", "$9$"],
        "answer": 1,
        "explanation": "$\\log_3(\\frac{18}{2}) = \\log_3 9 = 2$。"
    },
    26: {
        "question": "試求 $\\log_2 12 + \\log_2 40 - \\log_2 15$ 之值為多少？",
        "options": ["$4$", "$5$", "$6$", "$8$"],
        "answer": 1,
        "explanation": "$\\log_2(\\frac{12 \\times 40}{15}) = \\log_2 32 = 5$。"
    },

    # 例題 6(1~3) (27 ~ 29)
    27: {
        "question": "試求 $\\frac{\\log_5 32}{\\log_5 2}$ 之值為多少？",
        "options": ["$4$", "$5$", "$16$", "$\\log_5 30$"],
        "answer": 1,
        "explanation": "換底公式逆用為 $\\log_2 32 = 5$。"
    },
    28: {
        "question": "試求 $5^{\\frac{\\log_2 7}{\\log_2 5}}$ 之值為多少？",
        "options": ["$2$", "$5$", "$7$", "$35$"],
        "answer": 2,
        "explanation": "次方 $\\frac{\\log_2 7}{\\log_2 5} = \\log_5 7$，故 $5^{\\log_5 7} = 7$。"
    },
    29: {
        "question": "試求 $9^{\\log_3 5}$ 之值為多少？",
        "options": ["$5$", "$10$", "$15$", "$25$"],
        "answer": 3,
        "explanation": "$9^{\\log_3 5} = (3^2)^{\\log_3 5} = 3^{2\\log_3 5} = 3^{\\log_3 25} = 25$。"
    },

    # 隨堂 6(1~3) (30 ~ 32)
    30: {
        "question": "試求 $\\frac{\\log_2 243}{\\log_2 9}$ 之值為多少？",
        "options": ["$2$", "$\\frac{5}{2}$", "$3$", "$5$"],
        "answer": 1,
        "explanation": "換底公式逆運算：$\\log_9 243 = \\log_{3^2} 3^5 = \\frac{5}{2}$。"
    },
    31: {
        "question": "試求 $4^{\\frac{\\log_7 1}{\\log_7 3}}$ 之值為多少？",
        "options": ["$0$", "$1$", "$3$", "$4$"],
        "answer": 1,
        "explanation": "$\\log_7 1 = 0 \\implies$ 次方為 $0 \\implies 4^0 = 1$。"
    },
    32: {
        "question": "試求 $3^{\\log_9 16}$ 之值為多少？",
        "options": ["$2$", "$4$", "$8$", "$16$"],
        "answer": 1,
        "explanation": "$\\log_9 16 = \\log_{3^2} 4^2 = \\log_3 4$，故 $3^{\\log_3 4} = 4$。"
    },

    # 例題 7(1~2) (33 ~ 34)
    33: {
        "question": "試求 $\\log_2 5 \\times \\log_5 2$ 之值為多少？",
        "options": ["$0$", "$1$", "$2$", "$10$"],
        "answer": 1,
        "explanation": "底真顛倒互為倒數，乘積恆為 1。"
    },
    34: {
        "question": "試求 $\\log_2 3 \\times \\log_3 5 \\times \\log_5 8$ 之值為多少？",
        "options": ["$2$", "$3$", "$4$", "$8$"],
        "answer": 1,
        "explanation": "連鎖律首尾相接得 $\\log_2 8 = 3$。"
    },

    # 隨堂 7(1~2) (35 ~ 36)
    35: {
        "question": "試求 $\\log_4 6 \\times \\log_6 4$ 之值為多少？",
        "options": ["$0$", "$1$", "$2$", "$24$"],
        "answer": 1,
        "explanation": "互為倒數，相乘得 1。"
    },
    36: {
        "question": "試求 $\\log_9 8 \\times \\log_8 7 \\times \\log_7 3$ 之值為多少？",
        "options": ["$\\frac{1}{2}$", "$1$", "$2$", "$\\frac{1}{3}$"],
        "answer": 0,
        "explanation": "連鎖約分得 $\\log_9 3 = \\log_{3^2} 3^1 = \\frac{1}{2}$。"
    },

    # 例題 8(1~3) (37 ~ 39)
    37: {
        "question": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，則 $\\log_{10} 12$ 以 $x, y$ 表示為何？",
        "options": ["$x + y$", "$2x + y$", "$x + 2y$", "$2xy$"],
        "answer": 1,
        "explanation": "$12 = 2^2 \\times 3 \\implies \\log_{10} 12 = 2\\log 2 + \\log 3 = 2x + y$。"
    },
    38: {
        "question": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，則 $\\log_{10} \\frac{8}{9}$ 以 $x, y$ 表示為何？",
        "options": ["$3x - 2y$", "$2x - 3y$", "$3x + 2y$", "$\\frac{3x}{2y}$"],
        "answer": 0,
        "explanation": "$\\log 8 - \\log 9 = 3\\log 2 - 2\\log 3 = 3x - 2y$。"
    },
    39: {
        "question": "設 $\\log_{10} 2 = x$、$\\log_{10} 3 = y$，則 $\\log_3 40$ 以 $x, y$ 表示為何？",
        "options": ["$\\frac{2x + 1}{y}$", "$\\frac{x + 2}{y}$", "$\\frac{3x + 1}{y}$", "$2x + 1$"],
        "answer": 0,
        "explanation": "換底為 10：$\\frac{\\log 40}{\\log 3} = \\frac{\\log 4 + \\log 10}{\\log 3} = \\frac{2x + 1}{y}$。"
    },

    # 隨堂 8(1~3) (40 ~ 42)
    40: {
        "question": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，則 $\\log_{10} 45$ 以 $x, y$ 表示為何？",
        "options": ["$x + 2y$", "$2x + y$", "$2x - y$", "$xy$"],
        "answer": 1,
        "explanation": "$45 = 3^2 \\times 5 \\implies 2\\log 3 + \\log 5 = 2x + y$。"
    },
    41: {
        "question": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，則 $\\log_{10} \\frac{25}{27}$ 以 $x, y$ 表示為何？",
        "options": ["$2y - 3x$", "$3x - 2y$", "$2x - 3y$", "$\\frac{2y}{3x}$"],
        "answer": 0,
        "explanation": "$\\log 25 - \\log 27 = 2\\log 5 - 3\\log 3 = 2y - 3x$。"
    },
    42: {
        "question": "設 $\\log_{10} 3 = x$、$\\log_{10} 5 = y$，則 $\\log_{30} 15$ 以 $x, y$ 表示為何？",
        "options": ["$\\frac{x + y}{x + 1}$", "$\\frac{x + y}{y + 1}$", "$\\frac{xy}{x + 1}$", "$x + y - 1$"],
        "answer": 0,
        "explanation": "$\\frac{\\log 15}{\\log 30} = \\frac{\\log 3 + \\log 5}{\\log 3 + \\log 10} = \\frac{x + y}{x + 1}$。"
    },

    # 是非題 1~5 (43 ~ 47)
    43: {
        "question": "【是非題】若 $a > 0$ 且 $a \\ne 1$，則 $\\log_a 1 = 0$ 恆成立？",
        "options": ["○ 正確", "✕ 錯誤"],
        "answer": 0,
        "explanation": "正確，因 $a^0 = 1$。"
    },
    44: {
        "question": "【是非題】$\\log_a (M + N) = \\log_a M + \\log_a N$ 恆成立？",
        "options": ["○ 正確", "✕ 錯誤"],
        "answer": 1,
        "explanation": "錯誤，公式為 $\\log_a (MN) = \\log_a M + \\log_a N$，真數相加不可拆解。"
    },
    45: {
        "question": "【是非題】$\\frac{\\log_a M}{\\log_a N} = \\log_a (M - N)$ 恆成立？",
        "options": ["○ 正確", "✕ 錯誤"],
        "answer": 1,
        "explanation": "錯誤，$\\frac{\\log_a M}{\\log_a N} = \\log_N M$ 為換底公式；而 $\\log_a M - \\log_a N = \\log_a \\frac{M}{N}$。"
    },
    46: {
        "question": "【是非題】等式 $\\log_3 (-3)^2 = 2\\log_3 (-3)$ 是否成立？",
        "options": ["○ 正確", "✕ 錯誤"],
        "answer": 1,
        "explanation": "錯誤，右式真數為 $-3 < 0$，在實數對數中無意義。"
    },
    47: {
        "question": "【是非題】若 $b > 0$，則 $\\log_{10} b > 0$ 恆成立？",
        "options": ["○ 正確", "✕ 錯誤"],
        "answer": 1,
        "explanation": "錯誤，當 $0 < b < 1$ 時（例如 $b = 0.1$），$\\log_{10} 0.1 = -1 < 0$。"
    },

    # 基礎習題 1 ~ 5 (48 ~ 57)
    48: {
        "question": "若 $\\log_{x-2}(7 - x)$ 有意義，則 $x$ 的範圍為何？",
        "options": ["$x < 7$", "$2 < x < 7$", "$2 < x < 7$ 且 $x \\ne 3$", "$x > 2$ 且 $x \\ne 3$"],
        "answer": 2,
        "explanation": "真數 $7 - x > 0 \\implies x < 7$；底數 $x - 2 > 0 \\implies x > 2$ 且 $x \\ne 3$。交集得 $2 < x < 7$ 且 $x \\ne 3$。"
    },
    49: {
        "question": "試求 $\\log_{10} 10 + \\log_{10} 1$ 之值為多少？",
        "options": ["$0$", "$1$", "$2$", "$10$"],
        "answer": 1,
        "explanation": "$1 + 0 = 1$。"
    },
    50: {
        "question": "試求 $\\log_{\\sqrt{2}} 2 + \\log_9 \\sqrt{3} - \\log_{0.5} 0.125$ 之值為多少？",
        "options": ["$-\\frac{3}{4}$", "$\\frac{1}{4}$", "$1$", "$-\\frac{1}{2}$"],
        "answer": 0,
        "explanation": "$2 + \\frac{1}{4} - 3 = -\\frac{3}{4}$。"
    },
    51: {
        "question": "試求 $\\log_{12} 4 + \\log_{12} 36$ 之值為多少？",
        "options": ["$1$", "$2$", "$3$", "$12$"],
        "answer": 1,
        "explanation": "$\\log_{12}(4 \\times 36) = \\log_{12} 144 = 2$。"
    },
    52: {
        "question": "試求 $\\log_{10} 25 + \\log_{10} 12 - \\log_{10} 3$ 之值為多少？",
        "options": ["$1$", "$2$", "$3$", "$10$"],
        "answer": 1,
        "explanation": "$\\log_{10}(\\frac{25 \\times 12}{3}) = \\log_{10} 100 = 2$。"
    },
    53: {
        "question": "試求 $2\\log_5 10 - 4\\log_5 2 + \\log_5 20$ 之值為多少？",
        "options": ["$2$", "$3$", "$4$", "$5$"],
        "answer": 1,
        "explanation": "$\\log_5(\\frac{10^2 \\times 20}{2^4}) = \\log_5(\\frac{2000}{16}) = \\log_5 125 = 3$。"
    },
    54: {
        "question": "試求 $4^{\\frac{\\log_7 16}{\\log_7 4}}$ 之值為多少？",
        "options": ["$4$", "$8$", "$16$", "$64$"],
        "answer": 2,
        "explanation": "次方為 $\\log_4 16 = 2$，故 $4^2 = 16$。"
    },
    55: {
        "question": "試求 $3^{\\log_9 20 - \\log_9 5}$ 之值為多少？",
        "options": ["$2$", "$4$", "$5$", "$9$"],
        "answer": 0,
        "explanation": "次方為 $\\log_9 4 = \\log_3 2$，故 $3^{\\log_3 2} = 2$。"
    },
    56: {
        "question": "試求 $\\log_9(\\log_2 8)$ 之值為多少？",
        "options": ["$\\frac{1}{3}$", "$\\frac{1}{2}$", "$1$", "$2$"],
        "answer": 1,
        "explanation": "內層 $\\log_2 8 = 3$，外層 $\\log_9 3 = \\frac{1}{2}$。"
    },
    57: {
        "question": "試求 $\\log_9 7 \\times \\log_7 100 \\times \\log_{10} 3$ 之值為多少？",
        "options": ["$\\frac{1}{2}$", "$1$", "$2$", "$4$"],
        "answer": 1,
        "explanation": "$(\\frac{1}{2}\\log_3 7) \\times (2\\log_7 10) \\times \\log_{10} 3 = (\\frac{1}{2} \\times 2) \\times 1 = 1$。"
    },

    # 進階習題 6 ~ 9 (58 ~ 63)
    58: {
        "question": "設 $a = \\log_{10} 2$、$b = \\log_{10} 3$，以 $a, b$ 表示 $\\log_{12} 5$ 為何？",
        "options": ["$\\frac{1 - a}{2a + b}$", "$\\frac{a - 1}{2a + b}$", "$\\frac{1 - a}{a + 2b}$", "$\\frac{1 - b}{2a + b}$"],
        "answer": 0,
        "explanation": "$\\log_{12} 5 = \\frac{\\log 5}{\\log 12} = \\frac{1 - a}{2a + b}$。"
    },
    59: {
        "question": "已知 $\\log_{10} 2 \\approx 0.3010$、$\\log_{10} 3 \\approx 0.4771$，求 $\\log_{10} 6$ 之近似值？",
        "options": ["$0.7781$", "$0.1761$", "$0.6990$", "$0.8451$"],
        "answer": 0,
        "explanation": "$0.3010 + 0.4771 = 0.7781$。"
    },
    60: {
        "question": "已知 $\\log_{10} 2 \\approx 0.3010$，求 $\\log_{10} 5$ 之近似值？",
        "options": ["$0.6990$", "$0.7781$", "$0.3010$", "$0.5000$"],
        "answer": 0,
        "explanation": "$\\log 5 = 1 - \\log 2 \\approx 1 - 0.3010 = 0.6990$。"
    },
    61: {
        "question": "已知 $\\log_{10} 2 \\approx 0.3010$、$\\log_{10} 3 \\approx 0.4771$，求 $\\log_{10} \\frac{3}{2}$ 之近似值？",
        "options": ["$0.1761$", "$0.7781$", "$0.6990$", "$0.2385$"],
        "answer": 0,
        "explanation": "$0.4771 - 0.3010 = 0.1761$。"
    },
    62: {
        "question": "設 $x = \\log_{10} 5$，則 $100^x + 10^{-x}$ 之值為多少？",
        "options": ["$25.2$", "$25$", "$26$", "$125$"],
        "answer": 0,
        "explanation": "$10^x = 5 \\implies 100^x = 5^2 = 25$，$10^{-x} = \\frac{1}{5} = 0.2$。總和為 $25.2$。"
    },
    63: {
        "question": "試求 $(\\log_2 3 + \\log_4 9)(\\log_3 4 + \\log_9 2)$ 之值為多少？",
        "options": ["$4$", "$5$", "$6$", "$10$"],
        "answer": 1,
        "explanation": "$(2\\log_2 3) \\times (\\frac{5}{2}\\log_3 2) = 5 \\times (\\log_2 3 \\log_3 2) = 5$。"
    },

    # 生活素養題 10(1~2) (64 ~ 65)
    64: {
        "question": "芮氏地震關係式 $\\log_{10} E = 11.8 + 1.5M$，若釋放能量為 $10^{19.3}$ 爾格，則芮氏規模 $M$ 為何？",
        "options": ["$4.5$", "$5.0$", "$5.5$", "$6.0$"],
        "answer": 1,
        "explanation": "$19.3 = 11.8 + 1.5M \\implies 1.5M = 7.5 \\implies M = 5.0$。"
    },
    65: {
        "question": "芮氏規模 $7.3$ 的 921 集集大地震，震央釋放能量 $E$ 滿足 $\\log_{10} E = 11.8 + 1.5(7.3)$，則 $E$ 為多少爾格？",
        "options": ["$10^{22.75}$", "$10^{20.5}$", "$10^{18.8}$", "$10^{24}$"],
        "answer": 0,
        "explanation": "$11.8 + 1.5 \\times 7.3 = 11.8 + 10.95 = 22.75$，故 $E = 10^{22.75}$ 爾格。"
    }
}

# 卡片背面動態參數切換 (switchModel)
MODEL_DATA = {
    1: [
        {"name": "指數轉對數", "desc": "2^5 = 32 ⇔ log_2 32 = 5 ； 2^x = 30 ⇔ x = log_2 30"},
        {"name": "對數轉指數", "desc": "log_a b = x ⇔ a^x = b (底數 a 不變，次方與真數對調)"}
    ],
    2: [
        {"name": "底數 a > 1 遞增型", "desc": "函數 y = log_a x 嚴格遞增，過 (1,0)，當 x > 1 時 y > 0"},
        {"name": "底數 0 < a < 1 遞減型", "desc": "函數 y = log_a x 嚴格遞減，過 (1,0)，當 x > 1 時 y < 0"}
    ],
    3: [
        {"name": "和差化積商", "desc": "log_a M + log_a N = log_a(MN) ； log_a M - log_a N = log_a(M/N)"},
        {"name": "次方提前律", "desc": "log_{a^r} M^s = (s/r) log_a M ； a^{log_a M} = M"}
    ],
    4: [
        {"name": "換底公式模式", "desc": "log_a b = log_c b / log_c a (引入任意正底數 c ≠ 1)"},
        {"name": "連鎖骨牌約分", "desc": "log_a b × log_b c × log_c d = log_a d ； log_a b × log_b a = 1"}
    ],
    64: [
        {"name": "規模 M=5.0 (中型地震)", "desc": "log E = 11.8 + 1.5(5.0) = 19.3 ⇒ E = 10^{19.3} 爾格 (約 2×10^12 焦耳)"},
        {"name": "規模 M=7.3 (921集集強震)", "desc": "log E = 11.8 + 1.5(7.3) = 22.75 ⇒ E = 10^{22.75} 爾格 (能量增強約 2800 倍！)"}
    ]
}

# 六大關卡檢核系統 (STAGE 01 ~ 06：少年偵探團升級考核)
CHALLENGE_STAGES = [
    {
        "stage": 1,
        "title": "CASE 01 ‧ 初步勘驗：對數概念與存在條件",
        "desc": "掌握對數符號本質、底數與真數三大存在鐵律及範圍求解",
        "card_ids": [1, 2, 5, 6, 7, 8],
        "pass_score": 80
    },
    {
        "stage": 2,
        "title": "CASE 02 ‧ 暗號破譯：基本性質與對數求值",
        "desc": "精熟整數、分數、小數、方根底數對數求值與特徵值性質",
        "card_ids": [3, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        "pass_score": 80
    },
    {
        "stage": 3,
        "title": "CASE 03 ‧ 證物化驗：對數加減與運算整合",
        "desc": "靈活將同底對數加減化為真數乘除，熟練係數移回次方化簡",
        "card_ids": [21, 22, 23, 24, 25, 26],
        "pass_score": 80
    },
    {
        "stage": 4,
        "title": "CASE 04 ‧ 連環暗鎖：換底公式與連鎖律",
        "desc": "掌握換底公式逆用、骨牌連鎖約分與常用對數代數表達",
        "card_ids": [4, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42],
        "pass_score": 80
    },
    {
        "stage": 5,
        "title": "CASE 05 ‧ 警視廳特訓：章末習題實戰考核",
        "desc": "課本章末習題 100% 全數特訓，涵蓋是非辨析、基礎加減、進階代數與生活素養",
        "card_ids": [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65],
        "pass_score": 80
    },
    {
        "stage": 6,
        "title": "CASE 06 ‧ 劇場版大破案：終極魔王綜合考核",
        "desc": "全單元 65 件謎案隨機抽測 10 題，全方位考驗概念、精算、代數與地震素養",
        "card_ids": "RANDOM_10",
        "pass_score": 90
    }
]


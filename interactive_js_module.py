# -*- coding: utf-8 -*-
"""
interactive_js_module.py - 東大版 技術高中數學（第三冊）2-3 對數及其運算的意義
前端十大互動 JavaScript 核心邏輯模組
遵循 PLVS-MATH-DONGDA-SOP-FLAGSHIP v4.0 旗艦版標準：
- 雙向同步逐步導引 showStep（防短路鐵律，課堂聚焦與半透明模糊遮蔽）
- 心智圖返回鍵、全螢幕投影 (F 鍵) 與返回心智圖跳轉
- 多功能電子白板（橡皮擦 destination-out、4 段粗細、8 色 + 自訂取色、Undo、Clear）
- 頁尾第一列膠囊計數器（人氣/到訪/互動雙向同步，從 0 起算）
- 教師解答版密碼驗證 (88888888)
- 單元動態幾何實驗室 (對數曲線實驗室 + 芮氏地震能量對數尺)
- 六大關卡闖關檢核系統 (含 STAGE 05 習作實戰關與 STAGE 06 終極魔王關)
"""

INTERACTIVE_JS_CODE = r"""
// ==========================================
// 1. 全域狀態與初始化
// ==========================================
let allCards = [];
let currentCategory = 'all';
let currentCardView = 'all'; // all, mastered, review
let currentModalIndex = 0;
let fromMindmap = false;
let cardStepStates = {}; // 記錄每張卡片目前停留在哪一步 (預設 0=全部)

// 電子白板狀態
let isDrawing = false;
let whiteboardCanvas = null;
let whiteboardCtx = null;
let currentPenColor = '#dc2626';
let currentPenSize = 4;
let currentHighlighterAlpha = 0.4; // 螢光筆透明度 (0.2 ~ 0.8)
let currentEraserSize = 26; // 橡皮擦大小 (12, 26, 50, 90)
let whiteboardMode = 'mouse'; // 'mouse' (滑鼠操作內容), 'pen' (原子筆), 'highlighter' (螢光筆), 'eraser' (橡皮擦)
let isEraserMode = false;
let strokeHistory = [];

// 闖關檢核狀態
let currentStageIndex = 0;
let currentQuizQuestionIndex = 0;
let stageQuizList = [];
let currentLives = 3;
let currentScore = 0;
let currentCombo = 0;
let maxCombo = 0;

// 動態實驗室狀態
let currentLabBase = 2.0;
let currentEarthquakeM = 5.0;

document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    allCards = window.CARDS_DATA || [];
    renderCards();
    initStats();
    initWhiteboard();
    initKeyboardShortcuts();
    renderMindmapTree();
    updateProgressBar();
    initLab();
}

// ==========================================
// 2. 頁面載入與統計計數器 (Core Rule 5)
// ==========================================
function initStats() {
    let pageviews = parseInt(localStorage.getItem('plvs_2_3_pageviews') || '0', 10) + 1;
    let visitors = parseInt(localStorage.getItem('plvs_2_3_visitors') || '0', 10);
    let interactions = parseInt(localStorage.getItem('plvs_2_3_interactions') || '0', 10);

    if (!sessionStorage.getItem('plvs_2_3_session_visited')) {
        visitors += 1;
        sessionStorage.setItem('plvs_2_3_session_visited', 'true');
    }

    localStorage.setItem('plvs_2_3_pageviews', pageviews.toString());
    localStorage.setItem('plvs_2_3_visitors', visitors.toString());
    localStorage.setItem('plvs_2_3_interactions', interactions.toString());

    updateStatsDisplay(pageviews, visitors, interactions);
}

function recordInteraction() {
    let interactions = parseInt(localStorage.getItem('plvs_2_3_interactions') || '0', 10) + 1;
    localStorage.setItem('plvs_2_3_interactions', interactions.toString());
    let pageviews = parseInt(localStorage.getItem('plvs_2_3_pageviews') || '1', 10);
    let visitors = parseInt(localStorage.getItem('plvs_2_3_visitors') || '1', 10);
    updateStatsDisplay(pageviews, visitors, interactions);
}

function updateStatsDisplay(pv, vis, act) {
    const sPv = document.getElementById('stat-pageviews');
    const sVis = document.getElementById('stat-visitors');
    const sAct = document.getElementById('stat-interactions');
    if (sPv) sPv.innerText = pv;
    if (sVis) sVis.innerText = vis;
    if (sAct) sAct.innerText = act;

    const fPv = document.getElementById('footer-pageviews');
    const fVis = document.getElementById('footer-visitors');
    const fAct = document.getElementById('footer-interactions');
    if (fPv) fPv.innerText = pv;
    if (fVis) fVis.innerText = vis;
    if (fAct) fAct.innerText = act;
}

// ==========================================
// 3. 卡片網格渲染 (Core Rule 4: 雙欄無橫向捲軸)
// ==========================================
function renderCards() {
    const grid = document.getElementById('cards-grid');
    if (!grid) return;
    grid.innerHTML = '';

    const reviewSet = new Set(JSON.parse(localStorage.getItem('plvs_2_3_review_set') || '[]'));
    const masteredSet = new Set(JSON.parse(localStorage.getItem('plvs_2_3_mastered_set') || '[]'));

    allCards.forEach((card, idx) => {
        if (currentCategory !== 'all' && card.category !== currentCategory) return;
        if (currentCardView === 'review' && !reviewSet.has(card.id)) return;
        if (currentCardView === 'mastered' && !masteredSet.has(card.id)) return;

        const cardEl = document.createElement('div');
        cardEl.id = `card-wrapper-${idx}`;
        cardEl.className = 'flip-card-container group h-[530px] sm:h-[550px] lg:h-[565px] perspective';

        const isMastered = masteredSet.has(card.id);
        const isReview = reviewSet.has(card.id);
        const caseNumber = `CASE ${String(card.id).padStart(2, '0')}`;

        // 依題型動態賦予精美高對比徽章色彩
        let tagBadgeClass = 'bg-red-100 text-red-700 border border-red-200 font-black';
        if (card.tag.includes('例題')) {
            tagBadgeClass = 'bg-red-600 text-white font-black shadow-xs tracking-wide';
        } else if (card.tag.includes('隨堂')) {
            tagBadgeClass = 'bg-emerald-600 text-white font-black shadow-xs tracking-wide';
        } else if (card.tag.includes('觀念')) {
            tagBadgeClass = 'bg-indigo-600 text-white font-black shadow-xs tracking-wide';
        } else if (card.tag.includes('是非')) {
            tagBadgeClass = 'bg-amber-500 text-slate-950 font-black shadow-xs tracking-wide';
        } else if (card.tag.includes('習題')) {
            tagBadgeClass = 'bg-sky-600 text-white font-black shadow-xs tracking-wide';
        }

        cardEl.innerHTML = `
            <div id="card-inner-${idx}" class="flip-card-inner relative w-full h-full duration-500 transform-style-3d shadow-md hover:shadow-xl rounded-2xl border border-slate-200 bg-white transition-all">
                
                <!-- 卡片正面 (案件檔案：題目與審題提示) -->
                <div class="flip-card-front absolute w-full h-full backface-hidden rounded-2xl p-4 sm:p-5 lg:p-6 flex flex-col justify-between bg-gradient-to-b from-slate-50 via-white to-blue-50/30 overflow-hidden border-t-4 border-blue-900">
                    <div class="overflow-y-auto pr-1">
                        <!-- 標籤列 (柯南案卷標籤與題號) -->
                        <div class="flex items-center justify-between gap-2 mb-2 sm:mb-3">
                            <div class="flex items-center gap-1.5 flex-wrap">
                                <span class="px-2.5 py-0.5 text-xs font-black rounded-md bg-blue-900 text-white tracking-wider font-mono shadow-xs">
                                    ${caseNumber}
                                </span>
                                <span class="px-2.5 py-0.5 text-xs rounded-md ${tagBadgeClass}">
                                    ${card.tag}
                                </span>
                                <span class="text-xs font-bold text-slate-400">
                                    ${card.page}
                                </span>
                            </div>
                            <div class="flex items-center gap-1.5">
                                <button onclick="toggleCardStatus(event, ${card.id}, 'mastered')" class="p-1.5 rounded-lg text-xs font-bold transition-all ${isMastered ? 'bg-emerald-600 text-white' : 'bg-slate-100 text-slate-500 hover:bg-emerald-100 hover:text-emerald-700'}" title="結案歸檔（已熟練）">
                                    <i class="fa-solid fa-check"></i>
                                </button>
                                <button onclick="toggleCardStatus(event, ${card.id}, 'review')" class="p-1.5 rounded-lg text-xs font-bold transition-all ${isReview ? 'bg-amber-500 text-white' : 'bg-slate-100 text-slate-500 hover:bg-amber-100 hover:text-amber-700'}" title="標記待查證（待複習）">
                                    <i class="fa-solid fa-star"></i>
                                </button>
                                <button onclick="openModal(${idx})" class="p-1.5 rounded-lg bg-blue-100 text-blue-900 hover:bg-blue-900 hover:text-white transition-all text-xs font-bold" title="劇院全螢幕探案放大">
                                    <i class="fa-solid fa-expand"></i>
                                </button>
                            </div>
                        </div>

                        <!-- 標題 (使用 .innerHTML 渲染 KaTeX，加大字體) -->
                        <h3 class="text-lg sm:text-xl font-black text-slate-900 mb-2 leading-snug">
                            ${card.title}
                        </h3>

                        <!-- 題目核心內容 (案件密碼/題幹算式，加大字體 text-base sm:text-lg lg:text-xl) -->
                        <div class="front-math-container py-2 text-slate-800 text-base sm:text-lg lg:text-xl font-medium leading-relaxed break-words">
                            ${card.front_content}
                        </div>

                        <!-- 柯南審題思維導引 (加大字體 text-sm sm:text-base) -->
                        <div class="mt-3 p-3.5 rounded-xl bg-amber-50/90 border border-amber-300 text-sm sm:text-base text-amber-950 leading-relaxed shadow-2xs">
                            <span class="font-black text-red-600"><i class="fa-solid fa-magnifying-glass"></i> 柯南破案導引：</span>
                            ${card.front_tip}
                        </div>
                    </div>

                    <!-- 正面底部：自我破案抽屜按鈕與翻面按鈕 -->
                    <div class="pt-2.5 border-t border-slate-100 flex items-center justify-between">
                        <button onclick="toggleQuizDrawer(event, ${card.id})" class="text-xs font-bold text-blue-900 hover:text-red-600 flex items-center gap-1.5 py-1 px-2 rounded-md hover:bg-blue-50 transition-all">
                            <i class="fa-solid fa-clipboard-question"></i> 自主現場調查
                        </button>
                        <button onclick="flipCard(${idx})" class="text-xs font-bold bg-blue-950 hover:bg-red-600 text-white px-3.5 py-1.5 rounded-xl shadow-sm transition-all flex items-center gap-1.5">
                            <span>破案推理與證物</span> <i class="fa-solid fa-arrow-rotate-right text-[10px]"></i>
                        </button>
                    </div>

                    <!-- 自我破案即時檢核抽屜 (預設收合) -->
                    <div id="quiz-drawer-${card.id}" class="hidden absolute inset-0 bg-white/95 backdrop-blur-sm p-4 rounded-2xl flex flex-col justify-between z-20 border-2 border-blue-900 transition-all">
                        <div>
                            <div class="flex items-center justify-between mb-2">
                                <span class="text-xs font-black text-blue-900 flex items-center gap-1"><i class="fa-solid fa-fingerprint text-red-600"></i> 破案實力即時測驗</span>
                                <button onclick="toggleQuizDrawer(event, ${card.id})" class="text-slate-400 hover:text-slate-600 p-1">
                                    <i class="fa-solid fa-xmark"></i>
                                </button>
                            </div>
                            <p class="text-xs sm:text-sm font-bold text-slate-800 mb-3" id="quiz-q-${card.id}"></p>
                            <div class="space-y-1.5" id="quiz-opts-${card.id}"></div>
                        </div>
                        <div id="quiz-feedback-${card.id}" class="text-xs font-semibold p-2 rounded-lg hidden"></div>
                    </div>
                </div>

                <!-- 卡片背面 (名偵探推理筆記與證物圖解) -->
                <div id="card-back-${idx}" class="flip-card-back absolute w-full h-full backface-hidden rotate-y-180 rounded-2xl p-4 sm:p-5 lg:p-6 flex flex-col justify-between bg-gradient-to-b from-white via-slate-50 to-amber-50/20 overflow-hidden border-t-4 border-red-600">
                    <div class="overflow-y-auto pr-1">
                        <!-- 背面頂部操作列 (加入案號與題型題號標籤) -->
                        <div class="flex items-center justify-between gap-2 mb-2 pb-2 border-b border-slate-100">
                            <div class="flex items-center gap-1.5 flex-wrap">
                                <span class="px-2 py-0.5 text-xs font-black rounded-md bg-blue-900 text-white font-mono shadow-xs">${caseNumber}</span>
                                <span class="px-2.5 py-0.5 text-xs rounded-md ${tagBadgeClass}">${card.tag}</span>
                                <span class="text-xs font-black text-blue-950 flex items-center gap-1 ml-1">
                                    <i class="fa-solid fa-glasses text-red-600"></i> 推理筆記
                                </span>
                            </div>
                            <div class="flex items-center gap-1.5">
                                <button onclick="openModal(${idx})" class="p-1 rounded bg-slate-100 hover:bg-blue-100 text-slate-600 hover:text-blue-900 text-xs" title="劇院全螢幕探案">
                                    <i class="fa-solid fa-expand"></i>
                                </button>
                                <button onclick="flipCard(${idx})" class="p-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-600 text-xs" title="翻回案情">
                                    <i class="fa-solid fa-rotate-left"></i>
                                </button>
                            </div>
                        </div>

                        <!-- 步驟切換按鈕列 (Core Rule 10: 動態步數) -->
                        <div class="flex flex-wrap items-center gap-1 mb-2">
                            <button id="card-${idx}-step-btn-0" onclick="showStep(${idx}, 0)" class="step-btn px-2.5 py-1 text-xs font-bold rounded-lg bg-blue-900 text-white shadow-xs">全部</button>
                            ${card.steps.map((st, sIdx) => `
                                <button id="card-${idx}-step-btn-${sIdx+1}" onclick="showStep(${idx}, ${sIdx+1})" class="step-btn px-2.5 py-1 text-xs font-bold rounded-lg bg-slate-100 text-slate-700 hover:bg-blue-100 hover:text-blue-900">線索 ${sIdx+1}</button>
                            `).join('')}
                        </div>

                        <!-- 結構化步驟容器 (線索推理鏈，放大字體 text-sm sm:text-base) -->
                        <div class="space-y-2 text-sm sm:text-base">
                            ${card.steps.map((st, sIdx) => `
                                <div id="card-${idx}-step-${sIdx+1}" class="step-row step-row-${sIdx+1} p-2.5 rounded-lg bg-slate-50 border border-slate-200 cursor-pointer transition-all duration-300" onclick="showStep(${idx}, ${sIdx+1})">
                                    <span class="font-black text-blue-900 mr-2 text-sm sm:text-base">線索 ${st.num} [${st.title}]：</span>
                                    <span class="text-slate-800 leading-relaxed text-sm sm:text-base">${st.content}</span>
                                </div>
                            `).join('')}
                        </div>

                        <!-- 柯南破案印章結論列 (放大字體 text-sm sm:text-base) -->
                        <div id="card-${idx}-conclusion" class="conclusion-row mt-3 p-3 rounded-xl bg-red-50/80 border-2 border-red-500 text-sm sm:text-base font-bold text-red-950 transition-all duration-300 shadow-xs">
                            <div class="flex items-center gap-1.5 mb-1 text-red-600 font-black">
                                <i class="fa-solid fa-stamp"></i>
                                <span>【CASE CLOSED 真相永遠只有一個！】</span>
                            </div>
                            <div class="text-slate-900 leading-relaxed pl-1">${card.conclusion}</div>
                        </div>

                        <!-- 證物解析圖解 SVG 容器 -->
                        <div class="mt-3 p-2 bg-white rounded-xl border border-slate-200 flex items-center justify-center min-h-[150px] max-h-[190px] overflow-hidden">
                            ${card.svg}
                        </div>
                    </div>

                    <!-- 背面底部操作 -->
                    <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-xs text-slate-400">
                        <span class="font-mono font-semibold">${caseNumber} ‧ ${card.tag}</span>
                        <button onclick="flipCard(${idx})" class="font-bold text-slate-600 hover:text-red-600 flex items-center gap-1">
                            <i class="fa-solid fa-arrow-left"></i> 回案情
                        </button>
                    </div>
                </div>

            </div>
        `;

        grid.appendChild(cardEl);
        initCardQuiz(card.id);
    });

    if (window.renderMathInElement) {
        renderMathInElement(grid, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

function flipCard(idx) {
    recordInteraction();
    const inner = document.getElementById(`card-inner-${idx}`);
    if (inner) {
        inner.classList.toggle('rotate-y-180');
    }
}

function flipAllCards(toBack) {
    recordInteraction();
    allCards.forEach((_, idx) => {
        const inner = document.getElementById(`card-inner-${idx}`);
        if (inner) {
            if (toBack) {
                inner.classList.add('rotate-y-180');
            } else {
                inner.classList.remove('rotate-y-180');
            }
        }
    });
}

// ==========================================
// 4. 雙向同步逐步導引 (Core Rule 10: 防短路鐵律)
// ==========================================
function showStep(cardIdx, stepNum, silent = false) {
    if (!silent) recordInteraction();
    cardStepStates[cardIdx] = stepNum;
    const card = allCards[cardIdx];
    if (!card) return;

    const totalSteps = card.steps.length;

    const cardBackEl = document.getElementById(`card-back-${cardIdx}`);
    const modalBackContainer = document.getElementById('modal-steps-container');
    const isCurrentModal = (currentModalIndex === cardIdx);

    const targets = [];
    if (cardBackEl) targets.push({ container: cardBackEl, prefix: `card-${cardIdx}` });
    if (isCurrentModal && modalBackContainer) targets.push({ container: modalBackContainer, prefix: 'modal' });

    targets.forEach(({ container, prefix }) => {
        for (let i = 0; i <= totalSteps; i++) {
            const btn = document.getElementById(`${prefix}-step-btn-${i}`);
            if (btn) {
                if (i === stepNum) {
                    btn.className = 'step-btn px-2.5 py-1 text-xs font-black rounded-lg bg-indigo-600 text-white shadow-sm ring-2 ring-indigo-400';
                } else {
                    btn.className = 'step-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-100 text-slate-600 hover:bg-indigo-100 hover:text-indigo-700';
                }
            }
        }

        for (let s = 1; s <= totalSteps; s++) {
            const stepRow = container.querySelector(`.step-row-${s}`);
            if (stepRow) {
                if (stepNum === 0 || stepNum >= totalSteps) {
                    stepRow.className = `step-row step-row-${s} p-2.5 rounded-xl bg-slate-50 border border-slate-200 cursor-pointer opacity-100 transition-all duration-300`;
                } else if (s === stepNum) {
                    stepRow.className = `step-row step-row-${s} p-2.5 rounded-xl bg-indigo-100/90 border-2 border-indigo-500 shadow-sm opacity-100 scale-[1.01] cursor-pointer transition-all duration-300 ring-2 ring-indigo-300`;
                } else if (s < stepNum) {
                    stepRow.className = `step-row step-row-${s} p-2.5 rounded-xl bg-slate-50 border border-slate-200 cursor-pointer opacity-80 transition-all duration-300`;
                } else {
                    stepRow.className = `step-row step-row-${s} p-2.5 rounded-xl bg-slate-100/60 border border-dashed border-slate-300 cursor-pointer opacity-20 blur-[1.5px] pointer-events-none transition-all duration-300`;
                }
            }
        }

        const conclusionRow = (prefix === 'modal') 
            ? document.getElementById('modal-conclusion') 
            : document.getElementById(`card-${cardIdx}-conclusion`);
        if (conclusionRow) {
            if (stepNum === 0 || stepNum >= totalSteps) {
                conclusionRow.className = 'conclusion-row mt-2.5 p-2.5 rounded-xl bg-emerald-50 border border-emerald-300 text-xs sm:text-sm font-bold text-emerald-900 opacity-100 transition-all duration-300 shadow-xs';
            } else {
                conclusionRow.className = 'conclusion-row mt-2.5 p-2.5 rounded-xl bg-slate-100 border border-dashed border-slate-300 text-xs sm:text-sm font-semibold text-slate-400 opacity-20 blur-[1.5px] transition-all duration-300';
            }
        }
    });
}

// ==========================================
// 5. 劇院全螢幕模式 (Core Rule 11: 16:9 滿版寬螢幕佈局)
// ==========================================
function openModal(cardIdx, fromMap = false) {
    recordInteraction();
    currentModalIndex = cardIdx;
    fromMindmap = fromMap;
    const modal = document.getElementById('fullscreen-modal');
    if (!modal) return;

    modal.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');

    const backToMapBtn = document.getElementById('modal-back-to-mindmap-btn');
    if (backToMapBtn) {
        if (fromMindmap) {
            backToMapBtn.classList.remove('hidden');
        } else {
            backToMapBtn.classList.add('hidden');
        }
    }

    updateModalContent();
    clearWhiteboard();
    setWhiteboardMode('mouse');
}

function closeModal() {
    if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
    }
    const modal = document.getElementById('fullscreen-modal');
    if (modal) modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
}

function toggleCardModalFullscreen() {
    const modal = document.getElementById('fullscreen-modal');
    if (!modal) return;
    if (!document.fullscreenElement) {
        modal.requestFullscreen().catch(err => {
            console.log("全螢幕切換受限", err);
        });
    } else {
        document.exitFullscreen().catch(() => {});
    }
}

function returnToMindmap() {
    closeModal();
    openMindmapModal();
}

function updateModalContent() {
    const card = allCards[currentModalIndex];
    if (!card) return;

    const caseNumber = `CASE ${String(card.id).padStart(2, '0')}`;
    const mFrontTitle = document.getElementById('modal-front-title');
    const mFrontBadge = document.getElementById('modal-front-badge');
    const mFrontMath = document.getElementById('modal-front-math');
    const mFrontTip = document.getElementById('modal-front-tip');

    if (mFrontTitle) mFrontTitle.innerHTML = card.title;
    if (mFrontBadge) mFrontBadge.innerText = `${caseNumber} ‧ ${card.tag} ‧ ${card.page}`;
    if (mFrontMath) mFrontMath.innerHTML = card.front_content;
    if (mFrontTip) mFrontTip.innerHTML = `<span class="font-black text-red-600"><i class="fa-solid fa-magnifying-glass"></i> 柯南破案導引：</span>${card.front_tip}`;

    const mBackTitle = document.getElementById('modal-back-title');
    if (mBackTitle) mBackTitle.innerHTML = card.title;

    const mStepBtns = document.getElementById('modal-step-buttons');
    if (mStepBtns) {
        mStepBtns.innerHTML = `
            <button id="modal-step-btn-0" onclick="showStep(${currentModalIndex}, 0)" class="step-btn px-3 py-1 text-xs font-bold rounded-lg bg-blue-900 text-white shadow-sm">全部線索</button>
            ${card.steps.map((st, sIdx) => `
                <button id="modal-step-btn-${sIdx+1}" onclick="showStep(${currentModalIndex}, ${sIdx+1})" class="step-btn px-3 py-1 text-xs font-bold rounded-lg bg-slate-100 text-slate-600 hover:bg-blue-100 hover:text-blue-900">線索 ${sIdx+1}</button>
            `).join('')}
        `;
    }

    const mStepsContainer = document.getElementById('modal-steps-container');
    if (mStepsContainer) {
        mStepsContainer.innerHTML = card.steps.map((st, sIdx) => `
            <div class="step-row step-row-${sIdx+1} p-3 rounded-xl bg-slate-50 border border-slate-200 cursor-pointer transition-all duration-300" onclick="showStep(${currentModalIndex}, ${sIdx+1})">
                <span class="font-black text-blue-950 mr-2 text-sm">線索 ${st.num} [${st.title}]：</span>
                <span class="text-slate-800 text-sm leading-relaxed">${st.content}</span>
            </div>
        `).join('');
    }

    const mConclusion = document.getElementById('modal-conclusion');
    if (mConclusion) {
        mConclusion.innerHTML = `
            <div class="flex items-center gap-1.5 mb-1 text-red-600 font-black">
                <i class="fa-solid fa-stamp"></i>
                <span>【CASE CLOSED 真相永遠只有一個！】</span>
            </div>
            <div class="text-slate-900 font-bold pl-1">${card.conclusion}</div>
        `;
    }

    const mSvg = document.getElementById('modal-svg-container');
    if (mSvg) {
        mSvg.innerHTML = card.svg;
    }

    if (window.renderMathInElement) {
        renderMathInElement(document.getElementById('modal-content-wrapper'), {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }

    const savedStep = cardStepStates[currentModalIndex] || 0;
    showStep(currentModalIndex, savedStep, true);

    const mIdx = document.getElementById('modal-card-indicator');
    if (mIdx) mIdx.innerText = `${currentModalIndex + 1} / ${allCards.length}`;
}

function prevModalCard() {
    if (currentModalIndex > 0) {
        currentModalIndex--;
        updateModalContent();
    }
}

function nextModalCard() {
    if (currentModalIndex < allCards.length - 1) {
        currentModalIndex++;
        updateModalContent();
    }
}

// ==========================================
// 6. 多功能電子白板 (Core Rule 7: 滑鼠穿透操作、畫筆書寫、橡皮擦、粗細、選色)
// ==========================================
function initWhiteboard() {
    whiteboardCanvas = document.getElementById('whiteboard-canvas');
    if (!whiteboardCanvas) return;
    whiteboardCtx = whiteboardCanvas.getContext('2d');

    resizeWhiteboard();
    window.addEventListener('resize', resizeWhiteboard);

    whiteboardCanvas.addEventListener('mousedown', startDrawing);
    whiteboardCanvas.addEventListener('mousemove', draw);
    whiteboardCanvas.addEventListener('mouseup', stopDrawing);
    whiteboardCanvas.addEventListener('mouseleave', stopDrawing);

    whiteboardCanvas.addEventListener('touchstart', (e) => {
        if (whiteboardMode === 'mouse') return;
        const touch = e.touches[0];
        const rect = whiteboardCanvas.getBoundingClientRect();
        const mouseEvent = new MouseEvent('mousedown', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        whiteboardCanvas.dispatchEvent(mouseEvent);
    }, {passive: false});

    whiteboardCanvas.addEventListener('touchmove', (e) => {
        if (whiteboardMode === 'mouse') return;
        const touch = e.touches[0];
        const mouseEvent = new MouseEvent('mousemove', {
            clientX: touch.clientX,
            clientY: touch.clientY
        });
        whiteboardCanvas.dispatchEvent(mouseEvent);
    }, {passive: false});

    whiteboardCanvas.addEventListener('touchend', () => {
        if (whiteboardMode === 'mouse') return;
        const mouseEvent = new MouseEvent('mouseup', {});
        whiteboardCanvas.dispatchEvent(mouseEvent);
    });

    setWhiteboardMode('mouse');
}

function resizeWhiteboard() {
    if (!whiteboardCanvas) return;
    const rect = whiteboardCanvas.getBoundingClientRect();
    if (rect.width === 0 || rect.height === 0) return;

    let tempCanvas = null;
    if (whiteboardCanvas.width > 0 && whiteboardCanvas.height > 0) {
        tempCanvas = document.createElement('canvas');
        tempCanvas.width = whiteboardCanvas.width;
        tempCanvas.height = whiteboardCanvas.height;
        const tempCtx = tempCanvas.getContext('2d');
        tempCtx.drawImage(whiteboardCanvas, 0, 0);
    }

    whiteboardCanvas.width = rect.width;
    whiteboardCanvas.height = rect.height;

    if (tempCanvas && whiteboardCtx) {
        whiteboardCtx.drawImage(tempCanvas, 0, 0, rect.width, rect.height);
    }
}

let lastDrawX = 0;
let lastDrawY = 0;

function hexToRgba(hex, alpha) {
    if (!hex) return `rgba(250, 204, 21, ${alpha})`;
    if (hex.startsWith('rgba')) return hex;
    if (hex.startsWith('rgb')) {
        return hex.replace('rgb', 'rgba').replace(')', `, ${alpha})`);
    }
    let c = hex.replace('#', '');
    if (c.length === 3) c = c.split('').map(x => x + x).join('');
    const num = parseInt(c, 16);
    if (isNaN(num)) return `rgba(250, 204, 21, ${alpha})`;
    const r = (num >> 16) & 255;
    const g = (num >> 8) & 255;
    const b = num & 255;
    return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

function setWhiteboardMode(mode) {
    whiteboardMode = mode;
    isEraserMode = (mode === 'eraser');
    if (!whiteboardCanvas) return;

    if (mode === 'mouse') {
        // 核心關鍵：pointer-events: none 徹底釋放滑鼠，底層所有卡片內容、按鈕皆可點選操作
        whiteboardCanvas.style.pointerEvents = 'none';
        whiteboardCanvas.style.cursor = 'default';
    } else if (mode === 'pen') {
        whiteboardCanvas.style.pointerEvents = 'auto';
        whiteboardCanvas.style.cursor = 'crosshair';
        if (currentPenSize > 8) currentPenSize = 4;
    } else if (mode === 'highlighter') {
        whiteboardCanvas.style.pointerEvents = 'auto';
        whiteboardCanvas.style.cursor = 'crosshair';
        if (currentPenSize < 12) currentPenSize = 18;
        if (currentPenColor === '#0f172a' || currentPenColor === '#000000') {
            currentPenColor = '#facc15'; // 螢光黃預設
        }
    } else if (mode === 'eraser') {
        whiteboardCanvas.style.pointerEvents = 'auto';
        whiteboardCanvas.style.cursor = 'cell';
    }

    const sizeSelect = document.getElementById('wb-pen-size-select');
    if (sizeSelect && (mode === 'highlighter' || mode === 'pen')) {
        sizeSelect.value = currentPenSize.toString();
    }
    const eraserSelect = document.getElementById('wb-eraser-size-select');
    if (eraserSelect && mode === 'eraser') {
        eraserSelect.value = currentEraserSize.toString();
    }
    const alphaSelect = document.getElementById('wb-highlighter-alpha');
    if (alphaSelect) {
        alphaSelect.value = currentHighlighterAlpha.toString();
    }

    updateWhiteboardToolUI();
}

function startDrawing(e) {
    if (whiteboardMode === 'mouse') return;
    isDrawing = true;
    saveStrokeState();
    lastDrawX = e.offsetX;
    lastDrawY = e.offsetY;
}

function draw(e) {
    if (!isDrawing || whiteboardMode === 'mouse') return;
    whiteboardCtx.lineCap = 'round';
    whiteboardCtx.lineJoin = 'round';

    if (whiteboardMode === 'eraser') {
        // 橡皮擦大小動態調整
        whiteboardCtx.lineWidth = currentEraserSize;
        whiteboardCtx.globalCompositeOperation = 'destination-out';
        whiteboardCtx.strokeStyle = 'rgba(0,0,0,1)';
    } else if (whiteboardMode === 'highlighter' || currentPenSize >= 14) {
        // 螢光筆模式：動態粗細與自訂透明度 (currentHighlighterAlpha)
        whiteboardCtx.lineWidth = currentPenSize;
        whiteboardCtx.globalCompositeOperation = 'source-over';
        whiteboardCtx.strokeStyle = hexToRgba(currentPenColor, currentHighlighterAlpha);
    } else {
        whiteboardCtx.lineWidth = currentPenSize;
        whiteboardCtx.globalCompositeOperation = 'source-over';
        whiteboardCtx.strokeStyle = currentPenColor;
    }

    whiteboardCtx.beginPath();
    whiteboardCtx.moveTo(lastDrawX, lastDrawY);
    whiteboardCtx.lineTo(e.offsetX, e.offsetY);
    whiteboardCtx.stroke();

    lastDrawX = e.offsetX;
    lastDrawY = e.offsetY;
}

function stopDrawing() {
    if (isDrawing) {
        isDrawing = false;
        if (whiteboardCtx) whiteboardCtx.closePath();
    }
}

function setPenColor(color) {
    currentPenColor = color;
    if (whiteboardMode === 'mouse') {
        setWhiteboardMode('pen');
    } else {
        updateWhiteboardToolUI();
    }
}

function setPenSize(size) {
    currentPenSize = parseInt(size, 10) || 4;
    if (currentPenSize >= 14 && whiteboardMode !== 'highlighter') {
        setWhiteboardMode('highlighter');
    } else if (currentPenSize < 14 && whiteboardMode === 'highlighter') {
        setWhiteboardMode('pen');
    } else if (whiteboardMode === 'mouse') {
        setWhiteboardMode('pen');
    }
}

function setHighlighterAlpha(alpha) {
    currentHighlighterAlpha = parseFloat(alpha) || 0.4;
    const alphaSelect = document.getElementById('wb-highlighter-alpha');
    if (alphaSelect) alphaSelect.value = currentHighlighterAlpha.toString();
    if (whiteboardMode !== 'highlighter') {
        setWhiteboardMode('highlighter');
    }
}

function setEraserSize(size) {
    currentEraserSize = parseInt(size, 10) || 26;
    const eraserSelect = document.getElementById('wb-eraser-size-select');
    if (eraserSelect) eraserSelect.value = currentEraserSize.toString();
    if (whiteboardMode !== 'eraser') {
        setWhiteboardMode('eraser');
    }
}

function toggleEraser(isEraser) {
    setWhiteboardMode(isEraser ? 'eraser' : 'pen');
}

function updateWhiteboardToolUI() {
    const mouseBtn = document.getElementById('wb-tool-mouse');
    const penBtn = document.getElementById('wb-tool-pen');
    const highlighterBtn = document.getElementById('wb-tool-highlighter');
    const eraserBtn = document.getElementById('wb-tool-eraser');
    const floatMouseBtn = document.getElementById('wb-float-mouse');
    const floatPenBtn = document.getElementById('wb-float-pen');
    const floatHighlighterBtn = document.getElementById('wb-float-highlighter');
    const floatEraserBtn = document.getElementById('wb-float-eraser');

    // 工具群組顯示控制
    const penSizeGroup = document.getElementById('wb-pen-size-group');
    const alphaGroup = document.getElementById('wb-alpha-group');
    const eraserSizeGroup = document.getElementById('wb-eraser-size-group');
    const colorsGroup = document.getElementById('wb-colors-group');

    if (penSizeGroup && alphaGroup && eraserSizeGroup && colorsGroup) {
        if (whiteboardMode === 'eraser') {
            eraserSizeGroup.classList.remove('hidden');
            eraserSizeGroup.classList.add('flex');
            penSizeGroup.classList.add('hidden');
            penSizeGroup.classList.remove('flex');
            alphaGroup.classList.add('hidden');
            alphaGroup.classList.remove('flex');
            colorsGroup.classList.add('hidden');
            colorsGroup.classList.remove('flex');
        } else if (whiteboardMode === 'highlighter') {
            eraserSizeGroup.classList.add('hidden');
            eraserSizeGroup.classList.remove('flex');
            penSizeGroup.classList.remove('hidden');
            penSizeGroup.classList.add('flex');
            alphaGroup.classList.remove('hidden');
            alphaGroup.classList.add('flex');
            colorsGroup.classList.remove('hidden');
            colorsGroup.classList.add('flex');
        } else if (whiteboardMode === 'pen') {
            eraserSizeGroup.classList.add('hidden');
            eraserSizeGroup.classList.remove('flex');
            penSizeGroup.classList.remove('hidden');
            penSizeGroup.classList.add('flex');
            alphaGroup.classList.add('hidden');
            alphaGroup.classList.remove('flex');
            colorsGroup.classList.remove('hidden');
            colorsGroup.classList.add('flex');
        } else {
            // mouse mode
            eraserSizeGroup.classList.add('hidden');
            eraserSizeGroup.classList.remove('flex');
            penSizeGroup.classList.remove('hidden');
            penSizeGroup.classList.add('flex');
            alphaGroup.classList.add('hidden');
            alphaGroup.classList.remove('flex');
            colorsGroup.classList.remove('hidden');
            colorsGroup.classList.add('flex');
        }
    }

    // 頂部白板工具列按鈕高亮與樣式更新
    if (mouseBtn) {
        if (whiteboardMode === 'mouse') {
            mouseBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-emerald-600 text-white shadow-md ring-2 ring-emerald-400";
        } else {
            mouseBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700";
        }
    }
    if (penBtn) {
        if (whiteboardMode === 'pen') {
            penBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-indigo-600 text-white shadow-md ring-2 ring-indigo-400";
        } else {
            penBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700";
        }
    }
    if (highlighterBtn) {
        if (whiteboardMode === 'highlighter') {
            highlighterBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-amber-500 text-slate-900 shadow-md ring-2 ring-amber-300 font-black";
        } else {
            highlighterBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1.5 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700";
        }
    }
    if (eraserBtn) {
        if (whiteboardMode === 'eraser') {
            eraserBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1 transition-all bg-amber-600 text-white shadow-md ring-2 ring-amber-400";
        } else {
            eraserBtn.className = "px-2.5 py-1.5 rounded-lg text-xs font-bold flex items-center gap-1 transition-all bg-slate-800 text-slate-300 hover:text-white hover:bg-slate-700";
        }
    }

    // 懸浮快捷切換膠囊更新
    if (floatMouseBtn) {
        if (whiteboardMode === 'mouse') {
            floatMouseBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all bg-emerald-600 text-white shadow-lg ring-2 ring-emerald-400 font-black";
        } else {
            floatMouseBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800";
        }
    }
    if (floatPenBtn) {
        if (whiteboardMode === 'pen') {
            floatPenBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all bg-indigo-600 text-white shadow-lg ring-2 ring-indigo-400 font-black";
        } else {
            floatPenBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800";
        }
    }
    if (floatHighlighterBtn) {
        if (whiteboardMode === 'highlighter') {
            floatHighlighterBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all bg-amber-500 text-slate-900 shadow-lg ring-2 ring-amber-300 font-black";
        } else {
            floatHighlighterBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800";
        }
    }
    if (floatEraserBtn) {
        if (whiteboardMode === 'eraser') {
            floatEraserBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all bg-amber-600 text-white shadow-lg ring-2 ring-amber-400 font-black";
        } else {
            floatEraserBtn.className = "px-3.5 py-1.5 rounded-full flex items-center gap-1.5 transition-all text-slate-300 hover:text-white hover:bg-slate-800";
        }
    }
}



function saveStrokeState() {
    if (!whiteboardCanvas || !whiteboardCtx) return;
    if (strokeHistory.length > 20) strokeHistory.shift();
    strokeHistory.push(whiteboardCtx.getImageData(0, 0, whiteboardCanvas.width, whiteboardCanvas.height));
}

function undoStroke() {
    if (!whiteboardCanvas || !whiteboardCtx) return;
    if (strokeHistory.length > 0) {
        const lastState = strokeHistory.pop();
        whiteboardCtx.putImageData(lastState, 0, 0);
    } else {
        clearWhiteboard();
    }
}

function clearWhiteboard() {
    if (!whiteboardCanvas || !whiteboardCtx) return;
    whiteboardCtx.clearRect(0, 0, whiteboardCanvas.width, whiteboardCanvas.height);
    strokeHistory = [];
}


// ==========================================
// 6.5 名偵探解密口訣錦囊視窗
// ==========================================
function openCheatSheetModal() {
    recordInteraction();
    const modal = document.getElementById('cheatsheet-modal');
    if (modal) {
        modal.classList.remove('hidden');
        if (window.renderMathInElement) {
            renderMathInElement(modal, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        }
    }
    document.body.classList.add('overflow-hidden');
}

function closeCheatSheetModal() {
    const modal = document.getElementById('cheatsheet-modal');
    if (modal) modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
}

// ==========================================
// 7. 心智圖視窗 (Core Rule 6: 返回鍵與全螢幕投影)
// ==========================================
function openMindmapModal() {
    recordInteraction();
    const mm = document.getElementById('mindmap-modal');
    if (mm) mm.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');
    const treeContainer = document.getElementById('mindmap-tree-content');
    if (treeContainer && window.renderMathInElement) {
        renderMathInElement(treeContainer, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

function closeMindmapModal() {
    const mm = document.getElementById('mindmap-modal');
    if (mm) mm.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
}

function toggleMindmapFullscreen() {
    const mm = document.getElementById('mindmap-modal-dialog');
    if (!mm) return;
    if (!document.fullscreenElement) {
        mm.requestFullscreen().catch(err => {
            console.log("全螢幕切換受限", err);
        });
    } else {
        document.exitFullscreen();
    }
}

function renderMindmapTree() {
    const treeContainer = document.getElementById('mindmap-tree-content');
    if (!treeContainer) return;

    const chapters = [
        {
            title: "一、對數概念與存在條件 (Cards 01~02, 05~08)",
            icon: "fa-book-open",
            color: "blue",
            items: allCards.filter(c => c.category === "對數定義" || c.category === "存在條件")
        },
        {
            title: "二、對數基本性質與求值 (Cards 03, 09~20)",
            icon: "fa-calculator",
            color: "emerald",
            items: allCards.filter(c => c.category === "基本性質" || c.category === "對數求值")
        },
        {
            title: "三、同底對數加減運算 (Cards 21~26)",
            icon: "fa-plus-minus",
            color: "amber",
            items: allCards.filter(c => c.category === "加減運算")
        },
        {
            title: "四、換底公式與連鎖律 (Cards 04, 27~36)",
            icon: "fa-link",
            color: "purple",
            items: allCards.filter(c => c.category === "換底連鎖" || c.category === "換底公式" || c.category === "連鎖律")
        },
        {
            title: "五、綜合代數與數值逼近 (Cards 37~42)",
            icon: "fa-chart-line",
            color: "indigo",
            items: allCards.filter(c => c.category === "綜合應用")
        },
        {
            title: "六、自我評量與生活素養 (Cards 43~65)",
            icon: "fa-trophy",
            color: "rose",
            items: allCards.filter(c => c.category === "課後習作" || c.category === "進階思考" || c.category === "素養應用" || c.id >= 43)
        }
    ];

    treeContainer.innerHTML = chapters.map((ch) => `
        <div class="mb-4 bg-slate-50 border border-slate-200 rounded-xl p-3.5">
            <div class="font-bold text-slate-800 text-sm mb-2 flex items-center gap-2">
                <i class="fa-solid ${ch.icon} text-${ch.color}-600"></i>
                <span>${ch.title}</span>
            </div>
            <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-2">
                ${ch.items.map(it => `
                    <button onclick="jumpToCardFromMindmap(${it.id - 1})" class="p-2 rounded-lg bg-white border border-slate-200 hover:border-indigo-400 hover:shadow-sm text-left transition-all group">
                        <div class="text-[11px] font-black text-indigo-600 group-hover:text-indigo-800">${it.tag}</div>
                        <div class="text-xs text-slate-700 truncate font-semibold">${it.title}</div>
                    </button>
                `).join('')}
            </div>
        </div>
    `).join('');

    if (window.renderMathInElement) {
        renderMathInElement(treeContainer, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

function jumpToCardFromMindmap(cardIdx) {
    closeMindmapModal();
    openModal(cardIdx, true);
}

// ==========================================
// 8. 學習進度追蹤 (熟練/複習)
// ==========================================
function toggleCardStatus(event, cardId, type) {
    event.stopPropagation();
    recordInteraction();

    const storageKey = `plvs_2_3_${type}_set`;
    let set = new Set(JSON.parse(localStorage.getItem(storageKey) || '[]'));

    if (set.has(cardId)) {
        set.delete(cardId);
    } else {
        set.add(cardId);
        if (type === 'mastered') {
            let revSet = new Set(JSON.parse(localStorage.getItem('plvs_2_3_review_set') || '[]'));
            revSet.delete(cardId);
            localStorage.setItem('plvs_2_3_review_set', JSON.stringify(Array.from(revSet)));
        }
    }

    localStorage.setItem(storageKey, JSON.stringify(Array.from(set)));
    renderCards();
    updateProgressBar();
}

function updateProgressBar() {
    const masteredSet = new Set(JSON.parse(localStorage.getItem('plvs_2_3_mastered_set') || '[]'));
    const reviewSet = new Set(JSON.parse(localStorage.getItem('plvs_2_3_review_set') || '[]'));

    const total = allCards.length || 65;
    const mCount = masteredSet.size;
    const rCount = reviewSet.size;

    const percent = Math.round((mCount / total) * 100);
    const pBar = document.getElementById('progress-bar-fill');
    const pText = document.getElementById('progress-text');

    if (pBar) pBar.style.width = `${percent}%`;
    if (pText) pText.innerText = `已熟練 ${mCount} / ${total} 張 (${percent}%) ‧ 待複習 ${rCount} 張`;
}

function filterByStatus(view) {
    recordInteraction();
    currentCardView = view;
    renderCards();
}

function filterByCategory(cat) {
    recordInteraction();
    currentCategory = cat;
    renderCards();
}

// ==========================================
// 9. 正面即時測驗抽屜
// ==========================================
function toggleQuizDrawer(event, cardId) {
    event.stopPropagation();
    recordInteraction();
    const drawer = document.getElementById(`quiz-drawer-${cardId}`);
    if (drawer) {
        drawer.classList.toggle('hidden');
    }
}

function initCardQuiz(cardId) {
    const quiz = (window.QUIZ_DATA && window.QUIZ_DATA[cardId]) || null;
    if (!quiz) return;

    const qTitle = document.getElementById(`quiz-q-${cardId}`);
    const qOpts = document.getElementById(`quiz-opts-${cardId}`);
    if (qTitle) qTitle.innerHTML = quiz.question;

    if (qOpts) {
        qOpts.innerHTML = quiz.options.map((opt, oIdx) => `
            <button onclick="submitCardQuiz(${cardId}, ${oIdx})" class="w-full text-left p-2 rounded-lg text-xs font-semibold bg-slate-50 border border-slate-200 hover:bg-indigo-50 hover:border-indigo-300 transition-all">
                ${String.fromCharCode(65 + oIdx)}. ${opt}
            </button>
        `).join('');
    }
}

function submitCardQuiz(cardId, selectedIdx) {
    recordInteraction();
    const quiz = window.QUIZ_DATA[cardId];
    if (!quiz) return;

    const fb = document.getElementById(`quiz-feedback-${cardId}`);
    if (!fb) return;

    fb.classList.remove('hidden');
    if (selectedIdx === quiz.answer) {
        fb.className = 'text-xs font-bold p-2.5 rounded-lg bg-emerald-100 text-emerald-800 border border-emerald-300';
        fb.innerHTML = `<i class="fa-solid fa-circle-check text-emerald-600 mr-1"></i> 答對了！${quiz.explanation}`;
    } else {
        fb.className = 'text-xs font-bold p-2.5 rounded-lg bg-rose-100 text-rose-800 border border-rose-300';
        fb.innerHTML = `<i class="fa-solid fa-circle-xmark text-rose-600 mr-1"></i> 再試一次！正確答案是 (${String.fromCharCode(65 + quiz.answer)})。<br>${quiz.explanation}`;
    }

    if (window.renderMathInElement) {
        renderMathInElement(fb, {
            delimiters: [
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}

// ==========================================
// 10. 單元動態幾何實驗室 (Lab 1 & Lab 2)
// ==========================================
function openLabModal() {
    recordInteraction();
    const modal = document.getElementById('lab-modal');
    if (modal) {
        modal.classList.remove('hidden');
        if (window.renderMathInElement) {
            renderMathInElement(modal, {
                delimiters: [
                    {left: '$$', right: '$$', display: true},
                    {left: '$', right: '$', display: false}
                ],
                throwOnError: false
            });
        }
    }
    document.body.classList.add('overflow-hidden');
    renderLogCurveLab();
    renderEarthquakeLab();
}

function closeLabModal() {
    const modal = document.getElementById('lab-modal');
    if (modal) modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
}

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
}

function renderLogCurveLab() {
    const container = document.getElementById('lab-curve-svg-container');
    const valText = document.getElementById('lab-base-val');
    if (valText) valText.innerText = currentLabBase.toFixed(1);

    if (!container) return;
    const a = currentLabBase;
    const isIncreasing = (a > 1);

    // 產生 y = log_a(x) 的 SVG 路徑點 (x 從 0.15 到 8.5)
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
            <!-- 坐標軸線 -->
            <line x1="20" y1="120" x2="360" y2="120" stroke="#94a3b8" stroke-width="1.5"/>
            <line x1="50" y1="230" x2="50" y2="20" stroke="#94a3b8" stroke-width="1.5"/>

            <!-- 軸標籤與原點 (KaTeX 渲染) -->
            <foreignObject x="350" y="102" width="24" height="24">
                <div xmlns="http://www.w3.org/1999/xhtml" class="text-xs text-slate-500 font-serif">$x$</div>
            </foreignObject>
            <foreignObject x="56" y="12" width="24" height="24">
                <div xmlns="http://www.w3.org/1999/xhtml" class="text-xs text-slate-500 font-serif">$y$</div>
            </foreignObject>
            <foreignObject x="32" y="124" width="20" height="20">
                <div xmlns="http://www.w3.org/1999/xhtml" class="text-xs text-slate-500 font-serif">$O$</div>
            </foreignObject>

            <!-- 垂直漸近線 x = 0 (紅色虛線) -->
            <line x1="50" y1="20" x2="50" y2="230" stroke="#dc2626" stroke-width="1.5" stroke-dasharray="3,3"/>

            <!-- 關鍵定點 (1, 0) -->
            <circle cx="${originX + 1 * scaleX}" cy="${originY}" r="4" fill="#2563eb"/>
            <foreignObject x="${originX + 1 * scaleX - 10}" y="${originY - 26}" width="55" height="24">
                <div xmlns="http://www.w3.org/1999/xhtml" class="text-[11px] font-bold text-blue-600 text-center">$(1, 0)$</div>
            </foreignObject>

            <!-- 對數曲線動態繪製 -->
            <path d="${pathD}" fill="none" stroke="${isIncreasing ? '#2563eb' : '#dc2626'}" stroke-width="3"/>

            <!-- 印刷級數學方程式卡片 (KaTeX 渲染) -->
            <foreignObject x="175" y="15" width="195" height="95">
                <div xmlns="http://www.w3.org/1999/xhtml" class="bg-white/95 backdrop-blur-xs p-2.5 rounded-xl border ${isIncreasing ? 'border-blue-200' : 'border-rose-200'} shadow-md">
                    <div class="flex items-center justify-between pb-1 border-b border-slate-100">
                        <div class="text-base font-bold ${isIncreasing ? 'text-blue-800' : 'text-rose-800'}">
                            $y = \\log_{${a.toFixed(1)}} x$
                        </div>
                        <span class="text-[10px] font-black px-1.5 py-0.5 rounded ${isIncreasing ? 'bg-blue-100 text-blue-700' : 'bg-rose-100 text-rose-700'}">
                            ${isIncreasing ? '嚴格遞增' : '嚴格遞減'}
                        </span>
                    </div>
                    <div class="text-xs text-slate-600 mt-1.5 flex items-center gap-1 font-medium">
                        <span class="w-1.5 h-1.5 rounded-full bg-rose-500 shrink-0"></span>
                        <span>垂直漸近線：$x = 0$（$y$ 軸）</span>
                    </div>
                    <div class="text-[11px] text-slate-500 mt-0.5 flex items-center gap-1">
                        <span class="w-1.5 h-1.5 rounded-full bg-blue-500 shrink-0"></span>
                        <span>恆過定點：$(1, 0)$</span>
                    </div>
                </div>
            </foreignObject>
        </svg>
    `;

    if (window.renderMathInElement) {
        renderMathInElement(container, {
            delimiters: [
                {left: '$$', right: '$$', display: true},
                {left: '$', right: '$', display: false}
            ],
            throwOnError: false
        });
    }
}


function renderEarthquakeLab() {
    const M = currentEarthquakeM;
    const logE = 11.8 + 1.5 * M;
    const valText = document.getElementById('lab-eq-val');
    const resText = document.getElementById('lab-eq-result');

    if (valText) valText.innerText = M.toFixed(1);
    if (resText) {
        // 相當於幾顆廣島原子彈 (廣島原子彈約 6.3 x 10^20 爾格 = 10^20.8 爾格)
        const bombRatio = Math.pow(10, logE - 20.8);
        let ratioDesc = "";
        if (bombRatio < 0.01) {
            ratioDesc = "小型有感地震，地表輕微搖晃";
        } else if (bombRatio < 1) {
            ratioDesc = `約相當於 ${(bombRatio * 100).toFixed(1)}% 顆廣島原子彈能量`;
        } else {
            ratioDesc = `相當於爆炸約 ${Math.round(bombRatio).toLocaleString()} 顆廣島原子彈！`;
        }
        resText.innerHTML = `
            <div class="text-sm font-bold text-slate-800">
                釋放能量：$E = 10^{${logE.toFixed(2)}}$ 爾格
            </div>
            <div class="text-xs font-semibold text-rose-600 mt-1">
                ${ratioDesc}
            </div>
        `;
        if (window.renderMathInElement) {
            renderMathInElement(resText, {
                delimiters: [{left: '$', right: '$', display: false}],
                throwOnError: false
            });
        }
    }
}

// ==========================================
// 11. 六大關卡闖關系統 (Core Rule 7)
// ==========================================
function openChallengeModal(stageIdx = 0) {
    recordInteraction();
    currentStageIndex = stageIdx;
    const modal = document.getElementById('challenge-modal');
    if (modal) modal.classList.remove('hidden');
    document.body.classList.add('overflow-hidden');
    initStageQuiz();
}

function closeChallengeModal() {
    const modal = document.getElementById('challenge-modal');
    if (modal) modal.classList.add('hidden');
    document.body.classList.remove('overflow-hidden');
}

function initStageQuiz() {
    const stages = window.CHALLENGE_STAGES || [];
    const stage = stages[currentStageIndex];
    if (!stage) return;

    currentLives = 3;
    currentScore = 0;
    currentCombo = 0;
    maxCombo = 0;
    currentQuizQuestionIndex = 0;

    // 挑選題目
    if (stage.card_ids === "RANDOM_10") {
        const shuffled = [...allCards].sort(() => 0.5 - Math.random());
        stageQuizList = shuffled.slice(0, 10).map(c => c.id);
    } else {
        stageQuizList = [...stage.card_ids];
    }

    updateStageUI();
    renderCurrentStageQuestion();
}

function updateStageUI() {
    const stage = window.CHALLENGE_STAGES[currentStageIndex];
    const sTitle = document.getElementById('stage-title');
    const sDesc = document.getElementById('stage-desc');
    const sLives = document.getElementById('stage-lives');
    const sScore = document.getElementById('stage-score');
    const sCombo = document.getElementById('stage-combo');

    if (sTitle) sTitle.innerText = stage.title;
    if (sDesc) sDesc.innerText = stage.desc;
    if (sLives) sLives.innerHTML = '🎯'.repeat(currentLives) + '💨'.repeat(Math.max(0, 3 - currentLives));
    if (sScore) sScore.innerText = currentScore;
    if (sCombo) sCombo.innerText = currentCombo > 1 ? `⚡ 連續破案 x${currentCombo}！` : '';
}

function renderCurrentStageQuestion() {
    const container = document.getElementById('stage-question-container');
    if (!container) return;

    if (currentQuizQuestionIndex >= stageQuizList.length) {
        finishStage(true);
        return;
    }

    const cardId = stageQuizList[currentQuizQuestionIndex];
    const quiz = window.QUIZ_DATA[cardId];
    if (!quiz) {
        currentQuizQuestionIndex++;
        renderCurrentStageQuestion();
        return;
    }

    const caseNumber = `CASE ${String(cardId).padStart(2, '0')}`;

    container.innerHTML = `
        <div class="mb-3 text-xs font-black text-blue-900 flex items-center justify-between">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-folder-open text-red-600"></i> 搜查進度：第 ${currentQuizQuestionIndex + 1} / ${stageQuizList.length} 題 (${caseNumber})</span>
            <span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-bold">結案門檻：${window.CHALLENGE_STAGES[currentStageIndex].pass_score} 分</span>
        </div>
        <div class="text-sm sm:text-base font-bold text-slate-900 mb-4 bg-white p-3.5 rounded-xl border border-slate-200" id="stage-q-text">
            ${quiz.question}
        </div>
        <div class="grid grid-cols-1 sm:grid-cols-2 gap-2.5" id="stage-opt-list">
            ${quiz.options.map((opt, oIdx) => `
                <button onclick="handleStageAnswer(${cardId}, ${oIdx})" class="p-3 text-left rounded-xl bg-white border border-slate-200 hover:border-blue-900 hover:bg-blue-50/50 font-semibold text-xs sm:text-sm text-slate-800 transition-all shadow-2xs">
                    <span class="font-bold text-red-600 mr-1 font-mono">${String.fromCharCode(65 + oIdx)}.</span> ${opt}
                </button>
            `).join('')}
        </div>
        <div id="stage-feedback" class="mt-4 p-3 rounded-xl hidden text-xs sm:text-sm font-bold"></div>
    `;

    if (window.renderMathInElement) {
        renderMathInElement(container, {
            delimiters: [{left: '$', right: '$', display: false}],
            throwOnError: false
        });
    }
}

function handleStageAnswer(cardId, selectedIdx) {
    recordInteraction();
    const quiz = window.QUIZ_DATA[cardId];
    if (!quiz) return;

    const fb = document.getElementById('stage-feedback');
    const optList = document.getElementById('stage-opt-list');
    if (!fb || !optList) return;

    const buttons = optList.querySelectorAll('button');
    buttons.forEach(btn => btn.disabled = true);

    fb.classList.remove('hidden');

    if (selectedIdx === quiz.answer) {
        currentCombo++;
        if (currentCombo > maxCombo) maxCombo = currentCombo;
        currentScore += (10 + (currentCombo - 1) * 2);
        fb.className = 'mt-4 p-3 rounded-xl bg-emerald-100 text-emerald-900 border-2 border-emerald-400 shadow-xs';
        fb.innerHTML = `
            <div class="flex items-center justify-between">
                <span><i class="fa-solid fa-stamp text-red-600 mr-1.5"></i> 推理正確！真相破解 +${10 + (currentCombo - 1) * 2} 分</span>
                <button onclick="nextStageQuestion()" class="px-3 py-1 bg-emerald-700 text-white rounded-lg text-xs font-bold hover:bg-emerald-800 shadow-xs">下一案 ❯</button>
            </div>
            <div class="text-xs font-medium mt-1 text-slate-700">${quiz.explanation}</div>
        `;
    } else {
        currentCombo = 0;
        currentLives--;
        fb.className = 'mt-4 p-3 rounded-xl bg-red-100 text-red-950 border-2 border-red-400 shadow-xs';
        fb.innerHTML = `
            <div class="flex items-center justify-between">
                <span><i class="fa-solid fa-circle-xmark text-red-600 mr-1.5"></i> 證物判斷有誤！麻醉針指針減 1</span>
                <button onclick="nextStageQuestion()" class="px-3 py-1 bg-red-600 text-white rounded-lg text-xs font-bold hover:bg-red-700 shadow-xs">繼續搜查 ❯</button>
            </div>
            <div class="text-xs font-medium mt-1 text-slate-700">正確解答為 (${String.fromCharCode(65 + quiz.answer)})。<br>${quiz.explanation}</div>
        `;
    }

    updateStageUI();

    if (window.renderMathInElement) {
        renderMathInElement(fb, {
            delimiters: [{left: '$', right: '$', display: false}],
            throwOnError: false
        });
    }

    if (currentLives <= 0) {
        setTimeout(() => finishStage(false), 1200);
    }
}

function nextStageQuestion() {
    currentQuizQuestionIndex++;
    renderCurrentStageQuestion();
}

function finishStage(completed) {
    const container = document.getElementById('stage-question-container');
    if (!container) return;

    const stage = window.CHALLENGE_STAGES[currentStageIndex];
    const isPassed = completed && (currentScore >= stage.pass_score);

    container.innerHTML = `
        <div class="text-center py-6">
            <div class="text-5xl mb-3">${isPassed ? '🕵️‍♂️' : '🌧️'}</div>
            <h3 class="text-xl font-black text-slate-900 mb-2">${isPassed ? '【CASE CLOSED 真相大白！】成功結案' : '【破案受阻】線索不足，搜查中斷！'}</h3>
            <p class="text-sm text-slate-600 mb-4">
                本次偵查得分：<span class="font-extrabold text-blue-900 text-lg">${currentScore}</span> 分 ‧ 
                最高連環破案：<span class="font-bold text-red-600">${maxCombo}</span> 連擊
            </p>
            <div class="flex justify-center gap-3">
                <button onclick="initStageQuiz()" class="px-4 py-2 bg-blue-900 text-white font-bold rounded-xl text-sm hover:bg-blue-800 shadow-md">
                    <i class="fa-solid fa-rotate-left mr-1"></i> 重新調查
                </button>
                <button onclick="closeChallengeModal()" class="px-4 py-2 bg-slate-100 text-slate-700 font-bold rounded-xl text-sm hover:bg-slate-200">
                    返回案卷庫
                </button>
            </div>
        </div>
    `;
}

// ==========================================
// 12. 教師解答與教案下載密碼驗證 (SOP v4.0 密碼: 88888888)
// ==========================================
let currentDownloadTarget = 'teacher';

function openTeacherPwdModal(target = 'teacher') {
    currentDownloadTarget = target;
    recordInteraction();
    const modal = document.getElementById('teacher-pwd-modal');
    if (modal) modal.classList.remove('hidden');

    const titleEl = document.getElementById('teacher-pwd-modal-title');
    const descEl = document.getElementById('teacher-pwd-modal-desc');
    if (target === 'lesson_plan') {
        if (titleEl) titleEl.innerText = "四節課教學計畫與教案驗證";
        if (descEl) descEl.innerText = "本教案包含四節課完整教學目標、時間分配與微軟原生 OMML 數學式，請輸入授權密碼：";
    } else {
        if (titleEl) titleEl.innerText = "警視廳機密解答卷宗驗證";
        if (descEl) descEl.innerText = "本卷宗包含教師專用紅字 OMML 步驟解答，請輸入專業授權密碼：";
    }

    const input = document.getElementById('teacher-pwd-input');
    if (input) {
        input.value = '';
        input.focus();
    }
    const err = document.getElementById('teacher-pwd-err');
    if (err) err.classList.add('hidden');
}

function closeTeacherPwdModal() {
    const modal = document.getElementById('teacher-pwd-modal');
    if (modal) modal.classList.add('hidden');
}

function verifyTeacherPwd() {
    const input = document.getElementById('teacher-pwd-input');
    const err = document.getElementById('teacher-pwd-err');
    if (input && input.value.trim() === '88888888') {
        if (err) err.classList.add('hidden');
        closeTeacherPwdModal();
        if (currentDownloadTarget === 'lesson_plan') {
            downloadLessonPlanDocx();
        } else {
            downloadTeacherDocx();
        }
    } else {
        if (err) {
            err.classList.remove('hidden');
            err.innerText = '授權密碼錯誤，請確認後重試！';
        }
    }
}

function downloadStudentDocx() {
    recordInteraction();
    const b64 = window.B64_STUDENT_DOCX || window.DOCX_STUDENT_B64;
    if (b64 && b64.length > 100) {
        downloadBase64File(b64, '2-3_對數及其運算的意義_學生學習單.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    } else {
        window.location.href = 'download/2-3_對數及其運算的意義_學生學習單.docx';
    }
}

function downloadTeacherDocx() {
    recordInteraction();
    const b64 = window.B64_TEACHER_DOCX || window.DOCX_TEACHER_B64;
    if (b64 && b64.length > 100) {
        downloadBase64File(b64, '2-3_對數及其運算的意義_教師解答版.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    } else {
        window.location.href = 'download/2-3_對數及其運算的意義_教師解答版.docx';
    }
}

function downloadLessonPlanDocx() {
    recordInteraction();
    const b64 = window.B64_LESSON_PLAN_DOCX || window.DOCX_LESSON_PLAN_B64;
    if (b64 && b64.length > 100) {
        downloadBase64File(b64, '2-3_對數及其運算的意義_四節課教學計畫與教案.docx', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document');
    } else {
        window.location.href = 'download/2-3_對數及其運算的意義_四節課教學計畫與教案.docx';
    }
}

function downloadBase64File(base64Data, filename, mimeType) {
    const byteCharacters = atob(base64Data);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

// ==========================================
// 13. QR Code 視窗操作
// ==========================================
function openQrModal() {
    recordInteraction();
    const modal = document.getElementById('qrcode-modal');
    if (modal) modal.classList.remove('hidden');
    renderDynamicQr();
}

function closeQrModal() {
    const modal = document.getElementById('qrcode-modal');
    if (modal) modal.classList.add('hidden');
}

function renderDynamicQr() {
    const qrContainer = document.getElementById('qrcode-display');
    const urlInput = document.getElementById('qr-url-input');
    if (!qrContainer) return;
    qrContainer.innerHTML = '';
    const targetUrl = urlInput ? urlInput.value : window.location.href;
    if (window.QRCode) {
        new QRCode(qrContainer, {
            text: targetUrl,
            width: 200,
            height: 200,
            colorDark: "#1e293b",
            colorLight: "#ffffff",
            correctLevel: QRCode.CorrectLevel.H
        });
    }
}

function copyQrUrl() {
    const urlInput = document.getElementById('qr-url-input');
    if (urlInput) {
        urlInput.select();
        navigator.clipboard.writeText(urlInput.value).then(() => {
            alert('連線網址已複製到剪貼簿！');
        });
    }
}

// ==========================================
// 13.5 網頁全螢幕滿版投影切換
// ==========================================
function togglePageFullscreen() {
    recordInteraction();
    if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
            console.warn("無法啟動全螢幕模式：", err);
        });
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen().catch(() => {});
        }
    }
}

// ==========================================
// 14. 鍵盤快速鍵支援
// ==========================================
function initKeyboardShortcuts() {
    document.addEventListener('keydown', (e) => {
        // 如果使用者正在輸入文字或密碼，不攔截按鍵
        if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA')) {
            return;
        }

        const modal = document.getElementById('fullscreen-modal');
        const mindmap = document.getElementById('mindmap-modal');
        const lab = document.getElementById('lab-modal');
        const challenge = document.getElementById('challenge-modal');
        const cheatsheet = document.getElementById('cheatsheet-modal');

        const isModalOpen = modal && !modal.classList.contains('hidden');
        const isMindmapOpen = mindmap && !mindmap.classList.contains('hidden');
        const isLabOpen = lab && !lab.classList.contains('hidden');
        const isChallengeOpen = challenge && !challenge.classList.contains('hidden');
        const isCheatSheetOpen = cheatsheet && !cheatsheet.classList.contains('hidden');

        if (e.key === 'Escape') {
            if (isModalOpen) closeModal();
            if (isMindmapOpen) closeMindmapModal();
            if (isLabOpen) closeLabModal();
            if (isChallengeOpen) closeChallengeModal();
            if (isCheatSheetOpen) closeCheatSheetModal();
        } else if (isModalOpen) {
            if (e.key.toLowerCase() === 'f') {
                e.preventDefault();
                toggleCardModalFullscreen();
            } else if (e.key.toLowerCase() === 'v') {
                e.preventDefault();
                setWhiteboardMode('mouse');
            } else if (e.key.toLowerCase() === 'b' || e.key.toLowerCase() === 'p') {
                e.preventDefault();
                setWhiteboardMode('pen');
            } else if (e.key.toLowerCase() === 'h') {
                e.preventDefault();
                setWhiteboardMode('highlighter');
            } else if (e.key.toLowerCase() === 'e') {
                e.preventDefault();
                setWhiteboardMode('eraser');
            } else if (e.key === 'ArrowLeft') {
                prevModalCard();
            } else if (e.key === 'ArrowRight') {
                nextModalCard();
            } else if (e.key >= '0' && e.key <= '4') {
                showStep(currentModalIndex, parseInt(e.key, 10));
            }
        } else if (isMindmapOpen) {
            if (e.key.toLowerCase() === 'f') {
                e.preventDefault();
                toggleMindmapFullscreen();
            }
        } else {
            // 沒有開啟任何模態框時，按下 F 鍵即可一鍵切換網頁全螢幕滿版！
            if (e.key.toLowerCase() === 'f') {
                e.preventDefault();
                togglePageFullscreen();
            }
        }
    });

    document.addEventListener('fullscreenchange', () => {
        const isFs = !!document.fullscreenElement;
        
        // 1. 劇院卡片全螢幕按鈕更新
        const modalFsBtn = document.getElementById('modal-fs-toggle-btn');
        if (modalFsBtn) {
            if (isFs) {
                modalFsBtn.innerHTML = '<i class="fa-solid fa-compress"></i><span class="hidden lg:inline">退出滿版 (F)</span>';
            } else {
                modalFsBtn.innerHTML = '<i class="fa-solid fa-maximize"></i><span class="hidden lg:inline">滿版投影 (F)</span>';
            }
        }
        
        // 2. 頂部導覽列全螢幕按鈕更新
        const pageFsBtn = document.getElementById('page-fullscreen-btn');
        const pageFsIcon = document.getElementById('page-fullscreen-icon');
        const pageFsText = document.getElementById('page-fullscreen-text');
        if (pageFsBtn) {
            if (isFs) {
                pageFsBtn.classList.add('bg-red-700', 'text-white', 'border-red-500');
                pageFsBtn.classList.remove('bg-slate-800', 'text-amber-300', 'border-amber-400/50');
                if (pageFsIcon) pageFsIcon.className = 'fa-solid fa-compress text-white';
                if (pageFsText) pageFsText.innerText = '退出滿版';
            } else {
                pageFsBtn.classList.remove('bg-red-700', 'text-white', 'border-red-500');
                pageFsBtn.classList.add('bg-slate-800', 'text-amber-300', 'border-amber-400/50');
                if (pageFsIcon) pageFsIcon.className = 'fa-solid fa-expand text-amber-400';
                if (pageFsText) pageFsText.innerText = '全螢幕滿版';
            }
        }

        // 3. 懸浮全螢幕按鈕更新
        const floatFsIcon = document.getElementById('floating-fullscreen-icon');
        if (floatFsIcon) {
            floatFsIcon.className = isFs ? 'fa-solid fa-compress text-base' : 'fa-solid fa-expand text-base';
        }

        resizeWhiteboard();
    });
}
"""

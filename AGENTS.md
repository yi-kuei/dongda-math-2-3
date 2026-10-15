# 東大技術高中數學 2-3 對數及其運算的意義 數位互動教材教學學習包（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介
依據《技術高中東大版數學數位互動教材教學學習包 製作流程標準說明書》（PLVS-MATH-DONGDA-SOP-FLAGSHIP v5.0 旗艦完備版）標準，製作東大版技術高中數學（第三冊）單元 2-3「對數及其運算的意義」全套數位互動教材學習包。
本專案全面導入「名偵探柯南數理探案」情境包裝，並遵循純化標準（全面取消傳統 PPT 簡報），專注於三大核心交付物：
1. **旗艦單檔互動探案平台**（`index.html`，具備 3D 翻牌、7大動態實驗室、5大線上對戰競技場、全螢幕劇院模式、電子搜查白板、Base64 內嵌離線下載、手機平板 QR 局域網連線）。
2. **微軟原生 OMML 專業 Word 卷宗**（JIS B4 橫向雙欄學生實作單、JIS B4 橫向雙欄教師紅字解答版、JIS B4 直式單欄四節課教案，100% 微軟原生 `<m:oMath>` 數學方程式）。
3. **A4 橫向全套圖解學習卡 PDF**（高解析向量列印版，一頁一案，左欄正面題幹與導引，右欄背面線索鏈與向量幾何圖解）。

## 關鍵時程
- 2026-10-15：專案初始化與升級完成（確立 SOP v5.0 旗艦規範、完成 L1 本地藍圖與 L2 GitHub 私有儲存庫建立）。

## 目標與路線圖
- [x] 階段一：專案基礎建設與 SOP 標準規範確立（SOP v4.0 確立）
- [x] 階段二：單元教材剖析與課程教學包規劃書（完成 65 案知識節點、神技口訣與 6 階段闖關規劃）
- [x] 階段三：建置卡片資料庫與互動模組（`cards_part1.py`、`cards_part2.py`、`interactive_cards_data.py`）
- [x] 階段四：產出 JIS B4 微軟原生 OMML 學習單與四節課教案（`.docx` 與 Base64 編碼 `docx_b64.py`）
- [x] 階段五：編譯 A4 橫向全套圖解學習卡向量列印版 PDF（`全套65張圖解學習卡.pdf`）
- [x] 階段六：編譯 `index.html` 旗艦單檔離線互動探案平台（含 3 大實驗室、電子白板與免聯網 Base64 下載）
- [x] 階段七：驗收測試與發布打包（產生 `download/`、`start_qr_server.py` 與 `網站上傳包.zip`）
- [x] 階段八：擴充 5 大對數線上對戰電玩競技場（`games_module.py`，骨牌連鎖、密室逃脫、迷宮尋路、射擊防禦、芮氏天平與 Web Audio API）
- [x] 階段九：擴充阿笠博士 7 大動態數理實驗室（`lab_experiments_module.py`，底數形變、地震能量、指對鏡射、計算尺、分貝儀、pH 色階、首尾顯微鏡，分頁滿版無卷軸）

## 資料夾結構
```
20261015東大數學2-3/
├── .gitignore                                          # Git 忽略清單
├── 2-3_對數及其運算的意義.pdf                            # 課本來源教材
├── 2-3_對數及其運算的意義_課程教學包規劃書.md              # 課程教學大綱與 65 案架構規劃
├── 2-3_對數及其運算的意義_四節課教學計畫與教案.md          # 四節課（200分鐘）教案 Markdown 原稿
├── 2-3_對數及其運算的意義_四節課教學計畫與教案.docx        # JIS B4 直式單欄微軟原生 OMML 教案文件
├── 2-3_對數及其運算的意義_學生學習單.docx                 # JIS B4 橫向雙欄學生手寫實作單
├── 2-3_對數及其運算的意義_教師解答版.docx                 # JIS B4 橫向雙欄教師紅字解答版
├── 2-3_對數及其運算的意義_全套65張圖解學習卡.pdf           # A4 橫向向量列印版全套 65 張學習卡
├── index.html                                          # 單檔 100% 離線旗艦數位互動探案平台（含 7 大實驗室與 5 大競技場）
├── cards_printable.html                                # 高畫質滿版列印 HTML
├── 2-3_對數及其運算的意義_網站上傳包.zip                  # 包含 index.html 與 download/ 的發布包
├── download/                                           # 離線下載專欄資源實體目錄
│   ├── 2-3_對數及其運算的意義_學生學習單.docx
│   ├── 2-3_對數及其運算的意義_教師解答版.docx
│   ├── 2-3_對數及其運算的意義_四節課教學計畫與教案.docx
│   └── 2-3_對數及其運算的意義_全套65張圖解學習卡.pdf
├── 核心建置 Python 程式庫：
│   ├── cards_part1.py                                  # CASE 01~42 圖解卡資料集
│   ├── cards_part2.py                                  # CASE 43~65 圖解卡資料集
│   ├── interactive_cards_data.py                       # 65 題正面自檢題庫與 6 階段闖關考核
│   ├── interactive_js_module.py                        # 前端核心邏輯庫（三大實驗室、電子白板、密碼驗證）
│   ├── games_module.py                                 # 5 大對戰遊戲模組（消消樂、密室、迷宮、射擊、天平與 Web Audio）
│   ├── lab_experiments_module.py                      # 阿笠博士 7 大動態數理實驗室（分頁式滿版無卷軸設計）
│   ├── docx_b64.py                                     # 內嵌 Base64 檔案資料庫（三份 Word 原生卷宗）
│   ├── generate_lesson_plan_docx.py                    # JIS B4 直式單欄教案 OMML 生成腳本
│   ├── generate_landscape_worksheets.py                # JIS B4 橫向雙欄學習單 OMML 生成器
│   ├── generate_cards_pdf.py                           # Edge Headless 高解析 PDF 編譯器
│   ├── generate_full_flipcard_page.py                  # index.html 單檔平台編譯器
│   ├── package_for_web.py                              # 發布打包與 download/ 歸檔腳本
│   └── start_qr_server.py                              # 手機平板掃碼連線伺服器
├── 啟動手機掃碼連線伺服器.bat                            # Windows 雙擊一鍵啟動連線腳本
├── AGENTS.md                                           # 專案藍圖（本檔）
├── handoff.md                                          # 跨 Agent/電腦交接記錄檔
└── 技術高中東大版數學製作流程 SOP.md                      # 技術高中東大版數學製作流程標準說明書 (v4.0)
```

## 同步層級（本專案初始化至第 2 層級）

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地（雲端硬碟資料夾） | `AGENTS.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | `yi-kuei/dongda-math-2-3`（公開，已部署 GitHub Pages：https://yi-kuei.github.io/dongda-math-2-3/） | 指定時 |
| L3 | Obsidian | <未啟用｜這台電腦無 Obsidian MCP 工具> | 有需要時 |

## 工作約定
- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構
- 嚴格遵守《技術高中東大版數學製作流程 SOP》十九大核心製作鐵律

## 安全與隱私（不可違反）
- **不把 API key、密碼、憑證寫進 repo**，也不要貼進 `AGENTS.md`／`handoff.md`；一律放 `.env` 並列入 `.gitignore`
- **學生資料只用座號**，不出現姓名、學號、班級以外的個資、照片或聯絡方式
- 要公開分享前，先確認檔案裡沒有上述兩類內容

# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
1. 確定維持全套 65 案旗艦規格（一題一卡、一小題獨立成卡、例題隨堂習題全開）。
2. 完成四節課（每節 50 分鐘，共 200 分鐘）完整課程計畫與教學教案撰寫（`.md`）。
3. 建立 `generate_lesson_plan_docx.py` 並成功產出 JIS B4 直式單欄微軟原生 OMML 教案文件：`2-3_對數及其運算的意義_四節課教學計畫與教案.docx`（含 72 處原生 `<m:oMath>` 方程式），同步歸檔至 `download/`。
4. 確立首頁教案與解答卷宗下載授權密碼統一為 `88888888`。

## 🚦 目前狀態
教案與課程計畫已完備（Markdown 與 JIS B4 OMML docx 雙版本就緒）。隨時可啟動圖解卡資料庫（`cards_part1.py`、`cards_part2.py`）與雙欄學生/教師學習單建置。

## ➡️ 下一步
1. 建置卡片資料庫 `cards_part1.py`（CASE 01~42）與 `cards_part2.py`（CASE 43~65）。
2. 建置 `interactive_cards_data.py`（正面 65 道自檢題庫與 6 階段闖關考核）。
3. 撰寫 `generate_landscape_worksheets.py`，產出 JIS B4 橫向雙欄學生實作單與教師紅字解答版 `.docx`。
4. 將 Word 檔案編碼至 `docx_b64.py`，設定下載授權驗證密碼 `88888888`。

## ⚠️ 注意事項
- 嚴格遵守 SOP 十五大製作鐵律：課本題目 100% 忠實原文、嚴禁純文字打字數學式、卡片容器無橫向捲軸、行距 line-height 2.35。
- 密碼驗證統一為 `88888888`，首頁及任何介面絕不顯示明文密碼。
- 全面純化取消 PPT，專注於極致三大輸出物：單檔 `index.html`、微軟原生 OMML Word 卷宗、A4 橫向圖解卡 PDF。

## 🕐 最後更新
- 時間：2026-10-15 08:40
- 更新者：Antigravity @ DESKTOP-HS4CHCD
- Git push：✅ 已推

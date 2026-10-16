# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
1. **全套東大版技術高中數學 2-3「對數及其運算的意義」數位互動教材教學學習包已全面完工**（SOP v5.0 旗艦完備版）：
   - 旗艦單檔 `index.html`（602 KB，離線可用、3D 翻牌、7 大動態實驗室、5 大電玩競技場、電子搜查白板、大字體滿版與全域 `F` 鍵全螢幕投影、免聯網 Base64 下載）。
   - 微軟原生 OMML JIS B4 Word 卷宗（學生實作單、教師紅字解答版、四節課直式教案，100% `<m:oMath>` 數學式）。
   - A4 橫向全套 65 張向量圖解學習卡 PDF（`全套65張圖解學習卡.pdf`，2.06 MB）。
2. **GitHub Pages 線上部署已完成**：`https://yi-kuei.github.io/dongda-math-2-3/`。
3. **網易資訊虛擬主機（`http://ecourse.idv.tw/dongda3/math-2-3/`）部署全面完工**：
   - 經執行 `python deploy_to_ecourse.py`，成功連線至 `ecourse.idv.tw:21`（Pure-FTPd）。
   - 自動於 `public_html` 建立目標目錄結構 `dongda3/math-2-3/` 與 `download/`。
   - 成功上傳：`index.html` (575.8 KB)、`cards_printable.html` (356.9 KB)、A4 橫向學習卡 PDF (2,110.6 KB) 與三份 JIS B4 Word 卷宗。
   - 實測線上 HTTP 狀態碼驗收：首頁及 `download/` 所有教材檔案均回傳 **200 OK** 正常存取！

## 🚦 目前狀態
✅ **雙線上站台部署 100% 正常運作**：
   - 站台 1（網易資訊）：`http://ecourse.idv.tw/dongda3/math-2-3/`
   - 站台 2（GitHub Pages）：`https://yi-kuei.github.io/dongda-math-2-3/`
✅ 本地單檔離線探案平台、JIS B4 Word 卷宗、A4 橫向全套學習卡 PDF 均 100% 完工備妥。

## ➡️ 下一步
1. 實際於瀏覽器或教學現場投影機開啟 `http://ecourse.idv.tw/dongda3/math-2-3/` 進行課堂教學巡檢。
2. 如需在校園區域網路供學生平板/手機掃碼直連，可執行本機 `啟動手機掃碼連線伺服器.bat`（`python start_qr_server.py`）。

## ⚠️ 注意事項
- 教師解答版與教案下載密碼為 `88888888`。
- `.env` 存放網易主機 FTP 帳密（`FTP_USER=ecfsmcwl`），已列入 `.gitignore`，嚴禁加入 Git 版本控制。
- 伺服器有嚴格的爬蟲防護（ModSecurity），HTTP 測試須帶完整瀏覽器 `User-Agent`。

## 🕐 最後更新
- 時間：2026-10-16 17:10
- 更新者：Antigravity @ DESKTOP-KUEI
- Git push：✅ 已推（main 最新）

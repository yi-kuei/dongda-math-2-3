# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
1. **全套東大版技術高中數學 2-3「對數及其運算的意義」數位互動教材教學學習包已全面完工**（SOP v5.0 旗艦完備版）：
   - 旗艦單檔 `index.html`（602 KB，離線可用、3D 翻牌、7 大動態實驗室、5 大電玩競技場、電子搜查白板、大字體滿版與全域 `F` 鍵全螢幕投影、免聯網 Base64 下載）。
   - 微軟原生 OMML JIS B4 Word 卷宗（學生實作單、教師紅字解答版、四節課直式教案，100% `<m:oMath>` 數學式）。
   - A4 橫向全套 65 張向量圖解學習卡 PDF（`全套65張圖解學習卡.pdf`，2.06 MB）。
2. **GitHub Pages 線上部署已完成**：`https://yi-kuei.github.io/dongda-math-2-3/`。
3. **新增網易資訊（`http://ecourse.idv.tw/dongda3/math-2-3/`）自動部署腳本**：
   - 已完成主機檢測（IP `103.138.106.72`，FTP Port 21 與 cPanel Port 2083 皆開啟）。
   - 已建立自動部署腳本 `deploy_to_ecourse.py` 與本地 `.env` 設定檔（已列入 `.gitignore`）。
   - 因首次填入之 `@gmail.com` 為網易客戶專區（帳務後台）會員帳號，而非 cPanel/FTP 虛擬主機專用帳號，目前已依指示暫停執行，待補入 cPanel/FTP 主機帳號密碼後即可一鍵執行 `python deploy_to_ecourse.py` 完成上傳。

## 🚦 目前狀態
✅ GitHub Pages 線上版與本地全套教材學習包 100% 正常運作。
⏸️ 網易資訊主機（`http://ecourse.idv.tw/dongda3/math-2-3/`）FTP 部署暫停中，等待更新 `.env` 內的 cPanel/FTP 專用帳號密碼。

## ➡️ 下一步
1. 查詢網易資訊 cPanel 虛擬主機帳號與密碼（或於 cPanel 新增 FTP 帳戶），填入本地 `.env` 後執行 `python deploy_to_ecourse.py` 自動上傳至 `http://ecourse.idv.tw/dongda3/math-2-3/`。
2. 課堂可直接透過 GitHub Pages 網址（`https://yi-kuei.github.io/dongda-math-2-3/`）或單檔 `index.html` 進行授課與破冰對戰。

## ⚠️ 注意事項
- 教師解答版與教案下載密碼為 `88888888`。
- `.env` 存放網易主機 FTP 帳密，已列入 `.gitignore`，嚴禁加入 Git 版本控制；換電腦時需手動複製或建立 `.env`。
- 網易資訊（WantEasy）的 `@gmail.com` 是客戶專區帳務帳號，FTP（Port 21）與 cPanel（Port 2083）需使用虛擬主機專用帳號（通常為 6~8 碼英數字或 `帳號@ecourse.idv.tw`）。

## 🕐 最後更新
- 時間：2026-10-16 10:04
- 更新者：Antigravity @ DESKTOP-HS4CHCD
- Git push：✅ 已推（main 最新）

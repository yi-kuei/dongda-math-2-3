# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（若有 L3）。

## ⏯️ 目前做到哪
1. **全套東大版技術高中數學 2-3「對數及其運算的意義」數位互動教材教學學習包已全面完工**（SOP v5.0 旗艦完備版）：
   - 旗艦單檔 `index.html`（602 KB，離線可用、3D 翻牌、7 大動態實驗室、5 大電玩競技場、電子搜查白板、大字體滿版與全域 `F` 鍵全螢幕投影、免聯網 Base64 下載）。
   - 微軟原生 OMML JIS B4 Word 卷宗（學生實作單、教師紅字解答版、四節課直式教案，100% `<m:oMath>` 數學式）。
   - A4 橫向全套 65 張向量圖解學習卡 PDF（`全套65張圖解學習卡.pdf`，2.06 MB）。
2. **GitHub Pages 線上部署已完成**：`https://yi-kuei.github.io/dongda-math-2-3/`。
3. **網易資訊（`http://ecourse.idv.tw/dongda3/math-2-3/`）部署進度**：
   - 已確認虛擬主機 cPanel/FTP 帳號為 `ecfsmcwl`（已填入本地 `.env`），並已登入「網易資訊客戶專區（`https://my.wanteasy.com.tw/`）」進入 `Ecourse.idv.tw`（方案 `TWW-E02`）服務明細頁。
   - 因原 8 碼密碼驗證未過（`530 Login authentication failed`）且累計嘗試觸發主機防火牆暫時封鎖目前 IP，已先行暫停連線。

## 🚦 目前狀態
✅ GitHub Pages 線上版與本地全套教材學習包 100% 正常運作。
⏸️ 網易資訊主機（`http://ecourse.idv.tw/dongda3/math-2-3/`）等待於網易客戶專區重設密碼及 IP 解封後完成上傳。

## ➡️ 下一步
1. 於網易資訊客戶專區（`Ecourse.idv.tw` 服務明細頁）左側「🔧 操作」點選 **「變更密碼」** 重設 cPanel/FTP 密碼，並更新至本地 `.env` 的 `FTP_PASS=`。
2. 待主機防火牆 IP 自動解封（或改連手機熱點 / 填寫問題單請客服解封 IP）後：
   - **方法 A**：直接點選客戶專區左側 **「登入cPanel控制台」** → 檔案管理員 → `public_html/dongda3/math-2-3` → 上傳並解壓縮 `2-3_對數及其運算的意義_網站上傳包.zip`。
   - **方法 B**：在終端機執行 `python deploy_to_ecourse.py` 自動上傳並驗證。

## ⚠️ 注意事項
- 教師解答版與教案下載密碼為 `88888888`。
- `.env` 存放網易主機 FTP 帳密（`FTP_USER=ecfsmcwl`），已列入 `.gitignore`，嚴禁加入 Git 版本控制；換電腦時需手動複製或建立 `.env`。
- 切勿在未確認新密碼前連續重試 FTP 登入，以免再次觸發 `ecourse.idv.tw` 主機 cPHulk/CSF 防火牆封鎖 IP。

## 🕐 最後更新
- 時間：2026-10-16 14:14
- 更新者：Antigravity @ DESKTOP-HS4CHCD
- Git push：✅ 已推（main 最新）

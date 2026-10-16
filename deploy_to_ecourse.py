# -*- coding: utf-8 -*-
"""
網易資訊 (ecourse.idv.tw) 自動部署腳本
讀取本地 .env 中的 FTP 憑證，自動定位網站根目錄 (public_html)，
建立目標子目錄 (預設 dongda3/math-2-3)，並上傳 index.html 與 download/ 完整教學包。
"""

import os
import sys
import ftplib
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, ".env")


def load_env(path):
    config = {}
    if not os.path.exists(path):
        return config
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            config[k.strip()] = v.strip().strip('"').strip("'")
    return config


def ensure_ftp_dir(ftp, path_parts):
    for part in path_parts:
        if not part:
            continue
        try:
            ftp.cwd(part)
        except ftplib.error_perm:
            print(f"📁 建立遠端目錄: {part}")
            ftp.mkd(part)
            ftp.cwd(part)


def upload_file(ftp, local_path, remote_name):
    size_kb = os.path.getsize(local_path) / 1024.0
    print(f"⬆️ 正在上傳: {remote_name} ({size_kb:.1f} KB) ...")
    with open(local_path, "rb") as f:
        ftp.storbinary(f"STOR {remote_name}", f, blocksize=32768)
    print(f"   ✅ 完成: {remote_name}")


def main():
    cfg = load_env(ENV_PATH)
    host = cfg.get("FTP_HOST", "ecourse.idv.tw")
    port = int(cfg.get("FTP_PORT", "21"))
    user = cfg.get("FTP_USER", "")
    passwd = cfg.get("FTP_PASS", "")
    target_dir = cfg.get("FTP_TARGET_DIR", "dongda3/math-2-3").strip("/")

    if not user or not passwd or "請在此填入" in user or "請在此填入" in passwd:
        print("❌ 請先在 .env 檔案中填入正確的 FTP_USER 與 FTP_PASS！")
        sys.exit(1)

    print(f"🔌 正在連線至 {host}:{port} ...")
    ftp = ftplib.FTP()
    ftp.encoding = "utf-8"
    ftp.connect(host, port, timeout=30)
    ftp.login(user, passwd)
    ftp.set_pasv(True)
    print(f"✅ 登入成功！伺服器歡迎訊息: {ftp.getwelcome()}")

    # 自動偵測是否在 cPanel 家目錄（含有 public_html）或已在網站根目錄
    items = ftp.nlst()
    clean_items = [os.path.basename(x.rstrip("/")) for x in items]
    if "public_html" in clean_items:
        print("📂 偵測到 cPanel 標準目錄結構，進入 public_html ...")
        ftp.cwd("public_html")
    elif "www" in clean_items and "plvsxoops2511" not in clean_items:
        print("📂 偵測到 www 目錄，進入 www ...")
        ftp.cwd("www")
    else:
        print("📂 目前已位於網站根目錄")

    # 確保目標目錄存在 (例如 dongda3/math-2-3)
    parts = [p for p in target_dir.split("/") if p]
    ensure_ftp_dir(ftp, parts)
    remote_target_pwd = ftp.pwd()
    print(f"🎯 目標遠端路徑已就緒: {remote_target_pwd}")

    # 上傳主檔案
    for fname in ["index.html", "cards_printable.html"]:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            upload_file(ftp, fpath, fname)

    # 上傳 download/ 資料夾內所有教材檔案
    dl_local_dir = os.path.join(BASE_DIR, "download")
    if os.path.isdir(dl_local_dir):
        ensure_ftp_dir(ftp, ["download"])
        for fname in os.listdir(dl_local_dir):
            fpath = os.path.join(dl_local_dir, fname)
            if os.path.isfile(fpath):
                upload_file(ftp, fpath, fname)

    ftp.quit()
    url = f"http://{host}/{target_dir}/"
    print(f"\n🎉 全部檔案上傳完畢！正在驗證線上網址: {url}")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"🌐 HTTP 狀態碼: {resp.status} OK — 網站已正式上線！")
    except Exception as e:
        print(f"⚠️ 網頁連線測試提示: {e}")


if __name__ == "__main__":
    main()

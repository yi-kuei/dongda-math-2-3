@echo off
chcp 65001 >nul
title 東大數學 2-3 柯南數理探案伺服器
echo 正在啟動手機掃碼連線伺服器...
python start_qr_server.py
pause

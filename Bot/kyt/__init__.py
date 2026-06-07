from telethon import *
import datetime as DT
import requests, time, os, subprocess, re, sqlite3, sys, random, base64, json, math
import logging
logging.basicConfig(level=logging.INFO)
uptime = DT.datetime.now()

# Membaca data variabel dari file eksternal
exec(open("/usr/bin/kyt/var.txt", "r").read())

# Inisialisasi bot dengan token
bot = TelegramClient("ddsdswl", "6", "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token=BOT_TOKEN)

# Pengecekan atau pembuatan database jika belum ada
try:
    open("/usr/bin/kyt/database.db")
except:
    # Membuat koneksi dan tabel admin jika belum ada
    x = sqlite3.connect("/usr/bin/kyt/database.db")
    c = x.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS admin (user_id TEXT UNIQUE)")
    # Menambahkan admin pertama (bisa berupa satu admin atau lebih)
    admin_ids = ADMIN.split(",")  # Memungkinkan admin multi ID, dipisah dengan koma
    for admin_id in admin_ids:
        c.execute("INSERT OR IGNORE INTO admin (user_id) VALUES (?)", (admin_id,))
    x.commit()

# Fungsi untuk mendapatkan koneksi database
def get_db():
    x = sqlite3.connect("/usr/bin/kyt/database.db")
    x.row_factory = sqlite3.Row
    return x

# Fungsi untuk validasi ID admin
def valid(id):
    db = get_db()
    x = db.execute("SELECT user_id FROM admin").fetchall()
    a = [v['user_id'] for v in x]
    if str(id) in a:
        return "true"
    else:
        return "false"

# Fungsi untuk konversi ukuran file
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

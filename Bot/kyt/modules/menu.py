from kyt import *
import subprocess
from datetime import datetime, timedelta

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
    inline = [
        [Button.inline(" SSH OVPN MANAGER ","ssh")],
        [Button.inline(" VMESS MANAGER ","vmess"),
         Button.inline(" VLESS MANAGER ","vless")],
        [Button.inline(" TROJAN MANAGER ","trojan"),
         Button.inline(" SHDWSK MANAGER ","shadowsocks")],
        [Button.inline(" CHECK VPS INFO ","info"),
         Button.inline(" OTHER SETTING ","setting")],
        [Button.inline(" ‹ Back Menu › ","start")]
    ]
    
    sender = await event.get_sender()
    val = valid(str(sender.id))
    
    if val == "false":
        try:
            await event.answer(" ", alert=True)
        except:
            await event.reply(" ")
    elif val == "true":
        try:
            # Menjalankan perintah untuk mendapatkan informasi sistem
            sh = 'cat /etc/passwd | grep "home" | grep "false" | wc -l'
            ssh = subprocess.check_output(sh, shell=True).decode("ascii")
            vm = 'cat /etc/vmess/.vmess.db | grep "###" | wc -l'
            vms = subprocess.check_output(vm, shell=True).decode("ascii")
            vl = 'cat /etc/vless/.vless.db | grep "###" | wc -l'
            vls = subprocess.check_output(vl, shell=True).decode("ascii")
            tr = 'cat /etc/trojan/.trojan.db | grep "###" | wc -l'
            trj = subprocess.check_output(tr, shell=True).decode("ascii")
            ssr = 'cat /etc/shadowsocks/.shadowsocks.db | grep "###" | wc -l'
            ssrme = subprocess.check_output(ssr, shell=True).decode("ascii")
            sdss = "cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
            namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
            ipvps = "curl -s ipv4.icanhazip.com"
            ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
            citsy = "curl -s ipinfo.io/city"
            city = subprocess.check_output(citsy, shell=True).decode("ascii")
            # Mengambil username menggunakan IP publik
            myip = subprocess.check_output("cat /usr/bin/ipsave", shell=True).decode("ascii").strip()
            usrvps_cmd = f"cat /usr/bin/user"
            usrvpsme = subprocess.check_output(usrvps_cmd, shell=True).decode("ascii").strip()
            usrisp = 'curl -s ipinfo.io/org | cut -d " " -f 2-10'
            usrispme = subprocess.check_output(usrisp, shell=True).decode("ascii")
            
            # Mendapatkan masa aktif
            usrexp_cmd = f"cat /usr/bin/e"
            usrexp = subprocess.check_output(usrexp_cmd, shell=True).decode("ascii").strip()
            today = datetime.today().strftime('%Y-%m-%d')

            # Periksa apakah nilai di usrexp adalah tanggal atau jumlah hari
            try:
                # Jika berhasil diparsing sebagai tanggal
                d1 = datetime.strptime(usrexp, "%Y-%m-%d")
                d2 = datetime.strptime(today, "%Y-%m-%d")
                remaining_days = (d1 - d2).days
            except ValueError:
                # Jika tidak bisa diparsing sebagai tanggal, periksa apakah mengandung 'Day'
                if 'Day' in usrexp:
                    remaining_days = int(usrexp.split()[0])
                else:
                    remaining_days = 0
            
            if remaining_days <= 0:
                masaaktif = "EXPIRED"
            else:
                masaaktif = f"{remaining_days} Day"

            # Menghitung RAM
            ram_info = subprocess.check_output("free -m | awk 'NR==2 {print $2, $3, $4}'", shell=True).decode("ascii").strip().split()
            total_mem_mb, used_mem_mb, free_mem_mb = map(int, ram_info)
            total_mem_gb = total_mem_mb / 1024
            used_mem_gb = used_mem_mb / 1024
            free_mem_gb = free_mem_mb / 1024
            
            msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
.::. BOT ARISCTUNNEL V4 .::.
━━━━━━━━━━━━━━━━━━━━━━━ 
» SYSTEM    : {namaos.strip().replace('"','')}
» TOTAL RAM : {total_mem_gb:.2f} GB
» USED RAM  : {used_mem_gb:.2f} GB
» FREE RAM  : {free_mem_gb:.2f} GB
» CITY      : {city.strip()}
» IP VPS    : {ipsaya.strip()}
» ISP       : {usrispme.strip()}
» DOMAIN    : {DOMAIN}

» Total Account Created: 
» SSH OVPN    : {ssh.strip()} account
» XRAY VMESS  : {vms.strip()} account
» XRAY VLESS  : {vls.strip()} account
» XRAY TROJAN : {trj.strip()} account
» SSR-LIBEV   : {ssrme.strip()} account

» VERSION   : 4.0 LTS
» CLIENTS   : {usrvpsme}
» Expiry In : {masaaktif}
━━━━━━━━━━━━━━━━━━━━━━━``` 
"""
            x = await event.edit(msg, buttons=inline)
            if not x:
                await event.reply(msg, buttons=inline)

        except subprocess.CalledProcessError as e:
            await event.reply(f"Error executing command: {e}")
        except Exception as e:
            await event.reply(f"Unexpected error: {e}")

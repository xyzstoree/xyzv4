from kyt import *

@bot.on(events.CallbackQuery(data=b'regip'))
async def reg_ip(event):
	async def reg_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**IP VPS:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as dom:
			await event.respond('**NAMA CLIENT:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		async with bot.conversation(chat) as sub:
			await event.respond('**EXPAIRED:**')
			sub = sub.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			sub = (await sub).raw_text
		cmd = f'printf "%s\n" "1" "{user}" "{dom}" "{sub}"  | /usr/bin/Bot/bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Register IP**")
		else:
			msg = f"""**Successfully Register Ip {user}**
			```{a}```
			"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await reg_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'renip'))
async def renip(event):
	async def renip_(event):
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		async with bot.conversation(chat) as ipvps:
			await event.respond('**ADD RENEW EXPAIRED:**')
			ipvps = ipvps.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			ipvps = (await ipvps).raw_text
		cmd = f'printf "%s\n" "2" "{dom}" "{ipvps}"  | /usr/bin/Bot/bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Renew IP**")
		else:
			msg = f"""**Successfully Renew Ip {dom}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delip'))
async def delip(event):
	async def delip_(event):
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		cmd = f'printf "%s\n" "3" "{dom}" | /usr/bin/Bot/bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Delete IP**")
		else:
			msg = f"""**Successfully Delete Ip {dom}**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'install_link'))
async def install_link(event):
    await event.respond(
        "Link untuk instalasi: ```apt update > /dev/null 2>&1 && sysctl -w net.ipv6.conf.all.disable_ipv6=1 > /dev/null 2>&1 && echo -e 'waiting...' && sysctl -w net.ipv6.conf.default.disable_ipv6=1 > /dev/null 2>&1 && apt install screen curl wget python3-pip -y > /dev/null 2>&1 && pip install gdown > /dev/null 2>&1 && screen -dmS ari bash -c 'gdown \"1e2823tFfBjKOL98D0o8Ca5FfouBkYGvC\" -O install && chmod +x install && ./install; if [[ 0 -gt 0 ]]; then rm install; fi' && screen -r ari```"
    )


# Define the URL to check if IP is registered
data_ip = "https://raw.githubusercontent.com/xyzstoree/izin/main/ip-admin"

# Helper function to check if IP is registered
def is_ip_registered(ip):
    try:
        registered_ips = requests.get(data_ip).text
        return ip in registered_ips
    except Exception as e:
        print(f"Error checking IP registration: {e}")
        return False

@bot.on(events.CallbackQuery(data=b'reg'))
async def reg(event):
    async def reg_(event):
        inline = [
            [Button.inline(" ADD IP ", "regip"),
             Button.inline(" DELETE IP ", "delip")],
            [Button.inline(" RENEW IP ", "renip"),
             Button.inline(" LINK INSTALL ", "install_link")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]

        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
🐾🕊️ PREMIUM PANEL MENU 🕊️🐾
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 » Hostname/IP: {DOMAIN}
🔰 » ISP: {z["isp"]}
🔰 » Country: {z["country"]}
🤖 »@ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━``` 
"""

        # Get the user's IP
        user_ip = requests.get('https://ipv4.icanhazip.com').text.strip()

        # Check if IP is registered
        if is_ip_registered(user_ip):
            await event.edit(msg, buttons=inline)
        else:
            await event.answer("Akses Ditolak: IP tidak terdaftar", alert=True)

    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await reg_(event)
    else:
        await event.answer("Access Denied", alert=True)

@bot.on(events.CallbackQuery(data=b'reboot'))
async def rebooot(event):
	async def rebooot_(event):
		cmd = f'reboot'
		time.sleep(1)
		await event.edit("`Processing Restart Service Server...`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		subprocess.check_output(cmd, shell=True)
		await event.edit(f"""
**» REBOOT SERVER**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await rebooot_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'resx'))
async def resx(event):
	async def resx_(event):
		cmd = f'systemctl restart xray | systemctl restart nginx | systemctl restart haproxy | systemctl restart server | systemctl restart udp-custom | systemctl restart client'
		subprocess.check_output(cmd, shell=True)

		time.sleep(1)
		await event.edit("`Processing Restart Service Server...`")
		time.sleep(1)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(1)
		await event.edit(f"""
```Processing... 100%\n█████████████████████████ ```
**» Restarting Service Done**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await resx_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'speedtest'))
async def speedtest(event):
	async def speedtest_(event):
		cmd = 'speedtest-cli --share'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		time.sleep(0)
		await event.edit("`Processing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `")
		time.sleep(1)
		await event.edit("`Processing... 84%\n█████████████████████▒▒▒▒ `")
		time.sleep(0)
		await event.edit("`Processing... 100%\n█████████████████████████ `")
		await event.respond(f"""
**
{z}
**
**» 🤖@ARI_VPN_STORE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await speedtest_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'backup'))
async def backup(event):
    async def backup_(event):
        cmd = '/usr/bin/Bot/bot-backupfile'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Not Exist**")
        else:
            msg = f"""
```{a}```
**» 🤖@ARI_VPN_STORE**
"""
            await event.respond(msg)
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await backup_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'restore'))
async def restore(event):
    async def restore_(event):
        async with bot.conversation(chat) as user:
            await event.respond('**Link File   :**')
            file_id_event = await user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            file_id = file_id_event.raw_text
            
        cmd = f'printf "%s\n" "{file_id}" | /usr/bin/Bot/bot-restorefile'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("**Link Not Exist**")
        else:
            msg = f"""```{a}```
**🤖@ARI_VPN_STORE**
"""
            await event.respond(msg)
    
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await restore_(event)
    else:
        await event.answer("Akses Ditolak", alert=True)

@bot.on(events.CallbackQuery(data=b'addpoint'))
async def reg_ip(event):
	async def reg_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**HOST:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as dom:
			await event.respond('**IP VPS:**')
			dom = dom.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			dom = (await dom).raw_text
		cmd = f'printf "%s\n" "5" "3" "{user}" "{dom}"  | /usr/bin/Bot/bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Pointing**")
		else:
			msg = f"""
			**Successfully Pointing**
			**IP VPS:** `{dom}`
			**HOST:** `{user}.newsctunnel.me`
			"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await reg_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delpoint'))
async def reg_ip(event):
	async def reg_ip_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**HOST:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "6" "3" "{user}"  | /usr/bin/Bot/bot-add-ip'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond(f"**Successfully Delete Pointing**")
		else:
			msg = f"""
			**Successfully Delete Pointing**
			**HOST:** `{user}.newsctunnel.me`
			"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await reg_ip_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# Define the URL to check if IP is registered
data_ip = "https://raw.githubusercontent.com/xyzstoree/izin/main/ip-admin"

# Helper function to check if IP is registered
def is_ip_registered(ip):
    try:
        registered_ips = requests.get(data_ip).text
        return ip in registered_ips
    except Exception as e:
        print(f"Error checking IP registration: {e}")
        return False

@bot.on(events.CallbackQuery(data=b'point'))
async def point(event):
    async def point_(event):
        inline = [
            [Button.inline(" ADD DOMAIN ", "addpoint"),
             Button.inline(" DELETE DOMAIN ", "delpoint")],
            [Button.inline("‹ Main Menu ›", "menu")]
        ]

        z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
        msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
🐾🕊️ PREMIUM PANEL MENU 🕊️🐾
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 » Hostname/IP: {DOMAIN}
🔰 » ISP: {z["isp"]}
🔰 » Country: {z["country"]}
🤖 »@ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━``` 
"""

        # Get the user's IP
        user_ip = requests.get('https://ipv4.icanhazip.com').text.strip()

        # Check if IP is registered
        if is_ip_registered(user_ip):
            await event.edit(msg, buttons=inline)
        else:
            await event.answer("Akses Ditolak: IP tidak terdaftar", alert=True)

    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await point_(event)
    else:
        await event.answer("Access Denied", alert=True)

@bot.on(events.CallbackQuery(data=b'backer'))
async def backers(event):
	async def backers_(event):
		inline = [
[Button.inline(" BACKUP","backup"),
Button.inline(" RESTORE","restore")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
🐾🕊️ PREMIUM PANEL MENU 🕊️🐾
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 » Hostname/IP: {DOMAIN}
🔰 » ISP: {z["isp"]}
🔰 » Country: {z["country"]}
🤖 »@ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━```  
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await backers_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'setting'))
async def settings(event):
	async def settings_(event):
		inline = [
[Button.inline(" SPEEDTEST","speedtest"),
Button.inline(" BACKUP & RESTORE","backer")],
[Button.inline(" REBOOT SERVER","reboot"),
Button.inline(" RESTART SERVICE","resx")],
[Button.inline(" MENU ADD IP","reg"),
Button.inline(" MENU DOMAIN","point")],
[Button.inline("‹ Main Menu ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
🐾🕊️ PREMIUM PANEL MENU 🕊️🐾
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 » Hostname/IP: {DOMAIN}
🔰 » ISP: {z["isp"]}
🔰 » Country: {z["country"]}
🤖 »@ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━``` 
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await settings_(event)
	else:
		await event.answer("Access Denied",alert=True)

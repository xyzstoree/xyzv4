from kyt import *

# CREATE SHADOWSOCKS
@bot.on(events.CallbackQuery(data=b'create-shadowsocks'))
async def create_shadowsocks(event):
    async def create_shadowsocks_(event):
        async with bot.conversation(chat) as user:
            await event.respond('Username:')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        async with bot.conversation(chat) as pw:
            await event.respond("Limit IP:")
            pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw).raw_text
        async with bot.conversation(chat) as exp:
            await event.respond("Choose Expiry Day", buttons=[
                [Button.inline(" 3 Day ", "3"),
                 Button.inline(" 7 Day ", "7")],
                [Button.inline(" 30 Day ", "30"),
                 Button.inline(" 60 Day ", "60")]])
            exp = exp.wait_event(events.CallbackQuery)
            exp = (await exp).data.decode("ascii")
        await event.edit("Processing.")
        await event.edit("Processing..")
        await event.edit("Processing...")
        await event.edit("Processing....")
        time.sleep(3)
        await event.edit("Processing Create Premium Account")
        time.sleep(1)
        
        cmd = f'printf "%s\n" "{user}" "100" "{pw}" "{exp}" | /usr/bin/Bot/bot-add-ssr'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("User Already Exists")
        else:
            today = DT.date.today()
            later = today + DT.timedelta(days=int(exp))
            msg = f"""
━━━━━━━━━━━━━━━━
Shadowsocks Account
━━━━━━━━━━━━━━━━
» Username     : {user}
» Password     : {pw}
» Expiry       : {later}
» Port         : 8388
» Cipher       : aes-256-gcm
━━━━━━━━━━━━━━━━
» Server Info : {DOMAIN}
» Expired Until: {later}
» 🤖@ARI_VPN_STORE
"""
            await event.respond(msg)
    
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await create_shadowsocks_(event)
    else:
        await event.answer("Access Denied", alert=True)

# DELETE SHADOWSOCKS
@bot.on(events.CallbackQuery(data=b'delete-shadowsocks'))
async def delete_shadowsocks(event):
    async def delete_shadowsocks_(event):
        async with bot.conversation(chat) as user:
            await event.respond('Username To Be Deleted:')
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        cmd = f'printf "%s\n" "{user}" | delshadowsocks'
        try:
            a = subprocess.check_output(cmd, shell=True).decode("utf-8")
        except:
            await event.respond("User Not Found")
        else:
            await event.respond(f"Successfully Deleted {user}")
    
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await delete_shadowsocks_(event)
    else:
        await event.answer("Access Denied", alert=True)

# SHADOWSOCKS MAIN MENU
@bot.on(events.CallbackQuery(data=b'shadowsocks'))
async def shadowsocks(event):
    async def shadowsocks_(event):
        inline = [
            [Button.inline(" TRIAL SHADOWSOCKS ", "trial-shadowsocks"),
             Button.inline(" CREATE SHADOWSOCKS ", "create-shadowsocks")],
            [Button.inline(" DELETE SHADOWSOCKS ", "delete-shadowsocks"),
             Button.inline(" CHECK SHADOWSOCKS ", "cek-shadowsocks")],
            [Button.inline(" UNLOCK SHADOWSOCKS ", "unlock-shadowsocks"),
             Button.inline(" LOCK SHADOWSOCKS ", "lock-shadowsocks")],
             [Button.inline("‹ Main Menu ›", "menu")]
        ]
        try:
            z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
            msg = f"""
```━━━━━━━━━━━━━━━━━━━━━━━ 
🐾🕊️ SHDWSK MANAGER 🕊️🐾
━━━━━━━━━━━━━━━━━━━━━━━ 
🔰 » Service: SHADOWSOCKS
🔰 » Hostname/IP: {DOMAIN}
🔰 » ISP: {z["isp"]}
🔰 » Country: {z["country"]}
🤖 » @ARI_VPN_STORE
━━━━━━━━━━━━━━━━━━━━━━━``` 
"""
            await event.edit(msg, buttons=inline)
        except Exception as e:
            print(f"Error: {e}")
            await event.answer("An error occurred.", alert=True)

    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await shadowsocks_(event)
    else:
        await event.answer("Access Denied", alert=True)
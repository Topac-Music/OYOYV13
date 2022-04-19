import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["تحديث"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("①")
    await loli.edit("②")
    await loli.edit("③")
    await loli.edit("④")
    await loli.edit("⑤")
    await loli.edit("⑥")
    await loli.edit("⑦")
    await loli.edit("⑧")
    await loli.edit("⑨")
    await loli.edit("⑩")   
    await loli.edit("✅𝙏𝙊𝙋𝘼𝘾:@OYOYV تم اعاده تشغيل سورس ميوزك توب")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["اوامري"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    await m.reply_photo( photo="https://telegra.ph/file/22e2ffdf24abb6bc9bd1b.jpg",
    HELP = f"""
<b>👋 اهلا {m.from_user.mention}!

اوامر سورس ميوزك توب 
▪︎▪︎▪︎▪︎●︎︎▪︎▪︎︎▪︎▪︎
🎵 | لتشغيل صوتية في المكالمة أرسل ⇦ [ {HNDLR}تشغيل  + اسم الاغنية ]
🎵 | لتشغيل فيديو في المكالمة  ⇦ [ {HNDLR}تشغيل_فيديو  + اسم الاغنية ]
▪︎▪︎▪︎▪︎●︎︎▪︎▪︎︎▪︎▪︎

🎵 | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ {HNDLR}استئناف ] 
🎵 | لأعاده تشغيل الاغنية ⇦  [ {HNDLR}ايقاف_الاستئناف ]
🎵 | لأيقاف الاغنية  ⇦ [ {HNDLR}ايقاف ] 
▪︎▪︎▪︎▪︎●︎︎▪︎▪︎︎▪︎▪︎

🎵 | لتحميل صوتية أرسل ⇦ [ {HNDLR}تحميل + اسم الاغنية او الرابط ]
🎵 | لتحميل فيديو  ⇦  [ {HNDLR}تحميل_فيديو + اسم الاغنية او الرابط ]
▪︎▪︎▪︎▪︎●︎︎▪︎▪︎︎▪︎▪︎
🎵 | حول السورس ⇦  [ {HNDLR}معلومات ]
🎵 | لأعاده تشغيل التنصيب أرسل ⇦  [ {HNDLR}تحديث ]
▪︎▪︎▪︎▪︎●︎︎▪︎▪︎︎▪︎▪︎
🛠 | @OYOYV
⭐ | @GTT_G"""
    await m.reply(HELP)
@Client.on_message(filters.command(["معلومات"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!

🎶 هذا هو سورس ميوزك توب 
🤖 اختصاص هذا البوت تنزيل المقاطع الصوتيه
 وتشغيل او تنزيل مقاطع الفيديو و تشغيل 
وتشغيل الاغاني ول فيديوهات في المكالمات
@GTT_G @OYOYV
المساعده : @TROTOOL
"""
    await m.reply(REPO, disable_web_page_preview=True)

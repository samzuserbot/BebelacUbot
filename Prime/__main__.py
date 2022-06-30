# Copyright (C) 2020-2021 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/Prime-Userbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/Prime-Userbot/blob/master/LICENSE >
#
# All rights reserved.


from pyrogram import __version__ as pyver
from pyrogram import idle
from pyrogram.errors import BadRequest

from config import LOG_CHAT, PREFIX
from Prime import app

app.start()
me = app.get_me()

print(
    f"Prime UserBot started for user {me.first_name}. Type {PREFIX}help in any telegram chat."
)
try:
    app.send_message(
        LOG_CHAT,
        f"🔥 **Prime Userbot Udah aktif**🔥\n└ •**ᴏᴡɴᴇʀ** : [{me.first_name}](tg://user?id={me.id})\n└ •**Pyrogram Version** : `{pyver}`\n└ •**Support By**: @PrimeSupportGroup\n└ •**Patner**: @musikkugroup",
    )
    app.join_chat("primesupportgroup")
    app.join_chat("primesupportchannel")
    app.join_chat("musikkugroup")
    app.join_chat("musikkuchannel")
    idle()
except BadRequest:
    pass
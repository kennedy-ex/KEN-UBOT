# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# KEN-UBOT

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import APP2, APP3, APP4, APP5, bot, branch

MSG_ON = """
⚡ **Your KEN-UBOT Is Actived**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def ken_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if APP2:
            if BOTLOG_CHATID != 0:
                await APP2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if APP3:
            if BOTLOG_CHATID != 0:
                await APP3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if APP4:
            if BOTLOG_CHATID != 0:
                await APP4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if APP5:
            if BOTLOG_CHATID != 0:
                await APP5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

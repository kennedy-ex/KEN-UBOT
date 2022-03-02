# Man - UserBot
# Copyright (c) 2022 Man-Userbot
# Credits: @mrismanaziz || https://github.com/mrismanaziz
#
# KEN-UBOT

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, APP2, APP3, APP4, APP5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if APP2 is not None:
            id2 = await APP2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if APP3 is not None:
            id3 = await APP3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if APP4 is not None:
            id4 = await APP4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if APP5 is not None:
            id5 = await APP5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("ODQ0NDMyMjIw").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        KEN_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        KEN_USER = client.first_name
    ken_mention = f"[{KEN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, KEN_USER, ken_mention

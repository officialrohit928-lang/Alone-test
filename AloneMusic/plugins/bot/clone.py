import re
import logging
import asyncio
import requests
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid

# Adjust these imports according to your repo structure
from main import app  # aapke bot ka main Client object
from utils.database import clonebotdb, get_assistant, has_user_cloned_any_bot, get_owner_id_from_db
from utils.decorators import language
from config import API_ID, API_HASH, LOGGER_ID, CLONE_LOGGER, OWNER_ID, SUDOERS, SUPPORT_CHAT

CLONES = set()

C_BOT_DESC = (
    "Wᴀɴᴛ ᴀ ʙᴏᴛ ʟɪᴋᴇ ᴛʜɪs? Cʟᴏɴᴇ ɪᴛ ɴᴏᴡ! ✅\n\n"
    "Vɪsɪᴛ: @kriti_xmusic_bot ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ!\n\n"
    " - Uᴘᴅᴀᴛᴇ: @TEAM_BADNAM_BOTS\n - Sᴜᴘᴘᴏʀᴛ: @KRITI_UPDATE"
)

C_BOT_COMMANDS = [
    {"command": "/start", "description": "sᴛᴀʀᴛs ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ"},
    {"command": "/help", "description": "ɢᴇᴛ ʜᴇʟᴩ ᴍᴇɴᴜ ᴡɪᴛʜ ᴇxᴩʟᴀɴᴀᴛɪᴏɴ ᴏғ ᴄᴏᴍᴍᴀɴᴅs."},
    {"command": "/play", "description": "sᴛᴀʀᴛs sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛʀᴀᴄᴋ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ."},
    {"command": "/pause", "description": "ᴩᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ."},
    {"command": "/resume", "description": "ʀᴇsᴜᴍᴇ ᴛʜᴇ ᴩᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ."},
    {"command": "/skip", "description": "ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ᴀɴᴅ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴛʜᴇ ɴᴇxᴛ ᴛʀᴀᴄᴋ ɪɴ ǫᴜᴇᴜᴇ."},
    {"command": "/end", "description": "ᴄʟᴇᴀʀs ᴛʜᴇ ǫᴜᴇᴜᴇ ᴀɴᴅ ᴇɴᴅ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ."},
    {"command": "/ping", "description": "ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ."},
    {"command": "/id", "description": "ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ɢʀᴏᴜᴘ ɪᴅ. ɪғ ᴜsᴇᴅ ʙʏ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ɢᴇᴛs ᴛʜᴀᴛ ᴜsᴇʀ's ɪᴅ."},
]

# ---------------------------- CLONE BOT COMMAND ----------------------------

@app.on_message(filters.command("clone"))
@language
async def clone_txt(client, message, _):
    userbot = await get_assistant(message.chat.id)
    userid = message.from_user.id

    has_already_cbot = await has_user_cloned_any_bot(userid)
    if has_already_cbot and userid != OWNER_ID:
        return await message.reply_text(_["C_B_H_0"])

    if len(message.command) > 1:
        bot_token = message.text.split("/clone", 1)[1].strip()
        mi = await message.reply_text(_["C_B_H_2"])
        try:
            ai = Client(
                bot_token,
                API_ID,
                API_HASH,
                bot_token=bot_token,
                plugins=dict(root="cplugin"),  # adjust plugin folder if needed
            )
            await ai.start()
            bot = await ai.get_me()
            bot_id = bot.id
            c_b_owner_fname = message.from_user.first_name
            c_bot_owner = message.from_user.id
        except (AccessTokenExpired, AccessTokenInvalid):
            await mi.edit_text(_["C_B_H_3"])
            return
        except Exception as e:
            if "database is locked" in str(e).lower():
                await message.reply_text(_["C_B_H_4"])
            else:
                await mi.edit_text(f"An error occurred: {str(e)}")
            return

        await mi.edit_text(_["C_B_H_5"])
        try:
            await app.send_message(
                CLONE_LOGGER,
                f"**#New_Cloned_Bot**\n\n**ʙᴏᴛ:- {bot.mention}**\n**ᴜsᴇʀɴᴀᴍᴇ:** @{bot.username}\n**ʙᴏᴛ ɪᴅ :** `{bot_id}`\n\n"
                f"**ᴏᴡɴᴇʀ : ** [{c_b_owner_fname}](tg://user?id={c_bot_owner})"
            )
            await userbot.send_message(bot.username, "/start")

            details = {
                "bot_id": bot.id,
                "is_bot": True,
                "user_id": message.from_user.id,
                "name": bot.first_name,
                "token": bot_token,
                "username": bot.username,
                "channel": "KRITI_UPDATE",
                "support": "TEAM_BADNAM_BOTS",
                "premium": False,
                "Date": False,
            }
            clonebotdb.insert_one(details)
            CLONES.add(bot.id)

            # Set bot commands
            url = f"https://api.telegram.org/bot{bot_token}/setMyCommands"
            response = requests.post(url, json={"commands": C_BOT_COMMANDS})
            print(response.json())

            # Set bot description
            url = f"https://api.telegram.org/bot{bot_token}/setMyDescription"
            response = requests.post(url, data={"description": C_BOT_DESC})
            if response.status_code == 200:
                logging.info(f"Successfully updated Description for bot: {bot_token}")
            else:
                logging.error(f"Failed to update Description: {response.text}")

            await mi.edit_text(_["C_B_H_6"].format(bot.username))

        except Exception as e:
            logging.exception("Error while cloning bot.")
            await mi.edit_text(
                f"⚠️ <b>ᴇʀʀᴏʀ:</b>\n\n<code>{e}</code>\n\n**ᴋɪɴᴅʟʏ ғᴏᴡᴀʀᴅ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴛᴏ @KRITI_UPDATE ᴛᴏ ɢᴇᴛ ᴀssɪsᴛᴀɴᴄᴇ**"
            )
    else:
        await message.reply_text(_["C_B_H_1"])

# ---------------------------- DELETE BOT COMMAND ----------------------------

@app.on_message(filters.command(["delbot", "rmbot", "delcloned"]) & SUDOERS)
@language
async def delete_cloned_bot(client, message, _):
    try:
        if len(message.command) < 2:
            await message.reply_text(_["C_B_H_8"])
            return

        query_value = message.command[1].lstrip("@")
        cloned_bot = clonebotdb.find_one({"$or": [{"token": query_value}, {"username": query_value}]})

        if cloned_bot:
            C_OWNER = get_owner_id_from_db(cloned_bot['bot_id'])
            OWNERS = [OWNER_ID, C_OWNER]

            if message.from_user.id not in OWNERS:
                return await message.reply_text(_["NOT_C_OWNER"].format(SUPPORT_CHAT))

            clonebotdb.delete_one({"_id": cloned_bot["_id"]})
            CLONES.discard(cloned_bot["bot_id"])

            await message.reply_text(_["C_B_H_10"])
        else:
            await message.reply_text(_["C_B_H_11"])
    except Exception as e:
        logging.exception(e)
        await message.reply_text(_["C_B_H_12"])

#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union
from pyrogram import Client
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from AloneMusic import app
from AloneMusic.misc import SUDOERS
from AloneMusic.utils.inline.help import extra_features_panel
from AloneMusic.utils import help_pannel
from AloneMusic.utils.database import get_lang
from AloneMusic.utils.decorators.language import LanguageStart, languageCB
from AloneMusic.utils.inline.help import help_back_markup, private_help_panel
from config import BANNED_USERS, START_IMG_URL, SUPPORT_CHAT
from strings import get_string, helpers


@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
@app.on_callback_query(filters.regex("settings_back_helper") & ~BANNED_USERS)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    is_callback = isinstance(update, types.CallbackQuery)
    if is_callback:
        try:
            await update.answer()
        except:
            pass
        chat_id = update.message.chat.id
        language = await get_lang(chat_id)
        _ = get_string(language)
        keyboard = help_pannel(_, True)
        await update.edit_message_text(
            _["help_1"].format(SUPPORT_CHAT), reply_markup=keyboard
        )
    else:
        try:
            await update.delete()
        except:
            pass
        language = await get_lang(update.chat.id)
        _ = get_string(language)
        keyboard = help_pannel(_)
        await update.reply_photo(
            photo=START_IMG_URL,
            has_spoiler=True,
            caption=_["help_1"].format(SUPPORT_CHAT),
            reply_markup=keyboard,
        )

@app.on_message(filters.command(["help"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def help_com_group(client, message: Message, _):
    keyboard = private_help_panel(_)
    await message.reply_text(_["help_2"], reply_markup=InlineKeyboardMarkup(keyboard))

HELP_MAP = {
    "hb1": helpers.HELP_1,
    "hb2": helpers.HELP_2,
    "hb3": helpers.HELP_3,
    "hb4": helpers.HELP_4,
    "hb5": helpers.HELP_5,
    "hb6": helpers.HELP_6,
    "hb8": helpers.HELP_8,
    "hb9": helpers.HELP_9,
}

@app.on_callback_query()
async def all_callbacks(client, query):
    await query.answer()

    chat_id = query.message.chat.id
    language = await get_lang(chat_id)
    _ = get_string(language)

    data = query.data

    # ================= HELP BUTTONS =================
    if data.startswith("help_callback"):
        cb = data.split()[1]
        keyboard = help_back_markup(_)

        # sudo check
        if cb == "hb7":
            if query.from_user.id not in SUDOERS:
                return await query.answer("Only for sudo users", show_alert=True)

            return await query.message.edit_text(
                helpers.HELP_7,
                reply_markup=keyboard
            )

        # auto handle others
        if cb in HELP_MAP:
            return await query.message.edit_text(
                HELP_MAP[cb],
                reply_markup=keyboard
            )

    # ================= EXTRA FEATURES =================
    if data == "extra_features":
        return await query.message.edit_text(
            "💡 Extra Features:",
            reply_markup=extra_features_panel(_)
        )

    elif data == "tagall":
        return await query.message.edit_text(
            TAGALL_HELP,
            reply_markup=extra_features_panel(_)
        )

    elif data == "bans":
        return await query.message.edit_text(
            BANS_HELP,
            reply_markup=extra_features_panel(_)
        )

    elif data == "gpt_vc_logger":
        return await query.message.edit_text(
            GPT_VC_HELP,
            reply_markup=extra_features_panel(_)
        )

    elif data == "other_feature":
        return await query.message.edit_text(
            _["OTHER_FEATURE_HELP"],
            reply_markup=extra_features_panel(_)
        )

    # ================= BACK =================
    elif data == "help_back" or data == "settings_back_helper":
        return await query.message.edit_text(
            _["help_1"].format(SUPPORT_CHAT),
            reply_markup=help_pannel(_, True)
    )

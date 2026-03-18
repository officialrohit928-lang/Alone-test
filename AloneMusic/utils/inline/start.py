#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton

import config
from AloneMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


from pyrogram.types import InlineKeyboardButton
from pyrogram import enums  # 👈 ensure ye import hai

def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=enums.ButtonStyle.SUCCESS  # 🟢 Green (Add Me)
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                callback_data="shiv_aarumi",
                style=enums.ButtonStyle.PRIMARY  # 🔵 Blue (Support)
            ),
            InlineKeyboardButton(
                text="💌 ʏᴛ-ᴀᴘɪ",
                callback_data="bot_info_data",
                style=enums.ButtonStyle.SECONDARY  # ⚪ Grey
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=enums.ButtonStyle.DANGER  # 🔴 Red (Back)
            )
        ],
    ]
    return buttons

# Copyright (C) 2021-2022 by TheAloneteam@Github
# PyroFork compatible button panel

from pyrogram.types import InlineKeyboardButton
import config
from AloneMusic import app

# Start panel (public)
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT
            ),
        ],
    ]
    return buttons

# Private panel (DM / PM)
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                color="green"  # 🟢 Green for Add Me
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                callback_data="shiv_aarumi",
                color="blue"  # 🔵 Blue for Support
            ),
            InlineKeyboardButton(
                text="💌 ʏᴛ-ᴀᴘɪ",
                callback_data="bot_info_data",
                color="gray"  # ⚪ Grey
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                color="red"  # 🔴 Red for Back
            )
        ],
    ]
    return buttons

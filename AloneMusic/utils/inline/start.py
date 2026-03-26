from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle
import config
from AloneMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["S_B_2"],
                url=config.SUPPORT_CHAT,
                style=ButtonStyle.SUCCESS
            ),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.PRIMARY
            )
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_2"],
                callback_data="shiv_aarumi",
                style=ButtonStyle.SUCCESS
            ),
            InlineKeyboardButton(
                text="💌 ʏᴛ-ᴀᴘɪ",
                callback_data="bot_info_data",
                style=ButtonStyle.DANGER
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                callback_data="settings_back_helper",
                style=ButtonStyle.SECONDARY
            )
        ],
    ]
    return buttons

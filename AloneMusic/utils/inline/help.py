from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ✅ Safe import (IMPORTANT FIX)
try:
    from pyrogram.enums import ButtonStyle
except ImportError:
    ButtonStyle = None

from AloneMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [
        InlineKeyboardButton(
            text=_["CLOSE_BUTTON"],
            callback_data="close",
            style=ButtonStyle.DANGER if ButtonStyle else None
        )
    ]

    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settings_back_helper",  # ✅ fixed typo
            style=ButtonStyle.PRIMARY if ButtonStyle else None
        ),
    ]

    mark = second if START else first

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    _["H_B_1"], callback_data="help_callback:hb1",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_2"], callback_data="help_callback:hb2",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_3"], callback_data="help_callback:hb3",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
            ],
            [
                InlineKeyboardButton(
                    _["H_B_4"], callback_data="help_callback:hb4",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_5"], callback_data="help_callback:hb5",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_6"], callback_data="help_callback:hb6",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
            ],
            [
                InlineKeyboardButton(
                    _["H_B_7"], callback_data="help_callback:hb7",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_8"], callback_data="help_callback:hb8",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    _["H_B_9"], callback_data="help_callback:hb9",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
            ],
            [
                InlineKeyboardButton(
                    "Tᴀɢᴀʟʟ", callback_data="help_callback:hb10",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    "Wɪsʜ ᴛᴀɢ", callback_data="help_callback:hb11",
                    style=ButtonStyle.SUCCESS if ButtonStyle else None
                ),
                InlineKeyboardButton(
                    "Vᴄ ʟᴏɢs", callback_data="help_callback:hb12",
                    style=ButtonStyle.PRIMARY if ButtonStyle else None
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons

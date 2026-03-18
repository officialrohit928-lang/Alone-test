from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneMusic import app

# 🔹 MAIN HELP PANEL
def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settings_back_helper",
        ),
    ]
    mark = second if START else first

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(_["H_B_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(_["H_B_2"], callback_data="help_callback hb2"),
                InlineKeyboardButton(_["H_B_3"], callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(_["H_B_4"], callback_data="help_callback hb4"),
                InlineKeyboardButton(_["H_B_5"], callback_data="help_callback hb5"),
                InlineKeyboardButton(_["H_B_6"], callback_data="help_callback hb6"),
            ],
            [
                InlineKeyboardButton(_["H_B_7"], callback_data="help_callback hb7"),
                InlineKeyboardButton(_["H_B_8"], callback_data="help_callback hb8"),
                InlineKeyboardButton(_["H_B_9"], callback_data="help_callback hb9"),
            ],
            # 🔥 EXTRA FEATURES (MERGED)
            [
                InlineKeyboardButton("TagAll", callback_data="help_callback hb10"),
                InlineKeyboardButton("Bans", callback_data="help_callback hb11"),
                InlineKeyboardButton("VC Logger", callback_data="help_callback hb12"),
            ],
            mark,
        ]
    )
    return upl


# 🔹 BACK BUTTON (INSIDE HELP)
def help_back_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="settings_back_helper",
                )
            ]
        ]
    )


# 🔹 GROUP HELP BUTTON
def private_help_panel(_):
    return [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            )
        ]
    ]

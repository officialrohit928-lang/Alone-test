#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneMusic import app

# Main Help Panel
def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
    ]
    mark = second if START else first

    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["H_B_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["H_B_2"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["H_B_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["H_B_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["H_B_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["H_B_7"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["H_B_8"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["H_B_9"],
                    callback_data="help_callback hb9",
                ),
            ],
            # Extra Features Button Row
            [
                InlineKeyboardButton(
                    text="Extra Features",  # aap chahe toh helper me bhi define kar sakte ho
                    callback_data="extra_features"
                )
            ],
            mark,
        ]
    )
    return upl

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def extra_features_panel(_):
    buttons = [
        # 1st row: 3 buttons
        [
            InlineKeyboardButton(text="TagAll", callback_data="tagall"),
            InlineKeyboardButton(text="Bans", callback_data="bans"),
            InlineKeyboardButton(text="VC Logger", callback_data="gpt_vc_logger"),
        ],
        # 2nd row: 2 buttons
        [
            InlineKeyboardButton(text="Other Feature", callback_data="other_feature"),
            InlineKeyboardButton(text="Another Feature", callback_data="another_feature"),  # optional
        ],
        # 3rd row: Back button
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_back_helper")
        ]
    ]
    return InlineKeyboardMarkup(buttons)
    
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

# This file is a part of TG-FileStreamBot
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


class Language(object):
    def __new__ (self, message: Message):
        if getattr(message.from_user, 'language_code', 'Unknown') in self.available:
            return getattr(self, getattr(message.from_user, 'language_code', self.en), self.en)
        else:
            return self.en

    available=['en', 'Test']

    class en(object):
        START_TEXT = """
<i>你好,</i>{}\n
<i>此BOT可将发送从电报中任何文件或视频转为直链</i>\n"""

        HELP_TEXT = """
<i>- 给我发送任何文件（或）媒体来自Telegram。</i>
<i>- 我将提供外部直接下载链接！</i>
<i>- 本BOT基于TG-FileStreamBot项目改动</i>"""

        ABOUT_TEXT = """
<b>电报流媒体直链BOT</b>\n
"""

        stream_msg_text ="""
<i><u>你的链接生成完毕 !</u></i>\n
<b>📂 文件名 :</b> <i>{}</i>\n
<b>📦 文件大小 :</b> <i>{}</i>\n
<b>📥 下载 :</b> <i>{}</i>\n"""

    class Test(object):
        START_TEXT = """
<i>你好,</i>{}\n
<i>此BOT可将发送从电报中任何文件或视频转为直链</i>\n"""

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('帮助', callback_data='help'),
        InlineKeyboardButton('关于', callback_data='about'),
        InlineKeyboardButton('关闭', callback_data='close')
        ]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('主页', callback_data='home'),
        InlineKeyboardButton('关于', callback_data='about'),
        InlineKeyboardButton('关闭', callback_data='close'),
        ]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('主页', callback_data='home'),
        InlineKeyboardButton('帮助', callback_data='help'),
        InlineKeyboardButton('关闭', callback_data='close'),
        ]
        ]
    )

# This file is a part of TG-FileStreamBot

from urllib.parse import quote_plus
from pyrogram import Client
from typing import Any, Optional
from pyrogram.types import Message
from pyrogram.file_id import FileId
from pyrogram.raw.types.messages import Messages
from WebStreamer.server.exceptions import FIleNotFound
from WebStreamer.utils.Translation import Language
from WebStreamer.utils.human_readable import humanbytes
from WebStreamer.vars import Var
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def parse_file_id(message: "Message") -> Optional[FileId]:
    media = get_media_from_message(message)
    if media:
        return FileId.decode(media.file_id)

async def parse_file_unique_id(message: "Messages") -> Optional[str]:
    media = get_media_from_message(message)
    if media:
        return media.file_unique_id

async def get_file_ids(client: Client, chat_id: int, message_id: int) -> Optional[FileId]:
    message = await client.get_messages(chat_id, message_id)
    if message.empty:
        raise FIleNotFound
    media = get_media_from_message(message)
    file_unique_id = await parse_file_unique_id(message)
    file_id = await parse_file_id(message)
    setattr(file_id, "file_size", getattr(media, "file_size", 0))
    setattr(file_id, "mime_type", getattr(media, "mime_type", ""))
    setattr(file_id, "file_name", getattr(media, "file_name", ""))
    setattr(file_id, "unique_id", file_unique_id)
    return file_id

def get_media_from_message(message: "Message") -> Any:
    media_types = (
        "audio",
        "document",
        "photo",
        "sticker",
        "animation",
        "video",
        "voice",
        "video_note",
    )
    for attr in media_types:
        media = getattr(message, attr, None)
        if media:
            return media


def get_hash(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return getattr(media, "file_unique_id", "")[:6]

def get_media_file_size(m):
    media = get_media_from_message(m)
    return getattr(media, "file_size", "None")

def get_name(media_msg: Message) -> str:
    media = get_media_from_message(media_msg)
    return str(getattr(media, "file_name", "None"))

def get_media_mime_type(m):
    media = get_media_from_message(m)
    return getattr(media, "mime_type", "None/unknown")

def get_media_file_unique_id(m):
    media = get_media_from_message(m)
    return getattr(media, "file_unique_id", "")

# Generate Text, Stream Link, reply_markup
async def gen_link(m: Message,log_msg: Messages, from_channel: bool):
    """Generate Text for Stream Link, Reply Text and reply_markup"""
    lang = Language(m)
    file_name = get_name(log_msg)
    file_size = humanbytes(get_media_file_size(log_msg))

    page_link = f"{Var.URL}watch/{get_hash(log_msg)}{log_msg.id}"
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
    Stream_Text=lang.stream_msg_text.format(file_name, file_size, stream_link, page_link)
    reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("下载文件", url=stream_link)]])

    if from_channel:
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("下载文件", url=stream_link)]])
    else:
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("下载文件", url=stream_link)],
            [InlineKeyboardButton("删除链接", callback_data=f"msgdelconf2_{log_msg.id}_{get_media_file_unique_id(log_msg)}")]])

    return reply_markup, Stream_Text, stream_link
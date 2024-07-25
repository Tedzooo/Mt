import os
import time
import random
import asyncio
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from photos import PICS
from pyrogram import Client, filters, enums
import ffmpeg
from tqdm import tqdm


##########




@app.on_message(filters.command("help"))
async def start(client, message):
    start_message = (
    
        "👋 Hello welcome to the Video Sample Bot!\n\n"
        "Send me a video file (MKV or MP4), and I'll generate a 30-second sample video for you."
    )
    buttons = [[
            InlineKeyboardButton("➕️ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀᴛ ➕", url=f"http://t.me/{temp.U_NAME}?startgroup=true")
            ],[
            InlineKeyboardButton("Sᴇᴀʀᴄʜ 🔎", switch_inline_query_current_chat=''), 
            InlineKeyboardButton("Cʜᴀɴɴᴇʟ 🔈", url="https://t.me/PanjabiMoviePBX1")
            ],[      
            InlineKeyboardButton("Hᴇʟᴩ 🕸️", callback_data="cancel"),
            InlineKeyboardButton("Aʙᴏᴜᴛ ✨", callback_data="cancel")
        ]]
        m = await message.reply_sticker("CAACAgUAAxkBAAEBvlVk7YKnYxIHVnKW2PUwoibIR2ygGAACBAADwSQxMYnlHW4Ls8gQHgQ")
        await asyncio.sleep(2)
        await message.reply_photo(photo=random.choice(PICS), caption=start_message.format(user=message.from_user.mention, bot=client.mention), reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML)
        return await m.delete()

@app.on_callback_query(filters.regex("cancel"))
async def cancel(client, callback_query):
    await callback_query.message.delete()


@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = (
        "Welcome to the Video Sample Bot Help!\n\n"
        "Commands:\n"
        "/start - Start the bot and get instructions.\n"
        "/help - Get this help message.\n\n"
        "Usage:\n"
        "Send me a video file (MKV or MP4), and I'll generate a 30-second sample video for you.\n\n"
        "Note:\n"
        "This bot currently supports MKV and MP4 video formats for generating samples."
    )
    await message.reply_text(help_text)

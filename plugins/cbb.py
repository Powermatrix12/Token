#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>POWER OWNER</a>\n○ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+MhcwQJ-zeOUyZGQ9'>ᴄʏʙᴇʀᴍᴀᴛʀɪxᴛᴍ</a>\n○ ᴍᴏᴠɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/+zgKTqE-TN24yZjk1'>ᴘᴏᴡᴇʀᴍᴏᴠɪᴇs</a>\n○ ᴘʀᴇᴍɪᴜᴍ ᴍᴏᴅs : <a href='https://t.me/+00nBBOaHvmtlYWZl'>ᴘᴏᴡᴇʀᴠɪᴘᴍᴏᴅs</a>\n○ ɢʀᴏᴜᴘ ᴄʜᴀᴛ : <a href='https://t.me/+Hhszwjqoplk4YzFl'>sɪᴍᴘʟᴇ ʙᴜᴅᴅʏs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/+Vn7rZGdph280MDll')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

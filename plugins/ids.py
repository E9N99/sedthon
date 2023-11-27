import random
import re
from pyrogram import Client
from pyrogram.types import Message
from database import get_db_addcustomid, get_db_mypointgame, get_db_mymessage, get_db_mycontact
from localization import use_chat_lang
from config import get_bot_information
from plugins.admin import get_available_adminstrator
from plugins.rtp_function import get_Rank
#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####  #            #####    
#           #    #    #          #     ##   #     #
#              #      #####   ######   #     #


iddof = []
@app.on_message(
    command([" "," "])
    & filters.group
    & ~filters.edited
)
async def iddlock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("   ")
      iddof.append(message.chat.id)
      return await message.reply_text("    ")
   else:
      return await message.reply_text("      ")

@app.on_message(
    command([" "," "])
    & filters.group
    & ~filters.edited
)
async def iddopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("    ")
      iddof.remove(message.chat.id)
      return await message.reply_text("    ")
   else:
      return await message.reply_text("      ")




@app.on_message(
    command(["","id",""])
    & filters.group
    & ~filters.edited
)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f""" � :{message.from_user.mention}\n � :@{message.from_user.username}\n � :`{message.from_user.id}`\n � :{usr.bio}\n �: {message.chat.title}\n �. :`{message.chat.id}`""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



iddof = []
@app.on_message(
    command([" "," "])
    & filters.group
    & ~filters.edited
)
async def lllock(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if message.chat.id in iddof:
        return await message.reply_text("   ")
      iddof.append(message.chat.id)
      return await message.reply_text("    ")
   else:
      return await message.reply_text("      ")

@app.on_message(
    command([" "," "])
    & filters.group
    & ~filters.edited
)
async def idljjopen(client, message):
   get = await app.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in ["creator", "administrator"]:
      if not message.chat.id in iddof:
        return await message.reply_text("   ")
      iddof.remove(message.chat.id)
      return await message.reply_text("    ")
   else:
      return await message.reply_text("      ")




@app.on_message(
    command([""])
    & filters.group
    & ~filters.edited
)
async def idjjdd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"     \n \n: {ik} %", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       


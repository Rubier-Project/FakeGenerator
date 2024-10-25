configs = {
    "bot_token": ""
}

# ------------------

from core import loops
from asyncio import run
from random import choice
from os.path import getsize
from telebot import TeleBot
from telebot.async_telebot import AsyncTeleBot

from telebot.types import (
    Message, User,
    ReplyKeyboardMarkup, InlineKeyboardButton,
    InlineKeyboardMarkup, KeyboardButton
)

loops = loops.Loops()
bot = AsyncTeleBot(configs["bot_token"])
sync_bot = TeleBot(configs["bot_token"])

for user in sync_bot.get_me():
    user = User(user)
    configs['username'] = user.username.replace("@", "")
    break

print("Seted id:", configs['username'])

browsers = ["chrome", "edge", "firefox", "safari"]
oss = ["windows", "macos", "linux", "android", "ios"]
platforms = ["pc", "mobile", "tablet"]
userize = {}

@bot.message_handler(content_types=['text'], chat_types=['private', 'supergroup'])
async def on(message: Message):
    message.text == message.text.strip()

    if message.text == "/start":
        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton(
                "See Help",
                callback_data="Help"
            )
        )

        await bot.reply_to(
            message,
            "Welcome to The Fake Agent Generator Bot 👁",
            reply_markup=markup
        )

    elif message.text.startswith("/create"):
        txt = message.text[6:].strip()
        if not txt.isdigit():
            if txt == "fast":
                brw = choice(browsers)
                _os = choice(oss)
                plt = choice(platforms)
                agent = await loops.once(brw, _os, plt)
                
                await bot.reply_to(
                    message,
                    f"✳ Browser: {brw}\n🔰 OS: {_os}\n♻ Platform: {plt}\n🎟 Agent: `{agent}`",
                    parse_mode="Markdown"
                )
            
            else:
                userize[str(message.from_user.id)] = {}
                markup = ReplyKeyboardMarkup(resize_keyboard=True)
                for brw in browsers:
                    markup.add(
                        KeyboardButton(
                            f"{brw} 📱"
                        )
                    )

        else:
            if 0 < int(txt) <= 1000:
                userize[str(message.from_user.id)] = {}
                userize[str(message.from_user.id)]['length'] = int(txt)
            else:await bot.reply_to(message, "Invalid Range ! Type /help to see infos")

    elif message.text.startswith(f"/create@{configs['username']}"):
        txt = message.text[6+2+len(configs['username']):].strip()
        if not txt.isdigit():
            if txt == "fast":
                brw = choice(browsers)
                _os = choice(oss)
                plt = choice(platforms)
                agent = await loops.once(brw, _os, plt)
                
                await bot.reply_to(
                    message,
                    f"✳ Browser: {brw}\n🔰 OS: {_os}\n♻ Platform: {plt}\n🎟 Agent: `{agent}`",
                    parse_mode="Markdown"
                )
            
            else:
                userize[str(message.from_user.id)] = {}
                markup = ReplyKeyboardMarkup(resize_keyboard=True)
                for brw in browsers:
                    markup.add(
                        KeyboardButton(
                            f"{brw} 📱"
                        )
                    )

        else:
            if 0 < int(txt) <= 1000:
                userize[str(message.from_user.id)] = {}
                userize[str(message.from_user.id)]['length'] = int(txt)
            else:await bot.reply_to(message, "Invalid Range ! Type /help to see infos")

    # Browser

    elif message.text == "chrome 📱":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['browser'] = "chrome"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for o_s in oss:
                markup.add(
                    KeyboardButton(
                        f"{o_s} 💻"
                    )
                )

    elif message.text == "edge 📱":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['browser'] = "edge"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for o_s in oss:
                markup.add(
                    KeyboardButton(
                        f"{o_s} 💻"
                    )
                )

    elif message.text == "firefox 📱":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['browser'] = "firefox"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for o_s in oss:
                markup.add(
                    KeyboardButton(
                        f"{o_s} 💻"
                    )
                )

    elif message.text == "safari 📱":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['browser'] = "safari"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for o_s in oss:
                markup.add(
                    KeyboardButton(
                        f"{o_s} 💻"
                    )
                )

    # OS

    elif message.text == "windows 💻":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['os'] = "windows"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for plt in platforms:
                markup.add(
                    KeyboardButton(
                        f"{platforms} 📪"
                    )
                )

    elif message.text == "macos 💻":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['os'] = "macos"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for plt in platforms:
                markup.add(
                    KeyboardButton(
                        f"{platforms} 📪"
                    )
                )

    elif message.text == "linux 💻":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['os'] = "linux"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for plt in platforms:
                markup.add(
                    KeyboardButton(
                        f"{platforms} 📪"
                    )
                )

    elif message.text == "android 💻":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['os'] = "android"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for plt in platforms:
                markup.add(
                    KeyboardButton(
                        f"{platforms} 📪"
                    )
                )

    elif message.text == "ios 💻":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['os'] = "ios"
            markup = ReplyKeyboardMarkup(resize_keyboard=True)
            for plt in platforms:
                markup.add(
                    KeyboardButton(
                        f"{platforms} 📪"
                    )
                )

    # Platform

    elif message.text == "pc 📪":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['platform'] = "pc"
            data = await loops.createList(userize[str(message.from_user.id)]['browser'],
                                        userize[str(message.from_user.id)]['os'],
                                        userize[str(message.from_user.id)]['platform'],
                                        userize[str(message.from_user.id)]['length'])
            
            if data['status'] == "OK":
                size = getsize(data['file_name'])
                with open(data['file_name'], 'rb') as doc:
                    await bot.send_document(
                        message.chat.id,
                        data=doc,
                        caption=f"✳ Browser: {userize[str(message.from_user.id)]['browser']}\n🔰 OS: {userize[str(message.from_user.id)]['os']}\n♻ Platform: {userize[str(message.from_user.id)]['platform']}\n🎟 Agents Length: `{userize[str(message.from_user.id)]['length']}\n🎫 File Size: {size}`",
                        reply_to_message_id=message.id
                    )

                del userize[str(message.from_user.id)]

            else:
                await bot.reply_to(message, "An Error Detected: {}".format(data['message']))
                print(data['message'])

    elif message.text == "mobile 📪":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['platform'] = "mobile"
            data = await loops.createList(userize[str(message.from_user.id)]['browser'],
                                        userize[str(message.from_user.id)]['os'],
                                        userize[str(message.from_user.id)]['platform'],
                                        userize[str(message.from_user.id)]['length'])
            
            if data['status'] == "OK":
                size = getsize(data['file_name'])
                with open(data['file_name'], 'rb') as doc:
                    await bot.send_document(
                        message.chat.id,
                        data=doc,
                        caption=f"✳ Browser: {userize[str(message.from_user.id)]['browser']}\n🔰 OS: {userize[str(message.from_user.id)]['os']}\n♻ Platform: {userize[str(message.from_user.id)]['platform']}\n🎟 Agents Length: `{userize[str(message.from_user.id)]['length']}\n🎫 File Size: {size}`",
                        reply_to_message_id=message.id
                    )

                del userize[str(message.from_user.id)]

            else:
                await bot.reply_to(message, "An Error Detected: {}".format(data['message']))
                print(data['message'])

    elif message.text == "tablet 📪":
        if str(message.from_user.id) in list(userize.keys()):
            userize[str(message.from_user.id)]['platform'] = "tablet"
            data = await loops.createList(userize[str(message.from_user.id)]['browser'],
                                        userize[str(message.from_user.id)]['os'],
                                        userize[str(message.from_user.id)]['platform'],
                                        userize[str(message.from_user.id)]['length'])
            
            if data['status'] == "OK":
                size = getsize(data['file_name'])
                with open(data['file_name'], 'rb') as doc:
                    await bot.send_document(
                        message.chat.id,
                        data=doc,
                        caption=f"✳ Browser: {userize[str(message.from_user.id)]['browser']}\n🔰 OS: {userize[str(message.from_user.id)]['os']}\n♻ Platform: {userize[str(message.from_user.id)]['platform']}\n🎟 Agents Length: `{userize[str(message.from_user.id)]['length']}\n🎫 File Size: {size}`",
                        reply_to_message_id=message.id
                    )

                del userize[str(message.from_user.id)]

            else:
                await bot.reply_to(message, "An Error Detected: {}".format(data['message']))
                print(data['message'])

@bot.callback_query_handler(lambda call: True)
async def answerQuery(call):
    if call.data == "Help":
        await bot.send_message(
            call.message.chat.id,
            "For Create an Agent ( Once ): /create\nSend File with a huge Length ( 0 - 1000 ): /create <NUMBER> [ /create 400 ]"
        )

def runing():
    run(bot.polling())

if __name__ == "__main__":
    runing()
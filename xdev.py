import os
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

harshithxdev= Client(
    "Welcome-Bot",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@harshithxdev.on_message(filters.command("start"))
async def start(client: harshithxdev, update):
    start_msg = "👋Hy {}, Iam Simple Auto Welcome Bot\n\nPowered By »» @HarshithXDev"
    bot_username = await client.get_me()
    link = "HarshithXDev/AutoWelcomeBot"
    reply_markup = InlineKeyboardMarkup(
        [             
            [
                InlineKeyboardButton
                    (
                         "💞 Our Channel 💞", url="t.me/HarshithX"
                    ),
                InlineKeyboardButton
                    (
                         "✨ Source Code ✨", url="https://github.com/{link}"
                    )
            ],   
            [
                InlineKeyboardButton
                   (
                        "➕️ Add Me To Your Chats ➕️", url=f"http://t.me/{bot_username.username}?startgroup=botstart"
                   )
            ]
        ] 
    )                       
    await update.reply_text(
        text=start_msg.format(update.from_user.mention), reply_markup=reply_markup)



@harshithxdev.on_message(filters.private & filters.command("admin"))
async def admin(bot: harshithxdev, update):
    # Heroku Support
    user = "👋Hey {}, \n You are not the deploy of this bot"
    run = "WxJ3G7NBb4c" # https://github.com/HarshithXDev/AutoWelcomeBot
    api_key = os.environ.get("APP_NAME", "AutoWelcomeBot")
    DEPLOY = bool(os.environ.get("HOSTED"))
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())
    if not DEPLOY:
       reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️HEROKU SETTINGS⚙️", url=f"https://dashboard.heroku.com/apps/{api_key}/settings"
                    )
            ]
        ]
    )
    else:
       reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "⚙️RAILWAY APP⚙️", url="https://railway.app/"
                    )
            ]
        ]
    )
    if not DEPLOY:
       user_admin = "Open Heroku => Application => Settings => Config Vars => Welcome_Text Edit"
    else:
       user_admin = "Open Railway Website=> Application => Variables => Welcome_Text Edit"
    deploy =InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton
                    (
                        "💫 DEPLOY NOW 💫", url=f"https://youtu.be/{run}"
                    )
            ]
        ]
    )
    if update.from_user.id not in OWNER_ID:
        await update.reply_text(text=user.format(update.from_user.mention), reply_markup=deploy)
        return
    await update.reply_text(text=user_admin, reply_markup=reply_markup)

@harshithxdev.on_message(filters.new_chat_members)
async def auto_welcome(bot: harshithxdev, msg: Message):
    # from harshithxdev import ID-Bot
    first = msg.from_user.first_name
    last = msg.from_user.last_name
    mention = msg.from_user.mention
    username = msg.from_user.username
    id = msg.from_user.id
    group_name = msg.chat.title
    group_username = msg.chat.username
    name_button = "🔰 JOIN NOW 🔰"
    link_button = "t.me/HarshithX"
    button_name = os.environ.get("WELCOME_BUTTON_NAME", name_button)
    button_link = os.environ.get("WELCOME_BUTTON_LINK", link_button)
    welcome_text = f"Hey {mention}\nWelcome To {group_name}"
    WELCOME_TEXT = os.environ.get("WELCOME_TEXT", welcome_text)
    print("Welcome Message Activate")
    BUTTON = bool(os.environ.get("WELCOME_BUTTON"))
    if not BUTTON:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          )
       )
    else:
       await msg.reply_text(text=WELCOME_TEXT.format(
           first = msg.from_user.first_name,
           last = msg.from_user.last_name,
           username = None if not msg.from_user.username else '@' + msg.from_user.username,
           mention = msg.from_user.mention,
           id = msg.from_user.id,
           group_name = msg.chat.title,
           group_username = None if not msg.chat.username else '@' + msg.chat.username
          ),
       reply_markup=InlineKeyboardMarkup(
               [
                   [
                       InlineKeyboardButton
                           (
                               button_name, url=button_link
                           )
                   ]  
               ]
           )
       )  


print("""Auto Welcome Bot Started

Powered By @HarshithXDev""")

harshithxdev.run()

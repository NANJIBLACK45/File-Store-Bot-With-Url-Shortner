import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "8733404"))
  API_HASH = os.environ.get("API_HASH", "f19aed00b0c74abed0359016afc1733f")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "6898447547:AAGhJsfZlRdzJwn9_G7UOubEtBiBhN6wzfI")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "QL_Movie_Links_Bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002087036746"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "ae8999b1a230fee55d762c4682e14321d29f7038")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "1109543851"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "mongodb+srv://MrHyper:Ennapassword@123@cluster0.jg7wqsl.mongodb.net/?retryWrites=true&w=majority")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002087036746"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [VJ](https://telegram.me/Tamilan_Rocks)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/Tamilan_Rocks)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""

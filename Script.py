class script(object):
    START_TXT = """𝐇𝐞𝐲 {}

⎆𝐌𝐲 𝐍𝐚𝐦𝐞 𝐢𝐬 ᴢᴇɴɪsᴛᴜ ⚡️⚡️

⎆𝐈 𝐀𝐦 𝐚 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐟𝐢𝐥𝐭𝐞𝐫 𝐁𝐨𝐭

𝙹𝚞𝚜𝚝 𝚊𝚍𝚍 𝚖𝚎 𝚝𝚘 𝚢𝚘𝚞𝚛 𝚐𝚛𝚘𝚞𝚙 𝚝𝚑𝚊𝚝'𝚜 𝚊𝚕𝚕

𝙸 𝚙𝚛𝚘𝚟𝚒𝚍𝚎 𝚖𝚘𝚟𝚒𝚎𝚜 𝚝𝚑𝚎𝚛𝚎"""

    HELP_TXT = """🙋🏻‍♂️   Hellooo   {}🤓

○ <b><u>Available Commands</b></u>
     
 /start - Check I'm Alive..
 /info - User info 
 /id - User id
 /broadcast - Broadcast (owner only)
 /stats - Db status  (pm only )
/song (song name) - For Songs

○ <b><u>Notice 📙:-</b></u>

○Dont Spam Me...🤒
    SONG_TXT = ""<b>🎼Song Download🎼</b>

Song Download Module, For Those Who Love Music

<b>🎈 Command 🎈</b>

- /song [Song Name] - To Download Music 😁

<b>🌀Usage🌀</b>

- Can Be Used By Everyone

- Works in bot pm
©️MᴀɪɴᴛᴀɪɴᴇD Bʏ <a href=https://t.me/blesson_3>ᴍʀ ᴍᴀᴋʀɪ [ᴏɴʟɪɴᴇ]</a>"""
    ABOUT_TXT = """ 𝐌𝐲 𝐍𝐚𝐦𝐞 : {}

🐇 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 : <a href=https://t.me/blesson_3>ᴍʀ ᴍᴀᴋʀɪ [ᴏɴʟɪɴᴇ]</a>

🕊 𝐂𝐫𝐞𝐝𝐢𝐭𝐬 : <a href=https://t.me/blesson_3>ᴍʀ ᴍᴀᴋʀɪ [ᴏɴʟɪɴᴇ]</a>

🕊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞 : 𝐏𝐲𝐭𝐡𝐨𝐧3

🕊 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 : 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐚𝐬𝐲𝐧𝐜𝐢𝐨 0.17.1

🕊 𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐞𝐝 𝐒𝐢𝐭𝐞 : 𝐎𝐧𝐥𝐲 𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦

🕊 𝐒𝐞𝐫𝐯𝐞𝐫 : 𝐇𝐞𝐫𝐨𝐤𝐮

🕊 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞 : 𝐌𝐨𝐧𝐠𝐨𝐃𝐁

🕊 𝐁𝐮𝐢𝐥𝐝 𝐒𝐭𝐚𝐭𝐮𝐬 : 𝐕2.1 [𝐁𝐄𝐓𝐀]"""
    SOURCE_TXT = """<b>NOTE:</b>
- LUCIFER is a open source project. 
- Source - https://github.com/Akbotmakersnew/LUCIFER  

<b>DEVS:</b>
- <a href=https://t.me/Ls_Supportz>Team Ls BOTZ</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. LUCIFER should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- LUCIFER Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. LUCIFER supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Ls_Supportz)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    SONG_TXT = """Help : <b>🎼Song Download🎼</b>

Song Download Module, For Those Who Love Music

<b>🎈 Command 🎈</b>

- /song [Song Name] - To Download Music 😁
    CONNECTION_TXT = ""help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

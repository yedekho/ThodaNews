class script(object):
    START_TXT = """Hello 👋 {},
    
My Name Is <a href=https://t.me/{}>{}</a>, I Can Provide Movies Just Add Me To Your Group and Enjoy 😍

Created By <a href=https://t.me/BKM_TG>𝙼𝚛.𝙱𝙺𝙼 𝚃𝙶</a> """

    HELP_TXT = """Hey 👋 {},
    
Here Is The Help For My Commands."""

    ABOUT_TXT = """✯ My Name: {}
✯ Creator: <a href=https://t.me/BKM_TG>Mr.BKM TG</a>
✯ Library: Pyrogram 
✯ Language: Python3
✯ DataBase: MongoDB
✯ Bot Server: Heroku
✯ Build Status: v1.0.1 [ BETA ]"""

    SOURCE_TXT = """<b>NOTE:</b>
    
- Eva Maria Is a Open Source Project. 

- Source - <a href= https://github.com/Mr-BKM/Lucifer-RoBoT>Click Here</a> """

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter Is The Feature Were Users Can Set Automated Replies For a Particular Keyword and Lucifer Will Respond Whenever a keyword Is Found The Message 

<b>NOTE:</b>
1. Lucifer Should Have Admin Privillage.
2. Only Admin Filters In a Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<b>Commands and Usage:</b>
• /filter - <code>Add a Filter In Chat</code>
• /filters - <code>List All The Filters Of a Chat</code>
• /del - <code>Delete a Specific Filter In Chat</code>
• /delall - <code>Delete The Whole Filters In a Chat (Chat Owner Only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- Lucifer Supports Both URL and Alert Inline Buttons.

<b>NOTE:</b>
1. Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
2. Lucifer Supports Buttons With Any Telegram Media Type.
3. Buttons Should Be Properly Parsed As Markdown Format.

<b>URL Buttons:</b>
<code>[Button Text](buttonurl:https://t.me/xxxxxxxxxxxx)</code>

<b>Alert Buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make Me Admin Of Your Channel If It's Private.
2. Make Sure That Your Channel Does Not Contains CamRips, Porn and Fake Files.
3. Forward The Last Message To Me With Quotes, I'll Add All The Files In That Channel To My DataBase."""
 
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used To Connect Bot To PM For Managing Filters. 
- It Helps To Avoid Spamming In Groups.

<b>NOTE:</b>
1. Only Admins Can Add a Connection.
2. Send <code>/connect</code> For Connecting Me To Your PM.

<b>Commands and Usage:</b>
• /connect  - <code>Connect a Particular Chat To Your PM</code>
• /disconnect  - <code>Disconnect From a Chat</code>
• /connections - <code>List All Your Connections</code>"""

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
- These Are The Extra Features Of Lucifer.

<b>Commands and Usage:</b>
• /id - <code>Get ID Of a Specified User.</code>
• /info  - <code>Get Information About a User.</code>
• /imdb  - <code>Get The Film Information From IMDB Source.</code>
• /search  - <code>Get The Film Information From Various Source.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
- This Module Only Works For My Admins.

<b>Commands and Usage:</b>
• /logs - <code>To Get The Rescent Errors.</code>
• /stats - <code>To Get Status Of Files In DataBase.</code>
• /delete - <code>To Delete a Specific File From DataBase.</code>
• /users - <code>To Get List Of My Users and ID.</code>
• /chats - <code>To Get List Of My Chats and ID.</code>
• /leave  - <code>To Leave From a Chat.</code>
• /disable  -  <code>To Disable a Chat.</code>
• /ban  - <code>To Ban a User.</code>
• /unban  - <code>To Unban a User.</code>
• /channel - <code>To Get List Of Total Connected Channels.</code>
• /broadcast - <code>To Broadcast a Message To All Users.</code>"""

    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Used Storage: <code>{}</code> MIB
★ Free Storage: <code>{}</code> MIB"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""

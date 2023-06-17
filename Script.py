class script(object):
    START_TXT = """Hello 👋 {},
    
My Name Is <a href=https://t.me/{}>{}</a>, I Can Provide Movies Just Add Me To Your Group and Enjoy 😍

Created By <a href=https://t.me/BKM_TG>𝙼𝚛.𝙱𝙺𝙼 𝚃𝙶</a> """

    HELP_TXT = """Hello 👋 {},
    
Here Is The Help For My Commands."""

    ABOUT_TXT = """✯ My Name: {}
✯ Creator: <a href=https://t.me/BKM_TG>Mr.BKM TG</a>
✯ Library: Pyrogram 
✯ Language: Python3
✯ DataBase: MongoDB
✯ Bot Server: Heroku
✯ Build Status: v1.0.1 [ BETA ]"""

    SOURCE_TXT = """<b>NOTE:</b>
    
- Lucifer Is a Open Source Project. 

- Source - <a href= https://github.com/Mr-BKM/Lucifer-RoBoT>Click Here</a> """

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter Is The Feature Were Users Can Set Automated Replies For a Particular Keyword and Lucifer Will Respond Whenever a keyword Is Found The Message 

<b>NOTE:</b>
1. Lucifer Should Have Admin Privillage.
2. Only Admin Filters In a Chat.
3. Alert Buttons Have a Limit Of 64 Characters.

<b>Commands and Usage:</b>
• /filter - <code>Add a Filter In Chat.</code>
• /filters - <code>List All The Filters Of a Chat.</code>
• /del - <code>Delete a Specific Filter In Chat.</code>
• /delall - <code>Delete The Whole Filters In a Chat.(Chat Owner Only)</code>"""


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
• /connect  - <code>Connect a Particular Chat To Your PM.</code>
• /disconnect  - <code>Disconnect From a Chat.</code>
• /connections - <code>List All Your Connections.</code>"""

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
    
    DISC_TXT = """
<b><code>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴꜱ, ꜱʜᴀʀᴇ, ᴏʀ ᴄᴏɴꜱᴜᴍᴇ, ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. </code>

🌿 ʙʏ : <a href='t.me/heartlesssn'>ᴄʀᴀᴢʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>"""
    
    SHIV_TXT = """
<b>ᴄʜᴏᴏꜱᴇ ꜰʀᴏᴍ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ</b>"""
    
    EARN2_TXT = """<b>ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴍᴏᴠɪᴇ-ʟᴏᴠᴇʀ's ᴘᴀʀᴀᴅɪsᴇ ᴏɴ ᴏᴜʀ ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ. ᴅɪᴠᴇ ɪɴᴛᴏ ᴀ ᴠᴀsᴛ ᴄᴏʟʟᴇᴄᴛɪᴏɴ ᴏꜰ ꜰɪʟᴍs sᴘᴀɴɴɪɴɢ ᴠᴀʀɪᴏᴜs ɢᴇɴʀᴇs, ꜰʀᴏᴍ ᴀᴄᴛɪᴏɴ-ᴘᴀᴄᴋᴇᴅ ʙʟᴏᴄᴋʙᴜsᴛᴇʀs ᴛᴏ ᴛʜᴏᴜɢʜᴛ-ᴘʀᴏᴠᴏᴋɪɴɢ ᴅʀᴀᴍᴀs. ᴡɪᴛʜ ᴜsᴇʀ-ꜰʀɪᴇɴᴅʟʏ ɴᴀᴠɪɢᴀᴛɪᴏɴ, ᴘᴇʀsᴏɴᴀʟɪᴢᴇᴅ ʀᴇᴄᴏᴍᴍᴇɴᴅᴀᴛɪᴏɴs, ᴀɴᴅ ᴅᴇᴛᴀɪʟᴇᴅ ᴍᴏᴠɪᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ, ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪs ʏᴏᴜʀ ɢᴏ-ᴛᴏ ᴅᴇsᴛɪɴᴀᴛɪᴏɴ ꜰᴏʀ ᴄɪɴᴇᴍᴀᴛɪᴄ ʙʟɪss. ᴊᴏɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ, sᴛᴀʏ ᴜᴘᴅᴀᴛᴇᴅ ᴡɪᴛʜ ᴛʜᴇ ʟᴀᴛᴇsᴛ ɴᴇᴡs, ᴀɴᴅ ɪɴᴅᴜʟɢᴇ ɪɴ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏꜰ ᴍᴏᴠɪᴇs ʟɪᴋᴇ ɴᴇᴠᴇʀ ʙᴇꜰᴏʀᴇ. ɢᴇᴛ ʀᴇᴀᴅʏ ꜰᴏʀ ᴀ ᴡᴏʀʟᴅ ᴏꜰ ᴜɴʟɪᴍɪᴛᴇᴅ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ ᴀᴛ ʏᴏᴜʀ ꜰɪɴɢᴇʀᴛɪᴘs!

ǫᴜᴀʟɪᴛɪᴇs ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ

♻️ ᴀʟʟ ᴏᴛᴛ ᴘʟᴀᴛꜰᴏʀᴍ ᴍᴏᴠɪᴇ ᴏɴ ᴏɴᴇ ᴘʟᴀᴄᴇ.
♻️ 5 ʟᴀᴄᴋ + ᴍᴏᴠɪᴇs ᴀʟʀᴇᴀᴅʏ ʜᴇʀᴇ
♻️ ꜰɪʀsᴛ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ɴᴇᴡ ʀᴇʟᴇᴀsᴇᴅ ᴍᴏᴠɪᴇ ᴅɪʀᴇᴄᴛ ᴠᴇᴅɪᴏ.
♻️ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ 50+ ᴍᴏᴠɪᴇ
♻️ 24/7 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ᴀʟsᴏ

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='t.me/heartlesssn'>ᴄʀᴀᴢʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>"""

    CRAZY_TXT = """<b>हमारे मूवीज चैनल पर परम मूवी-प्रेमी के स्वर्ग का अनुभव करें। एक्शन से भरपूर ब्लॉकबस्टर से लेकर विचारोत्तेजक ड्रामा तक, विभिन्न शैलियों में फैली फिल्मों के विशाल संग्रह में गोता लगाएँ। उपयोगकर्ता के अनुकूल नेविगेशन, व्यक्तिगत अनुशंसाओं और विस्तृत मूवी जानकारी के साथ, हमारा चैनल सिनेमाई आनंद के लिए आपकी पसंदीदा जगह है। हमारे समुदाय से जुड़ें, ताज़ा ख़बरों से अपडेट रहें, और फ़िल्मों के ऐसे जादू का आनंद लें जैसा पहले कभी नहीं हुआ। अपनी उंगलियों पर असीमित मनोरंजन की दुनिया के लिए तैयार हो जाइए! 

💯 हमारे चैनल के गुण 

♻️ सभी ओटी प्लेटफॉर्म मूवी एक ही जगह पर । 

♻️ 5 लाख + फिल्में पहले से ही यहां उपलब्ध हैं ।

♻️ सबसे पहले टेलीग्राम पर नई रिलीज़ हुई मूवी डायरेक्ट वीडियो फॉर्मेट में। 

♻️ रोजाना 50+ मूवी रोजाना अपलोड ।

♻️ 24/7 आपकी सहायता के लिए ग्रुप

🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='t.me/heartlesssn'>ᴄʀᴀᴢʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ</a></b>"""
    
    SHIVN_TXT = """
<b>ᴄʜᴏᴏꜱᴇ ʏᴏᴜʀ ʟᴀɴɢᴜᴀɢᴇ ꜰʀᴏᴍ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ</b>"""

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

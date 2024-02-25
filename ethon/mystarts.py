from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.url("🤖 ᴜᴘᴅᴀᴛᴇ", url="https://t.me/BihariBots"),
                               Button.url("🔍 sᴜᴘᴘᴏʀᴛ", url="https://t.me/Bihari_Anime")],
                              [Button.url("❣️ ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="t.me/God_Xiao_Yan")]])
                           
    
async def vc_menu(event):
    await event.edit("**VIDEO CONVERTOR v1.4**", 
                    buttons=[
                        [Button.inline("info.", data="info"),
                         Button.inline("SOURCE", data="source")],
                        [Button.inline("NOTICE.", data="notice"),
                         Button.inline("Main.", data="help")],
                        [Button.url("DEVELOPER", url="t.me/God_Xiao_Yan")]])
    

import feedparser
import webbrowser
import os
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import ImportChatInviteRequest

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

client = TelegramClient('teste_betting_bot', api_id, api_hash).start(bot_token=bot_token)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # ...or even to any username
    await client.send_message('thu_ilario', 'Testing Telethon!')


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')
    id = event.chat_id
    print(id)

# Group ID = -1002202130484
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
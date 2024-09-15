import os
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import ImportChatInviteRequest
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

client = TelegramClient('teste_betting_bot', api_id, api_hash).start(bot_token=bot_token)

read_messages_entity = None
send_messages_entity = None

@client.on(events.NewMessage(incoming=True, pattern='(?i)hello.+'))
async def print_chat_id(event):
    await event.reply('hi!')
    id = event.chat_id
    print(id)

@client.on(events.NewMessage(incoming=True, pattern='COPY.+'))
async def read_and_post_messages(event):
    if event.chat_id == -4588254743:
        await client.send_message(-1002202130484, event.raw_text)

# Group ID = -1002202130484 (molina)
# Group ID = -4588254743 (le mensagem)
with client:
    read_messages_entity = await client.get_entity(some_id)
    send_messages_entity = await client.get_entity(some_id)
    client.run_until_disconnected()
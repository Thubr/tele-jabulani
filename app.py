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

async def setup():
    global read_messages_entity
    global send_messages_entity
    read_messages_entity = await client.get_entity(-4588254743)
    send_messages_entity = await client.get_input_entity(-1002202130484)

@client.on(events.NewMessage(incoming=True, pattern='(?i)hello.+'))
async def print_chat_id(event):
    await event.reply('hi!')
    id = event.chat_id
    print(id)

@client.on(events.NewMessage(incoming=True, pattern='COPY.+'))
async def read_and_post_messages(event):
    if event.chat_id == -4588254743:
        await client.send_message(send_messages_entity, event.raw_text)

# Group ID = -1002202130484 (molina)
# Group ID = -4588254743 (le mensagem)
with client:
    client.loop.run_until_complete(setup())
    client.run_until_disconnected()
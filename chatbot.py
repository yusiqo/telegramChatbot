from pyrogram import Client
import random
import time
from os import getenv

from dotenv import load_dotenv

load_dotenv()
api_id = int(getenv("API_ID", "29990172"))
api_hash = getenv("API_HASH", "d76936ea313a140516435843f37959f3")
chat_id = int(getenv("CHAT_ID", "-1001907080749"))
session = getenv("SESSION", "d76936ea313a140516435843f37959f3")

app = Client(session, api_id, api_hash)

async def send_random_message():
    # İşleme geçmeden önce bir süre bekleyebilirsiniz
    while True:
        time.sleep(1)
        # Mesajı göndermek için özel bir koşul eklemeye gerek yok
        # Rastgele bir mesaj seçmek için:
        total_messages = await app.get_chat_history_count(chat_id)
        random_message_number = random.randint(1, total_messages)
    
    # Retrieve the random message
        selected_message = await app.get_messages(chat_id, random_message_number)
        try:
            await app.send_message(chat_id, selected_message.text)
        except:
            print("error")
# Bir mesaj gönderdikten sonra döngüyü sonlandır

with app:
    app.loop.run_until_complete(send_random_message())

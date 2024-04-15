import time

from pyrogram import Client

api_id = 29080736
api_hash = "1526c448a89b7799ccb140b1822b7344"

app = Client("my_account", api_id=api_id, api_hash=api_hash)
pump_chat_id = 5577171870


async def main():
    async with app:
        while True:
            message = await app.send_photo(
                pump_chat_id,
                "https://dogatebee.com/dab.webp",
                caption="DogAteBee - $DAB\nI'm literally just a dog that ate a bee. smfh.",
            )
            print(
                f"{time.asctime()} — Sent message {message.id} to chat {pump_chat_id}"
            )
            time.sleep(60)


app.run(main())

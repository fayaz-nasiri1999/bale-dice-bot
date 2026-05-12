import requests
import random
import time

TOKEN = "641528681:mgE94zVRHfJNBTp5LTJhyV36JuWnsdHiBG4"
URL = f"https://tapi.bale.ai/bot{TOKEN}"

offset = 0

print("Bot is running...")

while True:
    try:
        response = requests.get(
            f"{URL}/getUpdates?offset={offset}",
            timeout=30
        )

        updates = response.json()

        for update in updates.get("result", []):

            offset = update["update_id"] + 1

            # فقط پیام‌های معمولی پردازش شوند
            if "message" not in update:
                continue

            message = update["message"]

            # اگر متن نداشت رد شود
            if "text" not in message:
                continue

            chat_id = message["chat"]["id"]
            text = message["text"]

            # دستور start
            if text == "/start":
                requests.post(
                    f"{URL}/sendMessage",
                    json={
                        "chat_id": chat_id,
                        "text": "سلام 👋\nبه ربات تاس خوش اومدی.\nهر پیامی بفرستی برات تاس میندازم 🎲"
                    }
                )
                continue

            # تولید عدد تاس
            dice = random.randint(1, 6)

            requests.post(
                f"{URL}/sendMessage",
                json={
                    "chat_id": chat_id,
                    "text": f"🎲 عدد تاس: {dice}"
                }
            )

    except Exception as e:
        print("ERROR:", e)

    time.sleep(1)


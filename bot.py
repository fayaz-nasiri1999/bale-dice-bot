import requests
import random

TOKEN = "641528681:mgE94zVRHfJNBTp5LTJhyV36JuWnsdHiBG4"
URL = f"https://tapi.bale.ai/bot{TOKEN}"
offset = 0

while True:
    updates = requests.get(f"{URL}/getUpdates?offset={offset}").json()

    for update in updates.get("result", []):
        offset = update["update_id"] + 1
        chat_id = update["message"]["chat"]["id"]

        dice = random.randint(1, 6)

        requests.post(f"{URL}/sendMessage", json={
            "chat_id": chat_id,
            "text": f"🎲 عدد تاس: {dice}"
        })


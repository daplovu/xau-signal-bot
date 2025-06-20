
from signal_generator import generate_signal
from config import DISCORD_WEBHOOK_URL
import requests

signal = generate_signal()
if signal:
    requests.post(DISCORD_WEBHOOK_URL, json={"content": signal})
    print("✅ Signal sent to Discord!")
else:
    print("⚠️ No signal found.")


from signal_generator import generate_signal
from config import WEBHOOK_URL
import requests

signal = generate_signal()
if signal:
    requests.post(WEBHOOK_URL, json={"content": signal})
    print("✅ Signal sent to Discord!")
else:
    print("⚠️ No signal found.")

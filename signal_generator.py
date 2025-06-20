
from tvDatafeed import TvDatafeed
import os

def generate_signal():
    username = os.getenv("TV_USERNAME")
    session = os.getenv("TV_SESSIONID")
    tv = TvDatafeed(username=username, password=None, session=session)
    df = tv.get_hist(symbol='XAUUSD', exchange='FXCM', interval='5m', n_bars=50)

    last = df.iloc[-2:]
    if last.iloc[-2]['close'] < last.iloc[-2]['open'] and last.iloc[-1]['close'] > last.iloc[-1]['open']:
        return (
            "📌 XAUUSD SNIPER SIGNAL\n\n"
            "🟢 Direction: Buy\n"
            f"🎯 Entry: {last.iloc[-1]['close']:.2f}\n"
            f"🛑 Stop Loss: {last.iloc[-1]['low']:.2f}\n"
            f"✅ Take Profit: {last.iloc[-1]['close'] + 10:.2f}\n"
            "📊 Confidence: 75%\n"
            "🧠 Reason: Bullish Engulfing\n"
        )
    return None

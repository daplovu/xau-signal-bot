
from libs.tvdatafeed.tvDatafeed import TvDatafeed
import os

def generate_signal():
    username = os.getenv("TV_USERNAME")
    session = os.getenv("TV_SESSIONID")
    tv = TvDatafeed(username=username, session=session)
    df = tv.get_hist(symbol='XAUUSD', exchange='FXCM', interval='5m', n_bars=3)

    if df.iloc[-2]['close'] < df.iloc[-2]['open'] and df.iloc[-1]['close'] > df.iloc[-1]['open']:
        return (
            "📌 XAUUSD SNIPER SIGNAL\n\n"
            "🟢 Direction: Buy\n"
            f"🎯 Entry: {df.iloc[-1]['close']:.2f}\n"
            f"🛑 Stop Loss: {df.iloc[-1]['low']:.2f}\n"
            f"✅ Take Profit: {df.iloc[-1]['close'] + 10:.2f}\n"
            "📊 Confidence: 75%\n"
            "🧠 Reason: Bullish Engulfing\n"
        )
    return None


import requests
import pandas as pd

class TvDatafeed:
    def __init__(self, username=None, password=None, session=None):
        self.username = username
        self.session = session
    def get_hist(self, symbol, exchange, interval, n_bars=50):
        # dummy data untuk test (replace dengan yang asli nanti)
        import pandas as pd
        import datetime
        now = datetime.datetime.now()
        data = {
            'open': [2330, 2331, 2332],
            'high': [2332, 2333, 2335],
            'low': [2328, 2329, 2330],
            'close': [2331, 2330, 2333],
        }
        return pd.DataFrame(data, index=[now, now, now])

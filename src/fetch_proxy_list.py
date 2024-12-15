from io import StringIO

import pandas as pd
import requests

URL = "https://free-proxy-list.net/"
HEADER = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}

response = requests.get(URL, headers=HEADER)

data = pd.read_html(StringIO(response.text))

data_proxies = data[0]

data_proxies = data_proxies.assign(
    proxy="http://"
    + data_proxies["IP Address"]
    + ":"
    + data_proxies["Port"].astype(str)
)

data_proxies["proxy"].to_csv("./scrapy_pokedex/proxies.txt", index=False, header=None)

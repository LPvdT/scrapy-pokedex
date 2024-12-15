from io import StringIO

import pandas as pd
import requests


def fetch_proxy_list(url: str, headers: dict[str, str]) -> requests.Response:
    """Fetch proxy list from the given URL with the provided headers"""

    response = requests.get(url, headers=headers)

    return response


def extract_proxy_data(response: requests.Response) -> pd.DataFrame:
    """Extract proxy data from the response"""

    response_data = pd.read_html(StringIO(response.text))[0]

    return response_data


def process_proxy_data(proxy_data: pd.DataFrame) -> pd.DataFrame:
    """Process proxy data and create a new column with the proxy URL"""

    proxy_data["proxy"] = (
        "http://"
        + proxy_data["IP Address"].astype(str)
        + ":"
        + proxy_data["Port"].astype(str)
    )

    return proxy_data


def save_proxy_data(proxy_data: pd.DataFrame, filename: str) -> None:
    """Save proxy data to a file"""

    proxy_data["proxy"].to_csv(filename, index=False, header=None)


def main() -> None:
    url = "https://free-proxy-list.net/"
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
    headers = {"User-Agent": user_agent, "X-Requested-With": "XMLHttpRequest"}
    filename = "proxies.txt"

    response = fetch_proxy_list(url, headers)
    proxy_data = extract_proxy_data(response)
    proxy_data = process_proxy_data(proxy_data)
    save_proxy_data(proxy_data, filename)


if __name__ == "__main__":
    main()

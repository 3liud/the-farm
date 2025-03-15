import pandas as pd
import requests

apis = {
    "counties": "https://statistics.kilimo.go.ke/en/kilimostat-api/counties/",
    "institutions": "https://statistics.kilimo.go.ke/en/kilimostat-api/institutions/",
    "subsectors": "https://statistics.kilimo.go.ke/en/kilimostat-api/subsectors/",
    "domains": "https://statistics.kilimo.go.ke/en/kilimostat-api/domains/",
    "subdomains": "https://statistics.kilimo.go.ke/en/kilimostat-api/subdomains/",
    "elements": "https://statistics.kilimo.go.ke/en/kilimostat-api/elements/",
    "itemcategories": "https://statistics.kilimo.go.ke/en/kilimostat-api/itemcategories/",
    "items": "https://statistics.kilimo.go.ke/en/kilimostat-api/items/",
    "units": "https://statistics.kilimo.go.ke/en/kilimostat-api/units/",
    "kilimodata": "https://statistics.kilimo.go.ke/en/kilimostat-api/kilimodata/",
}


def fetch_data(url, timeout=30):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return pd.DataFrame(response.json())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return pd.DataFrame()


def extract_all():
    data = {}
    for name, url in apis.items():
        df = fetch_data(url)
        if df.empty:
            print(f"Warning: {name} data is empty!")
        data[name] = df
    return data


if __name__ == "__main__":
    data_dict = extract_all()
    for key, df in data_dict.items():
        print(f"{key} fetched: {len(df)} records.")

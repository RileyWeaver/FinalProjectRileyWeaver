import requests

def get_ddragon_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()[0]

def fetch_champions():
    """Download full champion list (with stats) for the latest version."""
    version = get_ddragon_version()
    url     = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    resp    = requests.get(url)
    resp.raise_for_status()
    payload = resp.json()["data"]         # dict keyed by champion key

    champions = []
    for champ in payload.values():
        champ["version"] = version        # so template can do {{ champ.version }}
        champions.append(champ)
    return champions

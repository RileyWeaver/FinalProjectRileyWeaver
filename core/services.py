import requests

def get_ddragon_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.json()[0]

def fetch_champions():
    version = get_ddragon_version()
    url     = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    resp    = requests.get(url)
    resp.raise_for_status()
    payload = resp.json()["data"]

    champions = []
    for champ in payload.values():
        champ["version"] = version
        champions.append(champ)
    return champions

def fetch_champion_detail(key):
    # first grab the latest version again
    version = get_ddragon_version()
    url     = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{key}.json"
    resp    = requests.get(url)
    resp.raise_for_status()
    # Riot returns { "data": { "<key>": { … } } }
    return resp.json()["data"][key]

import requests

#This retrieves the katest data dragon from teh riot's CDN and constructs URLs for champion data
def get_ddragon_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    resp = requests.get(url)
    resp.raise_for_status() #Error handling in case of failure
    return resp.json()[0] #return the latest version in list

#fetches complete list of champions from Data Dragon
def fetch_champions():
    version = get_ddragon_version() #Find version
    # Build URL for champion master JSON
    url     = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    resp    = requests.get(url)
    resp.raise_for_status()
    payload = resp.json()["data"] #JSON is top-level object mapping for champions

    champions = []
    # Each champion entry, get version and collect into list
    for champ in payload.values():
        champ["version"] = version
        champions.append(champ)
    return champions

# fetches detail data for a single champion, dealing with spells and lore
def fetch_champion_detail(key):
    # first grab the latest version again
    version = get_ddragon_version()
    #Build specific champion JSON
    url     = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion/{key}.json"
    resp    = requests.get(url)
    resp.raise_for_status()

    return resp.json()["data"][key] #returns detailed champion data for the key

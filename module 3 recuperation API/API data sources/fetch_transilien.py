import requests
import pandas as pd


def fetch_transilien(ligne_train=None):
    url = "https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/comptage-voyageurs-trains-transilien/records"
    
    params = {"limit": 100, "offset": 0}
    
    if ligne_train:
        params["where"] = f'ligne="{ligne_train}"'
    
    # Premier appel pour récupérer total_count
    response = requests.get(url, params=params)
    data = response.json()
    total_count = data["total_count"]
    results = data["results"]
    
    # Pagination
    while params["offset"] + 100 < total_count:
        params["offset"] += 100
        response = requests.get(url, params=params)
        results.extend(response.json()["results"])
    
    return pd.DataFrame(results)
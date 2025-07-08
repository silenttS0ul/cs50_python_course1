
import requests

def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    except requests.HTTPError:
        print("Could not complete request!")    
    content = response.json()
    for artwork in content["data"]:
        print(f"*{artwork['title']}")





main()

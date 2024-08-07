import requests

if __name__ == '__main__':
    url = "https://ahrefs1.p.rapidapi.com/v1/keyword-generator/amazon"

    querystring = {"keyword": "keyword research", "country": "us"}

    headers = {
        "x-rapidapi-key": "fb6124e646msheb8c9d8bc5e44d4p1afcc3jsn1d7a6fd7f80c",
        "x-rapidapi-host": "ahrefs1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())
import requests

url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"US","topic":"ENTERTAINMENT"}

headers = {
    'x-rapidapi-key': "<API_URL>",
    'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


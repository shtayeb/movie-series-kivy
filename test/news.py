import requests

url = "https://google-news.p.rapidapi.com/v1/topic_headlines"

querystring = {"lang":"en","country":"US","topic":"ENTERTAINMENT"}

headers = {
    'x-rapidapi-key': "ef08742670msh47b686485cc7085p1f3af6jsn8877ae9469af",
    'x-rapidapi-host': "google-news.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)


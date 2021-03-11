movies = {}
import json, requests
baseurl = "http://omdbapi.com/?t=scream&apikey=36fb159c" #only submitting the title parameter
response = requests.get(baseurl)
if response.status_code == 200:
        data = response.text    
        movies = json.loads(data)
        print (movies)
else:
    print("Bad Request")


class imdb():
        
        def search_title(self,title):
                movies = {}
                import json, requests
                baseurl = 'http://omdbapi.com/?s='+title+'&plot=full&apikey=36fb159c' #only submitting the title parameter
                response = requests.get(baseurl)
                if response.status_code == 200:
                        data = response.text    
                        movies = json.loads(data)
                        return movies
                else:
                        print("Bad Request")
                        return "Connection Error !"


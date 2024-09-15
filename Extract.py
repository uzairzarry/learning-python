import requests
class API():
    def __init__(self,baseurl,endpoints) -> None:
        self.baseurl = baseurl
        self.endpoints = endpoints

    def get(self):
        try:
            url = f"{self.baseurl}/{self.endpoints}"
            response =  requests.get(url)
            response.raise_for_status() 
            return response.json
        except requests.exceptions.RequestException as e:
            pass
        


ins1 = API('anyanyany' , 'endpointxyz')
ins1.get()

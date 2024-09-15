import requests
def getRequest(*args,**kwargs):
    body,other = kwargs.get('body'),kwargs.get('other')
    
    url,endpoint = args
    
    
    response=requests.post(url+endpoint,json=body)
    print(response.json())


# arguments
url='https://uzairzarry.pythonanywhere.com/api'
endpoint='/login/'
body={
    'email':'uzairmushtaq1@gmail.com',
    'password':'error404'
}
other={}
getRequest(url,endpoint,body=body,other=other)

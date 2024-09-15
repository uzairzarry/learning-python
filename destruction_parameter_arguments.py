import requests
def getRequest(*args,**kwargs):
    body,other = kwargs.get('body'),kwargs.get('other')
    
    url,endpoint = args
    
    try:
        response=requests.post(url+endpoint,json=body)
        print(response.json())
    except Exception as e:
        print(e)

# arguments
url='https://loremlorem.com/api'
endpoint='/login/'
body={
    'email':'test1@gmail.com',
    'password':'test'
}
other={}
getRequest(url,endpoint,body=body,other=other)

import requests

class HTTPS:
    def responsePost(self,request):
        return requests.post(request["url"], data = request["parameters"])
    def responseGet(self,request):
        return requests.get(request["url"], params = request["parameters"], headers = request["token"])
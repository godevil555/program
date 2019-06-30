import requests
import os
import json
############## IP location
def check_ip():
    os.system('reset')
    location = requests.get('http://ip-api.com/json/')
    data = json.loads(location.text)
    print("IP : "+ str(data['query'])+"\ncountry : "+data['country']+"\nCity : "+ data['city'])




############i
#check_ip()
def check_tor_install():
    os.system(

#%%

import requests

def create_task(text):
    url = "http://localhost:5000/add_task/{}".format(text)
    response = requests.put(url)
    print(response.json())

def complete_task(text):
    url = "http://localhost:5000/complete_task/{}".format(text)
    response = requests.post(url)
    print(response.json())
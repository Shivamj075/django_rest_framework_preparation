# This is any 3rd party app which wants adata from api

import requests

URL = "http://127.0.0.1:8000/stuinfo/3"

r = requests.get(url = URL)

data = r.json()

print(data)
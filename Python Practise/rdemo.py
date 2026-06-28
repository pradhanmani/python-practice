
import requests


# payload = {'username':'corey', 'password': 'testing' }

r = requests.get('https://httpbin.org/delay/6',timeout=3)

# r_dict = r.json()
print(r)






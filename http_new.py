import requests

req = requests.request('GET', 'http://api.github.com/users/daisyndungu')
print (req.json)

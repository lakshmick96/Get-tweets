import sys
import requests
from requests_oauthlib import OAuth1

handle = sys.argv[1]
api = { 
		'Access token secret': 'gLl1jA5VuBonxpBnBBST6bz8rCTqN3E61xaX4MgXlheiy', 
                'API secret': 'SA3Gc0WzYMZZKZAprxgra0w0jH45p0ruqaRQNKhq3KMiIp2ahd', 
		'Access token': '618136745-5KlnXaU9ftalPUbdFm9WNlow1qh3N10iCsNQd6Zx', 
		'API Key': 'legBa7cVponDoNITc0oJ2MjxV'  
	      }
conn = OAuth1(
    api['API Key'],
    api['API secret'],
    api['Access token'],
    api['Access token secret'])

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
params = {'screen_name': handle, 'count':10}
results = requests.get(url, params=params, auth=conn)
for i in results.json():
	print i['text']




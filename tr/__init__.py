import requests
api = 'http://localhost:5000'
print('HTTP GET Request (text):')
response = requests.get(api + '/get/text')
print('Response: ', response.text)
print(111111111111111111111111)
print('HTTP POST Request (text):')
response = requests.post(api + '/post/text', 'hmmm')
print('Response: ', response.text)

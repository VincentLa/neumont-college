import requests

# Cat Facts
url = 'https://cat-fact.herokuapp.com/facts'
req = requests.get(url)

print(req.status_code)
print(req.text)

url = 'https://superheroapi.com/api/4034744783204480/644/powerstats'
req = requests.get(url)

print(req.status_code)
print(req.text)

# Example of using google translate with headers and a payload
# You have to get a valid api key and account

# url = 'https://google-translate1.p.rapidapi.com/language/translate/v2'
# headers = {
#     'content-type': 'application/x-www-form-urlencoded',
#     'x-rapidapi-key':'[API_KEY]',  
#     'x-rapidapi-host':'movie-database-imdb-alternative.p.rapidapi.com', 
#     'userQueryString':'true'}
# payload = {	
#     'q': 'Hello, world!',
# 	'source': 'en',
# 	'target': 'es'}
# req = requests.post(url, headers=headers, params=payload)

# print(req.text)
import requests

headers = {
    'User-Agent': 'Mozilla/5.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://techurls.com',
    'Referer': 'https://techurls.com/'
}

data = {
    'site': 'hackernews',
    'interval': 'latest',
    'last_id': '1089324',
    'load_more': 'true',
    'u': '2',
    'v': '194334'
}

response = requests.post('https://techurls.com/api/get_titles', 
                        headers=headers,
                        data=data)

print(response.json())

import requests

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://techurls.com",
    "Referer": "https://techurls.com/",
}

data = {"site": "hackernews", "interval": "latest", "u": "2", "v": "194334"}

response = requests.post(
    "https://techurls.com/api/get_titles", headers=headers, data=data
)

if response.status_code == 200:
    stories = response.json()
    print(stories)
    if stories["status"] == "success":
        newest_id = stories["data"][0]["id"]
        print(f"Newest ID: {newest_id}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)

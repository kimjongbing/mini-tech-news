from fastapi import FastAPI

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


app = FastAPI()


@app.get("/")
async def root():
    if response.status_code == 200:
        stories = response.json()
        return(stories)
    else:
        return(f"Error: {response.status_code}, {response.text}")

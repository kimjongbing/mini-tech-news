from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from datetime import datetime, timezone
import requests

router = APIRouter()


def fetch_stories(last_id=None):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://techurls.com",
        "Referer": "https://techurls.com/",
    }

    data = {"site": "hackernews", "interval": "latest"}

    if last_id:
        data["load_more"] = "true"
        data["last_id"] = str(last_id)

    response = requests.post(
        "https://techurls.com/api/get_titles", headers=headers, data=data
    )
    return response.json()


def format_time_ago(date_str):
    dt = datetime.strptime(date_str, "%Y-%m-%d %I:%M:%S%p UTC").replace(
        tzinfo=timezone.utc
    )
    delta = datetime.now(timezone.utc) - dt
    hours = delta.total_seconds() / 3600
    return f"{int(hours)}h ago"


@router.get("/api/feeds/hackernews", response_class=HTMLResponse)
async def hackernews_feed(request: Request, last_id: str = None):
    stories = fetch_stories(last_id)

    if stories["status"] != "success":
        return ""

    html = ""
    for story in stories["data"]:
        html += f"""
       <article class="story">
           <div class="story-header">
               <div>
                   <h2 class="story-title">
                       <a href="{story['url']}" target="_blank">{story['title']}</a>
                   </h2>
                   <div class="story-meta">
                       <span class="source source-hn">hackernews</span>
                       <span>{story['url'].split('/')[2]}</span>
                       <span>{format_time_ago(story['date'])}</span>
                       <a href="{story['comment_url']}" target="_blank">comments</a>
                   </div>
               </div>
           </div>
       </article>
       """

    if stories["data"]:
        last_story = stories["data"][-1]
        html += f"""
       <button 
           hx-get="/api/feeds/hackernews?last_id={last_story['id']}" 
           hx-target="this"
           hx-swap="outerHTML"
           class="load-more">
           Load More
           <span class="htmx-indicator">Loading...</span>
       </button>
       """

    return html

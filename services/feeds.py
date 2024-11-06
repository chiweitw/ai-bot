import requests

def fetch_feeds():
    url = "https://feed-api.llama.fi/tweets"
    response = requests.get(url)

    if response.status_code == 200:
        feeds = response.json()[:5]
        for feed in feeds:  
            content = feed['tweet']
            url = feed['url']
            user_name = feed['user_name']
            user_handle = feed['user_handle']
            user_icon = feed['user_icon']
            return f"*{user_name} (@{user_handle})*\n{content}\n[Read more]({url})"
    return None
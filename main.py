import os
import feedparser
import requests

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHANNEL_ID = '@your_channel_username'  # Замініть на назву вашого каналу

RSS_FEEDS = [
    'https://techcrunch.com/feed/',
    'https://www.sciencealert.com/rss',
    'http://feeds.bbci.co.uk/news/world/rss.xml'
]

posted_links = set()

def send_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHANNEL_ID, 'text': text, 'parse_mode': 'HTML'}
    requests.post(url, data=data)

def fetch_and_post():
    for feed_url in RSS_FEEDS:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            if entry.link not in posted_links:
                message = f"<b>{entry.title}</b>\n{entry.link}"
                send_message(message)
                posted_links.add(entry.link)

if __name__ == '__main__':
    fetch_and_post()
import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://time.com/"
contents = urllib.request.urlopen(url).read()
soup = BeautifulSoup(contents, 'html.parser')
latest_stories_div = soup.find('div', {'class': 'partial latest-stories'})
stories = [{'title': story.text.strip(), 'link': url + story.get('href') if story.get('href') and not story.get('href').startswith("http") else story.get('href')} for story in latest_stories_div.find_all('a')]
print(json.dumps(stories, indent=4))

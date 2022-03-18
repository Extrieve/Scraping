import requests
from bs4 import BeautifulSoup


url = 'https://www.reddit.com/'
website = requests.get(url).text

soup = BeautifulSoup(website, 'html.parser')

for post in soup.find_all('div', class_='_1poyrkZ7g36PawDueRza-J'):
    text = post.h3.text
    subreddit = post.find_all('a', class_='_3ryJoIoycVkA88fy40qNJc')
    subreddit = str(subreddit)

    try:
        index = subreddit.index('/r/') + 3
        end = subreddit[index+3:].index('/') + index + 3
        print(index, end)
        # print(end)
        mysub = subreddit[index:end]
        print(f'{text}\n{mysub}\n')
    except ValueError:
        pass

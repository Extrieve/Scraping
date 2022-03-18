from bs4 import BeautifulSoup
import requests
from datetime import datetime


def time_conversion(time):
    hour = int(time[:2])
    conversion = hour % 12

    if hour == 24:
        return f'{conversion}{time[2:]} AM'
    elif hour == 12:
        return time + ' PM'

    if conversion != int(time[:2]):
        time = f'{conversion}{time[2:]} PM'
        return time
    return time + ' AM'


usf_site = requests.get(
    'https://usf.campusdish.com/LocationsAndMenus/Tampa').text
soup = BeautifulSoup(usf_site, 'html.parser')
now = datetime.now()
current_time = now.strftime('%H:%M:%S')
counter = 0
for item in soup.text:
    if 'open' in item.lower():
        counter += 1

all_restaurants = soup.find_all('li')
restaurant_names = []
cur_status = []
for restaurant in all_restaurants:
    current = restaurant.find('a', 'card-link meta-data-tag')
    status = restaurant.find('div', 'location__status')
    try:
        # print(current.get_text())
        # print(status)
        name = current.get_text().replace("'", "").replace('"', "")
        restaurant_names.append(name)
    except AttributeError:
        pass

print(restaurant)

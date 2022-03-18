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


usf_site = requests.get('https://usf.campusdish.com/LocationsAndMenus/Tampa').text

soup = BeautifulSoup(usf_site, 'html.parser').prettify()
now = datetime.now()
current_time = now.strftime('%H:%M:%S')

all_restaurants = soup.find_all('li')
open_restaurants = []

for restaurant in all_restaurants:
    rest = restaurant.find('div')
    span = restaurant.get_text('span')
    a = restaurant.get_text('a')
    open_restaurants.append(span.replace('\t','').replace('\n','').replace('\r', ''))

# print(open_restaurants)


    # span = rest.find('span')
    # print(span)
    # if 'open' in span.lower():
    #     # print(a)
    #     print(span)

# for resturant in all_restaurants:
#     if 'Panda' in str(resturant):
#         index = str(resturant).index('hop')
#         rest = str(resturant)[index:index+50]
#         print(rest)
        # print(resturant.find('div', class_='location__times'))
        # my_res = str(resturant.find('div', class_='location__times'))

        # if my_res:
        #     specs.append(my_res)

# print(specs)

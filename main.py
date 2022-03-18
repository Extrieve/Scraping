from bs4 import BeautifulSoup

with open('home.html') as file:
    content = file.read()

    # Making an instance of the Soup
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')

    course_info = dict()
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        course_info[course_name] = course_price

    print(course_info)

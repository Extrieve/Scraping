import requests
from bs4 import BeautifulSoup

website = requests.get(
    'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=2&startPage=1').text

soup = BeautifulSoup(website, 'lxml')

job_postings = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
recent_jobs = []

no_skills = input('>')
no_skills = [item for item in no_skills.split(',')]
print(no_skills)
for job in job_postings:
    parsed_posting = []
    aptitude = True
    company = job.find(
        'h3', class_='joblist-comp-name').text.replace('\n', '').replace('\r', '').replace(' ', '')

    title = job.find('a').text.replace('\n', '').replace('\r', '')

    skills = job.find('span', class_='srp-skills').text.replace('\n',
                                                                '').replace('\r', '').replace(' ', '')
    skills = skills.replace(',', ', ')
    parsed_posting += company, title, skills
    if 'few days' in job.text:
        for skill in skills.split(','):
            if skill in no_skills:
                aptitude = False
        if aptitude:
            recent_jobs.append(parsed_posting)

for item in recent_jobs:
    print(
        f'Company Name: {item[0]}\nPosition Title: {item[1]}\nSkills: {item[-1]}\n')

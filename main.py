from bs4 import BeautifulSoup
import requests
import time
import os

print(f'Input the skills you are not familiar with...')
unfamiliar_skills = input('>')
print(f'Filtering out...{unfamiliar_skills}')
post_number = 1

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        post_time = job.find('span', class_='sim-posted').text
        if 'few' in post_time:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'post_{post_number}/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()}\n')
                    f.write(f'Skiils: {skills.strip()}\n')
                    f.write(f'More info: {more_info}\n')
                    print(f'{index} loaded')

if __name__ == '__main__':
    while True:
        os.mkdir(f'post_{post_number}')
        find_jobs()
        time.sleep(10)
        post_number += 1
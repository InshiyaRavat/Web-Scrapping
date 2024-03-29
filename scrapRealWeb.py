from bs4 import BeautifulSoup
import requests
import time

print("enter the skill that you want to search job for: ")
job_search = input(">")
print("put some string that youare unfamiliar with: ")
unfamiliar_skill = input(">")
print(f'Filtering out {unfamiliar_skill}')
#to get specific info from a website
def find_jobs():
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={job_search}&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    #enumerate allows us to iterate over the index of job list and also over the job content
    for index , job in enumerate(jobs):
        published_date = job.find('span',class_ = 'sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3',class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'Company Name : {company_name.strip()} \n')
                    f.write(f'Required Skills : {skills.strip()} \n')
                    f.write(f'More Info : {more_info}')
                print(f'File Saved : {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
from bs4 import BeautifulSoup

#allows to open a file and then read content of that sepcific file
with open("index.html","r") as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course_cards = soup.find_all('div' , class_ = 'course-wrapper')
    for course in course_cards:
        course_name = course.h1.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')

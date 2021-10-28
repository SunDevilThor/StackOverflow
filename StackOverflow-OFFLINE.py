# Offline file for StackOverflow.py

from bs4 import BeautifulSoup

file = open('StackOverflow.html')

soup = BeautifulSoup(file, 'html.parser')

questions = soup.find_all('div', class_= 'summary')

for item in questions: 
    question = {
        'title': item.find('h3').text,
        'link': 'http://stackoverflow.com' + item.find('a', class_= 'question-hyperlink')['href'],
        'date': item.find('span', class_='relativetime')['title'],
    }
    print(question)

# Stack Overflow Function
# Tutorial from John Watson Rooney YouTube channel

import requests 
from bs4 import BeautifulSoup
from requests.api import head
import pandas as pd

question_list = []

def get_questions(tag, page):
    url = f'https://stackoverflow.com/questions/tagged/{tag}?tab=Active&page={page}&pagesize=50' 
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    questions = soup.find_all('div', class_= 'summary')

    for item in questions: 
        question = {
            'tag': tag,
            'title': item.find('h3').text,
            'link': 'http://stackoverflow.com' + item.find('a', class_= 'question-hyperlink')['href'],
            'date': item.find('span', class_='relativetime')['title'],
        }

        question_list.append(question)

    return

for x in range(1, 5):
    print(f'Getting page: {x}')
    get_questions('python', x)
    get_questions('webscraping', x)
    get_questions('beautifulsoup', x)

def output():
    df = pd.DataFrame(question_list)
    print(df.head())
    df.to_csv('StackOverflow-Questions.csv')
    print('Saved items to CSV file.')

output()
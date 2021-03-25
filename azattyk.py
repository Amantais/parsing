import requests
from bs4 import BeautifulSoup
import csv 

def get_html(url):
    response = requests.get(url)
    return response.text 

def get_all_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find('div', class_='row').find_all('div', class_='media-block')
    links = []

    for td in tds:
        catched_url = td.find('a').get('href')
        link = 'https://www.azattyk.org/' + catched_url
        links.append(link)
    return links


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        title = soup.find('h1', class_='title pg-title').text.strip()
    except:
        title = ''
    try:
        description = soup.find('div', class_='intro m-t-md').find('p').text.strip()
    except:
        description = ''
    try:
        date = soup.find('span', class_='date').text.strip()
    except:
        date = ''
    data = {'title': title, 'description': description, 'date': date}
    return data 


def write_csv(data):
    with open('azattyk.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['title'],data['description'],data['date']))
        print(data['title'],data['description'],data['date'])

def main():
    url = 'https://www.azattyk.org/z/20111'
    all_links = get_all_links(get_html(url))
    for url in all_links:
        html = get_html(url)
        data = get_page_data(html)
        write_csv(data)

if __name__ == '__main__':
    main()
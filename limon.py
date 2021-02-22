import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)
    return response.text 


def get_all_links(html):
    soup = BeautifulSoup(html,'html.parser')
    tds = soup.find('div', class_='lastnewsblock').find_all('div', class_='col-md-6 item item-list')
    links = []

    for td in tds:
        catched_url = td.find('a').get('href')
        link = 'https://limon.kg' +  catched_url
        links.append(link)
    return links



def get_page_data(html):
    soup = BeautifulSoup(html,'html.parser')
    try:
        title = soup.find('h1', class_='title').text.strip()
    except:
        title = ''
    try: 
        description = soup.find('div', id='newstext').find('p').text.strip()
    except:
        description = ''
    try:
        date = soup.find('div', class_='date').text.strip()
    except:
        date = ''

    data = {'title': title, 'description': description, 'date': date}
    return data



def write_csv(data):
    with open('limon.csv','a') as file:
        writer = csv.writer(file)
        writer.writerow((data['title'],data['date'],data['description']))
        print(data['title'],data['date'],data['description'])



def main():
    url = 'https://limon.kg/' 
    all_links = get_all_links(get_html(url))
    for url in all_links:
        html = get_html(url)
        data = get_page_data(html)
        write_csv(data)
   

if __name__ == "__main__":
    main()
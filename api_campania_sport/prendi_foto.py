import pandas as pd
import requests
from bs4 import BeautifulSoup

def start():
    df = pd.DataFrame(columns=["title", "summary", "image_url", "text", "date"])

    r = requests.get('http://www.campaniasport.it/?s=')

    soup = BeautifulSoup(r.content, 'html.parser')
    number_of_pages = int(soup.find('span', class_="pages").text.split(' ')[-1])

    all_links = []

    for n in range(10):
        print(n)
        if n != 0:
            r = requests.get(f"http://www.campaniasport.it/page/{n}/?s")

        soup = BeautifulSoup(r.content, 'html.parser')

        for elem in soup.findAll("h3", class_="entry-title td-module-title"):
            all_links.append(elem.findAll('a')[0].attrs['href'])

        n = n + 1

    # ciclo su ogni link e  compongo il diz dell'articolo: titolo, body, image_url
    all_links=list(set(all_links))
    for link in all_links:
        try:
            print(link)
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'html.parser')

            body = soup.find('div', class_="td-post-content tagdiv-type").text
            try:
                image_url = get_image_url(soup.find('div', class_="postie-attachments"))
            except:
                image_url="https://th.bing.com/th/id/OIP.gnUTTRvGWBshUURB5OBkhQHaHa?pid=ImgDet&rs=1"
            date_article=soup.find('time', class_="entry-date updated td-module-date").text
            datetime_article=change_date(date_article)
            body = body.replace('\n', '').replace('\u200b', '')
            title = soup.find('title').text
            title = title.replace('| Campania Sport', '')
            article = {'title': title, 'body': body, 'image_url': image_url, 'date_article':datetime_article}
            print(article)
            df = df.append({"title": title, "image_url": image_url, "text": body, 'date_article':datetime_article}, ignore_index=True)
            #https://stackoverflow.com/questions/34425607/how-to-write-a-pandas-dataframe-to-django-model


        except:
            continue

    #TODO: inserire il codice necessario al popolare il db sql
    print("ECCOLO")
    print(df)
    df = df.sort_values(by='date_article', ascending=False)


def get_image_url(soup):
    soup_like_string=str(soup)
    image_url=soup_like_string.split('data-orig-file=')[1].split(' ')[0]
    return image_url

def change_date(date_article):
    from datetime import datetime

    date_article=date_article.split(' ')[1:]
    if date_article[1].lower() == 'gennaio':
        month='1'
    elif date_article[1].lower() == 'febbraio':
        month='2'
    elif date_article[1].lower() == 'marzo':
        month='3'
    elif date_article[1].lower() == 'aprile':
        month='4'
    elif date_article[1].lower() == 'maggio':
        month='5'

    elif date_article[1].lower() == 'giugno':
        month='6'

    elif date_article[1].lower() == 'luglio':
        month='7'

    elif date_article[1].lower() == 'agosto':
        month='8'

    elif date_article[1].lower() == 'settembre':
        month='9'

    elif date_article[1].lower() == 'ottobre':
        month='10'

    elif date_article[1].lower() == 'novembre':
        month='11'

    elif date_article[1].lower() == 'dicembre':
        month='12'

    datetime = datetime.strptime(date_article[2]+'-'+month+'-'+date_article[0], '%Y-%m-%d')
    print(datetime)

    return datetime



start()
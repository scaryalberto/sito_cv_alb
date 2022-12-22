import pandas as pd
import requests
from bs4 import BeautifulSoup
from api_campania_sport.models import CampaniaSportArticles, ScrapingReviewsUrls
from scraping_trust_pilot_class import scraping_trust_pilot

def delete_old_articles():
    """
    crontab che consente di cancellare tutti gli articoli presi con lo scraping il giorno prima. Parte alle 2 di notte
    :return:
    """
    CampaniaSportArticles.objects.all().delete()


def start():
    """
    crontab che parte ogni 2 ore e mi serve per popolare l'api dell'app
    :return:
    """
    urls_into_db = []  # vediamo quali link abbiamo nel db
    queryset = CampaniaSportArticles.objects.all()
    for x, new_val in enumerate(queryset):
        urls_into_db.append(queryset[x].article_url)

    df = pd.DataFrame(columns=["title", "summary", "image_url", "text", "article_url", "title_for_list"])

    r = requests.get('http://www.campaniasport.it/?s=')

    soup = BeautifulSoup(r.content, 'html.parser')
    number_of_pages = int(soup.find('span', class_="pages").text.split(' ')[-1])

    all_links = []

    for n in range(number_of_pages):
        print(n)
        if n != 0:
            r = requests.get(f"http://www.campaniasport.it/page/{n}/?s")

        soup = BeautifulSoup(r.content, 'html.parser')

        for elem in soup.findAll("h3", class_="entry-title td-module-title"):
            all_links.append(elem.findAll('a')[0].attrs['href'])

        n = n + 1

    # ciclo su ogni link e compongo il diz dell'articolo: titolo, body, image_url

    all_links = list(set(all_links))

    for link in all_links:
        try:
            print(link)
            # se il link che stiamo analizzando si trova già nel db, passiamo a quello successivo
            if link in urls_into_db:
                continue
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'html.parser')

            body = soup.find('div', class_="td-post-content tagdiv-type").text
            try:
                image_url = get_image_url(soup.find('div', class_="postie-attachments"))
            except:
                image_url = "https://th.bing.com/th/id/OIP.gnUTTRvGWBshUURB5OBkhQHaHa?pid=ImgDet&rs=1"
            date_article = soup.find('time', class_="entry-date updated td-module-date").text
            datetime_article = change_date(date_article)
            #tolgo il body, così se uno vuole usare l'api si dovrà collegare al sito di mio fratello
            body = ""#body.replace('\n', '').replace('\u200b', '')
            title = soup.find('title').text
            title = title.replace('| Campania Sport', '')
            article = {'title': title, 'body': body, 'image_url': image_url, 'date_article': datetime_article}
            print(article)
            if len(title) > 110:
                title_for_list = title[0:100] + '...'
            else:
                title_for_list = title
            df = df.append(
                {"title": title, "title_for_list": title_for_list, "image_url": image_url, "text": body,
                 'date_article': datetime_article,
                 'article_url': link},
                ignore_index=True)
            # https://stackoverflow.com/questions/34425607/how-to-write-a-pandas-dataframe-to-django-model


        except:
            continue

        scraping_trust_pilot()

    # TODO: inserire il codice necessario al popolare il db sql
    print("ECCOLO")
    print(df)
    df = df.sort_values(by='date_article', ascending=False)
    # https://stackoverflow.com/questions/34425607/how-to-write-a-pandas-dataframe-to-django-model

    # retrieving all the elements
    # Storing in the variable
    for ind in df.index:
        print(df['title'][ind], df['image_url'][ind])
        new_article = CampaniaSportArticles(title=df['title'][ind],
                                            image_url=df['image_url'][ind],
                                            text=df['text'][ind], article_url=df['article_url'][ind],
                                            title_for_list=df['title_for_list'][ind])
        new_article.save()


def get_image_url(soup):
    soup_like_string = str(soup)
    image_url = soup_like_string.split('data-orig-file=')[1].split(' ')[0]
    return image_url.replace('"', '')


def change_date(date_article):
    from datetime import datetime

    date_article = date_article.split(' ')[1:]
    if date_article[1].lower() == 'gennaio':
        month = '1'
    elif date_article[1].lower() == 'febbraio':
        month = '2'
    elif date_article[1].lower() == 'marzo':
        month = '3'
    elif date_article[1].lower() == 'aprile':
        month = '4'
    elif date_article[1].lower() == 'maggio':
        month = '5'

    elif date_article[1].lower() == 'giugno':
        month = '6'

    elif date_article[1].lower() == 'luglio':
        month = '7'

    elif date_article[1].lower() == 'agosto':
        month = '8'

    elif date_article[1].lower() == 'settembre':
        month = '9'

    elif date_article[1].lower() == 'ottobre':
        month = '10'

    elif date_article[1].lower() == 'novembre':
        month = '11'

    elif date_article[1].lower() == 'dicembre':
        month = '12'

    datetime = datetime.strptime(date_article[2] + '-' + month + '-' + date_article[0], '%Y-%m-%d')
    print(datetime)

    return datetime



def scraping_reviews():
    new_url = ScrapingReviewsUrls(url="link_inserito_a_mano")
    new_url.save()
    scraping_trust_pilot()

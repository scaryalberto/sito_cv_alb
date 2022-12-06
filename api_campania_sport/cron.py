import pandas as pd
import requests
from bs4 import BeautifulSoup
from api_campania_sport.models import CampaniaSportArticles

def start():
    df = pd.DataFrame(columns=["title", "summary", "image_url", "text"])

    r = requests.get('http://www.campaniasport.it/?s=')

    soup = BeautifulSoup(r.content, 'html.parser')
    numer_of_pages = int(soup.find('span', class_="pages").text.split(' ')[-1])

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

    for link in all_links:
        try:
            print(link)
            r = requests.get(link)
            soup = BeautifulSoup(r.content, 'html.parser')
            body = soup.find('div', class_="td-post-content tagdiv-type").text
            body = body.replace('\n', '').replace('\u200b', '')
            title = soup.find('title').text
            title = title.replace('| Campania Sport', '')
            article = {'title': title, 'body': body, 'image_url': ''}
            print(article)
            df = df.append({"title": title, "image_url": '', "text": body},
                           ignore_index=True)
            #todo: distruggo e lo ricreo... sperando che sia un'operazione veloce
            new_article = CampaniaSportArticles(title=title,
                                                image_url="",
                                                text=body)
            new_article.save()
            #df.to_csv('csvfilename.csv')

        except:
            continue

    #TODO: inserire il codice necessario al popolare il db sql
    print("ECCOLO")
    print(df)
    # Below are quick example
    # Creating Empty DataFrame with Column Names
    # Create DataFrame with index and columns
    # Note this is not considered empty DataFrame


start()
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://myanimelist.net/manga/genre/22/Romance').text
soup = BeautifulSoup(html_text, 'lxml')

animes = soup.find_all('div', class_ = 'seasonal-anime js-seasonal-anime')
counter = 1
for anime in animes:
    properties = anime.find('div', class_='properties')
    property = properties.find_all('span', class_ = 'item')
    for desired_property in property:
        desired_property = desired_property.a.text
        if 'School' in desired_property:
            anime_name = anime.find('h2', class_='h2_manga_title').text
            status = anime.find('div', class_='info')
            status_spans = status.find_all('span', class_='item')
            for des_status in status_spans:
                des_status = des_status.text
                if 'Finished'in des_status or 'Publishing' in des_status:
                    des_status_2 = des_status
                if 'vol' in des_status:
                    print(f'({counter})\n\nAnime name: {anime_name}\nStatus: {des_status_2}\nTheme: {desired_property}\nChapters: {des_status}\n\n')
                    counter = counter + 1
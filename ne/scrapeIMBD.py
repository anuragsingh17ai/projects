import requests, openpyxl
from bs4 import BeautifulSoup

excel=openpyxl.Workbook()
sheet=excel.active
sheet.title='Top rated DC Animated Movies'
sheet.append(['Rank','Name of Movie','Year of Release','IMBD Rating'])
try:
    source=requests.get('https://www.imdb.com/list/ls058721118/')
    source.raise_for_status()
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('div',class_='lister-list').find_all('div',class_='lister-item mode-detail')
    for movie in movies:
        rank=movie.find('h3',class_='lister-item-header').find('span',class_='lister-item-index').text
        name=movie.find('h3',class_='lister-item-header').a.text
        year=movie.find('h3',class_='lister-item-header').find('span',class_='lister-item-year').text.split()[0].strip('()')
        rating=movie.find('div',class_='ipl-rating-widget').find('div',class_='ipl-rating-star').find('span',class_='ipl-rating-star__rating').text
        sheet.append([rank,name,year,rating])
        
except Exception as e:
    print(e)

excel.save('IMDB Movie Rating.xlsx')
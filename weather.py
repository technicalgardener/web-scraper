import requests
from bs4 import BeautifulSoup, SoupStrainer

url = "https://forecast.weather.gov/MapClick.php?x=232&y=29&site=sew&zmx=&zmy=&map_x=232&map_y=29"
page = requests.get(url)

cnd = SoupStrainer("p", class_="myforecast-current")
tmp = SoupStrainer("p", class_="myforecast-current-lrg")

conditions = BeautifulSoup(page.content, 'lxml', parse_only=cnd)
temperature = BeautifulSoup(page.content, 'lxml', parse_only=tmp)

print("Current Bellingham Weather:")
print("Conditions: %s\nTemp: %s\n" %(conditions.get_text(), temperature.get_text()))

from bs4 import BeautifulSoup
import pandas as pd
import requests
# driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq")


# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
# name=a.find('div', attrs={'class':'_3wU53n'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text) 

# https://in.bookmyshow.com/buytickets/spider-man-no-way-home-patna/movie-patn-ET00319080-MT/20211225

# print(arr)
def get_alert():
	url = "https://in.bookmyshow.com/buytickets/spider-man-no-way-home-patna/movie-patn-ET00319080-MT/20211225"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, "html.parser")

	date_elements = soup.find_all("div", class_="date-numeric")
	arr = []
	for dates in date_elements:
		# print(dates.text.strip())
		arr.append(dates.text.strip())
	if (arr[-1] == '26') or (arr[-1] == '27') or (arr[-1] == '28') or (arr[-1] == '29'):
		return "High Alert"
	else:
		return "Ruko zara, sabar karo"



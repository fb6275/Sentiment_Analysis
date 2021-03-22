# -*- coding: utf-8 -*-
"""trustpilot_scraping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1023yjUeF-vdKeZ18I46pzvSs3ZBqQSCA

# SETUP

"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from random import randint
import json

PATH = "/Users/fb/chromedriver"  # the path were the chromedriver is
driver = webdriver.Chrome(PATH)

url = driver.get('https://fr.trustpilot.com/categories')

"""URL OF ALL CATEGORY"""

food = 'https://fr.trustpilot.com/categories/food_beverages_tobacco'
animals = 'https://fr.trustpilot.com/categories/animals_pets'
money = 'https://fr.trustpilot.com/categories/money_insurance'
beauty = 'https://fr.trustpilot.com/categories/beauty_wellbeing'
construct = 'https://fr.trustpilot.com/categories/construction_manufactoring'
educ = 'https://fr.trustpilot.com/categories/education_training'
tech = 'https://fr.trustpilot.com/categories/electronics_technology'
event = 'https://fr.trustpilot.com/categories/events_entertainment'
hobbie = 'https://fr.trustpilot.com/categories/hobbies_crafts'
house = 'https://fr.trustpilot.com/categories/home_garden'
media = 'https://fr.trustpilot.com/categories/media_publishing'
bar = 'https://fr.trustpilot.com/categories/restaurants_bars'
health = 'https://fr.trustpilot.com/categories/health_medical'
utilities = 'https://fr.trustpilot.com/categories/utilities'
home_service = 'https://fr.trustpilot.com/categories/home_services'
business_service = 'https://fr.trustpilot.com/categories/business_services'
legal_service = 'https://fr.trustpilot.com/categories/legal_services_government'
public_service = 'https://fr.trustpilot.com/categories/public_local_services'
fashion = 'https://fr.trustpilot.com/categories/shopping_fashion'
sport = 'https://fr.trustpilot.com/categories/sports'
vacation = 'https://fr.trustpilot.com/categories/travel_vacation'
vehicule = 'https://fr.trustpilot.com/categories/vehicles_transportation'

"""BEGIN"""

driver.get(animals)  # take the url animals

print(driver.current_url)

#time.sleep(randint(3, 5))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')  # create the soup and collect the html

# collect 20 shops in category sport

# target shops
commerces = soup.find_all('a', class_='link_internal__YpiJI link_wrapper__LEdx5')

commerces_link = []

# for each shop, collect the url stored in the html
# add to the list commerce_link
for i in commerces:
    link = i['href']
    commerces_link.append(link)

print(commerces_link)
# collect only the fist 20 link
commerces_link = commerces_link[:20]
print(commerces_link)

# to get entire links :

# page 1

real_link = []

for i in commerces_link:
    link = f'https://fr.trustpilot.com{i}'
    real_link.append(link)
print(real_link)

# page 2
page_two = []

for i in real_link:
    link = f'{i}?page=2'
    page_two.append(link)
print(page_two)

# page 3
page_three = []

for i in real_link:
    link = f'{i}?page=3'
    page_three.append(link)
print(page_three)

# page 4
page_four = []

for i in real_link:
    link = f'{i}?page=4'
    page_four.append(link)
print(page_four)

# page 5
page_five = []

for i in real_link:
    link = f'{i}?page=5'
    page_five.append(link)
print(page_five)

# page 6
page_six = []

for i in real_link:
    link = f'{i}?page=6'
    page_six.append(link)
print(page_six)

# page 7
page_seven = []

for i in real_link:
    link = f'{i}?page=7'
    page_seven.append(link)
print(page_seven)

# page 8
page_eight = []

for i in real_link:
    link = f'{i}?page=8'
    page_eight.append(link)
print(page_eight)

# page 9
page_nine = []

for i in real_link:
    link = f'{i}?page=9'
    page_nine.append(link)
print(page_nine)

# page 10
page_ten = []

for i in real_link:
    link = f'{i}?page=10'
    page_ten.append(link)
print(page_ten)

# create variable for stocking scraped data
date = []
titre = []
avis = []
score = []
error = '///Error_Scrap///'
shop_titre = []


# definition of the function scrap()
def scrape():
    # for each review
    for i in all_review:

        # ------------------------------------- REVIEW TITLE -------------------------------------
        try:
            # we try to collect the data
            title_review = i.find('a', class_='link link--large link--dark').text
            titre.append(title_review)
            shop_titre.append(shop_title)
            # time.sleep(randint(2, 3))

        except:
            # if fail, we append '///Error_Scrap///' instead of
            # break the code
            titre.append(error)
            shop_titre.append(shop_title)

        print(shop_titre)
        print(titre)

        # ------------------------------------- REVIEW -------------------------------------
        try:
            review = i.find('p', class_='review-content__text').text
            avis.append(review)
            # time.sleep(randint(2, 3))
        except:
            avis.append(error)

        print(avis)

        # ------------------------------------- SCORE -------------------------------------
        try:
            note = i.img['alt']
            score.append(note)
            # time.sleep(randint(2, 3))

        except:
            score.append(error)

        print(score)

        # ------------------------------------- DATE -------------------------------------
        # not working
        '''try:
          day = i.time['datetime']
          date.append(day)
          time.sleep(randint(2, 3))
        except:
          date.append(error)

        print(date)'''


# for each shop
for i in real_link:
    # collect the url
    driver.get(i)
    # print the actual url collected
    print(driver.current_url)
    # make a soup with current url
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # sleep for not breaking the code
    #time.sleep(randint(5, 7))

    # search all reviews
    all_review = soup.find_all('article', class_='review')
    # find the shop name
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    # find the total of review for each shop
    nb_avis = soup.find('span', class_='headline__review-count').text
    # replace html 'NBSP' by nothing
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    # convert in int
    nb_avis = int(float(nb_avis))
    # if number of review > 230, scrap, if not, pass
    if nb_avis > 230:
        scrape()
    else:
        pass
################################# PAGE 2 ################################

# same process for each page

for i in page_two:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 3 ################################


for i in page_three:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 4 ################################


for i in page_four:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass
################################# PAGE 5 ################################


for i in page_five:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 6 ################################


for i in page_six:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 7 ################################


for i in page_seven:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 8 ################################


for i in page_eight:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass
################################# PAGE 9 ################################


for i in page_nine:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

################################# PAGE 10 ################################


for i in page_ten:
    driver.get(i)
    print(driver.current_url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    #time.sleep(randint(5, 7))

    all_review = soup.find_all('article', class_='review')
    shop_title = soup.find('span', class_='multi-size-header__big').text
    print(shop_title)
    nb_avis = soup.find('span', class_='headline__review-count').text
    nb_avis = nb_avis.replace(' ', '')
    print(nb_avis)
    nb_avis = int(float(nb_avis))
    if nb_avis > 230:
        scrape()
    else:
        pass

driver.quit()  # when all the data is collected, close the driver


# create a dataframe

data = {'nom_shop': shop_titre,
        'titre_avis': titre,
        'avis': avis,
        'score': score
        }

df = pd.DataFrame(data, columns=['nom_shop', 'titre_avis', 'avis', 'score'])

print(df)
df.to_csv('animals.csv')  # transform the dataframe in csv

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


def scraping():
    PATH = "/Users/fb/chromedriver"  # the path where the chromedriver is
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
    hobby = 'https://fr.trustpilot.com/categories/hobbies_crafts'
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
    vehicle = 'https://fr.trustpilot.com/categories/vehicles_transportation'

    """# Choix de la catégorie"""

    choice = input("Entrez la catégorie choisie : \n "
                   "- tapez aliments pour Aliments, Boissons, Tabac \n"
                   " - tapez animaux pour Animaux \n"
                   " - tapez argent pour Argent & Assurance \n"
                   " - tapez beauty pour Beauté & Bien-être \n"
                   " - tapez construction pour Contruction & Fabrication \n"
                   " - tapez formation pour les Education & Formation \n"
                   " - tapez tech pour Electronique & Technologie \n"
                   " - tapez event pour Evenements & Divertissement \n"
                   " - tapez loisirs pour Loisirs & Artisanat \n"
                   " - tapez maison pour Maison & Jardin \n"
                   " - tapez media pour Média & Edition \n"
                   " - tapez bar pour Restaurants & Bars\n"
                   " - tapez health pour Santé & Médecine \n"
                   " - tapez services pour Services  \n"
                   " - tapez domicile pour Services à Domicile \n"
                   " - tapez entreprise pour Services aux entreprises \n"
                   " - tapez legal pour Services Juridiques & Administration \n"
                   " - tapez public pour Services Publics & Locaux  \n"
                   " - tapez fashion pour Shopping & Mode \n"
                   " - tapez sport pour Sport \n"
                   " - tapez vacances pour Vacances & Voyages \n"
                   " - tapez transport pour Vehicules & Transport : \n")

    """# Mise à jour de l'URL en fonction de la catégorie choisie"""

    for i in choice:

        if 'aliments' in choice:
            url = driver.get(food)

        elif 'animaux' in choice:
            url = driver.get(animals)

        elif 'argent' in choice:
            url = driver.get(money)

        elif 'beauty' in choice:
            url = driver.get(beauty)

        elif 'construction' in choice:
            url = driver.get(construct)

        elif 'formation' in choice:
            url = driver.get(educ)

        elif 'tech' in choice:
            url = driver.get(tech)

        elif 'event' in choice:
            url = driver.get(event)

        elif 'loisirs' in choice:
            url = driver.get(hobby)

        elif 'maison' in choice:
            url = driver.get(house)

        elif 'media' in choice:
            url = driver.get(media)

        elif 'bar' in choice:
            url = driver.get(bar)

        elif 'health' in choice:
            url = driver.get(health)

        elif 'services' in choice:
            url = driver.get(utilities)

        elif 'domicile' in choice:
            url = driver.get(home_service)

        elif 'entreprise' in choice:
            url = driver.get(business_service)

        elif 'legal' in choice:
            url = driver.get(legal_service)

        elif 'public' in choice:
            url = driver.get(public_service)

        elif 'fashion' in choice:
            url = driver.get(fashion)

        elif 'sport' in choice:
            url = driver.get(sport)

        elif 'vacances' in choice:
            url = driver.get(vacation)

        elif 'transport' in choice:
            url = driver.get(vehicle)

        else:
            print(choice)

    """BEGIN"""

    print(driver.current_url)

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

    # collect only the fist 20 link
    commerces_link = commerces_link[:20]

    # to get entire links :

    # page 1

    real_link = []

    for i in commerces_link:
        link = f'https://fr.trustpilot.com{i}'
        real_link.append(link)
    print(real_link)

    # create variable for stocking scraped data

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
                
            except:
                avis.append(error)

            print(avis)

            # ------------------------------------- SCORE -------------------------------------
            try:
                note = i.img['alt']
                score.append(note)

            except:
                score.append(error)

            print(score)

    # for each shop
    for i in real_link:
        # collect the url
        driver.get(i)
        # print the actual url collected
        print(driver.current_url)
        # make a soup with current url
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # search all reviews
        all_review = soup.find_all('article', class_='review')
        # find the shop name
        shop_title = soup.find('span', class_='multi-size-header__big').text
        print(shop_title)

        scrape()

    driver.quit()  # when all the data is collected, close the driver

    data = {'nom_shop': shop_titre,
            'titre_avis': titre,
            'avis': avis,
            'score': score
            }

    df = pd.DataFrame(data, columns=['nom_shop', 'titre_avis', 'avis', 'score'])

    print(df)
    name = input("choisissez un nom pour votre fichier : ")
    df.to_csv(f'{name}.csv')  # transform the dataframe in csv


scraping()

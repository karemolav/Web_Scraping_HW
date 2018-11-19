from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
from datetime import datetime
import time

# Scrape function
def Scrape():

    print("COMMENCING SCRAPE")
    print("----------------------------------")
    # Create a dictionary for all of the scraped data
    mars_dict = {}

    # Initialize browser
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless = False)

    #Visit the NASA page
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    #Scrape page into soup
    html = browser.html
    soup = bs(html,"html.parser")

    #Find the latest News Title and Paragraph Text.
    news_title = soup.find("div",class_="content_title").text
    news_p= soup.find("div", class_="article_teaser_body").text
    print(f"Title: {news_title}")
    print(f"Paragraph: {news_p}")

    # Add the news title and paragraph to the dictionary
    mars_dict["news_title"] = news_title
    mars_dict["news_p"] = news_p
    
    print("NEWS TITLE & DESCRIPTION ACQUIRED")

    # JPL Mars Space Images - Featured Image

    #Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    url_image = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    html = browser.html
    soup = bs(html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    img_url = "https://jpl.nasa.gov"+image
    img_url

    # Save a complete url string to a variable called `featured_image_url`
    featured_image_url = img_url

    # Add the featured image url to the dictionary
    mars_dict["featured_image_url"] = featured_image_url
    print("FEATURED IMAGE ACQUIRED")


    # Mars Weather

    #Visit the Mars Weather twitter account and scrape the latest Mars weather tweet from the page. 
    weather_url = 'https://twitter.com/marswxreport?lang=en '
    browser.visit(weather_url)

    #Save the tweet text for the weather report as a variable called mars_weather.
    html_weather = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html_weather, 'html.parser')

    # Find tweets
    latest_M_tweets = soup.find_all('div', class_='js-tweet-text-container')

    # Retrieve tweets and  heck for words that are weather related (Sol and pressure)and exclude non weather words
    for tweet in latest_M_tweets: 
        weather_tweet = tweet.find('p').text
        if 'Sol' and 'pressure' in weather_tweet:
            print(weather_tweet)
            break
        else: 
            pass
    # In[11]:
    mars_weather = weather_tweet
    # Add the weather to the dictionary
    mars_dict["mars_weather"] = mars_weather

    print("WEATHER ACQUIRED")

    #  Mars Facts

    #Visit the Mars Facts site and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    facts_url = 'http://space-facts.com/mars/'
    #Use Pandas to convert the data to a HTML table string
    mars_facts = pd.read_html(facts_url)
    # Find the mars facts and assign it to `mars_fact_df`
    mars_fact_df = mars_facts[0]
    mars_fact_df.columns = ['Description','Value']
    # Set the index 
    mars_fact_df.set_index('Description', inplace=True)
    # Save html 
    mars_fact_df.to_html()
    # Display mars_df
    mars_fact_df
    # Add the Mars facts table to the dictionary
    mars_dict["mars_fact_df"] = mars_fact_df

    # # Mars Hemispheres
    # Mars Hemispheres URL
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Empty list of image urls
    hemisphere_image_urls = []
    #Valles Marineris:
    # Setting up splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Valles Marineris Hemisphere')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    valles_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    valles_marineris = {
        "title": "Valles Marineris Hemisphere",
        "img_url": valles_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(valles_marineris)

    #Cerberus:
    # Setting up splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Cerberus Hemisphere')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    cerberus_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    cerberus = {
        "title": "Cerberus Hemisphere",
        "img_url": cerberus_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(cerberus)

    #Schiaparelli Hemisphere
    # Setting up splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)

    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Schiaparelli Hemisphere')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    schiaparelli_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    schiaparelli = {
        "title": "Schiaparelli Hemisphere",
        "img_url": schiaparelli_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(schiaparelli)

    #Syrtis Major
    # Setting up splinter
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser('chrome', **executable_path, headless=True)
    browser.visit(url)
    # Moving through pages
    time.sleep(5)
    browser.click_link_by_partial_text('Syrtis Major Hemisphere')
    time.sleep(5)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = bs(html, 'html.parser')

    # Store link
    syrtis_link = soup.find('div', 'downloads').a['href']

    # Create dictionary
    syrtis_major = {
        "title": "Syrtis Major Hemisphere",
        "img_url": syrtis_link
    }

    # Appending dictionary
    hemisphere_image_urls.append(syrtis_major)

    mars_dict["hemisphere_image_urls"] = hemisphere_image_urls
    print("HEMISPHERE IMAGES ACQUIRED")
    print("----------------------------------")
    print("SCRAPING COMPLETED")
    # Return the dictionary
    return mars_dict





from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
# load the environment variables
load_dotenv('.env')
# get the user agent from the environment variables
User_Agent = os.getenv('USER_AGENT')

"""
IMPORTANT NOTE:
===> URL = amazon men fleece sweaters clearance sale <===

when visit any website --> you send  http request(contains many things, one of them is HEADERS --> inside the headers you have +++User-Agent+++ - which is the browser you are using to visit the website, and the language you are using to visit the website, and TELL the website that you are a human, NOT a robot!!!),

# without the headers, the website will not allow you to visit the website, and will block you, and will not allow you to visit

## need to get the User-Agent ==>google->whatismybrowswer.com ->detect my settings-> what is my user agent -> copy the user agent
"""

URL = 'https://www.amazon.com/s?k=men+WINTER+fleece+sweaters+clearance+sale&crid=KI9NDB2AUBZB&sprefix=men+winter+fleece+sweaters+clearance+sale%2Caps%2C61&ref=nb_sb_noss'

# headers for requests // PASTE THE USER AGENT HERE, 'Accept-Language': 'en-US, en;q=0.5'
HEADERS = ({'User-Agent': User_Agent, 'Accept-Language': 'en-US, en;q=0.5'})

# send request to the url
webpage = requests.get(URL, headers=HEADERS)
print(webpage.status_code)
"""
CHECK IF THE REQUEST IS SUCCESSFUL
print(webpage.status_code)==> # 200 means the request is successful
"""

"""
when using BS4, need to specify the parser, in this case, we are using html.parser(sometimes it might not deal with the html properly, so we need to use "lxml parser" - best parser for BS4)
# install lxml parser ==> pip install lxml
"""
# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(webpage.content, 'lxml')

"""
statement to open the file
- 1st parameter is the file name
- 2nd parameter is the method you want to apply to open the file(read,write,both)
+ reading the file

"""
# ### WHEN HAVE THE FILE, NO NEED TO SEND THE REQUEST TO THE WEBSITE, JUST OPEN THE FILE
# with open('amazon_web_scrapper.html', 'r') as html_file:
#     content = html_file.read()

"""
find the product title by inspecting the html code
check the html code, find the id|| class name || the element of the product title
"""
# find the product title // find_all() returns a list // find() returns the first element
PRODUCTS = soup.find_all('div', class_='sg-col-inner')


reply = input("> Ready to begin?... Please reply 'yes' or 'no' and press Enter:")
if reply == 'yes':
    print("Starting the web scrapper...")
    #  PRODUCTS = soup.find_all('div', class_='sg-col-inner')
    for product in PRODUCTS:
        brand = product.find('span', class_='a-size-base-plus a-color-base')
        title = product.find('span', class_='a-text-normal')
        price = product.find('span', class_='a-offscreen')
        link = product.find('a', class_='a-link-normal', href=True)

        if brand and title and price and link:
            print("Product Brand:", brand.text)
            print("Product Title:", title.text)
            """
            need to add the link to the product link, because the link is not complete, it is missing the domain name, so we need to add the domain name to the link
            'https://www.amazon.com' + link['href'] - link of each product 
            // link is a dictionary, so we need to use the key to get the value
            """
            print("Product Link:", 'https://www.amazon.com' + link['href'])
            print("Product Price:", price.text)
            print("If you want to open a link from the terminal, type 'open' + the link")
            print("========================================")

else:
    print("Exiting the web scrapper...")
    exit()

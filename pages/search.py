"""
this module contains DuckDuckSearchPage,
thie page obkect for the DuckDickGo search page.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    URL  = 'https://www.duckduckgo.com'
    SEARH_INPUT   = (By.ID,'search_form_input_homepage')

#Initializer

    def __init__(self,browser):
        self.browser = browser

#Interactive Methods
    def load(self):
        self.browser.get(self.URL)


    def search(self,phrase):
        search_input = self.browser.find_element(*self.SEARH_INPUT) #this will throw excep if it is faild 
        search_input.send_keys(phrase,Keys.RETURN)  #commit that search and procced to the result page
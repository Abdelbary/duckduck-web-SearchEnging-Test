"""
This module contains DuckDuckGoTesulyPage,
the page object for the DuckDuckGo search result page.
"""
from selenium.webdriver.common.by import By


class DuckDucGoResultPage:
    
    SEARCH_RESULT_LINKS = (By.CSS_SELECTOR,'a.result__a')
    SEARCH_INPUT = (By.ID,'search_form_input')

    def __init__(self,brower):
        self.browser = brower

    def result_link_titles(self):
        links = self.browser.find_elements(*self.SEARCH_RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        searchInput = self.browser.find_element(*self.SEARCH_INPUT)
        value       = searchInput.get_attribute('value')#get the get_attribute for input elements not the text function
        return value


    def title(self):
        return self.browser.title
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage 
import pytest

@pytest.mark.parametrize('phrase',['panda','python','duck','ahmed','you','too'])
def test_basic_duckduckgo_search(browser,phrase):
    
    searchPage       = DuckDuckGoSearchPage(browser)
    serachResultPage = DuckDuckGoResultPage(browser)
    
    # Given the DuckDuckGo home page is displayed
    searchPage.load()


    # When the user searches for "panda"
    searchPage.search(phrase)

    # Then the search result is "panda"
    assert phrase == serachResultPage.search_input_value()

    browser.get_screenshot_as_png()
    # And the search result links pertain to "panda"
    for title in serachResultPage.result_link_titles():
        assert phrase.lower() in title.lower()

    
    # And the search result title contains "panda"
    assert phrase in serachResultPage.title()
   
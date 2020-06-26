from pages.result import DuckDucGoResultPage
from pages.search import DuckDuckGoSearchPage 

def test_basic_duckduckgo_search(browser):
    
    searchPage       = DuckDuckGoSearchPage(browser)
    serachResultPage = DuckDucGoResultPage(browser)
    PHASE  = "duck"
    
    # Given the DuckDuckGo home page is displayed
    searchPage.load()


    # When the user searches for "panda"
    searchPage.search(PHASE)


    # Then the search result title contains "panda"
    assert PHASE in serachResultPage.title()

    # And the search result is "panda"
    assert PHASE == serachResultPage.search_input_value()

    browser.get_screenshot_as_png()
    # And the search result links pertain to "panda"
    for title in serachResultPage.result_link_titles():
        assert PHASE.lower() in title.lower()
    # TODO remove this exception when done
    #raise Exception("Incomplete Test")
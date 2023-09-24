"""
These tests cover DuckDuckGo searches
"""
import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


@pytest.mark.parametrize('PHRASE', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, PHRASE):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

    # Then the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

    # And the search result title contains "panda"
    assert PHRASE in result_page.title()


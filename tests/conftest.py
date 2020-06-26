"""
this module contain shared fixtures
"""

import pytest
import selenium.webdriver
import json


@pytest.fixture
def config(scope='session'): # read the configration file once

    # Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Chrome','Firefox','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

def getBrowser(config):
    browser = config['browser']

    if   browser == "Chrome":
        b = selenium.webdriver.Chrome()

    elif browser == "Firefox":       
        b = selenium.webdriver.Firefox()

    elif browser == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser"{config["browser"]}" is not supported')

    return b



@pytest.fixture
def browser(config):

    b = getBrowser(config)

    b.implicitly_wait(config['implicit_wait'])

    yield b

    b.quit()
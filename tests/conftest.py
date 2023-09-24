import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):

    # Read the file
    with open('./tau-intro-selenium-py/config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Firefox']
    assert isinstance(config['implicitly_wait'], int)
    assert config['implicitly_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the ChromeDriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Firefox':
        opts = selenium.webdriver.FirefoxOptions()
        opts.add_argument('-headless')
        b = selenium.webdriver.Firefox(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicitly_wait'])
    
    # Return the webdriver instance for the setup
    yield b

    # Quit the Webdriver instance for the cleanup
    b.quit()


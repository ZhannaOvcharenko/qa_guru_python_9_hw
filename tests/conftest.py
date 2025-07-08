import pytest
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module", autouse=True)
def open_browser():
    service = Service(ChromeDriverManager().install())
    browser.config.driver = webdriver.Chrome(service=service)
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.maximize_window()

    yield

    browser.quit()
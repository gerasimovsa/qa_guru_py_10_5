import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.driver_name = "firefox"
    browser.config.timeout = 6.0
    browser.config.window_width = 2880
    browser.config.window_height = 1200
    yield
    browser.quit()

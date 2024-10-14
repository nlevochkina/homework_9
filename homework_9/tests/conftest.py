import pytest
from selene.support.shared import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def set_browser_size():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1080
    browser.config.window_width = 1920

import pytest
from selene import browser, be, have, by
from selenium import webdriver


@pytest.fixture(params=[(1920, 1080), (1366, 768), (375, 812), (414, 896)])
def settings_browser(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://github.com'
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

@pytest.mark.parametrize('settings_browser', [(375, 812), (414, 896)], indirect=True)
def test_sign_in_mobile(settings_browser):
    browser.open("/")
    browser.element("button.Button--link").should(be.visible).click()
    browser.element("a[href='/login']").should(be.visible).click()
    browser.should(have.url_containing("login"))

@pytest.mark.parametrize('settings_browser', [(1920, 1080), (1366, 768)], indirect=True)
def test_sign_in_desktop(settings_browser):
    browser.open("/")
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing("login"))

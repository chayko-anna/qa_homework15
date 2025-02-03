import pytest
from selene import browser, be, have

link = "https://github.com/"


def test_desktop_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Mobile resolution")
    browser.open(link)
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing("login"))


def test_mobile_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Desktop resolution")
    browser.open(link)
    browser.element("button.Button--link").should(be.visible).click()
    browser.element("a[href='/login']").should(be.visible).click()
    browser.should(have.url_containing("login"))

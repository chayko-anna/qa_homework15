from selene import browser, by, be, have


link = "https://github.com/"

def test_sign_in_mobile(mobile_browser):
    browser.open(link)
    browser.element("button.Button--link").should(be.visible).click()
    browser.element("a[href='/login']").should(be.visible).click()
    browser.should(have.url_containing("login"))

def test_sign_in_desktop(desktop_browser):
    browser.open(link)
    browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.should(have.url_containing("login"))
import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1280, 960), (1024, 768), (1024, 576), (412, 915)])
def setup_browser(request):

    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height

    yield "desktop" if width > 1024 else "mobile"

    browser.quit()


@pytest.fixture(params=[(1280, 960), (1024, 768), (1024, 576)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(414, 896), (390, 844), (412, 915)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
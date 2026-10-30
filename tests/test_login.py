from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_page_is_visible(page: Page) -> None:
    page.goto("/")
    login_page = LoginPage(page)
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_login_with_valid_credentials(page: Page) -> None:
    page.goto("/")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

def test_login_with_invalid_credentials(page: Page) -> None:
    page.goto("/")
    login_page = LoginPage(page)
    login_page.login("standard_user","12332")
    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Epic sadface: Username and password do not match any user in this service")
 

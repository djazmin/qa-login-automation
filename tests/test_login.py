from playwright.sync_api import Page, expect

def test_login_page_is_visible(page : Page) -> None:
    page.goto("https://www.saucedemo.com/")

    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()

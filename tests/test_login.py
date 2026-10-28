from playwright.sync_api import Page, expect

def test_login_page_is_visible(page: Page) -> None:
    page.goto("/")

    expect(page.locator("#user-name")).to_be_visible()
    expect(page.locator("#password")).to_be_visible()
    expect(page.locator("#login-button")).to_be_visible()


def test_login_with_valid_credentials(page: Page) -> None:
    page.goto("/")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

def test_login_with_invalid_credentials(page: Page) -> None:
    page.goto("/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("12334")
    page.locator("#login-button").click()
    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")
 

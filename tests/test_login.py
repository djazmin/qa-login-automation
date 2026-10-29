from playwright.sync_api import Page, expect

def test_login_page_is_visible(page: Page) -> None:
    page.goto("/")
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.get_by_role("button",name = "Login")).to_be_visible()


def test_login_with_valid_credentials(page: Page) -> None:
    page.goto("/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

def test_login_with_invalid_credentials(page: Page) -> None:
    page.goto("/")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("12334")
    page.get_by_role("button",name = "Login").click()
    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_have_text("Epic sadface: Username and password do not match any user in this service")
 

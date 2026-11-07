import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from test_data.users import STANDARD_USER, INVALID_USER, LOCKED_USER


def test_login_page_is_visible(page: Page, login_page: LoginPage) -> None:
    page.goto("/")

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


def test_login_with_valid_credentials(page: Page, login_page: LoginPage) -> None:
    page.goto("/")

    login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")

@pytest.mark.parametrize("user, expected_error", 
                         [(INVALID_USER,
                        "Epic sadface: Username and password do not match any user in this service"),
                        (LOCKED_USER,
                        "Epic sadface: Sorry, this user has been locked out.")],
                        ids=["invalid_user", "locked_user"])
def test_login_with_invalid_credentials(page: Page, login_page: LoginPage, user: dict, expected_error: str) -> None:
    page.goto("/")

    login_page.login(user["username"], user["password"])

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text(expected_error)
 

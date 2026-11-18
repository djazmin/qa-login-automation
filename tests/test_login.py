import pytest
from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from test_data.users import (
    User,
    STANDARD_USER,
    INVALID_USER,
    LOCKED_USER,
    EMPTY_USER,
    EMPTY_PASSWORD,
    EMPTY_CREDENTIALS,
    NON_EXISTENT_USER,
)


def test_login_page_is_visible(opened_login_page: LoginPage) -> None:

    expect(opened_login_page.username_input).to_be_visible()
    expect(opened_login_page.password_input).to_be_visible()
    expect(opened_login_page.login_button).to_be_visible()


def test_login_with_valid_credentials(
        page: Page, 
        opened_login_page: LoginPage, 
        inventory_page: InventoryPage, 
        base_url: str
    ) -> None:

    opened_login_page.login(STANDARD_USER["username"], STANDARD_USER["password"])

    expect(page).to_have_url(f"{base_url}/inventory.html")
    expect(inventory_page.title).to_have_text("Products")


@pytest.mark.parametrize("user, expected_error", [
    pytest.param(INVALID_USER, "Epic sadface: Username and password do not match any user in this service", id="invalid_user"),
    pytest.param(LOCKED_USER, "Epic sadface: Sorry, this user has been locked out.", id="locked_user"),
    pytest.param(EMPTY_USER, "Epic sadface: Username is required", id="empty_username"),
    pytest.param(EMPTY_PASSWORD, "Epic sadface: Password is required", id="empty_password"),
    pytest.param(EMPTY_CREDENTIALS, "Epic sadface: Username is required", id="empty_credentials"),
    pytest.param(NON_EXISTENT_USER, "Epic sadface: Username and password do not match any user in this service", id="non_existent_user"),
])
def test_login_is_rejected(
    page: Page, 
    opened_login_page: LoginPage, 
    user: User, 
    expected_error: str, 
    base_url: str
) -> None:
    opened_login_page.login(user["username"], user["password"])

    expect(opened_login_page.error_message).to_be_visible()
    expect(opened_login_page.error_message).to_have_text(expected_error)
    expect(page).to_have_url(f"{base_url}/")

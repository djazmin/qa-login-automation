from playwright.sync_api import Page


class LoginPage:
    # self is the LoginPage object being created.
    # page is the browser page that Playwright provides.
    # ": Page" is a type annotation: it says which kind of object is expected.
    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto("/")

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

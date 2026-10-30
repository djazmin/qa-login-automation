from playwright.sync_api import Page

'''
    self represents the object that we are creating
    page get the browser page from Playwright.
    : Page is an annotation that clarify which kind of object we are waiting to get
'''
class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator('[data-test="error"]')

    def login(self, username: str, password: str)-> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

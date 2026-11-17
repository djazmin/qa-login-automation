# QA Login Automation

[![Playwright Tests](https://github.com/djazmin/qa-login-automation/actions/workflows/tests.yml/badge.svg)](https://github.com/djazmin/qa-login-automation/actions/workflows/tests.yml)

Automated UI tests for the [SauceDemo](https://www.saucedemo.com/) login page using Python, Playwright, and pytest.

## Project Overview

This project demonstrates the fundamentals of web UI test automation, including the Page Object Model, accessible and stable locators, parametrized positive and negative scenarios, and continuous integration with GitHub Actions.

## Test Scenarios

The suite runs 7 test cases in Chromium:

- **Login page visibility:** Verifies that the username field, password field, and login button are visible.
- **Successful login:** Verifies that valid credentials navigate to the inventory page and display the "Products" title.
- **Rejected login:** Verifies that the expected error message is shown and the user stays on the login page for:
  - a valid username with a wrong password
  - a locked-out user
  - an empty username
  - an empty password
  - a username that does not exist

## Tech Stack

- Python 3.12
- Playwright
- pytest
- pytest-playwright
- GitHub Actions

## Prerequisites

- Python 3.12
- Git
- Visual Studio Code (recommended)
- The following installation commands are for macOS

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/djazmin/qa-login-automation.git
   cd qa-login-automation
   ```

2. Create a virtual environment:

   ```bash
   python3.12 -m venv .venv
   ```

3. Activate the virtual environment on macOS:

   ```bash
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Install the Playwright Chromium browser:

   ```bash
   python -m playwright install chromium
   ```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Run the tests with a visible browser:

```bash
pytest -v --headed
```

Run only the tests whose name matches an expression:

```bash
pytest -v -k rejected
```

Run the suite against another environment:

```bash
pytest -v --base-url https://staging.example.com
```

The base URL must not end with a slash. Default options (base URL, browser, tracing, and screenshots) are defined in `pytest.ini`.

## Test Reports

When a test fails, a Playwright trace and a screenshot are saved in `test-results/<test-name>/`. Open the trace to replay the test step by step:

```bash
python -m playwright show-trace test-results/<test-name>/trace.zip
```

Passing tests do not produce artifacts.

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/tests.yml` runs the suite on every push and pull request to `main`. If the test execution fails, the `test-results/` folder is uploaded as the `playwright-results` artifact. It can be downloaded from the GitHub Actions workflow run page.

## Project Structure

```text
qa-login-automation/
├── .github/
│   └── workflows/
│       └── tests.yml 
│
├── .claude/
│   └── skills/
│       └── qa-code-review/
│           └── SKILL.md
│
├── pages/                   # Page objects: locators and page interactions
│   ├── inventory_page.py
│   └── login_page.py
├── test_data/               # Reusable test data
│   └── users.py
├── tests/                   # Test cases and assertions
│   ├── conftest.py          # Shared fixtures
│   └── test_login.py
├── .gitignore
├── AGENTS.md                # AI collaboration rules
├── CLAUDE.md                # Testing strategy and code review rules
├── pytest.ini               # pytest and Playwright configuration
├── README.md
└── requirements.txt
```

## Architecture

- **Page Object Model:** Locators and page interactions live in `pages/`, so a UI change is fixed in one place instead of in every test.
- **Assertions in tests:** Page objects never assert. Expected outcomes stay in `tests/`, where they are easy to read.
- **Separated test data:** Users are defined in `test_data/users.py` and combined with expected errors through `pytest.mark.parametrize`.
- **Fixtures:** `conftest.py` provides the page objects. Each test gets a fresh browser page, so tests are independent of each other and of execution order.

## Learning Goals

- Build maintainable UI automation tests.
- Understand Playwright locators and assertions.
- Practice positive and negative testing.
- Integrate automated tests into a CI/CD pipeline.
- Apply the Page Object Model and pytest fixtures
- Use parametrization to cover multiple test scenarios

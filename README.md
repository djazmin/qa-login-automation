# QA Login Automation

Automated UI tests for the [SauceDemo](https://www.saucedemo.com/) login page using Python, Playwright, and pytest.

## Project Overview

This project demonstrates the fundamentals of web UI test automation, including element locators, assertions, positive and negative test scenarios, and automated test execution.

## Test Scenarios

The current test suite covers:

- **Login page visibility:** Verifies that the username field, password field, and login button are visible.
- **Successful login:** Verifies that valid credentials navigate to the inventory page and display the "Products" title.
- **Invalid credentials:** Verifies that invalid credentials display the expected error message.

## Tech Stack

- Python 3.12
- Playwright
- pytest
- pytest-playwright

## Prerequisites

- Python 3.12
- Git
- Visual Studio Code (recommended)

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
python -m pytest -v
```

Run the tests with a visible browser:

```bash
python -m pytest -v --headed
```

## Project Structure

```text
qa-login-automation/
├── tests/
│   └── test_login.py
├── docs/
├── .gitignore
├── AGENTS.md
├── pytest.ini
├── README.md
└── requirements.txt
```

## Current Status

The project currently includes three automated login tests. GitHub Actions CI/CD and additional test scenarios are planned for future iterations.

## Learning Goals

- Build maintainable UI automation tests.
- Understand Playwright locators and assertions.
- Practice positive and negative testing.
- Integrate automated tests into a CI/CD pipeline.

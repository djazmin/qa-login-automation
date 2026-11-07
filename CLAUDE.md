## Testing strategy
- Follow the Page Object Model (POM) architecture.
- Keep page locators and page interactions inside page objects.
- Keep assertions and expected outcomes inside test files.
- Store reusable test data separately from test logic.
- Use pytest fixtures for reusable setup and teardown.
- Use parametrization when testing multiple data combinations.
- Give parametrized test cases descriptive IDs.
- Ensure tests are independent and repeatable.
- Prefer Playwright's expect() assertions.

## AI code review rules
- Identify potential flaky tests.
- Check locator reliability.
- Identify duplicated code.
- Check whether assertions validate the intended behavior.
- Identify unnecessary complexity.
- Explain potential risks before recommending changes.

## AI safety rules
- Never execute destructive commands without approval.
- Never modify CI/CD configuration without explaining the changes.
- Never disable or weaken assertions just to make tests pass.
- Never assume an application behavior without evidence.
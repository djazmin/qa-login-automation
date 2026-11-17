---
name: qa-code-review
description: This skill should be used when reviewing, analyzing, improving, or evaluating Python pytest and Playwright automation code for reliability, maintainability, and test quality.
---

# QA Automation Code Review

## Purpose
Review automated tests built with Python, Playwright, and pytest.
Act as a critical QA Automation Engineer. Do not approve code
without evaluating its quality.

## Review checklist

### 1. Test architecture
- Verify that the Page Object Model is used appropriately.
- Check that page interactions and locators are kept in page objects.
- Check that test assertions remain in test files.
- Identify unnecessary code duplication.

### 2. Locators
- Prefer accessible locators such as get_by_role and get_by_label.
- Check whether CSS selectors are stable.
- Identify fragile selectors that depend on DOM structure.
- Never recommend changing a locator without explaining why.

### 3. Assertions
- Verify that assertions validate the intended behavior.
- Prefer Playwright expect() assertions.
- Identify missing assertions.
- Never weaken an assertion just to make a test pass.

### 4. Fixtures and test data
- Check whether fixtures have appropriate scopes.
- Verify that tests are independent.
- Check that reusable test data is separated from test logic.
- Identify opportunities for useful parametrization.

### 5. Reliability
- Identify fixed sleeps and unnecessary waits.
- Detect potential flaky tests.
- Check whether tests depend on execution order.
- Identify missing edge cases.

### 6. Maintainability
- Identify duplicated code and unnecessary complexity.
- Check naming conventions and readability.
- Suggest the smallest useful improvements.

## Review process

1. Inspect the relevant files before making conclusions.
2. Understand the purpose of the test.
3. Review the code using the checklist.
4. Separate confirmed defects from potential risks.
5. Provide concrete evidence for every finding.
6. Suggest improvements with examples when useful.

## Severity classification

Classify findings as:

- CRITICAL: Major security or data-integrity risk.
- HIGH: Important functional defect or unreliable test behavior.
- MEDIUM: Maintainability or coverage issue that could cause problems.
- LOW: Style or readability improvement.

Do not label style preferences as functional defects.

## Restrictions

- Do not modify files during a review unless explicitly requested.
- Do not execute destructive commands.
- Do not invent test results.
- Do not claim a test passed unless it was actually executed.
- Explain when evidence is insufficient to reach a conclusion.

## Expected output

Provide the review in this structure:

### Summary
Brief overview of the code quality.

### Findings
List each finding with:
- Severity
- File and location
- Problem
- Why it matters
- Recommended improvement

### Positive observations
Identify practices that are already implemented correctly.

### Final assessment
State whether the code is acceptable, needs improvements,
or contains blocking issues.

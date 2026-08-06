# Playwright Python – BDD Login Test Suite

A test automation demo project showcasing end-to-end UI testing with **Playwright** and **Python**, using **Behave** for BDD (Behavior-Driven Development) with Gherkin feature files.

Built against [Practice Software Testing](https://practicesoftwaretesting.com) — an open-source QA training site — this project demonstrates real-world testing patterns including the Page Object Model, structured test hooks, screenshot capture on failure, and configurable browser execution.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| [Playwright](https://playwright.dev/python/) | Browser automation |
| [Behave](https://behave.readthedocs.io/) | BDD test runner (Gherkin/Cucumber-style) |
| [PyYAML](https://pyyaml.org/) | External test configuration |
| [behave-html-formatter](https://github.com/behave-contrib/behave-html-formatter) | HTML test reports |
| Python 3.13+ | Language runtime |

---

## Project Structure

```
playwright-python-sample/
├── features/
│   ├── login.feature          # Gherkin scenarios for login workflows
│   ├── environment.py         # Behave hooks (setup/teardown, screenshot on failure)
│   └── steps/
│       └── login_steps.py     # Step definitions wiring Gherkin to page actions
├── pages/
│   └── login_page.py          # Page Object Model for the login page
├── reports/
│   └── screenshots/           # Auto-captured screenshots on test failure
├── config.yaml                # Base URL and test credentials
├── behave.ini                 # Behave configuration
└── requirements.txt           # Python dependencies
```

---

## Key Features

- **Page Object Model (POM)** — UI interactions are encapsulated in `pages/login_page.py`, keeping step definitions clean and maintainable
- **BDD with Gherkin** — Human-readable `.feature` files describe test scenarios in plain English
- **Configurable execution** — Browser headless mode is controlled via the `HEADLESS` environment variable, making it CI-friendly
- **Screenshot on failure** — Failed scenarios automatically capture a timestamped full-page screenshot to `reports/screenshots/`
- **External config** — Base URL and credentials are loaded from `config.yaml`, keeping test data separate from test logic

---

## Test Scenarios

The `features/login.feature` file covers the following scenarios:

| # | Scenario |
|---|---|
| 1 | Successful login with valid credentials |
| 2 | Unsuccessful login with invalid credentials |
| 3 | Error message when email is not provided |
| 4 | Error message when password is not provided |
| 5 | Request a password reset |
| 6 | Password reset with an invalid email shows an error |
| 7 | Password reset without an email address shows an error |

---

## Getting Started

### Prerequisites

- Python 3.13+
- A terminal with `pip` available

### 1. Clone the repository

```bash
git clone https://github.com/Termx/playwright-python-sample.git
cd playwright-python-sample
```

### 2. Create and activate a virtual environment

```bash
# macOS / Linux
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
python -m playwright install
```

---

## Running Tests

Run the full test suite:

```bash
behave
```

Run a specific feature file:

```bash
behave features/login.feature
```

Run a specific scenario by line number:

```bash
behave features/login.feature:<line_number>
```

Run in headed mode (browser visible):

```bash
HEADLESS=false behave       # macOS / Linux
$env:HEADLESS="false"; behave  # Windows (PowerShell)
```

Generate an HTML report:

```bash
behave -f html -o reports/report.html
```

---

## Notes

- If you see `module not found` errors, ensure your virtual environment is activated and dependencies are installed within it.
- Screenshots from failed scenarios are saved automatically to `reports/screenshots/` with a timestamp and scenario name.
- The test site ([practicesoftwaretesting.com](https://practicesoftwaretesting.com)) is a publicly available QA training application — credentials in `config.yaml` are intentionally shared as part of that project.

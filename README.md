This project uses Playwright with Python (demo with pytest-bdd). The steps below get you up and running quickly.

Prerequisites:
- Python 3.13+ (recommanded)
- A Python virtual environment (optional but recommended).

Create and activate a virtual environment (optional but best practice):
```bash
# macOS / Linux
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```
Upgrade pip:
```bash
python -m pip install --upgrade pip
```

Install Dependencies

Install project requirements:
```bash
pip install -r requirements.txt
```
Install Playwright Browsers

Playwright requires browser binaries for Chromium, Firefox, and WebKit. Install them with:
```bash
python -m playwright install
```
This downloads the browser engines Playwright automates.

Running tests

With everything installed, run your BDD tests using Behave:
```bash
behave
```
To run a specific feature or scenario:
```bash
behave features/<name>.feature
behave features/<name>.feature:<line>
```

Tips & Notes:
- Using a virtual environment ensures your system Python stays clean.
- Playwright’s browser installation step needs internet access and disk space (~hundreds of MB).
- If you encounter “module not found” errors, double-check that your venv is activated and that Playwright is installed in that environment.
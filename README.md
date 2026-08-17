# 🚀 Python Selenium BDD Behave HTML-Reporting Automation Framework

### Production-Ready Python Selenium BDD Automation Framework

Build reliable, maintainable, and scalable UI automation using **Python, Selenium WebDriver, Behave, Gherkin, and HTML Reporting**.

⭐ If this project helps you, please consider giving it a Star!

---

# 📖 About

This repository provides a production-ready **Python Selenium BDD Automation Framework** built using:

* 🐍 Python
* 🌐 Selenium WebDriver
* 🥒 Behave
* 📝 Gherkin
* 📊 HTML Reporting
* 🧩 Page Object Model
* ⚙️ Configuration Management
* 🪝 Behave Hooks
* 📸 Screenshot Capture
* 🚀 CI/CD Friendly

The framework focuses on **simplicity, readability, maintainability, and reusability** without introducing unnecessary design patterns.

It is suitable for:

* Automation Engineers
* SDET Engineers
* Software Engineers
* Beginners learning BDD automation
* Enterprise UI automation projects

---

# ✨ Features

* 🐍 Python 3.x
* 🌐 Selenium WebDriver
* 🥒 BDD using Behave
* 📝 Gherkin Feature Files
* 🧩 Simple Page Object Model (POM)
* 📊 HTML Test Reports
* 📸 Automatic Screenshot on Failure
* 🔄 Reusable Utilities
* 🎯 Tag-Based Test Execution
* 🌐 Cross-Browser Execution
* 🧪 Positive & Negative Test Scenarios
* 🚀 CI/CD Friendly
* 🧹 Easy Maintenance
* 📁 Clean Project Structure

---

# 🏗 Framework Design

The framework intentionally follows a simple and practical architecture.

It uses:

* ✅ Page Object Model
* ✅ Behave BDD
* ✅ Gherkin language
* ✅ Reusable Utility Classes
* ✅ Configuration-Driven Execution
* ✅ Hooks for Setup and Teardown
* ✅ Allure Reporting

The goal is to keep the framework:

> **Simple to understand → Easy to maintain → Easy to extend → Ready for CI/CD**

---

# 🥒 BDD with Behave

Behave enables the framework to follow **Behavior Driven Development (BDD)** using Gherkin syntax.

Example:

The Gherkin scenario is connected to Python step definitions.

```text
Feature File
     │
     ▼
Step Definitions
     │
     ▼
Page Objects
     │
     ▼
Selenium WebDriver
     │
     ▼
Web Application
```

---

# 🧩 Page Object Model

The framework uses a simple **Page Object Model (POM)** approach.

Each application page contains its:

* Locators
* Page actions
* Element interactions
* Page-specific validations

---

# 📊 HTML Reporting

The framework supports HTML-based execution reporting.

Reports can provide:

* Test execution summary
* Passed scenarios
* Failed scenarios
* Skipped scenarios
* Scenario details
* Step execution status
* Execution duration
* Failure information
* Screenshots for failed scenarios
---

# 📸 Screenshot on Failure

When a scenario fails, the framework can automatically capture a screenshot.

Example:

```text
reports/
└── screenshots/
    ├── login_invalid_password.png
    ├── checkout_payment_failure.png
    └── registration_validation_failure.png
```

This makes debugging failed UI tests significantly easier.

---

# 🌐 Cross-Browser Testing

The framework can be configured to execute tests against multiple browsers.

Supported browsers can include:

* Google Chrome
* Microsoft Edge

---

# 🏷 Tag-Based Test Execution

Behave tags can be used to organize and selectively execute scenarios.

Example:

```gherkin
@smoke
Scenario: Successful login
```

```gherkin
@regression
Scenario: Invalid login
```

Execute smoke tests:

```bash
behave --tags=smoke
```

Execute regression tests:

```bash
behave --tags=regression
```

Execute multiple tags:

```bash
behave --tags="smoke or regression"
```

---

# 📊 Data-Driven Testing

The framework is designed to support data-driven scenarios.

Example:

```gherkin
Scenario Outline: Login with different credentials

  Given the user is on the login page
  When the user enters "<username>" and "<password>"
  And clicks the login button
  Then the login result should be "<result>"

Examples:
  | username | password | result  |
  | user1    | pass1    | success |
  | user2    | wrong    | failure |
```

This allows multiple test conditions to be executed using a single scenario definition.

---

# 📂 Project Structure

```text
Automation_Python_Selenium_BDD_Behave_Reporting/
│
├── features/
│   │
│   ├── environment.py
│   │
│   ├── steps/
│   │   ├── login_steps.py
│   │   └── user_steps.py
│   │
│   ├── pages/
│   │   ├── login_page.py
│   │   └── home_page.py
│   │
│   ├── utils/
│   │   ├── driver_factory.py
│   │   ├── config_reader.py
│   │   ├── logger.py
│   │   └── screenshot.py
│   │
│   └── login.feature
│
├── config/
│   └── config.ini
│
├── reports/
│   ├── report.html
│   ├── screenshots/
│   └── logs/
│
├── requirements.txt
├── behave.ini
├── pytest.ini
├── .gitignore
└── README.md
```

---

# 🔄 Framework Execution Flow

```text
                 ┌──────────────────────┐
                 │   Gherkin Feature    │
                 │        File          │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Behave Runner      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Step Definitions    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    Page Objects      │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Selenium WebDriver   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Web Application    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Reports / Screenshots│
                 │       / Logs         │
                 └──────────────────────┘
```

# 💻 Prerequisites

Install the following before running the framework:

* Python 3.x
* pip
* Git
* Chrome / Edge
* IDE such as:

  * PyCharm
  * VS Code


# 🚀 Getting Started

## 1️⃣ Clone Repository

```bash
git clone https://github.com/imademethink/Automation_Java_Playwright_BDD_Cucumber_TestNG_Reporting_Maven.git
```

Navigate to the project:

```bash
cd Automation_Java_Playwright_BDD_Cucumber_TestNG_Reporting_Maven
```
Create environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install packages:

```bash
pip install -r requirements.txt
```

Run all tests:

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped
```


Generate Allure Reports:

```bash
allure serve allure-report
```

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Execute Tests

---

# 📊 Generate HTML Report

Example:

```bash
behave -f html -o reports/report.html
```

After execution:

```text
reports/
└── report.html
```

Open the generated HTML report in a browser.

---

# 🧪 Test Execution Examples

### Run Specific Scenario

```bash
behave -f allure_behave.formatter:AllureFormatter -o allure-report  -f plain  --no-skipped

allure serve allure-report
```


# 🔐 Environment Management

Different environments can be supported through configuration.

Example:

```text
config/
├── config.dev.ini
├── config.qa.ini
├── config.stage.ini
└── config.prod.ini
```

Example execution:

```bash
behave -D environment=qa
```

---

# 🧹 Clean Framework Principles

The framework follows a few simple principles:

### Feature Files

Contain business-readable scenarios.

### Step Definitions

Contain BDD step implementations.

### Page Objects

Contain Selenium interactions.

### Utilities

Contain reusable technical functionality.

### Hooks

Contain test lifecycle operations.

### Configuration

Contains environment-specific settings.

This separation prevents feature files from becoming tightly coupled with Selenium implementation.
---

# 📚 Learning Outcomes

This repository demonstrates:

* Python UI automation
* Selenium WebDriver
* BDD automation
* Behave
* Gherkin
* Page Object Model
* Test lifecycle management
* Behave hooks
* HTML reporting
* Screenshot handling
* Logging
* Configuration management
* Cross-browser testing
* Tag-based execution
* Data-driven testing
* CI/CD integration
* Maintainable automation framework design

---

# 🎓 Suitable For

This framework can be used by:

* Beginners learning Selenium with Python
* QA Automation Engineers
* SDETs
* Software Engineers
* Test Automation Leads
* QA Managers
* Teams building BDD automation frameworks
* Teams migrating from Selenium Java to Selenium Python

---

# 🤝 Contributing

Contributions are welcome!

Feel free to:

* ⭐ Star the repository
* 🍴 Fork the project
* 🐞 Report issues
* 💡 Suggest improvements
* 🚀 Submit Pull Requests

---

# 🗺️ Future Roadmap

Potential future enhancements:

* API Automation
* Database Validation
* Allure Reporting
* Extent-style reporting
* Docker Support
* Parallel Execution
* Retry Mechanism
* Selenium Grid
* Remote Browser Execution
* Cloud Browser Execution
* GitHub Actions Pipeline
* Jenkins Pipeline
* Azure DevOps Pipeline
* Test Data Management
* Excel-Based Test Data
* JSON-Based Test Data
* Environment Management
* Secret Management
* Advanced Failure Diagnostics

---

# 🌟 Why This Framework?

The framework is designed around a simple philosophy:

```text
Readable BDD
     +
Clean Python
     +
Reusable Page Objects
     +
Reliable Selenium
     +
Useful Reporting
     +
Simple Configuration
     =
Maintainable Automation
```

No unnecessary framework complexity.

No excessive design patterns.

Just a clean and practical automation architecture that teams can understand, maintain, and extend.

---

# 📌 Useful Commands

| Purpose              | Command                                 |
| -------------------- | --------------------------------------- |
| Install dependencies | `pip install -r requirements.txt`       |
| Run all tests        | `behave`                                |
| Run smoke tests      | `behave --tags=smoke`                   |
| Run regression       | `behave --tags=regression`              |
| Run feature          | `behave features/login.feature`         |
| Run scenario         | `behave --name "Scenario Name"`         |
| Select browser       | `behave -D browser=chrome`              |
| Generate HTML report | `behave -f html -o reports/report.html` |

---

# ❤️ Community

If you find this framework useful:

⭐ **Star the repository**

🍴 **Fork the repository**

🐞 **Report issues**

💡 **Suggest improvements**

🚀 **Contribute**

---

### Made with ❤️ for the Automation Testing Community

**Python • Selenium • Behave • Gherkin • BDD • HTML Reporting**

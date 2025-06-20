# Python for Testers - Automated Testing Framework

A comprehensive automated testing framework built with Python, Selenium, and Allure reporting. This project demonstrates various testing approaches including Web UI testing, API testing, and Page Object Model implementation.

## 📁 Project Structure

```
pythonfortesters/
├── .github/workflows/           # GitHub Actions CI/CD workflows
│   └── test-and-report.yml     # Main workflow for testing and reporting
├── practiceautomatedtesting/    # Main testing framework
│   ├── webelements/            # Web UI automation tests
│   │   ├── conftest.py         # Pytest configuration and fixtures
│   │   ├── test_*.py           # Individual test files for web elements
│   │   ├── downloads/          # Downloaded files from tests
│   │   └── allure-results/     # Local Allure test results
│   ├── shopping/               # Page Object Model implementation
│   │   ├── pages/              # Page Object classes
│   │   ├── tests/              # Shopping cart tests
│   │   ├── conftest.py         # Shopping-specific configuration
│   │   └── requirements.txt    # Shopping test dependencies
│   └── api/                    # API testing framework
│       ├── tests/              # API test files
│       ├── requirements.txt    # API test dependencies
│       └── README.md           # API testing documentation
├── examples/                   # Python learning examples
│   └── examples/               # Basic Python concepts
├── allure-results/             # Global Allure test results
├── allure-report/              # Generated Allure reports
├── allure-report-static/       # Static Allure reports
├── run_tests.py               # Local test runner script
└── README.md                  # This file
```

## 🚀 How It Works

### 1. Test Categories

#### **WebElements Testing** (`practiceautomatedtesting/webelements/`)
- **Purpose**: Tests various web UI elements and interactions
- **Technology**: Selenium WebDriver with Chrome
- **Test Coverage**: 20+ different web element types including:
  - Links, Checkboxes, Radio buttons
  - Forms, Tables, Modals, Tabs
  - Drag & Drop, File upload/download
  - Geolocation, Hover effects, Tooltips
  - Progress bars, Sliders, Date pickers
  - Shadow DOM, Frames, Broken links

#### **Shopping Cart Testing** (`practiceautomatedtesting/shopping/`)
- **Purpose**: E-commerce functionality testing
- **Pattern**: Page Object Model (POM)
- **Structure**:
  - `pages/`: Page Object classes for UI elements
  - `tests/`: Test scenarios using Page Objects
  - `conftest.py`: Shopping-specific test configuration

#### **API Testing** (`practiceautomatedtesting/api/`)
- **Purpose**: REST API endpoint testing
- **Technology**: Requests library with pytest
- **Features**: Authentication, CRUD operations, data validation

### 2. CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/test-and-report.yml`) provides:

#### **Automated Test Execution**
- **Triggers**: Push to main, Pull requests, Manual dispatch
- **Environment**: Ubuntu with Python 3.11
- **Parallel Execution**: 2 workers per test suite
- **Headless Mode**: Chrome in headless mode for CI

#### **Test Execution Flow**
1. **Setup**: Install dependencies, Chrome, Allure CLI
2. **WebElements Tests**: Run UI automation tests
3. **Shopping Tests**: Execute Page Object Model tests
4. **API Tests**: Perform API endpoint testing
5. **Report Generation**: Create Allure reports with history

#### **Artifact Management**
- **Test Results**: Uploaded as artifacts for 30 days
- **Allure Reports**: Available as downloadable artifacts
- **History**: Maintained for trend analysis
- **GitHub Pages**: Automatic deployment of reports

### 3. Allure Reporting

#### **Features**
- **Comprehensive Reports**: Detailed test execution results
- **Screenshot Capture**: Automatic screenshots on test failures
- **History & Trends**: Track test performance over time
- **Environment Info**: Browser and platform details
- **Test Categories**: Organized by features and severity

#### **Report Access**
- **GitHub Pages**: Live reports at repository Pages URL
- **Artifacts**: Downloadable from GitHub Actions
- **Local Generation**: Run `allure serve allure-results/`

### 4. Configuration Files

#### **conftest.py** (WebElements)
- **WebDriver Setup**: Chrome configuration for local and CI
- **Screenshot Capture**: Automatic failure screenshots
- **Environment Detection**: Headless mode for CI
- **Allure Integration**: Environment info and metadata

#### **requirements.txt** (Shopping & API)
- **Dependencies**: Specific packages for each test suite
- **Version Control**: Pinned versions for stability
- **Separation**: Isolated dependencies per test category

## 🛠️ Local Development

### Prerequisites
- Python 3.11+
- Chrome browser
- Git

### Setup
```bash
# Clone the repository
git clone <repository-url>
cd pythonfortesters

# Install dependencies for each test suite
pip install -r practiceautomatedtesting/webelements/requirements.txt
pip install -r practiceautomatedtesting/shopping/requirements.txt
pip install -r practiceautomatedtesting/api/requirements.txt

# Install Allure CLI (macOS)
brew install allure

# Install Allure CLI (Linux)
wget -qO- https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.0/allure-commandline-2.24.0.tgz | tar -xz -C /opt/
sudo ln -s /opt/allure-2.24.0/bin/allure /usr/local/bin/allure
```

### Running Tests Locally

#### **All Test Suites**
```bash
python run_tests.py
```

#### **Individual Test Suites**
```bash
# WebElements tests
cd practiceautomatedtesting/webelements
pytest --alluredir=allure-results -v

# Shopping tests
cd practiceautomatedtesting/shopping
pytest --alluredir=allure-results -v

# API tests
cd practiceautomatedtesting/api
pytest --alluredir=allure-results -v
```

#### **Specific Test Files**
```bash
# Run specific test file
pytest test_links.py -v

# Run tests with specific markers
pytest -m "critical" -v

# Run tests in parallel
pytest -n 2 --dist=loadfile -v
```

### Viewing Reports
```bash
# Generate and serve Allure report
allure generate allure-results --clean -o allure-report
allure open allure-report

# Or serve directly
allure serve allure-results
```

## 🔧 Key Features

### **Parallel Test Execution**
- Uses `pytest-xdist` for parallel execution
- 2 workers per test suite for optimal performance
- Load file distribution for better test isolation

### **Screenshot Capture**
- Automatic screenshots on test failures
- Attached to Allure reports
- Manual screenshot capture available

### **History & Trends**
- Maintains test execution history
- Shows trends over multiple runs
- Helps identify flaky tests

### **Environment Flexibility**
- Works in local development
- Optimized for CI/CD environments
- Headless mode support

### **Error Handling**
- Graceful failure handling
- Continue-on-error for non-critical tests
- Detailed error reporting

## 📊 Test Results

### **Accessing Results**
1. **GitHub Actions**: Check the Actions tab for latest runs
2. **Artifacts**: Download reports from successful runs
3. **GitHub Pages**: View live reports at repository Pages URL
4. **Local**: Run `allure serve allure-results/`

### **Report Features**
- **Test Overview**: Summary of all test executions
- **Detailed Results**: Step-by-step test execution
- **Screenshots**: Visual evidence of failures
- **Environment Info**: Browser and platform details
- **Trends**: Historical performance data

## 🤝 Contributing

### **Adding New Tests**
1. Create test file in appropriate directory
2. Follow naming convention: `test_*.py`
3. Use appropriate fixtures and configurations
4. Add Allure decorators for better reporting

### **Test Structure**
```python
import pytest
import allure

@allure.epic("Test Category")
@allure.feature("Feature Name")
@allure.story("Test Story")
@allure.severity(allure.severity_level.CRITICAL)
def test_example(driver):
    with allure.step("Test step description"):
        # Test implementation
        pass
```

### **Page Object Model** (for UI tests)
```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login")
    
    def login(self, username, password):
        # Implementation
        pass
```

## 📝 Notes

- **ChromeDriver**: Automatically managed by `webdriver-manager`
- **Headless Mode**: Enabled in CI, can be toggled locally
- **Timeout Handling**: 300-second timeout per test
- **Artifact Retention**: 30 days for reports, 7 days for history
- **Concurrency**: GitHub Pages deployment uses concurrency control

This framework provides a solid foundation for automated testing with comprehensive reporting and CI/CD integration.

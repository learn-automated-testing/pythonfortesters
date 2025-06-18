# Allure Test Reports

This repository automatically generates and deploys Allure test reports to GitHub Pages.

## 📊 Accessing Reports

### **GitHub Pages URL**
Once the workflow completes successfully, you can access the latest Allure report at:
```
https://learnautomatedtesting.github.io/pythonfortestersu/
```

### **How it works**
1. **Tests run** on every push to main/master branch
2. **Allure reports** are generated automatically
3. **GitHub Pages** are updated with the latest report
4. **Public URL** becomes available for easy access

## 🔄 Workflow Process

### **1. Test Execution** (`.github/workflows/test-and-report.yml`)
- Runs pytest tests from `practiceautomatedtesting/` directory
- Generates Allure-compatible test results
- Creates HTML reports and uploads as artifacts

### **2. GitHub Pages Deployment** (`.github/workflows/deploy-allure-pages.yml`)
- Triggers after successful test completion
- Downloads the Allure report artifact
- Deploys to GitHub Pages automatically

## 📁 Report Structure

The Allure report includes:
- **Test Overview** - Summary of all test suites
- **Detailed Results** - Individual test results with screenshots
- **Trends** - Historical test performance
- **Categories** - Failed, broken, skipped tests
- **Timeline** - Test execution timeline

## 🛠️ Local Development

To generate reports locally:
```bash
# Install Allure
brew install allure  # macOS
# or download from https://github.com/allure-framework/allure2/releases

# Run tests and generate report
cd practiceautomatedtesting/webelements
pytest --alluredir=../../allure-results/webelements

# Generate and serve report
allure serve allure-results
```

## 📈 Benefits

- **Always up-to-date** - Reports update automatically
- **Public access** - Share with team members easily
- **No downloads needed** - View directly in browser
- **Historical data** - Track test trends over time
- **Beautiful UI** - Professional test reporting interface 
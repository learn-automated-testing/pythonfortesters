#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
from datetime import datetime

def run_command(command, cwd=None, env=None):
    """Run a command and return its output"""
    try:
        result = subprocess.run(command, cwd=cwd, env=env, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Error: {e.stderr}"

def setup_allure_results():
    """Create or clean allure-results directory"""
    results_dir = "allure-results"
    if os.path.exists(results_dir):
        shutil.rmtree(results_dir)
    os.makedirs(results_dir)
    return results_dir

def setup_api_env():
    """Setup API test environment"""
    api_env = os.environ.copy()
    api_env.update({
        "API_BASE_URL": "https://api.practiceautomatedtesting.com",
        "API_USERNAME": "admin",
        "API_PASSWORD": "password123"
    })
    return api_env

def run_tests():
    """Run all test suites and generate Allure report"""
    # Setup allure results directory
    results_dir = setup_allure_results()
    
    # Get current timestamp for report name
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = f"allure-report_{timestamp}"
    
    # Run Selenium tests
    print("\n=== Running Selenium Tests ===")
    success, output = run_command(
        ["python3", "-m", "pytest", "practiceautomatedtesting/shopping/tests/", "-v", f"--alluredir={results_dir}"],
        cwd=os.getcwd()
    )
    print(output)
    if not success:
        print("Selenium tests failed!")
        return False
    
    # Setup API environment
    api_env = setup_api_env()
    
    # Run API tests
    print("\n=== Running API Tests ===")
    success, output = run_command(
        ["python3", "-m", "pytest", "practiceautomatedtesting/api/tests/", "-v", f"--alluredir={results_dir}"],
        cwd=os.getcwd(),
        env=api_env
    )
    print(output)
    if not success:
        print("API tests failed!")
        return False
    
    # Generate Allure report
    print("\n=== Generating Allure Report ===")
    success, output = run_command(
        ["allure", "generate", results_dir, "-o", report_dir, "--clean"]
    )
    print(output)
    if not success:
        print("Failed to generate Allure report!")
        return False
    
    # Open the report in default browser
    print("\n=== Opening Allure Report ===")
    success, output = run_command(
        ["open", f"{report_dir}/index.html"]
    )
    
    return True

if __name__ == "__main__":
    print("Starting test execution...")
    if run_tests():
        print("\nAll tests completed successfully!")
    else:
        print("\nTest execution failed!")
        sys.exit(1) 
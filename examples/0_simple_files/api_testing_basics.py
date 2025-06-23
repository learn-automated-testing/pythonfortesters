# API Testing Basics - Building on HTTP Requests

import requests
import json
import time
from datetime import datetime

class APITestFramework:
    def __init__(self, base_url="https://httpbin.org"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'APITestFramework/1.0',
            'Accept': 'application/json'
        })
        self.test_results = []
    
    def log_test(self, test_name, status, response_time, details=""):
        """Log test results"""
        test_result = {
            "test_name": test_name,
            "status": status,
            "response_time": response_time,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        self.test_results.append(test_result)
        print(f"✓ {test_name}: {status} ({response_time:.2f}s)")
    
    def test_get_request(self):
        """Test GET request"""
        print("=== Testing GET Request ===\n")
        
        start_time = time.time()
        try:
            response = self.session.get(f"{self.base_url}/get")
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            assert "application/json" in response.headers.get('content-type', ''), "Expected JSON response"
            
            data = response.json()
            assert 'url' in data, "Response should contain 'url' field"
            
            self.log_test("GET Request", "PASS", response_time, f"URL: {data['url']}")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("GET Request", "FAIL", response_time, str(e))
    
    def test_post_request(self):
        """Test POST request with JSON data"""
        print("=== Testing POST Request ===\n")
        
        test_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30,
            "skills": ["Python", "API Testing", "Selenium"]
        }
        
        start_time = time.time()
        try:
            response = self.session.post(f"{self.base_url}/post", json=test_data)
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            data = response.json()
            assert 'json' in data, "Response should contain 'json' field"
            assert data['json']['name'] == test_data['name'], "Name should match"
            assert data['json']['email'] == test_data['email'], "Email should match"
            
            self.log_test("POST Request", "PASS", response_time, f"Sent: {test_data['name']}")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("POST Request", "FAIL", response_time, str(e))
    
    def test_put_request(self):
        """Test PUT request"""
        print("=== Testing PUT Request ===\n")
        
        update_data = {"status": "updated", "timestamp": datetime.now().isoformat()}
        
        start_time = time.time()
        try:
            response = self.session.put(f"{self.base_url}/put", json=update_data)
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            data = response.json()
            assert 'json' in data, "Response should contain 'json' field"
            
            self.log_test("PUT Request", "PASS", response_time, f"Updated: {update_data['status']}")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("PUT Request", "FAIL", response_time, str(e))
    
    def test_delete_request(self):
        """Test DELETE request"""
        print("=== Testing DELETE Request ===\n")
        
        start_time = time.time()
        try:
            response = self.session.delete(f"{self.base_url}/delete")
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            data = response.json()
            assert 'url' in data, "Response should contain 'url' field"
            
            self.log_test("DELETE Request", "PASS", response_time, "Resource deleted")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("DELETE Request", "FAIL", response_time, str(e))
    
    def test_status_codes(self):
        """Test different HTTP status codes"""
        print("=== Testing Status Codes ===\n")
        
        status_tests = [
            (200, "OK"),
            (201, "Created"),
            (400, "Bad Request"),
            (401, "Unauthorized"),
            (403, "Forbidden"),
            (404, "Not Found"),
            (500, "Internal Server Error")
        ]
        
        for status_code, description in status_tests:
            start_time = time.time()
            try:
                response = self.session.get(f"{self.base_url}/status/{status_code}")
                response_time = time.time() - start_time
                
                # For error status codes, we expect them to be returned
                if status_code >= 400:
                    # These should actually return the status code we requested
                    assert response.status_code == status_code, f"Expected {status_code}, got {response.status_code}"
                    self.log_test(f"Status {status_code}", "PASS", response_time, description)
                else:
                    # Success codes should work normally
                    assert response.status_code == status_code, f"Expected {status_code}, got {response.status_code}"
                    self.log_test(f"Status {status_code}", "PASS", response_time, description)
                    
            except Exception as e:
                response_time = time.time() - start_time
                self.log_test(f"Status {status_code}", "FAIL", response_time, str(e))
    
    def test_response_headers(self):
        """Test response headers"""
        print("=== Testing Response Headers ===\n")
        
        start_time = time.time()
        try:
            response = self.session.get(f"{self.base_url}/headers")
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            data = response.json()
            assert 'headers' in data, "Response should contain 'headers' field"
            
            # Check for common headers
            headers = data['headers']
            assert 'User-Agent' in headers, "User-Agent header should be present"
            assert 'Accept' in headers, "Accept header should be present"
            
            self.log_test("Response Headers", "PASS", response_time, f"Found {len(headers)} headers")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("Response Headers", "FAIL", response_time, str(e))
    
    def test_query_parameters(self):
        """Test query parameters"""
        print("=== Testing Query Parameters ===\n")
        
        params = {
            'name': 'John',
            'age': '30',
            'city': 'New York',
            'skills': ['python', 'selenium', 'api']
        }
        
        start_time = time.time()
        try:
            response = self.session.get(f"{self.base_url}/get", params=params)
            response_time = time.time() - start_time
            
            # Assertions
            assert response.status_code == 200, f"Expected 200, got {response.status_code}"
            
            data = response.json()
            assert 'args' in data, "Response should contain 'args' field"
            
            # Check query parameters
            args = data['args']
            assert args['name'] == params['name'], "Name parameter should match"
            assert args['age'] == params['age'], "Age parameter should match"
            assert args['city'] == params['city'], "City parameter should match"
            
            self.log_test("Query Parameters", "PASS", response_time, f"Params: {list(params.keys())}")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("Query Parameters", "FAIL", response_time, str(e))
    
    def test_authentication(self):
        """Test basic authentication"""
        print("=== Testing Authentication ===\n")
        
        username = "testuser"
        password = "testpass"
        
        start_time = time.time()
        try:
            response = self.session.get(f"{self.base_url}/basic-auth/{username}/{password}")
            response_time = time.time() - start_time
            
            # This should fail without authentication
            assert response.status_code == 401, f"Expected 401, got {response.status_code}"
            
            # Now try with authentication
            auth_response = requests.get(
                f"{self.base_url}/basic-auth/{username}/{password}",
                auth=(username, password)
            )
            
            assert auth_response.status_code == 200, f"Expected 200, got {auth_response.status_code}"
            
            auth_data = auth_response.json()
            assert auth_data['authenticated'] == True, "Should be authenticated"
            assert auth_data['user'] == username, "Username should match"
            
            self.log_test("Authentication", "PASS", response_time, f"User: {username}")
            
        except Exception as e:
            response_time = time.time() - start_time
            self.log_test("Authentication", "FAIL", response_time, str(e))
    
    def generate_test_report(self):
        """Generate a test report"""
        print("\n=== Test Report ===")
        print(f"Total Tests: {len(self.test_results)}")
        
        passed = sum(1 for result in self.test_results if result['status'] == 'PASS')
        failed = len(self.test_results) - passed
        
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Success Rate: {(passed/len(self.test_results)*100):.1f}%")
        
        # Save report to file
        report_data = {
            "summary": {
                "total_tests": len(self.test_results),
                "passed": passed,
                "failed": failed,
                "success_rate": (passed/len(self.test_results)*100)
            },
            "tests": self.test_results
        }
        
        with open('api_test_report.json', 'w') as f:
            json.dump(report_data, f, indent=2)
        
        print(f"\nDetailed report saved to: api_test_report.json")
    
    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting API Test Suite\n")
        
        self.test_get_request()
        self.test_post_request()
        self.test_put_request()
        self.test_delete_request()
        self.test_status_codes()
        self.test_response_headers()
        self.test_query_parameters()
        self.test_authentication()
        
        self.generate_test_report()

# Run the tests
if __name__ == "__main__":
    api_tester = APITestFramework()
    api_tester.run_all_tests() 
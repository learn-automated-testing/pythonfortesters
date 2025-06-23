# Web Automation Introduction - Building Blocks for Selenium

import requests
from urllib.parse import urljoin, urlparse
import time

# Basic HTTP requests - Foundation for API testing
def basic_http_requests():
    print("=== Basic HTTP Requests ===\n")
    
    # GET request
    response = requests.get('https://httpbin.org/get')
    print(f"GET Status Code: {response.status_code}")
    print(f"Response Headers: {dict(response.headers)}")
    print(f"Response JSON: {response.json()}\n")
    
    # POST request
    data = {'name': 'John', 'age': 30}
    response = requests.post('https://httpbin.org/post', json=data)
    print(f"POST Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}\n")
    
    # PUT request
    response = requests.put('https://httpbin.org/put', json={'status': 'updated'})
    print(f"PUT Status Code: {response.status_code}\n")
    
    # DELETE request
    response = requests.delete('https://httpbin.org/delete')
    print(f"DELETE Status Code: {response.status_code}\n")

# URL handling - Important for web automation
def url_operations():
    print("=== URL Operations ===\n")
    
    base_url = "https://example.com"
    relative_path = "/api/users"
    
    # Join URLs
    full_url = urljoin(base_url, relative_path)
    print(f"Full URL: {full_url}")
    
    # Parse URL
    parsed = urlparse(full_url)
    print(f"Scheme: {parsed.scheme}")
    print(f"Domain: {parsed.netloc}")
    print(f"Path: {parsed.path}")
    
    # Build query parameters
    params = {'page': 1, 'limit': 10}
    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    url_with_params = f"{full_url}?{query_string}"
    print(f"URL with params: {url_with_params}\n")

# Response handling - Essential for automation
def handle_responses():
    print("=== Response Handling ===\n")
    
    # Successful request
    try:
        response = requests.get('https://httpbin.org/status/200')
        response.raise_for_status()  # Raises exception for 4XX/5XX status codes
        print("Request successful!")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    
    # Failed request
    try:
        response = requests.get('https://httpbin.org/status/404')
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"Expected HTTP Error: {e}")
    
    # Timeout handling
    try:
        response = requests.get('https://httpbin.org/delay/3', timeout=1)
    except requests.exceptions.Timeout:
        print("Request timed out (expected)")

# Session management - Important for maintaining state
def session_management():
    print("=== Session Management ===\n")
    
    # Create a session
    session = requests.Session()
    
    # Set default headers
    session.headers.update({
        'User-Agent': 'MyTestBot/1.0',
        'Accept': 'application/json'
    })
    
    # Make requests with session
    response1 = session.get('https://httpbin.org/headers')
    print(f"First request headers: {response1.json()['headers']}\n")
    
    response2 = session.get('https://httpbin.org/headers')
    print(f"Second request headers: {response2.json()['headers']}\n")

# Rate limiting simulation - Good practice for web scraping
def rate_limited_requests():
    print("=== Rate Limited Requests ===\n")
    
    urls = [
        'https://httpbin.org/get',
        'https://httpbin.org/status/200',
        'https://httpbin.org/headers'
    ]
    
    for i, url in enumerate(urls, 1):
        print(f"Request {i}: {url}")
        response = requests.get(url)
        print(f"Status: {response.status_code}")
        
        # Wait between requests (rate limiting)
        if i < len(urls):
            print("Waiting 1 second...")
            time.sleep(1)
        print()

# Practical example: Simple web scraper
def simple_web_scraper():
    print("=== Simple Web Scraper ===\n")
    
    try:
        # Get a simple HTML page
        response = requests.get('https://httpbin.org/html')
        response.raise_for_status()
        
        # Extract title from HTML (basic parsing)
        html_content = response.text
        if '<title>' in html_content and '</title>' in html_content:
            start = html_content.find('<title>') + 7
            end = html_content.find('</title>')
            title = html_content[start:end]
            print(f"Page title: {title}")
        
        print(f"Content length: {len(html_content)} characters")
        
    except Exception as e:
        print(f"Error scraping: {e}")

# Run all examples
if __name__ == "__main__":
    basic_http_requests()
    url_operations()
    handle_responses()
    session_management()
    rate_limited_requests()
    simple_web_scraper() 
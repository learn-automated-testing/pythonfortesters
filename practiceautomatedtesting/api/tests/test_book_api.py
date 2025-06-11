import pytest
import requests
import allure

BASE_PATH = "/v1/practice/books"

# Example books for testing
EXAMPLE_BOOKS = [
    {
        "title": "Python Test Book 1",
        "author": "Test Author 1",
        "price": 12.99,
        "description": "A book created by Python tests.",
        "category": "Testing",
        "isbn": "1234567890",
        "stock": 10
    },
    {
        "title": "Python Test Book 2",
        "author": "Test Author 2",
        "price": 24.99,
        "description": "Another book for testing.",
        "category": "Development",
        "isbn": "0987654321",
        "stock": 15
    }
]

@allure.epic("Book API")
@allure.feature("Book Management")
class TestBookAPI:
    @pytest.fixture(autouse=True)
    def setup(self, api_client):
        """Setup and cleanup for each test"""
        self.client = api_client
        self.created_book_ids = []
        yield
        # Cleanup: Delete all created books
        for book_id in self.created_book_ids:
            try:
                self.client.delete(f"{self.client.base_url}{BASE_PATH}/{book_id}")
            except:
                pass

    @allure.story("Get Books")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - Basic")
    def test_get_all_books_basic(self):
        """Test GET all books - Basic"""
        with allure.step("Get all books"):
            response = self.client.get(f"{self.client.base_url}{BASE_PATH}")
            assert response.ok
            books = response.json()
            assert isinstance(books, list)

    @allure.story("Search Books")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - With Search Query")
    def test_get_all_books_with_search(self):
        """Test GET all books - With Search Query"""
        with allure.step("Create a book with specific title"):
            create_response = self.client.post(
                f"{self.client.base_url}{BASE_PATH}",
                json=EXAMPLE_BOOKS[0]
            )
            assert create_response.ok
            created_book = create_response.json()
            self.created_book_ids.append(created_book["id"])

        with allure.step("Search for the book"):
            search_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?q=Python Test Book 1")
            assert search_response.ok
            search_results = search_response.json()
            assert len(search_results) > 0
            assert "Python Test Book 1" in search_results[0]["title"]

    @allure.story("Filter Books")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - With Category Filter")
    def test_get_all_books_with_category(self):
        """Test GET all books - With Category Filter"""
        with allure.step("Get books by category"):
            response = self.client.get(f"{self.client.base_url}{BASE_PATH}?category=Testing")
            assert response.ok
            books = response.json()
            for book in books:
                assert book["category"] == "Testing"

    @allure.story("Filter Books")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - With Price Range")
    def test_get_all_books_with_price_range(self):
        """Test GET all books - With Price Range"""
        with allure.step("Get books by price range"):
            response = self.client.get(f"{self.client.base_url}{BASE_PATH}?min_price=10&max_price=20")
            assert response.ok
            books = response.json()
            for book in books:
                assert 10 <= book["price"] <= 20

    @allure.story("Sort Books")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - With Sorting")
    def test_get_all_books_with_sorting(self):
        """Test GET all books - With Sorting"""
        with allure.step("Test ascending sort"):
            asc_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?sort=price&order=asc")
            assert asc_response.ok
            asc_books = asc_response.json()
            for i in range(1, len(asc_books)):
                assert asc_books[i]["price"] >= asc_books[i-1]["price"]

        with allure.step("Test descending sort"):
            desc_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?sort=price&order=desc")
            assert desc_response.ok
            desc_books = desc_response.json()
            for i in range(1, len(desc_books)):
                assert desc_books[i]["price"] <= desc_books[i-1]["price"]

    @allure.story("Pagination")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET all books - With Pagination")
    def test_get_all_books_with_pagination(self):
        """Test GET all books - With Pagination"""
        with allure.step("Get initial count of books"):
            initial_response = self.client.get(f"{self.client.base_url}{BASE_PATH}")
            assert initial_response.ok
            initial_books = initial_response.json()
            initial_count = len(initial_books)

        with allure.step("Create multiple books"):
            for book in EXAMPLE_BOOKS:
                create_response = self.client.post(f"{self.client.base_url}{BASE_PATH}", json=book)
                assert create_response.ok
                created_book = create_response.json()
                self.created_book_ids.append(created_book["id"])

        with allure.step("Test skip"):
            skip_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?skip=1")
            assert skip_response.ok
            skip_books = skip_response.json()
            assert len(skip_books) <= initial_count + len(self.created_book_ids)

        with allure.step("Test limit"):
            limit_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?limit=1")
            assert limit_response.ok
            limit_books = limit_response.json()
            assert len(limit_books) <= 1

        with allure.step("Test skip and limit together"):
            paginated_response = self.client.get(f"{self.client.base_url}{BASE_PATH}?skip=1&limit=1")
            assert paginated_response.ok
            paginated_books = paginated_response.json()
            assert len(paginated_books) <= 1

    @allure.story("Create Book")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test POST create book")
    def test_create_book(self):
        """Test POST create book"""
        with allure.step("Create a new book"):
            response = self.client.post(f"{self.client.base_url}{BASE_PATH}", json=EXAMPLE_BOOKS[0])
            assert response.ok
            book = response.json()
            assert book["title"] == EXAMPLE_BOOKS[0]["title"]
            assert "id" in book
            self.created_book_ids.append(book["id"])

    @allure.story("Get Book")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Test GET single book")
    def test_get_single_book(self):
        """Test GET single book"""
        with allure.step("Create a book first"):
            create_response = self.client.post(f"{self.client.base_url}{BASE_PATH}", json=EXAMPLE_BOOKS[0])
            assert create_response.ok
            created_book = create_response.json()
            self.created_book_ids.append(created_book["id"])

        with allure.step("Get the created book"):
            response = self.client.get(f"{self.client.base_url}{BASE_PATH}/{created_book['id']}")
            assert response.ok
            book = response.json()
            assert book["id"] == created_book["id"]

    @allure.story("Update Book")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test PUT update book")
    def test_update_book(self):
        """Test PUT update book"""
        with allure.step("Create a book first"):
            create_response = self.client.post(f"{self.client.base_url}{BASE_PATH}", json=EXAMPLE_BOOKS[0])
            assert create_response.ok
            created_book = create_response.json()
            self.created_book_ids.append(created_book["id"])

        with allure.step("Update the book"):
            updated_title = "Updated Book Title"
            update_data = {**EXAMPLE_BOOKS[0], "title": updated_title}
            response = self.client.put(
                f"{self.client.base_url}{BASE_PATH}/{created_book['id']}",
                json=update_data
            )
            assert response.ok
            book = response.json()
            assert book["title"] == updated_title

    @allure.story("Delete Book")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Test DELETE book")
    def test_delete_book(self):
        """Test DELETE book"""
        with allure.step("Create a book first"):
            create_response = self.client.post(f"{self.client.base_url}{BASE_PATH}", json=EXAMPLE_BOOKS[0])
            assert create_response.ok
            created_book = create_response.json()
            self.created_book_ids.append(created_book["id"])

        with allure.step("Delete the book"):
            response = self.client.delete(f"{self.client.base_url}{BASE_PATH}/{created_book['id']}")
            assert response.ok
            result = response.json()
            assert "deleted" in result["message"].lower() 
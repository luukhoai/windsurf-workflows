---
name: backend-test
description: Production-ready comprehensive testing skill for enterprise backend systems
---

# Backend Test Skill

This skill guides through writing and maintaining professional-grade tests for production backend systems with comprehensive coverage and quality assurance.

## When to Use
- Writing production-grade unit tests with >80% coverage
- Adding comprehensive tests for new features
- Implementing integration tests for microservices
- Creating performance and load testing scenarios
- Setting up security testing and penetration testing
- Debugging complex test failures in production systems

## Production Test Framework Stack
- **Core Framework**: pytest 7.4.2 with pytest-asyncio
- **HTTP Testing**: Flask test client with httpx
- **Database Testing**: pytest-postgresql with factory-boy
- **Mocking**: pytest-mock with unittest.mock
- **Coverage**: pytest-cov with HTML reports
- **Performance**: pytest-benchmark and locust
- **Security**: bandit and pytest-security
- **Integration**: testcontainers-python

## Production Test Architecture

### Test Structure
```
tests/
├── unit/                    # Unit tests
│   ├── services/            # Business logic tests
│   ├── repositories/       # Data access tests
│   ├── models/             # Domain model tests
│   └── utils/              # Utility function tests
├── integration/            # Integration tests
│   ├── api/                # API endpoint tests
│   ├── database/           # Database integration tests
│   └── external/           # External service tests
├── performance/           # Performance tests
│   ├── load/              # Load testing scenarios
│   └── stress/            # Stress testing scenarios
├── security/              # Security tests
│   ├── auth/              # Authentication tests
│   ├── authorization/     # Authorization tests
│   └── vulnerabilities/   # Security vulnerability tests
├── e2e/                   # End-to-end tests
└── fixtures/              # Test data and factories
```

## Production Testing Patterns

### Comprehensive Unit Tests
```python
# tests/unit/services/test_contact_service.py
import pytest
from unittest.mock import AsyncMock, Mock
from app.services.contact_service import ContactService
from app.repositories.contact_repository import ContactRepository
from app.models.contact import Contact
from app.utils.exceptions import ValidationError, DuplicateEmailError

@pytest.fixture
def mock_contact_repo():
    return AsyncMock(spec=ContactRepository)

@pytest.fixture
def contact_service(mock_contact_repo):
    return ContactService(mock_contact_repo)

@pytest.fixture
def sample_contact_data():
    return {
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'Test message'
    }

class TestContactService:
    async def test_create_contact_success(self, contact_service, 
                                         mock_contact_repo, sample_contact_data):
        """Test successful contact creation with all business rules."""
        # Arrange
        mock_contact_repo.email_exists.return_value = False
        expected_contact = Contact.create(sample_contact_data)
        mock_contact_repo.save.return_value = expected_contact
        
        # Act
        result = await contact_service.create_contact(sample_contact_data)
        
        # Assert
        assert result.name == sample_contact_data['name']
        assert result.email == sample_contact_data['email']
        mock_contact_repo.email_exists.assert_called_once_with(sample_contact_data['email'])
        mock_contact_repo.save.assert_called_once()

    async def test_create_contact_duplicate_email(self, contact_service, 
                                                mock_contact_repo, sample_contact_data):
        """Test contact creation with duplicate email raises appropriate error."""
        # Arrange
        mock_contact_repo.email_exists.return_value = True
        
        # Act & Assert
        with pytest.raises(DuplicateEmailError, match="Email already exists"):
            await contact_service.create_contact(sample_contact_data)
        
        mock_contact_repo.email_exists.assert_called_once_with(sample_contact_data['email'])
        mock_contact_repo.save.assert_not_called()

    async def test_create_contact_invalid_data(self, contact_service):
        """Test contact creation with invalid data raises validation error."""
        # Arrange
        invalid_data = {'name': '', 'email': 'invalid-email', 'message': ''}
        
        # Act & Assert
        with pytest.raises(ValidationError):
            await contact_service.create_contact(invalid_data)

    @pytest.mark.parametrize("field,value,expected_error", [
        ('name', '', 'Name cannot be empty'),
        ('email', 'invalid-email', 'Invalid email format'),
        ('message', 'x' * 1001, 'Message too long'),
    ])
    async def test_create_contact_validation_errors(self, contact_service, 
                                                   field, value, expected_error):
        """Test various validation scenarios."""
        # Arrange
        invalid_data = {'name': 'John', 'email': 'john@example.com', 'message': 'Test'}
        invalid_data[field] = value
        
        # Act & Assert
        with pytest.raises(ValidationError, match=expected_error):
            await contact_service.create_contact(invalid_data)

    async def test_get_contacts_with_pagination(self, contact_service, 
                                              mock_contact_repo):
        """Test contacts retrieval with pagination parameters."""
        # Arrange
        page, limit = 2, 20
        expected_contacts = [Mock(spec=Contact) for _ in range(20)]
        mock_contact_repo.find_all.return_value = expected_contacts
        
        # Act
        result = await contact_service.get_contacts(page=page, limit=limit)
        
        # Assert
        assert len(result) == 20
        mock_contact_repo.find_all.assert_called_once_with(page=page, limit=limit)
```

### Integration Tests
```python
# tests/integration/api/test_contacts_api.py
import pytest
from http import HTTPStatus
from app import create_app

@pytest.fixture
def app():
    app = create_app(testing=True)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_headers():
    return {'Authorization': 'Bearer valid_token'}

class TestContactsAPI:
    def test_create_contact_endpoint_success(self, client):
        """Test POST /api/contacts endpoint with valid data."""
        # Arrange
        contact_data = {
            'name': 'John Doe',
            'email': 'john@example.com',
            'message': 'Test message'
        }
        
        # Act
        response = client.post('/api/contacts', 
                             json=contact_data,
                             headers={'Content-Type': 'application/json'})
        
        # Assert
        assert response.status_code == HTTPStatus.CREATED
        data = response.get_json()
        assert data['success'] is True
        assert data['data']['name'] == contact_data['name']
        assert 'id' in data['data']
        assert 'created_at' in data['data']

    def test_create_contact_endpoint_validation_error(self, client):
        """Test POST /api/contacts endpoint with invalid data."""
        # Arrange
        invalid_data = {'name': '', 'email': 'invalid-email'}
        
        # Act
        response = client.post('/api/contacts', json=invalid_data)
        
        # Assert
        assert response.status_code == HTTPStatus.BAD_REQUEST
        data = response.get_json()
        assert data['success'] is False
        assert 'error' in data
        assert 'validation' in data['error'].lower()

    def test_get_contacts_endpoint_with_pagination(self, client):
        """Test GET /api/contacts endpoint with pagination."""
        # Act
        response = client.get('/api/contacts?page=1&limit=10')
        
        # Assert
        assert response.status_code == HTTPStatus.OK
        data = response.get_json()
        assert data['success'] is True
        assert 'data' in data
        assert 'meta' in data
        assert data['meta']['page'] == 1
        assert data['meta']['limit'] == 10

    def test_get_contacts_endpoint_requires_auth(self, client):
        """Test GET /api/contacts endpoint requires authentication."""
        # Act
        response = client.get('/api/contacts')
        
        # Assert
        assert response.status_code == HTTPStatus.UNAUTHORIZED
        data = response.get_json()
        assert data['success'] is False
        assert 'authentication' in data['error'].lower()

    def test_rate_limiting_enforcement(self, client):
        """Test rate limiting is enforced on endpoints."""
        # Arrange
        contact_data = {'name': 'Test', 'email': 'test@example.com', 'message': 'Test'}
        
        # Act - Make multiple requests quickly
        responses = []
        for _ in range(105):  # Exceed rate limit of 100
            response = client.post('/api/contacts', json=contact_data)
            responses.append(response)
        
        # Assert
        assert responses[-1].status_code == HTTPStatus.TOO_MANY_REQUESTS
```

### Performance Tests
```python
# tests/performance/test_contact_performance.py
import pytest
from concurrent.futures import ThreadPoolExecutor
import time

@pytest.mark.performance
class TestContactPerformance:
    def test_create_contact_performance(self, client):
        """Test contact creation performance meets SLA requirements."""
        # Arrange
        contact_data = {'name': 'Test', 'email': 'test@example.com', 'message': 'Test'}
        
        # Act
        start_time = time.time()
        response = client.post('/api/contacts', json=contact_data)
        end_time = time.time()
        
        # Assert
        assert response.status_code == 201
        response_time = end_time - start_time
        assert response_time < 0.5  # Should respond within 500ms

    def test_concurrent_contact_creation(self, client):
        """Test system handles concurrent contact creation."""
        # Arrange
        contact_data = {'name': 'Test', 'email': 'test@example.com', 'message': 'Test'}
        
        # Act
        def create_contact():
            return client.post('/api/contacts', json=contact_data)
        
        start_time = time.time()
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(create_contact) for _ in range(50)]
            responses = [future.result() for future in futures]
        end_time = time.time()
        
        # Assert
        success_count = sum(1 for r in responses if r.status_code == 201)
        assert success_count >= 45  # At least 90% success rate
        total_time = end_time - start_time
        assert total_time < 5.0  # Should complete within 5 seconds

    @pytest.mark.benchmark
    def test_contact_creation_benchmark(self, client, benchmark):
        """Benchmark contact creation performance."""
        contact_data = {'name': 'Test', 'email': 'test@example.com', 'message': 'Test'}
        
        def create_contact():
            return client.post('/api/contacts', json=contact_data)
        
        result = benchmark(create_contact)
        assert result.status_code == 201
```

### Security Tests
```python
# tests/security/test_contact_security.py
import pytest
from http import HTTPStatus

@pytest.mark.security
class TestContactSecurity:
    def test_sql_injection_prevention(self, client):
        """Test SQL injection attempts are prevented."""
        # Arrange
        malicious_payloads = [
            "'; DROP TABLE contacts; --",
            "' OR '1'='1",
            "'; INSERT INTO users VALUES ('hacker', 'password'); --"
        ]
        
        for payload in malicious_payloads:
            # Act
            response = client.post('/api/contacts', json={
                'name': payload,
                'email': 'test@example.com',
                'message': 'Test'
            })
            
            # Assert
            assert response.status_code in [HTTPStatus.BAD_REQUEST, HTTPStatus.CREATED]
            # Verify database integrity
            contacts_response = client.get('/api/contacts')
            assert contacts_response.status_code == HTTPStatus.OK

    def test_xss_prevention(self, client):
        """Test XSS attempts are prevented in contact data."""
        # Arrange
        xss_payloads = [
            '<script>alert("xss")</script>',
            'javascript:alert("xss")',
            '<img src="x" onerror="alert(\'xss\')">'
        ]
        
        for payload in xss_payloads:
            # Act
            response = client.post('/api/contacts', json={
                'name': payload,
                'email': 'test@example.com',
                'message': 'Test'
            })
            
            # Assert
            if response.status_code == HTTPStatus.CREATED:
                data = response.get_json()
                # Verify XSS payload is sanitized or escaped
                assert '<script>' not in data['data']['name']
                assert 'javascript:' not in data['data']['name']

    def test_authentication_bypass_attempts(self, client):
        """Test authentication bypass attempts are prevented."""
        # Arrange
        auth_bypass_attempts = [
            {'Authorization': 'Bearer fake_token'},
            {'Authorization': 'Basic invalid_credentials'},
            {'X-API-Key': 'fake_key'},
            {}  # No auth headers
        ]
        
        for headers in auth_bypass_attempts:
            # Act
            response = client.get('/api/contacts', headers=headers)
            
            # Assert
            assert response.status_code == HTTPStatus.UNAUTHORIZED
```

## Production Test Execution

### Comprehensive Test Suite
```bash
cd contact-form-app/backend
source venv/bin/activate

# Run all tests with coverage
pytest tests/ --cov=app --cov-report=html --cov-report=term-missing

# Run specific test categories
pytest tests/unit/ -v                    # Unit tests only
pytest tests/integration/ -v              # Integration tests only
pytest tests/performance/ -v               # Performance tests only
pytest tests/security/ -v                  # Security tests only

# Run with specific markers
pytest -m "not slow"                      # Skip slow tests
pytest -m "performance"                    # Performance tests only
pytest -m "security"                       # Security tests only
```

### Quality Gates
```bash
# Coverage requirements
pytest tests/ --cov=app --cov-fail-under=80

# Performance benchmarks
pytest tests/performance/ --benchmark-only

# Security scanning
pytest tests/security/ --bandit

# Load testing
locust -f tests/performance/locustfile.py --host=http://localhost:5000
```

### CI/CD Integration
```bash
# Parallel test execution
pytest tests/ -n auto --dist=loadscope

# JUnit XML for CI systems
pytest tests/ --junitxml=test-results.xml

# Test reports
pytest tests/ --html=test-report.html --self-contained-html
```

## Production Test Data Management

### Factory Pattern for Test Data
```python
# tests/factories/contact_factory.py
import factory
from faker import Faker
from app.models.contact import Contact

fake = Faker()

class ContactFactory(factory.Factory):
    class Meta:
        model = Contact
    
    name = factory.Faker('name')
    email = factory.Faker('email')
    message = factory.Faker('text', max_nb_chars=500)
    
    @classmethod
    def create_batch_with_unique_emails(cls, count):
        """Create batch of contacts with unique emails."""
        return [cls.create(email=fake.unique.email()) for _ in range(count)]
```

### Database Test Fixtures
```python
# tests/conftest.py
import pytest
import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database.connection import get_db_session
from app.models.base import Base

@pytest.fixture(scope='session')
def test_engine():
    engine = create_engine('postgresql://test:test@localhost:5433/test_db')
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture
def test_session(test_engine):
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
async def db_session(test_session):
    """Provide async database session for tests."""
    async with get_db_session() as session:
        yield session
```

## Production Test Checklist

### Test Coverage Requirements
- [ ] Unit test coverage >80% for business logic
- [ ] Integration test coverage >70% for API endpoints
- [ ] All critical paths tested
- [ ] All error scenarios covered
- [ ] Edge cases and boundary conditions tested

### Test Quality Standards
- [ ] Tests follow AAA pattern (Arrange-Act-Assert)
- [ ] Test names descriptive and clear
- [ ] Tests independent and isolated
- [ ] Proper fixtures and factory usage
- [ ] Mocking done correctly for external dependencies

### Performance Testing
- [ ] Response time SLAs verified (<500ms for API calls)
- [ ] Concurrent user load testing completed
- [ ] Database query performance tested
- [ ] Memory usage and resource leaks checked
- [ ] Scalability scenarios tested

### Security Testing
- [ ] Input validation and sanitization tested
- [ ] Authentication and authorization tested
- [ ] SQL injection prevention verified
- [ ] XSS protection tested
- [ ] Rate limiting effectiveness verified

### Integration Testing
- [ ] API endpoint integration tested
- [ ] Database integration tested
- [ ] External service integration tested
- [ ] Message queue integration tested
- [ ] Cache integration tested

### Production Readiness
- [ ] Test data management strategy in place
- [ ] Test environment properly configured
- [ ] Continuous integration pipeline configured
- [ ] Test reports and metrics available
- [ ] Test execution time within acceptable limits

## How to Invoke

```
Write comprehensive tests for [feature] using the backend-test skill
Run production test suite using the backend-test skill
Create performance tests for [endpoint] using the backend-test skill
Implement security tests for [feature] using the backend-test skill
```

## Related Skills

- **Analysis**: Use `backend-analysis-plan` skill for test planning
- **Implementation**: Use `backend-code` skill for production code
- **Review**: Use `backend-review` skill for test quality review

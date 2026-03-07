---
name: backend-code
description: Production-ready backend implementation skill with comprehensive quality checks
---

# Backend Code Skill

Implement production-ready backend code with comprehensive architecture compliance, security, and quality assurance.

## When to Use
- Implementing new API endpoints for production systems
- Adding business logic with scalability requirements
- Creating enterprise-grade utility functions
- After comprehensive analysis and planning stage
- When implementing microservices architecture

## Production Concept

- **This skill**: Implementation + Lint + Security + Architecture Compliance
- **Quality Gates**: Code + Architecture + Database + API + Security + Performance
- **Standards**: Comprehensive backend architecture (`.windsurf/rules/backend-development.md`)

## Production Implementation

See `.windsurf/rules/backend-development.md` for comprehensive backend architecture standards.

### Production Code Structure

| Layer | Location | Responsibility |
|-------|-----------|----------------|
| Controllers | `app/controllers/` | HTTP request handling, validation |
| Services | `app/services/` | Business logic, orchestration |
| Repositories | `app/repositories/` | Data access abstraction |
| Models | `app/models/` | Domain entities, business rules |
| Utils | `app/utils/` | Cross-cutting concerns |
| Config | `app/config/` | Configuration management |

### Production Code Patterns

#### Service Layer Pattern
```python
# app/services/contact_service.py
from typing import List, Optional
from app.repositories.contact_repository import ContactRepository
from app.models.contact import Contact
from app.utils.validators import validate_contact_data
from app.utils.logger import get_logger

logger = get_logger(__name__)

class ContactService:
    def __init__(self, contact_repo: ContactRepository):
        self.contact_repo = contact_repo
    
    async def create_contact(self, contact_data: dict) -> Contact:
        """Create a new contact with validation and business rules."""
        # Input validation
        validated_data = validate_contact_data(contact_data)
        
        # Business logic
        if await self.contact_repo.email_exists(validated_data['email']):
            raise ValueError("Email already exists")
        
        # Create entity
        contact = Contact.create(validated_data)
        
        # Persist
        result = await self.contact_repo.save(contact)
        
        # Audit logging
        logger.info(f"Contact created: {result.id}")
        
        return result
    
    async def get_contacts(self, page: int = 1, limit: int = 10) -> List[Contact]:
        """Retrieve contacts with pagination."""
        return await self.contact_repo.find_all(page=page, limit=limit)
```

#### Repository Pattern
```python
# app/repositories/contact_repository.py
from abc import ABC, abstractmethod
from typing import List, Optional
from app.models.contact import Contact
from app.database.connection import DatabaseConnection

class ContactRepository(ABC):
    @abstractmethod
    async def save(self, contact: Contact) -> Contact:
        pass
    
    @abstractmethod
    async def find_by_id(self, contact_id: str) -> Optional[Contact]:
        pass
    
    @abstractmethod
    async def find_all(self, page: int, limit: int) -> List[Contact]:
        pass
    
    @abstractmethod
    async def email_exists(self, email: str) -> bool:
        pass

class SqlContactRepository(ContactRepository):
    def __init__(self, db: DatabaseConnection):
        self.db = db
    
    async def save(self, contact: Contact) -> Contact:
        query = """
        INSERT INTO contacts (id, name, email, message, created_at)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id, created_at
        """
        params = (contact.id, contact.name, contact.email, 
                 contact.message, contact.created_at)
        
        result = await self.db.execute(query, params)
        contact.id = result['id']
        contact.created_at = result['created_at']
        
        return contact
```

#### Controller Pattern
```python
# app/controllers/contact_controller.py
from flask import Blueprint, request, jsonify
from typing import Dict, Any
from app.services.contact_service import ContactService
from app.utils.response_builder import ResponseBuilder
from app.utils.rate_limiter import rate_limit
from app.utils.auth import require_auth

contact_bp = Blueprint('contacts', __name__)

@contact_bp.route('/api/contacts', methods=['POST'])
@rate_limit(limit=100, window=60)  # 100 requests per minute
async def create_contact():
    """Create a new contact endpoint."""
    try:
        # Input validation
        data = request.get_json()
        if not data:
            return ResponseBuilder.error("No data provided", 400)
        
        # Service layer
        contact_service = ContactService()
        contact = await contact_service.create_contact(data)
        
        # Response
        return ResponseBuilder.success(
            data=contact.to_dict(),
            status_code=201,
            message="Contact created successfully"
        )
        
    except ValueError as e:
        return ResponseBuilder.error(str(e), 400)
    except Exception as e:
        logger.error(f"Error creating contact: {str(e)}")
        return ResponseBuilder.error("Internal server error", 500)

@contact_bp.route('/api/contacts', methods=['GET'])
@require_auth
async def get_contacts():
    """Get contacts with pagination."""
    try:
        page = int(request.args.get('page', 1))
        limit = min(int(request.args.get('limit', 10)), 100)  # Max 100
        
        contact_service = ContactService()
        contacts = await contact_service.get_contacts(page=page, limit=limit)
        
        return ResponseBuilder.success(
            data=[contact.to_dict() for contact in contacts],
            meta={
                'page': page,
                'limit': limit,
                'total': len(contacts)
            }
        )
        
    except Exception as e:
        logger.error(f"Error retrieving contacts: {str(e)}")
        return ResponseBuilder.error("Internal server error", 500)
```

## Production Quality Checks

### Code Quality
```bash
cd contact-form-app/backend
source venv/bin/activate

# Lint with strict standards
flake8 app/ tests/ --max-line-length=100 --ignore=E501,W503 --max-complexity=10

# Type checking
mypy app/ --strict

# Security scanning
bandit -r app/ -f json

# Code formatting
black app/ tests/ --check
isort app/ tests/ --check-only
```

### Security Validation
```bash
# Security vulnerability scan
snyk code test --severity-threshold=medium

# Dependency vulnerability check
snyk monitor

# Static analysis for security issues
bandit -r app/ -f json -o security-report.json
```

### Performance Analysis
```bash
# Code complexity analysis
radon cc app/ --min B

# Maintainability index
radon mi app/ --min B

# Import analysis
cyclonedx-bom app/ -o bom.json
```

## Production Commands

### Development Environment
```bash
cd contact-form-app/backend
source venv/bin/activate

# Run with development configuration
python run.py --env=development

# Run with hot reload
FLASK_ENV=development python run.py
```

### Production Environment
```bash
# Run with production configuration
python run.py --env=production

# Run with Gunicorn (production WSGI server)
gunicorn --bind 0.0.0.0:5000 --workers 4 --timeout 120 "app:create_app()"

# Run with uWSGI
uwsgi --http :5000 --wsgi-file app.py --callable app --processes 4 --threads 2
```

### Database Operations
```bash
# Run migrations
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "Add contacts table"

# Database backup
pg_dump contacts_db > backup_$(date +%Y%m%d_%H%M%S).sql
```

## Production Checklist

### Code Quality
- [ ] Code follows comprehensive backend architecture standards
- [ ] SOLID principles properly implemented
- [ ] Design patterns correctly applied (Repository, Service Layer)
- [ ] Type hints used throughout codebase
- [ ] Error handling comprehensive and secure
- [ ] Logging implemented with appropriate levels
- [ ] Code complexity within acceptable limits (<10)

### Security Implementation
- [ ] Input validation and sanitization implemented
- [ ] Authentication and authorization properly configured
- [ ] SQL injection prevention in place
- [ ] XSS protection implemented
- [ ] CSRF protection configured
- [ ] Rate limiting applied to endpoints
- [ ] Sensitive data properly handled and encrypted
- [ ] Security headers configured

### Performance & Scalability
- [ ] Database queries optimized with proper indexing
- [ ] Connection pooling configured
- [ ] Caching strategies implemented
- [ ] Async processing for heavy operations
- [ ] Resource cleanup and memory management
- [ ] Horizontal scaling considerations
- [ ] Monitoring and metrics implemented

### API Design
- [ ] RESTful conventions followed
- [ ] Proper HTTP status codes used
- [ ] Consistent response format
- [ ] API versioning strategy
- [ ] Comprehensive error responses
- [ ] Request/response validation
- [ ] OpenAPI documentation complete

### Testing Coverage
- [ ] Unit tests for all business logic (>80% coverage)
- [ ] Integration tests for API endpoints
- [ ] Repository tests with test database
- [ ] Service layer tests with mocked dependencies
- [ ] Error scenario testing
- [ ] Performance test scenarios

### Production Readiness
- [ ] Environment configuration management
- [ ] Health check endpoints implemented
- [ ] Graceful shutdown handling
- [ ] Database migration scripts ready
- [ ] Monitoring and alerting configured
- [ ] Backup and recovery procedures
- [ ] Documentation complete

## Related Standards

See `.windsurf/rules/backend-development.md` for:
- Comprehensive OOP/SOLID principles
- Database design and architecture
- API architecture and security
- Performance and scalability patterns
- Deployment and DevOps practices

## How to Invoke

```
Implement [feature] for production deployment using the backend-code skill
```

## Related Skills

- **Analysis**: Use `backend-analysis-plan` skill for comprehensive planning
- **Testing**: Use `backend-test` skill for production-grade testing
- **Review**: Use `backend-review` skill for production readiness review

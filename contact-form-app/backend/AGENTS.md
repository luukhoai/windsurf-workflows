# Backend API Guidelines

## Development Environment

### Python Virtual Environment
- **Always use the virtual environment** when running Python commands
- Activate venv: `source venv/bin/activate`
- Or use explicit path: `venv/bin/python` or `venv/bin/python3`

```bash
# Correct way to run commands
cd contact-form-app/backend
source venv/bin/activate
python run.py
pytest tests/ -v

# Or use explicit path
cd contact-form-app/backend
venv/bin/python run.py
venv/bin/python -m pytest tests/ -v
```

## Project-Specific Guidelines

### Endpoint Structure
- Use RESTful conventions for all endpoints
- Return consistent JSON response format: `{ success: boolean, data?: any, error?: string }`
- Include appropriate HTTP status codes (200, 201, 400, 404, 500)

### Error Handling
- Catch and log all exceptions with appropriate context
- Return user-friendly error messages to clients
- Never expose internal error details or stack traces

### Validation
- Validate all input data before processing
- Sanitize user inputs to prevent injection attacks
- Use type hints for all function parameters and return values

### Database Operations
- Use parameterized queries to prevent SQL injection
- Handle connection errors gracefully
- Close connections properly after use

### Logging
- Log all API requests with timestamp and endpoint
- Log errors with full context for debugging
- Avoid logging sensitive user data (passwords, tokens)

## Comprehensive Backend Standards

For complete backend development standards including:
- **OOP/SOLID Principles** - Class design, inheritance, SOLID implementation
- **Database Architecture** - Schema design, migrations, optimization
- **API Architecture** - RESTful design, versioning, documentation
- **Security Architecture** - Authentication, authorization, data protection
- **Performance & Scalability** - Optimization, caching, scaling
- **System Architecture** - Microservices, messaging, monitoring
- **Deployment & DevOps** - Containerization, CI/CD, infrastructure
- **Error Handling & Resilience** - Exception handling, circuit breakers

→ **See**: `.windsurf/rules/backend-development.md`

## Quality Pipeline

Use the `backend-code-test-review` workflow for all backend changes:
- Analyze → Implement → Test → Review
- Comprehensive quality gates (Code + Architecture + Security + Tests)
- OOP/SOLID compliance verification
- Database and API architecture validation

→ **See**: `.windsurf/workflows/backend-code-test-review.md`

## Entry Points
- **Run app**: `python run.py`
- **Run tests**: `pytest tests/ -v`
- **Run lint**: `flake8 app/ tests/`
- **Run security scan**: `snyk code test --severity-threshold=medium`
- **Format code**: `black app/ tests/`

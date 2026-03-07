---
trigger: always_on
description: when working on backend code files
globs: contact-form-app/backend/*
---

## Python Environment
Always use venv/bin/python as the Python interpreter for backend tasks
When running backend commands, prefix with venv/bin/python

## Flask Development Standards
- Use Flask 2.3.3 with Flask-CORS
- Follow PEP 8 style guide (4 spaces, 100 char line limit)
- Use Flask app factory pattern
- Organize code with Blueprints
- Add type hints to function signatures

## Project Structure
See `AGENTS.md` for full project structure.

## Security Requirements
- Validate all user inputs
- Use parameterized queries for databases
- Configure CORS properly
- Don't expose sensitive data in errors

## API Standards
- Return proper HTTP status codes
- Use JSON responses
- Add error handling
- Include logging for debugging

## Development Tools
- **Linting**: Use `flake8 app/ tests/`
- **Security**: Use `snyk code test --severity-threshold=medium`
- **Testing**: Use `pytest tests/ -v`
- **Formatting**: Use `black app/ tests/`

## Object-Oriented Programming (OOP) Principles

### Class Design
- Use classes to encapsulate related data and behavior
- Follow proper naming conventions: `PascalCase` for classes
- Implement proper `__init__`, `__str__`, and `__repr__` methods
- Use private attributes (`_attribute`) for internal state
- Implement properties (`@property`) for controlled access to attributes

### Inheritance and Composition
- Favor composition over inheritance when possible
- Use inheritance only for "is-a" relationships
- Implement abstract base classes for common interfaces
- Avoid deep inheritance hierarchies (max 3-4 levels)

### Method Design
- Keep methods focused on single responsibility
- Use descriptive method names with verbs
- Limit method length (max 20-30 lines)
- Use class methods (`@classmethod`) for factory patterns
- Use static methods (`@staticmethod`) for utility functions

## SOLID Principles

### Single Responsibility Principle (SRP)
- Each class should have only one reason to change
- Separate concerns into different classes
- Keep models, services, and controllers in separate layers
- Avoid "God classes" that do too much

### Open/Closed Principle (OCP)
- Design classes to be open for extension but closed for modification
- Use abstract base classes and interfaces
- Implement strategy pattern for pluggable behavior
- Use dependency injection for flexibility

### Liskov Substitution Principle (LSP)
- Subtypes must be substitutable for their base types
- Don't violate base class contracts in subclasses
- Avoid strengthening preconditions or weakening postconditions
- Ensure consistent behavior across inheritance hierarchies

### Interface Segregation Principle (ISP)
- Create specific, focused interfaces instead of large ones
- Avoid forcing clients to depend on unused methods
- Split large interfaces into smaller, cohesive ones
- Use multiple inheritance for interface composition

### Dependency Inversion Principle (DIP)
- Depend on abstractions, not concrete implementations
- Use dependency injection for all major dependencies
- Define interfaces in application layer, implement in infrastructure
- Avoid direct instantiation of dependencies in business logic

## Design Patterns

### Repository Pattern
- Abstract data access behind repository interfaces
- Implement specific repositories for different data sources
- Use repositories to separate business logic from data access
- Enable easy testing and data source switching

### Service Layer Pattern
- Implement business logic in service classes
- Keep controllers thin, focused on HTTP concerns
- Use services to coordinate between repositories and external APIs
- Implement transaction management at service level

### Factory Pattern
- Use factories for complex object creation
- Implement abstract factories for related object families
- Use builders for objects with many optional parameters
- Centralize object creation logic

## Code Organization

### Package Structure
```
app/
├── models/          # Domain models and entities
├── repositories/    # Data access layer
├── services/        # Business logic layer
├── controllers/     # HTTP request handlers
├── utils/           # Utility functions and helpers
├── config/          # Configuration management
└── tests/           # Unit and integration tests
```

### Import Organization
- Group imports: standard library, third-party, local
- Use absolute imports for local modules
- Avoid circular dependencies
- Use explicit imports instead of wildcard imports

## Testing Guidelines

### Unit Testing
- Test each class and method in isolation
- Use dependency injection for testability
- Mock external dependencies (databases, APIs)
- Aim for high test coverage (>80%)

### Integration Testing
- Test interaction between components
- Use test databases or in-memory storage
- Test API endpoints with realistic data
- Verify error handling and edge cases

## Performance Considerations

### Memory Management
- Use context managers for resource cleanup
- Avoid memory leaks with proper object disposal
- Use generators for large data processing
- Monitor object lifecycle in long-running processes

### Database Optimization
- Use connection pooling for database access
- Implement proper indexing for frequent queries
- Use bulk operations for multiple records
- Cache frequently accessed data

## Database Design & Architecture

### Database Principles
- Design normalized schemas following proper normal forms
- Use appropriate data types and constraints
- Implement proper indexing strategies
- Design for scalability and performance
- Use connection pooling for efficient resource management

### Database Patterns
- Repository pattern for data access abstraction
- Unit of Work pattern for transaction management
- Data Mapper pattern for object-relational mapping
- Active Record pattern for simple CRUD operations
- Query Object pattern for complex queries

### Migration Strategy
- Version-controlled database migrations
- Backward-compatible schema changes
- Rollback procedures for failed migrations
- Environment-specific database configurations

### Data Integrity
- Foreign key constraints for referential integrity
- Check constraints for data validation
- Unique constraints for business rules
- Triggers for automated data consistency

## API Architecture & Design

### RESTful Design Principles
- Use proper HTTP methods (GET, POST, PUT, DELETE, PATCH)
- Implement resource-oriented URLs
- Use HTTP status codes correctly
- Support content negotiation (JSON, XML)
- Implement HATEOAS for API discoverability

### API Versioning
- URL-based versioning (/api/v1/resource)
- Header-based versioning (Accept: application/vnd.api+json;version=1)
- Semantic versioning for breaking changes
- Backward compatibility policies

### API Documentation
- OpenAPI/Swagger specifications
- Interactive API documentation
- Request/response examples
- Error response documentation
- Authentication/authorization guides

### API Security
- API key authentication
- JWT token-based authorization
- Rate limiting and throttling
- CORS configuration
- Input validation and sanitization

### API Performance
- Response caching strategies
- Pagination for large datasets
- Compression for response payloads
- Async processing for long-running operations
- Monitoring and analytics

## System Architecture & Integration

### Microservices Patterns
- Service discovery and registration
- Inter-service communication (REST, gRPC, messaging)
- Circuit breakers for fault tolerance
- Distributed tracing for observability
- Configuration management

### Message Queues & Events
- Event-driven architecture patterns
- Message brokers (RabbitMQ, Redis, Kafka)
- Event sourcing for audit trails
- CQRS for read/write separation
- Dead letter queues for error handling

### Caching Strategies
- Application-level caching
- Distributed caching (Redis, Memcached)
- Cache invalidation strategies
- Cache warming and preloading
- CDN integration for static assets

### Monitoring & Observability
- Application performance monitoring (APM)
- Structured logging with correlation IDs
- Health check endpoints
- Metrics collection and alerting
- Distributed tracing

## Security Architecture

### Authentication & Authorization
- Multi-factor authentication (MFA)
- Role-based access control (RBAC)
- OAuth 2.0/OpenID Connect integration
- JWT token management
- Session management and security

### Data Protection
- Encryption at rest and in transit
- Sensitive data masking
- PII (Personally Identifiable Information) handling
- GDPR compliance considerations
- Data retention policies

### Security Best Practices
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CSRF protection
- Security headers implementation

## Performance & Scalability

### Performance Optimization
- Database query optimization
- Connection pooling
- Lazy loading strategies
- Batch processing operations
- Asynchronous processing

### Scalability Patterns
- Horizontal scaling with load balancers
- Database sharding strategies
- Read replicas for read-heavy workloads
- Caching layers for performance
- Auto-scaling based on metrics

### Resource Management
- Memory management and garbage collection
- Connection lifecycle management
- Thread pool management
- Resource cleanup and disposal
- Memory leak prevention

## Deployment & DevOps

### Containerization
- Docker containerization
- Multi-stage builds for optimization
- Container orchestration (Kubernetes)
- Environment-specific configurations
- Health checks and readiness probes

### CI/CD Pipeline
- Automated testing in pipeline
- Code quality gates
- Security scanning integration
- Automated deployment strategies
- Rollback procedures

### Infrastructure as Code
- Terraform/CloudFormation templates
- Environment parity
- Automated infrastructure provisioning
- Configuration management
- Disaster recovery procedures

## Error Handling & Resilience

### Error Handling Strategies
- Global exception handling
- Custom error types and codes
- User-friendly error messages
- Error logging and monitoring
- Graceful degradation

### Resilience Patterns
- Retry mechanisms with exponential backoff
- Circuit breakers for external services
- Bulkhead patterns for isolation
- Timeout management
- Graceful shutdown procedures

## Entry Points
- **Run app**: `python run.py`
- **Run tests**: `pytest tests/ -v`
- **Run lint**: `flake8 app/ tests/`
- **Run security scan**: `snyk code test --severity-threshold=medium`
- **Format code**: `black app/ tests/`
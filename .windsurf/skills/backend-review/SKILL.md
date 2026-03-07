---
name: backend-review
description: Production-ready comprehensive code review skill for enterprise backend systems
---

# Backend Review Skill

This skill guides through comprehensive code review for production backend systems, ensuring enterprise-grade quality, security, and architectural compliance.

## When to Use
- Before merging pull requests to production branches
- When reviewing critical backend implementations
- During architecture compliance audits
- For security vulnerability assessments
- When evaluating performance and scalability implementations
- During production readiness reviews

## Production Review Framework

### Review Categories
1. **Business Logic & Requirements** - Feature correctness and completeness
2. **Architecture & Design** - SOLID principles, patterns, and structure
3. **Code Quality** - Readability, maintainability, and standards
4. **API Design** - RESTful compliance and documentation
5. **Security** - Vulnerability prevention and data protection
6. **Performance & Scalability** - Optimization and resource management
7. **Database Design** - Schema, queries, and data integrity
8. **Testing Coverage** - Test quality and coverage requirements
9. **Production Readiness** - Monitoring, deployment, and operations

## Comprehensive Review Checklist

### 1. Business Logic & Requirements
- [ ] **Functional Requirements**: Does the code meet all specified business requirements?
- [ ] **Edge Cases**: Are all edge cases and boundary conditions handled?
- [ ] **Error Scenarios**: Are error paths properly implemented and user-friendly?
- [ ] **Business Rules**: Are business rules correctly implemented and validated?
- [ ] **Data Validation**: Is input validation comprehensive and secure?
- [ ] **Success Criteria**: Are success criteria and KPIs measurable?

### 2. Architecture & Design
- [ ] **SOLID Principles**: Are all SOLID principles properly applied?
  - [ ] **SRP**: Classes have single responsibility
  - [ ] **OCP**: Code is open for extension, closed for modification
  - [ ] **LSP**: Subtypes are substitutable for base types
  - [ ] **ISP**: Interfaces are focused and cohesive
  - [ ] **DIP**: Dependencies are inverted and injected
- [ ] **Design Patterns**: Are appropriate patterns correctly implemented?
  - [ ] **Repository Pattern**: Data access properly abstracted
  - [ ] **Service Layer**: Business logic separated from controllers
  - [ ] **Factory Pattern**: Object creation properly encapsulated
  - [ ] **Strategy Pattern**: Algorithms pluggable and interchangeable
- [ ] **Package Structure**: Does code follow proper package organization?
- [ ] **Dependency Management**: Are dependencies properly managed and injected?
- [ ] **Separation of Concerns**: Are concerns properly separated?

### 3. Code Quality
- [ ] **Readability**: Is code clear, readable, and self-documenting?
- [ ] **Naming**: Are variables, functions, and classes descriptively named?
- [ ] **Type Hints**: Are type hints used consistently and correctly?
- [ ] **Code Duplication**: Is code duplication minimized through proper abstraction?
- [ ] **Complexity**: Is cyclomatic complexity within acceptable limits (<10)?
- [ ] **PEP 8 Compliance**: Does code follow Python style guidelines?
- [ ] **Documentation**: Is code adequately documented with docstrings?
- [ ] **Import Organization**: Are imports properly organized and grouped?

### 4. API Design
- [ ] **RESTful Conventions**: Are HTTP methods used correctly?
  - [ ] GET for data retrieval
  - [ ] POST for resource creation
  - [ ] PUT/PATCH for updates
  - [ ] DELETE for removal
- [ ] **Status Codes**: Are proper HTTP status codes returned?
- [ ] **Response Format**: Are responses consistent and well-structured?
- [ ] **Error Handling**: Are error responses consistent and informative?
- [ ] **API Versioning**: Is versioning strategy implemented?
- [ ] **Pagination**: Are list endpoints properly paginated?
- [ ] **Filtering & Sorting**: Are query parameters properly handled?
- [ ] **OpenAPI Documentation**: Is API documentation complete and accurate?

### 5. Security Implementation
- [ ] **Input Validation**: Are all inputs validated and sanitized?
- [ ] **SQL Injection Prevention**: Are parameterized queries used?
- [ ] **XSS Prevention**: Are outputs properly escaped?
- [ ] **CSRF Protection**: Is CSRF protection implemented?
- [ ] **Authentication**: Is authentication properly implemented?
- [ ] **Authorization**: Are access controls properly enforced?
- [ ] **Rate Limiting**: Is rate limiting applied to prevent abuse?
- [ ] **Data Protection**: Is sensitive data properly encrypted and masked?
- [ ] **Security Headers**: Are security headers properly configured?
- [ ] **Audit Logging**: Are security events properly logged?

### 6. Performance & Scalability
- [ ] **Database Optimization**: Are queries optimized with proper indexing?
- [ ] **Connection Pooling**: Is database connection pooling configured?
- [ ] **Caching Strategy**: Are appropriate caching mechanisms implemented?
- [ ] **Async Processing**: Are long-running operations properly async?
- [ ] **Memory Management**: Are resources properly cleaned up?
- [ ] **Batch Operations**: Are bulk operations used where appropriate?
- [ ] **Resource Limits**: Are appropriate limits enforced?
- [ ] **Monitoring**: Are performance metrics implemented?

### 7. Database Design
- [ ] **Schema Design**: Is database schema properly normalized?
- [ ] **Data Integrity**: Are constraints properly defined?
- [ ] **Indexing Strategy**: Are indexes properly designed for performance?
- [ ] **Migration Scripts**: Are database migrations safe and reversible?
- [ ] **Transaction Management**: Are transactions properly used?
- [ ] **Connection Management**: Are database connections properly managed?
- [ ] **Backup Strategy**: Are backup and recovery procedures defined?

### 8. Testing Coverage
- [ ] **Unit Tests**: Are all business logic units tested (>80% coverage)?
- [ ] **Integration Tests**: Are API endpoints properly tested?
- [ ] **Repository Tests**: Are data access layers tested?
- [ ] **Service Tests**: Are business services comprehensively tested?
- [ ] **Error Testing**: Are error scenarios properly tested?
- [ ] **Performance Tests**: Are performance scenarios tested?
- [ ] **Security Tests**: Are security vulnerabilities tested?
- [ ] **Test Quality**: Are tests well-structured and maintainable?

### 9. Production Readiness
- [ ] **Environment Configuration**: Are environment variables properly managed?
- [ ] **Health Checks**: Are health check endpoints implemented?
- [ ] **Logging**: Is comprehensive logging implemented?
- [ ] **Monitoring**: Are application metrics and monitoring configured?
- [ ] **Error Tracking**: Is error tracking and alerting configured?
- [ ] **Graceful Shutdown**: Is graceful shutdown handling implemented?
- [ ] **Deployment Scripts**: Are deployment scripts tested and reliable?
- [ ] **Documentation**: Is operational documentation complete?

## Backend-Specific Technical Review

### Flask Application Review
- [ ] **Blueprint Organization**: Are blueprints properly organized and registered?
- [ ] **Middleware**: Is middleware properly configured and ordered?
- [ ] **Error Handlers**: Are custom error handlers defined?
- [ ] **Request Handling**: Is request parsing and validation robust?
- [ ] **Response Formatting**: Are JSON responses consistently formatted?
- [ ] **Configuration**: Is configuration management secure and flexible?

### Database Layer Review
- [ ] **ORM Usage**: Is ORM used efficiently and appropriately?
- [ ] **Query Optimization**: Are N+1 query problems avoided?
- [ ] **Data Validation**: Are database constraints and validation consistent?
- [ ] **Migration Safety**: Are migrations safe for production data?
- [ ] **Connection Security**: Are database connections secure?

### Service Layer Review
- [ ] **Business Logic**: Is business logic properly encapsulated?
- [ ] **Transaction Boundaries**: Are transaction boundaries appropriate?
- [ ] **Error Propagation**: Are errors properly handled and propagated?
- [ ] **Dependency Injection**: Are dependencies properly injected?
- [ ] **State Management**: Is state properly managed?

### Controller Layer Review
- [ ] **HTTP Handling**: Are HTTP requests properly handled?
- [ ] **Input Validation**: Is input validation comprehensive?
- [ ] **Response Building**: Are responses consistently built?
- [ ] **Authentication**: Are authentication checks properly placed?
- [ ] **Authorization**: Are authorization checks properly implemented?

## Security Review Checklist

### Authentication & Authorization
- [ ] **Password Security**: Are passwords properly hashed and stored?
- [ ] **Token Management**: Are JWT tokens properly managed and validated?
- [ ] **Session Security**: Are sessions properly secured?
- [ ] **Multi-Factor Auth**: Is MFA implemented where required?
- [ ] **Role-Based Access**: Is RBAC properly implemented?

### Data Protection
- [ ] **Encryption at Rest**: Is sensitive data encrypted at rest?
- [ ] **Encryption in Transit**: Is data encrypted in transit?
- [ ] **PII Handling**: Is personally identifiable information properly handled?
- [ ] **Data Masking**: Is sensitive data masked in logs?
- [ ] **Compliance**: Are compliance requirements (GDPR, SOC2) met?

### Vulnerability Prevention
- [ ] **Injection Attacks**: Are all injection vulnerabilities prevented?
- [ ] **Cross-Site Scripting**: Is XSS protection implemented?
- [ ] **Cross-Site Request Forgery**: Is CSRF protection implemented?
- [ ] **Security Misconfigurations**: Are security configurations correct?
- [ ] **Sensitive Data Exposure**: Is sensitive data properly protected?

## Performance Review Checklist

### Database Performance
- [ ] **Query Performance**: Are database queries optimized?
- [ ] **Index Usage**: Are indexes properly used?
- [ ] **Connection Efficiency**: Are database connections efficient?
- [ ] **Data Volume**: Are large datasets handled efficiently?
- [ ] **Query Caching**: Are query results cached appropriately?

### Application Performance
- [ ] **Response Time**: Are response times within SLA requirements?
- [ ] **Throughput**: Can the system handle expected load?
- [ ] **Memory Usage**: Is memory usage efficient?
- [ ] **CPU Usage**: Is CPU usage optimized?
- [ ] **I/O Operations**: Are I/O operations optimized?

### Scalability Review
- [ ] **Horizontal Scaling**: Can the system scale horizontally?
- [ ] **Load Balancing**: Is load balancing properly configured?
- [ ] **Caching Strategy**: Is caching strategy appropriate for scale?
- [ ] **Resource Limits**: Are resource limits properly configured?
- [ ] **Auto-scaling**: Is auto-scaling configured where needed?

## Production Review Process

### Review Preparation
1. **Code Analysis**: Run automated analysis tools
2. **Test Results**: Review test coverage and results
3. **Security Scan**: Review security vulnerability reports
4. **Performance Metrics**: Review performance benchmarks
5. **Documentation**: Review technical documentation

### Review Execution
1. **Code Walkthrough**: Systematic code review
2. **Architecture Review**: Validate architecture compliance
3. **Security Review**: Comprehensive security assessment
4. **Performance Review**: Performance and scalability assessment
5. **Production Readiness**: Operations and deployment review

### Review Output
1. **Findings Report**: Detailed findings with severity levels
2. **Action Items**: Specific actionable recommendations
3. **Approval Decision**: Go/No-Go decision with rationale
4. **Follow-up Plan**: Plan for addressing identified issues

## Review Severity Levels

### Critical (Blocker)
- Security vulnerabilities that could be exploited
- Data corruption or loss risks
- Performance issues that impact production
- Non-compliance with regulatory requirements

### High (Must Fix)
- Architecture violations that impact maintainability
- Significant performance degradation
- Security best practice violations
- Insufficient test coverage

### Medium (Should Fix)
- Code quality issues that impact readability
- Minor performance optimizations
- Documentation gaps
- Style guide violations

### Low (Nice to Fix)
- Minor code improvements
- Enhanced error messages
- Additional logging
- Code optimization opportunities

## Related Standards

See `.windsurf/rules/backend-development.md` for comprehensive backend architecture standards including:
- OOP/SOLID principles implementation
- Database design and architecture patterns
- API architecture and security standards
- Performance and scalability guidelines
- Deployment and DevOps best practices

## How to Invoke

```
Review the backend code for production readiness using the backend-review skill
Conduct comprehensive architecture review using the backend-review skill
Perform security assessment of [feature] using the backend-review skill
Evaluate performance and scalability of [implementation] using the backend-review skill
```

## Related Skills

- **Analysis**: Use `backend-analysis-plan` skill for pre-implementation review
- **Implementation**: Use `backend-code` skill for production-grade development
- **Testing**: Use `backend-test` skill for comprehensive testing review

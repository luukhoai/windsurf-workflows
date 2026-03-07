---
name: backend-analysis-plan
description: Production-ready analysis and planning skill for comprehensive backend architecture
---

# Backend Analysis Plan Skill

This skill guides through comprehensive requirement analysis and architectural planning for production backend systems.

## When to Use
- Before starting any new feature or API endpoint
- When requirements are unclear or complex
- Before major refactoring or architecture changes
- When estimating effort for production deployments
- When designing scalable backend systems
- For microservices architecture planning

## Production Analysis Process

### Step 1: Understand Business Requirements
1. **Functional Requirements**
   - Read and understand the feature/fix description
   - Identify the core business goal and expected outcome
   - Define success criteria and KPIs
   - Note any business constraints or SLAs

2. **Non-Functional Requirements**
   - Performance requirements (response time, throughput)
   - Scalability needs (concurrent users, data volume)
   - Security requirements (authentication, data protection)
   - Availability requirements (uptime, disaster recovery)
   - Monitoring and observability needs

### Step 2: Analyze Technical Context
1. **Existing Architecture Review**
   - Find relevant files in `contact-form-app/backend/`
   - Understand current implementation patterns
   - Identify affected components and dependencies
   - Review database schema and API contracts

2. **Integration Points**
   - Identify external service dependencies
   - Plan API versioning and backward compatibility
   - Consider message queues and event streaming
   - Review caching strategies

3. **Data Architecture**
   - Plan database schema changes
   - Consider data migration strategies
   - Design for data consistency and integrity
   - Plan backup and recovery procedures

### Step 3: Design Production Solution
1. **Architecture Design**
   - Apply SOLID principles and design patterns
   - Choose appropriate patterns (Repository, Service Layer, CQRS)
   - Plan microservices decomposition if needed
   - Design for failure and resilience

2. **API Design**
   - Design RESTful endpoints following OpenAPI standards
   - Plan request/response schemas
   - Design pagination, filtering, and sorting
   - Plan API versioning strategy

3. **Security Architecture**
   - Design authentication and authorization
   - Plan input validation and sanitization
   - Design for audit logging and compliance
   - Consider rate limiting and DDoS protection

4. **Performance & Scalability**
   - Design database queries and indexing
   - Plan caching strategies (Redis, CDN)
   - Consider async processing for heavy operations
   - Design for horizontal scaling

### Step 4: Production Planning
1. **Testing Strategy**
   - Unit tests for business logic (>80% coverage)
   - Integration tests for API endpoints
   - Performance and load testing
   - Security testing and penetration testing

2. **Deployment Strategy**
   - Plan CI/CD pipeline stages
   - Design blue-green or canary deployment
   - Plan database migrations
   - Design monitoring and alerting

3. **Monitoring & Observability**
   - Plan application metrics and logging
   - Design health check endpoints
   - Plan distributed tracing
   - Design error tracking and alerting

## Production Questions to Answer

Before implementing, clarify:
- **Business Impact**: What is the business value and ROI?
- **Scale Requirements**: Expected load, growth projections?
- **Security Requirements**: Authentication levels, data sensitivity?
- **Performance SLAs**: Response time, throughput requirements?
- **Failure Scenarios**: How does the system handle failures?
- **Monitoring Needs**: What metrics and alerts are required?
- **Compliance Requirements**: GDPR, SOC2, industry standards?
- **Rollback Strategy**: How to rollback if issues occur?

## Production Implementation Plan Template

```
## Implementation Plan for [Feature]

### Business Requirements
- Goal: [business objective]
- Success Criteria: [measurable outcomes]
- KPIs: [key performance indicators]

### Technical Architecture
- Design Patterns: [Repository, Service Layer, etc.]
- Database Changes: [schema, migrations]
- API Endpoints: [new/modified endpoints]
- Integration Points: [external services, message queues]

### Security & Compliance
- Authentication: [auth strategy]
- Data Protection: [encryption, PII handling]
- Audit Requirements: [logging, compliance]
- Rate Limiting: [protection strategy]

### Performance & Scalability
- Caching Strategy: [Redis, application-level]
- Database Optimization: [indexes, query optimization]
- Async Processing: [background jobs, queues]
- Scaling Plan: [horizontal scaling, load balancing]

### Testing Strategy
- Unit Tests: [coverage requirements]
- Integration Tests: [API, database tests]
- Performance Tests: [load testing scenarios]
- Security Tests: [penetration testing]

### Deployment & Operations
- CI/CD Pipeline: [stages, approvals]
- Migration Strategy: [database, configuration]
- Monitoring: [metrics, alerts, dashboards]
- Rollback Plan: [recovery procedures]

### Risk Assessment
- Technical Risks: [complexity, dependencies]
- Operational Risks: [deployment, monitoring]
- Mitigation Strategies: [risk reduction plans]

### Resource Requirements
- Development Effort: [story points, timeline]
- Infrastructure: [servers, databases, services]
- Team Skills: [required expertise]
```

## Production Checklist

### Requirements Analysis
- [ ] Business requirements clearly defined
- [ ] Non-functional requirements identified
- [ ] Success criteria and KPIs established
- [ ] Compliance requirements understood

### Technical Design
- [ ] Architecture patterns selected
- [ ] Database schema designed
- [ ] API contracts defined
- [ ] Security architecture planned
- [ ] Performance strategy designed
- [ ] Scalability approach defined

### Production Readiness
- [ ] Testing strategy comprehensive
- [ ] CI/CD pipeline planned
- [ ] Monitoring and observability designed
- [ ] Deployment strategy defined
- [ ] Rollback procedures planned
- [ ] Risk assessment completed

### Documentation
- [ ] Technical documentation complete
- [ ] API documentation updated
- [ ] Operational runbooks created
- [ ] Monitoring dashboards designed

## How to Invoke

```
Analyze and plan [feature/fix description] for production deployment using the backend-analysis-plan skill
```

## Related Skills

- **Implementation**: Use `backend-code` skill for development
- **Testing**: Use `backend-test` skill for comprehensive testing
- **Review**: Use `backend-review` skill for production readiness review

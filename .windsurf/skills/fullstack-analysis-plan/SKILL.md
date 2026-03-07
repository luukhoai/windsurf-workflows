---
name: fullstack-analysis-plan
description: Production-ready analysis and planning skill for comprehensive fullstack architecture
---

# Fullstack Analysis Plan Skill

This skill guides through comprehensive requirement analysis and architectural planning for production fullstack systems, ensuring seamless integration between backend and frontend with enterprise-grade standards.

## When to Use
- Before starting any new fullstack feature or system
- When requirements span both backend and frontend layers
- When designing comprehensive API contracts and data flows
- Before major refactoring affecting both layers
- For enterprise application architecture planning
- When implementing microservices or distributed systems
- For performance and scalability planning across layers

## Production Analysis Process

### Step 1: Understand Business & System Requirements
1. **Business Requirements Analysis**
   - Read and understand comprehensive feature/fix requirements
   - Identify user stories, acceptance criteria, and success metrics
   - Define business constraints, SLAs, and compliance requirements
   - Consider internationalization, localization, and accessibility needs

2. **System Requirements Analysis**
   - Identify non-functional requirements (performance, security, scalability)
   - Define system boundaries and integration points
   - Consider deployment architecture and infrastructure requirements
   - Plan for monitoring, logging, and operational requirements

3. **User Experience Requirements**
   - Define target user personas and use cases
   - Plan responsive design and mobile requirements
   - Consider accessibility compliance (WCAG 2.1 AA)
   - Design user journeys and interaction flows

### Step 2: Comprehensive Architecture Analysis

#### Backend Architecture Analysis
1. **System Architecture**
   - Use `backend-analysis-plan` skill for detailed backend analysis
   - Design microservices or monolithic architecture
   - Plan data architecture and database design
   - Consider caching strategies and data flow

2. **API Architecture**
   - Design RESTful or GraphQL API architecture
   - Plan API versioning and evolution strategy
   - Define authentication and authorization patterns
   - Consider rate limiting and API security

3. **Integration Architecture**
   - Identify external service integrations
   - Plan message queuing and event-driven architecture
   - Design error handling and resilience patterns
   - Consider monitoring and observability

#### Frontend Architecture Analysis
1. **Component Architecture**
   - Use `frontend-analysis-plan` skill for detailed frontend analysis
   - Design Atomic Design component hierarchy
   - Plan state management strategy (local, global, server state)
   - Consider component composition and reusability

2. **Performance Architecture**
   - Plan code splitting and lazy loading strategies
   - Design caching and optimization strategies
   - Consider Core Web Vitals and performance budgets
   - Plan for mobile performance optimization

3. **Accessibility Architecture**
   - Design semantic HTML structure and landmarks
   - Plan ARIA implementation and keyboard navigation
   - Consider screen reader compatibility
   - Design focus management and skip links

### Step 3: Design Production Solution Architecture

#### API Contract Design
1. **Endpoint Design**
   - Design comprehensive API endpoints with proper HTTP methods
   - Define request/response schemas with validation rules
   - Plan error response formats and status codes
   - Consider API pagination, filtering, and sorting

2. **Data Contract Design**
   - Define data models and transfer objects
   - Plan data validation and transformation
   - Consider data serialization formats (JSON, XML)
   - Design versioning strategy for data contracts

3. **Security Contract Design**
   - Define authentication and authorization requirements
   - Plan token management and session handling
   - Design API key management and rate limiting
   - Consider CORS policies and security headers

#### Integration Architecture Design
1. **Data Flow Architecture**
   - Design comprehensive data flow between layers
   - Plan state synchronization strategies
   - Consider optimistic updates and conflict resolution
   - Design error propagation and recovery

2. **Event-Driven Architecture**
   - Design event patterns for real-time updates
   - Plan WebSocket or SSE implementations
   - Consider event sourcing and CQRS patterns
   - Design event validation and error handling

3. **Performance Integration**
   - Design caching strategies across layers
   - Plan CDN integration and asset optimization
   - Consider database connection pooling and optimization
   - Design load balancing and scaling strategies

### Step 4: Production Planning

#### Testing Strategy
1. **Comprehensive Testing Plan**
   - Unit tests for both backend and frontend (>80% coverage)
   - Integration tests for API contracts and data flows
   - E2E tests for critical user journeys
   - Performance tests for system scalability
   - Security tests for vulnerability prevention
   - Accessibility tests for WCAG compliance

2. **Quality Gates Definition**
   - Define code quality standards and linting rules
   - Establish performance benchmarks and SLAs
   - Set security scanning and vulnerability thresholds
   - Plan automated testing in CI/CD pipeline

#### Deployment Strategy
1. **Infrastructure Planning**
   - Design containerization strategy (Docker, Kubernetes)
   - Plan CI/CD pipeline with automated deployments
   - Consider environment management (dev, staging, prod)
   - Design monitoring, logging, and alerting

2. **Operational Planning**
   - Plan health checks and monitoring endpoints
   - Design error tracking and alerting systems
   - Consider backup and disaster recovery strategies
   - Plan scaling and auto-scaling strategies

## Production Questions to Answer

Before implementing fullstack systems, clarify:

### Business & System Questions
- **Business Impact**: What is the business value and user impact?
- **Scale Requirements**: What are the expected load and scalability requirements?
- **Compliance**: Are there regulatory compliance requirements (GDPR, accessibility)?
- **Integration**: What external systems and services need integration?

### Technical Architecture Questions
- **Architecture Pattern**: Monolithic, microservices, or hybrid architecture?
- **Data Strategy**: What are the data storage, caching, and synchronization strategies?
- **Performance**: What are the performance targets (response times, throughput, Core Web Vitals)?
- **Security**: What are the security requirements and threat models?

### Operational Questions
- **Deployment**: What are the deployment and infrastructure requirements?
- **Monitoring**: What monitoring, logging, and alerting are needed?
- **Maintenance**: What are the maintenance and operational requirements?
- **Scaling**: How will the system scale horizontally and vertically?

## Production Implementation Plan Template

```
## Fullstack Implementation Plan for [Feature]

### Business & System Requirements
- User Stories: [detailed user stories with acceptance criteria]
- Success Metrics: [KPIs and measurable outcomes]
- Compliance Requirements: [GDPR, accessibility, security compliance]
- SLA Requirements: [performance, availability, scalability targets]

### Backend Architecture Design
- System Architecture: [monolithic/microservices/hybrid pattern]
- Database Design: [schema, migrations, optimization strategies]
- API Architecture: [RESTful/GraphQL, versioning, documentation]
- Security Architecture: [authentication, authorization, data protection]
- Integration Architecture: [external services, message queues, events]

### Frontend Architecture Design
- Component Architecture: [Atomic Design hierarchy, composition patterns]
- State Management: [local, global, server state strategies]
- Performance Architecture: [code splitting, caching, Core Web Vitals]
- Accessibility Architecture: [WCAG 2.1 AA compliance, semantic HTML, ARIA]
- Integration Architecture: [API integration, error handling, data flow]

### API Contract Specification
#### Endpoints:
- [method] /api/endpoint1
  - Request: [detailed schema with validation]
  - Response: [detailed schema with examples]
  - Error Responses: [error codes and formats]
  - Authentication: [required auth mechanisms]

#### Data Models:
- Model1: [fields, types, validation rules]
- Model2: [fields, types, relationships]

#### Security Contract:
- Authentication: [JWT, OAuth, API keys]
- Authorization: [RBAC, permissions, scopes]
- Rate Limiting: [limits, windows, strategies]

### Integration Architecture
- Data Flow: [comprehensive data flow diagram]
- State Synchronization: [strategies for consistency]
- Error Handling: [propagation, recovery, user experience]
- Performance Integration: [caching, optimization, monitoring]

### Testing Strategy
#### Backend Testing:
- Unit Tests: [coverage requirements, test patterns]
- Integration Tests: [API, database, external services]
- Performance Tests: [load testing, stress testing]
- Security Tests: [penetration testing, vulnerability scanning]

#### Frontend Testing:
- Unit Tests: [component, hook, utility testing]
- Integration Tests: [component interactions, API integration]
- E2E Tests: [critical user journeys, cross-browser]
- Accessibility Tests: [axe-core, manual testing, compliance]

#### Integration Testing:
- Full Stack Tests: [end-to-end user workflows]
- API Contract Tests: [request/response validation]
- Performance Tests: [integrated system performance]
- Security Tests: [full stack security validation]

### Deployment Strategy
- Containerization: [Docker configuration, Kubernetes setup]
- CI/CD Pipeline: [automated testing, deployment stages]
- Environment Management: [dev, staging, production configurations]
- Infrastructure: [cloud services, networking, storage]

### Operational Planning
- Monitoring: [metrics, dashboards, alerting]
- Logging: [structured logging, correlation IDs]
- Error Tracking: [error reporting, debugging tools]
- Health Checks: [application, database, external dependencies]

### Risk Assessment
- Technical Risks: [complexity, dependencies, scalability]
- Performance Risks: [bottlenecks, resource constraints]
- Security Risks: [vulnerabilities, data exposure]
- Operational Risks: [deployment failures, downtime]
- Mitigation Strategies: [risk reduction and contingency plans]

### Resource Requirements
- Development Team: [skills, roles, timeline]
- Infrastructure: [compute, storage, networking requirements]
- Tools & Services: [monitoring, testing, deployment tools]
- Budget: [development, operational, scaling costs]
```

## Production Checklist

### Requirements Analysis
- [ ] Business requirements clearly defined with success metrics
- [ ] System requirements identified (performance, security, scalability)
- [ ] User experience requirements specified
- [ ] Compliance requirements identified (GDPR, accessibility)
- [ ] Integration requirements documented

### Architecture Design
- [ ] Backend architecture designed (patterns, database, API)
- [ ] Frontend architecture designed (components, state, performance)
- [ ] API contract comprehensively specified
- [ ] Integration architecture designed (data flow, events)
- [ ] Security architecture planned (auth, authorization, data protection)

### Production Planning
- [ ] Testing strategy comprehensive (unit, integration, E2E, performance, security)
- [ ] Deployment strategy designed (containerization, CI/CD)
- [ ] Operational planning complete (monitoring, logging, health checks)
- [ ] Risk assessment completed with mitigation strategies
- [ ] Resource requirements identified and planned

### Quality Assurance
- [ ] Performance targets defined (response times, Core Web Vitals)
- [ ] Security requirements specified (threat models, compliance)
- [ ] Accessibility compliance planned (WCAG 2.1 AA)
- [ ] Scalability requirements established (load, growth)
- [ ] Monitoring and alerting strategy defined

## How to Invoke

```
Analyze and plan [fullstack feature] for production deployment using the fullstack-analysis-plan skill
Design comprehensive fullstack architecture for [system] using the fullstack-analysis-plan skill
Plan production-ready API contracts and integration using the fullstack-analysis-plan skill
```

## Related Skills

- **Backend Analysis**: Use `backend-analysis-plan` skill for detailed backend analysis
- **Frontend Analysis**: Use `frontend-analysis-plan` skill for detailed frontend analysis
- **Backend Implementation**: Use `backend-code` skill for production backend development
- **Frontend Implementation**: Use `frontend-code` skill for production frontend development
- **Testing**: Use `backend-test`, `frontend-test`, and `fullstack-test` skills for comprehensive testing
- **Review**: Use `backend-review` and `frontend-review` skills for production readiness assessment

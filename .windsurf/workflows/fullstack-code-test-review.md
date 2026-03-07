---
name: fullstack-code-test-review
description: Production-ready CI-style pipeline for fullstack analyze → implement → test → review with comprehensive architecture compliance
---

# Fullstack Code-Test-Review Pipeline

## Concept

- **Rules** → Enhanced Standards (`.windsurf/rules/`)
- **Skills** → Implementation + Lint + Security Scan + Full Architecture Review
- **Quality Gates** → Code + Architecture + Performance + Accessibility + Security + Integration Tests

## Pipeline

```
        ┌──────────┐
        │  ANALYZE │  ← Fullstack Architecture Planning
        │  Plan   │
        │Full Arch│
        └────┬─────┘
             │
    ┌────────┴────────┐
    │                   │
    ▼                   ▼
┌────────┐         ┌────────┐
│BACKEND │         │FRONTEND│  ← Production Implementation
│ CODE   │         │  CODE  │
│Full Arch│         │Full Arch│
└───┬─────┘         └───┬─────┘
    └────────┬────────┘
             │
             ▼
        ┌────────┐
        │  TEST  │  ← Comprehensive Testing
        │Verify  │
        │Full Arch│
        └────┬─────┘
             │
             ▼
        ┌────────┐
        │ REVIEW │  ← Production Readiness Review
        │Quality+ │
        │Comprehensive│
        └────────┘
```

## Prerequisites

**Backend:** `.windsurf/rules/backend-development.md` - Comprehensive backend architecture standards
**Frontend:** `.windsurf/rules/frontend-development.md` - Production frontend architecture standards

---

## Stage 1: Analyze & Plan

**Skill:** `fullstack-analysis-plan`

### Analysis Checklist
- [ ] Fullstack requirements clearly defined with user stories
- [ ] Backend architecture planned (OOP/SOLID, database, API design)
- [ ] Frontend architecture planned (Atomic Design, accessibility, performance)
- [ ] API contract designed with comprehensive specifications
- [ ] Data flow and state management strategy defined
- [ ] Security requirements identified for both layers
- [ ] Performance requirements established (Core Web Vitals, API response times)
- [ ] Integration points and dependencies identified
- [ ] Testing strategy for both layers and integration
- [ ] Deployment and operational considerations planned

### Gate: Plan written with comprehensive fullstack architecture considerations

---

## Stage 2: Implement

**Skills:** `backend-code` + `frontend-code`

Includes: Code + Lint + Security Scan + Full Architecture Compliance for each layer

### Commands
```bash
# Backend Implementation
cd contact-form-app/backend
source venv/bin/activate

# Run app
python run.py

# Quality checks
flake8 app/ tests/
black app/ tests/
snyk code test --severity-threshold=medium

# Type checking and security
python -m mypy app/
pytest tests/ --cov=app

# Frontend Implementation
cd contact-form-app/frontend

# Run app
npm start

# Quality checks
npm run lint
npm run type-check
npm run format

# Security and performance
snyk code test --severity-threshold=medium
npm audit
npm run analyze
npm run test:a11y
```

### Implementation Checks
#### Backend
- [ ] Backend follows OOP/SOLID principles and enterprise patterns
- [ ] Database design properly normalized and optimized
- [ ] API follows RESTful conventions with proper documentation
- [ ] Security measures implemented (authentication, validation, SQL injection prevention)
- [ ] Performance optimizations applied (caching, query optimization)
- [ ] Error handling and logging comprehensive
- [ ] Testing coverage >80% with comprehensive test suite

#### Frontend
- [ ] Frontend follows Atomic Design principles
- [ ] TypeScript strict typing implemented throughout
- [ ] Accessibility compliance (WCAG 2.1 AA) achieved
- [ ] Performance optimizations applied (Core Web Vitals, memoization)
- [ ] Security measures implemented (XSS prevention, CSP headers)
- [ ] Component architecture scalable and maintainable
- [ ] Testing coverage >80% with accessibility and E2E tests

#### Integration
- [ ] API contract properly implemented on both ends
- [ ] Error handling consistent across layers
- [ ] Data flow and state management working correctly
- [ ] Security tokens and authentication properly integrated
- [ ] Performance impact of integration considered

### Gate: Both layers pass with full architecture compliance

---

## Stage 3: Test

**Skills:** `backend-test` + `frontend-test` + Integration Testing

### Commands
```bash
# Backend Testing
cd contact-form-app/backend
pytest tests/ -v --cov=app --cov-report=html
pytest tests/ -v --cov=app --cov-fail-under=80

# Frontend Testing
cd contact-form-app/frontend
npm test -- --watchAll=false --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80,"statements":80}}'
npm run test:e2e
npm run test:a11y
npm run test:performance

# Integration Testing
# Start both servers and test full workflows
npm run test:integration
```

### Testing Requirements
#### Backend Tests
- [ ] Unit tests for all business logic (>80% coverage)
- [ ] Integration tests for API endpoints
- [ ] Database tests with migrations and constraints
- [ ] Security tests for authentication and authorization
- [ ] Performance tests for API response times
- [ ] Error handling and edge case testing

#### Frontend Tests
- [ ] Unit tests for all components and hooks (>80% coverage)
- [ ] Integration tests for component interactions
- [ ] E2E tests for critical user journeys
- [ ] Accessibility tests with axe-core integration
- [ ] Performance tests and Core Web Vitals measurement
- [ ] Visual regression tests for UI consistency

#### Integration Tests
- [ ] Full user journey testing from frontend to backend
- [ ] API contract validation between layers
- [ ] Error propagation testing across layers
- [ ] Authentication and authorization flow testing
- [ ] Performance testing of integrated system
- [ ] Cross-browser compatibility testing

### Gate: All tests pass with comprehensive coverage and integration validation

---

## Stage 4: Review

**Skills:** `backend-review` + `frontend-review` + Integration Review

### Review Checklist
#### Backend Review
- [ ] Architecture compliance with OOP/SOLID principles
- [ ] Code quality and maintainability standards met
- [ ] Security implementation comprehensive and robust
- [ ] Performance optimization appropriate and effective
- [ ] Database design optimized for scalability
- [ ] API design follows RESTful conventions
- [ ] Documentation complete and accurate

#### Frontend Review
- [ ] Component architecture follows Atomic Design
- [ ] Accessibility compliance (WCAG 2.1 AA) verified
- [ ] Performance meets Core Web Vitals targets
- [ ] Security implementation prevents XSS and other vulnerabilities
- [ ] Code quality and TypeScript standards met
- [ ] User experience and responsive design appropriate
- [ ] Testing coverage comprehensive and effective

#### Integration Review
- [ ] API contract properly implemented and documented
- [ ] Error handling consistent and user-friendly
- [ ] Data flow and state management efficient
- [ ] Security integration seamless and robust
- [ ] Performance impact acceptable and optimized
- [ ] Documentation for integration complete
- [ ] Production readiness verified

### Gate: Both layers reviewed and approved with integration validation

---

## Usage & Reference

### Invoke Pipeline
```bash
# Full pipeline
Use the fullstack-code-test-review pipeline to implement [feature] with comprehensive architecture compliance

# By stage
Analyze using fullstack-analysis-plan skill (include fullstack architecture design)
Implement backend using backend-code skill (follow comprehensive standards)
Implement frontend using frontend-code skill (follow production standards)
Test using backend-test, frontend-test, and integration skills
Review using backend-review and frontend-review skills (check full compliance)
```

### Stage Reference

| Stage | Skills | Gate | Focus |
|-------|--------|------|-------|
| 1. Analyze | fullstack-analysis-plan | Plan written | Requirements + Full Architecture Design |
| 2. Implement | backend-code, frontend-code | Both layers pass | Implementation + Complete Compliance |
| 3. Test | backend-test, frontend-test, integration | All tests pass | Verification + Comprehensive Testing |
| 4. Review | backend-review, frontend-review, integration | Approved | Code Quality + Full Architecture Review |

---

## Enhanced Features

### Quality Gates
- **Code Quality**: ESLint, Prettier, TypeScript strict mode, PEP 8, Black formatter
- **Architecture Quality**: OOP/SOLID, Atomic Design, React patterns, enterprise patterns
- **Security Quality**: SQL injection prevention, XSS prevention, CSP headers, authentication
- **Performance Quality**: Core Web Vitals, API response times, database optimization
- **Accessibility Quality**: WCAG 2.1 AA compliance, keyboard navigation, screen reader support
- **Integration Quality**: API contract validation, end-to-end testing, cross-layer consistency

### Production Readiness
- **Backend**: Database migrations, API documentation, error tracking, monitoring
- **Frontend**: Bundle optimization, performance monitoring, accessibility compliance
- **Integration**: API contract testing, full user journey validation, error propagation
- **Deployment**: Environment configuration, health checks, graceful shutdown
- **Operations**: Logging, monitoring, alerting, documentation

### Development Experience
- **Hot Reload**: Development servers for both backend and frontend
- **Type Safety**: Strict TypeScript and Python type checking
- **Code Quality**: Automated linting and formatting for both layers
- **Testing**: Comprehensive test suites with coverage requirements
- **Documentation**: API documentation and component documentation

---

## Verification

- [ ] Fullstack architecture plan documented with comprehensive considerations
- [ ] Backend implementation complete with full compliance
- [ ] Frontend implementation complete with production standards
- [ ] All tests pass with coverage and integration validation
- [ ] Both layers reviewed and approved
- [ ] Integration testing complete and successful
- [ ] Performance benchmarks met for both layers
- [ ] Accessibility compliance verified
- [ ] Security measures implemented and tested
- [ ] Production deployment ready
- [ ] Documentation complete and up-to-date
- [ ] All quality gates passed
- [ ] ✅ Ready for production

---

## Related Skills

- **Analysis**: Use `fullstack-analysis-plan` skill for comprehensive planning
- **Backend Implementation**: Use `backend-code` skill for production backend development
- **Frontend Implementation**: Use `frontend-code` skill for production frontend development
- **Testing**: Use `backend-test`, `frontend-test`, and integration skills for comprehensive testing
- **Review**: Use `backend-review` and `frontend-review` skills for production readiness assessment

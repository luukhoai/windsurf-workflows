---
name: backend-code-test-review
description: Professional CI-style pipeline for backend analyze → implement → test → review with comprehensive architecture compliance
---

# Backend Code-Test-Review Pipeline

## Concept

- **Rules** → Enhanced Standards (`.windsurf/rules/backend-development.md`)
- **Skills** → Implementation + Lint + Security Scan + Full Architecture Review
- **Quality Gates** → Code + Architecture + Database + API + Security + Tests

## Pipeline

```
┌──────────┐  ┌───────────┐  ┌─────────┐  ┌──────────┐
│ ANALYZE │─▶│ IMPLEMENT │─▶│  TEST   │─▶│  REVIEW  │
│  Plan   │  │Code+Lint│ │ Verify │  │Quality+  │
│Full Arch│  │+Security│ │+Full Arch│ │Comprehensive│
└──────────┘  └───────────┘  └─────────┘  └──────────┘
```

## Prerequisites

See `.windsurf/rules/backend-development.md` for comprehensive backend architecture standards including OOP, SOLID, database, API, security, performance, and DevOps guidelines.

---

## Stage 1: Analyze & Plan

**Skill:** `backend-analysis-plan`

### Analysis Checklist
- [ ] Requirements clearly defined
- [ ] OOP design patterns identified
- [ ] SOLID principles applied
- [ ] Package structure planned
- [ ] Dependencies identified
- [ ] Database schema designed
- [ ] API architecture planned
- [ ] Security requirements assessed
- [ ] Performance considerations identified
- [ ] Scalability requirements analyzed
- [ ] Integration points defined

### Gate: Plan written with comprehensive architecture considerations

---

## Stage 2: Implement

**Skill:** `backend-code`

Includes: Code + Lint + Security Scan + Full Architecture Compliance

### Commands
```bash
cd contact-form-app/backend
source venv/bin/activate

# Run app
python run.py

# Run lint
flake8 app/ tests/

# Run security scan
snyk code test --severity-threshold=medium

# Format code
black app/ tests/
```

### OOP/SOLID Implementation Checks
- [ ] Classes follow SRP (single responsibility)
- [ ] Dependencies injected (DIP)
- [ ] Interfaces segregated (ISP)
- [ ] Open/closed principle followed (OCP)
- [ ] Substitutable implementations (LSP)

### Database Implementation Checks
- [ ] Schema follows normalization principles
- [ ] Proper indexing implemented
- [ ] Data integrity constraints defined
- [ ] Migration scripts created
- [ ] Connection pooling configured

### API Implementation Checks
- [ ] RESTful conventions followed
- [ ] Proper HTTP methods used
- [ ] Status codes correctly applied
- [ ] API versioning implemented
- [ ] Request/response validation added

### Security Implementation Checks
- [ ] Input validation implemented
- [ ] Authentication/authorization added
- [ ] SQL injection prevention in place
- [ ] CORS properly configured
- [ ] Sensitive data protected

### Performance Implementation Checks
- [ ] Database queries optimized
- [ ] Caching strategies implemented
- [ ] Async processing for long operations
- [ ] Resource cleanup implemented
- [ ] Memory management addressed

### Gate: Code + Lint + Security + Full Architecture pass

---

## Stage 3: Test

**Skill:** `backend-test`

### Command
```bash
pytest tests/ -v
```

### Testing Requirements
- [ ] Unit tests for all classes (>80% coverage)
- [ ] Integration tests for component interactions
- [ ] Mock external dependencies
- [ ] Test error handling and edge cases
- [ ] Verify OOP design through tests
- [ ] Database integration tests
- [ ] API endpoint tests
- [ ] Security vulnerability tests
- [ ] Performance load tests
- [ ] Error recovery tests

### Gate: All tests pass with coverage requirements

---

## Stage 4: Review

**Skill:** `backend-review`

### Review Checklist
- [ ] Code follows PEP 8 and project standards
- [ ] OOP principles properly implemented
- [ ] SOLID principles followed
- [ ] Design patterns correctly applied
- [ ] Security requirements met
- [ ] Performance considerations addressed
- [ ] Documentation adequate
- [ ] Database design reviewed and approved
- [ ] API architecture validated
- [ ] Scalability concerns addressed

### Architecture Review
- [ ] Package structure follows guidelines
- [ ] Separation of concerns maintained
- [ ] Dependency injection implemented
- [ ] Repository pattern used where appropriate
- [ ] Service layer properly designed
- [ ] Database schema properly normalized
- [ ] API design follows RESTful principles
- [ ] Security architecture comprehensive
- [ ] Performance optimizations implemented
- [ ] Scalability patterns applied

### Gate: Code and architecture reviewed and approved

---

## Usage & Reference

### Invoke Pipeline
```bash
# Full pipeline
Use the backend-code-test-review pipeline to implement [feature] with comprehensive architecture compliance

# By stage
Analyze using backend-analysis-plan skill (include full architecture design)
Implement using backend-code skill (follow comprehensive standards)
Test using backend-test skill (verify complete architecture)
Review using backend-review skill (check full compliance)
```

### Stage Reference

| Stage | Skill | Gate | Focus |
|-------|-------|------|-------|
| 1. Analyze | backend-analysis-plan | Plan written | Requirements + Full Architecture Design |
| 2. Implement | backend-code | Code+Lint+Security pass | Implementation + Complete Compliance |
| 3. Test | backend-test | Tests pass + Coverage | Verification + Comprehensive Testing |
| 4. Review | backend-review | Approved | Code Quality + Full Architecture Review |

## Quality Gates Summary

### Code Quality
- ✅ PEP 8 compliance (flake8)
- ✅ Security scan passed (snyk)
- ✅ Code formatted (black)

### Architecture Quality
- ✅ OOP principles followed
- ✅ SOLID principles applied
- ✅ Design patterns correctly used
- ✅ Package structure compliant
- ✅ Database design properly normalized
- ✅ API architecture RESTful compliant
- ✅ Security architecture implemented
- ✅ Performance considerations addressed
- ✅ Scalability patterns applied

### Database Quality
- ✅ Proper schema design and indexing
- ✅ Data integrity constraints implemented
- ✅ Migration strategy defined
- ✅ Connection pooling configured
- ✅ Query optimization applied

### API Quality
- ✅ RESTful principles followed
- ✅ Proper HTTP status codes
- ✅ API versioning strategy
- ✅ Documentation complete
- ✅ Security measures implemented
- ✅ Performance optimizations applied

### Testing Quality
- ✅ Unit tests (>80% coverage)
- ✅ Integration tests
- ✅ Error handling tested
- ✅ Architecture verified through tests

## Verification

- [ ] Plan documented with comprehensive architecture design
- [ ] Implementation complete with full compliance
- [ ] Tests pass with coverage and comprehensive testing
- [ ] Code and architecture fully reviewed
- [ ] Database design validated
- [ ] API architecture verified
- [ ] Security architecture confirmed
- [ ] Performance optimizations validated
- [ ] Scalability patterns applied
- [ ] All quality gates passed
- [ ] ✅ Ready for production

## Enhanced Features

### Comprehensive Architecture Enforcement
- Automatic checks for OOP/SOLID principle violations
- Database design compliance verification
- API architecture validation
- Security architecture enforcement
- Performance optimization verification
- Scalability pattern validation

### Complete Testing Strategy
- Unit test coverage requirements
- Integration test mandates
- Database integration testing
- API endpoint testing
- Security vulnerability testing
- Performance load testing
- Architecture verification through testing

### Full-Stack Quality Assurance
- Code quality and formatting
- Security scanning and prevention
- Database schema validation
- API design compliance
- Performance benchmarking
- Scalability assessment
- Documentation completeness

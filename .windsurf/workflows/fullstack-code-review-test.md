---
name: Fullstack Code-Review-Test Pipeline
description: Professional CI-style pipeline for fullstack: analyze → backend code → frontend code → lint → scan → review → test
---

# Fullstack Code-Review-Test Pipeline

A professional workflow combining analysis, code implementation, linting, security scan, review, and testing for fullstack development (backend + frontend).

## Pipeline Overview

```
                         ┌─────────────────────────┐
                         │      ANALYZE & PLAN    │
                         │   (Full Application)   │
                         └───────────┬─────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
                    ▼                                 ▼
        ┌───────────────────┐             ┌───────────────────┐
        │   BACKEND CODE   │             │   FRONTEND CODE   │
        │  Implement API   │             │   Implement UI    │
        └────────┬─────────┘             └────────┬─────────┘
                 │                                 │
                 └─────────────┬───────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   COMBINED LINT    │
                    │  Backend + Frontend│
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   SECURITY SCAN     │
                    │  Backend + Frontend │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   CODE REVIEW       │
                    │  Backend + Frontend │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   TESTING           │
                    │  Backend + Frontend │
                    └──────────┬──────────┘
                               │
                               ▼
                         ✅ DONE
```

## Gate Logic

Each stage is a **gate**:
- **PASS** → proceed to the next stage
- **FAIL** → go back to the appropriate stage to fix, then rerun from that stage

```
Stage n FAIL → Fix at relevant previous stage → Run from that stage
```

---

## Stage 1: Analyze & Plan

### Fullstack Analysis
1. Understand requirements for full application (backend + frontend)
2. Explore existing code in both backend and frontend
3. Design solution for both layers
4. Document implementation plan
5. Identify API contracts between frontend and backend

### Analysis Checklist
- [ ] Requirements fully understood
- [ ] Backend API design planned
- [ ] Frontend UI/UX design planned
- [ ] API contract defined
- [ ] Edge cases identified for both layers
- [ ] Implementation plan documented

### Gate Criteria
- [ ] Requirements are clear and unambiguous
- [ ] Implementation plan is written
- [ ] API contract defined between frontend and backend

### If FAIL → Exit pipeline (cannot code without understanding requirements)

---

## Stage 2: Backend Code Implementation

### Using backend-code skill
1. Implement API endpoints in `contact-form-app/backend/app.py`
2. Follow backend coding standards
3. Add appropriate logging
4. Handle edge cases

### Backend Implementation Checklist
- [ ] API endpoints implemented according to requirements
- [ ] Error handling in place
- [ ] Logging added
- [ ] Type hints used

### Gate Criteria
- [ ] Backend code compiles (no Python syntax errors)
- [ ] API endpoints respond correctly

### If FAIL → Fix backend code → Rerun Stage 2

---

## Stage 3: Frontend Code Implementation

### Using frontend-code skill
1. Implement UI components in React
2. Follow frontend coding standards
3. Add proper TypeScript types
4. Integrate with backend API
5. Handle edge cases

### Frontend Implementation Checklist
- [ ] UI components implemented according to requirements
- [ ] TypeScript types defined
- [ ] State management implemented
- [ ] API integration working
- [ ] Error handling in place

### Gate Criteria
- [ ] Frontend code compiles (no TypeScript errors)
- [ ] Components render without errors
- [ ] API integration working

### If FAIL → Fix frontend code → Rerun Stage 3

---

## Stage 4: Combined Lint

### Run both backend and frontend linters

#### Backend Lint
```bash
cd contact-form-app/backend
source venv/bin/activate
flake8 . --max-line-length=100 --ignore=E501,W503
```

#### Frontend Lint
```bash
cd contact-form-app/frontend
npm run lint
```

### Lint Checklist
- [ ] Backend: flake8 passes with no errors
- [ ] Frontend: ESLint passes with no errors
- [ ] No TypeScript errors in frontend
- [ ] Code formatting applied

### Gate Criteria
- [ ] All linters pass with no errors

### If FAIL → Fix code (Stage 2 or Stage 3) → Rerun Stage 4

---

## Stage 5: Security Scan

### Run security scans on both layers

#### Backend Security
```bash
cd contact-form-app/backend
snyk code test --severity-threshold=medium
```

#### Frontend Security
```bash
cd contact-form-app/frontend
snyk code test --severity-threshold=medium
npm audit
```

### Security Checklist
- [ ] Backend: No SQL injection vulnerabilities
- [ ] Backend: Input validation in place
- [ ] Backend: No hardcoded secrets
- [ ] Frontend: No XSS vulnerabilities
- [ ] Frontend: No sensitive data in code
- [ ] Dependencies have no known vulnerabilities

### Gate Criteria
- [ ] No critical/high security issues in either layer

### If FAIL → Fix code (Stage 2 or Stage 3) → Rerun Stage 5

---

## Stage 6: Code Review

### Using backend-review and frontend-review skills
1. Review backend code for API design, security, quality
2. Review frontend code for React patterns, TypeScript, accessibility
3. Verify frontend-backend integration
4. Ensure consistency across both layers

### Review Focus Areas

#### Backend (backend-review skill)
- **API Design**: RESTful conventions, HTTP methods, status codes
- **Security**: Input validation, injection prevention
- **Error Handling**: Proper exceptions, status codes
- **Code Quality**: Readability, naming, duplication

#### Frontend (frontend-review skill)
- **React Patterns**: Hooks usage, component structure
- **TypeScript**: Proper typing, no `any`
- **Accessibility**: ARIA labels, keyboard navigation
- **Code Quality**: Readability, naming, duplication

#### Integration
- [ ] Frontend correctly calls backend API
- [ ] Data formats match between layers
- [ ] Error handling consistent

### Review Checklist
- [ ] Backend code reviewed
- [ ] Frontend code reviewed
- [ ] Integration verified
- [ ] No critical issues found

### Gate Criteria
- [ ] Code review passed (no critical issues)

### If FAIL → Fix code (Stage 2 or Stage 3) → Rerun Stage 4 → Rerun Stage 5 → Rerun Stage 6

---

## Stage 7: Testing

### Run tests for both layers

#### Backend Tests
```bash
cd contact-form-app/backend
source venv/bin/activate
pytest -v
```

#### Frontend Tests
```bash
cd contact-form-app/frontend
npm test -- --watchAll=false
```

### Test Checklist
- [ ] Backend: Existing tests pass (no regression)
- [ ] Backend: New feature tests added
- [ ] Backend: Edge cases covered
- [ ] Frontend: Existing tests pass (no regression)
- [ ] Frontend: New feature tests added
- [ ] Frontend: Edge cases covered

### Integration Tests
- [ ] Frontend-backend integration working
- [ ] API responses handled correctly
- [ ] Error states handled correctly

### Gate Criteria
- [ ] All tests pass in both backend and frontend

### If FAIL → Fix code (Stage 2 or Stage 3) → Rerun Stage 4 → Rerun Stage 5 → Rerun Stage 6 → Rerun Stage 7

---

## Pipeline Flow with Retry Logic

```
START
  │
  ▼
┌──────────────────┐
│  Stage 1         │──── FAIL ────▶ EXIT
│  ANALYZE & PLAN │──── PASS ────▶
└──────────────────┘
  │
  ▼
┌──────────────────┐     ┌──────────────────┐
│  Stage 2        │     │  Stage 3        │
│  BACKEND CODE   │     │  FRONTEND CODE  │
│  (can parallel) │     │  (can parallel) │
└────────┬─────────┘     └────────┬─────────┘
         │                          │
         └────────────┬─────────────┘
                      │
                      ▼
┌──────────────────┐
│  Stage 4        │──── FAIL ────▶ FIX → Stage 2/3 → Stage 4
│  COMBINED LINT  │──── PASS ────▶
└──────────────────┘
                      │
                      ▼
┌──────────────────┐
│  Stage 5        │──── FAIL ────▶ FIX → Stage 2/3 → Stage 4 → Stage 5
│  SECURITY SCAN  │──── PASS ────▶
└──────────────────┘
                      │
                      ▼
┌──────────────────┐
│  Stage 6        │──── FAIL ────▶ FIX → Stage 2/3 → Stage 4 → Stage 5 → Stage 6
│  CODE REVIEW    │──── PASS ────▶
└──────────────────┘
                      │
                      ▼
┌──────────────────┐
│  Stage 7        │──── FAIL ────▶ FIX → Stage 2/3 → Stage 4 → Stage 5 → Stage 6 → Stage 7
│  TESTING        │──── PASS ────▶
└──────────────────┘
                      │
                      ▼
                    ✅ DONE - Ready for commit
```

---

## Full Pipeline Usage

```bash
# Run full pipeline for a new fullstack feature
Use the fullstack-code-review-test pipeline to implement [feature description]

# Run specific stages
Analyze and plan [feature] using backend-analysis-plan skill
Implement backend API using backend-code skill
Implement frontend UI using frontend-code skill
Lint both layers using backend-lint and frontend-lint skills
Scan both layers using backend-security-scan and frontend-security-scan skills
Review code using backend-review and frontend-review skills
Run tests using backend-test and frontend-test skills
```

## Quick Reference

| Stage | Skills | Commands | Gate |
|-------|--------|----------|------|
| 1. Analyze | backend-analysis-plan, frontend-analysis-plan | Plan feature | Must pass |
| 2. Backend Code | backend-code | Implement API | Syntax OK |
| 3. Frontend Code | frontend-code | Implement UI | No TS errors |
| 4. Lint | backend-lint, frontend-lint | `flake8 .` + `npm run lint` | No errors |
| 5. Scan | backend-security-scan, frontend-security-scan | `snyk code test` | No critical issues |
| 6. Review | backend-review, frontend-review | Review code | No critical issues |
| 7. Test | backend-test, frontend-test | `pytest` + `npm test` | All pass |

## Verification

After completing all stages:
- [ ] Implementation plan documented
- [ ] API contract defined
- [ ] Backend code passes linting
- [ ] Frontend code passes linting
- [ ] No security issues found
- [ ] Code reviewed and approved
- [ ] All tests pass (backend + frontend)
- [ ] Integration working correctly
- [ ] ✅ Ready for commit

## Related Skills

### Backend Skills
- backend-analysis-plan
- backend-code
- backend-lint
- backend-review
- backend-test
- backend-security-scan

### Frontend Skills
- frontend-analysis-plan
- frontend-code
- frontend-lint
- frontend-review
- frontend-test
- frontend-security-scan

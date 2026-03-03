---
name: Backend Code-Review-Test Pipeline
description: Professional CI-style pipeline for backend: analyze → code → lint → scan → review → test
---

# Backend Code-Review-Test Pipeline

A professional workflow combining analysis, code implementation, linting, security scan, review, and testing for backend development.

## Pipeline Overview

```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│ ANALYZE │─▶│  CODE   │─▶│  LINT   │─▶│  SCAN   │─▶│ REVIEW  │─▶│  TEST   │
│  Plan   │  │Implement│  │  Style  │  │Security │  │Quality │  │  Verify │
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
                 ▲              ▲              ▲              ▲              ▲
                 │              │              │              │              │
                 └──────────────┴──────────────┴──────────────┴──────────────┘
                        (if fail → go back to previous stage to fix)
```

## Gate Logic

Each stage is a **gate**:
- **PASS** → proceed to the next stage
- **FAIL** → go back to the previous stage to fix, then run from that stage again

```
Stage n FAIL → Fix at Stage n-1 → Run from Stage n-1
```

---

## Stage 1: Analyze & Plan

### Using backend-analysis-plan skill
1. Understand requirements fully
2. Explore existing code
3. Design solution
4. Document implementation plan

### Analysis Checklist
- [ ] Requirements fully understood
- [ ] Existing code explored
- [ ] Solution designed
- [ ] Edge cases identified
- [ ] Implementation plan documented

### Gate Criteria
- [ ] Requirements are clear and unambiguous
- [ ] Implementation plan is written

### If FAIL → Exit pipeline (cannot code without understanding requirements)

---

## Stage 2: Code Implementation

### Using backend-code skill
1. Implement feature/fix in `contact-form-app/backend/app.py`
2. Follow coding standards from backend-code skill
3. Add appropriate logging
4. Handle edge cases

### Implementation Checklist
- [ ] Feature implemented according to requirements
- [ ] Code follows project conventions
- [ ] Error handling in place
- [ ] Logging added
- [ ] Type hints used

### Gate Criteria
- [ ] Code compiles/parses correctly (Python syntax correct)
- [ ] Basic functionality works

### If FAIL → Fix code → Rerun Stage 2

---

## Stage 3: Lint

### Using backend-lint skill
1. Run flake8 on modified files
2. Fix all linting errors
3. Run black formatter (optional)
4. Run isort for imports (optional)

### Lint Commands
```bash
cd contact-form-app/backend
source venv/bin/activate
flake8 . --max-line-length=100 --ignore=E501,W503
```

### Lint Checklist
- [ ] flake8 passes with no errors
- [ ] Code formatting applied
- [ ] Imports sorted
- [ ] No warnings

### Gate Criteria
- [ ] `flake8` passes with no errors

### If FAIL → Fix code (Stage 2) → Rerun Stage 3

---

## Stage 4: Security Scan

### Using backend-security-scan skill
1. Run Snyk code scan
2. Check for vulnerabilities
3. Fix any security issues found
4. Verify no critical issues remain

### Scan Commands
```bash
# Install Snyk if needed
npm install -g snyk

# Run Snyk Code Scan
cd contact-form-app/backend
snyk code test --severity-threshold=medium
```

### Security Checklist
- [ ] No SQL injection vulnerabilities
- [ ] Input validation in place
- [ ] No hardcoded secrets
- [ ] Error messages don't expose internals
- [ ] Dependencies have no known vulnerabilities

### Gate Criteria
- [ ] No critical/high security issues

### If FAIL → Fix code (Stage 2) → Rerun Stage 3 → Rerun Stage 4

---

## Stage 5: Code Review

### Using backend-review skill
1. Run code-review for the changes
2. Check API design
3. Verify error handling
4. Ensure code quality

### Review Focus Areas
- **API Design**: RESTful conventions, HTTP methods, status codes
- **Security**: Input validation, injection prevention
- **Error Handling**: Proper exceptions, status codes
- **Code Quality**: Readability, naming, duplication

### Review Checklist
- [ ] Code reviewed
- [ ] No security issues found
- [ ] Code quality meets standards
- [ ] Error handling verified

### Gate Criteria
- [ ] Code review passed (no critical issues)

### If FAIL → Fix code (Stage 2) → Rerun Stage 3 → Rerun Stage 4 → Rerun Stage 5

---

## Stage 6: Testing

### Using backend-test skill
1. Run existing tests first (no regression)
2. Write tests for new code
3. Cover edge cases
4. Verify all tests pass

### Test Commands
```bash
cd contact-form-app/backend
source venv/bin/activate

# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=term-missing
```

### Test Checklist
- [ ] Existing tests pass (no regression)
- [ ] New feature tests added
- [ ] Edge cases covered
- [ ] Error cases tested

### Gate Criteria
- [ ] All tests pass (`pytest` exit code 0)

### If FAIL → Fix code (Stage 2) → Rerun Stage 3 → Rerun Stage 4 → Rerun Stage 5 → Rerun Stage 6

---

## Pipeline Flow with Retry Logic

```
START
  │
  ▼
┌──────────────┐
│  Stage 1     │──── FAIL ────▶ EXIT (Requirements unclear)
│  ANALYZE     │──── PASS ────▶
└──────────────┘
  │
  ▼
┌──────────────┐
│  Stage 2     │──── FAIL ────▶ FIX → Stage 2
│  CODE        │──── PASS ────▶
└──────────────┘
  │
  ▼
┌──────────────┐
│  Stage 3     │──── FAIL ────▶ FIX → Stage 2 → Stage 3
│  LINT        │──── PASS ────▶
└──────────────┘
  │
  ▼
┌──────────────┐
│  Stage 4     │──── FAIL ────▶ FIX → Stage 2 → Stage 3 → Stage 4
│  SCAN        │──── PASS ────▶
└──────────────┘
  │
  ▼
┌──────────────┐
│  Stage 5     │──── FAIL ────▶ FIX → Stage 2 → Stage 3 → Stage 4 → Stage 5
│  REVIEW      │──── PASS ────▶
└──────────────┘
  │
  ▼
┌──────────────┐
│  Stage 6     │──── FAIL ────▶ FIX → Stage 2 → Stage 3 → Stage 4 → Stage 5 → Stage 6
│  TEST        │──── PASS ────▶
└──────────────┘
  │
  ▼
  ✅ DONE - Ready for commit
```

---

## Full Pipeline Usage

```bash
# Run full pipeline for a new feature
Use the backend-code-review-test pipeline to implement [feature description]

# Run specific stage (with automatic retry logic if fail)
Analyze and plan [feature] using backend-analysis-plan skill
Implement [feature] using backend-code skill
Lint the code using backend-lint skill
Scan for security issues using backend-security-scan skill
Review [file] using backend-review skill
Run tests using backend-test skill

# When encountering fail:
# - If Lint fail → Fix code then rerun Lint
# - If Scan fail → Fix code then rerun Lint → Scan
# - If Review fail → Fix code then rerun Lint → Scan → Review
# - If Test fail → Fix code then rerun Lint → Scan → Review → Test
```

## Quick Reference

| Stage | Skill | Command | Gate |
|-------|-------|---------|------|
| 1. Analyze | backend-analysis-plan | Plan feature | Must pass |
| 2. Code | backend-code | Implement feature | Syntax OK |
| 3. Lint | backend-lint | `flake8 .` | No errors |
| 4. Scan | backend-security-scan | `snyk code test` | No critical issues |
| 5. Review | backend-review | Review code | No critical issues |
| 6. Test | backend-test | `pytest -v` | All pass |

## Verification

After completing all stages:
- [ ] Implementation plan documented
- [ ] Code passes linting
- [ ] No security issues found
- [ ] Code reviewed and approved
- [ ] All tests pass
- [ ] ✅ Ready for commit

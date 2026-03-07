---
name: fullstack-test
description: Production-ready comprehensive testing skill for enterprise fullstack applications
---

# Fullstack Test Skill

This skill guides through comprehensive testing of production fullstack applications, ensuring seamless integration between backend and frontend layers with enterprise-grade quality assurance.

## When to Use
- Writing comprehensive tests for fullstack features and systems
- Running integrated test suites across both backend and frontend layers
- Testing frontend-backend integration and API contracts
- Implementing end-to-end testing for critical user journeys
- Validating performance and accessibility across the full stack
- Debugging complex integration test failures
- Ensuring production readiness of fullstack applications

## Production Test Framework Stack

### Backend Testing Stack
- **Framework**: pytest with comprehensive plugins
- **Database Testing**: pytest-postgresql, testcontainers
- **API Testing**: pytest-flask, requests-mock
- **Performance Testing**: pytest-benchmark, locust
- **Security Testing**: bandit, safety
- **Coverage**: pytest-cov with >80% requirements

### Frontend Testing Stack
- **Framework**: Jest with React Testing Library
- **E2E Testing**: Playwright or Cypress
- **Accessibility Testing**: axe-core integration
- **Performance Testing**: Lighthouse CI, WebPageTest
- **Visual Testing**: Chromatic or Percy
- **Mocking**: MSW (Mock Service Worker)

### Integration Testing Stack
- **Full Stack**: Testcontainers for database and services
- **API Contract**: Dredd or OpenAPI validation
- **Performance**: K6 or Artillery for load testing
- **Monitoring**: Custom test metrics and dashboards

## Production Test Architecture

### Test Structure
```
tests/
├── backend/                 # Backend-specific tests
│   ├── unit/                # Unit tests
│   ├── integration/         # API and database tests
│   ├── performance/         # Load and stress tests
│   └── security/           # Security vulnerability tests
├── frontend/               # Frontend-specific tests
│   ├── unit/               # Component and hook tests
│   ├── integration/        # Component interaction tests
│   ├── e2e/               # End-to-end user journey tests
│   ├── accessibility/     # WCAG compliance tests
│   ├── performance/       # Core Web Vitals tests
│   └── visual/            # Visual regression tests
├── integration/            # Fullstack integration tests
│   ├── api-contract/      # API contract validation
│   ├── user-journeys/     # End-to-end workflows
│   ├── data-flow/         # Data synchronization tests
│   ├── performance/       # Integrated performance tests
│   └── security/          # Full stack security tests
├── fixtures/              # Test data and fixtures
├── mocks/                 # Mock services and data
└── utils/                 # Test utilities and helpers
```

## Production Testing Process

### Step 1: Backend Testing
Use `backend-test` skill for comprehensive backend testing:
```bash
cd contact-form-app/backend

# Unit and integration tests with coverage
pytest tests/ -v --cov=app --cov-report=html --cov-fail-under=80

# Performance and load testing
pytest tests/performance/ -v
locust -f tests/locustfile.py --host=http://localhost:5000

# Security vulnerability scanning
bandit -r app/
safety check
```

### Step 2: Frontend Testing
Use `frontend-test` skill for comprehensive frontend testing:
```bash
cd contact-form-app/frontend

# Unit and integration tests with coverage
npm test -- --watchAll=false --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80,"statements":80}}'

# E2E testing
npm run test:e2e

# Accessibility testing
npm run test:a11y

# Performance testing
npm run test:performance

# Visual regression testing
npm run test:visual
```

### Step 3: Integration Testing

#### API Contract Testing
```bash
# Start backend server
cd contact-form-app/backend
source venv/bin/activate
python run.py &

# Run API contract tests
cd ../
npm run test:api-contract

# Validate OpenAPI specification
dredd ./api/swagger.yaml http://localhost:5000/api
```

#### Full Stack Integration Testing
```bash
# Start both services
docker-compose -f docker-compose.test.yml up -d

# Run integration tests
npm run test:integration

# Run end-to-end user journey tests
npm run test:e2e:fullstack

# Performance testing of integrated system
k6 run tests/performance/load-test.js
```

#### Data Flow Testing
```typescript
// tests/integration/data-flow/user-registration.test.ts
import { test, expect } from '@playwright/test';
import { UserFactory } from '../fixtures/user-factory';

test.describe('User Registration Data Flow', () => {
  test('complete user registration workflow', async ({ page }) => {
    const userData = UserFactory.createValid();
    
    // Navigate to registration
    await page.goto('/register');
    
    // Fill registration form
    await page.fill('[data-testid="email-input"]', userData.email);
    await page.fill('[data-testid="password-input"]', userData.password);
    await page.fill('[data-testid="name-input"]', userData.name);
    
    // Submit form
    await page.click('[data-testid="register-button"]');
    
    // Verify success
    await expect(page.locator('[data-testid="success-message"]')).toBeVisible();
    await expect(page.locator('text=Registration successful')).toBeVisible();
    
    // Verify user exists in backend
    const response = await fetch(`http://localhost:5000/api/users/${userData.email}`);
    const user = await response.json();
    expect(user.email).toBe(userData.email);
    expect(user.name).toBe(userData.name);
  });
  
  test('handles duplicate user registration', async ({ page }) => {
    const userData = UserFactory.createExisting();
    
    // Attempt duplicate registration
    await page.goto('/register');
    await page.fill('[data-testid="email-input"]', userData.email);
    await page.fill('[data-testid="password-input"]', userData.password);
    await page.fill('[data-testid="name-input"]', userData.name);
    await page.click('[data-testid="register-button"]');
    
    // Verify error handling
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
    await expect(page.locator('text=User already exists')).toBeVisible();
  });
});
```

### Step 4: Performance Testing

#### Backend Performance Testing
```python
# tests/performance/api-load-test.py
import pytest
import requests
import time
from concurrent.futures import ThreadPoolExecutor

class TestAPIPerformance:
    def test_api_response_time(self):
        """Test API response times under load"""
        url = "http://localhost:5000/api/contacts"
        
        def make_request():
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            return end_time - start_time, response.status_code
        
        # Run concurrent requests
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(100)]
            results = [future.result() for future in futures]
        
        # Validate performance
        response_times = [result[0] for result in results]
        status_codes = [result[1] for result in results]
        
        assert all(code == 200 for code in status_codes)
        assert sum(response_times) / len(response_times) < 0.5  # < 500ms average
        assert max(response_times) < 2.0  # < 2s max response time
```

#### Frontend Performance Testing
```javascript
// tests/performance/core-web-vitals.test.ts
import { test, expect } from '@playwright/test';

test.describe('Core Web Vitals', () => {
  test('meets LCP requirements', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    // Measure Largest Contentful Paint
    const lcp = await page.evaluate(() => {
      return new Promise((resolve) => {
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const lastEntry = entries[entries.length - 1];
          resolve(lastEntry.startTime);
        }).observe({ entryTypes: ['largest-contentful-paint'] });
      });
    });
    
    expect(lcp).toBeLessThan(2500); // < 2.5s
  });
  
  test('meets FID requirements', async ({ page }) => {
    await page.goto('/');
    
    // Measure First Input Delay
    const fid = await page.evaluate(() => {
      return new Promise((resolve) => {
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          const firstEntry = entries[0];
          resolve(firstEntry.processingStart - firstEntry.startTime);
        }).observe({ entryTypes: ['first-input'] });
      });
      
      // Trigger user interaction
      document.body.click();
    });
    
    expect(fid).toBeLessThan(100); // < 100ms
  });
});
```

### Step 5: Security Testing

#### Full Stack Security Testing
```typescript
// tests/integration/security/auth-flow.test.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication Security', () => {
  test('prevents SQL injection in login', async ({ page }) => {
    await page.goto('/login');
    
    // Attempt SQL injection
    await page.fill('[data-testid="email-input"]', "'; DROP TABLE users; --");
    await page.fill('[data-testid="password-input"]', "password");
    await page.click('[data-testid="login-button"]');
    
    // Should show error, not crash
    await expect(page.locator('[data-testid="error-message"]')).toBeVisible();
    await expect(page.locator('text=Invalid credentials')).toBeVisible();
    
    // Verify database integrity
    const response = await fetch('http://localhost:5000/api/health');
    expect(response.status).toBe(200);
  });
  
  test('prevents XSS in user input', async ({ page }) => {
    await page.goto('/contact');
    
    // Attempt XSS
    const xssPayload = '<script>alert("XSS")</script>';
    await page.fill('[data-testid="message-input"]', xssPayload);
    await page.click('[data-testid="submit-button"]');
    
    // Verify XSS is escaped
    const content = await page.content();
    expect(content).not.toContain('<script>alert("XSS")</script>');
    expect(content).toContain('&lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;');
  });
});
```

## Production Test Execution

### Comprehensive Test Suite
```bash
# Run all tests with comprehensive reporting
npm run test:fullstack

# Individual test categories
npm run test:backend
npm run test:frontend
npm run test:integration
npm run test:performance
npm run test:security
npm run test:accessibility
```

### CI/CD Integration
```bash
# Parallel test execution
npm run test:parallel

# Generate comprehensive reports
npm run test:reports

# Performance benchmarks
npm run test:benchmark

# Security scanning
npm run test:security-scan
```

## Production Test Data Management

### Factory Pattern for Full Stack Testing
```typescript
// tests/fixtures/fullstack-factory.ts
import { faker } from '@faker-js/faker';
import { UserFactory } from './user-factory';
import { ContactFactory } from './contact-factory';

export class FullstackFactory {
  static createUserWithContacts() {
    const user = UserFactory.create();
    const contacts = ContactFactory.createBatch(5, { userId: user.id });
    
    return {
      user,
      contacts,
      apiResponse: {
        user: { ...user, password: undefined },
        contacts
      }
    };
  }
  
  static createComplexWorkflow() {
    return {
      user: UserFactory.createAdmin(),
      contacts: ContactFactory.createBatch(10),
      apiEndpoints: [
        '/api/auth/login',
        '/api/contacts',
        '/api/contacts/:id',
        '/api/users/profile'
      ]
    };
  }
}
```

## Production Test Checklist

### Backend Testing Requirements
- [ ] Unit tests for all business logic (>80% coverage)
- [ ] Integration tests for API endpoints and database operations
- [ ] Performance tests for API response times and load handling
- [ ] Security tests for authentication, authorization, and vulnerability prevention
- [ ] Database tests for migrations, constraints, and data integrity
- [ ] Error handling and edge case testing

### Frontend Testing Requirements
- [ ] Unit tests for all components and hooks (>80% coverage)
- [ ] Integration tests for component interactions and state management
- [ ] E2E tests for critical user journeys and workflows
- [ ] Accessibility tests with axe-core integration (WCAG 2.1 AA)
- [ ] Performance tests for Core Web Vitals and bundle optimization
- [ ] Visual regression tests for UI consistency

### Integration Testing Requirements
- [ ] API contract validation between frontend and backend
- [ ] Full user journey testing from UI to database
- [ ] Data flow and state synchronization testing
- [ ] Error propagation and recovery testing
- [ ] Authentication and authorization flow testing
- [ ] Performance testing of integrated system

### Quality Gates
- [ ] All unit tests pass with >80% coverage
- [ ] All integration tests pass
- [ ] All E2E tests pass
- [ ] Performance benchmarks met (API < 500ms, Core Web Vitals)
- [ ] Accessibility compliance verified (WCAG 2.1 AA)
- [ ] Security scans pass (no critical vulnerabilities)
- [ ] Visual regression tests pass

## How to Invoke

```
Run comprehensive fullstack tests using the fullstack-test skill
Test fullstack integration for [feature] using the fullstack-test skill
Validate API contracts and data flow using the fullstack-test skill
Perform fullstack performance testing using the fullstack-test skill
Execute fullstack security validation using the fullstack-test skill
```

## Related Skills

- **Backend Testing**: Use `backend-test` skill for detailed backend testing
- **Frontend Testing**: Use `frontend-test` skill for detailed frontend testing
- **Backend Implementation**: Use `backend-code` skill for production backend development
- **Frontend Implementation**: Use `frontend-code` skill for production frontend development
- **Analysis**: Use `fullstack-analysis-plan` skill for comprehensive testing strategy
- **Review**: Use `backend-review` and `frontend-review` skills for production readiness assessment

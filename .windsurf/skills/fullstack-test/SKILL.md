---
name: Fullstack Test
description: Testing skill for fullstack applications (backend + frontend)
---

# Fullstack Test Skill

This skill guides through testing fullstack applications including backend API tests, frontend component tests, and integration tests.

## When to Use
- Writing tests for fullstack features
- Running tests across both layers
- Testing frontend-backend integration
- Debugging test failures

## Test Categories

### 1. Backend Tests
- Unit tests for API endpoints
- Validation tests
- Error handling tests

### 2. Frontend Tests
- Component rendering tests
- User interaction tests
- Form validation tests

### 3. Integration Tests
- Frontend-backend communication
- API response handling
- Error flow testing

## Running Tests

### Backend Tests
```bash
cd contact-form-app/backend
source venv/bin/activate

# Run all tests
pytest -v

# Run with coverage
pytest --cov=. --cov-report=term-missing
```

### Frontend Tests
```bash
cd contact-form-app/frontend

# Run all tests
npm test -- --watchAll=false

# Run with coverage
npm test -- --coverage --watchAll=false
```

### Run Both Together
```bash
# Backend
cd contact-form-app/backend && source venv/bin/activate && pytest -v

# Frontend
cd contact-form-app/frontend && npm test -- --watchAll=false
```

## Test Patterns

### Backend API Test
```python
def test_create_contact_success(client):
    """Test POST /api/contacts with valid data."""
    response = client.post('/api/contacts', json={
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'Hello world'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['contact']['name'] == 'John Doe'
```

### Frontend Component Test
```typescript
it('renders contact form', () => {
  render(<ContactForm />);
  expect(screen.getByLabelText(/name/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
});
```

### Integration Test (Manual)
```bash
# 1. Start backend
cd contact-form-app/backend && source venv/bin/activate && python app.py &

# 2. Start frontend
cd contact-form-app/frontend && npm start

# 3. Test in browser or with Cypress
```

## Test Checklist

### Backend
- [ ] Unit tests for new endpoints
- [ ] Validation tests
- [ ] Error handling tests
- [ ] Edge cases covered

### Frontend
- [ ] Component tests
- [ ] User interaction tests
- [ ] Form validation tests
- [ ] Edge cases covered

### Integration
- [ ] API integration working
- [ ] Error responses handled
- [ ] Loading states handled

## Common Issues

### Backend
- Database not initialized for tests
- Missing test fixtures
- Async test issues

### Frontend
- Mock API calls
- Async state updates
- Component not rendering

### Integration
- CORS issues
- API not running
- Port conflicts

## Related Skills

- backend-test - For detailed backend testing
- frontend-test - For detailed frontend testing

## How to Invoke

```
Run fullstack tests using the fullstack-test skill
Test the [feature] using the fullstack-test skill
```

import pytest
import json
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_check_email_not_exists(client):
    """Test email check for non-existent email."""
    response = client.get(
        '/api/contacts/check-email?email=nonexistent@example.com')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['exists'] is False
    assert data['data']['email'] == 'nonexistent@example.com'


def test_check_email_exists(client):
    """Test email check for existing email."""
    # First, create a contact
    response = client.post('/api/contacts', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'message': 'Test message'
    })
    assert response.status_code == 201

    # Then check if email exists
    response = client.get('/api/contacts/check-email?email=test@example.com')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['exists'] is True
    assert data['data']['email'] == 'test@example.com'


def test_check_email_case_insensitive(client):
    """Test email check is case insensitive."""
    # First, create a contact
    response = client.post('/api/contacts', json={
        'name': 'Test User',
        'email': 'case_test@example.com',
        'message': 'Test message'
    })
    assert response.status_code == 201

    # Then check with different case
    response = client.get(
        '/api/contacts/check-email?email=CASE_TEST@EXAMPLE.COM')
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
    assert data['data']['exists'] is True


def test_check_email_invalid_format(client):
    """Test email check with invalid format."""
    response = client.get('/api/contacts/check-email?email=invalid-email')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False
    assert 'Invalid email format' in data['error']


def test_check_email_missing_parameter(client):
    """Test email check without email parameter."""
    response = client.get('/api/contacts/check-email')
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] is False
    assert 'Email parameter is required' in data['error']


def test_submit_duplicate_email(client):
    """Test that duplicate emails are rejected during submission."""
    # First, create a contact
    response = client.post('/api/contacts', json={
        'name': 'Test User',
        'email': 'duplicate@example.com',
        'message': 'Test message'
    })
    assert response.status_code == 201

    # Try to create another contact with same email
    response = client.post('/api/contacts', json={
        'name': 'Another User',
        'email': 'duplicate@example.com',
        'message': 'Another message'
    })
    assert response.status_code == 409
    data = json.loads(response.data)
    assert data['success'] is False
    assert 'already exists' in data['error']


def test_submit_duplicate_email_case_insensitive(client):
    """Test that duplicate emails are rejected regardless of case."""
    # First, create a contact
    response = client.post('/api/contacts', json={
        'name': 'Test User',
        'email': 'case@example.com',
        'message': 'Test message'
    })
    assert response.status_code == 201

    # Try to create another contact with different case
    response = client.post('/api/contacts', json={
        'name': 'Another User',
        'email': 'CASE@EXAMPLE.COM',
        'message': 'Another message'
    })
    assert response.status_code == 409
    data = json.loads(response.data)
    assert data['success'] is False
    assert 'already exists' in data['error']

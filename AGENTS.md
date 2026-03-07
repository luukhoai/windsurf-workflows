# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Windsurf Development Framework** - a comprehensive guide demonstrating production-ready enterprise development using Windsurf's AI-powered workflows, skills, and rules. The project contains a functional contact form application that showcases the framework in practice with enterprise-grade architecture, security, performance, and accessibility standards.

## Framework Structure

```
./
├── .windsurf/                    # Windsurf framework configuration
│   ├── rules/                    # Development standards and guidelines
│   │   ├── backend-development.md    # Comprehensive backend architecture standards
│   │   └── frontend-development.md   # Production frontend architecture standards
│   ├── skills/                   # AI-powered development skills
│   │   ├── backend/               # Backend development skills
│   │   │   ├── analysis-plan.md   # Requirements analysis and planning
│   │   │   ├── code.md           # Implementation with quality checks
│   │   │   ├── test.md            # Comprehensive testing strategy
│   │   │   └── review.md         # Production readiness review
│   │   ├── frontend/              # Frontend development skills
│   │   │   ├── analysis-plan.md  # Frontend architecture planning
│   │   │   ├── code.md           # Production component development
│   │   │   ├── test.md            # Accessibility and performance testing
│   │   │   └── review.md         # Frontend quality review
│   │   └── fullstack/             # Fullstack development skills
│   │       ├── analysis-plan.md  # Comprehensive fullstack architecture planning
│   │       ├── test.md            # Fullstack integration testing
│   └── workflows/                # CI-style development pipelines
│       ├── backend-code-test-review.md    # Backend development pipeline
│       ├── frontend-code-test-review.md   # Frontend development pipeline
│       └── fullstack-code-test-review.md  # Fullstack development pipeline
├── contact-form-app/            # Sample application demonstrating framework usage
│   ├── backend/                 # Python Flask backend with enterprise patterns
│   └── frontend/                # React TypeScript frontend with production standards
└── README.md                     # Comprehensive framework guide
```

## Sample Application Structure

### Frontend (Production-Ready React TypeScript)
```
contact-form-app/frontend/
├── src/
│   ├── components/       # Atomic Design components (Atoms, Molecules, Organisms)
│   ├── pages/           # Page components (Templates, Pages)
│   ├── hooks/           # Custom hooks for reusable logic
│   ├── utils/           # Utility functions and helpers
│   ├── types/           # TypeScript type definitions
│   ├── styles/          # CSS modules and design tokens
│   ├── App.tsx          # Main app component
│   └── index.tsx        # Entry point
├── package.json
├── tsconfig.json
└── jest.config.js       # Testing configuration
```

### Backend (Enterprise Flask Python)
```
contact-form-app/backend/
├── app/
│   ├── __init__.py          # Flask app factory (create_app)
│   ├── config.py            # Configuration (Dev/Testing/Prod)
│   ├── models/
│   │   ├── __init__.py      # Contact model
│   │   └── base.py         # Base model with common patterns
│   ├── repositories/        # Data access layer (Repository pattern)
│   │   ├── __init__.py
│   │   └── contact_repository.py
│   ├── services/            # Business logic layer
│   │   ├── __init__.py
│   │   └── contact_service.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── contacts.py       # Contact API routes
│   └── utils/
│       ├── __init__.py
│       ├── validators.py     # Validation functions
│       └── helpers.py        # File handling helpers
├── tests/
│   ├── __init__.py
│   ├── test_contacts.py     # Unit tests
│   ├── test_integration.py  # Integration tests
│   └── conftest.py         # Test configuration
├── run.py                   # Entry point
├── requirements.txt
└── uploads/                 # File uploads directory
```

## Common Commands

### Frontend (Production-Ready React + TypeScript)
```bash
cd contact-form-app/frontend
npm install          # Install dependencies
npm start            # Start dev server on localhost:3000
npm test             # Run tests (Jest with React Testing Library)
npm run test:e2e     # Run E2E tests (Playwright)
npm run test:a11y    # Run accessibility tests (axe-core)
npm run test:performance # Run performance tests (Lighthouse)
npm run build        # Production build with optimization
npm run lint         # Lint with ESLint
npm run type-check   # TypeScript strict type checking
npm run format       # Format with Prettier
npm run analyze      # Bundle size analysis
```

### Backend (Enterprise Flask + Python)
```bash
cd contact-form-app/backend
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
pip install -r requirements.txt
python run.py              # Start server on localhost:5000

# Quality checks
flake8 app/ tests/         # Linting
black app/ tests/          # Formatting
snyk code test --severity-threshold=medium  # Security scan
pytest tests/ -v --cov=app --cov-fail-under=80  # Testing with coverage
```

### Fullstack Development
```bash
# Use Windsurf workflows for complete development cycles
/backend-code-test-review implement [feature]
/frontend-code-test-review create [component]
/fullstack-code-test-review develop [fullstack feature]

# Use specific skills for targeted development
/backend-analysis-plan plan [architecture]
/frontend-code implement [component]
/fullstack-test validate [integration]
```

## Production Architecture

The application follows enterprise-grade architecture patterns:

### Frontend Architecture
- **Atomic Design**: Atoms → Molecules → Organisms → Templates → Pages
- **TypeScript**: Strict typing with comprehensive interfaces and generics
- **State Management**: Local state (useState), global state (Context), server state (React Query)
- **Performance**: Code splitting, memoization, Core Web Vitals optimization
- **Accessibility**: WCAG 2.1 AA compliance, semantic HTML, ARIA implementation
- **Security**: XSS prevention, CSP headers, input validation

### Backend Architecture
- **OOP/SOLID**: Enterprise patterns with proper separation of concerns
- **Repository Pattern**: Abstract data access with testable implementations
- **Service Layer**: Business logic with dependency injection
- **API Design**: RESTful conventions with proper HTTP methods and status codes
- **Security**: SQL injection prevention, authentication, data validation
- **Testing**: >80% coverage with unit, integration, and performance tests

### Integration Architecture
- **API Contracts**: Comprehensive endpoint specifications with validation
- **Data Flow**: Seamless integration between frontend and backend
- **Error Handling**: Consistent error propagation and user-friendly messages
- **Performance**: Optimized API responses and frontend rendering

## Key Endpoints
- `POST /api/contacts` - Submit a contact form with validation
- `GET /api/contacts` - Retrieve all contacts with pagination
- `GET /api/contacts/:id` - Retrieve specific contact
- `PUT /api/contacts/:id` - Update contact information
- `DELETE /api/contacts/:id` - Delete contact

## Development Guidelines

### Production Standards
- **Backend**: Follow comprehensive OOP/SOLID principles (see `.windsurf/rules/backend-development.md`)
- **Frontend**: Implement Atomic Design with accessibility (see `.windsurf/rules/frontend-development.md`)
- **Fullstack**: Use integrated development workflows (see `.windsurf/workflows/`)
- **Quality**: Pass all quality gates (code, architecture, security, performance, tests)

### Code Quality Pipeline
- **Analysis**: Use `*-analysis-plan` skills for comprehensive planning
- **Implementation**: Use `*-code` skills with quality checks
- **Testing**: Use `*-test` skills for comprehensive validation
- **Review**: Use `*-review` skills for production readiness assessment

### Development Tools
#### Backend
- **Linting**: `flake8 app/ tests/`
- **Security**: `snyk code test --severity-threshold=medium`
- **Testing**: `pytest tests/ -v --cov=app --cov-fail-under=80`
- **Formatting**: `black app/ tests/`
- **Type Checking**: `python -m mypy app/`

#### Frontend
- **Linting**: `npm run lint`
- **Type Checking**: `npm run type-check`
- **Testing**: `npm test -- --coverage --coverageThreshold='{"global":{"branches":80,"functions":80,"lines":80,"statements":80}}'`
- **Accessibility**: `npm run test:a11y`
- **Performance**: `npm run test:performance`
- **Formatting**: `npm run format`

## Framework Usage

This project demonstrates how to effectively use Windsurf's AI-powered development framework:

1. **Workflows**: CI-style pipelines for complete development cycles
2. **Skills**: AI-powered capabilities for analysis, implementation, testing, and review
3. **Rules**: Comprehensive development standards ensuring enterprise quality

For detailed guidance, see the README.md and explore the `.windsurf/` directory to understand the complete framework architecture and usage patterns.

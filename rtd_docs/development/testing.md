# Testing strategy

Tests should provide fast feedback during development and confidence at integration boundaries. Organize tests inside the Django application they cover.

## Suggested structure

```text
apps/
└── example/
    └── tests/
        ├── unit_test/
        ├── integration_test/
        └── e2e_test/
```

Use the naming and directory conventions established by the generated project. Keep test ownership close to the code under test.

## Test scopes

- **Unit tests:** verify focused behavior in isolation, with external dependencies replaced where appropriate.
- **Integration tests:** verify interactions between application components, the database, caches, queues, or other infrastructure.
- **End-to-end tests:** exercise complete user-facing workflows across system boundaries.

API tests should cover successful requests and relevant failure cases, including validation, authentication, permissions, and error responses.

## Running tests

From the generated project root, run:

```bash
pytest
```

The exact test settings and dependencies depend on the options selected during project generation.

## Quality guidelines

1. Test observable behavior rather than implementation details.
2. Cover both expected success paths and meaningful failure paths.
3. Keep fixtures and factories reusable but avoid hidden global state.
4. Make tests deterministic and independent of execution order.
5. Add regression coverage for fixed defects.
6. Run the relevant test suite before opening a pull request.

For API design and permission-related checks, see [DRF best practices](drf-best-practices.md).

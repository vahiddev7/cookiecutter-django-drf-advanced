# Django REST Framework best practices

This guide describes practical review points for APIs built with the optional Django REST Framework integration.

## Serializers

- Validate untrusted input at the API boundary.
- Keep serializer validation focused on input and representation rules.
- Avoid placing complex multi-model workflows in serializer methods.
- Return clear validation errors without exposing internal implementation details.

## Views and services

- Keep views responsible for HTTP concerns, permissions, and orchestration.
- Move multi-step business workflows into services when that improves cohesion or testability.
- Use transactions when multiple database writes must succeed or fail together.
- Avoid adding abstraction layers for trivial operations.

## Querysets and selectors

- Filter data at the database layer.
- Use `select_related` and `prefetch_related` where they prevent avoidable query growth.
- Apply pagination to collection endpoints.
- Keep reusable or complex read queries in selectors when that makes ownership clearer.

## Authentication and permissions

- Define authentication and permission behavior explicitly.
- Apply least-privilege access by default.
- Test unauthenticated, authenticated, forbidden, and cross-tenant access cases where applicable.
- Do not rely on frontend restrictions to protect API resources.

## API tests

Cover:

- Valid requests and expected response schemas.
- Invalid payloads and serializer validation.
- Authentication and permission failures.
- Object-level access and tenant isolation.
- Not-found and conflict cases.
- Query behavior for endpoints returning collections.

Avoid asserting private implementation details unless they are part of a deliberate contract.

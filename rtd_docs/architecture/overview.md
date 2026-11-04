# Architecture overview

The template aims to provide a clear separation between HTTP handling, application behavior, and data access without forcing every Django app to contain every possible layer.

## Request flow

A typical write request can follow this flow:

```text
HTTP Request
    |
    v
View / API View
    |
    v
Serializer validation
    |
    v
Service (when useful)
    |
    v
Model / ORM
    |
    v
Database
```

A read request may use a selector for a reusable or sufficiently complex query:

```text
HTTP Request
    |
    v
View / API View
    |
    v
Selector (when useful)
    |
    v
ORM
    |
    v
Database
```

## Responsibilities

- **Views:** handle HTTP concerns and coordinate request/response behavior.
- **Serializers:** validate and represent API data when DRF is enabled.
- **Services:** encapsulate application operations and business workflows when separation improves clarity or testability.
- **Selectors:** keep reusable or complex read queries out of views.
- **Models:** represent persisted data and Django ORM behavior.
- **Tests:** verify behavior at unit, integration, API, and end-to-end levels as appropriate.

Services and selectors are conventions, not mandatory layers. Keep simple behavior simple. Avoid creating empty modules solely to satisfy a folder convention.

## Application boundaries

Keep code close to the Django application that owns the behavior. Prefer explicit interfaces and clear ownership over broad shared modules that become difficult to change safely.

## Test organization

Tests belong inside the application they cover and are grouped by scope. See the [testing strategy](../development/testing.md) for examples and guidance.

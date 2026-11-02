# Security Policy

## Reporting a vulnerability

Please do not report exploitable security vulnerabilities in public issues or pull requests.

Use GitHub's private vulnerability reporting feature for this repository, if enabled. If private reporting is unavailable, contact the repository maintainer through the contact information published on the maintainer's GitHub profile and include only the minimum information needed to understand the issue.

Please do not attach production credentials, personal data, or live secrets. Use a safe, reproducible example.

## Scope

This repository is a project generator. A vulnerability may affect the template itself, generated configuration, dependency selection, Docker setup, documentation, or CI/release automation.

When reporting an issue, include:
- The affected release tag or commit.
- The relevant Cookiecutter answers (with secrets removed).
- The expected and observed behavior.
- A minimal reproduction, where practical.

## Generated-project security

Generated projects are starting points, not complete security certifications. Before deployment, review secret management, allowed hosts, HTTPS, database permissions, storage access, task dashboard exposure, dependency updates, logging of sensitive data, and environment-specific settings.

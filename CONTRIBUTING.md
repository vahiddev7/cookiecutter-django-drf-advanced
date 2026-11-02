# Contributing

Thank you for helping improve Django DRF Advanced Cookiecutter.

## Before opening an issue

- Search existing issues and pull requests.
- Include the template revision or release tag you used.
- For generated-project bugs, include the Cookiecutter answers, Python version, operating system, and relevant sanitized error output.
- Never include credentials, access tokens, private keys, or a real `.env` file.

## Development workflow

1. Fork the repository and create a focused branch from `master`.
2. Make the smallest change that addresses the problem.
3. Update the README or documentation when behavior, options, defaults, or operational requirements change.
4. Add or update CI coverage for each affected Cookiecutter option combination.
5. Generate at least one minimal project and one project with the changed optional feature enabled.
6. Run the applicable checks before opening a pull request.

Useful local checks:

```bash
python -m pip install --upgrade cookiecutter
cookiecutter --no-input . --output-dir /tmp/generated \
  project_name="CI Test Project" project_slug=ci_test_project author_name=CI \
  use_drf=y use_swagger=n use_docker=n database_engine=sqlite \
  use_celery=n celery_broker=redis use_sentry=n cloud_storage=none
```

For Docker-enabled configurations, validate the generated Compose file from the generated project directory:

```bash
docker compose config --quiet
```

## Pull request expectations

- Explain the problem, the chosen approach, and any trade-offs.
- List the Cookiecutter configurations tested.
- Link related issues.
- Keep unrelated refactors out of feature changes.
- Do not commit generated secrets, local databases, build output, or personal environment files.
- Do not claim checks passed unless they were run successfully.

CI is the source of truth for supported generated-project combinations. A green check on one configuration does not imply every optional combination was tested.

## Commit and release conventions

Use clear, imperative commit messages. Prefer Conventional Commit-style prefixes such as `feat:`, `fix:`, `docs:`, `test:`, `ci:`, and `chore:`.

Releases use semantic version tags in the form `vMAJOR.MINOR.PATCH`. See the [release guide](docs/releasing.html) for the release process.

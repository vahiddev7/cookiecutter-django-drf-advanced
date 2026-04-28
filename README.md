# 🚀 Django Clean Architecture Cookiecutter

A production-ready Django project template following a clean, scalable, and maintainable architecture using **Services**, **Selectors**, and modular apps.

---

## ✨ Features

* 🧱 Clean Architecture (Service & Selector pattern)
* 🔌 Modular Django apps structure
* 🔐 Ready-to-use authentication system
* 📦 Docker support (development & production)
* ⚙️ Environment-based settings (dev/prod)
* 🧪 Structured test setup (API, services, selectors)
* 🔄 API versioning (`/api/v1/`)
* 🧰 Pre-configured project layout for scalability

---

## 🧠 Architecture Overview

This template follows an opinionated architecture:

### 🔹 Services

Handle business logic and write operations.

### 🔹 Selectors

Handle read-only queries from the database.

### 🔹 Serializers

Validate and transform data.

### 🔹 Views (API)

Thin layer that connects HTTP requests to services/selectors.

---

### 📌 Why this approach?

* Keeps views clean and simple
* Makes business logic reusable
* Improves testability
* Scales well for large projects

---

## 📁 Project Structure

```
apps/
  users/
    models/
    services/
    selectors/
    serializers/
    views/
    tests/
```

Each app is self-contained and follows the same structure.

---

## ⚡ Quick Start

### 1. Install Cookiecutter

```bash
pip install cookiecutter
```

### 2. Generate the project

```bash
cookiecutter https://github.com/your-username/your-repo
```

### 3. Run with Docker

```bash
docker-compose up --build
```

---

## ⚙️ Configuration Options

During setup, you will be prompted for:

* `project_name`
* `project_slug`
* `use_docker`
* `use_postgres`
* `use_celery`

---

## 🛠 Development

### Run migrations

```bash
python manage.py migrate
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Run server

```bash
python manage.py runserver
```

---

## 🧪 Testing

```bash
pytest
```

Tests are organized by:

* API
* Services
* Selectors

---

## 🧩 Creating a New App

Use the provided script:

```bash
./scripts/start_app.sh blog
```

This will generate a fully structured app with:

* services
* selectors
* serializers
* tests
* API views

---

## 🔐 Authentication

Includes basic authentication system:

* Register
* Login
* Token-based authentication (extendable)

---

## 🌍 Environment Settings

Settings are split into:

```
settings/
  base.py
  dev.py
  prod.py
```

---

## 🐳 Docker Support

Includes:

* Development setup
* Production-ready Dockerfile
* Nginx configuration

---

## 📌 When should you use this template?

✅ Large-scale Django projects
✅ Teams working on backend APIs
✅ Projects needing clean and testable architecture

---

## ⚠️ When NOT to use it

❌ Small/simple projects
❌ Prototypes or quick MVPs

---

## 💡 Philosophy

This template is **opinionated**.

It prioritizes:

* scalability
* maintainability
* separation of concerns

over simplicity.

---

## 🤝 Contributing

Contributions, issues, and suggestions are welcome!

---

## 📄 License

MIT License

---

## ⭐ Support

If you find this useful, consider giving it a star ⭐ on GitHub!

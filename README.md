# Django My Web 🌐

A modern Django web application featuring a portfolio and personal website with clean architecture and responsive design.

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Modern Django Framework**: Built with Django's latest best practices
- **Portfolio Pages**: Showcase your work and projects
- **Responsive Design**: Mobile-friendly interface
- **Clean Architecture**: Well-organized code structure with proper separation of concerns
- **Template System**: Reusable templates with inheritance
- **Static File Management**: Optimized handling of CSS, JavaScript, and media files

## 📁 Project Structure

```
Django-My-Web/
├── maxweb/                 # Main project directory
│   ├── manage.py          # Django management script
│   ├── db.sqlite3         # SQLite database
│   ├── maxweb/            # Project configuration
│   │   ├── __init__.py
│   │   ├── settings.py    # Django settings
│   │   ├── urls.py        # Main URL configuration
│   │   ├── wsgi.py        # WSGI configuration
│   │   └── asgi.py        # ASGI configuration
│   └── pages/             # Pages application
│       ├── models.py      # Data models
│       ├── views.py       # View controllers
│       ├── urls.py        # URL patterns
│       ├── admin.py       # Admin configuration
│       ├── apps.py        # App configuration
│       ├── tests.py       # Unit tests
│       ├── migrations/    # Database migrations
│       └── templates/     # HTML templates
│           └── pages/
│               ├── base.html      # Base template
│               ├── home.html      # Homepage
│               ├── about.html     # About page
│               └── portfolio.html # Portfolio page
└── README.md              # Project documentation
```

## 🔧 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://python.org/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MaximKoblyuk/Django-My-Web.git
cd Django-My-Web
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
# Or if you have a requirements.txt:
# pip install -r requirements.txt
```

### 4. Navigate to Project Directory

```bash
cd maxweb
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

## 🎯 Usage

### Development Server

Start the development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser to view the application.

### Available Pages

- **Home**: `/` - Landing page
- **About**: `/about/` - About page
- **Portfolio**: `/portfolio/` - Portfolio showcase
- **Admin**: `/admin/` - Django admin interface

## 🛠️ Development

### Running Tests

```bash
python manage.py test
```

### Collecting Static Files

```bash
python manage.py collectstatic
```

### Making Migrations

When you modify models:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Code Style

This project follows Django's coding standards and PEP 8 guidelines.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Best Practices

- Always activate the virtual environment before working on the project
- Keep dependencies updated and documented
- Follow Django's security best practices
- Write tests for new features
- Use meaningful commit messages
- Keep the codebase clean and well-documented

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Maxim Koblyuk** - [GitHub](https://github.com/MaximKoblyuk)

---

⭐ If you found this project helpful, please give it a star!
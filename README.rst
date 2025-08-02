# 🔐 Django Two-Factor Authentication System

A secure, production-ready Django application that integrates two-factor authentication (2FA) using time-based one-time passwords (TOTP), QR code setup, and backup tokens. This project allows users to enhance their login security by requiring a second layer of verification via authenticator apps like Google Authenticator, Authy, or Microsoft Authenticator.

## 🧭 Table of Contents

[Features](#-features)
[Tech Stack](#-tech-stack)
[Screenshots](#-screenshots)
[Demo](#-demo)
[Project Structure](#-project-structure)
[Getting Started](#-getting-started)
[Deployment](#-deployment)
[Contribution](#-contribution)
[License](#-license)
[Acknowledgements](#-acknowledgements)
[Author](#-author)
## 🚀 Features

🔐 Two-factor login (Password + OTP)
📱 Google Authenticator QR setup
🧾 Backup codes for recovery
👩‍💼 Admin & superuser access
🖼️ Custom UI with frontend styling
🚫 Prevent unauthorized access
🧩 Easy to extend into any Django app
## 🛠️ Technologies Used

Python 3.10+
Django 4+
django-otp
HTML5 / CSS3 / Bootstrap
SQLite (or PostgreSQL)
QR Code generation
**Virtualen
> _Upload screenshots of:_ - Login page - OTP QR setup page - Backup code interface - Admin panel

django-two-factor-auth/ structure │ ├── example/ # Fully working Django demo app │ ├── migrations/ # DB migrations │ ├── templates/ # HTML templates │ │ ├── login.html # Custom login form │ │ ├── base.html # Base template │ │ └── setup.html # 2FA QR Setup │ ├── static/ # CSS, JS, logo assets │ ├── settings.py # Django settings for demo app │ ├── urls.py # URL routes for 2FA pages │ └── views.py # App logic (very minimal) │ ├── two_factor/ # Main package (the 2FA logic) │ ├── admin.py # Admin integration │ ├── forms.py # Setup forms for OTP │ ├── gateways/ # Gateways like SMS, Twilio (optional) │ ├── models.py # Models if needed │ ├── templates/ # Override templates │ ├── urls.py # 2FA URL routing │ ├── utils.py # Helper methods │ └── views/core.py # Core logic for OTP/QR │ ├── docs/ # Documentation ├── tests/ # Unit tests ├── .gitignore ├── requirements_dev.txt # Dev dependencies ├── README.md # This file └── LICENSE

## 💻 Local Setup

### 🔧 Prerequisites

Python 3.10+
Git
pip
### 🧪 Installation Steps

```bash # Clone your fork git clone https://github.com/YOUR_USERNAME/django-two-factor-auth.git cd django-two-factor-auth

# Create virtual environment python3 -m venv venv source venv/bin/activate # or venvScriptsactivate on Windows

# Install dependencies pip install -r requirements_dev.txt

# Migrate and run example app cd example python manage.py migrate python manage.py createsuperuser python manage.py runserver

Local-Host - (http://127.0.0.1:8000/)

## 📷 Screenshots {Home.page} - https://github.com/Nicole9-Sky/django-two-factor-auth/blob/master/HOME%20(2).png {Login.page} - https://github.com/Nicole9-Sky/django-two-factor-auth/blob/master/LOGIN.png {Registration} - https://github.com/Nicole9-Sky/django-two-factor-auth/blob/master/REGISTRATION.png

## 🌐 Live Demo

🔗 [View Live Project on Render](https://django-two-factor-auth-1.onrender.com)

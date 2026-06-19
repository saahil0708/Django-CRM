# Django CRM

## About
Django CRM is a Customer Relationship Management system built with Python and the Django web framework. It provides a platform for businesses to manage their interactions with current and potential customers.

## Features
- User Authentication (Registration, Login, Logout)
- Database Integration (MySQL)
- *More features coming soon...*

## Tech Stack
- **Backend:** Python 3.12+, Django 6.0+
- **Database:** MySQL
- **Package Manager:** `uv`

## Requirements

Before starting, make sure you have the following installed on your local machine:
- **Python 3.12** or higher
- **MySQL Server**
- **Git**
- **uv** (Optional, recommended for faster package management)

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd django-crm
   ```

2. **Set up the virtual environment and install dependencies:**
   This project uses `uv` for package management. You can install all dependencies by running:
   ```bash
   uv sync
   ```
   Alternatively, using standard `pip`:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   pip install .
   ```

3. **Configure the Database:**
   - Ensure you have a MySQL server running locally.
   - Create a new MySQL database for the project.
   - Update the `DATABASES` settings in `dcrm/dcrm/settings.py` with your MySQL credentials (Database Name, User, Password, Host, Port).

4. **Apply database migrations:**
   ```bash
   cd dcrm
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and navigate to `http://127.0.0.1:8000/`.

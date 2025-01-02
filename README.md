# Aguacate Spanish Restaurant

**Aguacate Spanish Restaurant** is a Django-based project simulating a restaurant's website. It includes features such as a homepage, menu display, and reservation system.

## Features

- **Homepage**: Welcoming page with navigation links.
- **Menu Page**: Displays a list of menu items with descriptions, prices, and images.
- **Reservation System**: Allows users to book a table by submitting a form.

## Project Structure

```plaintext
spanish_restaurant_project/
├── media/                   # Media files (e.g., images, logo)
├── restaurant/              # Django app with templates, views, models
│   ├── templates/
│   ├── static/              # CSS and JavaScript files
│   ├── views.py             # View functions for the app
│   ├── models.py            # Database models
│   └── urls.py              # URL routing for the app
├── spanish_restaurant_project/
│   ├── settings.py          # Django project settings
│   ├── urls.py              # URL routing for the project
│   └── wsgi.py              # WSGI entry point for deployment
├── db.sqlite3               # SQLite database file
├── manage.py                # Django's management script


Installation
Clone the repository:
   git clone <repository-url>
   cd spanish_restaurant_project
Set up a virtual environment:
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
Apply migrations and start the server:
   python manage.py migrate
   python manage.py runserver
Access the project at http://127.0.0.1:8000/.

# API Test Project Using Django

## Project Overview

This Django project is designed for storing user data.

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/download/)
- [Django REST Framework](https://www.django-rest-framework.org/#installation)
- [Swagger](https://swagger.io/docs/open-source-tools/swagger-ui/usage/installation/)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/piash23/test_task
   cd test_task
   ```


1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
    ```
2. **Activate the Virtual Environment:**

   on Windows:
   ```bash
   venv\Scripts\activate
   ```
   on Linux or Mac:
    ```bash
   source venv/bin/activate
    ```
3. **Install the Requirements:**
   
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the migrations:**

   ```bash
    python manage.py migrate
    ```
5. **Run the Tests:**

   ```bash
    python manage.py test
    ```
6. **Run the Swagger:**

   ```bash
    python manage.py runserver
    ```
   Then go to http://localhost:8000/api/swagger/ to see the swagger documentation.
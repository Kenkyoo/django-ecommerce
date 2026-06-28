# Django E-Commerce Store

A full-stack e-commerce web application built with Django, demonstrating core concepts of backend web development including authentication, session management, and order processing.

🔗 **Live Demo**: [django-ecommerce-au5o.onrender.com](https://django-ecommerce-au5o.onrender.com/store)

---

## Features

- **Product catalog** with category filtering
- **User authentication** — register, login, logout with hashed passwords
- **Session-based shopping cart** — add, remove, and adjust quantities
- **Checkout flow** — place orders with shipping address and phone number
- **Order history** — authenticated users can view their past orders
- **Admin panel** — manage products, categories, customers, and orders via Django admin

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Django 4.2 |
| Database | SQLite (development) |
| Frontend | Bootstrap 5, HTML5 |
| Auth | Django sessions + `django.contrib.auth.hashers` |
| Static files | WhiteNoise |
| Deployment | Render |

---

## Project Structure

```
ecommerce/
├── ecommerce/          # Project config (settings, urls, wsgi)
└── store/
    ├── models/         # Customer, Products, Category, Order
    ├── views/          # Class-based views for each feature
    ├── templates/      # Bootstrap-based HTML templates
    └── urls.py
```

---

## Local Setup

```bash
# Clone the repo
git clone https://github.com/your-username/django-ecommerce.git
cd django-ecommerce/ecommerce

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser for the admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/store`.

---

## Adding Sample Data

Use the Django admin at `/admin` to create:
1. **Categories** (e.g. Electronics, Clothing)
2. **Products** with name, price, image, and category

---

## Notes

- This project uses **SQLite**, which is not persisted between deploys on Render. It is intended as a portfolio/demo project, not for production use with real users.
- Media files (product images) are served locally in development. In production, a persistent storage solution (e.g. AWS S3) would be needed.

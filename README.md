# ink.

A personal blog built with Django. Currently a work in progress — core post management is functional, with email features coming soon.

> ⚠️ **This project is still under active development.** Some features may be incomplete or subject to change.

---

## Features (so far)

- Create, edit, and delete blog posts
- Environment variable support via `.env`
- Email notification system *(in progress)*

---

## Requirements

- Python 3.12+
- Pipenv

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/KaranSaini-Git/ink..git
cd ink.
```

### 2. Install dependencies

```bash
pipenv install
```

### 3. Activate the virtual environment

```bash
pipenv shell
```

### 4. Set up your `.env` file

Create a `.env` file in the root of the project (same folder as `manage.py`):

```bash
touch .env
```

Then open it and add the following:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

To generate a secret key, run this inside your pipenv shell:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and paste it as the value for `SECRET_KEY` in your `.env` file.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
ink/
├── manage.py
├── Pipfile
├── Pipfile.lock
├── .env              ← you create this locally (not pushed to GitHub)
├── .gitignore
└── ...
```

---

## Notes

- The `.env` file is **not included** in this repository for security reasons. You must create it yourself following the instructions above.
- This project uses Django's built-in SQLite database for development. No additional database setup is required.
- Email functionality is currently being implemented and is not yet available.

---

## Contributing

This is a personal project and not currently open to contributions. Feel free to fork it and build your own version!

---

## Author

Made with 🖊️ by Karan Singh Saini. 
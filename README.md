# ink.

A personal Django blog project focused on clean writing, simple publishing, and an editorial-style interface.

## Features

- **Post publishing workflow**
  - Posts support **Draft** and **Published** states.
  - Public views only show published posts via a custom manager.

- **Post detail routing with dated URLs**
  - Each post has a slug and date-based canonical URL generated through `get_absolute_url()`.

- **Blog listing with pagination**
  - Post list is paginated at **3 posts per page**.
  - Handles invalid or out-of-range page values gracefully.

- **Comments system**
  - Visitors can submit comments with name, email, and body.
  - Only active comments are shown on post detail pages.

- **Share by email**
  - Built-in form to email a post recommendation.
  - Uses Django email utilities (`send_mail`) to send the message.

- **Admin experience improvements**
  - Customized `Post` and `Comment` admin panels with:
    - list views
    - filters
    - search fields
    - slug auto-population
    - publish date hierarchy
    - facet counts for filters

- **Custom frontend styling**
  - Handcrafted CSS design system with:
    - responsive layout
    - animated post cards
    - polished typography and spacing
    - dedicated styles for list, detail, share, pagination, and comments sections

## Tech Stack

- **Backend:** Django
- **Language:** Python
- **Database (default):** SQLite
- **Frontend:** HTML + CSS
- **Forms/Email:** Django Forms + Django Mail

## Project Structure

```text
.
├── DjangoFiles/                 # Project configuration (settings, urls, wsgi, asgi)
├── blog/                        # Main blog app
│   ├── migrations/
│   ├── static/blog/blog.css
│   ├── templates/blog/
│   │   ├── base.html
│   │   └── post/
│   │       ├── list.html
│   │       ├── detail.html
│   │       ├── share.html
│   │       ├── comment.html
│   │       └── includes/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── Pipfile
└── Pipfile.lock
```

## Run Locally

1. Install dependencies (Pipenv):
   - `pipenv install`
2. Activate shell:
   - `pipenv shell`
3. Apply migrations:
   - `python manage.py migrate`
4. Start server:
   - `python manage.py runserver`
5. Open:
   - `http://127.0.0.1:8000/blog/`

## Notes

This README reflects features that are currently implemented in the repository codebase on the `main` branch.

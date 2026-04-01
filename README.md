# ink.

A personal Django blog — a space for thoughts, notes, and ideas written down. Built from scratch as a learning project with a focus on clean design and a warm editorial aesthetic.

---

## Features

- **Post management** — create, edit, and delete posts via the Django admin panel with draft/published status workflow
- **Comment system** — readers can leave comments; each comment has an `active` flag for admin moderation
- **Tag filtering** — posts are tagged via `django-taggit`; clicking a tag filters the post list and highlights the active tag in the sidebar
- **Similar posts** — post detail pages show up to 4 related posts ranked by shared tag count
- **Share by email** — share any post via Gmail SMTP using a built-in email form
- **Pagination** — post list paginates at 3 posts per page
- **Dynamic sidebar** — shows all tags from published posts (ordered by newest) and a most-commented posts section
- **Dark mode toggle** — switches between a warm parchment light mode and deep charcoal dark mode, with preference saved via `localStorage`
- **Custom admin** — enhanced admin with facet counts, date hierarchy, slug auto-population, and search/filter for both posts and comments

---

## Tech Stack

| Layer | Tech |
|---|---|
| Backend | Django 6.0.3 |
| Database | SQLite (built-in) |
| Package manager | Pipenv |
| Python version | 3.14 |
| Tags | django-taggit 5.0.1 |
| Config | python-decouple 3.8 |
| SSL | certifi |
| Email | Gmail SMTP (TLS, port 587) |
| Frontend | Vanilla CSS + JavaScript |
| Fonts | Bricolage Grotesque, Lora (Google Fonts) |

---

## Project Structure

```
Django/
├── DjangoFiles/               ← project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── blog/                      ← main blog app
│   ├── migrations/
│   ├── static/blog/
│   │   └── blog.css           ← full custom CSS design system
│   ├── templates/blog/
│   │   ├── base.html          ← shared layout, sidebar, dark mode toggle
│   │   ├── pagination.html
│   │   └── post/
│   │       ├── list.html      ← post list with tag filtering
│   │       ├── detail.html    ← post detail, comments, similar posts
│   │       ├── share.html     ← share by email form
│   │       ├── comment.html
│   │       └── includes/
│   │           └── comment_form.html
│   ├── models.py              ← Post, Comment, PublishedManager
│   ├── views.py               ← post_list, post_detail, post_comment, post_share
│   ├── urls.py
│   ├── forms.py               ← CommentForm, EmailPostForm
│   ├── admin.py               ← PostAdmin, CommentAdmin
│   └── apps.py
├── PlayGames/                 ← placeholder app
├── manage.py
├── Pipfile
├── Pipfile.lock
├── .env                       ← not committed — create locally
├── .gitignore
└── README.md
```

---

## Prerequisites

Before getting started, make sure you have the following installed on your machine:

- **Python 3.14**
- **Pipenv** — install with `pip install pipenv`

## Dependencies

All dependencies are managed via Pipenv and install automatically when you run `pipenv install`:

| Package | Version | Purpose |
|---|---|---|
| Django | latest | Web framework |
| django-taggit | 5.0.1 | Tag system for posts |
| python-decouple | 3.8 | Environment variable management via `.env` |
| certifi | latest | SSL certificate handling for Gmail SMTP |

---

## Getting Started

### Installation

```bash
# Clone the repo
git clone https://github.com/KaranSaini-Git/ink..git
cd ink.

# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell
```

### Environment Variables

Create a `.env` file in the root directory (same level as `manage.py`):

```env
SECRET_KEY=your-django-secret-key
EMAIL_HOST_USER=your-gmail@gmail.com
EMAIL_HOST_PASSWARD=your-gmail-app-password
DEFAULT_FROM_EMAIL=your-gmail@gmail.com
```

> For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) — not your regular account password.

To generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Run the project

```bash
# Apply migrations
python manage.py migrate

# Create a superuser for admin access
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/blog/` to view the blog.
Visit `http://127.0.0.1:8000/admin/` to manage posts, comments, and tags.

---

## Usage Notes

- Posts must be set to **Published** status in the admin to appear on the blog
- Comments have an `active` boolean — set to `True` in admin for them to show on a post
- Tags are created directly from the post form in the admin and are automatically removed from the sidebar if no published post uses them
- The `PlayGames` app is a leftover placeholder from early Django exploration — it's not part of the blog

---

## Design

The blog uses a fully custom CSS design system with no frameworks:

- **Light mode** — warm parchment background (`#e2ddd6`), burnt sienna/rust accent (`#b85c38`), Lora italic logo
- **Dark mode** — deep charcoal background (`#1a1714`), lighter rust accent (`#d4855e`)
- **Typography** — Bricolage Grotesque (300–600 weight) for UI, Lora italic for the `ink.` wordmark
- **Animations** — subtle fade-in on page load and staggered card entrance; hover transitions throughout
- **Dark mode toggle** — button in the header nav; preference persists via `localStorage` across pages

---

## Author

Made by **Karan Singh Saini** — learning Django one feature at a time.
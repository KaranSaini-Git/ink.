# ink. ✍️

<p align="center">
  A minimal Django blogging platform focused on thoughtful writing, clean layout, and a warm editorial aesthetic.
</p>

<p align="center">
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white"></a>
  <a href="https://www.djangoproject.com/"><img alt="Django" src="https://img.shields.io/badge/Django-Framework-092E20?logo=django&logoColor=white"></a>
  <img alt="Frontend" src="https://img.shields.io/badge/Frontend-HTML%20%2B%20CSS-E34F26?logo=html5&logoColor=white">
  <img alt="Database" src="https://img.shields.io/badge/DB-SQLite-003B57?logo=sqlite&logoColor=white">
  <img alt="Status" src="https://img.shields.io/badge/Status-Active%20Learning%20Project-8A2BE2">
</p>

---

## 📌 Overview

**ink.** is a personal Django-powered blog project built to practice backend fundamentals and ship a complete content workflow: publishing posts, reading them in a polished UI, commenting, and sharing by email.

---

## ✨ Implemented Features

### 📝 Publishing workflow
- `Post` model with **Draft** and **Published** states.
- Custom manager returns only published posts for public views.

### 🔗 Clean post URLs
- Date + slug based post URLs generated via `get_absolute_url()`.

### 📚 Post listing with pagination
- Home/blog list page paginated at **3 posts per page**.
- Graceful handling of invalid or out-of-range page requests.

### 💬 Comment system
- Visitors can submit comments (name, email, body).
- Only comments with `active=True` are shown publicly.

### 📤 Share by email
- Built-in form for sharing any published post via email.
- Implemented with Django forms + `send_mail`.

### 🛠️ Enhanced Django admin
- Dedicated admin config for `Post` and `Comment`:
  - list display
  - filtering
  - search
  - slug auto-fill
  - publish date hierarchy
  - facet counts in filters

### 🎨 Custom UI styling
- Handcrafted CSS for:
  - responsive two-column layout
  - animated post cards
  - typography-forward reading experience
  - styled list/detail/share/comments/pagination sections

---

## 🧱 Tech Stack

- **Backend:** Django
- **Language:** Python
- **Database:** SQLite (default)
- **Frontend:** HTML + CSS
- **Forms & Email:** Django Forms, Django Mail
- **Dependency Management:** Pipenv

---

## 📂 Project Structure

```text
.
├── DjangoFiles/                 # Project configuration (settings, urls, wsgi, asgi)
├── blog/                        # Main app
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

---

## 🚀 Run Locally

```bash
# 1) Install dependencies
pipenv install

# 2) Enter virtual environment
pipenv shell

# 3) Run migrations
python manage.py migrate

# 4) Start dev server
python manage.py runserver
```

Open: `http://127.0.0.1:8000/blog/`

---

## ⚙️ Optional Email Setup (for share feature)

Configure email settings in your Django settings / environment variables so `send_mail` can deliver messages.

Typical Gmail SMTP setup:
- Host: `smtp.gmail.com`
- Port: `587`
- TLS: `True`
- Valid app password required

---

## 🗺️ Roadmap Ideas

- Dynamic tag system in UI
- Related/similar posts section
- Rich text editor for post body
- Search functionality
- Deployment + CI checks

---

## 📄 License

Add a `LICENSE` file (MIT recommended) if you want open-source reuse permissions.

---

<p align="center">
  Built with Django and a lot of curiosity.
</p>

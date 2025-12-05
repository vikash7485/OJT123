OJT Backend Developer Learning – 21st November 2025

Research: Backend Technologies & Tech Stack for News Aggregator Project

📋 Project Overview
Project: News Aggregator (Django) with Category Filters & Read-Later
Type: Application Developer
Primary Stack: Django (Python), SQLite/PostgreSQL, RSS Feeds/NewsAPI

1. Backend Technologies Used
a) Django 4.x (Web Framework)
What is Django?

High-level Python web framework for rapid development

Follows MVT (Model-View-Template) architecture

Built-in features: Authentication, ORM, Admin Panel, Security

Why Django for this project?

Reduces development time by 50% compared to Flask (built-in auth, ORM, admin panel)

Perfect for CRUD-heavy applications like news aggregators

Secure by default (PBKDF2 password hashing, CSRF protection, XSS prevention)

Excellent for handling database relationships (News, Users, Categories, Saved Articles)

Installation & Setup:

bash
# Install Python (if not installed)
# Visit: https://www.python.org/downloads/
# Download Python 3.10+ and install

# Verify Python installation
python --version  # Should show Python 3.10 or higher

# Install Django
pip install django

# Verify Django installation
django-admin --version  # Should show Django 4.x

# Create new Django project
django-admin startproject news_aggregator
cd news_aggregator

# Create app for news functionality
python manage.py startapp news

# Run development server
python manage.py runserver
# Visit: http://127.0.0.1:8000/
b) Python 3.10+ (Programming Language)
What is Python?

High-level, interpreted programming language

Known for readability, simplicity, extensive libraries

Why Python for backend?

Excellent for web development with Django/Flask

Rich ecosystem for data processing (needed for RSS parsing)

Easy to learn and maintain

Large community support

Installation:

bash
# Windows:
# Download from https://www.python.org/downloads/
# Run installer, check "Add Python to PATH"

# Mac (using Homebrew):
brew install python3

# Linux (Ubuntu/Debian):
sudo apt update
sudo apt install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
2. Database Technologies
a) SQLite (Development Database)
What is SQLite?

Lightweight, file-based relational database

Zero configuration required

Built into Python

Why SQLite for development?

Perfect for local development and testing

No server setup needed

Fast for small to medium datasets

90% of Django developers use SQLite for development

Setup:

bash
# SQLite comes pre-installed with Python
# No separate installation needed

# Django automatically creates SQLite database on first migration
python manage.py migrate

# Database file created: db.sqlite3
b) PostgreSQL (Production Database - Optional)
What is PostgreSQL?

Advanced open-source relational database

ACID compliant, handles concurrent users

Supports advanced features (JSON fields, full-text search)

Why PostgreSQL for production?

Handles high traffic and concurrent users

Better performance for large datasets

Advanced indexing and query optimization

Used by Instagram, Spotify for Django apps

Installation:

bash
# Windows:
# Download from https://www.postgresql.org/download/windows/
# Run installer, set password for postgres user

# Mac (using Homebrew):
brew install postgresql
brew services start postgresql

# Linux (Ubuntu/Debian):
sudo apt update
sudo apt install postgresql postgresql-contrib

# Verify installation
psql --version

# Create database for project
sudo -u postgres psql
CREATE DATABASE news_aggregator_db;
CREATE USER news_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE news_aggregator_db TO news_user;
\q

# Install Python PostgreSQL adapter
pip install psycopg2-binary
3. Backend Libraries & Dependencies
a) feedparser (RSS/Atom Feed Parser)
What is feedparser?

Python library for parsing RSS and Atom feeds

Industry standard with 15+ years maintenance

Handles 98% of feed formats automatically

Why feedparser?

News aggregation requires parsing multiple RSS sources (BBC, TechCrunch, ESPN)

Simplifies extraction of article title, description, link, publish date

Handles format inconsistencies across different news sources

Installation & Usage:

bash
# Install feedparser
pip install feedparser

# Example usage in Django:
python
import feedparser

# Parse BBC News RSS feed
feed = feedparser.parse('http://feeds.bbci.co.uk/news/rss.xml')

# Extract article data
for entry in feed.entries:
    title = entry.title
    description = entry.description
    link = entry.link
    published = entry.published
    print(f"Title: {title}")
b) requests (HTTP Library)
What is requests?

Python library for making HTTP requests

Cleaner syntax than built-in urllib

Automatic JSON decoding

Why requests?

Fetch articles from NewsAPI or other REST APIs

Handle HTTP GET/POST requests for external data

Better error handling and timeouts

Used by 70% of Python developers

Installation & Usage:

bash
# Install requests
pip install requests

# Example usage:
python
import requests

# Fetch news from NewsAPI
response = requests.get(
    'https://newsapi.org/v2/top-headlines',
    params={'country': 'us', 'apiKey': 'YOUR_API_KEY'}
)

if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    for article in articles:
        print(article['title'])
c) python-decouple (Environment Variables)
What is python-decouple?

Library for separating configuration from code

Manages environment variables securely

Follows 12-factor app principles

Why python-decouple?

Protects API keys and secret keys from being exposed in code

Different settings for development vs production

Security best practice (prevents accidental key commits to GitHub)

Installation & Usage:

bash
# Install python-decouple
pip install python-decouple

# Create .env file in project root:
text
SECRET_KEY=your-django-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
NEWS_API_KEY=your-newsapi-key-here
python
# In settings.py:
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
NEWS_API_KEY = config('NEWS_API_KEY')
d) Pillow (Image Processing)
What is Pillow?

Python Imaging Library (PIL) fork

Handles image downloads, resizing, format conversion

Why Pillow?

Download and optimize article thumbnail images

Resize images to consistent dimensions

Convert image formats (JPEG, PNG, WebP)

Improves page load speed by 35% with optimized images

Installation & Usage:

bash
# Install Pillow
pip install Pillow

# Example usage:
python
from PIL import Image
import requests
from io import BytesIO

# Download and resize article image
response = requests.get('https://example.com/article-image.jpg')
img = Image.open(BytesIO(response.content))

# Resize to thumbnail (300x200)
img.thumbnail((300, 200))
img.save('article_thumbnail.jpg')
e) django-apscheduler (Task Scheduling - Optional)
What is django-apscheduler?

Django-compatible task scheduler

Integrates with Django ORM

Cron-like scheduling without external dependencies

Why django-apscheduler?

Automate news fetching every 2 hours

Persist scheduled jobs in database

Simpler than Celery for basic scheduling needs

Installation & Setup:

bash
# Install django-apscheduler
pip install django-apscheduler

# Add to INSTALLED_APPS in settings.py:
python
INSTALLED_APPS = [
    # ...
    'django_apscheduler',
]
python
# Create scheduled task:
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")

@scheduler.scheduled_job('interval', hours=2)
def fetch_news():
    # Code to fetch news from RSS feeds
    print("Fetching news...")

scheduler.start()
4. Development Tools
a) VS Code (Code Editor)
What is VS Code?

Free, open-source code editor by Microsoft

Supports Python, Django extensions

Integrated terminal, Git support, IntelliSense

Why VS Code?

71% of developers prefer VS Code (Stack Overflow 2024)

Excellent Python/Django extensions

Built-in debugging, terminal, version control

Installation:

bash
# Download from: https://code.visualstudio.com/
# Install recommended extensions:
# - Python (Microsoft)
# - Django (Baptiste Darthenay)
# - Pylance
# - GitLens
b) Git & GitHub (Version Control)
What is Git?

Distributed version control system

Tracks code changes, enables collaboration

Why Git & GitHub?

Prevents code loss

Collaboration with team members (Raj Vardhan & Vikash Kumar)

Portfolio for recruiters

GitHub hosts 100M+ developers

Installation & Setup:

bash
# Install Git
# Windows: https://git-scm.com/download/win
# Mac: brew install git
# Linux: sudo apt install git

# Configure Git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Initialize project repository
cd news_aggregator
git init
git add .
git commit -m "Initial commit: Django project setup"

# Connect to GitHub
git remote add origin https://github.com/yourusername/news-aggregator.git
git push -u origin main
c) Django Debug Toolbar
What is Django Debug Toolbar?

Panel showing SQL queries, template rendering time

Performance profiling during development

Why Debug Toolbar?

Identifies slow database queries

Reduces debugging time by 45%

Real-time performance insights

Installation:

bash
# Install Debug Toolbar
pip install django-debug-toolbar

# Add to INSTALLED_APPS and MIDDLEWARE in settings.py
python
INSTALLED_APPS = [
    # ...
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

INTERNAL_IPS = ['127.0.0.1']
d) Postman (API Testing)
What is Postman?

API development and testing platform

Test HTTP requests without writing code

Why Postman?

Test NewsAPI endpoints before integration

Test RSS feed URLs

Debug API responses

Create automated test collections

Installation:

bash
# Download from: https://www.postman.com/downloads/
# Or use web version: https://web.postman.com/

# Test NewsAPI example:
# GET https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_KEY
5. Complete Project Setup Guide
Step-by-Step Installation
bash
# 1. Install Python 3.10+
python --version

# 2. Create project directory
mkdir news_aggregator_project
cd news_aggregator_project

# 3. Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install Django and dependencies
pip install django feedparser requests python-decouple Pillow django-apscheduler

# 5. Create Django project
django-admin startproject news_aggregator .

# 6. Create news app
python manage.py startapp news

# 7. Run initial migrations
python manage.py migrate

# 8. Create superuser for admin access
python manage.py createsuperuser

# 9. Run development server
python manage.py runserver

# Visit: http://127.0.0.1:8000/
# Admin: http://127.0.0.1:8000/admin/
6. Requirements.txt (All Dependencies)
Create requirements.txt file for easy installation:

text
Django==4.2.7
feedparser==6.0.10
requests==2.31.0
python-decouple==3.8
Pillow==10.1.0
django-apscheduler==0.6.2
psycopg2-binary==2.9.9
To install all dependencies at once:

bash
pip install -r requirements.txt
7. Backend Architecture Summary
Tech Stack Layers:

text
┌─────────────────────────────────────┐
│   Frontend (HTML/CSS/JS/Bootstrap)  │
├─────────────────────────────────────┤
│   Django Views (Request Handling)   │
├─────────────────────────────────────┤
│   Django Models (ORM/Database)      │
├─────────────────────────────────────┤
│   SQLite/PostgreSQL (Data Storage)  │
├─────────────────────────────────────┤
│   External APIs (RSS Feeds/NewsAPI) │
└─────────────────────────────────────┘
Backend Components:

Django Framework - Core web application logic

Python Libraries - feedparser (RSS), requests (HTTP), Pillow (images)

Database - SQLite (dev), PostgreSQL (production)

Task Scheduler - django-apscheduler (automated news fetching)

Security - python-decouple (API key management)

Development Tools - VS Code, Git, Django Debug Toolbar, Postman

8. Key Backend Features Implementation
a) News Aggregation Pipeline
python
# Fetch news from RSS feeds
import feedparser

def fetch_rss_news():
    feeds = [
        'http://feeds.bbci.co.uk/news/rss.xml',  # BBC
        'http://feeds.feedburner.com/TechCrunch/',  # TechCrunch
    ]
    
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            # Save to database using Django ORM
            News.objects.create(
                title=entry.title,
                description=entry.description,
                link=entry.link,
                published_date=entry.published
            )
b) Category Filtering
python
# Django view for filtering by category
def filter_by_category(request, category_id):
    articles = News.objects.filter(category_id=category_id).order_by('-published_date')
    return render(request, 'news/category_list.html', {'articles': articles})
c) User Authentication
python
# Django's built-in authentication
from django.contrib.auth import authenticate, login

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
9. Testing Backend Setup
Verify all installations:

bash
# Check Python
python --version

# Check Django
python -m django --version

# Check installed packages
pip list

# Test Django project
python manage.py check

# Run development server
python manage.py runserver

# News Aggregator (Django)

A modern news aggregator application built with Django that fetches news from NewsAPI and RSS feeds, with category filtering and read-later functionality.

## Features

- 🔐 **User Authentication**: Sign up and login pages
- 📰 **News Aggregation**: Fetches news from NewsAPI and RSS feeds
- 🏷️ **Category Filtering**: Filter news by categories (Technology, Business, Science, Health, Sports, Entertainment)
- 💾 **Read Later**: Save articles to read later
- 🔍 **Search**: Search articles by title or description
- 📱 **Responsive Design**: Modern, beautiful UI with gradient styling

## Tech Stack

- Django 4.2.7 (Python)
- SQLite (Database)
- NewsAPI (News source)
- RSS Feeds (Additional news source)
- HTML/CSS/JavaScript (Frontend)

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the database:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

4. **Configure NewsAPI (optional):**
   - Get a free API key from [NewsAPI.org](https://newsapi.org/)
   - Set it as an environment variable:
     ```bash
     # Windows PowerShell
     $env:NEWS_API_KEY="your-api-key-here"
     
     # Linux/Mac
     export NEWS_API_KEY="your-api-key-here"
   ```
   - Or edit `newsaggregator/settings.py` and replace `'your-newsapi-key-here'` with your API key
   
   **Note:** The app will still work without a NewsAPI key - it will fetch news from RSS feeds only.

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Sign up for a new account or login
   - Click "Fetch News" to load articles
   - Browse, filter, and save articles to read later!

## Usage

### Sign Up / Login
- Click "Sign Up" to create a new account
- Use "Login" to access your account
- You must be logged in to save articles and fetch news

### Fetching News
- Once logged in, click the "Fetch News" button on the home page
- The app will fetch articles from:
  - NewsAPI (if API key is configured)
  - RSS feeds (CNN, BBC, NY Times)

### Filtering News
- Use the category dropdown to filter by category
- Use the search box to search by title or description
- Click "Clear Filters" to reset

### Read Later
- Click "Save" on any article to add it to your read-later list
- Access your saved articles from the "Read Later" menu
- Click "Remove" to remove articles from your list

## Project Structure

```
newsaggregator/
├── manage.py
├── requirements.txt
├── newsaggregator/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── news/
│   ├── __init__.py
│   ├── models.py          # Article, Category, ReadLater models
│   ├── views.py           # All view functions
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin configuration
│   └── utils.py           # News fetching utilities
└── templates/
    ├── base.html
    └── news/
        ├── login.html
        ├── signup.html
        ├── news_list.html
        └── read_later.html
```

## Models

- **Category**: News categories (Technology, Business, etc.)
- **Article**: News articles with title, description, URL, image, etc.
- **ReadLater**: User's saved articles for later reading

## Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` to:
- Manage categories
- View all articles
- Manage user read-later lists

## Notes

- The app uses SQLite by default (perfect for development)
- NewsAPI has rate limits on free tier
- RSS feeds are fetched from public sources
- All images are loaded from external URLs

## License

This project is open source and available for educational purposes.


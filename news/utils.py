import requests
import feedparser
from datetime import datetime
from django.utils import timezone
from django.conf import settings
from .models import Article, Category


def get_or_create_category(name):
    """Get or create a category by name."""
    category, created = Category.objects.get_or_create(
        name=name,
        defaults={'slug': name.lower().replace(' ', '-')}
    )
    return category


def fetch_news_from_api():
    """Fetch news from NewsAPI."""
    api_key = settings.NEWS_API_KEY
    
    if api_key == 'your-newsapi-key-here':
        # If no API key, return 0
        return 0
    
    categories = ['technology', 'business', 'science', 'health', 'sports', 'entertainment']
    count = 0
    
    for category_name in categories:
        try:
            url = f'https://newsapi.org/v2/top-headlines'
            params = {
                'category': category_name,
                'country': 'us',
                'apiKey': api_key,
                'pageSize': 20
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data.get('status') == 'ok':
                articles = data.get('articles', [])
                category = get_or_create_category(category_name.title())
                
                for article_data in articles:
                    if article_data.get('title') and article_data.get('url'):
                        published_at = article_data.get('publishedAt')
                        if published_at:
                            try:
                                published_at = datetime.fromisoformat(
                                    published_at.replace('Z', '+00:00')
                                )
                            except:
                                published_at = timezone.now()
                        else:
                            published_at = timezone.now()
                        
                        article, created = Article.objects.get_or_create(
                            url=article_data['url'],
                            defaults={
                                'title': article_data.get('title', '')[:500],
                                'description': article_data.get('description', '')[:2000],
                                'url_to_image': article_data.get('urlToImage', ''),
                                'published_at': published_at,
                                'source': article_data.get('source', {}).get('name', ''),
                                'author': article_data.get('author', ''),
                                'category': category,
                            }
                        )
                        if created:
                            count += 1
        except Exception as e:
            print(f"Error fetching {category_name} news: {e}")
            continue
    
    return count


def fetch_news_from_feeds():
    """Fetch news from RSS feeds."""
    feeds = [
        {
            'url': 'https://rss.cnn.com/rss/edition.rss',
            'category': 'General'
        },
        {
            'url': 'https://feeds.bbci.co.uk/news/technology/rss.xml',
            'category': 'Technology'
        },
        {
            'url': 'https://feeds.bbci.co.uk/news/business/rss.xml',
            'category': 'Business'
        },
        {
            'url': 'https://feeds.bbci.co.uk/news/science_and_environment/rss.xml',
            'category': 'Science'
        },
        {
            'url': 'https://rss.nytimes.com/services/xml/rss/nyt/Health.xml',
            'category': 'Health'
        },
    ]
    
    count = 0
    
    for feed_info in feeds:
        try:
            feed = feedparser.parse(feed_info['url'])
            category = get_or_create_category(feed_info['category'])
            
            for entry in feed.entries[:20]:  # Limit to 20 per feed
                if entry.get('title') and entry.get('link'):
                    published_at = timezone.now()
                    if entry.get('published_parsed'):
                        try:
                            published_at = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
                        except:
                            pass
                    
                    article, created = Article.objects.get_or_create(
                        url=entry['link'],
                        defaults={
                            'title': entry.get('title', '')[:500],
                            'description': entry.get('summary', '')[:2000] if entry.get('summary') else '',
                            'url_to_image': entry.get('media_thumbnail', [{}])[0].get('url', '') if entry.get('media_thumbnail') else '',
                            'published_at': published_at,
                            'source': feed.feed.get('title', 'RSS Feed'),
                            'author': entry.get('author', ''),
                            'category': category,
                        }
                    )
                    if created:
                        count += 1
        except Exception as e:
            print(f"Error fetching feed {feed_info['url']}: {e}")
            continue
    
    return count


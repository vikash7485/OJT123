from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Article, Category, ReadLater
from .utils import fetch_news_from_api, fetch_news_from_feeds
import json


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('news_list')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'news/signup.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('news_list')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('news_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'news/login.html')


@login_required
def news_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category', '')
    search_query = request.GET.get('search', '')
    
    articles = Article.objects.all()
    
    if selected_category:
        articles = articles.filter(category__slug=selected_category)
    
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    # Get user's read-later article IDs
    read_later_ids = set()
    if request.user.is_authenticated:
        read_later_ids = set(
            ReadLater.objects.filter(user=request.user)
            .values_list('article_id', flat=True)
        )
    
    # Pagination
    paginator = Paginator(articles, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articles': page_obj,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'read_later_ids': read_later_ids,
    }
    return render(request, 'news/news_list.html', context)


@login_required
def read_later_list(request):
    read_later_items = ReadLater.objects.filter(user=request.user).select_related('article')
    
    paginator = Paginator(read_later_items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'read_later_items': page_obj,
    }
    return render(request, 'news/read_later.html', context)


@login_required
@require_POST
def toggle_read_later(request):
    try:
        data = json.loads(request.body)
        article_id = data.get('article_id')
        
        article = get_object_or_404(Article, id=article_id)
        read_later, created = ReadLater.objects.get_or_create(
            user=request.user,
            article=article
        )
        
        if not created:
            read_later.delete()
            return JsonResponse({'status': 'removed', 'message': 'Removed from read later'})
        else:
            return JsonResponse({'status': 'added', 'message': 'Added to read later'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@login_required
def fetch_news(request):
    if request.method == 'POST':
        try:
            # Fetch from NewsAPI
            api_count = fetch_news_from_api()
            
            # Fetch from RSS feeds
            feed_count = fetch_news_from_feeds()
            
            messages.success(
                request, 
                f'Successfully fetched {api_count} articles from NewsAPI and {feed_count} articles from RSS feeds!'
            )
        except Exception as e:
            messages.error(request, f'Error fetching news: {str(e)}')
    
    return redirect('news_list')


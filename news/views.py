from django.shortcuts import render, get_object_or_404
from .models import News, Category

def news_view(request):
    news = News.objects.all().order_by('-id')
    categories = Category.objects.all()
    return render(request, 'news.html', {'news': news, 'categories': categories})

def news_detail_view(request, pk):
    item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news': item})


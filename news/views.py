from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q

from news.models import New, Category
from news.forms import AddNewsForm, NewsFilterForm


def news_list_view(request):
    form = NewsFilterForm(request.GET or None)
    news = New.objects.all()

    if form.is_valid():
        search = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')

        if search:
            news = news.filter(
                Q(title__icontains=search) | Q(content__icontains=search)
            )
        if category:
            news = news.filter(category=category)

    context = {
        'latest_news': news,
        'categories': Category.objects.all(),
        'filter_form': form
    }
    return render(request, 'index.html', context)


def news_detail_view(request, pk):
    news = get_object_or_404(New, id=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        news.category = Category.objects.get(id=request.POST.get('category'))
        news.title = request.POST.get('title')
        if request.FILES.get('image'):
            news.image = request.FILES.get('image')
        news.content = request.POST.get('content')
        news.save()

    context = {
        'news': news,
        'categories': categories,
    }
    return render(request, 'news_detail.html', context)


def add_news_view(request):
    if request.method == 'GET':
        news_form = AddNewsForm()
        categories = Category.objects.all()
        context = {
            'news_form': news_form,
            'categories': categories,
        }
        return render(request, 'add_news.html', context)

    elif request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(reverse('home'))


def delete_news_view(request, pk):
    news = get_object_or_404(New, id=pk)
    news.delete()
    return render(request, 'news_deleted.html')

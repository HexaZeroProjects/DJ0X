from django.shortcuts import render
from .models import News_post

# Create your views here.
from django.shortcuts import render

def home(request):
	news = News_post.objects.all()
	return render(request, 'news/news.html', {'news': news})

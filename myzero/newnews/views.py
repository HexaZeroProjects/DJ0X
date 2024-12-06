from django.shortcuts import render, redirect, get_object_or_404
from .models import Lows_post
from .forms import NewsForm
from django.contrib.auth.decorators import login_required

# Главная страница с новостями
def home(request):
    news = Lows_post.objects.all()
    return render(request, 'newnews/news.html', {'news': news})

# Создание новости
@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # Сохраняем форму, передавая текущего пользователя
            form.save(user=request.user)  # Передаем пользователя
            return redirect('newnews:news_home')  # Перенаправляем на страницу новостей
        else:
            # Если форма не прошла валидацию, можно вывести ошибки
            print(form.errors)  # Для отладки, можно вывести ошибки в консоль
    else:
        form = NewsForm()

    return render(request, 'newnews/add_new_post.html', {'form': form})

# Редактирование новости
def edit_news(request, news_id):
    news = get_object_or_404(Lows_post, pk=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()  # Сохраняем изменения
            return redirect('newnews:news_home')  # Вместо 'news_home' используем 'newnews:news_home'
    else:
        form = NewsForm(instance=news)

    return render(request, 'newnews/edit_post.html', {'form': form})

# Удаление новости
def delete_news(request, news_id):
    news = get_object_or_404(Lows_post, pk=news_id)
    news.delete()  # Удаляем новость
    return redirect('news_home')  # Перенаправляем на главную страницу


# Просмотр полной новости
def view_news(request, news_id):
    news = get_object_or_404(Lows_post, pk=news_id)  # Получаем новость по ID
    return render(request, 'newnews/view_post.html', {'news': news})

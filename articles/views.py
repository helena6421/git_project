# 3 лаба
from django.shortcuts import render
from .models import Article

# 4 лаба
from django.shortcuts import get_object_or_404, redirect

# 5 лаба
from django.shortcuts import redirect
from .forms import ArticleForm

# 6 лаба
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# 3 лаба
def archive(request):
    articles = Article.objects.all().order_by('-created_date')
    return render(request, 'articles/archive.html', {'articles': articles})

# 4 лаба
def get_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article.html', {'article': article})

# 5 лаба
# 6 лаба
@login_required 
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('get_article', article_id=article.id)
    else:
        form = ArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})

# 6 лаба
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('archive')

#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']
#             )
#             login(request, user)
#             return redirect('archive')
#     else:
#         form = RegisterForm()

#     return render(request, 'articles/register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, 'Регистрация прошла успешно!')

            return redirect('archive')
    else:
        form = RegisterForm()

    return render(request, 'articles/register.html', {'form': form})


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('archive')

#     if request.method == 'POST':
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('archive')
#     else:
#         form = LoginForm()

#     return render(request, 'articles/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, 'Вы успешно вошли в систему')

            return redirect('archive')
    else:
        form = LoginForm()

    return render(request, 'articles/login.html', {'form': form})


# def logout_view(request):
#     logout(request)
#     return redirect('archive')

def logout_view(request):
    logout(request)

    messages.info(request, 'Вы вышли из аккаунта')

    return redirect('archive')
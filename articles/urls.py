from django.urls import path
from . import views

# 3 лаба
# urlpatterns = [
#     path('', views.archive, name='archive'),
# ]

# 4 лаба
urlpatterns = [
    path('', views.archive, name='archive'),
    path('article/<int:article_id>/', views.get_article, name='get_article'),
    # 5 лаба
    path('article/new/', views.create_article, name='create_article'),
    # 6 лаба
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
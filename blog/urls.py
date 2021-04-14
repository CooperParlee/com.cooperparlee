from . import views
from django.urls import path

app_name = 'blog'
urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<slug:slug>/', views.PostDetail.as_view(), {'article_title': 'memes'}, name='post_detail'),
]
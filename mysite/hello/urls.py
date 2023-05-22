from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.BlogPostListCreate.as_view(), name='blog-post-list-create'),
    path('posts/<slug:slug>', views.BlogPostDetail.as_view(), name='blog-post-detail'),
]

# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.PostListView.as_view(), name='post-list'),
    path('blog/<slug:slug>/', views.post_detail, name='post-detail'),
    path('blog/<slug:slug>/share/', views.post_share, name='post-share'),
    path('blog/<slug:slug>/comment/', views.post_comment, name='post-comment'),
]

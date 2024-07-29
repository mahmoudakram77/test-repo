# blog/urls.py
from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
app_name = 'blog'


sitemaps ={
  'posts': PostSitemap,
}

urlpatterns = [
    path('blog/', views.PostListView.as_view(), name='post-list'),
    # path('blog/', views.post_list , name='post-list'),
    path('blog/<slug:slug>/', views.post_detail, name='post-detail'),
    path('blog/<slug:slug>/share/', views.post_share, name='post-share'),
    path('blog/<slug:slug>/comment/', views.post_comment, name='post-comment'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps} , name='django.contrib.sitemaps.views.sitemap')
]

from django.urls import path
from .views import MainPageView, PostDetailView, About

app_name = "blog_app"
urlpatterns = [
    path('', MainPageView.as_view(), name='index'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', About.as_view(), name='about'),
    
]

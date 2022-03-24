from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile, name='profile'),
    path('publications', views.publications, name='publications'),
    path('books', views.books, name='books'),
]
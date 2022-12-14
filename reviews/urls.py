from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name="update"),
    path('<int:pk>/delete', views.delete, name="delete"),
    path('<int:pk>/detail/create', views.comments_create, name='comments_create'),
    path('<int:review_pk>/detail/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path('search/',views.search, name="search"),
    path('searchfail/',views.searchfail, name="searchfail"),
]
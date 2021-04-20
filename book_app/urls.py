from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path("books/create", views.book_create),
    path("authors/view", views.author_views),
    path("authors/create", views.author_create),
    path("books/<int:book_id>/view", views.book_view),
    path("authors/<int:author_id>/view", views.another_authors_view)
]
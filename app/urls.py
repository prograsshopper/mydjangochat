from django.urls import path

from app import views

urlpatterns = [
    path("echo/", views.echo_page),
    path("liveblog", views.liveblog_index),
    path("liveblog/post/<int:post_id>", views.post_partial, name="post-partial"),
]
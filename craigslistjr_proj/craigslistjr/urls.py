from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "index"),
    path('categories/', views.index),
    path('categories/new', views.cat_new, name="cat_new"),
    path('categories/<int:category_id>', views.cat_edit),
    path('categories/<int:category_id>/view', views.cat_view, name="cat_view"),
    path('categories/<int:category_id>/edit', views.cat_edit, name="cat_edit"),
    path('posts',views.post_new),
    path('categories/<int:category_id>/posts/new', views.post_new, name ="post_new"),
    path('posts/<int:post_id>',views.post_edit),
    path('categories/<int:category_id>/posts/<int:post_id>/view', views.post_view, name = "post_view"),
    path('categories/<int:category_id>/posts/<int:post_id>/edit', views.post_edit, name = "post_edit"),
    ]
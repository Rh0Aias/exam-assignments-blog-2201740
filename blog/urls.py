from django.urls import path

from . import views
app_name = "blog"

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create.as_view(), name='create'),
    # path('delete/', views.delete.as_view(), name='delete'),
]

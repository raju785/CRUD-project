

from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostList.as_view()),
    path('delete/<int:pk>/', views.PostRetrieveDestroy.as_view()),
]

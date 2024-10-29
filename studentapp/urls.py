from django.urls import path, include
from . import views

urlpatterns = [
    path('StudentHomePage/', views.StudentHomePage, name='StudentHomePage'),
    path('view_marks/', views.view_marks, name='view_marks'),

]
from django.urls import path
from . import views

app_name= 'moodapp'
urlpatterns = [
    path('', views.home, name= 'home'),
    path('quiz/', views.quiz ,name= 'quiz'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history')
]

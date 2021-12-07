from django.urls import path

from . import views

urlpatterns = [
    path('spaghetti_al_pomodoro/', views.spaghetti_al_pomodoro, name='spaghetti_al_pomodoro'),
    path('pancakes/', views.pancakes, name='pancakes'),
    path('porkchop/', views.pork_chop, name='porkchop'),
]

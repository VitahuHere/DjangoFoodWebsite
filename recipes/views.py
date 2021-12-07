from django.shortcuts import render


def spaghetti_al_pomodoro(request):
    return render(request, 'recipes/spaghetti al pomodoro.html')


def pancakes(request):
    return render(request, 'recipes/pancakes.html')


def pork_chop(request):
    return render(request, 'recipes/porkchop.html')

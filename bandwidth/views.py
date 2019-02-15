from django.http import HttpResponse


def index(request):
    return HttpResponse("Скоро тут будет прикольный сервис!")

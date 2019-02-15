from django.http import HttpResponse


def index(request):
    return HttpResponse("Скоро тут будет прикольный сервис!")


# def get_serializer_class(self):
#     if self.request.method == 'GET':
#         return StepResultSerializer
#     else:
#         return StepInputSerializer

from django.http import HttpResponse


def search(request):
    return HttpResponse("<h1>This is the Home app homepage</h1>")

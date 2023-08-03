from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets
from django_app import serializers as django_app_serializers
from django_app import models, tasks
from django_api import utils as django_utils


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>This is a Index Page</h1>")


def index_json(request: HttpRequest) -> JsonResponse:
    return JsonResponse(data={"response": "This is a Index Page"}, safe=False)


class HomeView(TemplateView):
    template_name = "index.html"


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  # User.objects.filter(is_active=True)
    serializer_class = django_app_serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = django_app_serializers.GroupSerializer


def start(request):
    # from celery.result import AsyncResult
    # from django_settings.celery import app as celery_app
    task_id = tasks.send_mass_mail.apply_async()
    return HttpResponse(f"<h1>Task_id: {task_id}</h1>")


@django_utils.logging_decorator
def rooms(request):
    return render(request, "django_app/home.html", context={"rooms": models.Room.objects.all()})


@django_utils.logging_decorator
@login_required
def room(request, slug):
    room_obj = models.Room.objects.get(slug=slug)
    last_5_mes = models.Message.objects.filter(room=room_obj).order_by('-id')[:5]
    last_5_mes = sorted(last_5_mes, key=lambda x:x.id, reverse=False)
    return render(
        request,
        "django_app/room.html",
        context={
            "room": room_obj,
            "messages": last_5_mes,
        },
    )

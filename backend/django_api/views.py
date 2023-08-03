import re
from django.core.cache import caches
from django.db import transaction
from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema, no_body
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from django_api import serializers as django_serializers, models as django_models, utils as django_utils


LocMemCache = caches["ram_cache"]

@django_utils.logging_decorator
@api_view(http_method_names=["POST"])
@permission_classes([AllowAny])
def user_register_f(request: Request) -> Response:
    """
    Создание нового пользователя
    """
    # {"username": "admin@gmail.com", "password": "qwerty12345", "first_name": "Adam", "last_name": "Eva", "mobile": "+7777777"}
    # {"username": "admin@gmail.com", "password": "Qwerty!12345", "first_name": "Adam", "last_name": "Eva", "mobile": "+7777777"}
    username = request.data["username"]
    password = request.data["password"]
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    mobile = request.data["mobile"]

    if re.search(r"^[a-z0-9]+[._]?[a-z0-9]+@\w+[.]\w{2,3}$", username) and re.search(
        r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).*$", password
    ):
        transaction.set_autocommit(False)
        transaction_id = transaction.savepoint()  # точка сохранения 1
        try:
            user_obj = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            user_obj.save()
            user_obj.profile.mobile = mobile
            user_obj.profile.save()
        except Exception as error:
            transaction.savepoint_rollback(transaction_id)
        else:
            transaction.savepoint_commit(transaction_id)

        return Response(data="Created", status=status.HTTP_201_CREATED)
    return Response(data="Incorrect username or password", status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method="POST", request_body=django_serializers.PostCreateSerializer, responses={201: "Created"})
@api_view(http_method_names=["POST"])
def post_create_f(request: Request) -> Response:
    """
    Создание нового поста
    """
    django_models.Post.objects.create(
        user=request.user,
        title=request.data["title"],
        description=request.data["description"],
    )
    return Response(data="Created", status=status.HTTP_201_CREATED)


@swagger_auto_schema(method="GET", request_body=no_body, responses={200: django_serializers.PostSerializer})
@api_view(http_method_names=["GET"])
def post_read_f(request: Request, pk: int) -> Response:
    """
    Чтение одного поста по id
    """
    post_obj = django_models.Post.objects.get(id=pk)
    post_json = django_serializers.PostSerializer(instance=post_obj, many=False).data
    return Response(data=post_json, status=status.HTTP_200_OK)


@swagger_auto_schema(method="GET", request_body=no_body, responses={200: django_serializers.PostListSerializer})
@api_view(http_method_names=["GET"])
def post_list_f(request: Request) -> Response:
    """
    Чтение всех постов
    """

    post_json = LocMemCache.get(f"{request.path} {request.method}")
    if post_json is None:
        post_obj = django_models.Post.objects.all()
        post_json = django_serializers.PostSerializer(instance=post_obj, many=True).data
        LocMemCache.set(f"{request.path} {request.method}", post_json, timeout=1)

    return Response(data=post_json, status=status.HTTP_200_OK)


@swagger_auto_schema(methods=["PUT", "PATCH"], request_body=django_serializers.PostUpdateSerializer, responses={200: "Updated"})
@api_view(http_method_names=["PUT", "PATCH"])
def post_update_f(request: Request, pk: int) -> Response:
    """
    Обновление поста
    """
    post_obj = django_models.Post.objects.get(id=pk)
    post_obj.title = request.data["title"]
    post_obj.description = request.data["description"]
    post_obj.is_completed = request.data["is_completed"]
    post_obj.save()
    return Response(data="Updated", status=status.HTTP_200_OK)


@swagger_auto_schema(methods=["DELETE"], request_body=no_body, responses={200: "Deleted"})
@api_view(http_method_names=["DELETE"])
def post_delete_f(request: Request, pk: int) -> Response:
    """
    Удаление поста
    """
    django_models.Post.objects.get(id=pk).delete()
    return Response(data="Deleted", status=status.HTTP_200_OK)

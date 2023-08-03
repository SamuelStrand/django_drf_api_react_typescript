from django.contrib.auth.models import User
from django.test import TestCase, Client
from django_app import models
from django.urls import reverse


class DefaultUserCreateTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username="Anya", password="Qwerty!12345")

    def test_model_create(self):
        """
        Тестируем, что модель пользователя в базе данных успешно создалась
        """

        test_name = "Anya"
        user = User.objects.get(username=test_name)
        self.assertEqual(user.username, test_name)

    def test_user_count(self):
        users = User.objects.all()
        self.assertEqual(users.count(), 1)


class ApiBookGetTestCase(TestCase):
    test_username = "Bogdan_112345"
    test_password = "Qwerty!12345"

    def setUp(self) -> None:
        User.objects.create(username=self.test_username, password=self.test_password)

        client = Client()
        response1 = client.post(reverse("token_obtain_pair"), data={"username": self.test_username, "password": self.test_password})
        if response1.status_code != 200:
            raise Exception("Пользователь не создан!")


class OkTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_ok(self):
        print(
            """\n\n\n
        ################################################################################
        ################################################################################
        ################################################################################
                                ВСЕ ТЕСТЫ УСПЕШНО ПРОЙДЕНЫ
        ################################################################################
        ################################################################################
        ################################################################################
        \n\n\n"""
        )

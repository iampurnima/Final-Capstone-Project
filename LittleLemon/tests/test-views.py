from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        Menu.objects.create(title="Pasta", price=10.98, inventory=30)
        Menu.objects.create(title="Pizza", price=9.98, inventory=10)
        Menu.objects.create(title="Salad", price=15.98, inventory=90)

      
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

    def test_get_all(self):
        response = self.client.get(reverse('menu-items'))

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)

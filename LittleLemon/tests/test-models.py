from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_menu(self):
        item = Menu.objects.create(title="Coffee", price=15, inventory=6)
        self.assertEqual(item,"Coffee : 15")

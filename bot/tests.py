from django.test import TestCase
from .models import Order
from django.core.exceptions import ValidationError


class UnitTestCase(TestCase):
    user_id = "U03HH4HRR5J"
    team_id = "T029W6KLKT9"
    item = "Big Mac"
    price = 30.89
    restaurant = "Mc Donald's"

    def test_order_save(self):
        test_order = Order(user_id=self.user_id, team_id=self.team_id, item=self.item, price=self.price,
                           restaurant=self.restaurant)
        self.assertEqual(test_order.user_id, self.user_id)
        self.assertEqual(test_order.team_id, self.team_id)
        self.assertEqual(test_order.item, self.item)
        self.assertEqual(test_order.price, self.price)
        self.assertEqual(test_order.restaurant, self.restaurant)

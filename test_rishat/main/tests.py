from django.test import Client, TestCase
from django.urls import reverse

from .models import Item, User


class ViewTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = User.objects.create_user(username='Testuser')
        cls.guest_client = Client()
        cls.item = Item.objects.create(
            name='Test name',
            description='Test test',
            price=1000
        )

    def test_view_item(self):

        response = ViewTest.guest_client.get(
            reverse('main:item', kwargs={'id': ViewTest.item.id})
        )

        self.assertTemplateUsed(response, 'main/item_profile.html')

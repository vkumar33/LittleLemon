from django.test import TestCase
from restaurant.models import Menu
from django.db.models import QuerySet


class MenuViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.instance = Menu.objects.create(id = 1, title="IceCream", price=80, inventory=100)
        cls.instance.save()


    def test_getall(self):
        # Create a model instance
        #instance = Menu()

        # Save the model instance
        #instance.save()

        # Get all model instances
        all_instances = Menu.objects.all()

        # Assert that the model instance is in the list of all model instances
        #self.assertIn(str(self.instance), all_instances)
        self.assertQuerysetEqual(QuerySet(self.instance), all_instances)
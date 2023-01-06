from django.test import TestCase

# Create your tests here.
from .models import HelloWorld

class HelloTestCase(TestCase):
    def setUp(self):
        HelloWorld.objects.create(
            name = "Hello World Object"
        )
    def test_product_generates_affiliate_link(self):
        hello_world = HelloWorld.objects.get(name="Hello World Object")
        field_name = hello_world._meta.get_field('name')
        test_field = field_name.value_from_object(hello_world)
        self.assertEqual("Hello World Object", test_field)
from django.db import models

class HelloWorld(models.Model):
    name = models.TextField(blank=True)
    hello_test_field = models.TextField(blank=True)
    def __str__(self):
        return self.name
from rest_framework import serializers
from .models import HelloWorld

class HelloWorldSerializer(serializers.ModelSerializer):
    hello_test_field = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = HelloWorld
        fields = ['id', 'name', 'hello_test_field']
    def get_hello_test_field(self, obj):
        return 'Test your code'
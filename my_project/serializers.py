from rest_framework import serializers

from my_project.models import Employee, Client


class EmployeeSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    total_clients = serializers.CharField()
    total_products = serializers.CharField()
    total_price = serializers.CharField()

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'total_clients', 'total_products', 'total_price')

    def full_name(self, obj):
        return f"{obj.full_name})"


class EmployeeDetailSerializers(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['full_name']

    def full_name(self, obj):
        return f"{obj.full_name})"


class ClientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ('id', 'full_name')

    def full_name(self, obj):
        return f"{obj.full_name}"

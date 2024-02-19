from django.db.models import Count, Sum, F
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from my_project.models import Employee, Order, Client
from my_project.serializers import EmployeeDetailSerializers, EmployeeSerializers, ClientSerializer


class EmployeeDetailView(APIView):

    def get(self, request, *args, **kwargs):
        employee = get_object_or_404(Employee, pk=kwargs['id'])
        month = int(request.GET.get('month', 0))
        year = int(request.GET.get('year', 0))
        orders = Order.objects.filter(date__month=month, date__year=year, employee=employee)

        if not orders:
            return Response({'message': 'Not found'}, status=status.HTTP_200_OK)

        total_clients = orders.count()
        total_products = sum(order.products.count() for order in orders)
        total_sales = sum(order.price for order in orders)

        serializer = EmployeeDetailSerializers(employee)

        data = serializer.data
        data['total_clients:'] = total_clients
        data['total_products:'] = total_products
        data['total_sales:'] = total_sales
        return Response(data, status=status.HTTP_200_OK)


class ClientDetailView(APIView):
    def get(self, request, *args, **kwargs):
        month = int(request.GET.get('month'))
        year = int(request.GET.get('year'))
        client = get_object_or_404(Client, pk=kwargs.get('id'))
        print(f"Client: {client}")

        orders = Order.objects.filter(date__month=month, date__year=year, client=client)

        if not orders:
            return Response({'message': 'Not Found'}, status=status.HTTP_200_OK)

        serializer = ClientSerializer(client)
        data = serializer.data
        data['total_products'] = sum(order.products.count() for order in orders)
        data['total_sales'] = sum(order.price for order in orders)

        return Response(data, status=status.HTTP_200_OK)


class EmployeeStatistics(APIView):
    def get(self, request, *args, **kwargs):
        month = int(request.GET.get("month"))
        year = int(request.GET.get("year"))
        orders = Order.objects.filter(date__month=month, date__year=year)
        if not orders:
            return Response({'Message': 'Not Found'}, status=status.HTTP_200_OK)

        employees = Employee.objects.filter(order__in=orders).annotate(
            total_price=Sum('order__price'),
            total_clients=Count('order__client'),
            total_products=Count('order__products'))

        serializer = EmployeeSerializers(employees, many=True)
        data = serializer.data
        return Response({'Employees Info: ': serializer.data}, status=status.HTTP_200_OK)

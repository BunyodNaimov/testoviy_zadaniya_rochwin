from django.urls import path

from my_project.views import EmployeeDetailView, EmployeeStatistics, ClientDetailView

app_name = 'my_project'
urlpatterns = [
    path('statistics/employee/<int:id>/', EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/statistics/', EmployeeStatistics.as_view(), name='employee_statistics'),
    path('statistics/client/<int:id>/', ClientDetailView.as_view(), name='client-detail')

]

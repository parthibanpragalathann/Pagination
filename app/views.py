
# Created app views here.
from rest_framework import viewsets
from .models import employes, company, projects
from .serializer import EmployesSerializer, CompanySerializer, ProjectsSerializer
from .pagination import CustomPageNumberPageination, CursorPaginationWithOrdering
# Create Employes views here.
class Employes_View(viewsets.ModelViewSet):
    queryset = employes.objects.order_by("name")
    serializer_class = EmployesSerializer
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering
# Create Company views here.
class Company_View(viewsets.ModelViewSet):
    queryset = company.objects.order_by("name")
    serializer_class = CompanySerializer
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering
# Create projects views here.
class Projects_View(viewsets.ModelViewSet):
    queryset = projects.objects.order_by("name")
    serializer_class = ProjectsSerializer
    #pagination_class = CustomPageNumberPageination
    #pagination_class = CursorPaginationWithOrdering
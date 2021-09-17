from rest_framework import serializers
from .models import company, employes, projects

class EmployesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employes
        fields = ("id", "url", "name")

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = company
        fields = ("id", "url", "name", "emp_name", "created_at")

class ProjectsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = projects
        fields = ("id", "url", "name", "emp_name", "comp_name")


from django.db import models

# Create app models here.

class employes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class company(models.Model):
    name = models.CharField(max_length=50)
    emp_name = models.ForeignKey(employes, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class projects(models.Model):
    name = models.CharField(max_length=100)
    emp_name = models.ForeignKey(employes, on_delete=models.CASCADE)
    comp_name = models.ForeignKey(company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

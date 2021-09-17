from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("employee", views.Employes_View)
router.register("company", views.Company_View)
router.register("project", views.Projects_View)


urlpatterns = [
    path("", include(router.urls))
]
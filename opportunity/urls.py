from django.conf.urls import url
from . import views

app_name = 'opportunity'
urlpatterns = [
    url('^add/', views.add, name="add"),
]

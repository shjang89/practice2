from django.urls import path
from double import views


urlpatterns = [
    path('double/<int:number>', views.double_number),
]

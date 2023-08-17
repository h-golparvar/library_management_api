from django.urls import path
from . import views

app_name= 'accounts'
urlpatterns= [
    path('identify/', views.IdentifyView.as_view()),
    path('tokenrevoke/', views.TokenRevoke.as_view()),
]


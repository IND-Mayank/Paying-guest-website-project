from django.urls import path
from . import views
urlpatterns=[
    path('test',views.test),
    path('pg',views.pg),
    path('page',views.page),
    path('res',views.res),
    path('PGres',views.PGres),
    path('yourpg',views.yourpg),
]
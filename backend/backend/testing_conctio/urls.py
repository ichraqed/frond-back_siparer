from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('tes<int:id>/',views.test) 
]
# import sympy 
# from sympy import symbols
# from sympy.solvers import solve
# x = symbols('x y')
# print(type(x))
# print(x)
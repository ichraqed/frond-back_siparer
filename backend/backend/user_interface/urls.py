from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('signup/',views.signup,name='signup') ,
    path('s/',views.search_view)  ,
    path('u<int:user_id>/',views.update_user)   ,
    path('D<int:id>/',views.delete) ,
    path('display/',views.display),
]
# import sympy 
# from sympy import symbols
# from sympy.solvers import solve
# x = symbols('x y')
# print(type(x))
# print(x)
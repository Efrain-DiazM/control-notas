from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('logout/', views.signout, name="logout"),
    path('', views.signin, name="signin"),
    # path('createCourse', views.createCourse, name="createCourse"),

    path('crearCursos/', views.crearCursos, name="crearCursos"),
    path('profile/', views.profile, name="profile"),
]
from django.urls import path, include
from main import views as v_main
from register import views as v_register
from exam import views as v_exam
from learn import views as v_learn
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v_main.home, name="home"),
    path('home/', v_main.home, name="home"),
    path('register/', v_register.register, name="register"),
    path('exam/', v_exam.exam, name="exam"),
    path('learn/', v_learn.learn, name="learn"),
    path('learn/learn_v/', v_learn.learn_v, name="learn_v"),
    path('', include("django.contrib.auth.urls")),
]

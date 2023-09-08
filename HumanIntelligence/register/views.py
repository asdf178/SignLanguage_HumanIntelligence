from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(response):
    if response.method == "POST": # 회원가입 눌렀을 때
        form = UserCreationForm(response.POST)
        if form.is_valid(): # 입력한 정보가 타당하다면
            form.save() # 회원가입 성공

        return redirect("/home") # home으로 이동
    else:
        form = UserCreationForm()
        if response.GET.get("register"): # 네비게이션 바에서 회원가입 클릭
            return redirect("/register") # 회원가입 창으로 이동
        elif response.GET.get("login"): # 네비게이션 바에서 로그인 클릭
            return redirect("/login") # 로그인 창으로 이동

    return render(response, "register/register.html", {"form":form})

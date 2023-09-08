from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(response):
    if response.method == "POST":
        if response.POST.get("login"): # 네비게이션 바의 로그인 클릭
            return redirect("/login") # 로그인 페이지로 이동
        elif response.POST.get("register"): # 네비게이션 바의 회원가입 클릭
            return redirect("/register") # 회원가입 페이지로 이동

    return render(response, "main/home.html", {}) # home html 렌더링함
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

from django.utils import timezone


# Create your views here.
def index(request):
    # print(request.user)
    # print(request.user.is_authenticated)
    # print(request.user.is_superuser)
    # print(request.user.is_staff)

    print(request.session)
    print("session 확인")

    print("visit_profile", request.session.get("visit_profile"))

    for k, v in request.session.items():
        print(k, v)
        print("-" * 10)
    request.session["visit_profile"] = timezone.now().timestamp()

    print(request.COOKIES)

    response = render(
        request,
        "user/index.html",
    )
    response.set_cookie("cookie-test", "cookie-test-value")
    return response


from django.urls import reverse


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.data.get("username")
            password = form.data.get("password1")

            # 검증하는 함수. user가 존재하면 user리턴, 없으면 None return
            user = authenticate(username=username, password=password)

            # 로그인 진행 = 세션에 등록
            login(request, user)

            # return redirect("/user")
            # 위와 아래는 같습니다.
            return redirect(reverse("user:profile"))

    return render(request, "user/register.html", {"form": form})

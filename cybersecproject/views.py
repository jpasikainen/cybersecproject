from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import Accounts, Posts

def home_view(request):
    return render(request, "pages/index.html", {"posts": Posts.objects.all()})

def login_view(request):
    if request.session.get("username") != None:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Flaw 2
        # Sql injection when username is correct and password is ' OR '1=1
        with connection.cursor() as cursor:
            query = """SELECT COUNT(*) FROM cybersecproject_accounts WHERE username='%s' AND password='%s'""" % (username, password,)
            cursor.execute(query)
            if cursor.fetchone()[0] > 0:
                request.session["username"] = username
                return redirect("/")
            return HttpResponse("Wrong password or username")
    
    return render(request, "pages/login.html", {})

def register_view(request):
    if request.method == "POST" and request.session.get("username") == None:
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if Accounts.objects.filter(username=username).exists():
            return HttpResponse("Username taken")

        user = Accounts(username=username, password=password, admin=False)
        user.save()

        return redirect("/")

    return render(request, "pages/register.html", {})

def logout_view(request):
    request.session.clear()
    return redirect("/")

def submit_post_view(request):
    if request.method == "POST" and request.session.get("username"):
        body = request.POST.get("body")[:299]
        tags = request.POST.get("tags")[:299]

        post = Posts(author=request.session["username"], body=body)
        post.save()

    return redirect("/")

def profile_view(request):
    if request.session.get("username"):
        # Flaw 3
        account = Accounts.objects.get(username=request.session.get("username").strip())
        return render(request, "pages/profile.html", {"username": account.username, "password": account.password})
    return redirect("/")
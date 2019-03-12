from django.shortcuts import redirect, render


# Create your views here.
def homepage_view(request):
    return redirect("/accounts/login/")

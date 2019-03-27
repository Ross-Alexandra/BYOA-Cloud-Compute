from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic

from .forms import JobCreateForm
from .models import Job


@login_required
def homepage_view(request):
    """Homepage to Login Redirect

    Returns to the user the homepage template if they are logged in, otherwise redirects them
    to the login page.
    """
    return render(request, "tmp_home.html")


@login_required
def job_create_view(request):
    """Job Create Page

    Returns to the user the job create page. The user must be logged in.
    """
    if request.method == "POST":
        form = JobCreateForm(request.POST)
        job = form.save(commit=False)
        job.user = request.user
        job.save()
        return HttpResponseRedirect(reverse("home"))
    else:
        form = JobCreateForm()

    context = {"form": form}

    return render(request, "job_create.html", context)


@login_required
def jobs_view(request):
    """Jobs Page

    Returns to the user all of their jobs and their status.
    """
    jobs_list = Job.objects.filter(user=request.user)
    context = {"jobs_list": jobs_list}
    return render(request, "jobs.html", context)


class SignUp(generic.CreateView):
    """Sign-up Page

    Returns to the user the sign-up template.
    """

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

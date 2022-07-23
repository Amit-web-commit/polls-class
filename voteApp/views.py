from multiprocessing import context
from re import template
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View, generic
from voteApp.forms import CandidateForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib import messages
# Create your views here.
class candidate_create_view(CreateView):
    model= Candidate
    form_class= CandidateForm
    template_name= "voteapp/index.html"
    # queryset= Candidate.objects.all()
    success_url= reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context =  super().get_context_data()
        context['candidate'] = Candidate.objects.all
        return context


class signupview(generic.CreateView):
    form_class = SignUpForm
    template_name= "voteapp/signup.html"
    success_url= reverse_lazy('login')


class loginview(generic.View):
    template_name = "voteapp/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.warning(request, "Username or Password is incorrect")
                return redirect("login")
        else:      
            return render(request, 'voteapp/login.html', {})


# class login_user(View):
#     def post(self, request):

class candidate_update_view(UpdateView): 
    model= Candidate
    form_class= CandidateForm
    template_name= "voteapp/update.html"
    # queryset= Candidate.objects.all()
    success_url= reverse_lazy('home')

class candidate_delete_view(DeleteView):
    model=Candidate
    # form_class= CandidateForm
    template_name='voteapp/delete.html'
    success_url=reverse_lazy("home")
    
    # model= Candidate
    # form_class= CandidateForm
    # template_name= "voteapp/delete.html"
    # queryset= Candidate.objects.all()
    # success_url= reverse_lazy('home')



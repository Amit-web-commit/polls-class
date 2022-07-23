
from django.urls import path
from django.views.generic import CreateView, UpdateView, DeleteView
from . import views
urlpatterns = [
    path('', views.candidate_create_view.as_view(), name='home'),
    path('candidate/<int:pk>/', views.candidate_update_view.as_view(), name="updateCandidate"),
    path('candidate/delete/<int:pk>/', views.candidate_delete_view.as_view(), name="deleteCandidate"),
    path('register/', views.signupview.as_view(), name='signup' ),
    path('login/', views.loginview.as_view(), name='login' ),

]
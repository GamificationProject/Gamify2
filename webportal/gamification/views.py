from django.shortcuts import render, redirect
from django.views import generic
from .models import Game
from .forms import UserForm, SignInForm
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class IndexView(generic.ListView):
    template_name = 'gamification/index.html'
    context_object_name = 'game_list'
    
    def get_queryset(self):
        return Game.objects.all()
    
class RegisterView(View):
    form_class = UserForm
    template_name = 'gamification/registration_form.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save(commit = False)
            username = form.data['username']
            first_name = form.data['first_name']
            last_name = form.data['last_name']
            password = form.data['password']
            user.set_password(password)
            user.save()
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('gamification:index')
        
        return render(request, self.template_name, {'form': form})
    
class SignInView(View):
    form_class = SignInForm
    template_name = 'gamification/login_form.html'
    
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            username = form.data['username']
            password = form.data['password']
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return redirect('gamification:index')
        
        return render(request, self.template_name, {'form': form})    

class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('gamification:index')
    
class TrialView(View):
    def get(self, request):
        return render(request, 'gamification/signup-trial.html', {})